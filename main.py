import os
import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():

URL = "https://instagram.com/favicon.ico"
response = requests.get(URL)
open("instagram.ico", "wb").write(response.content)
        
	name = os.getenv("NAME", "world")
	return f"hello {name}!"
