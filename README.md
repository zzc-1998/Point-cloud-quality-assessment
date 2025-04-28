# :point_right: 3DQA Databases (update)

If you want to add PCQA papers and codes to this list, feel free to start a pull request.

We are happy to see your contribution!


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
| BASICS                | Point cloud         | Colored             | 1,494     |
| CMDM                  | Mesh                | Colored             | 480       |
| TMQA                  | Mesh                | Textured            | 3,000     |
| Geo-Metric            | Mesh                | Geometry Faces      | 2,450     |
| DHHQA                 | Mesh                | Textured human heads| 1,540     |
| DDH-QA                | FBX/MP4             | Dynamic Digital Humans | 800     |
| SJTU-H3D              | Mesh                | Full-body Digital Humans | 1,120     |

## PCQA databases 
| # | Database Name                         | Title & Link                                                                                                                                         | Database Link                                                                                                       |
|---|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| 1 | SJTU-PCQA                             | [Predicting the Perceptual Quality of Point Cloud: A 3D-to-2D Projection-Based Exploration](https://ieeexplore.ieee.org/abstract/document/9238424) | [Link](https://smt.sjtu.edu.cn/database/)                                                                            |
| 2 | WPC                                   | [Perceptual Quality Assessment of Colored 3D Point Clouds](https://ieeexplore.ieee.org/document/9756929)                                           | [Link](https://github.com/qdushl/Waterloo-Point-Cloud-Database)                                                      |
| 3 | LS-PCQA                               | [Point Cloud Quality Assessment: Dataset Construction and Learning-based No-Reference Approach](https://arxiv.org/pdf/2012.11895.pdf)             | [Link](https://smt.sjtu.edu.cn/database/)                                                                            |
| 4 | WPC2.0(Compression)                   | [Reduced Reference Perceptual Quality Model with Application to Rate Control for Video-based Point Cloud Compression](https://ieeexplore.ieee.org/document/9490512) | [Link](https://github.com/qdushl/Waterloo-Point-Cloud-Database-2.0)                                                  |
| 5 | WPC3.0(Compression)                   | [No-reference Bitstream-layer Model for Perceptual Quality Assessment of V-PCC Encoded Point Clouds](https://ieeexplore.ieee.org/document/9782549) | [Link](https://github.com/qdushl/Waterloo-Point-Cloud-Database-3.0)                                                  |
| 6 | CPCD2.0(Compression & Noise)          | [TGP-PCQA: Texture and geometry projection based quality assessment for colored point clouds](https://www.sciencedirect.com/science/article/pii/S1047320322000128) | [Link](https://github.com/cherry0415/CPCD2.0)                                                                        |
| 7 | ICIP2020                              | [Quality Evaluation Of Static Point Clouds Encoded Using MPEG Codecs](https://ieeexplore.ieee.org/abstract/document/9191308)                        |                                                                                                                      |
| 8 | M-PCCD                                | [A comprehensive study of the rate-distortion performance in MPEG point cloud compression](https://www.nowpublishers.com/article/Details/SIP-132)   |                                                                                                                      |
| 9 | IRPC                                  | [Point Cloud Rendering after Coding : Impacts on Subjective and Objective Quality.](https://ieeexplore.ieee.org/abstract/document/9257015/)       |                                                                                                                      |
|10 | SIAT-PCQD                             | [Subjective Quality Database and Objective Study of Compressed Point Clouds With 6DoF Head-Mounted Display](https://ieeexplore.ieee.org/abstract/document/9502695) | [Link](https://dx.doi.org/10.21227/ad8d-7r28)                                                                        |
|11 | vsenseVVDB (Volumetric Video Quality Database #1) | [Subjective and Objective Quality Assessment for Volumetric Video Compression](https://v-sense.scss.tcd.ie/research/6dof/quality-assessment-for-fvv-compression/) | [Link](https://v-sense.scss.tcd.ie/research/6dof/quality-assessment-for-fvv-compression/)                            |
|12 | vsenseVVDB2 (Volumetric Video Quality Database #2) | [Textured mesh vs coloured point cloud: A subjective study for volumetric video compression](https://ieeexplore.ieee.org/abstract/document/9123137/) | [Link](https://v-sense.scss.tcd.ie/research/6dof/quality-assessment-for-fvv-compression/)                            |
|13 | BASICS                                | [BASICS: Broad quality Assessment of Static point clouds In Compression Scenarios](https://arxiv.org/pdf/2302.04796.pdf)                           |                                                                                                                      |

## MQA (mesh quality assessment) database 
| # | Database Name | Title & Link                                                                                                                                                          | Database Link                                                             |
|---|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| 1 | CMDM          | [Visual Quality of 3D Meshes With Diffuse Colors in Virtual Reality: Subjective and Objective Evaluation](https://ieeexplore.ieee.org/abstract/document/9252120)    | [Link](https://yananehme.github.io)                                        |
| 2 | TMQA          | [Textured Mesh Quality Assessment: Large-Scale Dataset and Deep Learning-based Quality Metric](https://yananehme.github.io/publications/2022-ACM-TOG)               | [Link](https://yananehme.github.io/publications/2022-ACM-TOG)               |
| 3 | -             | [Geo-Metric: A Perceptual Dataset of Distortions on Faces](https://dl.acm.org/doi/abs/10.1145/3550454.3555475)                                                     | [link](https://github.com/facebookresearch/Geo-metric)                      |
| 4 | SJTU-TMQA     | [SJTU-TMQA: A quality assessment database for static mesh with texture map](https://arxiv.org/abs/2309.15675) | [link](https://ccccby.github.io/) |


## Digital human quality assessment database
| # | Database Name | Title & Link                                                                                                                                                                    | Database Link                                                       |
|---|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| 1 | DHHQA         | [Perceptual Quality Assessment for Digital Human Heads](https://arxiv.org/abs/2209.09489)                                                                                       | [Link](https://github.com/zzc-1998/DHHQA)                           |
| 2 | DDH-QA        | [DDH-QA: A DYNAMIC DIGITAL HUMANS QUALITY ASSESSMENT DATABASE](https://arxiv.org/pdf/2212.12734.pdf)                                                                           | [Link](https://github.com/zzc-1998/DDH-QA)                          |
| 3 | SJTU-H3D      | [Advancing Zero-Shot Digital Human Quality Assessment through Text-Prompted Evaluation](https://arxiv.org/abs/2307.02808)                                                       | [Link](https://github.com/zzc-1998/SJTU-H3D)






# :point_right: 3DQA methods
## Basic FR-PCQA
Basic full-reference quality assessment metrics implemented by Python.

I try to implement the p2point, p2plane, and PSNR_yuv with [python](https://github.com/zzc-1998/Point-cloud-quality-assessment/).
The original algorithms come from ["Evaluation criteria for PCC (Point Cloud Compression)"](https://mpeg.chiariglione.org/standards/mpeg-i/point-cloud-compression/evaluation-criteria-pcc),["Dynamic Polygon Clouds: Representation and Compression for VR/AR"](https://www.cambridge.org/core/journals/apsipa-transactions-on-signal-and-information-processing/article/dynamic-polygon-clouds-representation-and-compression-for-vrar/A83EFCDBEF825DA5DC2A08308B6E21BE), and ["Geometric Distortion Metrics for Point Cloud Compression"](https://ieeexplore.ieee.org/document/8296925).

## FR-PCQA metrics

| # | Metric Name | Title & Link                                                                                                        | Code Link                                                         |
|---|-------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| 1 | PointSSIM   | ["Towards a Point Cloud Structural Similarity Metric"](https://ieeexplore.ieee.org/abstract/document/9106005)      | [Code](https://github.com/mmspg/pointssim)                        |
| 2 | GraphSIM    | ["Inferring Point Cloud Quality via Graph Similarity"](http://arxiv.org/abs/2006.00497)                            | [Code](https://github.com/NJUVISION/GraphSIM)                     |
| 3 | PCQM        | ["PCQM: A Full-Reference Quality Metric for Colored 3D Point Clouds"](https://ieeexplore.ieee.org/document/9123147) | [Code](https://github.com/MEPP-team/PCQM)                         |


## RR-PCQA metrics

| # | Metric Name | Title & Link                                                                                                                             | Code Link                                                         |
|---|-------------|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| 1 | PCMrr       | ["A Reduced Reference Metric for Visual Quality Evaluation of Point Cloud Contents"](https://ieeexplore.ieee.org/abstract/document/9198142) | [Code](https://github.com/cwi-dis/PCM_RR)                        |
| 2 | -           | ["Reduced Reference Quality Assessment for Point Cloud Compression"](https://arxiv.org/pdf/2301.01009.pdf)                                 | -                                                                 |
| 3 | -           | ["Reduced-Reference Quality Assessment of Point Clouds via Content-Oriented Saliency Projection"](https://arxiv.org/abs/2301.07681)       | [Code](https://github.com/weizhou-geek/RR-CAP)                    |
| 4 | -           | ["Support Vector Regression-based Reduced-Reference Perceptual Quality Model for Compressed Point Clouds"](https://ieeexplore.ieee.org/abstract/document/10375131)||


## NR-PCQA metrics

| #  | Metric Name               | Title & Link                                                                                                                                                                                                                                 | Code Link                                               |
|----|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| 1  | 3D-NSS                    | ["No-Reference Quality Assessment for 3D Colored Point Cloud and Mesh Models"](https://ieeexplore.ieee.org/document/9810024) [[Arxiv]](https://arxiv.org/abs/2107.02041)                                                                     | [Code](https://github.com/zzc-1998/NR-3DQA)            |
| 2  | ResSCNN                   | ["Point Cloud Quality Assessment: Dataset Construction and Learning-based No-Reference Approach"](https://arxiv.org/pdf/2012.11895.pdf)                                                                                                    | [Code](https://github.com/lyp22/ResSCNN)               |
| 3  | IT-PCQA                   | ["No-Reference Point Cloud Quality Assessment via Domain Adaptation"](https://openaccess.thecvf.com/content/CVPR2022/papers/Yang_No-Reference_Point_Cloud_Quality_Assessment_via_Domain_Adaptation_CVPR_2022_paper.pdf)                     | [Code](https://github.com/lyp22/IT-PCQA)               |
| 4  | 3D-CNN-PCQA               | ["A No-reference Quality Assessment Metric for Point Cloud Based on Captured Video Sequences"](https://arxiv.org/abs/2206.05054)                                                                                                          | -                                                      |
| 5  | VQA-PC                    | ["Evaluating Point Cloud from Moving Camera Videos: A No-Reference Metric"](https://arxiv.org/abs/2208.14085)                                                                                                              | [Code](https://github.com/zzc-1998/VQA_PC)             |
| 6  | -                         | ["Blind Quality Assessment of 3D Dense Point Clouds with Structure Guided Resampling"](https://arxiv.org/abs/2208.14603)                                                                                                                    | -                                                      |
| 7  | MM-PCQA                   | ["MM-PCQA: Multi-Modal Learning for No-reference Point Cloud Quality Assessment"](https://arxiv.org/abs/2209.00244)                                                                                                                        | [Code](https://github.com/zzc-1998/MM-PCQA)            |
| 8  | -                         | ["V-PCC Projection Based Blind Point Cloud Quality Assessment for Compression Distortion"](https://ieeexplore.ieee.org/document/9881542)                                                                                                    | -                                                      |
| 9  | -                         | ["GPA-Net: No-Reference Point Cloud Quality Assessment with Multi-task Graph Convolutional Network"](https://arxiv.org/abs/2210.16478)                                                                                                     | [Code](https://github.com/Slowhander/GPA-Net)          |
| 10 | -                         | ["PQA-Net: Deep No Reference Point Cloud Quality Assessment via Multi-View Projection"](https://ieeexplore.ieee.org/document/9496633)                                                                                                      | [Code](https://github.com/qdushl/PQA-Net)              |
| 11 | -                         | ["Progressive Knowledge Transfer Based on Human Visual Perception Mechanism for Perceptual Quality Assessment of Point Clouds"](https://arxiv.org/abs/2211.16646)                                                                           | -                                                      |
| 12 | -                         | ["Bitstream-based Perceptual Quality Assessment of Compressed 3D Point Clouds"](https://ieeexplore.ieee.org/abstract/document/10061856?casa_token=hh3eIB-ggm8AAAAA:wIXnZG4sBOPW-ZY1XZA0Z3TtpbQDhRbwqQUcijdTRwHIjEb1OEakhcN5_2HV38IYg_1oW5_rjfY) | -                                                      |
| 13 | -                         | ["GMS-3DQA: Projection-based Grid Mini-patch Sampling for 3D Model Quality Assessment"](https://arxiv.org/pdf/2306.05658.pdf)                                                                                                               | [Code](https://github.com/zzc-1998/GMS-3DQA)           |
| 14 | -                         | ["Once-Training-All-Fine: No-Reference Point Cloud Quality Assessment via Domain-relevance Degradation Description"](https://arxiv.org/abs/2307.01567)                                                                                     | -                                                      |
| 15 | -                         | ["Pseudo-Reference Point Cloud Quality Measurement Based on Joint 2-D and 3-D Distortion Description"](https://ieeexplore.ieee.org/abstract/document/10167694)                                                                            | -                                                      |
| 16 | -                         | ["pmBQA: Projection-based Blind Point Cloud Quality Assessment via Multimodal Learning"](https://dl.acm.org/doi/abs/10.1145/3581783.3611998)                                                                            | -                                                      |
| 17 | -                         | ["Non-Local Geometry and Color Gradient Aggregation Graph Model for No-Reference Point Cloud Quality Assessment"](https://dl.acm.org/doi/abs/10.1145/3581783.3612169)                                                                            | -                                                      |
| 18 | -                         | ["Simple Baselines for Projection-based Full-reference and No-reference Point Cloud Quality Assessment"](https://arxiv.org/abs/2310.17147)                                                                            | -                                                      |
| 19 | -                         |["Plain-PCQA: No-Reference Point Cloud Quality Assessment by Analysis of Plain Visual and Geometrical Components"](https://ieeexplore.ieee.org/document/10381826)|-|
| 20 | -                         |["Zoom to Perceive Better: No-reference Point Cloud Quality Assessment via Exploring Effective Multiscale Feature"](https://ieeexplore.ieee.org/document/10422856)|[Code](https://openi.pcl.ac.cn/OpenPointCloud/MOD-PCQA)|
| 21 | -                         |["PAME: SELF-SUPERVISED MASKED AUTOENCODER FOR NO-REFERENCE POINT CLOUD QUALITY ASSESSMENT"](https://arxiv.org/pdf/2403.10061.pdf)|-|
| 22 | -                         |["Contrastive Pre-Training with Multi-View Fusion for No-Reference Point Cloud Quality Assessment"](https://arxiv.org/pdf/2403.10066.pdf)|-|
| 23 | -                         |["MFT-PCQA: Multi-Modal Fusion Transformer for No-Reference Point Cloud Quality Assessment"](https://ieeexplore.ieee.org/abstract/document/10445736)|-|
| 24 | -                         |["Rating-Augmented No-Reference Point Cloud Quality Assessment Using Multi-Task Learning"](https://ieeexplore.ieee.org/abstract/document/10448511) |-|
| 25 | -                         |["3DTA: No-Reference 3D Point Cloud Quality Assessment with Twin Attention"](https://ieeexplore.ieee.org/abstract/document/10542438) | [Code](https://github.com/philox12358/3DTA-PCQA) |
| 26 | -                         |["Compressed Point Cloud Quality Index by Combining Global Appearance and Local Details"](https://dl.acm.org/doi/abs/10.1145/3672567) | - |
| 27 | -                         |["Asynchronous Feedback Network for Perceptual Point Cloud Quality Assessment"](https://arxiv.org/pdf/2407.09806) | [Code](https://github.com/zhangyujie-1998/AFNet) |
| 28 | -                         |["TCDM: Transformational Complexity Based Distortion Metric for Perceptual Point Cloud Quality Assessment](https://ieeexplore.ieee.org/abstract/document/10337742)  | [Code](https://github.com/zyj1318053/TCDM) |
| 29 | ACM MM Best Paper Nomination |["LMM-PCQA: Assisting Point Cloud Quality Assessment with LMM"](https://arxiv.org/abs/2404.18203) | [Code](https://github.com/Q-Future/LMM-PCQA) |
| 30 | - |["LLM-guided Cross-Modal Point Cloud Quality Assessment: A Graph Learning Approach"](https://ieeexplore.ieee.org/abstract/document/10660545) | - |
| 31 | -                         |["Visual-Saliency Guided Multi-modal Learning for No Reference Point Cloud Quality Assessment"](https://dl.acm.org/doi/abs/10.1145/3689093.3689183)   |  - | 
| 32 | -                         |["Perceptual Quality Assessment of Trisoup-Lifting Encoded 3D Point Clouds"](https://arxiv.org/abs/2410.06689)           |  -  |
| 33 | -                         |["No-Reference Point Cloud Quality Assessment Through Structure Sampling and Clustering Based on Graph"](https://ieeexplore.ieee.org/abstract/document/10737898/)       | - |
| 34 | -                         |["No-reference point cloud quality assessment via graph convolutional network"](https://orca.cardiff.ac.uk/id/eprint/172907/)                         |   -   |
| 35 | -                         |["CLIP-PCQA: Exploring Subjective-Aligned Vision-Language Modeling for Point Cloud Quality Assessment"](https://arxiv.org/abs/2501.10071)                         |   -   |
| 36 | -                         |["Information Exploration of Projected Views for Point Cloud Quality Measurement"](https://ieeexplore.ieee.org/abstract/document/10841467)                         |   -   |
| 37 | -                         |["CMDC-PCQA: No-Reference Point Cloud Quality Assessment via a Cross-Modal Deep-Coupling Framework"](https://ieeexplore.ieee.org/abstract/document/10884925)        |   -   |
| 38 | -                         |["No-reference geometry quality assessment for colorless point clouds via list-wise rank learning"](https://www.sciencedirect.com/science/article/abs/pii/S0097849325000159)     |   -   | 
| 39 | -                         |["Dynamic Hypergraph Convolutional Network for No-Reference Point Cloud Quality Assessment"](https://ieeexplore.ieee.org/abstract/document/10549980)     | [Code](https://github.com/chenwuwq/DHCN) |                                       


## Mesh QA metrics

1. "Surface-Sampling Based Objective Quality Assessment Metrics for Meshes" [[ICASSP]](https://ieeexplore.ieee.org/document/10096048)


# Contact Information
:sunglasses: If you want to make contributions, include your works, or simply make discussions, feel free to e-mail me at zzc1998@sjtu.edu.cn :sunglasses:

:sparkling_heart: If you find this collection helpful, please star this project! Thank you! :sparkling_heart:
