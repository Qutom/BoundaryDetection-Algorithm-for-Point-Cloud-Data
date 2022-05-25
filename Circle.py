import numpy as np
import math

class Circle :
    def __init__(self, p1, p2, p3) :
        v1 = p3 - p2
        v2 = p3 - p1
        v3 = p2 - p1

        w = np.cross(v1, v2)
        if np.linalg.norm(w) < 10e-10 :
            print("Colinear")
            return

        a = np.linalg.norm(v1)
        b = np.linalg.norm(v2)
        c = np.linalg.norm(v3)

        s = (a + b + c) / 2

        b1 = a*a * (b*b + c*c - a*a)
        b2 = b*b * (a*a + c*c - b*b)
        b3 = c*c * (a*a + b*b - c*c)


        self.normal = w / np.linalg.norm(w)
        self.radius = a*b*c / 4 / np.sqrt(s * (s - a) * (s - b) * (s - c))
        self.center = np.column_stack((p1, p2, p3)).dot(np.hstack((b1, b2, b3))) / (b1+b2+b3)

    def print(self) :
        print(f'N : {self.normal} R : {self.radius} C : {self.center}')

    def to_array(self) :
        arr = [[self.radius * math.sin(i), self.radius * math.cos(i), 0] for i in range(0, 360, 10)]
        return np.array(arr)

