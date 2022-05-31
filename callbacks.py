def on_log(client, userdata, level, buf):
    print("log: ",buf)

# callback per l'avvenuta connessione
def on_connect(client, userdata, flags, rc, properties=None):
    client_id = str(client._client_id)[2:-1]
    print("CONNACK returned with status -> " + str(rc) +
        " | From -> " + client_id)

# callback per l'avvenuta pubblicazione su un topic
def on_publish(client, userdata, mid):
    client_id = str(client._client_id)[2:-1]
    print("Published on -> " + client_id + 
        " | Mess. id -> " + str(mid))

# callback per l'avvenuta iscrizione ad un topic
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed -> " + str(mid) + " " + str(granted_qos))

# callback per l'arrivo di un messaggio da parte del broker
def on_message(client, userdata, msg):
    payload = str(msg.payload)[2:-1]
    payload = payload.replace('\\\\','\\')
    payload = payload.replace('\\','')
    payload = payload.replace('u00a','')
    print(payload)