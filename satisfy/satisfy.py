#! /usr/bin/env python3
#
def satisfy ( ):

#*****************************************************************************80
#
## MAIN is the main program for SATISFY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michael Quinn,
#    Parallel Programming in C with MPI and OpenMP,
#    McGraw-Hill, 2004,
#    ISBN13: 978-0071232654,
#    LC: QA76.73.C15.Q55.
#
  import platform

  print ( '' )
  print ( 'SATISFY' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  We have a logical function of N logical arguments.' )
  print ( '  We do an exhaustive search of all 2^N possibilities,' )
  print ( '  seeking those inputs that make the function TRUE.' )
#
#  Compute the number of binary vectors to check.
#
  n = 23
  ihi = 2 ** n

  print ( '' )
  print ( '  The number of logical variables is N = %d' % ( n ) )
  print ( '  The number of input vectors to check is %d' % ( ihi ) )
  print ( '' )
  print ( '   #       Index    ---------Input Values------------------------' )
  print ( '' )
#
#  Check every possible input vector.
#
  solution_num = 0

  for i in range ( 0, ihi ):

    lvec = i4_to_lvec ( i, n )

    value = circuit_value ( n, lvec )

    if ( value ):
      solution_num = solution_num + 1
      print ( '  %2d  %10d   ' % ( solution_num, i ), end = '' )
      for j in range ( 0, n ):
        print ( ' %d' % ( lvec[j] ), end = '' )
      print ( '' )
#
#  Report.
#
  print ( '' )
  print ( '  Number of solutions found was %d\n' % ( solution_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SATISFY' )
  print ( '  Normal end of execution.' )
  return

def circuit_value ( n, lvec ):

#*****************************************************************************80
#
## CIRCUIT_VALUE returns the value of a circuit for a given input set.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michael Quinn,
#    Parallel Programming in C with MPI and OpenMP,
#    McGraw-Hill, 2004,
#    ISBN13: 978-0071232654,
#    LC: QA76.73.C15.Q55.
#
#  Parameters:
#
#    Input, integer N, the length of the input vector.
#
#    Input, bool LVEC(N), the binary inputs.
#
#    Output, bool CIRCUIT_VALUE, the output of the circuit.
#
  value = \
        (     lvec[0]  or     lvec[1]  ) \
    and ( not lvec[1]  or not lvec[3]  ) \
    and (     lvec[2]  or     lvec[3]  ) \
    and ( not lvec[3]  or not lvec[4]  ) \
    and (     lvec[4]  or not lvec[5]  ) \
    and (     lvec[5]  or not lvec[6]  ) \
    and (     lvec[5]  or     lvec[6]  ) \
    and (     lvec[6]  or not lvec[15] ) \
    and (     lvec[7]  or not lvec[8]  ) \
    and ( not lvec[7]  or not lvec[13] ) \
    and (     lvec[8]  or     lvec[9]  ) \
    and (     lvec[8]  or not lvec[9]  ) \
    and ( not lvec[9]  or not lvec[10] ) \
    and (     lvec[9]  or     lvec[11] ) \
    and (     lvec[10] or     lvec[11] ) \
    and (     lvec[12] or     lvec[13] ) \
    and (     lvec[13] or not lvec[14] ) \
    and (     lvec[14] or     lvec[15] ) \
    and (     lvec[14] or     lvec[16] ) \
    and (     lvec[17] or     lvec[1]  ) \
    and (     lvec[18] or not lvec[0]  ) \
    and (     lvec[19] or     lvec[1]  ) \
    and (     lvec[19] or not lvec[18] ) \
    and ( not lvec[19] or not lvec[9]  ) \
    and (     lvec[0]  or     lvec[17] ) \
    and ( not lvec[1]  or     lvec[20] ) \
    and ( not lvec[21] or     lvec[20] ) \
    and ( not lvec[22] or     lvec[20] ) \
    and ( not lvec[21] or not lvec[20] ) \
    and (     lvec[22] or not lvec[20] )

  return value

def i4_to_lvec ( i, n ) :

#*****************************************************************************80
#
## I4_TO_LVEC makes a boolean vector from an integer.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, a nonnegative integer to be represented.
#
#    Input, integer N, the dimension of the vector.
#
#    Output, integer LVEC(N), the logical vector.
#
  import numpy as np

  lvec = np.zeros ( n, dtype = np.bool )

  for j in range ( n - 1, -1, -1 ):
    lvec[j] = ( i % 2 == 1 )
    i = ( i // 2 )

  return lvec

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  satisfy ( )
  timestamp ( )
