import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")


df = pd.read_csv('data/city.csv')

st.title('Interactive Dashboard: Exploring Streamlit & Taipy Fundamentals')
st.write ('**French Cities Dashboard**')
