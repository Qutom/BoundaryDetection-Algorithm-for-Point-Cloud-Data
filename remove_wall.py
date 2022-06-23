import numpy as np

"""
@Params : points : list
          boundary : list
@Return  : float
"""
def distance_cylinder(point, boundary) :
    return np.linalg.norm(point[:2] - boundary)

"""
@Params : points : numpy array
          boundary : numpy array
          raidus : float
@Return  : numpy array
"""
def remove_cylinder(points, boundary, radius) :
    for i in range(boundary.shape[0]) :
        length = points.shape[0]
        ind = []
        print(i)
        for j in range(length) :
            if distance_cylinder(points[j], boundary[i]) <= radius :
                ind.append(j)
        points = np.delete(points, ind, 0)

    return points

"""
@Params : points : numpy array
          boundary : numpy array
@Return  : numpy array
"""
def remove_wall(points, boundary, method="edge", radius=0.5, box_size=0.5) :
    if method == "edge" :
        #use edge algorithm
        pass
    if method == "box" :
        #use box algorithm
        pass
    if method == "cylinder" :
        result = remove_cylinder(points, boundary, radius=radius)

    return result