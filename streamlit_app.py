import streamlit as st
from create_account import create_account   
from swipe_page import swipe_page
from upload_id import upload_id
import sidebar

if 'key' not in st.session_state:
    st.session_state['key'] = 'login_page'
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'signUp' not in st.session_state:
    st.session_state['signUp'] = False
if 'job_list' not in st.session_state:
    st.session_state['job_list'] = [
        #name location desc needs payment
        ["Kurye","Beşiktaş","Motor Ehliyeti","10000 tl","iletişim numarası:1234567"],
        ["SWE","Nişantaşı","CS diploması","100000 tl","iletişim numarası:1234567"],
        ["Hademe","Çekmeköy","Yok","6000 tl","iletişim numarası:1234567"],
        ["Güvenlik Görevlisi","Levent","Güvenlik lisansı","12000 tl","iletişim numarası:1234567"],
    ]
if 'current_job' not in st.session_state:
    st.session_state['current_job'] = 0

st.session_state["current_usr"] = []

    
state = st.session_state['key']

if (state == 'create_account'):
    sidebar.newAccPage()
elif (state == 'verify'):
    upload_id()
elif (state == 'upload_id'):
    upload_id()
elif (state == 'swipe_page'):
    swipe_page()
elif(state == 'login_page'):
    sidebar.loginPage()