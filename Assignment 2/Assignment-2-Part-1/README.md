# CSYE7245---Team-4---Big-Data-Sys-Int-Analytics-Master

#### Team 4 : Part 1 : ML as a service

| NAME              |     NUID        |
|------------------ |-----------------|
| Samarth Hadawale  |   001053811     |
| Shivendra Shahi   |   001393331     |
| Siddhi Prabhu     |   001342165     |


Assignment 2 Part 1 :

1. Google Docs Link : https://docs.google.com/document/d/1xyNo4C4K2ylmPlk3ZPoeFgyWVN0DnnUSaAmMDiDSEK0/edit#

2. CLAT Document Link : https://codelabs-preview.appspot.com/?file_id=1xyNo4C4K2ylmPlk3ZPoeFgyWVN0DnnUSaAmMDiDSEK0#3

### About Activity 1

#### Identifying and working with sensitive healthcare data with Amazon Comprehend Medical

Followed the reference architecture : https://aws.amazon.com/blogs/machine-learning/identifying-and-working-with-sensitive-healthcare-data-with-amazon-comprehend-medical/

This architecture uses the following services:

Amazon Comprehend Medical to identify entities within a body of text
AWS Step Functions and AWS Lambda to coordinate and execute the workflow
Amazon DynamoDB to store the de-identified mapping 

##### Available Scripts

In the project directory, you can run:

#### `pip install boto3 --target python/.`
Installs boto3 library to integrate with AWS services.

#### `aws stepfunctions start-execution --state-machine-arn YOUR_STATEMACHINE_ARN --input file://example_note.json`
Testing the state machine by executing above command
Go to Step functions-> Execution Output in AWS to view the output
example_note.json contains the message and a choice of whether to anonymize the message or de-identify it.

### About Activity 2

Used Google Colab, Docker and Postman

1. Check Python performance
In the project directory, you can run:

#### `python plot_function.py`
Plots graph of python performance

#### `python regenerative_morph_slow.py`
Profiling on file regenerative_morph_slow.py to get an idea about the detailed runtime of each function.

#### `python regenerative_morph.py`
Compared the runtime of regenerative_morph.py and regenerative_morph_slow.py by executing them separately.

2. Serving a model with Docker

#### `docker build -t ml_deploy_demo:latest `
Building a Docker Image & checking it into Docker Images.

#### `run.sh`
Running the Docker container.

### About Activity 3

#### DataFlow De-identification pipeline - Google Cloud Platform

Followed the reference architecture : https://github.com/GoogleCloudPlatform/dlp-dataflow-deidentification

Performed Data de-identification using Cloud Storage and Dataflow
Configuration and Management using Cloud DLP and Cloud KMS
Passed the de-identified data to Data validation and re-identification structure(BigQuery, Dataflow and Pub/Sub)

In Google Cloud Shell, execute below command after creating project

#### `gcloud config set project project-id`
Executing above command to enable the recently created project
