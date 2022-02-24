from ScaraController import Scara
import utime

s = Scara()

s.home()

utime.sleep(3)

s.set_pos(100.0, 100.0)
