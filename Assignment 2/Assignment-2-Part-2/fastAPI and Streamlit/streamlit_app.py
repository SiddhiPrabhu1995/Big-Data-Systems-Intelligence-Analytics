import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image
import json,requests
verified = "True"

radio = st.sidebar.radio(
    "Select from options!",
    ("User Authentication","Scraping","Identify_PII_Entity","Mask Entities","Replace with EntityType","Anonymization")
)

st.markdown('<style>body{background-color: #FFF2C2;}</style>',unsafe_allow_html=True)

if radio == 'Scraping':
    
    st.title('Scraping')
    st.subheader('_Please enter link to be scraped_')
    
    sentence = st.text_input("Link Input")

    if st.button('Scrape'):
            payload = json.dumps({
                "link" : sentence
                })
            response = requests.get(f"http://127.0.0.1:8000/scrap?enterurl={sentence}")
            data_list = response.json()
            
            st.subheader("Scraping Done Successfully!!")

    st.subheader('_View Scraped Data_')
    if st.button('Display Scraped Data'):
            response = requests.get(f"http://127.0.0.1:8000/displayscrapdata")
            data_list = response.json()
   
            b=data_list['body']

            st.subheader(b)  

if radio == 'Identify_PII_Entity':
    
    st.title('Identify PII Entities')
    st.subheader('_Please click the button to Identify PII entities_')

    if st.button('Identify Entities'):

            response = requests.get(f"http://127.0.0.1:8000/identifyEntity?verified={verified}")
            data_list = response.json()
            b=data_list['body']
            
            st.subheader(b)

if radio == 'Mask Entities':
    
    st.title('Mask Entities')

    
    st.subheader('_Please click the button to Mask Entities_')
    
    if st.button('Masking'):

            response = requests.get(f"http://127.0.0.1:8000/maskEntity")
            data_list = response.json()
            b=data_list['body']
            st.subheader(b)

    if st.button('View Mask Entities'):

            response = requests.get(f"http://127.0.0.1:8000/display_mask_entity")
            data_list = response.json()
            b=data_list['body']
            st.subheader(b)

 #Replace with PII Entity Type       
if radio == 'Replace with EntityType':
    
    st.title('Replace with EntityType')

    
    st.subheader('_Please click the button to Replace with EntityType_')

    if st.button('Replace with EntityType'):

            response = requests.get(f"http://127.0.0.1:8000/replacePIIEntity")
            data_list = response.json()
            b=data_list['body']
            st.subheader(b)

    if st.button('View data Replaced with EntityType'):

            response = requests.get(f"http://127.0.0.1:8000/displayPIIEntity")
            data_list = response.json()
            b=data_list['body']
            st.subheader(b)

if radio == 'Anonymization':
  
    st.title('Anonymization')
    st.subheader('_Click button to deidentify entities_')

    if st.button('Anonymize'):

            response = requests.get(f"http://127.0.0.1:8000/Anonymize")
            data_list = response.json()
            b=data_list['body']
            st.subheader(b)

    if st.button('DeAnonymize'):

            response = requests.get(f"http://127.0.0.1:8000/deanonymize")
            data_list = response.json()
            b=data_list['body']
            st.subheader(b)

if radio == 'User Authentication':
    

    st.title('**_SYMPHONYLABS Welcomes you to their own Deidentification System!_**')
    image = Image.open('img-2.png')
    st.image(image, caption='',use_column_width=True)

    st.header('User Authentication')

    st.subheader('_Please enter valid username and password_')
    
    username = st.text_input('Username')
    password = st.text_input('Password')
   

    if st.button('Authenticate'):

            response = requests.get(f"http://127.0.0.1:8000/Authentication?usrName=username&usrPassword=password")
            data_list = response.json()
           
            verified = data_list
            print(verified)
            st.subheader(data_list)

