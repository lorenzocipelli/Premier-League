from callbacks import on_subscribe, on_message, on_publish, on_connect
from utils import USERNAME, PSW, URL, PORT
import time
import json
import paho.mqtt.client as paho
from paho import mqtt

client = paho.Client(client_id="ProgettoTELEMATICA", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# abilito TLS per una connessione sicura
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# imposta username e password
client.username_pw_set(USERNAME, PSW)
# connetto a HiveMQ Cloud sulla porta 8883 (default per MQTT)
client.connect(URL, PORT)

# imposto le callback
client.on_subscribe = on_subscribe
#client.on_message = on_message
client.on_publish = on_publish

# entro in loop di ascolto, grazie a questo comando sono rese effettive le callback
client.loop_start()

i = 0
for i in range(10):
    score = {
            'home_team': 'Parma',
            'away_team': 'Sassuolo',
            'home_team_score' : 3,
            'away_team_score' : 0 }

    client.publish("footballnews", payload=json.dumps(score), qos=1, retain=False)
    i += 1
    time.sleep(5)

client.loop_stop()