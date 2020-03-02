####################################################################
# Generate 3D grids from the a 2D grid.
#
# You need to have the following 2D grid files:
#  1. project_name.grid"
#  2. project_name.bcmap"
#
# Note: .grid file is a custom 2D unstructured grid file used
#       in edu2d codes.
#
#####################################################################

# As an example, first generate a 2D grid.

gfortran -O3 -ffast-math edu2d_fp_grid_v1.f90
./a.out

# This generates .grid and .bcmap files for a 2D grid.

# Now, you're going to generate its 3D version.
# Compile the 2D-3D code:

#----------------------------------------------------------------------
# For binary .ugrid file, endianness will be automatically detected, but if you wish,
# you can specify endianness at compilation: e.g., as follows:
#  gfortran -O2 -fconvert=big-endian -o edu2d_twod2threed  edu2d_twod2threed_v6.f90
#     ifort -O2 -convert big_endian  -o edu2d_twod2threed  edu2d_twod2threed_v6.f90
#----------------------------------------------------------------------

# Let us choose the big_endian (this only matters for the .ugrid file):
 gfortran -O2 -fconvert=big-endian -o edu2d_twod2threed  edu2d_twod2threed_v6.f90

# and run it:

./edu2d_twod2threed

# That's it.
# See screen output for details.
#




# To try out the rotation option, go to the directoty: example_rotation

cd example_rotation

# and run the program

gfortran -O2 -fconvert=big-endian -o edu2d_twod2threed  ../edu2d_twod2threed_v6.f90
./edu2d_twod2threed

# Visualize the grid by opning i50yen_3d.vtk or i50yen_3d_tec.dat.


cd ..


# To try out the rotation option with varying radius and z, go to the directoty: example_spiral

cd example_spiral

# and run the program

gfortran -O2 -fconvert=big-endian -o edu2d_twod2threed  ../edu2d_twod2threed_v6.f90
./edu2d_twod2threed

# Visualize the grid by opning i50yen_3d.vtk or i50yen_3d_tec.dat.


