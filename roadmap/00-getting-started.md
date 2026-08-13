# Bắt đầu roadmap

Bạn không cần chuẩn bị một chiếc máy mạnh. Nếu đã quen với biến, hàm, vòng lặp và cấu trúc dữ liệu, bạn có
đủ nền để bắt đầu. Toán sẽ được học đúng lúc nó xuất hiện trong bài, thay vì trở thành một cánh cửa phải vượt
qua trước.

## Trước buổi học đầu tiên

- Python 3.11-3.13; máy có tối thiểu 8 GB RAM. CPU đủ cho đường học cốt lõi.
- Biết chạy lệnh trong terminal và đọc một lỗi Python cơ bản. Git chỉ cần ở mức clone.
- Không cần tài khoản AWS, Colab hoặc Kaggle trước tuần 17.

GitHub chỉ dùng để clone/download repo mẫu do chủ repo phát hành. Người học không fork, không commit/push,
không tạo PR và không nộp bài.

```text
git clone https://github.com/quanntm1206/AWS-Cloud-Club.git
cd AWS-Cloud-Club
```

Chọn đúng lệnh cho hệ điều hành:

```powershell
pwsh scripts/setup.ps1 -Profile core
pwsh scripts/check.ps1 -Scope bootstrap
.venv\Scripts\python.exe scripts/run_lab.py --lab 0
```

```bash
bash scripts/setup.sh --profile core
bash scripts/check.sh --scope bootstrap
.venv/bin/python scripts/run_lab.py --lab 0
```

Nếu lệnh cuối in đường dẫn `.artifacts/lab-00-evidence.json`, môi trường mẫu đã chạy. Đây chỉ là smoke demo;
bạn vẫn cần đọc [lab 00](../labs/lab-00-environment-and-reproducibility/README.md) để hiểu và tự kiểm tra kết quả.

## Nhịp học gợi ý

- 2 giờ đọc và tự giải thích lại bằng lời của mình.
- 2 giờ thực hành có hướng dẫn.
- 3-4 giờ làm lab và quan sát lỗi.
- 1 giờ tự kiểm tra; 1 giờ ghi learning log hoặc hoàn thiện.

Phần `Stretch` không tính vào 8-10 giờ. Bận một tuần? Giữ bài đọc cốt lõi, chạy mini profile và ghi lại một
điều đã hiểu; chuyển phần mở rộng sang tuần sau.

## Bốn thói quen nên giữ

1. Chạy baseline trước model phức tạp; nếu baseline chưa rõ, model phức tạp chỉ làm lỗi khó thấy hơn.
2. Chia dữ liệu trước mọi phép biến đổi có học trạng thái từ dữ liệu.
3. Ghi config, seed, metric, runtime và cả kết quả không như mong đợi.
4. Với AWS, chỉ đánh dấu xong sau cleanup và residual scan. Không mua Colab/Kaggle hoặc nâng cấp AWS Paid
   Plan chỉ để hoàn thành phần bắt buộc.

## Cách học thuật ngữ

Không cần đọc thuộc glossary trước tuần 01. Trong mỗi lab, đi theo bốn dòng `Thuật ngữ mới`, `Ôn lại`,
`Áp dụng trong lab`, `Tự giải thích`. Khi ghi learning log, chọn ít nhất một từ mới và một từ ôn lại, nối chúng
với command, metric hoặc lỗi bạn vừa quan sát. Nếu chỉ chép định nghĩa mà chưa chỉ ra nó xuất hiện ở đâu trong
lab, hãy xem khái niệm đó chưa thật sự vững.

## Bạn sẽ lưu gì?

Tạo một thư mục cục bộ thuận tiện cho learning log, ghi chú, biểu đồ và artifact. Mỗi tuần giữ lại:

- command đã chạy và môi trường;
- metric hoặc kiểm tra quan trọng nhất;
- một lỗi đã gặp, nguyên nhân và cách sửa;
- một điều còn chưa chắc;
- quyết định sẽ giữ hoặc thay đổi ở lần chạy sau.

Dùng [`learning-log-template.md`](learning-log-template.md) nếu chưa biết bắt đầu ghi từ đâu. Không gửi các
file này cho ai; chúng là nhật ký giúp bạn thấy chính mình tiến bộ.

## Khi lệnh không chạy

1. Xác nhận đang đứng ở repository root và virtual environment đã được tạo.
2. Đọc lỗi đầu tiên, không chỉ dòng cuối; kiểm Python version và dependency.
3. Chạy lại `scripts/check` với scope `bootstrap`.
4. Nếu lỗi do GPU, internet hoặc quota, quay về local/`cpu-mini`; không cần trả phí.
5. Chưa giải quyết được thì ghi command, lỗi và điều đã thử vào learning log trước khi hỏi trợ giúp.

Bây giờ mở [Tuần 01](weeks/week-01.md). Không cần đọc trước cả 24 tuần.

Khi hoàn thành tuần 24, mở [`sau-24-tuan.md`](sau-24-tuan.md) để chọn một hướng đào sâu trong 90 ngày tiếp theo.
