!********************************************************************************
!  Educationally-Designed Unstructured 2D (EDU2D) Code
!
!  ---------------- EDU2D-Template02
!
! This is module_ccfv_data_soln.
!
! This module containes data required by a cell-centered FV discertization
! and a subroutine that constructs the data for a given grid.
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
! Katate Masatsuka, August 2018. http://www.cfdbooks.com
!********************************************************************************

 module module_mms

  implicit none

  !Subroutine that can be used in other modules/subroutines.

   public :: compute_manufactured_sol_and_f_euler

 contains

!********************************************************************************
! Educationally-Designed Unstructured 2D (EDU2D) Code
!
!  --- EDU2D_MMS_Euler
!
! This subroutine computes, for a given position (x,y), the manufactured
! solution values (w) and the forcing term (f) for the 2D Euler equations.
! The manufactured solution takes the following form:
!
!    w = c0 + cs*sin(cx*x+cy*y)
!
! with the coefficients, c0, cs, cx, cy chosen differently for different
! variable.
!
! The manufactured solution is the exact solution to the following equation:
!
!   dF(w)/dx + dG(w)/dy = f
!
! ------------------------
! Input:
!
!   (x,y) = Position at which the solution and forcing terms are sought.
!
! ------------------------
! Output:
!         w(1:4) = [rho,u,v,p] : Exact solution (sine functions)
!         f(1:4) = Forcing terms for continuity, x/y-momentum, and energy eqns.
!
! together satisfy dF(w)/dx + dG(w)/dy = f.
!
! ------------------------
!
!
! This is Version 1 (September, 2018).
!
! This F90 code is written and made available for an educational purpose.
! This file may be updated in future.
!
! Katate Masatsuka, http://www.cfdbooks.com
!********************************************************************************
 subroutine compute_manufactured_sol_and_f_euler(x,y, w,f)

 implicit none
 integer , parameter :: p2 = selected_real_kind(p=15)

 real(p2), parameter ::         pi = 3.141592653589793238_p2
 real(p2), parameter ::       half = 0.5_p2
 real(p2), parameter ::        one = 1.0_p2

!Input 
 real(p2),               intent( in) :: x, y

!Output
 real(p2), dimension(4), intent(out) :: w
 real(p2), dimension(4), intent(out) :: f

!Local variables

 real(p2) :: gamma

 real(p2) :: rho , u , v , p
 real(p2) :: rhox, ux, vx, px
 real(p2) :: rhoy, uy, vy, py

 real(p2) ::  a,  ax,  ay
 real(p2) ::  b,  bx,  by
 real(p2) ::  k,  kx,  ky

 real(p2) :: u2   , u2x   , u2y
 real(p2) :: v2   , v2x   , v2y

 real(p2) :: au   , aux   , auy
 real(p2) :: av   , avx   , avy
 real(p2) :: bu   , bux   , buy
 real(p2) :: bv   , bvx   , bvy
 real(p2) :: rhoH , rhoHx , rhoHy
 real(p2) :: rhouH, rhouHx, rhouHy
 real(p2) :: rhovH, rhovHx, rhovHy

 integer  :: iconti, ixmom, iymom, ienrgy

 real(p2) :: cr0, crs, crx, cry
 real(p2) :: cu0, cus, cux, cuy
 real(p2) :: cv0, cvs, cvx, cvy
 real(p2) :: cp0, cps, cpx, cpy

!-----------------------------------------------------------
! Ratio of specific heats for air. Let's assume air.

     gamma = 1.4_p2

!-----------------------------------------------------------
! Define some indices

    iconti =  1 ! continuity equation
    ixmom  =  2 ! x-momentum equation
    iymom  =  3 ! y-momentum equation
    ienrgy =  4 !     energy equation

!-----------------------------------------------------------
! Constants for the exact solution: c0 + cs*sin(cx*x+cy*y).
!
! Note: Make sure the density and pressure are positive.
! Note: These values are passed to the subroutine:
!         manufactured_sol(c0,cs,cx,cy, nx,ny,x,y),
!       whcih returns the solution value or derivatives.

 !-----------------------------------------
 ! Density    = cr0 + crs*sin(crx*x+cry*y)

  cr0 =  1.12_p2
  crs =  0.15_p2
  crx =  3.12_p2*pi
  cry =  2.92_p2*pi

 !-----------------------------------------
 ! X-velocity = cu0 + cus*sin(cux*x+cuy*y)

  cu0 =  1.32_p2
  cus =  0.06_p2
  cux =  2.09_p2*pi
  cuy =  3.12_p2*pi

 !-----------------------------------------
 ! Y-velocity = cv0 + cvs*sin(cvx*x+cvy*y)

  cv0 =  1.18_p2
  cvs =  0.03_p2
  cvx =  2.15_p2*pi
  cvy =  3.32_p2*pi

 !-----------------------------------------
 ! Pressure   = cp0 + cps*sin(cpx*x+cpy*y)

  cp0 =  1.62_p2
  cps =  0.31_p2
  cpx =  3.79_p2*pi
  cpy =  2.98_p2*pi

!-----------------------------------------------------------------------------
!-----------------------------------------------------------------------------
! Part I: Compute w = [rho,u,v,p] and grad(w).
!-----------------------------------------------------------------------------
!-----------------------------------------------------------------------------

 !------------------------------------------------------------------------
 ! rho: Density and its derivatives

      rho = manufactured_sol(cr0,crs,crx,cry, 0,0,x,y)
     rhox = manufactured_sol(cr0,crs,crx,cry, 1,0,x,y)
     rhoy = manufactured_sol(cr0,crs,crx,cry, 0,1,x,y)

 !------------------------------------------------------------------------
 ! u: x-velocity and its derivatives

       u  = manufactured_sol(cu0,cus,cux,cuy, 0,0,x,y)
       ux = manufactured_sol(cu0,cus,cux,cuy, 1,0,x,y)
       uy = manufactured_sol(cu0,cus,cux,cuy, 0,1,x,y)

 !------------------------------------------------------------------------
 ! v: y-velocity and its derivatives

       v  = manufactured_sol(cv0,cvs,cvx,cvy, 0,0,x,y)
       vx = manufactured_sol(cv0,cvs,cvx,cvy, 1,0,x,y)
       vy = manufactured_sol(cv0,cvs,cvx,cvy, 0,1,x,y)

 !------------------------------------------------------------------------
 ! p: pressure and its derivatives

       p  = manufactured_sol(cp0,cps,cpx,cpy, 0,0,x,y)
       px = manufactured_sol(cp0,cps,cpx,cpy, 1,0,x,y)
       py = manufactured_sol(cp0,cps,cpx,cpy, 0,1,x,y)

 !------------------------------------------------------------------------
 ! Store the exact solution in the array for return.

        w = (/ rho, u, v, p /)
 
!-----------------------------------------------------------------------------
!
! Exact (manufactured) solutons and derivatives have been computed.
! We move onto the forcing terms, which are the governing equations we wish
! to solve (the Euler) evaluated by the exact solution (i.e., 
! the function we wish to make exact with the forcing terms). See below.
!
! Euler:  dF(w)/dx + dG(w)/dy = 0.
!
! Our manufactured solutions, wm, are the exact soltuions to the following:
!
!   dF(w)/dx + dG(w)/dy = f,
!
! where f = dF(wm)/dx + dG(wm)/dy.
!
! So, if we solve
!
!   dF(w)/dx + dG(w)/dy = f
!
! then we can measure the discretization error (solution error): |w-wm|.
!
!-----------------------------------------------------------------------------

!-----------------------------------------------------------------------------
!-----------------------------------------------------------------------------
! Part II: Compute the forcing terms.
!-----------------------------------------------------------------------------
!-----------------------------------------------------------------------------

!-----------------------------------------------------------------------------
!-----------------------------------------------------------------------------
!-----------------------------------------------------------------------------
!  Inviscid terms
!-----------------------------------------------------------------------------
!-----------------------------------------------------------------------------
!-----------------------------------------------------------------------------

! The subroutine 'derivatives_ab" computes the product and derivatives of
! two variables (a,b): a*b, ax*b+a*bx, ay*b+a*by.


! Derivatives of u^2
  call derivatives_ab(u,ux,uy, u,ux,uy,  u2,u2x,u2y)

! Derivatives of v^2
  call derivatives_ab(v,vx,vy, v,vx,vy,  v2,v2x,v2y)

! Derivatives of k=(u^2+v^2)/2

  k     = half*(u*u  + v*v)
  kx    = half*(u2x   + v2x)
  ky    = half*(u2y   + v2y)

! Derivatives of rho*k = rho*(u^2+v^2)/2
  call derivatives_ab(rho,rhox,rhoy, k,kx,ky,  a,ax,ay) !a=rho*(u^2+v^2)/2

! Derivatives of rho*H = gamma/(gamma-1)*p + rho*k
  rhoH    = gamma/(gamma-one)*p    + a
  rhoHx   = gamma/(gamma-one)*px   + ax
  rhoHy   = gamma/(gamma-one)*py   + ay

!-----------------------------------------------------------------------------

! Compute derivatives of (rho*u)
  call derivatives_ab(rho,rhox,rhoy, u,ux,uy,   a,ax,ay) !a=(rho*u)

! Compute derivatives of (rho*v)
  call derivatives_ab(rho,rhox,rhoy, v,vx,vy,   b,bx,by) !b=(rho*v)

!-----------------------------------------------------------------------------

! Compute derivatives of (a*u)=(rho*u*u) !a=(rho*u)

  call derivatives_ab(a,ax,ay, u,ux,uy,      au,aux,auy)

! Compute derivatives of (a*v)=(rho*u*v) !a=(rho*u)

  call derivatives_ab(a,ax,ay, v,vx,vy,      av,avx,avy)

! Compute derivatives of (b*u)=(rho*v*u) !b=(rho*v)

  call derivatives_ab(b,bx,by,  u,ux,uy,     bu,bux,buy)

! Compute derivatives of (b*v)=(rho*v*v) !b=(rho*v)

  call derivatives_ab(b,bx, by, v,vx,vy,     bv,bvx,bvy)

!-----------------------------------------------------------------------------

! Compute derivatives of (u*rH)

  call derivatives_ab( u,ux,uy, rhoH,rhoHx,rhoHy,  rhouH,rhouHx,rhouHy)

! Compute derivatives of (v*rH)

  call derivatives_ab( v,vx,vy, rhoH,rhoHx,rhoHy,  rhovH,rhovHx,rhovHy)

!---------------------------------------------------------------------

!---------------------------------------------------------------------
! Store the inviscid terms in the forcing term array, f(:).
!---------------------------------------------------------------------

 !------------------------------------------------------
 ! Continuity:         (rho*u)_x   +   (rho*v)_y
    f(iconti)  = (rhox*u + rho*ux) + (rhoy*v + rho*vy)

 !------------------------------------------------------
 ! Momentum:     (rho*u*u)_x + (rho*u*v)_y + px
    f(ixmom)   =     aux     +    buy      + px

 !------------------------------------------------------
 ! Momentum:     (rho*u*v)_x + (rho*v*v)_y + px
    f(iymom)   =     avx     +    bvy      + py

 !------------------------------------------------------
 ! Energy:       (rho*u*H)_x + (rho*v*H)
    f(ienrgy)  =    rhouHx   +   rhovHy


 !Return f.

 ! Note: Later, we'll perform the following to compute the residual for
 !                   dF(w)/dx + dG(w)/dy = f
 !       Step 1. Comptue the residual: Res=dF(w)/dx + dG(w)/dy.
 !       Step 2. Subtract f: Res = Res - f.
 !

 end subroutine compute_manufactured_sol_and_f_euler

!********************************************************************************
!********************************************************************************

!********************************************************************************
!
! This subroutine computes first derivatives of a quadratic term
!
!  Input: a, ax, ay !Function value a, and its derivatives, (ax,ay).
!         b, bx, by !Function value b, and its derivatives, (bx,by).
!
! Output: ab = a*b, abx = d(a*b)/dx, aby = d(a*b)/dy.
!
!********************************************************************************
 subroutine derivatives_ab(a,ax,ay,  b,bx,by, ab,abx,aby)

 implicit none
 integer , parameter  :: p2 = selected_real_kind(p=15)

!Input
 real(p2), intent( in) ::  a,  ax,  ay
 real(p2), intent( in) ::  b,  bx,  by

!Output
 real(p2), intent(out) :: ab, abx, aby

  ab    = a*b 
  abx   = ax*b + a*bx
  aby   = ay*b + a*by

 end subroutine derivatives_ab

!********************************************************************************
!* This function computes the sine function:
!*
!*       f =  a0 + as*sin(ax*x+ay*y)
!*
!* and its derivatives:
!*
!*     df/dx^nx/dy^ny = d^{nx+ny}(a0+as*sin(ax*x+ay*y))/(dx^nx*dy^ny)
!*
!* depending on the input parameters:
!*
!*
!* Input:
!*
!*  a0,as,ax,ay = coefficients in the function: f =  a0 + as*sin(ax*x+ay*y).
!*            x = x-coordinate at which the function/derivative is evaluated.
!*            y = y-coordinate at which the function/derivative is evaluated.
!*           nx = nx-th derivative with respect to x (nx >= 0).
!*           ny = ny-th derivative with respect to y (ny >= 0).
!*
!* Output: The function value.
!*
!*
!* Below are some examples:
!*
!*     f =  a0 + as*sin(ax*x+ay*y)            !<- (nx,ny)=(0,0)
!*
!*    fx =  ax * as*cos(ax*x+ay*y)            !<- (nx,ny)=(1,0)
!*    fy =  ay * as*cos(ax*x+ay*y)            !<- (nx,ny)=(0,1)
!*
!*   fxx = -ax**2 * as*sin(ax*x+ay*y)         !<- (nx,ny)=(2,0)
!*   fxy = -ax*ay * as*sin(ax*x+ay*y)         !<- (nx,ny)=(1,1)
!*   fyy = -ay**2 * as*sin(ax*x+ay*y)         !<- (nx,ny)=(0,2)
!*
!*  fxxx = -ax**3        * as*cos(ax*x+ay*y)  !<- (nx,ny)=(3,0)
!*  fxxy = -ax**2 *ay    * as*cos(ax*x+ay*y)  !<- (nx,ny)=(2,1)
!*  fxyy = -ax    *ay**2 * as*cos(ax*x+ay*y)  !<- (nx,ny)=(1,2)
!*  fyyy = -       ay**3 * as*cos(ax*x+ay*y)  !<- (nx,ny)=(0,3)
!*
!* fxxxx =  ax**4        * as*sin(ax*x+ay*y)  !<- (nx,ny)=(4,0)
!* fxxxy =  ax**3 *ay    * as*sin(ax*x+ay*y)  !<- (nx,ny)=(3,1)
!* fxxyy =  ax**2 *ay**2 * as*sin(ax*x+ay*y)  !<- (nx,ny)=(2,2)
!* fxyyy =  ax    *ay**3 * as*sin(ax*x+ay*y)  !<- (nx,ny)=(1,3)
!* fyyyy =         ay**4 * as*sin(ax*x+ay*y)  !<- (nx,ny)=(0,4)
!*
!* and so on.
!*
!*
!********************************************************************************
 function manufactured_sol(a0,as,ax,ay, nx,ny,x,y) result(fval)

 implicit none
 integer , parameter  :: p2 = selected_real_kind(p=15)

!Input
 real(p2), intent(in) :: a0, as, ax, ay, x, y
 integer , intent(in) :: nx, ny

!Output
 real(p2)             :: fval

  if (nx < 0 .or. ny < 0) then
   write(*,*) " Invalid input: nx and ny must be greater or equal to zero... Try again."
   stop
  endif

  if ( nx+ny == 0 ) then

   fval = a0 + as*sin(ax*x + ay*y)

  elseif ( mod(nx+ny,2) == 0 ) then

   fval = - (ax**nx * ay**ny)*as*sin(ax*x + ay*y)
   if ( mod(nx+ny,4)   == 0 ) fval = -fval

  else

   fval = (ax**nx * ay**ny)*as*cos(ax*x + ay*y)
   if ( mod(nx+ny+1,4) == 0 ) fval = -fval

  endif


 end function manufactured_sol
!********************************************************************************



 end module module_mms

