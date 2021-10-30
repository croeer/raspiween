import RPi.GPIO as GPIO
import time
import requests
import json
import os
import random
#from playsound import playsound
 
SENSOR_PIN = 23
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
 
hue_user = os.environ['HUE_USER']
hue_ip = "192.168.178.33"

payload = {"on":False}
headers = {'content-type': 'application/json'}
r = requests.put("http://"+hue_ip+"/api/"+hue_user+"/lights/1/state", data=json.dumps(payload), headers=headers)

def mein_callback(channel):
	soundFile = random.randrange(1,5)
	print('Es gab eine Bewegung! Spiele Sound ' + str(soundFile))
	#playsound('sounds/sound' + str(soundFile) + '.wav')
	soundfile = 'sounds/sound' + str(soundFile) + '.wav'
	os.system(' aplay -D bluealsa:DEV=00:1D:DF:6E:F5:C3,PROFILE=a2dp ' + soundfile)
 
try:
	GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=mein_callback)
	while True:
		time.sleep(100)
except KeyboardInterrupt:
	print "Beende..."
GPIO.cleanup()
