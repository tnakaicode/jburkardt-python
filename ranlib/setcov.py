#! /usr/bin/env python
#
def setcov ( p, var, corr ):

#*****************************************************************************80
#
## SETCOV sets a covariance matrix from variance and common correlation.
#
#  Discussion:
#
#    This procedure sets the covariance matrix from the variance and
#    common correlation.
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
#    Input, integer P, the number of variables.
#
#    Input, real VAR(P), the variances.
#
#    Input, real CORR, the common correlaton.
#
#    Output, real COVAR(P,P), the covariance matrix.
#
  import numpy as np
  from sys import exit

  if ( any ( var[0:p] < 0.0 ) ):
    print ( '' )
    print ( 'SETCOV - Fatal error!' )
    print ( '  No variance should be negative.' )
    exit ( 'SETCOV - Fatal error!' )

  covar = np.zeros ( [ p, p ] )

  for i in range ( 0, p ):
    for  j in range ( 0, p ):
      if ( i == j ):
        covar[i,j] = var[i]
      else:
        covar[i,j] = corr * np.sqrt ( var[i] * var[j] )

  return covar

def setcov_test ( ):

#*****************************************************************************80
#
## SETCOV_TEST tests SETCOV.
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
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'SETCOV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SETCOV aets a covariance matrix.' )

  p = 3
  var = np.array ( [ 0.5, 0.2, 0.9 ] )
  corr = 0.25

  print ( '' )
  print ( '  Number of variables P = %d' % ( p ) )
  print ( '  Common correlation = %g' % ( corr ) )
  print ( '  Variances:' )
  print ( '    ' ),
  for i in range ( 0, p ):
    print ( '%g' % ( var[i] ) ),
  print ( '' )

  cov = setcov ( p, var, corr )

  print ( '' )
  print ( '  Covariance matrix:' )
  print ( '' )
  for i in range ( 0, p ):
    print ( '    ' ),
    for j in range ( 0, p ):
      print ( '%8f' % ( cov[i,j] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SETCOV_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  setcov_test ( )
  timestamp ( )

