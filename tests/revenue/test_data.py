from pathlib import Path

import pandas as pd
import pytest

from ml_roadmap.revenue.data import (
    aggregate_daily,
    build_forecast_features,
    engineer_features,
    load_revenue_csv,
)


def _records(days: int = 20) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for offset, date in enumerate(pd.date_range("2024-01-01", periods=days)):
        rows.extend(
            [
                {"date": date, "country": "Viet Nam", "revenue": 100.0 + offset},
                {"date": date, "country": "France", "revenue": 80.0 + offset * 2},
            ]
        )
    return pd.DataFrame(rows)


def test_load_revenue_csv_normalizes_and_validates_schema(tmp_path: Path) -> None:
    path = tmp_path / "revenue.csv"
    frame = _records(2)
    frame.to_csv(path, index=False)

    loaded = load_revenue_csv(path)

    assert list(loaded.columns) == ["date", "country", "revenue"]
    assert set(loaded["country"]) == {"viet_nam", "france"}
    assert pd.api.types.is_datetime64_any_dtype(loaded["date"])


@pytest.mark.parametrize(
    "frame,match",
    [
        (pd.DataFrame({"date": ["2024-01-01"]}), "missing required columns"),
        (
            pd.DataFrame({"date": ["bad"], "country": ["france"], "revenue": [1]}),
            "invalid dates",
        ),
        (
            pd.DataFrame({"date": ["2024-01-01"], "country": ["france"], "revenue": [-1]}),
            "non-negative",
        ),
        (
            pd.DataFrame({"date": ["2024-01-01"], "country": [None], "revenue": [1]}),
            "non-empty",
        ),
        (
            pd.DataFrame({"date": ["2024-01-01"], "country": ["france"], "revenue": [float("inf")]}),
            "finite",
        ),
    ],
)
def test_load_revenue_csv_rejects_invalid_data(
    tmp_path: Path, frame: pd.DataFrame, match: str
) -> None:
    path = tmp_path / "bad.csv"
    frame.to_csv(path, index=False)
    with pytest.raises(ValueError, match=match):
        load_revenue_csv(path)


def test_aggregate_daily_supports_country_and_all() -> None:
    frame = _records(3)

    france = aggregate_daily(frame, "france")
    combined = aggregate_daily(frame, "all")

    assert france["revenue"].tolist() == [80.0, 82.0, 84.0]
    assert combined["revenue"].tolist() == [180.0, 183.0, 186.0]
    with pytest.raises(ValueError, match="unknown country"):
        aggregate_daily(frame, "missing")


def test_engineer_features_is_chronological_and_leakage_safe() -> None:
    daily = aggregate_daily(_records(20), "france")

    features, target, dates = engineer_features(daily)

    assert list(features.columns) == [
        "day_of_week",
        "month",
        "trend",
        "lag_1",
        "lag_7",
        "rolling_mean_7",
    ]
    assert dates.is_monotonic_increasing
    assert features.iloc[0]["lag_1"] == daily.iloc[6]["revenue"]
    assert features.iloc[0]["rolling_mean_7"] == pytest.approx(
        daily.iloc[:7]["revenue"].mean()
    )
    assert target.iloc[0] == daily.iloc[7]["revenue"]


def test_build_forecast_features_uses_only_saved_history() -> None:
    daily = aggregate_daily(_records(20), "france")

    features = build_forecast_features(daily, pd.Timestamp("2024-02-01"))

    assert features.shape == (1, 6)
    assert features.iloc[0]["lag_1"] == daily.iloc[-1]["revenue"]
    assert features.iloc[0]["lag_7"] == daily.iloc[-7]["revenue"]
    assert features.iloc[0]["rolling_mean_7"] == pytest.approx(
        daily.iloc[-7:]["revenue"].mean()
    )
