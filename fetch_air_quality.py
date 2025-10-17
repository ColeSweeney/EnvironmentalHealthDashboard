import requests
import sqlite3

DB_PATH = 'env_health.db'

# 🔐 API Key (already hardcoded)
API_KEY = "533f963f2c5c6436d7338841a13ab26fc9c23a0de35819b40582e6e4967572f4"

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS air_quality (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT,
            city TEXT,
            country TEXT,
            date_utc TEXT,
            pm25 REAL
        )
    ''')
    conn.commit()
    conn.close()

def fetch_data(location='Compton-Rosecrans', parameter='pm25', limit=100):
    url = 'https://api.openaq.org/v3/measurements'
    params = {
        'location': location,
        'parameter': parameter,
        'limit': limit,
        'sort': 'desc',
        'order_by': 'datetime'
    }
    headers = {
        'accept': 'application/json',
        'X-API-Key': API_KEY
    }
    response = requests.get(url, params=params, headers=headers)
    
    try:
        result = response.json()
        print("Sample response:")
        print(result.get('results', [])[:3])
        return result.get('results', [])
    except Exception as e:
        print("Error parsing response:", e)
        return []

def insert_data(rows):
    conn = get_connection()
    c = conn.cursor()
    for row in rows:
        c.execute('''
            INSERT INTO air_quality (location, city, country, date_utc, pm25)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            row.get('location'),
            row.get('city'),
            row.get('country'),
            row['date']['utc'],
            row.get('value')
        ))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
    data = fetch_data(location="Compton-Rosecrans", parameter="pm25", limit=100)

    print(f"\nFetched {len(data)} records from OpenAQ\n")
    
    if data:
        insert_data(data)
        print(f"Inserted {len(data)} rows into the air_quality table.")
    else:
        print("No data was fetched. Check location name or API limits.")
