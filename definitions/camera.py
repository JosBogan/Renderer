class Camera():
    def __init__(self, near, far, point):
        self.point = point,
        self.near_frustum = near,
        self.far_frustum = far
