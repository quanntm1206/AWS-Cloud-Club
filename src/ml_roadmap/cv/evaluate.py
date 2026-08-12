from __future__ import annotations

from sklearn.metrics import f1_score, precision_recall_fscore_support


def per_class_metrics(
    truth: list[int], predicted: list[int], labels: list[int]
) -> dict[str, object]:
    precision, recall, f1, support = precision_recall_fscore_support(
        truth, predicted, labels=labels, zero_division=0
    )
    return {
        "macro_f1": float(f1_score(truth, predicted, average="macro")),
        "classes": {
            str(label): {
                "precision": float(precision[index]),
                "recall": float(recall[index]),
                "f1": float(f1[index]),
                "support": int(support[index]),
            }
            for index, label in enumerate(labels)
        },
    }


def failure_records(
    truth: list[int], predicted: list[int], ids: list[str]
) -> list[dict[str, object]]:
    return [
        {"id": item_id, "truth": expected, "predicted": actual}
        for item_id, expected, actual in zip(ids, truth, predicted, strict=True)
        if expected != actual
    ]

