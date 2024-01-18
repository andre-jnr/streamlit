import streamlit as st

st.subheader("Código")

code = """
import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


name = st.text_input("Your name", key="name")

# You can access the value at any point with:
if st.session_state.name:
    st.write(f'Olá {name}')
"""
st.code(code)

st.subheader("Output")

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


name = st.text_input("Your name", key="name")

# You can access the value at any point with:
if st.session_state.name:
    st.write(f'Olá {name}')
