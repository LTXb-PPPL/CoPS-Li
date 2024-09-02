import os


def geometry(geo_dir):
    # read shells.x, shells.y, shells.z and shells.norm, each of them has 3 columns, tab separated
    x, y, z, = [], [], []
    p1, p2, p3 = [], [], []
    norm = []
    centroid = []   
    areas = []
    with open(os.path.join(geo_dir, "target.x.DAT")) as f:
        for line in f:
            x.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "target.y.DAT")) as f:
        for line in f:
            y.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "target.z.DAT")) as f:
        for line in f:
            z.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "target.norm.DAT")) as f:
        for line in f:
            norm.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "target.centroids.DAT")) as f:
        for line in f:
            centroid.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "target.areas.DAT")) as f:
        for line in f:
            areas.append(float(line.strip()[1]))
    for x1, y1, z1 in zip(x, y, z):
        p1.append([x1[0],y1[0],z1[0]])
        p2.append([x1[1],y1[1],z1[1]])
        p3.append([x1[2],y1[2],z1[2]])
        
                        
    # read source.x, source.y, source.z and source.norm, each of them has 3 columns, tab separated
    source_x, source_y, source_z, = [], [], []
    source_p1, source_p2, source_p3 = [], [], []
    source_norm = []
    source_centroid = []
    source_areas = []
    with open(os.path.join(geo_dir, "source.x.DAT")) as f:
        for line in f:
            source_x.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "source.y.DAT")) as f:
        for line in f:
            source_y.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "source.z.DAT")) as f:
        for line in f:
            source_z.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "source.norm.DAT")) as f:
        for line in f:
            source_norm.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "source.centroids.DAT")) as f:
        for line in f:
            source_centroid.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "source.areas.DAT")) as f:
        for line in f:
            source_areas.append(float(line.strip()[1]))
            
    for x1, y1, z1 in zip(source_x, source_y, source_z):
        source_p1.append([x1[0],y1[0],z1[0]])
        source_p2.append([x1[1],y1[1],z1[1]])
        source_p3.append([x1[2],y1[2],z1[2]])
    
                               
    # read reflector.x, reflector.y, reflector.z and reflector.norm, each of the)m has 3 columns, tab separated
    reflector_x, reflector_y, reflector_z, = [], [], []
    reflector_p1, reflector_p2, reflector_p3 = [], [], []
    reflector_norm = []
    reflector_centroid = []
    reflector_areas = []
    with open(os.path.join(geo_dir, "reflector.x.DAT")) as f:
        for line in f:
            reflector_x.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "reflector.y.DAT")) as f:
        for line in f:
            reflector_y.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "reflector.z.DAT")) as f:
        for line in f:
            reflector_z.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "reflector.norm.DAT")) as f:
        for line in f:
            reflector_norm.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "reflector.centroids.DAT")) as f:
        for line in f:
            reflector_centroid.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "reflector.areas.DAT")) as f:
        for line in f:
            reflector_areas.append(float(line.strip()[1]))
    
    for x1, y1, z1 in zip(reflector_x, reflector_y, reflector_z):
        reflector_p1.append([x1[0],y1[0],z1[0]])
        reflector_p2.append([x1[1],y1[1],z1[1]])
        reflector_p3.append([x1[2],y1[2],z1[2]])
                                  
    # read obs_source.x, obs_source.y, obs_source.z and obs_source.norm, each of) them has 3 columns, tab separated
    obs_source_x, obs_source_y, obs_source_z, = [], [], []
    obs_source_p1, obs_source_p2, obs_source_p3 = [], [], []
    obs_source_norm = []
    obs_source_centroid = []
    obs_source_areas = []
    with open(os.path.join(geo_dir, "obs_source.x.DAT")) as f:
        for line in f:
            obs_source_x.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "obs_source.y.DAT")) as f:
        for line in f:
            obs_source_y.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "obs_source.z.DAT")) as f:
        for line in f:
            obs_source_z.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "obs_source.norm.DAT")) as f:
        for line in f:
            obs_source_norm.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "obs_source.centroids.DAT")) as f:
        for line in f:
            obs_source_centroid.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "obs_source.areas.DAT")) as f:
        for line in f:
            obs_source_areas.append(float(line.strip()[1]))
    
    for x1, y1, z1 in zip(obs_source_x, obs_source_y, obs_source_z):
        obs_source_p1.append([x1[0],y1[0],z1[0]])
        obs_source_p2.append([x1[1],y1[1],z1[1]])
        obs_source_p3.append([x1[2],y1[2],z1[2]])
    
                                   
    # read obs_reflector.x, obs_reflector.y, obs_reflector.z and obs_reflector.n)orm, each of them has 3 columns, tab separated
    obs_reflector_x, obs_reflector_y, obs_reflector_z, = [], [], []
    obs_reflector_p1, obs_reflector_p2, obs_reflector_p3 = [], [], []
    obs_reflector_norm = []
    obs_reflector_centroid = []
    obs_reflector_areas = []
    with open(os.path.join(geo_dir, "obs_reflector.x.DAT")) as f:
        for line in f:
            obs_reflector_x.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "obs_reflector.y.DAT")) as f:
        for line in f:
            obs_reflector_y.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "obs_reflector.z.DAT")) as f:
        for line in f:
            obs_reflector_z.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "obs_reflector.norm.DAT")) as f:
        for line in f:
            obs_reflector_norm.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "obs_reflector.centroids.DAT")) as f:
        for line in f:
            obs_reflector_centroid.append(list(map(float, line.strip().split("\t"))))
    with open(os.path.join(geo_dir, "obs_reflector.areas.DAT")) as f:
        for line in f:
            obs_reflector_areas.append(float(line.strip()[1]))
    
    for x1, y1, z1 in zip(obs_reflector_x, obs_reflector_y, obs_reflector_z):
        obs_reflector_p1.append([x1[0],y1[0],z1[0]])
        obs_reflector_p2.append([x1[1],y1[1],z1[1]])
        obs_reflector_p3.append([x1[2],y1[2],z1[2]])

# return as a dict
    return {
        "target": {
            "x": x,
            "y": y,
            "z": z,
            "p1": p1,
            "p2": p2,
            "p3": p3,
            "norm": norm,
            "centroid": centroid,
            "areas": areas
        },
        "source": {
            "x": source_x,
            "y": source_y,
            "z": source_z,
            "p1": source_p1,
            "p2": source_p2,
            "p3": source_p3,
            "norm": source_norm,
            "centroid": source_centroid,
            "areas": source_areas
        },
        "reflector": {
            "x": reflector_x,
            "y": reflector_y,
            "z": reflector_z,
            "p1": reflector_p1,
            "p2": reflector_p2,
            "p3": reflector_p3,
            "norm": reflector_norm,
            "centroid": reflector_centroid,
            "areas": reflector_areas
        },
        "obs_source": {
            "x": obs_source_x,
            "y": obs_source_y,
            "z": obs_source_z,
            "p1": obs_source_p1,
            "p2": obs_source_p2,
            "p3": obs_source_p3,
            "norm": obs_source_norm,
            "centroid": obs_source_centroid,
            "areas": obs_source_areas
        },
        "obs_reflector": {
            "x": obs_reflector_x,
            "y": obs_reflector_y,
            "z": obs_reflector_z,
            "p1": obs_reflector_p1,
            "p2": obs_reflector_p2,
            "p3": obs_reflector_p3,
            "norm": obs_reflector_norm,
            "centroid": obs_reflector_centroid,
            "areas": obs_reflector_areas
        }
    }