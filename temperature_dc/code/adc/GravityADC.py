# ----------------------------------------------------------------------
#
#    Temperature Monitoring (Basic solution) -- This digital solution enables, measures,
#    reports and records different  types of temperatures (contact, air, radiated)
#    so that the temperature conditions surrounding a process can be understood and 
#    taken action upon. Suppored sensors include 
#    k-type thermocouples, RTDs, air samplers, and NIR-based sensors.
#    The solution provides a Grafana dashboard that 
#    displays the temperature timeseries, set threshold value, and a state timeline showing 
#    the chnage in temperature. An InfluxDB database is used to store timestamp, temperature, 
#    threshold and status. 
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

from adc.DFRobot_ADS1115 import ADS1115


class ADC:
    def __init__(self, config):
        self.adc = ADS1115()
        self.channel = config['adc']['channel']
        self.ADCMax = 1024
        self.ADCVoltage = 1.024
        self.I2CAddress = config['adc'].get('i2c_address', 0x48)

    def sample(self):
        self.adc.set_addr_ADS1115(self.I2CAddress)  # See the physical switch on the module and change accordingly
        reading = self.adc.read_voltage(self.channel)['r']
        voltage = (reading / self.ADCMax * self.ADCVoltage)
        return voltage