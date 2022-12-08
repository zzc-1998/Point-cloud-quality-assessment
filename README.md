# :point_right: 3DQA databases (update)

## PCQA databases 
1. SJTU-PCQA: [Predicting the Perceptual Quality of Point Cloud: A 3D-to-2D Projection-Based Exploration](https://ieeexplore.ieee.org/abstract/document/9238424) [[Link]](https://smt.sjtu.edu.cn/database/)
2. WPC: [Perceptual Quality Assessment of Colored 3D Point Clouds](https://ieeexplore.ieee.org/document/9756929) [[Link]](https://github.com/qdushl/Waterloo-Point-Cloud-Database)
3. LS-PCQA: [Point Cloud Quality Assessment: Dataset Construction and Learning-based No-Reference Approach](https://arxiv.org/pdf/2012.11895.pdf) [[Link]](https://smt.sjtu.edu.cn/database/)
4. WPC2.0(Compression): [Reduced Reference Perceptual Quality Model with Application to Rate Control for Video-based Point Cloud Compression](https://ieeexplore.ieee.org/document/9490512)   [[Link]](https://github.com/qdushl/Waterloo-Point-Cloud-Database-2.0)
5. WPC3.0(Compression): [No-reference Bitstream-layer Model for Perceptual Quality Assessment of V-PCC Encoded Point Clouds](https://ieeexplore.ieee.org/document/9782549) [[Link]](https://github.com/qdushl/Waterloo-Point-Cloud-Database-3.0)
6. CPCD2.0(Compression & Noise): [TGP-PCQA: Texture and geometry projection based quality assessment for colored point clouds](https://www.sciencedirect.com/science/article/pii/S1047320322000128) [[Link]](https://github.com/cherry0415/CPCD2.0)
7. ICIP2020: [Quality Evaluation Of Static Point Clouds Encoded Using MPEG Codecs](https://ieeexplore.ieee.org/abstract/document/9191308)
8. M-PCCD: [A comprehensive study of the rate-distortion performance in MPEG point cloud compression](https://www.nowpublishers.com/article/Details/SIP-132)
9. IRPC: [Point Cloud Rendering after Coding : Impacts on Subjective and Objective Quality.](https://ieeexplore.ieee.org/abstract/document/9257015/)
10. SIAT-PCQD: [Subjective Quality Database and Objective Study of Compressed Point Clouds With 6DoF Head-Mounted Display](https://ieeexplore.ieee.org/abstract/document/9502695) [[Link]](https://dx.doi.org/10.21227/ad8d-7r28)
11. vsenseVVDB (Volumetric Video Quality Database #1): [Subjective and Objective Quality Assessment for Volumetric Video Compression] (https://v-sense.scss.tcd.ie/research/6dof/quality-assessment-for-fvv-compression/) [[Link]](https://v-sense.scss.tcd.ie/research/6dof/quality-assessment-for-fvv-compression/)
12. vsenseVVDB2 (Volumetric Video Quality Database #2): [Textured mesh vs coloured point cloud: A subjective study for volumetric video compression](https://ieeexplore.ieee.org/abstract/document/9123137/) [[Link]](https://v-sense.scss.tcd.ie/research/6dof/quality-assessment-for-fvv-compression/)


## MQA (mesh quality assessment) database 
1. CMDM: [Visual Quality of 3D Meshes With Diffuse Colors in Virtual Reality: Subjective and Objective Evaluation](https://ieeexplore.ieee.org/abstract/document/9252120) [[Link]](https://yananehme.github.io) 
2. TMQA: [Textured Mesh Quality Assessment: Large-Scale Dataset and Deep Learning-based Quality Metric](https://yananehme.github.io/publications/2022-ACM-TOG) [[Link]](https://yananehme.github.io/publications/2022-ACM-TOG)
3. [Geo-Metric: A Perceptual Dataset of Distortions on Faces](https://dl.acm.org/doi/abs/10.1145/3550454.3555475) [[link]](https://github.com/facebookresearch/Geo-metric)


## Overview of the databases
| Database              | Format | Attributes | Rated Models|
|-----------------------|---------------------|---------------------|-----------|
| M-PCCD                | Point cloud         | Colored             | 232       |
| IRPC                  | Point cloud         | Colorless & Colored | 54 & 54   |
| WPC                   | Point cloud         | Colored             | 740       |
| WPC2.0                | Point cloud         | Colored             | 400       | 
| WPC3.0                | Point cloud         | Colored             | 350       | 
| ICIP2020              | Point cloud         | Colored             | 96        |
| SJTU-PCQA             | Point cloud         | Colored             | 378       |
| SIAT-PCQD             | Point cloud         | Colored             | 340       |
| LS-PCQA               | Point cloud         | Colored             | 1,080     |
| CMDM                  | Mesh                | Colored             | 480       |
| TMQA                  | Mesh                | Textured            | 3,000     |
| Geo-Metric            | Mesh                | Geometry Faces      | 840       |




# :point_right: 3DQA methods
## Basic FR-PCQA
Basic full-reference quality assessment metrics implemented by python.

I try to implement the p2point, p2plane, and PSNR_yuv with [python](https://github.com/zzc-1998/Point-cloud-quality-assessment/).
The original algoritms come from ["Evaluation criteria for PCC (Point Cloud Compression)"](https://mpeg.chiariglione.org/standards/mpeg-i/point-cloud-compression/evaluation-criteria-pcc),["Dynamic Polygon Clouds: Representation and Compression for VR/AR"](https://www.cambridge.org/core/journals/apsipa-transactions-on-signal-and-information-processing/article/dynamic-polygon-clouds-representation-and-compression-for-vrar/A83EFCDBEF825DA5DC2A08308B6E21BE), and ["Geometric Distortion Metrics for Point Cloud Compression"](https://ieeexplore.ieee.org/document/8296925).

## FR-PCQA metrics

1.PointSSIM: "Towards a Point Cloud Structural Similarity Metric" [[IEEE]](https://ieeexplore.ieee.org/abstract/document/9106005) [[Code]](https://github.com/mmspg/pointssim)

2.GraphSIM: "Inferring Point Cloud Quality via Graph Similarity" [[IEEE]](http://arxiv.org/abs/2006.00497) [[Code]](https://github.com/NJUVISION/GraphSIM)

3.PCQM "PCQM: A Full-Reference Quality Metric for Colored 3D Point Clouds" [[IEEE]](https://ieeexplore.ieee.org/document/9123147) [[Code]](https://github.com/MEPP-team/PCQM)

## RR-PCQA metrics

1. PCMrr: "A Reduced Reference Metric for Visual Quality Evaluation of Point Cloud Contents" [[IEEE]](https://ieeexplore.ieee.org/abstract/document/9198142) [[Code]](https://github.com/cwi-dis/PCM_RR)

## NR-PCQA metrics

1. 3D-NSS: "No-Reference Quality Assessment for 3D Colored Point Cloud and Mesh Models" [[IEEE-TCSVT]](https://ieeexplore.ieee.org/document/9810024) [[Arxiv]](https://arxiv.org/abs/2107.02041) [[Code]](https://github.com/zzc-1998/NR-3DQA)

2. ResSCNN: "Point Cloud Quality Assessment: Dataset Construction and Learning-based No-Reference Approach"  [[Arxiv]](https://arxiv.org/pdf/2012.11895.pdf) [[Code]](https://github.com/lyp22/ResSCNN)

3. IT-PCQA:  "No-Reference Point Cloud Quality Assessment via Domain Adaptation" [[CVPR]](https://openaccess.thecvf.com/content/CVPR2022/papers/Yang_No-Reference_Point_Cloud_Quality_Assessment_via_Domain_Adaptation_CVPR_2022_paper.pdf)[[Code]](https://github.com/lyp22/IT-PCQA)

4. 3D-CNN-PCQA: "A No-reference Quality Assessment Metric for Point Cloud Based on Captured Video Sequences" [[Arxiv]](https://arxiv.org/abs/2206.05054)

5. VQA-PC:"Treating Point Cloud as Moving Camera Videos: A No-Reference Quality Assessment Metric" [[Arxiv]](https://arxiv.org/abs/2208.14085) [[Code]](https://github.com/zzc-1998/VQA_PC)

6. "Blind Quality Assessment of 3D Dense Point Clouds with Structure Guided Resampling" [[Arxiv]](https://arxiv.org/abs/2208.14603)

7. MM-PCQA: "MM-PCQA: Multi-Modal Learning for No-reference Point Cloud Quality Assessment" [[Arxiv]](https://arxiv.org/abs/2209.00244)

8. "V-PCC Projection Based Blind Point Cloud Quality Assessment for Compression Distortion" [[IEEE]](https://ieeexplore.ieee.org/document/9881542)

9. "GPA-Net:No-Reference Point Cloud Quality Assessment with Multi-task Graph Convolutional Network" [[Arxiv]](https://arxiv.org/abs/2210.16478) [[Code]](https://github.com/Slowhander/GPA-Net)

10. "PQA-Net: Deep No Reference Point Cloud Quality Assessment via Multi-View Projection" [[IEEE]](https://ieeexplore.ieee.org/document/9496633) [[Code]](https://github.com/qdushl/PQA-Net)

11. "Progressive Knowledge Transfer Based on Human Visual Perception Mechanism for Perceptual Quality Assessment of Point Clouds" [[Arxiv]](https://arxiv.org/abs/2211.16646)




# Contact Information
:sunglasses: If you want to make contributions, include your works, or simply make discussions, feel free to e-mail me at zzc1998@sjtu.edu.cn :sunglasses:

:sparkling_heart: If you find this collection helpful, please star this poject! Thank you! :sparkling_heart:
