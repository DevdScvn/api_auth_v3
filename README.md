# Приложения для аутентификации и авторизации с JWT

Описание проекта:
Приложение для аутентификации и авторизации пользователей с использованием JWT. Реализовано на FastAPI с использованием PostgreSQL в качестве базы данных. Проект упакован в Docker-контейнеры с помощью Docker Compose.

Основные функции
- Регистрация новых пользователей

- Аутентификация с выдачей access и refresh токенов

- Обновление access токена с помощью refresh токена

- CRUD-операции для управления пользователями

- Админ панель sqladmin 

**Стек технологий**
-Веб-фреймворк: FastAPI
-ORM: SQLAlchemy с асинхронной поддержкой через aiosqlite
-База данных: SQLite (легко заменяемая на другую SQL-СУБД)
-Система миграций: Alembic
-Авторизация/Аутентификация: bcrypt для хеширования паролей, python-jose для защиты данных с использованием JWT



Установка и запуск
Клонируйте репозиторий:

2. Запустите сервисы:
```bash
git clone https://github.com/yourusername/auth-app.git
```
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
```


```
.
├── src/                         # Основной исходный код
│   ├── admin_panel/             # Админ панель
│   │   ├── auth.py              # Конфигурация аутентификации для админ панели
│   │   ├── user.py              # Модели пользователей для админ панели
│   │   └── utils.py             # Вспомогательные функции
│   ├── alembic/                 
│       ├── versions/            
│       |           ├── 2025     
│   │   ├── env.py               
│   │   ├── README          
│   │   └── script.py.marko   
│   ├── auth/                    # Логика аутентификации
│   │   ├── auth.py              # Основная логика аутентификации
│   │   ├── dao.py               # CRUD операции для создания и обработки tokens
│   │   ├── models.py            # SQLAlchemy модели tokens
│   │   ├── router.py            # Router
│   │   ├── schemas.py           # Схемы пользователей
│   │   └── utils.py             # Вспомогательные функции
│   ├── dao/                     # CRUD операции
│   │   └── dao.py               # Базовый CRUD класс
│   ├── database/                # Работа с базой данных
│   │   ├── db_helper.py         # Подключение к БД
│   │   ├── base.py              # SQLAlchemy модели
│   ├── settings/                # Настройки приложения
│   │   ├── config.py            # Основной конфиг приложения
│   ├── user/                    # Логика пользователей
│   │   ├── dao.py               # CRUD операции для чтения и обработки пользователей
│   │   ├── models.py            # SQLAlchemy модели пользователей
│   │   ├── router.py            # Router
│   │   ├── schemas.py           # Схемы пользователей
│   ├── utils/                   # Общие утилиты
│   │   └── case_converter.py    # Преобразование названий таблиц
│   ├── .env                     # Переменные окружения
|   ├── alembic.ini              # Конфиг Alembic
│   └── main.py                  # Точка входа в приложение
├── tests/                       # Тесты
│   ├── conftest.py              # Фикстуры pytest
│   ├── test_auth.py             # Тесты аутентификации
├── .gitignore                   # Git ignore файл
├── docker-compose.yml           # Docker Compose конфигурация
├── Dockerfile                   # Docker конфигурация
├── pyproject.toml               # Конфигурация проекта
└── README.md                    # Документация
```


