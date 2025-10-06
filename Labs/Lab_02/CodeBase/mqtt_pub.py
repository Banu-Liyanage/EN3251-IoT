import json, time
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"   # public test broker
PORT   = 1883
TOPIC  = "Topic123"  
QOS    = 1
INPUT_FILE = "sensor.json"
i=0
# Load JSON from file 
with open(INPUT_FILE) as f:
    payload_obj = json.load(f)

# Encode to JSON string 
payload_str = json.dumps(payload_obj)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, keepalive=60)
client.loop_start()

while(i<20):
    result = client.publish(TOPIC, payload=payload_str, qos=QOS, retain=False)
    result.wait_for_publish()
    print(f"Published to {TOPIC}: {payload_str}")
    i=i+1

time.sleep(1)
client.loop_stop()
client.disconnect()
