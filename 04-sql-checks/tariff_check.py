python

"""
Проверка гипотезы: на тарифе «экспресс» проблемы встречаются чаще,
чем на «обычном».

Аналог SQL-запроса:
    SELECT 100.0 * COUNT(*) / (SELECT COUNT(*) FROM orders WHERE tariff = :t)
    FROM orders
    WHERE tariff = :t AND status = 'проблема';

Запуск:
    python tariff_check.py
"""

from pathlib import Path

import pandas as pd


DATA_PATH = Path(__file__).parent / "data" / "orders.csv"


def load_orders(path: Path = DATA_PATH) -> pd.DataFrame:
    """Загружает заказы из CSV."""
    df = pd.read_csv(path)
    required = {"order_id", "tariff", "status"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"В файле нет колонок: {missing}")
    return df


def problem_share(df: pd.DataFrame, tariff: str) -> float:
    """Доля проблемных заказов на тарифе, в процентах."""
    subset = df[df["tariff"] == tariff]
    if subset.empty:
        return 0.0
    problems = (subset["status"] == "проблема").sum()
    return round(100.0 * problems / len(subset), 2)


def compare_tariffs(df: pd.DataFrame) -> dict:
    """Считает долю проблем по тарифам и их соотношение."""
    usual = problem_share(df, "обычный")
    express = problem_share(df, "экспресс")
    ratio = round(express / usual, 2) if usual else None
    return {"обычный": usual, "экспресс": express, "ratio": ratio}


def main() -> None:
    df = load_orders()
    result = compare_tariffs(df)
    print(f"Доля проблемных заказов, обычный тариф: {result['обычный']}%")
    print(f"Доля проблемных заказов, экспресс тариф: {result['экспресс']}%")
    if result["ratio"] is not None:
        print(f"Соотношение экспресс / обычный: {result['ratio']}x")
    if result["ratio"] and result["ratio"] > 2:
        print("Гипотеза подтвердилась: на экспрессе проблем существенно больше.")


if __name__ == "__main__":
    main()
