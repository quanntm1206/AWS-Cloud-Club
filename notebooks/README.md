# Chạy notebook miễn phí

Phần tabular chạy tốt trên local CPU. Từ tuần 18, bạn chọn **một** trong hai nền tảng miễn phí cho Computer
Vision; không cần chạy cả Colab lẫn Kaggle và không cần mua gói trả phí.

## Quick start trong 5 phút

| Nền tảng | Notebook |
|---|---|
| Colab Free | [`colab/cv_transfer_learning_colab.ipynb`](colab/cv_transfer_learning_colab.ipynb) |
| Kaggle Free | [`kaggle/cv_transfer_learning_kaggle.ipynb`](kaggle/cv_transfer_learning_kaggle.ipynb) |
| Kiểm môi trường dùng chung | [`shared/00_environment_check.ipynb`](shared/00_environment_check.ipynb) |

1. Mở hoặc upload đúng notebook cho nền tảng đã chọn.
2. Chạy `Environment check`; đọc `device` và `profile` được in ra.
3. Giữ `cpu-mini` cho lần đầu. Profile này vẫn cố dùng pretrained ResNet18, nhưng FakeData chỉ là smoke
   test nên không chứng minh model có chất lượng.
4. Nếu GPU có sẵn, chạy lại với `gpu-free`; notebook dùng CIFAR10 subset, pretrained weights và tối đa 5 epoch.
5. Chờ cell export tạo `artifacts.zip`, tải file này về máy **trước** khi đóng runtime.
6. Giải phóng runtime/accelerator ngay khi xong.

Notebook đã gồm environment check, seed/config, train augmentation riêng, validation deterministic,
frozen-backbone baseline, training, evaluation, error analysis, best/last checkpoint, manifest và artifact
export. Đừng chạy cell lệch thứ tự ở lần đầu.

Cell evaluation xuất accuracy, macro/weighted F1, per-class metrics, confusion matrix dạng count và normalize
theo true class. Notebook chọn tối đa 20 lỗi theo confidence; mở từng ảnh rồi đổi `error_type='unreviewed'`
thành nhóm lỗi bạn quan sát được trước khi viết model card. Không đoán taxonomy tự động từ nhãn.

## Nếu phiên chạy bị ngắt

Mở runtime mới, chạy lại phần environment/config, upload `last_checkpoint.pt` hoặc `artifacts.zip`, đặt
`RESUME=True`, rồi chạy cell training. `RUN_EPOCHS` là số epoch chạy **thêm** trong phiên hiện tại: CPU-mini
mặc định train một epoch; phiên resume chạy thêm một epoch. Notebook lưu `last_checkpoint.pt` sau mọi epoch để
tiếp tục và chỉ dùng `best_checkpoint.pt` để đánh giá. Resume state cần model, optimizer, epoch, best metric,
config, seed và label mapping. Chỉ có model weights thì chưa đủ để resume đúng optimizer.

Đặt file upload ở thư mục làm việc của notebook với tên `last_checkpoint.pt` hoặc `artifacts.zip`. Khi
`RESUME=True`, notebook tự copy/giải nén vào `artifacts/`; nếu không tìm thấy checkpoint, cell dừng bằng lỗi rõ
ràng thay vì âm thầm train lại từ epoch 0.

## Lỗi thường gặp

- **Không có GPU:** tiếp tục với `cpu-mini`; bạn vẫn thực hành frozen pretrained backbone trên CPU. Muốn có
  evidence chất lượng, cần chạy thêm với dataset thật khi runtime cho phép.
- **CIFAR10 không tải được:** notebook chuyển sang FakeData. Ghi rõ đây là pipeline smoke, không báo accuracy.
- **Pretrained weights không tải được:** random-weight fallback chỉ kiểm tra luồng chạy, chưa đạt gate transfer
  learning. Thử lại khi có internet hoặc weights đã được cache; không đổi tên kết quả thành transfer learning.
- **Hết memory:** giảm `BATCH_SIZE`, `IMAGE_SIZE` hoặc `SAMPLES`; không tăng runtime trả phí.
- **Import torch/torchvision lỗi:** dùng cặp phiên bản tương thích của runtime rồi restart; không cài lặp trong mọi cell.
- **Mất file sau disconnect:** runtime là máy tạm. Luôn download `artifacts.zip` trước khi kết thúc phiên.

Hướng dẫn theo nền tảng: [Colab Free](../docs/source-notes/colab-free.md) và
[Kaggle Free](../docs/source-notes/kaggle-notebooks.md).
