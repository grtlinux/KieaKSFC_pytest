# file: title.py

import streamlit as st
import pandas as pd

st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is a text')
st.markdown('This is a markdown')
st.latex(r'''e^{i\pi} + 1 = 0''')
st.write('This is a write')
st.write(['This is a list', 'This is a list'])
st.write({'This is a dict': 'This is a dict'})
st.write(pd.DataFrame({'This is a dataframe': ['This is a dataframe']}))

