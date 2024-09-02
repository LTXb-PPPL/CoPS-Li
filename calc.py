
import generate_geom
import read
import numpy as np

import read
import numpy as np

geo_dir = '/p/ltxdata/Li_evporator/Li_Evap_Source/Fortran_Source/CAD_Source/geom_mark2'
#geo_dir = '/p/ltxdata/Li_evporator/test_geom'
geom = read.geometry(geo_dir)
import time
# check for each source element, check if the target element face it 

T = []
D = []
target_id = []

"""obs = [geom['target']['centroid']+geom['obs_source']['centroid'], geom['target']['norm']+geom['obs_source']['norm'],
    geom['target']['p1']+geom['obs_source']['p1'], geom['target']['p2']+geom['obs_source']['p2'],
    geom['target']['p3']+geom['obs_source']['p3']]
"""

obs = [geom['target']['centroid'], geom['target']['norm'],
    geom['target']['p1'], geom['target']['p2'],
    geom['target']['p3']]


target_c = np.array(geom['target']['centroid'])
target_n = np.array(geom['target']['norm'])
target_a = np.array(geom['target']['areas'])

chunks = 196

#source = geom['source']['centroid']
#source_norm = geom['source']['norm']

source = geom['source']['centroid']
source_norm = geom['source']['norm']


tc_ch = np.array_split(target_c,chunks)
print(f'target elements per chunk: {len(tc_ch[0])}')
tn_ch = np.array_split(target_n,chunks)
ta_ch = np.array_split(target_a,chunks)
chunk = 0
for tc, tn, ta in zip(tc_ch,tn_ch,ta_ch):
	thickness = np.zeros(len(tc))
	start = time.time()	
	# convert start to human readable time
	start_announce = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start))	
	print(f'startin chunk {chunk} at {start_announce}')
	for s, sn in zip(source, source_norm):
			
 		# check if target element face the source element
		ts = np.sum((s-tc)*tn,axis=1)
		ts = np.where(ts>0, 1, 0)
		# check if source element face the target element
		st = np.sum((tc-s)*sn,axis=1)
		st = np.where(st>0, 1, 0)
		# multiply the two arrays to get the face to face relation
		o = ts*st
		#orientation.append(ts*st)

		# find distance, t between source and target
		idx_o = np.where(o==1)[0]
		t_id = np.arange(len(o))[idx_o]
		target_centroid = tc[idx_o]
		#target_centroid = np.array(geom['target']['centroid'])
		target_source_vec = target_centroid - s
		target_source_vec_norm = np.linalg.norm(target_source_vec,axis=1)
		t = target_source_vec_norm
		#print(len(t))
		# find the unit vector
		target_source_vec_unit = target_source_vec / target_source_vec_norm[:,np.newaxis]
		d = target_source_vec_unit

		c_o = obs[0]
		n_o = obs[1]
		num = np.einsum('ij,ij->i',n_o,c_o) - np.einsum('ij,j->i',n_o,s)
		den = np.einsum('ij,kj->ik',d,n_o)
		tq = num/den
		pq = np.einsum('ik,ij->ijk',d,tq) + s
		p1 = np.array(obs[2])
		p2 = np.array(obs[3])
		p3 = np.array(obs[4])
		# reshape p1,p2,p3 to match the shape of pq
		p1 = np.tile(p1,(len(pq),1,1))-pq
		p2 = np.tile(p2,(len(pq),1,1))-pq
		p3 = np.tile(p3,(len(pq),1,1))-pq

		u = np.cross(p2,p3)
		v = np.cross(p3,p1)
		w = np.cross(p1,p2)

		# check if uvw point in the same direction 
		# if the dot product is positive, then the vectors point in the same direction
		uv = np.einsum('ijk,ijk->ij',u,v)
		wu = np.einsum('ijk,ijk->ij',w,u)
		uvw = np.zeros(uv.shape)
		# tile t to have len(t) rows and len(obs[2]) columns
		dist = np.tile(t,(len(obs[2]),1)).T - tq
		dist = np.where(dist>1E-5,1,0)
		# if both uv and wu are positive, then the vectors point in the same direction
		uvw = np.where(np.logical_and(uv>0,wu>0),1,0)
		#cond = np.sum(uvw,axis=1)
		cond  = np.sum(uvw*dist,axis=1)
		#print(len(cond),len(tc))
		cond_a = np.zeros(len(tc))
		source_target_vec = np.zeros((len(cond_a),3))
		areas = np.zeros(len(cond_a))
		distance = np.zeros(len(cond_a))
		for i in range(len(cond)):
			cond_a[t_id[i]] = cond[i]    
			source_target_vec[t_id[i]] = d[i]
			areas[t_id[i]] = ta[t_id[i]]
			distance[t_id[i]] = t[i]
		
		cond_a = np.where(cond_a<1e-5,1,0)
		aa = np.einsum('ij,j->i',source_target_vec,sn)/(np.linalg.norm(source_target_vec,axis=1)*np.linalg.norm(sn))
		phi = np.arccos(aa)*180/np.pi
		bb = np.einsum('ij,ij->i',-source_target_vec,tn)/(np.linalg.norm(source_target_vec,axis=1)*np.linalg.norm(tn,axis=1))
		theta = np.arccos(bb)*180/np.pi
		#print(np.linalg.norm(tn[0],axis=1),tn[0])
		s_t = 1000*(1e6*np.cos(phi*np.pi/180)*np.cos(theta*np.pi/180)/(0.534*np.pi*distance**2))*cond_a/len(source)

		thickness = thickness + np.where(np.isnan(s_t),0,s_t)

	stop = time.time()
	print(f"Time: {stop-start}")
	#thickness= thickness/len(geom['source']['centroid'])
	chunk += 1

	f = 'source_proj.txt'
	with open(f,'a') as file:
		for i,(dep, n, c) in enumerate(zip(thickness,tn,tc)):
			file.write(f"{i}\t{dep}\t{n}\t{c}"'\n')
	file.close()