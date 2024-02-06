import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")


data = pd.read_csv('data/city.csv')

st.title('Interactive Dashboard: Exploring Streamlit & Taipy Fundamentals')
st.sidebar.write('Streamlit by Zahra')
st.write ('**French Cities Dashboard**')
st.write('Data Frame')
st.dataframe(data.head(5))
fig = px.bar(data, x='City', y='Population', title='Population of French Cities')
st.plotly_chart(fig)


