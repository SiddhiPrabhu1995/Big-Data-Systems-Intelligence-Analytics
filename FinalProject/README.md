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


### Dashboard Links:
Tableau:https://public.tableau.com/profile/samarth.hadawale#!/vizhome/BigDataFinal_16082339565680/Dashboard1

QuickSight Dashboard:


### Implementation Architecture


### Real-Time Sentiment Analysis Architecture

### Use Cases

### Dataset
We will be working on audio files to convert them to text files in order to perform sentiment analysis, visualization(Statistics), masking and convert it back from text to speech by maintaining user confidentiality so that admin users can access them as per requirements.

Dataset Links :-
https://media.talkbank.org/ca/CallHome/eng/
https://www.cmswire.com/digital-asset-management/9-voice-datasets-you-should-know-about/
https://research.google.com/audioset/
https://commonvoice.mozilla.org/en/datasets



### 1. Historical Recording Analysis

Step 1:- Select file from dropdown to Transcribe
Step 2:- Click on "View Most Recently Transcribed file" to view trascribed file
Step 3:- Enter File name from Step2 to Masking Most Recently Transcribed file
Step 4:- Click on "View Masked Data" to View Most Recently Masked File Output
Step 5:- Enter file name from Step4 to Analyze Sentiment of Most Recently Masked File
Step 6:- Enter file name from Step5 to Converting Text to Audio of Most Recent Masked File
Step 7:- Click on "Download button" to download Most Recent Text-To-Audio Recording

### 2. FeedBack Form

Step 1:- Go to Feedback tab 
Step 2:- Enter Employee Name, Email, Subject and Message
Step 3:- Click on "Submit" button to Send the email to the employee

### 3. Transcribe: Real-Time Call Recordings Analysis

Step 1:- Please Click this link "https://d1vpe7uy6jo5tc.awsapps.com/connect/home" to login to Amazon Connect to access the AWS Connect Service 
Username:- SamArt
Password:- Siddh!@1995

Step 2:- Step 2: Please Click this link "https://d1z6rsdmogxasa.cloudfront.net/" to access Web UI to accept calls from customer as an Employee

Step 3:- Call on +1 929-357-9378 number(as a Customer) and then attend it using AWS Connect web page(as an Employee of a Company)

Step 4:- Click on "View" button to View Masked file of the Recent Real-Time Call

Step 5:- Click on "Analyze" button to Analyze Sentiment of the Recent Real-Time Call

Step 6:- Click on "Download" Button to download call Recording of the Recent Real-Time Call(Optional)

