import math
import unittest
from ScaraController import Scara
from Vector import Vector2


class ScaraUnitTest(unittest.TestCase):
    def test_calc_IK(self):
        scara = Scara()
        scara.a1 = 100
        scara.a2 = 100
        self.assertEqual(scara.calc_Scara_IK(Vector2(0, math.sqrt(2) * scara.a1)), {45, 90})
        self.assertEqual(scara.calc_Scara_IK(Vector2(100, 100)), {0, 90})
        self.assertEqual(scara.calc_Scara_IK(Vector2(0, 100)), {30, 120})

    def test_look_at(self):
        scara = Scara()
        scara.current_pos = Vector2()

        self.assertEqual(scara.look_at(Vector2(10, 0)), 90)
        self.assertEqual(scara.look_at(Vector2(30, 30)), 45)
        self.assertEqual(scara.look_at(Vector2(20, -20)), 135)
        self.assertEqual(scara.look_at(Vector2(-15, 0)), -90)
        self.assertEqual(scara.look_at(Vector2(-15, 15)), -45)


if __name__ == '__main__':
    unittest.main()