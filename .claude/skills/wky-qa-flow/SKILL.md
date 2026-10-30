---
name: wky-qa-flow
description: Chạy trọn quy trình QA cho một ticket WKY chỉ từ link ticket — lấy ticket, phân tích, đăng câu hỏi, dừng chờ người dùng trả lời trên WKY, đọc trả lời, thiết kế test, xuất Sheet, chạy test trên STG, log bug, báo cáo. Gọi lại cùng lệnh (hoặc nói "đã trả lời") để chạy tiếp từ chỗ dừng. Dùng khi người dùng đưa link / số issue WKY.
---

# Chạy trọn quy trình QA

Thứ tự: `wky-ticket-fetch` → `requirement-analysis` → `wky-qa-comment` → *(chờ trả lời)* → `requirement-analysis` (đọc trả lời) → `test-design` → `test-cases-to-gsheet` → `test-run` → `bug-log` → `test-report`. Bảng đầy đủ trong `README.md`.

Đầu vào: link ticket (vd `https://wky.liftsoft.vn/issue-management/2195`) hoặc số issue. Lấy số issue = phần số cuối link.
Tuỳ chọn: `bỏ qua câu hỏi` (không chờ trả lời, dùng giả định tạm), `chạy lại test` (thêm lượt `test-run` mới).
Đầu ra: các file `01`…`07` trong `docs/tickets/<Issue ID>/` và comment trên ticket, như từng skill con.

## Quy tắc

- Gọi từng skill con bằng Skill tool, đúng thứ tự dưới, không chép lại nội dung skill con.
- Không hỏi người dùng giữa chừng. Chỉ dừng ở 3 chỗ: **điểm chờ trả lời** (giai đoạn 1 → 2), cần người dùng đăng nhập (WKY / STG), hoặc một bước lỗi mà bước sau phụ thuộc vào.
- Bước đã có kết quả thì bỏ qua, nên gọi lại cùng lệnh là chạy tiếp từ chỗ dừng.
- `wky-ticket-fetch` nhận số issue; các skill sau nhận Issue ID (vd `LAP_I2195`) — lấy từ thư mục được tạo ở bước 1.

## Giai đoạn 1 — Phân tích và hỏi

| # | Skill | Bỏ qua khi |
|---|---|---|
| 1 | `wky-ticket-fetch <số issue>` | Đã có `01-ticket-raw.md` |
| 2 | `requirement-analysis <Issue ID>` | Đã có `02-requirement-analysis.md` |
| 3 | `wky-qa-comment <Issue ID>` | §8 của 02 không có Q-ID `Chưa hỏi` |

**Điểm chờ trả lời:** sau bước 3, nếu §8 còn Q-ID `Đã hỏi` (chưa có trả lời) → **dừng**. Báo người dùng: danh sách Q-ID đang chờ, link ticket, và cách chạy tiếp: trả lời trên WKY (theo Q-ID) rồi gõ lại `/wky-qa-flow <link>` hoặc nói "đã trả lời" trong cùng phiên. Không có câu hỏi nào → sang giai đoạn 2 luôn.

## Giai đoạn 2 — Test

| # | Skill | Bỏ qua khi |
|---|---|---|
| 4 | `requirement-analysis <Issue ID> đọc trả lời trên WKY <số issue>` | §8 không có Q-ID `Đã hỏi` |
| 5 | `test-design <Issue ID>` | Đã có `04-test-cases.md` |
| 6 | `test-cases-to-gsheet <Issue ID>` | File 04 đã có dòng `Google Sheet:` |
| 7 | `test-run <Issue ID>` | Đã có lượt chạy trong `05-test-run.md` (trừ khi `chạy lại test`) |
| 8 | `bug-log <Issue ID>` | Lượt chạy mới nhất không còn TC `Failed` chưa có BUG-ID |
| 9 | `test-report <Issue ID>` | Không bao giờ — luôn cập nhật |

- Sau bước 4, nếu còn Q-ID chưa có trả lời trên WKY → dừng lại ở điểm chờ (báo Q-ID còn thiếu), trừ khi người dùng nói `bỏ qua câu hỏi` — khi đó `test-design` dùng giả định tạm.
- Câu hỏi mới phát sinh ở bước 4-9 (vd Q-ID thêm khi chạy test) không làm dừng flow; ghi vào báo cáo cuối để người dùng hỏi ở lần chạy sau.

## Báo cáo cuối

Một bảng: bước — đã chạy / bỏ qua / dừng — kết quả chính (số BR/AC/Q, số TC, link Sheet, số TC theo trạng thái, BUG-ID). Kèm nguyên văn các comment đã đăng lên WKY trong lần chạy này, Q-ID đang chờ trả lời, và lệnh để chạy tiếp nếu đang dừng.
