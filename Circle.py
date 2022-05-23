class Circle :
    def __init__(self, p1, p2, p3) :
        cal_circle(p1, p2, p3)
    
    def cal_circle(self, p1, p2, p3) :
        v1 = p3 - p2
        v2 = p3 - p1
        v3 = p2 - p1

        a = np.linalg.norm(v1)
        b = np.linalg.norm(v2)
        c = np.linalg.norm(v3)

        s = (a + b + c) / 2

        b1 = a*a * (b*b + c*c - a*a)
        b2 = b*b * (a*a + c*c - b*b)
        b3 = c*c * (a*a + b*b - c*c)

        w = np.cross(v1,v2)
        self.nornal = w / np.linalg.norm(w)
        self.radius = a*b*c / 4 / np.sqrt(s * (s - a) * (s - b) * (s - c))
        self.center = np.column_stack((p1, p2, p3)).dot(np.hstack((b1, b2, b3))) / (b1+b2+b3)
