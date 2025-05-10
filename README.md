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
