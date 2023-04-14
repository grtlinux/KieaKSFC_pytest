# file: image.py

import streamlit as st
from PIL import Image

#PIL 패키지에 이미지 모듈을 통해 이미지 열기 
# Image.open('이미지 경로')
zarathu_img = Image.open('re_special_chars.png')
# zarathu_img = Image.open('https://github.com/grtlinux/KieaTips22/blob/main/python/Visual_Studio_Code_Hot_Keys.png?raw=true')

col1,col2 = st.columns([2,3])

with col1 :
  # column 1 에 담을 내용
  st.title('here is column1')
with col2 :
  # column 2 에 담을 내용
  st.title('here is column2')
  st.checkbox('this is checkbox1 in col2 ')


# 컬럼2에 불러온 사진 표시하기
col2.image(zarathu_img)

