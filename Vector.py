import math


class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"X {self.x} Y {self.y}"

    def __len__(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float):
        return Vector2(self.x * other, self.y * other)

    def __round__(self, n=None):
        return Vector2(round(self.x), round(self.y))


class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"X {self.x} Y {self.y} Z {self.z}"

    def __len__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __round__(self, n=None):
        return Vector3(round(self.x), round(self.y), round(self.z))