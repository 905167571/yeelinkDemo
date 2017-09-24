#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import RPi.GPIO as GPIO
import time
#程序结束后进行清理
# BOARD编号方式，基于BCM
GPIO.setmode(GPIO.BCM)
# 输出模式
GPIO.setup(24,GPIO.OUT)
# 设备URI，填写你的开关URL
apiurl = 'http://api.yeelink.net/v1.1/device/352059/sensor/396096/datapoints'
# 用户密码，API KEY，替换成你自己的
apiheaders = {'U-ApiKey': 'ee9a77d9d6f9d4d22059be9adf656fac'}
while True:
#发送请求
  r = requests.get(apiurl,headers=apiheaders)
  # 打印响应内容
  #print(r.text)
  # 转换为字典类型 请注意 2.7.4版本使用r.json(),我的是2.7.3
  led = r.json()
  # {'value':x} x=1打开状态，x=0关闭状态
  if led['value'] == 1:
    GPIO.output(24,GPIO.LOW)
  else:
    GPIO.output(24,GPIO.HIGH)
  # 延时5S
  time.sleep(1)
#程序结束后进行清理
