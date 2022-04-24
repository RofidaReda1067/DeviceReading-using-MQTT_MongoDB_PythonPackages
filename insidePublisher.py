import paho.mqtt.client as mqtt
from random import randrange
import time
import pymongo as py


client =py.MongoClient("mongodb+srv://iot12345:iot12345@mycluster.a5fvb.mongodb.net/myDB?retryWrites=true&w=majority")
db=client["myProject"]
col=db.door_status_inside


client=mqtt.Client("door_status_collection")
client.connect("mqtt.eclipseprojects.io")


while True:
    randomStatus=randrange(5,10)

    status= ""
    if randomStatus == 5:
        status = "the door is closed"
    else:
        status = "the door is opened"
    t=time.ctime()
    client.publish("door_status", payload=status+","+"door_inside_home")

    col.insert_one({"statusOutide":randomStatus,"status":status,"time":time})
    print(randomStatus, "time now is", time.ctime(), "", status)
    time.sleep(3)

