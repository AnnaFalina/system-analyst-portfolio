from unpaid_check import find_unpaid_orders

def test_unpaid_orders_found():
    result = find_unpaid_orders()
    
    # Проверяем, что скрипт вообще нашел неоплаченные заказы (или не нашел, если их нет)
    # Самое главное правило: у всех найденных заказов долг должен быть больше нуля!
    for index, row in result.iterrows():
        total_paid = row["total_paid"]
        amount = row["amount"]
        order_id = row["order_id"]
        
        # Проверяем, что оплачено меньше, чем стоимость заказа
        assert total_paid < amount, f"Ошибка в заказе {order_id}: оплачено больше или равно стоимости!"
        
        # Проверяем, что статус действительно "выдан" или "доставлен"
        assert row["status"] in ["выдан", "доставлен"], f"Ошибка в заказе {order_id}: неверный статус!"

def test_all_orders_are_checked():
    # Проверяем, что скрипт не падает и возвращает корректный DataFrame
    result = find_unpaid_orders()
    assert result is not None
