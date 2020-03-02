!*******************************************************************************
! Educationally-Designed Unstructured 2D (EDU2D) Code
!
!                         --- EDU2D-Twod2Threed ---
!
! This code reads a 2D grid and generates a 3D grid by extending it to the 3rd
! dimension:
!
! 1. Switch from (x,y) to (x,z) and define the first plane at y=0.
!
! 2. [Option 1]: Generate 2D planes along y-axis by copying the 2D (x,z) grid.
!    [Option 2]: Generate 2D planes along z-axis by copying the 2D (x,y) grid.
!    [Option 3]: Rotate the 2D grid.
!
! 3. Generate hex/prism elements by connecting two adjacent planes.
!    [Hex by extending quads, prism by extending triangles.]
!    There is an option to subdivide all prisms into tetrahedra.
!
!
!        written by Dr. Katate Masatsuka (info[at]cfdbooks.com),
!
! the author of useful CFD books, "I do like CFD" (http://www.cfdbooks.com).
!
! This is Version 8 (January, 2020).
!
!-------------------------------------------------------------------------------
!
!  Input:
!
!   project.grid  ! 2D grid file
!   project.bcmap ! 2D grid boundary condition information
!
!   NOTE: These files are used in EDU2D solvers.
!         The format of these files are explained further below.
!
!  Output:
!
!   project_3d.ugrid   ! 3D prismatic grid (UGRID format)
!   project_3d.mapbc   ! 3D BC infomation extended from 2D file
!   project_3d_tec.dat ! Tecplot file for viewing the boundary grid
!   project_3d.su2     ! SU2 format
!   project_3d.vtk     ! VTK format
!
!-------------------------------------------------------------------------------
!
!
! The program may be updated in future.
!
! Version 8 ( January 2020): Added an option to shift a 2D grid at a specified
!                            rate. (dx/dz,dy/dz) for "straight_in_z", or
!                                  (dx/dy,dz/dy) for "straight_in_y"
!                            This was needed to generate a space-time mesh for
!                            a moving cylinder case (2D unsteady problem).
!
! Version 7 ( January 2020): Added an option to extend (x,y) grid in z direction,
!                            for example, with the following parameters:
!
!                            extension_method = "straight_in_z"
!                                        z0   = 0.0
!                                        zn   = 0.18
!                              switch_y_and_z = F
!
! Version 6 (  August 2019): Added an option to change the radius of rotation
!                            and to linearly change the z-coordiante while rotating.
! Version 5 (  August 2019): Added an option to change y and z at the end.
! Version 4 (  August 2019): Bug fixed (all files were written even when not requested)
!                            BC markers were wrong for .su2 (fixed).
!                            Added a rotation option as another way to generate 3D from 2D.
! Version 3 (     May 2019): Introduced input file. Generate .su2 and .vtk files.
! Version 1 (   April 2016): Support mixed grid input, and generate a 3D hex/prism grid.
!
!
! This F90 code is written and made available for an educational purpose.
! This file may be updated in future.
!
! Katate Masatsuka, http://www.cfdbooks.com
!*******************************************************************************
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!
!  Input parameter module
!
!-------------------------------------------------------------------------------
!
!  Sample input file: 'input_twod2threed.nml' to generate a sample grid.
!  ------------------------------------------------------
!   &input_parameters
!             project_name   = "fp_grid"
!               n_2dplanes   = 3
!          extension_method = "straight_in_y"
!                       y0   = 0.0
!                       yn   = 2.0
!                prism2tetra = F
!      generate_ugrid_file   = T
!               ugrid_binary = T
!      generate_su2_file     = T
!      generate_tec_file_b   = T
!      generate_tec_v        = T
!      generate_vtk_file     = T
!   /
!  ------------------------------------------------------
!
!  or if you want to rotate it,
!
!  ------------------------------------------------------
!   &input_parameters
!             project_name   = "fp_grid"
!               n_2dplanes   = 30
!           extension_method = "rotate_around_z"
!           rotate_radius    = 2.0
!           rotate_end_angle = 180
!           rotate_z_shape   = "flat" !or ="sine" 
!           rotate_sine_freq = 11.0   !<- only for rotate_z_shape="sine" 
!                prism2tetra = F
!      generate_ugrid_file   = T
!               ugrid_binary = T
!      generate_su2_file     = T
!      generate_tec_file_b   = T
!      generate_tec_v        = T
!      generate_vtk_file     = T
!   /
!  ------------------------------------------------------
!
!   Note: No need to specify all namelist variables.
!         Those not specified are given their default values
!         as defined below.
!
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
 module input_parameter_module

  implicit none

  integer , parameter ::    dp = selected_real_kind(P=15)
  real(dp), parameter ::  zero = 0.0_dp
  real(dp), parameter ::   one = 1.0_dp
  real(dp), parameter ::   two = 2.0_dp
  real(dp), parameter :: three = 3.0_dp
  real(dp), parameter ::  half = 0.5_dp
  real(dp), parameter ::    pi = 3.14159265358979323846_dp

  public

!----------------------------
! Default input values
!----------------------------

!----------------------------
! Name of the input 2D grid.
! If "fp_grid.grid", then  project_name = "fp_grid".

 character(80) :: project_name = "fp_grid"

!----------------------------
! # of 2D planes.
! n_2dplanes = 2: No interior points (only 2 boundary planes).
! n_2dplanes = 3: One interior plane.

  integer :: n_2dplanes = 3

!----------------------------
! How to extend the 2D grid to 3D.

 character(80) :: extension_method = "straight_in_y" !or "rotate_around_z"

!----------------------------
! Parameters for extension_method = "straight_in_y"
!
! The input 2D grid will be placed at y=y0, and
! also at y=yn to create a 3D grid. With values below,
! if n_2dplanes = 3, one interior plane will be placed at y=1.0.

  real(dp) :: y0 = 0.0_dp
  real(dp) :: yn = 2.0_dp

  real(dp) :: dxdy = 0.0_dp
  real(dp) :: dzdy = 0.0_dp

! For extension_method = "straight_in_z"

  real(dp) :: z0 = 0.0_dp
  real(dp) :: zn = 2.0_dp

  real(dp) :: dxdz = 0.0_dp
  real(dp) :: dydz = 0.0_dp

!----------------------------
! Parameters for extension_method = "rotate_around_z"
!
! rotate_radius     : defines the rotation axis length
!                     This should be large enough.
! rotate_end_angle  : the final plane location in rotating angle.
! rotate_z_shape    : variation in z when rotating.
! rotate_sine_freq  : a in sin(a*pi) for rotate_z_shape="sine"
!                     More wavy if large.
! rotate_radius_rate: Increase the radius of rotation by
!                     100*rotate_radius_rate %.

  real(dp)      :: rotate_radius      =  5.0_dp
  real(dp)      :: rotate_radius_rate =  0.0_dp
  real(dp)      :: rotate_end_angle   = 90.0_dp
  character(80) :: rotate_z_shape     = "flat" !or "sine"
  real(dp)      :: rotate_sine_freq   = 2.0_dp
  real(dp)      :: rotate_z_zmax      = 1.0_dp

!----------------------------
! Swtich y and z at the end if requested, so that the grid
! looks extended in z instead of y.

  logical :: switch_y_and_z = .false.

!----------------------------
! To subdivide all elements into tetrahedra (if prism2tetra = T).
! Default = do not subdivide.

  logical :: prism2tetra = .false.

!----------------------------
! generate_ugrid_file = T to write a .ugrid file.
!                       F not to write.
!
!    b8_ugrid_format  = T (binary), = F (ASCII).

  logical :: generate_ugrid_file = .true.
  logical ::    ugrid_binary     = .false.

!----------------------------
! generate_su2_file = T to write .su2 file
!                     F not to write.

  logical :: generate_su2_file = .true.

!----------------------------
! generate_tec_file = T to write a Tecplot file.
!                     F not to write.

  logical :: generate_tec_file_b = .true.

  logical :: generate_tec_v      = .false.

!----------------------------
! generate_vtk_file = T to write a .vtk file.
!                     F not to write.

  logical :: generate_vtk_file = .true.

!----------------------------
! End of Default input values
!----------------------------

! Below is the list of all input parameters available:

  namelist / input_parameters /       &
                      project_name  , &
                        n_2dplanes  , &
                  extension_method  , &
                                y0  , &
                                yn  , &
                                dxdy, &
                                dzdy, &
                                z0  , &
                                zn  , &
                                dxdz, &
                                dydz, &
                  rotate_radius     , &
                  rotate_radius_rate, &
                  rotate_end_angle  , &
                  rotate_z_shape    , &
                  rotate_sine_freq  , &
                  rotate_z_zmax     , &
                    switch_y_and_z  , &
                       prism2tetra  , &
              generate_ugrid_file   , &
                      ugrid_binary  , &
              generate_su2_file     , &
              generate_tec_file_b   , &
              generate_tec_v        , &
              generate_vtk_file

 contains

!*****************************************************************************
!* Read input_parameters in the input file: file name = namelist_file
!*****************************************************************************
  subroutine read_nml_input_parameters(namelist_file)

  implicit none
  character(21), intent(in) :: namelist_file
  integer :: os

  write(*,*) "**************************************************************"
  write(*,*) " List of namelist variables and their values"
  write(*,*)

  open(unit=10,file=namelist_file,form='formatted',status='old',iostat=os)
  read(unit=10,nml=input_parameters)

  write(*,nml=input_parameters) ! Print the namelist variables.
  close(10)


  end subroutine read_nml_input_parameters

 end module input_parameter_module
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!
!  End of input parameter module
!
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------

!********************************************************************************
! Main program begins here.
!
!
!
! Katate Masatsuka, May 2019. http://www.cfdbooks.com
!********************************************************************************
 program edu2d_twod2threed

 use input_parameter_module

 implicit none

!-------------------------------------------------------------------------------
! Custom data types for 2D input grid

  type elm_data2d
   integer,   dimension(:), pointer :: vtx      !list of vertices
   integer                          :: nvtx
  end type elm_data2d

  type node_data2d
   real(dp)                         :: x, y !Coordinates in xy space
  end type node_data2d

  type bnode_data2d
   character(80)                    :: bc_type !type of boundary condition
   integer                          :: nbnodes !# of boundary nodes
   integer,   dimension(:), pointer :: bnode   !list of boundary nodes
  end type bnode_data2d

!-------------------------------------------------------------------------------
! Custom data types for 3D output grid

  type node_data
   real(dp) :: x, y, z !Coordinates in xy space
  end type node_data

!-------------------------------------------------------------------------------
! Local variables

 !2D input grid
  type( node_data2d)  , dimension(:), pointer ::  node2d
  type(  elm_data2d)  , dimension(:), pointer ::   elm2d
  type(bnode_data2d)  , dimension(:), pointer :: bound2d
  integer :: nnodes2d, nelms2d, ntria2d, nquad2d, nbound2d

 !3D output grid
  type( node_data), dimension(:)  , pointer :: node
  integer         , dimension(:,:), pointer :: hex, prs, tria, quad, tet
  integer                                   :: nnodes, nhex, nprs, ntria, nquad, nquad_loc

  integer                                   :: ntet

 !Local variables
  integer :: i, j, k, inode1, inode2, os

 !Pointer to the node in the next plane.
  integer, dimension(:,:), pointer :: adjct_node

 character(80) :: filename_boundary_tec, filename_ugrid, filename_mapbc
 character(80) :: filename_su2, filename_vtk, filename_tecplot_v
 character(80) :: datafile_grid_in, datafile_bcmap_in
      real(dp) :: dy, yi, xi, zi, rate
      real(dp) :: dz

 real(dp), dimension(:), allocatable :: xp, yp, zp

 integer :: n1, n2, n3,  n4, n5, n6

 integer, dimension(:,:), pointer :: bmark
 logical ::   boundary_n1n2
 logical ::   boundary_n2n3
 logical ::   boundary_n3n1
 integer :: i_boundary_n1n2
 integer :: i_boundary_n2n3
 integer :: i_boundary_n3n1

 integer :: i_boundary_u1u2
 integer :: i_boundary_u2u3
 integer :: i_boundary_u3u1

 integer :: i_boundary_u4u5
 integer :: i_boundary_u5u6
 integer :: i_boundary_u6u4

 integer               :: kmin
 integer, dimension(6) :: u



 integer               :: n_neg_dual_vol
 integer, dimension(8) :: itemp


   ntet = 0

   write(*,*)
   write(*,*)
   write(*,*) " Note: Make sure you have two input files:"
   write(*,*) "       1. project_name.grid"
   write(*,*) "       2. project_name.bcmap"
   write(*,*)
   write(*,*)

!-------------------------------------------------------------------------------
!
! Read the input parameters, defined in the file named as 'input.nml'.
!
!-------------------------------------------------------------------------------

   write(*,*) "Reading the input file: input_twod2threed.nml..... "
   write(*,*)
   call read_nml_input_parameters('input_twod2threed.nml')
   write(*,*)

!-------------------------------------------------------------------------------
!
! Define input parameters.
!
!-------------------------------------------------------------------------------

   datafile_grid_in = trim(project_name) // ".grid"  ! 2D input grid file name
  datafile_bcmap_in = trim(project_name) // ".bcmap" ! 2D input grid boundary info file name

    if ( big_endian_io(9999) ) then
     write(*,*) 'The system is big Endian'
     write(*,*) ' Ensure big Endian -> setenv F_UFMTENDIAN big'
    else
     write(*,*) 'The system is little Endian'
    endif

    if ( ugrid_binary ) then
     if ( big_endian_io(9999) ) then
      filename_ugrid       = trim(project_name) // "_3d.b8.ugrid"
     else
      filename_ugrid       = trim(project_name) // "_3d.lb8.ugrid"
     end if
    else
      filename_ugrid       = trim(project_name) // "_3d.ugrid"
    endif

     filename_mapbc        = trim(project_name) // "_3d.mapbc"
     filename_boundary_tec = trim(project_name) // "_3d_tec.dat"

     filename_su2          = trim(project_name) // "_3d.su2"
     filename_vtk          = trim(project_name) // "_3d.vtk"

     filename_tecplot_v    = trim(project_name) // "_3d_tec_volume.dat"

!-------------------------------------------------------------------------------
!
! Read a 2D grid in (x,y).
!
! Note: Read two files: "project.grid" and "project.bcmap", and store
!       information in 2D arrays: node2d, elm2d, bound2d, etc.

!-------------------------------------------------------------------------------

 call read_grid


  if (nquad2d > 0 .and. prism2tetra) then

   write(*,*) " Sorry. Cannot use prism2tetra=T for a mixed 2D grid... Use a triangular grid. Stop."
   stop

  else

   if (nquad2d == 0 .and. prism2tetra) then

   write(*,*) " OK, the 3D will be made pure tetrahedral."

   allocate( bmark(nnodes2d,nnodes2d) ) !We'll use this. This can be huge. Need to find a better way...
      bmark = 0
      do i = 1, nbound2d
       do j = 1, bound2d(i)%nbnodes-1
        inode1 = bound2d(i)%bnode(j)
        inode2 = bound2d(i)%bnode(j+1)
        bmark(inode1,inode2) = i
        bmark(inode2,inode1) = i
       end do
      end do

   endif

  endif

!-------------------------------------------------------------------------------
!
! Generate a 3D hex/prismatic grid.
!
!-------------------------------------------------------------------------------

!--------------------------------------------------------------------
! Allocate 3D arrays.

 write(*,*)
 write(*,*) " Estimating the dimensions of arrays..."
 write(*,*)

 nnodes = nnodes2d * n_2dplanes
   nhex =  nquad2d *(n_2dplanes-1)
   nprs =  ntria2d *(n_2dplanes-1)
  ntria =  ntria2d * 2             !Two boundary planes (always).
  nquad =  nquad2d * 2             !Two boundary planes (always).

 !Quad faces generated by extending 2D boundaries to 3D.

   do i = 1, nbound2d
   !                # of quads for i-th boundary  x 3D extension
    nquad = nquad + (bound2d(i)%nbnodes-1)        * (n_2dplanes-1)
   end do

  allocate( node( nnodes) )
  allocate(  hex( nhex,8) )

 ! NOTE: At this point, prism2tetra=T means no quads at all.

 !-----------------------------------
  if (prism2tetra) then

   ntet = 3*nprs
   allocate( tet(ntet,4) )
   nprs = 0

   ntria = ntria + 2*nquad
   nquad = 0

 !-----------------------------------
  else

   ntet = 0
   allocate( prs( nprs,6) )

  endif
 !-----------------------------------

  allocate( tria(ntria,4) )
  allocate( quad(nquad,5) )

 write(*,*)
 write(*,*) ">>> Expected dimensions"
 write(*,*) "     nnodes = ", nnodes
 write(*,*) "       nhex = ", nhex
 write(*,*) "       nprs = ", nprs
 write(*,*) "       ntet = ", ntet
 write(*,*) "      ntria = ", ntria
 write(*,*) "      nquad = ", nquad
 write(*,*)

!--------------------------------------------------------------------
! Generate nodes in 3D - (x,y,z).
! Note: The 2D (x,y) plane is stored as (x,z) plane in the 3D grid.

  write(*,*)
  write(*,*) " Generating nodes in a 3D grid..."
  write(*,*)

  allocate(adjct_node(nnodes2d,n_2dplanes))

 !--------------------------------------------------------------------
 !--------------------------------------------------------------------
 ! Extend 2D grid to 3D!
 !--------------------------------------------------------------------
 !--------------------------------------------------------------------

 !--------------------------------------------------------------------
 !(1)Extend the 2D grid in y direction.
 !--------------------------------------------------------------------
  if (trim(extension_method) == "straight_in_y") then

   dy = (yn-y0)/real(n_2dplanes-1,dp)

   nnodes = 0

   do k = 1, n_2dplanes

     !The 2D grid nodes are copied at every location in y:
      yi = y0 + dy*real(k-1,dp)

    do i = 1, nnodes2d

              nnodes = nnodes + 1
     adjct_node(i,k) = nnodes       !Pointer from the previous plane.

      node(nnodes)%x = node2d(i)%x + dxdy*(yi-y0)
      node(nnodes)%y = yi
      node(nnodes)%z = node2d(i)%y + dzdy*(yi-y0)

    end do

   end do

 !--------------------------------------------------------------------
 !(2)Extend the 2D grid in z direction.
 !--------------------------------------------------------------------
  elseif (trim(extension_method) == "straight_in_z") then

   dz = (zn-z0)/real(n_2dplanes-1,dp)

   nnodes = 0

   do k = 1, n_2dplanes

     !The 2D grid nodes are copied at every location in y:
      zi = z0 + dz*real(k-1,dp)

    do i = 1, nnodes2d

              nnodes = nnodes + 1
     adjct_node(i,k) = nnodes       !Pointer from the previous plane.

      node(nnodes)%x = node2d(i)%x + dxdz*(zi-z0)
      node(nnodes)%y = node2d(i)%y + dydz*(zi-z0)
      node(nnodes)%z = zi

    end do

   end do

 !--------------------------------------------------------------------
 !(3)Rotate the 2D grid around z axis.
 !--------------------------------------------------------------------
  elseif (trim(extension_method) == "rotate_around_z") then

   dy = (rotate_end_angle/180_dp*pi)/real(n_2dplanes-1,dp) !Angle from (x,z) plane at y=0.

   nnodes = 0

   do k = 1, n_2dplanes

      yi = 0.0_dp + dy*real(k-1,dp)        !Current angle
      xi = yi/ (dy*real(n_2dplanes-1,dp))  !Normalized coordiantes xi=[0,1]

    do i = 1, nnodes2d

              nnodes = nnodes + 1
     adjct_node(i,k) = nnodes       !Pointer from the previous plane.

      rate = 1.0_dp + xi*rotate_radius_rate

      node(nnodes)%x = ( rotate_radius*rate + node2d(i)%x ) * cos(yi)
      node(nnodes)%y = ( rotate_radius*rate + node2d(i)%x ) * sin(yi)

    !-----------------------------------------------------------------------
    !-----------------------------------------------------------------------
    !(1)Keep the same z coordinate (flat):
     if     (trim(rotate_z_shape)=="flat") then

      node(nnodes)%z = node2d(i)%y

    !-----------------------------------------------------------------------
    !-----------------------------------------------------------------------
    !(2)Sine-shape
     elseif (trim(rotate_z_shape)=="sine") then

      node(nnodes)%z = node2d(i)%y + sin(rotate_sine_freq*xi)

    !-----------------------------------------------------------------------
    !-----------------------------------------------------------------------
    !(3)Linearly varying
     elseif (trim(rotate_z_shape)=="linear") then

      node(nnodes)%z = node2d(i)%y + xi*rotate_z_zmax

    !-----------------------------------------------------------------------
    !-----------------------------------------------------------------------
    !
     else

      write(*,*) " Invalid input: rotate_z_shape = ", trim(rotate_z_shape)
      stop

     endif
    !-----------------------------------------------------------------------
    !-----------------------------------------------------------------------

    end do

   end do

  endif
 !--------------------------------------------------------------------
 !--------------------------------------------------------------------
 ! End of  Extend 2D grid to 3D!
 !--------------------------------------------------------------------
 !--------------------------------------------------------------------


!--------------------------------------------------------------------
!--------------------------------------------------------------------
! Construct hex/prismatic elements.
!--------------------------------------------------------------------
!--------------------------------------------------------------------

 write(*,*)
 write(*,*) " Generating elements in a 3D grid..."
 write(*,*)

  ntria = 0
  nquad = 0
   nhex = 0
   nprs = 0
   ntet = 0

 !--------------------------------------------------------------------
 ! Hexahedral elements:
 !--------------------------------------------------------------------

  if (nquad2d > 0) then

   do k = 1, n_2dplanes-1
    do i = 1, nquad2d

     nhex = nhex + 1

      !Nodes at kth plane (Note: k=1 is the original 2D grid at y=0)
      hex(nhex,1) = adjct_node(elm2d(ntria2d+i)%vtx(1),k)
      hex(nhex,2) = adjct_node(elm2d(ntria2d+i)%vtx(4),k)
      hex(nhex,3) = adjct_node(elm2d(ntria2d+i)%vtx(3),k)
      hex(nhex,4) = adjct_node(elm2d(ntria2d+i)%vtx(2),k)
      !Nodes at (k+1)st plane (Next plane in y)
      hex(nhex,5) = adjct_node(elm2d(ntria2d+i)%vtx(1),k+1)
      hex(nhex,6) = adjct_node(elm2d(ntria2d+i)%vtx(4),k+1)
      hex(nhex,7) = adjct_node(elm2d(ntria2d+i)%vtx(3),k+1)
      hex(nhex,8) = adjct_node(elm2d(ntria2d+i)%vtx(2),k+1)

    end do
   end do

  endif
 !--------------------------------------------------------------------

 !--------------------------------------------------------------------
 ! Prismatic elements:
 !--------------------------------------------------------------------

  if (.not.prism2tetra) then
   if (ntria2d > 0) then

    do k = 1, n_2dplanes-1
     do i = 1, ntria2d

      n1 = adjct_node(elm2d(i)%vtx(1),k)
      n2 = adjct_node(elm2d(i)%vtx(3),k)
      n3 = adjct_node(elm2d(i)%vtx(2),k)
      n4 = adjct_node(elm2d(i)%vtx(1),k+1)
      n5 = adjct_node(elm2d(i)%vtx(3),k+1)
      n6 = adjct_node(elm2d(i)%vtx(2),k+1)

      nprs = nprs + 1

      !Nodes at kth plane (Note: k=1 is the original 2D grid at y=0)
      prs(nprs,1) = adjct_node(elm2d(i)%vtx(1),k)
      prs(nprs,2) = adjct_node(elm2d(i)%vtx(3),k)
      prs(nprs,3) = adjct_node(elm2d(i)%vtx(2),k)
      !Nodes at (k+1)st plane (Next plane in y)
      prs(nprs,4) = adjct_node(elm2d(i)%vtx(1),k+1)
      prs(nprs,5) = adjct_node(elm2d(i)%vtx(3),k+1)
      prs(nprs,6) = adjct_node(elm2d(i)%vtx(2),k+1)

     end do
    end do

   endif
  endif
 !--------------------------------------------------------------------

 !--------------------------------------------------------------------
 ! Tetrahedral elements:
 !  Subdivide the prism into 3 tetrahedra.
 !  "How to Subdivide Pyramids, Prisms and Hexahedra into Tetrahedra",
 !  Julien Dompierre Paul Labb©ß Marie-Gabrielle Vallet Ricardo Camarero
 !  Rapport CERCA R99£ü78,1999. We're using only the prism subdivision below.
 !
 ! In this case, boundary information needs to be collected, which is
 ! best done at this stage.
 !--------------------------------------------------------------------

  if (prism2tetra) then
   if (ntria2d > 0) then

   do i = 1, ntria2d

       i_boundary_n1n2 = 0
       i_boundary_n2n3 = 0
       i_boundary_n3n1 = 0

       n1 = adjct_node(elm2d(i)%vtx(1),1)
       n2 = adjct_node(elm2d(i)%vtx(3),1)
       n3 = adjct_node(elm2d(i)%vtx(2),1)

       if (bmark(n1,n2) > 0) then
           boundary_n1n2 = .true.
         i_boundary_n1n2 = bmark(n1,n2)
       endif

       if (bmark(n2,n3) > 0) then
           boundary_n2n3 = .true.
         i_boundary_n2n3 = bmark(n2,n3)
       endif

       if (bmark(n3,n1) > 0) then
           boundary_n3n1 = .true.
         i_boundary_n3n1 = bmark(n3,n1)
       endif

    do k = 1, n_2dplanes-1

       i_boundary_u1u2 = 0
       i_boundary_u2u3 = 0
       i_boundary_u3u1 = 0

       i_boundary_u4u5 = 0
       i_boundary_u5u6 = 0
       i_boundary_u6u4 = 0

     n1 = adjct_node(elm2d(i)%vtx(1),k)
     n2 = adjct_node(elm2d(i)%vtx(3),k)
     n3 = adjct_node(elm2d(i)%vtx(2),k)
     n4 = adjct_node(elm2d(i)%vtx(1),k+1)
     n5 = adjct_node(elm2d(i)%vtx(3),k+1)
     n6 = adjct_node(elm2d(i)%vtx(2),k+1)

     !Reorder such that u(1) = min(n1,n2,n3,n4,n5,n6)
         u = (/ n1,n2,n3,n4,n5,n6 /)
      kmin = minloc(u, dim=1)

     if     (kmin==1) then

      u = (/ n1,n2,n3,n4,n5,n6 /)
      if (i_boundary_n1n2 > 0) i_boundary_u1u2 = i_boundary_n1n2
      if (i_boundary_n2n3 > 0) i_boundary_u2u3 = i_boundary_n2n3
      if (i_boundary_n3n1 > 0) i_boundary_u3u1 = i_boundary_n3n1

     elseif (kmin==2) then

      u = (/ n2,n3,n1,n5,n6,n4 /)
      if (i_boundary_n1n2 > 0) i_boundary_u3u1 = i_boundary_n1n2
      if (i_boundary_n2n3 > 0) i_boundary_u1u2 = i_boundary_n2n3
      if (i_boundary_n3n1 > 0) i_boundary_u2u3 = i_boundary_n3n1

     elseif (kmin==3) then

      u = (/ n3,n1,n2,n6,n4,n5 /)
      if (i_boundary_n1n2 > 0) i_boundary_u2u3 = i_boundary_n1n2
      if (i_boundary_n2n3 > 0) i_boundary_u3u1 = i_boundary_n2n3
      if (i_boundary_n3n1 > 0) i_boundary_u1u2 = i_boundary_n3n1

     elseif (kmin==4) then

      u = (/ n4,n6,n5,n1,n3,n2 /)
      if (i_boundary_n1n2 > 0) i_boundary_u6u4 = i_boundary_n1n2
      if (i_boundary_n2n3 > 0) i_boundary_u5u6 = i_boundary_n2n3
      if (i_boundary_n3n1 > 0) i_boundary_u4u5 = i_boundary_n3n1

     elseif (kmin==5) then

      u = (/ n5,n4,n6,n2,n1,n3 /)
      if (i_boundary_n1n2 > 0) i_boundary_u4u5 = i_boundary_n1n2
      if (i_boundary_n2n3 > 0) i_boundary_u6u4 = i_boundary_n2n3
      if (i_boundary_n3n1 > 0) i_boundary_u5u6 = i_boundary_n3n1

     elseif (kmin==6) then

      u = (/ n6,n5,n4,n3,n2,n1 /)
      if (i_boundary_n1n2 > 0) i_boundary_u5u6 = i_boundary_n1n2
      if (i_boundary_n2n3 > 0) i_boundary_u4u5 = i_boundary_n2n3
      if (i_boundary_n3n1 > 0) i_boundary_u6u4 = i_boundary_n3n1

     endif

    !-----------------------------------------------------
    ! Tetra 1

              ntet = ntet + 1
       tet(ntet,1) = u(1)
       tet(ntet,2) = u(5)
       tet(ntet,3) = u(6)
       tet(ntet,4) = u(4)

      if (i_boundary_u1u2 > 0 .or. i_boundary_u4u5 > 0) then
       ntria = ntria + 1
       tria(ntria,1) = u(1)
       tria(ntria,2) = u(5)
       tria(ntria,3) = u(2)
       tria(ntria,4) = max( i_boundary_u1u2, i_boundary_u4u5 ) + 2
       ntria = ntria + 1
       tria(ntria,1) = u(1)
       tria(ntria,2) = u(4)
       tria(ntria,3) = u(5)
       tria(ntria,4) = max( i_boundary_u1u2, i_boundary_u4u5 ) + 2
      endif

      if (i_boundary_u3u1 > 0 .or. i_boundary_u6u4 > 0) then
       ntria = ntria + 1
       tria(ntria,1) = u(1)
       tria(ntria,2) = u(3)
       tria(ntria,3) = u(6)
       tria(ntria,4) = max( i_boundary_u3u1, i_boundary_u6u4 ) + 2
       ntria = ntria + 1
       tria(ntria,1) = u(1)
       tria(ntria,2) = u(6)
       tria(ntria,3) = u(4)
       tria(ntria,4) = max( i_boundary_u3u1, i_boundary_u6u4 ) + 2
      endif

    !-----------------------------------------------------
    ! Case 1: Tetra 2 and 3

     if ( min( u(2), u(6) ) < min( u(3), u(5) ) ) then

              ntet = ntet + 1
       tet(ntet,1) = u(1)
       tet(ntet,2) = u(2)
       tet(ntet,3) = u(3)
       tet(ntet,4) = u(6)

              ntet = ntet + 1
       tet(ntet,1) = u(1)
       tet(ntet,2) = u(2)
       tet(ntet,3) = u(6)
       tet(ntet,4) = u(5)

      if (i_boundary_u2u3 > 0 .or. i_boundary_u5u6 > 0) then
       ntria = ntria + 1
       tria(ntria,1) = u(2)
       tria(ntria,2) = u(6)
       tria(ntria,3) = u(3)
       tria(ntria,4) = max( i_boundary_u2u3, i_boundary_u5u6 ) + 2
       ntria = ntria + 1
       tria(ntria,1) = u(2)
       tria(ntria,2) = u(5)
       tria(ntria,3) = u(6)
       tria(ntria,4) = max( i_boundary_u2u3, i_boundary_u5u6 ) + 2
      endif

    !-----------------------------------------------------
    ! Case 2: Tetra 2 and 3

     else

              ntet = ntet + 1
       tet(ntet,1) = u(1)
       tet(ntet,2) = u(2)
       tet(ntet,3) = u(3)
       tet(ntet,4) = u(5)

              ntet = ntet + 1
       tet(ntet,1) = u(1)
       tet(ntet,2) = u(5)
       tet(ntet,3) = u(3)
       tet(ntet,4) = u(6)

      if (i_boundary_u2u3 > 0 .or. i_boundary_u5u6 > 0) then
       ntria = ntria + 1
       tria(ntria,1) = u(2)
       tria(ntria,2) = u(5)
       tria(ntria,3) = u(3)
       tria(ntria,4) = max( i_boundary_u2u3, i_boundary_u5u6 ) + 2
       ntria = ntria + 1
       tria(ntria,1) = u(3)
       tria(ntria,2) = u(5)
       tria(ntria,3) = u(6)
       tria(ntria,4) = max( i_boundary_u2u3, i_boundary_u5u6 ) + 2
      endif

     endif
    !-----------------------------------------------------

    end do
   end do

   endif
  endif
 !--------------------------------------------------------------------
 ! End of tetra
 !--------------------------------------------------------------------

!--------------------------------------------------------------------
!--------------------------------------------------------------------
! Define boundary elements.
! Note: Nodes are ordered so that the boundary face points INWARD.
! Note: Triangular boundaries for pure tet has already been done in the above.
!--------------------------------------------------------------------
!--------------------------------------------------------------------

 write(*,*)
 write(*,*) " Generating boundary elements in a 3D grid..."
 write(*,*)

 !2D-grid boundaries:

  !-----------------------------------------------
  ! 2D-plane Boundary 1: (x,z)-plane at y=y0.
  ! This is the original input 2D grid.
  !----------------------------------------------------

   ! Triangular faces:
   do i = 1, ntria2d
    ntria = ntria + 1
    tria(ntria,1) = elm2d(i)%vtx(1)
    tria(ntria,2) = elm2d(i)%vtx(3)
    tria(ntria,3) = elm2d(i)%vtx(2)
    tria(ntria,4) = 1
   end do

   ! Quadrilateral faces:
   do i = 1, nquad2d
    nquad = nquad + 1
    quad(nquad,1) = elm2d(ntria2d+i)%vtx(1)
    quad(nquad,2) = elm2d(ntria2d+i)%vtx(4)
    quad(nquad,3) = elm2d(ntria2d+i)%vtx(3)
    quad(nquad,4) = elm2d(ntria2d+i)%vtx(2)
    quad(nquad,5) = 1
   end do

  !-----------------------------------------------
  ! 2D-plane Boundary 2: (x,z)-plane at y=yn.
  ! This is the copy of the original input 2D grid at the end place.
  !----------------------------------------------------

   ! Triangular faces:
   do i = 1, ntria2d
    ntria = ntria + 1
    tria(ntria,1) = adjct_node(elm2d(i)%vtx(1),n_2dplanes)
    tria(ntria,2) = adjct_node(elm2d(i)%vtx(2),n_2dplanes)
    tria(ntria,3) = adjct_node(elm2d(i)%vtx(3),n_2dplanes)
    tria(ntria,4) = 2
   end do

   ! Quadrilateral faces:
   do i = 1, nquad2d
    nquad = nquad + 1
    quad(nquad,1) = adjct_node(elm2d(ntria2d+i)%vtx(1),n_2dplanes)
    quad(nquad,2) = adjct_node(elm2d(ntria2d+i)%vtx(2),n_2dplanes)
    quad(nquad,3) = adjct_node(elm2d(ntria2d+i)%vtx(3),n_2dplanes)
    quad(nquad,4) = adjct_node(elm2d(ntria2d+i)%vtx(4),n_2dplanes)
    quad(nquad,5) = 2
   end do

  !----------------------------------------------------
  ! Boundaries generated by extending 2D boundaries.
  !----------------------------------------------------

   if (.not.prism2tetra) then

     do k = 1, n_2dplanes-1
      do i = 1, nbound2d
        nquad_loc = 0
       do j = 1, bound2d(i)%nbnodes-1
        inode1 = bound2d(i)%bnode(j)
        inode2 = bound2d(i)%bnode(j+1)
        nquad     = nquad     + 1
        nquad_loc = nquad_loc + 1

          quad(nquad,1) = adjct_node(inode1,k)
          quad(nquad,2) = adjct_node(inode2,k)
          quad(nquad,3) = adjct_node(inode2,k+1)
          quad(nquad,4) = adjct_node(inode1,k+1)
          quad(nquad,5) = i + 2  ! 2 boundaries already defined for triangular planes.
       end do
   !   write(*,*) " plane k = ", k, " ibound = ", i, " nquad_loc = ", nquad_loc
      end do
   !    write(*,*)
     end do

   endif
  !----------------------------------------------------
  !-----------------------------------------------



!--------------------------------------------------------------------
!--------------------------------------------------------------------
! End of Define boundary elements.
!--------------------------------------------------------------------
!--------------------------------------------------------------------

 write(*,*)
 write(*,*) ">>> Resulting dimensions"
 write(*,*) "     nnodes = ", nnodes
 write(*,*) "       nprs = ", nprs
 write(*,*) "       nhex = ", nhex
 write(*,*) "       ntet = ", ntet
 write(*,*) "      ntria = ", ntria
 write(*,*) "      nquad = ", nquad
 write(*,*)

 write(*,*)
 write(*,*) " 3D grid generated..."
 write(*,*)



!*******************************************************************************
! Fix the orientation.
!
! Note: The code extends a 2D grid in the direction that defines a left-handed
!       coordinate system (it was originally written this way...).
!       I guess it was because I wanted to use a 2D grid in (x,z) plane for some
!       initial target applications. But then I realize that I want to extend
!       a 2D (x,y) grid in the z-direction in some applications. 
!       So, in the case of the z-extension, a 2D grid is extended in the
!       opposite direction (right handed). So, all elements need to be reversed.
!*******************************************************************************

  fix_orientation_z : if (trim(extension_method) == "straight_in_z") then

   write(*,*) " Fix the orientation... Reverse the order! "


   if (ntet > 0) then
    do i = 1, ntet
     itemp(1:4) = tet(i,:)
       tet(i,1) = itemp(3)
       tet(i,2) = itemp(2)
       tet(i,3) = itemp(1)
       tet(i,4) = itemp(4)
    end do
   endif

   if (nprs > 0) then
    do i = 1, nprs
     itemp(1:6) = prs(i,:)
       prs(i,1) = itemp(3)
       prs(i,2) = itemp(2)
       prs(i,3) = itemp(1)
       prs(i,4) = itemp(6)
       prs(i,5) = itemp(5)
       prs(i,6) = itemp(4)
    end do
   endif

   if (nhex > 0) then
    do i = 1, nhex
     itemp(1:8) = hex(i,:)
       hex(i,1) = itemp(4)
       hex(i,2) = itemp(3)
       hex(i,3) = itemp(2)
       hex(i,4) = itemp(1)
       hex(i,5) = itemp(8)
       hex(i,6) = itemp(7)
       hex(i,7) = itemp(6)
       hex(i,8) = itemp(5)
    end do
   endif

   if (nquad > 0) then
    do i = 1, nquad
     itemp(1:5) = quad(i,:)
       quad(i,1) = itemp(4)
       quad(i,2) = itemp(3)
       quad(i,3) = itemp(2)
       quad(i,4) = itemp(1)
       quad(i,5) = itemp(5)
    end do
   endif

   if (ntria > 0) then
    do i = 1, ntria
     itemp(1:4) = tria(i,:)
       tria(i,1) = itemp(3)
       tria(i,2) = itemp(2)
       tria(i,3) = itemp(1)
       tria(i,4) = itemp(4)
    end do
   endif


  endif fix_orientation_z

!*******************************************************************************
! Change y and z if requested. We perform this without changing the orientation.
!  x -> y
!  z -> x
!  y -> z
!*******************************************************************************

   if (switch_y_and_z) then

    do i = 1, nnodes

     xi = node(i)%x
     yi = node(i)%y

     node(i)%x = node(i)%z
     node(i)%y = xi
     node(i)%z = yi

    end do

   endif

!*******************************************************************************
! Check the tetra volume. Yes, tetra only for now...
!*******************************************************************************

  n_neg_dual_vol = 0

  do i = 1, ntet
   if ( tet_volume( node(tet(i,1))%x, node(tet(i,2))%x, node(tet(i,3))%x, node(tet(i,4))%x,       &
                    node(tet(i,1))%y, node(tet(i,2))%y, node(tet(i,3))%y, node(tet(i,4))%y,       &
                    node(tet(i,1))%z, node(tet(i,2))%z, node(tet(i,3))%z, node(tet(i,4))%z ) < zero ) then
     n_neg_dual_vol = n_neg_dual_vol + 1
   endif
  end do

  if ( n_neg_dual_vol > 0 ) then
   write(*,*) " n_neg_dual_vol = ", n_neg_dual_vol
   stop
  endif

!*******************************************************************************
! Just for convenience...
!*******************************************************************************

  allocate( xp(nnodes), yp(nnodes), zp(nnodes) )
  do i = 1, nnodes
   xp(i) = node(i)%x
   yp(i) = node(i)%y
   zp(i) = node(i)%z
  end do

!*******************************************************************************
! Write a Tecplot boundary grid file for viewing. Just for viewing.
!******************************************************************************

 if (generate_tec_file_b) then

 write(*,*)
 write(*,*) " Writing a Tecplot file for the boudnary grid..."
 write(*,*)

 open(unit=4, file=filename_boundary_tec, status="unknown", iostat=os)

  write(4,*) 'title = "grid boundary"'
  write(4,*) 'variables = "x","y","z"'
  write(4,*) 'zone  n=', nnodes,',e=', ntria+nquad,', et=quadrilateral, f=fepoint'

  do i = 1, nnodes
    write(4,'(3es27.15)') xp(i), yp(i), zp(i)
  end do

  do i = 1, ntria
   write(4,'(4i10)') tria(i,1), tria(i,2), tria(i,3), tria(i,1)
  end do

  do i = 1, nquad
   write(4,'(4i10)') quad(i,1), quad(i,2), quad(i,3), quad(i,4)
  end do

 close(4)

 endif

!*******************************************************************************
! Write a UGRID file: a grid file for a solver.
!*******************************************************************************

 if (generate_ugrid_file) then

 write(*,*)
 write(*,*) " Writing UGRID file..."
 write(*,*)

  if ( ugrid_binary ) then
    open(unit=2, file=filename_ugrid, form='unformatted',access="stream",&
                                      status='unknown', iostat=os )
    write(2) nnodes,   ntria,    nquad,   ntet, 0, nprs, nhex
  else
    open(unit=2, file=filename_ugrid, status="unknown", iostat=os)
    !                  #nodes, #tri_faces, #quad_faces, #tetra, #pyr, #prz,
    !                    #hex
    write(2,'(7I20)') nnodes,   ntria,    nquad,   ntet, 0, nprs, nhex
  endif

 !--------------------------------------------------------------------
  binary : if ( ugrid_binary ) then

  ! Nodal coordinates
   do i = 1, nnodes
    write(2) xp(i), yp(i), zp(i) !node(i)%x, node(i)%y, node(i)%z
   end do

  ! Tria boundary faces
   do i = 1, ntria
    write(2) tria(i,1), tria(i,2), tria(i,3)
   end do

  ! Quad boundary faces
   do i = 1, nquad
    write(2) quad(i,1), quad(i,2), quad(i,3), quad(i,4)
   end do

  ! Face tag: Boundary group number

   do i = 1, ntria
    write(2) tria(i,4)
   end do

   do i = 1, nquad
    write(2) quad(i,5)
   end do

  ! Tetra
   do i = 1, ntet
   write(2) tet(i,1), tet(i,2), tet(i,3), tet(i,4)
   end do

  ! Prisms
   do i = 1, nprs
   write(2) prs(i,1), prs(i,2), prs(i,3), &
            prs(i,4), prs(i,5), prs(i,6)
   end do

  ! Hexadehra
   do i = 1, nhex
   write(2) hex(i,1), hex(i,2), hex(i,3), hex(i,4), &
            hex(i,5), hex(i,6), hex(i,7), hex(i,8)
   end do

 !--------------------------------------------------------------------
   else
 !--------------------------------------------------------------------

  ! Nodal coordinates
   do i = 1, nnodes
    write(2,'(3es27.15)') xp(i), yp(i), zp(i) !node(i)%x, node(i)%y, node(i)%z
   end do

  ! Tria boundary faces
   do i = 1, ntria
    write(2,'(3i10)') tria(i,1), tria(i,2), tria(i,3)
   end do

  ! Quad boundary faces
   do i = 1, nquad
    write(2,'(4i10)') quad(i,1), quad(i,2), quad(i,3), quad(i,4)
   end do

  ! Face tag: Boundary group number

   do i = 1, ntria
    write(2,'(i10)') tria(i,4)
   end do

   do i = 1, nquad
    write(2,'(i10)') quad(i,5)
   end do

  ! Tetra
   do i = 1, ntet
   write(2,'(4i10)') tet(i,1), tet(i,2), tet(i,3), tet(i,4)
   end do

  ! Prisms
   do i = 1, nprs
   write(2,'(6i10)') prs(i,1), prs(i,2), prs(i,3), &
                     prs(i,4), prs(i,5), prs(i,6)
   end do

  ! Hexadehra
   do i = 1, nhex
   write(2,'(8i10)') hex(i,1), hex(i,2), hex(i,3), hex(i,4), &
                     hex(i,5), hex(i,6), hex(i,7), hex(i,8)
   end do


  endif binary
 !--------------------------------------------------------------------

  close(2)

 endif

!*******************************************************************************
! Write a boundary condition map file: boundary marks
! Note: Set appropriate boundary condition numbers in this file.
!
! Note: This simply writes a file with some BC names.
!       It msut be edited manually for a flow solver.
!*******************************************************************************

 write(*,*)
 write(*,*) " Writing mapbc file... ", trim(filename_mapbc)
 write(*,*)

 open(unit=3, file=filename_mapbc, status="unknown", iostat=os)

   write(3,'(i10,a48)') nbound2d+2, " !Number of boundary parts (boundary conditions)"
   write(3,*) 1, "symmetry_0"
   write(3,*) 2, "symmetry_n"

  do i = 1, nbound2d
   write(3,*) i+2, trim(bound2d(i)%bc_type)
  end do

 close(3)

 write(*,*)
 write(*,*) " Note: You need to edit the mapbc file for your solver."
 write(*,*)

!*******************************************************************************

!-------------------------------------------------------------------------------
!
! Tecplot volume file if requested.
!
!-------------------------------------------------------------------------------

  if (generate_tec_v) then
   call write_tecplot_volume_file
  endif

!-------------------------------------------------------------------------------
!
! Generate a .su2 file for SU2 solver.
!
!-------------------------------------------------------------------------------

  if (generate_su2_file) then

  write(*,*)
  write(*,*) " Writing .su2 file... ", trim(filename_su2)
  write(*,*)

  call write_su2grid_file(filename_su2, nnodes,xp,yp,zp, ntet,tet, nprs,prs, &
                                             nhex,hex, ntria,tria, nquad,quad )

  endif

!-------------------------------------------------------------------------------
!
! Generate a .vtk file.
!
!-------------------------------------------------------------------------------

  if (generate_vtk_file) then

  write(*,*)
  write(*,*) " Writing .vtk file... ", trim(filename_vtk)
  write(*,*)

  call write_vtk_file(filename_vtk, nnodes,xp,yp,zp, ntet,tet, nprs,prs, nhex,hex )

  endif

!-------------------------------------------------------------------------------
!
!-------------------------------------------------------------------------------

  write(*,*)
  write(*,*)
  write(*,*) "Output:   mapbc file = ", trim(filename_mapbc)
  if (generate_tec_file_b) write(*,*) "Output: Tecplot file = ", trim(filename_boundary_tec)
  if (generate_ugrid_file) write(*,*) "Output:   UGRID file = ", trim(filename_ugrid)
  if (generate_su2_file)   write(*,*) "Output:    .su2 file = ", trim(filename_su2)
  if (generate_vtk_file)   write(*,*) "Output:    .vtk file = ", trim(filename_vtk)
  write(*,*)
  write(*,*)
  write(*,*) " 3D grid successfully generated. Done."
  write(*,*)

  stop

 contains

!********************************************************************************
!* Read a 2D grid file.
!*
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
!*   NOTE: bc_name is the name of the boundary condition.
!*         Only four BCs are available in this version:
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
 subroutine read_grid

 implicit none

!Local variables
 integer  :: i, j, os, dummy_int

!--------------------------------------------------------------------------------
! 1. Read grid file>: datafile_grid_in

  write(*,*) "-----------------------------------------------------------"
  write(*,*) " Reading the 2D grid file....", datafile_grid_in

!  Open the input file.
   open(unit=1, file=datafile_grid_in, status="unknown", iostat=os)

! READ: Get the size of the grid.
  read(1,*) nnodes2d, ntria2d, nquad2d
  nelms2d = ntria2d + nquad2d

!  Allocate node and element arrays.
   allocate(node2d(nnodes2d))
   allocate(elm2d(  nelms2d))

! READ: Read the nodal coordinates
  do i = 1, nnodes2d
   read(1,*) node2d(i)%x, node2d(i)%y
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
  if ( ntria2d > 0 ) then
   do i = 1, ntria2d
    elm2d(i)%nvtx = 3
    allocate(elm2d(i)%vtx(3))
    read(1,*) elm2d(i)%vtx(1), elm2d(i)%vtx(2), elm2d(i)%vtx(3)
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
  if ( nquad2d > 0 ) then
   do i = 1, nquad2d
    elm2d(ntria2d+i)%nvtx = 4
    allocate( elm2d(ntria2d+i)%vtx(4))
    read(1,*) elm2d(ntria2d+i)%vtx(1), elm2d(ntria2d+i)%vtx(2), &
              elm2d(ntria2d+i)%vtx(3), elm2d(ntria2d+i)%vtx(4)
   end do
  endif

!  Write out the grid data.

   write(*,*) " Total numbers:"
   write(*,*) "      nodes = ", nnodes2d
   write(*,*) "  triangles = ", ntria2d
   write(*,*) "      quads = ", nquad2d
   write(*,*)

! Read the boundary grid data

! READ: Number of boundary condition types
  read(1,*) nbound2d
  allocate(bound2d(nbound2d))

! READ: Number of Boundary nodes (including the starting one at the end if
! it is closed such as an airfoil.)
  do i = 1, nbound2d
   read(1,*) bound2d(i)%nbnodes
   allocate(bound2d(i)%bnode(bound2d(i)%nbnodes))
  end do

! READ: Read boundary nodes
  do i = 1, nbound2d
   do j = 1, bound2d(i)%nbnodes
   read(1,*) bound2d(i)%bnode(j)
   end do
  end do

!  Print the boundary grid data.
   write(*,*) " Boundary nodes:"
   write(*,*) "    segments = ", nbound2d
    do i = 1, nbound2d
     write(*,'(a9,i3,2(a11,i5))') " boundary", i, "  bnodes = ", bound2d(i)%nbnodes, &
                                                  "  bfaces = ", bound2d(i)%nbnodes-1
    end do
   write(*,*)

  close(1)

! End of Read grid file>: datafile_grid_in
!--------------------------------------------------------------------------------

!--------------------------------------------------------------------------------
! 2. Read the boundary condition data file

   write(*,*) "Reading the boundary condition file....", datafile_bcmap_in

! Open the input file.
  open(unit=2, file=datafile_bcmap_in, status="unknown", iostat=os)

  if (os/=0) then
   write(*,*) "The file ", datafile_bcmap_in, " is not available?"
   stop
  endif

    read(2,*) 

! READ: Read the boundary condition type
  do i = 1, nbound2d
    read(2,*) dummy_int, bound2d(i)%bc_type
   end do

!  Print the data
    write(*,*) " Boundary conditions:"
   do i = 1, nbound2d
    write(*,'(a9,i3,a12,a35)') " boundary", i, "  bc_type = ", trim(bound2d(i)%bc_type)
   end do

    i = dummy_int !Never mind. Just to avoid a compilation warning.

    write(*,*)

  close(2)

! End of Read the boundary condition data file
!--------------------------------------------------------------------------------

 write(*,*) "-----------------------------------------------------------"

 end subroutine read_grid


!--------------------------------------------------------------------------------
! big_endian?
!--------------------------------------------------------------------------------
 function big_endian_io( opt_unit )

 integer, intent(in) :: opt_unit
 logical             :: big_endian_io

! one-byte integer
 integer, parameter :: i1 = selected_int_kind(2)

! two-byte integer
 integer, parameter :: i2 = selected_int_kind(4)
 integer(i1)        :: byte_one, byte_two

! 00000000 00000001 big-endian binary
 integer(i2)        :: two_byte_int = 1_i2

    open(opt_unit,status='scratch',form='unformatted')
      write( opt_unit) two_byte_int
      rewind(opt_unit)
      read(  opt_unit) byte_one, byte_two
    close(opt_unit)
    big_endian_io = ( byte_one == 0 .and. byte_two == 1 )

 end function big_endian_io
!--------------------------------------------------------------------------------


!*******************************************************************************
! This subroutine writes a su2 grid file.
!
! Note: Nodes -> i = 0,1,2,...; Elements -> i = 0,1,2,...
!
!*******************************************************************************
 subroutine write_su2grid_file(filename, nnodes,xp,yp,zp, ntet,tet, nprs,prs, &
                                             nhex,hex, ntria,tria, nquad,quad )

  character(80),                 intent(in) :: filename
  integer      ,                 intent(in) :: nnodes
  integer      ,                 intent(in) :: ntet, nprs, nhex
  integer      ,                 intent(in) :: ntria, nquad
  real(dp)     , dimension(:  ), intent(in) :: xp, yp, zp
  integer      , dimension(:,:), intent(in) :: tria
  integer      , dimension(:,:), intent(in) :: quad
  integer      , dimension(:,:), intent(in) :: tet
  integer      , dimension(:,:), intent(in) :: prs
  integer      , dimension(:,:), intent(in) :: hex


  integer :: k, itag, i, ib

  open(unit=7, file=filename, status="unknown", iostat=os)

  write(7,*) "%"
  write(7,*) "% Problem dimension"
  write(7,*) "%"
  write(7,5) 3
5 format('NDIME= ',i12)

   write(7,*) "%"
   write(7,*) "% Inner element connectivity"
   k = ntet + nprs + nhex
   write(7,10) k
   write(*,10) k
10 format('NELEM= ',i12)

   k = 0

 !-------------------------------------------------------------------------
 ! Elements

  ! tet
    if (ntet > 0) then
     do i = 1, ntet
      write(7,'(6i20)') 10, tet(i,1)-1, tet(i,2)-1, tet(i,3)-1, tet(i,4)-1, k
      k = k + 1
     end do
    endif

  ! Prism: Orietation is reversed (See VTK format).
    if (nprs > 0) then
     do i = 1, nprs
      write(7,'(8i20)') 13, prs(i,3)-1, prs(i,2)-1, prs(i,1)-1, &
                            prs(i,6)-1, prs(i,5)-1, prs(i,4)-1, k
      k = k + 1
     end do
    endif

  ! Hex
    if (nhex > 0) then
     do i = 1, nhex
      write(7,'(10i20)') 12, hex(i,1)-1, hex(i,2)-1, hex(i,3)-1, hex(i,4)-1, &
                             hex(i,5)-1, hex(i,6)-1, hex(i,7)-1, hex(i,8)-1, k
      k = k + 1
     end do
    endif

   write(*,*) "  --- elm check", ntet + nprs + nhex, k

 !--------------------------------------------------------------------------
 ! Nodes

   write(7,*) "%"
   write(7,*) "% Node coordinates"
   write(7,*) "%"
   write(7,20) nnodes
20 format('NPOIN= ', i12)

   k = 0

  ! Nodes
    do i = 1, nnodes
     write(7,'(3es26.15,i20)')  xp(i), yp(i), zp(i) !node(i)%x, node(i)%y, node(i)%z, k
      k = k + 1
    end do

   write(*,*) "  --- node check", nnodes, k

 !--------------------------------------------------------------------------
 ! Boundary

    write(7,*) "%"
    write(7,*) "% Boundary elements"
    write(7,*) "%"
    write(7,30) nbound2d+2
30 format('NMARK= ',i12)

40 format('MARKER_TAG= ',a)
50 format('MARKER_ELEMS= ', i12)

   write(*,*)

 !--------------------------------------------------------------------------
 ! (1) (x,z)-plane at y=y0
 !--------------------------------------------------------------------------

   write(7,40) "symmetry_0"
   write(*,40) "symmetry_0"

   itag = 1
      k = 0

   ! Triangular faces = ntri
     if (ntria > 0) then
      do i = 1, ntria
       if ( tria(i,4) == itag ) k = k + 1
      end do
     endif

   ! Quad faces = nquad
     if (nquad > 0) then
      do i = 1, nquad
       if ( quad(i,5) == itag ) k = k + 1
      end do
     endif

   write(7,50) k

   ! Triangular faces = ntri
     if (ntria > 0) then
      do i = 1, ntria
       if ( tria(i,4) == itag ) write(7,'(4i20)') 5, tria(i,1)-1, tria(i,2)-1, tria(i,3)-1
      end do
     endif

   ! Quad faces = nquad
     if (nquad > 0) then
      do i = 1, nquad
       if ( quad(i,5) == itag ) write(7,'(5i20)') 9, quad(i,1)-1, quad(i,2)-1, quad(i,3)-1, quad(i,4)-1
      end do
     endif

   write(*,*) "    ---> symmetry_0 ", ": ntria+nquad=", k

 !--------------------------------------------------------------------------
 ! (2) (x,z)-plane at y=yn
 !--------------------------------------------------------------------------

   write(7,40) "symmetry_n"
   write(*,40) "symmetry_n"

   itag = 2
      k = 0

   ! Triangular faces = ntri
     if (ntria > 0) then
      do i = 1, ntria
       if ( tria(i,4) == itag ) k = k + 1
      end do
     endif

   ! Quad faces = nquad
     if (nquad > 0) then
      do i = 1, nquad
       if ( quad(i,5) == itag ) k = k + 1
      end do
     endif

   write(7,50) k

   ! Triangular faces = ntri
     if (ntria > 0) then
      do i = 1, ntria
       if ( tria(i,4) == itag ) write(7,'(4i20)') 5, tria(i,1)-1, tria(i,2)-1, tria(i,3)-1
      end do
     endif

   ! Quad faces = nquad
     if (nquad > 0) then
      do i = 1, nquad
       if ( quad(i,5) == itag ) write(7,'(5i20)') 9, quad(i,1)-1, quad(i,2)-1, quad(i,3)-1, quad(i,4)-1
      end do
     endif

   write(*,*) "    ---> symmetry_n ", ": ntria+nquad=", k

 !--------------------------------------------------------------------------
 ! Boundaries from 2D grid
 !--------------------------------------------------------------------------

  do ib = 1, nbound2d

   write(7,40) trim(bound2d(ib)%bc_type)
   write(*,40) trim(bound2d(ib)%bc_type)

   itag = ib + 2
      k = 0

   ! Triangular faces = ntri
     if (ntria > 0) then
      do i = 1, ntria
       if ( tria(i,4) == itag ) k = k + 1
      end do
     endif

   ! Quad faces = nquad
     if (nquad > 0) then
      do i = 1, nquad
       if ( quad(i,5) == itag ) k = k + 1
      end do
     endif

   write(7,50) k

   ! Triangular faces = ntri
     if (ntria > 0) then
      do i = 1, ntria
       if ( tria(i,4) == itag ) write(7,'(4i20)') 5, tria(i,1)-1, tria(i,2)-1, tria(i,3)-1
      end do
     endif

   ! Quad faces = nquad
     if (nquad > 0) then
      do i = 1, nquad
       if ( quad(i,5) == itag ) write(7,'(5i20)') 9, quad(i,1)-1, quad(i,2)-1, quad(i,3)-1, quad(i,4)-1
      end do
     endif

   write(*,*) "    ---> ", trim(bound2d(ib)%bc_type), ": ntria+nquad=", k

  end do

 !--------------------------------------------------------------------------
 !--------------------------------------------------------------------------

  close(7)

 end subroutine write_su2grid_file
!********************************************************************************

!*******************************************************************************
! This subroutine writes a .vtk file for the grid whose name is defined by
! filename_vtk.
!
!  Identifier:
!  Line          3
!  Triangle      5
!  Quadrilateral 9
!  Tetrahedral  10
!  Hexahedral   12
!  Prism        13
!  Pyramid      14
!
! Note: This version is only for tet, prs, and hex. Need to add pyramids and others
!       if needed.
!
! Use Paraview to read .vtk and visualize it.  https://www.paraview.org
!
! Search in Google for 'vkt format' to learn .vtk file format.
!*******************************************************************************
 subroutine write_vtk_file(filename, nnodes,xp,yp,zp, ntet,tet, nprs,prs, nhex,hex )

  implicit none

  character(80),                 intent(in) :: filename
  integer      ,                 intent(in) :: nnodes
  real(dp)     , dimension(:  ), intent(in) :: xp, yp, zp
  integer      ,                 intent(in) :: ntet, nprs, nhex
  integer      , dimension(:,:), intent(in) :: tet
  integer      , dimension(:,:), intent(in) :: prs
  integer      , dimension(:,:), intent(in) :: hex

!Local variables
  integer :: i, j, os

 !------------------------------------------------------------------------------
 !------------------------------------------------------------------------------
 !------------------------------------------------------------------------------

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
    write(8,'(3es25.15)') xp(j), yp(j), zp(j)
   end do

!---------------------------------------------------------------------------
! Cell information.

  !CELLS: # of total cells (ntet+nprs+nhex), total size of the cell list.

  write(8,'(a,i12,i12)') 'CELLS ',ntet+nprs+nhex, (4+1)*ntet + (6+1)*nprs + (8+1)*nhex

  ! Note: The latter is the number of integer values written below as data.
  !           5 for tets   (# of vertices + 4 vertices),
  !           7 for prisms (# of vertices + 6 vertices),
  !           9 for hexa   (# of vertices + 8 vertices).

  !---------------------------------
  ! 2.1 List of tets

   if (ntet > 0) then
    do i = 1, ntet
     write(8,'(a,4i12)') '4', tet(i,1)-1, tet(i,2)-1, tet(i,3)-1
                         ! -1 since VTK reads the nodes as 0,1,2,3,..., not 1,2,3,..
    end do
   endif

  !---------------------------------
  ! 2.2 List of prisms

   if (nprs > 0) then
    do i = 1, nprs
     write(8,'(a,6i12)') '6',  prs(i,3)-1, prs(i,2)-1, prs(i,1)-1, &
                               prs(i,6)-1, prs(i,5)-1, prs(i,4)-1
                         ! -1 since VTK reads the nodes as 0,1,2,3,..., not 1,2,3,..
    end do
   endif

  !---------------------------------
  ! 2.3 List of hexa

   if (nhex > 0) then
    do i = 1, nhex
     write(8,'(a,8i12)') '8',  hex(i,1)-1, hex(i,2)-1, hex(i,3)-1, hex(i,4)-1, &
                               hex(i,5)-1, hex(i,6)-1, hex(i,7)-1, hex(i,8)-1
                         ! -1 since VTK reads the nodes as 0,1,2,3,..., not 1,2,3,..
    end do
   endif

!---------------------------------------------------------------------------
! Cell type information.

                                   !# of all cells
  write(8,'(a,i11)') 'CELL_TYPES ', ntet+nprs+nhex

  !Tetrahedron is classified as the cell type 10 in the .vtk format.

  if (ntet > 0) then
   do i = 1, ntet
    write(8,'(i3)') 10
   end do
  endif

  !Prism is classified as the cell type 13 in the .vtk format.

  if (nprs > 0) then
   do i = 1, nprs
    write(8,'(i3)') 13
   end do
  endif

  !Hexahedron is classified as the cell type 12 in the .vtk format.

  if (nhex > 0) then
   do i = 1, nhex
    write(8,'(i3)') 12
   end do
  endif

!---------------------------------------------------------------------------

  close(8)


 end subroutine write_vtk_file
!********************************************************************************

!*******************************************************************************
! This subroutine writes a Tecplot file for the volume grid.
! In this program, only tetrahedral grids are considered.
!*******************************************************************************
 subroutine write_tecplot_volume_file

  implicit none

  integer :: i, os

 write(*,*)
 write(*,*) ' Tecplot volume file = ', trim(filename_tecplot_v)
 write(*,*)

  open(unit=8, file=filename_tecplot_v, status="unknown", iostat=os)
  write(8,*) 'TITLE = "GRID"'
  write(8,*) 'VARIABLES = "x","y","z"'

   if (ntet > 0) then

    write(8,*) 'zone  n=', nnodes,',e=', ntet,' , et=tetrahedron, f=fepoint'

     do i = 1, nnodes
       write(8,'(3es27.15)') xp(i), yp(i), zp(i)
     end do

     do i = 1, ntet
     write(8,*) tet(i,1),tet(i,2),tet(i,3),tet(i,4)
     end do

   endif

   if (nprs > 0) then

    write(8,*) 'zone  n=', nnodes,',e=', nprs,' , et=brick, f=fepoint'

     do i = 1, nnodes
       write(8,'(3es27.15)') xp(i), yp(i), zp(i)
     end do

     do i = 1, nprs
     write(8,*) prs(i,1), prs(i,2), prs(i,3), prs(i,3), &
                prs(i,4), prs(i,5), prs(i,6), prs(i,6)
     end do

   endif

   if (nhex > 0) then

    write(8,*) 'zone  n=', nnodes,',e=', nhex,' , et=brick, f=fepoint'

     do i = 1, nnodes
       write(8,'(3es27.15)') xp(i), yp(i), zp(i)
     end do

     do i = 1, nhex
     write(8,*) hex(i,1), hex(i,2), hex(i,3), hex(i,4), &
                hex(i,5), hex(i,6), hex(i,7), hex(i,8)
     end do

   endif

!---------------------------------------------------------------------------

 close(8)

 end subroutine write_tecplot_volume_file
!********************************************************************************


!*******************************************************************************
! Compute the volume of a tetrahedron defined by 4 vertices:
!
!       (x1,y1,z1), (x2,y2,z2), (x3,y3,z3), (x4,y4,z4),
!
! which are ordered as follows:
!
!            1
!            o
!           /| .
!          / |   .
!         /  |     .
!        /   |       .
!     2 o----|-------o 3
!        \   |     .
!         \  |    .
!          \ |  .
!           \|.
!            o
!            4
!
! Note: Volume = volume integral of 1 = 1/3 * volume integral of div(x,y,z) dV
!              = surface integral of (x,y,z)*dS
!              = sum of [ (xc,yc,zc)*area_vector ] over triangular faces.
!
! where the last step is exact because (x,y,z) vary linearly over the triangle.
! There are other ways to compute the volume, of course.
!
!*******************************************************************************
 function tet_volume(x1,x2,x3,x4, y1,y2,y3,y4, z1,z2,z3,z4)

 implicit none

 integer , parameter :: dp = selected_real_kind(15) !Double precision

 !Input
 real(dp), intent(in)   :: x1,x2,x3,x4, y1,y2,y3,y4, z1,z2,z3,z4
 !Output
 real(dp)               :: tet_volume

 real(dp)               :: xc, yc, zc
 real(dp), dimension(3) :: area
 integer                :: ix=1, iy=2, iz=3


 tet_volume = 0.0_dp

! Triangle 1-3-2

   !Centroid of the triangular face
      xc = (x1+x3+x2)/3.0_dp
      yc = (y1+y3+y2)/3.0_dp
      zc = (z1+z3+z2)/3.0_dp
   !Outward normal surface vector
   area = triangle_area_vector(x1,x3,x2, y1,y3,y2, z1,z3,z2)

   tet_volume = tet_volume + ( xc*area(ix) + yc*area(iy) + zc*area(iz) )

! Triangle 1-4-3

   !Centroid of the triangular face
      xc = (x1+x4+x3)/3.0_dp
      yc = (y1+y4+y3)/3.0_dp
      zc = (z1+z4+z3)/3.0_dp

   !Outward normal surface vector
   area = triangle_area_vector(x1,x4,x3, y1,y4,y3, z1,z4,z3)

   tet_volume = tet_volume + ( xc*area(ix) + yc*area(iy) + zc*area(iz) )

! Triangle 1-2-4

   !Centroid of the triangular face
      xc = (x1+x2+x4)/3.0_dp
      yc = (y1+y2+y4)/3.0_dp
      zc = (z1+z2+z4)/3.0_dp

   !Outward normal surface vector
   area = triangle_area_vector(x1,x2,x4, y1,y2,y4, z1,z2,z4)

   tet_volume = tet_volume + ( xc*area(ix) + yc*area(iy) + zc*area(iz) )

! Triangle 2-3-4

   !Centroid of the triangular face
      xc = (x2+x3+x4)/3.0_dp
      yc = (y2+y3+y4)/3.0_dp
      zc = (z2+z3+z4)/3.0_dp

   !Outward normal surface vector
   area = triangle_area_vector(x2,x3,x4, y2,y3,y4, z2,z3,z4)

   tet_volume = tet_volume + ( xc*area(ix) + yc*area(iy) + zc*area(iz) )

   tet_volume = tet_volume / 3.0_dp

 end function tet_volume


!*******************************************************************************
! Compute the area of a triangle in 3D defined by 3 vertices:
!
!       (x1,y1,z1), (x2,y2,z2), (x3,y3,z3),
!
! which is assumed to be ordered clockwise.
!
!     1             2
!      o------------o
!       \         .
!        \       . --------->
!         \    .
!          \ .
!           o
!           3
!
! Note: Area is a vector based on the right-hand rule: 
!       when wrapping the right hand around the triangle with the fingers in the
!       direction of the vertices [1,2,3], the thumb points in the positive
!       direction of the area.
!
! Note: Area vector is computed as the cross product of edge vectors [31] and [32].
!
!*******************************************************************************
 function triangle_area_vector(x1,x2,x3, y1,y2,y3, z1,z2,z3) result(area_vector)
 
 implicit none
 integer , parameter :: dp = selected_real_kind(15) !Double precision

 !Input
  real(dp), intent(in)   :: x1,x2,x3, y1,y2,y3, z1,z2,z3
 !Output
  real(dp), dimension(3) :: area_vector

  integer :: ix=1, iy=2, iz=3

  !x-component of the area vector
   area_vector(ix) = 0.5_dp*( (y1-y3)*(z2-z3)-(z1-z3)*(y2-y3) )

  !y-component of the area vector
   area_vector(iy) = 0.5_dp*( (z1-z3)*(x2-x3)-(x1-x3)*(z2-z3) )

  !z-component of the area vector
   area_vector(iz) = 0.5_dp*( (x1-x3)*(y2-y3)-(y1-y3)*(x2-x3) )

 end function triangle_area_vector


 end program edu2d_twod2threed




