!********************************************************************************
!  Educationally-Designed Unstructured 2D (EDU2D) Code
!
!  ---------------- EDU2D-CCFV-Euler-EXPLCT
!
! This is module_ccfv_gradient.
!
! This module containes data and subroutines required by a least-squares
! gradient method for a cell-centered FV method.
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

 module module_ccfv_gradient

  use module_common_data, only : p2, one, zero !To declare double precision variables below.

  implicit none

  !Data that can be used in other modules/subroutines.
   public :: cclsq

  !Subroutine that can be used in other modules/subroutines.
   public :: compute_lsq_coefficients !To compute LSQ coefficients. Call this somewhere in main.
   public :: compute_gradients        !To compute gradients. Call this in the residual subroutine.


  !The data defined below will not be used in other modules and main program.
  !So, they are not declared as public here.

 !------------------------------------------------------------------------------------
 !------------------------------------------------------------------------------------
 ! Below are the definition of the data used to a LSQ gradient method.
 !------------------------------------------------------------------------------------

  !------------------------------------------
  !>> Cell-centered LSQ stencil data
  !------------------------------------------

   !Custom data type for lsq gradient stencil (nghbrs used in LSQ).
    type cc_lsq_data_type
     integer                           :: nnghbrs_lsq !number of lsq neighbors
     integer , dimension(:)  , pointer ::  nghbr_lsq  !list of lsq neighbors
     real(p2), dimension(:)  , pointer ::         cx  !LSQ coefficient for x-derivative
     real(p2), dimension(:)  , pointer ::         cy  !LSQ coefficient for y-derivative
    end type cc_lsq_data_type

    !Cell data array in the custom data type.
     type(cc_lsq_data_type), dimension(:), pointer :: cclsq  !cell-centered LSQ array

    !E.g., # of nghbrs at cell i = cclsq(i)%nnghbrs_lsq 
    !      a list of nghbrs at cell i = cclsq(i)%nghbr_lsq(1:cclsq(i)%nnghbrs_lsq)

  !These data will be allocated for a given grid size, and filled in the
  !following subroutine: compute_lsq_coefficients.

 !------------------------------------------------------------------------------------
 ! End of the data used to implement a LSQ gradient method.
 !------------------------------------------------------------------------------------
 !------------------------------------------------------------------------------------

 contains

!*******************************************************************************
! Compute the LSQ gradients in all cells for all primitive variables.
!
! - Compute the gradient by [wx,wy] = sum_nghbrs [cx,cy]*(w_nghbr - wj),
!   where [cx,cy] are the LSQ coefficients.
!
!*******************************************************************************
 subroutine compute_gradients

  use module_common_data   , only : zero
  use module_ccfv_data_grid, only : ncells
  use module_ccfv_data_soln, only : gradw, w


  implicit none

  real(p2) :: wi, wk
  integer  :: ivar, i, k, nghbr_cell

 !Initialize the gradient array.

  gradw(:,:,:) = zero

 !Compute the gradients for each primitive variable.

  variables : do ivar = 1, 4

   !Compute the gradietns in all cells.
    cell_loop : do i = 1, ncells

      wi = w(i,ivar)

     nghbr_loop : do k = 1, cclsq(i)%nnghbrs_lsq

      nghbr_cell = cclsq(i)%nghbr_lsq(k) !Neighbor cell number
              wk = w(nghbr_cell,ivar)    !Solution at the neighbor cell.

       gradw(i,ivar,1) = gradw(i,ivar,1) + cclsq(i)%cx(k)*(wk-wi)
       gradw(i,ivar,2) = gradw(i,ivar,2) + cclsq(i)%cy(k)*(wk-wi)

     end do nghbr_loop

   end do cell_loop

  end do variables

 end subroutine compute_gradients
!*******************************************************************************

!*******************************************************************************
! Construct vertex-neighbor stencils for gradient computations:
!
! Vertex-neighbors = All cells sharing the vertices of the cell of interest.
!
! For each cell, i, collect all cells sharing the nodes
! of the cell, i, including face-neighors.
!
!     ____________
!     |     |     |
!     | 15  |  98 |
!     |_____|_____|
!    /\  3 / \    \
!   /  \  / i \ 43 \
!  /_9__\/_____\____\
!  \  2 /      /\    \
!   \  /  128 /  \ 17 \
!    \/______/_7__\____\
!
!          i: Cell of interest
!          o: 9 vertex neighbors = [3,9,2,15,7,128,17,43,98]
!
!*******************************************************************************
 subroutine construct_vertex_stencil

  use module_common_data   , only : nnodes
  use module_ccfv_data_grid, only : cell, ncells

  implicit none

  !To store the list of cells around each node.
   type node_type
    integer                        :: nc
    integer, dimension(:), pointer :: c
   end type node_type

  !Array of custom-node-type data.
  type(node_type), dimension(:), pointer :: node

  integer :: i, k, vk, kc, ii
  integer :: candidate_cell, n
  logical :: already_added

  integer :: ave_nghbr, min_nghbr, max_nghbr !<- For statistics
  integer :: max_nghbrs, imin, imax, icount  !<- For statistics
  integer, dimension(100) :: nghbrs !<- For statistics. Let's assume max # of nghbrs is 100. 

  write(*,*)
  write(*,*) " --------------------------------------------------"
  write(*,*) " Constructing vertex neighbors... "
  write(*,*)

 ! Initialization for statistical quantities.

   max_nghbrs = 0
       nghbrs = 0

    ave_nghbr = 0
    min_nghbr = 10000
    max_nghbr =-10000
         imin = 1
         imax = 1

 ! First, create node-to-cell lists for convenience.
 ! [Same as done in edu2d_module_ccfv_data_grid.f90.]

    allocate( node(nnodes) )

    do i = 1, nnodes
     node(i)%nc  = 0
    end do

    do i = 1, ncells
     do k = 1, cell(i)%nvtx
                vk = cell(i)%vtx(k)
       node(vk)%nc = node(vk)%nc + 1
     end do
    end do

    do i = 1, nnodes
     allocate( node(i)%c( node(i)%nc ) )
    end do

    do i = 1, nnodes
     node(i)%nc  = 0
    end do

    do i = 1, ncells
     do k = 1, cell(i)%nvtx
                              vk = cell(i)%vtx(k)
         node(vk)%nc             = node(vk)%nc + 1
         node(vk)%c(node(vk)%nc) = i
     end do
    end do

 !Allocate and initialize the LSQ (custom data) array.

  allocate(cclsq(ncells))

 !Initialize it.

  do i = 1, ncells
   cclsq(i)%nnghbrs_lsq = 0
  end do

 !------------------------------------------------------------------------
 ! Find vertex neighbors at each cell.

  cell_loop : do i = 1, ncells

   cell_vertex_loop : do k = 1, cell(i)%nvtx

     vk = cell(i)%vtx(k) !k-th vertex of cell i.

      node2cell_loop : do kc = 1, node(vk)%nc !cells around k-th vertex.

       candidate_cell = node(vk)%c(kc)

       if (candidate_cell == i) cycle node2cell_loop !Skip the cell i.

       !Check if the cell is already added.
        already_added = .false.
        if (cclsq(i)%nnghbrs_lsq > 0) then
         do ii = 1, cclsq(i)%nnghbrs_lsq
          if ( candidate_cell == cclsq(i)%nghbr_lsq(ii) ) then
           already_added = .true.
           exit !OK, it is already added. Go to the next candidate.
          endif
         end do
        endif

       !Add the candidate_cell if not added yet.
        if (.not.already_added) then
                            n = cclsq(i)%nnghbrs_lsq + 1
         cclsq(i)%nnghbrs_lsq = n                     !Increase the size by 1.
         call my_alloc_int_ptr(cclsq(i)%nghbr_lsq, n) !Expand the array by 1.
         cclsq(i)%nghbr_lsq(n) = candidate_cell       !Store the candidate.
        endif

      end do node2cell_loop

   end do cell_vertex_loop

  ! Allocate the LSQ coeffient arrays for the cell i:

    allocate( cclsq(i)%cx(cclsq(i)%nnghbrs_lsq) )
    allocate( cclsq(i)%cy(cclsq(i)%nnghbrs_lsq) )

  ! Record some statistics.

    ave_nghbr = ave_nghbr + cclsq(i)%nnghbrs_lsq
    if (cclsq(i)%nnghbrs_lsq < min_nghbr) imin = i
    if (cclsq(i)%nnghbrs_lsq > max_nghbr) imax = i
    min_nghbr = min(min_nghbr, cclsq(i)%nnghbrs_lsq)
    max_nghbr = max(max_nghbr, cclsq(i)%nnghbrs_lsq)

    icount         = cclsq(i)%nnghbrs_lsq
    max_nghbrs     = max(max_nghbrs, icount)
    nghbrs(icount) = nghbrs(icount) + 1

  end do cell_loop
 !------------------------------------------------------------------------

 ! Deallocate 'node' as we don't need it any more.

   deallocate( node )

 ! Print some statistics on screen.

   write(*,*)
   write(*,*) " Constructed vertex neighbors "
   write(*,*)
   write(*,*) "      ave_nghbr = ", ave_nghbr/ncells
   write(*,*) "      min_nghbr = ", min_nghbr, " elm = ", imin
   write(*,*) "      max_nghbr = ", max_nghbr, " elm = ", imax
   write(*,*)
    do k = 1, max_nghbrs
     write(*,*) " # of neighbors = ", k,  ": # of such cells = ", nghbrs(k)
    end do
   write(*,*)
   write(*,*) " End of Constructing vertex neighbors... "
   write(*,*) " --------------------------------------------------"
   write(*,*)

 end subroutine construct_vertex_stencil
!*******************************************************************************



!*******************************************************************************
! Cmpute the LSQ coefficients in all cells.
!
! - Each LSQ coefficient is stored in a 1D array. For example, the # of nghbrs
!   in a cell i is cclsq(i)%nnghbrs_lsq, and the list of neighbors is given by
!
!     cclsq(i)%nghbr_lsq(k), k = 1, cclsq(i)%nnghbrs_lsq
!
! - LSQ problem is a linear polynomial fit over neighbors (e.g., m nghbrs):
!
!     (x1-xi)*wxi + (y1-yi)*wyi = w1 - wi
!     (x2-xi)*wxi + (y2-yi)*wyi = w2 - wi
!                 .
!                 .
!     (xm-xi)*wxi + (ym-yi)*wyi = wm - wi
!
!   We use a weighted LSQ system (with a popular inverse-distance weighting):
!
!     weight_1 * [ (x1-xi)*wxi + (y1-yi)*wyi ] = weight_1 * [ w1 - wi ]
!     weight_2 * [ (x2-xi)*wxi + (y2-yi)*wyi ] = weight_2 * [ w2 - wi ]
!                 .
!                 .
!     weight_m * [ (xm-xi)*wxi + (ym-yi)*wyi ] = weight_2 * [ wm - wi ]
!
!   which is written as
!
!           A*(wx,wy)^T = RHS                (T: transpose)
!
!   where RHS = [ weight_1*(w1-wi), weight_2*(w2-wi), ..., weight_m*(wm-wi) ]^T.
!
!   Here, the problem solved by QR factorization: A = Q*R, which gives
!
!           (wx,wy)^T = R^{-1}*Q^T*RHS
!
! - QR factorization is performed by the subroutine qr_factorization().
!
!*******************************************************************************
 subroutine compute_lsq_coefficients

  use module_common_data   , only : p2, zero, one, two

  use module_ccfv_data_grid, only : cell, ncells

 implicit none

 integer                           :: i, k, nghbr_cell
 integer                           :: m, n             !Size of LSQ matrix: A(m,n).
 real(p2), pointer, dimension(:,:) :: a                !LSQ matrix: A(m,n).
 real(p2), pointer, dimension(:,:) :: rinvqt           !Pseudo inverse R^{-1}*Q^T
 real(p2)                          :: dx, dy, weight_k, lsq_weight_invdis_power
 integer                           :: ix, iy

 real(p2)                          :: xk, yk, xi, yi, wx, wy
 logical                           :: verifcation_error

 !--------------------------------------------------------------------------------
 !--------------------------------------------------------------------------------
 ! Allocate the custom-data LSQ array.

   call construct_vertex_stencil

  write(*,*)
  write(*,*) "--------------------------------------------------"
  write(*,*) " Computing LSQ coefficients... "
  write(*,*)

 ! Just for convenience.

   ix = 1
   iy = 2

 !--------------------------------------------------------------------------------
 !--------------------------------------------------------------------------------
 ! The power to the inverse distance weight. The value 0.0 is used to avoid
 ! instability known for Euler solvers. So, this is the unweighted LSQ gradient.
 ! More accurate gradients are obtained with 1.0, and such can be used for the
 ! viscous terms and source terms in turbulence models.

   lsq_weight_invdis_power = 0.0_p2

 !--------------------------------------------------------------------------------
 !--------------------------------------------------------------------------------
 ! Compute the LSQ coefficients (cx,cy) in all cells.

   cell_loop : do i = 1, ncells

   !-------------------------------------------------------
   ! Define the LSQ problem size

     m = cclsq(i)%nnghbrs_lsq !# of nghbrs
     n = 2                    !# of derivatives (unknowns) = 2, (ux,uy) in 2D.

   !-------------------------------------------------------
   ! Allocate LSQ matrix and the pseudo inverse, R^{-1}*Q^T.

     allocate(a(m,n))
     allocate(rinvqt(n,m))

   !-------------------------------------------------------
   ! Initialize A.

      a = zero

   !-------------------------------------------------------
   ! Build the weighted-LSQ matrix A(m,n).
   !
   !     weight_1 * [ (x1-xi)*wxi + (y1-yi)*wyi ] = weight_1 * [ w1 - wi ]
   !     weight_2 * [ (x2-xi)*wxi + (y2-yi)*wyi ] = weight_2 * [ w2 - wi ]
   !                 .
   !                 .
   !     weight_m * [ (xm-xi)*wxi + (ym-yi)*wyi ] = weight_2 * [ wm - wi ]

     nghbr_loop : do k = 1, m

      nghbr_cell = cclsq(i)%nghbr_lsq(k) !Neighbor cell number

             dx = cell(nghbr_cell)%xc - cell(i)%xc
             dy = cell(nghbr_cell)%yc - cell(i)%yc

       weight_k = one / sqrt( dx**2 + dy**2 )**lsq_weight_invdis_power

         a(k,1) = weight_k*dx
         a(k,2) = weight_k*dy

     end do nghbr_loop

   !-------------------------------------------------------
   ! Perform QR factorization and compute R^{-1}*Q^T from A(m,n).

     call qr_factorization(a,rinvqt,m,n)

   !-------------------------------------------------------
   ! Compute and store the LSQ coefficients: R^{-1}*Q^T*w.
   !
   ! (wx,wy) = R^{-1}*Q^T*RHS
   !         = sum_k (cx,cy)*(wk-wi).

     nghbr_loop2 : do k = 1, m

       nghbr_cell = cclsq(i)%nghbr_lsq(k) !Neighbor cell number

             dx = cell(nghbr_cell)%xc - cell(i)%xc
             dy = cell(nghbr_cell)%yc - cell(i)%yc

       weight_k = one / sqrt( dx**2 + dy**2 )**lsq_weight_invdis_power

      cclsq(i)%cx(k)  = rinvqt(ix,k) * weight_k
      cclsq(i)%cy(k)  = rinvqt(iy,k) * weight_k

     end do nghbr_loop2

   !-------------------------------------------------------
   ! Deallocate a and rinvqt, whose size may change in the next cell. 

     deallocate(a, rinvqt)

  end do cell_loop

! Verification:
!  Compute the gradient of w=2*x+y to see if we get wx=2 and wy=1 correctly.

   verifcation_error = .false.

  do i = 1, ncells

   !Initialize wx and wy
    wx = zero 
    wy = zero

   !(xi,yi) to be used to compute the function 2*x+y at i.
    xi = cell(i)%xc 
    yi = cell(i)%yc 

  !Loop over the vertex neighbors.
   do k = 1, cclsq(i)%nnghbrs_lsq

    nghbr_cell = cclsq(i)%nghbr_lsq(k) !Neighbor cell number

           !(xk,yk) to be used to compute the function 2*x+y at k.
            xk = cell(nghbr_cell)%xc
            yk = cell(nghbr_cell)%yc

           !This is how we use the LSQ coefficients: accumulate cx*(wk-wi) and cy*(wk-wi).
            wx = wx + cclsq(i)%cx(k)*( (two*xk+yk)-(two*xi+yi) )
            wy = wy + cclsq(i)%cy(k)*( (two*xk+yk)-(two*xi+yi) )

   end do

   if ( abs(wx-two) > 1.0e-10_p2 .or. abs(wy-one) > 1.0e-10_p2) then
    write(*,*) " wx = ", wx, " exact ux = 2.0"
    write(*,*) " wy = ", wy, " exact uy = 1.0"
    verifcation_error = .true.
   endif

  end do

  if (verifcation_error) then

   write(*,*) " LSQ coefficients are not correct. See above. Stop."
   stop

  else

   write(*,*) " Verified: LSQ coefficients are exact for a linear function."

  endif

  write(*,*)
  write(*,*) " End of Computing LSQ coefficients... "
  write(*,*) "--------------------------------------------------"
  write(*,*)

 ! End of Compute the LSQ coefficients in all cells.
 !--------------------------------------------------------------------------------
 !--------------------------------------------------------------------------------

 end subroutine compute_lsq_coefficients
!*******************************************************************************


!****************************************************************************
! ------------------ QR Factorization ---------------------
!
!  This subroutine solves the LSQ problem: A*x=b, A=mxn matrix.
!
!  IN :       a = (m x n) LSQ matrix.  (m >= n)
!
! OUT :  rinvqt = R^{-1}*Q^t, which gives the solution as x = R^{-1}*Q^t*b.
!
!*****************************************************************************
 subroutine qr_factorization(a,rinvqt,m,n)

 implicit none

  integer , parameter ::   p2 = selected_real_kind(P=15) !Double precision
  real(p2), parameter :: zero = 0.0_p2
  real(p2), parameter ::  one = 1.0_p2
  real(p2), parameter ::  two = 2.0_p2

!Input
 integer ,                 intent( in) :: m, n
 real(p2), dimension(m,n), intent( in) :: a

!Output
 real(p2), dimension(n,m), intent(out) :: rinvqt

! Local variables
!
! Note: Think if you can reduce the number of
!       variables below to save memory.

 integer                  :: i, j, k

 real(p2), dimension(m,n) :: r
 real(p2)                 :: abs_rk, sign_rkk, wTw
 real(p2), dimension(m)   :: w, rk
 real(p2), dimension(m,m) :: qt, wwT

 real(p2), dimension(n,n) ::  r_nxn
 real(p2), dimension(n)   ::   y, b
 real(p2)                 ::    rhs

 if (m < n) then
  write(*,*) " Underdetermined system detected... m < n: "
  write(*,*) "   m =  ", m
  write(*,*) "   n =  ", n
  write(*,*) " qr_factorization() not designed to solve such a problem... Stop. "
  stop
 endif

!-------------------------------------------------------
! Initialization: R = A

   r = a

!-------------------------------------------------------
! Initialization: Qt = I

       qt = zero

  do i = 1, m
   qt(i,i) = one
  end do

!-------------------------------------------------------
! Apply reflection to each column of R, and generate
! the final upper triangular matrix R and the transpose
! Qt of the orthonormal matrix Q.

 column_loop : do k = 1, n

  !Our target are the elements below the (k,k) element
  !in k-th column, i.e., r(k:m).
  !So, rk gets shorter as we move on (as k increases).

        rk      = zero
        rk(k:m) = r(k:m,k)

  !Reflector Hk will zero out all the elements below r(k).

  !Compute the length of rk and the sign of the kth element.

         abs_rk = sqrt( dot_product(rk,rk) )
       sign_rkk = sign( one, rk(k) )

  !Define the reflecting vector w:   w = |rk|*(1,0,0,...,0)-rk
  !                               or w =-|rk|*(1,0,0,...,0)-rk
  !We switch the reflection (there are two possible ones)
  !to avoid w = 0 that can happen if rk=(1,0,0,...,0).

         w      = zero
         w(k)   = -sign_rkk*abs_rk
         w(k:m) = w(k:m) - rk(k:m)

  !Compute the length^2 of w: wt*w = [x,x,...,x]|x| = dot product = scalar.
  !                                             |x|
  !                                             |.|
  !                                             |.|
  !                                             |x|

    wTw = dot_product(w,w)

  !Compute the dyad of w: w*wt = |x|[x,x,...,x] = mxm matrix.
  !                              |x|
  !                              |.|
  !                              |.|
  !                              |x|

    do i = 1, m
     do j = 1, m
      wwT(i,j) = w(i)*w(j)
     end do
    end do

  !We now apply the reflector matrix Hk = I-2*wwt/wTw,
  !and update R and Qt.

  !Update  R:  R = Hk*R  = (I-2*wwt/wTw)*R  = R-2*(wwt*R)/wTw

   r  =  r - two*matmul(wwT,r)/wTw

  !Update Qt: Qt = Hk*Qt = (I-2*wwt/wTw)*Qt = Qt-2*(wwt*Qt)/wTw

   qt = qt - two*matmul(wwT,qt)/wTw

 end do column_loop

!-------------------------------------------------------
! Compute rinvqt(1:n,1:m) = R_{nxn}^{-1} * Q_{nxm}^t by
! solving R_{nxn} * rinvqt(1:n,k) = Q_{nxm}^t(1:n,k)
! for k=1,n. We can solve it easily by back substitution
! since R_{nxn} is upper triangular.

   r_nxn =  r(1:n,1:n)

   do k = 1, m

    !Solve r*y = b, where y is the k-th column of rinvqt.

        b = qt(1:n,k)

    !Solve the lower right equation.

      rhs = b(n)
     y(n) = rhs/r_nxn(n,n)

    !Go up and solve.
     do i = n-1, 1, -1

     !Take all known parts (j=i+1,n) to the rhs.

      !RHS is known, of course.
        rhs = b(i)
      !Below are all known since the solutions y(j=i+1,n) has already been solved.
       do j = i+1, n
        rhs = rhs - r_nxn(i,j)*y(j)
       end do

     !Divide the rhs by the coefficient of the (i,i) part.
      y(i) = rhs/r_nxn(i,i)

     end do

   !The soluton x is the k-th column of rinvqt.
    rinvqt(:,k) = y(:)

   end do

 end subroutine qr_factorization


!********************************************************************************
! This subroutine is useful to expand integer arrays.
!
!  Array, x, will be allocated if the requested dimension is 1 (i.e., n=1).
!  Array, x, will be expanded to the requested dimension, n, if (n > dim(x)).
!
! For example, with the input
!
!  n = 7
!  x = [9,4,2,1]
!
! this subroutine will return
!
!  x = [9,4,2,1,0,0,0].
!
! Note: If n=1, this subroutine takes is as an initialization, and returns
!
!  x = [0].
!
! Note: So, this subroutine can only expand an interger array. It does not
!       shrink an array. If n < size(x), then it is considered as an error and
!       stop. If you want, I believe you can implement it.
!
!********************************************************************************
  subroutine my_alloc_int_ptr(x,n)

  implicit none

  integer, intent(in) :: n

  integer, dimension(:), pointer :: x
  integer, dimension(:), pointer :: temp

  integer :: i

! Error if n is negative.

  if (n <= 0) then
   write(*,*) "my_alloc_int_ptr received non-positive dimension. Stop."
   stop
  endif

! Shirinking an array is not implemented... Sorry.

  if ( n < size(x) ) then
   write(*,*) "my_alloc_int_ptr received a smaller dimension. Not implemented. Stop."
   stop
  endif

! If dimension 1, just allocate and return.

  if (n==1) then
   if (associated(x)) nullify(x)
   allocate(x(1))
   return
  endif

! If reallocation (i.e., n > size(x), create a pointer with a target with the requested dimension.

  allocate(temp(n))
  temp = 0

! Copy the existing data: e.g., for n=7 and x=[9,4,2,1] -> we construct temp=[9,4,2,1,0,0,0].

   do i = 1, size(x)
    temp(i) = x(i)
   end do

! Re-assign the pointer: x=[9,4,2,1,0,0,0].
   x => temp

  return

  end subroutine my_alloc_int_ptr
!********************************************************************************


 end module module_ccfv_gradient

