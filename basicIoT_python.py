#!/usr/bin/env python
import datetime
import time
import urllib3
# disable InsecureRequestWarning if your are working without certificate verification
# see https://urllib3.readthedocs.org/en/latest/security.html
# be sure to use a recent enough urllib3 version if this fails
try:
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recent enough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')
# use with or without proxy
#http = urllib3.PoolManager()
http = urllib3.proxy_from_url('http://proxy.pal.sap.corp:8080')
# interaction for a specific Device instance - replace 1 with your specific Device ID
#url = 'https://iotmms_on_your_trial_system.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/1'
url = 'https://iotmmsi326045trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = '5f2d9b1c-7979-4ab3-a012-2a809ca6b797'
url = url +deviceID
headers = urllib3.util.make_headers()
# use with authentication
# please insert correct OAuth token
headers['Authorization'] = 'Bearer ' + 'd468433e2f2e4467266d32669456c44'
headers['Content-Type'] = 'application/json;charset=utf-8'
#I just started with random numbers, you can choose what ever you like
temperature =29
humidity =5
#just put in 3 rows into the DB
#for x in range(0, 3):
while True:
	current_time = int (time.time())
	timestamp =str (current_time)
	humidity=humidity+1
	temperature=temperature+1
	stringHumidity = str(humidity)
	stringTemperature = str(temperature)
	#print (str (current_time))
	# send message body and the corresponding payload layout that you defined in the IoT Services Cockpit
	# replace messagetypeid with id from IOT cockpit
	body='{"messageType":"6a61b4aa6b54048f704d","mode":"sync","messages":[{"Timestamp":'
	body=body+timestamp
	body = body +',"Humidity":'+stringHumidity
	body = body +',"Temperature":'+stringTemperature+'}]}'
	#print ("")
	#print (body)
	#r = http.urlopen('POST', url, body=body, headers=headers)
	#print ("")
	#print(r.status)
	#print(r.data)
	r = http.urlopen('GET', url, body=body, headers=headers)
	print("")
	print(r.status)
	print(r.data)

