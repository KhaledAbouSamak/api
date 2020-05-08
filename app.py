import uvicorn
from  fastapi import FastAPI, Body, Path,Query
from pydantic import BaseModel,Field

class Item(BaseModel):
	name:str
	desc:str = Field(None, title = 'item description', max_length = 250)
	price:float = Field (...,gt = 0, le = 100)
	tax:float=None

class User(BaseModel):
	username:str
	full_name:str = None


app = FastAPI()

@app.get("/users/me")
async def read_user_me():
	return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id:str):
	return {"user_id": user_id}


@app.get("/items/")
async def read_items(skip: int = 10, limit :int = 4):
	return {"skip": skip, 'limit':limit}


@app.get("/all_items/{item_id}")
async def read_all_items(item_id:str, item:Item):
	return {"itemid": item_id, 'item':item}


@app.get("/mine/{item_id}")
async def read_mine(item_id:str, item:Item):
	return {"itemid": item_id, 'item':item}



@app.put("/items/{item_id}")
async def read_all_items(*, item_id:int, item:Item=Body(...,embed=True)):
	return {"itemid": item_id, 'item':item}

if __name__ == '__main__':
	uvicorn.run(app, host = '127.0.0.1', port = 8001)
