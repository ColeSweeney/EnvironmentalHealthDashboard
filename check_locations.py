import requests

# 🔐 Use your real API key here (DO NOT upload to GitHub!)
API_KEY = "533f963f2c5c6436d7338841a13ab26fc9c23a0de35819b40582e6e4967572f4"

url = "https://api.openaq.org/v3/locations"
params = {"country": "US", "limit": 200, "page": 1}
headers = {"X-API-Key": API_KEY}

res = requests.get(url, headers=headers, params=params)

print("Status Code:", res.status_code)
print("Response JSON:", res.json())  # See what's inside

# If the API works, print Indiana city names
if res.status_code == 200 and "results" in res.json():
    locations = res.json()["results"]
    indiana = [loc for loc in locations if "Indiana" in loc.get("city", "")]
    for loc in indiana:
        print(loc["city"], "-", loc["name"])
else:
    print("API request failed or returned unexpected data.")
