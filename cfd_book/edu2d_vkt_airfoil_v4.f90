!********************************************************************************
!* Subroutines for generating grids and computing exact solutions for the famous
!* Karman-Trefftz airfoil (includes the Jukowsky airfoil as a special case). 
!*
!*        written by Dr. Katate Masatsuka (info[at]cfdbooks.com),
!*
!* the author of useful CFD books, "I do like CFD" (http://www.cfdbooks.com).
!*
!* This is Version 4 (2019).
!*
!* Ver.4
!* 07-23-2019: Added .grid, .bcmap, .su2, .vkt, and tecplot files.
!* 
!* Ver.3
!* 10-12-11: Typo found in Eq.(7.10.58). The code corrected.
!*           [Thanks to Nico van den Berg for pointing out the problem.]
!*           generate_grids_kt_airfoil() should now work for cambered airfoils.
!*           exact_solution_kt_airfoil() still fails for highly-cambered airfoils.
!*           To be investigated.
!* 10-13-11: Connectivity of the triangulation has been modified to avoid
!*           vanishing area near the trailing edge.
!*
!* Ver.2
!* 03-07-11: Error found. Exact solution seems wrong on the line y=0 and x<0.
!*           Not sure how to fix now. Use an odd number for 'nx' to avoid the
!*           error. It works fine for a cylinder, though. Somebody, help me!
!* 03-08-11: A bug fixed on the numbering of triangles.
!* 03-08-11: It now generates a grid file with boundary info for an input to
!*           a flow solver.
!*
!* Ver.1
!* 12-29-10: Minor bugs fixed.
!*
!* These F90 routines were written and made available for download
!* for an educational purpose. Also, this is intended to provide all CFD
!* students and researchers with a tool for their code verification.
!*
!* This file may be updated in future.
!*
!* Katate Masatsuka, July 2019. http://www.cfdbooks.com
!********************************************************************************

!********************************************************************************
!* --- Driver code for the Karman-Trefftz airfoil ---
!* 
!* 1. Generate boundary points of the airfoil and Cp distribution.
!*    : The data is written in the file `airfoil.data'.
!*      It can be used as an input for other grid generation programs.
!*      Also, a Matlab file (vkt_airfoil_v1_display.m) that reads the data file
!*      and makes a plot is available for download.
!*
!* 2. Generate structured grids over the domain.
!*    : The grid data is written as a Tecplot file:
!*         airfoil_grid_soln_tec.dat     for a quadrilateral grid,
!*         airfoil_grid_soln_tri_tec.dat for a triangular grid.
!*
!*    : The grid data is written also as .grid file:
!*         airfoil_grid_soln.grid     for a quadrilateral grid,
!*         airfoil_grid_soln_tri.grid for a triangular grid.
!*      (These files contain boundary node information.)
!*
!* 3. Compute the exact solution on the grid points.
!*    : To demonstrate the ability of the subroutine 'exact_solution_kt_airfoil()'
!*      to compute the exact solution at a given point location in a physical
!*      domain. This subroutine can be used in your own code.
!*
!* Input ---------------------------------------------------
!*       ell = quater Chord length (chord=4*ell)
!*     alpha = Angle of attack (radian)
!*   epsilon = Thisckness
!*     kappa = Camber
!*       tau = Trailing edge angle (radian)
!*        nx = # of nodes in the circumferential direction.
!*        ny = # of nodes in the radial direction.
!*  distance = Distance to the outer boundary
!* 
!* Output --------------------------------------------------
!*  airfoil.data: boundary point and Cp data file
!*  airfoil_grid_soln_tec.dat : Tecplot grid data file for quadrilateral grid
!*                              (with exact solutions)
!*  airfoil_grid_soln_tri_tec.dat: Tecplot grid data file for triangular grid
!*                                 (with exact solutions)
!*
!*  Quad-grid files = airfoil_quad.grid
!*                    airfoil_quad.grid
!*                    airfoil_quad.su2
!*                    airfoil_quad.vtk
!*                    airfoil_quad_tec.dat
!*                    airfoil_quad_tec_b.dat_boundary.1.dat
!*                    airfoil_quad_tec_b.dat_boundary.2.dat
!*                    airfoil_quad_tec_b.dat_boundary.3.dat
!*                    airfoil_quad_tec_b.dat_boundary.4.dat
!*
!*  Tria-grid files = airfoil_tria.grid
!*                    airfoil_tria.grid
!*                    airfoil_tria.su2
!*                    airfoil_tria.vtk
!*                    airfoil_tria_tec.dat
!*                    airfoil_tria_tec_b.dat_boundary.1.dat
!*                    airfoil_tria_tec_b.dat_boundary.2.dat
!*                    airfoil_tria_tec_b.dat_boundary.3.dat
!*                    airfoil_tria_tec_b.dat_boundary.4.dat
!*
!*
!* Katate Masatsuka, March 2011. http://www.cfdbooks.com
!********************************************************************************
 program kt_airfoil
 implicit none
!Constants
 integer    , parameter :: sp = kind(1.0)
 integer    , parameter :: dp = selected_real_kind(2*precision(1.0_sp))
 real(dp)   , parameter :: zero=0.0_dp, one=1.0_dp, two=2.0_dp, four=4.0_dp
 real(dp)   , parameter :: pi=3.141592653589793238_dp

!Airfoil input parameters (See Section 7.10.4 of 'I do like CFD, VOL.1')
 real(dp), parameter ::     ell = 0.25_dp               !Chord length = 4*ell
 real(dp), parameter ::   alpha = 10.0_dp*(pi/180.0_dp) !Angle of attack
 real(dp), parameter :: epsilon = 0.10_dp               !Thickness
 real(dp), parameter ::   kappa = 0.15_dp               !Camber
 real(dp), parameter ::     tau = 10.0_dp*(pi/180.0_dp) !Trailing edge angle

!Cylinder version: tau=pi (NB: The stagnation is fixed at the rear end.)
! real(dp), parameter ::     ell = 0.5_dp              !Chord length = 4*ell
! real(dp), parameter ::   alpha = 0.0_dp*(pi/180.0_dp) !Angle of attack
! real(dp), parameter :: epsilon = 0.0_dp               !Thickness
! real(dp), parameter ::   kappa = 0.0_dp               !Camber
! real(dp), parameter ::     tau = pi                   !Trailing edge angle

!Grid input parameters
  integer, parameter :: nx = 161          !# of nodes around the airfoil (odd number)
  integer, parameter :: ny = 80          !# of nodes in the radial direction
 real(dp), parameter :: distance = 10.0_dp ! Distance to the outer boundary
 real(dp), parameter :: stretch_factor = 3.7_dp !Stretching factor in r-direction (>1.0)

!Local variables
 real(dp), dimension(:,:), allocatable :: x,y,psi,phi,u,v,cp
 real(dp) :: psie,phie,ue,ve,cpe, err_L1(5), err_max(5), x_max_err_phi(2)
 integer  :: i, j, k

 integer                               :: ntria, nquad, nnodes, inode
 integer , dimension(:,:), allocatable :: tria, quad
 real(dp), dimension(  :), allocatable :: xn, yn

 !- Boundary data requied by a solver.
 !   These are needed for .grid and .su2 files.
 integer                                :: ib, ic
 integer                                :: nb      !# of boundaries
 integer      , dimension(:  ), pointer :: nbnodes !# of nodes in each boundary
 integer      , dimension(:,:), pointer :: bnode   !List of boundary nodes
 character(80), dimension(:  ), pointer :: bnames  !Boundary names

 character(80) :: filename_grid
 character(80) :: filename_bcmap
 character(80) :: filename_su2
 character(80) :: filename_tec
 character(80) :: filename_tec_b
 character(80) :: filename_vtk


! 0. Allocate arrays.

  allocate(     x(nx, ny) )
  allocate(     y(nx, ny) )
  allocate(   psi(nx, ny) )
  allocate(   phi(nx, ny) )
  allocate(     u(nx, ny) )
  allocate(     v(nx, ny) )
  allocate(    cp(nx, ny) )

! 1. Grid generation for a specified Karman-Trefftz airfoil.
!    The exact solution will be computed and stored at each grid node.
!    The exact solution should be accurate for all possible parameter values.

 call generate_grids_kt_airfoil(ell,alpha,epsilon,kappa,tau, nx,ny,distance,&
                                           x,y,psi,phi,u,v,cp,stretch_factor)

!-----------------------------------------------------------
!-----------------------------------------------------------
!-----------------------------------------------------------
!-----------------------------------------------------------

  !Node data
   nnodes = (nx)*(ny)
   allocate( xn(nnodes), yn(nnodes) )

   do j = 1, ny
    do i = 1, nx
     inode = i + (j-1)*(nx)
       xn(inode) = x(i,j)
       yn(inode) = y(i,j)
    end do
   end do

  !Boundary data
   nb = 2
   allocate( bnode( max(ny+1,nx+1), nb) )
   allocate( nbnodes(nb) )
   allocate(  bnames(nb) )

  !(1)Airfoil: j = 1

      ib = 1
      bnames( ib) = "airfoil"
      nbnodes(ib) = nx+1
                j = 1

               ic = 1
     bnode(ic,ib) = 1
    do i = nx, 1, -1
            inode = i + (j-1)*nx
               ic = ic + 1
     bnode(ic,ib) = inode
    end do

  !(2)Farfield boundary: i = nx+1

      ib = 2
      bnames( ib) = "farfield"
      nbnodes(ib) = nx+1
               ic = 0

    do i = 1, nx
            inode = i + (ny-1)*nx
               ic = ic + 1
     bnode(ic,ib) = inode
    end do
     bnode(ic+1,ib) = 1 + (ny-1)*nx

   filename_bcmap = "airfoil_quad.bcmap"
   call write_bcmap_file(filename_bcmap, nb, bnames)

   filename_bcmap = "airfoil_tria.bcmap"
   call write_bcmap_file(filename_bcmap, nb, bnames)

 !-------------------------------------------------
 ! Quadrilateral grid

   write(*,*) " ------------------------------------- "
   write(*,*) "  Quadrilateral grid "
   write(*,*)

   ntria = 0
   nquad = 0
   allocate( tria(    1,3) )
   allocate( quad(nx*ny,4) )

   do j = 1, ny-1
     do i = 1, nx-1
       nquad = nquad + 1
       quad(nquad,1) = i+1 + (j-1)*(nx)
       quad(nquad,2) = i   + (j-1)*(nx)
       quad(nquad,3) = i   + (j  )*(nx)
       quad(nquad,4) = i+1 + (j  )*(nx)
     end do
       i = nx
       nquad = nquad + 1
       quad(nquad,1) = 1   + (j-1)*(nx)
       quad(nquad,2) = i   + (j-1)*(nx)
       quad(nquad,3) = i   + (j  )*(nx)
       quad(nquad,4) = 1   + (j  )*(nx)
   end do

   write(*,*) " nquad = ", nquad, "  nx*(ny-1) = ", nx*(ny-1)

   filename_grid  = "airfoil_quad.grid"
   call write_grid_file(filename_grid,nnodes,tria,ntria,quad,nquad,xn,yn, &
                                                       nb,nbnodes,bnode )
   filename_su2   = "airfoil_quad.su2"
   call write_su2_file(filename_su2,nnodes,tria,ntria,quad,nquad,xn,yn, &
                                              nb,nbnodes,bnode,bnames )
   filename_tec   = "airfoil_quad_tec.dat"
   call write_tecplot_file(filename_tec, nnodes,xn,yn, ntria,tria, &
                                                     nquad,quad  )

   filename_tec_b = "airfoil_quad_tec_b.dat"
   call write_tecplot_boundary_file(filename_tec_b,xn,yn,nb,nbnodes,bnode)

   filename_vtk   = "airfoil_quad.vtk"
   call write_vtk_file(filename_vtk, nnodes,xn,yn, ntria,tria, &
                                                 nquad,quad  )

   deallocate( tria, quad )

   write(*,*)
   write(*,*) " ------------------------------------- "

 !-------------------------------------------------
 ! Triangular grid

   write(*,*) " ------------------------------------- "
   write(*,*) "  Triangular grid "
   write(*,*)


   ntria = 0
   nquad = 0
   allocate( tria(2*nx*ny,3) )
   allocate( quad(      1,4) )

   do j = 1, ny-1
     do i = 1, nx-1

!    Split the quad
!       nquad = nquad + 1
!       quad(nquad,1) = i+1 + (j-1)*(nx) !1
!       quad(nquad,2) = i   + (j-1)*(nx) !2
!       quad(nquad,3) = i   + (j  )*(nx) !3
!       quad(nquad,4) = i+1 + (j  )*(nx) !4
!
!       i = nx
!       nquad = nquad + 1
!       quad(nquad,1) = 1   + (j-1)*(nx) !1
!       quad(nquad,2) = i   + (j-1)*(nx) !2
!       quad(nquad,3) = i   + (j  )*(nx) !3
!       quad(nquad,4) = 1   + (j  )*(nx) !4
!    into two triangles as below

! Triangular elements: diagonals are switched (top and bottom halves) to avoid
! vanishing elements at the trailing edge.

     if (i < nx/2+1 ) then
       ntria = ntria + 1
       tria(ntria,1) = i+1 + (j-1)*(nx) !1
       tria(ntria,2) = i   + (j-1)*(nx) !2
       tria(ntria,3) = i+1 + (j  )*(nx) !4

       ntria = ntria + 1
       tria(ntria,1) = i   + (j-1)*(nx) !2
       tria(ntria,2) = i   + (j  )*(nx) !3
       tria(ntria,3) = i+1 + (j  )*(nx) !4
     else
       ntria = ntria + 1
       tria(ntria,1) = i+1 + (j-1)*(nx) !1
       tria(ntria,2) = i   + (j-1)*(nx) !2
       tria(ntria,3) = i   + (j  )*(nx) !3

       ntria = ntria + 1
       tria(ntria,1) = i+1 + (j-1)*(nx) !1
       tria(ntria,2) = i   + (j  )*(nx) !3
       tria(ntria,3) = i+1 + (j  )*(nx) !4
     endif

     end do

       i = nx
       ntria = ntria + 1
       tria(ntria,1) = 1   + (j-1)*(nx) !1
       tria(ntria,2) = i   + (j-1)*(nx) !2
       tria(ntria,3) = i   + (j  )*(nx) !3

       ntria = ntria + 1
       tria(ntria,1) = 1   + (j-1)*(nx) !1
       tria(ntria,2) = i   + (j  )*(nx) !3
       tria(ntria,3) = 1   + (j  )*(nx) !4

   end do

   write(*,*) " ntria = ", ntria, "  2*(nx-1)*(ny-1) = ", 2*(nx-1)*(ny-1)

   filename_grid  = "airfoil_tria.grid"
   call write_grid_file(filename_grid,nnodes,tria,ntria,quad,nquad,xn,yn, &
                                                       nb,nbnodes,bnode )
   filename_su2   = "airfoil_tria.su2"
   call write_su2_file(filename_su2,nnodes,tria,ntria,quad,nquad,xn,yn, &
                                              nb,nbnodes,bnode,bnames )
   filename_tec   = "airfoil_tria_tec.dat"
   call write_tecplot_file(filename_tec, nnodes,xn,yn, ntria,tria, &
                                                     nquad,quad  )

   filename_tec_b = "airfoil_tria_tec_b.dat"
   call write_tecplot_boundary_file(filename_tec_b,xn,yn,nb,nbnodes,bnode)

   filename_vtk   = "airfoil_tria.vtk"
   call write_vtk_file(filename_vtk, nnodes,xn,yn, ntria,tria, &
                                                 nquad,quad  )

   deallocate( tria, quad )

   write(*,*)
   write(*,*) " ------------------------------------- "

!-----------------------------------------------------------
!-----------------------------------------------------------
!-----------------------------------------------------------
!-----------------------------------------------------------   

! 2. Computation of the exact solution on the grid generated above.
!
! NB: u(j,k) is the exact x-velocity at (x(j,k),y(j,k)) computed during the grid
!     generation. ue is the exact x-velocity computed by the subroutine,
!     'exact_solution_kt_airfoil()' with the coordinates (x(j,k),y(j,k)) as input.
!     We compare the two values; they must be the same. Similarly for other values.
!     HOWEVER, these solutions may not be accurate for highly-cambered airfoils.

  err_L1  = zero
  err_max = -10000000

 loop_radial : do k = 1, ny
  loop_circum : do j = 1, nx

  call exact_solution_kt_airfoil( x(j,k), y(j,k), ue,ve,cpe,phie,psie , &
                                        ell, alpha, epsilon, kappa, tau )

   err_L1(1) = err_L1(1) + abs(   ue -   u(j,k) ) 
   err_L1(2) = err_L1(2) + abs(   ve -   v(j,k) )
   err_L1(3) = err_L1(3) + abs(  cpe -  cp(j,k) ) 
!  Avoid the potential discontinuity (two solutions may no be the same).
   if (abs(y(j,k)) > 1.0e-14) err_L1(4) = err_L1(4) + abs( phie - phi(j,k) )
   err_L1(5) = err_L1(5) + abs( psie - psi(j,k) ) 

   err_max(1) = max( err_max(1), abs(   ue -   u(j,k) ) )
   err_max(2) = max( err_max(2), abs(   ve -   v(j,k) ) )
   err_max(3) = max( err_max(3), abs(  cpe -  cp(j,k) ) )
   if ( abs( phie - phi(j,k) ) > err_max(4) ) then
    x_max_err_phi(1)=x(j,k)
    x_max_err_phi(2)=y(j,k)
   endif
!  Avoid the potential discontinuity (two solutions may not be the same).
   if (abs(y(j,k)) > 1.0e-14) err_max(4) = max( err_max(4), abs( phie - phi(j,k) ) )
   err_max(5) = max( err_max(5), abs( psie - psi(j,k) ) )

  end do loop_circum
 end do loop_radial

 write(*,*) "-------- Differences (must be zero.) ----------"
 write(*,*) "          u          v         Cp          phi          psi"
 write(*,'(a7,5es10.3)' ) "L1  : ", err_L1/real(nx*ny,dp)
 write(*,'(a7,5es10.3)' ) "Linf: ", err_max
 write(*,'(a30,2es10.3)') "Linf_(error_phi) at (x,y) = ", x_max_err_phi

 write(*,*) 
 write(*,*) "NOTE: The differences may not be zero for highly cambered airfoils."
 write(*,*) "      The exact solution stored in the Tecplot and grid files should"
 write(*,*) "      be correct. It is the solution computed by "
 write(*,*) "      exact_solution_kt_airfoil() that may not be correct for cambered"
 write(*,*) "      airfoils. This problem is to be investigated."
 write(*,*)

 stop
!--------------------------------------------------------------------------------
!* End of Main Program
!--------------------------------------------------------------------------------

 contains

!********************************************************************************
!* This generates boundary points and computational (structured quadrilateral
!* and triangular) grids for a domain of Karman-Trefftz airfoil, based on the
!* algorithm described in the book,
!*    "I do like CFD, VOL.1" by Katate Masatuka (http://www.cfdbooks.com).
!* 
!* 1. Generate boundary points of the airfoil and Cp distribution.
!*    : The data is written in the file `airfoil.data'.
!*      It can be used as an input for other grid generation programs.
!*      Also, a Matlab file (vkt_airfoil_v1_display.m) that reads the data file
!*      and makes a plot is available for download.
!*
!* 2. Generate structured grids over the domain.
!*    : The grid data is written as a Tecplot file:
!*         airfoil_grid_soln_tec.dat     for a quadrilateral grid,
!*         airfoil_grid_soln_tri_tec.dat for a triangular grid.
!*
!*    : The grid data is written also as .grid file:
!*         airfoil_grid_soln.grid     for a quadrilateral grid,
!*         airfoil_grid_soln_tri.grid for a triangular grid.
!*      (These files contain boundary node information.)
!*
!* Input ---------------------------------------------------
!*       ell = quater Chord length (chord=4*ell)
!*     alpha = Angle of attack (radian)
!*   epsilon = Thisckness
!*     kappa = Camber
!*       tau = Trailing edge angle (radian)
!*        nx = # of nodes in the circumferential direction.
!*        ny = # of nodes in the radial direction.
!*  distance = Distance to the outer boundary
!*
!*  (See Section 7.10.4 of 'I do like CFD, VOL.1' for details.)
!*
!* Output --------------------------------------------------
!*  airfoil.data: boundary point and Cp data file
!*  airfoil_grid_soln_tec.dat : Tecplot grid data file for quadrilateral grid
!*                              (with exact solutions)
!*  airfoil_grid_soln_tri_tec.dat: Tecplot grid data file for triangular grid
!*                                 (with exact solutions)
!*
!* Katate Masatsuka, Januray 2010. http://www.cfdbooks.com
!********************************************************************************
 subroutine generate_grids_kt_airfoil(ell,alpha,epsilon,kappa,tau, nx,ny,distance,&
                                      x,y,psi,phi,u,v,cp,stretch_factor)
 implicit none
!Constants
 integer    , parameter :: sp = kind(1.0)
 integer    , parameter :: dp = selected_real_kind(2*precision(1.0_sp))
 real(dp)   , parameter :: zero=0.0_dp, one=1.0_dp, two=2.0_dp
 real(dp)   , parameter :: pi=3.141592653589793238_dp
 complex(dp), parameter :: i = cmplx(zero,one, dp) !Imaginray number

!Input
 real(dp), intent(in) :: ell, alpha, epsilon, kappa, tau !Airfoil parameters
 integer , intent(in) :: nx, ny !# of nodes in circumferential and radial directions
 real(dp), intent(in) :: distance !Distance to the outer boundary
 real(dp), intent(in) :: stretch_factor !Stretching factor in r-direction (>1.0)
!Output: grid and exact solution data
 real(dp), dimension(nx,ny), intent(out) :: x,y,psi,phi,u,v,cp

!Local variables
 real(dp)    :: a, n, beta, theta, xi, eta, r, r01
 complex(dp) :: mu, zeta, temp, Z, f, w, dZdzeta
 integer     :: j, k, inode

!Additioanl airfoil parameters (determined by the input parameters)
!(See Figure 7.10.8 of 'I do like CFD, VOL.1')

     a = ell*sqrt( (one+epsilon)**2 + kappa**2 ) !Radius of the circle

  if (ell*kappa/a > one) then
   write(*,*) " Camber parameter, kappa, is too large. Reduce kappa, and try again."
   stop
  endif

  beta = asin(ell*kappa/a)                       !Angle of the TE location - Typo in Eq. (7.10.58)
     n = two - tau/pi                            !Parameter related to TE angle
    mu = cmplx(-ell*epsilon,ell*kappa, dp)       !Center of the circle.

!********************************************************************************
! 1. Generate a KT-airfoil(at k=1): nodes ordered counterclockwise from TE
!********************************************************************************
! Open a file for the airfoil geometry with Cp for matlab visualization.
  open(1,FILE='airfoil.data',STATUS='unknown')

 k = 1 !Airfoil surface
 airfoil_boundary : do j = 1, nx
 theta = real(j-1, dp)*(two*pi)/real(nx, dp) !theta = [0, 2*pi]

! Coordinates in the circle plane: zeta = (xi, eta). Eqs.(7.10.77) and (7.10.78)

      xi = a*cos(theta-beta) + real(mu) !Note that theta=0 corresponds to TE.
     eta = a*sin(theta-beta) + imag(mu)
    zeta = cmplx(xi,eta, dp)

! Coordinates in the airfoil plane: Z = (x,y). Eq.(7.10.66)

      temp = (zeta-ell)**n/(zeta+ell)**n
         Z = n*ell*( one + temp )/( one - temp ) !Karman-Trefftz transformation
    x(j,k) = real(Z)
    y(j,k) = imag(Z)

! f(zeta): Complex potential in the circle plane. Eq.(7.10.59)

          f = cmplx_potential(zeta, alpha,beta,a,mu,i)
   phi(j,k) = real(f) ! Scalar potential (can be discontinuous for lifting flows)
   psi(j,k) = imag(f) ! Stream function

! w(zeta): Complex velocity in the circle plane (a flow around a cylinder) Eq.(7.10.60)

   w = cmplx_velocity(zeta, alpha,beta,a,mu,i)

!-- Compute the velocity in the airfoil plane: (u,v) = w/(dZ/dzeta)

! Derivative of the Karman-Trefftz transformation. Eq.(7.10.68) (There is a typo in the boo!)

   dZdzeta = derivative(zeta, ell,n)

! Special treatment at the trailing edge(theta=zero).
  if ( theta == zero ) then
!  (1)Joukowski airfoil (cusped trailing edge: tau = 0.0)
!     Use L'Hopital's rule for w/dZdzeta: Derive yourself. You can do it!
   if (tau == zero) then
     u(j,k) =  real( ell/a*exp(two*i*beta)*cos(alpha+beta) )
     v(j,k) = -imag( ell/a*exp(two*i*beta)*cos(alpha+beta) )
    cp(j,k) =  one - ( u(j,k)**2 + v(j,k)**2 )
!  (2)Karman-Trefftz airfoil (finite angle: tau > 0.0)
!     TE must be a stagnation point.
   else
     u(j,k) =  zero
     v(j,k) =  zero
    cp(j,k) =  one
   endif
! Elsewhere (anywhere not TE): (u,v) = w/(dZ/dzeta) Eq.(7.10.61)
  else
    u(j,k) = real(w/dZdzeta)
    v(j,k) =-imag(w/dZdzeta)
   cp(j,k) = one - ( u(j,k)**2 + v(j,k)**2 )
  endif

! Write down the data.
  write(1,*) x(j,k),y(j,k),cp(j,k)

 end do airfoil_boundary

! Record the first point at the end to close the airfoil contour.
  write(1,*) x(1,k),y(1,k),cp(1,k)

 close(1)
 write(*,*) "Airfoil geometry and Cp data has been written -> airfoil.data"
 write(*,*) "Run the matlab script vkt_airfoil_v1_display.m to view the results."
 write(*,*)
!********************************************************************************
! 2. Generate grid points between the outer boundary and the airfoil
!    by mapping circles in the circle plane onto the airfoil plane.
!    Stretching is applied in the radial direction to make the cell nearly
!    a square.
!********************************************************************************
 interior_k : do k = 2, ny

    r = real(k-1,dp)*(distance-a)/real(ny-1,dp) + a !   r = [a,distance]
  r01 = (r-a)/(distance-a)                          ! r01 = [0,1]
    !Apply stretching in r01.
    r = ( one - exp(stretch_factor*r01) )/( one - exp(stretch_factor) )
    r = r*(distance-a) + a                          !Transform back to r.

  interior_j : do j = 1, nx
 
   theta = real(j-1,dp)*(two*pi)/real(nx,dp)

! Coordinates in the circle plane: zeta = (xi,eta)

      xi = r*cos(theta-beta) + real(mu)
     eta = r*sin(theta-beta) + imag(mu)
    zeta = cmplx(xi,eta, dp)

! Coordinates in the airfoil plane: Z = (x,y)

      temp = (zeta-ell)**n/(zeta+ell)**n
         Z = n*ell*( one + temp )/( one - temp ) !Karman-Trefftz transformation
    x(j,k) = real(Z)
    y(j,k) = imag(Z)

! f(zeta): Complex potential in the circle plane.

          f = cmplx_potential(zeta, alpha,beta,a,mu,i)
   phi(j,k) = real(f) ! Scalar potential (can be discontinuous for lifting flows)
   psi(j,k) = imag(f) ! Stream function

! w(zeta): Complex velocity in the circle plane.

   w = cmplx_velocity(zeta, alpha,beta,a,mu,i)

!-- Velocity in the airfoil plane: (u,v) = w/(dZ/dzeta)

!  dZdzeta = dZ/dzeta: the derivative of the KT transformation

   dZdzeta = derivative(zeta, ell,n)

    u(j,k) = real(w/dZdzeta)
    v(j,k) =-imag(w/dZdzeta)
   cp(j,k) = one - ( u(j,k)**2 + v(j,k)**2 )

  end do interior_j
 end do interior_k

!********************************************************************************
! 3. Write a Tecplot file of a quadrilateral grid which includes the
!    exact solution values.
!********************************************************************************
 write(*,*) "Writing a Tecplot file (quadrilateral grid)..."
 open(unit=10, file ="airfoil_grid_soln_tec.dat", status="unknown")
 write(10,*) "TITLE = GRID" 
 write(10,*) "VARIABLES = x, y, u, v, cp, phi, psi"
 write(10,*) "ZONE  N=",nx*ny, ",E=" , nx*(ny-1), &
             " ,ET=QUADRILATERAL, F=FEPOINT"

! nodes: coordinates and exact solutions.
  do k = 1, ny
   do j = 1, nx
    write(10,'(7ES20.10)') x(j,k),y(j,k),u(j,k),v(j,k),cp(j,k),phi(j,k),psi(j,k)
   end do
  end do

! Quadrilateral elements
  do k = 1, ny-1
    do j = 1, nx-1
      write(10,*) nx*(k-1)+j, nx*k+j, nx*k+(j+1), nx*(k-1)+(j+1)
    end do
      j = nx
      write(10,*) nx*(k-1)+j, nx*k+j, nx*k+1, nx*(k-1)+1
  end do

 close(10) 
 write(*,*) "Quadrilateral grid data has been written -> airfoil_grid_soln_tec.dat"
 write(*,*) "Use Tecplot to display the results (grid and exact solutions)"
 write(*,*)
!********************************************************************************
! 4. Write a Tecplot file of a triangular grid which includes the
!    exact solution values.
!********************************************************************************
 write(*,*) "Writing a Tecplot file (triangular grid)..."
 open(unit=11, file ="airfoil_grid_soln_tri_tec.dat", status="unknown")
 write(11,*) "TITLE = GRID" 
 write(11,*) "VARIABLES = x, y, u, v, cp, phi, psi"
 write(11,*) "ZONE  N=",nx*ny, ",E=" , 2*nx*(ny-1), &
             " ,ET=TRIANGLE, F=FEPOINT"

! nodes: coordinates and exact solutions.
  do k = 1, ny
   do j = 1, nx
    write(11,'(7ES20.10)') x(j,k),y(j,k),u(j,k),v(j,k),cp(j,k),phi(j,k),psi(j,k)
   end do
  end do

! Triangular elements: diagonals are switched (top and bottom halves) to avoid
! vanishing elements at the trailing edge.
  do k = 1, ny-1
    do j = 1, nx-1
     if (j > nx/2 ) then
      write(11,*) nx*(k-1)+j  , nx*k+j, nx*(k-1)+j+1
      write(11,*) nx*(k-1)+j+1, nx*k+j ,    nx*k+j+1
     else
      write(11,*) nx*(k-1)+j+1, nx*(k-1)+j, nx*k+(j+1)
      write(11,*) nx*(k-1)+j,     nx*k+j  , nx*k+j+1
     endif
    end do
      j = nx
     if (j > nx/2 ) then
      write(11,*) nx*(k-1)+j, nx*k+j, nx*(k-1)+1
      write(11,*) nx*(k-1)+1, nx*k+j ,    nx*k+1
     else
      write(11,*) nx*(k-1)+j, nx*k+1, nx*(k-1)+1
      write(11,*) nx*(k-1)+j, nx*k+j,     nx*k+1
     endif
  end do

 close(11)
 write(*,*) "Triangular grid data has been written -> airfoil_grid_soln_tri_tec.dat"
 write(*,*) "Use Tecplot to display the results (grid and exact solutions)"
 write(*,*)

!********************************************************************************
! 5. Write a grid file of a quad grid.
!********************************************************************************
 write(*,*) "Writing a grid file (quadrilateral grid)..."
 open(unit=12, file ="airfoil_grid_quad.grid", status="unknown")

! Grid size: # of nodes, # of triangles, # of quadrilaterals
  write(12,*)      nx*ny,              0,           nx*(ny-1)

! Node data
  do k = 1, ny
   do j = 1, nx
    write(12,'(7ES20.10)') x(j,k), y(j,k)
   end do
  end do

! Quads
  do k = 1, ny-1
    do j = 1, nx-1
      write(12,*) nx*(k-1)+j, nx*k+j, nx*k+(j+1), nx*(k-1)+(j+1)
    end do
      j = nx
      write(12,*) nx*(k-1)+j, nx*k+j, nx*k+1, nx*(k-1)+1
  end do

! Boundary nodes are ordered counterclockwise (interior domain on the left)
  write(12,*) 2  !2 boundary segments
  write(12,*) nx+1 !Airfoil
  write(12,*) nx+1 !Outer Boundary

! Airfoil
    write(12,*) 1
   do j = nx, 1, -1
    inode = j
    write(12,*) inode
   end do
! Outer Boundary
  do j = 1, nx
    inode = j + (ny-1)*nx
    write(12,*) inode
  end do
    write(12,*) 1 + (ny-1)*nx

 close(12)
 write(*,*) "Quadrilateral grid data has been written -> airfoil_grid_quad.grid"
 write(*,*)

!********************************************************************************
! 6. Write a grid file of a triangular grid.
!********************************************************************************
 write(*,*) "Writing a grid file (triangular grid)..."
 open(unit=13, file ="project.grid", status="unknown")

! Grid size: # of nodes, # of triangles, # of quadrilaterals
  write(13,*)      nx*ny,   2*nx*(ny-1),                   0

! Node data
  do k = 1, ny
   do j = 1, nx
    write(13,'(7ES20.10)') x(j,k), y(j,k)
   end do
  end do

! Triangular elements: diagonals are switched (top and bottom halves) to avoid
! vanishing elements at the trailing edge.
  do k = 1, ny-1
    do j = 1, nx-1
     if (j > nx/2 ) then
      write(13,*) nx*(k-1)+j  , nx*k+j, nx*(k-1)+j+1
      write(13,*) nx*(k-1)+j+1, nx*k+j ,    nx*k+j+1
     else
      write(13,*) nx*(k-1)+j+1, nx*(k-1)+j, nx*k+(j+1)
      write(13,*) nx*(k-1)+j,       nx*k+j, nx*k+j+1
     endif
    end do
      j = nx
     if (j > nx/2 ) then
      write(13,*) nx*(k-1)+j, nx*k+j, nx*(k-1)+1
      write(13,*) nx*(k-1)+1, nx*k+j ,    nx*k+1
     else
      write(13,*) nx*(k-1)+j, nx*k+1, nx*(k-1)+1
      write(13,*) nx*(k-1)+j, nx*k+j,     nx*k+1
     endif
  end do

! Boundary nodes are ordered counterclockwise (interior domain on the left)
  write(13,*) 2  !2 boundary segments
  write(13,*) nx+1 !Airfoil
  write(13,*) nx+1 !Outer Boundary

! Airfoil
    write(13,*) 1
   do j = nx, 1, -1
    inode = j
    write(13,*) inode
   end do
! Outer Boundary
  do j = 1, nx
    inode = j + (ny-1)*nx
    write(13,*) inode
  end do
    write(13,*) 1 + (ny-1)*nx

 close(13)
 write(*,*) "Triangular grid data has been written -> airfoil_grid_tria.grid"
 write(*,*)

 return
 end subroutine generate_grids_kt_airfoil
!********************************************************************************

!********************************************************************************
!* This computes the exact solution of the KT airfoil for a given 
!* physical location (x,y) in the airfoil plane.
!*
!*        written by Dr. Katate Masatsuka (info[at]cfdbooks.com),
!*
!* the author of useful CFD books, "I do like CFD" (http://www.cfdbooks.com).
!*
!* This is Version 1 (2010).
!*
!* Input ---------------------------------------------------
!*  The following parameters are required to define the airfoil shape and the flow.
!*       ell = quater Chord length (chord=4*ell)
!*     alpha = Angle of attack (radian)
!*   epsilon = Thisckness
!*     kappa = Camber
!*       tau = Trailing edge angle (radian)
!*     (x,y) = The location (in the physical airfoil domain) where the solution
!*             is sought.
!*
!* Output --------------------------------------------------
!*  (u,v) = Velocity (divided by the free stream)
!*     cp = Pressure coefficient
!*    phi = Velocity potential
!*    psi = Stream function (contours are the streamlines)
!* 
!* This F90 routine was written and made available for download
!* for an educational purpose. Also, this is intended to provide all CFD
!* students and researchers with a tool for their code verification.
!*
!* This file may be updated in future.
!*
!* Katate Masatsuka, Januray 2010. http://www.cfdbooks.com
!********************************************************************************
 subroutine exact_solution_kt_airfoil(x,y,  u,v,cp,phi,psi , &
                            ell, alpha, epsilon, kappa, tau )
 implicit none
!Constants
 integer    , parameter :: sp = kind(1.0)
 integer    , parameter :: dp = selected_real_kind(2*precision(1.0_sp))
 real(dp)   , parameter :: zero=0.0_dp, one=1.0_dp, two=2.0_dp
 real(dp)   , parameter :: pi=3.141592653589793238_dp
 complex(dp), parameter :: i=cmplx(zero,one,dp)
!Input
 real(dp), intent( in) :: x,y                             !Location
 real(dp), intent( in) :: ell, alpha, epsilon, kappa, tau !Airfoil parameters
!Output
 real(dp), intent(out) :: u,v,cp,phi,psi                  !Exact solutions
!Local variables
 real(dp)    :: a, beta, n
 complex(dp) :: mu, Z, zeta, temp, f, w, dZdzeta, zetaTE

!Additional airfoil parameters (determined by the input parameters)
!(See Figure 7.10.8 of 'I do like CFD, VOL.1')

           a = ell*sqrt( (one+epsilon)**2 + kappa**2 ) !Radius of the circle

  if (ell*kappa/a > one) then
   write(*,*) " Camber parameter, kappa, is too large. Reduce kappa, and try again."
   stop
  endif

        beta = asin(ell*kappa/a)                       !Angle of TE location - Typo in Eq. (7.10.58)
           n = two - tau/pi                            !Parameter related to TE angle
          mu = cmplx(-ell*epsilon,ell*kappa, dp)       !Center of the circle.
      zetaTE = mu + a*exp(-i*beta)                     !zeta corresponds to the TE

!Inverse transform to map Z=(x,y) into zeta=(xi,eta). Eq.(7.10.67)

       Z = cmplx(x,y, dp)
    temp = (Z-n*ell)**(one/n)/(Z+n*ell)**(one/n)
    zeta = ell*( one + temp )/( one - temp )

!Compute the exact solutions in the circle plane (zeta-plane).

  f = zeta*exp(-i*alpha)                   & ! Free stream
    + i*two*a*sin(alpha+beta)*log(zeta-mu) & ! Vortex
    + a*a*exp(i*alpha)/(zeta-mu)             ! Doublet     Eq.(7.10.59)

  w = exp(-i*alpha)                        & ! Free stream
    + i*two*a*sin(alpha+beta)/(zeta-mu)    & ! Vortex
    - a*a*exp(i*alpha)/( (zeta-mu)**2 )      ! Doublet     Eq.(7.10.60)

  dZdzeta = four*(n*ell)**2*(zeta+ell)**(n-one)*(zeta-ell)**(n-one) &
            / ( (zeta+ell)**n - (zeta-ell)**n )**2 ! Eq.(7.10.68) (There is a typo in the book!)

  phi =  real(f) ! Scalar potential (discontinuous for a lifting case)
  psi =  imag(f) ! Stream function

! Special treatment at the trailing edge:
  if ( abs(zeta-zetaTE) < 1.0e-12_dp ) then
!  (1)Joukowski airfoil (cusped trailing edge: tau = 0.0)
!     Use L'Hopital's rule for w/dZdzeta: Derive yourself. You can do it!
   if (tau == zero) then
     u =  real( ell/a*exp(two*i*beta)*cos(alpha+beta) )
     v = -imag( ell/a*exp(two*i*beta)*cos(alpha+beta) )
!  (2)Karman-Trefftz airfoil (finite angle: tau > 0.0)
!     TE must be a stagnation point.
   else
     u =  zero
     v =  zero
   endif
! Elsewhere (anywhere not TE): (u,v) = w/(dZ/dzeta)
  else
     u =  real(w/dZdzeta)       ! x-velocity
     v = -imag(w/dZdzeta)       ! y-velocity
  endif

    cp =  one - ( u**2 + v**2 ) ! Pressure coefficient

 return
 end subroutine exact_solution_kt_airfoil

!********************************************************************************
! Complex potential in the circle plane (zeta-plane): Eq.(7.10.59)
 function cmplx_potential(zeta, alpha,beta,a,mu,i)
 implicit none
 complex(dp), intent(in) :: zeta, mu,i
    real(dp), intent(in) :: alpha, beta, a
 complex(dp)             :: cmplx_potential

  cmplx_potential = zeta*exp(-i*alpha)                     & ! Free stream
                    + i*two*a*sin(alpha+beta)*log(zeta-mu) & ! Vortex
                    + a*a*exp(i*alpha)/(zeta-mu)             ! Doublet
 return
 end function cmplx_potential
!********************************************************************************
! Complex velocity in the circle plane (zeta-plane):  Eq.(7.10.60)
 function cmplx_velocity(zeta, alpha,beta,a,mu,i)
 implicit none
 complex(dp), intent(in) :: zeta, mu,i
    real(dp), intent(in) :: alpha, beta, a
 complex(dp)             :: cmplx_velocity

  cmplx_velocity = exp(-i*alpha)                       & ! Free stream
                   + i*two*a*sin(alpha+beta)/(zeta-mu) & ! Vortex
                   - a*a*exp(i*alpha)/( (zeta-mu)**2 )   ! Doublet
 return
 end function cmplx_velocity
!********************************************************************************
! Derivative of the KT transformation: Eq.(7.10.68) (There is a typo in the book!)
 function derivative(zeta, ell,n)
 implicit none
 complex(dp), intent(in) :: zeta
    real(dp), intent(in) :: ell, n
 complex(dp)             :: derivative

  derivative = four*(n*ell)**2*((zeta+ell)*(zeta-ell))**(n-one) &
             / ( (zeta+ell)**n - (zeta-ell)**n )**2

 return
 end function derivative

!********************************************************************************






!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------


!*******************************************************************************
! This subroutine writes a Tecplot file for the grid.
!*******************************************************************************
 subroutine write_tecplot_file(filename, nnodes,x,y, ntria,tria, nquad,quad  )

  implicit none

  character(80),                 intent(in) :: filename
  integer      ,                 intent(in) :: nnodes, ntria, nquad
  real(dp)     , dimension(:  ), intent(in) :: x, y
  integer      , dimension(:,:), intent(in) :: tria
  integer      , dimension(:,:), intent(in) :: quad

!Local variables
  integer :: i, os

 write(*,*)
 write(*,*) ' Writing a Tecplot file = ', trim(filename)
 write(*,*)

  open(unit=9, file=filename, status="unknown", iostat=os)

  write(9,*) 'TITLE = "Grid"'
  write(9,*) 'VARIABLES = "x","y"'
!---------------------------------------------------------------------------
! zone

   write(9,*) 'zone t=', '"grid"'
   write(9,*)'  n=', nnodes,',e=', ntria+nquad,' , et=quadrilateral, f=fepoint'

   do i = 1, nnodes
     write(9,'(2es25.15)') x(i), y(i)
   end do

  if (ntria > 0) then
   do i = 1, ntria
    write(9,'(4i10)') tria(i,1), tria(i,2), tria(i,3), tria(i,3)
   end do
  endif

  if (nquad > 0) then
   do i = 1, nquad
    write(9,'(4i10)') quad(i,1), quad(i,2), quad(i,3), quad(i,4)
   end do
  endif

!---------------------------------------------------------------------------

 close(9)

 end subroutine write_tecplot_file
!********************************************************************************


!********************************************************************************
! This subroutine writes boundary grid files.
!********************************************************************************
 subroutine write_tecplot_boundary_file(filename,x,y,nb,nbnodes,bnode )

 implicit none

 character(80),                 intent(in) :: filename
 real(dp)     , dimension(:)  , intent(in) :: x, y
 integer                      , intent(in) :: nb
 integer      , dimension(:  ), intent(in) :: nbnodes
 integer      , dimension(:,:), intent(in) :: bnode

!Local variables
 character(80) :: filename_loc
 character(80) :: bid
 integer       :: ib, os

  do ib = 1, nb

     write( bid  , '(i0)' ) ib
     filename_loc = trim(filename) // trim("_boundary") // trim(".") // trim(bid) // '.dat'

   write(*,*)
   write(*,*) ' Writing a Tecplot file for boundary = ', ib , trim(filename_loc)
   write(*,*)

   open(unit=10, file=filename_loc, status="unknown", iostat=os)

    write(10,*) 'variables = "x", "y"'
    write(10,*) 'ZONE t="', trim("Boundary.") // trim(bid) ,'" I =', nbnodes(ib), ', DATAPACKING=POINT'

    do i = 1, nbnodes(ib)
     write(10,*) x( bnode(i,ib) ), y( bnode(i,ib) )
    end do

   close(10)

  end do

 end subroutine write_tecplot_boundary_file

!********************************************************************************
! This subroutine writes a grid file to be read by a solver.
! NOTE: Unlike the tecplot file, this files contains boundary info.
!********************************************************************************
 subroutine write_grid_file(filename,nnodes,tria,ntria,quad,nquad,x,y, &
                                                      nb,nbnodes,bnode )

 implicit none

 character(80),                 intent(in) :: filename
 integer                      , intent(in) :: nnodes, ntria, nquad
 integer      , dimension(:,:), intent(in) :: tria, quad
 real(dp)     , dimension(:)  , intent(in) :: x, y
 integer                      , intent(in) :: nb
 integer      , dimension(:  ), intent(in) :: nbnodes
 integer      , dimension(:,:), intent(in) :: bnode

!Local variables
 integer  :: os, i, j

   write(*,*)
   write(*,*) " Writing .grid file: ", trim(filename)

!--------------------------------------------------------------------------------
 open(unit=1, file=filename, status="unknown", iostat=os)

!--------------------------------------------------------------------------------
! Grid size: # of nodes, # of triangles, # of quadrilaterals
  write(1,*) nnodes, ntria, nquad

!--------------------------------------------------------------------------------
! Node data
  do i = 1, nnodes
   write(1,*) x(i), y(i)
  end do

!--------------------------------------------------------------------------------
! Triangle connectivity
  if (ntria > 0) then
   do i = 1, ntria
    write(1,*) tria(i,1), tria(i,2), tria(i,3)
   end do
  endif

  if (nquad > 0) then
   do i = 1, nquad
    write(1,*) quad(i,1), quad(i,2), quad(i,3), quad(i,4)
   end do
  endif

!--------------------------------------------------------------------------------
! Boundary data:
!
! The number of boundary segments
  write(1,*) nb

! The number of nodes in each segment:
  do i = 1, nb
   write(1,*) nbnodes(i)
  end do

  write(1,*)

! List of boundary nodes
  do i = 1, nb

   write(*,*) " write_grid_file: nbnodes(i) = ", nbnodes(i), i

   do j = 1, nbnodes(i)
    write(1,*) bnode(j,i)
   end do
    write(1,*)

  end do

!--------------------------------------------------------------------------------
 close(1)

 end subroutine write_grid_file
!********************************************************************************



!*******************************************************************************
! This subroutine writes a .bcmap for the grid.
!*******************************************************************************
 subroutine write_bcmap_file(filename, nb, bnames)

  implicit none

 character(80),                 intent(in) :: filename
 integer                      , intent(in) :: nb
 character(80),   dimension(:), intent(in) :: bnames

!Local variables
  integer :: i, os

 write(*,*)
 write(*,*) ' Writing a .bcmap file = ', trim(filename)
 write(*,*)

  open(unit=9, file=filename, status="unknown", iostat=os)


  write(9,*) "      Boundary Part          Boundary Condition"

  do i = 1, nb
   write(9,'(i20,a28)') i, '"' // trim(bnames(i)) // '"'
  end do

  close(9)

 end subroutine write_bcmap_file
!********************************************************************************

!*******************************************************************************
! This subroutine writes a su2 grid file.
!
! Note: Nodes -> i = 0,1,2,...; Elements -> i = 0,1,2,...
!
!
!  Identifier:
!  Line 	 3
!  Triangle 	 5
!  Quadrilateral 9
!  Tetrahedral 	10
!  Hexahedral 	12
!  Prism 	13
!  Pyramid 	14
!
!
!*******************************************************************************
 subroutine write_su2_file(filename,nnodes,tria,ntria,quad,nquad,x,y, &
                                              nb,nbnodes,bnode,bnames )

 character(80),                 intent(in) :: filename
 integer                      , intent(in) :: nnodes, ntria, nquad
 integer      , dimension(:,:), intent(in) :: tria, quad
 real(dp)     , dimension(:)  , intent(in) :: x, y
 integer                      , intent(in) :: nb
 integer      , dimension(:  ), intent(in) :: nbnodes
 integer      , dimension(:,:), intent(in) :: bnode
 character(80), dimension(:)  , intent(in) :: bnames

!Local variables
 integer :: i, ib, j, os

   write(*,*)
   write(*,*) " Writing .su2 file: ", trim(filename)

  open(unit=7, file=filename, status="unknown", iostat=os)

  write(7,*) "%"
  write(7,*) "% Problem dimension"
  write(7,*) "%"
  write(7,5) 2
5 format('NDIME= ',i12)

   write(7,*) "%"
   write(7,*) "% Inner element connectivity"
   write(7,10) ntria + nquad
10 format('NELEM= ',i12)

 !-------------------------------------------------------------------------
 ! Elements

  if (ntria > 0) then
   do i = 1, ntria
    write(7,'(4i20)') 5, tria(i,1)-1, tria(i,2)-1, tria(i,3)-1
   end do
  endif

  if (nquad > 0) then
   do i = 1, nquad
    write(7,'(5i20)') 9, quad(i,1)-1, quad(i,2)-1, quad(i,3)-1, quad(i,4)-1
   end do
  endif

 !--------------------------------------------------------------------------
 ! Nodes

   write(7,*) "%"
   write(7,*) "% Node coordinates"
   write(7,*) "%"
   write(7,20) nnodes
20 format('NPOIN= ', i12)

  ! Nodes
    do i = 1, nnodes
     write(7,'(2es26.15)') x(i), y(i)
    end do

 !--------------------------------------------------------------------------
 ! Boundary

30  format('NMARK= ',i12)
40  format('MARKER_TAG= ',a)
50  format('MARKER_ELEMS= ', i12)

    write(7,*) "%"
    write(7,*) "% Boundary elements"
    write(7,*) "%"
    write(7,30) nb !# of boundary parts.

   do ib = 1, nb

   !-------------------------
   !Just to print on screen
    write(*,*)
    write(*,40) trim(bnames(ib)) !ib-th boundary-part name, e.g., "farfield".
    write(*,50) nbnodes(ib)-1    !# of boundary elements (edges)
   !-------------------------

    write(7,40) trim(bnames(ib)) !ib-th boundary-part name, e.g., "farfield".
    write(7,50) nbnodes(ib)-1    !# of boundary elements (edges)

    do j = 1, nbnodes(ib)-1
     write(7,'(3i20)') 3, bnode(j,ib)-1, bnode(j+1,ib)-1
    end do

   end do

  close(7)

 end subroutine write_su2_file
!********************************************************************************

!*******************************************************************************
! This subroutine writes a .vtk file for the grid whose name is defined by
! filename_vtk.
!
! Use Paraview to read .vtk and visualize it.  https://www.paraview.org
!
! Search in Google for 'vkt format' to learn .vtk file format.
!*******************************************************************************
 subroutine write_vtk_file(filename, nnodes,x,y, ntria,tria, nquad,quad  )

  implicit none

  character(80),                 intent(in) :: filename
  integer      ,                 intent(in) :: nnodes, ntria, nquad
  real(dp)     , dimension(:  ), intent(in) :: x, y
  integer      , dimension(:,:), intent(in) :: tria
  integer      , dimension(:,:), intent(in) :: quad

!Local variables
  integer :: i, j, os

 !------------------------------------------------------------------------------
 !------------------------------------------------------------------------------
 !------------------------------------------------------------------------------

  write(*,*)
  write(*,*) ' Writing .vtk file = ', trim(filename)
  write(*,*)

 !Open the output file.
  open(unit=8, file=filename, status="unknown", iostat=os)

!---------------------------------------------------------------------------
! Header information

  write(8,'(a)') '# vtk DataFile Version 3.0'
  write(8,'(a)') filename
  write(8,'(a)') 'ASCII'
  write(8,'(a)') 'DATASET UNSTRUCTURED_GRID'

!---------------------------------------------------------------------------
! Nodal information
!
! Note: These nodes i=1,nnodes are interpreted as i=0,nnodes-1 in .vtk file.
!       So, later below, the connectivity list for tria and quad will be
!       shifted by -1.

   write(8,*) 'POINTS ', nnodes, ' double'

   do j = 1, nnodes
    write(8,'(3es25.15)') x(j), y(j), zero
   end do

!---------------------------------------------------------------------------
! Cell information.

  !CELLS: # of total cells (tria+quad), total size of the cell list.

  write(8,'(a,i12,i12)') 'CELLS ',ntria+nquad, (3+1)*ntria + (4+1)*nquad

  ! Note: The latter is the number of integer values written below as data.
  !           4 for triangles (# of vertices + 3 vertices), and
  !           5 for quads     (# of vertices + 4 vertices).

  !---------------------------------
  ! 2.1 List of triangles (counterclockwise vertex ordering)

   if (ntria > 0) then
                         ! (# of vertices = 3), 3 vertices in counterclockwise
    do i = 1, ntria
     write(8,'(a,4i12)') '3', tria(i,1)-1, tria(i,2)-1, tria(i,3)-1
                         ! -1 since VTK reads the nodes as 0,1,2,3,..., not 1,2,3,..
    end do
   endif

  !---------------------------------
  ! 2.2 List of quads (counterclockwise vertex ordering)

   if (nquad > 0) then
                         ! (# of vertices = 4), 4 vertices in counterclockwise
    do i = 1, nquad
     write(8,'(a,4i12)') '4', quad(i,1)-1, quad(i,2)-1, quad(i,3)-1, quad(i,4)-1
                         ! -1 since VTK reads the nodes as 0,1,2,3,..., not 1,2,3,..
    end do
   endif

!---------------------------------------------------------------------------
! Cell type information.

                                   !# of all cells
  write(8,'(a,i11)') 'CELL_TYPES ', ntria+nquad

  !Triangle is classified as the cell type 5 in the .vtk format.

  if (ntria > 0) then
   do i = 1, ntria
    write(8,'(i3)') 5
   end do
  endif

  !Triangle is classified as the cell type 9 in the .vtk format.

  if (nquad > 0) then
   do i = 1, nquad
    write(8,'(i3)') 9
   end do
  endif

!--------------------------------------------------------------------------------
! NOTE: Commented out because there are no solution data. This part should be
!       uncommented if this is used in a solver or if solution data are available
!       and one would like to plot them.
!
! Field data (e.g., density, pressure, velocity)are added here for visualization.

!   write(8,*) 'POINT_DATA   ',nnodes

!  !            FIELD  dataName    # of arrays (variables to plot) <--This is a commnet.
!   write(8,*) 'FIELD  FlowField ', 4

!   write(8,*) 'Density   ',  1 , nnodes, ' double'
!   do j = 1, nnodes
!    write(8,'(es25.15)') w(j,1)
!   end do

!   write(8,*) 'X-velocity ', 1 , nnodes, ' double'
!   do j = 1, nnodes
!    write(8,'(es25.15)') w(j,2)
!   end do

!   write(8,*) 'Y-veloiity ', 1 , nnodes, ' double'
!   do j = 1, nnodes
!    write(8,'(es25.15)') w(j,3)
!   end do

!   write(8,*) 'Pressure   ', 1 , nnodes, ' double'
!   do j = 1, nnodes
!    write(8,'(es25.15)') w(j,4)
!   end do

!---------------------------------------------------------------------------

 !Close the output file. <--This is a commnet.
  close(8)


 end subroutine write_vtk_file
!********************************************************************************







 end program kt_airfoil