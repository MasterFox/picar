#PiCar Selftest
#Licensed under the GNU GPL V3 License
#(C) Leon Schwarze
#Adapted from Ryanteck LTD.
from time import sleep #We will need to sleep the code at points
import RPi.GPIO as GPIO #Import the GPIO library as GPIO

#Setup GPIO
GPIO.setmode(GPIO.BCM) # Set the numbers to Broadcom Mode
GPIO.setwarnings(False) # Ignore any errors

#Assign variables to pins
m1a = 17
m1b = 18
m2a = 22
m2b = 23

#Setup the outputs
GPIO.setup(m1a,GPIO.OUT) #Set 17 as output (Motor 1 A)
GPIO.setup(m1b,GPIO.OUT) #Set 18 as output (Motor 1 B)
GPIO.setup(m2a,GPIO.OUT) #Set 22 as output (Motor 2 A)
GPIO.setup(m2b,GPIO.OUT) #Set 23 as output (Motor 2 B)
print("Successful setup of GPIO pins")

#Start selftest
GPIO.output(m1a, True)#forwards
sleep(1)
GPIO.output(m1a, False)
sleep(1)
GPIO.output(m1b, True)#backwards
sleep(1)
GPIO.output(m1b, False)
sleep(1)
GPIO.output(m2a, True)#left
sleep(1)
GPIO.output(m2a, False)
sleep(1)
GPIO.output(m2b, True)#right
sleep(1)
GPIO.output(m2b, False)
print("Ended selftest without any errors")

#Define functions
def forwards():
	GPIO.output(m1a, True)
	sleep(1)
	GPIO.output(m1a, False)

def backwards():
	GPIO.output(m1b, True)
	sleep(1)
	GPIO.output(m1b, False)

def leftforwards():
	GPIO.output(m1a, True)
	GPIO.output(m2a, True)
	sleep(1)
	GPIO.output(m1a, False)
	GPIO.output(m2a, False)

def rightforwards():
	GPIO.output(m1a, True)
	GPIO.output(m2b, True)
	sleep(1)
	GPIO.output(m1a, False)
	GPIO.output(m2b, False)	

def rightbackwards():
	GPIO.output(m1b, True)
	GPIO.output(m2b, True)
	sleep(1)
	GPIO.output(m1b, False)
	GPIO.output(m2b, False)	

def leftbackwards():
	GPIO.output(m1b, True)
	GPIO.output(m2a, True)
	sleep(1)
	GPIO.output(m1b, False)
	GPIO.output(m2a, False)		

#Open command interface
command = raw_input("?")
while command != "quit":
	if command == "forwards":
		forwards()
		command = raw_input("?")
	if command == "backwards":
		backwards()
		command = raw_input("?")
	if command == "left forwards":
		leftforwards()
		command = raw_input("?")
	if command == "right forwards":
		rightforwards()	
		command = raw_input("?")
	if command == "right backwards":
		rightbackwards()
		command = raw_input("?")
	if command == "left backwards":
		leftbackwards()
		command = raw_input("?")
	else:
		print("Invalid input")
		command = raw_input("?")

print("Program ended successfully")

