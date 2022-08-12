import os
import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from pydantic import BaseModel


host = "127.0.0.1"
port = 9998
logs_dir = os.path.join(os.path.dirname(__file__), 'logs')


class LogData(BaseModel):
    data: str


app = FastAPI()


@app.post("/log")
def log_data(data: LogData, request: Request):
    host = request.client.host
    print(host, data.data)
    with open(f'{logs_dir}/{host}.log', 'a') as f:
        f.write(data.data)


if __name__ == '__main__':
    os.mkdir(logs_dir, exist_ok=True)
    uvicorn.run(app, host=host, port=port)
