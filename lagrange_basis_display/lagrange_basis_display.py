#! /usr/bin/env python3
#
def lagrange_basis_display_test ( ):

#*****************************************************************************80
#
## lagrange_basis_display_test() tests lagrange_basis_display().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'lagrange_basis_display_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test lagrange_basis_display().' )
#
#  Plot the 11 standard "basis vectors".
#
  a = 0.0
  b = 1.0
  m = 10

  standard_basis_display ( a, b, m )
#
#  Plot the 11 Lagrange "basis vectors" for evenly spaced nodes.
#
  a = 0.0
  b = 1.0
  m = 10
  xd = np.linspace ( a, b, m + 1 )

  lagrange_basis_display ( a, b, m, xd, 0 )
#
#  Plot the 11 Lagrange "basis vectors" for Chebyshev-spaced nodes.
#
  a = -1.0
  b = 1.0
  m = 10
  xd = r8vec_cheby1space ( m + 1, -1.0, +1.0 ) 

  lagrange_basis_display ( a, b, m, xd, 1 )
#
#  Terminate.
#
  print ( '' )
  print ( 'lagrange_basis_display_test():' )
  print ( '  Normal end of execution.' )

  return

def r8vec_cheby1space ( n, a, b ):

#*****************************************************************************80
#
## r8vec_cheby1space() creates a vector of Type 1 Chebyshev values in [A,B].
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the first and last entries.
#
#  Output:
#
#    real X(N), a vector of Type 1 Chebyshev spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):

      theta = float ( n - i - 1 ) * np.pi / float ( n - 1 )

      c = np.cos ( theta )

      if ( ( n % 2 ) == 1 ):
        if ( 2 * i + 1 == n ):
          c = 0.0

      x[i] = ( ( 1.0 - c ) * a  \
             + ( 1.0 + c ) * b ) \
             /   2.0
 
  return x

def lagrange_basis_display ( a, b, m, xd, spacing ):

#*****************************************************************************80
#
## lagrange_basis_display() displays the Lagrange interpolation basis "vectors".
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 August 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the limits of the interval.  Typically 0 and 1.
#
#    integer M, the maximum polynomial degree.
#    0 <= M.
#
#    real XD(M+1), the interpolation nodes.
#
  import matplotlib.pyplot as plt
  import numpy as np

  yd = np.ones_like ( xd )

  ni = 501
  xi = np.linspace ( a, b, ni )

  plt.clf ( )

  for i in range ( 0, m + 1 ):

    yi = np.ones ( ni )

    for j in range ( 0, m + 1 ):

      if ( j != i ):
        yi = yi * ( xi - xd[j] ) / ( xd[i] - xd[j] )

    plt.plot ( xi, yi, linewidth = 2 )    

  plt.plot ( xd, yd, 'r.', markersize = 30 )  

  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<--B(IX)--->' )
  if ( spacing == 0 ):
    plt.title ( 'Lagrange basis, even spacing' )
    filename = 'lagrange_even.png'
  else:
    plt.title ( 'Lagrange basis, Chebyshev spacing' )
    filename = 'lagrange_cheby.png'

  plt.savefig ( filename )

  print ( '' )
  print ( '  Graphics saved as "' + filename + '".' )

  return

def standard_basis_display ( a, b, m ):

#*****************************************************************************80
#
## standard_basis_display() displays the standard monomial basis "vectors".
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 August 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the limits of the interval.  Typically 0 and 1.
#
#    integer M, the maximum polynomial degree.
#    0 <= M.
#
  import matplotlib.pyplot as plt
  import numpy as np

  x = np.linspace ( a, b, 501 )

  plt.clf ( )

  for i in range ( 0, m + 1 ):
    y = x**i
    plt.plot ( x, y, linewidth = 2 )    

  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<--B(IX)--->' )
  plt.title ( 'Monomial basis functions 0 through ' + str ( m ) )

  filename = 'standard_even.png'

  plt.savefig ( filename )

  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )

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
  lagrange_basis_display_test ( )
  timestamp ( )

