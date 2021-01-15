# CSYE7245---Team-4---Big-Data-Sys-Int-Analytics-Master

## Assignment 3 - To deploy a sentiment analysis model to create a Model-as-a-service for anonymized data 

| NAME              |     NUID        |
|------------------ |-----------------|
| Samarth Hadawale  |   001053811     |
| Shivendra Shahi   |   001393331     |
| Siddhi Prabhu     |   001342165     |


1. Google Docs Link : https://docs.google.com/document/d/167AMoTA-tuPNzGO_mYGN3pgtVuYu8BRkLI9biF1L78g/edit?usp=sharing

2. CLAT Document Link : https://codelabs-preview.appspot.com/?file_id=167AMoTA-tuPNzGO_mYGN3pgtVuYu8BRkLI9biF1L78g#0

### About Sentiment Analysis

![SENTIMENT](https://user-images.githubusercontent.com/57429405/104778822-fe90d380-574b-11eb-8785-75458816efa4.jpg)

Sentiment Analysis is a process of determining the emotional tone behind a series of words, used to gain an understanding of the the attitudes, opinions and emotions expressed within an online mention.

Sentiment Analysis helps businesses understand how customers feel about their brand, giving them first-hand information to improve their products, make data-driven decisions, and deliver better customer experiences.

### Objectives

Who - Helps Data analysts within large organizations conduct market research, monitor brand and product reputation, and understand customer experiences.Analyzing the sentiment can be used by companies in various sectors to classify the sentence sentiment as positive, negative or neutral.

What - Train tensorflow model using Bert, integrated trained model to fastaspi code to analyze the text files stored in S3 from previous assignment, Dockerized the API service and built a streamlit application to access API service

Why - To understand sentiment of the text for customer review analysis, conduct market research and monitor reputation

When - Over one week period timeline

Where - This project will be delivered to companies requiring to analyze their data in order to develop better marketing strategies, improve customer satisfaction, to analyze which movies/tv series are doing well and getting better reviews etc.

How - Implemented tensorflow model(python), AWS cloud services, FastAPI, Docker and Streamlit

### 1.Train TensorFlow models using TensorFlow Extended (TFX) 

Followed the reference architectures : https://blog.tensorflow.org/2020/03/part-1-fast-scalable-and-accurate-nlp-tensorflow-deploying-bert.html

https://blog.tensorflow.org/2020/06/part-2-fast-scalable-and-accurate-nlp.html

<img width="357" alt="bertLayer" src="https://user-images.githubusercontent.com/57429405/104778956-3dbf2480-574c-11eb-8e02-8c843ba9b354.PNG">

Train the model for the anonymized data using BERT and this architecture that leverages TensorFlow Hub, Tensorflow Transform, TensorFlow Data Validation and Tensorflow Text and Tensorflow Serving 

### 2.Serve the model as a REST API 

Reference link: https://github.com/curiousily/Deploy-BERT-for-Sentiment-Analysis-with-FastAPI

##### Swagger UI

<img width="759" alt="swaggerUI" src="https://user-images.githubusercontent.com/57429405/104779596-5a0f9100-574d-11eb-8ff1-67e6d21733b1.PNG">

##### Available Scripts

To run FastAPI code go to project directory:-

#### `uvicorn sentiment_analyzer.api:app`


### 3.Dockerize the API service. For sample code on how to Dockerize API

Building Docker Image:-

#### `docker build -t myfirstapi .`

Running the image on Docker container

#### `docker run -i --name myapicontainer -p 8000:8000 myfirstapi`

### 4.Build a Reference App in Streamlit to test the API

Reference link:- https://testdriven.io/blog/fastapi-streamlit/

##### Welcome Page

<img width="686" alt="welcomepage" src="https://user-images.githubusercontent.com/57429405/104779448-246aa800-574d-11eb-9083-7055dac588f0.PNG">

##### Analyze Sentiments

<img width="696" alt="Sentiments" src="https://user-images.githubusercontent.com/57429405/104779865-d609d900-574d-11eb-83b5-3e460fa1c042.PNG">

#### To run the streamlit app go to project directory:-

#### `streamlit run streamlit_app.py`
