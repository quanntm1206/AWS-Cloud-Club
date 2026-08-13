# Lab 13 - Viết test cho dữ liệu, model và artifact

## Mục tiêu

Test ML cần kiểm dữ liệu và artifact, không chỉ function trả đúng type. Lab này tập trung vào những lỗi thường xuất hiện sau khi model đã được đóng gói.

## Thuật ngữ trong lab

**Thuật ngữ mới:** `data contract`, `parity`

**Ôn lại:** `schema`, `pipeline`, `artifact`, `reproducibility`

**Áp dụng trong lab:** Viết `data contract` cho schema; test `parity` fit-save-load-predict của pipeline/artifact, negative case cho sample sai và tolerance cho reproducibility.

**Tự giải thích:** Data contract khác schema thuần túy thế nào; parity bảo vệ artifact ra sao?

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-14.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Test schema đúng và các case thiếu cột, sai dtype, NaN/Inf, empty input group.
2. Đưa unseen category qua đúng preprocessing pipeline.
3. Fit-save-load-predict rồi kiểm parity trong tolerance.
4. Tạo data synthetic có signal, xác nhận model vượt dummy bằng gate hợp lý.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 13
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 13
```

Kết quả được lưu tại `.artifacts/lab-13-evidence.json`. Trong `result`, bạn sẽ thấy `artifact_reload_parity=true` cùng negative cases tự bổ sung.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- `artifact_reload_parity=true`; negative cases tự bổ sung đều cho lỗi có chủ đích.
- Test nhỏ, deterministic; metric assertion có tolerance thay vì khóa số stochastic mong manh.

## Khi mắc kẹt

Chạy từng test riêng với synthetic data nhỏ. Nếu flaky, liệt kê nguồn randomness và khóa seed trước khi nới assertion.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
