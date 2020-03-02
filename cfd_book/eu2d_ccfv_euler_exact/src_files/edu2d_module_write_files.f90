!********************************************************************************
! Educationally-Designed Unstructured 2D (EDU2D) Code
!
!  ---------------- EDU2D-CCFV-Euler-LVL0
!
!  - Common data module
!
! This module containes subroutiens that write output files.
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

 module module_write_files

  implicit none

  public :: write_tecplot_file
  public :: write_vtk_file

 contains

!*******************************************************************************
! This subroutine writes a Tecplot file for the grid whose name is defined by
! filename_tecplot.
!*******************************************************************************
 subroutine write_tecplot_file

!To access the grid data required to write a Tecplot file.
  use module_common_data, only : nnodes      , & !# of nodes
                                 x, y        , & !nodal coords
                                 ntria, tria , & !# of triangles and triangle list
                                 nquad, quad , & !# of quads and quad list
                                 p2, zero, bc_type


!To access the output tecplot filename.
  use module_common_data, only : filename_tecplot

!To access the solution data.
  use module_ccfv_data_grid, only : cell, ncells, bound
  use module_ccfv_data_soln, only : w, ir, iu, iv, ip

  use module_input_parameter       , only : project_name

  implicit none

  integer :: i, os, ibn
  character(80) :: filename_tec_b

 !------------------------------------------------------------------------------
 !------------------------------------------------------------------------------
 !------------------------------------------------------------------------------
 ! Compute solutions at nodes from solutions in cells to simplify visualization.
 !
 ! Note: For 2nd-order scheme, this needs to be done with linear interpolation.
 ! Note: Tecplot has an option to load cell-centered data.
 !------------------------------------------------------------------------------

  integer                           :: j, k
  real(p2), dimension(:,:), pointer :: wn
  integer , dimension(:  ), pointer :: nc

  allocate(wn(nnodes,4))
  allocate(nc(nnodes  ))

   nc = 0    !<- nc(j) = # of cells contributing to node j.
   wn = zero !<- Initialize

   do i = 1, ncells

   !Loop over vertices of the cell i
    do k = 1, cell(i)%nvtx

     wn( cell(i)%vtx(k),:) = wn( cell(i)%vtx(k),:) + w(i,:) !<- Add up solutions
     nc( cell(i)%vtx(k)  ) = nc( cell(i)%vtx(k)  ) + 1      !<- Count # of contributing cells

    end do

   end do

   do j = 1, nnodes
     wn(j,:) = wn(j,:) / real(nc(j),p2) !<- Compute an average.
   end do

 !------------------------------------------------------------------------------
 !------------------------------------------------------------------------------
 !------------------------------------------------------------------------------

  write(*,*)
  write(*,*) "-------------------------------------------------------"
  write(*,*) ' Writing Tecplot file = ', trim(filename_tecplot)
  write(*,*)

 !Open the output file.
  open(unit=8, file=filename_tecplot, status="unknown", iostat=os)

!---------------------------------------------------------------------------

 !(0)Header information

  write(8,*) 'TITLE = "GRID"'
  write(8,*) 'VARIABLES = "x","y","rho","u","v","p"'

 !(1)Nodal information.

   write(8,*) 'zone  n=', nnodes,',e=', ntria+nquad,' , zonetype=fequadrilateral, datapacking=point'
   do j = 1, nnodes
     write(8,'(8es25.15)') x(j), y(j), wn(j,ir), wn(j,iu), wn(j,iv), wn(j,ip)
   end do

 !(2)List of triangles (as a degenerate quadrilateral).

  if (ntria > 0) then
   do i = 1, ntria
    write(8,'(4i10)') tria(i,1), tria(i,2), tria(i,3), tria(i,3)
   end do
  endif

 !(3)List of quadrilaterals

  if (nquad > 0) then
   do i = 1, nquad
    write(8,'(4i10)') quad(i,1), quad(i,2), quad(i,3), quad(i,4)
   end do
  endif

!---------------------------------------------------------------------------

 !Close the output file.
  close(8)

  write(*,*)
  write(*,*) ' End of Writing Tecplot file = ', trim(filename_tecplot)
  write(*,*) "-------------------------------------------------------"
  write(*,*)

!---------------------------------------------------------------------------
! Write out a x-y data for plotting solutions over the 1st boundary.
!---------------------------------------------------------------------------

 i = 1

 filename_tec_b = trim(project_name) // '_tec_b1.dat'
 open(unit=1, file=filename_tec_b, status="unknown", iostat=os)

 write(1,'(a)') 'title = "boundary data"'
 write(1,'(a)') 'variables = "x","y","rho","u","v","p"'
 write(1,*) 'zone t=',trim(bc_type(i)), ' I=',bound(i)%nbnodes, ' F=POINT'

 do j = 1, bound(i)%nbnodes
  ibn = bound(i)%bnode(j)
    write(1,*) x(ibn), x(ibn), (wn(ibn,k), k=1,4)
 end do

!---------------------------------------------------------------------------
!---------------------------------------------------------------------------


 end subroutine write_tecplot_file
!********************************************************************************

!*******************************************************************************
! This subroutine writes a .vtk file for the grid whose name is defined by
! filename_vtk.
!
! Use Paraview to read .vtk and visualize it.  https://www.paraview.org
!
! Search in Google for 'vkt format' to learn .vtk file format.
!*******************************************************************************
 subroutine write_vtk_file

!To access the grid data required to write a Tecplot file.
  use module_common_data, only : nnodes      , & !# of nodes
                                 x, y        , & !nodal coords
                                 ntria, tria , & !# of triangles and triangle list
                                 nquad, quad , & !# of quads and quad list
                                 p2, zero

!To access the output .vtk filename.
  use module_common_data, only : filename_vtk

!To access the solution data.
  use module_ccfv_data_grid, only : cell, ncells
  use module_ccfv_data_soln, only : w, ir, iu, iv, ip

  implicit none

  integer :: i, j, os

 !------------------------------------------------------------------------------
 !------------------------------------------------------------------------------
 !------------------------------------------------------------------------------
 ! Compute solutions at nodes from solutions in cells to simplify visualization.
 !
 ! Note: For 2nd-order scheme, this needs to be done with linear interpolation.
 ! Note: Tecplot has an option to load cell-centered data.
 !------------------------------------------------------------------------------

  integer                           :: k
  real(p2), dimension(:,:), pointer :: wn
  integer , dimension(:  ), pointer :: nc

  allocate(wn(nnodes,4))
  allocate(nc(nnodes  ))

   nc = 0    !<- nc(j) = # of cells contributing to node j.
   wn = zero !<- Initialize

   do i = 1, ncells

   !Loop over vertices of the cell i
    do k = 1, cell(i)%nvtx

     wn( cell(i)%vtx(k),:) = wn( cell(i)%vtx(k),:) + w(i,:) !<- Add up solutions
     nc( cell(i)%vtx(k)  ) = nc( cell(i)%vtx(k)  ) + 1      !<- Count # of contributing cells

    end do

   end do

   do j = 1, nnodes
     wn(j,:) = wn(j,:) / real(nc(j),p2) !<- Compute an average.
   end do

 !------------------------------------------------------------------------------
 !------------------------------------------------------------------------------
 !------------------------------------------------------------------------------

  write(*,*)
  write(*,*) "-------------------------------------------------------"
  write(*,*) ' Writing .vtk file = ', trim(filename_vtk)
  write(*,*)

 !Open the output file.
  open(unit=8, file=filename_vtk, status="unknown", iostat=os)

!---------------------------------------------------------------------------
! Header information

  write(8,'(a)') '# vtk DataFile Version 3.0'
  write(8,'(a)') filename_vtk
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

!---------------------------------------------------------------------------
! Field data (e.g., density, pressure, velocity)are added here for visualization.

   write(8,*) 'POINT_DATA   ',nnodes

  !            FIELD  dataName    # of arrays (variables tp plot)
   write(8,*) 'FIELD  FlowField ', 4

   write(8,*) 'Density   ',  1 , nnodes, ' double'
   do j = 1, nnodes
    write(8,'(es25.15)') wn(j,ir)
   end do

   write(8,*) 'X-velocity ', 1 , nnodes, ' double'
   do j = 1, nnodes
    write(8,'(es25.15)') wn(j,iu)
   end do

   write(8,*) 'Y-veloiity ', 1 , nnodes, ' double'
   do j = 1, nnodes
    write(8,'(es25.15)') wn(j,iv)
   end do

   write(8,*) 'Pressure   ', 1 , nnodes, ' double'
   do j = 1, nnodes
    write(8,'(es25.15)') wn(j,ip)
   end do

!---------------------------------------------------------------------------

 !Close the output file.
  close(8)

  write(*,*)
  write(*,*) ' End of Writing .vtk file = ', trim(filename_vtk)
  write(*,*) "-------------------------------------------------------"
  write(*,*)


 end subroutine write_vtk_file
!********************************************************************************


 end module module_write_files

