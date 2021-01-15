import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image
import json,requests
global authValue
authValue = False

radio = st.sidebar.radio(
    "Select from options!",
    ("Welcome Page","Sentiment Score")
)



st.markdown('<style>body{background-color: #FFF2C2;}</style>',unsafe_allow_html=True)


if radio == 'Welcome Page':
    

    st.title('**_Welcome to Sentiment Analysis System!_**')
    image = Image.open('download.jpg')
    st.image(image, caption='',use_column_width=True)

   

if radio == 'Sentiment Score':
    
    st.title('Sentiment Analysis of the file')

    st.subheader('_Please enter sentence_')
    filename = st.selectbox(
    "Choose the anonymize data file to analyze :",
    ('No Selection','abcde.txt','abc11.txt','abc1.txt','abc51.txt'))
 

    if st.button('Check Sentiment'):

            response = requests.post(f"http://127.0.0.1:8000/predict?filename={filename}")

            st.subheader(response.json()) 

