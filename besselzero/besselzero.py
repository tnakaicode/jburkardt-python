#! /usr/bin/env python3
#
def besselzero_test ( ):

#*****************************************************************************80
#
## besselzero_test() tests besselzero().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  import scipy as sp

  print ( '' )
  print ( 'besselzero_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  scipy version:  ' + sp.version.version )
  print ( '  Test besselzero()' )

  besselzero_j_print ( )
  besselzero_y_print ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'besselzero_test():' )
  print ( '  Normal end of execution.' )

  return

def besselzero_j_print ( ):

#*****************************************************************************80
#
## besselzero_j_print() tests jn_zeros() for the Bessel J function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2025
#
#  Author:
#
#    John Burkardt
#
  from scipy.special import jn_zeros

  print ( '' )
  print ( 'besselzero_j_print():' )
  print ( '  Print zeros of Bessel j function.' )

  n = 0
  nt = 10
  z0 = jn_zeros ( n, nt )

  n = 1
  nt = 10
  z1 = jn_zeros ( n, nt )

  print ( '' )
  print ( '    i    J0(root i)  J1(root i)' )
  print ( '' )
  for i in range ( 0, nt ):
    print ( '  %2d  %14.6g  %14.6g' % ( i, z0[i], z1[i] ) )

  return

def besselzero_y_print ( ):

#*****************************************************************************80
#
## besselzero_y_print() tests besselzero() for the Bessel Y function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2025
#
#  Author:
#
#    John Burkardt
#
  from scipy.special import yn_zeros

  print ( '' )
  print ( 'besselzero_y_print():' )
  print ( '  Print zeros of Bessel y function.' )

  n = 0
  nt = 10
  z0 = yn_zeros ( n, nt )

  n = 1
  nt = 10
  z1 = yn_zeros ( n, nt )

  print ( '' )
  print ( '    i    Y0(root i)  Y1(root i)' )
  print ( '' )
  for i in range ( 0, nt ):
    print ( '  %2d  %14.6g  %14.6g' % ( i, z0[i], z1[i] ) )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  besselzero_test ( )
  timestamp ( )

