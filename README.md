# Robotics-Vision
*Implementations and explorations of several pipelines and algorithms in Robotic Vision, as part of the Mobile Robotics (Monsoon 2023) class.*


<p align="center">
  <img src="https://user-images.githubusercontent.com/43912285/105778545-9aafab80-5f92-11eb-8451-2cd011412f9d.png" width=400>
</p>


## Contents

### Transformations-And-Mapping
This set consists implementations of: 
1) **Euclidean transformations.**
2) **Ways of representing rotations** , **interpolation between rotation matrices using SLERP.**
3) **Waypoint generation and trajectory visualization for the letter _M_.** 
4) **3D Mapping from RGBD Data with a specific scene in AI2Thor, creation of a point cloud of the scene and generating Occupancy Grid Maps of the environment from different heights.**

### ICP-SLAM and Pose Graph Optimization
This set consists implementations of:
1) **Non-Linear least squares optimization for Gaussian Function using Levenberg Marquardt (LM) algorithm.** 
2) **Procrustes alignment on two point clouds with (given) known correspondences**
3) **ICP algorithm with unknown correspondences.**
4) **Pose Graph Optimization:**
    - *PGO for 1D SLAM*
    - *PGO for 2D SLAM*
    - *Trajectory Evaluation and g2o optimization*

### Vision
This set consists implementations of:
1) **Estimation of fundamental matrix and plotting epipolar lines and epipole given two images of the same scene taken from different view-points.**
2) **Visual Odometry: recovering the egomotion (the trajectory) of an agent using only the input from the camera or a system of cameras attached to the agent.**
    1) *Feature extraction using SIFT detector.*
    2) *Estimation of essential matrix within RANSAC scheme.*
    3) *Obtaining transformations and plotting both ground-truth and calculated trajectories.*
3) **Stereo Dense Reconstruction: generating a dense 3D point cloud reconstruction of a scene from stereo images.** 