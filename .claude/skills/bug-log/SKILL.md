---
name: bug-log
description: Soạn bug từ các TC Failed trong docs/tickets/<Issue ID>/05-test-run.md (hoặc bug người dùng mô tả trong chat) vào 06-bugs.md, rồi tự đăng comment bug lên ticket WKY bằng Claude in Chrome. Cũng dùng để cập nhật trạng thái bug (fixed / verified / reopen). Dùng sau test-run.
---

# Ghi nhận bug

Đầu vào: TC `Failed` chưa có bug trong lượt chạy mới nhất của `05-test-run.md`, hoặc mô tả bug trong chat.
Đầu ra: `docs/tickets/<Issue ID>/06-bugs.md` copy từ `assets/bug-template.md`; một comment trên ticket WKY cho mỗi lần chạy; cột Bug trong `05-test-run.md` được điền.

## Quy tắc

- Đăng comment bug lên WKY không cần chờ duyệt. Đưa nguyên văn comment vào báo cáo cuối để người dùng xem lại.
- Một bug = một hành vi sai. Nhiều TC fail cùng nguyên nhân → một bug, liệt kê đủ TC.
- Trùng bug đang mở trong 06 → không tạo mới, thêm TC vào bug đó.
- Mức độ: P0 chặn luồng chính / mất dữ liệu; P1 sai AC P1; P2 sai AC P2 hoặc có cách tránh; P3 hiển thị, chữ.
- Kết quả thực tế ghi đúng cái quan sát được trong 05, không suy đoán nguyên nhân.
- Comment không chứa mật khẩu, token, dữ liệu cá nhân; không @mention trừ khi người dùng yêu cầu.

## Mẫu comment WKY

Chữ thường, không markdown:

```
[QA] Bug <BUG-ID> (<P1>): <tiêu đề>
Môi trường: <STG / PRODUCTION> — YYYY-MM-DD
TC: <TC-ID, …>
Các bước:
1. ...
Mong đợi: ...
Thực tế: ...
```

Nhiều bug trong cùng lần chạy → gộp vào một comment, cách nhau một dòng trống.

## Các bước — log bug mới

1. Đọc `05-test-run.md` (lượt mới nhất), `04-test-cases.md` (bước, mong đợi), `06-bugs.md` nếu đã có.
2. Gom TC Failed thành bug; đánh BUG-ID nối tiếp (`BUG-01`, `BUG-02`…). Ghi vào 06, trạng thái `Open`.
3. Điền cột Bug trong bảng kết quả của `05-test-run.md`.
4. Đăng comment theo mẫu: mở ticket và nhập comment như `wky-qa-comment` bước 3-8. Xác nhận bằng `get_page_text` comment đã có dòng `[QA] Bug`; không thấy → không gửi lại, báo người dùng.
5. Ghi `Đã log WKY YYYY-MM-DD` vào cột WKY của bug trong 06.
6. Báo cho người dùng: BUG-ID, mức độ, TC liên quan, nguyên văn comment đã đăng.

## Cập nhật trạng thái

`bug-log <Issue ID> fixed BUG-01` / `verified BUG-01` / `reopen BUG-01`:

- `fixed`: đổi trạng thái `Fixed`; liệt kê TC cần chạy lại = TC của bug, cộng toàn bộ TC cùng SC-ID nếu bug P0/P1. Gợi ý lệnh `test-run <Issue ID> <TC-ID…>`.
- `verified`: chỉ khi lượt chạy lại trong 05 có các TC đó `Passed` → `Verified`; ngược lại báo TC nào còn fail.
- `reopen`: đổi `Reopen`, đăng comment `[QA] Bug <BUG-ID> reopen` kèm kết quả lượt chạy lại.

## Bước tiếp theo

Sau khi Dev fix: `test-run` chạy lại → `bug-log … verified`. Khi xong: `test-report <Issue ID>`.
