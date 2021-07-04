# Realtime-time Stream Processing using Kinesis

 
AWS Lambda and Amazon Kinesis can be used to process real-time streaming data for 
application activity tracking, transaction order processing, click stream analysis, data cleansing, 
metrics generation, log filtering, indexing, social media analysis, and IoT device data telemetry 
and metering.

<img width="422" alt="twitter" src="https://user-images.githubusercontent.com/57429405/124401289-8072ba00-dcf6-11eb-90d6-701728128079.PNG">

Twitter API is used to fetch realtime tweet data from twitter using Python FastAPI(boto3 library) code.

Boto3 library connects to AWS kinesis and writes data into it to process tweets in batch of 25 items to Lambda function

Triggered Lambda function stores the data in No SQL DynamoDB 


<img width="468" alt="TweetsDynamoDB" src="https://user-images.githubusercontent.com/57429405/124401292-89638b80-dcf6-11eb-8d65-a2f3b58e42c5.PNG">


## Create a Kinesis Stream

  • Create a DynamoDB table named <stackname>-EventData

  • Create Lambda Function 1 (<stackname>-DDBEventProcessor) which receives records 
from Kinesis and writes records to the DynamoDB table

  • Create an IAM Role and Policy to allow the event processing Lambda function read from 
the Kinesis Stream and write to the DynamoDB table

  • Create an IAM user with permission to put events in the Kinesis stream together with 
credentials for the user to use in an API clien
