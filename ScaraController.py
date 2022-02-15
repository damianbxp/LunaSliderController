# from machine import Pin, PWM
from Vector import *


class Scara:
    def __init__(self):
        self.current_pos = Vector2(0, 0)

        self.a1 = 0
        self.a2 = 0

        self.servo_pins = {0, 0, 0, 0}

    def calc_Scara_IK(self, pos: Vector2):
        if pos.x == 0:
            pos.x = 0.000001

        theta2 = math.acos((pos.x ** 2 + pos.y ** 2 - self.a1 ** 2 - self.a2 ** 2) / (2 * self.a1 * self.a2))
        theta1 = math.atan(pos.y / pos.x) - math.atan(
            (self.a2 * math.sin(theta2))
            / (self.a1 + self.a2 * math.cos(theta2)))

        theta1 = round(math.degrees(theta1))
        theta2 = round(math.degrees(theta2))

        print(f"SCARA Angles: {theta1}° {theta2}°")
        return {theta1, theta2}

    def look_at(self, target:Vector2):
        '''
        :param target: look at target
        :return: Returns angle between -180° and 180°. 0° for point (0, y). Positive for clockwise offset
        '''
        """
            TODO:
            - Add 3rd dimension
            - Currently angle is local. Take arm angle to calculations 
        """
        #look_at_angle = round(math.degrees(math.atan2(target.y - self.current_pos.y, target.x - self.current_pos.x)))
        look_at_angle = round(math.degrees(math.atan2(target.x - self.current_pos.x, target.y - self.current_pos.y)))
        print(f"Look At angle: {look_at_angle}°")
        return look_at_angle