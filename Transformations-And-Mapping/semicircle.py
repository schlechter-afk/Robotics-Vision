import open3d as o3d
import numpy as np

# Define parameters
radius = 20.0  # Radius of the semicircle
center = np.array([20.0, 60.0, 0.0])  # Center of the semicircle
num_points = 100  # Number of points in the point cloud

# Generate points along the semicircle
theta = np.linspace(0, np.pi, num_points)
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)
z = center[2] * np.ones_like(x)

# Create a numpy array for the points
points = np.column_stack((x, y, z))
<<<<<<< HEAD
# reverse the above point array
points = points[::-1]
=======
# reverse the above numpy array
points = points[::-1]
for point in points:
    print(point)
>>>>>>> refs/remotes/origin/main

# Create an Open3D point cloud
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)

# Visualize the point cloud
o3d.visualization.draw_geometries([point_cloud])