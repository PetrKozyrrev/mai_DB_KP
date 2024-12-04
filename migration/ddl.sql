-- Таблица для хранения информации о гостиницах
DROP TABLE IF EXISTS hotel;
CREATE TABLE hotel (
    hotel_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_loc VARCHAR(255),
    city_loc VARCHAR(255),
    location VARCHAR(255),
   -- star_rates INT,
    user_id INT,
    amenities VARCHAR(500)
);

COMMENT ON TABLE hotel IS 'Данные о гостиницах';

COMMENT ON TABLE hotel.hotel_id IS 'Уникальный идентификатор отеля';

COMMENT ON COLUMN hotel.name IS 'Название отеля';

COMMENT ON COLUMN hotel.country_loc IS 'Страна расположения отеля';

COMMENT ON COLUMN hotel.city_loc IS 'Город расположения отеля';

COMMENT ON COLUMN hotel.location IS 'Адрес отеля';

COMMENT ON COLUMN hotel.star_rates IS 'Рейтинг отеля';

COMMENT ON COLUMN hotel.amenities IS 'Описание удобств отеля';


-- Таблица для хранения информации о номерах
DROP TABLE IF EXISTS room;
CREATE TABLE room (
    room_id SERIAL PRIMARY KEY,
    hotel_id INT,
    room_type INT,
    number_of_rooms INT,
    price INT,
    max_guests INT,
    availability BOOLEAN
);

COMMENT ON TABLE room IS 'Данные о номерах';

COMMENT ON TABLE room.room_id IS 'Уникальный идентификатор отеля';

COMMENT ON COLUMN room.hotel_id IS 'Идентификатор отеля';

COMMENT ON COLUMN room.room_type IS 'Тип номера (VIP/low cost/...)';

COMMENT ON COLUMN room.number_of_rooms IS 'Количество комнат';

COMMENT ON COLUMN room.price IS 'Цена номера';

COMMENT ON COLUMN room.availability IS 'Статус номера (свободен/занят)';


-- Таблица для хранения информации об описании типов номеров
DROP TABLE IF EXISTS room_types;
CREATE TABLE room_types (
    room_type SERIAL PRIMARY KEY,
    type_name VARCHAR(255),
    room_class INT,
    describtion TEXT
);

COMMENT ON TABLE room_types IS 'Данные о номерах';

COMMENT ON TABLE room_types.room_type IS 'Уникальный идентификатор типа';

COMMENT ON TABLE room_types.type_name IS 'Название типа комнаты';

COMMENT ON TABLE room_types.type_name IS 'Три типа номеров: Эконом, Медиум, VIP';

COMMENT ON COLUMN room_types.describtion IS 'Описание номера';


-- Таблица для хранения информации о пользователях
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
   	user_email VARCHAR(255),
   	user_phone VARCHAR(255),
    user_password VARCHAR(255),
    user_role INT
);

COMMENT ON TABLE users IS 'Данные о пользователях';

COMMENT ON TABLE users.user_id IS 'Уникальный идентификатор пользователя';

COMMENT ON TABLE users.user_name IS 'Логин пользователя';

COMMENT ON TABLE users.user_email IS 'Email пользователя';

COMMENT ON TABLE users.user_phone IS 'Телефон пользователя';

COMMENT ON COLUMN users.user_password IS 'Пароль пользователя';

COMMENT ON COLUMN users.user_role IS 'Роль пользователя (1 - Админ, 2 - Владелец отеля, 3 - Обычный пользователь)';


-- Таблица для хранения информации об отзывах
DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    hotel_id INT,
   	user_id INT,
   	rating INT,
    review_describe TEXT
);

COMMENT ON TABLE reviews IS 'Данные об отзывах';

COMMENT ON TABLE reviews.review_id IS 'Уникальный идентификатор отзыва';

COMMENT ON TABLE reviews.hotel_id IS 'Идентификатор отеля';

COMMENT ON TABLE reviews.user_id IS 'Идентификатор пользователя';

COMMENT ON TABLE reviews.rating IS 'Рейтинг отзыва';

COMMENT ON COLUMN reviews.review_describe IS 'Текст отзыва';

-- Таблица для хранения информации о бронировании номеров
DROP TABLE IF EXISTS booking;
CREATE TABLE booking (
    booking_id SERIAL PRIMARY KEY,
    room_id INT,
   	user_id INT,
   	check_in_date DATE,
    check_out_date DATE,
    status BOOLEAN
);

COMMENT ON TABLE booking IS 'Данные о бронировании номеров';

COMMENT ON TABLE booking.booking_id IS 'Уникальный идентификатор брони';

COMMENT ON TABLE booking.room_id IS 'Идентификатор комнаты';

COMMENT ON TABLE booking.user_id IS 'Идентификатор пользователя';

COMMENT ON TABLE booking.check_in_date IS 'Дата заезда';

COMMENT ON COLUMN booking.check_out_date IS 'Дата отъезда';

COMMENT ON COLUMN booking.status IS 'Оплачен/Не оплечен';


-- Таблица для хранения информации об оплате
DROP TABLE IF EXISTS payment;
CREATE TABLE payment (
    payment_id SERIAL PRIMARY KEY,
    booking_id INT,
   	amount INT,
   	payment_method VARCHAR(255),
    transaction_status VARCHAR(255)
);

COMMENT ON TABLE payment IS 'Данные об оплате';

COMMENT ON TABLE payment.payment_id IS 'Уникальный идентификатор оплаты';

COMMENT ON TABLE payment.booking_id IS 'Идентификатор брони';

COMMENT ON TABLE payment.amount IS 'Сумма заказа';

COMMENT ON TABLE payment.payment_method IS 'Способ оплаты';

COMMENT ON COLUMN payment.transaction_status IS 'Статус оплаты';


