import streamlit as st
from add_hotel_conn import add_new_hotel
from input_validation import valid_add_hotel,valid_country


def add_hotel_page():
    st.title("Добавить отель")

    name = st.text_input("Название отеля")
    country = st.text_input("Страна")
    city = st.text_input("Город")
    address = st.text_input("Точный адрес (Пример: ул. Пушкина, д. 21)")
    amenities = st.text_input("Описание")

    user_id = st.session_state.user_info[0][0]

    if st.button("Добавить"):
        if name and country and city and address and amenities:
            if(valid_country(country)):
                st.success("ok")
                if (valid_add_hotel(name, country, city)):
                    st.success("Отлель успешно добавлен!")
                    add_new_hotel(user_id, name, country, city, address, amenities)
                else:
                    st.error("В этом городе уже есть отель с таким названием")
            else:
                st.error("Некорректное название страны")
        else:
            st.error("Пожалуйста, заполните все поля.")
