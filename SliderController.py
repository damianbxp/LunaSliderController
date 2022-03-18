from Vector import Vector2
from machine import Pin
import Slider_config


class Slider:
    def __init__(self, motor_x_pin: int = None, motor_y_pin: int = None, endstop_pins: list = None, steps_per_mm: tuple = None):
        self.current_pos = Vector2()
        self.steps_per_mm = Slider_config.steps_per_mm if steps_per_mm is None else steps_per_mm

        # set endstop pins
        self.endstop_pins = Slider_config.endstop_pins if endstop_pins is None else endstop_pins

        # stepper motor pins
        self.motor_x = Slider_config.x_motor if motor_x_pin is None else motor_x_pin
        self.motor_y = Slider_config.y_motor if motor_y_pin is None else motor_y_pin

    def move(self, new_pos: Vector2):
        print(f"Moving from {self.current_pos} to {new_pos}")

    def home(self):
        print(f"Homing")
        while self.endstop_check(0):
            self.make_step(self.motor_x, -1)
        while self.endstop_check(2):
            self.make_step(self.motor_y, -1)

        self.current_pos = Vector2()

    def make_steps(self, x_steps: int, y_steps: int):
        x_dir = self._get_direction(x_steps)
        y_dir = self._get_direction(y_steps)

        x_steps = abs(x_steps)
        y_steps = abs(y_steps)

        for i in range(max(x_steps, y_steps)):
            if self.endstop_check():
                if i <= x_steps:
                    self.current_pos.x += 1/self.steps_per_mm * x_dir
                if i <= y_steps:
                    self.current_pos.y += 1/self.steps_per_mm * y_dir
            break


    def endstop_check(self, endstop_index):
        return Pin(self.endstop_pins[endstop_index], Pin.OUT).value()

    def endstop_check(self):
        for pin in self.endstops_pins:
            if Pin(pin, Pin.OUT).value() == 1:
                return False
        return True

    def get_endstops(self):
        endstops = []
        for pin in self.endstop_pins:
            endstops.append((pin, Pin(pin, Pin.OUT).value()))

        return endstops

    def _get_direction(self, steps):
        if steps > 0:
            return 1
        elif steps < 0:
            return -1
        else:
            return 0
