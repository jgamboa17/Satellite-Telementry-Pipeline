# Jonathan Gamboa
# Date 4/28/2025
# Python script to connect to the PostgreSQL Server

import psycopg2

def connect_to_db(): 
    try: 
        conn = psycopg2.connect(
            dbname =  "satellite_telemetry",
            user = "postgres",
            password = "johnjohn13",
            host = "localhost",
            port = "5432"
        )
        print("Connected to the database!")
        return conn
    except Exception as e:
        print("ERROR! Failed to conect to the database!")
        print(e)
        return None
    
if __name__ == "__main__":
    connect_to_db()
