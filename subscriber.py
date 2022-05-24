import time
import paho.mqtt.client as paho
from paho import mqtt

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    client_id = str(client._client_id)[2:-1]
    print("CONNACK returned with status -> " + str(rc) +
        "\nFrom -> " + client_id)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid):
    client_id = str(client._client_id)[2:-1]
    print("Published on -> " + client_id + 
        "\nMess. id -> " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed -> " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("ProgettoTELE", "Cipelli0Cresci")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("ff4612ecc8c647d7b6128392b277b68a.s1.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("footballnews/#", qos=1)

# a single publish, this can also be done in loops, etc.
#client.publish("encyclopedia/temperature", payload="hot", qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()