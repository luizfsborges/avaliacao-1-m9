# Using hiveMQ public broker and paho mqqt client, connect to the broker and subscribe to sensor data from the broker broker = "broker.hivemq.com" port = 1883 client = mqtt.Client("sensor_data_publisher") topic sensor_data

import paho.mqtt.client as mqtt
import time
import json

# Define the broker
broker = "broker.hivemq.com"
port = 1883

# Define the client
client = mqtt.Client("sensor_data_subscriber_n_verifier")

# Connect to the broker
client.connect(broker, port)

freezer_min_temperature = -25
freezer_max_temperature = -15
refrigerator_min_temperature = 2
refrigerator_max_temperature = 10

# Function to verify the temperature
def verify_temperature(sensor_data):
    if sensor_data["tipo"] == "freezer":
        if sensor_data["temperature"] < freezer_min_temperature:
            message = {
                "id": sensor_data["id"],
                "tipo": sensor_data["tipo"],
                "temperature": sensor_data["temperature"],
                "timestamp": sensor_data["timestamp"],
                "alerta": "Temperatura do freezer muito baixa"
            }

            return message
        elif sensor_data["temperature"] > freezer_max_temperature:
            message = {
                "id": sensor_data["id"],
                "tipo": sensor_data["tipo"],
                "temperature": sensor_data["temperature"],
                "timestamp": sensor_data["timestamp"],
                "alerta": "Temperatura do freezer muito alta"
            }

            return message
        else:
            message = {
                "id": sensor_data["id"],
                "tipo": sensor_data["tipo"],
                "temperature": sensor_data["temperature"],
                "timestamp": sensor_data["timestamp"],
                "alerta": "Temperatura do freezer normal"
            }

            return message
        
    elif sensor_data["tipo"] == "refrigerator":
        if sensor_data["temperature"] < refrigerator_min_temperature:
            message = {
                "id": sensor_data["id"],
                "tipo": sensor_data["tipo"],
                "temperature": sensor_data["temperature"],
                "timestamp": sensor_data["timestamp"],
                "alerta": "Temperatura do refrigerador muito baixa"
            }

            return message
        elif sensor_data["temperature"] > refrigerator_max_temperature:
            message = {
                "id": sensor_data["id"],
                "tipo": sensor_data["tipo"],
                "temperature": sensor_data["temperature"],
                "timestamp": sensor_data["timestamp"],
                "alerta": "Temperatura do refrigerador muito alta"
            }

            return message
        else:
            message = {
                "id": sensor_data["id"],
                "tipo": sensor_data["tipo"],
                "temperature": sensor_data["temperature"],
                "timestamp": sensor_data["timestamp"],
                "alerta": "Temperatura do refrigerador normal"
            }

            return message


'''
on client.on_message, aplly some formatting to the json printing outsite json format return from the verify_temperature function on a fuction called "on_message" printing in lines:
Supermercado n (com n = freezer_ids ou refrigerator_ids no indice 3)
Freezer 1
Temperatura: -16
Status: Temperatura do freezer normal
'''

# Function to print the message
def on_message(client, userdata, message):
    sensor_data = json.loads(message.payload)
    message = verify_temperature(sensor_data)
    print(f"Supermercado {sensor_data['id'][3]}")
    print(f"{sensor_data['tipo'].capitalize()} {sensor_data['id'][6]}")
    print(f"Temperatura: {sensor_data['temperature']}")
    print(f"Status: {message['alerta']}")
    print("\n")


# Set the on_message callback
client.on_message = on_message
client.subscribe("sensor_data")

# Loop to keep the client running
client.loop_start()
time.sleep(30)
client.loop_stop()


