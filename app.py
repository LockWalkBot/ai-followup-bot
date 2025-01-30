import streamlit as st
from ai_logic import generate_reply

st.title("AI-Powered Engagement Bot")

user_message = st.text_input("Enter a customer message:")

if st.button("Get AI Reply"):
    ai_response = generate_reply(user_message)
    st.write(f"AI Response: {ai_response}")
