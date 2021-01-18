# CSYE7245---Team-4---Big-Data-Sys-Int-Analytics-Master

## Final Project - Customer Interaction Sentiment Analysis 

#### Team 4 : 

| NAME              |     NUID        |
|------------------ |-----------------|
| Samarth Hadawale  |   001053811     |
| Shivendra Shahi   |   001393331     |
| Siddhi Prabhu     |   001342165     |


### AWS Deployment Link:
Link: http://3.93.151.226:8000/

Login Credentials to try our website:
Username: admin
Password: Pass@1234

1. Google Docs Link : https://docs.google.com/document/d/1V85ECK5Z20Oa4dCATP8U7lRnX1kA3P4unen8w8Tfuww/edit?usp=sharing

2. CLAT Document Link : https://codelabs-preview.appspot.com/?file_id=1V85ECK5Z20Oa4dCATP8U7lRnX1kA3P4unen8w8Tfuww#2

3. Demo Video Recording : https://drive.google.com/file/d/1j-gu9BEmxG2PMGpABEYVJsVUbtK3qs4j/view?usp=sharing

### Install instructions
Create an Amazon Web Services (AWS) account
If you already have an account, skip this step.

Go to this link and follow the instructions. You will need a valid debit or credit card. You will not be charged, it is only to validate your ID.

Install AWS Command Line Interface (AWSCLI)
Install the AWS CLI Version 1 for your operating system. Please follow the appropriate link below based on your operating system.

* [macOS](https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html)

* [Windows](https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html#install-msi-on-windows)

** Please make sure you add the AWS CLI version 1 executable to your command line Path. Verify that AWS CLI is installed correctly by running aws --version.

You should see something similar to aws-cli/1.17.0 Python/3.7.4 Darwin/18.7.0 botocore/1.14.0.
Configuring the AWS CLI
You need to retrieve AWS credentials that allow your AWS CLI to access AWS resources.

Sign into the AWS console. This simply requires that you sign in with the email and password you used to create your account. If you already have an AWS account, be sure to log in as the root user.
Choose your account name in the navigation bar at the top right, and then choose My Security Credentials.
Expand the Access keys (access key ID and secret access key) section.
Press Create New Access Key.
Press Download Key File to download a CSV file that contains your new AccessKeyId and SecretKey. Keep this file somewhere where you can find it easily.
Now, you can configure your AWS CLI with the credentials you just created and downloaded.

In your Terminal, run aws configure.

i. Enter your AWS Access Key ID from the file you downloaded.
ii. Enter the AWS Secret Access Key from the file.
iii. For Default region name, enter us-east-1.
iv. For Default output format, enter json.

Run aws s3 ls in your Terminal. If your AWS CLI is configured correctly, you should see nothing (because you do not have any existing AWS S3 buckets) or if you have created AWS S3 buckets before, they will be listed in your Terminal window.

** If you get an error, then please try to configure your AWS CLI again.

### Available Scripts

Download the available project folder

Install the following packages 

#### `pip install fastapi[all]`

#### `pip install boto3`

#### `pip install requests`

#### `pip install datetime`

#### `pip install botocore`

#### `pip install mangum`

#### `pip install fastapi_cloudauth`

#### `pip install nltk`

#### `pip install rake_nltk`

Run the application locally using following command

#### `uvicorn main:app --reload`

Go to http://127.0.0.1:8000 to view the application locally

### About Sentiment Analysis

Sentiment analysis (also known as opinion mining or emotion AI) refers to the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify the information.

Our Customer Sentiment analysis system is based upon the call recordings between customers and employee of the company with just one aim in mind 'Improving the Customer Service'.

Our Sentiment Analysis Data pipeline leverages various AWS services such as AWS Transcribe, AWS Comprehend, AWS Connect, AWS Polly, AWS Quicksight etc. to perform operations such as Transcription(Speech-To-Text), Anonymization, Text to Speech conversion, Analytical visualizations and Customer Sentiment Analysis.

![mainimage](https://user-images.githubusercontent.com/55570382/101235332-eda56a80-3695-11eb-98ed-588f2c07dfa7.jpg)

### Objectives

Who - Helps customer centric companies to conduct market research, monitor brand and product reputation, and understand customer experiences. Analyzing the sentiment can be used by companies in various sectors to classify the sentence sentiment as positive, negative or neutral to improve their customer service

What - Performed Real-time customer call recording using AWS Connect service and AWS Kinesis, Leverage AWS Comprehend service analyze Customer Sentiment, Anonymize customer data, convert Text to Speech on the anonymized data to maintain user confidentiality, gain detailed insights by leveraging AWS QuickSight and Tableau. 

Why - Assist the Admin User to gain real-time sentiment of the customer's call recording to improve customer service, visualize the sentiment based on age, sex, employees etc., convert Text-To-Speech on anonymized to main user confidentiality.

When - Over Two week period timeline

Where - This project will be delivered to companies requiring to analyze the sentiment of their customers on the basis of the employee-customer call recordings and develop better marketing strategies, improve customer satisfaction, to analyze best performing employee and give feedback accordingly to the respective employees

How - Implemented AWS cloud services, FastAPI, HTML/CSS/Bootstrap

### Implementation Architecture

![WhatsApp Image 2020-12-18 at 12 01 23](https://user-images.githubusercontent.com/55570382/102640674-d8feb300-4128-11eb-9d24-38131cd69f2a.jpeg)

### Real-Time Sentiment Analysis Architecture

![WhatsApp Image 2020-12-18 at 02 36 04](https://user-images.githubusercontent.com/55570382/102640706-e9af2900-4128-11eb-8509-8ef77db03a83.jpeg)

### Use Cases

![WhatsApp Image 2020-12-18 at 12 00 32](https://user-images.githubusercontent.com/55570382/102640745-f59aeb00-4128-11eb-8fac-ebd0a6238b4c.jpeg)

### Dataset
We will be working on audio files to convert them to text files in order to perform sentiment analysis, visualization(Statistics), masking and convert it back from text to speech by maintaining user confidentiality so that admin users can access them as per requirements.

Dataset Links :-

1. https://media.talkbank.org/ca/CallHome/eng/

2. https://www.cmswire.com/digital-asset-management/9-voice-datasets-you-should-know-about/

3. https://research.google.com/audioset/

4. https://commonvoice.mozilla.org/en/datasets

### 1. Login Page

Go to Deployment Link -> Enter valid username and password.

<img width="847" alt="login" src="https://user-images.githubusercontent.com/55570382/102641985-faf93500-412a-11eb-8988-da9a9d798dad.PNG">

### 2. Historical Recording Analysis

<img width="957" alt="hist1" src="https://user-images.githubusercontent.com/55570382/102642025-0c424180-412b-11eb-84fd-610ed4a99ef3.PNG">

<img width="916" alt="hist2" src="https://user-images.githubusercontent.com/55570382/102642063-195f3080-412b-11eb-8b26-c4f7a50a33c2.PNG">

Step 1:- Select file from dropdown to Transcribe 

Step 2:- Click on "View Most Recently Transcribed file" to view recently trascribed file

Step 3:- Enter File name from Step2 to Masking Most Recently Transcribed file

Step 4:- Click on "View Masked Data" to View Most Recently Masked File Output

Step 5:- Enter file name from Step4 to Analyze Sentiment of Most Recently Masked File

Step 6:- Enter file name from Step5 to Converting Text to Audio of Most Recent Masked File

Step 7:- Click on "Download button" to download Most Recent Text-To-Audio Recording


### 3. FeedBack Form

<img width="689" alt="feedback" src="https://user-images.githubusercontent.com/57429405/104776526-39910800-5748-11eb-9447-e35e48be4c59.PNG">

Step 1:- Go to Feedback tab 

Step 2:- Enter Employee Name, Email, Subject and Message

Step 3:- Click on "Submit" button to Send the email to the employee

### 4. Transcribe: Real-Time Call Recordings Analysis


<img width="943" alt="realtime" src="https://user-images.githubusercontent.com/55570382/102642447-aefac000-412b-11eb-9167-7d06849d1810.PNG">

Step 1:- Please Click this link "https://d1vpe7uy6jo5tc.awsapps.com/connect/home" to login to Amazon Connect to access the AWS Connect Service 

Username:- SamArt

Password:- Siddh!@1995

Step 2:- Step 2: Please Click this link "https://d1z6rsdmogxasa.cloudfront.net/" to access Web UI(employee) to accept calls from customer 

Step 3:- Call on +1 929-357-9378 number(as a Customer) and then attend it using AWS Connect web page(as an Employee of a Company)

Step 4:- Click on "View" button to View Masked file of the Recent Real-Time Call

Step 5:- Click on "Analyze" button to Analyze Sentiment of the Recent Real-Time Call

Step 6:- Click on "Download" Button to download call Recording of the Recent Real-Time Call(Optional)

### 5. Analytics

#### Tableau Dashboard:

<img width="712" alt="Dashboard 1" src="https://user-images.githubusercontent.com/57429405/104777027-0602ad80-5749-11eb-8ba3-2b52ccb512b5.png">

#### QuickSight Dashboard:

<img width="1203" alt="Quicksight" src="https://user-images.githubusercontent.com/55570382/102640005-d9e31500-4127-11eb-8cca-5926b80f4fe0.png">


Our Analysis analyzes the call recordings between employees and customers and evaluates tone, intent & emotions behind each call.

We are performing Sentiment analysis by categorizing the customers into four different segments such as Positive, Negative, Neutral and Mixed sentiments.

Our Dataset comprised of 500+ call recordings between customer and employee from which 34% of the calls had Positive , 27% had Negative, 32% had Neutral and 7% had Mixed sentiments.

Employee 6 and Employee 10 are the highest performing employees with each of them attending 69 calls approximately. Employee 10 is top performer with the highest amount of positive sentiment calls(28).

Out of 4 different categories Positive sentiment is the category with highest count(95) among Male whereas neutral sentiment is the category with highest count(75) among Female.

1. Please click on the link to view Quick Sight visualizations

2. View Tableau Dashboard visualization
