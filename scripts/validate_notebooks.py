from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_HEADINGS = (
    "Environment check",
    "Configuration and seed",
    "Data validation",
    "Baseline",
    "Training",
    "Evaluation and error analysis",
    "Save artifacts and manifest",
    "Release runtime",
)
SECRET_MARKERS = ("AKIA", "aws_secret_access_key", "kaggle.json")
EXECUTABLE_MARKERS = (
    "DataLoader",
    "resnet18",
    "loss.backward",
    "torch.save",
    "confusion_matrix",
    "metrics.json",
    "failure_examples",
    "except Exception",
    "shutil.make_archive",
    "WEIGHTS.transforms().mean",
    "optimizer.state_dict",
    "optimizer.load_state_dict",
    "best_validation_loss",
    "class_names",
    "UNFREEZE_LAST_BLOCK",
    "fine_tune_history.append",
    "save_failure_image",
    "failure-images",
    "ImageDraw",
    "failure_evidence",
    "exported all instead of padding to 20",
    "weights=WEIGHTS",
    "best_checkpoint_path",
    "last_checkpoint_path",
    "torch.save(checkpoint,last_checkpoint_path)",
    "RandomHorizontalFlip",
    "train_transform",
    "eval_transform",
    "weighted_f1",
    "confusion_matrix_normalized",
    "failure_candidates",
    "error_type",
    "confident-wrong",
    "RUN_EPOCHS",
    "target_epoch=start_epoch+RUN_EPOCHS",
    "range(start_epoch,target_epoch)",
    "build_transforms",
    "RUN_EPOCHS=1; SAMPLES=160; BATCH_SIZE=8; IMAGE_SIZE=96",
    "shutil.unpack_archive",
    "resume_checkpoint_path",
    "raise FileNotFoundError",
    "best_model_state",
    "checkpoint['best_model']",
    "shutil.unpack_archive(uploaded_archive_path,Path('artifacts'))",
    "torch.save(checkpoint,best_checkpoint_path)",
)

MIRRORS = {
    ROOT / "notebooks/colab/cv_transfer_learning_colab.ipynb": ROOT
    / "capstones/cv-image-classification/notebooks/colab.ipynb",
    ROOT / "notebooks/kaggle/cv_transfer_learning_kaggle.ipynb": ROOT
    / "capstones/cv-image-classification/notebooks/kaggle.ipynb",
}


def validate_notebook(path: Path) -> list[str]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    text = "\n".join("".join(cell.get("source", [])) for cell in notebook.get("cells", []))
    errors = [f"{path}: missing heading {heading}" for heading in REQUIRED_HEADINGS if heading not in text]
    for index, cell in enumerate(notebook.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        try:
            compile("".join(cell.get("source", [])), f"{path}:cell-{index}", "exec")
        except SyntaxError as error:
            errors.append(f"{path}: code cell {index} syntax error: {error.msg} at line {error.lineno}")
    if "cpu-mini" not in text or "cuda" not in text.lower():
        errors.append(f"{path}: missing device-aware CPU fallback")
    for marker in SECRET_MARKERS:
        if marker.lower() in text.lower():
            errors.append(f"{path}: possible secret marker {marker}")
    output_bytes = sum(len(json.dumps(cell.get("outputs", []))) for cell in notebook.get("cells", []))
    if output_bytes > 100_000:
        errors.append(f"{path}: saved outputs exceed 100 KB")
    if "transfer_learning" in path.name or "capstones" in path.parts:
        for marker in EXECUTABLE_MARKERS:
            if marker not in text:
                errors.append(f"{path}: missing executable CV marker {marker}")
    return errors


def main() -> int:
    notebooks = sorted((ROOT / "notebooks").rglob("*.ipynb")) + sorted(
        (ROOT / "capstones").glob("*/notebooks/*.ipynb")
    )
    errors = [error for path in notebooks for error in validate_notebook(path)]
    for source, mirror in MIRRORS.items():
        if not mirror.exists() or source.read_bytes() != mirror.read_bytes():
            errors.append(f"{mirror}: drifted from canonical notebook {source}")
    if errors or not notebooks:
        print("NOTEBOOKS FAIL")
        print("\n".join(f"- {error}" for error in errors or ["no notebooks found"]))
        return 1
    print(f"NOTEBOOKS PASS: {len(notebooks)} notebook(s) satisfy the execution contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
