import pandas as pd
import pytest

from ai_generated_growth import (
    share_of_total, yoy_growth)


@pytest.fixture
def trade():
    return pd.DataFrame({
        "reporter": ["A", "A", "B", "B"],
        "year": [2022, 2023, 2022, 2023],
        "exports_usd_m": [100.0, 110.0,
                          50.0, 40.0],
    })


def test_first_year_has_no_growth(trade):
    g = yoy_growth(trade)
    first = g[g["year"] == 2022]["growth_pct"]
    assert first.isna().all()


def test_growth_values(trade):
    g = yoy_growth(trade).set_index(
        ["reporter", "year"])["growth_pct"]
    assert g[("A", 2023)] == 10.0
    assert g[("B", 2023)] == -20.0


def test_shares_sum_to_100(trade):
    s = share_of_total(trade, 2023)
    assert s.sum() == pytest.approx(100, abs=0.1)
