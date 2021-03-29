import requests

url = "https://defendtheweb.net/playground/secure-agent"

headers = {
    "User-agent": "secure_user_agent",
}

response = requests.get(url,headers=headers)
print(response)