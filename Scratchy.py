import paho.mqtt.client as paho
import requests



def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    #print(msg.topic +" "+str(msg.qos) + msg.payload.decode('ascii'))
    value = msg.payload.decode('ascii')
    arrTopic = msg.topic.rsplit("/")    
    device = arrTopic[1]
    sensor = arrTopic[2]  
    print(device)
    print(sensor)
    print(value)
    url = 'http://ES_search_demo.com/document/record/_search?pretty=true'

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("broker.mqttdashboard.com", 1883)
client.subscribe("scratchy/#")
client.loop_forever()




"""
    url = 'http://ES_search_demo.com/document/record/_search?pretty=true'
    data = '''{
    "query": {
        "bool": {
        "must": [
            {
            "text": {
                "record.document": "SOME_JOURNAL"
            }
            },
            {
            "text": {
                "record.articleTitle": "farmers"
            }
            }
        ],
        "must_not": [],
        "should": []
        }
    },
    "from": 0,
    "size": 50,
    "sort": [],
    "facets": {}
    }'''
    response = requests.post(url, data=data)

"""


