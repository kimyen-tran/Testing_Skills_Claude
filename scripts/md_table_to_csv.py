"""Chuyển bảng markdown đầu tiên trong file thành CSV (in ra stdout).

Dùng cho bước test-cases-to-gsheet: CSV được upload lên Google Drive và
tự chuyển thành Google Sheet. `<br>` trong ô thành xuống dòng trong ô Sheet.

Cách dùng: python3 scripts/md_table_to_csv.py docs/tickets/<Issue ID>/04-test-cases.md
"""

import csv
import re
import sys


def split_row(line):
    # Tách ô theo `|`, bỏ qua `\|` (dấu | đã escape trong nội dung ô)
    cells = re.split(r"(?<!\\)\|", line.strip().strip("|"))
    return [c.strip().replace("\\|", "|").replace("<br>", "\n") for c in cells]


def first_table(lines):
    rows = []
    for line in lines:
        if line.lstrip().startswith("|"):
            rows.append(line)
        elif rows:
            break
    if len(rows) < 2:
        sys.exit("Không tìm thấy bảng markdown trong file")
    # Dòng thứ 2 là dòng phân cách |---|---|
    return [split_row(rows[0])] + [split_row(r) for r in rows[2:]]


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        table = first_table(f.read().splitlines())
    csv.writer(sys.stdout, lineterminator="\n").writerows(table)


if __name__ == "__main__":
    main()
