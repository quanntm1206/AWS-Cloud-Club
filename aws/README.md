# AWS cost-safe capstone

## Trước khi bắt đầu

1. Dùng AWS Free Plan nếu đủ điều kiện; không nâng cấp Paid Plan chỉ cho core lab.
2. Xác nhận đúng account và `us-east-1`; kiểm credit/plan trong Billing console.
3. Tạo AWS Budget actual + forecast alerts. **Budget không phải hard cap; billing có thể trễ.**
4. Đọc `cost-policy.yml`; kiểm artifact dưới 200 MB.
5. Không tạo GPU, EC2, NAT Gateway, SageMaker notebook/training/endpoint.

## Lifecycle bắt buộc

```text
Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit
```

Private Lambda invocation là core. `EnablePublicApi=false` mặc định. Nếu bật HTTP API, tạo và xóa trong
cùng phiên lab. Cleanup chỉ xóa stack exact-name có prefix `ml-roadmap-`; CloudFormation xử lý resource
dependency. Script không quét/xóa tài nguyên khác.

## Emergency cleanup

1. Dừng; xác nhận AWS account, Region và project ID.
2. Export artifact/log cần giữ.
3. Chạy cleanup dry-run, đọc exact stack/resource names.
4. Chạy execute với exact project ID.
5. Chạy residual scan; mở Billing/Cost Explorer/Free Tier widget để kiểm tra.

