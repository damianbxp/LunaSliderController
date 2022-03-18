import Slider_config
from Vector import *
from Servo import Servo


class Scara:
    def __init__(self, arm1_len:int = None, arm2_len:int = None, servo_pins:list = None):
        self.current_pos = Vector2(0, 0)

        # Scara arm lenght
        self.arm1_len = arm1_len
        self.arm2_len = arm2_len
        if self.arm1_len is None:
            self.arm1_len = Slider_config.arm1_len
        if self.arm2_len is None:
            self.arm2_len = Slider_config.arm2_len

        if servo_pins is None:
            servo_pins = Slider_config.servos_pins

        self.servos = [Servo(servo_pins[0], Slider_config.big_servo_limit, Slider_config.big_servo_pwm_range),
                       Servo(servo_pins[1], Slider_config.big_servo_limit, Slider_config.big_servo_pwm_range),
                       Servo(servo_pins[2], Slider_config.small_servo_limit, Slider_config.small_servo_pwm_range),
                       Servo(servo_pins[3], Slider_config.small_servo_limit, Slider_config.small_servo_pwm_range)]

    def fold(self):
        print(f"Scara folding")
        self.servos[0].set_angle(0)
        self.servos[1].set_angle(0)

    def set_pos(self, x: float, y: float):
        self.set_pos(Vector2(x,y))

    def set_pos(self, pos: Vector2):
        print(f"Scara position to {pos}")
        angles = self.calc_scara_IK(pos)

        self.servos[0].set_angle(angles[0])
        self.servos[1].set_angle(angles[1])

    def calc_scara_IK(self, pos: Vector2):
        """
        :param pos: Destination position
        :return: Tuple of angle for both servos
        """
        if pos.x == 0:
            pos.x = 0.000001

        theta2 = math.acos((pos.x ** 2 + pos.y ** 2 - self.arm1_len ** 2 - self.arm2_len ** 2) / (2 * self.arm1_len * self.arm2_len))
        theta1 = (math.atan(pos.y / pos.x) if pos.x!=0 else math.pi/2) - math.atan(
            (self.arm2_len * math.sin(theta2))
            / (self.arm1_len + self.arm2_len * math.cos(theta2)))

        theta1 = round(math.degrees(theta1))
        theta2 = round(math.degrees(theta2))

        print(f"SCARA Angles: {theta1}° {theta2}°")
        return [theta1, theta2]

    def look_at(self, target: Vector2):
        """
        :param target: look at target
        :return: Returns angle between -180° and 180°. 0° for point (0, y). Positive for clockwise offset
        """
        """
            TODO:
            - Add 3rd dimension
            - Currently angle is local. Take arm angle to calculations 
        """
        look_at_angle = round(math.degrees(math.atan2(target.x - self.current_pos.x, target.y - self.current_pos.y)))
        print(f"Look At angle: {look_at_angle}°")
        return look_at_angle
