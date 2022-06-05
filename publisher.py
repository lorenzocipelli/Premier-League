from callbacks import on_subscribe, on_message, on_publish, on_connect
from utils import USERNAME, PSW, HOST_TLS, PORT_TLS, WELCOME_MESSAGE, TEAM_MESSAGE_1, TEAM_MESSAGE_2, HOST_NO_TLS, PORT_NO_TLS
import pandas as pd
import time
import paho.mqtt.client as paho
from paho import mqtt

base_name = "premier_league_news/"

# CTRL + K + C -> comment block of code
# CTRL + K + U -> uncomment block of code

client = paho.Client(client_id="Publisher", userdata=None, protocol=paho.MQTTv5)
df = pd.read_csv("database/football_news.csv")
client.on_connect = on_connect

# abilito TLS per una connessione sicura
# client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# imposta username e password
# client.username_pw_set(USERNAME, PSW)
# connetto al broker (8883 porta default per mqtt over tls)
# client.connect(HOST_TLS, PORT_TLS)
client.connect(HOST_NO_TLS, PORT_NO_TLS)

# imposto le callback
client.on_subscribe = on_subscribe
client.on_publish = on_publish
# client.on_message = on_message

# entro in loop di ascolto, grazie a questo comando sono rese effettive le callback
client.loop_start()
# messaggio Retaied con la guida dei comandi per l'iscrizione ai sotto-topic
# client.publish("premier_league_news", payload=WELCOME_MESSAGE, qos=1, retain=True)

# in questa fase simuliamo l'invio settimanale di dati riguardanti il prezzo dei carburanti 
for index, row in df.iterrows():
    club_name = str(row["team_name"])
    news_content = row["news_content"]
    topic_name = base_name + club_name.lower().replace(' ', '_')
    client.publish(topic_name, payload=news_content, qos=1, retain=False)

    # PUBBLICAZIONE DEI MESSAGGI Retained per ogni sotto topic di premier_league_news
    # team_welcome = TEAM_MESSAGE_1 + club_name + TEAM_MESSAGE_2
    # client.publish(topic_name, payload=team_welcome, qos=1, retain=True)

    time.sleep(2)

client.loop_stop()