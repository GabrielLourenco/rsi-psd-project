import json
import time
import requests

THINGSBOARD_HOST = '172.16.206.232'
THINGSBOARD_PORT = '9090'
ACCESS_TOKEN = 'ONQGJIopoQeSabtQ3itA'
url = 'http://' + THINGSBOARD_HOST + ':' + THINGSBOARD_PORT + '/api/v1/' + ACCESS_TOKEN + '/telemetry'
headers = {}
headers['Content-Type'] = 'application/json'

def processRow(row):
    row_data = { row.__getitem__("ssid") : row.__getitem__("count")}
    requests.post(url, json=row_data)
