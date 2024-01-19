import smbus2
import time

mode_change = 0x09

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

while True:
    print("start of the alogrithm")
    switch = input("enter y to start sensor, n to stop sensor")
    if switch == "y":
        start_sensor()
    elif switch == "n":
        stop_sensor()
    else:
        print("wrong input")
        print("end of the algorithm")
        break