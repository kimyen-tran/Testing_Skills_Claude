# Testing_Skills

Bộ skill Claude Code cho quy trình QA ticket WKY (wky.liftsoft.vn).

## Chạy cả quy trình

```
/wky-qa-flow https://wky.liftsoft.vn/issue-management/<số issue>
```

Lần 1 chạy tới khi đăng câu hỏi lên WKY rồi dừng. Trả lời trên WKY (theo Q-ID), sau đó gõ lại lệnh trên để chạy tiếp tới báo cáo. Thêm `chạy lại test` sau khi Dev fix bug.

## Thứ tự chạy các skill

Skill nằm trong `.claude/skills/`. Đầu ra nằm trong `docs/tickets/<Issue ID>/` (gitignore).

| # | Skill | Việc làm | Đầu ra |
|---|---|---|---|
| 0 | `wky-qa-flow` | Gọi lần lượt các skill 1-8 | — |
| 1 | `wky-ticket-fetch` | Lấy nội dung ticket (chữ, ảnh) bằng Claude in Chrome | `01-ticket-raw.md` |
| 2 | `requirement-analysis` | Phân tích BR / AC / câu hỏi mở | `02-requirement-analysis.md` |
| 3 | `wky-qa-comment` | Đăng câu hỏi mở lên WKY | Comment WKY |
| — | *(chờ trả lời trên WKY)* | | |
| 4 | `requirement-analysis` (đọc trả lời trên WKY) | Cập nhật câu trả lời vào 02 | `02-requirement-analysis.md` |
| 5 | `test-design` | Kịch bản và test case | `03-test-scenarios.md`, `04-test-cases.md` |
| 6 | `test-cases-to-gsheet` | Xuất test case lên Google Sheet | Link Sheet trong `04` |
| 7 | `test-run` | Chạy test trên STG, xuất Sheet kết quả | `05-test-run.md` |
| 8 | `bug-log` | Ghi bug, đăng comment bug lên WKY | `06-bugs.md` |
| 9 | `test-report` | Tổng hợp trạng thái test | `07-test-report.md` |

## Cài đặt cần có

- Extension Claude in Chrome đang kết nối, Chrome đã đăng nhập WKY.
- Connector Google Drive bật trong claude.ai.
- Tài khoản STG trong `.claude/test-accounts.local.json` (gitignore):
  `{"STG": {"url": "https://...", "username": "...", "password": "..."}}`
