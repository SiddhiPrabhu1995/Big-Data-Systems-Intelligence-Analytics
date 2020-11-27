from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, JSONResponse
from fastapi import FastAPI
import json
import boto3

from app.api.api_v1.api import router as api_router
from mangum import Mangum

API_KEY = "1234567asdfgh"
API_KEY_NAME = "access_token"



api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)




async def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),

    
):

    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )

app = FastAPI()





@app.get("/")
async def root():
    dynamodb = boto3.resource('dynamodb')
    tableData = dynamodb.Table('fd_001_test')
    response = tableData.scan()
    return {
        'statusCode': 200,
        'body': response['Items']
        }

@app.get("/documentation", tags=["documentation"])
async def get_documentation(api_key: APIKey = Depends(get_api_key)):
    response = get_swagger_ui_html(openapi_url="/openapi.json", title="docs")
    response.set_cookie(
        API_KEY_NAME,
        value=api_key,
        httponly=True,
        max_age=1800,
        expires=1800,
    )
    return response


app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)
