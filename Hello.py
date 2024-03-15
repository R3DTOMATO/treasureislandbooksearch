import streamlit as st
import time

from streamlit_option_menu import option_menu
import bookname,writername

st.set_page_config(
   page_title="보물섬",
   page_icon="보물섬로고 (1).jpg",
   layout="wide",
)

st.image('보물섬타이틀.jpg')

with st.spinner('잠시만 기다려주세요.'):
    time.sleep(1)




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
        icons=["book",":writing_hand:"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
)
    
        if app == "책명":
            bookname.app()
        if app =="작가":
            writername.app()
            
    run()
