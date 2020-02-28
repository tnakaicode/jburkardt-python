#! /usr/bin/env python
#
def rat_farey2 ( n, a, b ):

#*****************************************************************************80
#
## RAT_FAREY2 computes the next row of the Farey fraction table.
#
#  Example:
#
#    Input:
#
#      N = 3
#      A =  0  1  1  2  1
#      B =  1  3  2  3  1
#
#    Output:
#
#      A =  0  1  1  2  1  3  2  3  1
#      B =  1  4  3  5  2  5  3  4  1
#
#  Discussion:
#
#    In this form of the Farey fraction table, fractions in row N lie between
#    0 and 1, and are in lowest terms.  For every adjacent pair of input
#    fractions, A1/B1 and A2/B2, the mediant (A1+A2)/(B1+B2) is computed
#    and inserted between them.
#
#    The number of items in the N-th row is 1+2^(N-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the input row number.  N must be nonnegative.
#    If N is zero, then the input values A and B are ignored, and the entries of
#    row 1 are computed directly.
#
#    Input, integer A(1+2^(N-1)), B(1+2^(N-1)),the entries of row N.
#
#    Output, integer A2(1+2^N), B2(1+2^N), the entries of row N+1.
#
  import numpy as np

  a2 = np.zeros ( 1 + 2 ** n )
  b2 = np.zeros ( 1 + 2 ** n )

  if ( n == 0 ):

    a2[0] = 0
    a2[1] = 1
    b2[0] = 1
    b2[1] = 1

  else:
#
#  Shift the current data.
#
    for i in range ( 2 ** ( n - 1 ), -1, -1 ):
      a2[2*i] = a[i]
      b2[2*i] = b[i]
#
#  Compute the mediants.
#
    for i in range ( 1, 2 ** n, 2 ):
      a2[i] = a2[i-1] + a2[i+1]
      b2[i] = b2[i-1] + b2[i+1]

  return a2, b2

def rat_farey2_test ( ):

#*****************************************************************************80
#
## RAT_FAREY2_TEST tests RAT_FAREY2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  max_n = 4
  
  print ( '' )
  print ( 'RAT_FAREY2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RAT_FAREY2 computes a row of the Farey fraction table.' )

  n = 0
  a = np.zeros ( n )
  b = np.zeros ( n )
  
  for n in range ( 0, 5 ):

    a, b = rat_farey2 ( n, a, b )
    num_frac = 2 ** n + 1

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
  print ( 'RAT_FAREY2_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rat_farey2_test ( )
  timestamp ( )

