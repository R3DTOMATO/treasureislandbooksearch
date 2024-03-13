import streamlit as st
import time

from streamlit_option_menu import option_menu
import bookname,writername

st.set_page_config(
   page_title="보물섬",
   page_icon="books.png",
   layout="wide",

)

st.title(':green[보물섬] 도서 검색사이트입니다.')
st.image('보물섬로고.png')

with st.spinner('잠시만 기다려주세요.'):
    time.sleep(5)




class MultiApp:
    
    def __init__(self):
        self.apps =[]
    def add_app(self, title, function):
        self.apps.append({
            "title":title,
            "function":function
        })
        
    def run():
        
        app = option_menu(
        menu_title=None,
        options=["책명","작가"],
        icons=["book","✍"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
)
    
        if app == "책명":
            bookname.app()
        if app =="작가":
            writername.app()
            
    run()
