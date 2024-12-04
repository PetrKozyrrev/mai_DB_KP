import psycopg2
import psycopg2.extras
from settings import DB_CONFIG


# Добавление нового отеля на странице "Добавить Отель"
def add_new_hotel(user_id, name, country, city, address, amenities):
    query = """
            INSERT INTO hotel (name, country_loc, city_loc, location,user_id, amenities)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, country, city, address, user_id, amenities))


# Добавление новой комнаты на странице "Добавить комнату"
def add_new_room(hotel_id, room_type, count_room, price, max_guests):
    availability = True
    query = """
            INSERT INTO room (hotel_id, room_type, number_of_rooms, price,availability, max_guests)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (hotel_id, room_type, int(count_room), int(price), availability, int(max_guests)))


# Получение названия отеля для чекбокса на странице "Добавить команту"
def get_hotels_name(user_id) -> list:
    query = f"SELECT name FROM hotel WHERE user_id = {user_id} GROUP BY 1;"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


# Получение типа комнаты для чекбокса на странице "Добавить команту"
def get_room_type() ->list:
    query = "SELECT type_name FROM room_types;"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


# Получение айди отеля
def get_hotel_id(hotel_name) -> list:
    query = f"SELECT hotel_id FROM hotel WHERE name = '{hotel_name}';"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


# Получение айди типа комнаты
def get_room_type_id(room_type_name) -> list:
    query = f"SELECT room_type FROM room_types WHERE type_name = '{room_type_name}';"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


# Получение room_id из таблицы room для страницы "Бронирование"
def get_room_id(country, city, name, room):
    query = f"""
                select
                    r.room_id
                from 
                    room r
                join hotel h
                    on r.hotel_id = h.hotel_id
                join room_types rt
                    on r.room_type = rt.room_type
                where 1=1
                    and h.name = '{name}'
                    and h.country_loc = '{country}'
                    and h.city_loc = '{city}'
                    and rt.type_name = '{room}';
            """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


# Получение всей информации об отелях для страницы "Добавленное"
def get_all_info_about_hotel(user_id, hotel_name) -> list:
    query = f"""
        SELECT
            h.country_loc,
            h.city_loc,
            h.location,
            h.amenities,
            sum(r.number_of_rooms) as count_rooms,
            sum(r.max_guests) as all_guests
        FROM hotel h
        LEFT JOIN room r
            ON h.hotel_id = r.hotel_id
        WHERE h.user_id = {user_id} and h.name = '{hotel_name}'
        GROUP BY h.hotel_id;
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
