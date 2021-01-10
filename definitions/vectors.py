class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.magnitude = self.calculateMagnitude(x, y, z)

    def __str__(self):
        return f'x:{self.x}, y:{self.y}, z:{self.z}, magnitute:{self.magnitude}'

    def calculateMagnitude(self, x, y, z):
        return ((x*x) + (y*y) + (z*z)) ** 0.5


def vectorAdd(a, b):
    x = a.x + b.x
    y = a.y + b.y
    z = a.z + b.z
    return Vector(x, y, z)

def vectorSubtract(a, b):
    x = a.x - b.x
    y = a.y - b.y
    z = a.z - b.z
    return Vector(x, y, z)

def vectorMultiply(v, m):
    x = v.x * m
    y = v.y * m
    z = v.z * m
    return Vector(x, y, z)


def vectorDivide(v, d):
    x = v.x / d
    y = v.y / d
    z = v.z / d
    return Vector(x, y, z)


def normaliseVector(v):
    x = v.x / v.magnitude
    y = v.y / v.magnitude
    z = v.z / v.magnitude
    return Vector(x, y, z)


def vectorFromPoints(a, b):

    x = b.x - a.x
    y = b.y - a.y
    z = b.z - a.z
    return Vector(x, y, z)

def vectorNegative(a):
    return Vector(-a.x, -a.y, -a.z)