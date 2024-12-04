import streamlit as st
from add_hotel_conn import get_hotel_id
from review_conn import checker_user, add_new_review


def reviews_page():
    st.title("Отзывы")

    st.write("Здесь вы можете оставить отзыв")

    country = st.text_input("Страна")
    city = st.text_input("Город")
    name = st.text_input("Название отеля")

    rate = st.slider("Оцените отель", min_value=1, max_value=5, step=1)
    describtion = st.text_area("Напишите ваш отзыв")

    if st.button("Оставить отзыв"):
        if country and city and name and describtion and rate:
            hotel_id = get_hotel_id(name)[0][0]
            if (checker_user(st.session_state.user_info[0][0],hotel_id)):
                st.success("Спасибо за ваш отзыв")
                add_new_review(hotel_id, st.session_state.user_info[0][0], rate, describtion)
            else:
                st.error("Вы не посещали данный отель и не можете оставить о нем отзыв")
        else:
            st.error("Заполните все поля")
