# Sau 24 tuần: chọn hướng đi tiếp

Bạn không cần quyết định nghề nghiệp ngay từ tuần đầu. Sau capstone, hãy nhìn lại phần nào khiến bạn muốn đào
sâu thêm. Ba hướng dưới đây đều dùng chung nền tảng của roadmap; khác nhau ở kỹ năng bạn ưu tiên trong 90
ngày tiếp theo.

## Hướng 1 - Model Engineering

Phù hợp nếu bạn thích dữ liệu, thí nghiệm và phân tích lỗi. Chọn một bài toán tabular mới; xây baseline mạnh,
thiết kế ablation, calibration và subgroup analysis. Đích sau 90 ngày: một experiment report có thể tái lập,
không phải một bảng leaderboard dài.

## Hướng 2 - ML Platform / MLOps

Phù hợp nếu bạn thích package, test, CI và vận hành. Mở rộng capstone local bằng data validation, model registry
nhỏ, batch inference, monitoring schema/drift và rollback drill. AWS chỉ là lựa chọn; bạn có thể mô phỏng toàn
bộ pipeline trên máy cá nhân.

## Hướng 3 - Applied Computer Vision

Phù hợp nếu bạn thích ảnh và transfer learning. Chọn dataset nhỏ có license rõ, giữ frozen-backbone baseline,
thử đúng một fine-tuning change, rồi phân tích lỗi theo class và điều kiện ảnh. Dùng Colab Free hoặc Kaggle
Free khi có accelerator; luôn giữ CPU-mini fallback.

## Một lịch 30-60-90 ngày thực tế

- **30 ngày:** chọn một hướng, đọc lại mốc năng lực liên quan, tái chạy capstone từ môi trường sạch.
- **60 ngày:** làm một thay đổi có giả thuyết; thêm test, failure analysis và reproduction note.
- **90 ngày:** demo 5-7 phút, nêu trade-off và điều chưa giải quyết; không cần giữ cloud endpoint hoạt động.

Nếu chưa biết chọn hướng nào, bắt đầu với Model Engineering. Nó buộc bạn hiểu dữ liệu và evaluation trước khi
thêm hạ tầng hoặc model lớn hơn.
