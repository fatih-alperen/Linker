import streamlit as st
import sidebar

def swipe_page():
    displayJob()
    st.button("İlgilenmiyorum", on_click=ignore)
    st.button("Harika!",on_click=celebrate)

def celebrate():
    st.balloons()
def ignore():
    getJob()

def getJob():
    #get next job from jobs and display
    st.session_state["current_job"] += 1
    if(st.session_state["current_job"]>= len(st.session_state["job_list"])):
        st.session_state["current_job"] = 0

def displayJob():
    job = st.session_state["job_list"][st.session_state["current_job"]]
    for i in range(5):
        st.write(job[i])