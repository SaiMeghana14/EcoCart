import streamlit as st

def show():
    st.header("🔐 Simple Login (Demo Mode)")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "user" and password == "pass":
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials")
