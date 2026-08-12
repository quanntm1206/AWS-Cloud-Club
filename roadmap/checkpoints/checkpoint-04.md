# Mốc năng lực 04 - Tuần 16

## Mục tiêu

Tự đánh giá khả năng biến notebook thành phần mềm ML có thể kiểm thử và vận hành.

## Bạn đã đạt mốc nếu

- Training/evaluation tách khỏi notebook thành module, config và CLI chạy từ môi trường sạch.
- Test bao phủ schema, transform, model artifact cùng boundary hợp lệ/không hợp lệ của inference API.
- Artifact gắn model version, checksum, config, metric và source run.
- CI chạy lint/test trên mini profile; Docker chỉ là phần mở rộng nếu máy không hỗ trợ.

## Minh chứng đạt mốc

- Package tree, quickstart và command train/evaluate/serve lưu cục bộ.
- Test report có ít nhất một negative case cho schema hoặc API contract.
- Artifact manifest và parity check giữa đường batch với inference.
- CI log hoặc local CI-equivalent; ghi rõ giới hạn môi trường/Docker nếu chưa chạy được.

## Rubric

| Tiêu chí | Điểm |
|---|---:|
| Cấu trúc package và CLI | 25 |
| Test và contract inference | 30 |
| CI và artifact versioning | 25 |
| Vận hành và giới hạn | 20 |

Điểm đạt: 70/100. Gate: không secret, mini run tái lập, malformed input trả lỗi có contract thay vì làm tiến trình crash.

## Câu hỏi tự nhìn lại

- Một người khác cần biết ít nhất những gì để chạy lại artifact?
- Test nào bảo vệ ranh giới nguy hiểm nhất của hệ thống?
- Notebook còn giữ trách nhiệm nào nên chuyển vào package?
