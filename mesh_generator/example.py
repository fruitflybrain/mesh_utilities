from generate_mesh import *

points = np.random.randn(1000,3) # Point cloud input here
alpha = 1. # Play with this parameter to change parameters of the extracted mesh
generate_mesh(points, name="output.json", alpha=alpha) # Processes and saves the mesh as output.json