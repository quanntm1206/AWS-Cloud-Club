# Kế hoạch chuyển roadmap sang mô hình tự học local

> **Ngày:** 2026-08-12  
> **Mục tiêu:** GitHub chỉ là nơi chủ repo phát hành bộ khung. Người học clone/download một lần, tự học và lưu kết quả cục bộ; không fork, commit, push, PR hoặc nộp bài.

## 1. Quyết định thuật ngữ

| Hiện tại | Sau sửa | Ý nghĩa |
|---|---|---|
| Deliverable GitHub | Kết quả hướng tới | Sản phẩm/kỹ năng người học tạo được trong tuần; lưu local |
| Checkpoint | Mốc năng lực | Điểm dừng tự đánh giá sau mỗi 4 tuần |
| Nộp GitHub / Nộp | Minh chứng đạt mốc | File, metric, test, model card hoặc log để người học tự kiểm tra local |
| Learning log và GitHub | Learning log và tự đánh giá | Một giờ ghi nhận kết quả, lỗi và bước tiếp theo |
| Portfolio GitHub | Tổng kết năng lực | Bộ demo/artifact local; không yêu cầu public repository |

Giữ từ `checkpoint` khi đó là thuật ngữ kỹ thuật ML, ví dụ model checkpoint, checkpoint/resume, file `checkpoint.pt`. Chỉ đổi `checkpoint` mang nghĩa đánh giá chương trình.

## 2. Phạm vi thay đổi

### 2.1 Nội dung học

- `roadmap/weeks/week-01.md` đến `week-24.md`
  - Đổi heading `## Deliverable GitHub` thành `## Kết quả hướng tới`.
  - Đổi dòng workload `Learning log và GitHub` thành `Learning log và tự đánh giá`.
  - Đổi nội dung `checkpoint N` mang nghĩa đánh giá thành `mốc năng lực N`.
  - Giữ nguyên model checkpoint ở tuần 18-20.
  - Xóa câu yêu cầu commit, tag, push, portfolio repository hoặc nộp bài.
- `roadmap/checkpoints/checkpoint-01.md` đến `checkpoint-06.md`
  - Đổi title hiển thị thành `Mốc năng lực NN - Tuần X`; có thể giữ filename ổn định để tránh phá đường dẫn.
  - Đổi `## Nộp` thành `## Minh chứng đạt mốc`.
  - Đổi văn phong chấm/nộp thành tự đánh giá theo rubric.
  - Xóa `commit/tag checkpoint`; minh chứng lưu trong thư mục local do người học chọn.
- `roadmap/00-getting-started.md`
  - Thêm bước clone/download repo mẫu.
  - Đổi `Bằng chứng GitHub` thành `Kết quả học tập cục bộ`.
  - Nêu rõ không fork, không commit/push, không PR, không nộp bài.

### 2.2 Mô hình dữ liệu và rubric

- `curriculum/curriculum.yml`
  - Đổi field đánh giá chương trình từ `checkpoint` thành `milestone` nếu blast radius nhỏ; nếu giữ schema nội bộ thì chỉ đổi nhãn hiển thị. Khuyến nghị đổi sang `milestone` để không tiếp tục phát tán thuật ngữ cũ.
  - Giá trị `checkpoint-01`... thành `milestone-01`...; giữ model checkpoint ngoài schema này.
  - Tuần 24 đổi title `Portfolio, cost audit và demo` thành `Tổng kết năng lực, cost audit và demo`.
- `curriculum/assessment.yml`
  - Đổi collection `checkpoints` thành `milestones`, ID `milestone-01`...`milestone-06`.
  - Focus cuối kỳ đổi `portfolio-and-cost-safety` thành `capability-summary-and-cost-safety`.
- `scripts/validate_curriculum.py`
  - Kiểm đúng sáu `milestone` có thứ tự; message dùng `mốc năng lực`.
- Tests curriculum cập nhật theo schema và nhãn mới.

### 2.3 Repo mẫu và lab

- `README.md`
  - Nói rõ repo này là bộ khung mẫu do chủ repo phát hành.
  - GitHub chỉ dùng để clone/download source.
  - Thêm lệnh clone bằng URL repo chính thức đã xác minh; không đoán URL.
  - Xóa ngôn ngữ ngụ ý người học phải xây GitHub portfolio.
- `labs/**/README.md`, `labs/**/expected/README.md`, capstone docs
  - Giữ acceptance/self-check và artifact local.
  - Xóa mọi commit/push/PR/submission wording nếu có.
  - Giải thích evidence chỉ phục vụ tự kiểm tra; không gửi cho chủ repo.
- `docs/superpowers/specs/2026-08-12-ml-engineer-roadmap-design.md`
  - Cập nhật design hiện hành: tự học local, mốc năng lực, tổng kết năng lực, GitHub clone-only.
- Kế hoạch lịch sử `docs/superpowers/plans/2026-08-12-ml-engineer-roadmap.md`
  - Không sửa toàn bộ lịch sử implementation; thêm banner `Historical plan` và link quyết định mới để tránh làm sai lịch sử.

### 2.4 DOCX builder và tài liệu phát hành

- `scripts/build_docx.py`
  - Parse `## Kết quả hướng tới`.
  - Nhãn bảng `Checkpoint` thành `Mốc năng lực`.
  - `Nộp GitHub:` thành `Kết quả hướng tới:`.
  - `Lab, checkpoint và rubric` thành `Lab, mốc năng lực và rubric`.
  - `Portfolio GitHub` thành `Tổng kết năng lực`.
  - Bỏ nội dung nộp README/code lên GitHub; thay bằng checklist artifact local.
  - Phần Colab/Kaggle có thể nói `mở notebook từ repo mẫu đã clone/upload`; không mô tả GitHub của người học.
- Rebuild `dist/ML-Roadmap-24-Tuan-AWS-Cloud-Club.docx`.
- Chạy a11y audit; Word render toàn bộ; xem contact sheet; cập nhật SHA/page count trong `.artifacts/release-verification.json`.

## 3. Guardrail chống tái phát

Thêm tests deterministic:

1. Mọi file tuần chứa `## Kết quả hướng tới`; không còn `## Deliverable GitHub`.
2. Mọi file mốc chứa `## Minh chứng đạt mốc`; không còn `## Nộp` hoặc `commit/tag checkpoint`.
3. Repo learner-facing không chứa các cụm: `Nộp GitHub`, `Portfolio GitHub`, `fork repo`, `push`, `pull request`, `commit mỗi tuần`, trừ tài liệu lịch sử đã đánh dấu.
4. README/getting-started chứa tuyên bố GitHub clone-only và `không nộp bài`.
5. Curriculum có đúng 6 milestone theo tuần 4, 8, 12, 16, 20, 24.
6. DOCX text chứa `Kết quả hướng tới`, `Mốc năng lực`, `Minh chứng đạt mốc`, `GitHub chỉ dùng để clone`; không chứa `Nộp GitHub`/`Portfolio GitHub`.
7. Không đổi thuật ngữ kỹ thuật `model checkpoint`, `checkpoint.pt`, checkpoint/resume.

## 4. Trình tự triển khai

### Task 1 - Red tests cho terminology contract

**Sửa:** `tests/curriculum/test_curriculum.py`, `tests/curriculum/test_docx_content.py`  
**Tạo:** `tests/curriculum/test_learner_workflow_language.py`

- Viết test mới theo 7 guardrail.
- Chạy test mục tiêu; expected fail trên nội dung hiện tại.

```powershell
.venv\Scripts\python.exe -m pytest tests/curriculum -q
```

### Task 2 - Đổi schema checkpoint đánh giá thành milestone

**Sửa:** `curriculum/curriculum.yml`, `curriculum/assessment.yml`, `scripts/validate_curriculum.py`, tests liên quan.

- Không chạm code/model checkpoint.
- Chạy validator và curriculum tests.

```powershell
.venv\Scripts\python.exe scripts/validate_curriculum.py
.venv\Scripts\python.exe -m pytest tests/curriculum -q
```

### Task 3 - Cập nhật 24 tuần và 6 mốc năng lực

**Sửa:** `roadmap/weeks/week-*.md`, `roadmap/checkpoints/checkpoint-*.md`, `roadmap/00-getting-started.md`.

- Thay heading/nhãn bằng script deterministic có assertion count: 24 heading tuần, 24 workload labels, 6 milestone docs.
- Đọc chính xác tuần 19 và mốc bất kỳ sau replace để bảo đảm model checkpoint không bị đổi.
- Chạy terminology tests.

### Task 4 - Cập nhật README, lab, capstone, design

**Sửa:** `README.md`, learner-facing `labs/**`, `capstones/**`, design spec.  
**Sửa có giới hạn:** historical plan chỉ thêm banner/superseding decision.

- GitHub duy nhất: clone/download repo mẫu của chủ repo.
- Artifact, log, test evidence lưu local; không gửi ai.
- Không thêm URL repo giả; chỉ ghi URL repo chính thức sau khi xác minh.

### Task 5 - Cập nhật DOCX builder

**Sửa:** `scripts/build_docx.py`, DOCX tests.

- Đổi parser/nhãn/section theo terminology mới.
- Test text extraction và negative assertions.

### Task 6 - Full validation và phát hành lại DOCX

```powershell
.\scripts\check.ps1 -Scope all -Profile release
```

Sau đó:

1. Build DOCX bằng bundled document runtime.
2. A11y audit phải 0 high/medium/low.
3. Word COM render sang PDF.
4. Render toàn bộ page PNG/contact sheet; kiểm clipping, overlap, blank page, broken heading.
5. Copy DOCX cuối vào `dist/`.
6. Cập nhật release receipt với test count, page count, SHA-256, scope.

### Task 7 - Reviewer loop

- Gọi lại reviewer `gpt-5.6-sol` xhigh theo yêu cầu trước.
- Audit tập trung: không còn nghĩa nộp GitHub, milestone đúng, model checkpoint không bị phá, DOCX/README nhất quán.
- Nếu `NEEDS_CHANGES`: sửa, full validation, rebuild artifact nếu cần, review lại.
- Dừng khi reviewer trả `SATISFACTORY`.

## 5. Tiêu chí hoàn thành

- GitHub chỉ được mô tả như nguồn clone/download repo mẫu của chủ repo.
- Không có yêu cầu learner fork/commit/push/PR/public portfolio/submission.
- 24 `Kết quả hướng tới`; 6 `Mốc năng lực`; 6 `Minh chứng đạt mốc`.
- Kết quả/artifact lưu local, dùng tự đánh giá.
- Model checkpoint/resume giữ nguyên kỹ thuật.
- Full release gate pass; DOCX a11y/render/hash pass.
- Reviewer xhigh trả `SATISFACTORY`.
