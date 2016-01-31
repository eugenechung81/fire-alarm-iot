import RPi.GPIO as GPIO
import time
import requests
import json
import pygame

#pins of concern
ledAlarmPin = 16
smokePin = 20
carbonMonoxidePin = 21
enterRoomSensorPin = 26
leaveRoomSensorPin = 19

#pin setup
GPIO.setmode(GPIO.BCM) #set pin allocation to broadcom type
GPIO.setup(ledAlarmPin, GPIO.OUT) # set led pin as output
GPIO.setup(smokePin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Fire button set as input with pullup
GPIO.setup(carbonMonoxidePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Carbon monoxide sensor set as input with pulldown
GPIO.setup(enterRoomSensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Enter button set as input with pullup
GPIO.setup(leaveRoomSensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Leave button set as input with pullup

# Initialize the led states
GPIO.output(ledAlarmPin, GPIO.LOW)

#initialize alarm state variables (mealy machine)
isFireAlarmOn = True # GPIO.LOW
isFireDetected = GPIO.LOW
isCarbonMonoxideAlarmOn = GPIO.LOW
isCarbonMonoxideDetected = GPIO.LOW

apartmentCount = 0

#initialize alarm sound
pygame.mixer.init()
pygame.mixer.music.load('FireAlarmSound.wav') 

print("Starting fire alarm , pres CTRL+c to exit")

try:
	while 1:
                if(not(GPIO.input(enterRoomSensorPin) == GPIO.HIGH)):
                        apartmentCount+=1
                        print "Person entered the apartment, there are now %i people in the apartment" % apartmentCount
                if(not(GPIO.input(leaveRoomSensorPin) == GPIO.HIGH)):
                        if(apartmentCount > 0):
                                apartmentCount-=1
                        print "Person left the apartment, there are now %i people in the apartment" % apartmentCount
		#get current fire and carbon monoxide detection states
                #print "The GPIO value for smokePin is :" + GPIO.input(smokePin)
		isFireDetected = not(GPIO.input(smokePin) == GPIO.HIGH)
		#print "Is Fire Detected :" + isFireDetected
		#print "The GPIO value for COPin is :" + GPIO.input(carbonMonoxidePin)
		isCarbonMonoxideDetected = GPIO.input(carbonMonoxidePin) == GPIO.LOW
		#print "Is C0 Detected :" + isCarbonMonoxideDetected
		
		#post update of fire or carbon monoxide status on change only
		#print isFireAlarmOn, isFireDetected
		if(isFireAlarmOn != isFireDetected):
			#current fire alarm state is different from last cycle, update in post
			strFireStatus = "FIRE" if isFireDetected else "NORMAL"
			print "changing status: %s" % strFireStatus
			r = requests.post(
				url="http://192.241.182.68:5000/status/livingroom",
				headers={'Content-type': 'application/json'},
				data=json.dumps({"occupancy": apartmentCount, "status": strFireStatus })
			)			
		
		if(isCarbonMonoxideAlarmOn != isCarbonMonoxideDetected):
			#current carbon monoxide alarm state is different from last cycle, update in post
                        print "changing carbon dectected: %s" % isCarbonMonoxideDetected
			r = requests.post(
				url="http://192.241.182.68:5000/status/livingroom",
				headers={'Content-type': 'application/json'},
				data=json.dumps({"occupancy": apartmentCount,"carbon_detected": isCarbonMonoxideDetected })
			)

		#play alarm if either fire or carbon detected
		# print "test2: %s %s" % (isFireDetected, isCarbonMonoxideDetected)
		if(isFireDetected or isCarbonMonoxideDetected):			
			pygame.mixer.music.play();	        #play sound
			GPIO.output(ledAlarmPin, GPIO.HIGH)	#flash light
			time.sleep(0.2)	#timer delay
			GPIO.output(ledAlarmPin, GPIO.LOW)	#stop light
		else:
			GPIO.output(ledAlarmPin, GPIO.LOW)	#stop light
			pygame.mixer.stop()	                #stop sound
			pygame.mixer.music.rewind()	        #set soundtrack to beginning

		#set last = current for fire and carbon alarm states
		isFireAlarmOn = isFireDetected
		isCarbonMonoxideAlarmOn = isCarbonMonoxideDetected
		
		time.sleep(0.2)	#timer delay
                
except KeyboardInterrupt: 
	GPIO.cleanup()
