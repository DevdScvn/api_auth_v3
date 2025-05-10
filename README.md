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

.
├── src/
│   ├── admin_panel/
│   │   ├── auth.py      
│   │   ├── user.py  
│   │   └── utils.py             
│   ├── alembic/                 
│       ├── versions/            
│       |           ├── 2025     
│   │   ├── env.py               
│   │   ├── README          
│   │   └── script.py.marko      
│   ├── db/                      
│   ├── auth/                    
│   │   ├── auth.py       
│   │   ├── dao.py       
│   │   ├── models.py            
│   │   ├── router.py            
│   │   ├── schemas.py           
│   │   └── utils.py             
│   ├── dao/                     
│   │   └── dao.py               
│   ├── database/                
│   │   ├── db_helper.py         
│   │   ├── base.py              
│   ├── settings/                
│   │   ├── config.py            
│   ├── user/                    
│   │   ├── dao.py       
│   │   ├── models.py
│   │   ├── router.py            
│   │   ├── schemas.py           
│   ├── utils/                   
│   │   └── case_converter.py   
│   ├── .env                     
│   ├── alembic.ini              
│   └── main.py                  
├── tests/                       
│   ├── conftest.py              
│   ├── test_auth.py             
├── .gitignore                   
├── docker-compose.yml           
├── Dockerfile                   
├── pyproject.toml               
└── README.md   




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



<img width="867" alt="Снимок экрана 2025-05-10 в 22 49 45" src="https://github.com/user-attachments/assets/98f71ee9-f886-42c8-a38a-127725b765de" />

