---
name: test-report
description: Tổng hợp trạng thái test của ticket WKY (bao nhiêu TC Passed / Failed / Blocked / Not Run, kèm lý do) từ 05-test-run.md thành docs/tickets/<Issue ID>/07-test-report.md. Dùng sau test-run / bug-log.
---

# Báo cáo kết quả test

Đầu vào: `05-test-run.md`, `04-test-cases.md` (danh sách đủ TC, link Sheet), `06-bugs.md` (nếu có).
Đầu ra: `docs/tickets/<Issue ID>/07-test-report.md` copy từ `assets/test-report-template.md` (ghi đè mỗi lần chạy — luôn là trạng thái mới nhất).

## Quy tắc

- Báo cáo chỉ gồm trạng thái đã test: số TC theo từng trạng thái, và danh sách TC không Passed kèm lý do. Không đề xuất Go/No-Go, không đăng comment lên WKY.
- Mỗi TC lấy trạng thái ở lượt chạy mới nhất có TC đó trong 05. TC trong 04 chưa từng chạy → `Not Run`.
- Mỗi TC Failed / Blocked / Skipped / Not Run phải có lý do: Failed → khác mong đợi ở điểm nào + BUG-ID; Blocked / Skipped → lý do ghi trong 05; Not Run → vì sao chưa chạy (vd "TC PRODUCTION, chưa test PRODUCTION", "chưa tới lượt").
- Không có lý do trong 05 → ghi `TBD — chưa ghi lý do`, không tự đặt ra.

## Các bước

1. Đọc các file đầu vào. Thiếu `05-test-run.md` → báo người dùng chạy `test-run` trước, rồi dừng.
2. Ghép trạng thái mới nhất cho từng TC trong 04.
3. Ghi `07-test-report.md`.
4. Báo cho người dùng: số TC theo trạng thái, link file.
