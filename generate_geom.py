import numpy as np
from stl import mesh


    
# import shells, obstruction and source
def load_geom(file_shell,file_source,file_reflector,file_obs_source,file_obs_reflector,geom_dir = '/p/ltxdata/Li_evporator/Li_Evap_Source/Fortran_Source/CAD_Source/geom_mark2'):
    shells = mesh.Mesh.from_file(file_shell)
    source = mesh.Mesh.from_file(file_source)
    reflector = mesh.Mesh.from_file(file_reflector)
    obs_source = mesh.Mesh.from_file(file_obs_source)
    obs_reflector = mesh.Mesh.from_file(file_obs_reflector)
    
    shells = mesh.Mesh.from_file(file_shell)
    source = mesh.Mesh.from_file(file_source)
    reflector = mesh.Mesh.from_file(file_reflector)
    obs_source = mesh.Mesh.from_file(file_obs_source)
    obs_reflector = mesh.Mesh.from_file(file_obs_reflector)

    elem = np.size(shells.areas)

    with open(f"{geom_dir}/target.x.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(shells.x[i][0]) + "\t" + str(shells.x[i][1]) + "\t" + str(shells.x[i][2]) + "\n")
            
    with open(f"{geom_dir}/target.y.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(shells.y[i][0]) + "\t" + str(shells.y[i][1]) + "\t" + str(shells.y[i][2]) + "\n")

    with open(f"{geom_dir}/target.z.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(shells.z[i][0]) + "\t" + str(shells.z[i][1]) + "\t" + str(shells.z[i][2]) + "\n")

    with open(f"{geom_dir}/target.norm.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(shells.normals[i][0]) + "\t" + str(shells.normals[i][1]) + "\t" + str(shells.normals[i][2]) + "\n")
            
    with open(f"{geom_dir}/target.areas.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(shells.areas[i]) + "\n")
            
    with open(f"{geom_dir}/target.centroids.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(shells.centroids[i][0]) + "\t" + str(shells.centroids[i][1]) + "\t" + str(shells.centroids[i][2]) + "\n")
            
            
    elem = np.size(source.areas)

    with open(f"{geom_dir}/source.x.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(source.x[i][0]) + "\t" + str(source.x[i][1]) + "\t" + str(source.x[i][2]) + "\n")

    with open(f"{geom_dir}/source.y.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(source.y[i][0]) + "\t" + str(source.y[i][1]) + "\t" + str(source.y[i][2]) + "\n")

    with open(f"{geom_dir}/source.z.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(source.z[i][0]) + "\t" + str(source.z[i][1]) + "\t" + str(source.z[i][2]) + "\n")

    with open(f"{geom_dir}/source.norm.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(source.normals[i][0]) + "\t" + str(source.normals[i][1]) + "\t" + str(source.normals[i][2]) + "\n")
            
    with open(f"{geom_dir}/source.areas.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(source.areas[i]) + "\n")
    
    with open(f"{geom_dir}/source.centroids.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(source.centroids[i][0]) + "\t" + str(source.centroids[i][1]) + "\t" + str(source.centroids[i][2]) + "\n")

    elem = np.size(reflector.areas)

    with open(f"{geom_dir}/reflector.x.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(reflector.x[i][0]) + "\t" + str(reflector.x[i][1]) + "\t" + str(reflector.x[i][2]) + "\n")
            
    with open(f"{geom_dir}/reflector.y.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(reflector.y[i][0]) + "\t" + str(reflector.y[i][1]) + "\t" + str(reflector.y[i][2]) + "\n")
            
    with open(f"{geom_dir}/reflector.z.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(reflector.z[i][0]) + "\t" + str(reflector.z[i][1]) + "\t" + str(reflector.z[i][2]) + "\n")
            
    with open(f"{geom_dir}/reflector.norm.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(reflector.normals[i][0]) + "\t" + str(reflector.normals[i][1]) + "\t" + str(reflector.normals[i][2]) + "\n")
            
    with open(f"{geom_dir}/reflector.areas.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(reflector.areas[i]) + "\n")
            
    with open(f"{geom_dir}/reflector.centroids.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(reflector.centroids[i][0]) + "\t" + str(reflector.centroids[i][1]) + "\t" + str(reflector.centroids[i][2]) + "\n")
        
            
    elem = np.size(obs_source.areas)

    with open(f"{geom_dir}/obs_source.x.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(obs_source.x[i][0]) + "\t" + str(obs_source.x[i][1]) + "\t" + str(obs_source.x[i][2]) + "\n")
            
    with open(f"{geom_dir}/obs_source.y.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(obs_source.y[i][0]) + "\t" + str(obs_source.y[i][1]) + "\t" + str(obs_source.y[i][2]) + "\n")
            
    with open(f"{geom_dir}/obs_source.z.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(obs_source.z[i][0]) + "\t" + str(obs_source.z[i][1]) + "\t" + str(obs_source.z[i][2]) + "\n")
            
    with open(f"{geom_dir}/obs_source.norm.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(obs_source.normals[i][0]) + "\t" + str(obs_source.normals[i][1]) + "\t" + str(obs_source.normals[i][2]) + "\n")
            
    with open(f"{geom_dir}/obs_source.areas.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(obs_source.areas[i]) + "\n")
            
    with open(f"{geom_dir}/obs_source.centroids.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(obs_source.centroids[i][0]) + "\t" + str(obs_source.centroids[i][1]) + "\t" + str(obs_source.centroids[i][2]) + "\n")
            
    elem = np.size(obs_reflector.areas)

    with open(f"{geom_dir}/obs_reflector.x.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(obs_reflector.x[i][0]) + "\t" + str(obs_reflector.x[i][1]) + "\t" + str(obs_reflector.x[i][2]) + "\n")

    with open(f"{geom_dir}/obs_reflector.y.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(obs_reflector.y[i][0]) + "\t" + str(obs_reflector.y[i][1]) + "\t" + str(obs_reflector.y[i][2]) + "\n")
            
    with open(f"{geom_dir}/obs_reflector.z.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(obs_reflector.z[i][0]) + "\t" + str(obs_reflector.z[i][1]) + "\t" + str(obs_reflector.z[i][2]) + "\n")
            
    with open(f"{geom_dir}/obs_reflector.norm.DAT","w") as X:   
        for i in range(0,elem):
            X.write(str(obs_reflector.normals[i][0]) + "\t" + str(obs_reflector.normals[i][1]) + "\t" + str(obs_reflector.normals[i][2]) + "\n")    
    
    with open(f"{geom_dir}/obs_reflector.areas.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(obs_reflector.areas[i]) + "\n")
            
    with open(f"{geom_dir}/obs_reflector.centroids.DAT","w") as X:
        for i in range(0,elem):
            X.write(str(obs_reflector.centroids[i][0]) + "\t" + str(obs_reflector.centroids[i][1]) + "\t" + str(obs_reflector.centroids[i][2]) + "\n")
            
    print("Following Geom files generated")
    print(f"{np.size(shells.areas)} elements -->", "shells.x.DAT","shells.y.DAT", "shells.z.DAT", "shells.norm.DAT", "shells.areas.DAT", "shells.centroids.DAT")
    print(f"{np.size(source.areas)} elements -->", "source.x.DAT","source.y.DAT", "source.z.DAT", "source.norm.DAT", "source.areas.DAT", "source.centroids.DAT")
    print(f"{np.size(reflector.areas)} elements -->", "reflector.x.DAT","reflector.y.DAT", "reflector.z.DAT", "reflector.norm.DAT", "reflector.areas.DAT", "reflector.centroids.DAT")
    print(f"{np.size(obs_source.areas)} elements -->", "obs_source.x.DAT","obs_source.y.DAT", "obs_source.z.DAT", "obs_source.norm.DAT", "obs_source.areas.DAT", "obs_source.centroids.DAT")
    print(f"{np.size(obs_reflector.areas)} elements -->", "obs_reflector.x.DAT","obs_reflector.y.DAT", "obs_reflector.z.DAT", "obs_reflector.norm.DAT")
    return 

def extract_faces(file='/p/ltxdata/Li_evporator/Li_Evap_Source/Fortran_Source/CAD_Source/shell_2024.stl',output='/p/ltxdata/Li_evporator/Li_Evap_Source/Fortran_Source/CAD_Source/shell_mod.stl'):
    # Extract the faces of the shell, given that the faces were stored with the 'canary' color attribute
    shell_og = mesh.Mesh.from_file(file)
    #idx = np.where(shell_og.data['attr'] > 6000)[0]
    idx = np.where(shell_og.data['attr']!=8833)[0]
    norm = np.delete(shell_og.data['normals'], idx, axis=0)
    vectors = np.delete(shell_og.data['vectors'], idx, axis=0)
    attr = np.delete(shell_og.data['attr'], idx, axis=0)
    areas = np.delete(shell_og._areas, idx, axis=0)
    centroids = np.delete(shell_og._centroids, idx, axis=0)
    shell_mod = mesh.Mesh(np.zeros(vectors.shape[0], dtype=mesh.Mesh.dtype))
    shell_mod.vectors = vectors
    shell_mod.normals = norm
    shell_mod.areas = areas
    shell_mod.centroids = centroids
    # print number of faces
    print(f'Total {len(areas)} detected')
    shell_mod.save(f'{output}')
    return