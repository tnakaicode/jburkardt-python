#! /usr/bin/env python3
#
def task_division_test ( ):

#*****************************************************************************80
#
## task_division_test() tests task_division().
#
#  Discussion:
#
#    This program simply demonstrates how one might automate the
#    assignment of T tasks to P processors, assuming that the assignment
#    is to be beforehand.
#
#    In that case, we just want to make sure that we assign each task
#    to a processor, that we assign about the same number of tasks
#    to each processor, and that we assign each processor a contiguous
#    range of tasks, say tasks I_LO to I_HI.
#
#    The routine that is called simulates this process.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'task_division_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  task_division() automates the division of' )
  print ( '  T tasks among a range of P processors' )
  print ( '  indexed from PROC_FIRST to PROC_LAST.' )

  task_number = 23
  proc_first = 0
  proc_last = 3
  task_division ( task_number, proc_first, proc_last )

  task_number = 17
  proc_first = 1
  proc_last = 6
  task_division ( task_number, proc_first, proc_last )

  task_number = 17
  proc_first = 4
  proc_last = 6
  task_division ( task_number, proc_first, proc_last )

  task_number = 5
  proc_first = -2
  proc_last = 6
  task_division ( task_number, proc_first, proc_last )

  task_number = 5
  proc_first = 0
  proc_last = 4
  task_division ( task_number, proc_first, proc_last )

  task_number = 5
  proc_first = 0
  proc_last = 0
  task_division ( task_number, proc_first, proc_last )

  task_number = 1000
  proc_first = 1
  proc_last = 17
  task_division ( task_number, proc_first, proc_last )
#
#  Terminate.
#
  print ( '' )
  print ( 'task_division_test():' )
  print ( '  Normal end of execution.' )

  return

def task_division ( task_number, proc_first, proc_last ):

#*****************************************************************************80
#
## task_division() divides tasks among processors.
#
#  Discussion:
#
#    This routine assigns each of T tasks to P processors, assuming that
#    the assignment is to be beforehand.
#
#    In that case, we just want to make sure that we assign each task
#    to a processor, that we assign about the same number of tasks
#    to each processor, and that we assign each processor a contiguous
#    range of tasks, say tasks I_LO to I_HI.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer TASK_NUMBER, the number of tasks.
#
#    integer PROC_FIRST, PROC_LAST, the first and last processors.
#
  p = proc_last + 1 - proc_first

  print ( '' )
  print ( 'task_division():' )
  print ( '  Divide T tasks among P processors.' )
  print ( '' )
  print ( '  Number of tasks T = ', task_number )
  print ( '  Number of processors P = ', p )
  print ( '' )
  print ( '  P_FIRST = ', proc_first )
  print ( '  P_LAST =  ', proc_last )
  print ( '' )
  print ( '             Number of   First      Last' )
  print ( ' Processor     Tasks     Task       Task' )
  print ( '' )

  i_hi = 0

  task_remain = task_number
  proc_remain = p

  for proc in range ( proc_first, proc_last + 1 ):

    task_proc = task_remain // proc_remain

    proc_remain = proc_remain - 1
    task_remain = task_remain - task_proc

    i_lo = i_hi + 1
    i_hi = i_hi + task_proc

    print ( '  %8d  %8d  %8d  %8d' % ( proc, task_proc, i_lo, i_hi ) )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  task_division_test ( )
  timestamp ( )

