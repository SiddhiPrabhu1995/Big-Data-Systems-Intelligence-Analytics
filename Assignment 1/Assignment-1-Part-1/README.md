# CSYE7245---Team-4---Big-Data-Sys-Int-Analytics-Master

## Assignment 1- Data as a Service 

| NAME              |     NUID        |
|------------------ |-----------------|
| Samarth Hadawale  |   001053811     |
| Shivendra Shahi   |   001393331     |
| Siddhi Prabhu     |   001342165     |


1. Google Docs Link : https://docs.google.com/document/d/1YLTFKUzdbuxrQO2cLU5RBFUIdrHWENIF0l27dtXGxLo/edit?usp=sharing

2. CLAT Document Link : https://codelabs-preview.appspot.com/?file_id=1YLTFKUzdbuxrQO2cLU5RBFUIdrHWENIF0l27dtXGxLo#0

3. Google Colab Link : https://colab.research.google.com/drive/1ZHoeErJbaOD6uKB3tTksM0iZYcbcMFBl#scrollTo=59WWk7oRRZaD

### Task 1 :- About Moody Analytics:-

![Moodys](https://user-images.githubusercontent.com/57429405/104783487-208e5400-5754-11eb-9136-a8b55afaf339.png)

Moody’s Analytics provides financial intelligence and analytical tools to help business leaders make better, faster decisions

Moody analytics provides DaaS solution

Moody’s Analytics provides a robust set of APIs that enable users to interact with their economic and credit solutions

#### Application Workflow:-

<img width="566" alt="workflow" src="https://user-images.githubusercontent.com/57429405/104866134-ca641100-590b-11eb-9965-e9b53777eaeb.PNG">

#### Objective:-

Who - Moody Analytics who have a large business user base provide secure API’s as per applications domain and functionality.
 
What - Perform Data ingestion, Design Fast API, enable API key authentication and test the API implementation 

Why - To illustrate the value of  Data as a Service to generate API’s and ease user experience by providing API as per business requirements.

When - Over a 1 week period timeline.
 
Where - This project will help business, leader's make better and faster decisions by making available API's as per their application's requirement. Providing interactive API will help enhance customer experience.
 
How - Used AWS services like S3 bucket, Lambda function, DynamoDB, API Gateway. Also used Postman, FastAPI (Swagger UI) and Diagrams to display the workflow.

### Task 2 :- Data Ingestion

Performed Data Ingestion from S3 bucket(Staging) to DynamoDB using Lambda function.

#### Proposed Approach :

![new1](https://user-images.githubusercontent.com/57429405/104783666-8d095300-5754-11eb-8cc8-cad96b8bdd31.jpg)

#### Our Implementation :

![Implemetation](https://user-images.githubusercontent.com/57429405/104783718-a8745e00-5754-11eb-90eb-36f2e3c308ce.jpg)


### Task 3 : Design the Fast API

##### Approaches:-

1. Integration of FastAPI with Lambda using Mangum 
2. Using lambda with API gateways - (Get, Post API)

<img width="600" alt="fastapi" src="https://user-images.githubusercontent.com/57429405/104866496-b5d44880-590c-11eb-80c8-9d8765fd7794.PNG">

### Task 4 : Enabling API key authentication

##### API key validation by:

Checking for a query parameter containing the API key

Checking for a header containing the API key

Checking for a cookie containing the API key

<img width="356" alt="securepage" src="https://user-images.githubusercontent.com/57429405/104866469-a3f2a580-590c-11eb-89df-f11f3be8ecf4.PNG">

<img width="600" alt="fastapi" src="https://user-images.githubusercontent.com/57429405/104866429-90473f00-590c-11eb-9fe6-a3fd82df1964.PNG">



