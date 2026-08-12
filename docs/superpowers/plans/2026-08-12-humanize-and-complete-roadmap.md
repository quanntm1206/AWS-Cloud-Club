# Kế hoạch làm mềm giọng văn và hoàn thiện roadmap

## Mục tiêu

Biến repo và DOCX từ bản tham chiếu cô đọng thành handbook tự học 24 tuần có giọng mentor gần gũi, chạy được,
đủ đường dẫn và tiêu chí tự đánh giá. Giữ local-first, Colab/Kaggle Free, AWS private Lambda; không thêm quy
trình nộp bài hoặc GitHub workflow cho người học.

## Phạm vi file

- `README.md`, `roadmap/00-getting-started.md`, `roadmap/weeks/*.md`: lời mở đầu, bản đồ sáu chặng,
  trực giác, ví dụ, dấu hiệu đã hiểu, khi mắc kẹt, lịch 8-10 giờ.
- `labs/**/README.md`, `labs/**/expected/README.md`, `labs/README.md`: nhiệm vụ riêng từng lab, lệnh thật,
  output mong đợi, lỗi thường gặp; không giả vờ starter là bài tập TODO nếu chỉ là demo.
- `notebooks/README.md`, `docs/source-notes/colab-free.md`, `docs/source-notes/kaggle-notebooks.md`:
  quick start, notebook cụ thể, accelerator/fallback/export/resume/troubleshooting.
- `capstones/*/README.md`: file map, dữ liệu, config, lệnh, từng giai đoạn, tiêu chí hoàn thành, khắc phục lỗi.
- `roadmap/checkpoints/*.md`, `curriculum/assessment.yml`, `curriculum/glossary.yml`: rubric riêng từng mốc,
  global gates, glossary mở rộng, định hướng 90 ngày.
- `aws/**`, tuần 21-24, lab 20: làm rõ Free/Paid Plan, USD 100 + tối đa USD 100, Organizations/Control Tower,
  loại public API khỏi learner execution path, recovery cleanup, Budget/residual/cost-audit caveat.
- `scripts/build_docx.py`, `dist/*.docx`: quick start, URL repo, điều hướng, roadmap/capstone/lab map/rubric,
  nội dung mới và giọng văn mentor.
- `tests/**`, validators: khóa các contract mới và ngăn tái xuất bản nội dung máy móc/sai chi phí.

## Thứ tự triển khai

1. Khóa contract bằng test: 21 lab, 8-10 giờ, URL/quick start, heading tiếng Việt, AWS stop conditions,
   rubric theo mốc, DOCX có đường dẫn repo/lệnh chạy.
2. Viết lại README/getting started; thêm bản đồ sáu chặng và hướng dẫn học khi chậm/không GPU.
3. Viết lại 24 tuần theo khung: vì sao quan trọng, cuối tuần làm được gì, kiến thức bằng trực giác,
   thực hành, kết quả cụ thể, dấu hiệu đã hiểu, khi mắc kẹt. Bổ sung xác suất thực dụng, calibration/log loss,
   regularization, overfit/underfit, monitoring/drift, subgroup risk ở tuần phù hợp.
4. Viết lại 21 lab + expected guide theo nhiệm vụ thật. CV lab 17-19 trỏ thẳng notebook PyTorch thật;
   central `run_example` được mô tả là smoke demo, không phải bài training hoàn chỉnh.
5. Mở rộng Colab/Kaggle và hai capstone bằng lệnh/file path/troubleshooting cụ thể.
6. Sửa AWS guardrails theo nguồn AWS chính thức đã kiểm ngày 2026-08-12; private invoke là đường duy nhất
   được thực thi. `ExpiresAt` là metadata, không phải TTL; lỗi sau deploy phải cleanup ngay.
7. Nâng rubric sáu mốc, glossary, định hướng 90 ngày; sửa inventory và workload.
8. Nâng DOCX builder, build lại DOCX bằng bundled runtime; render toàn bộ trang, kiểm a11y/layout/content.
9. Chạy `scripts/check.ps1 -Scope all -Profile release`, kiểm link/source, secret, git diff; audit độc lập
   kiến thức, chi phí, trải nghiệm người học. Sửa đến khi reviewer trả `SATISFACTORY`.
10. Commit, push `main`, chờ GitHub Actions xanh; báo URL và thay đổi chính.

## Tiêu chí hoàn thành

- Người mới clone repo, setup, chạy lab 00, mở đúng week/lab/notebook trong 15 phút.
- Mỗi tuần có giải thích tự nhiên, kết quả đo được, cách tự kiểm và recovery path; lịch không vượt 10 giờ.
- Mỗi lab nói đúng code thực sự làm gì; expected guide có oracle/output/hint riêng.
- Colab/Kaggle có CPU fallback, lưu artifact trước session end, không cần bản trả phí.
- AWS không mời bật public API; claim plan/credits/timing đúng nguồn; mọi deploy có cleanup/recovery.
- DOCX đủ dùng như handbook, đồng thời chỉ đúng repo để chạy lab; rubric/glossary/navigation sử dụng được.
- Repo test/lint/typecheck/validators và GitHub Actions đều pass.
