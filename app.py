import streamlit as st
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import time
from streamlit_option_menu import option_menu
#import re
#from datetime import date


st.header("Indroduzindo os Elementos  do Steamlit")
menu=option_menu(menu_title="Menu",
                 options=["Inicio", "Grafico Estatistico","Grafico Dinamico", "Widgts", "Formulario"],
                 icons=["house", "bar-chart", "graph-up", "toggles", "bar-chart"],
                 menu_icon="cast", 
                 default_index=0,
                 orientation="horizontal"
                )
with st.sidebar:
  st.success("**UPLOAD DE DADOS**")
  dados = st.file_uploader(
    "Carregue os dados",
    type=["xlsx", "xls"]
  )    
  if dados:
    def carregar_dados(dados):
      try:
        df=pd.read_excel(dados)
        return df
      except FileNotFoundError:
        return pd.DataFrame()
        df=carregar_dados(dados)
        st.table(df)
      else:
        st.info("Carregue um ficheiro Excel para começar")
        

