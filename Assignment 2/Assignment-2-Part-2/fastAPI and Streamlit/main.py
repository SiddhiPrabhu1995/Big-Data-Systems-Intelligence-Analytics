#Core Packages
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field   
from bs4 import BeautifulSoup
from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, JSONResponse
from fastapi import FastAPI
import json
import boto3
import requests,datetime
import time
from random import randint
import urllib.request
import logging
import threading
import sys
import logging
import threading
import sys
from botocore.vendored import requests
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from mangum import Mangum
from fastapi_cloudauth.cognito import Cognito, CognitoCurrentUser, CognitoClaims
from boto3.dynamodb.conditions import Key
verified = "False"

#init app
app = FastAPI(title="Deidentification System",
              description='''API to call from the recommendAPI''',
              version="0.1.0",)

@app.get("/scrap")
# def scrapeData(enterurl: str,verified: str):
def scrapeData(enterurl: str):
    def grab_page(url,url_ending):
        #print("attempting to grab page: " + url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
        'Connection' : 'keep-alive',
        'Content-Length' : '799',
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': '/',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'en-US,en-GB;q=0.9,en;q=0.8,hi;q=0.7,mr;q=0.6'
        }
        page = requests.get(url + "/", headers = headers, timeout=5)
        page_html = page.text
        soup = BeautifulSoup(page_html, 'html.parser')
        meta = soup.find("div",{'class':'a-info get-alerts'})
        content = soup.find(id="a-body")
 
        text = content.text
        
        s3 = boto3.resource('s3')
        s3.Object('inputpii', 'abc' + str(randint(0,100))+'.txt').put(Body=text)

    def process_list_page(k):
        #origin_page = "http://seekingalpha.com/earnings/earnings-call-transcripts" + "/" + str(k)
        origin_page = userurl + "/" + str(k)
        #print("getting page " + origin_page)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}
        page = requests.get(origin_page, headers = headers)
        page_html = page.text
    #print(page_html)
        soup = BeautifulSoup(page_html, 'html.parser')
        alist = soup.find_all("li",{'class':'list-group-item article'})
        for i in range(0,len(alist)):
            url_ending = alist[i].find_all("a")[0].attrs['href']
            url = "http://seekingalpha.com" + url_ending
            #print(url)
            #print(url_ending)
            grab_page(url,url_ending)
            #print(url)
            time.sleep(.5)
            
   # if ver
    for i in range(1,1): #choose what pages of earnings to scrape
        process_list_page(i,enterurl)
    
    return {
        #'statusCode': 200,
        'body': json.dumps('Successful')}

@app.get("/displayscrapdata")
def scrapdatadisplay():

    s3 = boto3.client("s3")
    bucket = "inputpii"
    key = "abcde.txt"
    file = s3.get_object(Bucket=bucket, Key=key)
    paragraph = str(file['Body'].read())
   
    return {
       
        'body': json.dumps(paragraph)
    }

@app.get("/identifyEntity")
def identifyPIIEntity(verified):
    print(verified)
    if(verified == "True"):
        s3 = boto3.client("s3")
        bucket = "inputpii"
        key = "abcde.txt"
        file = s3.get_object(Bucket=bucket, Key=key)
        paragraph = str(file['Body'].read())
  
        comprehend = boto3.client("comprehend")
    
        entities = comprehend.detect_entities(Text=paragraph, LanguageCode = "en")
        keyphrase = comprehend.detect_key_phrases(Text=paragraph, LanguageCode = "en")

        s3 = boto3.resource('s3')
        BUCKET_NAME = "outputpii"

        OUTPUT_NAME = f"dataKeyTest.json"
        OUTPUT_BODY = json.dumps(entities)
        s3.Bucket(BUCKET_NAME).put_object(Key=OUTPUT_NAME, Body=OUTPUT_BODY)

        return {
        
            'body': json.dumps(entities)
        }

    else:
        return{
            'body': json.dumps('Authenticate User')
        }

@app.get("/maskEntity")
def maskIdentifiedEntity():
    client = boto3.client(service_name='comprehend', region_name='us-east-1')
    
    response = client.start_pii_entities_detection_job(

    InputDataConfig={
        'S3Uri': 's3://inputpii/abcde.txt',

        'InputFormat': 'ONE_DOC_PER_LINE'

    },

    OutputDataConfig={

        'S3Uri': 's3://outputpii/MaskOutput/',

    },

    Mode='ONLY_REDACTION',

    RedactionConfig={

        'PiiEntityTypes': [

            'ALL'

        ],

        'MaskMode': 'MASK',

        'MaskCharacter': '*'

    },
   
    DataAccessRoleArn='arn:aws:iam::711797752508:role/service-role/AmazonComprehendServiceRole-newestIAM',

    JobName='comprehend-REDACTnew',

    LanguageCode='en'

    )

        
    return {
 
        'body': json.dumps('Successfully Masked entities!!')
    }

@app.get("/display_mask_entity")
def get_mask_PII_entity():
    s3 = boto3.client("s3")
    bucket = "outputpii"
    key = "abcde.txt.out"
    file = s3.get_object(Bucket=bucket, Key=key)
    paragraph = str(file['Body'].read())
   
    return {
        #'statusCode': 200,
        'body': json.dumps(paragraph)
    }

@app.get("/replacePIIEntity")
def replacewithPIIEntity():
    client = boto3.client(service_name='comprehend', region_name='us-east-1')
    
    response = client.start_pii_entities_detection_job(

    InputDataConfig={
        'S3Uri': 's3://inputpii/abcde.txt',

        'InputFormat': 'ONE_DOC_PER_LINE'

    },

    OutputDataConfig={

        'S3Uri': 's3://outputpii/MaskOutput/',

    },

    Mode='ONLY_REDACTION',

    RedactionConfig={

        'PiiEntityTypes': [

            'ALL'

        ],

        'MaskMode': 'REPLACE_WITH_PII_ENTITY_TYPE'

    },
   
    DataAccessRoleArn='arn:aws:iam::711797752508:role/service-role/AmazonComprehendServiceRole-newestIAM',

    JobName='comprehend-REDACTPIIEntities',

    LanguageCode='en'

    )    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully replaced with PII entities!!')
    }

@app.get("/displayPIIEntity")
def get_mask_PII_entity():
    s3 = boto3.client("s3")
    bucket = "outputpii"
    key = "replacewithPIIEntity.out"
    file = s3.get_object(Bucket=bucket, Key=key)
    paragraph = str(file['Body'].read())
   
    return {
        #'statusCode': 200,
        'body': json.dumps(paragraph)
    }


@app.get("/Authentication", tags=["Auth"])
async def userauthentication(usrName: str, usrPassword: str): 
    OTP = usrName+usrPassword
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    response = table.get_item(Key = {'Login': OTP})

    if response == "" :
        verified = "False"
        response = "Please enter valid username/password!!"
    else:
        verified = "True"
        response = "Congratulations User Verified!!"

    return response

#Deidentification generate HashMessage
@app.get("/Anonymize", tags=["Auth"])
async def deidentifyEntities(): 
    
    dynamodb = boto3.resource('dynamodb')
    dynamodbClient = boto3.client("dynamodb")
    table = dynamodb.Table('DeidentificationLookUpTable')
    Hash = 'c16e783f3dec14e234b1969b07af869de846f99f6a53df1954017b7779915ecb'
    fileName = str('deidentifiedmessage')

    s3 = boto3.client("s3")
    bucket = "outputpii"
    key = fileName + ".txt"
    file = s3.get_object(Bucket=bucket, Key=key)
    paragraph = str(file['Body'].read())
  

    return {
     
        'body': json.dumps(paragraph)
    }


    ##View Deidentified
@app.get("/deanonymize", tags=["Auth"])
async def deidentifyEntities(): 
    
    dynamodb = boto3.resource('dynamodb')
    dynamodbClient = boto3.client("dynamodb")
    table = dynamodb.Table('DeidentificationLookUpTable')
    Hash = 'c16e783f3dec14e234b1969b07af869de846f99f6a53df1954017b7779915ecb'
    fileName = str('deidentifiedmessage')

    s3 = boto3.client("s3")
    bucket = "outputpii"
    key = fileName + ".txt"
    file = s3.get_object(Bucket=bucket, Key=key)
    paragraph = str(file['Body'].read())

    Query = table.query(
        IndexName = 'MessageHash-index',
        KeyConditionExpression = Key('MessageHash').eq(Hash)
    )
    tableList = Query.get('Items')
    lengthList = len(tableList)
    entityValues = ""
    entityHash = ""
    for tableItem in tableList:
        entityValues = tableItem.get("Entity")
        entityHash =  tableItem.get("EntityHash")
        paragraph = paragraph.replace(entityHash,entityValues)
  

    paragraph = paragraph.replace("b","")
    paragraph = paragraph.replace('" ','')
    paragraph = paragraph.replace('"','')
    return {
           'body': json.dumps(paragraph)
    }