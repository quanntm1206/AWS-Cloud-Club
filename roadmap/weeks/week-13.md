# Tuần 13 - Notebook thành Python package

## Mục tiêu tuần

Tách notebook thành module, config và CLI.

## Vì sao tuần này quan trọng

Notebook giúp khám phá nhanh; package giúp logic có đầu vào rõ, tái sử dụng được và dễ test. ML Engineer cần biết chuyển từ cái đầu sang cái sau.

**Ví dụ gần gũi:** Cell chạy đúng nhờ biến còn trong memory sẽ thất bại khi mở notebook mới; CLI buộc dependency phải hiện rõ.

## Kiến thức cốt lõi

- Notebook để khám phá; production path là module có explicit input/output và CLI.
- Tách data, feature, train, evaluate, artifact I/O; notebook chỉ gọi package.
- Config có schema; CLI trả exit code và error message hữu ích.
- Đặt file/network side effects tại boundary, giữ core functions dễ test.

## Lịch 8-10 giờ

| Hoạt động | Giờ |
|---|---:|
| Đọc và ghi chú | 2 |
| Guided practice | 2 |
| Lab | 3 |
| Assessment/error analysis | 1 |
| Learning log và tự đánh giá | 1 |
| Review/hoàn thiện | 0 |

## Guided practice


1. Di chuyển train logic vào src nhưng giữ parity.
2. Thêm CLI nhận config/output/seed.
3. Chạy cùng config hai lần, so manifest và metric tolerance.

## Lab

**lab-12:** Notebook-to-package refactor. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn chạy cùng logic từ CLI và notebook, không copy hai phiên bản, và có config thay cho global state.

## Tự kiểm tra

1. Logic nào ở notebook/package?
2. Globals phá reproducibility ra sao?
3. CLI contract gồm gì?

## Kết quả hướng tới

installable package; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Giữ một nguồn training logic trong package; notebook và CLI cho kết quả tương đương.
- **Mở rộng:** Thêm một config validation hoặc error message hữu ích cho input sai.

## Lỗi thường gặp

- Copy logic ở hai nơi gây drift.
- Ẩn input trong working directory.

## Khi mắc kẹt

Restart kernel hoặc mở clean shell. Nếu chỉ notebook cũ chạy, lần theo biến ẩn và đường dẫn phụ thuộc working directory.

## Nguồn

Nguồn nên đọc: Python packaging/argparse và project structure references đã liệt kê trong `docs/sources.yml`.
