# Tuần 14 - Testing cho hệ thống ML

## Mục tiêu tuần

Test schema, transform, model và artifact.

## Vì sao tuần này quan trọng

Hệ thống ML hỏng không chỉ vì model kém. Schema đổi, category lạ hoặc artifact lỗi thường xuất hiện trước khi metric tụt.

**Ví dụ gần gũi:** Một API nhận tuổi dạng chuỗi nên bị từ chối rõ ràng, thay vì âm thầm biến đổi rồi trả prediction khó tin.

## Kiến thức cốt lõi

- ML tests bao phủ schema, transforms, determinism, metric sanity, reload và API boundary.
- Unit dùng synthetic nhỏ; integration chạy pipeline ngắn.
- Negative cases: thiếu cột, sai dtype, unseen category, NaN/Inf, empty input group, artifact hỏng.
- Metric assertion dùng threshold/tolerance có lý do, không khóa số stochastic mong manh.

## Từ khóa tuần này

**Thuật ngữ mới hoặc trọng tâm:** `data contract`, `parity`

**Ôn lại:** `schema`, `pipeline`, `artifact`, `reproducibility`

**Áp dụng:** Viết `data contract` cho `schema`; test `parity` qua fit, save, load và predict của `pipeline` cùng `artifact`, gồm một sample sai và tolerance đã nêu cho reproducibility.

## Giải thích khái niệm

### Contract tại boundary

**Cách hình dung:** `data contract`: Quy ước máy đọc được về schema, phạm vi và lỗi của dữ liệu. Cả producer lẫn consumer đều có thể validate cùng contract tại boundary.

**Vì sao quan trọng:** Data contract biến kỳ vọng schema thành check tại boundary trước khi input xấu tới model.

**Ví dụ xuyên suốt:** `data contract`: Request thiếu field tenure bị từ chối trước khi tới model.

**Dễ nhầm với:** Data contract quản data; API contract quản request và response của service.

**Tự kiểm tra:** Input không hợp lệ nào phải bị `data contract` từ chối trước khi model chạy?

### Training-serving parity

**Cách hình dung:** `parity`: Mức nhất quán giữa hai cách chạy được kỳ vọng cho cùng input. Tolerance phù hợp tùy output là label, probability hay floating-point array.

**Vì sao quan trọng:** Parity evidence cho thấy training và serving dùng cùng feature order, transformation và decision rule.

**Ví dụ xuyên suốt:** `parity`: Prediction trước và sau save/load khớp trong tolerance đã đặt.

**Dễ nhầm với:** Parity là hành vi khớp đủ mức yêu cầu, không nhất thiết file giống từng byte.

**Tự kiểm tra:** Tolerance nào chứng minh `parity` giữa training path và serving path?

## Kết nối kiến thức cũ

`schema` trở thành data contract thực thi được quanh `pipeline` và `artifact`. Prediction khớp trong tolerance đã nêu chứng minh `reproducibility` qua boundary save và load.

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


1. Test valid/invalid schema và unseen category.
2. Fit-save-load-predict, kiểm parity.
3. Kiểm model vượt dummy trên data có signal.

## Lab

**lab-13:** ML tests với edge cases. Môi trường chính: `local`.

## Dấu hiệu bạn đã hiểu

Bạn có test cho happy path lẫn missing, wrong dtype, unseen category, NaN/Inf và save-load parity.

## Tự kiểm tra

1. Nguồn randomness nào cần seed?
2. Vì sao exact metric dễ flaky?
3. Test nào bắt train/serve skew?

## Kết quả hướng tới

test evidence; lưu kèm lệnh đã chạy, cấu hình, metric, thời gian chạy và một điều còn hạn chế.

## Core vs stretch

- **Cốt lõi:** Test schema, negative cases, reload parity và model-vượt-dummy trên data synthetic nhỏ.
- **Mở rộng:** Thêm test artifact checksum hỏng hoặc input group rỗng; tránh exact metric dễ flaky.

## Lỗi thường gặp

- Chỉ test happy path.
- automated checks dùng production dataset lớn/nhạy cảm.

## Khi mắc kẹt

Dùng synthetic data nhỏ và sửa một test mỗi lần. Tránh khóa exact metric nếu thuật toán có ngẫu nhiên.

## Nguồn

Nguồn nên đọc: pytest documentation và scikit-learn guidance về common pitfalls/reproducibility.
