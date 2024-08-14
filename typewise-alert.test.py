
import unittest
from typewise_alert import classify_temperature_breach

class TestTemperatureBreach(unittest.TestCase):
    def test_passive_cooling(self):
        self.assertEqual(classify_temperature_breach('PASSIVE_COOLING', -1), 'TOO_LOW')
        self.assertEqual(classify_temperature_breach('PASSIVE_COOLING', 36), 'TOO_HIGH')
        self.assertEqual(classify_temperature_breach('PASSIVE_COOLING', 20), 'NORMAL')

    def test_high_active_cooling(self):
        self.assertEqual(classify_temperature_breach('HI_ACTIVE_COOLING', -1), 'TOO_LOW')
        self.assertEqual(classify_temperature_breach('HI_ACTIVE_COOLING', 46), 'TOO_HIGH')
        self.assertEqual(classify_temperature_breach('HI_ACTIVE_COOLING', 25), 'NORMAL')

    def test_medium_active_cooling(self):
        self.assertEqual(classify_temperature_breach('MED_ACTIVE_COOLING', -1), 'TOO_LOW')
        self.assertEqual(classify_temperature_breach('MED_ACTIVE_COOLING', 41), 'TOO_HIGH')
        self.assertEqual(classify_temperature_breach('MED_ACTIVE_COOLING', 30), 'NORMAL')

if __name__ == '__main__':
    unittest.main()
