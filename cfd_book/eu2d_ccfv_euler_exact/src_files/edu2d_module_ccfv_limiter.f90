!********************************************************************************
!  Educationally-Designed Unstructured 2D (EDU2D) Code
!
!  ---------------- EDU2D-CCFV-Euler-EXPLCT
!
! This is module_ccfv_limiter.
!
! This module containes data and subroutines required to apply a limiter
! for discontinuous capturing with 2nd-order scheme without oscillations.
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

 module module_ccfv_limiter

  use module_common_data, only : p2, one, zero !To declare double precision variables below.

  implicit none

  !Data that can be used in other modules/subroutines.
   public :: phi

  !Subroutine that can be used in other modules/subroutines.
   public :: compute_limiter

  !The data defined below will not be used in other modules and main program.
  !So, they are not declared as public here.

 !------------------------------------------------------------------------------------
 !------------------------------------------------------------------------------------
 ! Below are the definition of the data used to a LSQ gradient method.
 !------------------------------------------------------------------------------------

  !------------------------------------------
  !>> Cell-centered limiter data
  !------------------------------------------

     real(p2), dimension(:), pointer :: phi !limiter function


  !These data will be allocated for a given grid size, and filled in the
  !following subroutine: compute_lsq_coefficients.

 !------------------------------------------------------------------------------------
 ! End of the data used to implement a LSQ gradient method.
 !------------------------------------------------------------------------------------
 !------------------------------------------------------------------------------------

 contains

!*******************************************************************************
! Compute limiter functions
!
!*******************************************************************************
 subroutine compute_limiter

  use module_common_data   , only : p2, zero, x, y
  use module_ccfv_data_grid, only : ncells, cell
  use module_ccfv_data_soln, only : gradw, w

  use module_ccfv_gradient , only : cclsq

  implicit none

  integer  :: i, ivar, k, nghbr_cell, iv
  real(p2) :: wmin, wmax, xc, yc, xp, yp, wf, dwm, dwp
  real(p2) :: phi_vertex, phi_vertex_min, limiter_beps
  real(p2) :: phi_var_min


   allocate(phi(ncells))

   limiter_beps = 1.0e-14_p2

  !Loop over cells

   cell_loop : do i = 1, ncells

   !Loop over primitive variables

    variable_loop : do ivar = 1, 4

     !----------------------------------------------------
     ! Find the min and max values.
    
      !Initialize them with the solution at the current cell.
      !which could be min or max.

        wmin = w(i,ivar)
        wmax = w(i,ivar)
 
       !Loop over LSQ neighbors and find min and max.
        nghbr_loop : do k = 1, cclsq(i)%nnghbrs_lsq
         nghbr_cell = cclsq(i)%nghbr_lsq(k)
               wmin = min(wmin, w(nghbr_cell,ivar) )
               wmax = max(wmax, w(nghbr_cell,ivar) )
        end do nghbr_loop

     !----------------------------------------------------
     ! Compute phi to enforce maximum principle at vertices (MLP)
    
         xc = cell(i)%xc
         yc = cell(i)%yc

       !Loop over vertices of the cell i: 3 or 4 vertices for tria or quad.
        vertex_loop : do k = 1, cell(i)%nvtx

         iv = cell(i)%vtx(k)
         xp = x(iv)
         yp = y(iv)

        !Linear reconstruction to the vertex k
         wf = w(i,ivar) + gradw(i,ivar,1)*(xp-xc) + gradw(i,ivar,2)*(yp-yc)

        !Compute dw^-.
          dwm = wf - w(i,ivar)

        !Increase magnitude by 'limiter_beps' without changin sign.
        ! dwm = sign(one,dwm)*(abs(dwm) + limiter_beps)

        !Compute dw^+.
          if ( dwm > zero ) then
            dwp = wmax - w(i,ivar)
          else
            dwp = wmin - w(i,ivar)
          endif

        !Increase magnitude by 'limiter_beps' without changin sign.
        !  dwp = sign(one,dwp)*(abs(dwp) + limiter_beps)

        !Note: We always have dwm*dwp >= 0 by the above choice!!! So, r=a/b>0 always!!!

        ! Limiter function: Venkat limiter

          phi_vertex = vk_limiter(dwp, dwm, cell(i)%vol)

        ! Keep the minimum over the control points (vertices).
 
         if (k==1) then
          phi_vertex_min = phi_vertex
         else
          phi_vertex_min = min(phi_vertex_min, phi_vertex)
         endif

        end do vertex_loop

      !Keep the minimum over variables.

       if (ivar == 1) then
         phi_var_min = phi_vertex_min
       else
         phi_var_min = min(phi_var_min, phi_vertex_min)
       endif

    end do variable_loop


   !Set the minimum phi over the control points and over the variables to be
   !our limiter function. We'll use it for all variables to be on a safe side.

    phi(i) = phi_var_min

   end do cell_loop


 end subroutine compute_limiter
!*******************************************************************************

!********************************************************************************
!* -- Venkat Limiter Function--
!*
!* 'Convergence to Steady State Solutions of the Euler Equations on Unstructured
!*  Grids with Limiters', V. Venkatakrishnan, JCP 118, 120-130, 1995.
!*
!* The limiter has been implemented in such a way that the difference, b, is
!* limited in the form: b -> vk_limiter * b.
!*
!* ------------------------------------------------------------------------------
!*  Input:     a, b     : two differences
!*
!* Output:   vk_limiter : to be used as b -> vk_limiter * b.
!* ------------------------------------------------------------------------------
!*
!********************************************************************************
  pure function vk_limiter(a, b, vol)

  use module_common_data    , only : p2, two, pi, half

  real(p2), intent(in) :: a, b
  real(p2), intent(in) :: vol

  real(p2)             :: vk_limiter
  real(p2)             :: Kp
  real(p2)             :: eps2, diameter

!  real(p2)             :: r

   Kp = 5.0_p2   !<<<<< Adjustable parameter K

!   Mesh dependent constant (See Eqn.(33) in the paper) in Venkat limiter.
!   chokkei = (6.0_p2*elm(i)%vol/pi)**(1.0_p2/3.0_p2) ! 3D version
!      eps2 = (Kp*chokkei)**3

   diameter = two*(vol/pi)**half  ! 2D version = 2 times the diamater
       eps2 = (Kp*diameter)**3

! This is the form used by Venkat. This is in the form of
! limited_slope(a,b) / b, so that limited_slope(a,b) part resembles
! Van Albada's original limiter. And this way, he follows Van Albada
! and introduced epsilon to avoid limiting in nearly constant regions.
!
!    vk_limiter = ( b*(a**2 + eps2) + two*b**2*a )/(a**2 + two*b**2 + a*b + eps2) / b

! The above is equivalent to the following. This is within [0,1], well,
! it overshoots 1.0 near r=1.0, but approaches to 1.0 as r goes large...

     vk_limiter = ( (a**2 + eps2) + two*b*a )/(a**2 + two*b**2 + a*b + eps2)

!            r = a/b
!   vk_limiter = ( r + abs(r) ) / (one + abs(r) )
!   vk_limiter = ( two*r ) / (one + r )
!   vk_limiter = two*( a*b + eps )/( a**2 + b**2 + two*eps ) / b

  end function vk_limiter



 end module module_ccfv_limiter

