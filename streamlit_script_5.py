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
col1, col2= st.columns(2)

with col1:
    selected_city = st.selectbox('Select a City', data['City'].unique())
with col2:
    city_info = data[data['City'] == selected_city]['Population'].to_list()
    st.write('**Population**')
    st.write(f"The population of {selected_city} is {city_info[0]}")



