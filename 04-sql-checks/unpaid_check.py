import pandas as pd
from pathlib import Path

# Указываем пути к файлам
BASE_DIR = Path(__file__).parent / "data"
ORDERS_PATH = BASE_DIR / "orders.csv"
PAYMENTS_PATH = BASE_DIR / "payments.csv"

def find_unpaid_orders():
    # 1. Загружаем данные
    orders = pd.read_csv(ORDERS_PATH)
    payments = pd.read_csv(PAYMENTS_PATH)

    # 2. Группируем платежи по заказам и считаем сумму
    # (у одного заказа может быть несколько платежей, как у заказа №3)
    payments_sum = payments.groupby("order_id")["amount"].sum().reset_index()
    payments_sum.rename(columns={"amount": "total_paid"}, inplace=True)

    # 3. Объединяем заказы и суммы их оплат (Left Join)
    merged = pd.merge(orders, payments_sum, on="order_id", how="left")

    # Если заказа нет в таблице платежей, считаем, что оплачено 0
    merged["total_paid"] = merged["total_paid"].fillna(0)

    # 4. Фильтруем: только выданные/доставленные и оплаченные не полностью
    problems = merged[
        (merged["status"].isin(["выдан", "доставлен"])) & 
        (merged["total_paid"] < merged["amount"])
    ]

    return problems

if __name__ == "__main__":
    result = find_unpaid_orders()
    
    if result.empty:
        print("Все выданные заказы оплачены полностью!")
    else:
        print("Внимание! Найдены неоплаченные заказы:")
        for index, row in result.iterrows():
            debt = row['amount'] - row['total_paid']
            print(f"Заказ №{row['order_id']}: сумма {row['amount']} руб., оплачено {row['total_paid']} руб. (Долг: {debt} руб.)")
