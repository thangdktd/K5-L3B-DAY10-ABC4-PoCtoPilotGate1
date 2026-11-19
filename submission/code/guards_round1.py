"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _current_policy(ctx):
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _valid_approval(ctx, approval_id, order_id, amount_vnd):
    if not approval_id:
        return False
    cands = ctx.tools.lookup_approvals(approval_id=approval_id)
    for app in cands:
        if app.get("status") != "valid":
            continue
        exp = app.get("expires_at")
        if exp and exp < ctx.as_of:
            continue
        if app.get("order_id") and app.get("order_id") != order_id:
            continue
        if app.get("max_vnd") is not None and amount_vnd > app["max_vnd"]:
            continue
        return True
    return False


def _gate_issue_refund(ctx, action):
    if action.get("basis") == "fail_open":
        ctx.log("guard_block_fail_open", tool="issue_refund")
        return Verdict.escalate("LLM fail_open, chuyển người duyệt")

    ticket_id = action.get("ticket_id")
    order_id = action.get("order_id")
    if ticket_id and ctx.tools.ledger_rows(ticket_id=ticket_id):
        ctx.log("guard_block_duplicate_ticket", ticket_id=ticket_id)
        return Verdict.deny("ticket đã được hoàn tiền trước đó")

    order = ctx.tools.lookup_order(order_id) if order_id else None
    if order and (order.get("refund_status") == "REFUNDED" or ctx.tools.ledger_rows(order_id=order_id)):
        ctx.log("guard_block_duplicate_order", order_id=order_id)
        return Verdict.deny("đơn hàng đã được hoàn tiền trước đó")

    pol = _current_policy(ctx)
    if not order or not pol:
        return Verdict.escalate("thiếu dữ liệu đơn hàng hoặc chính sách hiệu lực")

    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay_days = H.db_delay_days(parcel, ctx.as_of)
    entitled = H.entitlement_vnd(pol, order, delay_days, parcel.get("delay_cause"))

    if entitled <= 0:
        ctx.log("guard_deny_ineligible", db_delay_days=delay_days, cause=parcel.get("delay_cause"))
        return Verdict.deny("theo tracking DB không đủ điều kiện hoàn tiền")

    req_amount = action.get("amount_vnd", 0)
    req_payer = action.get("payer", "LOGIX")
    changes = {}
    if req_amount > entitled:
        changes["amount_vnd"] = entitled
    if req_payer != "LOGIX":
        changes["payer"] = "LOGIX"

    final_amount = changes.get("amount_vnd", req_amount)
    approval_id = action.get("approval_id")
    auto_limit = pol.get("auto_limit_vnd")
    if auto_limit is not None and final_amount > auto_limit:
        if not _valid_approval(ctx, approval_id, order_id, final_amount):
            ctx.log("guard_escalate_invalid_approval", amount_vnd=final_amount, approval_id=approval_id)
            return Verdict.escalate("vượt hạn mức tự động và thiếu phê duyệt hợp lệ")

    if not approval_id:
        limits = ctx.tools.ops_limits() or {}
        cust_cap = limits.get("max_auto_refund_per_customer_per_day_vnd")
        cid = action.get("customer_id") or order.get("customer_id")
        if cust_cap is not None and cid:
            cust_spent = sum(
                r.get("amount_vnd", 0)
                for r in ctx.tools.ledger_rows(customer_id=cid)
                if not r.get("approval_id")
            )
            if cust_spent + final_amount > cust_cap:
                ctx.log("guard_escalate_customer_cap", customer_id=cid, spent=cust_spent)
                return Verdict.escalate("vượt trần hoàn tự động theo khách trong ngày")

        daily_cap = (ctx.gates or {}).get("business", {}).get("daily_refund_cap_vnd")
        if daily_cap is not None:
            spent = ctx.tools.auto_refund_today_vnd()
            if spent + final_amount > daily_cap:
                ctx.log("guard_escalate_daily_cap", spent=spent, cap=daily_cap)
                return Verdict.escalate("vượt trần hoàn tự động cả ngày")

    if changes:
        ctx.log("guard_modify_refund", **changes)
        return Verdict.modify("điều chỉnh hoàn tiền theo nguồn sự thật DB", **changes)
    return Verdict.allow()


def _gate_file_carrier_fault(ctx, action):
    order_id = action.get("order_id")
    order = ctx.tools.lookup_order(order_id) if order_id else None
    pol = _current_policy(ctx)
    if not order or not pol:
        return Verdict.deny("thiếu dữ liệu đơn hàng hoặc chính sách khi ghi lỗi hãng")

    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay_days = H.db_delay_days(parcel, ctx.as_of)
    require_cause = (ctx.gates or {}).get("legal", {}).get("carrier_fault_requires_recorded_cause", False)
    if (require_cause and not parcel.get("delay_cause")) or not H.carrier_at_fault(pol, parcel, delay_days):
        ctx.log("guard_deny_carrier_fault", db_delay_days=delay_days, cause=parcel.get("delay_cause"))
        return Verdict.deny("không đủ căn cứ ghi lỗi hãng theo tracking DB")

    limits = ctx.tools.ops_limits() or {}
    max_strikes = limits.get("max_auto_strikes_per_carrier_per_day")
    carrier_id = action.get("carrier_id") or parcel.get("carrier_id")
    if max_strikes is not None and carrier_id:
        strikes = len(ctx.tools.fault_rows(carrier_id=carrier_id))
        if strikes >= max_strikes:
            ctx.log("guard_escalate_carrier_strikes", carrier_id=carrier_id, strikes=strikes)
            return Verdict.escalate("vượt ngưỡng ghi lỗi hãng tự động trong ngày")
    return Verdict.allow()


def _gate_notify_carrier(ctx, action):
    payload = dict(action.get("payload") or {})
    blocked = set((ctx.gates or {}).get("legal", {}).get("pii_fields_blocked_to_third_party") or [])
    blocked.update({"recipient_contact", "phone", "name", "street", "customer_note"})

    pol = _current_policy(ctx)
    allowed_fields = set(pol.get("carrier_notice_fields", [])) if pol else set()

    cleaned = {}
    removed = []
    for k, v in payload.items():
        if k in blocked or (allowed_fields and k not in allowed_fields):
            removed.append(k)
            continue
        if isinstance(v, str) and len(H.digits(v)) >= 9:
            removed.append(k)
            continue
        cleaned[k] = v

    if removed:
        ctx.log("guard_strip_pii", removed=removed)
        return Verdict.modify("loại bỏ trường PII/ngoài danh mục trước khi gửi hãng", payload=cleaned)
    return Verdict.allow()


def pre_guard(ctx):
    pol = _current_policy(ctx)
    if pol:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool == "issue_refund":
        return _gate_issue_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _gate_file_carrier_fault(ctx, action)
    if tool == "notify_carrier":
        return _gate_notify_carrier(ctx, action)
    return Verdict.allow()
