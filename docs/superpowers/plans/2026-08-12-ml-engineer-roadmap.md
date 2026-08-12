# Kế hoạch triển khai roadmap Machine Learning Engineer 24 tuần

> **Đã được thay thế (2026-08-12):** Quyết định workflow người học trong kế hoạch lịch sử này được thay bởi
> `docs/superpowers/plans/2026-08-12-github-clone-only-learner-workflow.md`. GitHub chỉ dùng để chủ repo
> phát hành bộ khung cho người học clone/download; artifact và tự đánh giá lưu local. Không diễn giải các
> yêu cầu fork/commit/push/PR/nộp bài/portfolio bên dưới như workflow hiện hành.

> **Trạng thái:** Sẵn sàng thực thi sau khi duyệt  
> **Spec:** `docs/superpowers/specs/2026-08-12-ml-engineer-roadmap-design.md`  
> **Đầu ra:** DOCX hoàn chỉnh + repository GitHub-ready  
> **Ngôn ngữ:** Nội dung tiếng Việt; code, command và identifier tiếng Anh

## 1. Phạm vi

Kế hoạch tạo hai đầu ra đồng bộ từ một content source:

1. `dist/ML-Roadmap-24-Tuan-AWS-Cloud-Club.docx` cho người học đọc và theo dõi.
2. Repository chứa 24 tuần, lab, notebook, code mẫu, hai capstone, AWS cost guard và cleanup script.

Không tạo tài khoản AWS, không deploy resource thật trong giai đoạn xây tài liệu. Mọi kiểm thử AWS dùng static validation hoặc mock trừ khi có phiên nghiệm thu riêng được phê duyệt.

## 2. Requirement catalog

| ID | Yêu cầu quan sát được | Tiêu chí nghiệm thu |
|---|---|---|
| R01 | Roadmap đủ 24 tuần | Mỗi tuần có objective, theory, lab, deliverable, checkpoint và 8-10 giờ workload |
| R02 | Từ nền tảng đến ML Engineer | Bao phủ data, ML, evaluation, engineering, deployment, monitoring, portfolio |
| R03 | Local-first | Các bài nền tảng và tabular chạy local CPU |
| R04 | Colab/Kaggle Free | Có hướng dẫn riêng, accelerator detection, CPU fallback, checkpoint/export |
| R05 | Hai capstone | Tabular bắt buộc; CV mở rộng, train Colab/Kaggle |
| R06 | AWS cost-safe | Không GPU/NAT/endpoint nền; có estimate, budget warning, cleanup, residual scan |
| R07 | Repo-ready | README, license, setup, labs, notebooks, tests, CI, contributing |
| R08 | Code mẫu chạy được | Quick tests và mini training pass trên CPU |
| R09 | Cleanup an toàn | Dry-run mặc định, tag/prefix scope, allowlist, idempotent, PS/Bash parity |
| R10 | DOCX chuyên nghiệp | Preset đúng, render được, tất cả trang qua visual QA |
| R11 | Nguồn hiện trạng | URL chính thức + `verified_on`; không ghi quota Kaggle cố định |
| R12 | Không lộ secret | Secret scan pass; notebook và docs dùng placeholder/env vars |

## 3. Cấu trúc file mục tiêu

```text
E:/AWS/AWS Cloud Club/
|-- README.md
|-- LICENSE
|-- CODE_OF_CONDUCT.md
|-- CONTRIBUTING.md
|-- SECURITY.md
|-- pyproject.toml
|-- requirements.lock
|-- .gitignore
|-- .env.example
|-- .pre-commit-config.yaml
|-- Makefile
|-- docs/
|   |-- sources.yml
|   |-- source-notes/
|   |   |-- aws-free-tier.md
|   |   |-- colab-free.md
|   |   `-- kaggle-notebooks.md
|   |-- superpowers/specs/2026-08-12-ml-engineer-roadmap-design.md
|   `-- superpowers/plans/2026-08-12-ml-engineer-roadmap.md
|-- curriculum/
|   |-- curriculum.yml
|   |-- assessment.yml
|   `-- glossary.yml
|-- roadmap/
|   |-- 00-getting-started.md
|   |-- weeks/week-01.md ... weeks/week-24.md
|   |-- checkpoints/checkpoint-01.md ... checkpoint-06.md
|   `-- learning-log-template.md
|-- labs/
|   |-- lab-01-numpy-vectorization/
|   |-- lab-02-pandas-eda/
|   |-- ...
|   |-- lab-20-aws-cleanup-audit/
|   `-- README.md
|-- notebooks/
|   |-- shared/00_environment_check.ipynb
|   |-- local/
|   |-- colab/
|   |-- kaggle/
|   `-- README.md
|-- src/ml_roadmap/
|   |-- __init__.py
|   |-- config.py
|   |-- data.py
|   |-- validation.py
|   |-- features.py
|   |-- train_tabular.py
|   |-- evaluate.py
|   |-- artifacts.py
|   |-- inference.py
|   |-- api.py
|   `-- cv/
|       |-- data.py
|       |-- model.py
|       |-- train.py
|       `-- evaluate.py
|-- capstones/
|   |-- tabular-churn/
|   |   |-- README.md
|   |   |-- rubric.yml
|   |   |-- configs/{mini,full}.yml
|   |   |-- notebooks/
|   |   `-- reports/{experiment-report,model-card}.md
|   `-- cv-image-classification/
|       |-- README.md
|       |-- rubric.yml
|       |-- configs/{cpu-mini,gpu-free}.yml
|       |-- notebooks/{colab,kaggle}.ipynb
|       `-- reports/{experiment-report,model-card,aws-adr}.md
|-- aws/
|   |-- README.md
|   |-- cost-policy.yml
|   |-- resource-manifest.yml
|   |-- cloudformation/tabular-inference.yml
|   |-- iam/lab-policy.json
|   |-- lambda/handler.py
|   |-- scripts/{preflight,cost-check,deploy,cleanup,residual-scan}.{ps1,sh}
|   `-- events/{valid,invalid}.json
|-- scripts/
|   |-- setup.{ps1,sh}
|   |-- check.{ps1,sh}
|   |-- build_docx.py
|   |-- validate_curriculum.py
|   |-- validate_notebooks.py
|   |-- validate_sources.py
|   |-- validate_aws_safety.py
|   `-- export_notebook.py
|-- tests/
|   |-- unit/
|   |-- integration/
|   |-- notebooks/
|   |-- aws/
|   `-- curriculum/
|-- .github/
|   |-- workflows/ci.yml
|   |-- ISSUE_TEMPLATE/
|   `-- pull_request_template.md
`-- dist/
    `-- ML-Roadmap-24-Tuan-AWS-Cloud-Club.docx
```

## 4. Curriculum map 24 tuần

| Tuần | Chủ đề | Lab/đầu ra | Môi trường chính | AWS |
|---:|---|---|---|---|
| 1 | ML workflow, Python data stack, reproducibility | Setup + learning log + environment report | Local CPU | Không |
| 2 | NumPy, vectorization, shape, broadcasting | Cài linear prediction và metric bằng NumPy | Local CPU | Không |
| 3 | pandas, cleaning, EDA, visualization | EDA report trên dataset nhỏ | Local CPU | Không |
| 4 | Đại số tuyến tính, xác suất, gradient trực giác | Linear regression từ đầu + checkpoint 1 | Local CPU | Không |
| 5 | Supervised learning, train/validation/test | Baseline classification | Local CPU | Không |
| 6 | Preprocessing, missing/category, pipeline | Leakage-safe sklearn pipeline | Local CPU | Không |
| 7 | Metrics, imbalance, threshold, calibration | Metric decision report | Local CPU | Không |
| 8 | Cross-validation, bias/variance, learning curve | Model evaluation harness + checkpoint 2 | Local CPU | Không |
| 9 | Decision tree, random forest, boosting | So sánh ba model có giới hạn | Local CPU | Không |
| 10 | Feature engineering và selection | Ablation nhỏ, không sweep | Local CPU | Không |
| 11 | Interpretability, error analysis, fairness | Slice metrics + failure taxonomy | Local CPU | Không |
| 12 | Mini-project tabular | Report + model card + checkpoint 3 | Local CPU | Không |
| 13 | Project structure, config, logging | Chuyển notebook thành package | Local CPU | Không |
| 14 | Test data/model code, contracts | Unit + integration tests | Local CPU | Không |
| 15 | FastAPI inference, schema, errors | Local REST inference API | Local CPU | Không |
| 16 | Docker, CI, artifact/versioning | Container/local CI + checkpoint 4 | Local CPU | Kiến trúc sơ lược |
| 17 | Neural networks, PyTorch basics | MLP nhỏ, device detection | Local/Colab/Kaggle | Không |
| 18 | CNN và transfer learning | Frozen-backbone CV baseline | Chọn Colab hoặc Kaggle | Không |
| 19 | Fine-tuning tiết kiệm và checkpoints | 3-5 epoch + resume/export | Chọn Colab hoặc Kaggle | Không |
| 20 | CV evaluation, confusion matrix, failure cases | CV model card + checkpoint 5 | Local + selected free runtime | S3 optional design |
| 21 | AWS Free Plan, IAM, Budgets, S3 | Preflight, cost guard, upload/download artifact | AWS Free Plan | IAM/S3/Budgets |
| 22 | Lambda inference an toàn | Deploy ZIP Lambda, invoke riêng tư, cleanup | AWS Free Plan | Lambda/Logs |
| 23 | Capstone integration | API Gateway optional short session; residual scan | AWS Free Plan | HTTP API optional |
| 24 | Portfolio, incident/cost review | Demo, cleanup evidence, checkpoint 6 | Local + AWS audit | Cost audit |

## 5. Danh mục lab

Mỗi thư mục lab có `README.md`, `starter/`, `tests/`, `expected/README.md`; solution đầy đủ đặt ngoài đường mặc định hoặc dùng branch/tag instructor để tránh người học nhìn ngay đáp án.

| Lab | Tuần | Tên | Acceptance chính |
|---:|---:|---|---|
| 01 | 2 | NumPy vectorization | Kết quả khớp reference; không loop ở phần vectorized |
| 02 | 3 | pandas EDA | Data quality table + ba insight có bằng chứng |
| 03 | 4 | Linear regression from scratch | Loss giảm; gradient check trên mini data |
| 04 | 5 | First classifier | Dummy baseline + split cố định |
| 05 | 6 | Leakage-safe preprocessing | Preprocessor chỉ fit trên train |
| 06 | 7 | Metrics and threshold | Chọn metric/threshold theo constraint |
| 07 | 8 | Cross-validation | Mean/std + learning curve |
| 08 | 9 | Tree ensemble comparison | Tối đa ba candidate; runtime cap |
| 09 | 10 | Feature ablation | Một biến thay đổi mỗi experiment |
| 10 | 11 | Error analysis | Slice table + failure taxonomy |
| 11 | 12 | Tabular mini-project | Reproducible report + model card |
| 12 | 13 | Notebook-to-package | CLI train từ config |
| 13 | 14 | ML testing | Schema, transformation, metric tests |
| 14 | 15 | Local inference API | Valid/invalid payload contract |
| 15 | 16 | Docker and CI | Image builds; offline smoke passes |
| 16 | 17 | PyTorch device-aware MLP | CPU/GPU detection + seeded run |
| 17 | 18 | Transfer learning baseline | Frozen backbone + mini fallback |
| 18 | 19 | Checkpoint and resume | Resume creates consistent epoch history |
| 19 | 20 | CV error analysis | Per-class metrics + tối đa 20 failures; nếu ít hơn, export toàn bộ |
| 20 | 21-23 | AWS safe deployment | Full cost-safe lifecycle + zero residuals |

## 6. Rủi ro và test priority

Thang điểm: Severity, Likelihood, Detectability từ 1 (thấp) đến 5 (cao); `RPN = S * L * D`.

| Risk | S | L | D | RPN | Biện pháp/test |
|---|---:|---:|---:|---:|---|
| Tạo resource AWS tốn phí chạy nền | 5 | 3 | 4 | 60 | Static denylist, TTL tags, cleanup, residual scan, docs warning |
| Cleanup xóa nhầm resource | 5 | 2 | 4 | 40 | Dry-run, allowlist, exact prefix/tag, typed confirmation, mocked deletion tests |
| AWS Budget bị hiểu là hard cap | 5 | 3 | 2 | 30 | Cảnh báo lặp lại, quiz và preflight acknowledgment |
| Notebook phụ thuộc GPU/quota cụ thể | 3 | 4 | 3 | 36 | CPU mini profile, device detection, no quota assertion |
| Data leakage làm metric giả | 4 | 3 | 3 | 36 | Pipeline tests, split-before-fit checks, checkpoint rubric |
| Notebook không tái lập | 4 | 3 | 3 | 36 | Seed/config/artifact manifest, clean-run smoke |
| Secret AWS vào Git | 5 | 2 | 3 | 30 | `.gitignore`, env placeholders, secret scan, CI |
| Model/artifact quá lớn cho Lambda | 4 | 3 | 2 | 24 | Artifact hard cap, compression check, cold-start test |
| DOCX vỡ bảng/tiếng Việt | 3 | 3 | 2 | 18 | Render tất cả trang, visual QA, style/table geometry audit |
| Nội dung 24 tuần quá tải | 3 | 3 | 3 | 27 | Workload validator, core/stretch labels, pilot review |

## 7. Các task triển khai

### Task 1 - Khởi tạo repository và quality baseline

**Tạo:** `README.md`, `LICENSE`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `.gitignore`, `.env.example`, `pyproject.toml`, `requirements.lock`, `.pre-commit-config.yaml`, `Makefile`.

1. Viết `pyproject.toml` với Python range được chọn sau khi kiểm tài liệu package hiện hành; nhóm dependency `core`, `cv`, `dev`, `docs`.
2. Cấu hình formatter/linter/type/test trong một command `python -m ...`; không yêu cầu package toàn cục.
3. `.gitignore` loại `.env`, credential, checkpoints, datasets, generated reports, render QA và notebook checkpoints.
4. README mô tả đối tượng, 24 tuần, local-first, hai capstone, quickstart, chi phí và license.
5. Chạy:

```powershell
pwsh scripts/setup.ps1 -Profile core
pwsh scripts/check.ps1 -Scope bootstrap
```

**Expected:** virtual environment tạo thành công; import `ml_roadmap` pass; không cần AWS credential.

**Commit:** `chore: scaffold ML roadmap repository`

### Task 2 - Tạo curriculum schema và validators trước nội dung

**Tạo:** `curriculum/curriculum.yml`, `curriculum/assessment.yml`, `curriculum/glossary.yml`, `scripts/validate_curriculum.py`, `tests/curriculum/test_curriculum.py`.

1. Định nghĩa schema tuần gồm `id`, `title`, `objectives`, `prerequisites`, `hours`, `core_reading`, `lab`, `deliverables`, `assessment`, `environments`, `cost_class`, `stretch`.
2. Validator bắt đúng 24 tuần, tổng giờ mỗi tuần 8-10, sáu checkpoint, lab ID duy nhất, path tồn tại, AWS chỉ xuất hiện tuần 21-24 trừ nội dung kiến trúc.
3. Viết failing tests cho thiếu tuần, workload vượt giới hạn, duplicate lab, AWS forbidden service.
4. Hoàn thiện YAML skeleton đủ 24 entry để test pass.

```powershell
& .\.venv\Scripts\python.exe -m pytest tests/curriculum -q
& .\.venv\Scripts\python.exe scripts/validate_curriculum.py
```

**Expected:** `24 weeks; 6 checkpoints; workload valid; cost policy valid`.

**Commit:** `feat: define validated curriculum contract`

### Task 3 - Viết nội dung tuần 1-4 và checkpoint 1

**Tạo:** `roadmap/00-getting-started.md`, `roadmap/weeks/week-01.md` đến `week-04.md`, `roadmap/checkpoints/checkpoint-01.md`, `roadmap/learning-log-template.md`, labs 01-03.

Mỗi tuần dùng template:

```markdown
# Tuần NN - Chủ đề
## Kết quả đầu ra
## Kiến thức cốt lõi
## Lịch 8-10 giờ
## Guided practice
## Lab
## Tự kiểm tra
## Deliverable GitHub
## Core vs stretch
## Lỗi thường gặp
## Nguồn
```

Tests: NumPy expected arrays, EDA required-section check, finite-difference gradient check.

**Commit:** `feat: add data and math foundation phase`

### Task 4 - Viết nội dung tuần 5-8 và checkpoint 2

**Tạo:** `week-05.md` đến `week-08.md`, `checkpoint-02.md`, labs 04-07, code data/split/preprocessing/evaluate.

1. Dùng một dataset tabular nhỏ, license rõ, snapshot checksum hoặc deterministic fetch.
2. Viết baseline trước model candidate.
3. Pipeline test phải phát hiện fit transformer trên toàn bộ data.
4. Metric lab bao phủ imbalanced classes, threshold boundary và confusion matrix.
5. Cross-validation cố định seed; report mean, std, runtime.

**Commit:** `feat: add classical ML fundamentals phase`

### Task 5 - Viết nội dung tuần 9-12 và checkpoint 3

**Tạo:** `week-09.md` đến `week-12.md`, `checkpoint-03.md`, labs 08-11, tabular mini-project template.

1. Candidate list tối đa ba model; config chứa runtime cap.
2. Feature ablation thay đúng một yếu tố mỗi run.
3. Error analysis bắt buộc slice metrics và taxonomy.
4. Model card ghi intended use, limitations, data, metrics, ethical risks.
5. Checkpoint chấm bằng `assessment.yml`, không chấm theo accuracy đơn lẻ.

**Commit:** `feat: add applied tabular ML phase`

### Task 6 - Xây package tabular bằng TDD

**Tạo:** `src/ml_roadmap/{config,data,validation,features,train_tabular,evaluate,artifacts,inference}.py`, `tests/unit/`, `tests/integration/test_tabular_pipeline.py`.

Contracts:

```python
def load_config(path: Path) -> TrainConfig: ...
def validate_frame(frame: pd.DataFrame, schema: DataSchema) -> ValidationReport: ...
def train(config: TrainConfig) -> TrainResult: ...
def save_artifact(result: TrainResult, output_dir: Path) -> ArtifactManifest: ...
def predict(payload: dict[str, object], bundle: ModelBundle) -> PredictionResponse: ...
```

Test trước implementation: deterministic split, unknown category, missing column, extra column policy, artifact checksum, model reload parity.

```powershell
& .\.venv\Scripts\python.exe -m pytest tests/unit tests/integration/test_tabular_pipeline.py -q
```

**Commit:** `feat: add reproducible tabular training package`

### Task 7 - Viết tuần 13-16, API, Docker và CI local

**Tạo:** `week-13.md` đến `week-16.md`, `checkpoint-04.md`, labs 12-15, `src/ml_roadmap/api.py`, `Dockerfile`, `.dockerignore`.

1. FastAPI/Pydantic schema hoặc equivalent chỉ được chốt sau khi kiểm API/version hiện hành.
2. Test `200`, schema invalid `422`/contract tương ứng, model unavailable, health check.
3. Docker chạy non-root, copy dependency trước code, không chứa model secret hoặc credential.
4. CI chỉ lint, typecheck, unit, integration, notebook validation, source validation, AWS static safety.
5. Không có workflow deploy hoặc OIDC AWS trong repo học mặc định.

**Commit:** `feat: add ML engineering and local serving phase`

### Task 8 - Tạo hướng dẫn Colab Free và Kaggle Free

**Tạo:** `docs/source-notes/{colab-free,kaggle-notebooks}.md`, `notebooks/README.md`, `notebooks/shared/00_environment_check.ipynb`, `scripts/validate_notebooks.py`, `tests/notebooks/`.

1. Research lại tài liệu chính thức tại thời điểm thực thi; ghi URL, quote hỗ trợ, `verified_on`, `recheck_after`.
2. Không ghi quota GPU Kaggle cố định nếu không có nguồn chính thức ổn định.
3. Colab guide: upload/open GitHub notebook, runtime selection, Drive optional, checkpoint/export, disconnect/delete runtime.
4. Kaggle guide: add dataset, enable accelerator nếu có, internet/secret handling, save version/output, download artifact.
5. Shared environment cell in Python:

```python
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
PROFILE = "gpu-free" if DEVICE == "cuda" else "cpu-mini"
print({"device": DEVICE, "profile": PROFILE})
```

6. Notebook validator kiểm cell headings, seed, profile fallback, artifact export, không hardcode credential, không có output lớn.

**Commit:** `docs: add free Colab and Kaggle training paths`

### Task 9 - Xây CV training path và tuần 17-20

**Tạo:** `week-17.md` đến `week-20.md`, `checkpoint-05.md`, labs 16-19, `src/ml_roadmap/cv/`, capstone CV configs và notebooks.

1. Viết CPU mini test trước: tiny synthetic/image fixture, một epoch, checkpoint save/load.
2. `cpu-mini.yml`: ảnh nhỏ, subset nhỏ, batch nhỏ, 1 epoch smoke.
3. `gpu-free.yml`: frozen backbone, 3-5 epoch, early stopping, max wall-clock note.
4. Notebook Colab/Kaggle gọi cùng source package, chỉ khác bootstrap/data path.
5. Evaluation: accuracy + macro F1 + per-class + confusion matrix + tối đa 20 failure examples; nếu ít hơn, export toàn bộ.
6. Fine-tuning unfreeze là stretch; không là điều kiện pass.

```powershell
& .\.venv\Scripts\python.exe -m pytest tests/unit/test_cv_* tests/integration/test_cv_mini_train.py -q
```

**Commit:** `feat: add cost-aware computer vision phase`

### Task 10 - Thiết kế AWS cost policy trước IaC

**Tạo:** `aws/cost-policy.yml`, `aws/resource-manifest.yml`, `docs/source-notes/aws-free-tier.md`, `scripts/validate_aws_safety.py`, `tests/aws/test_cost_policy.py`.

`cost-policy.yml` phải encode:

```yaml
default_region: us-east-1
required_tags: [Project, Owner, Environment, ExpiresAt]
allowed_services: [s3, lambda, logs, iam, budgets, apigateway]
forbidden_resources:
  - AWS::EC2::NatGateway
  - AWS::SageMaker::Endpoint
  - AWS::SageMaker::NotebookInstance
  - AWS::SageMaker::TrainingJob
limits:
  lambda_memory_mb: 512
  lambda_timeout_seconds: 15
  log_retention_days: 1
  artifact_hard_limit_mb: 200
  upload_hard_limit_mb: 500
```

Validator fail nếu CloudFormation chứa service ngoài allowlist, wildcard IAM action/resource không có documented exception, missing tag, missing retention, public S3 hoặc artifact vượt cap.

Nguồn AWS phải kiểm lại Free/Paid plan, credits, Budget delay, Lambda/S3/CloudWatch/API Gateway/ECR offer tại ngày thực thi. Pricing/hạn mức trong roadmap luôn kèm ngày; không dùng dữ liệu memory.

**Commit:** `feat: codify AWS learning cost policy`

### Task 11 - Xây CloudFormation tabular inference tối giản

**Tạo:** `aws/cloudformation/tabular-inference.yml`, `aws/iam/lab-policy.json`, `aws/lambda/handler.py`, events và tests.

1. Bắt đầu bằng tests parse template và assert allowlist.
2. Kiến trúc mặc định: private Lambda invocation qua AWS CLI; S3 bucket chứa artifact; CloudWatch log retention một ngày.
3. API Gateway đặt condition `EnablePublicApi=false` mặc định.
4. Bucket chặn public access, encryption bật, lifecycle bảy ngày, deletion policy phù hợp lab cleanup.
5. IAM role chỉ `s3:GetObject` đúng object prefix và logging cần thiết.
6. Lambda env không chứa secret; handler validate schema và không log raw sensitive payload.
7. Template output resource names để cleanup/residual scan dùng deterministic manifest.

```powershell
& .\.venv\Scripts\python.exe -m pytest tests/aws/test_template.py tests/aws/test_lambda_handler.py -q
& .\.venv\Scripts\python.exe scripts/validate_aws_safety.py aws/cloudformation/tabular-inference.yml
```

**Commit:** `feat: add guarded serverless tabular inference template`

### Task 12 - Xây preflight, deploy, cleanup và residual scan

**Tạo:** các cặp `.ps1`/`.sh` trong `aws/scripts/`; `tests/aws/test_cleanup_contract.py`.

Script interface thống nhất:

```text
preflight --project-id <id> --region <region>
cost-check --project-id <id> --region <region>
deploy --project-id <id> --region <region> [--enable-public-api]
cleanup --project-id <id> --region <region> [--dry-run|--execute]
residual-scan --project-id <id> --region <region> [--json]
```

1. `preflight`: kiểm AWS identity, account plan acknowledgment, Region, budget presence, artifact size, tags, forbidden active resources liên quan prefix.
2. `cost-check`: in resource manifest, cost class, link Pricing Calculator/docs; không tuyên bố giá bằng 0.
3. `deploy`: validate trước create; tag đầy đủ; ghi deployment manifest local.
4. `cleanup`: dry-run mặc định; require exact project ID và confirmation khi execute; xóa theo dependency order.
5. `residual-scan`: chỉ query allowlist; output JSON; exit nonzero nếu còn resource.
6. Test PowerShell/Bash argument parity, dry-run no mutation, unknown project reject, missing tag reject, repeated cleanup success bằng AWS CLI mock.
7. Thêm emergency checklist normal-language vì đây là thao tác xóa: xem resource, xác nhận account/Region/project, export cần thiết, execute, scan lại.

**Commit:** `feat: add safe AWS deployment lifecycle scripts`

### Task 13 - Viết tuần 21-24 và checkpoint 6

**Tạo:** `week-21.md` đến `week-24.md`, `checkpoint-06.md`, lab 20, `aws/README.md`.

Mỗi AWS tuần lặp chính xác lifecycle:

```text
Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit
```

1. Tuần 21: account plan, IAM, Budgets caveat, tagging, S3 artifact checksum.
2. Tuần 22: private Lambda invoke, logs, invalid payload, cleanup.
3. Tuần 23: capstone end-to-end; API public optional, ngắn hạn, xóa trong buổi.
4. Tuần 24: demo, portfolio, incident scenario, residual report và billing review.
5. Mỗi tuần có stop conditions: sai account, sai Region, không có budget/acknowledgment, resource name collision, artifact quá cap.

**Commit:** `docs: add guarded AWS capstone phase`

### Task 14 - Hoàn thiện Capstone A tabular

**Tạo:** toàn bộ `capstones/tabular-churn/`.

Rubric 100 điểm:

- Problem/data contract: 10.
- Reproducible baseline/pipeline: 20.
- Evaluation/threshold/error analysis: 20.
- Code/test/artifact quality: 20.
- AWS lifecycle/cost safety: 20.
- Communication/model card/demo: 10.

Gates bất kể điểm: không data leakage; không secret; cleanup/residual evidence; không forbidden resource.

Acceptance command:

```powershell
pwsh scripts/check.ps1 -Scope capstone-tabular -Profile mini
```

**Commit:** `feat: complete tabular AWS capstone package`

### Task 15 - Hoàn thiện Capstone B CV

**Tạo:** toàn bộ `capstones/cv-image-classification/`.

1. Hai notebook wrapper Colab/Kaggle dùng cùng config/source.
2. README yêu cầu chọn một nền tảng, không chạy cả hai.
3. Artifact upload S3 là optional; AWS endpoint/training chỉ là ADR/cost exercise.
4. `aws-adr.md` so sánh Lambda, batch và managed endpoint nhưng kết luận theo constraint, không mặc định triển khai.
5. Rubric tập trung reproducibility, efficiency, per-class error analysis, model card, không thưởng việc dùng GPU lâu hơn.

```powershell
pwsh scripts/check.ps1 -Scope capstone-cv -Profile cpu-mini
```

**Commit:** `feat: complete free-compute CV capstone package`

### Task 16 - Source registry và fact validation

**Tạo:** `docs/sources.yml`, `scripts/validate_sources.py`, `tests/curriculum/test_sources.py`.

Mỗi source record:

```yaml
- id: aws-free-tier-overview
  url: https://aws.amazon.com/free/
  authority: primary
  supports: [R06]
  verified_on: 2026-08-12
  recheck_after: 2027-02-12
  volatile: true
```

1. Validator bắt URL HTTPS, authority, supports, verified date và recheck date cho claim volatile.
2. Link check chạy riêng, retry giới hạn; CI có thể warning khi site chặn bot nhưng schema vẫn hard fail.
3. DOCX hiển thị ngày kiểm chứng cho AWS/Colab/Kaggle current-state facts.

**Commit:** `docs: add verifiable primary-source registry`

### Task 17 - Sinh DOCX từ curriculum source

**Tạo:** `scripts/build_docx.py`, `tests/curriculum/test_docx_content.py`, `dist/ML-Roadmap-24-Tuan-AWS-Cloud-Club.docx`.

1. Dùng Python runtime/package do workspace dependency loader trả về; không dùng system Python.
2. Preset `compact_reference_guide` với token chính xác từ skill Documents:
   - Letter 8.5 x 11 inch, lề 1 inch, header/footer 0.492 inch.
   - Calibri 11 pt, body after 6 pt, line spacing 1.25.
   - H1 16 pt, H2 13 pt, H3 12 pt với màu/spacing preset.
   - Table width 9360 DXA, indent 120 DXA, cell margins 80/80/120/120.
3. Named override `cost_warning`: fill vàng nhạt, border cam đậm, label `CẢNH BÁO CHI PHÍ`; dùng đúng một style.
4. Dựng cover, TOC tĩnh, phase overview, 24 weekly sections, Colab/Kaggle guides, AWS safety, labs, capstones, rubric, glossary và sources.
5. Bảng dài repeat header; không split row khi có thể; column widths theo content.
6. Header/footer có tên chương trình và page number; accessibility: heading thật, alt text nếu có hình, không truyền thông tin chỉ bằng màu.
7. Content tests mở DOCX kiểm đủ 24 tiêu đề tuần, các cảnh báo bắt buộc, URL nguồn, hai capstone và cleanup lifecycle.

```powershell
$python = 'C:\Users\Admin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $python scripts/build_docx.py --curriculum curriculum/curriculum.yml --output dist/ML-Roadmap-24-Tuan-AWS-Cloud-Club.docx
& $python -m pytest tests/curriculum/test_docx_content.py -q
```

Khi thực thi, không hardcode runtime path trong repo; command trên là receipt của môi trường hiện tại. Script repo nhận interpreter đang chạy.

**Commit:** `docs: generate 24-week ML Engineer roadmap DOCX`

### Task 18 - Render và visual QA DOCX

**Dùng:** Documents skill renderer.

```powershell
$python = 'C:\Users\Admin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$skill = 'C:\Users\Admin\.codex\plugins\cache\openai-primary-runtime\documents\26.805.11740\skills\documents'
& $python "$skill/render_docx.py" dist/ML-Roadmap-24-Tuan-AWS-Cloud-Club.docx --output_dir .artifacts/docx-render --emit_pdf
& $python "$skill/scripts/a11y_audit.py" dist/ML-Roadmap-24-Tuan-AWS-Cloud-Club.docx
```

1. Chạy preset/style/table geometry audit.
2. Mở **tất cả** `page-*.png` ở 100%.
3. Kiểm cover, TOC, tiếng Việt, table wrapping, page breaks, repeated headers, footer/page number, cost callout.
4. Sửa builder, build lại, render lại; không sửa DOCX thủ công.
5. Không giao PNG/PDF QA trừ khi được yêu cầu.

**Exit:** không clipping, overlap, missing glyph, orphan heading hoặc bảng vỡ.

**Commit:** `fix: polish roadmap document rendering`

### Task 19 - CI và repository hygiene

**Tạo:** `.github/workflows/ci.yml`, templates GitHub.

CI jobs:

1. `curriculum`: schema/workload/path/source validation.
2. `python`: lint, typecheck, unit/integration mini.
3. `notebooks`: structure + secret/output scan; không chạy GPU.
4. `aws-safety`: template/cost-policy/cleanup mock tests; tuyệt đối không deploy.
5. `docs`: build DOCX structural test; render có thể tách local nếu LibreOffice không có.
6. `security`: dependency/secret scan bằng công cụ được repo chọn và pin sau research.

```powershell
pwsh scripts/check.ps1 -Scope all -Profile ci
```

**Expected:** một command local tái hiện các gate CI quan trọng.

**Commit:** `ci: validate curriculum code notebooks and AWS safety`

### Task 20 - Final verification và release packet

**Tạo:** `.artifacts/release-verification.json`, `.artifacts/traceability.md`; không commit raw logs trừ khi policy repo yêu cầu.

1. Fresh setup trên PowerShell; nếu có môi trường POSIX, chạy `.sh` parity.
2. Run curriculum/source checks.
3. Run unit, integration, CPU mini train, API smoke.
4. Run notebook validators.
5. Run AWS safety/cleanup mocked tests.
6. Build DOCX; render và inspect mọi trang.
7. Run secret/large-file scan.
8. Map R01-R12 tới test/evidence.
9. Ghi residual risks: live Colab/Kaggle availability; AWS pricing/offer changes; chưa deploy AWS thật.

```powershell
pwsh scripts/check.ps1 -Scope all -Profile release
```

**Expected:** exit 0; verification JSON liệt kê command, timestamp, status, artifact checksum.

**Commit:** `chore: verify ML roadmap release`

## 8. Traceability dự kiến

| Requirement | Planned tests/evidence |
|---|---|
| R01 | `test_curriculum.py`, weekly path scan, DOCX heading count |
| R02 | curriculum phase/objective validation, capstone rubric review |
| R03 | CPU mini integration tests, environment matrix |
| R04 | notebook contract tests, source notes, CPU fallback smoke |
| R05 | capstone check commands và rubric schemas |
| R06 | AWS denylist/static validator, lab lifecycle content test |
| R07 | bootstrap check, link/path validation, CI |
| R08 | unit/integration/API/CV mini tests |
| R09 | cleanup mock tests, PS/Bash interface parity, residual scan fixture |
| R10 | DOCX structural audit, render PNG visual QA, a11y audit |
| R11 | `sources.yml` schema + link/source review |
| R12 | secret scan, notebook output scan, `.gitignore` tests |

## 9. Verification order

1. Static schema and path validation.
2. Unit tests.
3. Tabular/CV mini integration tests trên CPU.
4. Notebook structure and secret scan.
5. AWS template/cost/cleanup mocked tests.
6. Full repository check.
7. DOCX build, structural audit, render, visual QA.
8. Release traceability and checksum.

## 10. Suspension criteria

Dừng release nếu:

- Một AWS template tạo resource ngoài allowlist hoặc thiếu cleanup path.
- Cleanup có thể chạm resource không đúng project/tag/prefix.
- Có credential, token, model hoặc dataset lớn trong Git.
- CPU mini path không hoàn thành.
- Một tuần vượt 10 giờ core workload mà chưa chuyển phần dư sang stretch.
- DOCX không render được vì lỗi nội dung/layout; chỉ ngoại lệ khi thiếu LibreOffice và phải báo rõ.
- Claim về pricing/quota/account plan không có nguồn chính thức được kiểm lại.

## 11. Definition of ready cho người học

- Clone -> setup -> quick check trong tối đa 15 phút trên máy phù hợp yêu cầu.
- Tuần 1 bắt đầu mà không cần AWS, Kaggle hoặc Colab account.
- Tuần 17 vẫn có CPU mini path nếu không nhận GPU miễn phí.
- Tuần 21 có thể dừng trước deploy và vẫn học được IAM/cost reasoning.
- AWS lab mặc định không yêu cầu Paid Plan; mọi optional paid-capable path đánh dấu rõ và tắt mặc định.
- Người học hoàn tất có hai portfolio package độc lập: tabular end-to-end và CV experiment/review.

## 12. Self-review receipt

- **Spec coverage:** R01-R12 đều có task triển khai và planned evidence trong traceability.
- **Cost coverage:** denylist, artifact cap, budget caveat, dry-run, allowlist cleanup, residual scan và mock tests đã có owner/task.
- **Learning coverage:** đủ 24 tuần, sáu checkpoint, 20 lab, hai capstone và ba môi trường local/Colab/Kaggle.
- **Placeholder scan:** không có `TODO`, `TBD`, “implement later”, “similar to” hoặc bước kiểm thử chung chung.
- **Contract consistency:** tên command cleanup, config profile, requirement ID và output path nhất quán giữa các task.
- **Residual gap:** quota/availability miễn phí và pricing là dữ liệu biến động; Task 8/10/16 bắt research lại ngay trước authoring và ghi ngày kiểm chứng.
