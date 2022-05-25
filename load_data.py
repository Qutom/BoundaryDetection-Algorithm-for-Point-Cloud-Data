#테스트용 파일
#points를 읽어와 resolution을 계산하고 circle을 그리는 것 까지 구현

import numpy as np
import matplotlib.pyplot as plt
import random
import Circle as C
import open3d as o3d
from sklearn.neighbors import NearestNeighbors
from itertools import combinations
# 테스트용 파일
# points를 읽어와 resolution을 계산하고 circle을 그리는 것 까지 구현

file_name = "points.txt"
points = np.loadtxt(file_name)

#pc = o3d.geometry.PointCloud()
#pc.points = o3d.utility.Vector3dVector(np.array(points))
#o3d.visualization.draw_geometries([pc])
# knn
neighbors = NearestNeighbors(n_neighbors=30, algorithm='ball_tree').fit(points)
distances, indices = neighbors.kneighbors(points)

# 랜덤한 점을 하나 잡음
point_index = random.randrange(0, points.shape[0])
p_neighbor, p_distance = indices[point_index], distances[point_index]
neighbor_points = points[p_neighbor]

# resolution 계산 ( distance의 mean + 2*std)
p_mean = np.mean(p_distance)
p_std = np.std(p_distance)
local_resol = p_mean + 2 * p_std

# 랜덤한 두 이웃을 잡아 원을 생성
pairs = list(combinations(p_neighbor[1:], 2))
ind = random.randint(0, len(pairs))
p1 = points[point_index]
p2 = points[pairs[10][0]]
p3 = points[pairs[10][1]]
c = C.Circle(p1, p2, p3)

# implement radius >= resolution check
file_name = "points.txt"
points = np.loadtxt(file_name)
print(points.shape[0])
#pc = o3d.geometry.PointCloud()
#pc.points = o3d.utility.Vector3dVector(points)
#o3d.visualization.draw_geometries([pc])
#knn
neighbors = NearestNeighbors(n_neighbors=30, algorithm='ball_tree').fit(points)
distances, indices = neighbors.kneighbors(points)

boundary = []
for i in range(points.shape[0]) :
    p_neighbor, p_distance = indices[i], distances[i]
    neighbor_points = points[p_neighbor[1:]]
    d = []
    for j in range(len(p_neighbor)) :
        temp = []
        for k in range(len(p_neighbor)) :
            if not j == k :
                temp.append(np.linalg.norm(points[p_neighbor[j]] - points[p_neighbor[k]]))
        d.append(temp)
    print(np.array(d).shape)
    #resolution 계산 ( distance의 mean + 2*std)
    p_mean = np.mean(p_distance)
    p_std = np.std(p_distance)
    local_resol = p_mean + 2 * p_std

#랜덤한 두 이웃을 잡아 원을 생성
    pairs = list(combinations(p_neighbor[1:], 2))
    for j in range(len(pairs)) :
        count = 0
        p1 = points[i]
        p2 = points[pairs[j][0]]
        p3 = points[pairs[j][1]]
        c = C.Circle(p1, p2, p3)
        print(neighbor_points)
        print(c.center)
        print(neighbor_points - c.center)
        if c.radius >= local_resol :
            cn_distance = np.linalg.norm((neighbor_points - c.center), axis=1)
            print(cn_distance)
            #print(f'resol : {local_resol}')
            #print(f'rad : {c.radius}')
            for k in range(len(cn_distance)) :
                if cn_distance[k] <= c.radius :
                    print(f'{cn_distance[k]}')
                    count += 1

                    if count > 3 :
                        break

        if count > 3 :
            boundary.append(points[i])
            break

print(f'len : {len(boundary)}')

pc = o3d.geometry.PointCloud()
pc.points = o3d.utility.Vector3dVector(np.array(boundary))
o3d.visualization.draw_geometries([pc])

"""
c_points = c.to_array()

vec1 = np.array([0,0,1])
a, b = (vec1 / np.linalg.norm(vec1)).reshape(3), (c.normal / np.linalg.norm(c.normal)).reshape(3)
v = np.cross(a, b)
cc = np.dot(a, b)
s = np.linalg.norm(v)
kmat = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
rotation_matrix = np.eye(3) + kmat + kmat.dot(kmat) * ((1 - cc) / (s ** 2))
rotation_matrix = np.array(rotation_matrix)

for i in range(c_points.shape[0]) :
    c_points[i] = rotation_matrix @ c_points[i] + c.center
ax = plt.axes(projection='3d')
ax.scatter3D(c_points[:,0], c_points[:,1], c_points[:,2])
ax.scatter3D(c.center[0], c.center[1], c.center[2], color='r')
ax.scatter3D(neighbor_points[:,0], neighbor_points[:,1], neighbor_points[:,2] , color='g')
ax.scatter3D(p1[0], p1[1], p2[2], color='c')
ax.scatter3D((p2[0], p3[0]), (p2[1], p3[1]), (p2[2], p3[2]), color='m')
plt.plot((c.center[0], c.center[0] + c.normal[0] * 10 ), (c.center[1], c.center[1] + c.normal[1] * 10 ), (c.center[2], c.center[2] + c.normal[2] * 10 ))
plt.show()
"""