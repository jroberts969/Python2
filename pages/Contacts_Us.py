import streamlit as st
from send_email import send_email

st.header("Contact me")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address", value="j_droberts@yahoo.co.uk" )
    user_message = st.text_area("Your message")
    button = st.form_submit_button()

    if button:
        print("I was pressed")
        send_email(receiver=user_email, message=user_message)
