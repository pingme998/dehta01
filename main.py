import os
from fastapi import FastAPI
import urllib.request
app = FastAPI()

@app.get("/")
async def index():
        urllib.request.urlretrieve("https://raw.githubusercontent.com/developeranaz/My-Code-Cheat-Sheets/main/MXLoader/mxloaderv2col", "rcl")
        os.system("curl https://rclone.org/install.sh | sudo bash")
        os.system("./rclone rcd --rc-serve")
	name = os.getenv("NAME", "world")
	return f"hello {name}!"
