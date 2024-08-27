import plane_extractor
import BPD
import numpy as np
import remove_wall
import open3d as o3d

def display_outlier(points, ind):
    inlier = points.select_by_index(ind)
    outlier = points.select_by_index(ind, invert=True)
    inlier.paint_uniform_color([0.7, 0.7, 0.7])
    outlier.paint_uniform_color([1, 0, 0])
    o3d.visualization.draw_geometries([inlier, outlier])

pc = o3d.io.read_point_cloud("cropped_1.ply")
#o3d.visualization.draw_geometries([pc])

plane, high_z, min_z = plane_extractor.extract_plane(pc)
boundary = BPD.cal_boundary(plane, save_filename="ceil_boundary.txt")
#boundary = np.loadtxt("ceil_boundary.txt")
points = np.array(pc.points)
high_z = float(np.max(points[:, 2]))
min_z = float(np.min(points[:, 2]))

props = remove_wall.remove_wall(points, boundary, method="cylinder", radius=0.07, min_z=min_z, high_z=high_z)

o3d.visualization.draw_geometries([props])

