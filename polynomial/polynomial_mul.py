#! /usr/bin/env python3
#
def polynomial_mul ( m, o1, c1, e1, o2, c2, e2 ):

#*****************************************************************************80
#
## POLYNOMIAL_MUL multiplies two polynomials.
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
#    Input, integer O2, the "order" of polynomial 2.
#
#    Input, real C2[O2], the coefficients of polynomial 2.
#
#    Input, integer E2[O2], the indices of the exponents of 
#    polynomial 2.
#
#    Output, integer O, the "order" of the polynomial product.
#
#    Output, real C[O], the coefficients of the polynomial product.
#
#    Output, integer E[O], the indices of the exponents of 
#    the polynomial product.
#
  from i4vec_concatenate import i4vec_concatenate
  from mono_rank_grlex import mono_rank_grlex
  from mono_unrank_grlex import mono_unrank_grlex
  from polynomial_compress import polynomial_compress
  from polynomial_sort import polynomial_sort
  from r8vec_concatenate import r8vec_concatenate
  import numpy as np

  f = np.zeros ( m, dtype = np.int32 )
  c = np.zeros ( o1 * o2, dtype = np.float32 )
  e = np.zeros ( o1 * o2, dtype = np.int32 )

  o = 0
  for j in range ( 0, o2 ):
    for i in range ( 0, o1 ):
      c[o] = c1[i] * c2[j]
      f1 = mono_unrank_grlex ( m, e1[i] )
      f2 = mono_unrank_grlex ( m, e2[j] )
      for k in range ( 0, m ):
        f[k] = f1[k] + f2[k]
      e[o] = mono_rank_grlex ( m, f )
      o = o + 1

  c, e = polynomial_sort ( o, c, e )
  o, c, e = polynomial_compress ( o, c, e )

  return o, c, e

def polynomial_mul_test ( ):

#*****************************************************************************80
#
## POLYNOMIAL_MUL_TEST tests POLYNOMIAL_MUL.
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
  o1 = 4
  c1 = np.array ( [ 2.0, 3.0, 4.0, 5.0 ], dtype = np.float64 )
  e1 = np.array ( [ 1, 3, 4, 6 ], dtype = np.int32 )

  o2 = 2
  c2 = np.array ( [ 6.0, 7.0 ], dtype = np.float64 )
  e2 = np.array ( [ 2, 5 ], dtype = np.int32 )

  print ( '' )
  print ( 'POLYNOMIAL_MUL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYNOMIAL_MUL multiplies two polynomials' )

  print ( '' )
  title = '  P1(X):'
  polynomial_print ( m, o1, c1, e1, title )

  print ( '' )
  title = '  P2(X):'
  polynomial_print ( m, o2, c2, e2, title )

  o, c, e = polynomial_mul ( m, o1, c1, e1, o2, c2, e2 )

  print ( '' )
  title = '  P(X) = P1(X) * P2(X):'
  polynomial_print ( m, o, c, e, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYNOMIAL_MUL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polynomial_mul_test ( )
  timestamp ( )
 
