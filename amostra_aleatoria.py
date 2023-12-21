import streamlit as st
import numpy as np

# linhas, colunas - números aleatórios
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)