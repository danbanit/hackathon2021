import paho.mqtt.client as mqtt
import time

topic = "ESP/VFIII/L/CMD/072444206066/004B0585" # Done! PLEASE CHANGE THIS
DISARM = "SDES02C000000FFF0123123120002104201432P*123414!803D" # Done! PLEASE CHANGE THIS
qos = 0

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic, 0) # Done! PLEASE CHANGE THIS

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def mqttSendDisarm():
    print("Connecting to broker")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    broker = "az-mqtt-sd.ops-esi.com" # "20.71.134.119" # Done! PLEASE CHANGE THIS
    client.connect(broker, 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_start()
    client.publish(topic, DISARM, qos, False)
    print(topic + ": " + DISARM)
    client.loop_stop()
