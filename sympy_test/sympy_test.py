#! /usr/bin/env python3
#
def sympy_test ( ):

#*****************************************************************************80
#
## sympy_test() tests sympy().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
  from sympy_derivative import sympy_derivative
  from sympy_evaluate import sympy_evaluate
  from sympy_integral import sympy_integral
  from sympy_limit import sympy_limit
  from sympy_linalg import sympy_linalg
  from sympy_ode import sympy_ode
  from sympy_plot import sympy_plot
  from sympy_polynomial import sympy_polynomial
  from sympy_sample import sympy_sample
  from sympy_series import sympy_series

  import numpy as np
  import platform
  import sympy

  print ( '' )
  print ( 'sympy_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  sympy version:  ' + sympy.__version__ )
  print ( '  sympy() is a symbolic mathematics package.' )
  print ( '' )

  sympy_derivative ( )
  sympy_evaluate ( )
  sympy_integral ( )
  sympy_limit ( )
  sympy_linalg ( )
  sympy_ode ( )
  sympy_plot ( )
  sympy_polynomial ( )
  sympy_sample ( )
  sympy_series ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sympy_test():' )
  print ( '  Normal end of execution.' )
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
  sympy_test ( )
  timestamp ( )

