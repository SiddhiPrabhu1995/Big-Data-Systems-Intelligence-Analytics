# AWS Cloud Architecture with Secure RestAPIs

## Summary:

Developed a solution leveraging AWS services to provide a robust set of APIs that enable users to interact with their economic and credit solutions.
Our solution provides `Data As a Service` by extracting, staging, processing and making data available as API's in a secure form only to authenticated users.

## Objective:

Who -  A company having a large business user base provides secure API’s as per applications domain and functionality.
 
What - Perform Data ingestion, transformation, processing, design Fast API's, enable API key authentication for data security and test the API implementation. 

Why - To illustrate the value of  `Data as a Service` to generate API’s and ease user experience by providing API as per business requirements.

When - Over a 3 weeks period timeline.
 
Where - This project will help business, leader's make better and faster decisions by making available API's as per their application's requirement. Providing interactive API will help enhance customer experience.
 
How - Used AWS services like AWS Comprehend, Cognito, S3 bucket, Lambda function, DynamoDB, API Gateway, fastapicloudauth  library, Boto3 library. Also used Postman, FastAPI (Swagger UI) and Diagrams to display the workflow.


## PART 1: DATA INGESTION, TRANSFORMATION, PROCESSING, DESIGN FASTAPI & ENABLE SECURE API KEY AUTHENTICATION

1. Google Docs Link Part 1: https://docs.google.com/document/d/1YLTFKUzdbuxrQO2cLU5RBFUIdrHWENIF0l27dtXGxLo/edit?usp=sharing

2. CLAT Document Link Part 1: https://codelabs-preview.appspot.com/?file_id=1YLTFKUzdbuxrQO2cLU5RBFUIdrHWENIF0l27dtXGxLo#0

### Application WorkfloW:-

<img width="566" alt="workflow" src="https://user-images.githubusercontent.com/57429405/104866134-ca641100-590b-11eb-9965-e9b53777eaeb.PNG">

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


## PART 2: Securing AWS API Gateway using AWS Cognito OAuth2 scopes


1. Google Docs Link Part 2 : https://docs.google.com/document/d/1CWMKdIsNJjLZv0qcbD8HJlER8kayqXF3_h_Z8590HRo/edit?ts=5f9c7773#heading=h.ui9fgw2vh8q

2. CLAT Document Link Part 2 : https://codelabs-preview.appspot.com/?file_id=1CWMKdIsNJjLZv0qcbD8HJlER8kayqXF3_h_Z8590HRo#5


<img width="519" alt="archtworkflow" src="https://user-images.githubusercontent.com/57429405/104873283-2f286700-591e-11eb-826e-4059c9d633dc.PNG">


### 1. ADD SECURE USER POOL IN AWS COGNITO

<img width="193" alt="userpool" src="https://user-images.githubusercontent.com/57429405/104872919-2edb9c00-591d-11eb-8db5-2eeaf177d12f.PNG">

Steps:-

1. Creating userpool -> Create User -> Confirming the user in user pool

2. Install fastapi cloudauth library -> `pip install fastapi-cloudauth`

3. Configure authadd.py fastapi file -> execute the fastapi file in command prompt `uvicorn authadd:app --reload --port 8000`

4. Go to http://127.0.0.1:8000 to view the fastapi in swagger ui locally

5. Authorize the API to access the API's

6. Click on 'Authorize' button -> Enter Token ID -> Click on 'Authorize' 

7. Only authorized users can access the API's

### 2. Save the tokens tied to the user-API into dynamodb

1. Writing a lambda function to manually insert generated tokens into DynamoDB

2. Storing the Tokens into DynamoDB Table

### 3. Create an API that will validate whether the token is valid or not

<img width="672" alt="refarch" src="https://user-images.githubusercontent.com/57429405/104873067-a27da900-591d-11eb-9d77-305e91030e9d.PNG">

1. Create user pool in AWS Cognito

2. Adding an Authorizer at the API Gateway level & tying the Recently created Cognito User pool to that Authorizer

3. Authorization details of API Gateway

4. Secured GET & POST methods of our API Gateway

5. Trying to access the data without an Access token so we are getting ‘Unauthorized' Error

6. Accessing the data from DynamoDB by passing the access token as an Authorization token

### 4. Anonymization of sensitive data

<img width="316" alt="sensitive" src="https://user-images.githubusercontent.com/57429405/104873124-c6d98580-591d-11eb-9999-29298ecc0051.PNG">

Install the following packages:-

##### `pip install boto3 --target python/.`

##### `pip install botocore --target python/.`

Following are the components of the architecture:-

1. Lambda function to identify the protected information

2. Lambda function to mask entities

3. Lambda function to De-identify entities

4. Building state machine to trigger the lambda function flow

