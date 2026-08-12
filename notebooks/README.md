# Notebook execution paths

- Tabular notebooks: local CPU mặc định.
- CV notebooks: chọn Colab Free **hoặc** Kaggle Free.
- Chạy `cpu-mini` trước; `gpu-free` chỉ khi accelerator có sẵn.
- Notebook bắt buộc có environment check, seed/config, mini fallback, validation, baseline, training,
  evaluation, error analysis, artifact export và runtime release.
- Không lưu secret trong cell; không commit output lớn hoặc checkpoint.

Hướng dẫn chi tiết: `docs/source-notes/colab-free.md`, `docs/source-notes/kaggle-notebooks.md`.

