import requests
import csv
from datetime import datetime
import time

API_KEY = "OM1ZYo3CE40rZj90iApZUIFl6RthtMTO"

locations = [
    (28.6139, 77.2090),  # Connaught Place, Delhi
    (28.7041, 77.1025),  # North Delhi
    (28.4595, 77.0266),  # Gurgaon
    (28.4089, 77.3178),  # Faridabad
    (28.5355, 77.3910),  # Noida
]

filename = "traffic_data.csv"

# Add header only once
with open(filename, 'a', newline='') as file:
    writer = csv.writer(file)
    if file.tell() == 0:  # if file is empty
        writer.writerow(["timestamp", "latitude", "longitude", "currentSpeed", "freeFlowSpeed", "congestionLevel"])

while True:
    for lat, lon in locations:
        url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point={lat},{lon}&key={API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            flow = data['flowSegmentData']

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            current_speed = flow['currentSpeed']
            free_flow_speed = flow['freeFlowSpeed']
            congestion_level = flow['currentTravelTime'] / flow['freeFlowTravelTime']

            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, lat, lon, current_speed, free_flow_speed, congestion_level])
            
            print(f"[{timestamp}] {lat},{lon} -> Speed: {current_speed}, Congestion: {congestion_level:.2f}")
        
        else:
            print(f"Failed to fetch data for {lat},{lon}: {response.status_code}")
    
    time.sleep(120)  # Wait for 2 mins before next fetch
