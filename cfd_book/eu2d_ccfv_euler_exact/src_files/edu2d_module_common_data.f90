!********************************************************************************
! Educationally-Designed Unstructured 2D (EDU2D) Code
!
!  ---------------- EDU2D-CCFV-Euler-LVL0
!
!  - Common data module
!
! This module containes grid, solution, and other data used throughout
! the whole program. These data are accessed by the use statement.
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

 module module_common_data

  implicit none

 !This module contains the following subroutines:
 ! - set_filenames
 ! - read_grid

 !Everything is in public and accessible by other modules.
  public


 !--------------------------------------------------------------------
 ! Constants

  integer , parameter :: p2 = selected_real_kind(P=15) !Double precision
  real(p2), parameter ::   zero = 0.0_p2
  real(p2), parameter ::   half = 0.5_p2
  real(p2), parameter ::    one = 1.0_p2
  real(p2), parameter ::    two = 2.0_p2
  real(p2), parameter ::  three = 3.0_p2
  real(p2), parameter ::   four = 4.0_p2
  real(p2), parameter ::   five = 5.0_p2
  real(p2), parameter ::  third = 1.0_p2/3.0_p2
  real(p2), parameter :: fourth = 1.0_p2/4.0_p2
  real(p2), parameter ::  sixth = 1.0_p2/6.0_p2
  real(p2), parameter :: my_eps = epsilon(one)  !Machine zero w.r.t. 1.0.

  real(p2), parameter :: pi = 3.141592653589793238_p2

  integer             :: ix = 1, iy = 2

 !--------------------------------------------------------------------
 !--------------------------------------------------------------------
 ! File names

  character(80) :: filename_grid         ! input grid filename (.ugrid)
  character(80) :: filename_bc           ! input bc   filename (.bc)
  character(80) :: filename_tecplot      ! output tecplot volume filename (.dat)
  character(80) :: filename_vtk          ! output .vtk volume filename (.vtk)
  character(80) :: filename_tec_hist     ! output tecplot history filename (.dat)

 !--------------------------------------------------------------------
 ! Data used to read a grid file and a BC file.

  !------------------------------------------
  !>> Node data
  integer                             :: nnodes
  real(p2), dimension(:  )  , pointer :: x, y

  !------------------------------------------
  !>> Boundary element data
   integer                              :: nb      !# of boundary segments
   integer      , dimension(:), pointer :: nbnodes !# of boundary nodes
   integer      , dimension(:), pointer ::  bnode  !List of boundary nodes
   character(80), dimension(:), pointer :: bc_type !type of boundary condition

  !------------------------------------------
  !>> Element conenctivity data

  !>> Triangular element data
  integer                           :: ntria !# of triangles
  integer , dimension(:,:), pointer ::  tria !List of vertices

  !>> Quadrilateral element data
  integer                           :: nquad !# of quadrilaterals
  integer , dimension(:,:), pointer ::  quad !List of vertices


  !Note: These variables are available within the entire module, and within
  !      so all subroutines contained below.

 contains

!********************************************************************************
!
! Define file names.
!
! Note: Actual filename character variables are defined in "module_common_data".
!       We access them by the "use" statement and assign the names here.
!
!********************************************************************************
 subroutine set_filenames

 !To access a user defined character "project_name"
  use module_input_parameter       , only : project_name

  implicit none

  write(*,*)
  write(*,*) "-------------------------------------------------------"
  write(*,*) " Setting up file names..... "
  write(*,*)

 !-----------------------------------------------------------------------
 ! Input grid file (.ugrid):
 ! E.g., filename_grid = "test.grid" if project_name = "test".

       filename_grid   = trim(project_name) // '.grid'

       write(*,'(a28,a28)') "   filename_grid = ", trim(filename_grid)

 !-----------------------------------------------------------------------
 ! Input boundary condition file (ASCII file)
 ! E.g., filename_bc = "test.bc" if project_name = "test".

      filename_bc   = trim(project_name) // '.bc'

       write(*,'(a28,a28)') "   filename_bc = ", trim(filename_bc)

 !-----------------------------------------------------------------------
 ! Output: Tecplot file (ASCII file)
 ! E.g., filename_tecplot = "test_tec.dat" if project_name = "test".

      filename_tecplot = trim(project_name) // '_tec.dat'

       write(*,'(a28,a28)') "   filename_tecplot = ", trim(filename_tecplot)

 !-----------------------------------------------------------------------
 ! Output: .vtk file (ASCII file)
 ! E.g., filename_tecplot = "test_tec.dat" if project_name = "test".

      filename_vtk = trim(project_name) // '.vtk'

       write(*,'(a28,a28)') "   filename_vtk = ", trim(filename_vtk)

 !-----------------------------------------------------------------------
 ! Output: Tecplot file (ASCII file)
 ! E.g., filename_tecplot = "test_tec.dat" if project_name = "test".

      filename_tec_hist = trim(project_name) // '_tec_hist.dat'

       write(*,'(a28,a28)') "   filename_tec_hist = ", trim(filename_tec_hist)

 !-----------------------------------------------------------------------

  write(*,*)
  write(*,*) " End of Setting up file names..... "
  write(*,*) "-------------------------------------------------------"
  write(*,*)

 end subroutine set_filenames

!********************************************************************************
!
! Read the grid, "project_name".grid file written in a custom format
! as explained below.
!
! ------------------------------------------------------------------------------
!  Input: filename_grid  = filename of the grid file
!
! Output: nnodes       !# of nodes
!         x, y         !nodal coords
!         ntria, tria  !# of triangles and triangle list
!         nquad, quad  !# of quads and quad list
!         nb           !# of boundaries (i.e., BCs)
!         nbnodes      !# of boundary nodes
!         nbnode       !list of boundary nodes
! ------------------------------------------------------------------------------
!
!*******************************************************************************
! 1. "filename_grid" is assumed to have been written in the following format:
!
!   -----------------------------------------------------------------------
!     write(*,*) nnodes, ntria, nquad !Numbers of nodes, triangles and quads
!
!    do i = 1, nnodes
!     write(*,*) x(i), y(i) !(x,y) coordinates of each node
!    end do
!
!    do i = 1, ntria        !Nodes of triangles ordered counterclockwise
!     write(*,*) node_1(i), node_2(i), node_3(i)
!    end do
!
!    do i = 1, nquad        !Nodes of quadrilaterals ordered counterclockwise
!     write(*,*) node_1(i), node_2(i), node_3(i), node_4(i)
!    end do
! 
!     write(*,*) nbound     !Number of boundary segments
!
!    do i = 1, nbound
!     write(*,*) nbnodes(i) !Number of nodes on each segment
!    end do
!
!    do i = 1, nbound
!     do j = 1, nbnodes(i)
!      write(*,*) bnode(j)  !Node number of each node j in segment i
!     end do
!    end do
!   -----------------------------------------------------------------------
!
!   NOTE: Add the first node to the end if the segment is closed
!         (e.g., airfoil) The number of nodes will be the actual number + 1
!         in that case.
!
!   NOTE: Boundary nodes must be ordered such that the domain is on the left.
!
!********************************************************************************
 subroutine read_grid

!To make no assumption for all the variables defined below. Write it always.
!(If not stated, for example, fortran90 will assume i,j,k will be integer.)

 implicit none

!Local variables

 integer  :: i, j, os, total_bnodes, dummy_int

  write(*,*)
  write(*,*) "-------------------------------------------------------"
  write(*,*) " Reading : ", trim(filename_grid), "  ", trim(filename_bc)
  write(*,*)

!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
! 1. Read the grid file.

!  Open the input file.

   open(unit=1, file=filename_grid, status="unknown", iostat=os)

! READ: Get the size of the grid.

  read(1,*) nnodes, ntria, nquad

  ! Write out the grid data.

   write(*,*) " Total numbers:"
   write(*,*) "      nodes = ", nnodes
   write(*,*) "  triangles = ", ntria
   write(*,*) "      quads = ", nquad
   write(*,*)

!  Allocate node and element arrays.

   if (ntria > 0) allocate(tria(ntria,3))
   if (nquad > 0) allocate(quad(nquad,4))

   allocate(x(nnodes), y(nnodes))

! READ: Read the nodal coordinates

  do i = 1, nnodes
   read(1,*) x(i), y(i)
  end do

! Read element-connectivity informationd

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
    read(1,*) tria(i,1), tria(i,2), tria(i,3)
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
    read(1,*) quad(i,1), quad(i,2), quad(i,3), quad(i,4)
   end do
  endif

!-------------------------------------------------------------------
! Read the boundary grid information contained in the grid file.

! READ: Number of boundaries.
  read(1,*) nb

 !Let us use the compressed row storage for the boundary node list.
  allocate(nbnodes(nb+1))

  nbnodes(1) = 0

! READ: Number of boundary nodes (including the starting one at the end if
! it is closed such as an airfoil.)

  total_bnodes = 0

  do i = 1, nb

  !Boundary nodes
   read(1,*) dummy_int !<- # of boundary nodes for the boundary segment i.

   total_bnodes = total_bnodes + dummy_int
   nbnodes(i+1) = total_bnodes

  !Boundary faces: e.g., o---o--o---o----o -> 5 nodes and 4 faces.

  end do

   allocate( bnode( total_bnodes ) )

! READ: Read boundary nodes (node numbers in the grid).
  do i = 1, nb
   do j = 1, nbnodes(i+1)-nbnodes(i)
   read(1,*) bnode( nbnodes(i) + j )
   end do
  end do

!  Print the boundary grid data.
   write(*,*) " Boundary nodes and faces:"
   write(*,*) " Boundary segments = ", nb
    do i = 1, nb
     write(*,'(a10,i3,2(a11,i5))') " boundary", i, "  bnodes = ", nbnodes(i+1)-nbnodes(i), &
                                                   "  bfaces = ", nbnodes(i+1)-nbnodes(i)-1
    end do
   write(*,*)

  close(1)

! End of Read grid file>: datafile_grid_in
!--------------------------------------------------------------------------------

!--------------------------------------------------------------------------------
! 2. Read the boundary condition data file

   write(*,*)
   write(*,*) " Reading the boundary condition file....", trim(filename_bc)
   write(*,*)

   allocate(bc_type(nb))

! Open the input file.
  open(unit=2, file=filename_bc, status="unknown", iostat=os)

    read(2,*) 

! READ: Read the boundary condition type
  do i = 1, nb
    read(2,*) dummy_int, bc_type(i)
   end do

!  Print the data
   do i = 1, nb
    write(*,'(a10,i3,a12,a20)') " boundary", i, "  bc_type = ", trim(bc_type(i))
   end do

    i = dummy_int !Never mind. Just to avoid a compilation warning.

    write(*,*)

  close(2)

! End of Read the boundary condition data file
!--------------------------------------------------------------------------------

  write(*,*)
  write(*,*) " End of Reading : ", trim(filename_grid), "  ", trim(filename_bc)
  write(*,*) "-------------------------------------------------------"
  write(*,*)

 end subroutine read_grid



 end module module_common_data

