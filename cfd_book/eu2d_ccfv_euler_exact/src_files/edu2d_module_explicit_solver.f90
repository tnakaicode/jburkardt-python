!********************************************************************************
!  Educationally-Designed Unstructured 2D (EDU2D) Code
!
!  ---------------- EDU2D-CCFV-Euler-EXPLCT
!
! This is module_explicit_solver.
!
!
! This module containes subroutines that integrates the 2D Euler equations
! in time by explicit schemes: e.g., the forward Euler scheme,
!
!   u^{n+1} = u^n - dt/V*Res(U)
!
! We can solve both steady and unsteady problems.
!
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

 module module_explicit_solver

 !This module contains the following subroutine:

  public :: explicit_steady_solver   ! solve a steady problem with local time step.
  public :: explicit_unsteady_solver ! solve an unsteady problem.

 contains

!*******************************************************************************
! Explicit Steady Solver: Ut + Fx + Gy = S, Ut -> 0.
!
! This subroutine solves a steady problem by explicit schemes with the time
! taken as a pseudo time, and thus we can use local time steps for speed up
! the convergence (and a local-preconditioning method if implemented).
!
! In other words, it solves a global system of nonlinear residual equations:
!   Res(U) = 0
! by explicit iteration schemes.
!
!*******************************************************************************
 subroutine explicit_steady_solver

  use module_common_data    , only : p2, one, half, filename_tec_hist
  use module_ccfv_residual  , only : compute_residual
  use module_input_parameter, only : tolerance, max_iteration

  use module_ccfv_data_soln , only : u, w, res, u2w
  use module_ccfv_data_grid , only : ncells, cell
  use module_ccfv_data_soln , only : dtau

  integer                :: i_iteration, i, stat, i_temp
  real(p2)               :: temp
  real(p2), dimension(4) :: res_norm
  real(p2), dimension(4) :: res_norm_initial
  real(p2), dimension(ncells,4) :: u0

  write(*,*)
  write(*,*) "---------------------------------------"
  write(*,*) " Pseudo time-Stepping"
  write(*,*)

  open(unit=1, file = "delete_me",  status="unknown")

 !-----------------------------------------------------------------------------
 !-----------------------------------------------------------------------------
 ! Pseudo time-stepping
 !-----------------------------------------------------------------------------
 !-----------------------------------------------------------------------------

  i_iteration = 0

  pseudo_time_loop : do

  !------------------------------------------------------
  ! Compute the residual (gradient computation is done within).

    call compute_residual

   !Compute the residual norm for checking convergence.

    call compute_residual_norm(res_norm)

   !Print residual status.

    !--- Initial (no solution update yet) ------------
    if (i_iteration == 0) then

     !Save the initial max res norm.
      res_norm_initial = res_norm

     !Print the headline.
      write(*,*) " Iteration   max(res)    max(res)/max(res)_initial "

     !Print the iteration number, max res, and the reduction of the max res = 1 for initial.
      write(*,'(i11,2es12.3)') i_iteration, maxval( res_norm(:) ), one
      write(1,*) i_iteration, one

    !--- After the first solution upate ------------
    else

     !Print the iteration number, max res, and the reduction of the max res.
      write(*,'(i11,2es12.3)') i_iteration, maxval( res_norm(:) ), maxval( res_norm(:)/res_norm_initial(:) )
      write(1,*) i_iteration, maxval( res_norm(:)/res_norm_initial(:) )

    endif

  !------------------------------------------------------
  ! Exit if the res norm is reduced below the tolerance specified by input.

    if ( maxval( res_norm(:)/res_norm_initial(:) ) < tolerance ) exit pseudo_time_loop

  !------------------------------------------------------
  ! Exit if we reach a specified number of iterations.

    if (i_iteration == max_iteration) exit pseudo_time_loop

  !------------------------------------------------------
  ! Increment the counter and go to the next iteration.

   i_iteration = i_iteration + 1 !<- This is the iteration that has just been done.

  !------------------------------------------------------
  ! Compute the local time step, dtau.

    call compute_local_time_step_dtau

  !------------------------------------------------------
  ! Update the solution by forward Euler scheme.

!    call forward_euler

  !-------------------------------------------------------------------
  ! Update the solution by 2nd-order TVD-RK.: u^n is saved as u0(:,:)
  !  1. u^*     = u^n - (dt/vol)*Res(u^n)
  !  2. u^{n+1} = 1/2*(u^n + u^*) - 1/2*(dt/vol)*Res(u^*)

  !-----------------------------
  !- 1st Stage of Runge-Kutta:

     u0 = u
    do i = 1, ncells
     u(i,:) = u0(i,:) - (dtau(i)/cell(i)%vol) * res(i,:) !This is u*.
     w(i,:) = u2w( u(i,:) )
    end do

  !-----------------------------
  !- 2nd Stage of Runge-Kutta:

    call compute_residual

    do i = 1, ncells
    u(i,:) = half*( u(i,:) + u0(i,:) ) - half*(dtau(i)/cell(i)%vol) * res(i,:)
    w(i,:) = u2w( u(i,:) )
    end do

  end do pseudo_time_loop

 !-----------------------------------------------------------------------------
 !-----------------------------------------------------------------------------
 ! End of Time-stepping
 !-----------------------------------------------------------------------------
 !-----------------------------------------------------------------------------

 !-----------------------------------------------------------------------------
 ! Print the exit status.

    write(*,*)
 
   if (i_iteration < max_iteration) then

    write(*,*) " Converged to the requested tolerance. "

   else

    write(*,*) " Max iteration reached..... "

   endif

 !-----------------------------------------------------------------------------
 ! Write a data file for plotting the convergence history:
 ! maximum L1 residual norm versus iteration.

  open(unit=2, file = filename_tec_hist,  status="unknown")

  write(2,*) "title = ",'"Convergence history"'
  write(2,*) "variables = ",'"Iteration",','"R1max"'
  write(2,*) "zone", " i = ",i_iteration+1, "f = point"

  rewind(1) !rewind the 'delete_me' file. Back to the top of the file.

  do i = 1, i_iteration+1  !<- includes the initial residual.
   read( 1,*) i_temp, temp !read from "delete_me"
   write(2,*) i_temp, temp !write to filename_tec_hist
  end do

  close(1)
  close(2)

 !Delete the temporary file 'delete_me'.
  open(unit=1, iostat=stat, file="delete_me", status='old')
  if (stat == 0) close(1, status='delete')

 !-----------------------------------------------------------------------------

  write(*,*)
  write(*,*) " End of Pseudo time-Stepping"
  write(*,*) "---------------------------------------"
  write(*,*)

 end subroutine explicit_steady_solver
!*******************************************************************************


!*******************************************************************************
! Explicit Unsteady Solver: Ut + Fx + Gy = S
!
! This subroutine solves an un steady problem by 2nd-order TVD-RK with a
! global time step.
!
!*******************************************************************************
 subroutine explicit_unsteady_solver

  use module_common_data    , only : p2, half, zero
  use module_ccfv_residual  , only : compute_residual
  use module_ccfv_data_grid , only : ncells, cell
  use module_ccfv_data_soln , only : u, w, res, u2w
  use module_input_parameter, only : t_final

  real(p2)                      :: dt, time
  logical                       :: final_step
  real(p2), dimension(ncells,4) :: u0
  integer                       :: i

  final_step = .false.

  write(*,*)
  write(*,*) "---------------------------------------"
  write(*,*) " Physical Time-Stepping"
  write(*,*)

 !-----------------------------------------------------------------------------
 !-----------------------------------------------------------------------------
 ! Physical time-stepping
 !-----------------------------------------------------------------------------
 !-----------------------------------------------------------------------------

  time = zero
  write(*,*) " time = ", time

  physical_time_loop : do

  !-------------------------------------------------------------------
  ! Compute the residual: res(i,:)

    call compute_residual

  !-------------------------------------------------------------------
  ! Compute the global time step, dt. One dt for all cells.

    call compute_global_time_step(dt)

    if (time+dt > t_final) then
     dt = t_final - time
     final_step = .true.
    write(*,*) " Adjusted"
    endif

  !-------------------------------------------------------------------
  ! Increment the physical time and exit if the final time is reached.

    time = time + dt

    write(*,*) " time = ", time, " dt = ", dt

  !-------------------------------------------------------------------
  ! Update the solution by 2nd-order TVD-RK.: u^n is saved as u0(:,:)
  !  1. u^*     = u^n - (dt/vol)*Res(u^n)
  !  2. u^{n+1} = 1/2*(u^n + u^*) - 1/2*(dt/vol)*Res(u^*)

  !-----------------------------
  !- 1st Stage of Runge-Kutta:

     u0 = u
    do i = 1, ncells
     u(i,:) = u0(i,:) - (dt/cell(i)%vol) * res(i,:) !This is u*.
     w(i,:) = u2w( u(i,:) )
    end do

  !-----------------------------
  !- 2nd Stage of Runge-Kutta:

    call compute_residual

    do i = 1, ncells
    u(i,:) = half*( u(i,:) + u0(i,:) ) - half*(dt/cell(i)%vol) * res(i,:)
    w(i,:) = u2w( u(i,:) )
    end do

    if (final_step) exit physical_time_loop

  end do physical_time_loop

 !-----------------------------------------------------------------------------
 !-----------------------------------------------------------------------------
 ! End of Physical time-stepping
 !-----------------------------------------------------------------------------
 !-----------------------------------------------------------------------------

  write(*,*)
  write(*,*) " End of Physical Time-Stepping"
  write(*,*) "---------------------------------------"
  write(*,*)

 end subroutine explicit_unsteady_solver
!*******************************************************************************


!********************************************************************************
!
! This subroutine computes the residual L1 norm (average of the absolute value).
!
!********************************************************************************
 subroutine compute_residual_norm(res_norm)

  use module_common_data   , only : p2, zero
  use module_ccfv_data_grid, only : ncells
  use module_ccfv_data_soln, only : res

  implicit none

  real(p2), dimension(4), intent(out) :: res_norm

 !Local variables
  integer                :: i

 !Initialize the norm:
   res_norm(:) =  zero

  cell_loop : do i = 1, ncells

   res_norm(:) = res_norm(:) + abs( res(i,:) ) !L1 norm

  end do cell_loop

   res_norm(:) = res_norm(:)/real(ncells,p2)   !L1 norm

 end subroutine compute_residual_norm
!********************************************************************************


!********************************************************************************
!
! This subroutine computes the local pseudo-time step at each node.
!
!********************************************************************************
 subroutine compute_local_time_step_dtau

  use module_common_data    , only : half
  use module_ccfv_data_grid , only : ncells, cell
  use module_ccfv_data_soln , only : dtau, wsn
  use module_input_parameter, only : CFL

  implicit none

  integer :: i

  cell_loop : do i = 1, ncells

  ! Local time step: dtau = CFL*volume/sum(0.5*max_wave_speed*face_area).

   dtau(i) = CFL * cell(i)%vol/( half*wsn(i) )

  end do cell_loop

 end subroutine compute_local_time_step_dtau
!********************************************************************************


!********************************************************************************
!
! Solution update by the forward Euler with local time stepping.
!
!********************************************************************************
 subroutine forward_euler

  use module_ccfv_data_grid, only : ncells, cell
  use module_ccfv_data_soln, only : res, u, dtau, w, u2w, w2u

  implicit none

  integer :: i

  cell_loop : do i = 1, ncells

  ! Forward Euler: Unew = Uold - (dtau/vol)*Res

    u(i,:) = u(i,:) - (dtau(i)/cell(i)%vol) * res(i,:)

  ! Update the primitive variables from the updated conservative variables.

    w(i,:) = u2w( u(i,:) )

  end do cell_loop

 end subroutine forward_euler
!*******************************************************************************



!********************************************************************************
!
! This subroutine computes the global time step.
!
!********************************************************************************
 subroutine compute_global_time_step(physical_time_step)

  use module_common_data    , only : p2, half
  use module_ccfv_data_grid , only : ncells, cell
  use module_ccfv_data_soln , only : wsn
  use module_input_parameter, only : CFL

  implicit none

  real(p2), intent(out) :: physical_time_step

  integer               :: i

  !Initialize dt with the local time step at cell 1.

    i = 1
    physical_time_step = CFL*cell(i)%vol/( half*wsn(i) )

  !Set 'dt' to be the minimum of all local time steps.

   cell_loop : do i = 2, ncells

    physical_time_step = min( physical_time_step, CFL*cell(i)%vol/( half*wsn(i) ) )

   end do cell_loop

 end subroutine compute_global_time_step
!********************************************************************************



 end module module_explicit_solver
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------

