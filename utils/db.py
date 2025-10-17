import sqlite3

def get_connection(db_path='env_health.db'):
    conn = sqlite3.connect(db_path)
    return conn

def create_air_quality_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS air_quality (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        county TEXT,
                        pm25 REAL
                     )''')
    conn.commit()
    conn.close()
