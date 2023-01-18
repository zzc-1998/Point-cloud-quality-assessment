import open3d as o3d
import numpy as np
def pc_normalize(pc):
    l = pc.shape[0]
    centroid = np.mean(pc, axis=0)
    pc = pc - centroid
    m = np.max(np.sqrt(np.sum(pc**2, axis=1)))
    pc = pc / m
    return pc

def estimate_normal(pcd):
    # estimate normals if point cloud does not have normals
    pcd.estimate_normals(
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=10000, max_nn=30))
    normals = np.asarray(pcd.normals)
    return normals

def match_point_compute_error(src,tar,normals):
    # Calculates the one way matching distortion from src -> target
    # building kdtree
    tar_pc = o3d.geometry.PointCloud()
    tar_pc.points = o3d.utility.Vector3dVector(tar)
    kdtree = o3d.geometry.KDTreeFlann(tar_pc)
    # matching points  
    point_size_src = src.shape[0]
    error_list = np.zeros(point_size_src)
    for i in range(point_size_src):
        [_,idx,dis] = kdtree.search_knn_vector_3d(src[i],1)
        normal = normals[i] # get the src normal
        error_vector = tar[idx[0]] - src[i] # compute the error vector
        error_list[i] = (np.dot(normal,error_vector))**2 # get the square of vector projection
    return error_list.sum()/point_size_src

def match_point_compute_error_hausdorf(src,tar,normals):
    # Calculates the one way matching distortion from src -> target
    # building kdtree
    tar_pc = o3d.geometry.PointCloud()
    tar_pc.points = o3d.utility.Vector3dVector(tar)
    kdtree = o3d.geometry.KDTreeFlann(tar_pc)
    # matching points  
    point_size_src = src.shape[0]
    error_list = np.zeros(point_size_src)
    for i in range(point_size_src):
        [_,idx,dis] = kdtree.search_knn_vector_3d(src[i],1)
        normal = normals[i] # get the src normal
        error_vector = tar[idx[0]] - src[i] # compute the error vector
        error_list[i] = (np.dot(normal,error_vector))**2 # get the square of vector projection
    return np.max(error_list)**0.5


#MSE P2PLANE   
def p2plane(ref_name,dis_name, no_normals = 'True'):
    ref = o3d.io.read_point_cloud(ref_name)
    dis = o3d.io.read_point_cloud(dis_name)
    if no_normals:
        ref_normals = estimate_normal(ref)
    else:
        ref_normals = np.array(ref.normals)
    ref_points = pc_normalize(np.array(ref.points))
    dis_points = pc_normalize(np.array(dis.points))
    return match_point_compute_error(ref_points,dis_points,ref_normals)

#HAUDORF P2PLANE
def p2plane_hausdorf(ref_name,dis_name, no_normals = 'True'):
    ref = o3d.io.read_point_cloud(ref_name)
    dis = o3d.io.read_point_cloud(dis_name)
    if no_normals:
        ref_normals = estimate_normal(ref)
    else:
        ref_normals = np.array(ref.normals)
    ref_points = pc_normalize(np.array(ref.points))
    dis_points = pc_normalize(np.array(dis.points))
    return match_point_compute_error_hausdorf(ref_points,dis_points,ref_normals)
