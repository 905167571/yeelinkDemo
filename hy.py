#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
import requests
import json
import RPi.GPIO as GPIO        
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.IN)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
a=1
c=0
v=0
def blink(i):
 for num in range(1,10):
	GPIO.output(12,GPIO.HIGH)
	GPIO.output(8,GPIO.LOW)
	time.sleep(i)
	GPIO.output(12,GPIO.LOW)
	GPIO.output(8,GPIO.HIGH)
	time.sleep(i)
while a==1:
	s=GPIO.input(7)
	v=0
	#apiurl = 'http://api.yeelink.net/v1.1/device/352059/sensor/397316/datapoints'
	#apiheaders = {'U-ApiKey': 'ee9a77d9d6f9d4d22059be9adf656fac', 'content-type': 'application/json'}
	#payload = {'value': v}
	if s==0:
		blink(0.08)
		v=100
		apiurl = 'http://api.yeelink.net/v1.1/device/352059/sensor/397316/datapoints'
		apiheaders = {'U-ApiKey': 'ee9a77d9d6f9d4d22059be9adf656fac', 'content-type': 'application/json'}
		payload = {'value': v}
		r = requests.post(apiurl, headers=apiheaders, data=json.dumps(payload))
		print(GPIO.input(7))	
	c=c+1
	time.sleep(0.35)
	if c==100:
		apiurl = 'http://api.yeelink.net/v1.1/device/352059/sensor/397316/datapoints'
		apiheaders = {'U-ApiKey': 'ee9a77d9d6f9d4d22059be9adf656fac', 'content-type': 'application/json'}
		payload = {'value': v}		
		r = requests.post(apiurl, headers=apiheaders, data=json.dumps(payload))
		c=0	
	GPIO.output(12,GPIO.LOW)
	GPIO.output(8,GPIO.LOW)
	
