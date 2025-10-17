""" import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAQ_API_KEY")
print("using API key:", API_KEY)
url = "https://api.openaq.org/v3/locations"
headers = {
    "accept": "application/json",
    "X-API-Key": API_KEY
}
params = {
    "country": "US",
    "limit": 100,
    "page": 1,
    "city": "Indianapolis"
}

res = requests.get(url, headers=headers, params=params)

if res.status_code == 200:
    results = res.json().get("results", [])
    results = res.json().get("results", [])
for loc in results:
    print(loc.get("city"), "-", loc.get("name"))
    cities = sorted(set(loc.get("city") for loc in results if "city" in loc and loc["city"]))
    print("Supported Cities:", cities)
else:
    print("Error:", res.status_code, res.text)
 """



import requests
import os

API_KEY = "533f963f2c5c6436d7338841a13ab26fc9c23a0de35819b40582e6e4967572f4"
url = "https://api.openaq.org/v3/locations"

params = {
    "country": "US",
    "parameter": "pm25",
    "limit": 100,
    "sort": "desc"
}
headers = {
    "X-API-Key": API_KEY,
    "accept": "application/json"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json().get("results", [])
    print("Sample PM2.5 locations in the US:")
    for loc in data:
        print(f"- {loc.get('name')} ({loc.get('city')})")
else:
    print(f"Error: {response.status_code}", response.text)
