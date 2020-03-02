!********************************************************************************
!* --- Educationally-Designed Unstructured 2D (EDU2D) Code
!*
!*
!* This version is a template for Node/Cell-Centered (NC/CC) finite-volume method:
!*
!*                           --- EDU2D-Template ---
!*
!*   It reads an unstructured grid, and makes some loops over edges, cells, nodes,
!*   and writes out Tecplot data file for viewing the grid and solutions.
!*   You can generate your own unstructured code by inserting your own solver.
!*
!*
!* Program Files (4 Fortran90 files):
!*
!* ------------------------------------------
!* - Main driver program file   : This reads grid and BC files, and call dummy NC/CC programs.
!*
!*     edu2d_main.f90 (This file), which contains a main driver program
!*      -- edu2d_template       : Main driver code, which calls main subroutines for NC and CC schemes.
!*
!* ------------------------------------------
!* - Basic EDU2D package file   : This is the file you can start with in writing your own CFD code!
!*
!*     edu2d_basic_package.f90, which contains the following modules.
!*      -- edu2d_constants      : Numerical values defined
!*      -- edu2d_grid_data_type : Grid data types defined
!*      -- edu2d_main_data      : Main grid data and parameters declared
!*      -- edu2d_grid_data      : Read/construct/check grid data
!*
!* ------------------------------------------
!* - Node-centered related file : Example for NC solvers.
!*
!*     edu2d_template_nc.f90, which contains a template for a main NC scheme program
!*      -- main_nc              : It shows how to write a program for NC schemes.
!*      -- compute_lsq_coeff_nc : Compute and store LSQ gradient coefficients at nodes
!*      --   check_lsq_coeff_nc : Check the computed LSQ coefficients
!*      --  compute_gradient_nc : Compute gradients at nodes
!*
!* ------------------------------------------
!* - Cell-centered related file : Example for CC solvers.
!*
!*     edu2d_template_cc.f90, which contains a template for a main CC scheme program
!*      -- main_cc              : It shows how to write a program for CC schemes.
!*      -- compute_lsq_coeff_cc : Compute and store LSQ gradient coefficients at cells
!*      --   check_lsq_coeff_cc : Check the computed LSQ coefficients
!*      --  compute_gradient_cc : Compute gradients at cells
!*
!*
!* ------------------------------------------------------------------------------
!*
!* Notes:
!*
!*  The purpose of this code is to give a beginner an opportunity to learn how to
!*  write an unstructured CFD code. Hence, the focus here is on the simplicity.
!*  The code is not optimized for efficiency.
!*
!*  If the code is not simple enough to understand, please send questions to Hiro
!*  at sunmasen(at)hotmail.com. I'll greatly appreciate it and revise the code.
!*
!*  If the code helps you understand how to write your own code that is more
!*  efficient and has more features, it'll have served its purpose.
!*
!* Katate Masatsuka, http://www.cfdbooks.com
!********************************************************************************

!********************************************************************************
!* Main driver code for testing templates for NC and CC schemes.
!*
!* Input -------------------------------------------------------
!*
!*  (1)Parameters to be specified inside the main program:
!*
!*   project_name = Project name that determines the names of grid and BC files to read,
!*                  as well as the names of output data files.
!*   nq = The number of equations/variables (it is set to be 3 in this template code).
!*   gradient_type = LSQ gradient type ('linear' or 'quadratic2')
!*   gradient_weight = LSQ gradient weight ('none' or 'inverse_distance')
!*   gradient_weight_p = Power of LSQ weight (any positive real number)
!*
!*  (2)Files that should be available befor running this code:
!*
!*   [project name].grid  = grid file containing boundary information
!*   [project name].bcmap = file that specifies boundary conditions
!*
!*   (Note: Compile and run generate_grids_edu2d_v0.f90 to generate
!*       these files for an exmaple square domain grid. )
!*
!*   (Note: See the subroutine "read_grid" in edu2d_grid_data.f90
!*          or generate_grids_edu2d_v0.f90 for the format of these files.)
!*
!* Output ------------------------------------------------------
!*
!*  From the NC solver part:
!*  - "[project name]_nc_tecplot.dat"   = Tecplot file containing the grid and the solution.
!*  - "[project name]_nc_b_tecplot.dat" = Tecplot file for boundary data.
!*
!*  From the CC solver part:
!*  - "[project name]_cc_tecplot.dat"   = Tecplot file containing the grid and the solution.
!*
!*
!*
!*        written by Dr. Katate Masatsuka (info[at]cfdbooks.com),
!*
!* the author of useful CFD books, "I do like CFD" (http://www.cfdbooks.com).
!*
!* This is Version 0 (July 2015).
!* This F90 code is written and made available for an educational purpose.
!* This file may be updated in future.
!*
!* Katate Masatsuka, http://www.cfdbooks.com
!********************************************************************************
 program edu2d_template_main

 use edu2d_constants   , only : one
 use edu2d_my_main_data, only : nq, gradient_type, gradient_weight, gradient_weight_p, &
                                node, nnodes, elm, nelms
 use edu2d_grid_data   , only : read_grid, construct_grid_data, check_grid_data

 use edu2d_template_nc , only : main_nc
 use edu2d_template_cc , only : main_cc

 implicit none

!Input grid data files
 character(80) :: datafile_grid_in  !Grid file
 character(80) :: datafile_bcmap_in !Boundary condition file

!Output data file for NC scheme
 character(80) :: datafile_nc_tec    !Tecplot file for viewing the result: Entire domain
 character(80) :: datafile_nc_tec_b  !Tecplot file for viewing the result: Boundary

!Output data file for CC scheme
 character(80) :: datafile_cc_tec    !Tecplot file for viewing the result: Entire domain

!Local
 character(80) :: project_name
 integer       :: i

! Set paramters (these variables are declared in the module 'my_main_data'.
  
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Setting up parameters..."
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*)

  !Number of equtaions/variables in the target equtaion.
   nq = 3  !<----- Here, we assume 3 equations/vairables.
  !Choice of LSQ gradient method (quadratic LSQ is not available for CC.)
   gradient_type     = "linear" ! or "quadratic2" for NC.
  !LSQ weight
   gradient_weight   = "none"   ! or "inverse_distance"
  !Power of LSQ weight
   gradient_weight_p =  one     ! or any other real value

   write(*,*)
   project_name      = "any_name"
   write(*,*) " Project name = ", project_name

! Read grid files
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Reading the grid and boundary condition files... "
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

  datafile_grid_in  = trim(project_name) // '.grid'  !<= any_name.grid
  datafile_bcmap_in = trim(project_name) // '.bcmap' !<= any_name.bcmap

  datafile_nc_tec   = trim(project_name) // '_nc_tecplot.dat'
  datafile_nc_tec_b = trim(project_name) // '_nc_b_tecplot.dat'

  datafile_cc_tec   = trim(project_name) // '_cc_tecplot.dat'

  call read_grid( datafile_grid_in, datafile_bcmap_in )

     !Allocate arrays

      do i = 1, nnodes
       allocate( node(i)%u(     nq  ) )
       allocate( node(i)%uexact(nq  ) )
       allocate( node(i)%gradu( nq,2) ) !<- 2: x and y components.
       allocate( node(i)%res(   nq  ) )
      end do

      do i = 1, nelms
       allocate( elm(i)%u(     nq  ) )
       allocate( elm(i)%uexact(nq  ) )
       allocate( elm(i)%gradu( nq,2) ) !<- 2: x and y components.
       allocate( elm(i)%res(   nq  ) )
      end do

! Construct grid data
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Constructing grid data... "
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*)
  call construct_grid_data

! Check the grid data (It is always good to check them before use!)
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Checking the grid data... "
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  call check_grid_data

!---------------------------------------------------------------------------
! 1. Call a template main program for Node-Centered (NC) scheme:
!---------------------------------------------------------------------------
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Template main program for node-centered (NC) schemes. "
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*)
  call main_nc(datafile_nc_tec,datafile_nc_tec_b)

!---------------------------------------------------------------------------
! 2. Call a template main program for Cell-Centered (CC) scheme:
!---------------------------------------------------------------------------
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Template main program for cell-centered (CC) schemes. "
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*)
  call main_cc(datafile_cc_tec)


  write(*,*)
  write(*,*) "Good. Successfully completed."
  write(*,*)

  stop

 end program edu2d_template_main




