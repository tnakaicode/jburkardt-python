######################################################################
# Running EDU2D-Template code
#
# Follow the steps to run the code.
# (Or just run this script by typing "source readme_v0.txt".)
#
# NOTE: The following is for gfortran. If you use other compiler,
#       replace "gfortran" by your compiler (ifort, g95, etc).
#
#
# Katate Masatsuka, http://www.cfdbooks.com
#####################################################################

#####################################################################
# 1. Compile the grid generation code.
#####################################################################

gfortran -O2 -o generate_grids_for_edu2d_v0 generate_grids_for_edu2d_v0.f90

#####################################################################
# 2. Run and generate a grid file and a BC file
#    Dimensions are defined in the program: 20x20 grid.
#    It will generate the following files:
#     any_name.grid        - Input EDU2D-Template code
#     any_name.bcmap       - Input EDU2D-Template code
#     other files          - Not needed by EDU2D-Template code
#####################################################################

./generate_grids_for_edu2d_v0

#####################################################################
# 3. Compile EDU2D-Template code
#    Use the following, or just type 'make' which uses Makefile.
#####################################################################

gfortran -O2 -c edu2d_basic_package_v0.f90
gfortran -O2 -c edu2d_template_nc_v0.f90
gfortran -O2 -c edu2d_template_cc_v0.f90
gfortran -O2 -c edu2d_template_main_v0.f90
gfortran -O2 -o edu2d_template edu2d_basic_package_v0.o edu2d_template_nc_v0.o edu2d_template_cc_v0.o edu2d_template_main_v0.o

#####################################################################
# 4. Run EDU2D-Template code
#
#    See 'any_name_screen_out.txt', which is what you should see on the screen.
#####################################################################

./edu2d_template

#####################################################################
# See screen output to learn what the code did.
#
# Note: It only runs some dummy finite-volume codes, and so the solution
#       has no physical meaning. It only shows how a finite-volume code
#       can be written in F90.
#####################################################################
