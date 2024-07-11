import streamlit as st
import pandas as pd

clientes = pd.read_csv('clientes.csv')

st.title('Clientes cadastrados')
st.divider()
st.dataframe(clientes)