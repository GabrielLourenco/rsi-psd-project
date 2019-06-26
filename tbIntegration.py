import json
import time
import requests

THINGSBOARD_HOST = '172.16.206.232'
THINGSBOARD_PORT = '9090'
headers = {}
headers['Content-Type'] = 'application/json'

def turnLedOn(pcap):
    global THINGSBOARD_HOST, THINGSBOARD_PORT, headers
    AT = 'XwlQnO4xcqJvqR3cQuHa'
    url = 'http://' + THINGSBOARD_HOST + ':' + THINGSBOARD_PORT + '/api/v1/' + AT + '/telemetry'
    requests.post(url, json={'led': pcap})

def devicesNumber(row):
    row_data = { 'devices' : row.__getitem__("count")}
    post('9AcKuG2Y6gSOvWmBacut', row_data)

def pnlNumber(row):
    row_data = { 'pnl' : row.__getitem__("count")}
    post('pRwrZlfbFvqeNJncFsKx', row_data)

def totalProbesNumber(row):
    row_data = { 'probes' : row.__getitem__("count")}
    post('Jp0eNJDS2sKFPAjBNIs3', row_data)

def drProbesNumber(row):
    row_data = { 'drprobes' : row.__getitem__("count")}
    post('5YExropi5V5tRJKxN7Mh', row_data)

def brProbesNumber(row):
    row_data = { 'brprobes' : row.__getitem__("count")}
    post('bTDyzkfou38KaibIGTK7', row_data)

def ssidNumber(row):
    row_data = { 'ssids' : row.__getitem__("count")}
    post('Gx0UeL5qeJx8D13rgCXD', row_data)

def processGraph1(row):
    row_data = { row.__getitem__("vendor") : row.__getitem__("macsDistinct")}
    post('y4jKDIkvpNs9sMuAmNsI', row_data)

def processGraph2(row):
    row_data = { row.__getitem__("vendor") : row.__getitem__("macsDistinct")}
    post('POp7uagT4HV8hegBEiqu', row_data)

def processTable1(row):
    row_data = { row.__getitem__("ssid") : row.__getitem__("ssidsDistinct")}
    post('UC6agSx0dX8GCf9zAaVp', row_data)

def processTable2(row):
    row_data = { row.__getitem__("mac") : row.__getitem__("ssidsDistinct")}
    post('KXYWAmDZKzyvqqKtuuRi', row_data)
    

def post(AT, data):
    global THINGSBOARD_HOST, THINGSBOARD_PORT, headers
    url = 'http://' + THINGSBOARD_HOST + ':' + THINGSBOARD_PORT + '/api/v1/' + AT + '/telemetry'
    requests.post(url, json=data)

