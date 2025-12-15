import streamlit as st
import numpy as np
import pandas as pd
import time
from streamlit_option_menu import option_menu
import re
from datetime import date

st.header("Introduzindo os Elementos do Streamlit")

menu = option_menu(
    menu_title="Menu",
    options=["Inicio", "Grafico Estatistico", "Grafico Dinamico", "Widgets", "Formulario"],
    icons=["house", "bar-chart", "graph-up", "toggles", "bar-chart"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

def carregar_dados(arquivo):
    try:
        df = pd.read_excel(arquivo)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar arquivo: {e}")
        return pd.DataFrame()

with st.sidebar:
    st.success("**UPLOAD DE DADOS**")
    dados = st.file_uploader("Carregue os dados", type=["xlsx", "xls"])

    if dados:
        df = carregar_dados(dados)
        st.subheader("Pré-visualização dos dados")
        st.dataframe(df)
    else:
        st.info("Carregue um ficheiro Excel para começar")

#INICIO
if menu == "Inicio":
    with st.expander("**sobre o instituto nacionl de estatistica**")
    st.write("acessse o site www.ine.cv")
    st.image("INE.png")

# Widgets
if menu == "Widgets":
    bt = st.button("Dê um clique!")

    if bt:
        st.info("Clicaste num botão acima!")

    sd = st.slider(
        "Novo ponto do slider!",
        min_value=25,
        max_value=35,
        value=30,
        step=1
    )

    texto = f"Eu tenho {sd} anos!"
    st.success(texto)


