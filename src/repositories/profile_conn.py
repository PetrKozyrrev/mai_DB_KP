import psycopg2
import psycopg2.extras
from settings import DB_CONFIG


# Получение активных броней на странице "Профиль"
def get_active_booking(user_id,today):
    query = f"""
            select 
                h.name,h.country_loc,h.city_loc,h.location,
                rt.type_name, b.check_in_date,b.check_out_date,r.price
            from booking b 
            join room r 
                on r.room_id = b.room_id 
            join hotel h 
                on h.hotel_id = r.hotel_id 
            join room_types rt 
                on rt.room_type = r.room_type
            where 1=1
                and b.user_id = {user_id}
                and check_in_date <= '{today}'
                and check_out_date >= '{today}'
            """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

# Получение отзывов пользователя на странице "Профиль"
def get_reviews(user_id):
    query = f"""
            select h.name,h.country_loc,h.city_loc,r.rating,r.review_describe
            from reviews r 
            join hotel h 
                on h.hotel_id = r.hotel_id 
            where r.user_id = {user_id}
            """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

# Редактирование логина на странице "Профиль"
def update_user_login(user_id,user_name):
    query = f"UPDATE users SET user_name = '{user_name}' WHERE user_id = {user_id};"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)