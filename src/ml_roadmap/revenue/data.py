from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd

REQUIRED_COLUMNS = ("date", "country", "revenue")
FEATURE_COLUMNS = (
    "day_of_week",
    "month",
    "trend",
    "lag_1",
    "lag_7",
    "rolling_mean_7",
)


def normalize_country(value: object) -> str:
    if pd.isna(value):
        raise ValueError("country values must be non-empty")
    country = re.sub(r"[^a-z0-9]+", "_", str(value).strip().lower()).strip("_")
    if not country:
        raise ValueError("country values must be non-empty")
    return country


def validate_revenue_frame(frame: pd.DataFrame) -> pd.DataFrame:
    missing = sorted(set(REQUIRED_COLUMNS) - set(frame.columns))
    if missing:
        raise ValueError(f"missing required columns: {missing}")

    clean = frame.loc[:, REQUIRED_COLUMNS].copy()
    parsed_dates = pd.to_datetime(clean["date"], errors="coerce")
    if parsed_dates.isna().any():
        raise ValueError("invalid dates in date column")
    clean["date"] = parsed_dates.dt.normalize()

    try:
        clean["country"] = clean["country"].map(normalize_country)
    except ValueError as exc:
        raise ValueError("country values must be non-empty") from exc

    clean["revenue"] = pd.to_numeric(clean["revenue"], errors="coerce")
    if clean["revenue"].isna().any():
        raise ValueError("revenue values must be numeric")
    if not np.isfinite(clean["revenue"]).all():
        raise ValueError("revenue values must be finite")
    if (clean["revenue"] < 0).any():
        raise ValueError("revenue values must be non-negative")
    return clean.sort_values(["date", "country"], ignore_index=True)


def load_revenue_csv(path: Path) -> pd.DataFrame:
    if not path.is_file():
        raise FileNotFoundError(f"revenue CSV not found: {path}")
    return validate_revenue_frame(pd.read_csv(path))


def aggregate_daily(frame: pd.DataFrame, country: str | None = "all") -> pd.DataFrame:
    clean = validate_revenue_frame(frame)
    label = "all" if country is None else normalize_country(country)
    if label != "all":
        available = set(clean["country"])
        if label not in available:
            raise ValueError(f"unknown country: {label}")
        clean = clean.loc[clean["country"] == label]

    daily = clean.groupby("date", as_index=False)["revenue"].sum().sort_values("date")
    complete_dates = pd.date_range(daily["date"].min(), daily["date"].max(), freq="D")
    return (
        daily.set_index("date")
        .reindex(complete_dates, fill_value=0.0)
        .rename_axis("date")
        .reset_index()
    )


def engineer_features(
    daily: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.Series, pd.Series]:
    ordered = daily.sort_values("date", ignore_index=True).copy()
    ordered["date"] = pd.to_datetime(ordered["date"])
    if len(ordered) < 10:
        raise ValueError("at least 10 daily observations are required")

    features = pd.DataFrame(
        {
            "date": ordered["date"],
            "day_of_week": ordered["date"].dt.dayofweek,
            "month": ordered["date"].dt.month,
            "trend": (ordered["date"] - ordered["date"].min()).dt.days,
            "lag_1": ordered["revenue"].shift(1),
            "lag_7": ordered["revenue"].shift(7),
            "rolling_mean_7": ordered["revenue"].shift(1).rolling(7).mean(),
            "target": ordered["revenue"],
        }
    ).dropna()
    return (
        features.loc[:, FEATURE_COLUMNS].reset_index(drop=True),
        features["target"].reset_index(drop=True),
        features["date"].reset_index(drop=True),
    )


def build_forecast_features(daily: pd.DataFrame, target_date: pd.Timestamp) -> pd.DataFrame:
    ordered = daily.sort_values("date", ignore_index=True).copy()
    ordered["date"] = pd.to_datetime(ordered["date"])
    if len(ordered) < 7:
        raise ValueError("at least 7 daily observations are required for prediction")
    date = pd.Timestamp(target_date).normalize()
    origin = ordered["date"].min()
    return pd.DataFrame(
        [
            {
                "day_of_week": date.dayofweek,
                "month": date.month,
                "trend": (date - origin).days,
                "lag_1": float(ordered.iloc[-1]["revenue"]),
                "lag_7": float(ordered.iloc[-7]["revenue"]),
                "rolling_mean_7": float(ordered.iloc[-7:]["revenue"].mean()),
            }
        ],
        columns=FEATURE_COLUMNS,
    )
