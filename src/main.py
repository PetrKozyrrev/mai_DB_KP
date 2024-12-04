import streamlit as st
from streamlit_extras.switch_page_button import switch_page

import pandas as pd
import numpy as np
from datetime import datetime

from auth_page import registration_page, login_page

from user_search_page import user_search_page
from booking_page import booking_page
from reviews_page import reviews_page

from add_hotel_page import add_hotel_page
from add_room_page import add_room_page
from analyze_page import analyze_page
from owner_hotels_page import owner_hotels_page
from profile_page import profile_page

from admin_all_users_page  import admin_all_users_page
from admin_all_hotels_page import admin_all_hotels_page
from admin_all_reviews_page import admin_all_reviews_page
from admin_all_booking_page import admin_all_booking_page

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "registration"  # Начальная страница

    # Логика отображения страниц регистрации и входа
    if st.session_state.page == "registration":
        registration_page()
    elif st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "initial":
        if (st.session_state.user_info[0][5] == '1' or st.session_state.user_info[0][5] == 1):
            st.title(f"Добро пожаловать, {st.session_state.user_info[0][1]}!")

            st.sidebar.title("Навигация")
            page = st.sidebar.radio(
                "Перейти к странице",
                ["Поиск отелей", "Бронирование", "Отзывы", "Профиль"],
            )

            if st.sidebar.button("Выход"):
                st.session_state.user_info = []
                st.session_state.page = "registration"
                switch_page("main")


            if page == "Поиск отелей":
                user_search_page()
            elif page == "Бронирование":
                booking_page()
            elif page == "Профиль":
                profile_page()
            elif page == "Отзывы":
                reviews_page()

        elif (st.session_state.user_info[0][5] == '2' or st.session_state.user_info[0][5] == 2):
            st.title(f"Добро пожаловать, {st.session_state.user_info[0][1]}!")

            st.sidebar.title("Навигация")
            page = st.sidebar.radio(
                "Перейти к странице",
                ["Добавить отель", "Добавить номер", "Анализ продаж", "Добавленное", "Профиль"],
            )

            if st.sidebar.button("Выход"):
                st.session_state.user_info = []
                st.session_state.page = "registration"
                switch_page("main")

            if page == "Добавить отель":
                add_hotel_page()
            elif page == "Добавить номер":
                add_room_page()
            elif page == "Анализ продаж":
                analyze_page()
            elif page == "Добавленное":
                owner_hotels_page()
            elif page == "Профиль":
                profile_page()
        else:
            st.title(f"Добро пожаловать, {st.session_state.user_info[0][1]}!")

            st.sidebar.title("Навигация")
            page = st.sidebar.radio(
                "Перейти к странице",
                ["Все пользователи", "Все отели", "Все отзывы", "Все брони"],
            )

            if st.sidebar.button("Выход"):
                st.session_state.user_info = []
                st.session_state.page = "registration"
                switch_page("main")

            if page == "Все пользователи":
                admin_all_users_page()
            elif page == "Все отели":
                admin_all_hotels_page()
            elif page == "Все отзывы":
                admin_all_reviews_page()
            elif page == "Все брони":
                admin_all_booking_page()



if __name__ == "__main__":
    main()
