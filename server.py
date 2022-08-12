import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from pydantic import BaseModel


class LogData(BaseModel):
    data: str


app = FastAPI()

@app.post("/log")
def log_data(data: LogData, request: Request):
    print(data.data)
    print(request.client.host)
    
uvicorn.run(app, host="127.0.0.1", port=9998)