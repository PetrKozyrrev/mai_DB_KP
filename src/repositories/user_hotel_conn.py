import psycopg2
import psycopg2.extras
from settings import DB_CONFIG


# Вся информация для бронирования отеля на странице пользователя "Поиск отелей"
def find_all_hotel_for_user(country, city, check_in_date, check_out_date, num_guests, price=50000) -> list:
    if len(city)>0:
        query = f"""select 
                    h.name,
	                h.country_loc,
	                h.city_loc,
	                h.location,
	                h.amenities,
	                rt.type_name,
	                rt.describtion,
	                r.number_of_rooms ,
	                r.price,
	                r.max_guests ,
	                r.availability,
	                b.check_in_date,
	                b.check_out_date,
	                coalesce(round((avg(r2.rating) over(partition by h.name)),2)::varchar, 'Пока нет оценок')
                from 
                    hotel h
                left join room r
	                on h.hotel_id = r.hotel_id 
                left join room_types rt
	                on r.room_type = rt.room_type
                left join booking b
	                on r.room_id = b.room_id
                left join reviews r2 
	                on h.hotel_id  = r2.hotel_id
                where 1=1
                    and h.country_loc = '{country}'
                    and h.city_loc = '{city}'
                    and r.max_guests >= {num_guests}
                    and r.price <= {price}
                order by h.name
                ;
            """
    else:
        query = f"""select 
                            h.name,
        	                h.country_loc,
        	                h.city_loc,
        	                h.location,
        	                h.amenities,
        	                rt.type_name,
        	                rt.describtion,
        	                r.number_of_rooms ,
        	                r.price,
        	                r.max_guests ,
        	                r.availability,
        	                b.check_in_date,
        	                b.check_out_date,
        	                coalesce(round((avg(r2.rating) over(partition by h.name)),2)::varchar, 'Пока нет оценок') 
                        from 
                            hotel h
                        left join room r
        	                on h.hotel_id = r.hotel_id 
                        left join room_types rt
        	                on r.room_type = rt.room_type
                        left join booking b
        	                on r.room_id = b.room_id
                        left join reviews r2 
        	                on h.hotel_id  = r2.hotel_id
                        where 1=1
                            and h.country_loc = '{country}'
                            and r.max_guests >= {num_guests}
                            and r.price <= {price}
                        order by h.name
                        ;
                    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


def calculate_price(country, city, name, room, check_in_date, check_out_date, num_guests):
    all_h = find_all_hotel_for_user(country, city, check_in_date, check_out_date, num_guests)
    h = ()
    for i in all_h:
        if i[0] == name and i[5] == room:
            h = i

    if(len(h) == 0):
        return -1
    else:
        delta = (check_out_date - check_in_date).days
        return delta * h[8]