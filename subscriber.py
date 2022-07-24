from callbacks import on_subscribe, on_message, on_connect, on_log
from utils import HOST_NO_TLS, HOST_TLS, PORT_NO_TLS, PORT_TLS, USERNAME, PSW, LOCALHOST
import paho.mqtt.client as paho
from paho import mqtt

CLIENT_ID = "Receiver_Cipelli"
TESTAMENT = CLIENT_ID + " went offline, sad :("

client_mqtt = paho.Client(client_id=CLIENT_ID, clean_session=False, userdata=None, protocol=paho.MQTTv311, reconnect_on_failure=True)
client_mqtt.on_connect = on_connect

# abilito TLS per una connessione sicura
# client_mqtt.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# imposta username e password
# client_mqtt.username_pw_set(USERNAME, PSW)
client_mqtt.will_set(topic="premier_league_news/manchester_city", payload=TESTAMENT, qos=0)
# connetto al broker (8883 porta default per mqtt over tls)
# client_mqtt.connect(HOST_TLS, PORT_TLS)
client_mqtt.connect(HOST_NO_TLS, PORT_NO_TLS, keepalive=60)

# imposto le callback
client_mqtt.on_subscribe = on_subscribe
client_mqtt.on_message = on_message
# client_mqtt.on_log=on_log

# ISCRIZIONE AI TOPIC DI INTERESSE
# client_mqtt.subscribe("premier_league_news", 1) # come se fosse un menù del servizio
client_mqtt.subscribe([("premier_league_news/manchester_city", 1),("premier_league_news/west_ham_united", 1)])
#client_mqtt.subscribe("premier_league_news/#", 1) # iscrizione a tutti i sotto-topic

# entro in loop di ascolto, grazie a questo comando sono rese effettive le callback
client_mqtt.loop_forever()