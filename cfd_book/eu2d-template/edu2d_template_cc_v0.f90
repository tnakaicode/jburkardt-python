module edu2d_template_cc

 private

 public :: main_cc

 contains

!********************************************************************************
! Educationally-Designed Unstructured 2D (EDU2D) Code
!
! This is a main template for a cell-centered (CC) schemes.
!
! A grid has been loaded, and necessary data have been constructed before
! this subroutine gets called. It has been done in edu2d_main.f90, 
! which is the main driver code and call this subroutine.
!
!
! Here, we do the following:
!
!  1. Construct LSQ gradient coefficients (linear) at all cells.
!  2. Verify the LSQ coefficients (exact for a linear function)
!  3. Set some initial solution and exact solutions.
!  4. Compute some residual and update the solution: A dummy solver as an example.
!     NOTE: This is just an example, by which you get an idea about how to implement
!           your own solver, hopefully.
!  5. Write out a tecplot file for viewing the solution and the grid.
!
!
!        written by Dr. Katate Masatsuka (info[at]cfdbooks.com),
!
! the author of useful CFD books, "I do like CFD" (http://www.cfdbooks.com).
!
! This is Version 0 (July 2015).
! This F90 code is written and made available for an educational purpose.
! This file may be updated in futu
!
!********************************************************************************
 subroutine main_cc(datafile_cc_tec)

 use edu2d_constants   , only : p2, zero, half
 use edu2d_my_main_data, only : nelms, elm, nfaces, face, nbound, bound, gradient_type

!Output data file
 character(80) :: datafile_cc_tec    !Tecplot file for viewing the result: Entire domain

!-- Variables used for a dummy solver ----------------------------------------
 integer  :: iteration, max_iteration, elm1, elm2, i, j, ix=1, iy=2
 real(p2) :: mag_n12, mag_e12, nx,ny, ex,ey, dt
 real(p2) :: uL(3),uR(3), num_flux(3)
!-----------------------------------------------------------------------------

! Compute LSQ gradient coefficients: linear LSQ and quadratic LSQ
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Computing LSQ coefficients (at cells)... "
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  call compute_lsq_coeff_cc

! Check LSQ gradient coefficients: linear LSQ and quadratic LSQ
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Checking the LSQ coefficients... "
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  call check_lsq_coeff_cc

! Store the initial and exact solutions.
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Setting initial and exact solutions... "
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  call initial_and_exact_solutions_cc


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
  write(*,*) ">>> CC Solver begins here....."
  write(*,*)

  max_iteration = 3
  iteration_loop : do iteration = 1, max_iteration

! 1. Computation of residual

   !Initialize the residul array.
   elms : do i = 1, nelms
    elm(i)%res = zero
   end do elms

   !Compute the gradients at elms
    call compute_gradient_cc(1,gradient_type) ! gradients of u(1)
    call compute_gradient_cc(2,gradient_type) ! gradients of u(2)
    call compute_gradient_cc(3,gradient_type) ! gradients of u(3)

   ! Flux computations through internal faces.
   !               
   !   -------------------------
   !   |           |           |
   !   |           |           |
   !   |           |(nx,ny)    |
   !   |    o------|----->o    |
   !   |           |           |
   !   |   elm1    |   elm2    |
   !   |           |           |    o: element centroid
   !   -------------------------
   ! Directed area vector is the face normal vector.
   !
   !
   !(1)Compute numerical flux at interior edges and accumulate at elms.
   faces : do i = 1, nfaces

       elm1 = face(i)%e1      ! Left element of the face
       elm2 = face(i)%e2      ! Right element of the face
    mag_n12 = face(i)%da      ! Magnitude of the directed area vector
         nx = face(i)%dav(ix) ! This is the directed area vector (unit vector)
         ny = face(i)%dav(iy)
 
    !Vector connecting the data points (cell centers)
         ex = elm(elm2)%x - elm(elm1)%x
         ey = elm(elm2)%y - elm(elm1)%y
    mag_e12 = sqrt( ex*ex + ey*ey )
         ex = ex/mag_e12
         ey = ey/mag_e12

     !Linear extrapolation of the solution from elm1 and elm2 to the midpoint.
     !Note: Not necessarily at the face on irregular meshes, but that's OK for 2nd-order accuracy.
     !      Or you can do it precisely by extrapolating exactly to the face midpoint from each cell.
     !      See http://www.hiroakinishikawa.com/My_papers/nishikawa_AIAA-2010-5093.pdf for details.
     uL = elm(elm1)%u + half*( elm(elm1)%gradu(:,ix)*ex + elm(elm1)%gradu(:,iy)*ey )*mag_e12
     uR = elm(elm2)%u - half*( elm(elm2)%gradu(:,ix)*ex + elm(elm2)%gradu(:,iy)*ey )*mag_e12

     !A kind of central flux defined at the midpoint.
     num_flux = half*(uL+uR)

     elm(elm1)%res = elm(elm1)%res  + num_flux *mag_n12 ! Add numerical flux to elm 1
     elm(elm2)%res = elm(elm2)%res  - num_flux *mag_n12 ! Subtract it from elm 2

   end do faces

   !(2)Close the residual by boundary flux contributions.
   !   Note: We consider a weak boundary procedure here.
   !         Boundary condition is imposed in a ghost state, which is sent to
   !         a numerical flux to determine the flux through the boundary.
 
 
   bc_loop : do i = 1, nbound

    bfaces : do j = 1, bound(i)%nbfaces

         nx = bound(i)%bfnx(j)     !x-component of the unit face normal vector
         ny = bound(i)%bfny(j)     !y-component of the unit face normal vector
    mag_n12 = bound(i)%bfn(j)      !Length of the boundary face, j.
       elm1 = bound(i)%belm(j)     !Element adjacent to the boundary face

      !Left state (interior)
       uL = elm(elm1)%u
      !Right state (boundary condition)
       uR = elm(elm1)%uexact ! Boundary condition given by the exact solution.
      !Central flux as an example.
       num_flux = half*(uL+uR)*nx + half*(uL+uR)*ny
      !Add the boundary flux contribution to the residual
       elm(elm1)%res = elm(elm1)%res  + num_flux *mag_n12

    end do bfaces
   end do bc_loop

! For implicit solvers, a linear solver should be placed here.
! Not considered in this tempalte code.

! 2. Update solutions

   !Some kind of explicit update
    dt = zero !<- Let's keep it zero, here. This is a dummy solver, anyway...
   elms_update : do i = 1, nelms
    elm(i)%u = elm(i)%u + dt*elm(i)%res
   end do elms_update

  end do iteration_loop

!---------------------------------------------------------------------------
!---------------------------------------------------------------------------
!------------------------------- End of Solver -----------------------------
!---------------------------------------------------------------------------
!---------------------------------------------------------------------------
  write(*,*)
  write(*,*)
  write(*,*) ">>> CC Solver ends here....."
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

! So, at this point, numerical solutions have been computed by some method.
! It is time to write out the data.

! Write out the tecplot data file in the entire domain (Solutions at nodes)
! Note: This subroutine writes a tecplot file for plotting cell-averaged solutions.
!       You can also consider recovering solutions at nodes (e.g., by averaging),
!       and then plot them. If you do so, then you can use tecplot subroutines in
!       edu2d_template_main_nc_v0.f90 to write tecplot data files.
  write(*,*)
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  write(*,*) ">>> Writing a tecplot file for viewing the grid and the solution..."
  write(*,*) ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
  call write_tecplot_file(   datafile_cc_tec )
  write(*,*) " file name = ", datafile_cc_tec

!--------------------------------------------------------------------------------

  write(*,*)
  write(*,*) "Computation successfully completed (main_cc). Stop."
  write(*,*)
  write(*,*)

 end subroutine main_cc

!********************************************************************************
!* Set initial and exact solutions
!*
!* Exact solution here has no meaning as we don't know what equation we solve.
!* So, just set u1=x, u2=2*y, u3=3*x: just random choice.
!*
!*  Written by Katate Masatsuka, http://www.cfdbooks.com
!********************************************************************************
 subroutine initial_and_exact_solutions_cc

 use edu2d_constants     , only : p2, one, two, three
 use edu2d_my_main_data  , only : nelms, elm

 implicit none

!Local variables
 integer  :: i
 real(p2) :: x, y

!----------------------------------------------------------
  elms : do i = 1, nelms

!  Cell center coordinates
   x = elm(i)%x
   y = elm(i)%y

!  Solution u1(x,y)
   elm(i)%uexact(1) = one*x

!  Solution u2(x,y)
   elm(i)%uexact(2) = two*y

!  Solution u3(x,y)
   elm(i)%uexact(3) = three*x

!  Set initial numerical solution to be exact
   elm(i)%u = elm(i)%uexact

  end do elms
!----------------------------------------------------------

 end subroutine initial_and_exact_solutions_cc
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
 write(1,*) 'zone nodes=',nnodes,',elements=',nelms, ',DATAPACKING=BLOCK', &
            ',ZONETYPE=FEQUADRILATERAL',',  VARLOCATION=([3-8]=CELLCENTERED)'

!--------------------------------------------------------------------------------
! X-coordinate (nodes)
 do i = 1, nnodes
  write(1,*) node(i)%x
 end do
! Y-coordinate (nodes)
 do i = 1, nnodes
  write(1,*) node(i)%y
 end do
! Solution (cells)
 do k = 1, 3
  do i = 1, nelms
   write(1,*) elm(i)%u(k)
  end do
 end do
! Exact solution (cells)
 do k = 1, 3
  do i = 1, nelms
   write(1,*) elm(i)%uexact(k)
  end do
 end do
!--------------------------------------------------------------------------------
! Both elements in quad format:
 do i = 1, nelms

  if (elm(i)%nvtx == 3) then

   write(1,*) elm(i)%vtx(1), elm(i)%vtx(2), elm(i)%vtx(3), elm(i)%vtx(3)

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
!********************************************************************************
!********************************************************************************
!********************************************************************************
!********************************************************************************
!* Below, you find the following subroutines for LSQ gradients:
!*
!*  - compute_lsq_coeff_cc : Compute and store LSQ gradient coefficients at a cell
!*  - check_lsq_coeff_cc   : Check the computed LSQ coefficients
!*  - compute_gradient_cc  : Compute gradients at a cell
!*
!*  - lsq_gradients_cc     : Compute gradients (loop over neighbros) at a cell
!*  - lsq01_2x2_coeff_nc   : Compute linear LSQ coefficients at a cell
!*  - lsq_weight           : Compute LSQ weights
!*
!********************************************************************************

!********************************************************************************
!* This subroutine computes the coefficients for linear LSQ gradeints at cells. 
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
!********************************************************************************
 subroutine compute_lsq_coeff_cc

 use edu2d_my_main_data , only : elm, nelms
 use edu2d_my_allocation, only : my_alloc_p2_ptr, my_alloc_p2_matrix_ptr

 integer :: i

  write(*,*)
  write(*,*) "Constructing LSQ coefficients (CC)..."

! 1. Coefficients for the linear LSQ gradients

  write(*,*) "---(1) Constructing Linear LSQ coefficients..."

  cells : do i = 1, nelms

     call my_alloc_p2_ptr(elm(i)%lsq2x2_cx,elm(i)%nvnghbrs)
     call my_alloc_p2_ptr(elm(i)%lsq2x2_cy,elm(i)%nvnghbrs)
     call lsq01_2x2_coeff_cc(i)

  end do cells

 end subroutine compute_lsq_coeff_cc

!********************************************************************************
!* This subroutine verifies the implementation of LSQ gradients.
!*
!* 1. Check if the linear LSQ gradients are exact for linear functions.
!*
!* Note: Here, we use only the first component of u=(u1,u2,u3), i.e., ivar=1.
!*
!********************************************************************************
 subroutine check_lsq_coeff_cc

 use edu2d_constants   , only : p2, one, two
 use edu2d_my_main_data, only : nelms, elm

 integer       :: i, ix, iy, ivar
 character(80) :: grad_type_temp
 real(p2)      :: error_max_ux, error_max_uy, x, y

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
   do i = 1, nelms
    x = elm(i)%x
    y = elm(i)%y
    elm(i)%u(ivar) = one*x + two*y
   end do

!  (2). Compute the gradient by linear LSQ

   write(*,*) "- Computing linear LSQ gradients.."
   grad_type_temp = 'linear'
   call compute_gradient_cc(ivar,grad_type_temp)

!  (3). Compute the relative errors (L_infinity)

   write(*,*) "- Computing the relative errors (L_infinity).."
   error_max_ux = -one
   error_max_uy = -one
   do i = 1, nelms
    error_max_ux = max( abs( elm(i)%gradu(ivar,ix) - one )/one, error_max_ux )
    error_max_uy = max( abs( elm(i)%gradu(ivar,iy) - two )/two, error_max_uy )
   end do

  write(*,*) " Max relative error in ux = ", error_max_ux
  write(*,*) " Max relative error in uy = ", error_max_uy
  write(*,*) "---------------------------------------------------------"
  write(*,*) "---------------------------------------------------------"

 end subroutine check_lsq_coeff_cc

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
 subroutine compute_gradient_cc(ivar,grad_type)

 use edu2d_my_main_data           , only : nelms

 integer, intent(in) :: ivar

 integer       :: i
 character(80) :: grad_type

  if (trim(grad_type) == "none") return

  if (trim(grad_type) == "quadratic2") then
   write(*,*) "!!!!!!!! grad_type = ", grad_type
   write(*,*) "!!!!!!!! Quadratic LSQ not available for CC...."
   write(*,*) "!!!!!!!! So, I change it to linear. Sorry......"
   grad_type = 'linear'
   write(*,*) "!!!!!!!! grad_type = ", grad_type
  endif

!------------------------------------------------------------
!------------------------------------------------------------
!-- Compute LSQ Gradients at all cells.
!------------------------------------------------------------
!------------------------------------------------------------

  cells : do i = 1, nelms

  !-------------------------------------------------
  ! Linear LSQ 2x2 system
    if (trim(grad_type) == "linear") then

       call lsq_gradients_cc(i,ivar)

  !-------------------------------------------------
    else

     write(*,*) " Invalid input value -> ", trim(grad_type)
     stop

    endif
  !-------------------------------------------------

   end do cells

 end subroutine compute_gradient_cc


!********************************************************************************
!* Compute the gradient, (ux,uy), for the variable u by Linear LSQ.
!*
!* ------------------------------------------------------------------------------
!*  Input:            inode = Node number at which the gradient is computed.
!*                     ivar =   Variable for which the gradient is computed.
!*           elm(:)%u(ivar) = Solution at nearby nodes.
!*
!* Output:  elm(ielm)%gradu = gradient of the requested variable
!* ------------------------------------------------------------------------------
!*
!********************************************************************************
 subroutine lsq_gradients_cc(ielm,ivar)

 use edu2d_my_main_data           , only : elm
 use edu2d_constants              , only : p2, zero

 implicit none

 integer, intent(in) :: ielm, ivar

!Local variables
 integer  :: in, inghbr
 integer  :: ix, iy
 real(p2) :: da, ax, ay

  ix = 1 
  iy = 2
  ax = zero
  ay = zero

!   Loop over vertex-neighbors:

     do in = 1, elm(ielm)%nvnghbrs
       inghbr = elm(ielm)%vnghbr(in)

          da = elm(inghbr)%u(ivar) - elm(ielm)%u(ivar)
 
      ax = ax + elm(ielm)%lsq2x2_cx(in)*da
      ay = ay + elm(ielm)%lsq2x2_cy(in)*da

     end do

      elm(ielm)%gradu(ivar,ix) = ax  !<-- du(ivar)/dx
      elm(ielm)%gradu(ivar,iy) = ay  !<-- du(ivar)/dy

 end subroutine lsq_gradients_cc
!--------------------------------------------------------------------------------


!********************************************************************************
!* --- LSQ Coefficients for 2x2 Linear Least-Squares Gradient Reconstruction ---
!*
!* ------------------------------------------------------------------------------
!*  Input:  icell = cell number at which the gradient is computed.
!*
!* Output:  cell(icell)%lsq2x2_cx(:)
!*          cell(icell)%lsq2x2_cx(:)
!* ------------------------------------------------------------------------------
!*
!********************************************************************************
 subroutine lsq01_2x2_coeff_cc(ielm)

 use edu2d_my_main_data           , only : elm
 use edu2d_constants              , only : p2, zero

 implicit none

 integer, intent(in) :: ielm
!Local variables
 real(p2) :: a(2,2), dx, dy, det, w2, w2dvar
 integer  :: k, inghbr, ix=1,iy=2
 real(p2), dimension(2,2) :: local_lsq_inverse

   a = zero

!  Loop over the neighbor elms.
   do k = 1, elm(ielm)%nvnghbrs
    inghbr = elm(ielm)%vnghbr(k)

      dx = elm(inghbr)%x - elm(ielm)%x
      dy = elm(inghbr)%y - elm(ielm)%y

      w2 = lsq_weight(dx, dy)**2

      a(1,1) = a(1,1) + w2 * dx*dx
      a(1,2) = a(1,2) + w2 * dx*dy

      a(2,1) = a(2,1) + w2 * dx*dy
      a(2,2) = a(2,2) + w2 * dy*dy

   end do

    det = a(1,1)*a(2,2) - a(1,2)*a(2,1)
    if (abs(det) < 1.0e-14) write(*,*) " Singular: LSQ det = ", det, " i=",ielm

! OK, invert and store the inverse matrix:

     local_lsq_inverse(1,1) =  a(2,2)/det
     local_lsq_inverse(1,2) = -a(2,1)/det
     local_lsq_inverse(2,1) = -a(1,2)/det
     local_lsq_inverse(2,2) =  a(1,1)/det

!  Now compute the coefficients for neighbors.

     nghbr : do k = 1, elm(ielm)%nvnghbrs
       inghbr = elm(ielm)%vnghbr(k)

        dx = elm(inghbr)%x - elm(ielm)%x
        dy = elm(inghbr)%y - elm(ielm)%y

      w2dvar = lsq_weight(dx, dy)**2

      elm(ielm)%lsq2x2_cx(k)  = local_lsq_inverse(ix,1)*w2dvar*dx &
                                + local_lsq_inverse(ix,2)*w2dvar*dy

      elm(ielm)%lsq2x2_cy(k)  = local_lsq_inverse(iy,1)*w2dvar*dx &
                                + local_lsq_inverse(iy,2)*w2dvar*dy

     end do nghbr

 end subroutine lsq01_2x2_coeff_cc
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

 end module edu2d_template_cc

