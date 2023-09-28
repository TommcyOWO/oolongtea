from fastapi import Depends, FastAPI,HTTPException,Request,Response
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

import json
import math
from pymongo import MongoClient

#過濾器
from model import *

#oauth 初始化
from oauth import *

#初始化
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(redoc_url=None,docs_url=None)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

origins = [
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#DB 初始化
#DB herf
client = MongoClient("mongodb://localhost:27017/")

#DB setup
db = client['count']

users = db.users
id_users = db.id_users

#阻擋request
@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=exc.status_code,
        content={"ERROR":f"Too many request,{exc.detail}"},
    )

#404 error handler
@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"ERROR":exc.detail},
    )

#405 error handler
@app.exception_handler(405)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"ERROR":exc.detail},
    )

#main
#oauth path

@app.post("/register")
async def register_user(user: User):
    users_db = users.find()
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = password_context.hash(user.password)
    users_db[user.username] = {
        "email": user.email,
        "username": user.username,
        "password": hashed_password
    }
    users.insert_one(users_db)
    return {"message": "User registered successfully"}

# @app.post("/reset")
# async def reset_acount(user:User):
    # with open(path+'count.json','r') as file:
        # reset_acount = json.load(file)
    # if user.username not in reset_acount:
        # raise HTTPException(status_code=400, detail="Username not exists.")
    # if user.email != reset_acount[user.username]['email']:
        # raise HTTPException(status_code=400, detail="Email do not match.")
    # hashed_password = password_context.hash(user.password)
    # with open(path+'count.json','w') as file:
        # reset_acount[user.username]["password"] = hashed_password
        # json.dump(reset_acount,file,indent=4)
    # return {"message":"Reset done"}

@app.post("/logon")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    users_db = users.find()
    if form_data.username not in users_db:
        raise HTTPException(status_code=400, detail="Wrong password or username")
    user = users_db[form_data.username]
    if user is None or not password_context.verify(form_data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=5000)
    #uvicorn.run(app,host='0.0.0.0',ssl_keyfile='./key.pem',ssl_certfile='./cert.pem')