PiCar 0.01alpha
===============

Control your radio-controlled car with some Python and Ryanteck Motor Controller Board!

Setup
=====

1. Download the archive and execute updater.sh
2. Install and wire the motors of your RC-car with the Ryanteck MCB and plug it on your RasPi
3. Move to the "picar"-directory and execute start.py
4. Report every bug to me! picar.infoandbugs@gmail.com

Usage
=====

After starting the program, you can use the following commands:

+ forwards - moves the car forwards
+ backwards - moves the car backwards
+ left /right forwards - makes your car turn left or right forwards
+ left /right backwards - makes your car turn left or right backwards
+ selftest - for checking the functionality of every motor
+ quit - quit the application
+ help - show command overview

PiCar 0.02alpha
===============

+ Added updater/installer
+ Removed the selftest at the program's beginning
+ Added command "help" for showing a short command overview
+ Added command "selftest" for testing your wiring


PiCar 0.01alpha
===============

+ Added motor control engine "MoviX"
+ Added simple command line interface
