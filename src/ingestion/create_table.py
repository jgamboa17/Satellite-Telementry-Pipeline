# Jonathan Gamboa
# Date 4/29/25
# This creates the table that will store the real time satellite data

import psycopg2
from db_connect import connect_to_db

def create_telemetry_table():
    conn = connect_to_db()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS telemetry (
                           id SERIAL PRIMARY KEY, 
                           satellite_id TEXT NOT NULL,
                           timestamp TIMESTAMPTZ NOT NULL,
                           latitude FLOAT NOT NULL,
                           longitude FLOAT NOT NULL,
                           altitude FLOAT NOT NULL,
                           velocity FLOAT NOT NULL,
                           battery FLOAT NOT NULL,
                           temperature FLOAT NOT NULL,
                           system_status TEXT NOT NULL
                       );
                       """)
        conn.commit()
        print("Telemetry table created successfully! (or already exists)")
    except Exception as e:
        print("ERROR! Table could not be created!", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    create_telemetry_table()