import streamlit as st
from send_email import send_email
import pandas as pan

df = pan.read_csv("topics.csv")

st.header("Contact me")

with st.form(key="email_form"):
    #print("df=" + df)
    #print("df[topic]=" + df["topic"])

    user_email = st.text_input("Your Email Address", value="j_droberts@yahoo.co.uk" )

    option = st.selectbox(
        'What topic would you like to discuss?', df["topic"]
        )

    user_message = st.text_area("Your message")

    button = st.form_submit_button()

    if button:
        print("I was pressed")
        send_email(receiver=user_email, message=user_message, option=option)
        st.info("The email was sent successfully")