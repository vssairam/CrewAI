import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv(override=True)

api_key = os.getenv("SERPER_API_KEY")

if not api_key:
    raise ValueError("SERPER_API_KEY not found in .env")

# Serper API endpoint
url = "https://google.serper.dev/search"

headers = {
    "X-API-KEY": api_key,
    "Content-Type": "application/json"
}

payload = {
    "q": "latest technology news",
    "num": 3
}

try:
    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=20
    )

    print("HTTP Status Code:", response.status_code)

    if response.status_code == 200:
        print("\nSUCCESS! Serper API is working.")

        data = response.json()

        for item in data.get("organic", []):
            print("\nTitle:", item.get("title"))
            print("Link:", item.get("link"))

    else:
        print("\nAPI request failed.")
        print("Response:", response.text)

except requests.RequestException as e:
    print("Connection error:", e)