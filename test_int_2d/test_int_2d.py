#! /usr/bin/env python3
#
def test_int_2d_test ( ):

#*****************************************************************************80
#
## test_int_2d_test() tests test_int_2d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'test_int_2d_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test test_int_2d().' )

  test_int_2d_test01 ( )
  test_int_2d_test02 ( )
  test_int_2d_test03 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_int_2d_test():' )
  print ( '  Normal end of execution.' )

  return

def test_int_2d_test01 ( ):

#*****************************************************************************80
#
## test_int_2d_test01() applies a Monte Carlo rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'test_int_2d_test01():' )
  print ( '  Use a Monte Carlo rule.' )
  print ( '  Repeatedly multiply the number of points by 16.' )

  problem_num = p00_problem_num ( )

  print ( '' )
  print ( '   Problem      Points      Approx          Error' )

  for problem in range ( 1, problem_num + 1 ):

    print ( '' )

    n = 1

    for i in range ( 0, 12 ):

      x = rng.random ( n )
      y = rng.random ( n )

      xlo, xhi, ylo, yhi = p00_lim ( problem )

      x = ( 1.0 - x ) * xlo + x * xhi
      y = ( 1.0 - y ) * ylo + y * yhi

      volume = ( xhi - xlo ) * ( yhi - ylo )

      fx = p00_fun ( problem, x, y )

      quad = volume * np.sum ( fx ) / n

      exact = p00_exact ( problem )

      error = np.abs ( quad - exact )

      print ( '  %8d  %10d  %14e  %14e' % ( problem, n, quad, error ) )

      n = n * 4

    print ( '  %8d       Exact  %14e' % ( problem, exact ) )

  return

def test_int_2d_test02 ( ):

#*****************************************************************************80
#
## test_int_2d_test02() applies a product of composite midpoint rules.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'test_int_2d_test02():' )
  print ( '  Apply a product of composite midpoint rules.' )
  print ( '  Repeatedly multiply the number of points by 16.' )

  problem_num = p00_problem_num ( )

  print ( '' )
  print ( '   Problem      Points      Approx          Error' )

  for problem in range ( 1, problem_num + 1 ):

    print ( '' )

    nx = 1
    ny = 1

    xlo, xhi, ylo, yhi = p00_lim ( problem )
    volume = ( xhi - xlo ) * ( yhi - ylo )

    for i in range ( 0, 12 ):

      n = nx * ny
      x1d = np.linspace ( xlo, xhi, nx )
      y1d = np.linspace ( ylo, yhi, ny )

      x, y = np.meshgrid ( x1d, y1d )

      fx = p00_fun ( problem, x, y )

      quad = volume * np.sum ( fx ) / n

      exact = p00_exact ( problem )

      error = np.abs ( quad - exact )

      print ( '  %8d  %10d  %14e  %14e' % ( problem, n, quad, error ) )

      nx = nx * 2
      ny = ny * 2

    print ( '  %8d       Exact  %14e' % ( problem, exact ) )

  return

def test_int_2d_test03 ( ):

#*****************************************************************************80
#
## test_int_2d_test03(): applies a product of Gauss-Legendre rules.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'test_int_2d_test03():' )
  print ( '  Use a product of Gauss-Legendre rules.' )
  print ( '  The 1D rules essentially double in order.' )

  problem_num = p00_problem_num ( )

  print ( '' )
  print ( '   Problem      Points       Approx         Error' )

  for problem in range ( 1, problem_num + 1 ):

    print ( '' )

    nx = 1
    ny = 1
    xlo, xhi, ylo, yhi = p00_lim ( problem )
    volume = ( xhi - xlo ) * ( yhi - ylo )

    for i in range ( 1, 9 ):

      z1d, w1d = legendre_dr_compute ( nx )

      nxy = nx * ny

      w = np.zeros ( nxy )
      x = np.zeros ( nxy )
      y = np.zeros ( nxy )

      k = 0
      for ix in range ( 0, nx ):
        for iy in range ( 0, ny ):
          x[k] = 0.5 * ( ( 1.0 - z1d[ix] ) * xlo + ( 1.0 + z1d[ix] ) * xhi )
          y[k] = 0.5 * ( ( 1.0 - z1d[iy] ) * ylo + ( 1.0 + z1d[iy] ) * yhi )
          w[k] = w1d[ix] * w1d[iy]
          k = k + 1

      fxy = p00_fun ( problem, x, y )

      quad = volume * np.dot ( w, fxy  ) / 4.0

      exact = p00_exact ( problem )

      error = abs ( quad - exact )

      print ( '  %8d  %10d  %14g  %14g' % ( problem, nxy, quad, error ) )

      nx = 2 * nx + 1
      ny = nx

    print ( '  %8d       Exact  %14g' % ( problem, exact ) )

  return

def legendre_dr_compute ( n ):

#*****************************************************************************80
#
## legendre_dr_compute(): Gauss-Legendre quadrature by Davis-Rabinowitz method.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the order.
#    N must be greater than 0.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  x = np.zeros ( n )
  w = np.zeros ( n )

  if ( n < 1 ):
    print ( '' )
    print ( 'legendre_dr_compute(): Fatal error!' )
    print ( '  Illegal value of N = ', n )
    raise Exception ( 'legendre_dr_compute(): Fatal error!' )

  e1 = n * ( n + 1 )

  m = ( ( n + 1 ) // 2 )

  for i in range ( 1, m + 1 ):

    mp1mi = m + 1 - i

    t = float ( 4 * i - 1 ) * np.pi / float ( 4 * n + 2 )

    x0 = np.cos ( t ) \
      * ( 1.0 - ( 1.0 - 1.0 / float ( n ) ) / float ( 8 * n * n ) )

    pkm1 = 1.0
    pk = x0

    for k in range ( 2, n + 1 ):
      pkp1 = 2.0 * x0 * pk - pkm1 - ( x0 * pk - pkm1 ) / float ( k )
      pkm1 = pk
      pk = pkp1

    d1 = float ( n ) * ( pkm1 - x0 * pk )

    dpn = d1 / ( 1.0 - x0 * x0 )

    d2pn = ( 2.0 * x0 * dpn - e1 * pk ) / ( 1.0 - x0 * x0 )

    d3pn = ( 4.0 * x0 * d2pn + ( 2.0 - e1 ) * dpn ) / ( 1.0 - x0 * x0 )

    d4pn = ( 6.0 * x0 * d3pn + ( 6.0 - e1 ) * d2pn ) / ( 1.0 - x0 * x0 )

    u = pk / dpn
    v = d2pn / dpn
#
#  Initial approximation H:
#
    h = - u * ( 1.0 + 0.5 * u * ( v + u * ( v * v - d3pn / ( 3.0 * dpn ) ) ) )
#
#  Refine H using one step of Newton's method:
#
    p = pk + h * ( dpn + 0.5 * h * ( d2pn + h / 3.0 \
      * ( d3pn + 0.25 * h * d4pn ) ) )

    dp = dpn + h * ( d2pn + 0.5 * h * ( d3pn + h * d4pn / 3.0 ) )

    h = h - p / dp

    xtemp = x0 + h

    x[mp1mi-1] = xtemp

    fx = d1 - h * e1 * ( pk + 0.5 * h * ( dpn + h / 3.0 \
      * ( d2pn + 0.25 * h * ( d3pn + 0.2 * h * d4pn ) ) ) )

    w[mp1mi-1] = 2.0 * ( 1.0 - xtemp * xtemp ) / fx / fx

  if ( ( n % 2 ) == 1 ):
    x[0] = 0.0
#
#  Shift the data up.
#
  nmove = ( ( n + 1 ) // 2 )
  ncopy = n - nmove

  for i in range ( 1, nmove + 1 ):
    iback = n + 1 - i
    x[iback-1] = x[iback-ncopy-1]
    w[iback-1] = w[iback-ncopy-1]
#
#  Reflect values for the negative abscissas.
#
  for i in range ( 1, n - nmove + 1 ):
    x[i-1] = - x[n-i]
    w[i-1] =   w[n-i]

  return x, w

def p00_exact ( problem ):

#*****************************************************************************80
#
## p00_exact() returns the exact integral for any problem.
#
#  Discussion:
#
#    This routine provides a "generic" interface to the exact integral
#    routines for the various problems, and allows a problem to be called
#    by index rather than by name.
#
#    In some cases, the "exact" value of the integral is in fact
#    merely a respectable approximation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem index.
#
#  Output:
#
#    real EXACT, the exact value of the integral.
#
  if ( problem == 1 ):
    exact = p01_exact ( )
  elif ( problem == 2 ):
    exact = p02_exact ( )
  elif ( problem == 3 ):
    exact = p03_exact ( )
  elif ( problem == 4 ):
    exact = p04_exact ( )
  elif ( problem == 5 ):
    exact = p05_exact ( )
  elif ( problem == 6 ):
    exact = p06_exact ( )
  elif ( problem == 7 ):
    exact = p07_exact ( )
  elif ( problem == 8 ):
    exact = p08_exact ( )
  else:
    print ( '' )
    print ( 'p00_exact(): Fatal error!' )
    print ( '  Illegal problem index = ', problem )
    raise Exception ( 'p00_exact(): Fatal error!' )

  return exact

def p00_fun ( problem, x, y ):

#*****************************************************************************80
#
## p00_fun() evaluates the integrand for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem index.
#
#    real X(*), Y(*), the evaluation points.
#
#  Output:
#
#    real FX(*), the integrand values.
#
  import numpy as np

  if ( problem == 1 ):
    fx = p01_fun ( x, y )
  elif ( problem == 2 ):
    fx = p02_fun ( x, y )
  elif ( problem == 3 ):
    fx = p03_fun ( x, y )
  elif ( problem == 4 ):
    fx = p04_fun ( x, y )
  elif ( problem == 5 ):
    fx = p05_fun ( x, y )
  elif ( problem == 6 ):
    fx = p06_fun ( x, y )
  elif ( problem == 7 ):
    fx = p07_fun ( x, y )
  elif ( problem == 8 ):
    fx = p08_fun ( x, y )
  else:
    print ( '' )
    print ( 'p00_fun(): Fatal error!' )
    print ( '  Illegal problem index = ', problem )
    raise Exception ( 'p00_fun(): Fatal error!' )

  return fx

def p00_lim ( problem ):

#*****************************************************************************80
#
## p00_lim() returns the integration limits for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem index.
#
#  Output:
#
#    real xlo, xhi, ylo, yhi: the limits of integration.
#
  if ( problem == 1 ):
    xlo, xhi, ylo, yhi = p01_lim ( )
  elif ( problem == 2 ):
    xlo, xhi, ylo, yhi = p02_lim ( )
  elif ( problem == 3 ):
    xlo, xhi, ylo, yhi = p03_lim ( )
  elif ( problem == 4 ):
    xlo, xhi, ylo, yhi = p04_lim ( )
  elif ( problem == 5 ):
    xlo, xhi, ylo, yhi = p05_lim ( )
  elif ( problem == 6 ):
    xlo, xhi, ylo, yhi = p06_lim ( )
  elif ( problem == 7 ):
    xlo, xhi, ylo, yhi = p07_lim ( )
  elif ( problem == 8 ):
    xlo, xhi, ylo, yhi = p08_lim ( )
  else:
    print ( '' )
    print ( 'p00_lim(): Fatal error!' )
    print ( '  Illegal problem index = ', problem )
    raise Exception ( 'p00_lim(): Fatal error!' )

  return xlo, xhi, ylo, yhi

def p00_problem_num ( ):

#*****************************************************************************80
#
## p00_problem_num() returns the number of test integration problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer PROBLEM_NUM, the number of problems.
#
  problem_num = 8

  return problem_num

def p01_exact ( ):

#*****************************************************************************80
#
## p01_exact() returns the exact integral for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = np.pi * np.pi / 6.0

  return exact

def p01_fun ( x, y ):

#*****************************************************************************80
#
## p01_fun() evaluates the integrand for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gwynne Evans,
#    Practical Numerical Integration,
#    Wiley, 1993,
#    ISBN: 047193898X,
#    LC: QA299.3E93.
#
#  Input:
#
#    real x(*), y(*): the evaluation points.
#
#  Output:
#
#    real fx(*): the integrand values.
#
  import numpy as np
  fx = np.zeros_like ( x )
  i = np.where ( 1.0 - x * y != 0.0 )
  fx[i] = 1.0 / ( 1.0 - x[i] * y[i] )

  return fx

def p01_lim ( ):

#*****************************************************************************80
#
## p01_lim() returns the integration limits for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real xlo, xhi, ylo, yhi: the limits of integration.
#
  xlo = 0.0
  xhi = 1.0
  ylo = 0.0
  yhi = 1.0

  return xlo, xhi, ylo, yhi

def p02_exact ( ):

#*****************************************************************************80
#
## p02_exact() returns the exact integral for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = 2.0 * np.pi * np.log ( 2.0 )

  return exact

def p02_fun ( x, y ):

#*****************************************************************************80
#
## p02_fun() evaluates the integrand for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gwynne Evans,
#    Practical Numerical Integration,
#    Wiley, 1993,
#    ISBN: 047193898X,
#    LC: QA299.3E93.
#
#  Input:
#
#    real x(*), y(*): the evaluation points.
#
#  Output:
#
#    real fx(*): the integrand values.
#
  import numpy as np
  fx = np.zeros_like ( x )
  i = np.where ( 1.0 - x**2 * y**2 != 0.0 )
  fx[i] = 1.0 / np.sqrt ( 1.0 - x[i]**2 * y[i]**2 )

  return fx

def p02_lim ( ):

#*****************************************************************************80
#
## p02_lim() returns the integration limits for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real xlo, xhi, ylo, yhi: the limits of integration.
#
  xlo = -1.0
  xhi = +1.0
  ylo = -1.0
  yhi = +1.0

  return xlo, xhi, ylo, yhi

def p03_exact ( ):

#*****************************************************************************80
#
## p03_exact() returns the exact integral for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = ( 16.0 / 3.0 ) * ( 2.0 - np.sqrt ( 2.0 ) )

  return exact

def p03_fun ( x, y ):

#*****************************************************************************80
#
## p03_fun() evaluates the integrand for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gwynne Evans,
#    Practical Numerical Integration,
#    Wiley, 1993,
#    ISBN: 047193898X,
#    LC: QA299.3E93.
#
#  Input:
#
#    real x(*), y(*): the evaluation points.
#
#  Output:
#
#    real fx(*): the integrand values.
#
  import numpy as np
  fx = np.zeros_like ( x )
  i = np.where ( np.sqrt ( 2.0 - x - y != 0.0 ) )
  fx[i] = 1.0 / np.sqrt ( 2.0 - x[i] - y[i] )

  return fx

def p03_lim ( ):

#*****************************************************************************80
#
## p03_lim() returns the integration limits for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real xlo, xhi, ylo, yhi: the limits of integration.
#
  xlo = -1.0
  xhi = +1.0
  ylo = -1.0
  yhi = +1.0

  return xlo, xhi, ylo, yhi

def p04_exact ( ):

#*****************************************************************************80
#
## p04_exact() returns the exact integral for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = ( np.sqrt ( 32.0 ) / 3.0 ) \
    * ( np.sqrt ( 27.0 ) - np.sqrt ( 8.0 ) - 1.0 )

  return exact

def p04_fun ( x, y ):

#*****************************************************************************80
#
## p04_fun() evaluates the integrand for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gwynne Evans,
#    Practical Numerical Integration,
#    Wiley, 1993,
#    ISBN: 047193898X,
#    LC: QA299.3E93.
#
#  Input:
#
#    real x(*), y(*): the evaluation points.
#
#  Output:
#
#    real fx(*): the integrand values.
#
  import numpy as np

  fx = np.zeros_like ( x )
  i = np.where ( np.sqrt ( 3.0 - x - 2.0 * y != 0.0 ) )
  fx[i] = 1.0 / np.sqrt ( 3.0 - x[i] - 2.0 * y[i] )

  return fx

def p04_lim ( ):

#*****************************************************************************80
#
## p04_lim() returns the integration limits for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real xlo, xhi, ylo, yhi: the limits of integration.
#
  xlo = -1.0
  xhi = +1.0
  ylo = -1.0
  yhi = +1.0

  return xlo, xhi, ylo, yhi

def p05_exact ( ):

#*****************************************************************************80
#
## p05_exact() returns the exact integral for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 4.0 / 9.0

  return exact

def p05_fun ( x, y ):

#*****************************************************************************80
#
## p05_fun() evaluates the integrand for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gwynne Evans,
#    Practical Numerical Integration,
#    Wiley, 1993,
#    ISBN: 047193898X,
#    LC: QA299.3E93.
#
#  Input:
#
#    real x(*), y(*): the evaluation points.
#
#  Output:
#
#    real fx(*): the integrand values.
#
  import numpy as np

  fx = np.sqrt ( x * y )

  return fx

def p05_lim ( ):

#*****************************************************************************80
#
## p05_lim() returns the integration limits for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real xlo, xhi, ylo, yhi: the limits of integration.
#
  xlo =  0.0
  xhi = +1.0
  ylo =  0.0
  yhi = +1.0

  return xlo, xhi, ylo, yhi

def p06_exact ( ):

#*****************************************************************************80
#
## p06_exact() returns the exact integral for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = ( 5.0 / 3.0 ) + ( np.pi / 16.0 )

  return exact

def p06_fun ( x, y ):

#*****************************************************************************80
#
## p06_fun() evaluates the integrand for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gwynne Evans,
#    Practical Numerical Integration,
#    Wiley, 1993,
#    ISBN: 047193898X,
#    LC: QA299.3E93.
#
#  Input:
#
#    real x(*), y(*): the evaluation points.
#
#  Output:
#
#    real fx(*): the integrand values.
#
  import numpy as np

  fx = np.abs ( x**2 + y**2 - 0.25 )

  return fx

def p06_lim ( ):

#*****************************************************************************80
#
## p06_lim() returns the integration limits for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real xlo, xhi, ylo, yhi: the limits of integration.
#
  xlo = -1.0
  xhi = +1.0
  ylo = -1.0
  yhi = +1.0

  return xlo, xhi, ylo, yhi

def p07_exact ( ):

#*****************************************************************************80
#
## p07_exact() returns the exact integral for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 8.0 / 15.0

  return exact

def p07_fun ( x, y ):

#*****************************************************************************80
#
## p07_fun() evaluates the integrand for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gwynne Evans,
#    Practical Numerical Integration,
#    Wiley, 1993,
#    ISBN: 047193898X,
#    LC: QA299.3E93.
#
#  Input:
#
#    real x(*), y(*): the evaluation points.
#
#  Output:
#
#    real fx(*): the integrand values.
#
  import numpy as np

  fx = np.sqrt ( np.abs ( x - y ) )

  return fx

def p07_lim ( ):

#*****************************************************************************80
#
## p07_lim() returns the integration limits for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real xlo, xhi, ylo, yhi: the limits of integration.
#
  xlo =  0.0
  xhi = +1.0
  ylo =  0.0
  yhi = +1.0

  return xlo, xhi, ylo, yhi

def p08_exact ( ):

#*****************************************************************************80
#
## p08_exact() returns the exact integral for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  from math import erf
  import numpy as np

  exact = 0.25 * np.pi * ( erf ( 1.0 ) + erf ( 4.0 ) )**2

  return exact

def p08_fun ( x, y ):

#*****************************************************************************80
#
## p08_fun() evaluates the integrand for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x(*), y(*): the evaluation points.
#
#  Output:
#
#    real fx(*): the integrand values.
#
  import numpy as np

  fx = np.exp ( - ( ( x - 4.0 )**2 + ( y - 1.0 )**2 ) )

  return fx

def p08_lim ( ):

#*****************************************************************************80
#
## p08_lim() returns the integration limits for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real xlo, xhi, ylo, yhi: the limits of integration.
#
  xlo = 0.0
  xhi = 5.0
  ylo = 0.0
  yhi = 5.0

  return xlo, xhi, ylo, yhi

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
  test_int_2d_test ( )
  timestamp ( )

