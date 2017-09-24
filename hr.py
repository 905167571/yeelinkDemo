#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
import requests
import json
import RPi.GPIO as GPIO        
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN)
a=1
s=0
sv=0
while a==1:
	v=GPIO.input(27)
	apiurl = 'http://api.yeelink.net/v1.1/device/352059/sensor/396759/datapoints'
	apiheaders = {'U-ApiKey': 'ee9a77d9d6f9d4d22059be9adf656fac', 'content-type': 'application/json'}
	#for num in range(1,50):
	if v==0:
		s=s+1
			#time.sleep(0.01)
	sv=sv+1  
	payload = {'value': s}
	time.sleep(0.01)
	if sv==100:
		time.sleep(10)
		r = requests.post(apiurl, headers=apiheaders, data=json.dumps(payload))
		sv=0
		s=0
	print(s,sv)
