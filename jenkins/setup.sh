#1/bin/bash

# install apt dependencies
source venv/bin/activate
sudo apt update
sudo apt install python3-venv python3-pip python3 -y

# create and activate virtual enviromment
python3 -m venv venv

# install pip requirements
pip3 install -r requirements.txt