import paho.mqtt.client as mqtt
import time
import pymongo as py

client =py.MongoClient("mongodb+srv://iot12345:iot12345@mycluster.a5fvb.mongodb.net/myDB?retryWrites=true&w=majority")
clientdb=py.MongoClient("mongodb://localhost:27017//")
db = clientdb["senseIt"]
col = db["status-collection"]


def on_message(client, userdata, message):
    info = message.payload.decode("utf-8").split(",")
    print(info)
    # print("recieved temperature is ",str(message.payload.decode("utf-8")))
    #col.insert_one({"door-status": info[0], "sender": info[1]})

    # print(info[0])
    # print()


client = mqtt.Client("senseIt")
client.connect("mqtt.eclipseprojects.io")

client.loop_start()
client.subscribe("door_status")
client.on_message = on_message
time.sleep(120)
client.loop_stop()
