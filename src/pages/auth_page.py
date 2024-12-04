import streamlit as st
from auth_conn import reg_new_user, chek_auth_user, return_user_data,check_new_user_login
from input_validation import valid_login, valid_email, valid_phone, valid_role, valid_password
from hash_password import hash_password


# Функция для страницы регистрации
def registration_page():
    st.title("Регистрация")

    # Поля для ввода информации
    login = st.text_input("Логин")
    phone = st.text_input("Телефон (в формате 71234567890)")
    email = st.text_input("Электронная почта")
    role = st.text_input("Роль: Введите 1 если вы арендатор, 2 если вы арендодатель")
    password = st.text_input("Пароль", type='password')

    # Кнопка для отправки регистрации
    if st.button("Зарегистрироваться"):
        if login and phone and email and role and password:
            if (not valid_login(login)):
                st.error("Некорректный логин")
            elif (not valid_phone(phone)):
                st.error("Некорректный телефон")
            elif (not valid_email(email)):
                st.error("Некорректный email")
            elif (not valid_role(role)):
                st.error("Некорректная роль")
            elif (not valid_password(password)):
                st.error("Некорректный пароль")
            else:
                if check_new_user_login(login):
                    st.success("Вы успешно зарегистрированы!")

                    # Добавляю нового пользователя в БД
                    reg_new_user(login, phone, email, role, hash_password(password))

                    # Сохраняю данные зарегистрированного пользователя
                    user_data = return_user_data(login, hash_password(password))
                    user_data[0] = list(user_data[0])
                    st.session_state.user_info = user_data

                    st.session_state.page = "initial"
                else:
                    st.error("Пользователь с таким логином уже есть")

        else:
            st.error("Пожалуйста, заполните все поля.")

    # Кнопка для перехода на страницу входа
    if st.button("Уже есть аккаунт? Войти"):
        st.session_state.page = "login"


# Функция для страницы входа
def login_page():
    st.title("Вход в аккаунт")

    # Поля для ввода информации
    login = st.text_input("Логин")
    password = st.text_input("Пароль", type='password')

    # Кнопка для отправки данных для входа
    if st.button("Войти"):
        if login and password:
            if (chek_auth_user(login, hash_password(password)) == 1):
                st.error("Нет такого пользователя")
            else:
                st.success("Вы успешно вошли в аккаунт!")
                user_data = return_user_data(login, hash_password(password))
                user_data[0] = list(user_data[0])
                st.session_state.user_info = user_data
                st.session_state.page = "initial"
        else:
            st.error("Пожалуйста, введите логин и пароль.")

    # Кнопка для перехода на страницу регистрации
    if st.button("Нет аккаунта? Зарегистрироваться"):
        st.session_state.page = "registration"
