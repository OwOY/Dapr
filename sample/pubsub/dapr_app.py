import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dapr.clients import DaprClient

app = FastAPI()
@app.get('/sidecar_test')
def test():
    with DaprClient() as client:
        client.publish_event(
            pubsub_name='pubsub',
            topic_name='any_topic',
            data='message',
            metadata={'foo':'bar'}
        )
    return JSONResponse({'status':'OK'})


if __name__ == '__main__':
    uvicorn.run('dapr_app:app', host='0.0.0.0', port=8081)