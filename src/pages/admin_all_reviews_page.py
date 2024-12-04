import streamlit as st
from admin_conn import get_all_reviews, get_user_id, delete_review
from add_hotel_conn import get_hotel_id


def admin_all_reviews_page():
    st.title("Все Отзывы")

    reviews = get_all_reviews()

    st.dataframe(reviews)

    st.write("Удалить: ")
    user_login = st.selectbox("Имя пользователя", ("-", *reviews['User_login']))
    hotel_name = st.selectbox("Название отеля", ("-", *reviews['Hotel_name']))

    if hotel_name != "-":
        hotel_id = get_hotel_id(hotel_name)[0][0]

    if user_login != "-":
        user_id = get_user_id(user_login)[0][0]

    if st.button("Удалить комментарий"):
        delete_review(user_id, hotel_id)
        st.success("Запись успешно удалена")
