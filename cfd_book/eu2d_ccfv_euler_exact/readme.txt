#################################################################
#
#  EDU2D-CCFV-Euler-Explicit:
#
#  This is a cell-centered explicit Euler code.
#
#  - Source files (.f90) are stored in "src_files".
#    You're encouraged to look at the source files
#    to understand the algorithms and implementation.
#
#    [This code was used in a graduate course at Old Dominion
#     University in 2018. There is an implicit-solver version.]
#
#  - To compile and generate an executable.
#    There are two directories:
#
#    executable_debug         !<- For debugging
#    executable_optimized     !<- For running cases
#
#    In each directory, just type make at a prompt:
#
#    %make
#
#    This will use the Makfile there to compile the code,
#    and generate the executable 'edu2d' in there.
#
#  - To run cases, there are case directories:
#
#    case_steady_airfoil
#    case_steady_cylinder
#    case_unsteady_vortex
#    case_verification_te
#
#    Go in any of these directories, and type:
#
#    %../executable_optimized/edu2d
#
#    (Note: the optimized executable is faster to run)
#
#    to run the case.
#
#    Example:
#             % cd case_implicit_steady_cylinder
#             %../executable_optimized/edu2d
#
#  - Look at the input file 'input.nml', and modify it to
#    change parameters. Not all input variables are specified
#    there. See src_files/edu2d_module_input_parameter.f90 to
#    find a complete list of input variables and their default
#    values.
#
#  - To clean up .o .mod and the executable in the executable directory,
#    type "make clean":
#
#     %make clean
#
#
#
# Katate Masatsuka, August 2019
#################################################################

