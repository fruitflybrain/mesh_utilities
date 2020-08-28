# Mesh Utilities
This repository contains scripts for generating neuropil meshes for NeuroNLP and FlyBrainLab.

# Installation Instructions

On a Python 3.6 environment, run

```
pip install pyvista
```
to install pyvista.

# Examples

The file mesh_generator/stl_2_ffbo_mesh.py can be run as follows to convert a mesh from the .stl format to .json:
```
python stl_2_ffbo_mesh.py -i _temp_mesh.stl -o out.json
```

To generate a mesh from point cloud input, check out mesh_generator/example.py as a starting point:
```
python example.py
```
You may want to open the generated mesh _temp_mesh.stl in an application like MeshLab for further improvements before conversion to .json.