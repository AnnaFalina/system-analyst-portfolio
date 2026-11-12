 
import pandas as pd
from pathlib import Path

# Путь к файлу данных (лежит в папке data рядом со скриптом)
DATA_PATH = Path(__file__).parent / "data" / "orders.csv"

def load_orders(path: Path = DATA_PATH) -> pd.DataFrame:
    # Указываем, что колонка order_id — это именно ID заказа
    df = pd.read_csv(path)
    return df

def problem_share(df: pd.DataFrame, tariff: str) -> float:
    # Ищем заказы по тарифу
    subset = df[df["tariff"] == tariff]
    if subset.empty:
        return 0.0
    # Считаем, сколько из них в статусе "проблема"
    problems = (subset["status"] == "проблема").sum()
    return round(100.0 * problems / len(subset), 2)

def main() -> None:
    df = load_orders()
    usual = problem_share(df, "обычный")
    express = problem_share(df, "экспресс")
    
    print(f"Доля проблемных заказов, обычный тариф: {usual}%")
    print(f"Доля проблемных заказов, экспресс тариф: {express}%")
    
    if usual > 0:
        print(f"Соотношение экспресс / обычный: {round(express / usual, 2)}x")

if __name__ == "__main__":
    main()
