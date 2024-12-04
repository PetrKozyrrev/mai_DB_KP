import streamlit as st
from user_hotel_conn import find_all_hotel_for_user
from booking_page import booking_page
from input_validation import valid_country
import datetime


def user_search_page():
    st.title("Поиск Отелей")

    country = st.text_input("Страна")

    city = st.text_input("Город")

    check_in_date = st.date_input("Дата заезда")
    check_out_date = st.date_input("Дата выезда")

    num_guests = st.text_input("Количество гостей")

    price = st.slider("Цена за ночь", min_value=1000, max_value=50000, step=500)

    if st.button("Найти"):
        if country and check_in_date and check_out_date and num_guests:
            if valid_country(country):
                if(check_in_date < check_out_date):
                    if (check_in_date >= datetime.date.today()):
                        finded_hotels = find_all_hotel_for_user(country, city, check_in_date, check_out_date, int(num_guests),
                                                    int(price))
                        if (len(finded_hotels) == 0):
                            st.error("Мы не нашли отелей с такими параметрами, попробуйте скорретировать ваш запрос")
                        else:
                            st.success("Вот, что мы нашли:")

                            for i in range(len(finded_hotels)):
                                if (i == 0 or finded_hotels[i][0] != finded_hotels[i - 1][0]):
                                    st.write("===================================================================")
                                    st.write(f"Отель: {finded_hotels[i][0]}, {finded_hotels[i][1]}, {finded_hotels[i][2]}, "
                             f"{finded_hotels[i][3]}, Rating: {finded_hotels[i][13]}")
                                    st.write(f"{finded_hotels[i][4]}")
                                st.write("---------------------------------------------------------------")
                                st.write(f"Номер: {finded_hotels[i][5]}")
                                st.write(f"{finded_hotels[i][6]}")
                                st.write(f"Количество комнат: {finded_hotels[i][7]}")
                                st.write(f"Цена за ночь: {finded_hotels[i][8]}")
                                st.write(f"Вместимость номера: {finded_hotels[i][9]}")

                            st.write("===================================================================")
                    else:
                        st.error("Неправильно введены даты")
                else:
                    st.error("Неправильно введены даты")
            else:
                st.error("Ошибка, неправильно введена страна")
        else:
            st.error("Пожалуйста, заполните все поля.")
