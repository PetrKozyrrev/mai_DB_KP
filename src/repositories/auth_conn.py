import psycopg2
import psycopg2.extras
from settings import DB_CONFIG

# Регистрация нового пользователя на странице "Регистрация"
def reg_new_user(login, phone, email, role, password):
    query = """
            INSERT INTO users (user_name, user_email, user_phone, user_password, user_role)
            VALUES (%s, %s, %s, %s, %s);
        """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (login, email, phone, password, role))

# Проверка существует ли пользователь с таким логином на странице "Регистрация"
def check_new_user_login(login):
    query = f"SELECT user_name,user_password FROM users WHERE user_name = '{login}';"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchall()
            if (len(row) == 0):
                return 1
            else:
                return 0

# Проверка логина и пароля пользователя на странице "Вход"
def chek_auth_user(login, password) -> int:
    query = f"SELECT user_name,user_password FROM users WHERE user_name = '{login}' and user_password = '{password}';"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchall()
            if (len(row) == 0):
                return 1
            else:
                return 0


# Возвращение данных пользователя на страницах "Регистрация" и "Вход"
def return_user_data(login, password) -> list:
    query = f"""SELECT user_id, user_name, user_email, user_phone, user_password, user_role 
                FROM users 
                WHERE user_name = '{login}' and user_password = '{password}';"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
