# Security

Không gửi credential AWS trong issue, notebook hoặc commit. Nếu lộ secret, vô hiệu hóa secret ngay,
kiểm CloudTrail/Billing, rồi báo riêng cho quản trị AWS Cloud Club. Repository chỉ dùng environment
variables và placeholder; CI không deploy AWS.

