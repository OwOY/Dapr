from fastapi import FastAPI
import uvicorn 
from dapr.ext.fastapi import DaprApp

app = FastAPI()
dapr_app = DaprApp(app) # 繼承app

@dapr_app.subscribe(pubsub='pubsub', topic='topic')
def test():
    return {'status':'OK'}

if __name__ == '__main__':
    uvicorn.run('mainapp:app', host='0.0.0.0', port=8080)