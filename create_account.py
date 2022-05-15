import streamlit as st
import sidebar
def create_account():
    st.title("HESAP OLUŞTUR")
    with st.form("signupform") : 
        st.text_input("KULLANICI ADI", key="su_name")
        st.text_input("ŞİFRE", type = "password", key="su_pw")
        st.form_submit_button("Hesabını oluştur", on_click=signup)
        
def signup():
    name = st.session_state["su_name"]
    pw = st.session_state["su_pw"]
    login_tuple = [name,pw]
    st.secrets["login_data"].append(login_tuple)
    sidebar.change_page("verify")
