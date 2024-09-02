# CoPS-Li
Coverage Prediction for Surface sources - Lithium 

Parallel Fortran code to quickly calculate Lithium deposited on a surface from a combination of surfaces sources. 

How to use 

1. Create STL files using any CAD software of target surface, source surface, reflector surface, oobjects that might block/obstruct either the source or reflector lines of sights. One way to do this is to give the surfaces you want to extract a unique color and then extract faces with the 'attribute' feature that correspond to that color. This can be done programmatically by using `generate_geom.extract_faces()`
2. Use generate_geom.py to read data from stl files into `.DAT` files that fortran can read. 
3. Modify `source_cyl.f90` or `source_ref.f90`
   * Feed the paths of all `.DAT` files
   * Decide on the number of chunks the input target should be sub-divided into
   * Give appropriate names to output files.
4. Complie using any mpi based compiler and launch on a cluster using `launch.sh`. The problem is 'embarrasingly parallel' so more cores is linearly faster
5. Use `save_obj.py` to save the result as an `.obj` file

`.obj` files can be accessed and viewed using blender. 

More post-processing will be added eventually and if there is interest. 
