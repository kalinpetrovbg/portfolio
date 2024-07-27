import os
import re
import smtplib
import ssl

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.header("Contact Me")


def send_email(email, message):
    host = "smtp.gmail.com"
    port = 465
    sender = email
    username = "kalinpetrovbg@gmail.com"
    password = os.getenv('EMAIL_PASSWORD')
    receiver = "kalinpetrovbg@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(sender, receiver, message)


def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


with st.form(key="contact_form", clear_on_submit=False):
    input_email = st.text_input("Your Email Address")
    input_message = st.text_area("Your Message")
    button = st.form_submit_button("Submit")
    if button:
        error_messages = []
        if not input_email or not is_valid_email(input_email):
            error_messages.append("Please enter a valid email address.")
        if not input_message:
            error_messages.append("Please enter a message.")

        if error_messages:
            st.error(" ".join(error_messages))
        else:
            send_email(input_email, input_message)
            st.success("Email sent successfully.")
