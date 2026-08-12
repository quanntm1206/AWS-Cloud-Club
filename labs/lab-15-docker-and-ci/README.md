# lab-15: Docker and CI

## Goal

Non-root image; offline smoke; CI không deploy cloud.

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
.venv\Scripts\python.exe scripts/run_lab.py --lab 15
```

Starter chỉ kiểm contract tĩnh. Docker acceptance cần Docker Desktop/Engine đang chạy:

```powershell
docker build -t ml-roadmap:lab15 .
docker run --rm ml-roadmap:lab15 id
docker run --rm -d --name ml-roadmap-lab15 -p 8000:8000 ml-roadmap:lab15
Invoke-RestMethod http://127.0.0.1:8000/health
$body = @{age=35; tenure_months=12; monthly_charge=79; region='north'; contract='monthly'} | ConvertTo-Json
try { Invoke-WebRequest http://127.0.0.1:8000/predict -Method Post -ContentType application/json -Body $body } catch { $_.Exception.Response.StatusCode.value__ }
docker logs ml-roadmap-lab15
docker stop ml-roadmap-lab15
```

`id` phải cho user khác root; health trả `degraded` khi chưa mount artifact; predict trả `503` an toàn. Với artifact local, mount thư mục read-only và đặt `ML_ROADMAP_ARTIFACT_DIR=/artifacts`, rồi health phải có `model_loaded=true`. Luôn `docker stop` trong `finally` nếu smoke lỗi. CI chỉ chạy offline checks; không thêm AWS deploy.

Output starter có `status=starter-example-completed`: starter chạy xong, **không** có nghĩa Docker acceptance đã đạt. Lưu build/run/non-root/health/predict evidence cục bộ để tự đánh giá rồi mới đánh dấu lab complete; không gửi các file này cho ai.

## Acceptance

- Mini path chạy được; kết quả tái lập trong tolerance đã ghi.
- Không leakage/secret; config và artifact manifest đầy đủ.
- Stretch tách riêng, không cần để pass.

Bash (macOS/Linux), từ repository root:

```bash
.venv/bin/python scripts/run_lab.py --lab 15
```
