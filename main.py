

#TODO(initial) - start initial code using smbus library, create first basic function for reading
# data from I2C on Pi
import smbus2
import time

# I2C address
sensor_address = 0x57

# mode change register
mode_change = 0x09

# instance of smbus
bus = smbus2.SMBus(1)

#initialize sensor
#TODO(step 2) - check wheter these adresses are correct with data sheet
bus.write.byte_data(sensor_address,0x09,0xff) # check wheter this is a reset or not
time.sleep(0.1)
bus.write.byte_data(sensor_address,0x09,0x03)

# read data from sensor, but is it continuous???
while True:
    data = bus.read_i2c_block_data(sensor_address,0x00,6)

    # what kind of data will i get and how to convert it to integer BPM?
    #TODO(step 3) - check what type of data do i get
    # and what the conversion will be like

    print(data)
    time.sleep(0.1)

def start_sensor(channel=1, address = 0x57):
    """
    Starts sensor
    """
    bus = smbus2.SMBus(channel)
    bus.write_block_data(address,mode_change,0x80)


def stop_sensor(channel=1, address = 0x57):
    """
    Stops sensor
    """
    bus = smbus2.SMBus(channel)
    bus.write_block_data(address, mode_change, 0x40)
    time.sleep(1)
