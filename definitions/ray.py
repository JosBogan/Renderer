from .triangle import calculateDotProduct, calculateCrossProduct
from .vectors import normaliseVector, Vector, vectorSubtract, vectorMultiply, vectorAdd, vectorFromPoints, vectorDivide, vectorNegative

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

    def calculateProjection(self, projectFrom, projectTo):

        topHalf = calculateDotProduct(projectFrom, projectTo)
        bottomHalf = calculateDotProduct(projectFrom, projectFrom)

        coefficient = topHalf / bottomHalf

        # print(f'coefficient:{coefficient}')


        intersect = vectorMultiply(projectTo, coefficient)

        # print(f'intersect{intersect}')

        vector = vectorFromPoints(projectFrom, intersect)

        # print(f'vectorV:{vector}')


        return vector


    def calculateBarycentricCoordinates(self, a, i, projectFrom, projectTo):

        print(projectFrom)
        print(projectTo)

        v = self.calculateProjection(projectFrom, projectTo)
    

        topHalf = calculateDotProduct(v, vectorFromPoints(a, i))
        bottomHalf = calculateDotProduct(v, projectTo)

        coords = 1 - (topHalf - bottomHalf)

        print(coords)
        # return coords


    def checkInTriangle(self, hit, triangle): # ! FIX ME!!

        vBA = vectorFromPoints(triangle.b, triangle.a)
        vBC = vectorFromPoints(triangle.b, triangle.c)

        self.calculateBarycentricCoordinates(triangle.a, hit, vBA, vBC)


    def calculateIntersection(self, objects):
        for x in objects:

            self.hit = self.calculatePlaneIntersection(x)

            self.checkInTriangle(self.hit, x)

            # print(self.hit)


    def getHit(self):
        return self.hit

    def getDistance(self):
        return self.hit

    def getDirection(self):
        return self.direction

    def getPoint(self):
        return self.point