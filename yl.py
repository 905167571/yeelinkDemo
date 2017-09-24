#!/usr/bin/env python -*- coding: UTF-8 -*-
import requests 
import json 
import time 
import smbus 
bus = smbus.SMBus(1)
address = 0x48
a=1
while a==1:
	bus.write_byte(address,0x40)
        bus.read_byte(address)
        temp = bus.read_byte(address)
	temp = 255-temp
	apiurl = ' http://api.yeelink.net/v1.1/device/352059/sensor/396760/datapoints'
	apiheaders = {'U-ApiKey': 'ee9a77d9d6f9d4d22059be9adf656fac', 'content-type': 'application/json'}
	payload = {'value':temp}
        r = requests.post(apiurl,headers=apiheaders,data=json.dumps(payload))
	print(payload)
