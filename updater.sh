#!/bin/bash
echo "Updater for PiCar - Ver. 0.01alpha"
echo "Please ensure that you are connected to the internet."
sleep 2
#Create update directory
mkdir ~/update
cd ~/update
#Download update file
wget -N https://github.com/LinuxMaya123/picar/releases/download/0.01alpha/picar_newest.tar.gz
echo "Update successfully downloaded."
echo "Unpacking update..."
tar -xzf picar*.tar.gz 
echo "Installing update..."
mkdir ~/picar_newest
mv ~/update/picar2/* ~/picar_newest
#Cleaning up
rm -R ~/update
echo "Update successfully installed."
#Doing some adverstising :)
echo "Please report every bug to picar.infoandbugs@gmail.com."
echo "Follow us on Twitter @picar_os!"

