#!/bin/bash

sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo apt install git
sudo rm -r pid-led-ldr-with-RPI
git clone https://github.com/manhoosbilli1/pid-led-ldr-with-RPI.git
sudo rm -r project
cp -r pid-led-ldr-with-RPI project
cd project
pip install -r req.txt
sudo rm -r pid-led-ldr-with-RPI
echo -e "\n\n\n\n\n You are all done. now just type switch to 'project' directory by cd project and type 'python script.py' and you will see output" 
echo "Enjoy! good bye. "

