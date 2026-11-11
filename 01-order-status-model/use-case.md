markdown
```mermaid   
sequenceDiagram
    actor Client as Клиент
    participant Staff as Сотрудник пункта
    participant System as Система "Чисто"
    participant SMS as SMS-провайдер

    Client->>Staff: Приносит вещь
    Staff->>System: Создает заказ (ФИО, телефон, тариф)
    System->>System: Генерирует уникальный ID
    System->>SMS: Запрос на отправку уведомления
    SMS-->>Client: SMS с деталями заказа
    Staff-->>Client: Выдает бумажную копию (опционально)

...
```
