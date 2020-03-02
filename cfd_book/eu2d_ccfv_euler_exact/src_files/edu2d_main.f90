!********************************************************************************
! Educationally-Designed Unstructured 2D (EDU2D) Code
!
!  ---------------- EDU2D-CCFV-Euler-EXPLCT
!
!  Now you can solve steady/unsteady inviscid-flow problems!
!
!  - Main program
!
! This program does the following:
!
! - reads a custom 2D unstructured grid (.grid)
! - constructs grid data required by CCFV.
! - constructs solution data required by CCFV.
! - set initial soltion
! - perform explicit-time stepping (pseudo-time iteration) to solve Euler
! - (optional) can compute the TE with MMS for verification.
! - writes tecplot and .vtk files for viewing the grid.
!
!
!
!        written by Dr. Katate Masatsuka (info[at]cfdbooks.com),
!
! the author of useful CFD books, "I do like CFD" (http://www.cfdbooks.com).
!
! This is Version 1.0.
!
!--------------------------------------------------------------------------------
! This main program uses the following module files.
!
!
! EDU2D-Template had the following files.
!
!  - edu2d_module_input_parameter.f90
!    -> This file contains a module that defines the input data variables, and
!       contains a subroutine that reads an input file named as "input.nml".     
!
!  - edu2d_module_common_data.f90
!    -> This file contains a module that defines common data to be used in the
!       main program and other modules (e.g., basic grid data, file names).
!
!  - edu2d_module_write_files.f90
!    -> This file contains a module that defines subroutiens that write output
!       files: tecplot and .vtk.
!
!
! EDU2D-CCFV-Template had the following additional module:
!
!  - edu2d_module_ccfv_data_grid.f90
!    -> This file contains a module that defines grid data required by CCFV,
!       and contains a subroutine for constructing the grid data.
!
!
! EDU2D-CCFV-Euler-Res had the following additional modules:
!
!  - edu2d_module_ccfv_data_soln.f90
!    -> This file contains a module that defines solution data specific to
!       the 2D Euler equations and contains related subroutines.
!
!  - edu2d_module_flux.f90
!    -> This file contains a subroutine that computes a numerical flux.
!
!  - edu2d_module_bc_states.f90
!    -> This file contains a subroutine that computes a BC state for weak BC.
!
!  - edu2d_module_ccfv_residual.f90
!    -> This file contains a subroutine that computes the cccfv residual.
!
!  - edu2d_module_mms.f90
!    -> This file contains subroutines for Method of Manufactured Solution (MMS).
!
!
! EDU2D-CCFV-Euler-EXPLCT has now the following additional modules:
!
!  - edu2d_module_explicit_solver.f90
!    -> This file contains a subroutine for performing a physical/pseudo-time stepping.
!
!  - edu2d_module_gradient.f90
!    -> Gradient methods not implemented yet...
!
!     NOTE: Following files from EDU2D-CCFV-Euler-Res have been slightly modified:
!           - edu2d_main.f90
!           - edu2d_module_input_parameter.f90 (added some input parameters)
!
!
! You can compile the code by typing "make" at a prompt, which executes
! the Makefile provided and compiles and links the code.
!--------------------------------------------------------------------------------
!
! ................
! | Main program |
! |              | ................ ................
! |              | | module 1     | | module 2     |
! |              | |              | |              |
! |              | | Data         | | Data         |
! |              | |              | |              |
! | contains     | | contains     | | contains     | . . . . . . .
! |--------------| |--------------| |--------------| 
! | subroutine 1 | | subroutine 1 | | subroutine 1 |
! | subroutine 2 | | subroutine 2 | | subroutine 2 |
! |            . | |            . | |            . |
! |..............| |..............| |..............|
!
! The EDU2D-CCFV-Euler-Explct is an explicit Euler solver for steady
! and unsteady problems.
!
!
! This F90 program is written and made available for an educational purpose.
!
! This file may be updated in future.
!
! Katate Masatsuka, http://www.cfdbooks.com
!
! Notes:
!
!  The purpose of this code is to give a beginner an opportunity to learn how to
!  write an unstructured CFD code. Hence, the focus here is on simplicity.
!  The code is not optimized for efficiency.
!
!  If the code is not simple enough to understand, please send questions to Hiro
!  at sunmasen(at)hotmail.com. He'll greatly appreciate it and revise the code.
!
!  If the code helps you understand how to write your own code that is more
!  efficient and has more features, it'll have served its purpose.
!
! Katate Masatsuka http://www.cfdbooks.com
!********************************************************************************

 program edu2d_ccfv_euler_explct

 ! Access data in module_input_parameter.
 ! - read_nml_input_parameters : subroutine to read the input file "input.nml".
 ! -         generate_tec_file : write a Tecplot file if set to be .true.
 ! -         generate_vtk_file : write a .vtk file if set to be .true.

   use module_input_parameter, only : read_nml_input_parameters, &
                                              generate_tec_file, &
                                              generate_vtk_file, &
                                                 compute_te_mms, &
                                             steady_or_unsteady, &
                                                   project_name

 ! To access the subroutines: set_filenames and read_grid.

   use module_common_data, only : set_filenames, read_grid

 ! To access the subroutine "construct_ccfv_grid_data" in module_ccfv_data_grid.

   use module_ccfv_data_grid , only : construct_ccfv_grid_data

 ! To access the subroutines "construct_ccfv_soln_data" and "set_initial_solution"
 ! in module_ccfv_data_soln.

   use module_ccfv_data_soln , only : construct_ccfv_soln_data, &
                                      set_initial_solution, set_initial_solution_vortex

 ! To access the subroutines: write_tecplot_file and write_vtk_file

   use module_write_files    , only : write_tecplot_file, write_vtk_file

 ! To access the subroutine "explicit_steady_solver" in module_explicit_solver.

   use module_explicit_solver, only : explicit_steady_solver, explicit_unsteady_solver

   use module_ccfv_gradient  , only : compute_lsq_coefficients

 ! Below
 ! "implicit none" means that no assumption is made for all the variables to be
 !  defined below, i.e., all variables must be explicitly defiend.
 !  Well, this version does not declare any variable, though...

   implicit none

   write(*,*)
   write(*,*) "----------------------------------------------------------------"
   write(*,*)
   write(*,*) "  This is EDU2D-CCFV-Euler-EXPLCT."
   write(*,*)
   write(*,*) "----------------------------------------------------------------"
   write(*,*)

!-------------------------------------------------------------------------------
! Read the input parameters

   call read_nml_input_parameters("input.nml")

   !------------------------------------------------------------
   ! Perform tests by MMS if requested by compute_te_mms=T

     if (compute_te_mms) then

      call mms_truncation_error !This subroutine is contained in this file.

      stop !<- stop the program.

     endif

   ! End of Perform tests by MMS
   !------------------------------------------------------------

   !------------------------------------------------------------
   ! Perform inviscid vortex test if requested by 'project_name'='vortex'

     if (trim(project_name)=="vortex") then

      call test_inviscid_vortex !This subroutine is contained in this file.

      stop !<- stop the program.

     endif

   ! End of Perform inviscid vortex test
   !------------------------------------------------------------

!-------------------------------------------------------------------------------
! Set file names.

  call set_filenames

!-------------------------------------------------------------------------------
! Read a grid file (.ugrid).

  call read_grid

!-------------------------------------------------------------------------------
! Cell-centered finite-volume method.

  !-----------------------------------------------------------------------------
  ! Construct grid metrics required for the CCFV discretization and solvers.

    call construct_ccfv_grid_data

  !-----------------------------------------------------------------------------
  ! Define solution parameters/arrays for the 2D Euler equations.

    call construct_ccfv_soln_data

    call compute_lsq_coefficients

  !-----------------------------------------------------------------------------
  ! Set initial solution.

    call set_initial_solution

  !-----------------------------------------------------------------------------
  ! Solve: explicit time-stepping scheme: Ut + Fx + Gy = 0 (Euler eqs).
 
    if     (trim(steady_or_unsteady) == "steady") then

     call explicit_steady_solver

    elseif (trim(steady_or_unsteady) == "unsteady") then

     call explicit_unsteady_solver

    endif

!-------------------------------------------------------------------------------
! Write output files for visualization (if requested).

   if (generate_tec_file) call write_tecplot_file ! if generate_tec_file = T
   if (generate_vtk_file) call write_vtk_file     ! if generate_vtk_file = T

   write(*,*)
   write(*,*)
   write(*,*)
   write(*,*) "----------------------------------------------------------------"
   write(*,*)
   write(*,*) "  End of EDU2D-CCFV-Euler-EXPLCT. "
   write(*,*)
   write(*,*) "----------------------------------------------------------------"
   write(*,*)

 stop

! Main program stops here. Below are the subroutines used in the main program.

 contains

!********************************************************************************
! This subroutine computes the truncation error for a given grid.
!
! (This is a kind of a main program for performing a test.)
!
! This program is activated by
!   compute_te_mms = T
! in the input.nml.
!
! (1)Compute and store the exact solution at centroids: w = wexact, and u=w2u(w).
! (2)Compute the forcing term at centroids, f = dF(wexact)/dx + dG(wexact)/dy 
!
!    Note: (1) and (2) by using "compute_manufactured_sol_and_f_euler()".
!
! (3)Compute the residual with the forcing term: Res = CCFV[dF(w)/dx+dG(w)/dy].
! (4)Subtract the forcing term:  Res = Res - f. (This is TE.)
! (5)Compute the L1 norm of the residual (This is the TE norm).
! (6)Print the L1 norms for all 4 equations with effective mesh spacings (heff).
!
! --- Run this for several different sizes of grids, plot the L1 norm versus heff
!     in log-log scale with lines of sploe 1 and 2; then you'll see the order of
!     truncation error.
!
!********************************************************************************
 subroutine mms_truncation_error

  use module_input_parameter, only : read_nml_input_parameters, &
                                             generate_tec_file, &
                                             generate_vtk_file

  use module_common_data   , only : p2, read_grid, set_filenames, zero, bc_type
  use module_ccfv_data_grid, only : construct_ccfv_grid_data, ncells, cell, heffv, nbound
  use module_ccfv_data_soln, only : construct_ccfv_soln_data, w2u, u, w, res

  use module_ccfv_gradient , only : compute_lsq_coefficients

  use module_ccfv_residual , only : compute_residual
  use module_write_files   , only : write_tecplot_file, write_vtk_file

  use module_mms           , only : compute_manufactured_sol_and_f_euler

  implicit none

  integer                           :: i
  real(p2), dimension(:,:), pointer :: f     !Forcing term
  real(p2), dimension(4)            :: norm1 !L1 norm of the residual (TE)


  write(*,*) "**************************************************************" 
  write(*,*) " MMS truncation error" 
  write(*,*) "**************************************************************" 


 !Prepare for the residual (TE) computation.

  call set_filenames
  call read_grid
  call construct_ccfv_grid_data
  call construct_ccfv_soln_data
  call compute_lsq_coefficients


 !Check the BC type. If not "dirichlet", enforce "dirichlet" (i.e., overwrite).

  do i = 1, nbound
   if (trim(bc_type(i)) /= "dirichlet") then
    bc_type(i) = "dirichlet"
    write(*,*) "  Dirichlet BC enforced: ", i, trim(bc_type(i))
   endif
  end do

 !Compute and store the exact solution and forcing term.

  !Allocate a forcing term array:
   allocate(f(ncells,4))

  !Initialize f.
   f = zero

   do i = 1, ncells

   !Compute and store w (exact soltion in primitive variables) and f:
    call compute_manufactured_sol_and_f_euler( cell(i)%xc, cell(i)%yc, w(i,:), f(i,:) )

   !Compute conservative variables from primitive variables.
    u(i,:) = w2u(w(i,:))

   end do

 !Compute the residuals (=TE*volume), and store them in res(:,:).

    call compute_residual

 !Subtract the forcing term.
 !Note: Res is an integral of Fx+Gy. So, the forcing term is also integrated,
 !      and so multiplied by the cell volume.

   do i = 1, ncells
    res(i,:) = res(i,:) - f(i,:)*cell(i)%vol
   end do

 !Compute L1 norms and print them on screen.

   !Initialization

    norm1 = zero

   !Sum of absolute values:

    do i = 1, ncells
     norm1 = norm1 + abs(res(i,:)/cell(i)%vol) !TE = Res/Volume.
    end do

   !Take an average; this is the TE.

    norm1 = norm1 / real(ncells,p2)


 !Print the TE for all 4 equations.

   write(*,*)
   write(*,*)
   write(*,*)
   write(*,*) " -------------- Truncation error norm ------------------"
   write(*,*) "              conti     x-mom       y-mom        energy       heffv" 
   write(*,'(a,5es13.5)') "  L1(TE) ", norm1, heffv
   write(*,*)
   write(*,*)
   write(*,*)
   write(*,*)
   write(*,*)

 !Write visualization files.

  if (generate_tec_file) call write_tecplot_file
  if (generate_vtk_file) call write_vtk_file

  write(*,*) "**************************************************************" 
  write(*,*) " End of MMS truncation error" 
  write(*,*) "**************************************************************" 

 end subroutine mms_truncation_error


!********************************************************************************
! This subroutine solve the inviscid vortex problem.
!
! (This is a kind of a main program for performing a test.)
!
! This program is activated by
!     project_name = "vortex"
! in the input.nml.
!
!********************************************************************************
 subroutine test_inviscid_vortex

  use module_input_parameter, only : read_nml_input_parameters, &
                                             generate_tec_file, &
                                             generate_vtk_file

  use module_common_data   , only : read_grid, set_filenames, filename_tecplot
  use module_ccfv_data_grid, only : construct_ccfv_grid_data
  use module_ccfv_data_soln, only : construct_ccfv_soln_data, set_initial_solution_vortex
  use module_ccfv_gradient , only : compute_lsq_coefficients

  use module_ccfv_residual , only : compute_residual
  use module_write_files   , only : write_tecplot_file, write_vtk_file

  implicit none

  integer :: status

  write(*,*) "**************************************************************" 
  write(*,*) " Inviscid Vortex Test" 
  write(*,*) "**************************************************************" 


 !Prepare for the inviscid vortex problem.

  call set_filenames
  call read_grid
  call construct_ccfv_grid_data
  call construct_ccfv_soln_data
  call compute_lsq_coefficients

 !Set initial inviscid vortex solution.

  call set_initial_solution_vortex
  call write_tecplot_file
  status = rename( filename_tecplot, "vortex_tec_initial.dat" )
  if ( status .ne. 0 ) stop 'rename: error'

 !Solve by explicit time-stepping scheme: Ut + Fx + Gy = 0 (Euler eqs).
 !Invisicd vortex problem is unsteady, and so there is no choice but unsteady solver.

  call explicit_unsteady_solver

 !Write visualization files.

  if (generate_tec_file) call write_tecplot_file
  if (generate_vtk_file) call write_vtk_file

  write(*,*) "**************************************************************" 
  write(*,*) " End of Inviscid Vortex Test" 
  write(*,*) "**************************************************************" 

 end subroutine test_inviscid_vortex



 end program edu2d_ccfv_euler_explct

