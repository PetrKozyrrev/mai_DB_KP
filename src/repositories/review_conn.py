import psycopg2
import psycopg2.extras
from settings import DB_CONFIG


# Проверка посещал ли пользователь данный отель на странице "Отзывы"
def checker_user(user_id, hotel_id) -> int:
    query = f"""select 
                    b.user_id 
                from 
                    booking b
                join room r
                    on b.room_id = r.room_id
                where 1=1
                    and b.user_id = {user_id} 
                    and r.hotel_id = {hotel_id};"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchall()
            if (len(row) == 0):
                return 0
            else:
                return 1


# Добавление отзыва на странице "Отзывы"
def add_new_review(hotel_id, user_id, rate, describtion):
    query = """
                INSERT INTO reviews (hotel_id,user_id,rating,review_describe)
                VALUES (%s, %s, %s, %s);
            """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (hotel_id, user_id, rate, describtion))
