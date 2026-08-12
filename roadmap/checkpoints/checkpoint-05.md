# Mốc năng lực 05 - Tuần 20

## Mục tiêu

Tự đánh giá Computer Vision với transfer learning và giới hạn compute miễn phí.

## Bạn đã đạt mốc nếu

- Dùng đúng pretrained weights/normalization, có frozen-backbone baseline và CPU mini fallback. Nếu pretrained
  weights không tải được, random-weight run chỉ là execution smoke và chưa đạt gate transfer learning.
- Checkpoint lưu đủ model, optimizer, epoch, best metric, history, config, seed và class mapping.
- Resume tiếp tục từ epoch đúng; không âm thầm train lại từ đầu khi runtime bị ngắt.
- Báo macro/per-class metric, confusion matrix và phân nhóm failure cases thay vì chỉ accuracy.

## Minh chứng đạt mốc

- Notebook Colab hoặc Kaggle chạy được với device check, mini profile và lệnh/config tái lập lưu cục bộ.
- Checkpoint manifest, checksum và log chứng minh resume path hoạt động.
- Bảng frozen/unfreeze có runtime, metric và giới hạn quota/compute.
- Confusion matrix, per-class report và tối đa 20 failure examples; nếu ít hơn, lưu toàn bộ và ghi rõ.

## Rubric

| Tiêu chí | Điểm |
|---|---:|
| Transfer learning đúng | 25 |
| Checkpoint và resume | 25 |
| Đánh giá per-class | 30 |
| Failure analysis và giới hạn | 20 |

Điểm đạt: 70/100. Gate: pretrained weights và normalization đúng, best/last checkpoint load được, CPU mini path
tái lập, không có token trong notebook/output. FakeData có thể chứng minh pipeline; evidence chất lượng cần dữ liệu thật.

## Câu hỏi tự nhìn lại

- Cải thiện metric có đáng với runtime và quota đã dùng không?
- Class hoặc điều kiện ảnh nào model thường nhầm nhất, vì sao?
- Kết quả nào chỉ là execution smoke, chưa chứng minh chất lượng model?
