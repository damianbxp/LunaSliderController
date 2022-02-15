# from machine import Pin, PWM
from Vector import *


class Scara:
    def __init__(self):
        self.a1 = 0
        self.a2 = 0

        self.servo_pins = {0, 0, 0, 0}

    def calc_Scara_IK(self, pos: Vector2):
        theta2 = math.acos((pos.x ** 2 + pos.y ** 2 - self.a1 ** 2 - self.a2 ** 2) / (2 * self.a1 * self.a2))
        theta1 = math.atan(pos.y / pos.x) - math.atan(
            (self.a2 * math.sin(theta2)) / (self.a1 + self.a2 * math.cos(theta2)))

        theta1 = math.degrees(theta1)
        theta2 = math.degrees(theta2)

        print(f"SCARA Angles: {theta1}° {theta2}°")
        return {theta1, theta2}

