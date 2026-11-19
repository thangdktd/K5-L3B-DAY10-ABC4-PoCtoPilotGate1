# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):
- Lớp: `L3A` / `L3B`
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |           |      |     |             |
|   2 |           |      |     |             |
|   3 |           |      |     |             |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

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
