# Tuần 18 - CNN và transfer learning

## Mục tiêu tuần

Hiểu CNN và transfer learning.

## Kiến thức cốt lõi

- Convolution học kernel cục bộ chia sẻ weight; stride/padding đổi spatial size, downsampling giảm compute.
- Transfer learning dùng pretrained backbone và thay head; frozen-backbone chỉ train head nên nhẹ hơn full fine-tune.
- Input normalization phải khớp pretrained weights; train augmentation khác validation transform deterministic.
- Notebook có CPU-mini và FakeData khi GPU/internet thiếu; FakeData chỉ smoke pipeline, không chứng minh accuracy.

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

1. Tính conv output size và in shape qua model.
2. Freeze backbone, xác nhận chỉ head trainable.
3. Chạy CIFAR10 subset; ép FakeData fallback rồi ghi limitation.

## Lab

**lab-17:** Frozen-backbone baseline trên một free runtime. Môi trường chính: `colab, kaggle`.

## Tự kiểm tra

1. Frozen backbone giảm compute vì sao?
2. Normalization sai ảnh hưởng gì?
3. FakeData chứng minh được gì?

## Kết quả hướng tới

CV baseline; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Báo transfer learning dù pretrained weights không tải.
- Báo FakeData accuracy như chất lượng thật.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
