import streamlit as st

st.header("Contact me")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    user_message = st.text_area("Your message")
    button = st.form_submit_button()

    if button:
        print("I was pressed")
