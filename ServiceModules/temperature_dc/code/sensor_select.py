
#import math                                # Not used currently
from smbus2 import SMBus
#from mlx90614 import MLX90614              # imported below when class is created
#from w1thermsensor import W1ThermSensor    # imported below when class is created
#import max6675                             # Not used currently
#import MAX31865                            # imported below when class is created
#import adafruit_ahtx0                      # imported below when class is created
#import board                               # imported below when class is created
import logging
import importlib
#import serial                              # imported below when class is created
import json
import time

# import sys
# sys.path.append(docker exec -it )
# from DFRobot_MAX31855 import *

logger = logging.getLogger("main.measure.sensor")


#adc_module = "DFRobot_MAX31855"
#try:
#    local_lib = importlib.import_module(f"adc.{adc_module}")
#    logger.debug(f"Imported {adc_module}")
#except ModuleNotFoundError as e:
#    logger.error(f"Unable to import module {adc_module}. Stopping!!")






class k_type:
    # https://github.com/DFRobot/DFRobot_MAX31855/tree/main/raspberrypi/python
    def __init__(self):
        import adc.DFRobot_MAX31855 as DFRobot_MAX31855
        self.I2C_1       = 0x01
        self.I2C_ADDRESS = 0x10
        #Create MAX31855 object
        #self.max31855 = local_lib.DFRobot_MAX31855(self.I2C_1 ,self.I2C_ADDRESS)
        self.max31855 = DFRobot_MAX31855(self.I2C_1 ,self.I2C_ADDRESS)


    def ambient_temp(self):
        logger.info("TemperatureMeasureBuildingBlock- k-type started")
        return self.max31855.read_celsius()



class MLX90614_temp:
    def __init__(self):
        from mlx90614 import MLX90614
        self.bus = SMBus(1)
        self.sensor=MLX90614(self.bus,address=0x5a)

    def ambient_temp(self):
        logger.info("TemperatureMeasureBuildingBlock- MLX90614_temp started")
        return self.sensor.get_amb_temp()

    def object_temp(self):
        return self.sensor.get_obj_temp()



class sht30:
    def __init__(self):
        self.bus = SMBus(1)
        self.bus.write_i2c_block_data(0x44, 0x2C, [0x06])
        time.sleep(0.5)
        self.data = self.bus.read_i2c_block_data(0x44, 0x00, 6)

    def ambient_temp(self):
        logger.info("TemperatureMeasureBuildingBlock- SHT30 started")
        self.temp = self.data[0] * 256 + self.data[1]
        return -45 + (175 * self.temp / 65535.0)



class W1Therm:
    def __init__(self):
        from w1thermsensor import W1ThermSensor
        self.sensor = W1ThermSensor()


    def ambient_temp(self):
        logger.info("TemperatureMeasureBuildingBlock- w1therm started")
        return self.sensor.get_temperature()



class PT100_arduino:

    def __init__(self):
        import serial
        self.ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)

    def ambient_temp(self):
        logger.info("TemperatureMeasureBuildingBlock- PT100_arduino started")
        with self.ser as ser:
            if ser.isOpen():
                ser.flushInput()
                time.sleep(0.5)
                data_string = ser.readline().decode('utf-8').strip()
                data = json.loads(data_string)
                self.reading = data["T"]
        return self.reading

    def close(self):
        self.ser.close()


class PT100_raspi:

    def __init__(self):
        import adc.MAX31865 as MAX31865
        self.MyMax = MAX31865.max31865()
        self.MyMax.set_config(VBias=1, continous=1, filter50Hz=1)
        self.MyRTD = MAX31865.PT_RTD(100)

    def ambient_temp(self):
        logger.info("TemperatureMeasureBuildingBlock- PT100_raspi started")
        return self.MyRTD(self.MyMax())

    def close(self):
        self.MyMax.spi.close()


class PT100_raspi_sequentmicrosystems_HAT:

    def __init__(self):
        import adc.SequentMicrosystemsRTDHAT as RTDHAT
        self.RTD_ADC = RTDHAT

    def ambient_temp(self):
        return self.RTD_ADC.get_poly5(0, 6) # hard coding first layer, channel "RTD6". To be made configurable.


class aht20:
    def __init__(self):
        import board
        import adafruit_ahtx0
        # self.bus = SMBus(1)
        # self.sensor=adafruit_ahtx0.AHTx0(self.bus,address=0x38)
        i2c = board.I2C()
        self.sensor = adafruit_ahtx0.AHTx0(i2c)

    def ambient_temp(self):
        logger.info("TemperatureMeasureBuildingBlock- aht20 started")
        return self.sensor.temperature
