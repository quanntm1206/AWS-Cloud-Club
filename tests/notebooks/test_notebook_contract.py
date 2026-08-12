from pathlib import Path

import pytest

from scripts.validate_notebooks import validate_notebook

ROOT = Path(__file__).resolve().parents[2]


def test_all_notebooks_follow_contract() -> None:
    notebooks = list((ROOT / "notebooks").rglob("*.ipynb")) + list(
        (ROOT / "capstones").glob("*/notebooks/*.ipynb")
    )
    assert notebooks
    assert [error for path in notebooks for error in validate_notebook(path)] == []


def test_cv_notebooks_contain_real_training_and_evaluation() -> None:
    notebooks = list((ROOT / "notebooks").glob("*/cv_transfer_learning_*.ipynb"))
    assert len(notebooks) == 2
    for path in notebooks:
        text = path.read_text(encoding="utf-8")
        assert "loss.backward" in text
        assert "confusion_matrix" in text
        assert "torch.save" in text
        assert "except Exception" in text
        assert "shutil.make_archive" in text
        assert "WEIGHTS.transforms().mean" in text
        assert "optimizer.state_dict" in text
        assert "optimizer.load_state_dict" in text
        assert "best_validation_loss" in text
        assert "UNFREEZE_LAST_BLOCK" in text
        assert "fine_tune_history.append" in text
        assert "save_failure_image" in text
        assert "failure-images" in text
        assert "ImageDraw" in text
        assert "failure_evidence" in text
        assert "exported all instead of padding to 20" in text
        assert "weights=WEIGHTS" in text
        assert "best_checkpoint_path" in text
        assert "last_checkpoint_path" in text
        assert "torch.save(checkpoint,last_checkpoint_path)" in text
        assert "RandomHorizontalFlip" in text
        assert "train_transform" in text and "eval_transform" in text
        assert "weighted_f1" in text
        assert "confusion_matrix_normalized" in text
        assert "failure_candidates" in text
        assert "error_type" in text
        assert "confident-wrong" in text
        assert "RUN_EPOCHS" in text
        assert "target_epoch=start_epoch+RUN_EPOCHS" in text
        assert "range(start_epoch,target_epoch)" in text
        assert "'max_epochs'" not in text
        assert "build_transforms" in text
        assert "RUN_EPOCHS=1; SAMPLES=160; BATCH_SIZE=8; IMAGE_SIZE=96" in text
        assert "shutil.unpack_archive" in text
        assert "resume_checkpoint_path" in text
        assert "raise FileNotFoundError" in text
        assert "best_model_state" in text
        assert "checkpoint['best_model']" in text
        assert "shutil.unpack_archive(uploaded_archive_path,Path('artifacts'))" in text
        assert "torch.save(checkpoint,best_checkpoint_path)" in text


def test_capstone_notebooks_match_canonical_copies() -> None:
    pairs = [
        ("colab/cv_transfer_learning_colab.ipynb", "colab.ipynb"),
        ("kaggle/cv_transfer_learning_kaggle.ipynb", "kaggle.ipynb"),
    ]
    for source, mirror in pairs:
        assert (ROOT / "notebooks" / source).read_bytes() == (
            ROOT / "capstones/cv-image-classification/notebooks" / mirror
        ).read_bytes()


def test_validator_rejects_invalid_code_cell(tmp_path: Path) -> None:
    path = tmp_path / "broken.ipynb"
    path.write_text(
        '{"cells":[{"cell_type":"code","source":["value = \'unterminated"]}]}',
        encoding="utf-8",
    )
    with pytest.raises(AssertionError):
        assert not any("syntax error" in error for error in validate_notebook(path))
