from pandas import DataFrame
import psycopg2
import psycopg2.extras
from settings import DB_CONFIG


def get_statistics(user_id) -> DataFrame:
    query = f"""
            select 
	            h.name,
	            b.check_in_date,
	            sum(p.amount) as sum_price
            from hotel h 
            join room r 
                on r.hotel_id = h.hotel_id 
            join booking b 
                on b.room_id = r.room_id 
            join payment p 
                on p.booking_id = b.booking_id
            where h.user_id = {user_id}
            group by 1,2           
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return DataFrame(cursor.fetchall(), columns=["name", "date", "sum_price"])
