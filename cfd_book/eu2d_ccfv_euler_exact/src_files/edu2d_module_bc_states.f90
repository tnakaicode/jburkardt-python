!********************************************************************************
!  Educationally-Designed Unstructured 2D (EDU2D) Code
!
!  ---------------- EDU2D-Template02
!
! This is module_bc_states.
!
!
! This module containes subroutines that solve the global system of nonlinear
! residual equations:
!
!     Res(U) = 0.
!
! - This is a nonlinear system solver, which some people call a steady solver.
!
! - So, this can solve unsteady residuals as well, which incorporate physical
!   time derivatives as source terms, or any nonlinear system as long as
!   a Jacobian is provided.
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
! Katate Masatsuka, October 2017. http://www.cfdbooks.com
!********************************************************************************

 module module_bc_states

 !This module contains the following subroutines:

  public :: get_right_state

 contains

!********************************************************************************
! 
! ------------------------------------------------------------------------------
!  Input: xb,yb = boundary face midpoint
!           ucL = Interior conservative variables (rho, rho*u, rho*v, rho*E)
!           njk = Outward boundary normal vector.
!           bc_state_type = BC name
! 
! Output:   ucb = Boundary state in conservative variables (rho, rho*u, rho*v, rho*E)
! ------------------------------------------------------------------------------
!
! Note:    E = p/(gamma-1)/rho + 0.5*(u^2+v^2)
!       -> p = (gamma-1)*rho*E-0.5*rho*(u^2+v^2)
!
!********************************************************************************
 subroutine get_right_state(xb,yb,ucL,njk,bc_state_type, ucb)

 use module_common_data     , only : p2
 use module_ccfv_data_soln  , only : u2w, w2u
 use module_mms             , only : compute_manufactured_sol_and_f_euler


 implicit none

!Input
 real(p2)              , intent( in) :: xb, yb
 real(p2), dimension(4), intent( in) :: ucL
 real(p2), dimension(2), intent( in) :: njk
 character(80),          intent( in) :: bc_state_type

!Output
 real(p2), dimension(4), intent(out) :: ucb

!Local variables
 real(p2), dimension(4) :: wL, wb
 real(p2), dimension(4) :: dummy

!---------------------------------------------------------
! Get the primitive variables [rho,u,v,p] as input to
! the following subroutines, which return the boundary
! state in the primitive variables.

  wL = u2w(ucL)

!---------------------------------------------------------
! Below, input is wLp = the primitive variabes [rho,u,v,p].
! Output is the right state in wRp = [rho,u,v,p].

  select case(trim(bc_state_type))

   case('freestream')

     call freestream(wb)

   case('outflow_subsonic')

     call back_pressure(wL, wb)

   case('symmetry_y')

     call symmetry_y(wL,njk, wb)

   case('slip_wall')

     call slip_wall(wL,njk, wb)

   case('outflow_supersonic')

     call outflow_supersonic(wL, wb)

   case('dirichlet')

    !Dirichlet assumes the manufactured solution: so, compute wb for (xb,yb).
     call compute_manufactured_sol_and_f_euler(xb,yb, wb,dummy)

   case default

     write(*,*) "Boundary condition=",trim(bc_state_type),"  not implemented."
     write(*,*) " --- Stop at get_right_state() in edu2d_module_bc_bc_states.f90..."
     stop

  end select

!---------------------------------------------------------
! Return the right state in conservative variables:
!                                 [rho,rho*u,rho*v,rho*E]

  ucb = w2u(wb)

 end subroutine get_right_state
!********************************************************************************


!********************************************************************************
! Freesteam
!********************************************************************************
 subroutine freestream(wb)

 use module_common_data   , only : p2
 use module_ccfv_data_soln, only : rho_inf, u_inf, v_inf, p_inf

 implicit none

 real(p2), dimension(4), intent(out) :: wb

   wb(1)    = rho_inf
   wb(2)    =   u_inf
   wb(3)    =   v_inf
   wb(4)    =   p_inf

 end subroutine freestream
!********************************************************************************


!********************************************************************************
! Subsonic outflow (Back Pressure)
!********************************************************************************
 subroutine back_pressure(wL, wb)

 use module_common_data   , only : p2
 use module_ccfv_data_soln, only : p_inf

 implicit none

 real(p2), dimension(4), intent( in) :: wL
 real(p2), dimension(4), intent(out) :: wb

!-------------------------
! Back pressure condition

   wb    = wL
   wb(4) = p_inf  !<- Just fix the pressure.

 end subroutine back_pressure
!********************************************************************************


!********************************************************************************
! Symmetry w.r.t. x-axis, which is called y-symmetry here.
!
! Note: This is a simplified implementation similar to slip wall condition.
!********************************************************************************
 subroutine symmetry_y(wL,njk, wb)

 use module_common_data, only : p2, zero

 implicit none

 real(p2), dimension(4), intent( in) :: wL
 real(p2), dimension(2), intent( in) :: njk
 real(p2), dimension(4), intent(out) :: wb

 real(p2) :: un

   un = wL(2)*njk(1) + wL(3)*njk(2)

!-------------------------
! Define the right state:

   wb = wL

! Ensure zero y-momentum flux on average:
!
   wb(3) = zero

! (ub,vb) = (uL,vL) - 2*un*njk -> 0.5[(ub,vb)+(uL,vL)]*njk = (0,0).
! Since rho_b = rhoL as set in the above, this means the momemtum
! in n direction is also zero.

 end subroutine symmetry_y
!********************************************************************************

 
!********************************************************************************
! Slip wall
!
!********************************************************************************
 subroutine slip_wall(wL,njk, wb)

 use module_common_data     , only : p2

 implicit none

 real(p2), dimension(4), intent( in) :: wL
 real(p2), dimension(2), intent( in) :: njk
 real(p2), dimension(4), intent(out) :: wb

 real(p2) :: un

   un = wL(2)*njk(1) + wL(3)*njk(2)

!-------------------------
! Define the right state:

   wb = wL

 ! Ensure zero normal velocity on average:

   wb(2) = wL(2) - un*njk(1)
   wb(3) = wL(3) - un*njk(2)

 end subroutine slip_wall
!********************************************************************************


!********************************************************************************
! Outflow supersonic
!********************************************************************************
 subroutine outflow_supersonic(wL, wb)

 use module_common_data     , only : p2

 implicit none

 real(p2), dimension(4), intent( in) :: wL
 real(p2), dimension(4), intent(out) :: wb

!---------------------------------------------
! Take everything from the interior.

  wb = wL

 end subroutine outflow_supersonic
!********************************************************************************


 end module module_bc_states
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------

