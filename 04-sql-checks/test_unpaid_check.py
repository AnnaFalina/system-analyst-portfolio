import pytest
from unpaid_check import find_unpaid_orders

def test_unpaid_orders_found():
    result = find_unpaid_orders()
    
    # Проверяем, что скрипт нашел ровно 2 проблемных заказа (№8 и №22)
    assert len(result) == 2
    
    # Проверяем, что это именно те заказы
    found_ids = result["order_id"].tolist()
    assert 8 in found_ids
    assert 22 in found_ids
