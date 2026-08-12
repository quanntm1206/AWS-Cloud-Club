# lab-13: ML testing

## Goal

Test schema, missing, unknown category, reload parity và metric boundaries.

## Preconditions

- Đọc tuần tương ứng; dùng mini profile trước.
- Không đưa token, credential, data cá nhân hoặc artifact lớn vào Git.

## Steps

1. Ghi giả thuyết, input/output contract và baseline.
2. Chạy tests/checks trước thay đổi; lưu failure có ý nghĩa.
3. Hoàn thiện phần `starter/`; ghi command, seed, runtime, metric.
4. Phân tích ít nhất một failure case; cập nhật README.
5. Chạy acceptance checks và lưu output tóm tắt.

## Command

Chạy từ repository root:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 13
```


Bash (macOS/Linux), từ repository root:

```bash
.venv/bin/python scripts/run_lab.py --lab 13
```

Code mẫu domain nằm trong `src/ml_roadmap/lab_examples.py`; output `.artifacts/lab-13-evidence.json` có `status=starter-example-completed`: starter chạy xong, **không** có nghĩa toàn bộ acceptance của lab đã đạt. Hoàn thành các bước, lưu evidence/rubric cục bộ để tự đánh giá rồi mới đánh dấu lab complete; không gửi các file này cho ai.

## Acceptance

- Mini path chạy được; kết quả tái lập trong tolerance đã ghi.
- Không leakage/secret; config và artifact manifest đầy đủ.
- Stretch tách riêng, không cần để pass.
