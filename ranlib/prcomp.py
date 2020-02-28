#! /usr/bin/env python
#
def prcomp ( maxobs, p, mean, xcovar, answer ):

#*****************************************************************************80
#
## PRCOMP prints covariance information.
#
#  Discussion:
#
#    I didn't feel up to creating a test problem for this function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, integer MAXOBS, the number of observations.
#
#    Input, integer P, the number of variables.
#
#    Input, real MEAN(P), the mean for each column.
#
#    Input, real XCOVAR(P,P), the variance/covariance matrix.
#
#    Input, real ANSWER(MAXOBS,P), the observed values.
#
  import numpy as np
  from r4vec_covariance import r4vec_covariance
  from stats import stats

  print ( '' )
  print ( 'PRCOMP:' )
  print ( '  Print and compare covariance information' )
  print ( '' )

  rmean = np.zeros ( p )
  rvar = np.zeros ( p )

  for j in range ( 0, p ):
    rmean, rvar, rmin, rmax = stats ( answer[0:maxobs,j], maxobs )
    print ( '  Variable Number %d' % ( j ) )
    print ( '  Mean     %12g  Generated %12g' % ( mean[j], rmean ) )
    print ( '  Variance %12g  Generated 512g' % ( xcovar[j,j], rvar ) )

  print ( '' )
  print ( '  Covariances:' )
  print ( '' )

  for i in range ( 0, p ):
    for j in range ( 0, i ):
      print ( '  I = %d, J = %d' % ( i, j ) )
      rcovar[i,j] = r4vec_covariance ( maxobs, answer[0:maxobs,i], answer[0:maxobs,j] )
      print ( '  Covariance %12g  Generated %12g' % ( xcovar[i,j], rcovar[i,j] ) )

  return

def prcomp_test ( ):

#*****************************************************************************80
#
## PRCOMP_TEST tests PRCOMP.
#
#  Discussion:
#
#    I didn't feel up to creating a test problem for this function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    Python version by John Burkardt.
#
  print ( '' )
  print ( 'PRCOMP_TEST' )
  print ( '  PRCOMP prints and compares covariance information.' )
  print ( '  Warning! - No test code has been provided.' )
  print ( '' )
  print ( 'PRCOMP_TEST:' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  prcomp_test ( )
  timestamp ( )

