import streamlit as st
import base64
import requests
import json

import sidebar

def try_verify():
    if(not st.session_state["verified"]):
            st.warning("Lütfen sizden istenilen bilgileri verin")
    else:
            sidebar.change_page("swipe_page")

def upload_id():
    if 'verified' not in st.session_state:
        st.session_state['verified'] = False
    
    picture = st.camera_input("Fotograf Cek")

    uploaded_file = st.file_uploader("Fotoğraf Seçiniz")
    st.button("İş bulmaya başla!",on_click=try_verify)
    
    if(uploaded_file is not None):
        picture = uploaded_file
    if picture:
        st.image(picture)
        data = base64.b64encode(picture.getvalue())
        url = "https://base64.ai/api/scan"
        payload = json.dumps({
        "image": "data:image/png;base64,"+data.decode('utf-8'),
        "modelTypes":"id/tur"      
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'ApiKey bahadiratilgan136@gmail.com:cb800714-2da5-441b-a4c5-4ddc03f4b552'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        st.session_state["id_data"] = json.loads(response.content)
        if(st.session_state["id_data"][0]["model"]["type"] != "id/tur"):
            st.warning("Lütfen bir T.C. kimlik kartı resmi yükleyin (Fotoğraf çözünürlüğünün düşük olması bu hatayı almanıza sebep olabilir)")
        else:
            id_fields = st.session_state["id_data"][0]["fields"]
            #fields.sex.value fields.age.value fields.givenName.value fields.familyName.value
            st.session_state["current_usr"] = [id_fields["sex"]["value"], id_fields["age"]["value"], id_fields["givenName"]["value"], id_fields["familyName"]["value"]]
            st.write(st.session_state["current_usr"])
            st.session_state["verified"] = True
            st.session_state["logged_in"] = True

   