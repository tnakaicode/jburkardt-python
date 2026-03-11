#! /usr/bin/env python3
#
def test_interp_fun_test ( ):

#*****************************************************************************80
#
## test_interp_fun_test() tests test_interp_fun().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  timestamp (  )

  print ( '' )
  print ( 'test_interp_fun_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test test_interp_fun().' )

  test_interp_fun_test01 ( )
  test_interp_fun_test02 ( )
  test_interp_fun_test03 ( )
# test_interp_fun_test04 ( )
# test_interp_fun_test05 ( )
# test_interp_fun_test06 ( )
# test_interp_fun_test07 ( )
# test_interp_fun_test08 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_interp_fun_test():' )
  print ( '  Normal end of execution.' )

  return

def p00_fun ( prob, x ):

#*****************************************************************************80
#
## p00_fun() evaluates the function for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the desired test problem.
#
#    real X, the point at which the function
#    is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  if ( prob == 1 ):
    value = p01_fun ( x )
  elif ( prob == 2 ):
    value = p02_fun ( x )
  elif ( prob == 3 ):
    value = p03_fun ( x )
  elif ( prob == 4 ):
    value = p04_fun ( x )
  elif ( prob == 5 ):
    value = p05_fun ( x )
  else:
    print ( '' )
    print ( 'P00_fun - Fatal error!' )
    print ( '  Illegal problem number = ', prob )
    value = 0.0
    raise Exception ( 'P00_fun - Fatal error!' )

  return value

def p00_lim ( prob ):

#*****************************************************************************80
#
## p00_lim() returns the limits of the approximation interval for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the desired test problem.
#
#  Output:
#
#    real A, B, the lower and upper limits of
#    the approximation interval.
#
  if ( prob == 1 ):
    a, b = p01_lim ( )
  elif ( prob == 2 ):
    a, b = p02_lim ( )
  elif ( prob == 3 ):
    a, b = p03_lim ( )
  elif ( prob == 4 ):
    a, b = p04_lim ( )
  elif ( prob == 5 ):
    a, b = p05_lim ( )
  else:
    print ( '' )
    print ( 'P00_lim - Fatal error!' )
    print ( '  Illegal problem number = ', prob )
    raise Exception ( 'P00_lim - Fatal error!' )

  return a, b

def p00_plot ( prob ):

#*****************************************************************************80
#
## p00_plot() plots the data for any of the tests.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
  import matplotlib.pyplot as plt
  import numpy as np

  prob_num = p00_prob_num ( )

  if ( prob < 1 or prob_num < prob ):
    print ( '' )
    print ( 'p00_plot(): Fatal error!' )
    print ( '  Values of PROB must be between 1 and', prob_num )
    raise Exception ( 'p00_plot(): Fatal error!' )

  a, b = p00_lim ( prob )

  x = np.linspace ( a, b, 501 )

  y = p00_fun ( prob, x )

  t = p00_title ( prob )

  plt.clf ( )
  plt.plot ( x, y, linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.title ( t )
  plt.show ( )

  return

def p00_prob_num ( ):

#*****************************************************************************80
#
## p00_prob_num() returns the number of problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer PROB_NUM, the number of problems.
#
  prob_num = 5

  return prob_num

def p00_story ( prob ):

#*****************************************************************************80
#
## p00_story() prints the "story" for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
  if ( prob == 1 ):
    p01_story ( )
  elif ( prob == 2 ):
    p02_story ( )
  elif ( prob == 3 ):
    p03_story ( )
  elif ( prob == 4 ):
    p04_story ( )
  elif ( prob == 5 ):
    p05_story ( )
  else:
    print ( '' )
    print ( 'p00_story(): Fatal error!' )
    print ( '  Unexpected input value of PROB.' )
    raise Exception ( 'p00_story(): Fatal error!' )

  return

def p00_title ( prob ):

#*****************************************************************************80
#
## p00_title() returns the title of any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the desired test problem.
#
#  Output:
#
#    string TITLE, the title of the problem.
#
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
  else:
    title = ' '
    print ( '' )
    print ( 'p00_title(): Fatal error!' )
    print ( '  Illegal problem number = ', prob )
    raise Exception ( 'p00_title(): Fatal error!' )

  return title

def p01_fun ( x ):

#*****************************************************************************80
#
## p01_fun() evaluates the function for problem 1.
#
#  Discussion:
#
#    This is a famous example, due to Runge.  If equally spaced
#    abscissas are used, the sequence of interpolating polynomials Pn(X)
#    diverges, in the sense that the max norm of the difference
#    between Pn(X) and F(X) becomes arbitrarily large as N increases.
#
#  Dimension:
#
#    N = 1
#
#  Interval:
#
#    -5 <= X <= 5
#
#  Function:
#
#    1 / ( X * X + 1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which the function
#    is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  value = 1.0 / ( x * x + 1.0 )

  return value

def p01_lim ( ):

#*****************************************************************************80
#
## p01_lim() returns the limits of the approximation interval for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of the interval
#    of approximation.
#
  a = -5.0
  b =  5.0

  return a, b

def p01_story ( ):

#*****************************************************************************80
#
## p01_story() prints the "story" for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( '  This is a famous example, due to Runge.  If equally spaced' )
  print ( '  abscissas are used, the sequence of interpolating polynomials Pn(X)' )
  print ( '  diverges, in the sense that the max norm of the difference' )
  print ( '  between Pn(X) and F(X) becomes arbitrarily large as N increases.' )

  return

def p01_title ( ):

#*****************************************************************************80
#
## p01_title() returns the title of problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Runge example, f(x) = 1 / ( x * x + 1 ), [-5,5]'

  return title

def p02_fun ( x ):

#*****************************************************************************80
#
## p02_fun() evaluates the function for problem 2.
#
#  Discussion:
#
#    This example is due to Bernstein.  If equally spaced
#    abscissas are used, the sequence of interpolating polynomials Pn(X)
#    only converges to F(X) at -1, 0, and 1.
#
#  Dimension:
#
#    N = 1
#
#  Interval:
#
#    -1 <= X <= 1
#
#  Function:
#
#    ABS ( X )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which the function
#    is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  import numpy as np

  value = np.abs ( x )

  return value

def p02_lim ( ):

#*****************************************************************************80
#
## p02_lim() returns the limits of the approximation interval for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of the interval
#    of approximation.
#
  a = -1.0
  b =  1.0

  return a, b

def p02_story ( ):

#*****************************************************************************80
#
## p02_story() prints the "story" for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( '  This example is due to Bernstein.' )
  print ( '  If equally spaced abscissas are used, the sequence of interpolating' )
  print ( '  polynomials Pn(X) only converges to F(X) at -1, 0, and 1.' )

  return

def p02_title ( ):

#*****************************************************************************80
#
## p02_title() returns the title of problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Bernstein example, f(x) = abs ( x ), [-1,1]'

  return title

def p03_fun ( x ):

#*****************************************************************************80
#
## p03_fun() evaluates the function for problem 3.
#
#  Discussion:
#
#    This is a step function with a jump from 0 to 1 at 0.
#
#  Dimension:
#
#    N = 1
#
#  Interval:
#
#    -1 <= X <= 1
#
#  Function:
#
#    F(X) = 0 if X < 0
#           1 if 0 < X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which the function
#    is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  if ( 0.0 <= x ):
    value = 1.0
  else:
    value = 0.0

  return value

def p03_lim ( ):

#*****************************************************************************80
#
## p03_lim() returns the limits of the approximation interval for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of the interval
#    of approximation.
#
  a = -1.0
  b =  1.0

  return a, b

def p03_story ( ):

#*****************************************************************************80
#
## p03_story() prints the "story" for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( '  The step function is discontinuous.' )
  print ( '  Attempts to approximate this function by high degree polynomials' )
  print ( '  will rapidly diverge.' )

  return

def p03_title ( ):

#*****************************************************************************80
#
## p03_title() returns the title of problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Step function, f jumps from 0 to 1 at 0.'

  return title

def p04_fun ( x ):

#*****************************************************************************80
#
## p04_fun() evaluates the function for problem 4.
#
#  Discussion:
#
#    This function is highly oscillatory near X = 0.
#
#  Dimension:
#
#    N = 1
#
#  Interval:
#
#    0 <= X <= 1
#
#  Function:
#
#    F(X) = sqrt ( x * ( 1 - x ) ) * sin ( 2.1 * pi / ( x + 0.05 ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which the function
#    is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  import numpy as np

  value = np.sqrt ( x * ( 1.0 - x ) ) * np.sin ( 2.1 * np.pi / ( x + 0.05 ) )

  return value

def p04_lim ( ):

#*****************************************************************************80
#
## p04_lim() returns the limits of the approximation interval for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of the interval
#    of approximation.
#
  a = 0.0
  b = 1.0

  return a, b

def p04_story ( ):

#*****************************************************************************80
#
## p04_story() prints the "story" for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( '  The Doppler function is continuous, but highly oscillatory' )
  print ( '  near the value X = 0.' )

  return

def p04_title ( ):

#*****************************************************************************80
#
## p04_title() returns the title of problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'The Doppler function, highly oscillatory near X = 0.'

  return title

def p05_fun ( x ):

#*****************************************************************************80
#
## p05_fun() evaluates the function for problem 5.
#
#  Discussion:
#
#    This example is difficult to interpolate because it has a piecewise
#    definition, and the character of the function changes dramatically
#    from piece to piece.
#
#  Dimension:
#
#    N = 1
#
#  Interval:
#
#    0 <= X <= 10
#
#  Function:
#
#    F(X) = max ( sin(x) + sin(x^2), 1 - abs(x-5)/5 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which the function
#    is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  import numpy as np

  value = max ( np.sin ( x ) + np.sin ( x * x ), 1.0 - np.abs ( x - 5.0 ) / 5.0 )

  return value

def p05_lim ( ):

#*****************************************************************************80
#
## p05_lim() returns the limits of the approximation interval for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of the interval
#    of approximation.
#
  a = 0.0
  b = 10.0

  return a, b

def p05_story ( ):

#*****************************************************************************80
#
## p05_story() prints the "story" for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( '  This example is very difficult to interpolate.' )
  print ( '  It is essentially defined as a piecewise function,' )
  print ( '  alternating between a straight line and a sinusoidal curve.' )

  return

def p05_title ( ):

#*****************************************************************************80
#
## p05_title() returns the title of problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Rabbit ears, f(x) = max(sin(x)+sin(x^2),1-abs(x-5)/5), [0,10].'

  return title

def test_interp_fun_test01 ( ):

#*****************************************************************************80
#
## test_interp_fun_test01() tests p00_title().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'test_interp_fun_test01():' )
  print ( '  p00_prob_num() returns the number of problems.' )
  print ( '  p00_title() returns the problem title.' )
  print ( '  p00_limit() returns the problem limits.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '  Number of problems = ', prob_num )

  for prob in range ( 1, prob_num + 1 ):

    print ( '' )
    print ( '  Problem ', prob )
    title = p00_title ( prob )
    print ( title )
    a, b = p00_lim ( prob )
    print ( '  Range is [', a, ',', b, ']' )

  return

def test_interp_fun_test02 ( ):

#*****************************************************************************80
#
## test_interp_fun_test02() tests p00_story().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'test_interp_fun_test02():' )
  print ( '  p00_story() prints the problem "story".' )

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    print ( '' )
    print ( '  The story for problem ', prob )

    p00_story ( prob )

  return

def test_interp_fun_test03 ( ):

#*****************************************************************************80
#
## test_interp_fun_test03() uses equally spaced polynomial interpolation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  max_tab = 21

  print ( '' )
  print ( 'test_interp_fun_test03():' )
  print ( '  Equally spaced polynomial interpolation.' )
  print ( '  Evaluate the function at N equally spaced points.' )
  print ( '  Determine the N-1 degre polynomial interpolant.' )
  print ( '  Estimate the maximum difference between the function' )
  print ( '  and the interpolant.' )

  prob_num = p00_prob_num ( )

  for prob in range ( 1, prob_num + 1 ):

    title = p00_title ( prob )
    a, b = p00_lim ( prob )

    print ( '' )
    print ( '  Problem', prob )
    print ( '  ' + title )
    print ( '' )
    print ( '     N   Max |Error|' )
    print ( '' )

    for n in range ( 1, max_tab + 1, 4 ):
#
#  Evaluate the function at N equally spaced points.
#
      xtab = np.zeros ( n )
      ytab = np.zeros ( n )

      for i in range ( 0, n ):

        if ( n == 1 ):
          xtab[i] = 0.5 * ( a + b )
        else:
          xtab[i] = ( ( n - i - 1 ) * a \
                    + (     i     ) * b \
                  ) / ( n     - 1 )

        ytab[i] = p00_fun ( prob, xtab[i] )
#
#  Construct the interpolating polynomial via finite differences.
#
      diftab = data_to_dif ( n, xtab, ytab )
#
#  Now examine the approximation error.
#
      error_max = 0.0
      imax = 100

      for i in range ( 0, imax + 1 ):

        if ( imax == 0 ):
          x = 0.5 * ( a + b )
        else:
          x = ( ( imax - i ) * a    \
              + (        i ) * b  ) \
              / ( imax     )

        ytrue = p00_fun ( prob, x )
        yapprox = dif_value ( n, xtab, diftab, x )
        error_max = max ( error_max, np.abs ( ytrue - yapprox ) )

      print ( '  %4d  %14g' % ( n, error_max ) )

  return

def data_to_dif ( ntab, xtab, ytab ):

#*****************************************************************************80
#
## data_to_dif() computes a divided difference table from raw data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer NTAB, the number of pairs of points
#    (XTAB(I),YTAB(I)) which are to be used as data.  The
#    number of entries to be used in DIFTAB, XTAB and YTAB.
#
#    real XTAB(NTAB), the X values at which data was taken.
#
#    real YTAB(NTAB), the corresponding Y values.
#
#  Output:
#
#    real DIFTAB(NTAB), the divided difference
#    coefficients corresponding to the input (XTAB,YTAB).
#
  if ( not r8vec_is_distinct ( ntab, xtab ) ):
    print ( '' )
    print ( 'data_to_dif(): Fatal error!' )
    print ( '  Two entries of XTAB are equal!' )
    print ( xtab )
    raise Exception ( 'data_to_dif(): Fatal error!' )
#
#  Copy the data values into DIFTAB.
#
  diftab = ytab.copy()
#
#  Compute the divided differences.
#
  for i in range ( 2, ntab + 1 ):
    for j in range ( ntab, i - 1, -1 ):
      diftab[j-1] = ( diftab[j-1] - diftab[j-1-1] ) / ( xtab[j-1] - xtab[j+1-i-1] )

  return diftab

def dif_value ( nd, xd, yd, xv ):

#*****************************************************************************80
#
## dif_value() evaluates a divided difference polynomial at one or more points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carl deBoor,
#    A Practical Guide to Splines,
#    Springer, 2001,
#    ISBN: 0387953663,
#    LC: QA1.A647.v27.
#
#  Input:
#
#    integer ND, the order of the difference table.
#
#    real XD(ND), the X values of the difference table.
#
#    real YD(ND), the divided differences.
#
#    real XV(NV), the evaluation points.
#
#  Output:
#
#    real YV(NV), the value of the divided difference
#    polynomial at the evaluation points.
#
  import numpy as np
#
#  If XV is a scalar, we need to make it look like a vector!
#
  xv = np.atleast_1d ( xv )

  nv = xv.shape[0]
  yv = yd[nd-1] * np.ones ( nv )
#
#  Another indexing issue resolved by adding -1 to array indices.
#
  for i in range ( 1, nd ):
    yv[0:nv] = yd[nd-i-1] + ( xv[0:nv] - xd[nd-i-1] ) * yv[0:nv]

  if ( nv == 1 ):
    yv = yv[0]

  return yv

def r8vec_is_distinct ( n, a ):

#*****************************************************************************80
#
## r8vec_is_distinct() is true if the entries in an R8VEC are distinct.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector to be checked.
#
#  Output:
#
#    bool VALUE is true if the elements of A are distinct.
#
  for i in range ( 1, n ):
    for j in range ( 0, i ):
      if ( a[i] == a[j] ):
        value = False;
        return value

  value = True

  return value

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
  test_interp_fun_test ( )
  timestamp ( )

