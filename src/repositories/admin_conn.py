from pandas import DataFrame
import psycopg2
import psycopg2.extras
from settings import DB_CONFIG


def get_all_users() -> DataFrame:
    query = f"SELECT user_name,user_email,user_phone,user_role FROM users Where user_name != 'admin'"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return DataFrame(cursor.fetchall(), columns=['login', 'email', 'phone', 'role'])


def get_all_hotels() -> DataFrame:
    query = f"SELECT h.name,h.country_loc,h.city_loc,h.location,u.user_name FROM hotel h join users u on u.user_id = h.user_id;"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return DataFrame(cursor.fetchall(), columns=['Hotel_name', 'Country', 'City', 'Adress', 'Owner'])


def get_all_reviews() -> DataFrame:
    query = f"""SELECT h.name,u.user_name,r.rating,r.review_describe FROM reviews r join hotel h on h.hotel_id = r.hotel_id join users u on u.user_id = r.user_id"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return DataFrame(cursor.fetchall(), columns=['Hotel_name', 'User_login', 'Rate', 'Describtion'])


def get_user_id(user_name):
    query = f"SELECT user_id FROM users WHERE user_name = '{user_name}';"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


def delete_review(user_id, hotel_id):
    query = f"DELETE FROM reviews WHERE user_id = {user_id} and hotel_id = {hotel_id}"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)


def get_all_bookings() -> DataFrame:
    query = f"""SELECT u.user_name,b.check_in_date,b.check_out_date,h.name
                FROM booking b 
                join users u on u.user_id = b.user_id
                join room r on r.room_id = b.room_id
                join hotel h on h.hotel_id = r.hotel_id"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return DataFrame(cursor.fetchall(), columns=['User_name', 'check_in_date', 'check_out_date','hotel_name'])
