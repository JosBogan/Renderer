from .triangle import calculateDotProduct
from .vectors import normaliseVector, Vector, vectorSubtract, vectorMultiply, vectorAdd

class Ray():
    def __init__(self, point, direction, distance):
        self.point = point
        self.direction = normaliseVector(vectorSubtract(point, direction))
        self.distance = distance
        self.hit = None

    def __str__(self):
        return f'Point:{self.point}, direction:{self.direction}, distance:{self.distance}'

    def calculateIntersection(self, objects):
        for x in objects:
            topHalf = 0 - calculateDotProduct(x.normal, self.point)
            bottomHalf = calculateDotProduct(x.normal, self.direction)
            
            t = topHalf / bottomHalf

            self.hit = vectorAdd(self.point, vectorMultiply(self.direction, t))