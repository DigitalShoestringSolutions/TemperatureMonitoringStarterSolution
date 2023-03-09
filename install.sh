# ----------------------------------------------------------------------
#
#    Temperature Monitoring (Basic solution) -- This digital solution enables, measures,
#    reports and records different  types of temperatures (ambient, process, equipment)
#    so that the temperature conditions surrounding a process can be understood and 
#    taken action upon. This version can work for 4 types of temperature sensors (now)
#    which include k-type, RTD, ambient (AHT20), and NIR-based sensors. 
#    The solution provides a Grafana dashboard that 
#    displays the temperature timeseries, set threshold value, and a state timeline showing the chnage in temperature.
#    An InfluxDB database is used to store timestamp, temperature, threshold and status. 
#
#    Copyright (C) 2022  Shoestring and University of Cambridge
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see https://www.gnu.org/licenses/.
#
# ----------------------------------------------------------------------

sudo  apt-get update
sudo curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo groupadd docker
sudo usermod -aG docker pi
sudo newgrp docker
sudo apt-get install -y libffi-dev libssl-dev
sudo apt-get install -y python3 python3-pip
sudo apt-get remove python-configparser
sudo apt install docker-compose
pip3 install paho-mqtt

