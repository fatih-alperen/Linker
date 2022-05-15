import streamlit as st

def change_page(target):
    st.session_state['key'] = target

def loginSidebar():
    with st.sidebar:
        st.title("GİRİŞ EKRANI")
        with st.form("loginform") : 
            st.text_input("KULLANICI ADI", key="login_name")
            st.text_input("ŞİFRE", type = "password", key="login_pw")
            st.form_submit_button("Giriş yap", on_click=auth)
        st.button("Hesap oluştur",on_click=change_page,args=("create_account",) )

def loginPage():
        st.title("GİRİŞ EKRANI")
        with st.form("loginform") : 
            st.text_input("KULLANICI ADI", key="login_name")
            st.text_input("ŞİFRE", type = "password", key="login_pw")
            st.form_submit_button("Giriş yap", on_click=auth)
        st.button("Hesap oluştur",on_click=change_page,args=("create_account",) )


def newAccSidebar():
    with st.sidebar:
        st.title("HESAP OLUŞTUR")
        with st.form("signupform") : 
            st.text_input("KULLANICI ADI", key="su_name")
            st.text_input("ŞİFRE", type = "password", key="su_pw")
            st.form_submit_button("Devam et", on_click=signup)
            
def newAccPage():
        st.title("HESAP OLUŞTUR")
        with st.form("signupform") : 
            st.text_input("KULLANICI ADI", key="su_name")
            st.text_input("ŞİFRE", type = "password", key="su_pw")
            st.form_submit_button("Devam et", on_click=signup)

def fav_adv():
    with st.sidebar:     
        st.title("Giriş yapıldı")
        for i in range(4):
            st.write(st.session_state["current_usr"][i])

def auth():
    name = st.session_state["login_name"]
    pw = st.session_state["login_pw"]
    if (
            [name,pw] in st.secrets["login_data"]
        ):
            #st.session_state['logged_in'] = True 
            change_page("verify")

    else:
        st.warning("Kullanıcı adı ve şifre eşleşmiyor")

def signup():
    name = st.session_state["su_name"]
    pw = st.session_state["su_pw"]
    login_tuple = [name,pw]
    st.secrets["login_data"].append(login_tuple)
    st.session_state["signUp"]=False

def sidebar():
    pass
    isLogged = st.session_state['logged_in']
    if(isLogged):
        fav_adv()
    else:
        loginSidebar()
