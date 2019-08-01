import paho.mqtt.client as paho
import requests

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    value = msg.payload.decode('ascii')
    arrTopic = msg.topic.rsplit("/")    
    device = arrTopic[1]
    sensor = arrTopic[2]  
    url = "http://35.157.193.102:8080/devices/" + device + "/data"
    data = {
        'name':sensor,
        'value':value
    }
    r = requests.post(url, json=data)

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("broker.mqttdashboard.com", 1883)
client.subscribe("scratchy/#")
client.loop_forever()