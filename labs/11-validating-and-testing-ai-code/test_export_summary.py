"""Tests for export_summary.py.

Run from the repository root:
    pytest labs/11-validating-and-testing-ai-code -v

The fixtures are tiny tables where you can work out every answer by hand.
"""
import math

import pandas as pd
import pytest

from export_summary import (
    agricultural_share, average_tariff, export_growth, exports_by_region,
    growth_rate, top_exporters, total_exports, trade_balance,
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


def test_total_exports(trade):
    # 20 + 100 + 60 + 40
    assert total_exports(trade, 2023) == 220.0


def test_growth_rate():
    assert growth_rate(100, 110) == pytest.approx(10.0)


# TODO: write at least one test for each remaining function:
#   export_growth, agricultural_share, trade_balance, top_exporters,
#   average_tariff, exports_by_region
# Work out the expected answers from the fixtures BY HAND first.
