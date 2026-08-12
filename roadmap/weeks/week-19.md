# Tuần 19 - Fine-tuning tiết kiệm và checkpoint

## Mục tiêu tuần

Checkpoint/resume; fine-tune tiết kiệm.

## Kiến thức cốt lõi

- Train head trước; chỉ unfreeze block cuối nếu validation và runtime budget biện minh.
- Pretrained layers thường dùng learning rate thấp hơn head; so một policy, không sweep free GPU.
- Resumable checkpoint cần model, optimizer, epoch, best metric, config, seed, label mapping.
- Early stopping theo validation với patience; best checkpoint khác last; test không tham gia mỗi epoch.
- Free runtime có thể ngắt/quota đổi; export ZIP bền vững trước khi release session.

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

1. Train tối đa 3-5 epoch, save best validation checkpoint.
2. Dừng-load-resume thêm một epoch.
3. Tạo ZIP self-contained, manifest và checksum ngay trong notebook.

## Lab

**lab-18:** 3-5 epoch, early stopping, export artifact. Môi trường chính: `colab, kaggle`.

## Tự kiểm tra

1. Optimizer state cần vì sao?
2. Best khác last khi nào?
3. Test có tham gia early stopping?

## Kết quả hướng tới

checkpoint artifact; kèm config, command, metric, runtime và một failure/limitation.

## Core vs stretch

- **Core:** hoàn thành mini profile, test và kết quả cốt lõi.
- **Stretch:** thử đúng một cải tiến có giả thuyết; không hyperparameter sweep.

## Lỗi thường gặp

- Chỉ lưu weights nhưng gọi resumable.
- Giữ accelerator session chạy sau lab.

## Nguồn

Xem `docs/sources.yml`; ưu tiên textbook và tài liệu chính thức được ghi trong lab.
