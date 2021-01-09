from .triangle import calculateDotProduct, calculateCrossProduct
from .vectors import normaliseVector, Vector, vectorSubtract, vectorMultiply, vectorAdd, vectorFromPoints

class Ray():
    def __init__(self, point, direction, distance):
        self.point = point
        self.direction = normaliseVector(vectorSubtract(point, direction))
        self.distance = distance
        self.hit = None

    def __str__(self):
        return f'Point:{self.point}, direction:{self.direction}, distance:{self.distance}, hit:{self.hit}'


    def calculatePlaneIntersection(self, x):
        d = calculateDotProduct(x.normalisedNormal, x.a)

        topHalf = d - calculateDotProduct(x.normalisedNormal, self.point)
        bottomHalf = calculateDotProduct(x.normalisedNormal, self.direction)
        
        t = topHalf / bottomHalf

        return vectorAdd(self.point, vectorMultiply(self.direction, t))

    def checkInTriangle(self, hit, triangle): # ! FIX ME!!

        vAB = vectorFromPoints(triangle.b, triangle.a)
        vBC = vectorFromPoints(triangle.c, triangle.b)
        vCA = vectorFromPoints(triangle.a, triangle.c)

        if calculateDotProduct(calculateCrossProduct(vAB, vectorSubtract(hit, triangle.a)), triangle.normalisedNormal) >= 0:
            return False
        if calculateDotProduct(calculateCrossProduct(vBC, vectorSubtract(hit, triangle.a)), triangle.normalisedNormal) >= 0:
            return False
        if calculateDotProduct(calculateCrossProduct(vCA, vectorSubtract(hit, triangle.a)), triangle.normalisedNormal) >= 0:
            return False
        return True


    def calculateIntersection(self, objects):
        for x in objects:

            self.hit = self.calculatePlaneIntersection(x)

            did_hit = self.checkInTriangle(self.hit, x)

            print(did_hit)

            # d = calculateDotProduct(x.normalisedNormal, x.a)


            # topHalf = d - calculateDotProduct(x.normalisedNormal, self.point)
            # bottomHalf = calculateDotProduct(x.normalisedNormal, self.direction)
            
            # t = topHalf / bottomHalf


            # self.hit = vectorAdd(self.point, vectorMultiply(self.direction, t))

    def getHit(self):
        return self.hit

    def getDistance(self):
        return self.hit

    def getDirection(self):
        return self.direction

    def getPoint(self):
        return self.point