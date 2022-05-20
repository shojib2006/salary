import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from member_page import show_member_page

page = st.sidebar.selectbox("Page", ("Predict", "Explore", "Member"))

if page == "Predict":
    show_predict_page()
elif page == "Explore":
    show_explore_page()
elif page == "Member":
    show_member_page()