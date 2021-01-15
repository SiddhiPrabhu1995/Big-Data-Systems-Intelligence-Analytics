#Core Packages
from random import randint
from fastapi import Security, Depends, FastAPI
from pydantic import BaseModel, Field   
from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, JSONResponse
import json, boto3, requests, datetime, time, urllib.request, logging, threading, sys, boto
from botocore.vendored import requests
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from mangum import Mangum
from fastapi_cloudauth.cognito import Cognito, CognitoCurrentUser, CognitoClaims
from boto3.dynamodb.conditions import Key
from boto.s3.connection import S3Connection
from starlette.middleware.cors import CORSMiddleware
import string
from rake_nltk import Rake
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from starlette.routing import Router


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/',response_class=HTMLResponse)
def index(request: Request):
    
	return templates.TemplateResponse('authenticateuser.html', {"request": request})


@app.get('/logout',response_class=HTMLResponse)
def index(request: Request):
    
	return templates.TemplateResponse('authenticateuser.html', {"request": request})

@app.get('/authuser',response_class=HTMLResponse)
def index(request: Request):
    
	return templates.TemplateResponse('authuser.html', {"request": request})

@app.get("/authenticate", response_class=HTMLResponse)

def authenticatepage(request: Request, user: str, password: str):    
    OTP = user+password
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    response = table.get_item(Key = {'OTP': OTP})
    
    fullstring = str(response)
  
    substring = OTP
    verified = False
    
    if substring in fullstring:
        verified = True
        return templates.TemplateResponse('authuser.html', {"request": request})
    else:
        verified = False
        result = "Please enter valid username/password!!"
        return templates.TemplateResponse('viewrealsenti.html', {"request": request, "data":result})

	
    
    
@app.get("/reatimeanalysis", response_class=HTMLResponse)
def reatimeanalysis(request: Request):
	
    return templates.TemplateResponse('reatimeanalysis.html', {"request": request})

@app.get("/historicalrecordings", response_class=HTMLResponse)
def historicalrecordings(request: Request):
	
    return templates.TemplateResponse('historicalrecordings.html', {"request": request})

@app.get("/form", response_class=HTMLResponse)
def form(request: Request):
	
    return templates.TemplateResponse('form.html', {"request": request})

@app.get("/analytics", response_class=HTMLResponse)
def reatimeanalysis(request: Request):
	
    return templates.TemplateResponse('analytics.html', {"request": request})

################Transcribe, Mask & Analyze Sentiment on a click################
@app.get("/getfilenames", tags=["Transcribe"])
def getaudiofilename():

        s3 = boto3.resource('s3')
        my_bucket = s3.Bucket('callrecordingsproject')
        fileList = []
        for my_bucket_object in my_bucket.objects.all():
            fileList.append(my_bucket_object)
        fileList = str(fileList)
        fileList = fileList.replace("key=","")
        fileList = fileList.replace("s3.ObjectSummary", "")
        fileList = fileList.replace("(","")
        fileList = fileList.replace("bucket_name","")
        fileList = fileList.replace("callrecordingsproject","")
        fileList = fileList.replace(",","")
        fileList = fileList.replace("=","")
        fileList = fileList.replace("[","")
        fileList = fileList.replace("]","")
        fileList = fileList.replace(")","")
        fileList = fileList.replace("'","")

        return fileList




@app.get("/transcribe", tags=["Transcribe"])
def transcribefunction(request: Request, filename:str):

    client = boto3.client(service_name='transcribe')
            
    response = client.start_transcription_job(

    TranscriptionJobName='Transcribe'+str(randint(0,100000)),
    LanguageCode='en-US',
    #MediaFormat='wav',
    Settings={
        #'VocabularyName': 'string',
        #'ShowSpeakerLabels': True,
        #'MaxSpeakerLabels': 9,
        'ChannelIdentification': True,
        #'ShowAlternatives': True,
        #'MaxAlternatives': 9,
        #'VocabularyFilterName': 'string',
        #'VocabularyFilterMethod': 'remove'|'mask'
    },
    Media={
        'MediaFileUri': 's3://callrecordingsproject/'+filename
    },
    OutputBucketName='audiotextoutput',
    OutputKey=str(randint(0,100))+'.txt',

        )

           
    result = filename + "Transcribe Job in Progress!!"
   
    return templates.TemplateResponse('viewrealsenti.html', {"request": request, "data":result})

@app.get("/gettextfilename", tags=["Anonymize Sensitive Data"])
def gettextfilename():

        s3 = boto3.resource('s3')
        my_bucket = s3.Bucket('audiotextoutput')
        fileList = []
        for my_bucket_object in my_bucket.objects.all():
            fileList.append(my_bucket_object)
        fileList = str(fileList)
        fileList = fileList.replace("key=","")
        fileList = fileList.replace("s3.ObjectSummary", "")
        fileList = fileList.replace("(","")
        fileList = fileList.replace("bucket_name","")
        fileList = fileList.replace("audiotextoutput","")
        fileList = fileList.replace(",","")
        fileList = fileList.replace("=","")
        fileList = fileList.replace("[","")
        fileList = fileList.replace("]","")
        fileList = fileList.replace(")","")
        fileList = fileList.replace("'","")
        fileList = fileList.replace(".write_access_check_file.temp  ","")

        return fileList

#View transcribed file
@app.get("/viewtranscribe", tags=["Transcribe"])
def viewtranscriberesult(request: Request):

        s3_client = boto3.client('s3')
        response = s3_client.list_objects_v2(Bucket='audiotextoutput')
        all = response['Contents']        
        latest = max(all, key=lambda x: x['LastModified'])

        s3_bucket = boto3.client("s3")
        bucket = "audiotextoutput"
        key = latest['Key']
        
        file = s3_bucket.get_object(Bucket=bucket, Key=key)
        paragraph = (file['Body'].read())
        paragraph = json.loads(paragraph.decode('utf-8'))
        
        para = paragraph['results']['transcripts'][0]['transcript']
        return templates.TemplateResponse('viewtransoutput.html', {"request": request, "data":para, "filename":key})


#Trigger Step function to Anonymize Data
@app.get("/TriggerStepFunction", tags=["Anonymize Sensitive Data"])
async def triggerStepFunctions(filename: str): 
        
    
            #Step function logic starts from here
            STATE_MACHINE_ARN = 'arn:aws:states:us-east-1:231038452309:stateMachine:MyStateMachinenew'
    
            #The name of the execution
            EXECUTION_NAME = 'Anonymize'+str(randint(0,1000000))+filename

            
            s3 = boto3.client("s3", region_name='us-east-1')
            bucket = "audiotextoutput"
            key = filename
            
            file = s3.get_object(Bucket=bucket, Key=key)
            paragraph = (file['Body'].read())
           
            paragraph = json.loads(paragraph.decode('utf-8'))

            makeDict = paragraph['results']['transcripts'][0]['transcript']

            inputJSON = {    "message": makeDict[:20000] }  
            
            INPUT = json.dumps(inputJSON)
            sfn = boto3.client('stepfunctions')
            
            response = sfn.start_execution(
                stateMachineArn=STATE_MACHINE_ARN,
                name=EXECUTION_NAME,
                input=INPUT
            )

            executionARN = response.get('executionArn')
        
            time.sleep(1)
        
            time.sleep(5)
        
            time.sleep(4)

            response = sfn.get_execution_history(
                executionArn= executionARN,
                maxResults=1,
                reverseOrder=True
            )
            
            name = 'Masking Completed Successfully:  '+filename
            return name

#View masked output
@app.get("/viewmaskedoutput", tags=["Transcribe"])
def viewmaskedoutput(request: Request):

        s3_client = boto3.client('s3')
        response = s3_client.list_objects_v2(Bucket='hashedaudiotext')
        all = response['Contents']        
        latest = max(all, key=lambda x: x['LastModified'])

        s3_bucket = boto3.client("s3")
        bucket = "hashedaudiotext"
        key = latest['Key']
        
        file = s3_bucket.get_object(Bucket=bucket, Key=key)
        paragraph = str(file['Body'].read())

        return templates.TemplateResponse('viewtransoutput.html', {"request": request, "data":paragraph, "filename":key})


#Amazon Polly
@app.get("/getaudiofilename", tags=["Text to Speech"])
def getaudiofilename():

        s3 = boto3.resource('s3')
        my_bucket = s3.Bucket('hashedaudiotext')
        fileList = []
        for my_bucket_object in my_bucket.objects.all():
            fileList.append(my_bucket_object)
        fileList = str(fileList)
        fileList = fileList.replace("key=","")
        fileList = fileList.replace("s3.ObjectSummary", "")
        fileList = fileList.replace("(","")
        fileList = fileList.replace("bucket_name","")
        fileList = fileList.replace("hashedaudiotext","")
        fileList = fileList.replace(",","")
        fileList = fileList.replace("=","")
        fileList = fileList.replace("[","")
        fileList = fileList.replace("]","")
        fileList = fileList.replace(")","")
        fileList = fileList.replace("'","")
        

        return fileList



@app.get("/TextToSpeech", tags=["Text to Speech"])
def texttospeech(filename: str,request: Request):

    s3 = boto3.client("s3")
    bucket = "hashedaudiotext"
    key = filename
    
    file = s3.get_object(Bucket=bucket, Key=key)
    paragraph = str(file['Body'].read())

    client = boto3.client(service_name='polly')
            
    response = client.start_speech_synthesis_task(
    Engine='standard',
    LanguageCode='en-US',
    OutputFormat='mp3',
    OutputS3BucketName='pollytexttoaudio',

    Text=paragraph,

    VoiceId='Emma'
    )
            
    result = "Successfully Converted File from Text to Audio!!"
    return templates.TemplateResponse('viewrealsenti.html', {"request": request, "data":result})

#Download audio file
@app.get("/callrecord", tags=["REALTIME"])
def downloadrecord(request: Request):
    
        s3_client = boto3.client('s3')
        response = s3_client.list_objects_v2(Bucket='pollytexttoaudio')
        all = response['Contents']        
        latest = max(all, key=lambda x: x['LastModified'])

        s3 = boto3.client("s3")

        BUCKET_NAME = 'pollytexttoaudio' 
        KEY = latest['Key'] 
        
        s3 = boto3.resource('s3')

        s3.Bucket(BUCKET_NAME).download_file(KEY,KEY)
       
        paragraph = "Successfully Downloaded Masked Call Recording!!"
        return templates.TemplateResponse('viewrealsenti.html', {"request": request, "data":paragraph})

# Sentiment Analysis

@app.get("/getfilesentiname", tags=["Sentiment Analysis"])
def getfilename():

        s3 = boto3.resource('s3')
        my_bucket = s3.Bucket('hashedaudiotext')
        fileList = []
        for my_bucket_object in my_bucket.objects.all():
            fileList.append(my_bucket_object)
        fileList = str(fileList)
        fileList = fileList.replace("key=","")
        fileList = fileList.replace("s3.ObjectSummary", "")
        fileList = fileList.replace("(","")
        fileList = fileList.replace("bucket_name","")
        fileList = fileList.replace("hashedaudiotext","")
        fileList = fileList.replace(",","")
        fileList = fileList.replace("=","")
        fileList = fileList.replace("[","")
        fileList = fileList.replace("]","")
        fileList = fileList.replace(")","")
        fileList = fileList.replace("'","")
        fileList = fileList.replace(".write_access_check_file.temp  ","")

        return fileList

class SentimentResponse(BaseModel):
    sentiment: str
    sentiscore: dict

@app.post("/sentimentanalysis", tags=["Sentiment Analysis"])
def senitmentanalysis(filename: str):

    s3 = boto3.client("s3")
    bucket = "hashedaudiotext"
    key = filename
    
    file = s3.get_object(Bucket=bucket, Key=key)
    paragraph = str(file['Body'].read())



    comp = boto3.client('comprehend')

  
    #Sentiment Analysis
    sentiment = comp.detect_sentiment(Text = paragraph[:5000], LanguageCode = 'en') #API call for sentiment analysis
    sentRes = sentiment['Sentiment'] #Positive, Neutral, or Negative
    sentScore = sentiment['SentimentScore'] #Percentage of Positive, Neutral, and Negative

    return SentimentResponse(
        sentiment=sentRes, sentiscore=sentScore
    )

#Rake sentiment analysis
@app.post("/sentiment", tags=["Sentiment Analysis"])
def senitmentrake(filename: str, request: Request):

    s3 = boto3.client("s3")
    bucket = "hashedaudiotext"
    key = filename
    
    file = s3.get_object(Bucket=bucket, Key=key)
    paragraph = str(file['Body'].read())

    title_importance = 1
    language_importance = 1
    series_importance = 1
    authors_importance = 1
    genres_importance = 1

    soup = ''
    
    # Keywords from description.
    desc = paragraph
    if desc != "":
        rake = Rake()
        rake.extract_keywords_from_text(desc)
        desc_soup = ' '.join(list(rake.get_word_degrees().keys()))
        soup = ' '.join(filter(None, [soup, desc_soup]))


    comp = boto3.client('comprehend')

    #Sentiment Analysis
    sentiment = comp.detect_sentiment(Text = soup[:5000], LanguageCode = 'en') #API call for sentiment analysis
    sentRes = sentiment['Sentiment'] #Positive, Neutral, or Negative
    sentScore = sentiment['SentimentScore'] #Percentage of Positive, Neutral, and Negative
    
    return templates.TemplateResponse('sentianalyze.html', {"request": request, "data":sentiment})


#REAL TIME TRIGGER STEP FUNCTIONS
@app.get("/TrigStepFuncRealTime", tags=["REALTIME"])
async def triggerStepFunctions(): 
        
    
            #Step function logic starts from here
            STATE_MACHINE_ARN = 'arn:aws:states:us-east-1:231038452309:stateMachine:MyStateMachinenew'
    
            #The name of the execution
            EXECUTION_NAME = str(randint(0,100))+'AnonymizeAudioText'

            
            s3 = boto3.client("s3")
            bucket = "audiotextoutput"
            key = filename
            
            file = s3.get_object(Bucket=bucket, Key=key)
            paragraph = (file['Body'].read())
           
            paragraph = json.loads(paragraph.decode('utf-8'))

            makeDict = paragraph['results']['transcripts'][0]['transcript']

            inputJSON = {    "message": makeDict[:20000] }  
            
            INPUT = json.dumps(inputJSON)
            sfn = boto3.client('stepfunctions')
            
            response = sfn.start_execution(
                stateMachineArn=STATE_MACHINE_ARN,
                name=EXECUTION_NAME,
                input=INPUT
            )

            executionARN = response.get('executionArn')
        
            time.sleep(1)
        
            time.sleep(5)
        
            time.sleep(4)

            response = sfn.get_execution_history(
                executionArn= executionARN,
                maxResults=1,
                reverseOrder=True
            )
            
            return 'Triggered Step function'

##REALTIME
##View sentiment
@app.get("/viewsrealsentiment", tags=["REALTIME"])
def viewsrealsentiment(request: Request):

        s3_client = boto3.client('s3')
        response = s3_client.list_objects_v2(Bucket='realtimesentiment')
        all = response['Contents']        
        latest = max(all, key=lambda x: x['LastModified'])

        s3_bucket = boto3.client("s3")
        bucket = "realtimesentiment"
        key = latest['Key']
        print(key)
        file = s3_bucket.get_object(Bucket=bucket, Key=key)
        paragraph = str(file['Body'].read())
        
        #return JSONResponse(content=paragraph)
        # return paragraph
        return templates.TemplateResponse('viewrealsenti.html', {"request": request, "data":paragraph})


@app.get("/maskresult", tags=["REALTIME"])
def viewmaskresult(request: Request):

        s3_client = boto3.client('s3')
        response = s3_client.list_objects_v2(Bucket='hashedaudiotextrealtime')
        all = response['Contents']        
        latest = max(all, key=lambda x: x['LastModified'])

        s3_bucket = boto3.client("s3")
        bucket = "hashedaudiotextrealtime"
        key = latest['Key']
        #print(key)
        file = s3_bucket.get_object(Bucket=bucket, Key=key)
        paragraph = str(file['Body'].read())

        return templates.TemplateResponse('viewrealsenti.html', {"request": request, "data":paragraph})

@app.get("/realcallrecord", tags=["REALTIME"])
def downloadrecord(request: Request):
    
        s3_client = boto3.client('s3')
        response = s3_client.list_objects_v2(Bucket='amazonpollyrealtime')
        all = response['Contents']        
        latest = max(all, key=lambda x: x['LastModified'])

        s3 = boto3.client("s3")

        BUCKET_NAME = 'amazonpollyrealtime' 
        KEY = latest['Key'] 
        
        s3 = boto3.resource('s3')

        s3.Bucket(BUCKET_NAME).download_file(KEY,KEY)
       
        paragraph = "Successfully Downloaded Masked Call Recording!!"
        return templates.TemplateResponse('viewrealsenti.html', {"request": request, "data":paragraph})