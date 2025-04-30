# Jonathan Gamboa
# Date: 04/29/2025
# This code will insert data into the table in our database

import psycopg2
from db_connect import connect_to_db
from simulate_telemetry import generate_random_telemetry # type: ignore

def insert_telemetry(data):
    conn = connect_to_db()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO telemetry (
                satellite_id, timestamp, latitude, longitude, altitude, velocity,
                battery, temperature, system_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,(
            data["satellite_id"],
            data["timestamp"],
            data["latitude"],
            data["longitude"],
            data["altitude_m"],
            data["velocity_m_s"],
            data["battery_level_percent"],
            data["temperature_celcius"],
            data["system_status"]
        )) 
        conn.commit()
        print("Successfully insert data to table!")

    except Exception as e:
        print("ERROR! Failed to insert data!", e)
    
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    telemetry = generate_random_telemetry()
    insert_telemetry(telemetry)