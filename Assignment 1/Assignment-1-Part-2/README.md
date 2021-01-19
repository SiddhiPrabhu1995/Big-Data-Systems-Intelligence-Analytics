# CSYE7245---Team-4---Big-Data-Sys-Int-Analytics-Master

## Assignment 1 Part 2 :- Data as a Service 

| NAME              |     NUID        |
|------------------ |-----------------|
| Samarth Hadawale  |   001053811     |
| Shivendra Shahi   |   001393331     |
| Siddhi Prabhu     |   001342165     |


1. Google Docs Link : https://docs.google.com/document/d/1CWMKdIsNJjLZv0qcbD8HJlER8kayqXF3_h_Z8590HRo/edit?ts=5f9c7773#heading=h.ui9fgw2vh8q

2. CLAT Document Link : https://codelabs-preview.appspot.com/?file_id=1CWMKdIsNJjLZv0qcbD8HJlER8kayqXF3_h_Z8590HRo#0

## About Data as a Service

Data as a service (DaaS) is a data management strategy that uses the cloud to deliver data storage, integration, processing, and/or analytics services via a network connection.

### Architectural Workflow : Securing AWS API Gateway using AWS Cognito OAuth2 scopes

<img width="519" alt="archtworkflow" src="https://user-images.githubusercontent.com/57429405/104873283-2f286700-591e-11eb-826e-4059c9d633dc.PNG">

### Implementation : Task 1 : Extend the tutorial to add a new user pool tied to the Fast API you created in Assignment 1- Part 1

<img width="193" alt="userpool" src="https://user-images.githubusercontent.com/57429405/104872919-2edb9c00-591d-11eb-8db5-2eeaf177d12f.PNG">

Steps:-

1. Creating userpool -> Create User -> Confirming the user in user pool

2. Install fastapi cloudauth library -> `pip install fastapi-cloudauth`

3. Configure authadd.py fastapi file -> execute the fastapi file in command prompt `uvicorn authadd:app --reload --port 8000`

4. Go to http://127.0.0.1:8000 to view the fastapi in swagger ui locally

5. Authorize the API to access the API's

6. Click on 'Authorize' button -> Enter Token ID -> Click on 'Authorize' 

7. Only authorized users can access the API's


### Task 2 : Save the tokens tied to the user-API into dynamodb

1. Writing a lambda function to manually insert generated tokens into DynamoDB

2. Storing the Tokens into DynamoDB Table

### Task 3 : Create an API that will validate whether the token is valid or not

References : https://medium.com/@awskarthik82/part-1-securing-aws-api-gateway-using-aws-cognito-oauth2-scopes-410e7fb4a4c0

<img width="672" alt="refarch" src="https://user-images.githubusercontent.com/57429405/104873067-a27da900-591d-11eb-9d77-305e91030e9d.PNG">

1. Create user pool in AWS Cognito

2. Adding an Authorizer at the API Gateway level & tying the Recently created Cognito User pool to that Authorizer

3. Authorization details of API Gateway

4. Secured GET & POST methods of our API Gateway

5. Trying to access the data without an Access token so we are getting ‘Unauthorized' Error

6. Accessing the data from DynamoDB by passing the access token as an Authorization token

### Task 4 : Anonymization of sensitive data

<img width="316" alt="sensitive" src="https://user-images.githubusercontent.com/57429405/104873124-c6d98580-591d-11eb-9999-29298ecc0051.PNG">

Install the following packages:-

##### `pip install boto3 --target python/.`

##### `pip install botocore --target python/.`

