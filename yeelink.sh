	sudo python /home/pi/yeelink/demo1/tempwd.py
	curl --request POST --data-binary @"/home/pi/yeelink/demo1/temper_data.txt" --header "U-ApiKey:ee9a77d9d6f9d4d22059be9adf656fac" --verbose http://api.yeelink.net/v1.1/device/352059/sensor/396091/datapoints
