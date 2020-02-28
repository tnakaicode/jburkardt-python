#! /usr/bin/env python3
#
def p00_ab ( problem, m ):

#*****************************************************************************80
#
## P00_AB evaluates the limits of the optimization region for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer PROBLEM, the problem number.
#
#    Input, integer M, the number of variables.
#
#    Output, real A(M), B(M), the lower and upper bounds.
#
  if ( problem == 1 ):
    a, b = p01_ab ( m )
  elif ( problem == 2 ):
    a, b = p02_ab ( m )
  elif ( problem == 3 ):
    a, b = p03_ab ( m )
  elif ( problem == 4 ):
    a, b = p04_ab ( m )
  elif ( problem == 5 ):
    a, b = p05_ab ( m )
  elif ( problem == 6 ):
    a, b = p06_ab ( m )
  elif ( problem == 7 ):
    a, b = p07_ab ( m )
  elif ( problem == 8 ):
    a, b = p08_ab ( m )
  elif ( problem == 9 ):
    a, b = p09_ab ( m )
  elif ( problem == 10 ):
    a, b = p10_ab ( m )
  elif ( problem == 11 ):
    a, b = p11_ab ( m )
  elif ( problem == 12 ):
    a, b = p12_ab ( m )
  else:
    print ( '' )
    print ( 'P00_AB - Fatal error!' )
    print ( '  Illegal value of PROBLEM =  %d' % ( problem ) )
    exit ( 'P00_AB - Fatal error!' )

  return a, b

def p00_compass_search ( problem, m, x0, delta_tol, delta_init, k_max ):

#*****************************************************************************80
#
## P00_COMPASS_SEARCH carries out a direct search minimization algorithm.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Tamara Kolda, Robert Michael Lewis, Virginia Torczon,
#    Optimization by Direct Search: New Perspectives on Some Classical
#    and Modern Methods,
#    SIAM Review,
#    Volume 45, Number 3, 2003, pages 385-482.
#
#  Parameters:
#
#    Input, integer PROBLEM, the problem number.
#
#    Input, integer M, the number of variables.
#
#    Input, real X0(M), a starting estimate for the minimizer.
#
#    Input, real DELTA_TOL, the smallest step size that is allowed.
#
#    Input, real DELTA_INIT, the starting stepsize.
#
#    Input, integer K_MAX, the maximum number of steps allowed.
#
#    Output, real X(M), the estimated minimizer.
#
#    Output, real FX, the function value at X.
#
#    Output, integer K, the number of steps taken.
#
  from sys import exit

  n = 1
  k = 0
  x = x0.copy ( )
  fx = p00_f ( problem, m, n, x )

  if ( delta_tol <= 0.0 ):
    print ( '' )
    print ( 'P00_COMPASS_SEARCH - Fatal error!' )
    print ( '  DELTA_TOL <= 0.0.' )
    print ( '  DELTA_TOL = %g' % ( delta_tol ) )
    exit ( 'P00_COMPASS_SEARCH - Fatal error!' )

  if ( delta_init <= delta_tol ):
    print ( '' )
    print ( 'P00_COMPASS_SEARCH - Fatal error!' )
    print ( '  DELTA_INIT < DELTA_TOL.' )
    print ( '  DELTA_INIT = %g' % ( delta_init ) )
    print ( '  DELTA_TOL = %g' % ( delta_tol ) )
    exit ( 'P00_COMPASS_SEARCH - Fatal error!' )

  delta = delta_init

  while ( k < k_max ):

    k = k + 1
#
#  For each coordinate direction I, seek a lower function value
#  by increasing or decreasing X[i] by DELTA.
#
    decrease = False
    s = + 1.0
    i = 0

    for ii in range ( 0, 2 * m ):

      xd = x.copy ( )
      xd[i] = xd[i] + s * delta
      fxd = p00_f ( problem, m, n, xd )
#
#  As soon as a decrease is noticed, accept the new point.
#
      if ( fxd[0] < fx[0] ):
        x = xd.copy ( )
        fx[0] = fxd[0]
        decrease = True
        break

      s = - s

      if ( s == + 1.0 ):
        i = i + 1
#
#  If no decrease occurred, reduce DELTA.
#
    if ( not decrease ):

      delta = delta / 2.0

      if ( delta < delta_tol ):
        break

  return x, fx, k

def p00_f ( problem, m, n, x ):

#*****************************************************************************80
#
## P00_F evaluates the objective function for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer PROBLEM, the problem number.
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of arguments.
#
#    Input, real X(M,N), the argument of the objective function.
#
#    Output, real F(N), the objective function evaluated at
#    each argument.
#
  x.shape = ( m, n )

  if ( problem == 1 ):
    f = p01_f ( m, n, x )
  elif ( problem == 2 ):
    f = p02_f ( m, n, x )
  elif ( problem == 3 ):
    f = p03_f ( m, n, x )
  elif ( problem == 4 ):
    f = p04_f ( m, n, x )
  elif ( problem == 5 ):
    f = p05_f ( m, n, x )
  elif ( problem == 6 ):
    f = p06_f ( m, n, x )
  elif ( problem == 7 ):
    f = p07_f ( m, n, x )
  elif ( problem == 8 ):
    f = p08_f ( m, n, x )
  elif ( problem == 9 ):
    f = p09_f ( m, n, x )
  elif ( problem == 10 ):
    f = p10_f ( m, n, x )
  elif ( problem == 11 ):
    f = p11_f ( m, n, x )
  elif ( problem == 12 ):
    f = p12_f ( m, n, x )
  else:
    print ( '' )
    print ( 'P00_F - Fatal error!' )
    print ( '  Illegal value of PROBLEM =  %d', problem )
    exit ( 'P00_F - Fatal error!' )

  return f

def p00_problem_num ( ):

#*****************************************************************************80
#
## P00_PROBLEM_NUM returns the number of problems available.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#   Output, integer PROBLEM_NUM, the number of problems available.
#
  problem_num = 12

  return problem_num

def p00_sol ( problem, m, know ):

#*****************************************************************************80
#
## P00_SOL returns the solution for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROBLEM, the problem number.
#
#    Input, integer M, the spatial dimension.
#
#    Input/output, integer KNOW.
#    On input, KNOW is 0, or the index of the previously returned solution.
#    On output, KNOW is 0 if there are no more solutions, or it is the
#    index of the next solution.
#
#    Output, real X(M), the solution, if known.
#
  if ( problem == 1 ):
    know, x = p01_sol ( m, know )
  elif ( problem == 2 ):
    know, x = p02_sol ( m, know )
  elif ( problem == 3 ):
    know, x = p03_sol ( m, know )
  elif ( problem == 4 ):
    know, x = p04_sol ( m, know )
  elif ( problem == 5 ):
    know, x = p05_sol ( m, know )
  elif ( problem == 6 ):
    know, x = p06_sol ( m, know )
  elif ( problem == 7 ):
    know, x = p07_sol ( m, know )
  elif ( problem == 8 ):
    know, x = p08_sol ( m, know )
  elif ( problem == 9 ):
    know, x = p09_sol ( m, know )
  elif ( problem == 10 ):
    know, x = p10_sol ( m, know )
  elif ( problem == 11 ):
    know, x = p11_sol ( m, know )
  elif ( problem == 12 ):
    know, x = p12_sol ( m, know )
  else:
    print ( 'x' )
    print ( 'P00_SOL - Fatal error!' )
    print ( '  Illegal value of PROBLEM =  %d', problem )
    exit ( 'P00_SOL - Fatal error!' )

  return know, x

def p00_title ( problem ):

#*****************************************************************************80
#
## P00_TITLE returns a title for any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROBLEM, the number of the problem.
#
#    Output, string TITLE, a title for the problem.
#
  from sys import exit

  if ( problem == 1 ):
    title = p01_title ( )
  elif ( problem == 2 ):
    title = p02_title ( )
  elif ( problem == 3 ):
    title = p03_title ( )
  elif ( problem == 4 ):
    title = p04_title ( )
  elif ( problem == 5 ):
    title = p05_title ( )
  elif ( problem == 6 ):
    title = p06_title ( )
  elif ( problem == 7 ):
    title = p07_title ( )
  elif ( problem == 8 ):
    title = p08_title ( )
  elif ( problem == 9 ):
    title = p09_title ( )
  elif ( problem == 10 ):
    title = p10_title ( )
  elif ( problem == 11 ):
    title = p11_title ( )
  elif ( problem == 12 ):
    title = p12_title ( )
  else:
    print ( '' )
    print ( 'P00_TITLE - Fatal error!' )
    print ( '  Illegal value of PROBLEM = %d' % ( problem ) )
    exit ( 'P00_TITLE - Fatal error!' )

  return title

def p01_ab ( m ):

#*****************************************************************************80
#
## P01_AB evaluates the limits of the optimization region for problem 01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real A(M), B(M), the lower and upper bounds.
#
  import numpy as np

  a = - 5.0 * np.ones ( m )
  b = + 5.0 * np.ones ( m )

  return a, b

def p01_f ( m, n, x ):

#*****************************************************************************80
#
## P01_F evaluates the objective function for problem 01.
#
#  Discussion:
#
#    The function is continuous, convex, and unimodal.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hugues Bersini, Marco Dorigo, Stefan Langerman, Gregory Seront,
#    Luca Gambardella,
#    Results of the first international contest on evolutionary optimisation,
#    In Proceedings of 1996 IEEE International Conference on Evolutionary
#    Computation,
#    IEEE Press, pages 611-615, 1996.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of arguments.
#
#    Input, real X(M,N), the arguments.
#
#    Output, real F(N), the function evaluated at the arguments.
#
  import numpy as np

  f = np.zeros ( n )

  for j in range ( 0, n ):
    f[j] = np.sum ( ( x[0:m,j] - 1.0 ) ** 2 )

  return f

def p01_sol ( m, know ):

#*****************************************************************************80
#
## P01_SOL returns the solution for problem 01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input/output, integer KNOW.
#    On input, KNOW is 0, or the index of the previously returned solution.
#    On output, KNOW is 0 if there are no more solutions, or it is the
#    index of the next solution.
#
#    Output, real X(M,1), the solution, if known.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.ones ( m )
  else:
    know = 0
    x = np.zeros ( m )

  return know, x

def p01_title ( ):

#*****************************************************************************80
#
## P01_TITLE returns a title for problem 01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, a title for the problem.
#
  title = 'The sphere model.'

  return title

def p02_ab ( m ):

#*****************************************************************************80
#
## P02_AB evaluates the limits of the optimization region for problem 02.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real A(M), B(M), the lower and upper bounds.
#
  import numpy as np

  a = - 5.12 * np.ones ( m )
  b = + 5.12 * np.ones ( m )

  return a, b

def p02_f ( m, n, x ):

#*****************************************************************************80
#
## P02_F evaluates the objective function for problem 02.
#
#  Discussion:
#
#    This function is also known as the weighted sphere model.
#
#    The function is continuous, convex, and unimodal.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of arguments.
#
#    Input, real X(M,N), the arguments.
#
#    Output, real F(N), the function evaluated at the arguments.
#
  import numpy as np

  f = np.zeros ( n )

  y = r8vec_indicator1 ( m )

  for j in range ( 0, n ):
    f[j] = np.sum ( y[0:m] * x[0:m,j] ** 2 )

  return f

def p02_sol ( m, know ):

#*****************************************************************************80
#
## P02_SOL returns the solution for problem 02.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input/output, integer KNOW.
#    On input, KNOW is 0, or the index of the previously returned solution.
#    On output, KNOW is 0 if there are no more solutions, or it is the
#    index of the next solution.
#
#    Output, real X(M), the solution, if known.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.zeros ( m )
  else:
    know = 0
    x = np.zeros ( m )

  return know, x

def p02_title ( ):

#*****************************************************************************80
#
## P02_TITLE returns a title for problem 02.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, a title for the problem.
#
  title = 'The axis-parallel hyper-ellipsoid function.'

  return title

def p03_ab ( m ):

#*****************************************************************************80
#
## P03_AB evaluates the limits of the optimization region for problem 03.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real A(M), B(M), the lower and upper bounds.
#
  import numpy as np

  a = - 65.536 * np.ones ( m )
  b = + 65.536 * np.ones ( m )

  return a, b

def p03_f ( m, n, x ):

#*****************************************************************************80
#
## P03_F evaluates the objective function for problem 03.
#
#  Discussion:
#
#    This function is also known as the weighted sphere model.
#
#    The function is continuous, convex, and unimodal.
#
#     There is a typographical error in Molga and Smutnicki, so that the
#     formula for this function is given incorrectly.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of arguments.
#
#    Input, real X(M,N), the arguments.
#
#    Output, real F(N), the function evaluated at the arguments.
#
  import numpy as np

  f = np.zeros ( n )

  for j in range ( 0, n ):

    x_sum = 0.0

    for i in range ( 0, m ):
      x_sum = x_sum + x[i,j]
      f[j] = f[j] + x_sum ** 2

  return f

def p03_sol ( m, know ):

#*****************************************************************************80
#
## P03_SOL returns the solution for problem 03.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input/output, integer KNOW.
#    On input, KNOW is 0, or the index of the previously returned solution.
#    On output, KNOW is 0 if there are no more solutions, or it is the
#    index of the next solution.
#
#    Output, real X(M), the solution, if known.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.zeros ( m )
  else:
    know = 0
    x = np.zeros ( m )

  return know, x

def p03_title ( ):

#*****************************************************************************80
#
## P03_TITLE returns a title for problem 03.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, a title for the problem.
#
  title = 'The rotated hyper-ellipsoid function.'

  return title

def p04_ab ( m ):

#*****************************************************************************80
#
## P04_AB evaluates the limits of the optimization region for problem 04.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real A(M), B(M), the lower and upper bounds.
#
  import numpy as np

  a = - 2.048 * np.ones ( m )
  b = + 2.048 * np.ones ( m )

  return a, b

def p04_f ( m, n, x ):

#*****************************************************************************80
#
## P04_F evaluates the objective function for problem 04.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Howard Rosenbrock,
#    An Automatic Method for Finding the Greatest or Least Value of a Function,
#    Computer Journal,
#    Volume 3, 1960, pages 175-184.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of arguments.
#
#    Input, real X(M,N), the arguments.
#
#    Output, real F(N), the function evaluated at the arguments.
#
  import numpy as np

  f = np.zeros ( n )

  for j in range ( 0, n ):
    f[j] = np.sum ( ( 1.0 - x[0:m,j] ) ** 2 ) \
         + np.sum ( ( x[1:m,j] - x[0:m-1,j] ) ** 2 )

  return f

def p04_sol ( m, know ):

#*****************************************************************************80
#
## P04_SOL returns the solution for problem 04.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input/output, integer KNOW.
#    On input, KNOW is 0, or the index of the previously returned solution.
#    On output, KNOW is 0 if there are no more solutions, or it is the
#    index of the next solution.
#
#    Output, real X(M), the solution, if known.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.ones ( m )
  else:
    know = 0
    x = np.zeros ( m )

  return know, x

def p04_title ( ):

#*****************************************************************************80
#
## P04_TITLE returns a title for problem 04.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, a title for the problem.
#
  title = 'Rosenbrock\'s valley.'

  return title

def p05_ab ( m ):

#*****************************************************************************80
#
## P05_AB evaluates the limits of the optimization region for problem 05.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real A(M), B(M), the lower and upper bounds.
#
  import numpy as np

  a = - 5.12 * np.ones ( m )
  b = + 5.12 * np.ones ( m )

  return a, b

def p05_f ( m, n, x ):

#*****************************************************************************80
#
## P05_F evaluates the objective function for problem 05.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of arguments.
#
#    Input, real X(M,N), the arguments.
#
#    Output, real F(N), the function evaluated at the arguments.
#
  import numpy as np

  f = np.zeros ( n )

  for j in range ( 0, n ):

    f[j] = 10.0 * float ( m )

    for i in range ( 0, m ):
      f[j] = f[j] + x[i,j] ** 2 - 10.0 * np.cos ( 2.0 * np.pi * x[i,j] )

  return f

def p05_sol ( m, know ):

#*****************************************************************************80
#
## P05_SOL returns the solution for problem 05.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input/output, integer KNOW.
#    On input, KNOW is 0, or the index of the previously returned solution.
#    On output, KNOW is 0 if there are no more solutions, or it is the
#    index of the next solution.
#
#    Output, real X(M), the solution, if known.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.zeros ( m )
  else:
    know = 0
    x = np.zeros ( m )

  return know, x

def p05_title ( ):

#*****************************************************************************80
#
## P05_TITLE returns a title for problem 05.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, a title for the problem.
#
  title = 'Rastrigin\'s function.'

  return title

def p06_ab ( m ):

#*****************************************************************************80
#
## P06_AB evaluates the limits of the optimization region for problem 06.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real A(M), B(M), the lower and upper bounds.
#
  import numpy as np

  a = - 500.0 * np.ones ( m )
  b = + 500.0 * np.ones ( m )

  return a, b

def p06_f ( m, n, x ):

#*****************************************************************************80
#
## P06_F evaluates the objective function for problem 06.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hans-Paul Schwefel,
#    Numerical optimization of computer models,
#    Wiley, 1981,
#    ISBN13: 978-0471099888,
#    LC: QA402.5.S3813.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of arguments.
#
#    Input, real X(M,N), the arguments.
#
#    Output, real F(N), the function evaluated at the arguments.
#
  import numpy as np

  f = np.zeros ( n )

  for j in range ( 0, n ):
    f[j] = - np.sum ( x[0:m,j] * np.sin ( np.sqrt ( abs ( x[0:m,j] ) ) ) )

  return f

def p06_sol ( m, know ):

#*****************************************************************************80
#
## P06_SOL returns the solution for problem 06.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input/output, integer KNOW.
#    On input, KNOW is 0, or the index of the previously returned solution.
#    On output, KNOW is 0 if there are no more solutions, or it is the
#    index of the next solution.
#
#    Output, real X(M), the solution, if known.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = 420.9687 * np.ones ( m )
  else:
    know = 0
    x = np.zeros ( m )

  return know, x

def p06_title ( ):

#*****************************************************************************80
#
## P06_TITLE returns a title for problem 06.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, a title for the problem.
#
  title = 'Schwefel\'s function.'

  return title

def p07_ab ( m ):

#*****************************************************************************80
#
## P07_AB evaluates the limits of the optimization region for problem 07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real A(M), B(M), the lower and upper bounds.
#
  import numpy as np

  a = - 600.0 * np.ones ( m )
  b = + 600.0 * np.ones ( m )

  return a, b

def p07_f ( m, n, x ):

#*****************************************************************************80
#
## P07_F evaluates the objective function for problem 07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of arguments.
#
#    Input, real X(M,N), the arguments.
#
#    Output, real F(N), the function evaluated at the arguments.
#
  import numpy as np

  f = np.zeros ( n )
  y = r8vec_indicator1 ( m )
  y[0:m] = np.sqrt ( y[0:m] )

  for j in range ( 0, n ):
    f[j] = np.sum ( x[0:m,j] ** 2 ) / 4000.0 \
      - np.prod ( np.cos ( x[0:m,j] / y[0:m] ) ) + 1.0

  return f

def p07_sol ( m, know ):

#*****************************************************************************80
#
## P07_SOL returns the solution for problem 07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input/output, integer KNOW.
#    On input, KNOW is 0, or the index of the previously returned solution.
#    On output, KNOW is 0 if there are no more solutions, or it is the
#    index of the next solution.
#
#    Output, real X(M), the solution, if known.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.zeros ( m )
  else:
    know = 0
    x = np.zeros ( m )

  return know, x

def p07_title ( ):

#*****************************************************************************80
#
## P07_TITLE returns a title for problem 07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, a title for the problem.
#
  title = 'Griewank\'s function.'

  return title

def p08_ab ( m ):

#*****************************************************************************80
#
## P08_AB evaluates the limits of the optimization region for problem 08.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real A(M), B(M), the lower and upper bounds.
#
  import numpy as np

  a = - 1.0 * np.ones ( m )
  b = + 1.0 * np.ones ( m )

  return a, b

def p08_f ( m, n, x ):

#*****************************************************************************80
#
## P08_F evaluates the objective function for problem 08.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of arguments.
#
#    Input, real X(M,N), the arguments.
#
#    Output, real F(N), the function evaluated at the arguments.
#
  import numpy as np

  f = np.zeros ( n )

  y = r8vec_indicator1 ( m )
  y[0:m] = y[0:m] + 1.0

  for j in range ( 0, n ):
    f[j] = np.sum ( abs ( x[0:m,j] ) ** y[0:m] )

  return f

def p08_sol ( m, know ):

#*****************************************************************************80
#
## P08_SOL returns the solution for problem 08.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input/output, integer KNOW.
#    On input, KNOW is 0, or the index of the previously returned solution.
#    On output, KNOW is 0 if there are no more solutions, or it is the
#    index of the next solution.
#
#    Output, real X(M), the solution, if known.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.zeros ( m )
  else:
    know = 0
    x = np.zeros ( m )

  return know, x

def p08_title ( ):

#*****************************************************************************80
#
## P08_TITLE returns a title for problem 08.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, a title for the problem.
#
  title = 'The power sum function.'

  return title

def p09_ab ( m ):

#*****************************************************************************80
#
## P09_AB evaluates the limits of the optimization region for problem 09.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real A(M), B(M), the lower and upper bounds.
#
  import numpy as np

  a = - 32.768 * np.ones ( m )
  b = + 32.768 * np.ones ( m )

  return a, b

def p09_f ( m, n, x ):

#*****************************************************************************80
#
## P09_F evaluates the objective function for problem 09.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of arguments.
#
#    Input, real X(M,N), the arguments.
#
#    Output, real F(N), the function evaluated at the arguments.
#
  import numpy as np

  f = np.zeros ( n )

  a = 20.0
  b = 0.2
  c = 0.2

  for j in range ( 0, n ):
    f[j] = - a * np.exp ( - b * np.sqrt ( np.sum ( x[0:m,j] ** 2 ) / float ( m ) ) ) \
      - np.exp ( np.sum ( np.cos ( c * np.pi * x[0:m,j] ) ) / float ( m ) ) \
      + a + np.exp ( 1.0 )

  return f

def p09_sol ( m, know ):

#*****************************************************************************80
#
## P09_SOL returns the solution for problem 09.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input/output, integer KNOW.
#    On input, KNOW is 0, or the index of the previously returned solution.
#    On output, KNOW is 0 if there are no more solutions, or it is the
#    index of the next solution.
#
#    Output, real X(M), the solution, if known.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.zeros ( m )
  else:
    know = 0
    x = np.zeros ( m )

  return know, x

def p09_title ( ):

#*****************************************************************************80
#
## P09_TITLE returns a title for problem 09.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, a title for the problem.
#
  title = 'Ackley\'s function.'

  return title

def p10_ab ( m ):

#*****************************************************************************80
#
## P10_AB evaluates the limits of the optimization region for problem 10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real A(M), B(M), the lower and upper bounds.
#
  import numpy as np

  a = np.zeros ( m )
  b = np.pi * np.ones ( m )

  return a, b

def p10_f ( m, n, x ):

#*****************************************************************************80
#
## P10_F evaluates the objective function for problem 10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of arguments.
#
#    Input, real X(M,N), the arguments.
#
#    Output, real F(N), the function evaluated at the arguments.
#
  import numpy as np

  f = np.zeros ( n )

  p = 10

  y = r8vec_indicator1 ( m )

  for j in range ( 0, n ):
    f[j] = - np.sum ( \
      np.sin ( x[0:m,j] ) \
      * ( np.sin ( x[0:m,j] ** 2 * y[0:m] / np.pi ) ) ** ( 2 * p ) \
    )

  return f

def p10_sol ( m, know ):

#*****************************************************************************80
#
## P10_SOL returns the solution for problem 10.
#
#  Discussion:
#
#    The minimum value is - 0.966 * M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input/output, integer KNOW.
#    On input, KNOW is 0, or the index of the previously returned solution.
#    On output, KNOW is 0 if there are no more solutions, or it is the
#    index of the next solution.
#
#    Output, real X(M), the solution, if known.
#
  import numpy as np

  know = 0
  x = np.zeros ( m )

  return know, x

def p10_title ( ):

#*****************************************************************************80
#
## P10_TITLE returns a title for problem 10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, a title for the problem.
#
  title = 'Michalewicz\'s function.'

  return title

def p11_ab ( m ):

#*****************************************************************************80
#
## P11_AB evaluates the limits of the optimization region for problem 11.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real A(M), B(M), the lower and upper bounds.
#
  import numpy as np

  a = - 5.12 * np.ones ( m )
  b = + 5.12 * np.ones ( m )

  return a, b

def p11_f ( m, n, x ):

#*****************************************************************************80
#
## P11_F evaluates the objective function for problem 11.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of arguments.
#
#    Input, real X(M,N), the arguments.
#
#    Output, real F(N), the function evaluated at the arguments.
#
  import numpy as np

  f = np.zeros ( n )

  for j in range ( 0, n ):

    rsq = np.sum ( x[0:m,j] ** 2 )

    f[j] = - ( 1.0 + np.cos ( 12.0 * np.sqrt ( rsq ) ) ) / ( 0.5 * rsq + 2.0 )

  return f

def p11_sol ( m, know ):

#*****************************************************************************80
#
## P11_SOL returns the solution for problem 11.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input/output, integer KNOW.
#    On input, KNOW is 0, or the index of the previously returned solution.
#    On output, KNOW is 0 if there are no more solutions, or it is the
#    index of the next solution.
#
#    Output, real X(M), the solution, if known.
#
  import numpy as np

  if ( know == 0 ):
    x = np.zeros ( m )
    know = 1
  else:
    know = 0
    x = np.zeros ( m )

  return know, x

def p11_title ( ):

#*****************************************************************************80
#
## P11_TITLE returns a title for problem 11.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, a title for the problem.
#
  title = 'Drop wave function.'

  return title

def p12_ab ( m ):

#*****************************************************************************80
#
## P12_AB evaluates the limits of the optimization region for problem 12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real A(M), B(M), the lower and upper bounds.
#
  import numpy as np

  a = 0.0 * np.ones ( m )
  b = 1.0 * np.ones ( m )

  return a, b

def p12_f ( m, n, x ):

#*****************************************************************************80
#
## P12_F evaluates the objective function for problem 12.
#
#  Discussion:
#
#    In dimension I, the function is a piecewise linear function with
#    local minima at 0 and 1.0, and a global minimum at ALPHA[i] = I/(M+1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Marcin Molga, Czeslaw Smutnicki,
#    Test functions for optimization needs.
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of arguments.
#
#    Input, real X(M,N), the arguments.
#
#    Output, real F(N), the function evaluated at the arguments.
#
  import numpy as np

  f = np.zeros ( n )

  beta = 2.0
#
#  I'm just choosing ALPHA in [0,1] arbitrarily.
#
  alpha = np.zeros ( m )
  for i in range ( 0, m ):
    alpha[i] = float ( i + 1 ) / float ( m + 1 )

  for j in range ( 0, n ):

    for i in range ( 0, m ):

      if ( x[i,j] <= 0.0 ):
        g = x[i,j]
      elif ( x[i,j] <= 0.8 * alpha[i] ):
        g = 0.8 - x[i,j] / alpha[i]
      elif ( x[i,j] <= alpha[i] ):
        g = 5.0 * x[i,j] / alpha[i] - 4.0
      elif ( x[i,j] <= ( 1.0 + 4.0 * alpha[i] ) / 5.0 ):
        g = 1.0 + 5.0 * ( x[i,j] - alpha[i] ) / ( alpha[i] - 1.0 )
      elif ( x[i,j] <= 1.0 ):
        g = 0.8 + ( x[i,j] - 1.0 ) / ( 1.0 - alpha[i] )
      else:
        g = x[i,j] - 1.0

      f[j] = f[j] + g

    f[j] = f[j] / float ( m )
    f[j] = - ( f[j] ** beta )

  return f

def p12_sol ( m, know ):

#*****************************************************************************80
#
## P12_SOL returns the solution for problem 12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input/output, integer KNOW.
#    On input, KNOW is 0, or the index of the previously returned solution.
#    On output, KNOW is 0 if there are no more solutions, or it is the
#    index of the next solution.
#
#    Output, real X(M), the solution, if known.
#
  import numpy as np

  alpha = np.zeros ( m )
  for i in range ( 0, m ):
    alpha[i] = float ( i +1 ) / float ( m + 1 )

  if ( know == 0 ):
    know = 1
    x = alpha.copy ( )
  else:
    know = 0
    x = np.zeros ( m )
 
  return know, x

def p12_title ( ):

#*****************************************************************************80
#
## P12_TITLE returns a title for problem 12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, a title for the problem.
#
  title = 'The deceptive function.'

  return title

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_PRINT prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  from r8mat_print_some import r8mat_print_some

  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_TEST tests R8MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ' ),

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ) ),

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ) ),

      print ( '' )

  return

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT_SOME prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8col_uniform_abvec ( m, n, a, b, seed ):

#*****************************************************************************80
#
## R8COL_UNIFORM_ABVEC fills an R8COL with scaled pseudorandom numbers.
#
#  Discussion:
#
#    An R8COL is an array of R8 values, regarded as a set of column vectors.
#
#    The user specifies a minimum and maximum value for each row.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Springer Verlag, pages 201-202, 1983.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, pages 362-376, 1986.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, pages 136-143, 1969.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in
#    the array.
#
#    Input, real A(M), B(M), the lower and upper limits.
#
#    Input/output, integer SEED, the "seed" value, which
#    should NOT be 0.  On output, SEED has been updated.
#
#    Output, real R(M,N), the array of pseudorandom values.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8COL_UNIFORM_ABVEC - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8COL_UNIFORM_ABVEC - Fatal error!' )

  r = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):

    for j in range ( 0, n ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge;

      r[i,j] = a[i] + ( b[i] - a[i] ) * seed * 4.656612875E-10

  return r, seed

def r8col_uniform_abvec_test ( ):

#*****************************************************************************80
#
## R8COL_UNIFORM_ABVEC_TEST tests R8COL_UNIFORM_ABVEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  m = 5
  n = 4
  a = np.array ( ( -1.0, 0.0, 50.0, 100.0, 17.0 ) )
  b = np.array ( ( +1.0, 1.0, 55.0, 100.1, 20.0 ) )

  seed = 123456789

  print ( '' )
  print ( 'R8COL_UNIFORM_ABVEC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8COL_UNIFORM_ABVEC computes a random scaled R8COL.' )
  print ( '' )
  print ( '   Col         Min         Max' )
  print ( '' )

  for i in range ( 0, m ):
    print ( '  %4d  %10g  %10g' % ( i, a[i], b[i] ) )

  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8col_uniform_abvec ( m, n, a, b, seed )

  r8mat_print ( m, n, v, '  Random R8COL:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8COL_UNIFORM_ABVEC_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## R8VEC_INDICATOR1 sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements of the vector.
#
#    Output, real A(N), the indicator array.
#
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## R8VEC_INDICATOR1_TEST tests R8VEC_INDICATOR1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'R8VEC_INDICATOR1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_INDICATOR1 returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_INDICATOR1_TEST' )
  print ( '  Normal end of execution.' )
  return

def test_optimization_test01 ( ):

#*****************************************************************************80
#
## TEST_OPTIMIZATION_TEST01 simply prints the title of each problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'TEST_OPTIMIZATION_TEST01' )
  print ( '  For each problem, print the title.' )
#
#  Get the number of problems.
#
  problem_num = p00_problem_num ( )

  print ( '' )
  print ( '  Problem  Title' )
  print ( '' )

  for problem in range ( 1, problem_num + 1 ):

    title = p00_title ( problem )

    print ( '  %7d  %s' % ( problem, title ) )

  return

def test_optimization_test02 ( ):

#*****************************************************************************80
#
## TEST_OPTIMIZATION_TEST02 samples the function at 1,000 points and prints the minimum.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
  m = 2
  n = 1000

  print ( '' )
  print ( 'TEST_OPTIMIZATION_TEST02' )
  print ( '  For each problem, using dimension M = 2' )
  print ( '  sample the function at N = 1000 points,' )
  print ( '  and print the minimum and maximum.' )

  seed = 123456789
#
#  Get the number of problems.
#
  problem_num = p00_problem_num ( )

  print ( '' )
  print ( '  Problem     Minimum  Sample Minimum  Sample Maximum' )
  print ( '' )

  for problem in range ( 1, problem_num + 1 ):

    know = 0
    know, x = p00_sol ( problem, m, know )

    if ( know != 0 ):
      f = p00_f ( problem, m, 1, x )
      f_min = f[0]

    a, b = p00_ab ( problem, m )
    x, seed = r8col_uniform_abvec ( m, n, a, b, seed )
    f = p00_f ( problem, m, n, x )

    if ( know != 0 ):
      print ( '  %7d  %14g  %14g  %14g' \
        % ( problem, f_min, min ( f[0:n] ), max ( f[0:n] ) ) )
    else:
      print ( '  %7d                  %14g  %14g' \
        % ( problem,         min ( f[0:n] ), max ( f[0:n] ) ) )
  return

def test_optimization_test03 ( ):

#*****************************************************************************80
#
## TEST_OPTIMIZATION_TEST03 tries Compass Search on each problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 2
  n = 1000
  delta_tol = 0.000001
  k_max = 20000

  print ( '' )
  print ( 'TEST_OPTIMIZATION_TEST03' )
  print ( '  For each problem, using dimension M = 2' )
  print ( '  try compass search.' )
#
#  Get the number of problems.
#
  problem_num = p00_problem_num ( )

  for problem in range ( 1, problem_num + 1 ):

    seed = 123456789

    a, b = p00_ab ( problem, m )
    x0, seed = r8col_uniform_abvec ( m, 1, a, b, seed )
    fx = p00_f ( problem, m, 1, x0 )
    delta_init = 0.3 * np.linalg.norm ( x0 ) / float ( m )
    delta_init = max ( delta_init, 1000.0 * delta_tol )
    print ( '' )
    print ( '  Problem %2d  DELTA_INIT = %14g' % ( problem, delta_init ) )
    print ( '  Initial:  %14g  %14g  %14g' % ( x0[0,0], x0[1,0], fx[0] ) )
    x, fx, k = p00_compass_search ( problem, m, x0, delta_tol, \
      delta_init, k_max )
    print ( '  Final:    %14g  %14g  %14g  Steps = %d' \
      % ( x[0,0], x[1,0], fx[0], k ) )

    know = 0
    while ( True ):
      know, x = p00_sol ( problem, m, know )
      if ( know == 0 ):
        break
      fx = p00_f ( problem, m, 1, x )
      print ( '  Exact:    %14g  %14g  %14g' % ( x[0,0], x[1,0], fx[0] ) )

  return

def test_optimization_test ( ):

#*****************************************************************************80
#
## TEST_OPTIMIZATION_TEST tests the TEST_OPTIMIZATION library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TEST_OPTIMIZATION_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the TEST_OPTIMIZATION library.' )

  test_optimization_test01 ( )
  test_optimization_test02 ( )
  test_optimization_test03 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TEST_OPTIMIZATION_TEST' )
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
  test_optimization_test ( )
  timestamp ( )

