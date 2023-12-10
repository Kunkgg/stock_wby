import sys

sys.path.append(".")
import uvicorn
from fastapi import FastAPI, Request
from src.combination.main import combination_app


app = FastAPI(title='WBY Stock', version='1.0.0')

app.include_router(combination_app, prefix="/api", tags=["combination"])


if __name__ == '__main__':
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
