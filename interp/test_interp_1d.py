#! /usr/bin/env python3
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

def p00_plot ( prob ):

#*****************************************************************************80
#
## P00_PLOT plots the data for any of the tests.
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
#    Input, integer PROB, the problem index.
#
#    Output, string FILENAME, the name of the plot filename.
#
  import matplotlib.pyplot as plt
  import numpy as np

  prob_num = p00_prob_num ( )

  if ( prob < 1 or prob_num < prob ):
    print ( '' )
    print ( 'P00_PLOT - Fatal error!' )
    print ( '  Values of PROB must be between 1 and %d.' % ( prob_num ) )
    exit ( 'P00_PLOT - Fatal error!' )

  xmin = 0.0
  xmax = 1.0
  n = 501

  x = np.linspace ( xmin, xmax, n )
  y = p00_f ( prob, n, x )
  t = p00_title ( prob )
#
#  PYLAB commands.
#
  plt.plot ( x, y, linewidth = 2.0 )
  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )

  filename = 'p0' + str ( prob ) + '_plot.png'

  plt.savefig ( filename )
  plt.show ( block = False )
  plt.clf ( )

  return filename

def p00_plot_test ( ):

#*****************************************************************************80
#
## P00_PLOT_TEST tests P00_PLOT.
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
  import platform

  print ( '' )
  print ( 'P00_PLOT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_PLOT plots any test problem.' )

  num = p00_prob_num ( )

  print ( '' )
  print ( '  TEST_INTERP_1D includes %d test problems.' % ( num ) )

  print ( '' )
  for prob in range ( 1, num + 1 ):
    filename = p00_plot ( prob )
    print ( '  #%d  "%s"' % ( prob, filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_PLOT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_prob_num ( ):

#*****************************************************************************80
#
## P00_PROB_NUM returns the number of problems.
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
#    Output, integer VALUE, the number of problems.
#
  value = 8

  return value

def p00_prob_num_test ( ):

#*****************************************************************************80
#
## P00_PROB_NUM_TEST tests P00_PROB_NUM.
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
  import platform

  print ( '' )
  print ( 'P00_PROB_NUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_PROB_NUM returns the number of test problems.' )

  num = p00_prob_num ( )

  print ( '' )
  print ( '  TEST_INTERP_1D includes %d test problems.' % ( num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_PROB_NUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p00_title ( prob ):

#*****************************************************************************80
#
## P00_TITLE returns the title of any problem.
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
#    Output, string TITLE, the title of the problem.
#
  from sys import exit

  if ( prob == 1 ):
    title = p01_title ( )
  elif ( prob == 2 ):
    title = p02_title ( )
  elif ( prob == 3 ):
    title = p03_title ( )
  elif ( prob == 4 ):
    title = p04_title ( )
  elif ( prob == 5 ):
    title = p05_title ( )
  elif ( prob == 6 ):
    title = p06_title ( )
  elif ( prob == 7 ):
    title = p07_title ( )
  elif ( prob == 8 ):
    title = p08_title ( )
  else:
    print ( '' )
    print ( 'P00_TITLE - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    exit ( 'P00_TITLE - Fatal error!' )

  return title

def p01_title ( ):

#*****************************************************************************80
#
## P01_TITLE returns the title of problem p01.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = steps -1/2/1 at [0,1/3], [1/3,4/5], [4/5,1].'

  return title

def p02_title ( ):

#*****************************************************************************80
#
## P02_TITLE returns the title of problem p02.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = (1-3x), x < 1/3 (6x-2) if 1/3 < x'

  return title

def p03_title ( ):

#*****************************************************************************80
#
## P03_TITLE returns the title of problem p03.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = x (10*x-1) (5x-2) (5x-2) (4x-3.4) (x-1)'

  return title

def p04_title ( ):

#*****************************************************************************80
#
## P04_TITLE returns the title of problem p04.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = atan ( 40 * x - 15 )'

  return title

def p05_title ( ):

#*****************************************************************************80
#
## P05_TITLE returns the title of problem p05.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = cos(7*x)+5*cos(11.2*x)-2*cos(14*x)+5*cos(31.5*x)+7*cos(63*x).'

  return title

def p06_title ( ):

#*****************************************************************************80
#
## P06_TITLE returns the title of problem p06.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = exp ( - ( 4*x-1 )^2 )'

  return title

def p07_title ( ):

#*****************************************************************************80
#
## P07_TITLE returns the title of problem p07.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = exp ( 2 x ) if x < 0.5, 0 otherwise'

  return title

def p08_title ( ):

#*****************************************************************************80
#
## P08_TITLE returns the title of problem p08.
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
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = 1 / ( 1 + ( 10 * (x-1/2) )^2 )'

  return title

def p00_title_test ( ):

#*****************************************************************************80
#
## P00_TITLE_TEST tests P00_TITLE.
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
  import platform

  print ( '' )
  print ( 'P00_TITLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_TITLE returns the title of any test problems.' )

  num = p00_prob_num ( )

  print ( '' )
  print ( '  TEST_INTERP_1D includes %d test problems.' % ( num ) )

  print ( '' )
  for prob in range ( 1, num + 1 ):
    title = p00_title ( prob )
    print ( '  #%d  "%s"' % ( prob, title ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_TITLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## R8VEC2_PRINT prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
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
#    Input, integer N, the number of components of the vector.
#
#    Input, real A1(N), A2(N), the vectors to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## R8VEC2_PRINT_TEST tests R8VEC2_PRINT.
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

  print ( '' )
  print ( 'R8VEC2_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC2_PRINT prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def test_interp_1d_test ( ):

#*****************************************************************************80
#
## TEST_INTERP_1D_TEST tests the TEST_INTERP_1D library.
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
  import platform

  print ( '' )
  print ( 'TEST_INTERP_1D_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the TEST_INTERP_1D library.' )

  p00_prob_num_test ( )
  p00_title_test ( )
  p00_f_test ( )
  p00_plot_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TEST_INTERP_1D_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  test_interp_1d_test ( )
  timestamp ( )


