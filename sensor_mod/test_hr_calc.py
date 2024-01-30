import unittest
from sensor_mod import hr_hrcalc

class TestHrCalc(unittest.TestCase):

    def test_calc_hr_and_spo2(self):
        ir_data = [100, 200, 300, 400, 500, 600, 700,
                   800, 900, 1000, 1100, 1200, 1300,
                   1400, 1500, 1600, 1700, 1800, 1900, 2000]

        hr, hr_valid = hr_hrcalc.calc_hr_and_spo2(ir_data)

        expected_hr = -999
        expected_hr_valid = False
        self.assertEqual(hr, expected_hr)
        self.assertEqual(hr_valid, expected_hr_valid)

    # ran more tests to test the methods in hr_calc.py
    # def test_moving_average(self):
    #     signal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #     size = 3
    #     expected = [2, 3, 4, 5, 6, 7]
    #     self.assertEqual(hr_hrcalc.moving_average(signal, size), expected)

    # def test_find_peaks(self):
    #     dummy_ir = [60000, 70000, 60000, 90000, 100000, 90000, 60000, 70000, 60000]
    #     size = len(dummy_ir)
    #     min_height = 60000
    #     min_dist = 1
    #     max_num = 3
    #     # The expected result depends on the specific behavior of your find_peaks function
    #     # Replace 'expected' with the expected output for your dummy_ir data
    #     expected = ([], 0)
    #     self.assertEqual(hr_hrcalc.find_peaks(dummy_ir, size, min_height, min_dist, max_num), expected)

    def test_find_peaks_above_min_height1(self):
        x = [1, 2, 1]
        size = len(x)
        min_height = 1
        max_num = 3
        expected = ([1], 1)
        self.assertEqual(hr_hrcalc.find_peaks_above_min_height(x, size, min_height, max_num), expected)

    def test_find_peaks_above_min_height2(self):
        # test 2 border cases for function find_peaks_above_min_height
        x = [1, 2, 3]
        size = len(x)
        min_height = 1
        max_num = 3
        expected = ([], 0)
        self.assertEqual(hr_hrcalc.find_peaks_above_min_height(x, size, min_height, max_num), expected)

    def test_find_peaks_above_min_height3(self):
        x = [3, 2, 1]
        size = len(x)
        min_height = 1
        max_num = 3
        expected = ([0], 1)
        self.assertEqual(hr_hrcalc.find_peaks_above_min_height(x, size, min_height, max_num), expected)

    def test_find_peaks_above_min_height4(self):
        # test 1 border case more
        x = [1, 2, 3, 1]
        size = len(x)
        min_height = 3
        max_num = 3
        expected = ([], 0)
        self.assertEqual(hr_hrcalc.find_peaks_above_min_height(x, size, min_height, max_num), expected)


if __name__ == '__main__':
    unittest.main()