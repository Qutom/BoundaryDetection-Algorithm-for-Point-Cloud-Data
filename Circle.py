import numpy as np
import math

class Circle :
    def __init__(self, p1, p2, p3) :
        v1 = np.dot(p2, p2.transpose())
        v2 = (np.dot(p1, p1.transpose()) - v1) / 2
        v3 = (v1 - (p3[0]**2) - (p3[1]**2)) / 2
        det = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])

        if abs(det) < 1.0e-10:
            self.radius = None
            self.center = None
            return

        # Center of circle
        cx = round((v2 * (p2[1] - p3[1]) - v3 * (p1[1] - p2[1])) / det, 5)
        cy = round(((p1[0] - p2[0]) * v3 - (p2[0] - p3[0]) * v2) / det, 5)

        self.center = np.array([cx,cy])
        self.radius = round(np.linalg.norm(p1-self.center), 5)

    def print(self) :
        print(f'R : {self.radius} C : {self.center}')

    def to_array(self) :
        arr = [[self.radius * math.sin(i), self.radius * math.cos(i)] for i in range(0, 360, 10)]
        return np.array(arr)

