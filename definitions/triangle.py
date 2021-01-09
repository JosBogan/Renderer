from .vectors import vectorFromPoints, Vector
from .point import Point


class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.vAB = vectorFromPoints(a, b)
        self.vAC = vectorFromPoints(a, c)
        self.vBC = vectorFromPoints(b, c)
        self.normal = self.calculateNormalSelf()
        self.dp = self.calculateDotProductSelf()


    def __str__(self):
        return f'{self.vAB}, {self.vAC} - {self.normal}'

    def calculateNormalSelf(self):
        return calculateCrossProduct(self.vAB, self.vAC)

    def calculateDotProductSelf(self):

        return self.vAB.x * self.vAC.x + self.vAB.y * self.vAC.y + self.vAB.z * self.vAC.z


def calculateDotProduct(a, b):

    dotProduct = a.x * b.x + a.y * b.y + a.z * b.z

    return dotProduct

def calculateCrossProduct(a, b):

    x = a.y * b.z - a.z * b.y
    y = -(a.x * b.z - a.z * b.x)
    z = a.x * b.y - a.y * b.x

    return Vector(x, y, z)

def calculateNormal(triangle):

    return calculateCrossProduct(triangle.vAB, triangle.vAC)

# a = Point(2, 5, 3)
# b = Point(1, 3, 7)
# c = Point(8, 1, 4)

# myTriangle = Triangle(a, b, c)

# print(myTriangle)