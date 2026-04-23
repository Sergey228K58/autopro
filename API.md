API приложения «AutoPro»
Назначение API
API приложения AutoPro предоставляет программный доступ к основным функциям системы:
авторизация, управление заказами, сервисными работами, складом, финансами и клиентским порталом.
API используется для интеграции с внешними системами, мобильными приложениями и автоматизации внутренних процессов.

Маршруты API
Ниже приведена таблица всех доступных маршрутов приложения, включая метод, путь, требуемую роль и назначение.
 
Публичные маршруты
Метод	Путь	Роль	Описание
GET	/login	Не требуется	Страница авторизации
POST	/login	Не требуется	Проверка логина и пароля, создание сессии
GET	/logout	Авторизованный пользователь	Завершение сессии


Защищённые маршруты (требуют авторизации)
Главная страница
Метод	Путь	Роль	Описание
GET	/	Любая авторизованная	Главная страница приложения


Управление заказами
Метод	Путь	Роль	Описание
GET	/orders	manager, admin	Просмотр списка заказов
GET	/orders/create	manager, admin	Форма создания заказа
POST	/orders/create	manager, admin	Создание нового заказа
POST	/orders//status	manager, admin	Обновление статуса заказа
GET	/orders//contract	manager, admin	Генерация договора в формате TXT


Сервисные работы
Метод	Путь	Роль	Описание
GET	/service	master, manager, admin	Просмотр сервисных заказов
GET	/service/create	master, manager, admin	Форма создания сервисного заказа
POST	/service/create	master, manager, admin	Создание сервисного заказа
POST	/service//close	master, manager, admin	Закрытие сервисного заказа


Склад
Метод	Путь	Роль	Описание
GET	/parts	storekeeper, master, manager, admin	Просмотр склада
GET	/parts/receive	storekeeper, admin	Форма приёмки запчастей
POST	/parts/receive	storekeeper, admin	Приёмка запчастей
POST	/parts/inventory	storekeeper, admin	Выгрузка инвентаризации в Excel


Финансы
Метод	Путь	Роль	Описание
GET	/finance	accountant, admin	Просмотр финансовых операций
POST	/finance/add	accountant, admin	Добавление финансовой операции
GET	/finance/calc_cost/	accountant, admin	Расчёт себестоимости заказа
GET	/finance/report	accountant, admin	Выгрузка отчёта в Excel


Клиентский портал
Метод	Путь	Роль	Описание
GET	/client-portal	client, admin	Просмотр заказов клиента
GET	/client-portal/booking	client, admin	Форма записи на сервис
POST	/client-portal/booking	client, admin	Создание записи


Чат
Метод	Путь	Роль	Описание
GET	/chat	client, manager, admin	Просмотр сообщений
POST	/chat	client, manager, admin	Отправка сообщения