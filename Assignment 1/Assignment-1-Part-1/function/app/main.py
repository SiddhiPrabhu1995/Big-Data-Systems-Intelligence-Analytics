#import to support API key checking
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, JSONResponse
from fastapi import FastAPI
import json
import boto3

from api.api_v1.api import router as api_router
from mangum import Mangum

API_KEY = "1234567asdfgh"
API_KEY_NAME = "access_token"
COOKIE_DOMAIN = "localtest.me"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_cookie = APIKeyCookie(name=API_KEY_NAME, auto_error=False)


#checks the API key in the following order:
#Query parameter
#Header value
#Cookie


async def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),
    api_key_cookie: str = Security(api_key_cookie),
    
):

    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    elif api_key_cookie == API_KEY:
        return api_key_cookie
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

@app.get("/")
async def homepage():
    return "Welcome to the security test!"

#/documentation and /openapi.json endpoint are both protected by the get_api_key dependency
# if you access the /documentation endpoint with a valid API key, a cookie with the API key will be set which allows to use entire documentation
@app.get("/openapi.json", tags=["documentation"])
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    response = JSONResponse(
        get_openapi(title="FastAPI security test", version=1, routes=app.routes)
    )
    return response

@app.get("/documentation", tags=["documentation"])
async def get_documentation(api_key: APIKey = Depends(get_api_key)):
    response = get_swagger_ui_html(openapi_url="/openapi.json", title="docs")
    response.set_cookie(
        API_KEY_NAME,
        value=api_key,
        domain=COOKIE_DOMAIN,
        httponly=True,
        max_age=1800,
        expires=1800,
    )
    return response

#/logout endpoint is provided to clear the cookie and its contents.
@app.get("/logout")
async def route_logout_and_remove_cookie():
    response = RedirectResponse(url="/")
    response.delete_cookie(API_KEY_NAME, domain=COOKIE_DOMAIN)
    return response

#create a secure endpoint which only works if you have a valid API key
#GET methods
@app.get("/secure_fd_001_test", tags=["test"])
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    dynamodb = boto3.resource('dynamodb')
    tableData = dynamodb.Table('fd_001_test')
    response = tableData.scan()
    return {
        'statusCode': 200,
        'body': response['Items']
        }

@app.get("/secure_fd_002_test", tags=["test"])
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    dynamodb = boto3.resource('dynamodb')
    tableData = dynamodb.Table('fd_002_test')
    response = tableData.scan()
    return {
        'statusCode': 200,
        'body': response['Items']
        }

#POST method-Insert data in the table
class Item(BaseModel):
   
    id : str
    unit_number : str
    Sensor_Measure_1 : str
    Sensor_Measure_10 : str
    Sensor_Measure_11 : str
    Sensor_Measure_13 : str
    Sensor_Measure_15 : str
    Sensor_Measure_17 : str
    Sensor_Measure_19 : str
    Sensor_Measure_2 : str
    Sensor_Measure_21 : str
    Sensor_Measure_22 : str
    Sensor_Measure_23 : str
    Sensor_Measure_24 : str
    Sensor_Measure_25 : str
    Sensor_Measure_26 : str
    Sensor_Measure_3 : str
    Sensor_Measure_4 : str
    Sensor_Measure_5 : str
    Sensor_Measure_6 : str

@app.post("/items1234/")
def lambda_handler(item: Item):
    
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
      
    tableTemperature = dynamodb.Table('TEMP')
      
    id = item.id
    unit_number = item.unit_number
    Sensor_Measure_1 = item.Sensor_Measure_1
    Sensor_Measure_10 = item.Sensor_Measure_10
    Sensor_Measure_11 = item.Sensor_Measure_11
    Sensor_Measure_13 = item.Sensor_Measure_13
    Sensor_Measure_15 = item.Sensor_Measure_15
    Sensor_Measure_17 = item.Sensor_Measure_17
    Sensor_Measure_19 = item.Sensor_Measure_19
    Sensor_Measure_2 = item.Sensor_Measure_21
    Sensor_Measure_21 = item.Sensor_Measure_22
    Sensor_Measure_22 = item.Sensor_Measure_22
    Sensor_Measure_23 = item.Sensor_Measure_23
    Sensor_Measure_24 = item.Sensor_Measure_24
    Sensor_Measure_25 = item.Sensor_Measure_25
    Sensor_Measure_26 = item.Sensor_Measure_26
    Sensor_Measure_3 = item.Sensor_Measure_3
    Sensor_Measure_4 = item.Sensor_Measure_4
    Sensor_Measure_5 = item.Sensor_Measure_5
    Sensor_Measure_6 = item.Sensor_Measure_6
    
    try:
    
        tableTemperature.put_item(
            Item={
            'id' : id,
            'unit_number' : unit_number,
            'Sensor_Measure_1' : Sensor_Measure_1,
            'Sensor_Measure_10' : Sensor_Measure_10,
            'Sensor_Measure_11' : Sensor_Measure_11,
            'Sensor_Measure_13' : Sensor_Measure_13,
            'Sensor_Measure_15' : Sensor_Measure_15,
            'Sensor_Measure_17' : Sensor_Measure_17,
            'Sensor_Measure_19' : Sensor_Measure_19,
            'Sensor_Measure_2' : Sensor_Measure_2,
            'Sensor_Measure_21' : Sensor_Measure_21,
            'Sensor_Measure_22' : Sensor_Measure_22,
            'Sensor_Measure_23' : Sensor_Measure_23,
            'Sensor_Measure_24' : Sensor_Measure_24,
            'Sensor_Measure_25' : Sensor_Measure_25,
            'Sensor_Measure_26' : Sensor_Measure_26,
            'Sensor_Measure_3' : Sensor_Measure_3,
            'Sensor_Measure_4' : Sensor_Measure_4,
            'Sensor_Measure_5' : Sensor_Measure_5,
            'Sensor_Measure_6' : Sensor_Measure_6
                
             }
            )
        
        return {
         'statusCode': 200,
        'body': json.dumps('Succesfully inserted Data!')
         }
    except:
        print('Closing lambda function')
        return {
        'statusCode': 400,
        'body': json.dumps('Error saving the data')
        }

app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)