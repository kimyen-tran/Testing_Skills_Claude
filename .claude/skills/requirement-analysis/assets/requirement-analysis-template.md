# Phân tích yêu cầu — [Issue ID] [Tiêu đề]

| | |
|---|---|
| Nguồn | `01-ticket-raw.md` — [WKY URL] |
| Loại / Ưu tiên ticket | [Change request / Bug ...] / [Cao ...] |
| QA / Ngày | [Tên] / YYYY-MM-DD |
| Trạng thái | Draft / Ready for test design / Blocked |

## 1. Mục tiêu
[1-3 câu: thay đổi gì, vì sao]

## 2. Phạm vi
- Trong phạm vi: [màn hình, field, role, môi trường]
- Ngoài phạm vi: [...]
- Vùng ảnh hưởng (regression): [chức năng dùng chung logic/data]

## 3. Luồng chính
1. [...]

Luồng phụ / lỗi: [...]

## 4. Business rules
| ID | Rule | Trước | Sau | Thay đổi | Nguồn |
|---|---|---|---|---|---|
| BR-01 | [...] | [...] | [...] | NEW / CHANGED / SAME | [mục trong ticket] |

## 5. Acceptance criteria
| ID | Given | When | Then | BR | Priority (tạm) |
|---|---|---|---|---|---|
| AC-01 | [...] | [...] | [...] | BR-01 | P1 |

Priority do PM chốt; QA chỉ đề xuất.

## 6. Chiến lược test
- Loại test: [Manual UI / API / ...] — lý do
- Môi trường: [STG / PROD]
- Test data cần chuẩn bị: [...]
- Bắt đầu test khi: [build lên STG, câu hỏi Blocker đã trả lời, ...]
- Kết thúc test khi: [100% P0/P1 Passed, không còn bug P0/P1 mở, ...]
- Priority: P0 = chặn release · P1 = phải pass trừ khi chấp nhận rủi ro · P2 = pass ≥ 90% · P3 = có thể hoãn

## 7. Rủi ro & phụ thuộc
- [...]

## 8. Câu hỏi mở
| ID | Câu hỏi | Vì sao cần hỏi | Giả định tạm | Mức độ | Trạng thái | Trả lời |
|---|---|---|---|---|---|---|
| Q-01 | [...] | [...] | [...] | Blocker / High / Low | Chưa hỏi / Đã hỏi YYYY-MM-DD / Đã trả lời | |
