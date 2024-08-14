
import unittest
from typewise_alert import infer_breach  # Adjust this line based on the functions you need

class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertEqual(infer_breach(20, 50, 100), 'TOO_LOW')
        self.assertEqual(infer_breach(110, 50, 100), 'TOO_HIGH')
        self.assertEqual(infer_breach(75, 50, 100), 'NORMAL')

if __name__ == '__main__':
    unittest.main()
