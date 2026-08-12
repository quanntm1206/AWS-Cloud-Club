from __future__ import annotations


def transfer_learning_policy(profile: str) -> dict[str, object]:
    return {
        "backbone": "resnet18",
        "pretrained": True,
        "freeze_backbone": True,
        "fine_tune": profile == "gpu-free",
        "max_epochs": 5,
    }

