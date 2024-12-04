import streamlit as st
from add_hotel_conn import get_hotels_name, get_all_info_about_hotel


def owner_hotels_page():
    st.title("Ваше добавленное")

    hotels_lists = (i for i in get_hotels_name(st.session_state.user_info[0][0]))

    for hotel in hotels_lists:
        hotel_name = hotel[0]
        hotel_info = get_all_info_about_hotel(st.session_state.user_info[0][0], hotel_name)
        st.write(f'Отель: "{hotel_name}"')
        st.write(f"Адрес: {hotel_info[0][0]}, {hotel_info[0][1]}, {hotel_info[0][2]}")
        st.write(f"Всего комнат: {hotel_info[0][4]}")
        st.write(f"Общая вместимость: {hotel_info[0][5]}")
        st.write("\n")
