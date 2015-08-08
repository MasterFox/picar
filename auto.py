#!/usr/bin/python
__author__ = 'Leon Schwarze'
#Licensed under the GNU GPL V2 License
#(C) Leon Schwarze
#Adapted from Ryanteck LTD.

#importing some very important stuff
import time
import RPi.GPIO as GPIO
import sys

if sys.argv is None:
	startarg = False
else:
	startarg = True

print("PiCar 0.03beta - Developed by Leon Schwarze under GNU-GPL Version 2 license")
print("Welcome")
print
print("Setting up GPIO pins...")

#Setup GPIO
GPIO.setmode(GPIO.BCM) #Set the pin numbers to Broadcom Mode

GPIO.setwarnings(False)
#Assign variables to pins
motor1_a = 17
motor1_b = 18
motor2_a = 22
motor2_b = 23
lighting = 24
usonic_trig = 25
usonic_echo = 27


#Setup the outputs
GPIO.setup(motor1_a,GPIO.OUT) #Set 17 as output (Motor 1 A)
GPIO.setup(motor1_b,GPIO.OUT) #Set 18 as output (Motor 1 B)
GPIO.setup(motor2_a,GPIO.OUT) #Set 22 as output (Motor 2 A)
GPIO.setup(motor2_b,GPIO.OUT) #Set 23 as output (Motor 2 B)
GPIO.setup(lighting, GPIO.OUT) #Set up lighting output
GPIO.setup(usonic_trig, GPIO.OUT)
GPIO.setup(usonic_echo, GPIO.IN)
print("Done.")


#Define functions
def forwards(dur):
	GPIO.output(motor1_a, True)
	time.sleep(dur)
	GPIO.output(motor1_a, False)

def backwards(dur):
	GPIO.output(motor1_b, True)
	time.sleep(dur)
	GPIO.output(motor1_b, False)

def leftforwards(dur):
	GPIO.output(motor1_a, True)
	GPIO.output(motor2_a, True)
	time.sleep(dur)
	GPIO.output(motor1_a, False)
	GPIO.output(motor2_a, False)

def rightforwards(dur):
	GPIO.output(motor1_a, True)
	GPIO.output(motor2_b, True)
	time.sleep(dur)
	GPIO.output(motor1_a, False)
	GPIO.output(motor2_b, False)

def rightbackwards(dur):
	GPIO.output(motor1_b, True)
	GPIO.output(motor2_b, True)
	time.sleep(dur)
	GPIO.output(motor1_b, False)
	GPIO.output(motor2_b, False)

def leftbackwards(dur):
	GPIO.output(motor1_b, True)
	GPIO.output(motor2_a, True)
	time.sleep(dur)
	GPIO.output(motor1_b, False)
	GPIO.output(motor2_a, False)

def help():
	print("forwards - move your car forwards")
	print("backwards - move your car backwards")
	print("left forwards - move your car left forwards")
	print("right forwards - move your car right forwards")
	print("For turning backwards use the same pattern with backwards")
	print("selftest - for testing the correct wiring of your car")
	print("help - show this overview")
	print("quit - quit the application")

def navix():
	GPIO.output(usonic_trig, False)
	time.sleep(2)
	GPIO.output(usonic_trig, True)
	time.sleep(0.00001)
	GPIO.output(usonic_trig, False)

	while GPIO.input(usonic_echo)==0:
  		pulse_start = time.time()

	while GPIO.input(usonic_echo)==1:
 		pulse_end = time.time()

 	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)

	global navix_distance
	navix_distance = distance
print
navix_validation = raw_input("Please confirm autonomous drive by pressing y or quit with q: ")
print
i = 1
navix()
while navix_validation != "q":
	if i < 11:
		if navix_distance > 50:
			print navix_distance
			forwards(1)
			i = i + 1
			navix()
		if navix_distance < 50:
			print navix_distance
			backwards(1)
			leftforwards(1.5)
			i = i + 1
			navix()
	if i == 11:
		navix_validation = raw_input("Please confirm autonomous drive by pressing y or quit with q: ")
		i = 1

print		
print("Program ended successfully")
