!********************************************************************************
!* Educationally-Designed Unstructured 2D (EDU2D) Code
!*
!*
!*
!* This file contains 4 modules:
!*
!*  1. module edu2d_constants      - Some numerical values, e.g., zero, one, pi, etc.
!*  2. module edu2d_grid_data_type - Grid data types: node, edge, face, element, etc.
!*  3. module edu2d_my_main_data   - Parameters and arrays mainly used in a solver.
!*  4. module edu2d_my_allocation  - Subroutines for dynamic allocation
!*  5. module edu2d_grid_data      - Subroutines for reading/constructing/checking grid data
!*
!* All data in the modules can be accessed by the use statement, e.g., 'use constants'.
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

!********************************************************************************
!********************************************************************************
!********************************************************************************
!********************************************************************************
!********************************************************************************
!* 1. module edu2d_constants
!*
!* Some useful constants are defined here.
!* They can be accessed by the use statement, 'use constants'.
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
 module edu2d_constants

  implicit none

  private

  public :: p2
  public :: zero, one, two, three, four, five, six, seven, eight, nine
  public :: ten, eleven
  public :: half, third, fourth, fifth, sixth, two_third, four_third
  public :: three_fourth, twelfth, pi, one_twentyfourth

  integer , parameter :: sp = kind(1.0)
  integer , parameter :: p2 = selected_real_kind(2*precision(1.0_sp))

  real(p2), parameter :: zero = 0.0_p2, &
                          one = 1.0_p2, &
                          two = 2.0_p2, &
                        three = 3.0_p2, &
                         four = 4.0_p2, &
                         five = 5.0_p2, &
                          six = 6.0_p2, &
                        seven = 7.0_p2, &
                        eight = 8.0_p2, &
                         nine = 9.0_p2, &
                          ten = 10.0_p2, &
                       eleven = 11.0_p2, &
                         half = 0.5_p2, &
                        third = 1.0_p2/ 3.0_p2, &
                       fourth = 1.0_p2/ 4.0_p2, &
                        fifth = 1.0_p2/ 5.0_p2, &
                        sixth = 1.0_p2/ 6.0_p2, &
                    two_third = 2.0_p2/ 3.0_p2, &
                   four_third = 4.0_p2/ 3.0_p2, &
                 three_fourth = 3.0_p2/ 4.0_p2, &
                      twelfth = 1.0_p2/12.0_p2, &
             one_twentyfourth = 1.0_p2/24.0_p2

  real(p2), parameter :: pi = 3.141592653589793238_p2

 end module edu2d_constants
!********************************************************************************

!********************************************************************************
!********************************************************************************
!********************************************************************************
!********************************************************************************
!********************************************************************************
!* 2. module grid_data_type
!*
!* This module defines custom grid data types for unstructured grids
!*
!* NOTE: These data types are designed to make it easier to understand the code.
!*       They may not be the best in terms of efficiency.
!*
!* NOTE: Custom grid data types (derived types) are very useful.
!*       For example, if I declare a variable, "a", by the statemant:
!*           type(node_type), dimension(100) :: a
!*       The variable, a, is a 1D array each component of which contains all data
!*       defined as below. These data can be accessed by %, e.g.,
!*           a(1)%x, a(1)%y, a(1)%nghbr(1:nnghbrs), etc.
!*       In C-programming, this type of data is called "structure", I think.
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
 module edu2d_grid_data_type

  use edu2d_constants, only : p2

  implicit none

  private

  public ::  node_type
  public ::   elm_type
  public ::  edge_type
  public :: bgrid_type
  public ::  face_type

!----------------------------------------------------------
! Data type for nodal quantities (used for node-centered schemes)
! Note: Each node has the following data.
!----------------------------------------------------------
  type node_type
!  to be read from a grid file
   real(p2)                          :: x, y      !nodal coordinates
!  to be constructed in the code
   integer                           :: nnghbrs   !number of neighbors
   integer,   dimension(:), pointer  :: nghbr     !list of neighbors
   integer                           :: nelms     !number of elements
   integer,   dimension(:), pointer  :: elm       !list of elements
   real(p2)                          :: vol       !dual-cell volume
   integer                           :: bmark     !Boundary mark
   integer                           :: nbmarks   !# of boundary marks
!  to be computed in the code
   real(p2), dimension(:)  , pointer :: u         !conservative variables
!NotUsed   real(p2), dimension(:)  , pointer :: du        !change in conservative variables
   real(p2), dimension(:)  , pointer :: uexact    !conservative variables
   real(p2), dimension(:,:), pointer :: gradu     !gradient of u
   real(p2), dimension(:)  , pointer :: res       !residual (rhs)
   real(p2)                          :: ar        ! Control volume aspect ratio

!NotUsed  real(p2), dimension(:), pointer   :: r_temp    ! For GCR implementation
!NotUsed  real(p2), dimension(:), pointer   :: u_temp    ! For GCR implementation
!NotUsed  real(p2), dimension(:), pointer   :: w_temp    ! For GCR implementation

   real(p2), dimension(:)  , pointer :: lsq2x2_cx !    Linear LSQ coefficient for ux
   real(p2), dimension(:)  , pointer :: lsq2x2_cy !    Linear LSQ coefficient for uy

   real(p2), dimension(:)  , pointer :: lsq5x5_cx ! Quadratic LSQ coefficient for ux
   real(p2), dimension(:)  , pointer :: lsq5x5_cy ! Quadratic LSQ coefficient for uy
   real(p2), dimension(:  ), pointer :: dx, dy    ! Extra data used by Quadratic LSQ
   real(p2), dimension(:,:), pointer :: dw        ! Extra data used by Quadratic LSQ

  end type node_type

!----------------------------------------------------------
! Data type for element/cell quantities (used for cell-centered schemes)
! Note: Each element has the following data.
!----------------------------------------------------------
  type elm_type
!  to be read from a grid file
   integer                           :: nvtx     !number of vertices
   integer,   dimension(:), pointer  :: vtx      !list of vertices
!  to be constructed in the code
   integer                           :: nnghbrs  !number of neighbors
   integer,   dimension(:), pointer  :: nghbr    !list of neighbors
   real(p2)                          :: x, y     !cell center coordinates
   real(p2)                          :: vol      !cell volume

   integer,  dimension(:)  , pointer :: edge     !list of edges
   real(p2), dimension(:)  , pointer :: u        !conservative variables
   real(p2), dimension(:)  , pointer :: uexact   !conservative variables
   real(p2), dimension(:)  , pointer :: du       !change in conservative variables
   real(p2), dimension(:,:), pointer :: gradu    !gradient of u
   real(p2), dimension(:)  , pointer :: res      !residual (rhs)
   real(p2)                          :: dt       !local time step
   real(p2)                          :: wsn      !
   integer                           :: bmark    !Boundary mark
   integer                           :: nvnghbrs !number of vertex neighbors
   integer,  dimension(:), pointer   :: vnghbr   !list of vertex neighbors
   real(p2)                          :: ar       !Element volume aspect ratio
   real(p2), dimension(:) , pointer  :: lsq2x2_cx!Linear LSQ coefficient for ux
   real(p2), dimension(:) , pointer  :: lsq2x2_cy!Linear LSQ coefficient for uy

  end type elm_type

!----------------------------------------------------------
! Data type for edge quantities (used for node-centered schemes)
! Note: Each edge has the following data.
!----------------------------------------------------------
  type edge_type
!  to be constructed in the code
   integer                          :: n1, n2 !associated nodes
   integer                          :: e1, e2 !associated elements
   real(p2),           dimension(2) :: dav    !unit directed-area vector
   real(p2)                         :: da     !magnitude of the directed-area vector
   real(p2),           dimension(2) :: ev     !unit edge vector
   real(p2)                         :: e      !magnitude of the edge vector
   integer                          :: kth_nghbr_of_1 !neighbor index
   integer                          :: kth_nghbr_of_2 !neighbor index
  end type edge_type

!----------------------------------------------------------
! Data type for boundary quantities (for both node/cell-centered schemes)
! Note: Each boundary segment has the following data.
!----------------------------------------------------------
  type bgrid_type
!  to be read from a boundary grid file
   character(80)                    :: bc_type !type of boundary condition
   integer                          :: nbnodes !# of boundary nodes
   integer,   dimension(:), pointer :: bnode   !list of boundary nodes
!  to be constructed in the code
   integer                          :: nbfaces !# of boundary faces
   real(p2),  dimension(:), pointer :: bfnx    !x-component of the face outward normal
   real(p2),  dimension(:), pointer :: bfny    !y-component of the face outward normal
   real(p2),  dimension(:), pointer :: bfn     !magnitude of the face normal vector
   real(p2),  dimension(:), pointer :: bnx     !x-component of the outward normal
   real(p2),  dimension(:), pointer :: bny     !y-component of the outward normal
   real(p2),  dimension(:), pointer :: bn      !magnitude of the normal vector
   integer ,  dimension(:), pointer :: belm    !list of elm adjacent to boundary face
   integer ,  dimension(:), pointer :: kth_nghbr_of_1
   integer ,  dimension(:), pointer :: kth_nghbr_of_2
  end type bgrid_type

!----------------------------------------------------------
! Data type for face quantities (used for cell-centered schemes)
!
! A face is defined by a line segment connecting two nodes.
! The directed area is defined as a normal vector to the face,
! pointing in the direction from e1 to e2.
!
!      n2
!       o------------o
!     .  \         .
!    .    \   e2  .
!   .  e1  \    .
!  .        \ .         Directed area is positive: n1 -> n2
! o----------o         e1: left element
!             n1       e2: right element (e2 > e1 or e2 = 0)
!
! Note: Each face has the following data.
!----------------------------------------------------------
  type face_type
! to be constructed in the code (NB: boundary faces are excluded.)
   integer                         :: n1, n2 !associated nodes
   integer                         :: e1, e2 !associated elements
   real(p2),          dimension(2) :: dav    !unit directed-area vector
   real(p2)                        :: da     !magnitude of the directed-area vector
  end type face_type


 end module edu2d_grid_data_type
!********************************************************************************


!********************************************************************************
!********************************************************************************
!********************************************************************************
!********************************************************************************
!********************************************************************************
!* 3. module my_main_data 
!*
!* This module defines the main data that will be used in the code.
!*
!* The main data include parameters and data arrays. They can be accessed by
!* other routines via the use statement: 'use my_main_data'.
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
 module edu2d_my_main_data

  use edu2d_constants     , only : p2, one
  use edu2d_grid_data_type, only : node_type, elm_type, edge_type, bgrid_type, face_type

  implicit none

  private

  public :: nnodes, node
  public :: ntria, nquad, nelms, elm
  public :: nedges, edge
  public :: nbound, bound
  public :: nfaces, face

  public :: nq, gradient_type, gradient_weight, gradient_weight_p

!  Parameters

   integer       :: nq = 3 ! Number of equtaions/variables in the target equtaion.
                           ! Here, 3 equations/vairables has been assumed.
   character(80) ::     gradient_type  = "linear" ! or "quadratic2"
   character(80) ::    gradient_weight = "none"   ! or "inverse_distance"
   real(p2)      :: gradient_weight_p  =  one     ! or any other real value

!  Node data
   integer                                 :: nnodes !total number of nodes
   type(node_type), dimension(:), pointer  :: node   !array of nodes

!  Element data (element=cell)
   integer                                 :: ntria  !total number of triangler elements
   integer                                 :: nquad  !total number of quadrilateral elements
   integer                                 :: nelms  !total number of elements
   type(elm_type),  dimension(:), pointer  :: elm    !array of elements

!  Edge data
   integer                                 :: nedges !total number of edges
   type(edge_type), dimension(:), pointer  :: edge   !array of edges

!  Boundary data
   integer                                 :: nbound !total number of boundary types
   type(bgrid_type), dimension(:), pointer :: bound  !array of boundary segments

!  Face data (cell-centered scheme only)
   integer                                 :: nfaces !total number of cell-faces
   type(face_type), dimension(:), pointer  :: face   !array of cell-faces

 end module edu2d_my_main_data
!********************************************************************************


!********************************************************************************
!********************************************************************************
!********************************************************************************
!********************************************************************************
!********************************************************************************
!* 4. module my_allocation
!*
!* This module defines some useful subroutines used for dynamic allocation.
!*
!*  - my_alloc_int_ptr       : Allocate/reallocate an integer 1D array
!*  - my_alloc_p2_ptr        : Allcoate/reallocate a real 1D array
!*  - my_alloc_p2_matrix_ptr : Allcoate/reallocate a real 2D array
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
 module edu2d_my_allocation

  implicit none

  private

  public :: my_alloc_int_ptr
  public :: my_alloc_p2_ptr
  public :: my_alloc_p2_matrix_ptr

  contains

!********************************************************************************
!* This subroutine is useful to expand or shrink integer arrays.
!*
!*  Array, x, will be allocated if the requested dimension is 1 (i.e., n=1)
!*  Array, x, will be expanded to the requested dimension, n, if (n > dim(x)).
!*  Array, x, will be shrinked to the requested dimension, n, if (n < dim(x)).
!*
!********************************************************************************
  subroutine my_alloc_int_ptr(x,n)

  implicit none
  integer, intent(in) :: n
  integer, dimension(:), pointer :: x
  integer, dimension(:), pointer :: temp
  integer :: i

  if (n <= 0) then
   write(*,*) "my_alloc_int_ptr received non-positive dimension. Stop."
   stop
  endif

! If not allocated, allocate and return
  if (.not.(associated(x))) then
   allocate(x(n))
   return
  endif

! If reallocation, create a pointer with a target of new dimension.
  allocate(temp(n))
   temp = 0

! (1) Expand the array dimension
  if ( n > size(x) ) then

   do i = 1, size(x)
    temp(i) = x(i)
   end do

! (2) Shrink the array dimension: the extra data, x(n+1:size(x)), discarded.
  else

   do i = 1, n
    temp(i) = x(i)
   end do

  endif

! Destroy the target of x
!  deallocate(x)

! Re-assign the pointer
   x => temp

  return

  end subroutine my_alloc_int_ptr
!********************************************************************************


!********************************************************************************
!* This subroutine is useful to expand or shrink real arrays.
!*
!*  Array, x, will be allocated if the requested dimension is 1 (i.e., n=1)
!*  Array, x, will be expanded to the requested dimension, n, if (n > dim(x)).
!*  Array, x, will be shrinked to the requested dimension, n, if (n < dim(x)).
!*
!********************************************************************************
  subroutine my_alloc_p2_ptr(x,n)

  use edu2d_constants   , only : p2

  implicit none
  integer, intent(in) :: n
  real(p2), dimension(:), pointer :: x
  real(p2), dimension(:), pointer :: temp
  integer :: i

  if (n <= 0) then
   write(*,*) "my_alloc_int_ptr received non-positive dimension. Stop."
   stop
  endif

! If not allocated, allocate and return
  if (.not.(associated(x))) then
   allocate(x(n))
   return
  endif

! If reallocation, create a pointer with a target of new dimension.
  allocate(temp(n))
   temp = 0

! (1) Expand the array dimension
  if ( n > size(x) ) then

   do i = 1, size(x)
    temp(i) = x(i)
   end do

! (2) Shrink the array dimension: the extra data, x(n+1:size(x)), discarded.
  else

   do i = 1, n
    temp(i) = x(i)
   end do

  endif

! Destroy the target of x
  deallocate(x)

! Re-assign the pointer
   x => temp

  return

  end subroutine my_alloc_p2_ptr


!********************************************************************************
!* This subroutine is useful to expand or shrink real arrays.
!*
!*  Array, x, will be allocated if the requested dimension is 1 (i.e., n=1)
!*  Array, x, will be expanded to the requested dimension, n, if (n > dim(x)).
!*  Array, x, will be shrinked to the requested dimension, n, if (n < dim(x)).
!*
!********************************************************************************
  subroutine my_alloc_p2_matrix_ptr(x,n,m)

  use edu2d_constants   , only : p2

  implicit none
  integer, intent(in) :: n, m
  real(p2), dimension(:,:), pointer :: x
  real(p2), dimension(:,:), pointer :: temp
  integer :: i, j

  if (n <= 0) then
   write(*,*) "my_alloc_int_ptr received non-positive dimension. Stop."
   stop
  endif

! If not allocated, allocate and return
  if (.not.(associated(x))) then
   allocate(x(n,m))
   return
  endif

! If reallocation, create a pointer with a target of new dimension.
  allocate(temp(n,m))
   temp = 0.0_p2

  do i = 1, min(n, size(x,1))
   do j = 1, min(m, size(x,2))
    temp(i,j) = x(i,j)
   end do
  end do

! Destroy the target of x
  deallocate(x)

! Re-assign the pointer
   x => temp

  return

  end subroutine my_alloc_p2_matrix_ptr

 end module edu2d_my_allocation
!********************************************************************************


!********************************************************************************
!********************************************************************************
!********************************************************************************
!********************************************************************************
!********************************************************************************
!* 5. module edu2d_grid_data
!*
!* This module contians subroutines used for reading a grid, constructing
!* additional grid data, and check the grid data.
!*
!*  - my_alloc_int_ptr       : Allocate/reallocate an integer 1D array
!*  - my_alloc_p2_ptr        : Allcoate/reallocate a real 1D array
!*  - my_alloc_p2_matrix_ptr : Allcoate/reallocate a real 2D array
!*
!*
!* Public subroutines:
!*
!*  - read_grid            : Read a grid file, allocate necessary data.
!*  - construct_grid_data  : Construct additional data, allocate more data.
!*  - check_grid_data      : Check the whole grid data.
!*
!* Private functions and subroutines:
!*
!*  - tri_area             : Computed a triangle area
!*  - check_skewness_nc    : Compute the skewness (e*n).
!*  - compute_ar           : Compute aspect ratio at node and element.
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
 module edu2d_grid_data

 private

 public :: read_grid
 public :: construct_grid_data
 public :: check_grid_data

 contains

!********************************************************************************
!* Read the grid and the exact solution.
!* ------------------------------------------------------------------------------
!*  Input: datafile_grid_in  = filename of the grid file
!*         datafile_bcmap_in = filename of the bc file
!*
!* Output: nnodes, ncells, node(:), elm(:), bound(:) = data used in the solver
!* ------------------------------------------------------------------------------
!*
!********************************************************************************
!* 1. "datafile_grid_in" is assumed to have been written in the following format:
!*
!*   -----------------------------------------------------------------------
!*    write(*,*) nnodes, ntria, nquad !Numbers of nodes, triangles and quads
!*
!*   do i = 1, nnodes
!*    write(*,*) x(i), y(i) !(x,y) coordinates of each node
!*   end do
!*
!*   do i = 1, ntria        !Nodes of triangles ordered counterclockwise
!*    write(*,*) node_1(i), node_2(i), node_3(i)
!*   end do
!*
!*   do i = 1, nquad        !Nodes of quadrilaterals ordered counterclockwise
!*    write(*,*) node_1(i), node_2(i), node_3(i), node_4(i)
!*   end do
!* 
!*    write(*,*) nbound     !Number of boundary segments
!*
!*   do i = 1, nbound
!*    write(*,*) nbnodes(i) !Number of nodes on each segment
!*   end do
!*
!*   do i = 1, nbound
!*    do j = 1, nbnodes(i)
!*     write(*,*) bnode(j)  !Node number of each node j in segment i
!*    end do
!*   end do
!*   -----------------------------------------------------------------------
!*
!*   NOTE: Add the first node to the end if the segment is closed
!*         (e.g., airfoil) The number of nodes will be the actual number + 1
!*         in that case.
!*
!*   NOTE: Boundary nodes must be ordered such that the domain is on the left.
!*
!********************************************************************************
!*
!* 2. "datafile_bcmap_in" is assumed have been written in the following format:
!*
!*   -----------------------------------------------------------------------
!*    write(*,*) "Boundary Segment              Boundary Condition"
!*   do i = 1, nbound
!*    write(*,*) i, bc_name
!*   end do
!*   -----------------------------------------------------------------------
!*
!*   NOTE: bc_name is the name of the boundary condition, e.g.,
!*
!*         1. "freestream"
!*             Roe flux with freestream condition on the right state.
!*
!*         2. "slip_wall"
!*             Solid wall condition. Mass flux through the boundary is set zero.
!*
!*         3. "outflow_supersonic"
!*             Just compute the boundary flux by the physical Euler flux
!*             (equivalent to the interior-extrapolation condition.)
!*
!*         4. "outflow_back_pressure"
!*             Fix the back pressure. This should work for subsonic flows in a
!*             large enough domain.
!*
!*         Something like the above needs to be implemented in a solver.
!*
!********************************************************************************
!* Data to be read and stored:
!*
!* 1. Some numbers
!*    nnodes        = Number of nodes
!*    ntria         = Number of triangular elements
!*    nquad         = Number of quadrilateral elements
!*    nelms         = Total number of elements (=ntria+nquad)
!*
!* 2. Element data:
!*    elm(1:nelms)%nvtx   =  Number of vertices of each element
!*    elm(1:nelms)%vtx(:) = Pointer to vertices of each element
!*
!* 3. Node data: nodes are stored in a 1D array
!*    node(1:nnodes)%x     = x-coordinate of the nodes
!*    node(1:nnodes)%y     = y-coordinate of the nodes
!*
!* 4. Boundary Data:
!*    nbound                   = Number of boundary segments
!*    bound(1:nbound)%nbnodes  = Number of nodes in each segment
!*    bound(1:nbound)%bnode(:) = List of node numbers for each segment
!*    bound(1:nbound)%bc_type  = Boundary condition name for each segment
!*    bound(1:nbound)%bc_type  = Boundary condition name for each segment
!*
!********************************************************************************
 subroutine read_grid(datafile_grid_in, datafile_bcmap_in)

 use edu2d_my_main_data, only : nnodes, node, ntria, nquad, nelms, elm, nbound, bound

 implicit none
 character(80), intent(in) :: datafile_grid_in, datafile_bcmap_in

!Local variables
 integer  :: i, j, os, dummy_int

!--------------------------------------------------------------------------------
! 1. Read grid file>: datafile_grid_in

  write(*,*) "Reading the grid file....", datafile_grid_in

!  Open the input file.
   open(unit=1, file=datafile_grid_in, status="unknown", iostat=os)

! READ: Get the size of the grid.
  read(1,*) nnodes, ntria, nquad
  nelms = ntria + nquad

!  Allocate node and element arrays.
   allocate(node(nnodes))
   allocate(elm(  nelms))

! READ: Read the nodal coordinates
  do i = 1, nnodes
   read(1,*) node(i)%x, node(i)%y
  end do

! Read element-connectivity information

! Triangles: assumed that the vertices are ordered counterclockwise
!
!         v3
!         /\
!        /  \
!       /    \
!      /      \
!     /        \
!    /__________\
!   v1           v2

! READ: read connectivity info for triangles
  if ( ntria > 0 ) then
   do i = 1, ntria
    elm(i)%nvtx = 3
    allocate(elm(i)%vtx(3))
    read(1,*) elm(i)%vtx(1), elm(i)%vtx(2), elm(i)%vtx(3)
   end do
  endif

! Quads: assumed that the vertices are ordered counterclockwise
!
!        v4________v3
!         /        |
!        /         |
!       /          |
!      /           |
!     /            |
!    /_____________|
!   v1             v2

! READ: read connectivity info for quadrilaterals
  if ( nquad > 0 ) then
   do i = 1, nquad
    elm(ntria+i)%nvtx = 4
    allocate( elm(ntria+i)%vtx(4))
    read(1,*) elm(ntria+i)%vtx(1), elm(ntria+i)%vtx(2), &
              elm(ntria+i)%vtx(3), elm(ntria+i)%vtx(4)
   end do
  endif

!  Write out the grid data.

   write(*,*)
   write(*,*) " Total numbers:"
   write(*,*) "      nodes = ", nnodes
   write(*,*) "  triangles = ", ntria
   write(*,*) "      quads = ", nquad
   write(*,*)

! Read the boundary grid data

! READ: Number of boundary condition types
  read(1,*) nbound
  allocate(bound(nbound))

! READ: Number of Boundary nodes (including the starting one at the end if
! it is closed such as an airfoil.)
  do i = 1, nbound
   read(1,*) bound(i)%nbnodes
   allocate(bound(i)%bnode(bound(i)%nbnodes))
  end do

! READ: Read boundary nodes
  do i = 1, nbound
   do j = 1, bound(i)%nbnodes
   read(1,*) bound(i)%bnode(j)
   end do
  end do

!  Print the boundary grid data.
   write(*,*) " Boundary nodes:"
   write(*,*) "    segments = ", nbound
    do i = 1, nbound
     write(*,'(a9,i3,2(a11,i5))') " boundary", i, "  bnodes = ", bound(i)%nbnodes, &
                                                  "  bfaces = ", bound(i)%nbnodes-1
    end do
   write(*,*)

  close(1)

! End of Read grid file>: datafile_grid_in
!--------------------------------------------------------------------------------

!--------------------------------------------------------------------------------
! 2. Read the boundary condition data file

   write(*,*)
   write(*,*) "Reading the boundary condition file....", datafile_bcmap_in
   write(*,*)

! Open the input file.
  open(unit=2, file=datafile_bcmap_in, status="unknown", iostat=os)

    read(2,*) 

! READ: Read the boundary condition type
  do i = 1, nbound
    read(2,*) dummy_int, bound(i)%bc_type
   end do

!  Print the data
    write(*,*) " Boundary conditions:"
   do i = 1, nbound
    write(*,'(a9,i3,a12,a35)') " boundary", i, "  bc_type = ", trim(bound(i)%bc_type)
   end do

    i = dummy_int !Never mind. Just to avoid a compilation warning.

    write(*,*)

  close(2)

! End of Read the boundary condition data file
!--------------------------------------------------------------------------------

 end subroutine read_grid

!********************************************************************************
!* Construct the grid data:
!*
!* The following data, needed for NCFV method, will be constructed based on the
!* data read from the grid file.
!*
!* 1. Element data:
!*    elm(:)%nnghbrs  = Number of element neighbors of each element
!*    elm(:)%nghbr(:) = List of element neighbors of each element
!*    elm(:)%x        = x-coordinate of the centroid
!*    elm(:)%y        = y-coordinate of the centroid
!*    elm(:)%vol      = Volume of the element
!*
!*
!* 2. Node data:
!*    node(:)%nnghbrs = Number of node neighbors of each node
!*    node(:)%nghbr(:)= List of node neighbors of each node
!*    node(:)%nelms   = Number of adjacent elements of each node
!*    node(:)%elm     = List of adjacent elements of each node
!*    node(:)%vol     = Volume of the dual volume around each node
!*
!* 3. Edge data:
!*    edge(:)%n1, n2  = End nodes of each edge (edge points n1 -> n2)
!*    edge(:)%e1, e2  = Left and right elements of each edge
!*    edge(:)%dav     = Unit directed area vector of each edge
!*    edge(:)%da      = Magnitude of the directed area vector for each edge
!*    edge(:)%ev      = Unit edge vector of each edge (vector n1 -> n2)
!*    edge(:)%e       = Magnitude of the edge vector for each edge
!*
!*
!* 4. Boudnary data
!*    bound(:)%bnx    = Outward normal at boundary nodes (x-component of unit vector)
!*    bound(:)%bny    = Outward normal at boundary nodes (y-component of unit vector)
!*    bound(:)%bn     = Magnitude of (bnx,bny)
!*    NOTE: In this code, the above normal vector at boundary nodes is computed by
!*          a quadratic fit. It is sufficiently accuarte for 3rd-order schemes.
!*          See http://www.hiroakinishikawa.com/My_papers/nishikawa_jcp2015v281pp518-555_preprint.pdf
!*          for details on the quadratic approximation for computing more accurate normals.
!*    bound(:)%bfnx   = Outward normal at boundary nodes (x-component of unit vector)
!*    bound(:)%bfny   = Outward normal at boundary nodes (y-component of unit vector)
!*    bound(:)%bfn    = Magnitude of (bfnx,bfny)
!*    bound(:)%belm   = Element to which the boundary face belongs
!*
!********************************************************************************
 subroutine construct_grid_data

 use edu2d_my_main_data , only : nnodes, node, nelms, elm, nedges, edge, nbound, bound, face, nfaces
 use edu2d_constants    , only : p2, zero, half, third
 use edu2d_my_allocation, only : my_alloc_int_ptr, my_alloc_p2_ptr, my_alloc_p2_matrix_ptr

 implicit none

!Local variables
 integer  ::  i, j, k, ii, in, im, jelm, v1, v2, v3, v4
 real(p2) :: x1, x2, x3, x4, y1, y2, y3, y4, xm, ym, xc, yc
 real(p2) :: xj, yj, xm1, ym1, xm2, ym2, dsL,dsR,dx,dy
 logical  :: found
 integer  :: vL, vR, n1, n2, e1, e2
 integer  :: vt1, vt2, ielm

 integer  :: ave_nghbr, min_nghbr, max_nghbr, imin, imax

 integer :: iedge

 real(p2)                          :: ds

! Some initialization
 v2 = 0
 vL = 0
 im = 0
 jelm = 0

  write(*,*) "Constructing grid data...."

! Initializations
  do i = 1, nnodes
   node(i)%nelms = 0
  end do
   nedges = 0

!--------------------------------------------------------------------------------
! Loop over elements and construct the fololowing data.
!
! 1. Surrounding elements: node(:)%nelms, node(:)%elm(:)
!
!    Example: Node i is surrounded by the eleemnts, 23, 101, 13, 41.
!             node(i)%nelms = 4
!             node(i)%elm(1) = 23
!             node(i)%elm(2) = 13
!             node(i)%elm(3) = 41
!             node(i)%elm(4) = 101
!
!        o-------o-------------o
!       /        |   .         |
!      /    23   |      41     |
!     o----------o-------------o
!      \        i \            |
!       \   101    \     13    |
!        \          \          | 
!         o----------o---------o
!
! 2. Element quantities  : elm(:)%x,elm(:)%y,elm(:)%vol
!
!  o-----------o            
!   \          |            o
!    \    (x,y)|           / \
!     \   .    |          /   \
!      \       |         /  .  \    (x,y): centroid coordinates
!       \      |        / (x,y) \     vol: volume of element
!        o-----o       o---------o

  elements : do i = 1, nelms

   v1 = elm(i)%vtx(1)
   v2 = elm(i)%vtx(2)
   v3 = elm(i)%vtx(3)

   x1 = node(v1)%x
   x2 = node(v2)%x
   x3 = node(v3)%x

   y1 = node(v1)%y
   y2 = node(v2)%y
   y3 = node(v3)%y

! Distribute the element index to nodes.

   node(v1)%nelms = node(v1)%nelms + 1
   call my_alloc_int_ptr(node(v1)%elm, node(v1)%nelms)
   node(v1)%elm(node(v1)%nelms) = i

   node(v2)%nelms = node(v2)%nelms + 1
   call my_alloc_int_ptr(node(v2)%elm, node(v2)%nelms)
   node(v2)%elm(node(v2)%nelms) = i

   node(v3)%nelms = node(v3)%nelms + 1
   call my_alloc_int_ptr(node(v3)%elm, node(v3)%nelms)
   node(v3)%elm(node(v3)%nelms) = i

! Compute the cell center and cell volume.
   tri_or_quad : if (elm(i)%nvtx==3) then

!   Triangle centroid and volume
    elm(i)%x   = third*(x1+x2+x3)
    elm(i)%y   = third*(y1+y2+y3)
    elm(i)%vol = tri_area(x1,x2,x3,y1,y2,y3)

   elseif (elm(i)%nvtx==4) then

!   OK, this is a quad. Get the 4th vertex.
    v4 = elm(i)%vtx(4)
    x4 = node(v4)%x
    y4 = node(v4)%y
!   Centroid: median dual
!   (Note: There is an alternative. See Appendix B in Nishikawa AIAA2010-5093.)
    xm1 = half*(x1+x2)
    ym1 = half*(y1+y2)
    xm2 = half*(x3+x4)
    ym2 = half*(y3+y4)
    elm(i)%x   = half*(xm1+xm2)
    elm(i)%y   = half*(ym1+ym2)
!   Volume is computed as a sum of two triangles: 1-2-3 and 1-3-4.
    elm(i)%vol = tri_area(x1,x2,x3,y1,y2,y3) + tri_area(x1,x3,x4,y1,y3,y4)

     xc = elm(i)%x
     yc = elm(i)%y
    if (tri_area(x1,x2,xc,y1,y2,yc)<zero) then
     write(*,*) " Centroid outside the quad element 12c: i=",i
     write(*,'(a10,2es10.2)') "  (x1,y1)=",x1,y1
     write(*,'(a10,2es10.2)') "  (x2,y2)=",x2,y2
     write(*,'(a10,2es10.2)') "  (x3,y3)=",x3,y3
     write(*,'(a10,2es10.2)') "  (x4,y4)=",x4,y4
     write(*,'(a10,2es10.2)') "  (xc,yc)=",xc,yc
     stop
    endif

    if (tri_area(x2,x3,xc,y2,y3,yc)<zero) then
     write(*,*) " Centroid outside the quad element 23c: i=",i
     write(*,'(a10,2es10.2)') "  (x1,y1)=",x1,y1
     write(*,'(a10,2es10.2)') "  (x2,y2)=",x2,y2
     write(*,'(a10,2es10.2)') "  (x3,y3)=",x3,y3
     write(*,'(a10,2es10.2)') "  (x4,y4)=",x4,y4
     write(*,'(a10,2es10.2)') "  (xc,yc)=",xc,yc
     stop
    endif

    if (tri_area(x3,x4,xc,y3,y4,yc)<zero) then
     write(*,*) " Centroid outside the quad element 34c: i=",i
     write(*,'(a10,2es10.2)') "  (x1,y1)=",x1,y1
     write(*,'(a10,2es10.2)') "  (x2,y2)=",x2,y2
     write(*,'(a10,2es10.2)') "  (x3,y3)=",x3,y3
     write(*,'(a10,2es10.2)') "  (x4,y4)=",x4,y4
     write(*,'(a10,2es10.2)') "  (xc,yc)=",xc,yc
     stop
    endif

    if (tri_area(x4,x1,xc,y4,y1,yc)<zero) then
     write(*,*) " Centroid outside the quad element 41c: i=",i
     write(*,'(a10,2es10.2)') "  (x1,y1)=",x1,y1
     write(*,'(a10,2es10.2)') "  (x2,y2)=",x2,y2
     write(*,'(a10,2es10.2)') "  (x3,y3)=",x3,y3
     write(*,'(a10,2es10.2)') "  (x4,y4)=",x4,y4
     write(*,'(a10,2es10.2)') "  (xc,yc)=",xc,yc
     stop
    endif

!  Distribution of element number to the 4th node of the quadrilateral
   node(v4)%nelms = node(v4)%nelms + 1
   call my_alloc_int_ptr(node(v4)%elm, node(v4)%nelms)
   node(v4)%elm(node(v4)%nelms) = i

   endif tri_or_quad

  end do elements

! Median dual volume

  do i = 1, nnodes
   node(i)%vol = zero
  end do

  elementsv : do i = 1, nelms

   v1 = elm(i)%vtx(1)
   v2 = elm(i)%vtx(2)
   v3 = elm(i)%vtx(3)

   tri_or_quadv : if (elm(i)%nvtx==3) then
!   Dual volume is exactly 1/3 of the volume of the triangle.
    node(v1)%vol = node(v1)%vol + third*elm(i)%vol
    node(v2)%vol = node(v2)%vol + third*elm(i)%vol
    node(v3)%vol = node(v3)%vol + third*elm(i)%vol

   elseif (elm(i)%nvtx==4) then
    v4 = elm(i)%vtx(4)

    x1 = node(v1)%x
    x2 = node(v2)%x
    x3 = node(v3)%x
    x4 = node(v4)%x
    xc = elm(i)%x

    y1 = node(v1)%y
    y2 = node(v2)%y
    y3 = node(v3)%y
    y4 = node(v4)%y
    yc = elm(i)%y

! - Vertex 1
     xj = node(v1)%x
     yj = node(v1)%y
    xm1 = half*(xj+x2)
    ym1 = half*(yj+y2)
    xm2 = half*(xj+x4)
    ym2 = half*(yj+y4)

!   Median volume is computed as a sum of two triangles.
    node(v1)%vol = node(v1)%vol + & 
                   tri_area(xj,xm1,xc,yj,ym1,yc) + tri_area(xj,xc,xm2,yj,yc,ym2)

! - Vertex 2
     xj = node(v2)%x
     yj = node(v2)%y
    xm1 = half*(xj+x3)
    ym1 = half*(yj+y3)
    xm2 = half*(xj+x1)
    ym2 = half*(yj+y1)

!   Median volume is computed as a sum of two triangles.
    node(v2)%vol = node(v2)%vol + &
                   tri_area(xj,xm1,xc,yj,ym1,yc) + tri_area(xj,xc,xm2,yj,yc,ym2)

! - Vertex 3
     xj = node(v3)%x
     yj = node(v3)%y
    xm1 = half*(xj+x4)
    ym1 = half*(yj+y4)
    xm2 = half*(xj+x2)
    ym2 = half*(yj+y2)

!   Median volume is computed as a sum of two triangles.
    node(v3)%vol = node(v3)%vol + &
                   tri_area(xj,xm1,xc,yj,ym1,yc) + tri_area(xj,xc,xm2,yj,yc,ym2)

! - Vertex 4
     xj = node(v4)%x
     yj = node(v4)%y
    xm1 = half*(xj+x1)
    ym1 = half*(yj+y1)
    xm2 = half*(xj+x3)
    ym2 = half*(yj+y3)

!   Median volume is computed as a sum of two triangles.
    node(v4)%vol = node(v4)%vol + &
                   tri_area(xj,xm1,xc,yj,ym1,yc) + tri_area(xj,xc,xm2,yj,yc,ym2)
 
   endif tri_or_quadv

  end do elementsv

!--------------------------------------------------------------------------------
! Loop over elements 2
!
!  Allocate elm(:)%nghbr(:) : elm(:)%nnghrs, elm(:)%nghr(:)
!  Construct element nghbr data: elm(:)%nghbr(:)
!  Order of neighbor elements [e1,e2,e3,..] are closely related to
!  the order of vertices [v1,v2,v3,..] (see below).
!
!          o------o
!          |      |                
!        v4|  e1  |v3                     v3
!    o-----o------o------o      o---------o------------o
!    |     |      |      |       .      .   .        .
!    | e2  |      |  e4  |        . e2 .     . e1  .
!    o-----o------o------o         .  .       .  .
!       v1 |     .v2              v1 o---------o v2   
!          | e3 .                     .   e3  .
!          |   .                        .    .
!          |  .                           . .
!          | .                             o
!          o
!

! Allocate the neighbor array

  do i = 1, nelms

!  3 neighbors for triangle
   if (elm(i)%nvtx==3) then

    elm(i)%nnghbrs = 3
    allocate(elm(i)%nghbr(3))

!  4 neighbors for quadrilateral
   elseif (elm(i)%nvtx==4) then

    elm(i)%nnghbrs = 4
    allocate(elm(i)%nghbr(4))

   endif

  end do

! Begin constructing the element-neighbor data

  elements2 : do i = 1, nelms

   elm_vertex : do k = 1, elm(i)%nvtx

!   Get the face of the element i:
!
!             vL      vR
!              o------o
!             /       |
!            /        |
!           o---------o
!
    if (k  < elm(i)%nvtx) vL = elm(i)%vtx(k+1)
    if (k == elm(i)%nvtx) vL = elm(i)%vtx(1)     
    vR = elm(i)%vtx(k)

!   Loop over the surrounding elements of the node vR,
!   and find the element neighbor from them.
    found = .false.
    elms_around_vR : do j = 1, node(vR)%nelms
    jelm = node(vR)%elm(j)

     edge_matching : do ii = 1, elm(jelm)%nvtx
                   v1 = elm(jelm)%vtx(ii)
      if (ii  > 1) v2 = elm(jelm)%vtx(ii-1)
      if (ii == 1) v2 = elm(jelm)%vtx(elm(jelm)%nvtx)

      if (v1==vR .and. v2==vL) then
       found = .true.
       im = ii+1
       if (im > elm(jelm)%nvtx) im = im - elm(jelm)%nvtx
       exit edge_matching
      endif
     end do edge_matching

     if (found) exit elms_around_vR

    end do elms_around_vR

     in = k + 2
     if (in > elm(i)%nvtx) in = in - elm(i)%nvtx

    if (found) then
     elm(   i)%nghbr(in) = jelm
     elm(jelm)%nghbr(im) = i
    else
     elm(   i)%nghbr(in) = 0
    endif

   end do elm_vertex

  end do elements2

!--------------------------------------------------------------------------------
! Edge-data for node-centered (edge-based) scheme.
!
! Loop over elements 3
! Construct edge data: edge(:)%n1, n2, e1, e2.
! Edge points from node n1 to node n2.
!
!      n2
!       o------------o
!     .  \         .
!    .    \   e2  .
!   .  e1  \    .
!  .        \ .         Directed area is positive: n1 -> n2
! o----------o         e1: left element
!             n1       e2: right element (e2 > e1 or e2 = 0)

! First count the number of edges.
!
! NOTE: Count edges only if the neighbor element number is
!       greater than the current element (i) to avoid double
!       count. Zero element number indicates that it is outside
!       the domain (boundary face).

  elements0 : do i = 1, nelms

   v1 = elm(i)%vtx(1)
   v2 = elm(i)%vtx(2)
   v3 = elm(i)%vtx(3)

   tri_quad0 : if (elm(i)%nvtx==3) then

    if ( elm(i)%nghbr(3) > i  .or. elm(i)%nghbr(3)==0 ) then
     nedges = nedges + 1
    endif

    if ( elm(i)%nghbr(1) > i .or. elm(i)%nghbr(1)==0 ) then
     nedges = nedges + 1
    endif

    if ( elm(i)%nghbr(2) > i .or. elm(i)%nghbr(2)==0 ) then
     nedges = nedges + 1
    endif

   elseif (elm(i)%nvtx==4) then

    v4 = elm(i)%vtx(4)

    if ( elm(i)%nghbr(3) > i .or. elm(i)%nghbr(3) ==0 ) then
     nedges = nedges + 1
    endif

    if ( elm(i)%nghbr(4) > i .or. elm(i)%nghbr(4) ==0 ) then
     nedges = nedges + 1
    endif

    if ( elm(i)%nghbr(1) > i .or. elm(i)%nghbr(1) ==0 ) then
     nedges = nedges + 1
    endif

    if ( elm(i)%nghbr(2) > i .or. elm(i)%nghbr(2) ==0 ) then
     nedges = nedges + 1
    endif

   endif tri_quad0

  end do elements0

! Allocate the edge array.
  allocate(edge(nedges))
  nedges = 0
  edge(:)%e1 = 0
  edge(:)%e2 = 0

! Construct the edge data:
!  two end nodes (n1, n2), and left and right elements (e1, e2)

  elements3 : do i = 1, nelms

   v1 = elm(i)%vtx(1)
   v2 = elm(i)%vtx(2)
   v3 = elm(i)%vtx(3)

! Triangular element
   tri_quad2 : if (elm(i)%nvtx==3) then

    if ( elm(i)%nghbr(3) > i  .or. elm(i)%nghbr(3)==0 ) then
     nedges = nedges + 1
     edge(nedges)%n1 = v1
     edge(nedges)%n2 = v2
     edge(nedges)%e1 = i
     edge(nedges)%e2 = elm(i)%nghbr(3)
    endif

    if ( elm(i)%nghbr(1) > i .or. elm(i)%nghbr(1)==0 ) then
     nedges = nedges + 1
     edge(nedges)%n1 = v2
     edge(nedges)%n2 = v3
     edge(nedges)%e1 = i
     edge(nedges)%e2 = elm(i)%nghbr(1)
    endif

    if ( elm(i)%nghbr(2) > i .or. elm(i)%nghbr(2)==0 ) then
     nedges = nedges + 1
     edge(nedges)%n1 = v3
     edge(nedges)%n2 = v1
     edge(nedges)%e1 = i
     edge(nedges)%e2 = elm(i)%nghbr(2)
    endif

!  Quadrilateral element
   elseif (elm(i)%nvtx==4) then

    v4 = elm(i)%vtx(4)

    if ( elm(i)%nghbr(3) > i .or. elm(i)%nghbr(3) ==0 ) then
     nedges = nedges + 1
     edge(nedges)%n1 = v1
     edge(nedges)%n2 = v2
     edge(nedges)%e1 = i
     edge(nedges)%e2 = elm(i)%nghbr(3)
    endif

    if ( elm(i)%nghbr(4) > i .or. elm(i)%nghbr(4) ==0 ) then
     nedges = nedges + 1
     edge(nedges)%n1 = v2
     edge(nedges)%n2 = v3
     edge(nedges)%e1 = i
     edge(nedges)%e2 = elm(i)%nghbr(4)
    endif

    if ( elm(i)%nghbr(1) > i .or. elm(i)%nghbr(1) ==0 ) then
     nedges = nedges + 1
     edge(nedges)%n1 = v3
     edge(nedges)%n2 = v4
     edge(nedges)%e1 = i
     edge(nedges)%e2 = elm(i)%nghbr(1)
    endif

    if ( elm(i)%nghbr(2) > i .or. elm(i)%nghbr(2) ==0 ) then
     nedges = nedges + 1
     edge(nedges)%n1 = v4
     edge(nedges)%n2 = v1
     edge(nedges)%e1 = i
     edge(nedges)%e2 = elm(i)%nghbr(2)
    endif

   endif tri_quad2

  end do elements3

! Loop over edges
! Construct edge vector and directed area vector.
!
! Edge vector is a simple vector pointing froom n1 to n2.
! For each edge, add the directed area vector (dav) from
! the left and right elements.
!
!              n2
!   o-----------o-----------o
!   |     dav   |  dav      |
!   |       ^   |   ^       |
!   |       |   |   |       |
!   |   c - - - m - - -c    |
!   |           |           |
!   |           |           |    m: edge midpoint
!   |           |           |    c: element centroid
!   o-----------o-----------o
!                n1
!
  edges : do i = 1, nedges

   n1 = edge(i)%n1
   n2 = edge(i)%n2
   e1 = edge(i)%e1
   e2 = edge(i)%e2
   xm = half*( node(n1)%x + node(n2)%x )
   ym = half*( node(n1)%y + node(n2)%y )

   edge(i)%dav = zero

! Contribution from the left element
  if (e1 > 0) then
   xc = elm(e1)%x
   yc = elm(e1)%y
   edge(i)%dav(1) = -(ym-yc)
   edge(i)%dav(2) =   xm-xc
  endif

! Contribution from the right element
  if (e2 > 0) then
   xc = elm(e2)%x
   yc = elm(e2)%y
   edge(i)%dav(1) = edge(i)%dav(1) -(yc-ym)
   edge(i)%dav(2) = edge(i)%dav(2) + xc-xm
  endif

  if (e1 < 0 .and. e2 < 0) then
   write(*,*) "!!!!! e1 and e2 are both negative... No way..."
  endif

! Magnitude and unit vector
   edge(i)%da  = sqrt( edge(i)%dav(1)**2 + edge(i)%dav(2)**2 )
   edge(i)%dav = edge(i)%dav / edge(i)%da

! Edge vector

  edge(i)%ev(1) = node(n2)%x - node(n1)%x
  edge(i)%ev(2) = node(n2)%y - node(n1)%y
  edge(i)%e     = sqrt( edge(i)%ev(1)**2 + edge(i)%ev(2)**2 )
  edge(i)%ev    = edge(i)%ev / edge(i)%e

  end do edges

!--------------------------------------------------------------------------------
! Construct node neighbor data:
!  pointers to the neighbor nodes(o)
!
!        o     o
!         \   / 
!          \ /
!     o-----*-----o
!          /|
!         / |
!        /  o        *: node in interest
!       o            o: neighbors (edge-connected nghbrs)
!

  do i = 1, nnodes
   node(i)%nnghbrs = 0
  end do

! Loop over edges and distribute the node numbers:

  edges4 : do i = 1, nedges

   n1 = edge(i)%n1
   n2 = edge(i)%n2

! (1) Add node1 to the neighbor list of n2
   node(n1)%nnghbrs = node(n1)%nnghbrs + 1
   call my_alloc_int_ptr(node(n1)%nghbr, node(n1)%nnghbrs)
   node(n1)%nghbr(node(n1)%nnghbrs) = n2

! (2) Add node2 to the neighbor list of n1
   node(n2)%nnghbrs = node(n2)%nnghbrs + 1
   call my_alloc_int_ptr(node(n2)%nghbr, node(n2)%nnghbrs)
   node(n2)%nghbr(node(n2)%nnghbrs) = n1

  end do edges4

!--------------------------------------------------------------------------------
! Boundary normal at nodes constructed by accumulating the contribution
! from each boundary face normal. This vector will be used to enforce
! the tangency condition, for example.
!
!
!        Interior domain      /
!                            o
!                  .        /
!                  .       /
! --o-------o-------------o
!           j   |  .  |   j+1
!               v  .  v
!
!        Left half added to the node j, and
!       right half added to the node j+1.
!

! Allocate and initialize the normal vector arrays
  do i = 1, nbound

   allocate(bound(i)%bnx(bound(i)%nbnodes))
   allocate(bound(i)%bny(bound(i)%nbnodes))
   allocate(bound(i)%bn( bound(i)%nbnodes))

   do j = 1, bound(i)%nbnodes
    bound(i)%bnx(j) = zero
    bound(i)%bny(j) = zero
    bound(i)%bn( j) = zero
   end do

  end do

! Normal vector at boundary nodes
! Note: Below it describes normals of linear approximation.
!       We will overwrite it by a quadratic approximation.
!
! Linear approximation:
!
! Step 1. Compute the outward normals
  do i = 1, nbound
   do j = 1, bound(i)%nbnodes-1

    x1 = node(bound(i)%bnode(j  ))%x
    y1 = node(bound(i)%bnode(j  ))%y

    x2 = node(bound(i)%bnode(j+1))%x
    y2 = node(bound(i)%bnode(j+1))%y

!   Normal vector pointing into the domain at this point.
    bound(i)%bnx(j) = bound(i)%bnx(j) + half*( -(y2-y1) )
    bound(i)%bny(j) = bound(i)%bny(j) + half*(   x2-x1  )

    bound(i)%bnx(j+1) = bound(i)%bnx(j+1) + half*( -(y2-y1) )
    bound(i)%bny(j+1) = bound(i)%bny(j+1) + half*(   x2-x1  )

   end do
  end do

! Step 2. Compute the magnitude and turn (bnx,bny) into a unit vector
  do i = 1, nbound
   do j = 1, bound(i)%nbnodes

    bound(i)%bn(j)  = sqrt( bound(i)%bnx(j)**2 + bound(i)%bny(j)**2 )
!   Minus sign to make it pont out towards the outside of the domain.
    bound(i)%bnx(j) =  - bound(i)%bnx(j) / bound(i)%bn(j)
    bound(i)%bny(j) =  - bound(i)%bny(j) / bound(i)%bn(j)

   end do
  end do

! Now, ignore the linear approximation, and let us construct
! more accurate surfae normal vectors and replace the linear ones.
! So, we will overwrite the unit normal vectors: bnx, bny.
! Note: We keep the magnitude of the normal vector.
!
! Quadratic approximation:
! See http://www.hiroakinishikawa.com/My_papers/nishikawa_jcp2015v281pp518-555_preprint.pdf
! for details on the quadratic approximation for computing more accurate normals.
! 
  boundary_type0 : do i = 1, nbound
   boundary_nodes0 : do j = 1, bound(i)%nbnodes

     if (j==1) then
      v1 = bound(i)%bnode(j  )
      v2 = bound(i)%bnode(j+1)
      v3 = bound(i)%bnode(j+2)
     elseif (j==bound(i)%nbnodes) then
      v1 = bound(i)%bnode(j-2)
      v2 = bound(i)%bnode(j-1)
      v3 = bound(i)%bnode(j  )
     else
      v1 = bound(i)%bnode(j-1)
      v2 = bound(i)%bnode(j)
      v3 = bound(i)%bnode(j+1)
     endif

     x1 = node(v1)%x
     x2 = node(v2)%x
     x3 = node(v3)%x

     y1 = node(v1)%y
     y2 = node(v2)%y
     y3 = node(v3)%y

!----------------------------------------------------------------------
!   Fit a quadratic over 3 nodes

!    Skip the last one if the boundary segment is a closed boundary 
!    in which case the last node is the same as the first one.
     if (j==bound(i)%nbnodes .and. bound(i)%bnode(j)==bound(i)%bnode(1) ) then
      bound(i)%bn(j)  = bound(i)%bn(1)
      bound(i)%bnx(j) = bound(i)%bnx(1)
      bound(i)%bny(j) = bound(i)%bny(1)
      cycle
     endif

     dsL = sqrt( (x2-x1)**2 + (y2-y1)**2 )
     dsR = sqrt( (x3-x2)**2 + (y3-y2)**2 )
      dx = dsR*x1/(dsL*(-dsL-dsR))-x2/dsR+x2/dsL+dsL*x3/((dsR+dsL)*dsR)
      dy = dsR*y1/(dsL*(-dsL-dsR))-y2/dsR+y2/dsL+dsL*y3/((dsR+dsL)*dsR)

     ds  = sqrt( dx**2 + dy**2 )
     bound(i)%bnx(j) = -( -dy / ds )
     bound(i)%bny(j) = -(  dx / ds )

   end do boundary_nodes0
  end do boundary_type0

!--------------------------------------------------------------------------------
! Construct neighbor index over edges
!
!  Example:
!
!        o     o
!         \   / 
!          \j/       k-th neighbor
!     o-----*----------o
!          /|  edge i
!         / |
!        /  o        Note: k-th neighbor is given by "node(j)%nghbr(k)"
!       o
!
!  Consider the edge i
!
!   node j        k-th neighbor
!       *----------o
!      n1  edge i  n2
!
!   We store "k" in the edge data structure as
!
!    edge(i)%kth_nghbr_of_1: n2 is the "edge(i)%kth_nghbr_of_1"-th neighbor of n1
!    edge(i)%kth_nghbr_of_2: n1 is the "edge(i)%kth_nghbr_of_3"-th neighbor of n2
!
!   That is,  we have
!
!    n2 = node(n1)%nghbr(edge(i)%kth_nghbr_of_1)
!    n1 = node(n2)%nghbr(edge(i)%kth_nghbr_of_2)
!
!   We make use of this data structure to access off-diagonal entries in Jacobian matrix.
!

! Loop over edges

  edges5 : do i = 1, nedges

   n1 = edge(i)%n1
   n2 = edge(i)%n2

   do k = 1, node(n2)%nnghbrs

    if ( n1 == node(n2)%nghbr(k) ) then
     edge(i)%kth_nghbr_of_2 = k
    endif

   end do

   do k = 1, node(n1)%nnghbrs

    if ( n2 == node(n1)%nghbr(k) ) then
     edge(i)%kth_nghbr_of_1 = k
    endif

   end do

  end do edges5

! Boundary mark: It should be an array actually because some nodes are associated with
!                more than one boundaries.
  do i = 1, nnodes
   node(i)%bmark   = 0
   node(i)%nbmarks = 0
  end do

  do i = 1, nbound
   do j = 1, bound(i)%nbnodes
    node( bound(i)%bnode(j) )%bmark   = i
    node( bound(i)%bnode(j) )%nbmarks = node( bound(i)%bnode(j) )%nbmarks + 1
   end do
  end do

!--------------------------------------------------------------------------------
! Boundary face data
!
!      |     Domain      |
!      |                 |
!      o--o--o--o--o--o--o  <- Boundary segment
!   j= 1  2  3  4  5  6  7
!
!   In the above case, nbnodes = 7, nbfaces = 6
!

  do i = 1, nbound
   bound(i)%nbfaces = bound(i)%nbnodes-1
   allocate(bound(i)%bfnx(    bound(i)%nbfaces   ))
   allocate(bound(i)%bfny(    bound(i)%nbfaces   ))
   allocate(bound(i)%bfn(     bound(i)%nbfaces   ))
   allocate(bound(i)%belm(    bound(i)%nbfaces   ))
   allocate(bound(i)%kth_nghbr_of_1(    bound(i)%nbfaces   ))
   allocate(bound(i)%kth_nghbr_of_2(    bound(i)%nbfaces   ))
  end do

! Boundary face vector: outward normal
  do i = 1, nbound
   do j = 1, bound(i)%nbfaces

    x1 = node(bound(i)%bnode(j  ))%x
    y1 = node(bound(i)%bnode(j  ))%y
    x2 = node(bound(i)%bnode(j+1))%x
    y2 = node(bound(i)%bnode(j+1))%y

    bound(i)%bfn(j)  =  sqrt( (x1-x2)**2 + (y1-y2)**2 )
    bound(i)%bfnx(j) = -(y1-y2) / bound(i)%bfn(j)
    bound(i)%bfny(j) =  (x1-x2) / bound(i)%bfn(j)

   end do
  end do

! Boundary normal vector at nodes: outward normal
  do i = 1, nbound
   do j = 1, bound(i)%nbfaces

    x1 = node(bound(i)%bnode(j  ))%x
    y1 = node(bound(i)%bnode(j  ))%y
    x2 = node(bound(i)%bnode(j+1))%x
    y2 = node(bound(i)%bnode(j+1))%y

    bound(i)%bfn(j)  =  sqrt( (x1-x2)**2 + (y1-y2)**2 )
    bound(i)%bfnx(j) = -(y1-y2) / bound(i)%bfn(j)
    bound(i)%bfny(j) =  (x1-x2) / bound(i)%bfn(j)

   end do
  end do

! Neighbor index over boundary edges (faces)

  do i = 1, nbound
   do j = 1, bound(i)%nbfaces

    n1 = bound(i)%bnode(j  )  !Left node
    n2 = bound(i)%bnode(j+1)  !Right node

    do k = 1, node(n2)%nnghbrs
     if ( n1 == node(n2)%nghbr(k) ) then
      bound(i)%kth_nghbr_of_2(j) = k
     endif
    end do

    do k = 1, node(n1)%nnghbrs
     if ( n2 == node(n1)%nghbr(k) ) then
      bound(i)%kth_nghbr_of_1(j) = k
     endif
    end do

   end do
  end do

! Find element adjacent to the face: belm
!
!  NOTE: This is useful to figure out what element
!        each boundary face belongs to. Boundary flux needs
!        special weighting depending on the element.
!
!      |_________|_________|________|
!      |         |         |        | 
!      |         |         |        | 
!      |_________|_________|________|
!      |         |         |        |     <- Grid (e.g., quads)
!      |         | elmb(j) |        |
!   ---o---------o---------o--------o---  <- Boundary segment
!                 j-th face
!
! elmb(j) is the element number of the element having the j-th boundary face.
!

  do i = 1, nbound
   do j = 1, bound(i)%nbfaces

!   bface is defined by the nodes v1 and v2.
    v1 = bound(i)%bnode(j  )
    v2 = bound(i)%bnode(j+1)

    found = .false.
!   Find the element having the bface from the elements
!   around the node v1.
    do k = 1, node(v1)%nelms
     ielm = node(v1)%elm(k)
     do ii = 1, elm(ielm)%nvtx
      in = ii
      im = ii+1
      if (im > elm(ielm)%nvtx) im = im - elm(ielm)%nvtx !return to 1
      vt1 = elm(ielm)%vtx(in)
      vt2 = elm(ielm)%vtx(im)
       if (vt1 == v1 .and. vt2 == v2) then
        found = .true.
        exit
       endif
     end do
     if (found) exit
    end do

    if (found) then
     bound(i)%belm(j) = ielm
    else
     write(*,*) " Boundary-adjacent element not found. Error..."
     stop
    endif

   end do
  end do

!--------------------------------------------------------------------------------
! Construct least-squares matrix for node-centered schemes.
!
!        o     o
!         \   / 
!          \ /
!     o-----*-----o
!          /|
!         / |
!        /  o        *: node in interest
!       o            o: neighbors (edge-connected nghbrs)
!

! Check the number of neighbor nodes (must have at least 2 neighbors)
  write(*,*) " --- Node neighbor data:"

  ave_nghbr = node(1)%nnghbrs
  min_nghbr = node(1)%nnghbrs
  max_nghbr = node(1)%nnghbrs
       imin = 1
       imax = 1
   if (node(1)%nnghbrs==2) then
    write(*,*) "--- 2 neighbors for the node = ", 1
   endif

  do i = 2, nnodes
   ave_nghbr = ave_nghbr + node(i)%nnghbrs
   if (node(i)%nnghbrs < min_nghbr) imin = i
   if (node(i)%nnghbrs > max_nghbr) imax = i
   min_nghbr = min(min_nghbr, node(i)%nnghbrs)
   max_nghbr = max(max_nghbr, node(i)%nnghbrs)
   if (node(i)%nnghbrs==2) then
    write(*,*) "--- 2 neighbors for the node = ", i
   endif
  end do

  write(*,*) "      ave_nghbr = ", ave_nghbr/nnodes
  write(*,*) "      min_nghbr = ", min_nghbr, " at node ", imin
  write(*,*) "      max_nghbr = ", max_nghbr, " at node ", imax
  write(*,*)

!--------------------------------------------------------------------------------
! Cell centered scheme data
!--------------------------------------------------------------------------------

  write(*,*) "Generating CC scheme data......"

  do i = 1, nelms   
   allocate(elm(i)%edge( elm(i)%nnghbrs ) )
  end do

  edges3 : do i = 1, nedges

   e1 = edge(i)%e1
   e2 = edge(i)%e2

! Left element
  if (e1 > 0) then
   do k = 1, elm(e1)%nnghbrs
    if (elm(e1)%nghbr(k)==e2) elm(e1)%edge(k) = i
   end do
  endif

! Right element
  if (e2 > 0) then
   do k = 1, elm(e2)%nnghbrs
    if (elm(e2)%nghbr(k)==e1) elm(e2)%edge(k) = i
   end do
  endif

  end do edges3

! Face-data for cell-centered (edge-based) scheme.
!
! Loop over elements 4
! Construct face data:
! face is an edge across elements pointing
! element e1 to element e2 (e2 > e1):
!
!       e2
!        \    
!         \ face: e1 -> e2 
!          \
!  n1 o--------------o n2 <-- face
!            \
!             \          n1, n2: end nodes of the face
!              \         e1: element 1
!              e1        e2: element 2  (e2 > e1)
!
! Note: Face data is dual to the edge data.
!       It can be trivially constructed from the edge data, but
!       here the face data is constructed by using the element
!       neighbor data just for an educational purpose.

  nfaces = 0
  elements4 : do i = 1, nelms
   do k = 1, elm(i)%nnghbrs
   jelm = elm(i)%nghbr(k)
    if (jelm > i) then
     nfaces = nfaces + 1
    endif
   end do
  end do elements4

  allocate(face(nfaces))

  nfaces = 0

  elements5 : do i = 1, nelms
   do k = 1, elm(i)%nnghbrs
   jelm = elm(i)%nghbr(k)

    if (jelm > i) then

     nfaces = nfaces + 1

     face(nfaces)%e1 = i
     face(nfaces)%e2 = jelm

     iedge = elm(i)%edge(k)
     v1 = edge(iedge)%n1
     v2 = edge(iedge)%n2

     if (edge(iedge)%e1 == jelm) then
      face(nfaces)%n1 = v1
      face(nfaces)%n2 = v2
     else
      face(nfaces)%n1 = v2
      face(nfaces)%n2 = v1
     endif
   
    elseif (jelm == 0) then
!    Skip boundary faces.
    endif

   end do
  end do elements5

! Loop over faces
! Construct directed area vector.

  faces : do i = 1, nfaces

   n1 = face(i)%n1
   n2 = face(i)%n2
   e1 = face(i)%e1
   e2 = face(i)%e2

! Face vector
  face(i)%dav(1) = -( node(n2)%y - node(n1)%y )
  face(i)%dav(2) =    node(n2)%x - node(n1)%x
  face(i)%da     = sqrt( face(i)%dav(1)**2 + face(i)%dav(2)**2 )
  face(i)%dav    = face(i)%dav / face(i)%da

  end do faces

! Construct vertex-neighbor data for cell-centered scheme.
!
! For each element, i, collect all elements sharing the nodes
! of the element, i, including face-neighors.
!
!      ___________
!     |     |     |
!     |  o  |  o  |
!     |_____|_____|
!    /\    / \    \
!   / o\ o/ i \  o \
!  /____\/_____\____\
!  \    /      /\    \
!   \o /  o   / o\ o  \
!    \/______/____\____\
!
!          i: Element of interest
!          o: Vertex neighbors (k = 1,2,...,9)

  write(*,*) " --- Vertex-neighbor data:"

  do i = 1, nelms
   elm(i)%nvnghbrs = 1
   call my_alloc_int_ptr(elm(i)%vnghbr, 1)
  end do

  ave_nghbr = 0
  min_nghbr = 10000
  max_nghbr =-10000
       imin = 1
       imax = 1

! Initialization
  elements6 : do i = 1, nelms
   elm(i)%nvnghbrs = 0
  end do elements6

! Collect vertex-neighbors
  elements7 : do i = 1, nelms

! (1)Add face-neighbors
   do k = 1, elm(i)%nnghbrs
    if ( elm(i)%nghbr(k) > 0 ) then
     elm(i)%nvnghbrs = elm(i)%nvnghbrs + 1
     call my_alloc_int_ptr(elm(i)%vnghbr, elm(i)%nvnghbrs)
     elm(i)%vnghbr(elm(i)%nvnghbrs) = elm(i)%nghbr(k)
    endif
   end do

! (2)Add vertex-neighbors
   do k = 1, elm(i)%nvtx
    v1 = elm(i)%vtx(k)

    velms : do j = 1, node(v1)%nelms
     e1 = node(v1)%elm(j)
     if (e1 == i) cycle velms

!    Check if the element is already added.
       found = .false.
     do ii = 1, elm(i)%nvnghbrs
      if ( e1 == elm(i)%vnghbr(ii) ) then
       found = .true.
       exit
      endif
     end do

!    Add the element, e1, if not added yet.
     if (.not.found) then
      elm(i)%nvnghbrs = elm(i)%nvnghbrs + 1
      call my_alloc_int_ptr(elm(i)%vnghbr, elm(i)%nvnghbrs)
      elm(i)%vnghbr(elm(i)%nvnghbrs) = e1
     endif
    end do velms

   end do

   ave_nghbr = ave_nghbr + elm(i)%nvnghbrs
   if (elm(i)%nvnghbrs < min_nghbr) imin = i
   if (elm(i)%nvnghbrs > max_nghbr) imax = i
   min_nghbr = min(min_nghbr, elm(i)%nvnghbrs)
   max_nghbr = max(max_nghbr, elm(i)%nvnghbrs)
   if (elm(i)%nvnghbrs < 3) then
    write(*,*) "--- Not enough neighbors: elm = ", i, &
               "elm(i)%nvnghbrs=",elm(i)%nvnghbrs
   endif

  end do elements7

  write(*,*) "      ave_nghbr = ", ave_nghbr/nelms
  write(*,*) "      min_nghbr = ", min_nghbr, " elm = ", imin
  write(*,*) "      max_nghbr = ", max_nghbr, " elm = ", imax
  write(*,*)


  do i = 1, nelms
   elm(i)%bmark = 0
  end do

  bc_loop : do i = 1, nbound
   if (trim(bound(i)%bc_type) == "dirichlet") then
    do j = 1, bound(i)%nbfaces
     elm( bound(i)%belm(j) )%bmark = 1
    end do
   endif
  end do bc_loop

!--------------------------------------------------------------------------------

 return

 end subroutine construct_grid_data

!********************************************************************************

!********************************************************************************
!* Compute the area of the triangle defined by the nodes, 1, 2, 3.
!*
!*              3 (x3,y3)
!*              o 
!*             / \ 
!*            /   \
!* (x1,y1) 1 o-----o 2 (x2,y2)
!*
!* Nodes must be ordered counterclockwise (otherwise it gives negative area)
!*
!********************************************************************************
 function tri_area(x1,x2,x3,y1,y2,y3) result(area)
 use edu2d_constants, only : p2, half
 implicit none
 real(p2), intent(in) :: x1,x2,x3,y1,y2,y3
 real(p2) :: area

  area = half*( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )

 end function tri_area


!********************************************************************************
!* Check the grid data.
!*
!* 1. Directed area must sum up to zero around every node.
!* 2. Directed area must sum up to zero over the entire grid.
!* 3. Global sum of the boundary normal vectors must vanish.
!* 4. Global sum of the boundary face normal vectors must vanish.
!* 5. Check element volumes which must be positive.
!* 6. Check dual volumes which must be positive.
!* 7. Global sum of the dual volumes must be equal to the sum of element volumes.
!*
!* Add more tests you can think of.
!*
!********************************************************************************
 subroutine check_grid_data

 use edu2d_my_main_data  , only : nnodes, node,  nelms,   elm, nedges, edge, &
                            nbound, bound
 use edu2d_constants     , only : p2, zero, half

 implicit none
!Local variables
 integer  :: i, j, n1, n2, ierr, k
 real(p2), dimension(nnodes,2) :: sum_dav_i
 real(p2), dimension(2) :: sum_dav, sum_bn
 real(p2), dimension(2) :: sum_bfn
 real(p2)               :: sum_volc, sum_vol
 real(p2)               :: mag_dav, mag_bn
 real(p2)               :: vol_min, vol_max, vol_ave

  write(*,*) "Checking grid data...."

  mag_dav = zero
  mag_bn  = zero

!--------------------------------------------------------------------------------
! Directed area sum check
!--------------------------------------------------------------------------------

! Compute the sum of the directed area for each node.

   sum_dav_i = zero
  do i = 1, nedges
   n1 = edge(i)%n1
   n2 = edge(i)%n2
   sum_dav_i(n1,:) = sum_dav_i(n1,:) + edge(i)%dav(:)*edge(i)%da
   sum_dav_i(n2,:) = sum_dav_i(n2,:) - edge(i)%dav(:)*edge(i)%da
   mag_dav = mag_dav + edge(i)%da
  end do
   mag_dav = mag_dav/real(nedges,p2)

! Add contribution from boundary edges.
  do i = 1, nbound
   do j = 1, bound(i)%nbfaces

     n1 = bound(i)%bnode(j)
     n2 = bound(i)%bnode(j+1)

     sum_dav_i(n1,1) = sum_dav_i(n1,1) + half*bound(i)%bfnx(j)*bound(i)%bfn(j)
     sum_dav_i(n1,2) = sum_dav_i(n1,2) + half*bound(i)%bfny(j)*bound(i)%bfn(j)

     sum_dav_i(n2,1) = sum_dav_i(n2,1) + half*bound(i)%bfnx(j)*bound(i)%bfn(j)
     sum_dav_i(n2,2) = sum_dav_i(n2,2) + half*bound(i)%bfny(j)*bound(i)%bfn(j)

   end do
  end do

! Compute also the sum of the boundary normal vector (at nodes).

  sum_bn = 0
  do i = 1, nbound
   do j = 1, bound(i)%nbnodes
     k = bound(i)%bnode(j)
     if (j > 1 .and. k==bound(i)%bnode(1)) cycle !Skip if the last node is equal to the first node).
    sum_bn(1)      = sum_bn(1)      + bound(i)%bnx(j)*bound(i)%bn(j)
    sum_bn(2)      = sum_bn(2)      + bound(i)%bny(j)*bound(i)%bn(j)
    mag_bn = mag_bn + abs(bound(i)%bn(j))
   end do
    mag_bn = mag_bn/real(bound(i)%nbnodes,p2)
  end do

! Global sum of boundary normal vectors must vanish.

!  if (sum_bn(1) > 1.0e-12_p2*mag_bn .and. sum_bn(2) > 1.0e-12_p2*mag_bn) then
!   write(*,*) "--- Global sum of the boundary normal vector:"
!   write(*,'(a19,es10.3)') "    sum of bn_x = ", sum_bn(1)
!   write(*,'(a19,es10.3)') "    sum of bn_y = ", sum_bn(2)
!   write(*,*) "Error: boundary normal vectors do not sum to zero..."
!   stop
!  endif

! Sum of the directed area vectors must vanish at every node.

  do i = 1, nnodes
   if (abs(sum_dav_i(i,1))>1.0e-12_p2*mag_dav .or. abs(sum_dav_i(i,2))>1.0e-12_p2*mag_dav) then
   write(*,'(a11,i5,a7,2es10.3,a9,2es10.3)') &
    " --- node=", i, " (x,y)=", node(i)%x, node(i)%y, " sum_dav=",sum_dav_i(i,:)
   endif
  end do

   write(*,*) "--- Max sum of directed area vector around a node:"
   write(*,*) "  max(sum_dav_i_x) = ", maxval(sum_dav_i(:,1))
   write(*,*) "  max(sum_dav_i_y) = ", maxval(sum_dav_i(:,2))

  if (maxval(abs(sum_dav_i(:,1)))>1.0e-12_p2*mag_dav .or. &
      maxval(abs(sum_dav_i(:,2)))>1.0e-12_p2*mag_dav) then
   write(*,*) "--- Max sum of directed area vector around a node:"
   write(*,*) "  max(sum_dav_i_x) = ", maxval(sum_dav_i(:,1))
   write(*,*) "  max(sum_dav_i_y) = ", maxval(sum_dav_i(:,2))
   write(*,*) "Error: directed area vectors do not sum to zero..."
   stop
  endif

! Of course, the global sum of the directed area vector sum must vanish.
   sum_dav = zero
  do i = 1, nnodes
   sum_dav = sum_dav + sum_dav_i(i,:)
  end do

   write(*,*) "--- Global sum of the directed area vector:"
   write(*,'(a19,es10.3)') "    sum of dav_x = ", sum_dav(1)
   write(*,'(a19,es10.3)') "    sum of dav_y = ", sum_dav(2)

  if (sum_dav(1) > 1.0e-12_p2*mag_dav .and. sum_dav(2) > 1.0e-12_p2*mag_dav) then
   write(*,*) "Error: directed area vectors do not sum globally to zero..."
   write(*,*) "--- Global sum of the directed area vector:"
   write(*,'(a19,es10.3)') "    sum of dav_x = ", sum_dav(1)
   write(*,'(a19,es10.3)') "    sum of dav_y = ", sum_dav(2)
   stop
  endif

!--------------------------------------------------------------------------------
! Global sum check for boundary face vector
!--------------------------------------------------------------------------------
  sum_bfn = 0
  do i = 1, nbound
   do j = 1, bound(i)%nbfaces
     sum_bfn(1) =  sum_bfn(1) + bound(i)%bfnx(j)*bound(i)%bfn(j)
     sum_bfn(2) =  sum_bfn(2) + bound(i)%bfny(j)*bound(i)%bfn(j)
   end do
  end do

   write(*,*) "--- Global sum of the boundary face vector:"
   write(*,'(a19,es10.3)') "    sum of bfn_x = ", sum_bfn(1)
   write(*,'(a19,es10.3)') "    sum of bfn_y = ", sum_bfn(2)

  if (sum_bfn(1) > 1.0e-12_p2*mag_bn .and. sum_bfn(2) > 1.0e-12_p2*mag_bn) then
   write(*,*) "Error: boundary face normals do not sum globally to zero..."
   write(*,*) "--- Global sum of the boundary face normal vector:"
   write(*,'(a19,es10.3)') "    sum of bfn_x = ", sum_bfn(1)
   write(*,'(a19,es10.3)') "    sum of bfn_y = ", sum_bfn(2)
   stop
  endif

!--------------------------------------------------------------------------------
! Volume check
!--------------------------------------------------------------------------------
! (1)Check the element volume: make sure there are no zero or negative volumes

   vol_min =  1.0e+15
   vol_max = -1.0
   vol_ave =  zero

       ierr = 0
   sum_volc = zero
  do i = 1, nelms

      vol_min = min(vol_min,elm(i)%vol)
      vol_max = max(vol_max,elm(i)%vol)
      vol_ave = vol_ave + elm(i)%vol

   sum_volc = sum_volc + elm(i)%vol

   if (elm(i)%vol < zero) then
     write(*,*) "Negative volc=",elm(i)%vol, " elm=",i, " stop..."
     ierr = ierr + 1
   endif

   if (abs(elm(i)%vol) < 1.0e-14_p2) then
     write(*,*) "Vanishing volc=",elm(i)%vol, " elm=",i, " stop..."
     ierr = ierr + 1
   endif

  end do

   vol_ave = vol_ave / real(nelms)

   write(*,*)
   write(*,'(a30,es25.15)') "    minimum element volume = ", vol_min
   write(*,'(a30,es25.15)') "    maximum element volume = ", vol_max
   write(*,'(a30,es25.15)') "    average element volume = ", vol_ave
   write(*,*)

!--------------------------------------------------------------------------------
! (2)Check the dual volume (volume around a node)

   vol_min =  1.0e+15
   vol_max = -1.0
   vol_ave =  zero

      ierr = 0
   sum_vol = zero
  do i = 1, nnodes

      vol_min = min(vol_min,node(i)%vol)
      vol_max = max(vol_max,node(i)%vol)
      vol_ave = vol_ave + node(i)%vol

   sum_vol = sum_vol + node(i)%vol

   if (node(i)%vol < zero) then
     write(*,*) "Negative vol=",node(i)%vol, " node=",i, " stop..."
     ierr = ierr + 1
   endif

   if (abs(node(i)%vol) < 1.0e-14_p2) then
     write(*,*) "Vanishing vol=",node(i)%vol, " node=",i, " stop..."
     ierr = ierr + 1
   endif

  end do

   vol_ave = vol_ave / real(nnodes)

   write(*,*)
   write(*,'(a30,es25.15)') "    minimum dual volume = ", vol_min
   write(*,'(a30,es25.15)') "    maximum dual volume = ", vol_max
   write(*,'(a30,es25.15)') "    average dual volume = ", vol_ave
   write(*,*)


  if (ierr > 0) stop

  if (abs(sum_vol-sum_volc) > 1.0e-08_p2*sum_vol) then
   write(*,*) "--- Global sum of volume: must be the same"
   write(*,'(a19,es10.3)') "    sum of volc = ", sum_volc
   write(*,'(a19,es10.3)') "    sum of vol  = ", sum_vol
   write(*,'(a22,es10.3)') " sum_vol-sum_volc  = ", sum_vol-sum_volc
   write(*,*) "Error: sum of dual volumes and cell volumes do not match..."
   stop
  endif

  call check_skewness_nc
  call compute_ar

  write(*,*)
  write(*,*) "Grid data look good!"

 end subroutine check_grid_data

!*******************************************************************************
!* Skewness computation for edges.
!*******************************************************************************
 subroutine check_skewness_nc
 use edu2d_my_main_data  , only : nedges, edge
 use edu2d_constants     , only : p2, zero

 implicit none
 integer :: i
 real(p2) :: e_dot_n, e_dot_n_min, e_dot_n_max, alpha

     e_dot_n = zero
 e_dot_n_min = 100000.0_p2
 e_dot_n_max =-100000.0_p2

  edges : do i = 1, nedges

   alpha = edge(i)%ev(1)*edge(i)%dav(1) + edge(i)%ev(2)*edge(i)%dav(2)
   e_dot_n     = e_dot_n + abs(alpha)
   e_dot_n_min = min(e_dot_n_min, abs(alpha))
   e_dot_n_max = max(e_dot_n_max, abs(alpha))

  end do edges

  e_dot_n = e_dot_n / real(nedges,p2)

 write(*,*)
 write(*,*) " ------ Skewness check (NC control volume) ----------"
 write(*,*) "   L1(e_dot_n) = ", e_dot_n
 write(*,*) "  Min(e_dot_n) = ", e_dot_n_min
 write(*,*) "  Max(e_dot_n) = ", e_dot_n_max
 write(*,*) " ----------------------------------------------------"

 end subroutine check_skewness_nc


!*******************************************************************************
!* Control volume aspect ratio
!*******************************************************************************
 subroutine compute_ar
 use edu2d_my_main_data  , only : node, nnodes, elm, nelms
 use edu2d_constants     , only : p2, zero, one, half, two

 implicit none
 integer :: i, n1, n2
 real(p2) :: ar, ar_min, ar_max, nnodes_eff

 integer  :: k
 real(p2) :: side_max, side(4), side_mid, side_min, height

! Initialization

  node1 : do i = 1, nnodes
   node(i)%ar     = zero
  end do node1

! Compute element aspect-ratio: longest_side^2 / vol

  elm1: do i = 1, nelms

   side_max = -one
   
   do k = 1, elm(i)%nvtx

     n1 = elm(i)%vtx(k)
    if (k == elm(i)%nvtx) then
     n2 = elm(i)%vtx(1)
    else
     n2 = elm(i)%vtx(k+1)
    endif

     side(k) = sqrt( (node(n2)%x-node(n1)%x)**2 + (node(n2)%y-node(n1)%y)**2 )
    side_max =  max(side_max, side(k))

   end do

   if (elm(i)%nvtx == 3) then

 ! AR for triangle:  Ratio of a half of a square with side_max to volume
    elm(i)%ar = (half*side_max**2) / elm(i)%vol

    if     (side(1) >= side(2) .and. side(1) >= side(3)) then

       side_max = side(1)
      if (side(2) >= side(3)) then
       side_mid = side(2); side_min = side(3)
      else
       side_mid = side(3); side_min = side(2)
      endif

    elseif (side(2) >= side(1) .and. side(2) >= side(3)) then

       side_max = side(2)
      if (side(1) >= side(3)) then
       side_mid = side(1); side_min = side(3)
      else
       side_mid = side(3); side_min = side(1)
      endif

    else

       side_max = side(3)
      if (side(1) >= side(2)) then
       side_mid = side(1); side_min = side(2)
      else
       side_mid = side(2); side_min = side(1)
      endif

    endif

       height = two*elm(i)%vol/side_mid
    elm(i)%ar = side_mid/height

   else

  ! AR for quad: Ratio of a square with side_max to volume
    elm(i)%ar = side_max**2 / elm(i)%vol

   endif

  end do elm1

! Compute the aspect ratio:
  node2 : do i = 1, nnodes

    node(i)%ar = zero
   do k = 1, node(i)%nelms
    node(i)%ar = node(i)%ar + elm(node(i)%elm(k))%ar
   end do

    node(i)%ar = node(i)%ar / real(node(i)%nelms, p2)

  end do node2

! Compute the min/max and L1 of AR

  nnodes_eff= zero
         ar = zero
     ar_min = 100000.0_p2
     ar_max =-100000.0_p2

  node3: do i = 1, nnodes
   if (node(i)%bmark /= 0) cycle node3
   ar     = ar + abs(node(i)%ar)
   ar_min = min(ar_min, abs(node(i)%ar))
   ar_max = max(ar_max, abs(node(i)%ar))
   nnodes_eff = nnodes_eff + one
  end do node3

  ar = ar / nnodes_eff

 write(*,*)
 write(*,*) " ------ Aspect ratio check (NC control volume) ----------"
 write(*,*) " Interior nodes only"
 write(*,*) "   L1(AR) = ", ar
 write(*,*) "  Min(AR) = ", ar_min
 write(*,*) "  Max(AR) = ", ar_max

  nnodes_eff= zero
         ar = zero
     ar_min = 100000.0_p2
     ar_max =-100000.0_p2

  node4: do i = 1, nnodes
   if (node(i)%bmark == 0) cycle node4
   ar     = ar + abs(node(i)%ar)
   ar_min = min(ar_min, abs(node(i)%ar))
   ar_max = max(ar_max, abs(node(i)%ar))
   nnodes_eff = nnodes_eff + one
  end do node4

  ar = ar / nnodes_eff

 write(*,*)
 write(*,*) " Boundary nodes only"
 write(*,*) "   L1(AR) = ", ar
 write(*,*) "  Min(AR) = ", ar_min
 write(*,*) "  Max(AR) = ", ar_max
 write(*,*) " --------------------------------------------------------"

 end subroutine compute_ar



 end module edu2d_grid_data

