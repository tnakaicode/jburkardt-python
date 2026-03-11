#! /usr/bin/env python3
#
def test_opt_con_test ( ):

#*****************************************************************************80
#
## test_opt_con_test() tests test_opt_con().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'test_opt_con_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test test_opt_con().' )

  test_opt_con_test01 ( )
  test_opt_con_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_opt_con_test():' )
  print ( '  Normal end of execution.' )

  return

def test_opt_con_test01 ( ):

#*****************************************************************************80
#
## test_opt_con_test01() simply prints the title of each problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'test_opt_con_test01():' )
  print ( '  For each problem, print the title.' )
#
#  Get the number of problems.
#
  problem_num = p00_problem_num ( )

  print ( '' )
  print ( '  Problem     Title' )
  print ( '' )

  for problem in range ( 1, problem_num + 1 ):

    title = p00_title ( problem )

    print ( '  %6d  %s' % ( problem, title ) )

  return

def test_opt_con_test02 ( ):

#*****************************************************************************80
#
## test_opt_con_test02() evaluates the objective function at each starting point.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  n = 100000

  print ( '' )
  print ( 'test_opt_con_test02():' )
  print ( '  For each problem, evaluate the function at many points.' )
  print ( '  Number of sample points = ', n )
#
#  Get the number of problems.
#
  problem_num = p00_problem_num ( )

  for problem in range ( 1, problem_num + 1 ):

    print ( '' )
    print ( '  Problem ', problem )

    title = p00_title ( problem )

    print ( '  "' + title + '"' )

    m = p00_m ( problem )

    print ( '  M =', m )
 
    a, b = p00_ab ( problem, m )

    print ( '' )
    print ( '    I      A(i)      B(i)' )
    print ( '' )

    for i in range ( 0, m ):
      print ( '  %4d  %10g  %10g' % ( i, a[i], b[i] ) )

    x = rng.random ( [ m, n ] )
    for i in range ( 0, m ):
      x[i,:] = a[i] * ( 1.0 - x[i,:] ) + b[i] * x[i,:]

    f = p00_f ( problem, m, n, x )

    print ( '' )
    print ( '  Max(F) = ', np.max ( f ) )
    print ( '  Min(F) = ', np.min ( f ) )

    know = 0
    xs, know = p00_sol ( problem, m, know )
    if ( know ):
      fs = p00_f ( problem, m, 1, xs )
      print ( '  F(X*)  = ', fs )
    else:
      print ( '  X* is not given.' )

  return

def p00_ab ( problem, m ):

#*****************************************************************************80
#
## p00_ab() returns bounds for a problem specified by index.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem index.
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real a[m], b[m], lower and upper bounds.
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
  else:
    print ( '' )
    print ( 'p00_ab(): Fatal error!' )
    print ( '  Problem index out of bounds.' )
    raise Exception ( 'p00_ab(): Fatal error!' )

  return a, b

def p00_f ( problem, m, n, x ):

#*****************************************************************************80
#
## p00_f() returns the objective function value for a problem specified by index.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem index.
#
#    integer M, the spatial dimension.
#
#    integer N, the number of arguments.
#
#    real X(M,N), the arguments.
#
#  Output:
#
#    real F(N), the function values.
#
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
  else:
    print ( '' )
    print ( 'p00_f(): Fatal error!' )
    print ( '  Problem index out of bounds.' )
    raise Exception ( 'p00_f(): Fatal error!' )

  return f

def p00_m ( problem ):

#*****************************************************************************80
#
## p00_m() returns the spatial dimension for a problem specified by index.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
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
#    integer M, the spatial dimension.
#
  if ( problem == 1 ):
    m = p01_m ( )
  elif ( problem == 2 ):
    m = p02_m ( )
  elif ( problem == 3 ):
    m = p03_m ( )
  elif ( problem == 4 ):
    m = p04_m ( )
  elif ( problem == 5 ):
    m = p05_m ( )
  elif ( problem == 6 ):
    m = p06_m ( )
  elif ( problem == 7 ):
    m = p07_m ( )
  elif ( problem == 8 ):
    m = p08_m ( )
  else:
    print ( '' )
    print ( 'p00_m(): Fatal error!' )
    print ( '  Problem index out of bounds.' )
    raise Exception ( 'p00_m(): Fatal error!' )

  return m

def p00_problem_num ( ):

#*****************************************************************************80
#
## p00_problem_num() returns the number of problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 January 2012
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer PROBLEM_NUM, the number of defined problems.
#
  problem_num = 8

  return problem_num

def p00_sol ( problem, m, know ):

#*****************************************************************************80
#
## p00_sol() returns known solutions for a problem specified by index.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem index.
#
#    integer M, the order of the problem.
#
#    integer KNOW, 0, or the index of the previously returned solution.
#
#  Output:
#
#    real x[m,1]: the solution.
#
#    integer KNOW, 0 if there are no more solutions, or it is the
#    index of the next solution.
#
  import numpy as np

  if ( problem == 1 ):
    x, know = p01_sol ( m, know )
  elif ( problem == 2 ):
    x, know = p02_sol ( m, know )
  elif ( problem == 3 ):
    x, know = p03_sol ( m, know )
  elif ( problem == 4 ):
    x, know = p04_sol ( m, know )
  elif ( problem == 5 ):
    x, know = p05_sol ( m, know )
  elif ( problem == 6 ):
    x, know = p06_sol ( m, know )
  elif ( problem == 7 ):
    x, know = p07_sol ( m, know )
  elif ( problem == 8 ):
    x, know = p08_sol ( m, know )
  else:
    print ( '' )
    print ( 'p00_sol(): Fatal error!' )
    print ( '  Problem index out of bounds.' )
    raise Exception ( 'p00_sol(): Fatal error!' )

  return x, know

def p00_title ( problem ):

#*****************************************************************************80
#
## p00_title() returns a title for a problem specified by index.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
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
#    string TITLE, a title for the problem.
#
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
  else:
    print ( '' )
    print ( 'p00_title(): Fatal error!' )
    print ( '  Problem index out of bounds.' )
    raise Exception ( 'p00_title(): Fatal error!' )

  return title

def p01_ab ( m ):

#*****************************************************************************80
#
## p01_ab() returns bounds for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real a[m], b[m], lower and upper bounds.
#
  import numpy as np

  a = np.zeros ( m )
  b = np.ones ( m )

  return a, b

def p01_f ( m, n, x ):

#*****************************************************************************80
#
## p01_f() returns the objective function value for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of arguments.
#
#    real X(M,N), the arguments.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = np.zeros ( n )

  for j in range ( 0, n ):
    p = np.prod ( x[:,j] )
    s = np.sum ( x[:,j] )
    f[j] = - np.exp ( p ) * np.sin ( s )

  return f

def p01_m ( ):

#*****************************************************************************80
#
## p01_m() returns the spatial dimension for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Output:
#
#    integer M, the spatial dimension.
#
  m = 4

  return m

def p01_sol ( m, know ):

#*****************************************************************************80
#
## p01_sol() returns known solutions for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the order of the problem.
#
#    integer KNOW, 0, or the index of the previously returned solution.
#
#  Output:
#
#    real x[m,1]: the solution.
#
#    integer KNOW, 0 if there are no more solutions, or it is the
#    index of the next solution.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.array ( [ \
      [ 0.409887209247642, \
      0.409887209247642, \
      0.409887209247642, \
      0.409887209247642 ] ] )
  else:
    know = 0
    x = np.zeros ( [ 1, m ] )
#
#  Currently, *SOL returns X as a [1,M] array, 
#  but the code assumes [M,1].
#  For now, simply transpose it here.
#  This is only a cheap and temporary solution.
#
  x = np.transpose ( x )

  return x, know

def p01_title ( ):

#*****************************************************************************80
#
## p01_title() returns a title for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'f(x) = - exp(prod(x)) * sin(sum(x)).'

  return title

def p02_ab ( m ):

#*****************************************************************************80
#
## p02_ab() returns bounds for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real a[m], b[m], lower and upper bounds.
#
  import numpy as np

  a = np.zeros ( m )
  b = np.ones ( m )

  return a, b

def p02_f ( m, n, x ):

#*****************************************************************************80
#
## p02_f() returns the objective function value for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of arguments.
#
#    real X(M,N), the arguments.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = np.zeros ( n )

  for j in range ( 0, n ):
    p = x[0,j] * x[1,j]**2 * x[2,j]**3 * x[3,j]**4
    s = np.sum ( x[:,j] )
    f[j] = - np.exp ( p ) * np.sin ( s )

  return f

def p02_m ( ):

#*****************************************************************************80
#
## p02_m() returns the spatial dimension for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Output:
#
#    integer M, the spatial dimension.
#
  m = 4

  return m

def p02_sol ( m, know ):

#*****************************************************************************80
#
## p02_sol() returns known solutions for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the order of the problem.
#
#    integer KNOW, 0, or the index of the previously returned solution.
#
#  Output:
#
#    real x[m,1]: the solution.
#
#    integer KNOW, 0 if there are no more solutions, or it is the
#    index of the next solution.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.array ( [ \
      [ 0.390500591228663, \
        0.392051909813608, \
        0.393601661544812, \
        0.395149843840982 ] ] )
  else:
    know = 0
    x = np.zeros ( [ 1, m ] )
#
#  Currently, *SOL returns X as a [1,M] array, 
#  but the code assumes [M,1].
#  For now, simply transpose it here.
#  This is only a cheap and temporary solution.
#
  x = np.transpose ( x )

  return x, know

def p02_title ( ):

#*****************************************************************************80
#
## p02_title() returns a title for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'f(x) = - exp(x(1)*x(2)^2*x(3)^3*x(4)^4) * sin(sum(x)).'

  return title

def p03_ab ( m ):

#*****************************************************************************80
#
## p03_ab() returns bounds for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real a[m], b[m], lower and upper bounds.
#
  import numpy as np

  a = np.zeros ( m )
  b = np.ones ( m )

  return a, b

def p03_f ( m, n, x ):

#*****************************************************************************80
#
## p03_f() returns the objective function value for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of arguments.
#
#    real X(M,N), the arguments.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = np.zeros ( n )

  for j in range ( 0, n ):
    s = - x[0,j] - 2.0 * x[1,j] - 3.0 * x[2,j] - 4.0 * x[3,j]
    f[j] = - 10000.0 * np.prod ( x[:,j] ) * np.exp ( s )

  return f

def p03_m ( ):

#*****************************************************************************80
#
## p03_m() returns the spatial dimension for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Output:
#
#    integer M, the spatial dimension.
#
  m = 4

  return m

def p03_sol ( m, know ):

#*****************************************************************************80
#
## p03_sol() returns known solutions for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the order of the problem.
#
#    integer KNOW, 0, or the index of the previously returned solution.
#
#  Output:
#
#    real x[m,1]: the solution.
#
#    integer KNOW, 0 if there are no more solutions, or it is the
#    index of the next solution.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.array ( [ \
     [ 0.999980569087140, \
       0.500000721280566, \
       0.333341891834645, \
       0.249997266604697 ] ] )
  else:
    know = 0
    x = np.zeros ( [ 1, m ] )
#
#  Currently, *SOL returns X as a [1,M] array, 
#  but the code assumes [M,1].
#  For now, simply transpose it here.
#  This is only a cheap and temporary solution.
#
  x = np.transpose ( x )

  return x, know

def p03_title ( ):

#*****************************************************************************80
#
## p03_title() returns a title for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'f(x) = -1000 * product(x) * exp(-x(1)-2x(2)-3x(3)-4x(4)).'

  return title

def p04_ab ( m ):

#*****************************************************************************80
#
## p04_ab() returns bounds for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real a[m], b[m], lower and upper bounds.
#
  import numpy as np

  a = np.zeros ( m )
  b = np.ones ( m )

  return a, b

def p04_f ( m, n, x ):

#*****************************************************************************80
#
## p04_f() returns the objective function value for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of arguments.
#
#    real X(M,N), the arguments.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = np.zeros ( n )

  for j in range ( 0, n ):
    f[j] = - 100.0 * np.prod ( x[:,j] ) * np.exp ( - x[3,j] ) \
      / ( 1.0 + x[0,j] * x[1,j] * x[2,j] )**2

  return f

def p04_m ( ):

#*****************************************************************************80
#
## p04_m() returns the spatial dimension for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Output:
#
#    integer M, the spatial dimension.
#
  m = 4

  return m

def p04_sol ( m, know ):

#*****************************************************************************80
#
## p04_sol() returns known solutions for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the order of the problem.
#
#    integer KNOW, 0, or the index of the previously returned solution.
#
#  Output:
#
#    real x[m,1]: the solution.
#
#    integer KNOW, 0 if there are no more solutions, or it is the
#    index of the next solution.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.ones ( [ 1, m ] )
  else:
    know = 0
    x = np.zeros ( [ 1, m ] )
#
#  Currently, *SOL returns X as a [1,M] array, 
#  but the code assumes [M,1].
#  For now, simply transpose it here.
#  This is only a cheap and temporary solution.
#
  x = np.transpose ( x )

  return x, know

def p04_title ( ):

#*****************************************************************************80
#
## p04_title() returns a title for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'f(x) = -100 * product(x) * exp(-x(4)) / (1+x(1)+x(2)+x(3)).'

  return title

def p05_ab ( m ):

#*****************************************************************************80
#
## p05_ab() returns bounds for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real a[m], b[m], lower and upper bounds.
#
  import numpy as np

  a = np.zeros ( m )
  b = np.ones ( m )

  return a, b

def p05_f ( m, n, x ):

#*****************************************************************************80
#
## p05_f() returns the objective function value for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of arguments.
#
#    real X(M,N), the arguments.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = np.zeros ( n )

  for j in range ( 0, n ):
    f[j] = ( x[0,j] -  3.0 / 11.0 )**2 \
         + ( x[1,j] -  6.0 / 13.0 )**2 \
         + ( x[2,j] - 12.0 / 23.0 )**4 \
         + ( x[3,j] -  8.0 / 37.0 )**6

  return f

def p05_m ( ):

#*****************************************************************************80
#
## p05_m() returns the spatial dimension for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Output:
#
#    integer M, the spatial dimension.
#
  m = 4

  return m

def p05_sol ( m, know ):

#*****************************************************************************80
#
## p05_sol() returns known solutions for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the order of the problem.
#
#    integer KNOW, 0, or the index of the previously returned solution.
#
#  Output:
#
#    real x[m,1]: the solution.
#
#    integer KNOW, 0 if there are no more solutions, or it is the
#    index of the next solution.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.array ( [ \
      [ 3.0 / 11.0, \
        6.0 / 13.0, \
       12.0 / 23.0, \
        8.0 / 37.0 ] ] )
  else:
    know = 0
    x = np.zeros ( [ 1, m ] )
#
#  Currently, *SOL returns X as a [1,M] array, 
#  but the code assumes [M,1].
#  For now, simply transpose it here.
#  This is only a cheap and temporary solution.
#
  x = np.transpose ( x )

  return x, know

def p05_title ( ):

#*****************************************************************************80
#
## p05_title() returns a title for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'f(x) = (x(1)-3/11)^2+(x(2)-6/13)^2+(x(3)-12/23)^4+(x(4)-8/37)^6'

  return title

def p06_ab ( m ):

#*****************************************************************************80
#
## p06_ab() returns bounds for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real a[m], b[m], lower and upper bounds.
#
  import numpy as np

  a = np.zeros ( m )
  b = np.ones ( m )

  return a, b

def p06_f ( m, n, x ):

#*****************************************************************************80
#
## p06_f() returns the objective function value for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of arguments.
#
#    real X(M,N), the arguments.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = np.zeros ( n )

  for j in range ( 0, n ):
    arg = \
        1.0 / x[0,j] \
      + 1.0 / x[1,j] \
      + 1.0 / x[2,j] \
      + 1.0 / x[3,j]
    f[j] = - np.sin ( arg )

  return f

def p06_m ( ):

#*****************************************************************************80
#
## p06_m() returns the spatial dimension for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Output:
#
#    integer M, the spatial dimension.
#
  m = 4

  return m

def p06_sol ( m, know ):

#*****************************************************************************80
#
## p06_sol() returns known solutions for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Input:
#
#    integer M, the order of the problem.
#
#    integer KNOW, 0, or the index of the previously returned solution.
#
#  Output:
#
#    real x[m,1]: the solution.
#
#    integer KNOW, 0 if there are no more solutions, or it is the
#    index of the next solution.
#
  import numpy as np

  if ( know == 0 ):
    know = 1
    x = np.array ( [ \
      [ 0.509282516910744, \
        0.509282516910744, \
        0.509282516910746, \
        0.509282516910744 ] ] )
  else:
    know = 0
    x = np.zeros ( [ 1, m ] )
#
#  Currently, *SOL returns X as a [1,M] array, 
#  but the code assumes [M,1].
#  For now, simply transpose it here.
#  This is only a cheap and temporary solution.
#
  x = np.transpose ( x )

  return x, know

def p06_title ( ):

#*****************************************************************************80
#
## p06_title() returns a title for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Harald Niederreiter, Kevin McCurley,
#    Optimization of functions by quasi-random search methods,
#    Computing,
#    Volume 22, Number 2, 1979, pages 119-123.
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'f(x) = - sin(1/x(1)+1/x(2)+1/x(3)+1/x(4))'

  return title

def p07_ab ( m ):

#*****************************************************************************80
#
## p07_ab() returns bounds for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real a[m], b[m]: lower and upper bounds.
#
  import numpy as np

  a = np.zeros ( m )
  b = 10.0 * np.ones ( m )

  return a, b

def p07_f ( m, n, x ):

#*****************************************************************************80
#
## p07_f() returns the objective function value for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:

#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Langerman10 reference?
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of arguments.
#
#    real X(M,N), the arguments.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = np.zeros ( n )

  a = np.array ( [ \
    [ 3.0, 5.0, 2.0, 1.0, 7.0 ], \
    [ 5.0, 2.0, 1.0, 4.0, 9.0 ] ] )

  c = np.array ( [ 1.0, 2.0, 5.0, 2.0, 3.0 ] )

  for j in range ( 0, n ):
    for k in range ( 0, 5 ):
      arg = np.linalg.norm ( x[:,j] - a[:,k] )
      f[j] = f[j] - c[k] * np.exp ( - arg**2 / np.pi ) * np.cos ( np.pi * arg )

  return f

def p07_m ( ):

#*****************************************************************************80
#
## p07_m() returns the spatial dimension for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the spatial dimension.
#
  m = 2

  return m

def p07_sol ( m, know ):

#*****************************************************************************80
#
## p07_sol() returns known solutions for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the order of the problem.
#
#    integer KNOW, 0, or the index of the previously returned solution.
#
#  Output:
#
#    real x[m,1]: the solution.
#
#    integer KNOW, 0 if there are no more solutions, or it is the
#    index of the next solution.
#
  import numpy as np

  know = 0
  x = np.zeros ( [ 1, m ] )
#
#  Currently, *SOL returns X as a [1,M] array, 
#  but the code assumes [M,1].
#  For now, simply transpose it here.
#  This is only a cheap and temporary solution.
#
  x = np.transpose ( x )

  return x, know

def p07_title ( ):

#*****************************************************************************80
#
## p07_title() returns a title for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'f(x) = Langerman2 function'

  return title

def p08_ab ( m ):

#*****************************************************************************80
#
## p08_ab() returns bounds for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real a[m], b[m], lower and upper bounds.
#
  import numpy as np

  a = np.zeros ( m )
  b = 10.0 * np.ones ( m )

  return a, b

def p08_f ( m, n, x ):

#*****************************************************************************80
#
## p08_f() returns the objective function value for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Langerman10 reference?
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of arguments.
#
#    real X(M,N), the arguments.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = np.zeros ( n )
#
#  A has been entered as the transpose of what it should be.
#
  a = np.array ( [ \
   [ 9.681, 0.667, 4.783, 9.095, 3.517, 9.325, 6.544, 0.211, 5.122, 2.020 ], \
   [ 9.400, 2.041, 3.788, 7.931, 2.882, 2.672, 3.568, 1.284, 7.033, 7.374 ], \
   [ 8.025, 9.152, 5.114, 7.621, 4.564, 4.711, 2.996, 6.126, 0.734, 4.982 ], \
   [ 2.196, 0.415, 5.649, 6.979, 9.510, 9.166, 6.304, 6.054, 9.377, 1.426 ], \
   [ 8.074, 8.777, 3.467, 1.863, 6.708, 6.349, 4.534, 0.276, 7.633, 1.567 ], \
   [ 7.650, 5.658, 0.720, 2.764, 3.278, 5.283, 7.474, 6.274, 1.409, 8.208 ], \
   [ 1.256, 3.605, 8.623, 6.905, 4.584, 8.133, 6.071, 6.888, 4.187, 5.448 ], \
   [ 8.314, 2.261, 4.224, 1.781, 4.124, 0.932, 8.129, 8.658, 1.208, 5.762 ], \
   [ 0.226, 8.858, 1.420, 0.945, 1.622, 4.698, 6.228, 9.096, 0.972, 7.637 ], \
   [ 7.305, 2.228, 1.242, 5.928, 9.133, 1.826, 4.060, 5.204, 8.713, 8.247 ], \
   [ 0.652, 7.027, 0.508, 4.876, 8.807, 4.632, 5.808, 6.937, 3.291, 7.016 ], \
   [ 2.699, 3.516, 5.874, 4.119, 4.461, 7.496, 8.817, 0.690, 6.593, 9.789 ], \
   [ 8.327, 3.897, 2.017, 9.570, 9.825, 1.150, 1.395, 3.885, 6.354, 0.109 ], \
   [ 2.132, 7.006, 7.136, 2.641, 1.882, 5.943, 7.273, 7.691, 2.880, 0.564 ], \
   [ 4.707, 5.579, 4.080, 0.581, 9.698, 8.542, 8.077, 8.515, 9.231, 4.670 ], \
   [ 8.304, 7.559, 8.567, 0.322, 7.128, 8.392, 1.472, 8.524, 2.277, 7.826 ], \
   [ 8.632, 4.409, 4.832, 5.768, 7.050, 6.715, 1.711, 4.323, 4.405, 4.591 ], \
   [ 4.887, 9.112, 0.170, 8.967, 9.693, 9.867, 7.508, 7.770, 8.382, 6.740 ], \
   [ 2.440, 6.686, 4.299, 1.007, 7.008, 1.427, 9.398, 8.480, 9.950, 1.675 ], \
   [ 6.306, 8.583, 6.084, 1.138, 4.350, 3.134, 7.853, 6.061, 7.457, 2.258 ], \
   [ 0.652, 2.343, 1.370, 0.821, 1.310, 1.063, 0.689, 8.819, 8.833, 9.070 ], \
   [ 5.558, 1.272, 5.756, 9.857, 2.279, 2.764, 1.284, 1.677, 1.244, 1.234 ], \
   [ 3.352, 7.549, 9.817, 9.437, 8.687, 4.167, 2.570, 6.540, 0.228, 0.027 ], \
   [ 8.798, 0.880, 2.370, 0.168, 1.701, 3.680, 1.231, 2.390, 2.499, 0.064 ], \
   [ 1.460, 8.057, 1.336, 7.217, 7.914, 3.615, 9.981, 9.198, 5.292, 1.224 ], \
   [ 0.432, 8.645, 8.774, 0.249, 8.081, 7.461, 4.416, 0.652, 4.002, 4.644 ], \
   [ 0.679, 2.800, 5.523, 3.049, 2.968, 7.225, 6.730, 4.199, 9.614, 9.229 ], \
   [ 4.263, 1.074, 7.286, 5.599, 8.291, 5.200, 9.214, 8.272, 4.398, 4.506 ], \
   [ 9.496, 4.830, 3.150, 8.270, 5.079, 1.231, 5.731, 9.494, 1.883, 9.732 ], \
   [ 4.138, 2.562, 2.532, 9.661, 5.611, 5.500, 6.886, 2.341, 9.699, 6.500 ] ] )

  c = np.array ( [ \
    0.806, 0.517, 1.500, 0.908, 0.965, \
    0.669, 0.524, 0.902, 0.531, 0.876, \
    0.462, 0.491, 0.463, 0.714, 0.352, \
    0.869, 0.813, 0.811, 0.828, 0.964, \
    0.789, 0.360, 0.369, 0.992, 0.332, \
    0.817, 0.632, 0.883, 0.608, 0.326 ] )

  a = np.transpose ( a )

  for j in range ( 0, n ):
    for k in range ( 0, 30 ):
      arg = np.linalg.norm ( x[:,j] - a[:,k] )
      f[j] = f[j] - c[k] * np.exp ( - arg**2 / np.pi ) * np.cos ( np.pi * arg )

  return f

def p08_m ( ):

#*****************************************************************************80
#
## p08_m() returns the spatial dimension for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer M, the spatial dimension.
#
  m = 10

  return m

def p08_sol ( m, know ):

#*****************************************************************************80
#
## p08_sol() returns known solutions for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the order of the problem.
#
#    integer KNOW, 0, or the index of the previously returned solution.
#
#  Output:
#
#    real x[m,1]: the solution.
#
#    integer KNOW, 0 if there are no more solutions, or it is the
#    index of the next solution.
#
  import numpy as np

  know = 0
  x = np.zeros ( [ 1, m ] )
#
#  Currently, *SOL returns X as a [1,M] array, 
#  but the code assumes [M,1].
#  For now, simply transpose it here.
#  This is only a cheap and temporary solution.
#
  x = np.transpose ( x )

  return x, know

def p08_title ( ):

#*****************************************************************************80
#
## p08_title() returns a title for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'f(x) = Langerman10 function'

  return title

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
  test_opt_con_test ( )
  timestamp ( )

