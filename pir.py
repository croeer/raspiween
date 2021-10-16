import RPi.GPIO as GPIO
import time
from playsound import playsound
 
SENSOR_PIN = 23
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
 
def mein_callback(channel):
	print('Es gab eine Bewegung!')
	# playsound('Music/Baal/attack1.wav')
 
try:
	GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=mein_callback)
	while True:
		time.sleep(100)
except KeyboardInterrupt:
	print "Beende..."
GPIO.cleanup()
