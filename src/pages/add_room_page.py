import streamlit as st
from add_hotel_conn import get_hotels_name, get_room_type, get_hotel_id, get_room_type_id, add_new_room


def add_room_page():
    st.title("Добавить комнату")

    # Список отелей для селектбокса
    hotels_lists = (i for i in get_hotels_name(st.session_state.user_info[0][0]))
    hotel_name = st.selectbox("Отель", hotels_lists)

    hotel_id = get_hotel_id(hotel_name)[0][0]

    # Список типов комнат
    room_type_list = (i for i in get_room_type())
    room_type_name = st.selectbox("Тип комнаты", room_type_list)

    room_type = get_room_type_id(room_type_name)[0][0]

    count_room = st.text_input("Количество комнат")
    price = st.text_input("Цена за ночь (максимум 50.000)")
    max_guests = st.text_input("Максимальное количество гостей")

    if st.button("Добавить комнату"):
        if hotel_name and room_type and count_room and price and max_guests:
            st.success("Комната успешно добавлена!")
            add_new_room(hotel_id, room_type, count_room, price, max_guests)
        else:
            st.error("Пожалуйста, заполните все поля.")
