from ScaraController import Scara
from SliderController import Slider
from Vector import *
import utime


class Controller:
    def __init__(self, slider: Slider, scara: Scara):
        self.slider = slider
        self.scara = scara

    def move(self, new_pos: Vector3):
        self.scara.fold()
        utime.sleep(1)

        self.slider.move(Vector2(new_pos.x, new_pos.y))

        if new_pos.z != 0:
            self.scara.set_pos(Vector2(0, new_pos.z))

    def home(self):
        self.scara.fold()
        utime.sleep(1)
        self.slider.home()
