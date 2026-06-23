import streamlit as st

st.set_page_config(page_title="Hello Streamlit", page_icon="👋", layout="centered")

st.title("Hello, Streamlit Community Cloud!")
st.write("This is a minimal app deployed from GitHub.")

name = st.text_input("Enter your name")
if name:
    st.success(f"Welcome, {name}!")
