import requests as rq

# url = 'http://localhost:5000/register'
# user_data = {
    # "username": "john_doe",
    # "email": "john@example.com",
    # "password": "mysecretpassword"
# }
# 
# 發送 POST 請求
# response = rq.post(url, json=user_data)
# 
# 檢查回應狀態碼
# if response.status_code == 200:
    # print("用戶註冊成功！")
# else:
    # print(f"用戶註冊失敗，錯誤訊息：{response.json()}")
    
url = "http://127.0.0.1:5000/logon"  # 請確保這是你 FastAPI 應用程序運行的地址

# 假設用戶名稱和密碼
user_data = {
    "username": "john_doe",
    "password": "mysecretpassword"
}

# 發送 POST 請求
response = rq.post(url, data=user_data)

# 檢查回應狀態碼
if response.status_code == 200:
    print("登錄成功！")
    print("Access Token:", response.json()["access_token"])
    print("Token Type:", response.json()["token_type"])
else:
    print(f"登錄失敗，錯誤訊息：{response.json()}")
