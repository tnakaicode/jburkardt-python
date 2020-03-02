
# As an example, first generate a 2D grid.
# This will generate a .su2 file for a 2D grid.

# Compile the 2D grid generation code.

gfortran -O3 -ffast-math ../edu2d_fp_grid_v1.f90

# Run the 2D grid generation code.

./a.out


# Now run SU2 with the configuration file test.cfg:

SU2_CFD test.cfg

