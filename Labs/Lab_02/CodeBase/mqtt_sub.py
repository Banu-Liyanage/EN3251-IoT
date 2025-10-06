import json
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT   = 1883
TOPIC  = "Topic123" 
QOS    = 1
OUTPUT_FILE = "sensor_received.json"

def on_connect(client, userdata, flags, reason_code, props=None):
    print("Connected:", reason_code)
    client.subscribe(TOPIC, qos=QOS)

def on_message(client, userdata, msg):
    print(f"Received on {msg.topic}: {msg.payload.decode('utf-8')}")
    try:
        obj = json.loads(msg.payload.decode("utf-8"))
        with open(OUTPUT_FILE, "w") as f:
            json.dump(obj, f, indent=4)
        print(f"Saved to {OUTPUT_FILE}")
    except Exception as e:
        print("Decode/write error:", e)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, keepalive=60)
client.loop_forever()