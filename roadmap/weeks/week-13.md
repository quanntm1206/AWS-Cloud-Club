# Tuần 13 - Notebook thành Python package

## Mục tiêu tuần

Tách notebook thành module, config và CLI.

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

## Tự kiểm tra

1. Logic nào ở notebook/package?
2. Globals phá reproducibility ra sao?
3. CLI contract gồm gì?

## Kết quả hướng tới

installable package; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Copy logic ở hai nơi gây drift.
- Ẩn input trong working directory.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
