!********************************************************************************
! Educationally-Designed Unstructured 2D (EDU2D) Code
!
!  ---------------- EDU2D-CCFV-Euler-EXPLCT
!
!  - Input parameter module
!
! This module defines input parameters, and set the default values.
! These parameters are specified in the file named 'input.nml', and read
! in the main program by the subroutine "read_nml_input_parameters".
!
!
!        written by Dr. Katate Masatsuka (info[at]cfdbooks.com),
!
! the author of useful CFD books, "I do like CFD" (http://www.cfdbooks.com).
!
! 
! This F90 program is written and made available for an educational purpose.
!
! This file may be updated in future.
!
! Katate Masatsuka http://www.cfdbooks.com
!********************************************************************************

 module module_input_parameter

  implicit none

 !This module contains the following subroutine:
 ! -read_nml_input_parameters ! read the input file

 !Make all input parameters andn subroutines available to other modules.
  public

!-------------------------------------------------------------------------
! Define 'p2' for double precidion real .

  integer, parameter :: p2 = selected_real_kind(P=15)

!-------------------------------------------------------------------------
! Define input variables and specify default values

! Project name
  character(80) ::      project_name = "default"    ! project name

! To write a Tecplot data file
  logical       :: generate_tec_file = .true.  ! generate_tec_file = T

! To write a .vtk data file
  logical       :: generate_vtk_file = .true.  ! generate_vtk_file = T

! Mach number
  real(p2) :: M_inf = 0.3_p2        ! Freestream Mach number
  real(p2) ::   aoa = 0.0_p2        ! Angle of attack in degrees

! MMS testing
  logical                :: compute_te_mms = .false.

! Steady or unsteady
  character(80) :: steady_or_unsteady = "steady" !or "unsteady"
  real(p2)      ::            t_final = 1.0_p2   !Final time for an unsteady problem.

! Scheme/solver parameters
  real(p2)               :: CFL             = 0.5_p2
  integer                :: max_iteration   = 100
  real(p2)               :: tolerance       = 1.0e-05_p2
  character(80)          :: inviscid_flux   = "roe"
  real(p2), dimension(5) :: eig_limiting_factor = (/ 0.1, 0.1, 0.1, 0.1, 0.1 /)  !eigenvalue limiting factor

  logical                :: second_order = .false.
  logical                ::  use_limiter = .false.

! End of Default input values
!-------------------------------------------------------------------------


!-------------------------------------------------------------------------
! Group them into "input_parameters":

 namelist / input_parameters / &
  project_name       , &
  generate_tec_file  , &
  generate_vtk_file  , &
  M_inf              , &
  aoa                , &
  compute_te_mms     , &
  steady_or_unsteady , &
  t_final            , &
  CFL                , &
  max_iteration      , &
  tolerance          , &
  inviscid_flux      , &
  eig_limiting_factor, &
  second_order       , &
  use_limiter

  !Note: These variables defined above are available within the entire
  !      module, and so within all subroutines contained below.


 contains

!*****************************************************************************
!
! This subroutine reads input_parameters specified in the input file:
!
!    file name = namelist_file
!
! prints the content on screen.
!
! In the main program, we set: namelist_file = "input.nml"
!
!*****************************************************************************

  subroutine read_nml_input_parameters(namelist_file)

  implicit none
  character(9), intent(in) :: namelist_file
  integer :: os

  write(*,*)
  write(*,*) "-------------------------------------------------------"
  write(*,*) " Reading the input file: input.nml..... "
  write(*,*)

  open(unit=10,file=trim(namelist_file),form='formatted',status='old',iostat=os)
  read(unit=10,nml=input_parameters)

  write(*,*)
  write(*,*) " List of given namelist variables and their values"
  write(*,*)

  write(*,nml=input_parameters) ! Print the namelist variables on screen.
  close(10)

  write(*,*)
  write(*,*) " End of Reading the input file: input.nml..... "
  write(*,*) "-------------------------------------------------------"
  write(*,*)

  end subroutine read_nml_input_parameters
!*****************************************************************************

 end module module_input_parameter
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!
!  End of input parameter module
