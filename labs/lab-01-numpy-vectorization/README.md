# Lab 01 - Đọc shape bằng NumPy và đối chiếu vectorization

## Mục tiêu

Phép nhân ma trận chỉ hữu ích khi bạn biết mỗi chiều đại diện cho gì. Lab này giúp bạn nối công thức `X @ w` với dữ liệu nhiều hàng, thay vì học vectorization như một mẹo viết code ngắn.

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-02.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Viết shape dự kiến của `X`, `w` và `X @ w` trước khi chạy.
2. Tính score của một hàng bằng tay, sau đó chạy loop và phép nhân vectorized.
3. Dùng `np.allclose` để đối chiếu; cố ý đổi một shape hoặc axis và đọc lỗi.
4. Tự tính MAE/standardization trên mảng nhỏ, kiểm zero variance hoặc input rỗng.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 1
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 1
```

Kết quả được lưu tại `.artifacts/lab-01-evidence.json`. Trong `result`, bạn sẽ thấy `vectorization_matches_loop=true` và năm score đầu.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- `vectorization_matches_loop=true`; một hàng tính tay khớp output trong tolerance.
- Bạn giải thích được broadcasting nào hợp lệ và vì sao `reshape` tùy tiện có thể che lỗi nghiệp vụ.

## Khi mắc kẹt

Thu nhỏ còn hai hàng, in `shape` và gắn tên cho từng axis. Đừng thêm `reshape` cho tới khi nói được chiều mới có ý nghĩa gì.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
