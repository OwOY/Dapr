from fastapi import FastAPI
import uvicorn 

app = FastAPI()
@app.get('/test')
def test():
    return {'status':'OK'}

if __name__ == '__main__':
    uvicorn.run('mainapp:app', host='0.0.0.0', port=8080)