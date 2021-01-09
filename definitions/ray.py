class Ray():
    def __init__(self, point, direction, distance):
        self.point = point
        self.direction = direction
        self.distance = distance    

    def __str__(self):
        return f'Point:{self.point}, direction:{self.direction}, distance:{self.distance}'

    def calculateIntersection(self, objects):
