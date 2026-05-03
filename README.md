# AutoPro 

## Технологии

- Python, Flask
- Excel (openpyxl) как хранилище данных
- bcrypt для хеширования паролей
- Чистый HTML + CSS

## Запуск

```bash
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate в Windows
pip install -r requirements.txt
python app.py

## Автоматизация с помощью GitHub Actions

В проекте настроены следующие workflow:

### 1. Tests (tests.yml)
Запускается при каждом push и pull request.  
Выполняет:
- установку зависимостей
- запуск pytest
- генерацию отчёта о покрытии

### 2. Build (build.yml)
Проверяет, что проект успешно собирается:
- устанавливает зависимости
- выполняет компиляцию Python-кода

### 3. Deploy (deploy.yml)
Автоматически собирает Docker-образ и отправляет его в Docker Hub.  
Использует секреты GitHub для авторизации.

### Бейджи статуса
В README отображаются бейджи статуса тестов, сборки и деплоя.

## CI/CD Status

![Tests](https://github.com/Sergey228K58/autopro/actions/workflows/tests.yml/badge.svg)
![Build](https://github.com/Sergey228K58/autopro/actions/workflows/build.yml/badge.svg)
![Deploy](https://github.com/Sergey228K58/autopro/actions/workflows/deploy.yml/badge.svg)
