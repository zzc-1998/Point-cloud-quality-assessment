import open3d as o3d
import numpy as np
import math 

def pc_normalize(pc):
    l = pc.shape[0]
    centroid = np.mean(pc, axis=0)
    pc = pc - centroid
    m = np.max(np.sqrt(np.sum(pc**2, axis=1)))
    pc = pc / m
    return pc

def RGB2YUV( rgb ):  
    m = np.array([[ 0.29900, -0.16874,  0.50000],
                 [0.58700, -0.33126, -0.41869],
                 [ 0.11400, 0.50000, -0.08131]])
    yuv = np.dot(rgb,m)
    yuv[:,1:]+=128.0
    return yuv


def match_point_compute_mse(src,tar,src_yuv,tar_yuv):
    # Calculates the one way matching distortion from src -> target
    # building kdtree
    tar_pc = o3d.geometry.PointCloud()
    tar_pc.points = o3d.utility.Vector3dVector(tar)
    kdtree = o3d.geometry.KDTreeFlann(tar_pc)
    # matching points and caculate distance    
    point_size_src = src.shape[0]
    y_list = np.zeros(point_size_src)
    for i in range(point_size_src):
        [_,idx,dis] = kdtree.search_knn_vector_3d(src[i],1)
        y_list[i] = (src_yuv[i][0] - tar_yuv[idx[0]][0])**2 # get the square of the closest point's y
    return np.sum(y_list)/point_size_src




def psnr_y(ref_name,dis_name):
    ref = o3d.io.read_point_cloud(ref_name)
    dis = o3d.io.read_point_cloud(dis_name)
    ref_points = pc_normalize(np.array(ref.points))
    dis_points = pc_normalize(np.array(dis.points))
    ref_yuv = RGB2YUV(np.array(ref.colors)*255)
    dis_yuv = RGB2YUV(np.array(dis.colors)*255)
    mse_square = match_point_compute_mse(ref_points,dis_points,ref_yuv,dis_yuv)
    return 10 * math.log10(255.0**2/mse_square)



ref_name = 'hhi.ply'
dis_name = 'hhi_0.ply'
#print(p2point(ref_name,dis_name))
print(psnr_y(ref_name,dis_name))