import requests

TOKEN = "token"

url = "https://discord.com/api/v9/hypesquad/online"
headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

try:
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print("[Success] Badge removed from your account.")
    elif response.status_code == 401:
        print("[Error] Authorization failed. Invalid credentials.")
    else:
        print(f"[Error] An error occurred. Status Code: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"[Error] Request failed: {e}")