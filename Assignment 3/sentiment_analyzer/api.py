from typing import Dict

import json, boto3, requests, urllib.request

from botocore.vendored import requests

from boto3.dynamodb.conditions import Key

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from .sam import Model, get_model

app = FastAPI()


#class SentimentRequest(BaseModel):
#    text: str


class SentimentResponse(BaseModel):
    probabilities: Dict[str, float]
    sentiment: str
    confidence: float


@app.post("/predict", response_model=SentimentResponse)
#@app.post("/predict")
def predict(filename: str, model: Model = Depends(get_model)):
    
    s3 = boto3.client("s3")
    bucket = "inputpii"
    key = filename
    file = s3.get_object(Bucket=bucket, Key=key)
    paragraph = str(file['Body'].read())
    #return paragraph
    
    sentiment, confidence, probabilities = model.predict(paragraph)
    return SentimentResponse(
        sentiment=sentiment, confidence=confidence, probabilities=probabilities
    )


