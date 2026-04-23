# Общая информация

# API приложения AutoPro предоставляет доступ к функционалу:

- авторизация

- управление заказами

- сервисные работы

- склад

- финансы

- клиентский портал

- чат

# Все защищённые маршруты требуют авторизации и проверки роли.
| Метод | Путь | Описание |
| --- | --- | --- |
| **GET** | ``/login`` | Страница авторизации |
| **POST** | ``/login`` | Проверка логина и пароля |
| **GET** | ``/logout`` | Выход из системы |

| Метод | Путь | Роль | Описание |
| --- | --- | --- | --- |
| **GET** | ``/`` | Любая авторизованная | Главная страница приложения |

| Метод | Путь | Роль | Описание |
| --- | --- | --- | --- |
| **GET** | ``/orders`` | manager, admin | Список заказов |
| **GET** | ``/orders/create`` | manager, admin | Форма создания заказа |
| **POST** | ``/orders/create`` | manager, admin | Создание заказа |
| **POST** | ``/orders/``<id>/status</id>`` | manager, admin | Обновление статуса |
| **GET** | ``/orders/``<id>/contract</id>`` | manager, admin | Генерация договора TXT |

| Метод | Путь | Роль | Описание |
| --- | --- | --- | --- |
| **GET** | ``/service`` | master, manager, admin | Список сервисных заказов |
| **GET** | ``/service/create`` | master, manager, admin | Форма создания |
| **POST** | ``/service/create`` | master, manager, admin | Создание сервисного заказа |
| **POST** | ``/service/``<id>/close</id>`` | master, manager, admin | Закрытие заказа |

| Метод | Путь | Роль | Описание |
| --- | --- | --- | --- |
| **GET** | ``/parts`` | storekeeper, master, manager, admin | Просмотр склада |
| **GET** | ``/parts/receive`` | storekeeper, admin | Форма приёмки |
| **POST** | ``/parts/receive`` | storekeeper, admin | Приёмка запчастей |
| **POST** | ``/parts/inventory`` | storekeeper, admin | Выгрузка инвентаризации (Excel) |

| Метод | Путь | Роль | Описание |
| --- | --- | --- | --- |
| **GET** | ``/finance`` | accountant, admin | Список операций |
| **POST** | ``/finance/add`` | accountant, admin | Добавление операции |
| **GET** | ``/finance/calc_cost/``<id></id>`` | accountant, admin | Расчёт себестоимости |
| **GET** | ``/finance/report`` | accountant, admin | Выгрузка отчёта (Excel) |

| Метод | Путь | Роль | Описание |
| --- | --- | --- | --- |
| **GET** | ``/client-portal`` | client, admin | Личный кабинет клиента |
| **GET** | ``/client-portal/booking`` | client, admin | Форма записи |
| **POST** | ``/client-portal/booking`` | client, admin | Создание записи |

| Метод | Путь | Роль | Описание |
| --- | --- | --- | --- |
| **GET** | ``/chat`` | client, manager, admin | Просмотр сообщений |
| **POST** | ``/chat`` | client, manager, admin | Отправка сообщения |

