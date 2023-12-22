import streamlit as st
import pandas as pd

st.title("Código")

codigo = """
st.set_page_config(page_title='Meu site Streamlit')

with st.container():
    st.subheader('Meu primeiro site com Streamlit')
    st.title('Registro de contratos')
    st.write('Informações sobre os contratos fechados pela control ao longo de maio')
    st.write(
        'Quer ver mais código: [clique aqui](https://github.com/andre-jnr)')


@st.cache_data
def carregar_dados():
    tabela = pd.read_csv('resultados.csv')
    return tabela


with st.container():
    st.write('---')
    dados = carregar_dados()
    qtde_dias = st.selectbox('Selecione o periodo', [
                             '7D', '15D', '21D', '30D'])
    num_dias = int(qtde_dias.replace('D', ''))
    dados = dados[-num_dias:]
    st.area_chart(dados, x='Data', y='Contratos')
    st.bar_chart(dados, x='Data', y='Contratos')
"""

st.code(codigo)

st.title("Output")

with st.container():
    st.subheader('Meu primeiro site com Streamlit')
    st.title('Registro de contratos')
    st.write('Informações sobre os contratos fechados pela control ao longo de maio')
    st.write(
        'Quer ver mais código: [clique aqui](https://github.com/andre-jnr)')


@st.cache_data
def carregar_dados():
    tabela = pd.read_csv('pages/resultados.csv')
    return tabela


with st.container():
    st.write('---')
    dados = carregar_dados()
    qtde_dias = st.selectbox('Selecione o periodo', [
                             '7D', '15D', '21D', '30D'])
    num_dias = int(qtde_dias.replace('D', ''))
    dados = dados[-num_dias:]
    st.area_chart(dados, x='Data', y='Contratos')
    st.bar_chart(dados, x='Data', y='Contratos')
