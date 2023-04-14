# file: spinner.py

import streamlit as st
#방법2  st.spinner 사용 
import time 

with st.spinner('Wait for it...'):
  time.sleep(5)
  st.success('Done!') 
  