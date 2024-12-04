import streamlit as st
from time import sleep
from user_hotel_conn import calculate_price
from add_hotel_conn import get_room_id
from booking_conn import add_new_booking, get_booking_id,add_new_transaction
from input_validation import valid_country
import datetime

def booking_page():
    st.title("Бронирование")

    country = st.text_input("Страна")
    city = st.text_input("Город")
    name = st.text_input("Название отеля")
    room = st.text_input("Комната")
    check_in_date = st.date_input("Дата заезда")
    check_out_date = st.date_input("Дата выезда")
    num_guests = st.text_input("Количество гостей")

    if "booking_page_continue" not in st.session_state:
        st.session_state["booking_page_continue"] = False

    if "booking_page_choose" not in st.session_state:
        st.session_state["booking_page_choose"] = False

    if st.button("Продолжить"):
        st.session_state["booking_page_continue"] = not st.session_state["booking_page_continue"]

    if st.session_state["booking_page_continue"]:
        if country and city and name and room and check_in_date and check_out_date and num_guests:
            if valid_country(country):
                if(check_in_date < check_out_date):
                    if(check_in_date >= datetime.date.today()):
                        st.session_state.final_price = calculate_price(country, city, name, room, check_in_date, check_out_date,
                                                           num_guests)
                        st.write(f"Сумма заказа составляет {st.session_state.final_price} руб.")
                        st.session_state.payment_method = st.selectbox("Выберите способ оплаты",
                                                           ("-", "Наличными при заселении", "СБП (временно недоступно)",
                                                            "Картой (временно недоступно)"))
                        if st.button("Выбрать"):
                            st.session_state["booking_page_choose"] = not st.session_state["booking_page_choose"]
                    st.error("Неправильно выбраны даты")
                else:
                    st.error("Неправильно выбраны даты")
            else:
                st.error("Ошибка! неправльно введена страна")
        else:
            st.error("Заполните все поля")

    if (st.session_state["booking_page_continue"] and st.session_state["booking_page_choose"]):
        if (st.session_state.payment_method == "СБП (временно недоступно)"):
            # phone = st.text_input("Введите номер телефона")
            # bank = st.selectbox("Выберите мобильный банк", ("Сбер", "Т-Банк", "ВТБ", "Альфа-Банк"))
            # pay = "sbp"
            st.error("Извините, но оплата по СБП временно недоступна. Выберите альтернативный способ опалты")
            # if st.button("Оплатить"):
            #     sleep(5)
            #     st.success("Оплата прошла успешно")
            #     st.write("Приятной поездки!")
        elif (st.session_state.payment_method == "Картой (временно недоступно)"):
            # card_number = st.text_input("Введите номер карты")
            # bank = st.selectbox("Выберите мобильный банк", ("Сбер", "Т-Банк", "ВТБ", "Альфа-Банк"))
            # csv_code = st.text_input("Введите csv-код карты (3 цифры на обратной стороне)", type="password")
            # pay = "card"
            st.error("Извините, но оплата картой временно недоступна. Выберите альтернативный способ опалты")
            # if st.button("Оплатить"):
            #     sleep(5)
            #     st.success("Оплата прошла успешно")
            #     st.write("Приятной поездки!")
        elif (st.session_state.payment_method == "Наличными при заселении"):
            pay = "cash"
            st.success("Приятной поездки!")
            room_id = get_room_id(country, city, name, room)[0][0]
            add_new_booking(room_id, st.session_state.user_info[0][0], check_in_date, check_out_date, status=True)
            booking_id = get_booking_id(room_id, st.session_state.user_info[0][0], check_in_date, check_out_date)[0][0]
            add_new_transaction(booking_id, st.session_state.final_price, pay)

    # if st.button("Продолжить"):
    #     if country and city and name and room and check_in_date and check_out_date and num_guests:
    #         final_price = calculate_price(country, city, name, room, check_in_date, check_out_date, num_guests)
    #         st.write(f"Сумма заказа составляет {final_price} руб.")
    #         payment_method = st.selectbox("Выберите способ оплаты",
    #                                       ("-", "Наличными при заселении", "СБП (временно недоступно)", "Картой (временно недоступно)"))
    #         if st.button("Выбрать"):
    #             st.write("djshjkfad")
    #             if (payment_method == "СБП (временно недоступно)"):
    #                 # phone = st.text_input("Введите номер телефона")
    #                 # bank = st.selectbox("Выберите мобильный банк", ("Сбер", "Т-Банк", "ВТБ", "Альфа-Банк"))
    #                 # pay = "sbp"
    #                 st.error("Извините, но оплата по СБП временно недоступна. Выберите альтернативный способ опалты")
    #                 # if st.button("Оплатить"):
    #                 #     sleep(5)
    #                 #     st.success("Оплата прошла успешно")
    #                 #     st.write("Приятной поездки!")
    #             elif (payment_method == "Картой (временно недоступно)"):
    #                 # card_number = st.text_input("Введите номер карты")
    #                 # bank = st.selectbox("Выберите мобильный банк", ("Сбер", "Т-Банк", "ВТБ", "Альфа-Банк"))
    #                 # csv_code = st.text_input("Введите csv-код карты (3 цифры на обратной стороне)", type="password")
    #                 # pay = "card"
    #                 st.error("Извините, но оплата картой временно недоступна. Выберите альтернативный способ опалты")
    #                 # if st.button("Оплатить"):
    #                 #     sleep(5)
    #                 #     st.success("Оплата прошла успешно")
    #                 #     st.write("Приятной поездки!")
    #             elif (payment_method == "Наличными при заселении"):
    #                 pay = "cash"
    #                 st.write("Приятной поездки!")
    #     else:
    #         st.error("Заполните все поля")
