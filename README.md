PiCar 0.3beta
=============

Control your radio-controlled car with some Python and Ryanteck Motor Controller Board! Let it drive through an area completely autonomous!

Setup
=====

1. Download the archive and execute updater.sh
2. Install and wire the motors of your RC-car with the Ryanteck MCB and plug it on your RasPi.
3. Connect lighting (if available) to pin 24 and GROUND.
4. Move to the "picar"-directory and execute start.py as root.
5. Type "selftest" to check the correct wiring of your motors and if needed change the wiring.
6. Report every bug to me! picar.infoandbugs@gmail.com
7. To enable the experimental features remove the '#' before the code parts marked as experimental. USAGE AT YOUR OWN RISK!

Usage
=====

After starting the program, you can use the following commands:

+ forwards - moves the car forwards
+ backwards - moves the car backwards
+ left /right forwards - makes your car turn left or right forwards
+ left /right backwards - makes your car turn left or right backwards
+ selftest - for checking the functionality of every motor
+ distance - shows the current distance to the next object using the ultrasonic sensor
+ stealth - the lighting is switched off
+ light - the lighting is switched on
+ auto - activating autonomous drive
+ quit - quit the application
+ help - show command overview
+ update - starts update.sh
+ turn over - the car turns by 180°
+ come back - the car comes back to its starting point
+ clear directions - clears the cache of NaviX Comeback 
+ network status - checks if PiCar is online

Autonomous drive
================

Just execute $ cd picar && sudo python auto.py

PiCar 0.3beta
=============

+ Migrated auto.py into start.py
+ Enabled autonomous drive
+ Added NaviX Comeback: PiCar now returns to you, when you want it to!
+ Added NaviX Netstat: PiCar checks it's internet connection at startup
+ Improved startup messages
+ System messages now have the same format
+ ...and many, many bugfixes!

PiCar 0.2beta
=============

+ Added Lumix engine with awesome new features
+ Lighting can now be switched on and off
+ LumiX engine provides visual feedback in case of errors
+ Added command "distance" for printing out the distance to an object detected by the ultrasonic sensor
+ Added command "stealth" and "light" for switching the lighting on and off
+ Fixed bug #1912142116 (#11)

PiCar 0.1beta
=============

+ Added automotive drive module (NaviX 0.1beta; auto.py) CAUTION: THIS MODULE CAN END UP IN AN INFINITE LOOP! PLEASE USE WITH CARE!
+ Added NaviX to selftest


PiCar 0.04alpha
===============

+ Renamed internal variables because of development guideline
+ EXPERIMENTAL: Added 'stealth'-mode
+ EXPERIMENTAL: Added 'debug'-mode

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
