from pymongo import MongoClient
import json
from bson import json_util

# 初始化資料庫連接
client = MongoClient("mongodb://localhost:27017/")

# 設定資料庫
db = client['count']

users = db.users
id_users = db.id_users

user_db = users.find_one({"name":"user.username","email":"user.email"})
if user_db != None:
    print('ea')
    


# users_db = {
    # "name":"user.username",
    # "email": "user.email",
    # "username": "user.username",
    # "password": "hashed_password"
# }
# users.insert_one(users_db)
# print(users.find())