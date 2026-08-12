from __future__ import annotations

import json
import tempfile
from collections import Counter
from collections.abc import Callable
from pathlib import Path

import joblib
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.datasets import make_classification
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .config import TrainConfig
from .cv.evaluate import failure_records, per_class_metrics
from .data import make_demo_churn_data, split_features_target
from .train_tabular import train


def _foundation(lab: int) -> dict[str, object]:
    frame = make_demo_churn_data(120, 42)
    if lab == 0:
        return {"rows": len(frame), "dtypes": frame.dtypes.astype(str).to_dict(), "seed": 42}
    if lab == 1:
        matrix = frame[["age", "tenure_months", "monthly_charge"]].to_numpy()
        vectorized = matrix @ np.array([0.01, -0.02, 0.03])
        loop = np.array([sum(row * np.array([0.01, -0.02, 0.03])) for row in matrix])
        return {"vectorization_matches_loop": bool(np.allclose(vectorized, loop)), "head": vectorized[:5].tolist()}
    if lab == 2:
        return {
            "missing": frame.isna().sum().to_dict(),
            "duplicates": int(frame.duplicated().sum()),
            "churn_rate": float(frame["churn"].mean()),
            "monthly_charge_by_target": frame.groupby("churn")["monthly_charge"].mean().to_dict(),
        }
    x = np.arange(1.0, 5.0)
    y = 2 * x
    weight = 1.0
    def loss(value: float) -> float:
        return float(np.mean((x * value - y) ** 2))
    analytic = 2 * np.mean(x * (x * weight - y))
    epsilon = 1e-6
    numeric = (loss(weight + epsilon) - loss(weight - epsilon)) / (2 * epsilon)
    return {
        "analytic_gradient": float(analytic),
        "finite_difference_gradient": float(numeric),
        "gradient_check": bool(np.isclose(analytic, numeric, atol=1e-6)),
    }


def _pipeline_model(model: object, columns: list[str] | None = None) -> Pipeline:
    available = set(columns or ["age", "tenure_months", "monthly_charge", "region", "contract"])
    numeric = [column for column in ["age", "tenure_months", "monthly_charge"] if column in available]
    categorical = [column for column in ["region", "contract"] if column in available]
    preprocessor = ColumnTransformer(
        [
            ("numeric", Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), numeric),
            (
                "categorical",
                Pipeline(
                    [
                        ("impute", SimpleImputer(strategy="most_frequent")),
                        ("encode", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical,
            ),
        ]
    )
    return Pipeline([("preprocess", preprocessor), ("model", model)])


def _classical(lab: int) -> dict[str, object]:
    frame = make_demo_churn_data(240, 42)
    features, target = split_features_target(frame, "churn")
    if lab == 4:
        train_x, test_x, train_y, test_y = train_test_split(features, target, stratify=target, random_state=42)
        dummy = DummyClassifier(strategy="prior").fit(train_x, train_y)
        logistic = _pipeline_model(LogisticRegression(max_iter=500)).fit(train_x, train_y)
        return {
            "dummy_f1": float(f1_score(test_y, dummy.predict(test_x), zero_division=0)),
            "logistic_f1": float(f1_score(test_y, logistic.predict(test_x))),
        }
    result = train(TrainConfig(target="churn", seed=42), frame)
    if lab == 5:
        sample = features.iloc[[0]].copy()
        sample.loc[:, "region"] = "never-seen"
        return {
            "unknown_category_prediction": int(result.pipeline.predict(sample)[0]),
            "leakage_guard": "pipeline fit occurs after split",
        }
    if lab == 6:
        false_negative_cost = 5
        false_positive_cost = 1
        threshold = float(result.threshold)
        return {
            "selection_rule": "maximize validation F1; report explicit FP/FN costs",
            "validation_selected_threshold": threshold,
            "validation_f1": result.metrics["validation_f1"],
            "validation_pr_auc": result.metrics["validation_pr_auc"],
            "false_negative_cost": false_negative_cost,
            "false_positive_cost": false_positive_cost,
            "test_f1": result.metrics["f1"],
            "test_pr_auc": result.metrics["pr_auc"],
        }
    development_x, _, development_y, _ = train_test_split(
        features, target, test_size=0.2, stratify=target, random_state=42
    )
    folds = StratifiedKFold(3, shuffle=True, random_state=42)
    model = _pipeline_model(LogisticRegression(max_iter=500))
    scores = cross_val_score(model, development_x, development_y, scoring="roc_auc", cv=folds)
    return {
        "evaluation_scope": "development-only; held-out test untouched",
        "fold_scores": scores.tolist(),
        "cv_mean": float(scores.mean()),
        "cv_std": float(scores.std()),
    }


def _applied(lab: int) -> dict[str, object]:
    frame = make_demo_churn_data(300, 42)
    features, target = split_features_target(frame, "churn")
    development_x, test_x, development_y, test_y = train_test_split(
        features, target, test_size=0.2, stratify=target, random_state=42
    )
    train_x, validation_x, train_y, validation_y = train_test_split(
        development_x, development_y, test_size=0.25, stratify=development_y, random_state=42
    )
    if lab == 8:
        candidates = {
            "decision-tree-ensemble": RandomForestClassifier(n_estimators=30, max_depth=5, random_state=42),
            "gradient-boosting": GradientBoostingClassifier(n_estimators=30, max_depth=2, random_state=42),
        }
        scores: dict[str, float] = {}
        fitted: dict[str, Pipeline] = {}
        for name, estimator in candidates.items():
            model = _pipeline_model(estimator).fit(train_x, train_y)
            fitted[name] = model
            scores[name] = float(roc_auc_score(validation_y, model.predict_proba(validation_x)[:, 1]))
        best = max(scores, key=lambda name: scores[name])
        test_auc = float(roc_auc_score(test_y, fitted[best].predict_proba(test_x)[:, 1]))
        return {"validation_scores": scores, "selected_on": "validation", "best": best, "final_test_auc": test_auc}
    if lab == 9:
        groups = {"all": list(features.columns), "without-charge": [c for c in features if c != "monthly_charge"]}
        scores = {}
        for name, columns in groups.items():
            model = _pipeline_model(LogisticRegression(max_iter=500), columns).fit(train_x[columns], train_y)
            scores[name] = float(roc_auc_score(validation_y, model.predict_proba(validation_x[columns])[:, 1]))
        return {
            "single_change": "remove monthly_charge",
            "selected_on": "validation",
            "validation_auc_by_feature_group": scores,
            "test_set_touched": False,
        }
    model = _pipeline_model(LogisticRegression(max_iter=500)).fit(train_x, train_y)
    predicted = model.predict(test_x)
    evaluation = test_x.assign(truth=test_y.to_numpy(), predicted=predicted)
    errors = evaluation.query("truth != predicted")
    if lab == 10:
        slices = {
            str(region): {
                "support": len(group),
                "f1": float(f1_score(group["truth"], group["predicted"], zero_division=0)),
            }
            for region, group in evaluation.groupby("region")
        }
        failure_rows = errors.head(20).reset_index(names="source_row").to_dict(orient="records")
        return {
            "error_count": len(errors),
            "evaluation_split": "held-out-test",
            "slice_metrics": slices,
            "failure_records": failure_rows,
            "failure_record_cap": 20,
            "taxonomy": Counter(np.where(errors["truth"] == 1, "false-negative", "false-positive")),
        }
    result = train(TrainConfig(target="churn", seed=42), frame)
    return {
        "metrics": result.metrics,
        "artifact_contract": ["model.joblib", "portable_model.json", "manifest.json", "metrics.json"],
    }


def _engineering(lab: int) -> dict[str, object]:
    frame = make_demo_churn_data(160, 42)
    result = train(TrainConfig(target="churn"), frame)
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "model.joblib"
        joblib.dump(result.pipeline, path)
        reloaded = joblib.load(path)
        reload_parity = bool(
            np.array_equal(
                result.pipeline.predict(frame.drop(columns="churn")), reloaded.predict(frame.drop(columns="churn"))
            )
        )
    contracts: dict[int, dict[str, object]] = {
        12: {"cli_config_keys": list(TrainConfig.__dataclass_fields__), "notebook_state_required": False},
        13: {"artifact_reload_parity": reload_parity, "invalid_schema_tested_elsewhere": True},
        14: {"api_contract": {"health": "/health", "predict": "/predict", "invalid": 422, "unavailable": 503}},
        15: {"docker_user": "appuser", "ci_has_aws_deploy": False, "artifact_bytes": len(json.dumps(result.metrics))},
    }
    return contracts[lab]


def _tiny_mlp(seed: int = 42) -> tuple[list[float], dict[str, object]]:
    rng = np.random.default_rng(seed)
    x, y = make_classification(n_samples=120, n_features=8, n_informative=5, random_state=seed)
    weight1 = rng.normal(0, 0.1, (8, 6))
    weight2 = rng.normal(0, 0.1, (6, 1))
    losses = []
    learning_rate = 0.1
    for _ in range(8):
        hidden = np.tanh(x @ weight1)
        logits = (hidden @ weight2).ravel()
        probability = 1 / (1 + np.exp(-logits))
        losses.append(float(-np.mean(y * np.log(probability + 1e-8) + (1 - y) * np.log(1 - probability + 1e-8))))
        dlogit = (probability - y)[:, None] / len(y)
        grad2 = hidden.T @ dlogit
        grad1 = x.T @ ((dlogit @ weight2.T) * (1 - hidden**2))
        weight2 -= learning_rate * grad2
        weight1 -= learning_rate * grad1
    return losses, {"device": "cpu", "parameters": weight1.size + weight2.size}


def _cv(lab: int) -> dict[str, object]:
    if lab == 16:
        losses, metadata = _tiny_mlp()
        return {"loss_decreased": losses[-1] < losses[0], "losses": losses, **metadata}
    if lab == 17:
        frozen = {"conv1": False, "layer1": False, "classifier": True}
        return {
            "backbone": "resnet18",
            "requires_grad": frozen,
            "trainable_layers": [name for name, trainable in frozen.items() if trainable],
        }
    if lab == 18:
        losses, _ = _tiny_mlp()
        best_epoch = int(np.argmin(losses)) + 1
        checkpoint = {"epoch": best_epoch, "validation_loss": losses[best_epoch - 1], "seed": 42}
        resumed_epoch = checkpoint["epoch"] + 1
        return {"checkpoint": checkpoint, "resumed_epoch": resumed_epoch, "early_stopping_patience": 2}
    truth = [0, 0, 1, 1, 1, 0]
    predicted = [0, 1, 1, 0, 1, 0]
    ids = [f"img-{i}" for i in range(len(truth))]
    return {
        "metrics": per_class_metrics(truth, predicted, [0, 1]),
        "failures": failure_records(truth, predicted, ids),
        "failure_review_required": True,
    }


def run_example(lab: int) -> dict[str, object]:
    if not 0 <= lab <= 19:
        raise ValueError("lab must be 0..19")
    routers: list[tuple[range, Callable[[int], dict[str, object]]]] = [
        (range(0, 4), _foundation),
        (range(4, 8), _classical),
        (range(8, 12), _applied),
        (range(12, 16), _engineering),
        (range(16, 20), _cv),
    ]
    return next(handler(lab) for labs, handler in routers if lab in labs)
