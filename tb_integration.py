import paho.mqtt.client as mqtt
import json
import time

THINGSBOARD_HOST = '172.16.206.232'
ACCESS_TOKEN = 'PotOorQHxrb7YW9PXcsN'

def processRow(row):
    print(row)
    # row_data = "{" + row.word + ":" + str(row.count) + "}"
    # row_data = { row.word : row.__getitem__("count")}
    row_data = { 'SSID_325455' : 54, 'timestamp': time.time()*100 }

    # Write row to storage
    client = mqtt.Client()
    # Set access token
    client.username_pw_set(ACCESS_TOKEN)
    # Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
    client.connect(THINGSBOARD_HOST, 1883, 60)
    # Sending humidity and temperature data to ThingsBoard
    client.publish('v1/devices/me/telemetry', json.dumps(row_data), 1)

processRow('SSID_325455')