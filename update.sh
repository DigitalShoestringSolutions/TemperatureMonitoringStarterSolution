
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
echo "============================================================================"
echo "	Updating Application"
echo "============================================================================"
OLD_HEAD=$(git rev-parse HEAD)
echo current commit hash is $OLD_HEAD
echo stashing local changes
git stash
echo "fetching updates"
git pull --rebase origin
NEW_HEAD=$(git rev-parse HEAD)
if [ ! $OLD_HEAD = $NEW_HEAD ]
then
    echo new commit hash is $NEW_HEAD
	source hooks/update_hook.sh
fi
echo reapllying local changes
git stash pop
echo "============================================================================"
echo "	Update Complete"
echo "============================================================================"

