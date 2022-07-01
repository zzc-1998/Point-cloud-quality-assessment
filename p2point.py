import open3d as o3d
import numpy as np
def pc_normalize(pc):
    l = pc.shape[0]
    centroid = np.mean(pc, axis=0)
    pc = pc - centroid
    m = np.max(np.sqrt(np.sum(pc**2, axis=1)))
    pc = pc / m
    return pc


def d_rms(src,tar):
    # Calculates the one way matching distortion from src -> target
    # building kdtree
    tar_pc = o3d.geometry.PointCloud()
    tar_pc.points = o3d.utility.Vector3dVector(tar)
    kdtree = o3d.geometry.KDTreeFlann(tar_pc)
    # matching points and caculate distance    
    point_size_src = src.shape[0]
    distance_list = np.zeros(point_size_src)
    for i in range(point_size_src):
        [_,idx,dis] = kdtree.search_knn_vector_3d(src[i],1)
        distance_list[i] = dis[0] # get the square of the closest point's distance
    return (distance_list.sum()/point_size_src)**0.5

def d_hausdorf(src,tar):
    # Calculates the one way matching distortion from src -> target
    # building kdtree
    tar_pc = o3d.geometry.PointCloud()
    tar_pc.points = o3d.utility.Vector3dVector(tar)
    kdtree = o3d.geometry.KDTreeFlann(tar_pc)
    # matching points and caculate distance    
    point_size_src = src.shape[0]
    distance_list = np.zeros(point_size_src)
    for i in range(point_size_src):
        [_,idx,dis] = kdtree.search_knn_vector_3d(src[i],1)
        distance_list[i] = dis[0] # get the square of the closest point's distance
    return np.max(distance_list)**0.5

def d_symmetric_rms(pc1,pc2,mode = 'max'):
    # p2point see Evaluation criteria for PCC (Point Cloud Compression)
    if mode == 'max':
        return max(d_rms(pc1,pc2),d_rms(pc2,pc1))
    else:
    # see See `"Dynamic Polygon Clouds: Representation and Compression for VR/AR" <https://arxiv.org/abs/1610.00402>` paper.
        return (d_rms(pc1,pc2)+d_rms(pc2,pc1))/2 

def d_symmetric_hausdorf(pc1,pc2):
    # haudorf p2point see Evaluation criteria for PCC (Point Cloud Compression)
    return max(d_hausdorf(pc1,pc2),d_hausdorf(pc2,pc1))


def p2point(ref_name,dis_name):
    ref = o3d.io.read_point_cloud(ref_name)
    dis = o3d.io.read_point_cloud(dis_name)
    ref_points = pc_normalize(np.array(ref.points))
    dis_points = pc_normalize(np.array(dis.points))
    return d_symmetric_rms(ref_points,dis_points)

def p2point_hausdorf(ref_name,dis_name):
    ref = o3d.io.read_point_cloud(ref_name)
    dis = o3d.io.read_point_cloud(dis_name)
    ref_points = pc_normalize(np.array(ref.points))
    dis_points = pc_normalize(np.array(dis.points))
    return d_symmetric_hausdorf(ref_points,dis_points)

ref_name = 'hhi.ply'
dis_name = 'hhi_0.ply'
#print(p2point(ref_name,dis_name))
print(p2point_hausdorf(ref_name,dis_name))