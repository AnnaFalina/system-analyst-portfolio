
"""Тесты для tariff_check.py. Запуск: pytest -q"""

import pandas as pd
import pytest

from tariff_check import compare_tariffs, problem_share


@pytest.fixture
def orders() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5],
            "tariff": ["обычный", "обычный", "обычный", "экспресс", "экспресс"],
            "status": ["выдан", "выдан", "проблема", "проблема", "выдан"],
        }
    )


def test_problem_share_usual(orders):
    # 1 проблема из 3 обычных = 33.33%
    assert problem_share(orders, "обычный") == 33.33


def test_problem_share_express(orders):
    # 1 проблема из 2 экспресс = 50.0%
    assert problem_share(orders, "экспресс") == 50.0


def test_compare_tariffs_ratio(orders):
    result = compare_tariffs(orders)
    assert result["обычный"] == 33.33
    assert result["экспресс"] == 50.0
    assert result["ratio"] == 1.5


def test_unknown_tariff_returns_zero(orders):
    assert problem_share(orders, "несуществующий") == 0.0
