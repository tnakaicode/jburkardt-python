#! /usr/bin/env python3
#
def satisfy_brute_test ( ):

#*****************************************************************************80
#
## satisfy_brute_test() tests satisfy_brute().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'satisfy_brute_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test satisfy_brute().' )

  satisfy_brute_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'satisfy_brute_test():' )
  print ( '  Normal end of execution.' )

  return

def satisfy_brute_test01 ( ):

#*****************************************************************************80
#
## satisfy_brute_test01() tests satisfy_brute() on a particular formula.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'satisfy_brute_test01():' )
  print ( '  satisfy_brute() seeks values of logical' )
  print ( '  variables that make a given formula true' )

  n = 23

  satisfy_brute ( n, formula_01 )

  return

def satisfy_brute ( n, formula ):

#*****************************************************************************80
#
## satisfy_brute() solves the formula satisfaction problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 October 2022
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
#  Input:
#
#    integer n: the number of variables in the formula.
#
#    integer formula ( integer bvec[] ): a function which evaluates the formula.
#
  print ( '' )
  print ( 'satisfy_brute():' )
  print ( '  We have a logical function of N logical arguments.' )
  print ( '  We do an exhaustive search of all 2^N possibilities,' )
  print ( '  seeking those inputs that make the function TRUE.' )
#
#  Compute the number of binary vectors to check.
#
  ihi = 2 ** n

  print ( '' )
  print ( '  The number of logical variables is N = ', n )
  print ( '  The number of input vectors to check is ', ihi )
  print ( '' )
  print ( '   #       Index    ---------Input Values------------------------' )
  print ( '' )
#
#  Check every possible input vector.
#
  solution_num = 0

  for i in range ( 0, ihi ):

    lvec = i4_to_lvec ( i, n )

    value = formula ( lvec )

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
  print ( '  Number of solutions found was ', solution_num )

  return

def formula_01 ( lvec ):

#*****************************************************************************80
#
## formula_01() returns the value of a circuit for a given input set.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 October 2022
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
#  Input:
#
#    bool LVEC(N), the binary inputs.
#
#  Output:
#
#    bool value: the output of the circuit.
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
## i4_to_lvec() makes a boolean vector from an integer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, a nonnegative integer to be represented.
#
#    integer N, the dimension of the vector.
#
#  Output:
#
#    integer LVEC(N), the logical vector.
#
  import numpy as np

  lvec = np.zeros ( n, dtype = bool )

  for j in range ( n - 1, -1, -1 ):
    lvec[j] = ( i % 2 == 1 )
    i = ( i // 2 )

  return lvec

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
#    06 April 2013
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
  satisfy_brute_test ( )
  timestamp ( )
 
