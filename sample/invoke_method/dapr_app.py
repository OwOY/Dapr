from fastapi import FastAPI
import uvicorn
from dapr.clients import DaprClient
import json

data = {'foo':'bar'}
query_string = [('foo', 'bar')]
method = 'GET'
headers = [('host', '127.0.0.1')]

app = FastAPI()
@app.get('/sidecar_test')
async def test():
    with DaprClient() as client:
        response = await client.invoke_method_async(
            app_id='app', # 對應該service的app id
            method_name='/test', # 對應該service的API
            data=json.dumps(data), # 傳入參數
            http_querystring=query_string, # 傳入queryString
            http_verb=method, # API方法
            metadata=headers # headers
        )
    return response

if __name__ == '__main__':
    uvicorn.run('dapr_app:app', host='0.0.0.0', port=8080)