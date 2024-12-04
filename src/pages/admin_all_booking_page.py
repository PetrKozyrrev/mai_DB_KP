import streamlit as st
from admin_conn import get_all_bookings

def admin_all_booking_page():
    st.title("Все брони")

    bookings = get_all_bookings()

    st.dataframe(bookings)