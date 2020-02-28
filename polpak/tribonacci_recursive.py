#! /usr/bin/env python
#
def tribonacci_recursive ( n ):

#*****************************************************************************80
#
## TRIBONACCI_RECURSIVE computes the first N Tribonacci numbers.
#
#  Recursion:
#
#    F(1) = 1
#    F(2) = 1
#    F(3) = 1
#    F(N) = F(N-1) + F(N-2) + F(N-3)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the highest number to compute.
#
#    Output, integer F(N+1), the first N Tribonacci numbers.
#
  import numpy as np

  f = np.zeros ( n + 1 )

  f[0] = 0

  if ( 0 < n ):

    f[1] = 1

    if ( 1 < n ):

      f[2] = 1
      
      if ( 2 < n ):
      
        f[3] = 1

        for i in range ( 4, n + 1 ):
          f[i] = f[i-1] + f[i-2] + f[i-3]

  return f

def tribonacci_recursive_test ( ):

#*****************************************************************************80
#
## TRIBONACCI_RECURSIVE_TEST tests TRIBONACCI_RECURSIVE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_print import i4vec_print

  n = 20

  print ( '' )
  print ( 'TRIBONACCI_RECURSIVE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIBONACCI_RECURSIVE computes Tribonacci numbers recursively;' )

  f = tribonacci_recursive ( n )

  i4vec_print ( n + 1, f, '  The Tribonacci numbers:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIBONACCI_RECURSIVE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tribonacci_recursive_test ( )
  timestamp ( )
