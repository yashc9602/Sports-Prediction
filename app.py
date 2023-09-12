import streamlit as st
from predict_cricket import show_predict_page
from news import fetch_news
from football import show_details
st.sidebar.title("Hello there.....")
st.sidebar.write("How you feeling today?")
selection = st.sidebar.selectbox("Explore", ("Cricket","Football","News"))
if selection == "Cricket":
    show_predict_page()
elif selection == "Football":
    show_details()
else:
    fetch_news()