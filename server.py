import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from pydantic import BaseModel


class LogData(BaseModel):
    data: str


app = FastAPI()

@app.post("/log")
def log_data(data: LogData, request: Request):
    host = request.client.host
    print(host, data.data)
    with open(f'logs/{host}.log', 'a') as f:
        f.write(data.data)
    
uvicorn.run(app, host="127.0.0.1", port=9998)