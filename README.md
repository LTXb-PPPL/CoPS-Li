# CoPS-Li
Coverage Prediction for Surface sources - Lithium 

Parallel Fortran code to quickly calculate Lithium deposited on a surface from a combination of surfaces sources. 

How to use 

1. Create STL files using any CAD software of target surface, source surface, reflector surface, oobjects that might block/obstruct either the source or reflector lines of sights.
2. Use generate_geom.py to read data from stl files into .DAT files that fortran can read.
3. Modify source_cyl.f90 or source_ref.f90
   a. Feed the paths of all .DAT files
   b. Decide on the number of chunks the input target should be sub-divided into
   c. Give appropriate names to output files.
4. Launch on a cluster using launch.sh. The problem is 'embarrasingly parallel' so more cores is linearly faster
5. Use save_obj.py to save the result as an .obj file

More post-processing will be added eventually and if there is interest. 
