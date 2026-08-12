# Lab 02 - Lập hồ sơ chất lượng dữ liệu trước khi vẽ biểu đồ

## Mục tiêu

EDA tốt bắt đầu bằng câu hỏi “mỗi hàng có đáng tin không?”, không phải “vẽ biểu đồ nào đẹp?”. Bạn sẽ tạo một bản kiểm kê đủ để quyết định dữ liệu cần sửa gì trước modeling.

## Trước khi bắt đầu

Đọc `roadmap/weeks/week-03.md`, chạy từ repository root và tạo chỗ lưu evidence cục bộ. Không đưa
credential, dữ liệu cá nhân hoặc artifact lớn vào Git.

## Các bước thực hiện

1. Lập bảng schema, missing, duplicate, range và phân bố target.
2. Chọn một khóa nghiệp vụ, kiểm hàng trùng và mô tả hậu quả nếu để nguyên.
3. So churn rate tổng thể với ít nhất một nhóm; tách quan sát khỏi lời giải thích.
4. Viết ba ghi chú theo mẫu evidence - hypothesis - next check.

## Chạy smoke demo

PowerShell:

```powershell
.venv\Scripts\python.exe scripts/run_lab.py --lab 2
```

Bash (macOS/Linux):

```bash
.venv/bin/python scripts/run_lab.py --lab 2
```

Kết quả được lưu tại `.artifacts/lab-02-evidence.json`. Trong `result`, bạn sẽ thấy missing count, duplicate count, churn rate và mean theo target.
`status=starter-example-completed` chỉ xác nhận code mẫu chạy; **không** có nghĩa toàn bộ acceptance đã đạt.

## Khi nào xem như hoàn thành?

- Báo cáo có missing count, duplicate count, target rate và một so sánh theo nhóm.
- Không xóa outlier/missing chỉ vì biểu đồ; mọi quyết định cleaning có lý do và tác động dự kiến.

## Khi mắc kẹt

Quay về năm câu hỏi: một hàng là gì, key là gì, target là gì, giá trị nào không thể có, dữ liệu được ghi vào lúc nào.

Sau khi tự dự đoán output, đối chiếu [`expected/README.md`](expected/README.md) và ghi lại điều đã học ở local.
