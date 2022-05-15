from attr import NOTHING
import streamlit as st
st.title("Yetenekler")

#il ilce adres
city = st.text_input("Şehir giriniz..")
district = st.text_input("İlce giriniz")
adress = st.text_input("Adres giriniz...")
#egitim
education = st.radio("Eğitim Durumunuzu Seçiniz: ",('Diğer','Okuryazar','İlköğretim','Lise','Ön Lisans','Lisans','Yüksek Lisans','Doktora'))

if(not(education == NOTHING)):
    st.write("aferim")

language = st.multiselect('Yabancı Dil',['İngilizce','Fransızca','Almanca','Arapça'])

