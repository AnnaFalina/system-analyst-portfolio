# SQL-проверки гипотез

Проверка требований и гипотез на данных после нескольких месяцев работы системы.

## Проверка 1. Неоплаченные выданные заказы

**Требование:** заказ нельзя выдать без полной оплаты.

```sql
SELECT o.id AS order_id,
       o.amount AS стоимость_заказа,
       SUM(p.amount) AS сумма_платежей
FROM orders o
JOIN payments p ON p.order_id = o.id
WHERE o.status IN ('выдан', 'доставлен')
GROUP BY o.id, o.amount
HAVING SUM(p.amount) < o.amount;
SELECT 100.0 * COUNT(*) / (
  SELECT COUNT(*) FROM orders WHERE tariff = 'обычный'
) AS процент_проблем
FROM orders
WHERE tariff = 'обычный' AND status = 'проблема';


SELECT id, ready_date,
       DATE '2026-08-05' - ready_date AS время_хранения
FROM orders
WHERE pickup_date IS NULL
  AND ready_date IS NOT NULL
  AND DATE '2026-08-05' - ready_date >= 25;
