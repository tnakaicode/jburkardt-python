#! /usr/bin/env python
#
def i4_to_i4poly ( intval, base, degree_max ):

#*****************************************************************************80
#
## I4_TO_I4POLY converts an integer to an integer polynomial in a given base.
#
#  Example:
#
#    INTVAL  BASE  Degree     A (in reverse order!)
#
#         1     2       0     1
#         6     2       2     1  1  0
#        23     2       4     1  0  1  1  1
#        23     3       2     2  1  2
#        23     4       2     1  1  3
#        23     5       1     4  3
#        23     6       1     3  5
#        23    23       1     1  0
#        23    24       0    23
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer INTVAL, an integer to be converted.
#
#    Input, integer BASE, the base, which should be greater than 1.
#
#    Input, integer DEGREE_MAX, the maximum degree.
#
#    Output, integer A[0:DEGREE], contains the coefficients
#    of the polynomial expansion of INTVAL in base BASE.
#
#    Output, integer DEGREE, the degree of the polynomial.
#
  import numpy as np

  a = np.zeros ( degree_max + 1 )

  j = abs ( intval )

  degree = 0

  a[degree] = ( j % base )

  j = j - a[degree]
  j = ( j // base )

  while ( 0 < j ):

    degree = degree + 1

    a[degree] = ( j % base )

    j = j - a[degree]
    j = ( j // base )

  if ( intval < 0 ):
    for i in range ( 0, degree + 1 ):
      a[i] = - a[i]

  return a, degree

def i4_to_i4poly_test ( ):

#*****************************************************************************80
#
## I4_TO_I4POLY_TEST tests I4_TO_I4POLY
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 9

  base_test = np.array ( [ 2, 2, 2, 3, 4, 5, 6, 23, 24 ] )
  intval_test = np.array ( [ 1, 6, 23, 23, 23, 23, 23, 23, 23 ] )

  print ( '' )
  print ( 'I4_TO_I4POLY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_TO_I4POLY converts an integer to a polynomial' )
  print ( '  in a given base' )
  print ( '' )
  print ( '       I    BASE  DEGREE  Coefficients' )
  print ( '' )

  for test in range ( 0, test_num ):
    intval = intval_test[test]
    base = base_test[test]
    degree_max = 9
    a, degree = i4_to_i4poly ( intval, base, degree_max )
    print ( '  %6d  %6d  %6d' % ( intval, base, degree ) ),
    for i in range ( degree, -1, -1 ):
      print ( '  %6d' % ( a[i] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_TO_I4POLY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_to_i4poly_test ( )
  timestamp ( )

