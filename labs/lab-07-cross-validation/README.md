# Lab 07 - Đo độ ổn định bằng cross-validation

## Mục tiêu

Một split may mắn có thể làm model trông ổn định hơn thực tế. Cross-validation cho bạn thấy kết quả thay đổi ra sao khi dữ liệu được chia lại có kiểm soát.

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-08.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Đặt pipeline đầy đủ bên trong 3-fold CV; khóa seed và scoring.
2. Ghi từng fold score cùng runtime, sau đó tính mean/std.
3. So với một preprocessing sai nằm ngoài CV và mô tả leakage risk.
4. Vẽ learning curve ở ba train sizes; nêu dấu hiệu bias/variance.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 7
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 7
```

Kết quả được lưu tại `.artifacts/lab-07-evidence.json`. Trong `result`, bạn sẽ thấy fold scores, `cv_mean`, `cv_std`.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- JSON có fold scores, mean và std; mọi transform được fit lại trong từng fold.
- Bạn chọn được Stratified/Group/time split theo quan hệ giữa mẫu, không mặc định shuffle.

## Khi mắc kẹt

Nếu fold dao động mạnh, xem class/group/time distribution của từng fold. Đừng tăng số fold trước khi hiểu nguyên nhân.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
