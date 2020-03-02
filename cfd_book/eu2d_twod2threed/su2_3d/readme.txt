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

gfortran -O3 -ffast-math ../edu2d_fp_grid_v1.f90
./a.out

# This generates .grid and .bcmap files for a 2D grid.


# Now, you're going to generate its 3D version.
# Compile the 2D-3D code:

#----------------------------------------------------------------------
# For binary .ugrid file, endianness will be automatically detected, but if you wish,
# you can specify endianness at compilation: e.g., as follows:
#  gfortran -O2 -fconvert=big-endian -o edu2d_twod2threed_v3  ../edu2d_twod2threed_v3.f90
#     ifort -O2 -convert big_endian  -o edu2d_twod2threed_v3  ../edu2d_twod2threed_v3.f90
#----------------------------------------------------------------------

# Let us choose the big_endian (this only matters for the .ugrid file):

gfortran -O2 -fconvert=big-endian ../edu2d_twod2threed_v3.f90
./a.out

# That's it. A .su2 grid file is generated.
# See screen output for details.
#

# Now run SU2

SU2_CFD test.cfg

