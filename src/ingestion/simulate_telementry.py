# Jonathan Gamboa
# Date: 4/27/25
# Version 1: Create random data, will soon run real-time data

import randomq
import time

def generate_random_telemetry():
    telemetry_data = {
        "timestamp": time.time(),
        "latitude": random.uniform(-90, 90),
        "longitude": random.uniform(-180, 180),
        "altitude_m": random.uniform(0, 40000), # meters
        "velocity_m_s": random.uniform(0, 8000), # meters per second
    }
    return telemetry_data

def main():
    while True:
            data = generate_random_telemetry()
            print(data)
            time.sleep(1) #waits 1 second before updating information

if __name__ == "__main__":
    main()