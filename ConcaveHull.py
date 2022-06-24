import numpy as np
import matplotlib.pyplot as plt
import sklearn.neighbors as NearestNeighbors

def is_same_point(p1, p2) :
    return (p1[0] == p2[0]) and (p1[1] == p2[1])

#sort neightbors in descending order of right-hand term
def sort_by_angle(center, neighbors, prevAngle) :
    pass

#cal angle between two point
def angle(p1, p2) :
    pass

#check intersect
def is_intersect(...) :
    pass

def concavehull(input_points, k=3) :
    k = max(k,3)
    points = np.unique(input_points, axis=0)

    points_length = points.shape[0]
    if points_length < 3 :
        print("points must be 3>")
        return None
    if points_length == 3 :
        return points

    k = min(k, points_length)

    knn = NearestNeighbors(n_neighbors=k).fit(points)
    distances, indices = knn.kneighbors(points)

    #find minYpoint
    min_y_ind = np.argmin(points[:, 1])
    start_point = points(min_y_ind)
    points = np.delete(points, min_y_ind)
    current_point = start_point

    hull = [current_point]
    prev_angle = 0
    step = 2

    while (not is_same_point(current_point, start_point) or step == 2) and points.shape[0] > 0:
        if step == 5 :
            points.append(start_point)

        #current point에 대한 neighbor 구하기
        neighbors = None
        c_point = sort_by_angle(current_point, neighbors, prev_angle)
        c_point_length = c_point.shape[0]
        its = True
        i = 0

        while its and i < c_point_length :
            i += 1
            if is_same_point(c_point[i], start_point) :
                last_point = 1
            else
                last_point = 0
            j = 2

            its = False
            hull_length = len(hull)
            while not its and j < (hull_length - last_point) :
                #intersection 체크
                its = is_intersect()
                j += 1

        if its :
            return concavehull(points, k+1)

        current_point = c_point[i]
        hull.append(current_point)
        prev_angle = angle(hull[step], hull[step-1])
        step += 1

    #check all inside
    if is_all_inside(input_points, hull) :
        return hull
    else :
        return concavehull4(input_points, k+1)


