import requests

API_KEY = "533f963f2c5c6436d7338841a13ab26fc9c23a0de35819b40582e6e4967572f4"

headers = {
    "accept": "application/json",
    "X-API-Key": API_KEY
}

print("US Locations with PM2.5:\n")

for page in range(1, 6):  # Pages 1–5
    url = "https://api.openaq.org/v3/locations"
    params = {
        "limit": 100,
        "page": page,
        "sort": "desc",
        "order_by": "id"
        # ❌ no country param — filter manually below
    }

    res = requests.get(url, headers=headers, params=params)
    results = res.json().get("results", [])

    for r in results:
        country_code = r.get("country", {}).get("code", None)
        param_list = [s["parameter"]["name"] for s in r.get("sensors", []) if "parameter" in s]

        if country_code == "US" and "pm25" in param_list:
            print(f"- {r['name']} (city: {r.get('locality', 'Unknown')})")
