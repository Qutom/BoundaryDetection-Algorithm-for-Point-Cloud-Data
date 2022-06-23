import numpy as np
import open3d as o3d


def display_outlier(points, ind):
    inlier = points.select_by_index(ind)
    outlier = points.select_by_index(ind, invert=True)
    inlier.paint_uniform_color([0.7, 0.7, 0.7])
    outlier.paint_uniform_color([1, 0, 0])
    o3d.visualization.draw_geometries([inlier, outlier])


def extract_plane(pointcloud, show_progress=False, voxel_size=0.1, nb_neighbors=30, std_ratio=2.0, z_ratio=0.25,
                  save_filename=None):
    if show_progress:
        o3d.visualization.draw_geometries([pointcloud])

    # remove outlier
    pc_down = pointcloud.voxel_down_sample(voxel_size=voxel_size)
    cl, ind = pc_down.remove_statistical_outlier(nb_neighbors=nb_neighbors, std_ratio=std_ratio)
    if show_progress:
        display_outlier(pc_down, ind)

    pc_down = pc_down.select_by_index(ind)

    # extract ceil
    high_z = -10000
    min_z = 1000000
    high_ind = 0
    low_ind = 0
    points = pc_down.points
    for i in range(len(points)):
        if points[i][2] > high_z:
            high_z = points[i][2]
            high_ind = i

        if points[i][2] < min_z:
            min_z = points[i][2]
            low_ind = i

    if show_progress:
        print(f'{high_z} , {min_z}')
        high_point = pc_down.select_by_index([high_ind])
        low_point = pc_down.select_by_index([low_ind])
        temp = pc_down.select_by_index([high_ind, low_ind], invert=True)
        temp.paint_uniform_color([0.7, 0.7, 0.7])
        high_point.paint_uniform_color([1, 0, 0])
        low_point.paint_uniform_color([0, 1, 0])

        o3d.visualization.draw_geometries([low_point, high_point, temp])

    # Parameter
    z_threshold = abs(high_z - min_z) * z_ratio
    inliers = []
    for i in range(len(points)) :
        if points[i][2] >= z_threshold :
            inliers.append(i)

    # remove outlier in ceil
    segments = pc_down.select_by_index(inliers)
    if show_progress :
        o3d.visualization.draw_geometries([segments])

    cl, ind = segments.remove_statistical_outlier(nb_neighbors=nb_neighbors, std_ratio=std_ratio)
    if show_progress:
        display_outlier(segments, ind)
    segments = segments.select_by_index(ind)

    # project to highest Z value
    points = np.array(segments.points)
    points[:, 2] = high_z
    segments.points = o3d.utility.Vector3dVector(points)

    if show_progress:
        o3d.visualization.draw_geometries([segments])

    points = np.array(segments.points)

    if save_filename != None:
        np.savetxt(save_filename, points[:, :2])

    return points[:, :2]
