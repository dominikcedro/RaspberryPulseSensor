import smbus
import time

class MAX30102:
    # Constants and methods from the original script...

    def control_led(self, state):
        """
        Control the sensor LED state.

        Parameters:
            state (bool): True to turn the LED on, False to turn it off.
        """
        # Assuming you have a register for controlling the LED state
        LED_CONTROL_REG = 0xXYZ  # Replace with the actual register address

        # Read the current register value
        current_reg_value = self.bus.read_byte_data(self.I2C_ADDRESS, LED_CONTROL_REG)

        # Modify the appropriate bit to control the LED
        if state:
            # Turn the LED on
            modified_reg_value = current_reg_value | 0x01
        else:
            # Turn the LED off
            modified_reg_value = current_reg_value & ~0x01

        # Write the modified value back to the register
        self.bus.write_byte_data(self.I2C_ADDRESS, LED_CONTROL_REG, modified_reg_value)

if __name__ == "__main__":
    sensor = MAX30102()
    sensor.setup()

    try:
        while True:
            red, ir = sensor.read_sensor()
            print(f"Red: {red}, IR: {ir}")

            user_input = input("Do you want to turn the LED on (y) or off (n)? ")
            if user_input.lower() == "y":
                sensor.control_led(True)
            elif user_input.lower() == "n":
                sensor.control_led(False)
            else:
                print("Invalid input. Please enter 'y' to turn the LED on or 'n' to turn it off.")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nExiting the program.")
