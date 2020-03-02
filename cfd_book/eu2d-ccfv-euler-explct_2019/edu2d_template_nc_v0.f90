module edu2d_template_nc

 private

 public :: main_nc

 contains

!********************************************************************************
! Educationally-Designed Unstructured 2D (EDU2D) Code
!
! This is a main template for a node-centered (NC) schemes.
!
! A grid has been loaded, and necessary data have been constructed before
! this subroutine gets called. It has been done in edu2d_main.f90, 
! which is the main driver code and call this subroutine.
!
!
! Here, we do the following:
!
!  1. Construct LSQ gradient coefficients (linear and quadratic) at all nodes.
!  2. Verify the LSQ coefficients (exact for linear and quadratic functions)
!  3. Set some initial solution and exact solutions.
!  4. Compute some residual and update the solution: A dummy solver as an example.
!     NOTE: This is just an example, by which you get an idea about how to implement
!           your own solver, hopefully.
!  5. Write out tecplot files for viewing the solution and the grid.
!
!
!        written by Dr. Katate Masatsuka (info[at]cfdbooks.com),
!
! the author of useful CFD books, "I do like CFD" (http://www.cfdbooks.com).
!
! This is Version 0 (July 2015).
! This F90 code is written and made available for an educational purpose.
! This file may be updated in future.
!
!********************************************************************************
 subroutine main_nc(datafile_nc_tec,datafile_nc_tec_b)

 use edu2d_constants   , only : p2, zero, half
 use edu2d_my_main_data, only : nnodes, node, edge, nedges, nbound, bound, gradient_type

!Output data file
 character(80) :: datafile_nc_tec    !Tecplot file for viewing the result: Entire domain
 character(80) :: datafile_nc_tec_b  !Tecplot file for viewing the result: Boundary

!-- Variables used in a dummy solver ----------------------------------------
 integer  :: iteration, max_iteration, node1, node2, n1, n2, i, j, ix=1, iy=2
 real(p2) :: mag_n12, mag_e12, nx,ny, ex,ey, dt
 real(p2) :: uL(3),uR(3), bflux1(3),bflux2(3), num_flux(3)
!-----------------------------------------------------------------------------

! Compute LSQ gradient coefficients: linear LSQ and quadratic LSQ
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Computing LSQ coefficients (at nodes)... "
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  call compute_lsq_coeff_nc

! Check LSQ gradient coefficients: linear LSQ and quadratic LSQ
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Checking the LSQ coefficients... "
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  call check_lsq_coeff_nc

! Store the initial and exact solutions.
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Setting initial and exact solutions... "
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  call initial_and_exact_solutions_nc


! At this point, given the grid data and the initial solution at nodes, 
! we are ready to solve some target equation and obtain numerical solution.

!---------------------------------------------------------------------------
!---------------------------------------------------------------------------
!---------------------------- Beginning of Solver --------------------------
!---------------------------------------------------------------------------
!---------------------------------------------------------------------------
! NOTE: This is a dummy solver (it doens't solve anything actually!).
!
! Solver should be placed here, which takes the initial soluton and compute
! numerical solutions for a target equation. Here, as this is just a template
! code and we don't know what equation we wish to solve, we just make a loop
! over edges and compute something like a residual for a kind of node-centered
! finite-volume method and pretend to update the solution in an explicit 
! manner, and exit.
!
! Note: Do not try to understand the details of the following part.
!       It is intended to be just an example of how the grid data are used
!       to compute the residual or update the solution, etc.

  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> NC Solver begins here....."
  write(*,*)

  max_iteration = 3
  iteration_loop : do iteration = 1, max_iteration

! 1. Computation of residual

   !Initialize the residul array.
   nodes : do i = 1, nnodes
    node(i)%res = zero
   end do nodes

   !Compute the gradients at nodes
    call compute_gradient_nc(1,gradient_type) ! gradients of u(1)
    call compute_gradient_nc(2,gradient_type) ! gradients of u(2)
    call compute_gradient_nc(3,gradient_type) ! gradients of u(3)

   ! Flux computation across internal edges (to be accumulated in res(:))
   !
   !   node2              1. Extrapolate the solutions to the edge-midpoint
   !       o                 from the nodes, node1 and node2.
   !        \   face      2. Compute the numerical flux
   !         \ -------c2  3. Add it to the residual for node1, and subtract it from
   !        / \              the residual for node2.
   !   face/   \ edge
   !      /     o         Directed area is the sum of the left and the right faces.
   !    c1    node1       Left/right face is defined by the edge-midpoint and
   !                      the centroid of the left/right element.
   !                      Directed area is positive in node1 -> node2
   !
   ! (c1, c2: element centroids)
   !
   !(1)Compute numerical flux at interior edges and accumulate at nodes.
   edges : do i = 1, nedges

      node1 = edge(i)%n1  ! Left node of the edge
      node2 = edge(i)%n2  ! Right node of the edge
    mag_n12 = edge(i)%da  ! Magnitude of the directed area vector
    mag_e12 = edge(i)%e   ! Magnitude of the edge vector (Length of the edge)
 
     !Directed area, n=(nx,ny), and edge vectors, e=(ex,ey).
     !Skewness is measured by n*e: Non-skewed mesh => n*e=0, Highly skewed mesh => n*e~0.

         nx = edge(i)%dav(ix) ! This is the directed area vector (unit vector)
         ny = edge(i)%dav(iy)
         ex = edge(i)%ev( ix) ! This is the vector along the edge (unit vector)
         ey = edge(i)%ev( iy)

     !Linear extrapolation of the solution from node1 and node2 to the edge-midpoint.
     uL = node(node1)%u + half*( node(node1)%gradu(:,ix)*ex + node(node1)%gradu(:,iy)*ey )*mag_e12
     uR = node(node2)%u - half*( node(node2)%gradu(:,ix)*ex + node(node2)%gradu(:,iy)*ey )*mag_e12

     !A kind of central flux defined at edge-midpoint.
     num_flux = half*(uL+uR)

     node(node1)%res = node(node1)%res  + num_flux *mag_n12 ! Add numerical flux to node 1
     node(node2)%res = node(node2)%res  - num_flux *mag_n12 ! Subtract it from node 2

   end do edges

   !(2)Close the residual by boundary flux contributions.
   !   Note: We consider a weak boundary procedure here.
   !         Boundary condition is imposed in a ghost state, which is sent to
   !         a numerical flux to determine the flux through the boundary.
 
   !-------------------------------------------------------------------------
   ! Close with the boundary flux using the element-based formula that is
   ! exact for linear fluxes (See Nishikawa AIAA2010-5093 for boundary weights
   ! that ensure the linear exactness for 2D/3D elements. The paper is avaiable at
   ! http://www.hiroakinishikawa.com/My_papers/nishikawa_AIAA-2010-5093.pdf  )
   !
   !      |  Interior Domain          |
   !      |        .........          |
   !      |        .       .          |
   !      |        .       .          |
   !      o--o--o-----o---------o--o--o  <- Boundary segment
   !                  n1   |    n2
   !                       v
   !                     n12 (unit face normal vector)
   !
   ! NOTE: We visit each boundary face, defined by the nodes n1 and n2,
   !       and compute the flux across the boundary face: left half for n1,
   !       and the right half for n2. In the above figure, the dots indicate
   !       the control volume around the node n1. Clearly, the flux across the
   !       left half of the face contributes to the node n1. Similarly for n2.
   !
   !
   bc_loop : do i = 1, nbound

    bfaces : do j = 1, bound(i)%nbfaces

         n1 = bound(i)%bnode(j  )  !Left node
         n2 = bound(i)%bnode(j+1)  !Right node
         nx = bound(i)%bfnx(j)     !x-component of the unit face normal vector
         ny = bound(i)%bfny(j)     !y-component of the unit face normal vector
    mag_e12 = bound(i)%bfn(j)
    mag_n12 = bound(i)%bfn(j)*half !Half length of the boundary face, j.

      !Left node = n1
       uL = node(n1)%u
       uR = node(n1)%uexact ! Boundary condition given by the exact solution.
       bflux1 = half*(uL+uR)! Again, a central flux

      !Right node = n2
       uL = node(n2)%u
       uR = node(n2)%uexact ! Boundary condition given by the exact solution.
       bflux2 = half*(uL+uR)! Again, a central flux

      !This is a well known formula for 2nd-order accuracy for triangular grids.
       node(n1)%res = node(n1)%res + (5.0_p2*bflux1 + bflux2)/6.0_p2*mag_n12
       node(n2)%res = node(n2)%res + (5.0_p2*bflux2 + bflux1)/6.0_p2*mag_n12
      !See JCP2015v281pp518-555 for details (weights depend on the element):
      !http://www.hiroakinishikawa.com/My_papers/nishikawa_jcp2015v281pp518-555_preprint.pdf

    end do bfaces
   end do bc_loop

! For implicit solvers, a linear solver should be placed here.
! Not considered in this tempalte code.

! 2. Update solutions

   !Some kind of explicit update
    dt = zero !<- Let's keep it zero, here. This is a dummy solver, anyway...
   nodes_update : do i = 1, nnodes
    node(i)%u = node(i)%u + dt*node(i)%res
   end do nodes_update

  end do iteration_loop

!---------------------------------------------------------------------------
!---------------------------------------------------------------------------
!------------------------------- End of Solver -----------------------------
!---------------------------------------------------------------------------
!---------------------------------------------------------------------------
  write(*,*)
  write(*,*)
  write(*,*) ">>> NC Solver ends here....."
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

! So, at this point, numerical solutions have been computed by some method.
! It is time to write out the data.

! Write out the tecplot data file in the entire domain (Solutions at nodes)
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Writing a tecplot file for viewing the grid and the solution..."
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  call write_tecplot_file(   datafile_nc_tec )
  write(*,*) " file name = ", datafile_nc_tec

! Write out the tecplot data file for boundaries (Solutions at nodes)
! Note: This is a data file containing only the boundary data.
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Writing a tecplot file for boundary data..."
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  call write_tecplot_file_b( datafile_nc_tec_b )
  write(*,*) " file name = ", datafile_nc_tec_b

!--------------------------------------------------------------------------------

  write(*,*)
  write(*,*) "Computation successfully completed (main_nc). Stop."
  write(*,*)
  write(*,*)

 end subroutine main_nc

!********************************************************************************
!* Set initial and exact solutions
!*
!* Exact solution here has no meaning as we don't know what equation we solve.
!* So, just set u1=x, u2=2*y, u3=3*x: just random choice.
!*
!*  Written by Katate Masatsuka, http://www.cfdbooks.com
!********************************************************************************
 subroutine initial_and_exact_solutions_nc

 use edu2d_constants     , only : p2, one, two, three
 use edu2d_my_main_data  , only : nnodes, node

 implicit none

!Local variables
 integer  :: i
 real(p2) :: x, y

!----------------------------------------------------------
  nodes : do i = 1, nnodes

   x = node(i)%x
   y = node(i)%y

!  Solution u1(x,y)
   node(i)%uexact(1) = one*x

!  Solution u2(x,y)
   node(i)%uexact(2) = two*y

!  Solution u3(x,y)
   node(i)%uexact(3) = three*x

!  Set initial numerical solution to be exact
   node(i)%u = node(i)%uexact

  end do nodes
!----------------------------------------------------------

 end subroutine initial_and_exact_solutions_nc
!********************************************************************************

!********************************************************************************
!* Write a tecplot file: grid and solution
!*
!*  Written by Katate Masatsuka, http://www.cfdbooks.com
!********************************************************************************
 subroutine write_tecplot_file(datafile_tec)

 use edu2d_my_main_data, only : nnodes, node, elm, nelms

 implicit none

!Input
 character(80), intent(in) :: datafile_tec

 integer :: i, k, os

!--------------------------------------------------------------------------------
 open(unit=1, file=datafile_tec, status="unknown", iostat=os)

  write(1,*) 'title = "grid"'
  write(1,'(a100)') 'variables = "x","y","u1","u2","u3","u1exact","u2exact","u3exact"'
  write(1,*) 'zone n=',nnodes,' e =', nelms,' et=quadrilateral, f=fepoint'

! Nodal quantities: x, y, u1, u2, u3

  do i = 1, nnodes
   write(1,*) node(i)%x, node(i)%y, (node(i)%u(k),k=1,3), (node(i)%uexact(k),k=1,3)
  end do

! Both quad and tria elements in quad format:

  do i = 1, nelms

   !Triangles
   if (elm(i)%nvtx == 3) then

    write(1,*) elm(i)%vtx(1), elm(i)%vtx(2), elm(i)%vtx(3), elm(i)%vtx(3)

   !Quadrilaterals
   elseif (elm(i)%nvtx == 4) then

    write(1,*) elm(i)%vtx(1), elm(i)%vtx(2), elm(i)%vtx(3), elm(i)%vtx(4)

   else

    !Impossible
    write(*,*) " Error in elm%vtx data... Stop..: elm(i)%nvtx=",elm(i)%nvtx
    stop

   endif

  end do

!--------------------------------------------------------------------------------
 close(1)
 end subroutine write_tecplot_file
!********************************************************************************


!********************************************************************************
!* Write a tecplot file: grid and solution on bourdaries
!*
!*  Written by Katate Masatsuka, http://www.cfdbooks.com
!********************************************************************************
 subroutine write_tecplot_file_b(datafile_tec)

 use edu2d_my_main_data           , only : node, bound, nbound

 implicit none

!Input
 character(80), intent(in) :: datafile_tec

 integer :: i, k, os, j, ibn

!--------------------------------------------------------------------------------
 open(unit=1, file=datafile_tec, status="unknown", iostat=os)

 write(1,*) 'title = "boundary data"'

 write(1,'(a)') 'variables = "x","y","u1","u2","u3","u1exact","u2exact","u3exact"'

 bc_loop : do i = 1, nbound

  write(1,*) 'zone t=',trim(bound(i)%bc_type), ' I=',bound(i)%nbnodes, ' F=POINT'

  bnodes : do j = 1, bound(i)%nbnodes

  ibn = bound(i)%bnode(j)

    write(1,*) node(ibn)%x, node(ibn)%y    , &
               (node(ibn)%u(k),k=1,3)      , &
               (node(ibn)%uexact(k) ,k=1,3)

  end do bnodes

 end do bc_loop

!--------------------------------------------------------------------------------
 close(1)
 end subroutine write_tecplot_file_b
!********************************************************************************


!********************************************************************************
!********************************************************************************
!********************************************************************************
!********************************************************************************
!********************************************************************************
!* Below, you find the following subroutines associated with LSQ gradients:
!*
!*  - compute_lsq_coeff_nc : Compute and store LSQ gradient coefficients at node
!*  - check_lsq_coeff_nc   : Check the computed LSQ coefficients
!*  - compute_gradient_nc  : Compute gradients at nodes
!*
!*  - lsq_gradients_nc     : Compute gradients (loop over neighbros) at a node
!*  - lsq_gradients2_nc    : Compute gradients (including neighbors of neighbors) at a node
!*  - lsq01_2x2_coeff_nc   : Compute linear LSQ coefficients at a node
!*  - lsq02_5x5_coeff2_nc  : Compute quadratic LSQ coefficients at all nodes
!*  - lsq_weight           : Compute LSQ weights
!*  - gewp_solve           : Gauss elimination to ivert a matrix
!
!********************************************************************************
!********************************************************************************

!********************************************************************************
!* This subroutine computes the coefficients for linear and quadratic LSQ
!* gradeints. 
!*
!* Note: Quadratic LSQ method is implemented in two steps as described in
!*       Nishikawa, JCP2014v273pp287-309 for details, which is available at 
!* http://www.hiroakinishikawa.com/My_papers/nishikawa_jcp2014v273pp287-309_preprint.pdf.
!*       This two-step method is useful in a paralell environment: it takes into
!*       account neighbors of neighbors without accessing neighbors of neighbors.
!*       So, it can be implemented only with edge-connected-neighbor information.
!*       In other words, each step is compact.
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
!********************************************************************************
 subroutine compute_lsq_coeff_nc

 use edu2d_my_main_data , only : nnodes, node
 use edu2d_my_allocation, only : my_alloc_p2_ptr, my_alloc_p2_matrix_ptr

 integer :: i, in, ell, ii, k

  write(*,*)
  write(*,*) "Constructing LSQ coefficients..."

! 1. Coefficients for the linear LSQ gradients

  write(*,*) "---(1) Constructing Linear LSQ coefficients..."

  nodes : do i = 1, nnodes

     call my_alloc_p2_ptr(node(i)%lsq2x2_cx,node(i)%nnghbrs)
     call my_alloc_p2_ptr(node(i)%lsq2x2_cy,node(i)%nnghbrs)
     call lsq01_2x2_coeff_nc(i)

  end do nodes

! 2. Coefficients for the quadratic LSQ gradients (two-step method)

  write(*,*) "---(2) Constructing Quadratic LSQ coefficients..."

  do i = 1, nnodes

        ii = 0 
     nghbr : do k = 1, node(i)%nnghbrs
        in = node(i)%nghbr(k)
      nghbr_nghbr : do ell = 1, node(in)%nnghbrs
        ii = ii + 1
      end do nghbr_nghbr
     end do nghbr

     call my_alloc_p2_ptr(node(i)%lsq5x5_cx, ii)
     call my_alloc_p2_ptr(node(i)%lsq5x5_cy, ii)
     call my_alloc_p2_ptr(node(i)%dx,node(i)%nnghbrs)
     call my_alloc_p2_ptr(node(i)%dy,node(i)%nnghbrs)
     call my_alloc_p2_matrix_ptr(node(i)%dw, 3,node(i)%nnghbrs)

  end do

     call lsq02_5x5_coeff2_nc

 end subroutine compute_lsq_coeff_nc

!********************************************************************************
!* This subroutine verifies the implementation of LSQ gradients.
!*
!* 1. Check if the linear LSQ gradients are exact for linear functions.
!* 2. Check if the quadratic LSQ gradients are exact for quadratic functions.
!*
!* Note: Here, we use only the first component of u=(u1,u2,u3), i.e., ivar=1.
!*
!********************************************************************************
 subroutine check_lsq_coeff_nc

 use edu2d_constants   , only : p2, one, two
 use edu2d_my_main_data, only : nnodes, node

 integer       :: i, ix, iy, ivar
 character(80) :: grad_type_temp
 real(p2)      :: error_max_ux, error_max_uy, x, y
 real(p2)      :: x_max_ux, y_max_ux, x_max_uy, y_max_uy, ux, uxe, uy, uye
 real(p2)      :: a0, a1, a2, a3, a4, a5

  ix = 1
  iy = 2

! We only use u(1) for this test.
  ivar = 1
 
!---------------------------------------------------------------------
! 1. Check linear LSQ gradients
!---------------------------------------------------------------------
  write(*,*)
  write(*,*) "---------------------------------------------------------"
  write(*,*) "---------------------------------------------------------"
  write(*,*) "- Checking Linear LSQ gradients..."

!  (1). Store a linear function in u(ivar) = x + 2*y.
!       So the exact gradient is grad(u(ivar)) = (1,2).

   write(*,*) "- Storing a linear function values..."
   do i = 1, nnodes
    x = node(i)%x
    y = node(i)%y
    node(i)%u(ivar) = one*x + two*y
   end do

!  (2). Compute the gradient by linear LSQ

   write(*,*) "- Computing linear LSQ gradients.."
   grad_type_temp = 'linear'
   call compute_gradient_nc(ivar,grad_type_temp)

!  (3). Compute the relative errors (L_infinity)

   write(*,*) "- Computing the relative errors (L_infinity).."
   error_max_ux = -one
   error_max_uy = -one
   do i = 1, nnodes
    error_max_ux = max( abs( node(i)%gradu(ivar,ix) - one )/one, error_max_ux )
    error_max_uy = max( abs( node(i)%gradu(ivar,iy) - two )/two, error_max_uy )
   end do

  write(*,*) " Max relative error in ux = ", error_max_ux
  write(*,*) " Max relative error in uy = ", error_max_uy
  write(*,*) "---------------------------------------------------------"
  write(*,*) "---------------------------------------------------------"


!---------------------------------------------------------------------
! 2. Check quadratic LSQ gradients
!---------------------------------------------------------------------
  write(*,*)
  write(*,*) "---------------------------------------------------------"
  write(*,*) "---------------------------------------------------------"
  write(*,*) "- Checking Quadratic LSQ gradients..."

!  (1). Store a quadratic function in w(ivar) = a0 + a1*x + a2*y + a3*x**2 + a4*x*y + a5*y**2
!       So the exact gradient is grad(w(ivar)) = (a1+2*a3*x+a4*y, a2+2*a5*y+a4*x)

   a0 =    12.191_p2
   a1 =     1.000_p2
   a2 = -   1.970_p2
   a3 =   280.400_p2
   a4 = -2129.710_p2
   a5 =   170.999_p2

   write(*,*) "- Storing a quadratic function values..."
   do i = 1, nnodes
    x = node(i)%x
    y = node(i)%y
    node(i)%u(ivar) = a0 + a1*x + a2*y + a3*x**2 + a4*x*y + a5*y**2
   end do

!  (2). Compute the gradient by linear LSQ

   write(*,*) "- Computing quadratic LSQ gradients.."
   grad_type_temp = 'quadratic2'
   call compute_gradient_nc(ivar,grad_type_temp)

!  (3). Compute the relative errors (L_infinity)

   write(*,*) "- Computing the relative errors (L_infinity).."
   error_max_ux = -one
   error_max_uy = -one
   do i = 1, nnodes
    x = node(i)%x
    y = node(i)%y

    if ( abs( node(i)%gradu(ivar,ix) - (a1+2.0_p2*a3*x+a4*y) )/(a1+2.0_p2*a3*x+a4*y) >  error_max_ux ) then
      ux  = node(i)%gradu(ivar,ix)
      uxe = a1+2.0_p2*a3*x+a4*y
      error_max_ux = abs( ux - uxe )/uxe
      x_max_ux = x
      y_max_ux = y
    endif

    if ( abs( node(i)%gradu(ivar,iy) - (a2+2.0_p2*a5*y+a4*x) )/(a2+2.0_p2*a5*y+a4*x) >  error_max_uy ) then
      uy  = node(i)%gradu(ivar,iy)
      uye = a2+2.0_p2*a5*y+a4*x
      error_max_uy = abs( uy - uye )/uye
      x_max_uy = x
      y_max_uy = y
    endif

   end do

  write(*,'(a,es20.3,a,2es12.5)') " Max relative error in ux = ", error_max_ux, " at (x,y) = ", x_max_ux, y_max_ux
  write(*,'(a,es20.10,a,es20.10)')  "   At this location, LSQ ux = ", ux, ": Exact ux = ", uxe
  write(*,'(a,es20.3,a,2es12.5)') " Max relative error in uy = ", error_max_uy, " at (x,y) = ", x_max_uy, y_max_uy
  write(*,'(a,es20.10,a,es20.10)')  "   At this location, LSQ uy = ", uy, ": Exact uy = ", uye
  write(*,*) "---------------------------------------------------------"
  write(*,*) "---------------------------------------------------------"
  write(*,*)

 end subroutine check_lsq_coeff_nc

!********************************************************************************
!* This subroutine computes gradients at nodes for the variable u(ivar),
!* where ivar = 1,2,3, ..., or nq.
!*
!* ------------------------------------------------------------------------------
!*  Input: node(:)%u(ivar)
!*
!* Output: node(i)%gradu(ivar,1:2) = ( du(ivar)/dx, du(ivar)/dy )
!* ------------------------------------------------------------------------------
!********************************************************************************
 subroutine compute_gradient_nc(ivar,grad_type)

 use edu2d_my_main_data, only : node, nnodes

 integer, intent(in) :: ivar

 integer       :: i, k, in
 character(80) :: grad_type

  if (trim(grad_type) == "none") return

!-------------------------------------------------
!  Two-step quadratic LSQ 5x5 system
!  Note: See Nishikawa, JCP2014v273pp287-309 for details, which is available at 
!        http://www.hiroakinishikawa.com/My_papers/nishikawa_jcp2014v273pp287-309_preprint.pdf.

   if (trim(grad_type) == "quadratic2") then

!  Perform Step 1 as below (before actually compute the gradient).

      do i = 1, nnodes

       nghbr0 : do k = 1, node(i)%nnghbrs
                   in      = node(i )%nghbr(k)
        node(i)%dx(k)      = node(in)%x       - node(i)%x
        node(i)%dy(k)      = node(in)%y       - node(i)%y
        node(i)%dw(ivar,k) = node(in)%u(ivar) - node(i)%u(ivar)
       end do nghbr0
      end do

   endif
!-------------------------------------------------

!------------------------------------------------------------
!------------------------------------------------------------
!-- Compute LSQ Gradients at all nodes.
!------------------------------------------------------------
!------------------------------------------------------------

  nodes : do i = 1, nnodes

  !-------------------------------------------------
  ! Linear LSQ 2x2 system
    if (trim(grad_type) == "linear") then

       call lsq_gradients_nc(i,ivar)

  !-------------------------------------------------
  ! Two-step quadratic LSQ 5x5 system
  !  Note: See Nishikawa, JCP2014v273pp287-309 for details, which is available at 
  !        http://www.hiroakinishikawa.com/My_papers/nishikawa_jcp2014v273pp287-309_preprint.pdf.
    elseif (trim(grad_type) == "quadratic2") then

      call lsq_gradients2_nc(i,ivar)

  !-------------------------------------------------
    else

     write(*,*) " Invalid input value -> ", trim(grad_type)
     stop

    endif
  !-------------------------------------------------

   end do nodes

 end subroutine compute_gradient_nc


!********************************************************************************
!* Compute the gradient, (ux,uy), for the variable u by Linear LSQ.
!*
!* ------------------------------------------------------------------------------
!*  Input:            inode = Node number at which the gradient is computed.
!*                     ivar =   Variable for which the gradient is computed.
!*          node(:)%u(ivar) = Solution at nearby nodes.
!*
!* Output:  node(inode)%gradu = gradient of the requested variable
!* ------------------------------------------------------------------------------
!*
!********************************************************************************
 subroutine lsq_gradients_nc(inode,ivar)

 use edu2d_my_main_data           , only : node
 use edu2d_constants              , only : p2, zero

 implicit none

 integer, intent(in) :: inode, ivar

!Local variables
 integer  :: in, inghbr
 integer  :: ix, iy
 real(p2) :: da, ax, ay

  ix = 1 
  iy = 2
  ax = zero
  ay = zero

!   Loop over neighbors

     do in = 1, node(inode)%nnghbrs
       inghbr = node(inode)%nghbr(in)

          da = node(inghbr)%u(ivar) - node(inode)%u(ivar)
 
      ax = ax + node(inode)%lsq2x2_cx(in)*da
      ay = ay + node(inode)%lsq2x2_cy(in)*da

     end do

      node(inode)%gradu(ivar,ix) = ax  !<-- du(ivar)/dx
      node(inode)%gradu(ivar,iy) = ay  !<-- du(ivar)/dy

 end subroutine lsq_gradients_nc
!--------------------------------------------------------------------------------


!********************************************************************************
!* Compute the gradient, (ux,uy), for the variable u by Quadratic LSQ.
!*
!* ------------------------------------------------------------------------------
!*  Input:            inode = Node number at which the gradient is computed.
!*                     ivar =   Variable for which the gradient is computed.
!*          node(:)%u(ivar) = Solution at nearby nodes.
!*
!* Output:  node(inode)%gradu = gradient of the requested variable
!* ------------------------------------------------------------------------------
!*
!********************************************************************************
 subroutine lsq_gradients2_nc(inode,ivar)

 use edu2d_my_main_data, only : node
 use edu2d_constants   , only : p2, zero

 implicit none

 integer, intent(in) :: inode, ivar

!Local variables
 integer  :: in
 integer  :: ix, iy, ii, ell, k
 real(p2) :: da, ax, ay

   ix = 1 
   iy = 2
   ax = zero
   ay = zero

!   Loop over neighbors

       ii = 0

     nghbr : do k = 1, node(inode)%nnghbrs
              in = node(inode)%nghbr(k)

      nghbr_nghbr : do ell = 1, node(in)%nnghbrs

       da = node(in)%u(ivar) - node(inode)%u(ivar) + node(in)%dw(ivar,ell)

       if ( node(in)%nghbr(ell) == inode ) then
        da = node(in)%u(ivar) - node(inode)%u(ivar)
       endif

       ii = ii + 1

       ax = ax + node(inode)%lsq5x5_cx(ii)*da
       ay = ay + node(inode)%lsq5x5_cy(ii)*da

      end do nghbr_nghbr

     end do nghbr

      node(inode)%gradu(ivar,ix) = ax  !<-- du(ivar)/dx
      node(inode)%gradu(ivar,iy) = ay  !<-- du(ivar)/dy

 end subroutine lsq_gradients2_nc
!--------------------------------------------------------------------------------



!********************************************************************************
!* --- LSQ Coefficients for 2x2 Linear Least-Squares Gradient Reconstruction ---
!*
!* ------------------------------------------------------------------------------
!*  Input:  inode = node number at which the gradient is computed.
!*
!* Output:  node(inode)%lsq2x2_cx(:)
!*          node(inode)%lsq2x2_cx(:)
!* ------------------------------------------------------------------------------
!*
!********************************************************************************
 subroutine lsq01_2x2_coeff_nc(inode)

 use edu2d_my_main_data           , only : node
 use edu2d_constants              , only : p2, zero

 implicit none

 integer, intent(in) :: inode
!Local variables
 real(p2) :: a(2,2), dx, dy, det, w2, w2dvar
 integer  :: k, inghbr, ix=1,iy=2
 real(p2), dimension(2,2) :: local_lsq_inverse

   a = zero

!  Loop over the neighbor nodes.
   do k = 1, node(inode)%nnghbrs
    inghbr = node(inode)%nghbr(k)

      dx = node(inghbr)%x - node(inode)%x
      dy = node(inghbr)%y - node(inode)%y

      w2 = lsq_weight(dx, dy)**2

      a(1,1) = a(1,1) + w2 * dx*dx
      a(1,2) = a(1,2) + w2 * dx*dy

      a(2,1) = a(2,1) + w2 * dx*dy
      a(2,2) = a(2,2) + w2 * dy*dy

   end do

    det = a(1,1)*a(2,2) - a(1,2)*a(2,1)
    if (abs(det) < 1.0e-14) write(*,*) " Singular: LSQ det = ", det, " i=",inode

! OK, invert and store the inverse matrix:

     local_lsq_inverse(1,1) =  a(2,2)/det
     local_lsq_inverse(1,2) = -a(2,1)/det
     local_lsq_inverse(2,1) = -a(1,2)/det
     local_lsq_inverse(2,2) =  a(1,1)/det

!  Now compute the coefficients for neighbors.

     nghbr : do k = 1, node(inode)%nnghbrs
       inghbr = node(inode)%nghbr(k)

        dx = node(inghbr)%x - node(inode)%x
        dy = node(inghbr)%y - node(inode)%y

      w2dvar = lsq_weight(dx, dy)**2

      node(inode)%lsq2x2_cx(k)  = local_lsq_inverse(ix,1)*w2dvar*dx &
                                + local_lsq_inverse(ix,2)*w2dvar*dy

      node(inode)%lsq2x2_cy(k)  = local_lsq_inverse(iy,1)*w2dvar*dx &
                                + local_lsq_inverse(iy,2)*w2dvar*dy

     end do nghbr

 end subroutine lsq01_2x2_coeff_nc
!********************************************************************************
!*
!********************************************************************************


!********************************************************************************
!* --- LSQ Coefficients for 5x5 Quadratic Least-Squares Gradient Reconstruction ---
!*
!* Note: See Nishikawa, JCP2014v273pp287-309 for details, which is available at 
!*
!* http://www.hiroakinishikawa.com/My_papers/nishikawa_jcp2014v273pp287-309_preprint.pdf.
!*
!* ------------------------------------------------------------------------------
!*  Input:
!*
!* Output:  node(:)%lsq5x5_cx(ii)
!*          node(:)%lsq5x5_cx(ii)
!*
!* Note: This subroutine computes the LSQ coefficeints at all nodes.
!* ------------------------------------------------------------------------------
!*
!********************************************************************************
 subroutine lsq02_5x5_coeff2_nc

 use edu2d_my_main_data           , only : node, nnodes
 use edu2d_constants              , only : p2, zero, half

 implicit none

!Local variables
 real(p2) :: a(5,5), ainv(5,5), dx, dy
 real(p2) :: dummy1(5), dummy2(5)
 real(p2) :: w2
 integer  :: istat, ix=1, iy=2

 integer :: i, k, ell, in, ii

! Step 1

  node1 : do i = 1, nnodes
   nghbr : do k = 1, node(i)%nnghbrs

               in   = node(i)%nghbr(k)
    node(i)%dx(k)   = node(in)%x - node(i)%x
    node(i)%dy(k)   = node(in)%y - node(i)%y

   end do nghbr
  end do node1

! Step 2

  node2 : do i = 1, nnodes

     a = zero

!  Get dx, dy, and dw

   nghbr2 : do k = 1, node(i)%nnghbrs

              in = node(i)%nghbr(k)

    nghbr_nghbr : do ell = 1, node(in)%nnghbrs

     dx = node(in)%x - node(i)%x + node(in)%dx(ell)
     dy = node(in)%y - node(i)%y + node(in)%dy(ell)

     if ( node(in)%nghbr(ell) == i ) then

      dx = node(in)%x - node(i)%x
      dy = node(in)%y - node(i)%y

      if ( abs(dx) + abs(dy) < 1.0e-13_p2 ) then
       write(*,*) " Zero distance found at lsq02_5x5_coeff2_nc..."
       write(*,*) "    dx = ", dx
       write(*,*) "    dy = ", dy
       write(*,*) "- Centered node = ", i
       write(*,*) "          (x,y) = ", node(in)%x, node(in)%y
       write(*,*) "- Neighbor node = ", in
       write(*,*) "          (x,y) = ", node(in)%x, node(in)%y
       stop
      endif

     endif


        w2 = lsq_weight(dx, dy)**2

      a(1,1) = a(1,1) + w2 * dx         *dx
      a(1,2) = a(1,2) + w2 * dx         *dy
      a(1,3) = a(1,3) + w2 * dx         *dx*dx * half
      a(1,4) = a(1,4) + w2 * dx         *dx*dy
      a(1,5) = a(1,5) + w2 * dx         *dy*dy * half

!     a(2,1) = a(2,1) + w2 * dy         *dx
      a(2,2) = a(2,2) + w2 * dy         *dy
      a(2,3) = a(2,3) + w2 * dy         *dx*dx * half
      a(2,4) = a(2,4) + w2 * dy         *dx*dy
      a(2,5) = a(2,5) + w2 * dy         *dy*dy * half

!     a(3,1) = a(3,1) + w2 * half*dx*dx *dx
!     a(3,2) = a(3,2) + w2 * half*dx*dx *dy
      a(3,3) = a(3,3) + w2 * half*dx*dx *dx*dx * half
      a(3,4) = a(3,4) + w2 * half*dx*dx *dx*dy
      a(3,5) = a(3,5) + w2 * half*dx*dx *dy*dy * half

!     a(4,1) = a(4,1) + w2 *      dx*dy *dx
!     a(4,2) = a(4,2) + w2 *      dx*dy *dy
!     a(4,3) = a(4,3) + w2 *      dx*dy *dx*dx * half
      a(4,4) = a(4,4) + w2 *      dx*dy *dx*dy
      a(4,5) = a(4,5) + w2 *      dx*dy *dy*dy * half

!     a(5,1) = a(5,1) + w2 * half*dy*dy *dx
!     a(5,2) = a(5,2) + w2 * half*dy*dy *dy
!     a(5,3) = a(5,3) + w2 * half*dy*dy *dx*dx * half
!     a(5,4) = a(5,4) + w2 * half*dy*dy *dx*dy
      a(5,5) = a(5,5) + w2 * half*dy*dy *dy*dy * half

    end do nghbr_nghbr

   end do nghbr2

!   Fill symmetric part

      a(2,1) = a(1,2);
      a(3,1) = a(1,3);  a(3,2) = a(2,3);
      a(4,1) = a(1,4);  a(4,2) = a(2,4); a(4,3) = a(3,4);
      a(5,1) = a(1,5);  a(5,2) = a(2,5); a(5,3) = a(3,5); a(5,4) = a(4,5);

!   Invert the matrix

     dummy1 = zero
     dummy2 = zero
     call gewp_solve(a,dummy1,dummy2,ainv,istat, 5);

     if (istat/=0) write(*,*) "Problem in solving the linear system!: Quadratic_LSJ_Matrix"

!  Now compute the coefficients for neighbors.

      ii = 0

     nghbr3 : do k = 1, node(i)%nnghbrs
                in = node(i)%nghbr(k)

      nghbr_nghbr2 : do ell = 1, node(in)%nnghbrs

       dx = node(in)%x - node(i)%x + node(in)%dx(ell)
       dy = node(in)%y - node(i)%y + node(in)%dy(ell)

       if ( node(in)%nghbr(ell) == i ) then
        dx = node(in)%x - node(i)%x
        dy = node(in)%y - node(i)%y
       endif

       ii = ii + 1
       
       w2 = lsq_weight(dx, dy)**2

 !  Multiply the inverse LSQ matrix to get the coefficients: cx(:) and cy(:):

      node(i)%lsq5x5_cx(ii)  =  ainv(ix,1)*w2*dx             &
                              + ainv(ix,2)*w2*dy             &
                              + ainv(ix,3)*w2*dx*dx * half   &
                              + ainv(ix,4)*w2*dx*dy          &
                              + ainv(ix,5)*w2*dy*dy * half

      node(i)%lsq5x5_cy(ii)  =  ainv(iy,1)*w2*dx             &
                              + ainv(iy,2)*w2*dy             &
                              + ainv(iy,3)*w2*dx*dx * half   &
                              + ainv(iy,4)*w2*dx*dy          &
                              + ainv(iy,5)*w2*dy*dy * half
      end do nghbr_nghbr2

     end do nghbr3

  end do node2

 end subroutine lsq02_5x5_coeff2_nc
!********************************************************************************
!*
!********************************************************************************


!****************************************************************************
!* Compute the LSQ weight
!*
!* Note: The weight computed here is the square of the actual LSQ weight.
!*****************************************************************************
 function lsq_weight(dx, dy)

 use edu2d_constants   , only : p2, one
 use edu2d_my_main_data, only : gradient_weight, gradient_weight_p

 implicit none

!Input
 real(p2), intent(in) :: dx, dy
!Output
 real(p2)             :: lsq_weight
!Local
 real(p2)             :: distance

  if     (trim(gradient_weight) == "none"            ) then

        lsq_weight = one

  elseif (trim(gradient_weight) == "inverse_distance") then

          distance = sqrt(dx*dx + dy*dy)
        lsq_weight = one / distance**gradient_weight_p

  endif

 end function lsq_weight

!****************************************************************************
!* ------------------ GAUSS ELIMINATION WITH PIVOTING ---------------------
!*
!*  This computes the inverse of an (Nm)x(Nm) matrix "ai".
!*
!*  IN :       ai = an (Nm)x(Nm) matrix whoise inverse is sought.
!*             bi = right hand side of a linear system: ai*x=bi.
!*             nm = the size of the matrix "ai"
!*
!* OUT :  inverse = the inverse of "ai".
!*            sol = solution to the linear system, ai*x=bi
!*       idetstat = 0 -> inverse successfully computed
!*                  1 -> THE INVERSE DOES NOT EXIST (det=0).
!*                  2 -> No unique solutions exist.
!*
!* Katate Masatsuka, April 2015. http://www.cfdbooks.com
!*****************************************************************************
 subroutine gewp_solve(ai,bi,sol,inverse,idetstat,nm)

  use edu2d_constants   , only : p2, zero, one

  implicit none

! Input
  real(p2), intent( in) :: ai(:,:),bi(:)
  integer , intent( in) :: nm

! Output
  real(p2), intent(out) :: sol(:),inverse(nm,nm)
  integer , intent(out) :: idetstat

! Local variables
  real(p2) :: a(nm,nm+1),x(nm)
  integer  :: i,j,k,pp,nrow(nm),m

 do m=1,nm
!*****************************************************************************
!*****************************************************************************
       do j=1,nm
        do i=1,nm
          a(i,j) = ai(i,j)
        end do
       end do
       do k=1,nm
          a(k,nm+1)=zero; nrow(k)=k
       end do
          a(m,nm+1)=one
!*****************************************************************************
       do j=1,nm-1
!*****************************************************************************
!* find smallest pp for a(pp,j) is maximum in jth column.
!***************************************************************************** 
      call findmax(nm,j,pp,a,nrow)
!*****************************************************************************
!* if a(nrow(p),j) is zero, there's no unique solutions      
!*****************************************************************************
      if ( abs(a(nrow(pp),j) - zero) < 1.0e-15 ) then
       write(6,*) 'the inverse does not exist.'
        idetstat = 1
        return
      else
      endif
!*****************************************************************************
!* if the max is not a diagonal element, switch those rows       
!*****************************************************************************
      if (nrow(pp) .ne. nrow(j)) then
      call switch(nm,j,pp,nrow)
      else
      endif  
!*****************************************************************************
!* eliminate all the entries below the diagonal one
!***************************************************************************** 
      call eliminate_below(nm,j,a,nrow)

      end do
!*****************************************************************************
!* check if a(nrow(n),n)=0.0 .
!*****************************************************************************
      if ( abs(a(nrow(nm),nm) - zero) < 1.0e-15 ) then
        write(6,*) 'no unique solution exists!';  idetstat = 2
        return 
      else
      endif
!*****************************************************************************
!* backsubstitution!
!*****************************************************************************
      call backsub(nm,x,a,nrow)
!*****************************************************************************
!* store the solutions, you know they are inverse(i,m) i=1...
!*****************************************************************************
      do i=1,nm
         inverse(i,m)=x(i)
      end do
!*****************************************************************************
 end do
!*****************************************************************************
!* solve
!*****************************************************************************
    do i=1,nm; sol(i)=zero;
     do j=1,nm
       sol(i) = sol(i) + inverse(i,j)*bi(j)
     end do
    end do

    idetstat = 0;
    return

 end subroutine gewp_solve


!Four subroutines below are used in gewp above.


!*****************************************************************************
!* Find maximum element in jth column 
!***************************************************************************** 
 subroutine findmax(nm,j,pp,a,nrow)

  use edu2d_constants   , only : p2

  implicit none

! Input
  integer , intent( in) :: nm
  real(p2), intent( in) :: a(nm,nm+1)
  integer , intent( in) :: j,nrow(nm)

! Output
  integer , intent(out) :: pp

! Local variables
  real(p2) :: max
  integer :: i

            max=abs(a(nrow(j),j)); pp=j
           do i=j+1,nm
             if (max < abs(a(nrow(i),j))) then
                  pp=i; max=abs(a(nrow(i),j))
             endif
           end do

  return

 end subroutine findmax

!*****************************************************************************
!* Switch rows       
!*****************************************************************************
 subroutine switch(nm,j,pp,nrow)

 implicit none

! Input
  integer, intent(   in) :: nm,j,pp

! Output
  integer, intent(inout) :: nrow(nm)

! Local
  integer :: ncopy

      if (nrow(pp).ne.nrow(j)) then
         ncopy=nrow(j)
         nrow(j)=nrow(pp)
         nrow(pp)=ncopy
      endif  

  return

 end subroutine switch

!*****************************************************************************
!* Eliminate all the entries below the diagonal one
!* (give me j, the column you are working on now)
!***************************************************************************** 
 subroutine eliminate_below(nm,j,a,nrow)

  use edu2d_constants   , only : p2, zero

  implicit none
  
! Input
  integer , intent(   in) :: nm
  integer , intent(   in) :: j,nrow(nm)

! Output
  real(p2), intent(inout) :: a(nm,nm+1)

! Local
  real(p2) :: m
  integer  :: k,i

      do i=j+1,nm
        m=a(nrow(i),j)/a(nrow(j),j)
        a(nrow(i),j)=zero
          do k=j+1,nm+1
            a(nrow(i),k)=a(nrow(i),k)-m*a(nrow(j),k)
          end do
      end do

  return

 end subroutine eliminate_below

!*****************************************************************************
!* Backsubstitution!
!*****************************************************************************
 subroutine backsub(nm,x,a,nrow)

  use edu2d_constants   , only : p2, zero

  implicit none

! Input
  integer , intent( in) :: nm
  real(p2), intent( in) :: a(nm,nm+1)
  integer , intent( in) :: nrow(nm)

! Output
  real(p2), intent(out) :: x(nm)

! Local
  real(p2) :: sum
  integer :: i,k

      x(nm)=a(nrow(nm),nm+1)/a(nrow(nm),nm)
      do i=nm-1,1,-1
         sum=zero
           do k=i+1,nm
              sum=sum+a(nrow(i),k)*x(k)
           end do
      x(i)=(a(nrow(i),nm+1)-sum)/a(nrow(i),i)
      end do

  return

 end subroutine backsub
!*********************************************************************


 end module edu2d_template_nc

