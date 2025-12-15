import streamlit as st
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import time
from streamlit_option_menu import option_menu
import re
from datetime import date


st.header("Indroduzindo os Elementos  do Steamlit")
menu=option_menu(menu_title="Menu",
                 options=["Inicio", "Grafico Estatistico","Grafico Dinamico", "Widgts", "Formulario"],
                 icons=["house", "bar_chat", "bar_chart_line","toggles","bar_chart"],
                 menu_icon="cast", 
                 default_index=0,
                 orientation="horizontal"
                )


