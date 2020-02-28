#! /usr/bin/env python
#
def lagrange_basis_1d ( nd, xd, ni, xi ):

#*****************************************************************************80
#
## LAGRANGE_BASIS_1D evaluates a 1D Lagrange basis.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ND, the number of data points.
#
#    Input, real XD(ND,1), the interpolation nodes.
#
#    Input, integer NI, the number of evaluation points.
#
#    Input, real XI(NI,1), the evaluation points.
#
#    Output, real LB(NI,ND), the value, at the I-th point XI, of the
#    Jth basis function.
#
  import numpy as np

  lb = np.zeros ( [ ni, nd ] )
  
  for i in range ( 0, ni ):
    for j in range ( 0, nd ):
      lb[i,j] = 1.0
      for k in range ( 0, nd ):
        if ( k != j ):
          lb[i,j] = lb[i,j] * ( xi[i] - xd[k]  ) / ( xd[j] - xd[k]  )

  return lb

def lagrange_basis_1d_test ( ):

#*****************************************************************************80
#
## LAGRANGE_BASIS_1D_TEST tests LAGRANGE_BASIS_1D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  nd = 4
  ni = 21

  xd = np.array ( [ 0.0, 2.0, 5.0, 10.0 ] )
 
  print ( '' )
  print ( 'LAGRANGE_BASIS_1D_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LAGRANGE_BASIS_1D evaluates the Lagrange 1D basis' )
  print ( '  functions.' )

  x_min = 0.0
  x_max = 10.0
  xi = np.linspace ( x_min, x_max, ni )

  lb = lagrange_basis_1d ( nd, xd, ni, xi )

  r8mat_print ( ni, nd, lb, '  The Lagrange basis functions:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'LAGRANGE_BASIS_1D_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lagrange_basis_1d_test ( )
  timestamp ( )

