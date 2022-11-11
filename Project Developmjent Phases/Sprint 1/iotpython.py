import time
import sys
import ibmiotf.application
import ibmiotf.device
import random


organization = "hztfwg"
deviceType = "DeviceType1"
deviceId = "Deviceid1"
authMethod = "token"
authToken = "X4C_j!VzrEFM3Qt43L"

deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
deviceCli = ibmiotf.device.Client(deviceOptions)
deviceCli.connect()

def myCommandCallback(cmd):
    print("Message received from Ibm IOT Platform: %s" % cmd.data["command"])
    m=cmd.data['command']
    if(m=="motor on"):
        print("motor is Switched on")
    elif(m=="motor off"):
        print("motor is off")
    print(" ")

while True:
    soil =random.randint(0,100)
    temp =random.randint(-20,125)
    hum =random.randint(0,100)
    myData={'soil_moisture': soil,'temperature': temp,'humidity': hum}
    def myOnPublishCallback():
            print ("Published Temperature = %s C" % temp,"Moisture= %s" % soil, "Humidity = %s %%" % hum, "to IBM Watson")

    success = deviceCli.publishEvent("event_1", "json", data=myData, qos=0, on_publish=myOnPublishCallback)
    if not success:
        print("Not connected to IoTF")
    time.sleep(2)
    deviceCli.commandCallback = myCommandCallback

deviceCli.disconnect()
