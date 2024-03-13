import streamlit as st
import pandas as pd
import urllib 
from urllib.request import urlopen

def app():
    def book():
        url="https://drive.google.com/file/d/1qZKgawn4iYB6ADeUnWuu4s2Put7T4Ltt/view?usp=sharing"
        response = urllib.request.urlopen(url)
        df = pd.read_csv("도서정보.csv")
        return df.set_index("책제목")

    try:
        urllib.request.urlopen("https://drive.google.com/file/d/1qZKgawn4iYB6ADeUnWuu4s2Put7T4Ltt/view?usp=sharing")
        df = book()
        bookSelect = st.selectbox(
        label="책 이름을 입력하세요", options=list(df.index)
        )
        if not bookSelect:
            st.error("책 이름을 선택해주세요")
        else:
            data = df.loc[bookSelect]
            st.write('당신이 선택한 책:',bookSelect, options=list(df.index))

            data = data.T.reset_index()
        

    except urllib.error.URLError as e:
        print ('Error code: ', e.code)
