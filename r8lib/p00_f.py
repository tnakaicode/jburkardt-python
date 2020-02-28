#! /usr/bin/env python
#
def p00_f ( prob, n, x ):

#*****************************************************************************80
#
## P00_F evaluates the function for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the number of the desired test problem.
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  from sys import exit

  if ( prob == 1 ):
    value = p01_f ( n, x )
  elif ( prob == 2 ):
    value = p02_f ( n, x )
  elif ( prob == 3 ):
    value = p03_f ( n, x )
  elif ( prob == 4 ):
    value = p04_f ( n, x )
  elif ( prob == 5 ):
    value = p05_f ( n, x )
  elif ( prob == 6 ):
    value = p06_f ( n, x )
  elif ( prob == 7 ):
    value = p07_f ( n, x )
  elif ( prob == 8 ):
    value = p08_f ( n, x )
  else:
    print ( '' )
    print ( 'P00_F - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    exit ( 'P00_F - Fatal error!' )

  return value

def p01_f ( n, x ):

#*****************************************************************************80
#
## P01_F evaluates the function for problem p01.
#
#  Discussion:
#
#    Step function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = 2.0 * np.ones ( n )

  i = ( x <= 1.0 / 3.0 )
  j = ( 4.0 / 5.0 <= x )

  value[i] = -1.0
  value[j] = +1.0

  return value

def p02_f ( n, x ):

#*****************************************************************************80
#
## P02_F evaluates the function for problem p02.
#
#  Discussion:
#
#    Nondifferentiable function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = np.zeros ( n )

  i = ( x <= 1.0 / 3.0 )
  j = ( 1.0 / 3.0 < x )

  value[i] = 1.0 - 3.0 * x[i]
  value[j] = 6.0 * x[j] - 2.0

  return value

def p03_f ( n, x ):

#*****************************************************************************80
#
## P03_F evaluates the function for problem p03.
#
#  Discussion:
#
#    Step function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = x * ( 10.0 * x - 1.0 ) * ( 5.0 * x - 2.0 ) * ( 5.0 * x - 2.0 ) \
    * ( 4 * x - 3.4 ) * ( x - 1.0 )

  return value

def p04_f ( n, x ):

#*****************************************************************************80
#
## P04_F evaluates the function for problem p04.
#
#  Discussion:
#
#    Step function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = np.arctan ( 40.0 * x - 15.0 )

  return value

def p05_f ( n, x ):

#*****************************************************************************80
#
## P05_F evaluates the function for problem p05.
#
#  Discussion:
#
#    Step function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value =       np.cos (  7.0 * x ) \
        + 5.0 * np.cos ( 11.2 * x ) \
        - 2.0 * np.cos ( 14.0 * x ) \
        + 5.0 * np.cos ( 31.5 * x ) \
        + 7.0 * np.cos ( 63.0 * x )

  return value

def p06_f ( n, x ):

#*****************************************************************************80
#
## P06_F evaluates the function for problem p06.
#
#  Discussion:
#
#    f(x) = exp ( - (4 * x - 1)^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Genz,
#    A Package for Testing Multiple Integration Subroutines,
#    in Numerical Integration: Recent Developments, Software
#    and Applications,
#    edited by Patrick Keast and Graeme Fairweather,
#    D Reidel, 1987, pages 337-340,
#    LC: QA299.3.N38.
#
#  Parameters:
#
#    Input, integer N, the number of points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = np.exp ( - ( 4.0 * x - 1.0 ) ** 2 )

  return value

def p07_f ( n, x ):

#*****************************************************************************80
#
## P07_F evaluates the function for problem p07.
#
#  Discussion:
#
#    f(x) = exp ( 4 * x ) if x <= 1/2
#           0                  otherwise
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Genz,
#    A Package for Testing Multiple Integration Subroutines,
#    in Numerical Integration: Recent Developments, Software
#    and Applications,
#    edited by Patrick Keast and Graeme Fairweather,
#    D Reidel, 1987, pages 337-340,
#    LC: QA299.3.N38.
#
#  Parameters:
#
#    Input, integer N, the number of points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = np.zeros ( n )

  i = ( x < 0.5 )

  value[i] = np.exp ( 4.0 * x[i] )

  return value

def p08_f ( n, x ):

#*****************************************************************************80
#
## P08_F evaluates the function for problem p08.
#
#  Discussion:
#
#    This is a famous example, due to Runge.  If equally spaced
#    abscissas are used, the sequence of interpolating polynomials Pn(X)
#    diverges, in the sense that the max norm of the difference
#    between Pn(X) and F(X) becomes arbitrarily large as N increases.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  value = 1.0 / ( ( 10.0 * ( x - 0.5 ) ) ** 2 + 1.0 )

  return value

def p00_f_test ( ):

#*****************************************************************************80
#
## P00_F_TEST tests P00_F.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from p00_prob_num import p00_prob_num
  from r8vec2_print import r8vec2_print

  print ( '' )
  print ( 'P00_F_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_F evaluates any function at N points X.' )

  prob_num = p00_prob_num ( )

  n = 11
  a = 0.0
  b = 1.0
  x = np.linspace ( a, b, n )

  print ( '' )

  for prob in range ( 1, prob_num + 1 ):

    y = p00_f ( prob, n, x )
    title = 'X, Y for problem ' + str ( prob )
    r8vec2_print ( n, x, y, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_F_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  p00_f_test ( )
  timestamp ( )

