from ScaraController import Scara
from Vector import Vector2
import utime

s = Scara()

s.home()
utime.sleep(2)
s.set_pos(Vector2(0,100))
utime.sleep(2)
s.set_pos(Vector2(0,50))
utime.sleep(2)
s.home()