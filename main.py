import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
        osinfo = os.getenv()
	name = os.getenv("NAME", "world")
	return f"hello {name}!"
