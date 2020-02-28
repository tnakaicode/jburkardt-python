#! /usr/bin/env python
#
def r8poly_power ( na, a, p ):

#*****************************************************************************80
#
## R8POLY_POWER computes a positive integer power of a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1)*x + ... + a(n-1)*x^(n-1) + a(n)*x^(n)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NA, the dimension of A.
#
#    Input, real A(1:NA+1), the polynomial to be raised to the power.
#
#    Input, integer P, the nonnegative power to which A is raised.
#
#    Output, real B(P*NA+1), the power of the polynomial.
#
  import numpy as np
#
#  Zero out B.
#
  b = np.zeros ( p * na + 1 )
#
#  Search for the first nonzero element in A.
#
  nonzer = -1

  for i in range ( 0, na + 1 ):
    if ( a[i] != 0.0 ):
      nonzer = i
      break

  if ( nonzer == -1 ):
    return b

  b[0] = a[nonzer] ** p

  for i in range ( 1, p*(na-nonzer)+1 ):

    if ( i + nonzer <= na ):
      b[i] = i * p * b[0] * a[i+nonzer]
    else:
      b[i] = 0.0

    for j in range ( 1, i ):

      if ( j+nonzer <= na ):
        b[i] = b[i] - ( i - j ) * a[j+nonzer] * b[i-j]

      if ( i-j+nonzer <= na ):
        b[i] = b[i] + ( i - j ) * p * b[j] * a[i-j+nonzer]

    b[i] = b[i] / ( i * a[nonzer] )
#
#  Shift B up.
#
  for i in range ( p*nonzer, p*na + 1 ):
    b[i] = b[i-p*nonzer]

  for i in range ( 0, p * nonzer ):
    b[i] = 0.0

  return b

def r8poly_power_test ( ):

#*****************************************************************************80
#
## R8POLY_POWER_TEST tests R8POLY_POWER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8poly_print import r8poly_print

  print ( '' )
  print ( 'R8POLY_POWER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_POWER takes a polynomial to a power.' )
#
#  Cube (2-X).  Answer is 8-12*X+6*X^2-X^3.
#
  na = 1
  a = np.array ( [ 2.0, -1.0 ] )
  p = 3

  r8poly_print ( na, a, '  The polynomial A:' )
 
  b = r8poly_power ( na, a, p )
 
  r8poly_print ( p*na, b, '  Raised to the power 3:' )
#
#  Square X+X^2
#
  na = 2
  a = np.array ( [ 0.0, 1.0, 1.0 ] )
  p = 2

  r8poly_print ( na, a, '  The polynomial A:' )
 
  b = r8poly_power ( na, a, p )
 
  r8poly_print ( p*na, b, '  Raised to the power 2:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_POWER_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_power_test ( )
  timestamp ( )
