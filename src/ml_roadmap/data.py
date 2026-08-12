from __future__ import annotations

import numpy as np
import pandas as pd


def make_demo_churn_data(rows: int = 200, seed: int = 42) -> pd.DataFrame:
    if rows < 20:
        raise ValueError("rows must be at least 20")
    rng = np.random.default_rng(seed)
    age = rng.integers(18, 75, size=rows)
    tenure = rng.integers(0, 73, size=rows)
    monthly_charge = rng.normal(70, 22, size=rows).clip(15, 160)
    region = rng.choice(["north", "central", "south"], size=rows)
    contract = rng.choice(["monthly", "annual"], p=[0.65, 0.35], size=rows)
    logit = (
        -0.2
        + 0.025 * (monthly_charge - 70)
        - 0.035 * tenure
        + 0.9 * (contract == "monthly")
        + 0.25 * (region == "south")
    )
    probability = 1 / (1 + np.exp(-logit))
    churn = rng.binomial(1, probability)
    return pd.DataFrame(
        {
            "age": age,
            "tenure_months": tenure,
            "monthly_charge": monthly_charge.round(2),
            "region": region,
            "contract": contract,
            "churn": churn,
        }
    )


def split_features_target(frame: pd.DataFrame, target: str) -> tuple[pd.DataFrame, pd.Series]:
    if target not in frame.columns:
        raise ValueError(f"target column not found: {target}")
    return frame.drop(columns=target), frame[target]
