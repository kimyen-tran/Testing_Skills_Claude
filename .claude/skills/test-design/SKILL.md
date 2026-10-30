---
name: test-design
description: Thiết kế test cho ticket WKY từ 02-requirement-analysis.md — tạo 03-test-scenarios.md (kịch bản theo nhóm và mức rủi ro) và 04-test-cases.md (test case từng bước, nguồn để đẩy lên Google Sheet). Dùng sau requirement-analysis.
---

# Thiết kế test

Đầu vào: `docs/tickets/<Issue ID>/02-requirement-analysis.md`.
Đầu ra trong cùng thư mục, copy từ `assets/`:
- `03-test-scenarios.md` ← `test-scenarios-template.md`
- `04-test-cases.md` ← `test-cases-template.md`

## Quy tắc

- Nếu bản phân tích đang `Blocked`: vẫn tiếp tục, dùng "Giả định tạm" của từng câu hỏi Blocker và ghi Q-ID vào cột Ghi chú của TC; liệt kê các giả định này trong báo cáo cuối. Không dừng lại hỏi.
- Kịch bản: phủ mọi BR và AC; đi qua mọi nhóm trong template (nhóm không áp dụng ghi `N/A` kèm lý do). Với rule kết hợp nhiều điều kiện, phủ mọi tổ hợp chứ không chỉ các tổ hợp ticket liệt kê. Nghĩ tới biên: hoa/thường, khoảng trắng, chuỗi con, giá trị rỗng, nhiều từ khoá trong cùng một giá trị. Ticket rộng hoặc rủi ro cao có thể dùng thêm `/ck:scenario` để lấy ý tưởng.
- Mỗi kịch bản Critical / High / Medium có ít nhất 1 TC; kịch bản Low có thể gộp.
- Không để trống Điều kiện trước / Test data / Các bước / Kết quả mong đợi / Priority / Loại. Kết quả mong đợi ghi giá trị UI cụ thể, không ghi "hiển thị đúng".
- Mỗi TC trỏ về một SC-ID và một AC/BR. Không có TC "mồ côi".
- Nghi vấn mới → thêm Q-ID vào `02-requirement-analysis.md` §8.
- Viết bằng tiếng Việt; nhãn UI và giá trị giữ nguyên như trong ticket.

## Các bước

1. Đọc `02-requirement-analysis.md`.
2. Ghi `03-test-scenarios.md`, sau đó `04-test-cases.md` kèm bảng tổng hợp theo priority.
3. Báo cho người dùng: số lượng SC / TC theo priority, nhóm chưa phủ, câu hỏi mới.

## Bước tiếp theo

`test-cases-to-gsheet <Issue ID>` xuất `04-test-cases.md` thành Google Sheet.
