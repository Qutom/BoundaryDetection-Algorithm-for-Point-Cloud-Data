import numpy as np
import open3d as o3d

"""
@Params : points : numpy array
          boundary : numpy array
          raidus : float
          min_z  : float
          high_z : float
@Return  : pointcloud data
"""
def remove_cylinder(points, boundary, radius, min_z, high_z) :
    pc = o3d.geometry.PointCloud()
    pc.points = o3d.utility.Vector3dVector(points)

    for i in range(boundary.shape[0]) :
        z = np.arange(min_z, high_z, radius * 0.7)
        pillar_points = np.tile(boundary[i], (z.shape[0], 1))

        pillar_points = np.hstack((pillar_points, z.reshape(z.shape[0], 1)))
        pillar_pc = o3d.geometry.PointCloud()
        pillar_pc.points = o3d.utility.Vector3dVector(pillar_points)

        dists = np.asarray(pc.compute_point_cloud_distance(pillar_pc))
        ind = np.where(dists > radius)[0]
        pc = pc.select_by_index(ind)
        print(i)
    return pc

"""
@Params : points : numpy array
          boundary : numpy array
@Return  : numpy array
"""
def remove_wall(points, boundary, method="edge", radius=0.5, box_size=0.5, min_z=None, high_z=None) :
    if method == "edge" :
        #use edge algorithm
        pass
    if method == "box" :
        #use box algorithm
        pass
    if method == "cylinder" :
        result = remove_cylinder(points, boundary, radius=radius, min_z=min_z, high_z=high_z)

    return result