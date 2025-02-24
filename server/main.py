from fastapi import *
from pydantic import BaseModel as bm

app = FastAPI()

class chun(bm):
	name:str


l = ['saeed','bigjm','jm']

@app.post("/username/check")
def index(log:chun):
	if log.name in l:
		return(0)
	return 1
	if len(log.name)<=0:
		return -1

#sssss
