from kafka import KafkaProducer

# Create an instance of the Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: str(v).encode('utf-8'))

def sendToSpark(mac, timestamp, ssid):
    global producer
    producer.send('probes', '%s|%s|%f|%f' %(mac, ssid, timestamp, timestamp/10))