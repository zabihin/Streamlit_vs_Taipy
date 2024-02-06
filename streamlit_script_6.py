import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")


data = pd.read_csv('data/city.csv')
st.title('Interactive Dashboard: Exploring Streamlit & Taipy Fundamentals')
st.sidebar.write('Streamlit by Zahra')


col1, col2= st.columns(2)
with col1:
    pege_1 = st.button('page 1')
with col2:
    pege_2 = st.button('Page 2')
   
if pege_1:
    
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
        st.header("Population")
        st.write(f"The population of {selected_city} is {city_info[0]}")

if pege_2:
    fig = px.scatter_mapbox(data, lat='Latitude', lon='Longitude',size='Population', zoom=5,mapbox_style="open-street-map", height=600)
    st.header('Map of French Cities')
    st.plotly_chart(fig)
