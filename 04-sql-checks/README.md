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
