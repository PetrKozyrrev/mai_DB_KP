import streamlit as st
from analyze_conn import get_statistics


def analyze_page():
    st.title("Анализ продаж")

    data = get_statistics(st.session_state.user_info[0][0])
    print(data)
    st.line_chart(data, x="date", y="sum_price", color="name")
