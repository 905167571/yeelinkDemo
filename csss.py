#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
import requests
import json
import RPi.GPIO as GPIO        
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
a=1
while a==1:
	GPIO.output(25,GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(25,GPIO.LOW)
	time.sleep(0.5)
