
from hr_max30102 import MAX30102
import hr_hrcalc
import threading
import time
import numpy as np
from hr_plot import plot_hr


class HeartRateMonitor(object):
    """
    A class that encapsulates the max30102 device into a thread
    """

    LOOP_TIME = 0.01

    def __init__(self):
        self.bpm = 0
        self.isSensor = False
        self.bpm_readings = []
        self.result = 0

    def run_sensor(self):
        sensor = MAX30102()
        ir_data = []
        red_data = []
        bpms = []
        sensor_output_sum = 0


        while not self._thread.stopped:
            num_bytes = sensor.get_data_present()
            if num_bytes > 0:
                while num_bytes > 0:
                    red, ir = sensor.read_fifo()
                    num_bytes -= 1
                    ir_data.append(ir)
                    red_data.append(red)
                    sensor_output_sum += ir

                while len(ir_data) > 100:
                    ir_data.pop(0)
                    red_data.pop(0)

                if len(ir_data) == 100:
                    bpm, valid_bpm = hr_hrcalc.calc_hr_and_spo2(ir_data, red_data)
                    if valid_bpm:
                        bpms.append(bpm)
                        while len(bpms) > 4:
                            bpms.pop(0)
                        self.bpm = np.mean(bpms)
                        self.bpm_readings.append(self.bpm)
                        if (np.mean(ir_data) < 50000 and np.mean(red_data) < 50000):
                            self.bpm = 0
        sensor.shutdown()

    def start_sensor(self):
        self.bpm_readings = []
        self._thread = threading.Thread(target=self.run_sensor)
        self._thread.stopped = False
        self.isSensor = True
        self._thread.start()

    def stop_sensor(self, timeout=2.0):
        self._thread.stopped = True
        self.bpm = 0
        self.isSensor = False
        self._thread.join(timeout)
        print(self.bpm_readings)  # Add this line
        fig= plot_hr(self.bpm_readings)
        self.result = np.mean(self.bpm_readings)

        return self.result, fig

