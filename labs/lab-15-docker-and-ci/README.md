# Lab 15 - Đóng gói service và chạy CI smoke

## Mục tiêu

Container giúp runtime nhất quán, nhưng một image build thành công chưa chứng minh service an toàn. Bạn sẽ kiểm user, health, predict và cleanup container.

## Thuật ngữ trong lab

**Thuật ngữ mới:** `container`, `CI`

**Ôn lại:** `API contract`, `artifact`, `reproducibility`, `latency`

**Áp dụng trong lab:** Đóng package/API contract vào `container`, dùng `CI` chạy data validation, parity và test artifact; đo latency nhỏ rồi cleanup container để giữ reproducibility.

**Tự giải thích:** Container và CI giúp reproducibility ở phần nào nhưng không thay thế test nào?

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-16.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Chạy smoke demo Python để xem contract Docker/CI tĩnh.
2. Build image, chạy `id` và xác nhận process không dùng root.
3. Start container; gọi `/health`, payload valid/invalid `/predict`, rồi đọc logs.
4. Stop container kể cả khi smoke lỗi; kiểm CI chỉ chạy offline checks, không deploy AWS.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 15
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 15
```

Kết quả được lưu tại `.artifacts/lab-15-evidence.json`. Trong `result`, bạn sẽ thấy non-root user, health/predict smoke và CI không deploy AWS.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- Có evidence build/run/non-root/health/predict/log/stop; container không còn chạy nền.
- Health degraded và predict 503 khi thiếu artifact; mount read-only giúp `model_loaded=true`.

## Khi mắc kẹt

Đọc build log đầu tiên, kiểm `.dockerignore` và build context. Nếu service lỗi, xem `docker logs` trước rồi vẫn `docker stop`.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.


## Docker smoke thật

Smoke demo Python chỉ kiểm contract tĩnh. Phần dưới cần Docker Desktop/Engine đang chạy:

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

`id` phải cho thấy user khác root. Khi chưa mount artifact, health trả `degraded` và predict trả `503` an
toàn. Với artifact local, mount thư mục read-only, đặt `ML_ROADMAP_ARTIFACT_DIR=/artifacts`, rồi kiểm
`model_loaded=true`. Nếu một bước lỗi, vẫn chạy `docker logs` và `docker stop`; không để container chạy nền.
