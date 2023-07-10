import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = config["client_id"]
CLIENT_SECRET = config["secret_key"]
REDIRECT_URI = config["redirect_url"]


def exchange_code(code: str):
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post("%s/oauth2/token" % API_ENDPOINT, data=data, headers=headers)
    r.raise_for_status()
    return r.json()
