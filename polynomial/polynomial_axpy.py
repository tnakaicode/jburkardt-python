#! /usr/bin/env python3
#
def polynomial_axpy ( s, o1, c1, e1, o2, c2, e2 ):

#*****************************************************************************80
#
## POLYNOMIAL_AXPY adds a multiple of one polynomial to another.
#
#  Discussion:
#
#    P(X) = S * P1(X) + P2(X)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real S, the multiplier for the first polynomial.
#
#    Input, integer O1, the "order" of polynomial 1.
#
#    Input, real C1[O1], the coefficients of polynomial 1.
#
#    Input, integer E1[O1], the indices of the exponents of 
#    polynomial 1.
#
#    Input, integer O2, the "order" of polynomial 2.
#
#    Input, real C2[O2], the coefficients of polynomial 2.
#
#    Input, integer E2[O2], the indices of the exponents of 
#    polynomial 2.
#
#    Output, integer O, the "order" of the polynomial sum.
#
#    Output, real C[O], the coefficients of the polynomial sum.
#
#    Output, integer E[O], the indices of the exponents of 
#    the polynomial sum.
#
  from i4vec_concatenate import i4vec_concatenate
  from polynomial_compress import polynomial_compress
  from polynomial_sort import polynomial_sort
  from r8vec_concatenate import r8vec_concatenate
  import numpy as np

  o = o1 + o2

  sc1 = np.zeros ( o1, dtype = np.float64 )
  for i in range ( 0, o1 ):
    sc1[i] = s * c1[i]

  c = r8vec_concatenate ( o1, sc1, o2, c2 )
  e = i4vec_concatenate ( o1, e1, o2, e2 )

  c, e = polynomial_sort ( o, c, e )
  o, c, e = polynomial_compress ( o, c, e )

  return o, c, e

def polynomial_axpy_test ( ):

#*****************************************************************************80
#
## POLYNOMIAL_AXPY_TEST tests POLYNOMIAL_AXPY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from polynomial_print import polynomial_print

  m = 3
  o1 = 6
  c1 = np.array ( [ 7.0, - 5.0, 9.0, 11.0, 0.0, - 13.0 ], dtype = np.float64 )
  e1 = np.array ( [ 1, 2, 4, 5, 12, 33 ], dtype = np.int32 )

  o2 = 5
  c2 = np.array ( [ 2.0, 3.0, -8.0, 4.0, 9.0 ], dtype = np.float64 )
  e2 = np.array ( [ 1, 3, 4, 30, 33 ], dtype = np.int32 )

  s = 10.0

  print ( '' )
  print ( 'POLYNOMIAL_AXPY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYNOMIAL_AXPY adds a multiple of one polynomial to another.' )

  print ( '' )
  title = '  P1(X):'
  polynomial_print ( m, o1, c1, e1, title )

  print ( '' )
  title = '  P2(X):'
  polynomial_print ( m, o2, c2, e2, title )

  print ( '' )
  print ( '  Use the multiplier S = %g' % ( s ) )
  o, c, e = polynomial_axpy ( s, o1, c1, e1, o2, c2, e2 )

  print ( '' )
  title = '  P(X) = S * P1(X) + P2(X):'
  polynomial_print ( m, o, c, e, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYNOMIAL_AXPY_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polynomial_axpy_test ( )
  timestamp ( )
 