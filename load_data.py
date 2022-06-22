import numpy as np
import matplotlib.pyplot as plt
import random
import Circle as C
import open3d as o3d
import polar
from sklearn.neighbors import NearestNeighbors
from itertools import combinations

file_name = "ceil.txt"

points = np.loadtxt(file_name)

pc = o3d.geometry.PointCloud()
pc.points = o3d.utility.Vector3dVector(np.pad(np.array(points), (0, 1), 'constant', constant_values=0))
o3d.visualization.draw_geometries([pc])

# knn
neighbors = NearestNeighbors(n_neighbors=30).fit(points)
distances, indices = neighbors.kneighbors(points)

max_b = 0
min_b = 1000000000

boundary = []
for i in range(points.shape[0]) :
    is_boundary = False
    p_neighbor, p_distance = indices[i], np.round(distances[i], 5)
    neighbor_points = points[p_neighbor[1:]]

    p_mean = np.mean(p_distance)
    p_std = np.std(p_distance)
    local_resol = round(p_mean + 2 * p_std, 5)

    if local_resol > max_b :
        max_b = local_resol
    if min_b > local_resol :
        min_b = local_resol

    pairs = list(combinations(p_neighbor[1:], 2))
    print(i)
    for j in range(len(pairs)) :
        count = 0
        p1 = points[i]
        p2 = points[pairs[j][0]]
        p3 = points[pairs[j][1]]
        c = C.Circle(p1, p2, p3)
        if c.radius == None :
            continue

        if c.radius >= local_resol :
            cn_distance = np.linalg.norm((neighbor_points - c.center), axis=1)
            cn_distance = np.round(cn_distance, 5)

            for k in range(len(cn_distance)) :
                if cn_distance[k] <= c.radius :
                    count += 1

                    if count > 3 :
                        break

        if count == 3 :
            boundary.append(points[i])
            is_boundary = True
            break

    #use polar coordinate
    if not is_boundary :
        pol = polar.Polar(np.array(points[i]), neighbor_points, normalize=True)



print(f'len : {len(boundary)}')
print(f'{min_b}')
print(f'{max_b}')
pc = o3d.geometry.PointCloud()
pc.points = o3d.utility.Vector3dVector(np.pad(np.array(boundary), (0, 1), 'constant', constant_values=0))
o3d.visualization.draw_geometries([pc])


