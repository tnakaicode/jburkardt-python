!********************************************************************************
!
!                             --- EDU2D-FP-Grid --- 
!
! This program generates a grid over a flat plate located from (x,y)=(0,0) to
! (xmax,0).
!
!
!        written by Dr. Katate Masatsuka (info[at]cfdbooks.com),
!
! the author of useful CFD books, "I do like CFD" (http://www.cfdbooks.com).
!
! This is Version 1 (2019).
!
!
! # Compile the code: e.g.,
!
!   gfortran -O3 -ffast-math edu2d_fp_grid.f90
!
! # and run it (which will read "input.nml"):
!
!   ./a.out
!
!
! Version 1:  A bug fixed. One node was missing in the viscous boundary data.
!
!
! Note: The Blasius-solution computation (generate_sample_data = T) can be
!       very slow. The option "-O3 -ffast-math" is necessary to speed it up.
!
!
! These F90 routines were written and made available for download
! for an educational purpose. Also, this is intended to provide all CFD
! students and researchers with a tool for their code verification.
!
! This file may be updated in future.
!
! Katate Masatsuka, http://www.cfdbooks.com
!********************************************************************************
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
!  Sample input file: 'input.nml' to generate a sample grid.
!  ------------------------------------------------------
!   &input_parameters
!                          Re_inf   = 1.0e+06
!                      igrid_type   = 1    
!                 random_diagonal   = F
!                            xmin   = -2.0
!                            xmax   = 2.0
!                            ymin   = 0.0
!                            ymax   = 4.0
!              generate_sample_data = T
!               x_sample_location   = 0.9
!                             nxL   =  17
!                             nxR   =  17
!                             ny    =  24
!           stretching_factor_xL    = 5.0
!           stretching_factor_xR    = 5.3
!           stretching_factor_y     = 9.5
!                  perturb_factor   = 0.0
!              generate_grid_file   = T
!              generate_su2_file    = T  
!              generate_tec_file    = T 
!              generate_vtk_file    = T   
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
! Reynolds number per unit length to estimate BL thickness,
! and also to compute Blasius solution.

  real(dp) ::  Re_inf = 1.0e+06_dp

!----------------------------
! igrid_type = Element type as listed below.
!
!             1 = Quads
!             2 = Trias
!             3 = Mixed
!
! Mixed grid will have quads in the inner region and
! triangles in the outer region (inner/outer based
! on the thickness estimate).

  integer :: igrid_type = 1

!----------------------------
! Random diagonal insertion.

  logical :: random_diagonal = .false.

!----------------------------
! Domain definition.
!
! Note: Flat plate length = xmax.

  real(dp) :: xmin = -0.5_dp
  real(dp) :: xmax =  1.0_dp

  real(dp) :: ymin =  0.0_dp
  real(dp) :: ymax =  4.0_dp

!----------------------------
! generate_sample_data = T to write a Blasius solution data.

  logical :: generate_sample_data = .false.

!----------------------------
! Location at which the Blasius solution is computed.

  real(dp) :: x_sample_location = 0.9_dp

!----------------------------
! # of elements

  integer :: nxL = 17 !in x-direction on the left  half (x < 0)
  integer :: nxR = 17 !in x-direction on the right half (x > 0)
  integer :: ny  = 23 !in y-direction.

!----------------------------
! Stretching factors.

  real(dp) :: stretching_factor_xL = 5.0_dp !towards LE from the left.
  real(dp) :: stretching_factor_xR = 5.3_dp !towards LE from the right.
  real(dp) :: stretching_factor_y  = 9.5_dp !towards the bottom.

!----------------------------
! Ransom perturbation to the nodal coordinates.

  real(dp) :: perturb_factor = 0.0_dp

!----------------------------
! generate_tec_file = T to write a Tecplot file.

  logical :: generate_grid_file = .true.

!----------------------------
! generate_su2_file = T to write .su2 file
!                         F not to write.

  logical :: generate_su2_file = .true.

!----------------------------
! generate_tec_file = T to write a Tecplot file.

  logical :: generate_tec_file = .true.

!----------------------------
! generate_vtk_file = T to write a .vtk file.

  logical :: generate_vtk_file = .true.

!----------------------------
! End of Default input values
!----------------------------

! Below is the list of all input parameters available:

  namelist / input_parameters /   &
                          Re_inf, &
                      igrid_type, &
                 random_diagonal, &
                            xmin, &
                            xmax, &
                            ymin, &
                            ymax, &
               x_sample_location, &
                             nxL, &
                             nxR, &
                             ny , &
            stretching_factor_xL, &
            stretching_factor_xR, &
            stretching_factor_y , &
                  perturb_factor, &
              generate_grid_file, &
              generate_su2_file , &
              generate_tec_file , &
              generate_vtk_file , &
              generate_sample_data

 contains

!*****************************************************************************
!* Read input_parameters in the input file: file name = namelist_file
!*****************************************************************************
  subroutine read_nml_input_parameters(namelist_file)

  implicit none
  character(9), intent(in) :: namelist_file
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

 program edu2d_grid_generation_fp

 use input_parameter_module

 implicit none

!Output file names
 character(80) :: filename_grid  = "fp_grid.grid"
 character(80) :: filename_bcmap = "fp_grid.bcmap"
 character(80) :: filename_su2   = "fp_grid.su2"

 character(80) :: filename_tec   = "fp_grid_tec.dat"
 character(80) :: filename_vtk   = "fp_grid.vtk"

 character(80) :: filename_sample_line     = "fp_grid.line1"
 character(80) :: filename_sample_line_tec = "fp_grid_tec.line1"

 real(dp), dimension(:,:), allocatable :: xs, ys
 integer , dimension(:,:), allocatable :: tria, quad
 real(dp), dimension(:)  , allocatable :: x, y

 !- Boundary data requied by a solver.
 !   These are needed for .grid and .su2 files.
 integer                                :: nb      !# of boundaries
 integer      , dimension(:  ), pointer :: nbnodes !# of nodes in each boundary
 integer      , dimension(:,:), pointer :: bnode   !List of boundary nodes
 character(80), dimension(:  ), pointer :: bnames  !Boundary names

 integer  :: i, j, ib, ic
 integer  :: nx, nnodes, ntria, nquad, inode, i_sample
 real(dp) :: U_inf, thickness, dx, dy, rn, s, sf, xp, yp, etap, u, v, f, f1, f2, nu

 real(dp) :: fp_length

 integer, dimension(:), allocatable :: inode_sample

!-------------------------------------------------------------------------------
!
! Read the input parameters, defined in the file named as 'input.nml'.
!
!-------------------------------------------------------------------------------

   write(*,*) "Reading the input file: input.nml..... "
   write(*,*)
   call read_nml_input_parameters('input.nml')
   write(*,*)

  !Flat plate is placed at the origin extending to the right boundary, xmax.
  !So, the length is equal to xmax.

  fp_length = xmax

  write(*,*)
  write(*,*) " Flat plate length = xmax = ", fp_length
  write(*,*)

  write(*,*) "**************************************************************"
  write(*,*)

            U_inf = 1.0_dp
               nu = U_inf*fp_length/Re_inf 

  write(*,*) " ---> Compute the viscosity nu = U_inf*L_ref/Re_inf "
  write(*,*) "                               = U_inf*fp_length/Re_inf   "
  write(*,*) "                               = ", nu


  write(*,*)
  write(*,*)  " U_inf = 1 is used, but it doesn't matter since Re_inf is the one"
  write(*,*)  " that will be used in the Blasius solution in the local Re = U_inf*xp/nu."
  write(*,*)

  write(*,*)
  write(*,*) "**************************************************************"


  !Let's make it # of nodes (i.e., nnodes = ncells + 1 in y-direction):

    ny = ny + 1

!-------------------------------------------------------------------------------
!
! Estimate the boundary layer thickness at the right end.
! Use this for switching from quads to trias in a mixed grid.
!
!-------------------------------------------------------------------------------

     Re_inf = 1.0e+06_dp
  thickness = 2.5_dp * ( 5.0_dp / sqrt(Re_inf*fp_length) )
  write(*,*) "BL thickness = ", thickness
  write(*,*)

!-------------------------------------------------------------------------------
!
! Allocate arrays.
!
!-------------------------------------------------------------------------------

 !Note: nxL=# of elements on the left half, nxR=# of elements on the right half.
 !      nx = # of nodes in the x-direction over the entire domain (so, +1)

   nx = nxL + nxR + 1
   allocate(xs(nx,ny),ys(nx,ny))

!-------------------------------------------------------------------------------
!
! Generate a uniform 2D grid, using (i,j) data.
!
!-------------------------------------------------------------------------------

  write(*,*) "Generating an initial grid.."

      dy = (ymax-ymin)/real(ny-1) !Uniform spacing in y. ny=# of nodes in y.

! Free stream region to the leading edge point.
! nxL = # elements -> nxL nodes and LE is nxL+1.

      dx = (zero-xmin)/real(nxL)

    do j = 1, ny
     do i = 1, nxL+1
      xs(i,j) = xmin + dx*real(i-1)
      ys(i,j) = ymin + dy*real(j-1)
     end do
    end do

! Flat plate region: leading edge -> i = nxL+1. Here, we start from i = nxL + 2.

      dx = (xmax-zero)/real(nxR)

    do j = 1, ny
     do i = nxL+2, nx
      xs(i,j) = zero + dx*real(i - (nxL+1) )
      ys(i,j) = ymin + dy*real(j-1)
     end do
    end do

!-------------------------------------------------------------------------------
!
! Perturb the nodal coordinates if requested with perturb_factor > 0.
!
!-------------------------------------------------------------------------------

   if ( abs(perturb_factor) > 1.0e-12_dp ) then

     write(*,*) "Perturbing nodal coordinates..."

    do j = 2, ny-1
     do i = 2, nx-1
      if (i == nxL+1) cycle !Skip the nodes above LE.
      call random_number(rn)
           dx = half*( xs(i+1,j  ) - xs(i-1,j  ) )
           dy = half*( ys(i  ,j+1) - ys(i  ,j-1) )
      xs(i,j) = xs(i,j) + (rn-half)*dx* (perturb_factor*1.5_dp)
      ys(i,j) = ys(i,j) - (rn-half)*dy* (perturb_factor*1.5_dp)
     end do
    end do

!    Nodes on the plate
     j = 1
     do i = nxL+2, nx-1
      call random_number(rn)
           dx = half*( xs(i+1,j  ) - xs(i-1,j  ) )
      xs(i,j) = xs(i,j) + (rn-half)* dx*perturb_factor
     end do

!    Nodes on the outer boudnary
     j = ny
     do i = 2, nx-1
      call random_number(rn)
           dx = half*( xs(i+1,j  ) - xs(i-1,j  ) )
      xs(i,j) = xs(i,j) + (rn-half)* dx*perturb_factor
     end do

!    Nodes at inflow boundary
     i=1
     do j = 2, ny-1
      call random_number(rn)
           dy = half*( ys(i  ,j+1) - ys(i  ,j-1) )
      ys(i,j) = ys(i,j) - (rn-half)* dy*perturb_factor
     end do

!    Nodes at outflow boundary
     i=nx
     do j = 2, ny-1
      call random_number(rn)
           dy = half*( ys(i  ,j+1) - ys(i  ,j-1) )
      ys(i,j) = ys(i,j) - (rn-half)* dy*perturb_factor
     end do

   else

    write(*,*) "No perturbation on nodal coordinates. Skiped perturbation."

   endif

!-------------------------------------------------------------------------------
!
! Stretching in x-direction
!
!-------------------------------------------------------------------------------

  write(*,*) "Stretching in x-direction..."

! Free stream region to the leading edge point.

   sf = stretching_factor_xL

   do j = 1, ny
    do i = 1, nxL+1
           s = (xs(i,j)-xs(1,j))/(xs(nxL+1,j)-xs(1,j))
     xs(i,j) = xmin + (one-exp(-sf*s))/(one-exp(-sf)) * (xs(nxL+1,j)-xs(1,j))
    end do
   end do

! Flat plate region: leading edge -> i = nx1. Here we start from i=nx1+1

   sf = stretching_factor_xR

   do j = 1, ny
    do i = nxL+2, nx
           s = (xs(i,j)-xs(nxL+1,j))/(xs(nx,j)-xs(nxL+1,j))
     xs(i,j) = xmax*(one-exp(sf*s))/(one-exp(sf))
    end do
   end do

!-------------------------------------------------------------------------------
!
! Stretching in y-direction
!
!-------------------------------------------------------------------------------

     write(*,*) "Stretching in y-direction..."

     sf = stretching_factor_y

    do j = 1, ny
     do i = 1, nx
      ys(i,j) = ymax*(one-exp(sf* (ys(i,j)-ys(i,1))/(ys(i,ny)-ys(i,1)) ))/(one-exp(sf))
     end do
    end do

!-------------------------------------------------------------------------------
!
! Sample location is set to be x=x_sample_location.
!
!-------------------------------------------------------------------------------

  find_sample_location : do i = 1, nx

   if (xs(i,1) > x_sample_location) then

      i_sample = i-1
     xs(i-1,1) = x_sample_location

    do j = 1, ny
     xs(i-1,j) = x_sample_location
    end do

    exit find_sample_location

   endif

  end do find_sample_location

!-------------------------------------------------------------------------------
!
! Generate 1D array for nodes:
!
!-------------------------------------------------------------------------------

   write(*,*) "Generating 1D array for nodes..."

   nnodes = nx*ny

   allocate(x(nnodes),y(nnodes))
   allocate( inode_sample(ny) )

  !Node data

   do j = 1, ny
    do i = 1, nx
     inode = i + (j-1)*nx
       x(inode) = xs(i,j)
       y(inode) = ys(i,j)
     if (i==i_sample) then
      inode_sample(j) = inode
     endif
    end do
   end do

!-------------------------------------------------------------------------------
!
! Create boundary data.
!
!-------------------------------------------------------------------------------

   write(*,*) "Creating boundary data information..."

  nb = 5
  allocate( bnode( max(ny,nx), nb) )
  allocate( nbnodes(nb) )
  allocate(  bnames(nb) )

   ib = 1
   bnames( ib) = "symmetry_y"
   nbnodes(ib) = nxL+1
      j = 1
     ic = 0
   do i = 1, nxL+1
           inode = i + (j-1)*nx
              ic = ic + 1
    bnode(ic,ib) = inode
   end do

   ib = 2
   bnames( ib) = "viscous_wall"
   nbnodes(ib) = nxR+1
      j = 1
     ic = 0
   do i = nxL+1, nx
           inode = i + (j-1)*nx
              ic = ic + 1
    bnode(ic,ib) = inode
   end do

   ib = 3
   bnames( ib) = "outflow"
   nbnodes(ib) = ny
      i = nx
     ic = 0
   do j = 1, ny
           inode = i + (j-1)*nx
              ic = ic + 1
    bnode(ic,ib) = inode
   end do

   ib = 4
   bnames( ib) = "farfield"
   nbnodes(ib) = nx
      j = ny
     ic = 0
   do i = nx, 1, -1
           inode = i + (j-1)*nx
              ic = ic + 1
    bnode(ic,ib) = inode
   end do

   ib = 5
   bnames( ib) = "inflow"
   nbnodes(ib) = ny
      i = 1
     ic = 0
   do j = ny, 1, -1
           inode = i + (j-1)*nx
              ic = ic + 1
    bnode(ic,ib) = inode
   end do

!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
! Optional: Write a data file for the Blasius solution at x=x_sample.
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
 if (generate_sample_data) then

  open(unit=110, file=filename_sample_line    , status="unknown")
  open(unit=111, file=filename_sample_line_tec, status="unknown")
  write(111,*) 'title = "blasius data"'
  write(111,*) 'variables = "inode","x","y","eta","u","v","f","f1","f2","nu","U_inf"'
  write(111,*) 'zone t=sample I= ', ny, 'F=POINT'

  write(110,*) ny

    write(*,*)
    write(*,*) " Computing Blasius solution at x = ", x_sample_location
    write(*,*)
    write(*,*) " node,       eta,         u,         v,         f,         f1,          f2"
    write(*,*)

  do j=1,ny
    xp = x(inode_sample(j))
    yp = y(inode_sample(j))
   call blasius(etap,u,v,f,f1,f2, xp,yp,nu,U_inf)
   write(110,*) inode_sample(j), etap,u,v,f,f1,f2
   write(111,*) inode_sample(j), x(inode_sample(j)), y(inode_sample(j)), etap,u,v,f,f1,f2, nu, U_inf

   write(*,'(i6,6es12.3)') inode_sample(j),etap,u,v,f,f1,f2

  end do
  close(110)
  close(111)
 
  write(*,*)
  write(*,*) " Blasius solution is written in the following two data files:"
  write(*,*) "  ", trim(filename_sample_line)
  write(*,*) "  ", trim(filename_sample_line_tec)

  write(*,*)

 endif
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------

!-------------------------------------------------------------------------------
!
! Generate unstructured data:
!
!-------------------------------------------------------------------------------

 !This is just the maximum possible dimensions:
  allocate(tria(2*(nx-1)*(ny-1),3), quad((nx-1)*(ny-1),4))


 !Quadrilateral grid
  if     (igrid_type == 1) then

   write(*,*) "Generating quad grid..."
   call generate_quad_grid(tria, quad, ntria, nquad, nx, ny)

 !Triangular grid
  elseif (igrid_type == 2) then

   write(*,*) "Generating triangular grid..."
   call generate_tri_grid(tria, quad, ntria, nquad, nx, ny, random_diagonal)

 !Mixed grid
  elseif (igrid_type == 3) then

   write(*,*) "Generating mixed grid..."
   call generate_mixed_grid(tria, quad, ntria, nquad, nx, ny, random_diagonal)

  endif

!--------------------------------------------------------------------------------

  write(*,*)
  write(*,*) "  Resulting dimension:"
  write(*,*) "      nnodes = ", nnodes
  write(*,*) "      nquad  = ", nquad
  write(*,*) "      ntria  = ", ntria
  write(*,*)

!-------------------------------------------------------------------------------
!
! Generate a .grid file for a 2D solver.
!
!-------------------------------------------------------------------------------

  if (generate_grid_file) then

   call write_grid_file(filename_grid,nnodes,tria,ntria,quad,nquad,x,y, &
                                                       nb,nbnodes,bnode )

   call write_bcmap_file(filename_bcmap, nb, bnames)

  endif

!-------------------------------------------------------------------------------
!
! Generate a .grid file for a 2D solver.
!
!-------------------------------------------------------------------------------

  if (generate_su2_file) then

   call write_su2_file(filename_su2,nnodes,tria,ntria,quad,nquad,x,y, &
                                              nb,nbnodes,bnode,bnames )
  endif

!-------------------------------------------------------------------------------
!
! Generate a Tecplot file.
!
!-------------------------------------------------------------------------------

  if (generate_tec_file) then

   call write_tecplot_file(filename_tec, nnodes,x,y, ntria,tria, &
                                                     nquad,quad  )

   filename_tec = "fp_grid_tec"
   call write_tecplot_boundary_file(filename_tec,x,y,nb,nbnodes,bnode )

  endif

!-------------------------------------------------------------------------------
!
! Generate a .vtk file
!
!-------------------------------------------------------------------------------

  if (generate_vtk_file) then

   call write_vtk_file(filename_vtk, nnodes,x,y, ntria,tria, &
                                                 nquad,quad  )
  endif

!-------------------------------------------------------------------------------

 write(*,*) "Successfully completed. Stop."
 write(*,*)

 stop

 contains
 



!********************************************************************************
 subroutine generate_tri_grid(tri, quad, ntri, nquad, nx, ny, random_diagonal)
 implicit none
 integer,                 intent( in) ::   nx, ny 
 logical,                 intent( in) :: random_diagonal
 integer,                 intent(out) :: ntri, nquad
 integer, dimension(:,:), intent(out) ::  tri, quad
!Local variables
 integer  :: i, j, inode, i1, i2, i3, i4
 real(dp) :: rn, rn2

! No quads
 nquad = 0
  quad = 0

! Trianguler grid with right-up diagonals (i.e., / ).

 ntri = 0

 do j = 1, ny-1
  do i = 1, nx-1

   inode = i + (j-1)*nx
      i1 = inode
      i2 = inode + 1
      i3 = inode + nx + 1
      i4 = inode + nx

  if (random_diagonal) then
   call random_number(rn)
  else
   rn = 1.0d0
  endif

   rn2 = 2.0d0*rn-1.0d0

   if (rn2 > 0.0d0 ) then
!! /
           ntri = ntri + 1
    tri(ntri,1) = i1
    tri(ntri,2) = i2
    tri(ntri,3) = i3

           ntri = ntri + 1
    tri(ntri,1) = i1
    tri(ntri,2) = i3
    tri(ntri,3) = i4

   else

!! \
           ntri = ntri + 1
    tri(ntri,1) = i1
    tri(ntri,2) = i2
    tri(ntri,3) = i4

           ntri = ntri + 1
    tri(ntri,1) = i2
    tri(ntri,2) = i3
    tri(ntri,3) = i4

   endif

  end do
 end do

 end subroutine generate_tri_grid
!********************************************************************************

!********************************************************************************
 subroutine generate_quad_grid(tri, quad, ntri, nquad, nx, ny)
 implicit none
 integer,                 intent( in) ::   nx, ny 
 integer,                 intent(out) :: ntri, nquad
 integer, dimension(:,:), intent(out) ::  tri, quad
!Local variables
 integer :: i, j, inode, i1, i2, i3, i4

! No triangles
  ntri = 0
   tri = 0

! Quadrilateral grid

 nquad = 0

 do j = 1, ny-1
  do i = 1, nx-1

   inode = i + (j-1)*nx
      i1 = inode
      i2 = inode + 1
      i3 = inode + nx + 1
      i4 = inode + nx

!  Order the quad counterclockwise:
          nquad = nquad + 1
   quad(nquad,1) = i1
   quad(nquad,2) = i2
   quad(nquad,3) = i3
   quad(nquad,4) = i4

  end do
 end do

 end subroutine generate_quad_grid
!********************************************************************************


!********************************************************************************
 subroutine generate_mixed_grid(tri, quad, ntri, nquad, nx, ny, random_diagonal)
 implicit none
 integer,                 intent( in) ::   nx, ny 
 logical,                 intent( in) :: random_diagonal
 integer,                 intent(out) :: ntri, nquad
 integer, dimension(:,:), intent(out) ::  tri, quad
!Local variables
 integer :: i, j, inode, i1, i2, i3, i4
 real(dp) :: rns, rns2

! No quads
 nquad = 0
  quad = 0
  ntri = 0

 do j = 1, ny-1
  do i = 1, nx-1

   inode = i + (j-1)*nx
      i1 = inode
      i2 = inode + 1
      i3 = inode + nx + 1
      i4 = inode + nx

 !----------------------------------------------------
 ! Triangular grid outside the BL.
   if     ( ys(i,j) >= thickness ) then ! Triangle

    if (random_diagonal) then
      call random_number(rns)
      rns2 = two*rns-one
    else
      rns2 = one
    endif

    if (rns2 > zero) then
! /
            ntri = ntri + 1
     tri(ntri,1) = i1
     tri(ntri,2) = i2
     tri(ntri,3) = i3
            ntri = ntri + 1
     tri(ntri,1) = i1
     tri(ntri,2) = i3
     tri(ntri,3) = i4
 
    else
!\
            ntri = ntri + 1
     tri(ntri,1) = i1
     tri(ntri,2) = i2
     tri(ntri,3) = i4
            ntri = ntri + 1
     tri(ntri,1) = i2
     tri(ntri,2) = i3
     tri(ntri,3) = i4

    endif
 
 !----------------------------------------------------
 ! Quads inside the BL.
   elseif ( ys(i,j) < thickness  ) then ! Quadrilateral

           nquad = nquad + 1
    quad(nquad,1) = i1
    quad(nquad,2) = i2
    quad(nquad,3) = i3
    quad(nquad,4) = i4

   endif

  end do
 end do

 end subroutine generate_mixed_grid
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

!********************************************************************************
!* This computes the solution set (u,v,f,f1,f2) at a given position (xp,yp),
!* using the one-step integration method described in the book,
!* "I do like CFD, VOL.1, Second Edition" (See Section 7.15.9).
!* 
!*  U_inf --->
!*
!*  ^ y
!*  |                                                .(xp,yp)
!*  |
!*  ----->x         ------------------------------------------------------------
!*                x=0                  flat plate
!*
!* Input ---------------------------------------------------
!*   (xp,yp) = position where the exact solution is sought.
!*        nu = kinematic viscosity
!*     U_inf = Freestream velocity (x-direction only)
!*
!* Output --------------------------------------------------
!*   (u,v) = velocity vector
!*    etap = self-similar variable, eta
!*       f = function f in the streamfunction: Eq.(7.15.45)
!*      f1 = derivative of f
!*      f2 = second derivative of f
!*
!* NB: The location (xp,yp) must be far enough from the leading edge of the
!*     plate, i.e., x >> 0. Otherwise the solution will not be self-similar,
!*     and the Blasius solution does not apply.
!*
!* NB: This subroutine requires the function, rhs(Fv), for computing the right
!*     hand side of the ordinary differential equation.
!*
!*        written by Dr. Katate Masatsuka (info[at]cfdbooks.com),
!*
!* the author of useful CFD books, "I do like CFD" (http://www.cfdbooks.com).
!*
!* Katate Masatsuka, March 2010. http://www.cfdbooks.com
!********************************************************************************
 subroutine blasius(etap,u,v,f,f1,f2, xp,yp,nu,U_inf)
 implicit none
!Parameters
 integer , parameter :: sp = kind(1.0)
 integer , parameter :: dp = selected_real_kind(2*precision(1.0_sp))
 real(dp), parameter :: zero=0.0_dp, two=2.0_dp
 real(dp), parameter :: third=1.0_dp/3.0_dp, sixth=1.0_dp/6.0_dp, half=0.5_dp
!Input and Output
 real(dp), intent( in)  :: xp, yp    ! position at which the solution is computed.
 real(dp), intent( in)  :: nu, U_inf ! viscosity and freestrem velocity
 real(dp), intent(out)  :: u, v, f, f1, f2, etap ! velocity, f-functions, etap
!Local variables
 real(dp)               :: Rex, f2_0
 real(dp)               :: eta, deta
 real(dp), dimension(3) :: Fv, K1, K2, K3
 logical                :: finish

  f2_0 = 0.3320573362151946_dp ! Pre-computed initial value: Eq.(7.15.61)
   Rex = U_inf*xp/nu           ! Reynolds number based on x: Eq.(7.15.46)
  etap = yp/xp*sqrt(Rex)       ! Variable eta              : Eq.(7.15.46)

!Increment for ODE integration: default = 1.0e-04
   deta = 1.0e-04_dp

!Integrate ODE up to eta = etap by the classical RK4.
! 1. Initial values.
      eta = zero
    Fv(1) = zero
    Fv(2) = zero
    Fv(3) = f2_0
   finish = .false.
! 2. Stepping to etap! (NB: no need to integrate if etap==0.)
   if (etap > zero) then
    do
     if (eta + deta > etap) then
      deta = etap - eta
      finish = .true.
     endif
     eta = eta + deta
      K1 = Fv + half*deta*rhs(Fv)
      K2 = Fv + half*deta*rhs(K1)
      K3 = Fv +      deta*rhs(K2)
      Fv = (K1 + two*K2 + K3 - Fv)*third + deta*rhs(K3)*sixth
     if (finish) exit
    end do
   endif

!write(*,*) k

!Solution at eta=etap, i.e., (x,y)=(xp,yp).
   f = Fv(1)
  f1 = Fv(2)
  f2 = Fv(3)
   u = f1
   v = half/sqrt(Rex)*(etap*f1-f)

 return
 end subroutine blasius

!*******************************************************************************
!* Right hand side of the ODE: Equation (7.15.52) in "I do like CFD, VOL.1, Second Edition"
!*
!* This function is used in the subroutine, blasius().
!*
!* Katate Masatsuka, March 2010. http://www.cfdbooks.com
!*******************************************************************************
 function rhs(Fv) result(G)
 implicit none
 integer , parameter  :: sp = kind(1.0)
 integer , parameter  :: dp = selected_real_kind(2*precision(1.0_sp))
 real(dp), parameter  :: half=0.5_dp
 real(dp), intent(in) :: Fv(3)
 real(dp) :: G(3)
 real(dp) :: f, f1, f2
    f  = Fv(1) 
    f1 = Fv(2)
    f2 = Fv(3)
  G(1) = f1
  G(2) = f2
  G(3) = -half*f*f2
 end function rhs
!*******************************************************************************

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

 end program edu2d_grid_generation_fp

