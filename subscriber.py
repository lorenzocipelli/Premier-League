from callbacks import on_subscribe, on_message, on_publish, on_connect
from utils import USERNAME, PSW, URL, PORT
import json
import time
import paho.mqtt.client as paho
from paho import mqtt

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# abilito TLS per una connessione sicura
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# imposta username e password
client.username_pw_set(USERNAME, PSW)
# connetto a HiveMQ Cloud sulla porta 8883 (default per MQTT)
client.connect(URL, PORT)

# imposto le callback
client.on_subscribe = on_subscribe
client.on_message = on_message
#client.on_publish = on_publish

# iscrizione ai topic di interesse
client.subscribe("footballnews/#", qos=1)

# entro in loop di ascolto, grazie a questo comando sono rese effettive le callback
client.loop_forever()