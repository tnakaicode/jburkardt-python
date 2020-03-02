!********************************************************************************
!  Educationally-Designed Unstructured 2D (EDU2D) Code
!
!  ---------------- EDU2D-CCFV-Euler-Res
!
!
! This is module_ccfv_data_soln.
!
! This module containes data required by a cell-centered FV discertization
! for the 2D Euler equtions, and a subroutine that constructs the data for
! a given grid.
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

 module module_ccfv_data_soln

  use module_common_data, only : p2, one, zero !To declare double precision variables below.

  implicit none

  !Public means these data can be accessed in other program, subroutine/function,
  !and modules. Those not explcitly stated are private to this module, and cannot
  !be accessed by other modules and subroutines/functions.

  !Data that can be used in other modules/subroutines.
   public :: nq, u, w, gradw, res, wsn, dtau
   public :: ir, iu, iv, ip
   public :: gamma
   public :: rho_inf, u_inf, v_inf, p_inf

  !Subroutine that can be used in other modules/subroutines.
   public :: construct_ccfv_soln_data
   public :: set_initial_solution, set_initial_solution_vortex
   public :: w2u, u2w

 !------------------------------------------------------------------------------------
 !------------------------------------------------------------------------------------
 ! Below are the definition of the data used to implement a cell-centered FV method.
 !------------------------------------------------------------------------------------

  !------------------------------------------
  !>> Solution data
  !------------------------------------------

   integer                             :: nq    !# of eqns/solns (4 for 2D Euler/NS).
   real(p2), dimension(:,:)  , pointer :: u     !conservative variables at cells/nodes.
   real(p2), dimension(:,:)  , pointer :: w     !primitive variables at cells/nodes.
   real(p2), dimension(:,:,:), pointer :: gradw !gradients of w at cells/nodes.

   real(p2), dimension(:)    , pointer :: dtau  !pseudo time step
   real(p2), dimension(:)    , pointer :: wsn   !maximum eigenvalue at faces

  !Just for convenience and clarity in acecssing variables in w or residual components.
   integer                           :: ir = 1  !w(ir) = density
   integer                           :: iu = 2  !w(iu) = x-velocity
   integer                           :: iv = 3  !w(iv) = y-velocity
   integer                           :: ip = 4  !w(ip) = pressure

   real(p2), dimension(:,:), pointer :: res     !residual vector

  !------------------------------------------
  !>> Paramteres
  !------------------------------------------

   real(p2) :: gamma = 1.4_p2 !Ratio of specific heats for air

  !Free stream values: will be set in 'set set_initial_solution' for a given
  !free stream Mach number.
   real(p2) :: rho_inf = one
   real(p2) ::   u_inf = one
   real(p2) ::   v_inf = zero
   real(p2) ::   p_inf = one/1.4_p2


  !These data will be allocated for a given grid size, and filled in the
  !following subroutine: construct_ccfv_data.

 !------------------------------------------------------------------------------------
 ! End of the data used to implement a cell-centered FV method.
 !------------------------------------------------------------------------------------
 !------------------------------------------------------------------------------------


 contains

!*******************************************************************************
! Define and allocate the data for target equations and solutions.
!
! Note: Here, we solve 2D Euler/NS equations.
!
!*******************************************************************************
 subroutine construct_ccfv_soln_data

  use module_common_data   , only : zero   !some p2 values

  use module_ccfv_data_grid, only : ncells !# of cells.

  implicit none

 ! 2D Euler/NS equations = 4 equations:
 !
 ! (1)continuity
 ! (2)x-momentum
 ! (3)y-momentum
 ! (4)energy

    nq = 4

 !------------------------------------------------------
 ! Allocate solution arrays

  allocate( u(ncells,nq) )
  allocate( w(ncells,nq) )

  ! Initialization
    u = zero
    w = zero

 !------------------------------------------------------
 ! Allocate pseudo time step array

  allocate( dtau(ncells) )

  ! Initialization
    dtau = zero

 !------------------------------------------------------
 ! Allocate max wave speed array

  allocate( wsn(ncells) )

  ! Initialization
    wsn = zero

 !------------------------------------------------------
 ! Allocate gradient array

 ! Initialize gradient arrays (just zero here).

  allocate( gradw(ncells,nq,2) )

  ! Initialization
    gradw = zero

 !------------------------------------------------------
 ! Allocate residual array

  allocate( res(ncells,nq) )

  ! Initialization
    res = zero


 end subroutine construct_ccfv_soln_data


!*******************************************************************************
! Set the initial solution.
!
! We initialize the solution with a free stream condition defined by the Mach
! number and the angle of attack specified by the input parameters: M_inf and aoa.
!
!*******************************************************************************
 subroutine set_initial_solution

  use module_common_data    , only : p2, one, pi
  use module_ccfv_data_grid , only : ncells
  use module_input_parameter, only : M_inf, aoa

  implicit none

  integer                :: i
  real(p2), dimension(4) :: w_initial

  !Set free stream values based on the input Mach number.

   rho_inf = one
     u_inf = M_inf*cos(aoa *pi/180_p2) !aoa converted from degree to radian
     v_inf = M_inf*sin(aoa *pi/180_p2) !aoa converted from degree to radian
     p_inf = one/gamma

  !Set initial solution by the free stream values
   cell_loop : do i = 1, ncells

    w_initial(ir) = rho_inf
    w_initial(iu) =   u_inf
    w_initial(iv) =   v_inf
    w_initial(ip) =   p_inf

   !Store the initial solution

    w(i,:) = w_initial

   !Compute and store conservative variables.
    u(i,:) = w2u( w_initial )

   end do cell_loop

 end subroutine set_initial_solution
!*******************************************************************************

!*******************************************************************************
! Set the initial solution for the inviscid vortex test case.
!
! We initialize the solution with the exact solution. See 'I do like CFD, VOL.1"
!
! Note: The grid must be generated in the square domain defined by
!
!       [x,y] = [-20,10]x[-20,10]
!
!       Initially, the vortex is centered at (x,y)=(-10,-10), and will be
!       convected to the origin at the final time t=5.0.
!
!*******************************************************************************
 subroutine set_initial_solution_vortex

  use module_common_data    , only : p2, one, pi, half, two
  use module_ccfv_data_grid , only : ncells, cell

  implicit none

  integer                :: i
  real(p2)               :: x0, y0, K, alpha, x, y, r, temperature
  real(p2), dimension(4) :: w_initial

      x0 = -10.0_p2
      y0 = -10.0_p2
       K =  5.0_p2
   alpha =  one

  !Set free stream values (the input Mach number is not used in this test).

   rho_inf = one
     u_inf = two
     v_inf = two
     p_inf = one/gamma

  !Note: Speed of sound a_inf is sqrt(gamma*p_inf/rho_inf) = 1.0.

  !Set initial solution by the exact vortex solution.
   cell_loop : do i = 1, ncells

    x = cell(i)%xc - x0
    y = cell(i)%yc - y0
    r = sqrt( x**2 + y**2 )

    w_initial(iu) =  u_inf - K/(two*pi)*y*exp(alpha*half*(1-r**2))
    w_initial(iv) =  v_inf + K/(two*pi)*x*exp(alpha*half*(1-r**2))
      temperature =    one - K*(gamma-one)/(8.0_p2*alpha*pi**2)*exp(alpha*(1-r**2))
    w_initial(ir) = rho_inf*temperature**(  one/(gamma-one)) !Density
    w_initial(ip) = p_inf  *temperature**(gamma/(gamma-one)) !Pressure

   !Store the initial solution

    w(i,:) = w_initial

   !Compute and store conservative variables.
    u(i,:) = w2u( w_initial )

   end do cell_loop

 end subroutine set_initial_solution_vortex
!*******************************************************************************

!********************************************************************************
! Compute U from W
!
! ------------------------------------------------------------------------------
!  Input:  w =    primitive variables (rho,     u,     v,     p)
! Output:  u = conservative variables (rho, rho*u, rho*v, rho*E)
! ------------------------------------------------------------------------------
!
! Note: E = p/(gamma-1)/rho + 0.5*(u^2+v^2)
!
!********************************************************************************
 function w2u(w) result(u)

  use module_common_data, only : p2, one, half

  implicit none

  real(p2), dimension(4), intent(in) :: w ! input
  real(p2), dimension(4)             :: u !output

   u(1) = w(ir)
   u(2) = w(ir)*w(iu)
   u(3) = w(ir)*w(iv)
   u(4) = w(ip)/(gamma-one)+half*w(ir)*(w(iu)*w(iu)+w(iv)*w(iv))

 end function w2u
!------------------------------------------------------------------------------

!********************************************************************************
! Compute U from W
!
! ------------------------------------------------------------------------------
!  Input:  u = conservative variables (rho, rho*u, rho*v, rho*E)
! Output:  w =    primitive variables (rho,     u,     v,     p)
! ------------------------------------------------------------------------------
!
! Note:    E = p/(gamma-1)/rho + 0.5*(u^2+v^2)
!       -> p = (gamma-1)*rho*E-0.5*rho*(u^2+v^2)
! 
!********************************************************************************
 function u2w(u) result(w)

  use module_common_data, only : p2, one, half

  implicit none

  real(p2), dimension(4), intent(in) :: u ! input
  real(p2), dimension(4)             :: w !output

    w(ir) = u(1)
    w(iu) = u(2)/u(1)
    w(iv) = u(3)/u(1)
    w(ip) = (gamma-one)*( u(4) - half*w(1)*(w(2)*w(2)+w(3)*w(3)) )

 end function u2w
!--------------------------------------------------------------------------------


 end module module_ccfv_data_soln

