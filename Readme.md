Настройки для работы:
1) Установить зависимости: pip install -r requirements.txt
2) Создать базу данных postgres
3) Создать в корневой директории проекта файл .env и дописать в переменные окружения данные

USER_POSTGRES=имя пользователя postgresql
DB_PASS=пароль пользователя postgresql
NAME_DB=имя базы данных для проекта
SECRET_KEY=секретный ключ Django
STRIPE_API_KEY=секретный ключ Stripe (получить после регистрации на https://dashboard.stripe.com/register)

4) Создать базу данных в postgresql, c названием указанным в NAME_DB
5) Применить миграции
