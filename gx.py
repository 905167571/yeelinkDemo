#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
import requests
import json
import RPi.GPIO as GPIO        
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.IN)
a=1
while a==1:
	v=GPIO.input(16)
	#apiurl = 'http://api.yeelink.net/v1.1/device/352059/sensor/396438/datapoints'
	#apiheaders = {'U-ApiKey': 'ee9a77d9d6f9d4d22059be9adf656fac', 'content-type': 'application/json'}
	#payload = {'value': v}
        #r = requests.post(apiurl, headers=apiheaders, data=json.dumps(payload))
	#if v==0:
		#blink(0.1)
	print(GPIO.input(16))  
		#payload = {'value': v}
		#r = requests.post(apiurl, headers=apiheaders, data=json.dumps(payload))
	#else:
		#GPIO.output(3,GPIO.LOW)
		#print(GPIO.input(22))
