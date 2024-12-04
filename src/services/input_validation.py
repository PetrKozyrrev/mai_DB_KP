import psycopg2
import psycopg2.extras
from settings import DB_CONFIG

from const import ALL_COUNTRIES


def valid_login(login:str) -> bool:
    if(len(login) > 255 or len(login) == 0): return False

    return True

def valid_email(email:str) -> bool:
    if (len(email) > 255 or len(email) == 0): return False

    if (("@gmail.com" in email) or ("@mail.ru" in email) or ("@yandex.ru" in email) or ("@email.com" in email) or ("@email.ru" in email)):
        return True
    else:
        return False

def valid_phone(phone:str) -> bool:
    if (len(phone) != 11): return False

    if(phone.isdigit()):
        return True
    else:
        return False

def valid_role(role:str) -> bool:
    if(role not in ('1','2')): return False

    return True

def valid_password(password:str) -> bool:
    if(len(password) > 255 or len(password) == 0): return False

    return True

def valid_country(country):
    if country in ALL_COUNTRIES:
        return 1
    else:
        return 0

def valid_add_hotel(name,country,city) -> int:
    query = f"SELECT hotel_id FROM hotel WHERE name = '{name}' and country_loc = '{country}' and city_loc = '{city}';"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            d = cursor.fetchall()
            if(len(d) == 0):
                return 1
            else:
                return 0