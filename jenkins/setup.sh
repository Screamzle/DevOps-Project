#1/bin/bash

# install apt dependencies
source venv/bin/activate
sudo apt-get update
sudo apt-get install python3-venv python3-pip python3 -y

# create and activate virtual enviromment
python3 -m -S venv venv

# install pip requirements
pip3 install -r requirements.txt

# docker login
docker login --username $DOCKER_HUB_CREDS_USR --password $DOCKER_HUB_CREDS_PSW