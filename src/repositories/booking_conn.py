import psycopg2
import psycopg2.extras
from settings import DB_CONFIG


# Добавление брони на странице "Бронирование"
def add_new_booking(room_id, user_id, check_in_date, check_out_date, status=True):
    query = """
                INSERT INTO booking (room_id, user_id, check_in_date, check_out_date, status)
                VALUES (%s, %s, %s, %s, %s);
            """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (room_id, user_id, check_in_date, check_out_date, status))


# Добавление транзакции на странице оплаты "Бронирование"
def add_new_transaction(booking_id, amount, payment_method, transaction_status="ok"):
    query = """
                INSERT INTO payment (booking_id,amount,payment_method,transaction_status)
                VALUES (%s, %s, %s, %s);
            """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (booking_id, amount, payment_method, transaction_status))


# Получение booking_id
def get_booking_id(room_id, user_id, check_in_date, check_out_date):
    query = f"""SELECT booking_id FROM booking WHERE room_id = '{room_id}' and user_id = '{user_id}' 
                and check_in_date = '{check_in_date}' and check_out_date = '{check_out_date}';"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
