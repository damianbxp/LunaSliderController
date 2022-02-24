import unittest
from LunaMath import *


class ClampTest(unittest.TestCase):
    def test_clamp(self):
        self.assertEqual(clamp(0, 1, 0.35), 0.35)
        self.assertEqual(clamp(0, 1, 1.35), 1)
        self.assertEqual(clamp(0, 1, -2), 0)


if __name__ == '__main__':
    unittest.main()
