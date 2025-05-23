# API для аутентификации и авторизации с JWT

Приложение для аутентификации и авторизации пользователей с использованием JWT. Реализовано на FastAPI с использованием PostgreSQL в качестве базы данных и ее взаимодействие через SQLAlchemy с асинхронной поддержкой.

**Основные функции**


- Регистрация новых пользователей

- Аутентификация с выдачей access и refresh токенов

- Админ панель sqladmin 

**Стек технологий**
- Веб-фреймворк: FastAPI

- ORM: SQLAlchemy с асинхронной поддержкой

- База данных: PostgreSQL

- Система миграций: Alembic

# Структура проекта
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

1. Запуск приложения:

```bash
git clone https://github.com/DevdScvn/api_auth_v3
```

Создайте файл:

.env на основе .env.example

Установите зависимости:
```bash
poetry install
```

Запустите сервисы с помощью Docker Compose:

```bash
docker-compose up -d --build
```
Приложение запоковано в docker, так же в корне проекта прописан prestart.sh, который прогонит миграции.
Если так не работает, для этого нужно полностью удалить папку alembic и сделать альтернативным способом - представленным ниже.


Запустите приложение с Uvicorn:

```bash
cd src
uvicorn main:main_app --reload --port 8000
```

**После запуска приложение будет доступно по адресу:**

http://localhost:8000

http://localhost:8000/docs



2. Миграции базы данных

Инициализируйте Alembic:

```bash
cd app
alembic init -t async migration
```

Затем переместите alembic.ini в корень проекта.

Создайте миграцию:

```bash
alembic revision --autogenerate -m "Initial migration"
```

Примените миграции:

```bash
cd src
alembic upgrade head
```

