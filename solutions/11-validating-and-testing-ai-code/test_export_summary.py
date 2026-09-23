"""Tests for export_summary.py (solution).

Run from the repository root:
    pytest solutions/11-validating-and-testing-ai-code -v
"""
import math

import pandas as pd
import pytest

from export_summary import (
    agricultural_share, average_tariff, export_growth, exports_by_region,
    growth_rate, load_data, top_exporters, total_exports, trade_balance,
)


@pytest.fixture
def trade():
    # Two reporters, two years, two products each.
    return pd.DataFrame({
        "reporter":      ["A", "A", "B", "B", "A", "A", "B", "B"],
        "region":        ["X", "X", "Y", "Y", "X", "X", "Y", "Y"],
        "year":          [2022, 2022, 2022, 2022, 2023, 2023, 2023, 2023],
        "product_code":  ["AGR", "MAN", "AGR", "MAN", "AGR", "MAN", "AGR", "MAN"],
        "exports_usd_m": [10.0, 90.0, 50.0, 50.0, 20.0, 100.0, 60.0, 40.0],
        "imports_usd_m": [30.0, 30.0, 70.0, 70.0, 40.0, 40.0, 80.0, 80.0],
    })


@pytest.fixture
def tariffs():
    return pd.DataFrame({
        "iso3": ["AAA", "AAA", "AAA", "BBB"],
        "year": [2022, 2023, 2023, 2023],
        "product_code": ["AGR", "AGR", "MAN", "AGR"],
        "avg_mfn_tariff_pct": [10.0, float("nan"), 20.0, 5.0],
    })


# ---- total_exports ---------------------------------------------------------
def test_total_exports(trade):
    assert total_exports(trade, 2023) == 220.0          # 20 + 100 + 60 + 40


def test_total_exports_missing_year_is_zero(trade):
    assert total_exports(trade, 1999) == 0


# ---- growth_rate / export_growth -------------------------------------------
def test_growth_rate():
    assert growth_rate(100, 110) == pytest.approx(10.0)


def test_growth_rate_decline():
    assert growth_rate(100, 80) == pytest.approx(-20.0)


def test_growth_from_zero_is_undefined():
    assert math.isnan(growth_rate(0, 5))


def test_export_growth(trade):
    g = export_growth(trade, 2022, 2023)
    assert g["A"] == 20.0                                 # 100 -> 120
    assert g["B"] == 0.0                                  # 100 -> 100


# ---- agricultural_share ----------------------------------------------------
def test_agricultural_share_is_percentage(trade):
    s = agricultural_share(trade, 2023)
    assert s["A"] == pytest.approx(16.7, abs=0.05)        # 20 / 120
    assert s["B"] == 60.0                                 # 60 / 100


# ---- trade_balance ---------------------------------------------------------
def test_trade_balance_is_exports_minus_imports(trade):
    b = trade_balance(trade, 2023)
    assert b["A"] == 40.0                                 # 120 - 80
    assert b["B"] == -60.0                                # 100 - 160


# ---- top_exporters ---------------------------------------------------------
def test_top_exporters_largest_first(trade):
    top = top_exporters(trade, 2023, n=1)
    assert list(top.index) == ["A"]


# ---- average_tariff --------------------------------------------------------
def test_average_tariff_ignores_missing(tariffs):
    assert average_tariff(tariffs, "AAA") == pytest.approx(15.0)   # mean of 10, 20


def test_average_tariff_unknown_country_is_nan(tariffs):
    assert math.isnan(average_tariff(tariffs, "ZZZ"))


# ---- exports_by_region -----------------------------------------------------
def test_exports_by_region_in_billions(trade):
    r = exports_by_region(trade, 2023)
    assert r["X"] == pytest.approx(0.1, abs=0.05)         # 120 USD m = 0.12 USD bn


# ---- reconciliation against the real file ----------------------------------
def test_region_totals_reconcile_with_total():
    trade, _ = load_data()
    by_region_m = exports_by_region(trade, 2023).sum() * 1000
    assert by_region_m == pytest.approx(total_exports(trade, 2023), rel=0.001)
