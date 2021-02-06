# app.py, run with 'streamlit run app.py'
import pandas as pd
import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\Kajal C Soni\Downloads\state_wise.csv")  # read a CSV file inside the 'data" folder next to 'app.py'

#t.title("Covid-19 India")  # add a title
#st.write(df)

st.title("Covid-19 Dashboard For India")
st.markdown('The dashboard will visualize the Covid-19 Situation in India')
st.markdown('Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.')
st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:")
select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
if not st.sidebar.checkbox("Hide", True, key='1'):
    if select == 'Pie chart':
        st.title("Selected top 5 cities")
        fig = px.pie(df, values=df['Confirmed'][:5], names=df['State'][:5], title='Total Confirmed Cases')
        st.plotly_chart(fig)
        if select=='Bar plot':
         st.title("Selected Top 5 Cities")
fig = go.Figure(data=[
    go.Bar(name='Confirmed', x=df['State'][:5], y=df['Confirmed'][:5]),
    go.Bar(name='Recovered', x=df['State'][:5], y=df['Recovered'][:5]),
    go.Bar(name='Active', x=df['State'][:5], y=df['Active'][:5])])
st.plotly_chart(fig)

df2 = pd.read_csv(r"C:\Users\Kajal C Soni\Downloads\case_time_series.csv")
df2['Date'] =  df2['Date']
select1 = st.sidebar.selectbox('Select', ['Confirmed', 'Recovered'], key='2')
if not st.sidebar.checkbox("Hide", True, key='3'):
    if select1 == 'Confirmed':
        fig = px.line(df2, x="Date", y="Total Confirmed")
        st.plotly_chart(fig)
    elif select1 == 'Recovered':
        fig = px.line(df2, x="Date", y="Daily Recovered")
        st.plotly_chart(fig)


