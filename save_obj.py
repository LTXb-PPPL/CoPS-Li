import trimesh 
import numpy as np

mesh = trimesh.load_mesh('/p/ltxdata/Li_evporator/Li_Evap_Source/Fortran_Source/CAD_Source/shell_mod_coarse_faces_2024.stl')
thickness_ro = np.zeros(len(mesh.faces))
# read LTX_SO.txt and LTX_RO_true.txt to get deposition on faces
with open('LTX_R0.txt') as f:
    lines = f.readlines()
    # read second column of the file
    for i,line in enumerate(lines):
        thickness_ro[i] = float(line.split()[1])
thickness_so = np.zeros(len(mesh.faces))
with open('LTX_SO.txt') as f:
    lines = f.readlines()
    # read second column of the file
    for i,line in enumerate(lines):
        thickness_so[i] = float(line.split()[1])
        
thickness = thickness_ro + thickness_so
faces_to_color = np.arange(len(mesh.faces)).tolist()
color = trimesh.visual.interpolate(thickness, color_map='coolwarm')
# set to white if thickness is zero
color[thickness==0.0] = [255,255,255,255]
mesh.visual.face_colors[faces_to_color] = color[faces_to_color]

source_mesh = trimesh.load_mesh('/p/ltxdata/Li_evporator/Li_Evap_Source/Fortran_Source/CAD_Source/rounded_source.stl')

source_obs = '/p/ltxdata/Li_evporator/Li_Evap_Source/Fortran_Source/CAD_Source/obs_source.stl'
source_obs_mesh = trimesh.load_mesh(source_obs)
source_obs_mesh.visual.face_colors = [0,0,255,255]


# add the two meshes together into a single obj and export
combined_mesh = mesh + source_mesh + source_obs_mesh 

combined_mesh.export('deposition_new.obj')
