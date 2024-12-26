import streamlit as st
from streamlit import button, form_submit_button
from send_email import send_email



st.header("Contact Me")




with st.form(key="email_forms"):#This is the unique key for this form, allowing you to reference it.
    user_email = st.text_input("Your email address")#This function creates a text input field where the user can enter their email address.
    row_message = st .text_area("Your message")#This function creates a larger text input box where the user can write their message. The content they enter is stored in row_message.

    message = f"""\
Subject: New Email from {user_email}

From:{user_email}
{row_message}


"""

    btn = st.form_submit_button("Submit")
    print(btn)
    if btn:
        send_email(message)
        st.info("Your email was sent Succesfully")
