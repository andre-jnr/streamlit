import streamlit as st
import numpy as np

st.subheader('Código')

codigo = """
import streamlit as st
import numpy as np

# linhas, colunas - números aleatórios
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
"""

st.code(codigo)

st.subheader('Output')

# linhas, colunas - números aleatórios
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
