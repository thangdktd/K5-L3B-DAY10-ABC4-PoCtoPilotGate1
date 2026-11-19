# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `ABC4`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-ABC4-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S3`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Hồng Thắng | 2A202603829 | Sản phẩm và kinh doanh | x |
|   2 | Lê Danh Giang | 2A202603912 | Sản phẩm và kinh doanh (Phân tích và rủi ro) | |
|   3 | Đỗ Lý Hoàng Nam | 2A202603777 | Kỹ sư cổng | |
|   4 | Hoàng Thế Phong | 2A202603832 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenHongThang-2A202603829

### Phần việc phụ trách

- Vai: **Trưởng nhóm · Sản phẩm và kinh doanh (TV1)**.
- Phụ trách: Điều phối nhóm, tổng hợp Phiếu A (`templates/form-a-criteria.md`), viết và ký `config/acceptance_criteria.json`; chạy `lab10.checkpoint` chốt cổng Vòng 1 và viết Quyết định Gate 1 `v1` (Phiếu B mục B8); nhận thẻ sự cố `incidents/S3/`; viết Quyết định Gate 1 `v2` & ba dòng bắt buộc (Phiếu C mục C12), điền `submission/submission.json` và gom bài nộp.

### Đóng góp cụ thể

- **Khối 1 (`templates/form-a-criteria.md` & `config/acceptance_criteria.json`):** Tổng hợp mục tiêu hệ thống A1–A4, bộ ngưỡng `required` (`pass_rate_min = 0.96`, `pass_k_min = 0.91`, 3 chỉ số an toàn `= 0`), `nice_to_have` (`escalation_rate_max = 0.28`), `business_ops` (`cost_per_ticket_vnd_max = 7000`, `roi_min = 0.4`, `queue_stuck_max = 0`), `stop_condition`, `decision_rule` và ký bằng `lab10.criteria sign` trước mọi lần đánh giá đầu tiên.
- **Vòng 1 (`B8` & `lab10.checkpoint`):** Chốt cổng Vòng 1 (`29e2d521`, tạo `lab10/guards_round1.py` và `config/operating_gates.round1.json`), chạy `eval --suite base --stage prepared` + `lab10.gate`, đưa ra quyết định **v1 = `Cải tiến thêm`** do nhóm kho `?` tốn `10.359đ/ticket` (> làm tay `10.000đ`) và chưa có bằng chứng trên gói sự cố.
- **Vòng 2 (`S3` & `C12`):** Kéo thẻ `incidents/S3/`, kiểm tra chứng từ sau khi đội hoàn thiện `guards.py`, `monitors.py`, `C0–C11`, viết Quyết định **v2 = `Thu hẹp`** (mở 100% pilot cho các kho xác định `HN/HCM/CT/DN`, tách riêng ticket thiếu định danh kho `?` sang làm tay), điền `submission/submission.json` và chốt Giai đoạn 5.

### Bằng chứng

- Commits: `c975007` (`Sign acceptance criteria`, `2026-11-19T15:30:04`), `c34c791` (Phiếu A), `2bb8d8d` (chốt Vòng 1 & `B8`), `d4602a5` (nhận thẻ `S3`), `07478a6` (quyết định `C12` v2).
- Mã lần chạy / file: `R-base-prepared-20261119-164758-4ca3d6` (`B8`), `R-S3-after-20261119-174948-bad148`, `R-S3-grade-20261119-174945-bad148`, `R-base-after-20261119-175128-bad148` (`C12`); `config/acceptance_criteria.json`, `config/acceptance_criteria.lock`, `config/round1.lock`, `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md` (`B8`), `templates/form-c-incident.md` (`C12`), `submission/submission.json`.

### Exit ticket

- **Một điều học được:** Ký bản tiêu chí gồm cả `business_ops` (`cost_per_ticket_vnd`, `roi`, `queue_stuck`) và `decision_rule` trước khi đo giúp quyết định Gate 1 không chạy theo `pass_rate` đơn thuần; dù tổng hợp `S3 · after` đạt `1.0` và `ROI = 1.27`, phân tích theo `by_segment` vẫn chỉ ra cần **Thu hẹp** riêng nhóm thiếu kho (`?`, `10.359đ/ticket`).
- **Một điều còn chưa chắc:** Trên dữ liệu production thật, tỷ lệ ticket thiếu mã kho (`?`) và độ trễ đồng bộ `tracking DB` có thể biến động mạnh trong mùa cao điểm/thiên tai nên cần đo lại ở tuần pilot đầu tiên trước Bước đánh giá 2.

---

## LeDanhGiang-2A202603912

### Phần việc phụ trách

- Vai: **Phân tích và rủi ro (Sản phẩm và kinh doanh – TV2)**.
- Phụ trách: Đề xuất thước đo Phiếu A (`A2`), chạy Baseline và lập `BASELINE_REPORT_ABC4.md`, hoàn thiện Phiếu B mục `B0–B6` (`templates/form-b-evaluation-gates.md`) và hoàn thiện phần phân tích sự cố + tổng hợp Phiếu C mục `C0–C7`, `C9–C10` (`templates/form-c-incident.md`).

### Đóng góp cụ thể

- **Baseline & Vòng 1 (`B0–B6`):** Chạy `base · before` (`pass_rate = 0.9909`, `pass_k = 0.9545`, `wrongful_refund_vnd = 20000`, `wrongful_carrier_faults = 1`), dò trace `T-002@55` lập bảng soát lỗi `B1–B2`, lập bản đồ dữ liệu và drift chính sách `REFUND-v3 → REFUND-v4` (`B3`), HAZOP 6 dòng ngoài mô hình (`B4`), checklist 9 nhóm có PIC cụ thể (`B5`) và Pre-mortem 4 lăng kính dẫn thẳng thành 3 cổng phòng ngừa (`B6`).
- **Vòng 2 (`S3` & `C0–C7`, `C9–C10`):** Chạy `grade` tại mốc `prepared` (`pass_rate = 0.8333`), dò trace `S3-01`, `S3-02`, `S3-04`, `S3-20` (Vòng 1 đã đỡ sạch `900.000đ` hoàn sai và `35` lỗi oan) cùng `S3-42`, `S3-43` (`10/60` lượt hỏng do `escalate` ở `file_carrier_fault` sau khi `issue_refund` đã ghi sổ cái); viết C1–C6, tổng hợp sau sửa `C0` (`2–4`), `C7`, Fault tree sau sửa `C9` và Risk Register 3 dòng (`C10`) gắn ngưỡng monitor.

### Bằng chứng

- Commits: `4895926` (`BASELINE_REPORT_ABC4.md`), `7b27095` & `543c6f2` (`B0–B6`), `67a59d1` (`C0–C6`), `6d11df4` / `ef281a4` (`C0, C7, C9, C10`).
- Mã lần chạy: `runs/R-base-before-20261119-155457-bde05c`, `runs/R-S3-before-20261119-171840-4ca3d6`, `runs/R-S3-prepared-20261119-171840-4ca3d6`, `runs/R-S3-after-20261119-174452-4b50ac`, `runs/R-base-after-20261119-174453-4b50ac`, `runs/R-S3-grade-20261119-174454-4b50ac` (`pass_rate = 1.0`, `pass_k = 1.0`, `13/13` unit tests `OK`).

### Exit ticket

- **Một điều học được:** So sánh Fault Tree trước và sau sửa cùng 3 mốc `base · prepared · after` giúp tách bạch nhánh đã được chặn cứng từ Vòng 1 (`policy` drift, `delay_cause: null`/`FORCE_MAJEURE`) khỏi lỗi thứ tự thực thi ở nhánh vượt trần lỗi hãng (`S3-42`, `S3-43`), đồng thời nhìn rõ nhánh còn hở sau khi chuyển sang `Verdict.deny`.
- **Một điều còn chưa chắc:** Khi nhánh vượt 2 lỗi/hãng/ngày chặn êm bằng `Verdict.deny` (`guard_deny_carrier_strikes`), cần theo dõi trên dữ liệu pilot thật xem có phát sinh bỏ sót khoản thu hồi `120.000đ`/lỗi từ các hãng vi phạm thật ngoài thiên tai hay không.

---

## DoLyHoangNam-2A202603777

### Phần việc phụ trách

- Vai: **Kỹ sư cổng (TV3 – Lập trình guards)**.
- Phụ trách: Kiểm tra tính khả thi kỹ thuật cho Phiếu A; xây dựng cổng Vòng 1 và hoàn thiện mục B7.1–B7.3 trong `templates/form-b-evaluation-gates.md`; sửa cổng Vòng 2 cho thẻ `S3` trong `lab10/guards.py` (liên kết mục C7 trong `templates/form-c-incident.md`).

### Đóng góp cụ thể

- **Phiếu A:** Rà soát `lab10/guards.py` và `lab10/helpers.py`, xác nhận tính khả thi kiểm soát 3 chỉ số an toàn (`wrongful_refund_vnd = 0`, `wrongful_carrier_faults = 0`, `pii_leaks = 0`) và góp ý hạn chế lạm dụng `escalate` gây ùn hàng chờ.
- **Vòng 1 (`lab10/guards.py` & Phiếu B B7.1–B7.3):** Cài đặt 3 cổng phòng ngừa (`pre_guard` ghim chính sách hiệu lực `H.effective_policy`; `write_gate` kiểm soát `issue_refund` theo `H.db_delay_days`, `H.entitlement_vnd`, `ledger_rows`, `approvals`, trần khách/ngày và trần ngày; `write_gate` kiểm soát `file_carrier_fault` theo `H.carrier_at_fault` và lọc PII ở `notify_carrier`). Chạy 2 `--adhoc` behavioral test.
- **Vòng 2 (`lab10/guards.py`):** Phát hiện và sửa lỗi thứ tự ghi sổ cái trước khi `file_carrier_fault` ở `S3-42`, `S3-43` bằng cách chuyển nhánh vượt trần lỗi hãng/ngày từ `Verdict.escalate` sang `Verdict.deny` + ghi sự kiện `guard_deny_carrier_strikes`, giữ nguyên cổng Vòng 1 và không hardcode.

### Bằng chứng

- Commit Vòng 1: `73ca49d` (PR `#2`, merge `79369c8`).
- Mã lần chạy Vòng 1: `runs/R-base-after-20261119-162606-a1f53e` (`pass_rate = 1.0`, `pass_k = 1.0`, 13/13 unit tests OK).
- Mã lần chạy Vòng 2: `runs/R-S3-after-20261119-172648-bd4074` (`S3 · after`: `pass_rate = 1.0`, `pass_k = 1.0`, `60/60`) và `runs/R-base-after-20261119-172649-bd4074` (`base · after`: `pass_rate = 1.0`, `110/110`, không regression).

### Exit ticket

- **Một điều học được:** Thứ tự gọi tool ghi (`issue_refund` trước `file_carrier_fault`) ảnh hưởng trực tiếp tới hành vi của `Verdict.escalate`; nếu đặt `escalate` sau khi đã ghi sổ cái thì đơn bị treo dù tiền đã xuất.
- **Một điều còn chưa chắc:** Trên dữ liệu thật ngoài pilot với nhiều chính sách chuyển tiếp và nhiều kho mới, cần đo thêm xem tỉ lệ `guard_deny_carrier_strikes` có làm tăng tải đối soát thủ công cho kế toán/vận hành hay không.

---

## HoangThePhong-2A202603832

### Phần việc phụ trách

- Vai: **Vận hành và pháp lý (TV4)**.
- Phụ trách: Rà soát yêu cầu vận hành & đối soát trong Phiếu A (`A1`, `A2` telemetry), cấu hình `config/operating_gates.json` (3 khối `business`, `operations`, `legal`), viết Phiếu B mục `B7.4–B7.6` (Runbook 1–3 & Giờ cao điểm), cài đặt chỉ số theo dõi mới trong `lab10/monitors.py` và hoàn thiện Phiếu C mục `C8`, `C11` (cập nhật checklist & Runbook 4–5).

### Đóng góp cụ thể

- **Vòng 1 (`config/operating_gates.json` & `B7.4–B7.6`):** Đặt các ngưỡng `business` (`daily_refund_cap_vnd = 2000000`, `cost_budget_per_ticket_vnd = 1500`, `roi_min = 0.4`, `pilot_scope` all/100%), `operations` (`pic = "NV-TUNG"`, `approver_id = "NV-HANH"`, `reviewers_on_shift = 1`, `review_capacity_per_hour = 6`, `max_queue_wait_minutes = 60`, `alert_channel = "#ops-refund-alerts"`, `decision_note = true`, `review_sampling_pct = 10`, `stop_conditions` 3 điều kiện) và `legal` (khóa 5 trường PII, bật `carrier_fault_requires_recorded_cause = true`); viết Runbook 1–3 và kịch bản Giờ cao điểm.
- **Vòng 2 (`lab10/monitors.py` & `C8`, `C11`):** Bổ sung 2 monitor mới không cần nhãn vào `MONITORS` là `carrier_fault_rate` và `auto_refund_rate` (sáng đèn rõ rệt: `carrier_fault_rate` trên bộ nền `0.509091 → 0.500000` vs trên `S3` `0.833333 → 0.333333`, đạt `6 monitor ✅`); cập nhật checklist nhóm 7–8 và viết Runbook 4–5 (quy trình đối soát bão lũ 4 giờ với `MKD` qua `NV-OANH`, nâng kiểm mẫu `review_sampling_pct` lên `20%` vùng thiên tai).

### Bằng chứng

- Commits: `45d2b2e` (PR `#3` `25f5f15`: `config/operating_gates.json`, `B7.4–B7.6`), `8c15f72` (PR `#6` `54deded`: `lab10/monitors.py`, `C8`, `C11`).
- Mã lần chạy / file: `R-S3-grade-20261119-173749-809348` (`C11`), `R-S3-grade-20261119-174454-4b50ac` (`6 monitor ✅`), `lab10/monitors.py`, `config/operating_gates.json`, `templates/form-b-evaluation-gates.md` (`B7.4–B7.6`), `templates/form-c-incident.md` (`C8`, `C11`).

### Exit ticket

- **Một điều học được:** Trong production không có sẵn nhãn "phạt oan", nên phải kết hợp chỉ số telemetry không cần nhãn (`carrier_fault_rate` với ngưỡng VÀNG `> 30%` / ĐỎ `> 40%`) cùng Runbook có tên PIC cụ thể (`NV-TUNG`, `NV-HANH`, `NV-OANH`) mới phản ứng kịp trước khi đối tác khiếu nại.
- **Một điều còn chưa chắc:** Khi nâng tỷ lệ kiểm mẫu lên `20%` trong bão lũ trùng giờ sale cao điểm, công suất `1 reviewer = 6 ca/giờ` có thể chạm hạn chờ nếu không kích hoạt nhân sự dự phòng kịp thời trong 30 phút đầu.
