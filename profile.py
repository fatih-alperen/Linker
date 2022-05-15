import streamlit as st
def profile_page():
    st.write("profil sayfası")
    st.button("İş aramaya devam et",on_click=change_page, args=("swipe_page",))
