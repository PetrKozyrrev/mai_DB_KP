import streamlit as st
from admin_conn import get_all_hotels

def admin_all_hotels_page():
    st.title("Все Отели")

    hotels = get_all_hotels()

    st.dataframe(hotels)
