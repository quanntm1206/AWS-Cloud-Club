# Mốc năng lực 06 - Tuần 24

## Mục tiêu

Tự đánh giá capstone end-to-end, khả năng trình bày và an toàn chi phí AWS.

## Bạn đã đạt mốc nếu

- Demo từ input đến prediction bằng local fallback; AWS chỉ dùng private Lambda trong phiên có kiểm soát.
- Manifest nối model version, schema, threshold, checksum và source run; handler từ chối contract sai.
- Thực hiện đủ cost check, preflight, deploy, verify, cleanup, residual scan và cost audit.
- Trình bày được problem, constraint, baseline, quyết định, failure, limitation và cách tái lập trong 5-7 phút.

## Minh chứng đạt mốc

- Capstone README, architecture note, model card, reproduction command và demo outline lưu cục bộ.
- Test report cho valid/invalid inference cùng local/portable parity.
- Cost manifest, deployment manifest, cleanup output và zero-residual report; không lưu account ID hay raw billing.
- Retrospective ghi một incident drill hoặc điều sẽ làm khác nếu triển khai thật.

## Rubric

| Tiêu chí | Điểm |
|---|---:|
| Tích hợp end-to-end | 25 |
| Kiểm thử và khả năng tái lập | 25 |
| AWS cost safety và cleanup | 30 |
| Demo và retrospective | 20 |

Điểm đạt: 75/100. Gate: không leakage/secret, private-only, mini run tái lập; cleanup và residual scan phải sạch. Nếu AWS không an toàn hoặc credit/plan không rõ, dùng local fallback và chưa chấm phần AWS đã triển khai.

## Câu hỏi tự nhìn lại

- Bằng chứng nào cho thấy hệ thống sạch tài nguyên, thay vì chỉ thấy lệnh cleanup trả về thành công?
- Nếu billing cập nhật trễ, bạn sẽ kiểm lại khi nào và ghi nhận ra sao?
- Quyết định kỹ thuật nào thể hiện rõ nhất tư duy ML Engineer của bạn?
