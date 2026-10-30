# WKY Testing Skills

Trạng thái: đang làm (Phase 3)

## Mục tiêu
Quy trình QA cho ticket WKY, từ ticket đến báo cáo kết quả test. Cấu trúc riêng, lấy ý tưởng từ QA Test Process Guide của tổ chức (không lưu guide trong repo).

| Bước | Skill | Đầu ra trong `docs/tickets/<Issue ID>/` | Trạng thái |
|---|---|---|---|
| 1 | `wky-ticket-fetch` | `01-ticket-raw.md` | ✅ |
| 2 | `requirement-analysis` | `02-requirement-analysis.md` (cả cập nhật câu trả lời) | ✅ chạy trên LAP_I2195 |
| 3 | `wky-qa-comment` | Câu hỏi mở đăng lên WKY; cập nhật trạng thái ở 02 §8 | đã viết skill |
| 4 | `test-design` | `03-test-scenarios.md`, `04-test-cases.md` | ✅ chạy trên LAP_I2195 |
| 5 | `test-cases-to-gsheet` | Google Sheet mới; link ghi ở đầu `04` | đã viết skill |
| 6 | `test-run` | Kết quả trong `04`; `05-test-run.md`; Sheet kết quả mới mỗi lượt | đã viết skill |
| 7 | `bug-log` | `06-bugs.md`; comment bug trên WKY | đã viết skill |
| 8 | `test-report` | `07-test-report.md` (số TC theo trạng thái + lý do) | đã viết skill |

Script: `scripts/md_table_to_csv.py` (bảng 04 → CSV, chỉ dùng thư viện chuẩn).

## Quyết định
- Cấu trúc riêng dựa trên guide, không copy (2026-10-29). Lấy từ guide: AC dạng Given/When/Then, priority P0-P3, liên kết kịch bản → TC, điều kiện bắt đầu/kết thúc test, câu hỏi mở có người phụ trách, không để trống ô, regression bắt buộc khi fix bug P0/P1. Gộp spec-overview + spec + checklist + test-strategy của guide thành `02-requirement-analysis.md`. Bỏ (không có source code LAP, test trên UI): checklist kỹ thuật, Postman, fixture, Gate 0-3, coverage, flaky track, chữ ký.
- File đánh số theo bước để thư mục đọc theo thứ tự. Template nằm trong `assets/` của từng skill.
- Thư mục mỗi ticket = Issue ID WKY, nằm trong `docs/tickets/` (gitignore — nội dung nội bộ).
- WKY không có API → dùng **Claude in Chrome** trên Chrome đã đăng nhập của người dùng. Agent không bao giờ nhập mật khẩu.
- Google Sheet (2026-10-30): mỗi ticket một Sheet mới, tạo bằng connector **Google Drive** của claude.ai (upload CSV → tự chuyển thành Sheet). Bỏ service account / `gspread`. Không có connector Google Sheets, Drive không ghi được vào ô → kết quả ghi vào `04` + `05`, mỗi lượt chạy xuất một Sheet kết quả mới (người dùng chọn 2026-10-30).
- Chạy test (2026-10-30): Claude tự chạy bằng Claude in Chrome, **chỉ STG** (chưa làm PRODUCTION; TC PRODUCTION giữ `Not Run`). Đăng nhập bằng tài khoản test trong `.claude/test-accounts.local.json` (gitignore, không commit). URL STG ghi ở `02` §6.
- Báo cáo (2026-10-30): `07-test-report.md` chỉ gồm số TC Passed / Failed / Blocked / Skipped / Not Run và lý do từng TC không Passed. Không Go/No-Go, không comment "Test done".
- Tự chạy, ít hỏi (2026-10-30): skill chỉ dừng hỏi khi cần đăng nhập (WKY / STG chuyển sang SSO, không có tài khoản) hoặc thiếu URL môi trường. Mọi comment WKY (câu hỏi, bug), tạo Sheet, ghi kết quả đều không chờ duyệt; nguyên văn comment đưa vào báo cáo cuối. Điểm mơ hồ → ghi giả định / Q-ID và chạy tiếp.
- Mọi file skill/md viết bằng tiếng Việt; giữ nguyên thuật ngữ kỹ thuật, tên tool, tên field.

## Các phase
| # | Phase | Xong khi |
|---|---|---|
| 0 | ✅ Lấy ticket (chữ + ảnh + chữ tô màu) | `docs/tickets/LAP_I2195/01-ticket-raw.md` |
| 1 | ✅ Chạy bước 2 trên LAP_I2195 | Người dùng duyệt 02 |
| 2 | `wky-qa-comment`: Q-ID ở 02 §8 → bản nháp → duyệt → đăng | Comment thử trên 2195 |
| 3 | Chạy bước 5-8 trên LAP_I2195 | Sheet có link trong 04; 05/06/07 được tạo; comment trên 2195 |
| 4 | `wky-qa-flow <link ticket>`: giai đoạn 1 (lấy ticket → phân tích → đăng câu hỏi) → dừng chờ trả lời → giai đoạn 2 (đọc trả lời → thiết kế test → Sheet → chạy test → bug → báo cáo); gọi lại cùng lệnh để chạy tiếp (đã viết skill) + evals | Chạy trọn chuỗi trên ticket mới |

## Rủi ro
- Giao diện WKY thay đổi → việc lấy ticket dựa vào chữ trên trang, không dựa vào selector.
- Hết phiên đăng nhập → skill nhận ra `/login`, người dùng tự đăng nhập lại.
- Cần extension Claude in Chrome đang kết nối; không chạy được kiểu headless/lên lịch.
- Claude đánh giá sai Passed/Failed → TC mơ hồ đánh `Blocked` + Q-ID, không đoán; người dùng xem lại `05-test-run.md`.
- Comment bug tự đăng có thể sai → người dùng xem nguyên văn trong báo cáo cuối của `bug-log` và sửa trên WKY nếu cần.
- Mỗi lượt chạy tạo thêm một Sheet trên Drive → tên file có ngày để phân biệt; người dùng tự dọn Sheet cũ.
