# Mốc năng lực 03 - Tuần 12

## Mục tiêu

Tự đánh giá một dự án tabular hoàn chỉnh, từ dữ liệu đến phân tích lỗi.

## Bạn đã đạt mốc nếu

- Pipeline xử lý schema, missing/category và model trong cùng contract chống leakage.
- Baseline và các candidate dùng cùng split, seed, metric và runtime budget.
- Feature engineering có giả thuyết; ablation chỉ thay một quyết định mỗi lần.
- Error analysis dẫn tới hành động tiếp theo, đồng thời nêu subgroup hoặc failure mode còn yếu.

## Minh chứng đạt mốc

- Data/model card ngắn, split manifest, pipeline config và reproduction command lưu cục bộ.
- Bảng baseline/candidate/ablation, gồm cả một kết quả âm có ý nghĩa.
- Metric tổng, metric subgroup phù hợp và danh sách failure cases đã phân nhóm.
- Artifact manifest cùng test schema, prediction parity hoặc invariant quan trọng.

## Rubric

| Tiêu chí | Điểm |
|---|---:|
| Pipeline và data contract | 30 |
| Baseline và thí nghiệm có kiểm soát | 25 |
| Error analysis | 25 |
| Tái lập và giao tiếp | 20 |

Điểm đạt: 70/100. Gate: không leakage, không secret, mini run tái lập; test cuối không bị dùng để sửa quyết định.

## Câu hỏi tự nhìn lại

- Candidate tốt hơn baseline vì tín hiệu thật hay vì quy trình đánh giá thay đổi?
- Failure cluster nào đáng xử lý trước, dựa trên tác động nào?
- Nếu có thêm hai giờ, thí nghiệm nhỏ nhất giúp giảm bất định là gì?
