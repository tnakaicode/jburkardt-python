!********************************************************************************
!* This program generates 2D quad and triangular grids for a flow over Rankine's
!* half body. See Section 7.11.2, page 225, "I do like CFD, VOL.1 (2nd Edition)".
!*
!*   Exact solution: We set sigma = Vinf, so that
!*
!*       Velocity potential: phi/Vinf = x + ln(x^2+y^2)/(4*pi)
!*          Stream function: psi/Vinf = y + theta/(2*pi)
!*               X-velocity:   u/Vinf = 1 + x/(2*pi)/(x^2+y^2)
!*               Y-velocity:   u/Vinf =     y/(2*pi)/(x^2+y^2)
!*
!*      --------------------------------------
!*      .                                    .
!*      .                                    .
!*      .                                 .  .
!*      .                           .     
!*      .                       .     
!*      .                    .
!*      .  Flow            .
!*      .  --->           .   Rankine's half body
!*      .                  .   
!*      .                     .
!*      .                           . 
!*      .                                 .  .
!*      .                                    .
!*      .                                    .
!*      .                                    .
!*      --------------------------------------
!*
!* 3-Step Generation:
!*
!* 1. Generate a temporary structured grid data for nodes: xs(i,j) and ys(i,j)
!* 2. Generate a 1D node array: x(1:nnodes), y(1:nnodes)
!* 3. Generate element connectivity data: tria(1:ntria,3), quad(1:nquad,4)
!*
!*
!*  Input: 
!*               nxp = number of nodes over the half body
!*                ny = number of nodes in the direction from the body to outer boundary
!*
!*        (NOTE: All input parameters are defined inside the program.)
!*
!* Output:
!*        tria_rankine_grid_tecplot.dat = tecplot file of the triangular grid (with exact sol)
!*        quad_rankine_grid_tecplot.dat = tecplot file of the quadrilateral grid (with exact sol)
!*                    tria_rankine.grid = triangular-grid file for EDU2D solver
!*                    quad_rankine.grid = quadrilateral-grid file for EDU2D solver
!*                        project.bcmap = file that contains boundary condition info
!*                    quad_rankine.su2  = quadrilateral-grid file for SU2
!*                    tria_rankine.su2  = triangular-grid file for SU2
!*                    quad_rankine.vtk  = quadrilateral-grid file in .vtk
!*                    tria_rankine.vtk  = triangular-grid file in .vtk
!*
!*        (NOTE: The grid file contains 6 boundary segments. See write_grid_file() on the
!*               bottom of this file. Boudnary condition files project.bcmap
!*               specify the boundary condition to be applied to each segment.)
!*
!*
!*
!*        written by Dr. Katate Masatsuka (info[at]cfdbooks.com),
!*
!* the author of useful CFD books, "I do like CFD" (http://www.cfdbooks.com).
!*
!* This is Version 1 (July 2019).
!
!  07-24-19: It now generates .su2 and .vtk files.
!
!
!* This F90 code is written and made available for an educational purpose.
!* This file may be updated in future.
!*
!* Katate Masatsuka, May 2015. http://www.cfdbooks.com
!********************************************************************************
 program twod_rankine_half_body_grid

 implicit none

!Parameters
  integer, parameter :: sp = kind(1.0)
  integer, parameter :: p2 = selected_real_kind(2*precision(1.0_sp))
  real(p2) :: zero=0.0_p2, half=0.5_p2, one=1.0_p2, two=2.0_p2, four=4.0_p2
  real(p2) :: pi = 3.141592653589793238_p2

!Input  - domain size and grid dimensions
 integer  :: nxp
 integer  :: ny

!Output - grid files
 character(80) :: datafile_tria_tec = "tria_rankine_grid_tecplot.dat"
 character(80) :: datafile_quad_tec = "quad_rankine_grid_tecplot.dat"
 character(80) :: datafile_tria = "tria_rankine.grid" !Triangular grid file for solver
 character(80) :: datafile_quad = "quad_rankine.grid" !      Quad grid file for solver
 character(80) :: datafile_bcmap = "project.bcmap"    !             bc file for solver

!Local variables
 real(p2), dimension(:,:), allocatable :: xs, ys !Structured grid data

 real(p2) :: xmin, xmax
 real(p2) :: ymin, ymax
 integer  :: nx
 integer  :: nnodes !Total number of nodes
 integer  ::  ntria !Total number of triangles
 integer  ::  nquad !Total number of quadrilaterals
 integer  ::  inode !Local variables used in the 1D nodal array

 integer , dimension(:,:), allocatable :: tria !Triangle connectivity data
 integer , dimension(:,:), allocatable :: quad !Quad connectivity data
 real(p2), dimension(:)  , allocatable :: x, y !Nodal coordinates, 1D array

 real(p2) :: dx !Uniform grid spacing in x-direction = (xmax-xmin)/nx
 real(p2) :: dy !Uniform grid spacing in y-direction = (ymax-ymin)/ny
 integer  :: i, j, os

 real(p2) :: theta, dtheta, theta_min, theta_max, fnc, dfnc, sf, s, snew, z1, rn
 real(p2) :: ex,ey, distance, dr
 integer , dimension(:), allocatable :: bmark
 real(p2), dimension(:), allocatable :: phi, psi, u, v
 logical  :: irregular_grid

 !- Boundary data requied by a solver.
 !   These are needed for .grid and .su2 files.
 integer                                :: ib
 integer                                :: nb      !# of boundaries
 integer      , dimension(:  ), pointer :: nbnodes !# of nodes in each boundary
 integer      , dimension(:,:), pointer :: bnode   !List of boundary nodes
 character(80), dimension(:  ), pointer :: bnames  !Boundary names
 character(80) :: filename_su2
 character(80) :: filename_vtk

! Set this to be .false. to generate non-irregular triangular grid.
  irregular_grid = .true.
 
!--------------------------------------------------------------------------------
! 0. Define the grid size and allocate the structured grid data array.
!
!                    B5
! ymax --------------------------------------  ^
!      .                                    .  | ny nodes here
!      .                                 B6 .  |
!      .                                 .  .  v 
!      .                           .        theta=theta_min
!      .                       .     
!      .                    .
!      .                  .
!    B4.             B1  .  <-- Origin (0,0)    
!      .                  .   
!      .                     .
!      .                           .        theta=theta_max
!      .                                 .  .  ^
!      .                                    .  | ny nodes here
!      .                                 B2 .  |
!      .             B3                     .  v
! ymin --------------------------------------
!    xmin                                  xmax
!
!  Boundaries are considered separately, for the body(B1), lower outflow(B2),
!  bottom outer boundary(B3), left inflow boundary(B4), top outer boundary(B5),
!  and top outflow(B6).
!

!  Define the domain: here we define the coordinates that define the corners.

      xmin =-one
      xmax = one

      ymin =-one
      ymax = one

!  Define the grid size

   !Input parameters: nxp and ny, nxp=even to avoid the singularity at the origin for x.

    nxp = 20         ! The number of nodes along each straight outer boundaries(B3,B4,B5).
    ny  = 21         ! The number of nodes in the direciton from the body(B1) to the outer boudnary(B3,B4,B5).

    nx  = 3*nxp - 2  ! The number of nodes over the half-body(B1) = Nodes on B3, B4, and B5

!  Allocate arrays.
   allocate(xs(nx,ny),ys(nx,ny))

!--------------------------------------------------------------------------------
! 1. Generate nodes along the Rankine half body (B1): i=1,nx, j=1
!    Note: We consider a structured grid with the half body as the bottom, i.e., j=1,
!          and the outer boundary(B3,B4,B5) as top, i.e., j=ny. The index i runs from 1
!          to nx along the half-body or the outer boundary in the clockwise direction.

  !First, find the starting value of theta, which gives x=1.0.

   write(*,*) "Finding the starting parameter value for the half body..."

  theta_min = zero

   write(*,*)
   write(*,'(a67,i3,2es25.16)') "    -- Newton iteration:  itr         theta_min         residual"
 
 find_theta_min : do i = 1, 100

   !Equation of theta, representing x=1.0. (See Eq.(7.11.15) on page 225;
   !This is basically streamfunction=sigma/2 with x=1.0).
   fnc = tan(theta_min) - half*(one-theta_min/pi)

   write(*,'(a28,i3,2es25.16)') "    -- Newton iteration: ", i, theta_min, fnc

   !If the equation is satisfied, we're done.
   if (abs(fnc) < 1.0e-18_p2) then
    write(*,*)
    write(*,*) " The starting value of theta has been successfully found.."
    write(*,*) "           i = ", i
    write(*,*) "         fnc = ", fnc
    write(*,*) "   theta_min = ", theta_min
    write(*,*)
    exit
   endif

   !Derivative (Jacobian) of the equation we are solving.
        dfnc = one/cos(theta_min)**2 + half/pi

   !Newton iteration:
   theta_min = theta_min - fnc/dfnc

  end do find_theta_min

  !By symmetry, the maximum value of theta is just 2*pi-theta_min.
  theta_max = two*pi - theta_min

  !On the half body
  j = 1

   write(*,*) "Generating nodes along the half body..."

  ! i=1,nx corresponds to theta=theta_max,theta_min
  do i = 1, nx

      dtheta = (theta_max-theta_min)/real(nx-1,p2)
       theta = theta_max - dtheta*real(i-1,p2)
       call random_number(rn)
       if (irregular_grid) theta = theta + dtheta*(rn-half)

       ! Apply stretching ibn theta to distribute nodes as uniformly as possible.
           sf = 4.0_p2
            s = ( theta-theta_min ) / (theta_max-theta_min)                 !Transform in space s=[0,1]
           z1 = -tanh(sf*(-half))
         snew = half*(z1+tanh(sf*(s-half))) / ( half*(z1+tanh(sf*(half))) ) !Apply stretching in s
        theta = (theta_max-theta_min)*snew + theta_min                      !Transform back in theta

   !Equation (7.11.19) on page 225
    ys(i,j) = half*(one-theta/pi)

   !From the definition: tan(theta)=y/x: Careful here, we choose nxp(even) such that we avoid theta=pi.
    xs(i,j) = ys(i,j)/tan(theta)

  end do

!--------------------------------------------------------------------------------
! 2. Generate nodes along the outer boundary (B3,B4,B5): : i=1,nx, j=ny

   write(*,*) "Generating nodes along the outer boundary..."

 ! Outer boundary
   j = ny

 ! Bottom(B3): x=[-1.0 1.0] and y=-1.0
   do i = 1, nxp
    dx = two/real(nxp-1,p2)
    xs(i,j) =  one - dx*real(i-1,p2)
    ys(i,j) = -one
   end do
 
 ! Left(B4): x=-1.0 and y=[-1.0 1.0]
   do i = 1, nxp
    dy = two/real(nxp-1,p2)
    xs(nxp+(i-1),j) = -one
    ys(nxp+(i-1),j) = -one + dy*real(i-1,p2)
   end do
 
 ! Top(B5): x=[-1.0 1.0] and y=1.0
   do i = 1, nxp
    dx = two/real(nxp-1,p2)
    xs(2*nxp-1+(i-1),j) = -one + dx*real(i-1,p2)
    ys(2*nxp-1+(i-1),j) =  one
   end do

!--------------------------------------------------------------------------------
! 3. Generate a structured 2D grid data, (i,j) data
!
     write(*,*) "Generating interior nodes..."

!  Generate nodes in the domain.

  ! Go along the body(B1) clockwise.
   do i = 1, nx

    !(ex,ey) is the unit vector pointing from a node on the body to the corresponding
    ! node at the outer boundary.

     ex = xs(i,ny)-xs(i,1)
     ey = ys(i,ny)-ys(i,1)

    !distance is the distance between the two nodes.

     distance = sqrt(ex**2+ey**2)

     ex = ex / distance !<-- Unit vector
     ey = ey / distance !<-- Unit vector

    !dr is the uniform spacing between the two nodes.
    dr = distance/real(ny-1,p2)

   !Generate interior nodes uniformly by going up from the body(B1) to the outer(B3,B4,B5)
   !Note: No stretching is applied here. It may be better to apply some stretching.
    do j = 2, ny-1
     xs(i,j) = xs(i,1) + dr*real(j-1)*ex
     ys(i,j) = ys(i,1) + dr*real(j-1)*ey
    end do

   end do

!--------------------------------------------------------------------------------
! 4. Generate unstructured data: 1D array to store the node information.
!
!
   write(*,*) "Generating 1D node array for unstructured grid data..."

!  Total number of nodes
   nnodes = nx*ny

!  Allocate the arrays
   allocate(x(nnodes),y(nnodes))
   allocate(bmark(nnodes))
   allocate(phi(nnodes),psi(nnodes),u(nnodes),v(nnodes))

! Node data: the nodes are ordered in 1D array.

  do j = 1, ny   !Go up in y-direction.
   do i = 1, nx  !Go to the right in x-direction.

    inode = i + (j-1)*nx   !<- Node number in the lexcographic ordering
      x(inode) =   xs(i,j)
      y(inode) =   ys(i,j)

    !Create boundary mark: =0 for interior nodes, =1 for boundary nodes
               bmark(inode) = 0
    if (i== 1) bmark(inode) = 1
    if (i==nx) bmark(inode) = 1
    if (j== 1) bmark(inode) = 1
    if (j==ny) bmark(inode) = 1

    !Compute the exact solution
       distance = sqrt( x(inode)**2 + y(inode)**2 )
      if (y(inode) < zero) then
       theta = two*pi - acos( x(inode)/distance )
      else
       theta = acos( x(inode)/distance )
      endif
      phi(inode) = x(inode) + one/(four*pi)*log(distance**2)
      psi(inode) = y(inode) + theta/(two*pi)
        u(inode) = one + x(inode)/(two*pi)/distance**2
        v(inode) =       y(inode)/(two*pi)/distance**2

   end do
  end do

! Deallocate the structured data: xs and ys, which are not needed any more.
! - You guys helped me create the 1D array. Thanks!
  deallocate(xs, ys)

 write(*,*)
 write(*,*) " Nodes have been generated:"
 write(*,*) "       nx  =", nx
 write(*,*) "       ny  =", ny
 write(*,*) "    nx*ny  =", nx*ny
 write(*,*) "    nnodes =", nnodes
 write(*,*)
 write(*,*) " Now, generate elements..."
 write(*,*)

!-----------------------------------------------------------
!-----------------------------------------------------------
!-----------------------------------------------------------
!-----------------------------------------------------------

  !Boundary data for .su2 file.
   nb = 6
   allocate( bnode( max(nx,ny,nxp), nb) )
   allocate( nbnodes(nb) )
   allocate(  bnames(nb) )

  !(1)Solid body(B1)

      ib = 1
      bnames( ib) = "half_body"
      nbnodes(ib) = nx
                j = 1
      do i = 1, nx
       bnode(i,ib) = i
      end do

  !(2)Lower outflow(B2)

      ib = 2
      bnames( ib) = "outflow_lower"
      nbnodes(ib) = ny
                i = 1
      do j = ny, 1, -1
       bnode(j,ib) = i + (j-1)*nx
      end do

  !(3)Bottom(B3)

      ib = 3
      bnames( ib) = "bottom"
      nbnodes(ib) = nxp
                j = ny
      do i = nxp, 1, -1
       bnode(i,ib) = i + (j-1)*nx
      end do

  !(4)Inflow(B4)

      ib = 4
      bnames( ib) = "inflow"
      nbnodes(ib) = nxp
                j = ny
      do i = nxp, 1, -1
       bnode(i,ib) = (i-1)+nxp + (j-1)*nx
      end do

  !(5)Top(B5)

      ib = 5
      bnames( ib) = "top"
      nbnodes(ib) = nxp
                j = ny
      do i = nxp, 1, -1
       bnode(i,ib) = nxp + nxp-1 + (i-1) + (j-1)*nx
      end do

  !(6)Top outflow(B6)

      ib = 6
      bnames( ib) = "outflow_upper"
      nbnodes(ib) = ny
                i = nx
      do i = 1, ny
       bnode(i,ib) = i + (j-1)*nx
      end do

!--------------------------------------------------------------------------------
! 5. Generate unstructured element data:
!
!    We generate both quadrilateral and triangular grids.
!    Both grids are constructed in the unstructured (finite-element) data.
!

! Allocate arrays of triangular and quad connectivity data.

!-----------------------------------------------------------
! (1)Generate a quadrilateral grid
!-----------------------------------------------------------

!   Number of quadrilaterals = (nx-1)(ny-1)

    allocate( quad((nx-1)*(ny-1)  ,4) )

  write(*,*) "Generating quad grid..."
  call generate_quad_grid
  write(*,*)
  write(*,*) " Number of quads =", nquad
  write(*,*)
  write(*,*) "Writing a tecplot file for the quadrilateral grid..."
  call write_tecplot_file(datafile_quad_tec)
  write(*,*) " --> File generated: ", datafile_quad_tec

  write(*,*) "Writing a grid file for the quadrilateral grid..."
  call write_grid_file(datafile_quad)
  write(*,*) " --> File generated: ", datafile_quad

   filename_su2   = "quad_rankine.su2"
   call write_su2_file(filename_su2,nnodes,tria,ntria,quad,nquad,x,y, &
                                              nb,nbnodes,bnode,bnames )
   filename_vtk   = "quad_rankine.vtk"
   call write_vtk_file(filename_vtk, nnodes,x,y, ntria,tria, &
                                                 nquad,quad  )

!-----------------------------------------------------------
! (2)Generate a triangular grid
!-----------------------------------------------------------

!   Number of triangles = 2*(nx-1)*(ny-1)

    allocate(  tria(2*(nx-1)*(ny-1),3) )

  write(*,*) "Generating triangular grid..."
  call generate_tria_grid

  write(*,*) "Applying smoothing and random perturbation..."
  if (irregular_grid) call smooth_perturb_tria_grid

    !Nodes smoothed and/or perturbed? Welll, we have to re-Compute the exact solution, then...
     do i = 1, nnodes
       distance = sqrt( x(i)**2 + y(i)**2 )
      if (y(i) < zero) then
       theta = two*pi - acos( x(i)/distance )
      else
       theta = acos( x(i)/distance )
      endif
      phi(i) = x(i) + one/(four*pi)*log(distance**2)
      psi(i) = y(i) + theta/(two*pi)
        u(i) = one + x(i)/(two*pi)/distance**2
        v(i) =       y(i)/(two*pi)/distance**2
     end do

  write(*,*)
  write(*,*) " Number of triangles =", ntria
  write(*,*)
  write(*,*) "Writing a tecplot file for the triangular grid..."
  call write_tecplot_file(datafile_tria_tec)
  write(*,*) " --> File generated: ", datafile_tria_tec

  write(*,*) "Writing a grid file for the triangular grid..."
  call write_grid_file(datafile_tria)
  write(*,*) " --> File generated: ", datafile_tria

  write(*,*)

   nquad = 0

   filename_su2   = "tria_rankine.su2"
   call write_su2_file(filename_su2,nnodes,tria,ntria,quad,nquad,x,y, &
                                              nb,nbnodes,bnode,bnames )
   filename_vtk   = "tria_rankine.vtk"
   call write_vtk_file(filename_vtk, nnodes,x,y, ntria,tria, &
                                                 nquad,quad  )

!-----------------------------------------------------------
! (3)Generate a mixed grid. (not implemented. I'll leave it to you! You can do it!)
!-----------------------------------------------------------
!
!-----------------------------------------------------------
! (4)Write a boundary condition file for your sovler
!-----------------------------------------------------------
  write(*,*) "Generating bcmap file..."
  open(unit=1, file=datafile_bcmap, status="unknown", iostat=os)
  write(1,*) "Boundary Segment  Boundary Condition"
  write(1,*) "               1   slip_wall"
  write(1,*) "               2     outflow"
  write(1,*) "               3     outflow"
  write(1,*) "               4      inflow"
  write(1,*) "               5     outflow"
  write(1,*) "               6     outflow"
  close(1)

!--------------------------------------------------------------------------------

!-----------------------------------------------------------
!-----------------------------------------------------------
!-----------------------------------------------------------
!-----------------------------------------------------------

!-----------------------------------------------------------
!-----------------------------------------------------------
!-----------------------------------------------------------
!-----------------------------------------------------------

 write(*,*)
 write(*,*) "Successfully completed. Stop."

 stop

 contains


!********************************************************************************
! This subroutine apply smoothing and/or perturbation to the triangular grid
!********************************************************************************
 subroutine smooth_perturb_tria_grid
 implicit none
!Local variables
 integer :: i, v1,v2,v3, k, j

 
 integer , dimension(:,:), allocatable :: nghbr
 integer , dimension(:)  , allocatable :: nnghbrs
 real(p2) :: dx, dy, factor, rn

 factor = 0.2_p2

 !Construct neighbor data

  allocate(nghbr(nnodes,16),nnghbrs(nnodes))
  nnghbrs = 0
    nghbr = 0

  do i = 1, ntria

   v1 = tria(i,1)
   v2 = tria(i,2)
   v3 = tria(i,3)

   !Node 1 has node 2 and node 3 as neighbors.
   nnghbrs(v1) = nnghbrs(v1) + 1
   nghbr(v1,nnghbrs(v1)) = v2
   nnghbrs(v1) = nnghbrs(v1) + 1
   nghbr(v1,nnghbrs(v1)) = v3

   !Node 2 has node 1 and node 3 as neighbors.
   nnghbrs(v2) = nnghbrs(v2) + 1
   nghbr(v2,nnghbrs(v2)) = v1
   nnghbrs(v2) = nnghbrs(v2) + 1
   nghbr(v2,nnghbrs(v2)) = v3

   !Node 3 has node 1 and node 2 as neighbors.
   nnghbrs(v3) = nnghbrs(v3) + 1
   nghbr(v3,nnghbrs(v3)) = v1
   nnghbrs(v3) = nnghbrs(v3) + 1
   nghbr(v3,nnghbrs(v3)) = v2

  end do

 !Apply smoothing: Average the coordinates with a small relaxation factor.
 ! You can play with the maximum number which is set 150 here.
  smoothing_steps : do k = 1, 150

   do i = 1, nnodes
   if (bmark(i)/=0) cycle

     dx = zero
     dy = zero

    nghbr_loop : do j = 1, nnghbrs(i)
     dx = dx + x(nghbr(i,j))-x(i)
     dy = dy + y(nghbr(i,j))-y(i)
    end do nghbr_loop

     x(i) = x(i) + factor * dx/real(nnghbrs(i),p2)
     y(i) = y(i) + factor * dy/real(nnghbrs(i),p2)

   end do

  end do smoothing_steps

  !Apply random perturbation: just do it randomly!

   do i = 1, nnodes
   if (bmark(i)/=0) cycle !Skip boundary nodes

     dx = zero
     dy = zero
    do j = 1, nnghbrs(i)
     dx = dx + abs(x(nghbr(i,j))-x(i))
     dy = dy + abs(y(nghbr(i,j))-y(i))
    end do

     call random_number(rn)
    if (x(i) > zero .or. abs(y(i)) > 0.5_p2) then !<-- ? Just random!
     x(i) = x(i) + 0.50_p2*(two*rn-one)*dx/real(nnghbrs(i),p2) !<-- 0.5? Just random!
     y(i) = y(i) + 0.50_p2*(two*rn-one)*dy/real(nnghbrs(i),p2)
    else
     x(i) = x(i) + 0.30_p2*(two*rn-one)*dx/real(nnghbrs(i),p2) !<-- 0.3? Just random!
     y(i) = y(i) + 0.30_p2*(two*rn-one)*dy/real(nnghbrs(i),p2)
    endif

   end do

 end subroutine smooth_perturb_tria_grid

!********************************************************************************
! This subroutine generates triangles by constructing the connectivity data.
!********************************************************************************
 subroutine generate_tria_grid
 implicit none
!Local variables
 integer  :: i, j, inode, i1, i2, i3, i4

! No quads
 nquad = 0
  quad = 0

! Trianguler grid with right-up diagonals (i.e., / ).
!
!  inode+nx   inode+nx+1     i4      i3
!       o--------o           o--------o
!       |     .  |           |     .  |
!       |   .    |     or    |   .    |
!       | .      |           | .      |
!       o--------o           o--------o
!    inode    inode+1        i1      i2
!
! Triangle is defined by the counterclockwise ordering of nodes.

 ntria = 0

 do j = 1, ny-1
  do i = 1, nx-1

   inode = i + (j-1)*nx

!     Define the local numbers (see figure above)
      i1 = inode
      i2 = inode + 1
      i3 = inode + nx + 1
      i4 = inode + nx

           ntria = ntria + 1
    tria(ntria,1) = i1
    tria(ntria,2) = i2
    tria(ntria,3) = i3

           ntria = ntria + 1
    tria(ntria,1) = i1
    tria(ntria,2) = i3
    tria(ntria,3) = i4

  end do
 end do

 end subroutine generate_tria_grid
!********************************************************************************


!********************************************************************************
! This subroutine generates quads by constructing the connectivity data.
!********************************************************************************
 subroutine generate_quad_grid
 implicit none
!Local variables
 integer :: i, j, inode, i1, i2, i3, i4

! No triangles
  ntria = 0
   tria = 0

!
!  inode+nx   inode+nx+1     i4      i3
!       o--------o           o--------o
!       |        |           |        |
!       |        |     or    |        |
!       |        |           |        |
!       o--------o           o--------o
!     inode   inode+1        i1      i2
!
! Quad is defined by the counterclockwise ordering of nodes.

! Quadrilateral grid

 nquad = 0

 do j = 1, ny-1
  do i = 1, nx-1

   inode = i + (j-1)*nx
!     Define the local numbers (see figure above)
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
! This subroutine writes a tecplot file.
!********************************************************************************
 subroutine write_tecplot_file(datafile)
 implicit none
 character(80),            intent(in) :: datafile
 integer :: os
!--------------------------------------------------------------------------------
 open(unit=1, file=datafile, status="unknown", iostat=os)
 write(1,*) 'title = "grid"'
 write(1,*) 'variables = "x","y","phi","psi","u","v"'
 write(1,*) 'zone N=',nnodes,',E=',ntria+nquad,',ET=quadrilateral,F=FEPOINT'
!--------------------------------------------------------------------------------
 do i = 1, nnodes
  write(1,*) x(i),y(i), phi(i),psi(i),u(i),v(i)
 end do
!--------------------------------------------------------------------------------
!Triangles
 if (ntria > 0) then
  do i = 1, ntria
   write(1,*)  tria(i,1),  tria(i,2), tria (i,3),  tria(i,3) !The last one is a dummy.
  end do
 endif

!Quadrilaterals
 if (nquad > 0) then
  do i = 1, nquad
   write(1,*) quad(i,1), quad(i,2), quad(i,3), quad(i,4)
  end do
 endif
!--------------------------------------------------------------------------------
 close(1)
 end subroutine write_tecplot_file
!********************************************************************************

!********************************************************************************
! This subroutine writes a grid file to be read by a solver.
! NOTE: Unlike the tecplot file, this files contains boundary info.
!********************************************************************************
 subroutine write_grid_file(datafile)
 implicit none
 character(80),            intent(in) :: datafile
 integer :: os
!--------------------------------------------------------------------------------
 open(unit=1, file=datafile, status="unknown", iostat=os)

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

! Quad connectivity
  if (nquad > 0) then
   do i = 1, nquad
    write(1,*) quad(i,1), quad(i,2), quad(i,3), quad(i,4) 
   end do
  endif

! Boundary data:
!
! Number of boundary segments: Anti-clockwise (move along with the domain on your left.)
  write(1,*) 6

  write(1,*) nx          !Solid body    (B1)
  write(1,*) ny          !Lower outflow (B2)
  write(1,*) nxp         !Bottom outer  (B3)
  write(1,*) nxp         !Left inflow   (B4)
  write(1,*) nxp         !Top    outer  (B5)
  write(1,*) ny          !Upper outflow (B6)

  write(1,*)

! Solid body(B1)
   j = 1
  do i = 1, nx
    write(1,*) i
  end do

! Lower outflow(B2)
  i = 1
  do j = ny, 1, -1
    write(1,*) i + (j-1)*nx
  end do

! Bottom outer(B3)
   j = ny
  do i = nxp, 1, -1
    write(1,*) i + (j-1)*nx
  end do

! Left inflow(B4)
   j = ny
  do i = nxp, 1, -1
    write(1,*) (i-1)+nxp + (j-1)*nx
  end do

! Top outer(B5)
   j = ny
  do i = nxp, 1, -1
    write(1,*) nxp + nxp-1 + i-1 + (j-1)*nx
  end do

! Upper outflow(B6)
   i = nx
  do j = 1, ny
    write(1,*) i + (j-1)*nx
  end do

!--------------------------------------------------------------------------------
 close(1)
 end subroutine write_grid_file
!********************************************************************************

!********************************************************************************
! This subroutine computes an integral of (u^2+v^2) along the half body
! by the trapezoidal rule with n segments.
! Note: n must be an odd number to avoid the singularity.
! Note: Try some different values of n. The integral value doesn't fully converge.
!       Not sure exactly why at the moment.
!********************************************************************************
 subroutine integral_u2_plus_v2(n)
 implicit none

 integer, intent(in) :: n

 real(p2) :: integral_value, t1,t2, x1,y1, x2,y2, u1,v1, u2,v2, f1,f2
 real(p2) :: dtheta, distance, dis_min, dis_max, temp
 integer  :: i

  if (mod(n,2)==0) then
   write(*,*) " n must be an odd number to avoid the singularity: n = ", n
   write(*,*) " Change n, and try again. Stop at integral_u2_plus_v2..."
  endif

         dis_min =  1.0e+09
         dis_max = -one
  integral_value = zero

  !Add up the trapezoidal rule applied to n pieces of divided segments along the half body.
  do i = 1, n

      dtheta = (theta_max-theta_min)/real(n,p2)
          t1 = theta_max - dtheta*real(i-1,p2)
          t2 = theta_max - dtheta*real(i  ,p2)

          y1 = half*(one-t1/pi)
          y2 = half*(one-t2/pi)

          x1 = y1/tan(t1)
          x2 = y2/tan(t2)

        temp = half/pi/(x1**2+y1**2)
          u1 = one + x1*temp
          v1 =       y1*temp

        temp = half/pi/(x2**2+y2**2)
          u2 = one + x2*temp
          v2 =       y2*temp

          f1 = u1**2 + v1**2
          f2 = u2**2 + v2**2

    distance = sqrt( (x2-x1)**2 + (y2-y1)**2 )
    dis_min  = min(dis_min,distance)
    dis_max  = max(dis_max,distance)

   integral_value = integral_value  +  half*( f1 + f2 )*distance

  end do

  write(*,'(a25,es25.16,a6,i10,2es10.3)') " Integral of (u^2+v^2) = ", &
                           integral_value, " N = ",n, dis_min, dis_max

 end subroutine integral_u2_plus_v2



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
 real(p2)     , dimension(:)  , intent(in) :: x, y
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
  real(p2)     , dimension(:  ), intent(in) :: x, y
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





 end program twod_rankine_half_body_grid
