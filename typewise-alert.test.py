import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import typewise_alert

class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertEqual(typewise_alert.infer_breach(20, 50, 100), 'TOO_LOW')
        self.assertEqual(typewise_alert.infer_breach(110, 50, 100), 'TOO_HIGH')
        self.assertEqual(typewise_alert.infer_breach(75, 50, 100), 'NORMAL')

if __name__ == '__main__':
    unittest.main()
