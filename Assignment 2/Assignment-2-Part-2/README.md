# CSYE7245---Team-4---Big-Data-Sys-Int-Analytics-Master

#### Team 4 : 

| NAME              |     NUID        |
|------------------ |-----------------|
| Samarth Hadawale  |   001053811     |
| Shivendra Shahi   |   001393331     |
| Siddhi Prabhu     |   001342165     |


Assignment 2 - Part 2:

#### Google Docs Link
https://docs.google.com/document/d/12VoxhbA7NaXx5GRiiRAunz3cxcH0hUMFM_bTlqL7O-A/edit?usp=sharing

#### CLAAT Link
https://codelabs-preview.appspot.com/?file_id=12VoxhbA7NaXx5GRiiRAunz3cxcH0hUMFM_bTlqL7O-A#0

### About Data Masking, Anonymization and Deanonymization

Masking is hiding data with altered values like * or # or replacing it with PII entity type
Anonymization is used to prevent someone's personal identity from being revealed by generating it's MessageHash and EntityHash which can later be deanonymized using MessageHash

### Objectives

Who- Masking and Anonymization system can be used by companies in all sectors like Healthcare, Banking, Technology etc. whose customer data needs to be kept secure

What- To Scrap data, Identify PII entities from the scrapped data, perform masking and anonymization on the identified PII entities and Deanonymize the data 

Why- Personally Identified information identifies an individual's information which cannot be shared and needs to be kept private. Masking and anonymization would assist in securing individual's personal information and Deanonymization can retrieve the data as per requirements  

When -Over a 2 weeks period timeline

Where -This project will be delivered to the companies requiring to secure their customers personal information

How- Implemented scrapping, Identify PII entites, perform masking and anonymization and deanonymize the data and used technologies like Streamlit, FastAPI, AWSCloud.

## Available Scripts

In the project directory, you can run:

### `streamlit run streamlit_app.py`
Open [http://localhost:8501](http://localhost:8501) to view it in the browser.

Hot reloading will be enabled when in settings you will select 'run on save'.<br />

### `uvicorn main:app --reload`
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
Swagger UI page will be displayed where you can test your API's


### User Authentication 

<img width="708" alt="userauth" src="https://user-images.githubusercontent.com/55570382/100290057-65fa8600-2f48-11eb-8d35-38a3fe73b10e.PNG">

#### API 1 : Scraping

![API1](https://user-images.githubusercontent.com/57429405/104782075-a3fa7600-5751-11eb-81c1-554b2d2a70df.jpg)

<img width="708" alt="API1" src="https://user-images.githubusercontent.com/55570382/100290181-b83ba700-2f48-11eb-9f3d-9887c2cad13b.PNG">

#### API 2 : Named Entity Recognition 

![API2](https://user-images.githubusercontent.com/57429405/104782131-ba083680-5751-11eb-927e-540972690ed1.jpg)

<img width="685" alt="api2" src="https://user-images.githubusercontent.com/55570382/100290198-c5f12c80-2f48-11eb-8e37-6736fb3973a8.PNG">

#### API 3 Part 1: Implement masking

![API3_Masking](https://user-images.githubusercontent.com/57429405/104782187-d015f700-5751-11eb-9e73-3e45c27164fd.jpg)

<img width="690" alt="api3_mask" src="https://user-images.githubusercontent.com/55570382/100290214-d2758500-2f48-11eb-8553-10c182767131.PNG">

#### API 3 Part 2: Anonymization functions

<img width="722" alt="API4_anonymize" src="https://user-images.githubusercontent.com/55570382/100290237-df927400-2f48-11eb-909b-d45e23886f52.PNG">

#### API 4 : Deanonymization

![API4](https://user-images.githubusercontent.com/57429405/104782271-f045b600-5751-11eb-8620-5c318dca78ac.jpg)

<img width="692" alt="DeanonymizeAPI4" src="https://user-images.githubusercontent.com/55570382/100290263-ec16cc80-2f48-11eb-9c12-f6c6121b79fb.PNG">





