# -*- coding: utf-8 -*- 
import requests 
import json
import time
var=1
while	var==1:
# 打开文件 
	file = open("/sys/bus/w1/devices/28-000006c54d62/w1_slave") 
# 读取结果，并转换为浮点数 
	temp = float(file.read()) / 1000 
# 关闭文件 
	file.close() 
# 向控制台打印结果 
	print "temp : %.1f" %temp 

# 设备URI 
	apiurl = 'http://api.yeelink.net/v1.1/device/352059/sensor/396091/datapoints' 
# 用户密码, 指定上传编码为JSON格式 
	apiheaders = {'U-ApiKey': 'ee9a77d9d6f9d4d22059be9adf656fac', 'content-type': 'application/json'} 
# 字典类型数据，在post过程中被json.dumps转换为JSON格式字符串 {"value": 48.123} 
	payload = {'value': temp} 
#发送请求 
	r = requests.post(apiurl, headers=apiheaders, data=json.dumps(payload)) 

# 打印返回码
	#print "response status: %d" %r.status_code
