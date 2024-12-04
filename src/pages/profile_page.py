import streamlit as st
import datetime
from profile_conn import get_active_booking,get_reviews,update_user_login
from input_validation import valid_login,valid_email,valid_phone

def profile_page():
    st.title("Ваш профиль:")

    st.markdown(f"***Логин***: {st.session_state.user_info[0][1]}")

    if "update_login_button" not in st.session_state:
        st.session_state["update_login_button"] = False

    if st.button("Редактировать логин"):
        st.session_state["update_login_button"] = not st.session_state["update_login_button"]

    if st.session_state["update_login_button"]:
        new_login = st.text_input("Новый логин")
        # new_email = st.text_input("Новый email")
        # new_phone = st.text_input("Новый телефон")
        if st.button("Обновить"):
            if new_login:
                if valid_login(new_login):
                    update_user_login(st.session_state.user_info[0][0],new_login)
                    st.success("Логин обновлен")
                    st.session_state.user_info[0][1] = new_login
                    st.session_state["update_login_button"] = not st.session_state["update_login_button"]
                else:
                    st.error("Некорректный логин")

    st.markdown(f"***Email***: {st.session_state.user_info[0][2]}")
    st.markdown(f"***Телефон***: +{st.session_state.user_info[0][3][0]} ({st.session_state.user_info[0][3][1:4]}) {st.session_state.user_info[0][3][4:7]}-{st.session_state.user_info[0][3][7:9]}-{st.session_state.user_info[0][3][9:11]}")








    if(st.session_state.user_info[0][5] == 1 or st.session_state.user_info[0][5] == '1'):
        st.markdown(f"***Статус***: Путешественник\n")

        st.markdown("***Ваши активные брони***: ")
        active_booking = get_active_booking(st.session_state.user_info[0][0],datetime.date.today())
        if (len(active_booking) == 0):
            st.write("У вас нет активных броней.")
        else:
            st.write(f"{active_booking[0][0]}, {active_booking[0][1]}, {active_booking[0][2]},{active_booking[0][3]}")
            st.write(f"От {active_booking[0][5]} до {active_booking[0][6]}\n")

        st.markdown("***Ваши отзывы***: ")
        active_reviews = get_reviews(st.session_state.user_info[0][0])
        if(len(active_reviews) == 0):
            st.write("У вас еще нет отзывов.")
        else:
            for i in range(len(active_reviews)):
                st.write(f"{active_reviews[i][0]}, {active_reviews[i][1]}, {active_reviews[i][2]} - {active_reviews[i][3]}, {active_reviews[i][4]}")

    elif(st.session_state.user_info[0][5] == 2 or st.session_state.user_info[0][5] == '2'):
        st.markdown(f"***Статус***: Владелец")
