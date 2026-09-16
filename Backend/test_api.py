# .\venv\Script\Active.ps1
import requests

url = "http://127.0.0.1:5000/predict"

data={
    "message":"Congratulation! You have won a free prize"
}

response = requests.post(url,json=data)

print(response.json())