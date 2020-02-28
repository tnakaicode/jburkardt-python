#! /usr/bin/env python
#
def rat_farey ( n, max_frac ):

#*****************************************************************************80
#
## RAT_FAREY computes the N-th row of the Farey fraction table.
#
#  Example:
#
#    N = 5
#
#    NUM_FRAC = 11
#    A =  0  1  1  1  2  1  3  2  3  4  1
#    B =  1  5  4  3  5  2  5  3  4  5  1
#
#  Discussion:
#
#    In this form of the Farey fraction table, fractions in row N lie between
#    0 and 1, are in lowest terms, and have a denominator that is no greater
#    than N.  Row N is computed directly, and does not require the computation
#    of previous rows.
#
#    The data satisfy the relationship:
#
#      A(K+1) * B(K) - A(K) * B(K+1) = 1
#
#    The number of items in the N-th row is roughly N^2 / PI^2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms,
#    Addison Wesley, 1968, page 157.
#
#  Parameters:
#
#    Input, integer N, the desired row number.  N must be positive.
#
#    Input, integer MAX_FRAC, the maximum number of fractions to compute.
#
#    Output, integer A(NUM_FRAC), B(NUM_FRAC), contains the
#    numerators and denominators of the N-th row of the Farey fraction table.
#
#    Output, integer NUM_FRAC, the number of fractions computed.
#
  import numpy as np

  a = np.zeros ( max_frac )
  b = np.zeros ( max_frac )

  if ( max_frac <= 0 ):
    num_frac = 0
    return a, b, num_frac

  if ( n <= 0 ):
    num_frac = 0
    return a, b, num_frac

  k = 0
  a[k] = 0
  b[k] = 1

  if ( max_frac <= k + 1 ):
    num_frac = k + 1
    return a, b, num_frac

  k = 1
  a[k] = 1
  b[k] = n

  while ( k + 1 < max_frac ):

    if ( a[k] == 1 and b[k] == 1 ):
      break

    k = k + 1
    c = ( ( b[k-2] + n ) // b[k-1] )
    a[k] = c * a[k-1] - a[k-2]
    b[k] = c * b[k-1] - b[k-2]

  num_frac = k + 1

  return a, b, num_frac

def rat_farey_test ( ):

#*****************************************************************************80
#
## RAT_FAREY_TEST tests RAT_FAREY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  max_frac = 20

  print ( '' )
  print ( 'RAT_FAREY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RAT_FAREY computes a row of the Farey fraction table.' )

  for n in range ( 1, 8 ):

    a, b, num_frac = rat_farey ( n, max_frac )
 
    print ( '' )
    print ( '  Row %d' % ( n ) )
    print ( '  Number of fractions: %d' % ( num_frac ) )

    for i in range ( 0, num_frac ):
      print ( '  %d/%d' % ( a[i], b[i] ) ),
      if ( ( ( i + 1 ) % 10 == 0 ) or i == num_frac - 1 ):
        print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'RAT_FAREY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rat_farey_test ( )
  timestamp ( )

