#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
import requests
import json        
import time
import smbus
a=1
bus = smbus.SMBus(1)
address = 0x48
self.result_var = DoubleVar()
while a==1:
	apiurl = 'http://api.yeelink.net/v1.1/device/352059/sensor/396438/datapoints'
	apiheaders = {'U-ApiKey': 'ee9a77d9d6f9d4d22059be9adf656fac', 'content-type': 'application/json'}
	payload = {'value': self.read_AIN0}
        r = requests.post(apiurl, headers=apiheaders, data=json.dumps(payload))
	self.aout_var = DoubleVar()
def read_AIN0(self):
            bus.write_byte(address,0x40)
            bus.read_byte(address)
            temp = bus.read_byte(address)
            self.result_var.set(temp)
            
