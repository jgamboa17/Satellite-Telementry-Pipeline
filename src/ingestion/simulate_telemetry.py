# Jonathan Gamboa
# Date: 4/27/25
# Version 1: Create random data, will soon run real-time data

import random
import time
from datetime import datetime
import csv
import os
import subprocess

def generate_random_telemetry():
    telemetry_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "latitude": random.uniform(-90, 90),
        "longitude": random.uniform(-180.0, 180.0),
        "altitude_m": random.uniform(160.0, 40000.0), # meters
        "velocity_m_s": 7800 + random.uniform(-50.0,50.0), # meters per second
        "satellite_id" : random.uniform(0, 10.0), # randrom satellite ID, once data is implemented, will have a real ID
        "battery_level_percent" : random.uniform(20.0,100.0),
        "temperature_celcius": random.uniform(-100.0, 100,0),
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