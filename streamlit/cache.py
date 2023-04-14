# file: cache.py

import streamlit as st
import pandas as pd 

file_path = '~~~filepath'
@st.cache
def load_data():
  data = pd.read_csv(file_path)
  return data
