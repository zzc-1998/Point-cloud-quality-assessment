# 3D Quality Assessment Resources

A curated collection of public resources for 3D quality assessment, including point cloud quality assessment (PCQA), mesh quality assessment (MQA), and digital human quality assessment datasets and methods.

Contributions are welcome. If you would like to add new papers, datasets, or code repositories, please open a pull request or contact the maintainer.

## Contents

- [Datasets](#datasets)
  - [Dataset Overview](#dataset-overview)
  - [Point Cloud Quality Assessment Datasets](#point-cloud-quality-assessment-datasets)
  - [Mesh Quality Assessment Datasets](#mesh-quality-assessment-datasets)
  - [Digital Human Quality Assessment Datasets](#digital-human-quality-assessment-datasets)
- [Methods](#methods)
  - [Basic Full-Reference PCQA](#basic-full-reference-pcqa)
  - [Full-Reference PCQA Metrics](#full-reference-pcqa-metrics)
  - [Reduced-Reference PCQA Metrics](#reduced-reference-pcqa-metrics)
  - [No-Reference PCQA Metrics](#no-reference-pcqa-metrics)
  - [Mesh QA Metrics](#mesh-qa-metrics)
- [Contact](#contact)

## Datasets

### Dataset Overview

| Dataset | Format | Attributes | Rated Models |
|---|---|---|---:|
| M-PCCD | Point cloud | Colored | 232 |
| IRPC | Point cloud | Colorless and colored | 54 and 54 |
| WPC | Point cloud | Colored | 740 |
| WPC2.0 | Point cloud | Colored | 400 |
| WPC3.0 | Point cloud | Colored | 350 |
| ICIP2020 | Point cloud | Colored | 96 |
| SJTU-PCQA | Point cloud | Colored | 378 |
| SIAT-PCQD | Point cloud | Colored | 340 |
| LS-PCQA | Point cloud | Colored | 1,080 |
| BASICS | Point cloud | Colored | 1,494 |
| PointQ-Bench | Point cloud | MOS, issue tags, and QA pairs | 3,083 |
| CMDM | Mesh | Colored | 480 |
| TMQA | Mesh | Textured | 3,000 |
| Geo-Metric | Mesh | Geometry faces | 2,450 |
| DHHQA | Mesh | Textured human heads | 1,540 |
| DDH-QA | FBX/MP4 | Dynamic digital humans | 800 |
| SJTU-H3D | Mesh | Full-body digital humans | 1,120 |

### Point Cloud Quality Assessment Datasets

| # | Dataset | Paper | Dataset Link |
|---:|---|---|---|
| 1 | SJTU-PCQA | [Predicting the Perceptual Quality of Point Cloud: A 3D-to-2D Projection-Based Exploration](https://ieeexplore.ieee.org/abstract/document/9238424) | [Link](https://smt.sjtu.edu.cn/database/) |
| 2 | WPC | [Perceptual Quality Assessment of Colored 3D Point Clouds](https://ieeexplore.ieee.org/document/9756929) | [Link](https://github.com/qdushl/Waterloo-Point-Cloud-Database) |
| 3 | LS-PCQA | [Point Cloud Quality Assessment: Dataset Construction and Learning-based No-Reference Approach](https://arxiv.org/pdf/2012.11895.pdf) | [Link](https://smt.sjtu.edu.cn/database/) |
| 4 | WPC2.0 (Compression) | [Reduced Reference Perceptual Quality Model with Application to Rate Control for Video-based Point Cloud Compression](https://ieeexplore.ieee.org/document/9490512) | [Link](https://github.com/qdushl/Waterloo-Point-Cloud-Database-2.0) |
| 5 | WPC3.0 (Compression) | [No-reference Bitstream-layer Model for Perceptual Quality Assessment of V-PCC Encoded Point Clouds](https://ieeexplore.ieee.org/document/9782549) | [Link](https://github.com/qdushl/Waterloo-Point-Cloud-Database-3.0) |
| 6 | CPCD2.0 (Compression and Noise) | [TGP-PCQA: Texture and geometry projection based quality assessment for colored point clouds](https://www.sciencedirect.com/science/article/pii/S1047320322000128) | [Link](https://github.com/cherry0415/CPCD2.0) |
| 7 | ICIP2020 | [Quality Evaluation Of Static Point Clouds Encoded Using MPEG Codecs](https://ieeexplore.ieee.org/abstract/document/9191308) | - |
| 8 | M-PCCD | [A comprehensive study of the rate-distortion performance in MPEG point cloud compression](https://www.nowpublishers.com/article/Details/SIP-132) | - |
| 9 | IRPC | [Point Cloud Rendering after Coding: Impacts on Subjective and Objective Quality](https://ieeexplore.ieee.org/abstract/document/9257015/) | - |
| 10 | SIAT-PCQD | [Subjective Quality Database and Objective Study of Compressed Point Clouds With 6DoF Head-Mounted Display](https://ieeexplore.ieee.org/abstract/document/9502695) | [Link](https://dx.doi.org/10.21227/ad8d-7r28) |
| 11 | vsenseVVDB (Volumetric Video Quality Database #1) | [Subjective and Objective Quality Assessment for Volumetric Video Compression](https://v-sense.scss.tcd.ie/research/6dof/quality-assessment-for-fvv-compression/) | [Link](https://v-sense.scss.tcd.ie/research/6dof/quality-assessment-for-fvv-compression/) |
| 12 | vsenseVVDB2 (Volumetric Video Quality Database #2) | [Textured mesh vs coloured point cloud: A subjective study for volumetric video compression](https://ieeexplore.ieee.org/abstract/document/9123137/) | [Link](https://v-sense.scss.tcd.ie/research/6dof/quality-assessment-for-fvv-compression/) |
| 13 | BASICS | [BASICS: Broad quality Assessment of Static point clouds In Compression Scenarios](https://arxiv.org/pdf/2302.04796.pdf) | - |
| 14 | PointQ-Bench | [PointQ-Bench: Benchmarking Diagnostic and Interpretable Point Cloud Quality Assessment](https://arxiv.org/abs/2605.28241) | - |

### Mesh Quality Assessment Datasets

| # | Dataset | Paper | Dataset Link |
|---:|---|---|---|
| 1 | CMDM | [Visual Quality of 3D Meshes With Diffuse Colors in Virtual Reality: Subjective and Objective Evaluation](https://ieeexplore.ieee.org/abstract/document/9252120) | [Link](https://yananehme.github.io) |
| 2 | TMQA | [Textured Mesh Quality Assessment: Large-Scale Dataset and Deep Learning-based Quality Metric](https://yananehme.github.io/publications/2022-ACM-TOG) | [Link](https://yananehme.github.io/publications/2022-ACM-TOG) |
| 3 | Geo-Metric | [Geo-Metric: A Perceptual Dataset of Distortions on Faces](https://dl.acm.org/doi/abs/10.1145/3550454.3555475) | [Link](https://github.com/facebookresearch/Geo-metric) |
| 4 | SJTU-TMQA | [SJTU-TMQA: A quality assessment database for static mesh with texture map](https://arxiv.org/abs/2309.15675) | [Link](https://ccccby.github.io/) |

### Digital Human Quality Assessment Datasets

| # | Dataset | Paper | Dataset Link |
|---:|---|---|---|
| 1 | DHHQA | [Perceptual Quality Assessment for Digital Human Heads](https://arxiv.org/abs/2209.09489) | [Link](https://github.com/zzc-1998/DHHQA) |
| 2 | DDH-QA | [DDH-QA: A Dynamic Digital Humans Quality Assessment Database](https://arxiv.org/pdf/2212.12734.pdf) | [Link](https://github.com/zzc-1998/DDH-QA) |
| 3 | SJTU-H3D | [Advancing Zero-Shot Digital Human Quality Assessment through Text-Prompted Evaluation](https://arxiv.org/abs/2307.02808) | [Link](https://github.com/zzc-1998/SJTU-H3D) |

## Methods

### Basic Full-Reference PCQA

This repository provides Python implementations of basic full-reference quality assessment metrics, including p2point, p2plane, and PSNR-yuv.

The implementations are based on the following works:

- [Evaluation criteria for PCC (Point Cloud Compression)](https://mpeg.chiariglione.org/standards/mpeg-i/point-cloud-compression/evaluation-criteria-pcc)
- [Dynamic Polygon Clouds: Representation and Compression for VR/AR](https://www.cambridge.org/core/journals/apsipa-transactions-on-signal-and-information-processing/article/dynamic-polygon-clouds-representation-and-compression-for-vrar/A83EFCDBEF825DA5DC2A08308B6E21BE)
- [Geometric Distortion Metrics for Point Cloud Compression](https://ieeexplore.ieee.org/document/8296925)

### Full-Reference PCQA Metrics

| # | Metric | Paper | Code |
|---:|---|---|---|
| 1 | PointSSIM | [Towards a Point Cloud Structural Similarity Metric](https://ieeexplore.ieee.org/abstract/document/9106005) | [Code](https://github.com/mmspg/pointssim) |
| 2 | GraphSIM | [Inferring Point Cloud Quality via Graph Similarity](http://arxiv.org/abs/2006.00497) | [Code](https://github.com/NJUVISION/GraphSIM) |
| 3 | PCQM | [PCQM: A Full-Reference Quality Metric for Colored 3D Point Clouds](https://ieeexplore.ieee.org/document/9123147) | [Code](https://github.com/MEPP-team/PCQM) |

### Reduced-Reference PCQA Metrics

| # | Metric | Paper | Code |
|---:|---|---|---|
| 1 | PCMrr | [A Reduced Reference Metric for Visual Quality Evaluation of Point Cloud Contents](https://ieeexplore.ieee.org/abstract/document/9198142) | [Code](https://github.com/cwi-dis/PCM_RR) |
| 2 | - | [Reduced Reference Quality Assessment for Point Cloud Compression](https://arxiv.org/pdf/2301.01009.pdf) | - |
| 3 | RR-CAP | [Reduced-Reference Quality Assessment of Point Clouds via Content-Oriented Saliency Projection](https://arxiv.org/abs/2301.07681) | [Code](https://github.com/weizhou-geek/RR-CAP) |
| 4 | - | [Support Vector Regression-based Reduced-Reference Perceptual Quality Model for Compressed Point Clouds](https://ieeexplore.ieee.org/abstract/document/10375131) | - |

### No-Reference PCQA Metrics

| # | Metric | Paper | Code |
|---:|---|---|---|
| 1 | 3D-NSS | [No-Reference Quality Assessment for 3D Colored Point Cloud and Mesh Models](https://ieeexplore.ieee.org/document/9810024) [[Arxiv]](https://arxiv.org/abs/2107.02041) | [Code](https://github.com/zzc-1998/NR-3DQA) |
| 2 | ResSCNN | [Point Cloud Quality Assessment: Dataset Construction and Learning-based No-Reference Approach](https://arxiv.org/pdf/2012.11895.pdf) | [Code](https://github.com/lyp22/ResSCNN) |
| 3 | IT-PCQA | [No-Reference Point Cloud Quality Assessment via Domain Adaptation](https://openaccess.thecvf.com/content/CVPR2022/papers/Yang_No-Reference_Point_Cloud_Quality_Assessment_via_Domain_Adaptation_CVPR_2022_paper.pdf) | [Code](https://github.com/lyp22/IT-PCQA) |
| 4 | 3D-CNN-PCQA | [A No-reference Quality Assessment Metric for Point Cloud Based on Captured Video Sequences](https://arxiv.org/abs/2206.05054) | - |
| 5 | VQA-PC | [Evaluating Point Cloud from Moving Camera Videos: A No-Reference Metric](https://arxiv.org/abs/2208.14085) | [Code](https://github.com/zzc-1998/VQA_PC) |
| 6 | - | [Blind Quality Assessment of 3D Dense Point Clouds with Structure Guided Resampling](https://arxiv.org/abs/2208.14603) | - |
| 7 | MM-PCQA | [MM-PCQA: Multi-Modal Learning for No-reference Point Cloud Quality Assessment](https://arxiv.org/abs/2209.00244) | [Code](https://github.com/zzc-1998/MM-PCQA) |
| 8 | - | [V-PCC Projection Based Blind Point Cloud Quality Assessment for Compression Distortion](https://ieeexplore.ieee.org/document/9881542) | - |
| 9 | GPA-Net | [GPA-Net: No-Reference Point Cloud Quality Assessment with Multi-task Graph Convolutional Network](https://arxiv.org/abs/2210.16478) | [Code](https://github.com/Slowhander/GPA-Net) |
| 10 | PQA-Net | [PQA-Net: Deep No Reference Point Cloud Quality Assessment via Multi-View Projection](https://ieeexplore.ieee.org/document/9496633) | [Code](https://github.com/qdushl/PQA-Net) |
| 11 | - | [Progressive Knowledge Transfer Based on Human Visual Perception Mechanism for Perceptual Quality Assessment of Point Clouds](https://arxiv.org/abs/2211.16646) | - |
| 12 | - | [Bitstream-based Perceptual Quality Assessment of Compressed 3D Point Clouds](https://ieeexplore.ieee.org/abstract/document/10061856?casa_token=hh3eIB-ggm8AAAAA:wIXnZG4sBOPW-ZY1XZA0Z3TtpbQDhRbwqQUcijdTRwHIjEb1OEakhcN5_2HV38IYg_1oW5_rjfY) | - |
| 13 | GMS-3DQA | [GMS-3DQA: Projection-based Grid Mini-patch Sampling for 3D Model Quality Assessment](https://arxiv.org/pdf/2306.05658.pdf) | [Code](https://github.com/zzc-1998/GMS-3DQA) |
| 14 | - | [Once-Training-All-Fine: No-Reference Point Cloud Quality Assessment via Domain-relevance Degradation Description](https://arxiv.org/abs/2307.01567) | - |
| 15 | - | [Pseudo-Reference Point Cloud Quality Measurement Based on Joint 2-D and 3-D Distortion Description](https://ieeexplore.ieee.org/abstract/document/10167694) | - |
| 16 | pmBQA | [pmBQA: Projection-based Blind Point Cloud Quality Assessment via Multimodal Learning](https://dl.acm.org/doi/abs/10.1145/3581783.3611998) | - |
| 17 | - | [Non-Local Geometry and Color Gradient Aggregation Graph Model for No-Reference Point Cloud Quality Assessment](https://dl.acm.org/doi/abs/10.1145/3581783.3612169) | - |
| 18 | - | [Simple Baselines for Projection-based Full-reference and No-reference Point Cloud Quality Assessment](https://arxiv.org/abs/2310.17147) | - |
| 19 | Plain-PCQA | [Plain-PCQA: No-Reference Point Cloud Quality Assessment by Analysis of Plain Visual and Geometrical Components](https://ieeexplore.ieee.org/document/10381826) | - |
| 20 | MOD-PCQA | [Zoom to Perceive Better: No-reference Point Cloud Quality Assessment via Exploring Effective Multiscale Feature](https://ieeexplore.ieee.org/document/10422856) | [Code](https://openi.pcl.ac.cn/OpenPointCloud/MOD-PCQA) |
| 21 | PAME | [PAME: Self-Supervised Masked Autoencoder for No-Reference Point Cloud Quality Assessment](https://arxiv.org/pdf/2403.10061.pdf) | - |
| 22 | - | [Contrastive Pre-Training with Multi-View Fusion for No-Reference Point Cloud Quality Assessment](https://arxiv.org/pdf/2403.10066.pdf) | - |
| 23 | MFT-PCQA | [MFT-PCQA: Multi-Modal Fusion Transformer for No-Reference Point Cloud Quality Assessment](https://ieeexplore.ieee.org/abstract/document/10445736) | - |
| 24 | - | [Rating-Augmented No-Reference Point Cloud Quality Assessment Using Multi-Task Learning](https://ieeexplore.ieee.org/abstract/document/10448511) | - |
| 25 | 3DTA | [3DTA: No-Reference 3D Point Cloud Quality Assessment with Twin Attention](https://ieeexplore.ieee.org/abstract/document/10542438) | [Code](https://github.com/philox12358/3DTA-PCQA) |
| 26 | - | [Compressed Point Cloud Quality Index by Combining Global Appearance and Local Details](https://dl.acm.org/doi/abs/10.1145/3672567) | - |
| 27 | AFNet | [Asynchronous Feedback Network for Perceptual Point Cloud Quality Assessment](https://arxiv.org/pdf/2407.09806) | [Code](https://github.com/zhangyujie-1998/AFNet) |
| 28 | TCDM | [TCDM: Transformational Complexity Based Distortion Metric for Perceptual Point Cloud Quality Assessment](https://ieeexplore.ieee.org/abstract/document/10337742) | [Code](https://github.com/zyj1318053/TCDM) |
| 29 | LMM-PCQA | [LMM-PCQA: Assisting Point Cloud Quality Assessment with LMM](https://arxiv.org/abs/2404.18203) | [Code](https://github.com/Q-Future/LMM-PCQA) |
| 30 | - | [LLM-guided Cross-Modal Point Cloud Quality Assessment: A Graph Learning Approach](https://ieeexplore.ieee.org/abstract/document/10660545) | - |
| 31 | - | [Visual-Saliency Guided Multi-modal Learning for No Reference Point Cloud Quality Assessment](https://dl.acm.org/doi/abs/10.1145/3689093.3689183) | - |
| 32 | - | [Perceptual Quality Assessment of Trisoup-Lifting Encoded 3D Point Clouds](https://arxiv.org/abs/2410.06689) | - |
| 33 | - | [No-Reference Point Cloud Quality Assessment Through Structure Sampling and Clustering Based on Graph](https://ieeexplore.ieee.org/abstract/document/10737898/) | - |
| 34 | - | [No-reference point cloud quality assessment via graph convolutional network](https://orca.cardiff.ac.uk/id/eprint/172907/) | - |
| 35 | CLIP-PCQA | [CLIP-PCQA: Exploring Subjective-Aligned Vision-Language Modeling for Point Cloud Quality Assessment](https://arxiv.org/abs/2501.10071) | - |
| 36 | - | [Information Exploration of Projected Views for Point Cloud Quality Measurement](https://ieeexplore.ieee.org/abstract/document/10841467) | - |
| 37 | CMDC-PCQA | [CMDC-PCQA: No-Reference Point Cloud Quality Assessment via a Cross-Modal Deep-Coupling Framework](https://ieeexplore.ieee.org/abstract/document/10884925) | - |
| 38 | - | [No-reference geometry quality assessment for colorless point clouds via list-wise rank learning](https://www.sciencedirect.com/science/article/abs/pii/S0097849325000159) | - |
| 39 | DHCN | [Dynamic Hypergraph Convolutional Network for No-Reference Point Cloud Quality Assessment](https://ieeexplore.ieee.org/abstract/document/10549980) | [Code](https://github.com/chenwuwq/DHCN) |
| 40 | DQP-PCQA | [DQP-PCQA: Deep Quantization Parameters Bring New Insight to Point Cloud Quality Assessment](https://ieeexplore.ieee.org/abstract/document/11078383/) | - |
| 41 | - | [Perception-Weighted Multi-View Point Cloud Quality Assessment with Saliency-Guided Coverage Analysis](https://ieeexplore.ieee.org/abstract/document/11081825) | - |
| 42 | MPV-PCQA | [Mpv-pcqa: multimodal no-reference point cloud quality assessment via point cloud and captured dynamic video](https://link.springer.com/article/10.1007/s00530-025-01887-2) | - |
| 43 | COPP-Net | [COPP-Net: No-Reference Point Cloud Quality Assessment via Weighted Patch Quality Prediction](https://ieeexplore.ieee.org/abstract/document/11131459/) | [Code](https://github.com/philox12358/COPP-Net) |
| 44 | BMPCQA | [BMPCQA: Bioinspired Metaverse Point Cloud Quality Assessment Based on Large Multimodal Models](https://advanced.onlinelibrary.wiley.com/doi/abs/10.1002/aisy.202500504) | [Code](https://github.com/IntMeGroup/BMPCQA) |
| 45 | UPDA | [UPDA: Unsupervised Progressive Domain Adaptation for No-Reference Point Cloud Quality Assessment](https://arxiv.org/abs/2602.11969) | - |
| 46 | DPR-Net | [DPR-Net: dual-branch probabilistic regression for no-reference point cloud quality assessment](https://link.springer.com/article/10.1007/s00530-025-02167-9) | - |
| 47 | EGMS-PCQM | [EGMS-PCQM: Entropy-Guided Multiscale Sampling based Dual-net for No-Reference Point Cloud Quality Measurement](https://ieeexplore.ieee.org/abstract/document/11408287) | [Code](https://github.com/ll2s/EGMS-PCQM) |
| 48 | QD-PCQA | [QD-PCQA: Quality-Aware Domain Adaptation for Point Cloud Quality Assessment](https://arxiv.org/abs/2603.03726) | [Code](https://github.com/huhu-code/QD-PCQA) |
| 49 | PIT-QMM | [PIT-QMM: A Large Multimodal Model For No-Reference Point Cloud Quality Assessment](https://arxiv.org/abs/2510.07636) | [Code](https://github.com/shngt/pit-qmm) |

### Mesh QA Metrics

| # | Method | Paper | Code |
|---:|---|---|---|
| 1 | - | [Surface-Sampling Based Objective Quality Assessment Metrics for Meshes](https://ieeexplore.ieee.org/document/10096048) | - |

## Contact

If you would like to contribute resources, include your work, or discuss related topics, please contact zzc1998@sjtu.edu.cn.

If this collection is helpful to your research, please consider starring the project.
