# Danh mục lab

Repo có **21 lab**: lab 00 giúp kiểm tra môi trường; lab 01-19 chạy offline hoặc bằng free compute; lab 20
là chuỗi AWS có guardrail và được dùng lại trong tuần 21-24.

## Cách làm một lab

1. Đọc tuần tương ứng để biết vì sao bài này xuất hiện.
2. Chạy command trong README để xem **smoke demo** và dạng output.
3. Làm nhiệm vụ thực hành được mô tả; code trung tâm là ví dụ tham khảo, không phải scaffold cần điền.
4. Đối chiếu `expected/README.md`, ghi kết quả và một lỗi có ý nghĩa vào learning log cục bộ.
5. Chỉ xem như hoàn thành khi bạn giải thích được kết quả, không chỉ khi command exit 0.

`status=starter-example-completed` chỉ có nghĩa demo chạy xong. Nó không chứng minh bạn đã đạt mục tiêu học tập.
Không commit hoặc gửi evidence cho ai; tránh secret, dữ liệu cá nhân và output lớn.

| Lab | Chủ đề | Tuần |
|---|---|---:|
| [00 - Kiểm tra môi trường và khả năng tái lập](lab-00-environment-and-reproducibility/README.md) | environment and reproducibility | 1 |
| [01 - Đọc shape bằng NumPy và đối chiếu vectorization](lab-01-numpy-vectorization/README.md) | numpy vectorization | 2 |
| [02 - Lập hồ sơ chất lượng dữ liệu trước khi vẽ biểu đồ](lab-02-pandas-eda/README.md) | pandas eda | 3 |
| [03 - Tự kiểm gradient của linear regression](lab-03-linear-regression-from-scratch/README.md) | linear regression from scratch | 4 |
| [04 - So dummy baseline với logistic regression](lab-04-first-classifier/README.md) | first classifier | 5 |
| [05 - Dựng preprocessing không nhìn test](lab-05-leakage-safe-preprocessing/README.md) | leakage safe preprocessing | 6 |
| [06 - Chọn metric và threshold theo chi phí lỗi](lab-06-metrics-and-threshold/README.md) | metrics and threshold | 7 |
| [07 - Đo độ ổn định bằng cross-validation](lab-07-cross-validation/README.md) | cross validation | 8 |
| [08 - So sánh tree ensembles công bằng](lab-08-tree-ensemble-comparison/README.md) | tree ensemble comparison | 9 |
| [09 - Kiểm một feature bằng ablation](lab-09-feature-ablation/README.md) | feature ablation | 10 |
| [10 - Biến lỗi model thành việc cần làm tiếp](lab-10-error-analysis/README.md) | error analysis | 11 |
| [11 - Ghép pipeline tabular thành mini-project](lab-11-tabular-mini-project/README.md) | tabular mini project | 12 |
| [12 - Tách logic khỏi notebook thành config và CLI](lab-12-notebook-to-package/README.md) | notebook to package | 13 |
| [13 - Viết test cho dữ liệu, model và artifact](lab-13-ml-testing/README.md) | ml testing | 14 |
| [14 - Kiểm contract của inference API local](lab-14-local-inference-api/README.md) | local inference api | 15 |
| [15 - Đóng gói service và chạy CI smoke](lab-15-docker-and-ci/README.md) | docker and ci | 16 |
| [16 - Nhìn rõ tensor, gradient và device](lab-16-device-aware-mlp/README.md) | device aware mlp | 17 |
| [17 - Chạy transfer learning thật trên free runtime](lab-17-transfer-learning/README.md) | transfer learning | 18 |
| [18 - Lưu và resume checkpoint đúng nghĩa](lab-18-checkpoint-and-resume/README.md) | checkpoint and resume | 19 |
| [19 - Đánh giá CV theo từng class và failure](lab-19-cv-error-analysis/README.md) | cv error analysis | 20 |

Lab 20: [AWS safe lifecycle](lab-20-aws-safe-lifecycle/README.md).
