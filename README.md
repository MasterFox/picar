PiCar 0.03alpha
================

Control your radio-controlled car with some Python and Ryanteck Motor Controller Board!

We want you! 
============
You are interested in joining the PiCar project or you have some great ideas for features we should include? Feel free to contact me via picar.infoandbugs@gmail.com or on Twitter: @picar_os!

Setup
=====

1. Download the archive and execute updater.sh
2. Install and wire the motors of your RC-car with the Ryanteck MCB and plug it on your RasPi.
3. Connect lighting (if available) to pin 24 and GROUND.
4. Move to the "picar"-directory and execute start.py as root.
5. Type "selftest" to check the correct wiring of your motors and if needed change the wiring.
6. Report every bug to me! picar.infoandbugs@gmail.com

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

PiCar 0.03alpha
===============

+ Added lighting control engine "LumiX"
+ Removed syntax error in help()

PiCar 0.021alpha
================

+ Fixed bug #121020141714

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
