from machine import Pin, PWM
from LunaMath import lerp_1D, clamp


class Servo:
    def __init__(self, pin: int, max_angle: float, angle_PWM_range: tuple, freq=50):
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(freq)

        self.max_angle = max_angle
        self.angle_pwm_range = angle_PWM_range

        self.current_angle = 0

    def set_angle(self, angle: float):
        serwo_pwm = round(lerp_1D(self.angle_pwm_range, clamp(0, 1, angle / self.max_angle)))
        print(f"send to servo: {serwo_pwm}")
        self.pwm.duty_u16(serwo_pwm)
        self.current_angle = angle
