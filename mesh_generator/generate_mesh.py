import numpy as np
import pyvista as pv
from stl_2_ffbo_mesh import *

def generate_mesh(points, name="output.json", alpha=1.):
    cloud = pv.PolyData(points)
    vol = cloud.delaunay_3d(alpha = alpha)
    generated_mesh = vol.extract_geometry()
    pv.save_meshio("_temp_mesh.stl", generated_mesh)
    stl_to_ffbo_json("_temp_mesh.stl", name)