# Приложения для аутентификации и авторизации с JWT

Описание проекта:
Приложение для аутентификации и авторизации пользователей с использованием JWT. Реализовано на FastAPI с использованием PostgreSQL в качестве базы данных. Проект упакован в Docker-контейнеры с помощью Docker Compose.

Основные функции
- Регистрация новых пользователей

- Аутентификация с выдачей access и refresh токенов

- Обновление access токена с помощью refresh токена

- CRUD-операции для управления пользователями

- Админ панель sqladmin 

Дополнительно: SQLAlchemy (ORM), Pydantic (валидация данных), Alembic (миграции)

<img width="867" alt="Снимок экрана 2025-05-10 в 22 49 45" src="https://github.com/user-attachments/assets/98f71ee9-f886-42c8-a38a-127725b765de" />

Установка и запуск
Клонируйте репозиторий:

bash
 ```git clone https://github.com/yourusername/auth-app.git ```
cd auth-app
Создайте файл .env на основе .env.example:

Запустите приложение с помощью Docker Compose:

bash
docker-compose up -d --build
После запуска приложение будет доступно по адресу:

http://localhost:8000
Документация API (Swagger UI) доступна по адресу:

http://localhost:8000/docs

- **Дополнительно**: 
2. Запустите сервисы:
```bash
docker-compose up -d --build
