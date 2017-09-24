#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
import requests
import json
import RPi.GPIO as GPIO        
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.IN)
GPIO.setup(25,GPIO.OUT)
a=1
c=0
v=0
def blink(i):
 for num in range(1,10):
	GPIO.output(25,GPIO.HIGH)
	time.sleep(i)
	GPIO.output(25,GPIO.LOW)
	time.sleep(i)
while a==1:
	s=GPIO.input(16)
	v=0
	#apiurl = 'http://api.yeelink.net/v1.1/device/352059/sensor/397312/datapoints'
	#apiheaders = {'U-ApiKey': 'ee9a77d9d6f9d4d22059be9adf656fac', 'content-type': 'application/json'}
	#payload = {'value': v}
    	#r = requests.post(apiurl, headers=apiheaders, data=json.dumps(payload))
	if s==1:
		blink(0.2)
		v=100
		apiurl = 'http://api.yeelink.net/v1.1/device/352059/sensor/397312/datapoints'
		apiheaders = {'U-ApiKey': 'ee9a77d9d6f9d4d22059be9adf656fac', 'content-type': 'application/json'}
		payload = {'value': v}
		r = requests.post(apiurl, headers=apiheaders, data=json.dumps(payload))
		time.sleep(2)
		print(GPIO.input(16))
	c=c+1
	time.sleep(0.2)
	if c==100:
		apiurl = 'http://api.yeelink.net/v1.1/device/352059/sensor/397312/datapoints'
		apiheaders = {'U-ApiKey': 'ee9a77d9d6f9d4d22059be9adf656fac', 'content-type': 'application/json'}	
		payload = {'value': v}
		r = requests.post(apiurl, headers=apiheaders, data=json.dumps(payload))
		c=0
		
	#else:
		#GPIO.output(3,GPIO.LOW)
		#print(GPIO.input(22))
