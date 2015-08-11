#!/usr/bin/python
__author__ = 'Leon Schwarze'
#Licensed under the GNU GPL V2 License
#(C) Leon Schwarze
#Adapted from Ryanteck LTD.

#importing some very important stuff
import time
import RPi.GPIO as GPIO
import sys
import subprocess

if sys.argv is None:
	startarg = False
else:
	startarg = True

print("PiCar 0.03beta - Developed by Leon Schwarze under GNU-GPL Version 2 license")
print("Welcome!")
print
print("Setting up GPIO pins...")

#Setup GPIO
GPIO.setmode(GPIO.BCM) #Set the pin numbers to Broadcom Mode

#Check if started in debug mode (will be include later; buggy!)
#if startarg:
#	if sys.argv[1] == "--debug":
#		GPIO.setwarnings(True) #Show all errors
	#if sys.argv[2] == "--debug":
	#	GPIO.setwarnings(True)
#	else:
#		GPIO.setwarnings(False) #Ignore any errors
#else:
#	pass

GPIO.setwarnings(False)
#Assign variables to pins
motor1_a = 17
motor1_b = 18
motor2_a = 22
motor2_b = 23
lighting = 24
usonic_trig = 25
usonic_echo = 27
navix_directions = []

#Setup the outputs
GPIO.setup(motor1_a,GPIO.OUT) #Set 17 as output (Motor 1 A)
GPIO.setup(motor1_b,GPIO.OUT) #Set 18 as output (Motor 1 B)
GPIO.setup(motor2_a,GPIO.OUT) #Set 22 as output (Motor 2 A)
GPIO.setup(motor2_b,GPIO.OUT) #Set 23 as output (Motor 2 B)
GPIO.setup(lighting, GPIO.OUT) #Set up lighting output
GPIO.setup(usonic_trig, GPIO.OUT)
GPIO.setup(usonic_echo, GPIO.IN)
print("[Done] Successful setup of GPIO pins.")
print("Starting LumiX engine...")
GPIO.output(lighting, True)
print("[Done]")
print("Setting up NaviX Comeback...")
navix_directions.append("end")
print("[Done]")
print
#Check if started in stealth mode (will be included later; buggy!)
#if startarg:
#	if sys.argv[1] == "--stealth":
#		print("Successful started in stealth-mode. WARNING: Visual feedback is not possible in stealth mode!")
#	else:
#		print("Starting lighting engine LumiX")
#		GPIO.output(lighting, True)
#else:
#	pass

#Define basic selftest
def selftest():
	print("Driving forwards...")
	GPIO.output(motor1_a, True)
	time.sleep(1)
	GPIO.output(motor1_a, False)
	print("[Done]")
	time.sleep(1)
	print("Driving backwards...")
	GPIO.output(motor1_b, True)
	time.sleep(1)
	GPIO.output(motor1_b, False)
	print("[Done]")
	time.sleep(1)
	print("Turning left...")
	GPIO.output(motor2_a, True)
	time.sleep(1)
	GPIO.output(motor2_a, False)
	print("[Done]")
	time.sleep(1)
	print("Turning right...")
	GPIO.output(motor2_b, True)
	time.sleep(1)
	GPIO.output(motor2_b, False)
	print("[Done]")
	time.sleep(1)
	print("Checking ultrasonic sensor...")
	navix()
	print "[Done] Current distance: %s" % (navix_distance)
	print("Checking lighting...")
	GPIO.output(lighting, True)
	time.sleep(1)
	GPIO.output(lighting, False)
	print("[Done] Lighting checked.")
	print("Checking network status...")
	proc = subprocess.Popen(["ping -c 2 www.google.com"], stdout = subprocess.PIPE, shell = True)
	if "0% packet loss" in proc.stdout.read():
		print "[Done] PiCar is online." 
	else:
		print("[Error] PiCar is offline.")

	print("Ended selftest without any errors")


#Define functions
def lumix(arg):
	if arg == "blink":
		GPIO.output(lighting, False)
		GPIO.output(lighting, True)
		GPIO.output(lighting, False)
		GPIO.output(lighting, True)
	elif arg == "stealth":
		GPIO.output(lighting, False)
	elif arg == "light":
		GPIO.output(lighting, True)
	else:
		pass

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
	time.sleep(0.5)
	GPIO.output(motor2_a, False)
	

def rightforwards(dur):
	GPIO.output(motor1_a, True)
	GPIO.output(motor2_b, True)
	time.sleep(dur)
	GPIO.output(motor1_a, False)
	time.sleep(0.5)
	GPIO.output(motor2_b, False)
	

def rightbackwards(dur):
	GPIO.output(motor1_b, True)
	GPIO.output(motor2_b, True)
	time.sleep(dur)
	GPIO.output(motor1_b, False)
	time.sleep(0.5)
	GPIO.output(motor2_b, False)
	

def leftbackwards(dur):
	GPIO.output(motor1_b, True)
	GPIO.output(motor2_a, True)
	time.sleep(dur)
	GPIO.output(motor1_b, False)
	time.sleep(0.5)
	GPIO.output(motor2_a, False)
	

def auto():
	i = 1
	navix()
	navix_validation = raw_input("Please confirm autonomous drive by pressing y or quit with q: ")
	while navix_validation != "q":
		if i < 6:
			if navix_distance > 50:
				print navix_distance
				forwards(1)
				i = i + 1
				navix()
			if navix_distance < 50:
				print navix_distance
				backwards(1)
				navix()
				print navix_distance
				while navix_distance < 70:
					backwards(1)
					navix()
					print navix_distance
				leftforwards(1.5)
				i = i + 1
				navix()
		if i == 6:
			navix_validation = raw_input("Please confirm autonomous drive by pressing y or quit with q: ")
			if navix_validation == "y":
				i = 1
				continue
			else:
				break  
	
def help():
	print("forwards - move your car forwards")
	print("backwards - move your car backwards")
	print("left forwards - move your car left forwards")
	print("right forwards - move your car right forwards")
	print("For turning backwards use the same pattern with backwards")
	print("selftest - for testing the correct wiring of your car")
	print("distance - shows the current distance to the next object using the ultrasonic sensor")
	print("stealth - the lighting is switched off")
	print("light - the lighting is switched on")
	print("auto - activating autonomous drive")
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

def update():
	print("Executing updater...")
	proc = subprocess.Popen("./updater.sh")
	print("Terminating PiCar. Please restart after updating process.")

def turnover():
	print("Turning over...")
	leftbackwards(1)
	time.sleep(1)
	rightforwards(1)
	time.sleep(1)
	leftbackwards(1)
	time.sleep(1)
	rightforwards(1)
	time.sleep(1)
	leftbackwards(1)
	time.sleep(1)
	rightforwards(1)
	time.sleep(1)
	leftbackwards(1)
	time.sleep(1)
	rightforwards(1)
	time.sleep(1)
	leftbackwards(1)
	time.sleep(1)
	rightforwards(1)
	print("[Done]")

def comeback():
	i = 0
	print(navix_directions)
	turnover()
	while navix_directions.pop() != "end":
		print(navix_directions)
		if navix_directions.pop() == "forwards":
			print(navix_directions.pop())
			forwards(1)
			time.sleep(1)
			i = i+1
		elif navix_directions.pop() == "backwards":
			print(navix_directions.pop())
			backwards(1)
			time.sleep(1)
			i = i+1
		elif navix_directions.pop() == "left forwards":
			print(navix_directions.pop())
			leftforwards(1)
			time.sleep(1)
			i = i+1
		elif navix_directions.pop() == "right forwards":
			print(navix_directions.pop())
			rightforwards(1)
			time.sleep(1)
			i = i+1
		elif navix_directions.pop() == "left backwards":
			print(navix_directions.pop())
			leftbackwards(1)
			time.sleep(1)
			i = i+1
		elif navix_directions.pop() == "right backwards":
			print(navix_directions.pop())
			rightbackwards(1)
			time.sleep(1)
			i = i+1
		else:
			pass


#Open command interface
command = raw_input("?")
while command != "quit":
	if command == "forwards":
		forwards(1)
		navix_directions.append("forwards")
		command = raw_input("?")
	elif command == "backwards":
		backwards(1)
		navix_directions.append("backwards")
		command = raw_input("?")
	elif command == "left forwards":
		leftforwards(1)
		navix_directions.append("right forwards")
		command = raw_input("?")
	elif command == "right forwards":
		rightforwards(1)
		navix_directions.append("left forwards")
		command = raw_input("?")
	elif command == "right backwards":
		rightbackwards(1)
		navix_directions.append("left backwards")
		command = raw_input("?")
	elif command == "left backwards":
		leftbackwards(1)
		navix_directions.append("right backwards")
		command = raw_input("?")
	elif command == "selftest":
		selftest()
		command = raw_input("?")
	elif command == "help":
		help()
		command = raw_input("?")
	elif command == "distance":
		navix()
		print navix_distance
		command = raw_input("?")
	elif command == "stealth":
		lumix("stealth")
		command = raw_input("?")
	elif command == "light":
		lumix("light")
		command = raw_input ("?")
	elif command == "auto":
		auto()
		command == raw_input("?")
	elif command == "update":
		update()
		break
	elif command == "turn over":
		turnover()
		command = raw_input("?")
	elif command == "come back":
		comeback()
		command = raw_input("?")
	else:
		lumix("blink")
		print("Invalid input, try again")
		command = raw_input("?")

print("Terminating PiCar...")
print("[Done]")
print
