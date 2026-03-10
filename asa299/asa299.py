#! /usr/bin/env python3
#
def asa299_test ( ):

#*****************************************************************************80
#
## asa299_test() tests asa299().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'asa299_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa299().' )

  asa299_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa299_test():' )
  print ( '  Normal end of execution.' )

  return

def asa299_test01 ( ):

#*****************************************************************************80
#
## asa299_test01() tests simplex_lattice_point_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  t = 4

  print ( '' )
  print ( 'asa299_test01():' )
  print ( '  simplex_lattice_point_next() generates lattice points' )
  print ( '  in the simplex' )
  print ( '    0 <= X' )
  print ( '    sum ( X[:] ) <= T' )
  print ( '  Here N = ', n )
  print ( '  and T =  ', t )
  print ( '' )
  print ( '     Index        X(0)      X(1)      X(2)      X(3)' )
  print ( '' )

  more = False
  x = np.zeros ( n )

  i = 0

  while ( True ):

    more, x = simplex_lattice_point_next ( n, t, more, x )

    print ( '  %8d  '% ( i ), end = '' )
    for j in range ( 0, n ):
      print ( '  %8d' % ( x[j] ), end = '' )
    print ( '' )

    if ( not more ):
      break

    i = i + 1

  return

def simplex_lattice_point_next ( n, t, more, x ):

#*****************************************************************************80
#
## simplex_lattice_point_next() generates lattice points in a simplex.
#
#  Discussion:
#
#    The simplex is defined by N-dimensional points X such that:
#
#        0 <= X(1:N)
#
#    and
#
#      sum ( X(1:N) ) <= T
#
#    where T is an integer.
#
#    Lattice points are points X which satisfy the simplex conditions and
#    for which all the components are integers.
#
#    This routine generates all the lattice points in a given simplex, one at
#    a time, in a reverse lexicographic order.
#
#    To use the routine, initialize by setting N and T to appropriate values,
#    and MORE to FALSE.  Initialize X to the empty vector, [].
#
#    Call the routine. On return, X will contain the first lattice point in
#    the simplex.  If MORE is TRUE, then the routine may be called again to
#    get the next point.  In fact, as long as the output value of MORE is
#    TRUE, there is at least one more lattice point that can be found by
#    making another call.  When MORE is returned as FALSE, then there are no
#    more lattice points the value of X returned at that time is the
#    "last" such point.
#
#    During the computation of a sequence of lattice points, the user should
#    not change the values of N, T, MORE or X.
#
#    The output for N = 3, T = 4 would be:
#
#       1    4  0  0
#       2    3  1  0
#       3    3  0  1
#       4    2  2  0
#       5    2  1  1
#       6    2  0  2
#       7    1  3  0
#       8    1  2  1
#       9    1  1  2
#      10    1  0  3
#      11    0  4  0
#      12    0  3  1
#      13    0  2  2
#      14    0  1  3
#      15    0  0  4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Scott Chasalow, Richard Brand,
#    Algorithm AS 299:
#    Generation of Simplex Lattice Points,
#    Applied Statistics,
#    Volume 44, Number 4, 1995, pages 534-545.
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms for Computers and Calculators,
#    Second Edition,
#    Academic Press, 1978,
#    ISBN: 0-12-519260-6,
#    LC: QA164.N54.
#
#  Input:
#
#    integer N, the spatial dimension.
#    N must be positive.
#
#    integer T, the characteristic of the simplex.
#    T must be nonnegative.
#
#    logical MORE, initialized to FALSE by the user to
#    begin a sequence of calculations.  Thereafter, the input value
#    should be the output value from the previous call.
#
#    integer X(N), should be initialized to [] on the very first
#    call.  Thereafter, the input value should be the output value
#    from the previous call.
#
#  Output:
#
#    logical MORE, returned by the routine as TRUE,
#    if there are more values of X that can be calculated, or FALSE
#    if the accompanying value of X is the last one for this sequence.
#
#    integer X(N), the next point in the sequence.
#
  import numpy as np

  if ( not more ):

    if ( n < 1 ):
      print ( '' )
      print ( 'simplex_lattice_point_next(): Fatal error!' )
      print ( '  N < 1.' )
      raise Exception ( 'simplex_lattice_point_next(): Fatal error!' )

    if ( t < 0 ):
      print ( '' )
      print ( 'simplex_lattice_point_next(): Fatal error!' )
      print ( '  T < 0.' )
      raise Exception ( 'simplex_lattice_point_next(): Fatal error!' )

    more = True
    j = 0
    x = np.zeros ( n, dtype = int )
    x[j] = t
#
#  The first point can actually also be the last!
#
    if ( n == 1 ):
      more = False

  else:
#
#  Search X(N-1 down to 1) for the first nonzero element.
#  If none, then terminate.  (This should not happen!)
#  Otherwise, set J to this index.
#  Decrement X(J) by 1.
#  Set X(J+1:N) to (T-X(1:J),0,0,...0).
#
    j = n - 1

    for i in range ( n-2, -1, -1 ):

      if ( 0 < x[i] ):
        j = i
        break

    if ( j == n - 1 ):
      print ( '' )
      print ( 'simplex_lattice_point_next(): Fatal error!' )
      print ( '  The input X vector is nonpositive in all entries' )
      print ( '  except possibly the last one.' )
      print ( '' )
      print ( '  Perhaps the user has miscalled the routine' )
      print ( '  or altered data between calls.' )
      print ( '' )
      print ( 'Abnormal termination.' )
      raise Exception ( 'simplex_lattice_point_next(): Fatal error!' )

    x[j] = x[j] - 1
    x[j+1] = t - np.sum ( x[0:j+1] )
    x[j+2:] = 0
#
#  Is this the last point?
#
    if ( x[n-1] == t ):
      more = False

  return more, x

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
  asa299_test ( )
  timestamp ( )

