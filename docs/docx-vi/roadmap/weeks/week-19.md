# Tuần 19 - Fine-tuning tiết kiệm và checkpoint

## Mục tiêu tuần

Checkpoint/resume; fine-tune tiết kiệm.

## Vì sao tuần này quan trọng

Free runtime có thể ngắt bất cứ lúc nào. Checkpoint tốt biến một lần ngắt thành gián đoạn nhỏ thay vì mất toàn bộ buổi train.

**Ví dụ gần gũi:** Best checkpoint giữ epoch validation tốt nhất; last checkpoint chỉ phản ánh lần cập nhật gần nhất và có thể kém hơn.

## Kiến thức cốt lõi

- Train head trước; chỉ unfreeze block cuối nếu validation và runtime budget biện minh.
- Pretrained layers thường dùng learning rate thấp hơn head; so một policy, không sweep free GPU.
- Resumable checkpoint cần model, optimizer, epoch, best metric, config, seed, label mapping.
- Early stopping theo validation với patience; best checkpoint khác last; test không tham gia mỗi epoch.
- Free runtime có thể ngắt/quota đổi; export ZIP bền vững trước khi release session.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `fine-tuning`, `checkpoint`, `early stopping`

**Ôn lại:** `transfer learning`, `freeze`, `optimizer`, `epoch`, `validation set`

**Áp dụng:** Bắt đầu từ frozen `transfer learning` baseline, sau đó mới cân nhắc `fine-tuning`; lưu `checkpoint` gồm optimizer và epoch state, dùng `early stopping` trên `validation set`, rồi resume một lần để kiểm state đã lưu.

## Giải thích khái niệm

### Checkpoint khi fine-tuning

**Cách hình dung:** `fine-tuning`: Tiếp tục train một phần model pretrained bằng learning rate nhỏ cho bài toán mới. Nó thường diễn ra sau frozen-head training và dùng learning rate thấp hơn cho layer được unfreeze. `checkpoint`: Trạng thái training đã lưu để có thể tiếp tục sau khi runtime bị ngắt. Nó thường chứa model parameter, optimizer state, epoch number và training history.

**Vì sao quan trọng:** Checkpoint giữ model và optimizer state để quyết định fine-tuning có thể tái lập hoặc resume an toàn.

**Ví dụ xuyên suốt:** `fine-tuning`: Unfreeze layer4 sau frozen-head baseline. `checkpoint`: Last checkpoint chứa model, optimizer, epoch và history.

**Dễ nhầm với:** Fine-tuning cập nhật pretrained layer; frozen-head training giữ nguyên chúng. Checkpoint có thể resume training; final artifact được chuẩn bị cho evaluation hoặc serving.

**Tự kiểm tra:** `checkpoint` phải giữ state nào để resume chính xác run `fine-tuning`?

### Early stopping

**Cách hình dung:** `early stopping`: Dừng training khi validation không cải thiện qua số epoch đã định. Setting patience quy định số epoch không cải thiện được chấp nhận.

**Vì sao quan trọng:** Early stopping dùng validation evidence để dừng trước khi epoch bổ sung chủ yếu ghi nhớ training noise.

**Ví dụ xuyên suốt:** `early stopping`: Dừng khi validation loss không cải thiện trong hai epoch.

**Dễ nhầm với:** Early stopping là quy tắc training, không bảo đảm loại bỏ mọi overfitting.

**Tự kiểm tra:** Validation signal và patience rule nào kích hoạt `early stopping`?

## Kết nối kiến thức cũ

Frozen `transfer learning` baseline và policy `freeze` vẫn là mốc so sánh. `optimizer` cùng `epoch` state được restore, kết hợp rule không đổi trên `validation set`, cho biết fine-tuning có thật sự cải thiện model hay không.

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

## Dấu hiệu bạn đã hiểu

Bạn lưu đủ model, optimizer, epoch, config và label mapping; dừng rồi resume thêm một epoch thành công.

## Tự kiểm tra

1. Optimizer state cần vì sao?
2. Best khác last khi nào?
3. Test có tham gia early stopping?

## Kết quả hướng tới

checkpoint artifact; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Lưu checkpoint đủ state, chủ động dừng/resume và export artifact trước khi đóng runtime.
- **Mở rộng:** Unfreeze block cuối chỉ khi validation/runtime có lý do; dùng learning rate thấp hơn head.

## Lỗi thường gặp

- Chỉ lưu weights nhưng gọi resumable.
- Giữ accelerator session chạy sau lab.

## Khi mắc kẹt

Giảm data và epoch trước. Nếu resume sai, so architecture, label mapping và optimizer state thay vì chỉ load weights.

## Nguồn

Nguồn nên đọc: PyTorch saving/loading checkpoint tutorial và notebook contract trong repo.
