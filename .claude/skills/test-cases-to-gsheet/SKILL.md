---
name: test-cases-to-gsheet
description: Xuất bảng test case trong docs/tickets/<Issue ID>/04-test-cases.md thành một Google Sheet mới trên Google Drive của người dùng, rồi ghi link Sheet vào đầu file 04. Dùng sau test-design, trước test-run.
---

# Xuất test case lên Google Sheet

Đầu vào: `docs/tickets/<Issue ID>/04-test-cases.md` (chưa có thì chạy `test-design` trước).
Đầu ra: một Google Sheet tên `[QA] <Issue ID> - Test cases`; dòng `Google Sheet: <link>` ở đầu file 04.

## Quy tắc

- Mỗi ticket một Sheet. File 04 đã có dòng `Google Sheet:` → dừng, báo link hiện có; chỉ tạo Sheet mới khi người dùng nói rõ "tạo lại" (Sheet cũ giữ nguyên, không xoá).
- Cột trên Sheet = cột bảng của file 04, giữ nguyên thứ tự và tên cột.
- Sheet này là bản test case ban đầu. Kết quả test do `test-run` ghi vào file 04 rồi xuất thành Sheet kết quả riêng cho mỗi lượt chạy.
- Không đổi quyền chia sẻ Sheet; người dùng tự chia sẻ nếu cần.

## Các bước

1. Đổi bảng sang CSV: `python3 scripts/md_table_to_csv.py docs/tickets/<Issue ID>/04-test-cases.md`. Lỗi → báo người dùng, không tự soạn CSV bằng tay.
2. Upload CSV lên Google Drive qua connector Google Drive, tên file `[QA] <Issue ID> - Test cases`, kiểu nội dung `text/csv` để Drive tự chuyển thành Google Sheet. Không có connector → báo người dùng bật connector Google Drive trong claude.ai, rồi dừng.
3. Từ kết quả lấy file ID, link = `https://docs.google.com/spreadsheets/d/<file ID>/edit`.
4. Thêm vào ngay dưới tiêu đề file 04: `Google Sheet: <link> (xuất YYYY-MM-DD)`.
5. Báo cho người dùng: link Sheet, số dòng TC đã xuất.

## Bước tiếp theo

`test-run <Issue ID>` để chạy test trên STG.
