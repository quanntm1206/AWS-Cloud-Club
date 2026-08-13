# Lab 03 - Tự kiểm gradient của linear regression

## Mục tiêu

Thay vì tin gradient vì loss có giảm, bạn sẽ kiểm nó bằng một phép xấp xỉ độc lập. Đây là thói quen debug quan trọng trước khi mô hình trở nên lớn hơn.

## Thuật ngữ trong lab

**Thuật ngữ mới:** `prediction`, `loss`, `gradient`, `learning rate`

**Ôn lại:** `feature`, `label / target`, `data validation`

**Áp dụng trong lab:** Tính `prediction`, `loss`, `gradient` và cập nhật parameter bằng `learning rate`; giữ feature, label / target và ghi lỗi data validation nếu input sai.

**Tự giải thích:** Loss, gradient và learning rate liên hệ thế nào khi parameter được cập nhật?

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-04.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc file kết quả lớn vào Git.

## Các bước thực hiện

1. Tính prediction, MSE và analytic gradient trên bốn điểm bằng tay.
2. Cài gradient descent; ghi loss ở từng bước với learning rate nhỏ.
3. Tính central finite difference qua vài `epsilon`, so với analytic gradient.
4. Thử learning rate quá lớn, mô tả đường loss rồi khôi phục cấu hình ổn định.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 3
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 3
```

Kết quả được lưu tại `.artifacts/lab-03-evidence.json`. Trong `result`, bạn sẽ thấy analytic gradient, finite-difference gradient và `gradient_check=true`.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- Analytic và finite-difference gradient gần nhau trong tolerance; `gradient_check=true`.
- Bạn phân biệt được convergence chậm, divergence và lỗi công thức gradient.

## Khi mắc kẹt

Kiểm dấu, hệ số `2/n` và việc cập nhật parameter sau khi tính gradient. Với finite difference, thử `epsilon` ở nhiều bậc độ lớn.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
