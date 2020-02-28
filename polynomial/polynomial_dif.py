#! /usr/bin/env python3
#
def polynomial_dif ( m, o1, c1, e1, dif ):

#*****************************************************************************80
#
## POLYNOMIAL_DIF differentiates a polynomial.
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
#    Input, integer M, the spatial dimension.
#
#    Input, integer O1, the "order" of polynomial 1.
#
#    Input, real C1[O1], the coefficients of polynomial 1.
#
#    Input, integer E1[O1], the indices of the exponents of 
#    polynomial 1.
#
#    Input, integer DIF[M], indicates the number of 
#    differentiations in each component.
#
#    Output, integer O, the "order" of the polynomial derivative.
#
#    Output, real C[O], the coefficients of the polynomial derivative.
#
#    Output, integer E[O], the indices of the exponents of 
#    the polynomial derivative.
#
  from i4_fall import i4_fall
  from mono_rank_grlex import mono_rank_grlex
  from mono_unrank_grlex import mono_unrank_grlex
  from polynomial_compress import polynomial_compress
  from polynomial_sort import polynomial_sort
  import numpy as np

  o = o1
  c = np.zeros ( o, dtype = np.float64 )
  for i in range ( 0, o ):
    c[i] = c1[i]
  e = np.zeros ( o, dtype = np.int32 )

  for j in range ( 0, o1 ):
    f1 = mono_unrank_grlex ( m, e1[j] )
    for i in range ( 0, m ):
      c[j] = c[j] * i4_fall ( f1[i], dif[i] )
      f1[i] = max ( f1[i] - dif[i], 0 )
    e[j] = mono_rank_grlex ( m, f1 )

  c, e = polynomial_sort ( o, c, e )
  o, c, e = polynomial_compress ( o, c, e )

  return o, c, e

def polynomial_dif_test ( ):

#*****************************************************************************80
#
## POLYNOMIAL_DIF_TEST tests POLYNOMIAL_DIF.
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

  m = 2
  o1 = 4
  c1 = np.array ( [ 2.0, 3.0, 4.0, 5.0 ], dtype = np.float64 )
  e1 = np.array ( [ 1, 10, 12, 32 ], dtype = np.int32 )
  dif = np.array ( [ 2, 1 ], dtype = np.int32 )

  print ( '' )
  print ( 'POLYNOMIAL_DIF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYNOMIAL_DIF differentiates a polynomial.' )

  print ( '' )
  title = '  P(X):'
  polynomial_print ( m, o1, c1, e1, title )

  o, c, e = polynomial_dif ( m, o1, c1, e1, dif )

  print ( '' )
  title = '  d3 P(X) dx1 dx1 dx2 ='
  polynomial_print ( m, o, c, e, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYNOMIAL_DIF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polynomial_dif_test ( )
  timestamp ( )
 
