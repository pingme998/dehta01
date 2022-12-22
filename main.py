import os
import subprocess
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():

        name = subprocess.check_output("echo hi", shell=True)

	return f"hello {name}!"
