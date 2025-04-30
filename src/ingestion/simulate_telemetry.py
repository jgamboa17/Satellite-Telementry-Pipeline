# Jonathan Gamboa
# Date: 4/27/25
# Version 1: Create random data, will soon run real-time data

import random
import time
from datetime import datetime, timezone
import csv
import os
import subprocess

def generate_random_telemetry():
    telemetry_data = {
        "satellite_id" : "SAT-118", # randrom satellite ID, once data is implemented, will have a real ID
        "timestamp": datetime.now(timezone.utc),
        "latitude": round(random.uniform(-90, 90), 2),
        "longitude": round(random.uniform(-180, 180), 2),
        "altitude_m": round(random.uniform(200, 400), 2), # meters
        "velocity_m_s": round(random.uniform(6, 8),2 ), # meters per second
        "battery_level_percent" : round(random.uniform(20, 100), 2),
        "temperature_celcius": round(random.uniform(-100, 100), 2),
        "system_status": random.choice(["Nominal", "Warning", "Critical"])

    }
    return telemetry_data

def save_to_csv(data, filename="telementry_log.csv"):
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="") as csvfile:
        fieldnames = ["timestamp", "latitude", "longitude", "altitude_m", "velocity_m_s", "satellite_id", 
        "battery_level_percent", "temperature_celcius", "system_status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)

        if not file_exists: 
             subprocess.run(["code", filename])
        
    print("Saving to:", os.path.abspath(filename))

def main():
    while True:
            data = generate_random_telemetry()
            print(data)
            save_to_csv(data)
            time.sleep(1) #waits 1 second before updating information

if __name__ == "__main__":
    main()