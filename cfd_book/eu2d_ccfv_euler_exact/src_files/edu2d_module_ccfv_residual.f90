!********************************************************************************
!  Educationally-Designed Unstructured 2D (EDU2D) Code
!
!  ---------------- EDU2D-CCFV-Euler-EXPLCT
!
! This is module_ccfv_residual.
!
! This module containes a subroutine that comptutes the residuals at cells for
! the cell-centered finite-volume discretization.
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

 module module_ccfv_residual

 !This module contains the following subroutine:
 
  public :: compute_residual ! compute the residual

 contains

!********************************************************************************
!
! This subtourine computes the residual at all cells based on the cell-centered
! discretization.
!
! The residual is computed in a loop over faces with a numerical flux computed
! at the face midpoint, followed by the boundary closure.
!
!********************************************************************************
 subroutine compute_residual

 use module_common_data     , only : p2, zero, half, one

 use module_common_data     , only : x, y, bc_type

 use module_ccfv_data_grid  , only : nfaces, face, ncells, cell, bound, nbound, face_nrml, face_nrml_mag

 use module_ccfv_data_soln  , only : res, u, gradw, wsn

 use module_flux            , only : interface_flux
 use module_bc_states       , only : get_right_state
 use module_ccfv_gradient   , only : compute_gradients
 use module_input_parameter , only : second_order, use_limiter
 use module_ccfv_limiter    , only : compute_limiter, phi

 implicit none


!Local variables

 real(p2)                 :: xm, ym
 integer                  :: i
 integer                  :: c1, c2

 real(p2), dimension(4)   :: u1, u2
 real(p2), dimension(4,2) :: gradw1, gradw2
 real(p2), dimension(2)   :: unit_face_normal

 real(p2), dimension(4)   :: num_flux
 integer                  :: j, ib, v1, v2
 real(p2), dimension(4)   :: ub
 real(p2)                 :: wave_speed
 real(p2)                 :: phi1, phi2

!--------------------------------------------------------------------------------
! Initialize the residuals and wsn = the sum of (max_wave_speed)*(face length)).
! Note: wsn is required to define a time step.

  cell_loop1 :  do i = 1, ncells

   res(i,:) = zero
   wsn(i)   = zero

  end do cell_loop1

!--------------------------------------------------------------------------------
! Compute gradients at cells.

 !For now, let's set gradients to be zero in all cells...
 !Later we'll implement a subroutine that computes gradients.

  cell_loop2 :  do i = 1, ncells

   gradw(i,:,:) = zero

  end do cell_loop2

  if (second_order) call compute_gradients
  if (use_limiter)  call compute_limiter

!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
! Residual computation: interior faces

!--------------------------------------------------------------------------------
! Flux computation across internal faces (to be accumulated in res(:))
!
!          v2=Left(2)
!        o---o---------o       face(j,:) = [i,k,v2,v1]
!       .    .          .
!      .     .           .
!     .      .normal      .
!    .  Left .--->  Right  .
!   .   c1   .       c2     .
!  .         .               .
! o----------o----------------o
!          v1=Right(1)
!
!
! 1. Extrapolate the solutions to the face-midpoint from centroids 1 and 2.
! 2. Compute the numerical flux.
! 3. Add it to the residual for 1, and subtract it from the residual for 2.
!
!--------------------------------------------------------------------------------
  loop_faces : do i = 1, nfaces

 ! Left and right cells of the i-th face

     c1 = face(i,1)  ! Left cell of the face
     c2 = face(i,2)  ! Right cell of theface

     v1 = face(i,3)  ! Left  node of the face
     v2 = face(i,4)  ! Right node of the face

     u1 = u(c1,1:4) !Conservative variables at c1
     u2 = u(c2,1:4) !Conservative variables at c2

    gradw1 = gradw(c1,1:4,1:2) !Gradient of primitive variables at c1
    gradw2 = gradw(c2,1:4,1:2) !Gradient of primitive variables at c2

   unit_face_normal = face_nrml(i,1:2) !Unit face normal vector: c1 -> c2.

   !Face midpoint at which we compute the flux.
     xm = half*( x(v1) + x(v2) )
     ym = half*( y(v1) + y(v2) )

   !Set limiter functions
     if (use_limiter) then
      phi1 = phi(c1)
      phi2 = phi(c2)
     else
      phi1 = one
      phi2 = one
     endif

 ! Reconstruct the solution to the face midpoint and compute a numerical flux.
 ! (reconstruction is implemented inside "interface_flux".

   call interface_flux(          u1,       u2   , & !<- Left/right states
                             gradw1,      gradw2, & !<- Left/right gradients
                                unit_face_normal, & !<- unit face normal
                        cell(c1)%xc, cell(c1)%yc, & !<- Left  cell centroid
                        cell(c2)%xc, cell(c2)%yc, & !<- Right cell centroid
                                 xm,          ym, & !<- face midpoint
                               phi1,        phi2, & !<- Limiter functions
                            num_flux, wave_speed  ) !<- Output

 !  Add the flux multiplied by the magnitude of the directed area vector to c1.

     res(c1,:) = res(c1,:)  +  num_flux * face_nrml_mag(i)
       wsn(c1) = wsn(c1)    + wave_speed* face_nrml_mag(i)

 !  Subtract the flux multiplied by the magnitude of the directed area vector from c2.
 !  NOTE: Subtract because the outward face normal is -n for the c2.

     res(c2,:) = res(c2,:)  -  num_flux * face_nrml_mag(i)
       wsn(c2) = wsn(c2)    + wave_speed* face_nrml_mag(i)

  end do loop_faces

! End of Residual computation: interior faces
!--------------------------------------------------------------------------------


!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
!--------------------------------------------------------------------------------
! Residual computation: boundary faces:
!
! Close the residual by looping over boundary faces and distribute a contribution
! to the corresponding cell.

! Boundary face j consists of nodes j and j+1.
!
!  Interior domain      /
!                      /
!              /\     o
!             /  \   /
!            / c1 \ /   Outside the domain
! --o-------o------o
!           j   |  j+1
!               |   
!               v Face normal for the face j.
!
! c = bcell, the cell having the boundary face j.
!

  boundary_part : do ib = 1, nbound

   bface : do j = 1, bound(ib)%nbfaces

     v1 = bound(ib)%bnode(j)
     v2 = bound(ib)%bnode(j+1)

    !Face midpoint at which we compute the flux.
     xm = half*( x(v1) + x(v2) )
     ym = half*( y(v1) + y(v2) )

    !Set limiter functions
     if (use_limiter) then
      phi1 = phi(c1)
      phi2 = one
     else
      phi1 = one
      phi2 = one
     endif

    !Cell having a boundary face defined by the set of nodes j and j+1.
     c1 = bound(ib)%bcell(j)

         u1 = u(c1,1:4)
     gradw1 = gradw(c1,1:4,1:2)

     unit_face_normal = bound(ib)%bface_nrml(j,1:2)

   !---------------------------------------------------
   ! Get the right state (weak BC!)

     call get_right_state(xm,ym, u1, unit_face_normal, bc_type(ib), ub)

     gradw2 = gradw2 !<- Gradient at the right state. Give the same gradient for now.

   !---------------------------------------------------
   ! Compute a flux at the boundary face.

     call interface_flux(           u1(1:4), ub(1:4) , & !<- Left/right states
                                     gradw1,  gradw2 , & !<- Left/right same gradients
                                     unit_face_normal, & !<- unit face normal
                          cell(c1)%xc, cell(c1)%yc   , & !<- Left cell centroid
                                   xm,          ym   , & !<- Set right centroid = (xm,ym)
                                   xm,          ym   , & !<- face midpoint
                                 phi1,        phi2   , & !<- Limiter functions
                                 num_flux,  wave_speed ) !<- Output

    !Note: No gradients available outside the domain, and use the gradient at cell c
    !      for the right state. This does nothing to inviscid fluxes (see below) but
    !      is important for viscous fluxes.

    !Note: Set right centroid = (xm,ym) so that the reconstruction from the right cell
    !      that doesn't exist is automatically cancelled: wR=wb+gradw*(xm-xc2)=wb.

   !---------------------------------------------------
   ! Add the boundary contributions to the residual.

     res(c1,:) = res(c1,:)  + num_flux * bound(ib)%bface_nrml_mag(j)

       wsn(c1) = wsn(c1)  + wave_speed * bound(ib)%bface_nrml_mag(j)

   end do bface

  end do boundary_part 

! End of Residual computation: boundary faces
!--------------------------------------------------------------------------------

 end subroutine compute_residual
!********************************************************************************

 end module module_ccfv_residual
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
