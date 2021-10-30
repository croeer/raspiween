import RPi.GPIO as GPIO
import time
import requests
import json
import os
import random
#from playsound import playsound
import threading
 
SENSOR_PIN = 23
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
 
hue_user = os.environ['HUE_USER']
hue_ip = "192.168.178.33"

payload = {"on":False}
headers = {'content-type': 'application/json'}
r = requests.put("http://"+hue_ip+"/api/"+hue_user+"/lights/1/state", data=json.dumps(payload), headers=headers)
effect_time = 10 # time in 100*ms

def fire_effect():
	no_loops = random.randint(5,8)
	for i in range(1,no_loops):
		hue = random.randint(1,6000)
		bri = random.randint(10,254)
		#print(hue, bri)

		payload = {"on":True,"bri": bri,"sat": 254,"hue": hue,"transitiontime":effect_time}
		r = requests.put("http://"+hue_ip+"/api/"+hue_user+"/lights/1/state", data=json.dumps(payload), headers=headers)
		#print(r.content)
		time.sleep(effect_time * 1.1 / 10)

	payload = {"on":False,"transitiontime":effect_time}
	r = requests.put("http://"+hue_ip+"/api/"+hue_user+"/lights/1/state", data=json.dumps(payload), headers=headers)


def mein_callback(channel):
	soundFile = random.randrange(1,5)
	print('Es gab eine Bewegung! Spiele Sound ' + str(soundFile))
	#playsound('sounds/sound' + str(soundFile) + '.wav')
	fire_thread = threading.Thread(target=fire_effect, name="Fire Effect Thread")
	fire_thread.start()
	soundfile = 'sounds/sound' + str(soundFile) + '.wav'
	os.system(' aplay -D bluealsa:DEV=00:1D:DF:6E:F5:C3,PROFILE=a2dp ' + soundfile)
 
try:
	GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=mein_callback)
	while True:
		time.sleep(100)
except KeyboardInterrupt:
	print "Beende..."
GPIO.cleanup()
