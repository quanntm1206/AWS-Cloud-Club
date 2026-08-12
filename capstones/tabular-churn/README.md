# Capstone A - Dự đoán churn từ đầu đến private Lambda

Capstone này gom toàn bộ đường học cốt lõi: đặt bài toán, xây baseline, chống leakage, chọn threshold, đóng gói
artifact rồi invoke private Lambda trên AWS. Training vẫn chạy local CPU; AWS chỉ nhận model logistic nhỏ.

## Bạn sẽ tạo ra gì?

- Pipeline churn có dummy baseline, preprocessing và logistic regression.
- `model.joblib`, portable model, manifest/checksum, metrics, experiment report và model card.
- Test evidence local; nếu chọn phần AWS, có deployment manifest, cleanup và residual scan.

## File map

- [`configs/mini.yml`](configs/mini.yml): cấu hình chạy nhanh trước.
- [`configs/full.yml`](configs/full.yml): cấu hình thứ hai để so có kiểm soát, không phải sweep.
- [`reports/experiment-report.md`](reports/experiment-report.md): khung ghi câu hỏi, kết quả và negative result.
- [`reports/model-card.md`](reports/model-card.md): intended use, metric, subgroup và giới hạn.
- [`rubric.yml`](rubric.yml): tiêu chí tự đánh giá.
- [`../../labs/lab-20-aws-safe-lifecycle/README.md`](../../labs/lab-20-aws-safe-lifecycle/README.md): đường deploy an toàn.

## Giai đoạn 1 - Chạy local trước

Tạo demo data không chứa dữ liệu cá nhân:

```powershell
.venv\Scripts\python.exe -c "from pathlib import Path; from ml_roadmap.data import make_demo_churn_data; p=Path('.artifacts/churn.csv'); p.parent.mkdir(exist_ok=True); make_demo_churn_data(300,42).to_csv(p,index=False); print(p)"
.venv\Scripts\python.exe -m ml_roadmap.train_tabular --config capstones/tabular-churn/configs/mini.yml --data .artifacts/churn.csv --output .artifacts/churn-model
```

```bash
.venv/bin/python -c "from pathlib import Path; from ml_roadmap.data import make_demo_churn_data; p=Path('.artifacts/churn.csv'); p.parent.mkdir(exist_ok=True); make_demo_churn_data(300,42).to_csv(p,index=False); print(p)"
.venv/bin/python -m ml_roadmap.train_tabular --config capstones/tabular-churn/configs/mini.yml --data .artifacts/churn.csv --output .artifacts/churn-model
```

Mở metrics và manifest. Xác nhận model vượt dummy theo metric đã chọn, threshold đến từ validation, artifact
load lại được. Test set chỉ được dùng sau khi candidate và threshold đã khóa.

## Giai đoạn 2 - Báo cáo và tự kiểm

1. Điền experiment report: câu hỏi, schema/license, split, baseline, candidate, threshold, test và failure slices.
2. Điền model card: intended/out-of-scope use, data, metrics, privacy, operational limit và rollback signal.
3. Chạy test/check từ clean shell; lưu command, environment và limitation cục bộ.
4. Chấm theo `rubric.yml`. Gate bắt buộc: không leakage, không secret, artifact tái lập.

## Giai đoạn 3 - AWS tùy điều kiện tài khoản

Đọc toàn bộ lab 20 trước khi chạy. Quy trình duy nhất là private invoke:
`Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit`.
Không bật public HTTP API. Nếu plan/credit/Region hoặc estimate chưa rõ, dừng ở local capstone; năng lực ML cốt
lõi vẫn hoàn thành. Sau deploy, dù verify thành công hay thất bại, cleanup ngay trong cùng phiên.

## Khi nào xem như hoàn thành?

- Local pipeline chạy lại từ clean shell, model vượt baseline và mọi quyết định chọn model dùng validation.
- Artifact checksum hợp lệ; prediction trước/sau load khớp trong tolerance.
- Report và model card nêu ít nhất một failure, một giới hạn và một next experiment.
- Nếu đã dùng AWS: private invoke có valid/invalid event, zero known residual sau cleanup và kiểm billing lại.

## Khi mắc kẹt

- **Không có `.artifacts/churn.csv`:** chạy lệnh tạo demo data trước, từ repository root.
- **Config bị từ chối:** kiểm key hợp lệ trong `src/ml_roadmap/config.py`; không tự đoán schema.
- **Metric không vượt baseline:** kiểm split, target, leakage và data signal trước khi đổi model.
- **Artifact load lỗi:** đối chiếu checksum, feature order, dependency và đúng output directory.
- **AWS bước bất kỳ lỗi:** dừng deploy, chạy cleanup/residual scan; không sửa bằng cách mở thêm resource.

Mọi kết quả được lưu local để tự đánh giá; không xuất bản hoặc gửi cho ai.
