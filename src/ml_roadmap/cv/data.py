from __future__ import annotations


def profile_limits(profile: str) -> dict[str, int]:
    profiles = {
        "cpu-mini": {"image_size": 96, "batch_size": 8, "epochs": 1, "samples": 160},
        "gpu-free": {"image_size": 160, "batch_size": 32, "epochs": 5, "samples": 3000},
    }
    if profile not in profiles:
        raise ValueError(f"unknown profile: {profile}")
    return profiles[profile]

