!********************************************************************************
!  Educationally-Designed Unstructured 2D (EDU2D) Code
!
!  ---------------- EDU2D-CCFV-Template
!
!
! This is module_ccfv_data.
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

 module module_ccfv_data_grid

  use module_common_data, only : p2 !To declare double precision variables below.

  implicit none

  !'public' means these data can be accessed in other program, subroutine/function,
  !and modules. Those not explcitly stated are private to this module, and cannot
  !be accessed by other modules and subroutines/functions.

  !To make the data accesible by other modules/subroutines.
   public :: cell, ncells                           !cell data
   public :: nfaces, face, face_nrml, face_nrml_mag !face data
   public :: bound, nbound                             !boundary data
   public :: heffn, heffc, heffv, heffv_min, heffv_max !effective mesh spacigns

  !To make the subroutine accesible by other modules/subroutines.
   public :: construct_ccfv_grid_data !This constructs the cell-centered FV data.

 !------------------------------------------------------------------------------------
 !------------------------------------------------------------------------------------
 ! Below are the definition of the data used to implement a cell-centered FV method.
 !------------------------------------------------------------------------------------

  !------------------------------------------------
  !>> Cell data: 1D array including trias + quads
  !------------------------------------------------

     integer  :: ncells !number of cells: ncells = ntria + nquad

   !Custom data type for cell-centered methods
    type cc_data_type

     integer                          ::    nvtx  !number of vertices(vertexes)
     integer, dimension(:)  , pointer ::     vtx  !list of vertices(vertexes)
     real(p2)                         ::  xc, yc  !cell centroid coordinates
     real(p2)                         ::     vol  !volume of cell
     integer                          :: nnghbrs  !number of face neighbors
     integer, dimension(:)  , pointer ::  nghbr   !list of face neighbors
     integer, dimension(:,:), pointer :: commonv  !list of vertices shared with nghbr

    end type cc_data_type

    !Cell data array in the custom data type.
     type(cc_data_type), dimension(:), pointer :: cell

    !Note: Components can be accessed by using '%': e.g.,
    !      cell(10)%vol is the volume of the cell 10.

  !------------------------------------------
  !>> Face data: interior faces
  !------------------------------------------

   integer                           :: nfaces        !# of interior faces
   integer , dimension(:,:), pointer :: face          !interior face list: face2cells
   real(p2), dimension(:,:), pointer :: face_nrml     !face normals (unit vectors)
   real(p2), dimension(:)  , pointer :: face_nrml_mag !face normal magnitude

  !------------------------------------------
  !>> Boundary face data
  !------------------------------------------'

    integer  :: nbound    !# of boundary parts (copy from nb in common data just for convenience)


   type bgrid_type
    integer                           :: nbnodes        !# of boundary nodes
    integer,  dimension(:)  , pointer :: bnode          !list of boundary nodes
    integer                           :: nbfaces        !# of boundary faces
    real(p2), dimension(:,:), pointer :: bface_nrml     !face normals (unit vectors)
    real(p2), dimension(:)  , pointer :: bface_nrml_mag !face normal magnitude
    integer , dimension(:)  , pointer :: bcell          !adjacent cell (bface to cell)
   end type bgrid_type

   !Boundary data array in the custom data type.
    type(bgrid_type), dimension(:), pointer :: bound


  !------------------------------------------------
  !>> Various effective mesh spacings.
  !------------------------------------------------

    real(p2) ::  heffn     !Effective mesh spacing based on number of nodes.
    real(p2) ::  heffc     !Effective mesh spacing based on number of cells.
    real(p2) ::  heffv     !Effective mesh spacing based on sqrt(volume).
    real(p2) ::  heffv_min !Min effective mesh spacing based on sqrt(volume).
    real(p2) ::  heffv_max !Max effective mesh spacing based on sqrt(volume).


  !These data will be allocated for a given grid size, and filled in the
  !following subroutine: construct_ccfv_data.

 !------------------------------------------------------------------------------------
 ! End of the data used to implement a cell-centered FV method.
 !------------------------------------------------------------------------------------
 !------------------------------------------------------------------------------------

 contains

!*******************************************************************************
! Create the data required by the ccfv scheme, and verify them.
!
! - Cell data: ncells, and cell%nvtx, vtx, xc, yc, vol, nnghbrs, nghbr, commonv
! - Face data: nfaces, face, face_nrml, face_nrml_mag
! - Boundary data: bound%nbnodes, bnode, nbfaces, bface_nrml, bface_nrml_mag, bcell
!
! Note: We will call this subroutine in the main program.
!
!*******************************************************************************
 subroutine construct_ccfv_grid_data

 !Input: data read from a given grid, and some parameters.
  use module_common_data, only : nnodes                , & !# of nodes
                                 x, y                  , & !nodal coords
                                 ntria, tria           , & !# of trias, and list
                                 nquad, quad           , & !# of quads, and list
                                 nb, bnode, nbnodes    , & !elements
                                 ix, iy                , & !ix=1, iy=2
                                 p2                    , & !Double precision
                                 zero, half, one           !some p2 values

 !Output: Cell data, Face data, and Boundary face data.

  implicit none

 !------------------------------------------------------------------
 ! Below are local (temporary) data used to construct the CCFV data.

  !To store the list of cells around each node.
   type node_type
    integer                        :: nc
    integer, dimension(:), pointer :: c
   end type node_type

  !Array of custom-node-type data.
  type(node_type), dimension(:), pointer :: node


  !Local variables
  integer, dimension(4)   :: temp
  integer, dimension(4,2) :: tempv
  integer                 ::   i,   j,   k,  kk, ck
  integer                 ::  v1,  v2,  v3,  v4
  integer                 :: vk1, vk2, vk3, vk4, vk
  real(p2)                ::  x1,  x2,  y1,  y2

  !Variables used in verification
  integer                           :: cell1, cell2
  real(p2)                          :: vol_domain, vol_domain_cells, xm, ym, volk
  real(p2), dimension(2)            :: sum_bnormal
  real(p2), dimension(:,:), pointer :: sum_face_normal
  real(p2)                          :: machine0_1      !to store machine zero relative to 1
  real(p2)                          :: sum_machine0_1  !to store sum of machine zero
  real(p2)                          :: ref_mag         !to store a reference magnitude

   write(*,*)
   write(*,*) "-------------------------------------------------------"
   write(*,*) "-------------------------------------------------------"
   write(*,*) "-------------------------------------------------------"
   write(*,*) " Construct ccfv grid data and verifty them." 
   write(*,*)

!------------------------------------------------------------------------------------
!------------------------------------------------------------------------------------
! Construct a single custum-data array for cells, which stores cell information
! in a single array, where the first ntria elements are for triangles, and
! the last nquad elements are for quadrilaterals.
!------------------------------------------------------------------------------------
!------------------------------------------------------------------------------------

 !---------------------------------------------------------------
 !---------------------------------------------------------------
 ! (1) Create a single cell array: cell(:)
 !
 !    Note: We already have triangle and quad lists read from
 !          .grid file: tria(:,3) and quad(:,4). We will store
 !          them in a single custom-data array:
 !
 !               cell(i), i=1,ncells.
 !---------------------------------------------------------------

  write(*,*) " >>> Copying tria and quad to a single custom-data-type array....."
 
 !Cells are ordered in the order written in the input .grid file, i.e.,
 !triangles and then quads: cell(:) = [ tria1, tria2, ..., quad1, quad2,...].

 !Total # of cells
  ncells = ntria + nquad

 !Allocate the single array.
  allocate( cell(ncells) )

 !cell(1:ntria) for triangles.
  triangles : do i = 1, ntria

   cell(i)%nvtx = 3

   allocate( cell(i)%vtx(3) ) !allocate array of size 3.

   cell(i)%vtx(1) = tria(i,1)
   cell(i)%vtx(2) = tria(i,2)
   cell(i)%vtx(3) = tria(i,3)

  end do triangles

 !cell(ntria+1:ncells) for quadrialterals
  quads : do i = 1, nquad

   cell( ntria + i )%nvtx = 4

   allocate( cell(ntria + i)%vtx(4) ) !allocate array of size 4.

   cell(ntria + i)%vtx(1) = quad(i,1)
   cell(ntria + i)%vtx(2) = quad(i,2)
   cell(ntria + i)%vtx(3) = quad(i,3)
   cell(ntria + i)%vtx(4) = quad(i,4)

  end do quads

 !Read a re-ordering array (from RCM) if available, and re-order
 !the cell array here.

 !Now we can loop over all cells by cell(i), i=1,ncells, instead
 !of loop over triangles and then quads. Good.

 !---------------------------------------------------------------
 !---------------------------------------------------------------
 ! (2) Compute and store the centroid coordiantes.
 !---------------------------------------------------------------

  write(*,*) " >>> Computing centroid coordinates....."
 
  do i = 1, ncells

  !Centroid of triangle
   if     (cell(i)%nvtx==3) then

    v1 = cell(i)%vtx(1)
    v2 = cell(i)%vtx(2)
    v3 = cell(i)%vtx(3)

    cell(i)%xc = ( x(v1) + x(v2) + x(v3) ) / 3.0_p2
    cell(i)%yc = ( y(v1) + y(v2) + y(v3) ) / 3.0_p2

  !Centroid of quad (intersection of bimedians)
   elseif (cell(i)%nvtx==4) then

    v1 = cell(i)%vtx(1)
    v2 = cell(i)%vtx(2)
    v3 = cell(i)%vtx(3)
    v4 = cell(i)%vtx(4)

    cell(i)%xc = ( x(v1) + x(v2) + x(v3) + x(v4) ) / 4.0_p2
    cell(i)%yc = ( y(v1) + y(v2) + y(v3) + y(v4) ) / 4.0_p2

   else

    write(*,*) "Something is wrong. Invalid cell(i)%nvtx = ", cell(i)%nvtx
    stop

   endif

  end do

 !---------------------------------------------------------------
 !---------------------------------------------------------------
 ! (3) Compute and store the volume.
 !
 !     Use the function 'triangle_area(x1,x2,x3, y1,y2,y3'
 !     included at the bottom of this file for both tria and quad.
 !---------------------------------------------------------------

  write(*,*) " >>> Computing cell volumes by triangles....."
 
  do i = 1, ncells

  !Tria volume (area)
   if     (cell(i)%nvtx==3) then

    !       3
    !       o
    !     .  \
    !    .    \
    !   .      \
    !  .        \
    ! o----------o 
    ! 1          2

    v1 = cell(i)%vtx(1)
    v2 = cell(i)%vtx(2)
    v3 = cell(i)%vtx(3)

    cell(i)%vol = triangle_area( x(v1),x(v2),x(v3), y(v1),y(v2),y(v3) )

  !Quad volume (area) as the sum of two triangle volumes.
   elseif (cell(i)%nvtx==4) then

    !       4            3          4            3
    !       o------------o          o------------o
    !     .             .         .  .         .
    !    .            .    =   .     .      .
    !   .           .        .       .   .
    !  .          .        .         ..  
    ! o----------o        o----------o
    ! 1          2        1          2

    v1 = cell(i)%vtx(1)
    v2 = cell(i)%vtx(2)
    v3 = cell(i)%vtx(3)
    v4 = cell(i)%vtx(4)

    cell(i)%vol =   triangle_area( x(v1),x(v2),x(v4), y(v1),y(v2),y(v4) ) &
                  + triangle_area( x(v2),x(v3),x(v4), y(v2),y(v3),y(v4) )

   else

    write(*,*) "Something is wrong. Invalid cell(i)%nvtx = ", cell(i)%nvtx
    stop

   endif

  end do

 !---------------------------------------------------------------
 !---------------------------------------------------------------
 ! (4) Construct face-neighbor lists
 !---------------------------------------------------------------

  !-------------------------------------------------------
  ! First, create node-to-cell lists for convenience.
  !
  ! Example: node i has 4 cells around it,
  !
  !        o-------o-------------o
  !       /        |             |
  !      /    23   |      41     |
  !     o----------o-------------o
  !      \        i \            |
  !       \   101    \     13    |
  !        \          \          | 
  !         o----------o---------o
  !
  !          and so we'll have
  !            node(i)%nc     = 4
  !            node(i)%c(1:4) = [13,23,41,101] !<- No particular order.
  !

    write(*,*) " >>> Constructing node to cell lists....."

    allocate( node(nnodes) )

  ! Initialize the # of cells around a node.
 
    do i = 1, nnodes
     node(i)%nc  = 0
    end do

  ! Count the # of cells around a node.

    do i = 1, ncells
     do k = 1, cell(i)%nvtx
                vk = cell(i)%vtx(k)
       node(vk)%nc = node(vk)%nc + 1
     end do
    end do

  ! We can now allocate the node-to-cell arrays.

    do i = 1, nnodes
     allocate( node(i)%c( node(i)%nc ) )
    end do

  ! Re-initialize the # of cells around a node.

    do i = 1, nnodes
     node(i)%nc  = 0
    end do

  ! Fill the node-to-cell arrays.

    do i = 1, ncells
     do k = 1, cell(i)%nvtx
                              vk = cell(i)%vtx(k)
         node(vk)%nc             = node(vk)%nc + 1
         node(vk)%c(node(vk)%nc) = i
     end do
    end do

  !-------------------------------------------------------
  !-------------------------------------------------------
  ! Now create the face-neighbor list for each cell.
  !
  ! Example: The cell i below has 4 face neighbors:
  !          the cells, 3, 4, 6, 9,
  !
  !          / \
  !         / 9 \
  !  _____ /_____\
  !  \  4 /      /\
  !   \  /   i  /  \
  !    \/______/__3_\
  !     \     /
  !      \ 6 /
  !       \ /
  !
  ! and so we'll have
  !
  !         cell(i)%nnghbrs    = 4
  !         cell(i)%nghbr(1:4) = [3,6,9,4] !<- No particular order here.
  !
  ! and for each face, k, we'll also store the nodes(vertices) that
  ! defines the face:
  !
  !         cell(i)%commonv(k,1) !right node seen from i to k
  !         cell(i)%commonv(k,2) ! left node seen from i to k
  !
  !        _______2 (left node)
  !       /      /\
  !      /   i  /k \
  !     /______/____\
  !           1 (right node)

    write(*,*) " >>> Constructing face-negihbor lists....."

   cell_loop : do i = 1, ncells

    !Initialize the # of neighbors around a cell i.
     cell(i)%nnghbrs = 0

    !Loop over the vertices or equivalently faces.
    face_k : do k = 1, cell(i)%nvtx

    !Define a face by two vertices [v1,v2], for which a neighbor is sought. 

      v1 = cell(i)%vtx(k)

     if (k+1 > cell(i)%nvtx) then
      v2 = cell(i)%vtx(1)   !<- Back to the first vertex.
     else
      v2 = cell(i)%vtx(k+1) !<- Next vertex
     endif

    !Look for a neighbor in the cells around v1.

     find_nghbr : do kk = 1, node(v1)%nc

                ck = node(v1)%c(kk)

     !Neighbor cell is a triangle.
      if ( cell(ck)%nvtx == 3 ) then

        vk1 = cell(ck)%vtx(1)
        vk2 = cell(ck)%vtx(2)
        vk3 = cell(ck)%vtx(3)

       !Check if any of the face matches (v1,v2).
        if    ( (v1==vk2 .and.v2==vk1) .or. &
                (v1==vk3 .and.v2==vk2) .or. &
                (v1==vk1 .and.v2==vk3)      ) then

                      cell(i)%nnghbrs = cell(i)%nnghbrs + 1
          temp(  cell(i)%nnghbrs    ) = ck
          tempv( cell(i)%nnghbrs, 1 ) = v1
          tempv( cell(i)%nnghbrs, 2 ) = v2

          exit find_nghbr

        endif

     !Neighbor cell is a quadrialteral
      elseif ( cell(ck)%nvtx == 4 ) then

        vk1 = cell(ck)%vtx(1)
        vk2 = cell(ck)%vtx(2)
        vk3 = cell(ck)%vtx(3)
        vk4 = cell(ck)%vtx(4)

       !Check if any of the face matches (v1,v2).
        if    ( (v1==vk2 .and.v2==vk1) .or. &
                (v1==vk3 .and.v2==vk2) .or. &
                (v1==vk4 .and.v2==vk3) .or. &
                (v1==vk1 .and.v2==vk4)      ) then

                      cell(i)%nnghbrs = cell(i)%nnghbrs + 1
          temp(  cell(i)%nnghbrs    ) = ck
          tempv( cell(i)%nnghbrs, 1 ) = v1
          tempv( cell(i)%nnghbrs, 2 ) = v2

          exit find_nghbr

        endif

      else
       write(*,*) " Cell ", i, " is not tria nor quad... Something is wrong. Stop."
      endif

     end do find_nghbr

    end do face_k

 ! Store the neighbors in the neighbor list.

    allocate( cell(i)%nghbr(   cell(i)%nnghbrs    ) )
    allocate( cell(i)%commonv( cell(i)%nnghbrs, 2 ) )

    do k = 1, cell(i)%nnghbrs
     cell(i)%nghbr(k)     = temp(k)    !kth neighbor cell
     cell(i)%commonv(k,1) = tempv(k,1) !shared vertex (right seen from i)
     cell(i)%commonv(k,2) = tempv(k,2) !shared vertex ( left seen from i)
    end do

   end do cell_loop

 !---------------------------------------------------------------
 !---------------------------------------------------------------
 ! (5) Construction of face data.
 !---------------------------------------------------------------

 ! Note: The face data contain only the interior faces, which are shared by two cells.
 ! Note: Define the face as pointing from cell1 to cell2, where cell2 > cell1
 !       (i.e., smaller cell number to larger cell number).
 !       So, a face is oriented from a cell number to a larger cell number.

    write(*,*) " >>> Constructing face data....."

 !---------------------------------------
 ! First, count the number of total interior faces.

  nfaces = 0

  do i = 1, ncells

   do k = 1, cell(i)%nnghbrs

   !This identifies a face and avoids double count.
    if ( i < cell(i)%nghbr(k) ) then

      nfaces = nfaces + 1

    endif

   end do

  end do

 !---------------------------------------
 ! Allocate and fill the face arrays.

   allocate(face(         nfaces,4)) !face list: (lefft/right cells and nodes)
   allocate(face_nrml(    nfaces,2)) !unit face normal vector
   allocate(face_nrml_mag(nfaces  )) !magnitude of face vector

  !We need to re-count 'nfaces'. So, initialize it.
   nfaces = 0

  !Now, construct the face arrays!

   do i = 1, ncells

    do k = 1, cell(i)%nnghbrs

     !To avoid duplicating faces, we define a face pointing
     !from a smaller cell number to a larger cell number.

     if ( i < cell(i)%nghbr(k) ) then

      !Face is found when the neighbor cell number is greater than i.

               nfaces = nfaces + 1

      !           Left(2)
      !        o---o---------o
      !       .    .          .
      !      .     .           .
      !     .      .normal      .
      !    .  Left .--->  Right  .
      !   .    i   .       k      .
      !  .         .               .
      ! o----------o----------------o
      !          Right(1)
      !

      !Left cell
       face(nfaces,1) = i
      !Right cell
       face(nfaces,2) = cell(i)%nghbr(k)

      !Left node
       face(nfaces,3) = cell(i)%commonv(k,2)
      !Right node
       face(nfaces,4) = cell(i)%commonv(k,1)

      !Right vertex (seen from i)
       x1 = x( cell(i)%commonv(k,1) )
       y1 = y( cell(i)%commonv(k,1) )

      !Left vertex (seen from i)
       x2 = x( cell(i)%commonv(k,2) )
       y2 = y( cell(i)%commonv(k,2) )

      !Face normal pointing from i to k.
       face_nrml(nfaces,1) = -(y1-y2)
       face_nrml(nfaces,2) =   x1-x2

      !Magnitude of the face normal pointing from i to k.
       face_nrml_mag(nfaces) = sqrt( ( x1-x2 )**2 + ( -(y1-y2) )**2 )

      !Face normal pointing from i to k.
       face_nrml(nfaces,1) = -(y1-y2)/ face_nrml_mag(nfaces)
       face_nrml(nfaces,2) =  (x1-x2)/ face_nrml_mag(nfaces)

     endif

    end do

   end do

  !-------------------------------------------------------------------------------
  ! Compute and store the boundary face normals.
  !-------------------------------------------------------------------------------

  ! Boundary face j consists of nodes j and j+1.
  !
  !  Interior domain      /
  !                      /
  !              /\     o
  !             /  \   /
  !            / ck \ /   Outside the domain
  ! --o-------o------o
  !           j   |  j+1
  !               |   
  !               v Face normal for the face j.
  !
  ! ck = bcell, the cell having the boundary face j.
  !
  ! Note: Boundary data were read from .grid file and stored in a compressed-row
  !       storage (CRS, bnode(:) with nbnodes(:) ); see edu2d_module_common_data.f90.
  !       We will use them and construct the custom-data array 'bound', which
  !       will be used in our CCFV solver.

   write(*,*) " >>> Compute boundary face normals..."

   allocate(bound(nb))

   boundary_parts : do i = 1, nb

    !For convenience, let's store node information in bound(i)%bnode(:).

     bound(i)%nbnodes = nbnodes(i+1) - nbnodes(i) !<- # of nodes in the boundary group i.

     allocate( bound(i)%bnode(bound(i)%nbnodes) ) !<- Allocate a bnode array within 'bound'.

    !Copy the data from the CRS 'bnode'.
     bnode_loop : do j = 1, bound(i)%nbnodes
      bound(i)%bnode(j) = bnode( nbnodes(i) + j )
     end do bnode_loop

    !Now, boundary faces.

     bound(i)%nbfaces = (nbnodes(i+1)-nbnodes(i)) - 1 ! # of faces = # of nodes - 1

    !Allocate boundary face normal arrays.
     allocate( bound(i)%bface_nrml(     bound(i)%nbfaces,2 ) )
     allocate( bound(i)%bface_nrml_mag( bound(i)%nbfaces   ) )

    !Now compute and store the boundary face normals.

    bface_loop : do j = 1, bound(i)%nbfaces

    !Boundary face segment with nodes j and j+1
     v1 = bound(i)%bnode(j)
     v2 = bound(i)%bnode(j+1)

    !Outward face normal (Note: Boundary nodes are ordered such that the domain
    !is on the left). The normal is outward to the outside the domain. Use the basic formula.

      bound(i)%bface_nrml_mag(j) = sqrt( ( y(v2) - y(v1) )**2 + ( -( x(v2) - x(v1) ) )**2 )

      bound(i)%bface_nrml(j,ix)  =  ( y(v2) - y(v1) ) / bound(i)%bface_nrml_mag(j)
      bound(i)%bface_nrml(j,iy)  = -( x(v2) - x(v1) ) / bound(i)%bface_nrml_mag(j)

    end do bface_loop

   end do boundary_parts

  !-------------------------------------------------------------------------------
  ! Find and store the cell number for each boundary face.
  !
  ! bound(i)%bcell(j) = cell having the boundary face j in the boundary part i.
  !-------------------------------------------------------------------------------

   write(*,*) " >>> Finding and storing a cell having a boundary face (bcell),"
   write(*,*) "     which we wish to access from a boundary face..."

  ! Boundary face j consists of nodes j and j+1.
  !
  !   Interior domain           
  !        /     \ /    \ /
  !       .............../
  !      / \     /\     o
  !     /   \   /  \   /
  !    /     \ / ck \ /   Outside the domain
  ! --o-------o------o
  !           j      j+1
  ! Outside the domain
  !
  ! The adjacent cell must be contained in the list of cells around the node j.
  ! Find it for each boundary face.

    get_bcell : do i = 1, nb

     allocate( bound(i)%bcell( bound(i)%nbfaces ) )

    loop_over_bfaces : do j = 1, bound(i)%nbfaces

    !Boundary face segment with nodes j and j+1
     v1 = bound(i)%bnode(j)
     v2 = bound(i)%bnode(j+1)

     !Find bcell having the boundary face j from the cells around v1.
     find_bcell : do kk = 1, node(v1)%nc

      ck = node(v1)%c(kk)

     !-----------------------------------------------
     ! ck is a triangle.
      if ( cell(ck)%nvtx == 3 ) then

        vk1 = cell(ck)%vtx(1)
        vk2 = cell(ck)%vtx(2)
        vk3 = cell(ck)%vtx(3)

       !Check if any of the faces matches (v1,v2).
        if    ( (v1==vk1 .and.v2==vk2) .or. &
                (v1==vk2 .and.v2==vk3) .or. &
                (v1==vk3 .and.v2==vk1)      ) then

          bound(i)%bcell(j) = ck
          exit find_bcell

        endif

     !-----------------------------------------------
     ! ck is a quadrialteral
      elseif ( cell(ck)%nvtx == 4 ) then

        vk1 = cell(ck)%vtx(1)
        vk2 = cell(ck)%vtx(2)
        vk3 = cell(ck)%vtx(3)
        vk4 = cell(ck)%vtx(4)

       !Check if any of the faces matches (v1,v2).
        if    ( (v1==vk1 .and.v2==vk2) .or. &
                (v1==vk2 .and.v2==vk3) .or. &
                (v1==vk3 .and.v2==vk4) .or. &
                (v1==vk4 .and.v2==vk1)      ) then

          bound(i)%bcell(j) = ck
          exit find_bcell

        endif

      endif

     end do find_bcell

    end do loop_over_bfaces

   end do get_bcell

!------------------------------------------------------------------------------------
! Copy nb to nbound just for convenience.
! So, we can access the boundary information bound(1:nbound) and nbound from the
! same module (this module). To use them, just state 
!            use module_ccfv_data_grid, only : bound, nbound.

   nbound = nb

!------------------------------------------------------------------------------------
! Deallocate node2cell data, which was useful to construct face data.
! We don't need this any more. Thanks and bye.

  deallocate(node)




!------------------------------------------------------------------------------------
!------------------------------------------------------------------------------------
! Verify the CCFV data.
!
! - Cell data         : sum of the cell volume must be equal to the volume of the domain.
! - Boundary face data: sum of boundary face normals must be zero.
! - Face data         : sum of face normals must be zero for each cell.
!
! Note: These tests do not detect mesh tangling and zero/negative volume elements.
!       You can add tests to detect such.
!
!------------------------------------------------------------------------------------
!------------------------------------------------------------------------------------

   write(*,*)
   write(*,*) " >>> Verifying the ccfv grid data..."
   write(*,*)


   machine0_1 = epsilon(1.0_p2) !Fortran function that returns machine zero.

   write(*,*) "     Machine zero relative to 1 = ",  machine0_1

  !--------------------------------------------------------
  ! Cetroid check
  !--------------------------------------------------------
   write(*,*)
   write(*,*)
   write(*,*) " --- Check the centroids:"
   write(*,*)

      !          4             3
      !          o-------------o
      !         .            . |   c is the centroid.
      !        .           .   |
      !       .          .     |   Form a triangle with c and a face.
      !      .         c  volk |   If the area of the triangle 'volk' is negative,
      !     .            .     |   the centroid is outside, which is usually
      !    .               .   |   considered as a failure. So, check it
      !   .                  . |   for all faces. (Left is an example of triangle c-2-3.)
      !  o---------------------o
      ! 1                      2
      !

    do i = 1, ncells

    !Nodes are ordered counterclockwise. Take two consecutive ones.
     do k = 1, cell(i)%nvtx

        v1 = cell(i)%vtx(k)

       if (k+1 > cell(i)%nvtx) then
        v2 = cell(i)%vtx(1)   !<- Back to the first vertex.
       else
        v2 = cell(i)%vtx(k+1) !<- Next vertex
       endif

       x1 = x(v1)
       y1 = y(v1)

       x2 = x(v2)
       y2 = y(v2)

      volk = triangle_area(x1,x2, cell(i)%xc, y1,y2, cell(i)%yc)

     !If volume_k is negative, stop.
      if (volk < zero) then
       write(*,*) " A centroid is outside the cell... Cell = ", i, " Stop..."
       write(*,*) "                      (xc,yc) = ", cell(i)%xc, cell(i)%yc
       write(*,*) "                      (x1,y1) = ", x1, y1
       write(*,*) "                      (x2,y2) = ", x2, y2
       write(*,*) "  Partial volume (tria c-1-2) = ", volk
       stop
      endif

     end do

    end do

   !You get here. It means there are not centroids outside a cell.

     write(*,*) "  No centroids found that are located outside a cell. Good."

  !--------------------------------------------------------
  ! Volume check
  !--------------------------------------------------------
   write(*,*)
   write(*,*)
   write(*,*) " --- Check the total volume:"
   write(*,*)


   !(0)Sum of machine zero relative to volume for correctly check zero.

     sum_machine0_1 = zero

    do i = 1, ncells
     sum_machine0_1   = sum_machine0_1   + cell(i)%vol*machine0_1
    end do

    write(*,*) "     Machine zero relative to sum of volumes = ", sum_machine0_1
    write(*,*)

   !(1)Compute the total volume of the entire domain by applying
   !   the Green-Gauss volume formula over the boundary faces.
   !   Store the total volume in "vol_domain".
   !
   !   Note: The GG volume is correct even of there are multiple objects inside the
   !         domain. Think about why it works fine.

    vol_domain = zero

    do i = 1, nb

     do j = 1, bound(i)%nbfaces

      v1 = bound(i)%bnode(j)
      v2 = bound(i)%bnode(j+1)

      xm = half*( x(v1) + x(v2) )
      ym = half*( y(v1) + y(v2) )

      vol_domain = vol_domain &
                 + half*(   xm*bound(i)%bface_nrml(j,ix) &
                          + ym*bound(i)%bface_nrml(j,iy) )*bound(i)%bface_nrml_mag(j)

     end do

    end do

     write(*,*) "  Total volume of the domain = ", vol_domain


   !(2)Compute the total volume of the entire domain by adding up the cell volumes.
   !   Store it in "vol_domain_cells".

    vol_domain_cells = zero

    do i = 1, ncells

     vol_domain_cells = vol_domain_cells + cell(i)%vol

    end do


   !(3)Print and check the difference, which must be zero.
   !

    write(*,*) "     Sum of the cell volumes = ", vol_domain_cells
    write(*,*) "                  Difference = ", abs(vol_domain - vol_domain_cells)
    write(*,*) "         sum of machine zero = ", sum_machine0_1


    if ( abs(vol_domain - vol_domain_cells) > 50.0_p2*sum_machine0_1 ) then
     write(*,*) " Difference is larger than round-off error... Something is wrong. Stop."
     stop
    endif

  !--------------------------------------------------------
  ! Boundary normal sum check
  !--------------------------------------------------------
   write(*,*)
   write(*,*)
   write(*,*) " --- Check the sum of all boundary normals (must be zero):"
   write(*,*)

   !(0)Sum of machine zero relative to face magnitude for correctly check zero.
   !

     sum_machine0_1 = zero

     do i = 1, nb
      do j = 1, bound(i)%nbfaces
       sum_machine0_1  = sum_machine0_1  + bound(i)%bface_nrml_mag(j)*machine0_1 
      end do
     end do

    write(*,*) "     Machine zero relative to sum of boundary face mag = ", sum_machine0_1
    write(*,*)

   !(1)Compute the sum of all boundary face normal vectors = sum_bnormal(ix) and sum_bnormal(iy),
   !   which must be zero.
   !

      sum_bnormal = zero

   !All boundary groups
    do i = 1, nb

    !All boundary faces
     do j = 1, bound(i)%nbfaces

      sum_bnormal(ix) = sum_bnormal(ix) + bound(i)%bface_nrml(j,ix) * bound(i)%bface_nrml_mag(j)
      sum_bnormal(iy) = sum_bnormal(iy) + bound(i)%bface_nrml(j,iy) * bound(i)%bface_nrml_mag(j)

     end do

    end do

   !(3)Print and check the boundary face normal sum, which must be zero.
   !

    write(*,*) "     Sum of boundary face normal (nx) = ", sum_bnormal(ix)
    write(*,*) "     Sum of boundary face normal (ny) = ", sum_bnormal(iy)


    if ( abs(sum_bnormal(ix)) > 50.0_p2*sum_machine0_1 .or. &
         abs(sum_bnormal(iy)) > 50.0_p2*sum_machine0_1      ) then

     write(*,*) " Boundary face vector sum is larger than machine zero....."
     write(*,*) " Something is wrong. Stop."

     stop

    endif

  !--------------------------------------------------------
  ! Face normal sum check for each cell
  !--------------------------------------------------------
   write(*,*)
   write(*,*)
   write(*,*) " --- Check the face-normal sum over faces of a cell:"
   write(*,*)

   allocate(sum_face_normal(ncells,2))
   sum_face_normal = zero

  !----------------------------------------------------
  ! Accumulate face normals at cells by looping over interior faces.

   do i = 1, nfaces

    cell1 = face(i,1)
    sum_face_normal( cell1, ix ) = sum_face_normal( cell1, ix ) + face_nrml(i,ix)*face_nrml_mag(i)
    sum_face_normal( cell1, iy ) = sum_face_normal( cell1, iy ) + face_nrml(i,iy)*face_nrml_mag(i)

    cell2 = face(i,2)
    sum_face_normal( cell2, ix ) = sum_face_normal( cell2, ix ) - face_nrml(i,ix)*face_nrml_mag(i)
    sum_face_normal( cell2, iy ) = sum_face_normal( cell2, iy ) - face_nrml(i,iy)*face_nrml_mag(i)

   end do

  !----------------------------------------------------
  ! Add boundary face normal contributions to cells by looping over boundary faces.

   !Loop over boundary segments
    do i = 1, nb

     !Loop over boundary faces
     do j = 1, bound(i)%nbfaces

     cell1 = bound(i)%bcell(j)

     sum_face_normal( cell1, ix ) = sum_face_normal( cell1, ix ) &
                                  + bound(i)%bface_nrml(j,ix) * bound(i)%bface_nrml_mag(j)

     sum_face_normal( cell1, iy ) = sum_face_normal( cell1, iy ) &
                                  + bound(i)%bface_nrml(j,iy) * bound(i)%bface_nrml_mag(j)
     end do

    end do

    write(*,*) "   Display the maximum over all cells (must be zero):"
    write(*,*) "   (the sum of face normals over each cell)"
    write(*,*)
    write(*,*) "     Max of |sum_faces face normal (nx)| = ", maxval(abs(sum_face_normal(:,ix)))
    write(*,*) "     Max of |sum_faces face normal (ny)| = ", maxval(abs(sum_face_normal(:,iy)))

  !----------------------------------------------------
  ! Check the maximum sum over all cells. Must be zero.

   !Use the maximum sqrt(vol) as a reference magnitude for checking zero face normal sum.

    ref_mag = maxval( sqrt(cell(1:ncells)%vol) )

     write(*,*)
     write(*,*) "              Reference magnitude = ", ref_mag
     write(*,*) "      Machine zero w.r.t. ref mag = ", ref_mag*machine0_1
     write(*,*)


    if ( maxval(abs(sum_face_normal( 1:ncells, ix ))) > 50.0_p2*ref_mag*machine0_1 .or. &
         maxval(abs(sum_face_normal( 1:ncells, iy ))) > 50.0_p2*ref_mag*machine0_1      ) then

     write(*,*) " Max face vector sum over a cell is larger than machine zero... Something is wrong. Stop."

     stop

    endif

   deallocate(sum_face_normal)


 !Any other check?

   write(*,*)
   write(*,*)
   write(*,*) " >>> Finished Verifying the ccfv grid data..."

!------------------------------------------------------------------------------------
! Compute mesh spacing statistics.
!
!   heffn     = Effecrtive spacing based on # of nodes
!   heffc     = Effecrtive spacing based on # of cells
!   heffv     = Average of sqrt(volume).
!   heffv_min = Minimum sqrt(volume).
!   heffv_max = Maximum sqrt(volume).
!

   write(*,*)
   write(*,*)
   write(*,*) " >>> Compute effective mesh spacings"
   write(*,*)

   !>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    heffn     = sqrt( one/real(nnodes,p2) ) !Effecrtive spacing based on # of nodes
    heffc     = sqrt( one/real(ncells,p2) ) !Effecrtive spacing based on # of cells

   !Compute average, min, and max effective mesh spacing based on sqrt(volume).

    heffv     = sqrt( cell(1)%vol )
    heffv_min = sqrt( cell(1)%vol )
    heffv_max = sqrt( cell(1)%vol )

    do i = 2, ncells
     heffv     = heffv + sqrt( cell(i)%vol )
     heffv_min = min( heffv_min, sqrt( cell(i)%vol ) )
     heffv_max = max( heffv_max, sqrt( cell(i)%vol ) )
    end do

     heffv     = heffv / real(ncells,p2)

   !>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

   write(*,*) "  heffn     = ", heffn
   write(*,*) "  heffc     = ", heffc
   write(*,*)
   write(*,*) "  heffv     = ", heffv
   write(*,*) "  heffv_min = ", heffv_min
   write(*,*) "  heffv_max = ", heffv_max
   write(*,*)
   write(*,*)

!------------------------------------------------------------------------------------
!------------------------------------------------------------------------------------
!------------------------------------------------------------------------------------

   write(*,*)
   write(*,*) " End of Construct ccfv grid data and verifty them." 
   write(*,*) "-------------------------------------------------------"
   write(*,*) "-------------------------------------------------------"
   write(*,*) "-------------------------------------------------------"
   write(*,*)

 end subroutine construct_ccfv_grid_data
!*******************************************************************************


!*******************************************************************************
! Compute the area of a triangle defined by 3 vertices:
!
!       (x1,y1), (x2,y2), (x3,y3),
!
! which is assumed to be ordered clockwise.
!
!     1              3
!      o------------o
!       \         .
!        \       .
!         \    .
!          \ .
!           o
!           2
!
! Note: Area is a vector based on the right-hand rule: 
!       when wrapping the right hand around the triangle with the fingers in the
!       direction of the vertices [1,2,3], the thumb points in the positive
!       direction of the area (towards you).
!
! Note: Area vector is computed as the cross product of edge vectors [31] and [32].
!
!*******************************************************************************
 function triangle_area(x1,x2,x3, y1,y2,y3) result(area)
 
 implicit none

 integer , parameter :: p2 = selected_real_kind(15) !Double precision

 !Input
  real(p2), intent(in)   :: x1,x2,x3, y1,y2,y3

 !Output
  real(p2) :: area

  !Area in 2D (= z-component of the area vector in 3D)

!   area = 0.5_p2*( (x1-x3)*(y2-y3)-(y1-y3)*(x2-x3) )      !<- cross product
    area = 0.5_p2*( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) ) !<- just rearranged


 end function triangle_area
!*******************************************************************************


 end module module_ccfv_data_grid

