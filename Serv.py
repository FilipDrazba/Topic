import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/paho/mqtt")

import paho.mqtt.client as mqtt

# Konfiguracja klienta
broker_address = "localhost"
topic = "test/topic"

def on_connect(client, userdata, flags, reasonCode, properties):
    print("Połączono z brokerem MQTT z kodem: " + str(reasonCode))

client = mqtt.Client(protocol=mqtt.MQTTv5)  # Użycie nowszej wersji protokołu MQTT v5
client.on_connect = on_connect

client.connect(broker_address)

client.loop_start()

# Publikowanie wiadomości na temat
while True:
    message = input("Wpisz wiadomość do wysłania: ")
    client.publish(topic, message)
    print(f"Wysłano wiadomość: {message}")

client.loop_stop()
client.disconnect()
