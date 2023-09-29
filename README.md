# Проект: Приложение Благотворительного фонда поддержки котиков QRKot

## Описание проекта:
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.
Учебный проект 

## Использованные технологии:
- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Alembic
- SQLite
- Google Sheets

### Инструкция по установке

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/vartexxx/cat_charity_fund.git

cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

Создать и заполнить файл конфигурации .env по шаблону:  
```  
APP_TITLE=Название
DESCRIPTION=Описание
DATABASE_URL=sqlite+aiosqlite:///./test.db
SECRET=Секретный ключ

FIRST_SUPERUSER_EMAIL=<email суперюзера>
FIRST_SUPERUSER_PASSWORD=<пароль суперюзера>
TYPE=service_account
PROJECT_ID=atomic-climate-<идентификатор>
PRIVATE_KEY_ID=<id приватного ключа>
PRIVATE_KEY="-----BEGIN PRIVATE KEY-----<приватный ключ>-----END PRIVATE KEY-----\n"
CLIENT_EMAIL=<email сервисного аккаунта>
CLIENT_ID=<id сервисного аккаунта>
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=<ссылка>
EMAIL=<email пользователя>
```  

Применить миграции:  
```
alembic upgrade head
```

Запустить проект:  
```
uvicorn app.main:app --reload
```

### Автор:
[Бурлака Владислав](https://github.com/vartexxx) vartexxx29@yandex.ru