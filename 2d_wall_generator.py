import numpy as np
import matplotlib.pyplot as plt
import random
import Circle as C
import open3d as o3d
import alphashape
from sklearn.neighbors import NearestNeighbors
from itertools import combinations

def display_inlier_outlier(cloud, ind):
    inlier_cloud = cloud.select_by_index(ind)
    outlier_cloud = cloud.select_by_index(ind, invert=True)

    print("Showing outliers (red) and inliers (gray): ")
    outlier_cloud.paint_uniform_color([1, 0, 0])
    inlier_cloud.paint_uniform_color([0.8, 0.8, 0.8])
    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])

#pc = o3d.io.read_point_cloud("cropped_1.ply")
pc = o3d.io.read_point_cloud("pointcloud.ply")
o3d.visualization.draw_geometries([pc])

#Method : Get Highest Z Value

#remove outlier
pc_down = pc.voxel_down_sample(voxel_size=0.1)
cl, ind = pc_down.remove_statistical_outlier(nb_neighbors=30, std_ratio=2.0)
display_inlier_outlier(pc_down, ind)

pc_down = pc_down.select_by_index(ind)

#extract ceil
high_z = -10000
min_z = 1000000
points = pc_down.points
for i in range(len(points)) :
    if points[i][2] > high_z :
        high_z = points[i][2]

    if points[i][2] < min_z :
        min_z = points[i][2]

print(f'{high_z} , {min_z}')
inliers = []

#Parameter
z_ratio = 0.25
z_threshold = abs(high_z - min_z) * z_ratio

for i in range(len(points)) :
    if points[i][2] >= high_z - z_threshold :
        inliers.append(i)

#remove outlier in ceil
segments = pc_down.select_by_index(inliers)
o3d.visualization.draw_geometries([segments])
cl, ind = segments.remove_statistical_outlier(nb_neighbors=30, std_ratio=2.0)
display_inlier_outlier(segments, ind)

segments = segments.select_by_index(ind)

#project to highest Z value
points = np.array(segments.points)
points[:, 2] = high_z
segments.points = o3d.utility.Vector3dVector(points)
o3d.visualization.draw_geometries([segments])

points = np.array(segments.points)

np.savetxt("ceil.txt", points[:, :2])

