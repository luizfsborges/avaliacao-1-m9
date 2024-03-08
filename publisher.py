import paho.mqtt.client as mqtt
import time
import random
import json

# Função para retornar o timestamp
def get_timestamp():
    time_stamp = time.strftime("%d/%m/%Y %H:%M")
    return time_stamp

# Definição do broker
broker = "broker.hivemq.com"
port = 1883

# Dfinição do cliente
client = mqtt.Client("sensor_data_publisher")

# Conecção ao broker
client.connect(broker, port)

# IDs dos sensores dos freezers e refrigeradores para os supermercados 1 e 2
freezer_ids = ["lj01f01", "lj01f02", "lj02f01", "lj02f02"]
refrigerator_ids = ["lj01r01", "lj01r02", "lj02r01", "lj02r02"]

freezer_test_temps = [-16, -14, -26]
refrigerator_test_temps = [9, 11, 1]

modo_publisher = input("Digite o modo de publicação de dados: [T]este ou [P]rodução: ")

if modo_publisher == "T":
    for i in range(len(freezer_ids)-1):
        sensor_data_freezer = {
            "id": freezer_ids[i],
            "tipo": "freezer",
            "temperature": freezer_test_temps[i],
            "timestamp": get_timestamp()
        }

        # Publicar dados do freezer no topico "sensor_data" com qos 1
        client.publish("sensor_data", json.dumps(sensor_data_freezer), qos=1)
        time.sleep(1)

    for i in range(len(refrigerator_ids)-1):
        sensor_data_refrigerator = {
            "id": refrigerator_ids[i],
            "tipo": "refrigerator",
            "temperature": refrigerator_test_temps[i],
            "timestamp": get_timestamp()
        }

        # Publicar dados do refrigerador no topico "sensor_data" com qos 1
        client.publish("sensor_data", json.dumps(sensor_data_refrigerator), qos=1)
        time.sleep(1)

elif modo_publisher == "P":
    while True:
        for i in range(len(freezer_ids)-1):
            sensor_data_freezer = {
                "id": freezer_ids[i],
                "tipo": "freezer",
                "temperature": random.randint(-30, -10),
                "timestamp": get_timestamp()
            }

            # Publicar dados do freezer no topico "sensor_data" com qos 1
            client.publish("sensor_data", json.dumps(sensor_data_freezer), qos=1)
            time.sleep(1)

        for i in range(len(refrigerator_ids)-1):
            sensor_data_refrigerator = {
                "id": refrigerator_ids[i],
                "tipo": "refrigerator",
                "temperature": random.randint(0, 15),
                "timestamp": get_timestamp()
            }

            # Publicar dados do refrigerador no topico "sensor_data" com qos 1
            client.publish("sensor_data", json.dumps(sensor_data_refrigerator), qos=1)
            time.sleep(1)

client.disconnect()
        