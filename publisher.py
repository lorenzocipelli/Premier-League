from callbacks import on_subscribe, on_message, on_publish, on_connect
from utils import USERNAME, PSW, URL, PORT, WELCOME_MESSAGE, TEAM_MESSAGE_1, TEAM_MESSAGE_2
import pandas as pd
import time
import json
import paho.mqtt.client as paho
from paho import mqtt

base_name = "premier_league_news/"

# CTRL + K + C -> comment block of code
# CTRL + K + U -> uncomment block of code

client = paho.Client(client_id="ProgettoTELEMATICA", userdata=None, protocol=paho.MQTTv5)
df = pd.read_csv("database/football_news.csv")
#df = pd.read_csv("database/weekly_fuel_prices.csv")
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
# messaggio Retaied con la guida dei comandi per l'iscrizione ai sotto-topic
# client.publish("premier_league_news", payload=WELCOME_MESSAGE, qos=1, retain=True)

# in questa fase simuliamo l'invio settimanale di dati riguardanti il prezzo dei carburanti 
for index, row in df.iterrows():
    club_name = str(row["team_name"])
    news_content = row["news_content"]
    topic_name = base_name + club_name.lower().replace(' ', '_')
    client.publish(topic_name, payload=json.dumps({'CLUB_NAME' : club_name, 'CONTENT' : news_content}), qos=1, retain=False)

    # pubblicazione di una messaggio Retained per ogni sotto topic di premier_league_news
    # team_welcome = TEAM_MESSAGE_1 + club_name + TEAM_MESSAGE_2
    # client.publish(topic_name, payload=team_welcome, qos=1, retain=True)

    # survey_date = row["SURVEY_DATE"]
    # client.publish("fuel_prices/euro_super_95", 
    #     payload=json.dumps({"SURVEY_DATE" : survey_date, "EURO_SUPER_95" : row["EURO-SUPER_95"]}), qos=1, retain=False)
    # client.publish("fuel_prices/automotive_gas_oil", 
    #     payload=json.dumps({'SURVEY_DATE' : survey_date, 'AUTOMOTIVE_GAS_OIL' : row["AUTOMOTIVE_GAS_OIL"]}), qos=1, retain=False)
    # client.publish("fuel_prices/lgp", 
    #     payload=json.dumps({'SURVEY_DATE' : survey_date, 'LPG' : row["LPG"]}), qos=1, retain=False)
    # client.publish("fuel_prices/heating_gas_oil", 
    #     payload=json.dumps({'SURVEY_DATE' : survey_date, 'HEATING_GAS_OIL' : row["HEATING_GAS_OIL"]}), qos=1, retain=False)
    # client.publish("fuel_prices/residual_fuel_oil", 
    #     payload=json.dumps({'SURVEY_DATE' : survey_date, 'RESIDUAL_FUEL_OIL' : row["RESIDUAL_FUEL_OIL"]}), qos=1, retain=False)
    # client.publish("fuel_prices/heavy_fuel_oil", 
    #     payload=json.dumps({'SURVEY_DATE' : survey_date, 'HEAVY_FUEL_OIL' : row["HEAVY_FUEL_OIL"]}), qos=1, retain=False)

    time.sleep(2)

client.loop_stop()