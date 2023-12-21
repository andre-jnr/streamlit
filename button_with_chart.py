import streamlit as st
import numpy as np
import pandas as pd

st.checkbox('Show dataframe 2')
st.checkbox('Show dataframe 3')
st.checkbox('Show dataframe 4')

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data