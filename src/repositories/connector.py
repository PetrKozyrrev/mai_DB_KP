import psycopg2
from psycopg2 import pool
from contextlib import contextmanager
from src.settings import DB_CONFIG, POOL_MIN_CONN, POOL_MAX_CONN
import atexit


# Инициализируем пул подключений
print("Initializing connection pool...")
connection_pool = psycopg2.pool.SimpleConnectionPool(**DB_CONFIG, minconn=1, maxconn=10)


@contextmanager
def get_connection():
    connection = connection_pool.getconn()
    try:
        yield connection
    finally:
        connection_pool.putconn(connection)


def example_fetchall():
    query = "SELECT * FROM room_types;"

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]
            rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

    for row in rows:
        print(row)

    print("example4 finished")


def close_connection_pool():
    if connection_pool:
        connection_pool.closeall()
        print("Connection pool closed.")


def on_exit():
    print("Приложение завершено! Закрываем ресурсы...")
    close_connection_pool()


example_fetchall()

# Регистрируем функцию для выполнения при завершении программы
atexit.register(on_exit)