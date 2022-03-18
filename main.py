from MainController import Controller
from ScaraController import Scara
from Vector import Vector2
import utime


def setup(controller : Controller):
    print("Setting up")
    controller.scara = Scara(200,200,0)


    print("Setup completed")
    return controller

def loop():
    print("")


if __name__ == "main":
    setup()

    while True:
        loop()
