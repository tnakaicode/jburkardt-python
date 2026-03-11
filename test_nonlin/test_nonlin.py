#! /usr/bin/env python3
#
def p01_fx ( n, x ):

#*****************************************************************************80
#
## p01_fx() evaluates the function for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  fx[0] = 1.0 - x[0]
  fx[1:n] = 10.0 * ( x[1:n] - x[0:n-1] * x[0:n-1] )

  return fx

def p01_jac ( n, x ):

#*****************************************************************************80
#
## p01_jac() sets the jacobian for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  fjac[0,0] = - 1.0

  for i in range ( 1, n ):
    fjac[i,i-1] = - 20.0 * x[i-1]
    fjac[i,i] = 10.0

  return fjac

def p01_n ( ):

#*****************************************************************************80
#
## p01_n() returns the number of equations for problem 1.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = -2

  return n

def p01_sol ( n ):

#*****************************************************************************80
#
## p01_sol() returns the solution of problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value, if known.
#
  import numpy as np

  x = np.ones ( n )

  return x

def p01_start ( n ):

#*****************************************************************************80
#
## p01_start() specifies a standard approximate solution for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.ones ( n )
  x[0] = - 1.2

  return x

def p01_test ( ):

#*****************************************************************************80
#
## p01_test() tests p01().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p01_title ( )
  print ( '' )
  print ( 'p01 test_nonlin problem:' )
  print ( ' ', title )
  n = p01_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p01_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p01_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p01_sol ( n )
  if ( xe.size == 0 ):
    fjac = p01_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 1, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p01_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p01_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 1, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

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
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Generalized Rosenbrock function'

  return title

def p02_fx ( n, x ):

#*****************************************************************************80
#
## p02_fx() evaluates the function for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  fx[0] = x[0] + 10.0 * x[1]
  fx[1] = np.sqrt ( 5.0 ) * ( x[2] - x[3] )
  fx[2] = ( x[1] - 2.0 * x[2] )**2
  fx[3] = np.sqrt ( 10.0 ) * ( x[0] - x[3] ) * ( x[0] - x[3] )

  return fx

def p02_jac ( n, x ):

#*****************************************************************************80
#
## p02_jac() sets the jacobian for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  fjac[0,0] = 1.0
  fjac[0,1] = 10.0
  fjac[0,2] = 0.0
  fjac[0,3] = 0.0

  fjac[1,0] = 0.0
  fjac[1,1] = 0.0
  fjac[1,2] = np.sqrt ( 5.0 )
  fjac[1,3] = - np.sqrt ( 5.0 )

  fjac[2,0] = 0.0
  fjac[2,1] = 2.0 * ( x[1] - 2.0 * x[2] )
  fjac[2,2] = - 4.0 * ( x[1] - 2.0 * x[2] )
  fjac[2,3] = 0.0

  fjac[3,0] = 2.0 * np.sqrt ( 10.0 ) * ( x[0] - x[3] )
  fjac[3,1] = 0.0
  fjac[3,2] = 0.0
  fjac[3,3] = - 2.0 * np.sqrt ( 10.0 ) * ( x[0] - x[3] )

  return fjac

def p02_n ( ):

#*****************************************************************************80
#
## p02_n() returns the number of equations for problem 2.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = 4

  return n

def p02_sol ( n ):

#*****************************************************************************80
#
## p02_sol() returns the solution of problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.zeros ( n )

  return x

def p02_start ( n ):

#*****************************************************************************80
#
## p02_start() specifies a standard approximate solution for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.array ( [ 3.0, -1.0, 0.0, 1.0 ] )

  return x

def p02_test ( ):

#*****************************************************************************80
#
## p02_test() tests p02().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p02_title ( )
  print ( '' )
  print ( 'p02 test_nonlin problem:' )
  print ( ' ', title )
  n = p02_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p02_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p02_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p02_sol ( n )
  if ( xe.size == 0 ):
    fjac = p02_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 2, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p02_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p02_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 2, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

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
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Powell singular function'

  return title

def p03_fx ( n, x ):

#*****************************************************************************80
#
## p03_fx() evaluates the function for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  fx[0] = 10000.0 * x[0] * x[1] - 1.0
  fx[1] = np.exp ( - x[0] ) + np.exp ( - x[1] ) - 1.0001

  return fx

def p03_jac ( n, x ):

#*****************************************************************************80
#
## p03_jac() sets the jacobian for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  fjac[0,0] = 10000.0 * x[1]
  fjac[0,1] = 10000.0 * x[0]

  fjac[1,0] = - np.exp ( - x[0] )
  fjac[1,1] = - np.exp ( - x[1] )

  return fjac

def p03_n ( ):

#*****************************************************************************80
#
## p03_n() returns the number of equations for problem 3.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = 2

  return n

def p03_sol ( n ):

#*****************************************************************************80
#
## p03_sol() returns the solution of problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.array ( [ 1.098159E-05, 9.106146 ] )

  return x

def p03_start ( n ):

#*****************************************************************************80
#
## p03_start() specifies a standard approximate solution for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.array ( [ 0.0, 1.0 ] )

  return x

def p03_test ( ):

#*****************************************************************************80
#
## p03_test() tests p03().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p03_title ( )
  print ( '' )
  print ( 'p03 test_nonlin problem:' )
  print ( ' ', title )
  n = p03_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p03_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p03_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p03_sol ( n )
  if ( xe.size == 0 ):
    fjac = p03_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 3, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p03_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p03_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 3, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

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
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Powell badly scaled function'

  return title

def p04_fx ( n, x ):

#*****************************************************************************80
#
## p04_fx() evaluates the function for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  temp1 = x[1] - x[0] * x[0]
  temp2 = x[3] - x[2] * x[2]

  fx[0] = - 200.0 * x[0] * temp1 - ( 1.0 - x[0] )
  fx[1] = 200.0 * temp1 + 20.2 * ( x[1] - 1.0 ) + 19.8 * ( x[3] - 1.0 )
  fx[2] = - 180.0 * x[2] * temp2 - ( 1.0 - x[2] )
  fx[3] = 180.0 * temp2 + 20.2 * ( x[3] - 1.0 ) + 19.8 * ( x[1] - 1.0 )

  return fx

def p04_jac ( n, x ):

#*****************************************************************************80
#
## p04_jac() sets the jacobian for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real fjac[N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  fjac[0,0] = - 200.0 * ( x[1] - 3.0 * x[0] * x[0] ) + 1.0
  fjac[0,1] = - 200.0 * x[0]
  fjac[0,2] = 0.0
  fjac[0,3] = 0.0

  fjac[1,0] = - 400.0 * x[0]
  fjac[1,1] =   220.2
  fjac[1,2] =     0.0
  fjac[1,3] =    19.8

  fjac[2,0] = 0.0
  fjac[2,1] = 0.0
  fjac[2,2] = - 180.0 * ( x[3] - 3.0 * x[2] * x[2] ) + 1.0
  fjac[2,3] = - 180.0 * x[2]

  fjac[3,0] =     0.0
  fjac[3,1] =    19.8
  fjac[3,2] = - 360.0 * x[2]
  fjac[3,3] =   300.2

  return fjac

def p04_n ( ):

#*****************************************************************************80
#
## p04_n() returns the number of equations for problem 4.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = 4

  return n

def p04_sol ( n ):

#*****************************************************************************80
#
## p04_sol() returns the solution of problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.ones ( n )

  return x

def p04_start ( n ):

#*****************************************************************************80
#
## p04_start() specifies a standard approximate solution for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.array ( [ -3.0, -1.0, -3.0, -1.0 ] )

  return x

def p04_test ( ):

#*****************************************************************************80
#
## p04_test() tests p04().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p04_title ( )
  print ( '' )
  print ( 'p04 test_nonlin problem:' )
  print ( ' ', title )
  n = p04_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p04_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p04_fx ( n, xs )
  print ( '  Norm of f(xs] = ', norm ( fxs ) )
  xe = p04_sol ( n )
  if ( xe.size == 0 ):
    fjac = p04_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 4, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p04_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p04_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 4, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

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
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Wood function'

  return title

def p05_fx ( n, x ):

#*****************************************************************************80
#
## p05_fx() evaluates the function for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  if ( 0.0 < x[0] ):
    temp = np.arctan ( x[1] / x[0] ) / ( 2.0 * np.pi )
  elif (x[0] < 0.0 ):
    temp = np.arctan ( x[1] / x[0] ) / ( 2.0 * np.pi ) + 0.5
  else:
    temp = 0.25 * np.sign ( x[1] )

  fx[0] = 10.0 * ( x[2] - 10.0 * temp )
  fx[1] = 10.0 * ( np.sqrt ( x[0] * x[0] + x[1] * x[1] ) - 1.0 )
  fx[2] = x[2]

  return fx

def p05_jac ( n, x ):

#*****************************************************************************80
#
## p05_jac() sets the jacobian for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  fjac[0,0] =  100.0 * x[1] / ( 2.0 * np.pi * ( x[0]**2 + x[1]**2 ) )
  fjac[0,1] = -100.0 * x[0] / ( 2.0 * np.pi * ( x[0]**2 + x[1]**2 ) )
  fjac[0,2] =   10.0

  fjac[1,0] = 10.0 * x[0] / np.sqrt ( x[0]**2 + x[1]**2 )
  fjac[1,1] = 10.0 * x[1] / np.sqrt ( x[0]**2 + x[1]**2 )
  fjac[1,2] = 0.0

  fjac[2,0] = 0.0
  fjac[2,1] = 0.0
  fjac[2,2] = 1.0

  return fjac

def p05_n ( ):

#*****************************************************************************80
#
## p05_n() returns the number of equations for problem 5.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = 3

  return n

def p05_sol ( n ):

#*****************************************************************************80
#
## p05_sol() returns the solution of problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.array ( [ 1.0, 0.0, 0.0 ] )

  return x

def p05_start ( n ):

#*****************************************************************************80
#
## p05_start() specifies a standard approximate solution for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.array ( [ -1.0, 0.0, 0.0 ] )

  return x

def p05_test ( ):

#*****************************************************************************80
#
## p05_test() tests p05().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p05_title ( )
  print ( '' )
  print ( 'p05 test_nonlin problem:' )
  print ( ' ', title )
  n = p05_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p05_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p05_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p05_sol ( n )
  if ( xe.size == 0 ):
    fjac = p05_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 5, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p05_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p05_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 5, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

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
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Helical valley function'

  return title

def p06_fx ( n, x ):

#*****************************************************************************80
#
## p06_fx() evaluates the function for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  for i in range ( 1, 30 ):

    ti = i / 29.0

    sum1 = 0.0
    temp = 1.0
    for j in range ( 1, n ):
      sum1 = sum1 + j * temp * x[j]
      temp = ti * temp

    sum2 = 0.0
    temp = 1.0
    for j in range ( 0, n ):
      sum2 = sum2 + temp * x[j]
      temp = ti * temp

    temp = 1.0 / ti

    for k in range ( 0, n ):
      fx[k] = fx[k] + temp * ( sum1 - sum2 * sum2 - 1.0 ) * ( k - 2.0 * ti * sum2 )
      temp = ti * temp

  fx[0] = fx[0] + 3.0 * x[0] - 2.0 * x[0] * x[1] + 2.0 * x[0]**3
  fx[1] = fx[1] + x[1] - x[1]**2 - 1.0

  return fx

def p06_jac ( n, x ):

#*****************************************************************************80
#
## p06_jac() sets the jacobian for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  for i in range ( 1, 30 ):

    ti = i / 29.0

    sum1 = 0.0
    temp = 1.0
    for j in range ( 1, n ):
      sum1 = sum1 + j * temp * x[j]
      temp = ti * temp

    sum2 = 0.0
    temp = 1.0
    for j in range ( 0, n ):
      sum2 = sum2 + temp * x[j]
      temp = ti * temp

    temp1 = 2.0 * ( sum1 - sum2 * sum2 - 1.0 )
    tk = 1.0

    for k in range ( 0, n ):
      tj = tk
      for j in range ( k, n ):
        fjac[k,j] = fjac[k,j] \
          + tj * ( ( k / ti - 2.0 * sum2 ) * ( j / ti - 2.0 * sum2 ) - temp1 )
        tj = ti * tj
      tk = ti * ti * tk

  fjac[0,0] = fjac[0,0] + 3.0 - 2.0 * x[1] + 6.0 * x[0]**2
  fjac[0,1] = fjac[0,1] - 2.0 * x[0]

  fjac[1,0] = fjac[1,0] - 2.0 * x[0]
  fjac[1,1] = fjac[1,1] + 1.0

  for k in range ( 0, n ):
    fjac[k:n,k] = fjac[k,k:n]

  return fjac

def p06_n ( ):

#*****************************************************************************80
#
## p06_n() returns the number of equations for problem 6.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = - 2

  return n

def p06_sol ( n ):

#*****************************************************************************80
#
## p06_sol() returns the solution of problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.array ( [] )

  return x

def p06_start ( n ):

#*****************************************************************************80
#
## p06_start() specifies a standard approximate solution for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.zeros ( n )

  return x

def p06_test ( ):

#*****************************************************************************80
#
## p06_test() tests p06().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p06_title ( )
  print ( '' )
  print ( 'p06 test_nonlin problem:' )
  print ( ' ', title )
  n = p06_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p06_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p06_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p06_sol ( n )
  if ( xe.size == 0 ):
    fjac = p06_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 6, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p06_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p06_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 6, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p06_title ( ):

#*****************************************************************************80
#
## p06_title() returns the title of problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Watson function'

  return title

def p07_fx ( n, x ):

#*****************************************************************************80
#
## p07_fx() evaluates the function for problem 7.
#
#  Discussion:
#
#    The Chebyquad function is related to the computation of the
#    abscissas for Chebyshev quadrature.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  for j in range ( 0, n ):

    t1 = 1.0
    t2 = x[j]

    for i in range ( 0, n ):

      fx[i] = fx[i] + t2

      t3 = 2.0 * x[j] * t2 - t1
      t1 = t2
      t2 = t3

  fx = fx / n

  for i in range ( 0, n ):
    ip1 = i + 1
    if ( np.mod ( ip1, 2 ) == 0 ):
      fx[i] = fx[i] + 1.0 / ( ip1 * ip1 - 1 )

  return fx

def p07_jac ( n, x ):

#*****************************************************************************80
#
## p07_jac() sets the jacobian for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):

    t1 = 1.0
    t2 = x[j]

    t4 = 0.0
    t5 = 1.0

    for i in range ( 0, n ):

      fjac[i,j] = t5

      t6 = 2.0 * t2 + 2.0 * t5 * x[j] - t4
      t4 = t5
      t5 = t6

      t3 = 2.0 * x[j] * t2 - t1
      t1 = t2
      t2 = t3

  fjac = fjac / n

  return fjac

def p07_n ( rng ):

#*****************************************************************************80
#
## p07_n() returns the number of equations for problem 7.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  import numpy as np

  i = rng.integers ( low = 0, high = 7, endpoint = True )

  if ( i == 0 ):
    n = 1
  elif ( i == 1 ):
    n = 2
  elif ( i == 2 ):
    n = 3
  elif ( i == 3 ):
    n = 4
  elif ( i == 4 ):
    n = 5
  elif ( i == 5 ):
    n = 6
  elif ( i == 6 ):
    n = 7
  elif ( i == 7 ):
    n = 9
  else:
    print ( '' )
    print ( 'p07_n(): Fatal error!' )
    print ( '  Bogus problem index.' )

  return n

def p07_sol ( n ):

#*****************************************************************************80
#
## p07_sol() returns the solution of problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  if ( n == 1 ):
    x = np.zeros ( n )
    x[0] = 0.5000000000000000
    x = 2.0 * x - 1.0
  elif ( n == 2 ):
    x = np.zeros ( n )
    x[0] = 0.2113248654051871
    x[1] = 0.7886751345948129
    x = 2.0 * x - 1.0
  elif ( n == 3 ):
    x = np.zeros ( n )
    x[0] = 0.1464466094067263
    x[1] = 0.5000000000000000
    x[2] = 0.8535533905932737
    x = 2.0 * x - 1.0
  elif ( n == 4 ):
    x = np.zeros ( n )
    x[0] = 0.1026727638500000
    x[1] = 0.4062037629500000
    x[2] = 0.5937962370500000
    x[3] = 0.8973272361500000
    x = 2.0 * x - 1.0
  elif ( n == 5 ):
    x = np.zeros ( n )
    x[0] = 8.3751256499999982E-02
    x[1] = 0.3127292952000000
    x[2] = 0.5000000000000000
    x[3] = 0.6872707048000000
    x[4] = 0.9162487435000000
    x = 2.0 * x - 1.0
  elif ( n == 6 ):
    x = np.zeros ( n )
    x[0] = 6.6876590949999981E-02
    x[1] = 0.2887406731000000
    x[2] = 0.3666822992500000
    x[3] = 0.6333177007499999
    x[4] = 0.7112593269000000
    x[5] = 0.9331234090500000
    x = 2.0 * x - 1.0
  elif ( n == 7 ):
    x = np.zeros ( n )
    x[0] = 5.8069149599999981E-02
    x[1] = 0.2351716123500000
    x[2] = 0.3380440947500000
    x[3] = 0.5000000000000000
    x[4] = 0.6619559052500000
    x[5] = 0.7648283876499999
    x[6] = 0.9419308504000000
    x = 2.0 * x - 1.0
  elif ( n == 9 ):
    x = np.zeros ( n )
    x[0] = 4.4205346149999991E-02
    x[1] = 0.1994906723000000
    x[2] = 0.2356191084500000
    x[3] = 0.4160469079000000
    x[4] = 0.5000000000000000
    x[5] = 0.5839530921000000
    x[6] = 0.7643808915500000
    x[7] = 0.8005093276999999
    x[8] = 0.9557946538500000
    x = 2.0 * x - 1.0
  else:
    x = np.array ( [] )
    print ( '' )
    print ( 'p07_sol - Warning' )
    print ( '  Nonexistent solution requested.' )

  return x

def p07_start ( n ):

#*****************************************************************************80
#
## p07_start() specifies a standard approximate solution for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = ( 2 * i + 1 - n ) / ( n + 1 )

  return x

def p07_test ( rng ):

#*****************************************************************************80
#
## p07_test() tests p07().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p07_title ( )
  print ( '' )
  print ( 'p07 test_nonlin problem:' )
  print ( ' ', title )
  n = p07_n ( rng )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p07_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p07_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p07_sol ( n )
  if ( xe.size == 0 ):
    fjac = p07_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 7, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p07_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p07_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 7, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p07_title ( ):

#*****************************************************************************80
#
## p07_title() returns the title of problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Chebyquad function'

  return title

def p08_fx ( n, x ):

#*****************************************************************************80
#
## p08_fx() evaluates the function for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  fx[0:n-1] = x[0:n-1] + np.sum ( x ) - ( n + 1 )

  fx[n-1] = np.prod ( x ) - 1.0

  return fx

def p08_jac ( n, x ):

#*****************************************************************************80
#
## p08_jac() sets the jacobian for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    fjac[0:n-1,j] = 1.0

  for i in range ( 0, n - 1 ):
    fjac[i,i] = 2.0
#
#  Last row:
#
  for j in range ( 0, n ):
    p = 1.0
    for k in range ( 0, n ):
      if ( k != j ):
        p = x[k] * p
    fjac[n-1,j] = p

  return fjac

def p08_n ( ):

#*****************************************************************************80
#
## p08_n() returns the number of equations for problem 8.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = - 1

  return n

def p08_sol ( n ):

#*****************************************************************************80
#
## p08_sol() returns the solution of problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.ones ( n )

  return x

def p08_start ( n ):

#*****************************************************************************80
#
## p08_start() specifies a standard approximate solution for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = 0.5 * np.ones ( n )

  return x

def p08_test ( ):

#*****************************************************************************80
#
## p08_test() tests p08().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p08_title ( )
  print ( '' )
  print ( 'p08 test_nonlin problem:' )
  print ( ' ', title )
  n = p08_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p08_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p08_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p08_sol ( n )
  if ( xe.size == 0 ):
    fjac = p08_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 8, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p08_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p08_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 8, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p08_title ( ):

#*****************************************************************************80
#
## p08_title() returns the title of problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Brown almost linear function'

  return title

def p09_fx ( n, x ):

#*****************************************************************************80
#
## p09_fx() evaluates the function for problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  h = 1.0 / ( n + 1 )

  for k in range ( 0, n ):

    fx[k] = 2.0 * x[k] + 0.5 * h * h * ( x[k] + ( k + 1 ) * h + 1.0 )**3

    if ( 0 < k ):
      fx[k] = fx[k] - x[k-1]

    if ( k < n - 1 ):
      fx[k] = fx[k] - x[k+1]

  return fx

def p09_jac ( n, x ):

#*****************************************************************************80
#
## p09_jac() sets the jacobian for problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):

    fjac[i,i] = 2.0 + 1.5 * ( x[i] + 1.0 + ( i + 1 ) / ( n + 1 ) )**2 / ( n + 1 )**2

    if ( 0 < i ):
      fjac[i,i-1] = - 1.0

    if ( i < n - 1 ):
      fjac[i,i+1] = - 1.0

  return fjac

def p09_n ( ):

#*****************************************************************************80
#
## p09_n() returns the number of equations for problem 9.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = - 1

  return n

def p09_sol ( n ):

#*****************************************************************************80
#
## p09_sol() returns the solution of problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.array ( [] )

  return x

def p09_start ( n ):

#*****************************************************************************80
#
## p09_start() specifies a standard approximate solution for problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    ip1 = i + 1
    x[i] = ( ip1 * ( ip1 - n - 1 ) ) / ( n + 1 )**2

  return x

def p09_test ( ):

#*****************************************************************************80
#
## p09_test() tests p09().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p09_title ( )
  print ( '' )
  print ( 'p09 test_nonlin problem:' )
  print ( ' ', title )
  n = p09_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p09_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p09_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p09_sol ( n )
  if ( xe.size == 0 ):
    fjac = p09_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 9, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p09_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p09_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 9, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p09_title ( ):

#*****************************************************************************80
#
## p09_title() returns the title of problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Discrete boundary value function'

  return title

def p10_fx ( n, x ):

#*****************************************************************************80
#
## p10_fx() evaluates the function for problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  h = 1.0 / ( n + 1 )

  for k in range ( 0, n ):

    tk = ( k + 1 ) / ( n + 1 )

    sum1 = 0.0
    for j in range ( 0, k + 1 ):
      tj = ( j + 1 ) * h
      sum1 = sum1 + tj * ( x[j] + tj + 1.0 )**3

    sum2 = 0.0
    for j in range ( k + 1, n ):
      tj = ( j + 1 ) * h
      sum2 = sum2 + ( 1.0 - tj ) * ( x[j] + tj + 1.0 )**3

    fx[k] = x[k] + h * ( ( 1.0 - tk ) * sum1 + tk * sum2 ) / 2.0

  return fx

def p10_jac ( n, x ):

#*****************************************************************************80
#
## p10_jac() sets the jacobian for problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):

    ti = ( i + 1 ) / ( n + 1 )

    for j in range ( 0, n ):
      tj = ( j + 1 ) / ( n + 1 )
      temp1 = ( x[j] + tj + 1.0 )**2
      temp2 = min ( ti, tj ) - ti * tj
      fjac[i,j] = 1.5 * temp2 * temp1 / ( n + 1 )

    fjac[i,i] = fjac[i,i] + 1.0

  return fjac

def p10_n ( ):

#*****************************************************************************80
#
## p10_n() returns the number of equations for problem 10.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = - 1

  return n

def p10_sol ( n ):

#*****************************************************************************80
#
## p10_sol() returns the solution of problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.array ( [] )

  return x

def p10_start ( n ):

#*****************************************************************************80
#
## p10_start() specifies a standard approximate solution for problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    ip1 = i + 1
    x[i] = ( ip1 * ( ip1 - n - 1 ) ) / ( n + 1 )**2

  return x

def p10_test ( ):

#*****************************************************************************80
#
## p10_test() tests p10().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p10_title ( )
  print ( '' )
  print ( 'p10 test_nonlin problem:' )
  print ( ' ', title )
  n = p10_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p10_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p10_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p10_sol ( n )
  if ( xe.size == 0 ):
    fjac = p10_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 10, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p10_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p10_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 10, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p10_title ( ):

#*****************************************************************************80
#
## p10_title() returns the title of problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Discrete integral equation function'

  return title

def p11_fx ( n, x ):

#*****************************************************************************80
#
## p11_fx() evaluates the function for problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  c_sum = np.sum ( np.cos ( x ) )

  for k in range ( 0, n ):
    fx[k] =  n - c_sum + ( k + 1 ) * ( 1.0 - np.cos ( x[k] ) ) - np.sin ( x[k] )

  return fx

def p11_jac ( n, x ):

#*****************************************************************************80
#
## p11_jac() sets the jacobian for problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):

    for j in range ( 0, n ):

      if ( i != j ):
        fjac[i,j] = np.sin ( x[j] )
      else:
        fjac[i,j] = ( j + 2 ) * np.sin ( x[j] ) - np.cos ( x[j] )

  return fjac

def p11_n ( ):

#*****************************************************************************80
#
## p11_n() returns the number of equations for problem 11.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = - 1

  return n

def p11_sol ( n ):

#*****************************************************************************80
#
## p11_sol() returns the solution of problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.array ( [] )

  return x

def p11_start ( n ):

#*****************************************************************************80
#
## p11_start() specifies a standard approximate solution for problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.ones ( n ) / n

  return x

def p11_test ( ):

#*****************************************************************************80
#
## p11_test() tests p11().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p11_title ( )
  print ( '' )
  print ( 'p11 test_nonlin problem:' )
  print ( ' ', title )
  n = p11_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p11_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p11_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p11_sol ( n )
  if ( xe.size == 0 ):
    fjac = p11_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 11, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p11_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p11_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 11, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p11_title ( ):

#*****************************************************************************80
#
## p11_title() returns the title of problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Trigonometric function'

  return title

def p12_fx ( n, x ):

#*****************************************************************************80
#
## p12_fx() evaluates the function for problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  sum1 = 0.0
  for j in range ( 0, n ):
    sum1 = sum1 + ( j + 1 ) * ( x[j] - 1.0 )

  for k in range ( 0, n ):
    fx[k] = x[k] - 1.0 + ( k + 1 ) * sum1 * ( 1.0 + 2.0 * sum1 * sum1 )

  return fx

def p12_jac ( n, x ):

#*****************************************************************************80
#
## p12_jac() sets the jacobian for problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  sum1 = 0.0
  for i in range ( 0, n ):
    sum1 = sum1 + ( i + 1 ) * ( x[i] - 1.0 )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      fjac[i,j] = ( i + 1 ) * ( j + 1 ) * ( 1.0 + 6.0 * sum1 * sum1 )

      if ( i == j ):
        fjac[i,j] = fjac[i,j] + 1.0

  return fjac

def p12_n ( ):

#*****************************************************************************80
#
## p12_n() returns the number of equations for problem 12.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = - 1

  return n

def p12_sol ( n ):

#*****************************************************************************80
#
## p12_sol() returns the solution of problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.ones ( n )

  return x

def p12_start ( n ):

#*****************************************************************************80
#
## p12_start() specifies a standard approximate solution for problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    ip1 = i + 1
    x[i] = 1.0 - ip1 / n

  return x

def p12_test ( ):

#*****************************************************************************80
#
## p12_test() tests p12().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p12_title ( )
  print ( '' )
  print ( 'p12 test_nonlin problem:' )
  print ( ' ', title )
  n = p12_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p12_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p12_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p12_sol ( n )
  if ( xe.size == 0 ):
    fjac = p12_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 12, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p12_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p12_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 12, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p12_title ( ):

#*****************************************************************************80
#
## p12_title() returns the title of problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Variably dimensioned function'

  return title

def p13_fx ( n, x ):

#*****************************************************************************80
#
## p13_fx() evaluates the function for problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  for k in range ( 0, n ):

    fx[k] = ( 3.0 - 2.0 * x[k] ) * x[k] + 1.0

    if ( 0 < k ):
      fx[k] = fx[k] - x[k-1]

    if ( k < n - 1 ):
      fx[k] = fx[k] - 2.0 * x[k+1]

  return fx

def p13_jac ( n, x ):

#*****************************************************************************80
#
## p13_jac() sets the jacobian for problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  for k in range ( 0, n ):

    fjac[k,k] = 3.0 - 4.0 * x[k]

    if ( 0 < k ):
      fjac[k,k-1] = - 1.0

    if ( k < n - 1 ):
      fjac[k,k+1] = - 2.0

  return fjac

def p13_n ( ):

#*****************************************************************************80
#
## p13_n() returns the number of equations for problem 13.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = - 1

  return n

def p13_sol ( n ):

#*****************************************************************************80
#
## p13_sol() returns the solution of problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.array ( [] )

  return x

def p13_start ( n ):

#*****************************************************************************80
#
## p13_start() specifies a standard approximate solution for problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = - np.ones ( n )

  return x

def p13_test ( ):

#*****************************************************************************80
#
## p13_test() tests p13().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p13_title ( )
  print ( '' )
  print ( 'p13 test_nonlin problem:' )
  print ( ' ', title )
  n = p13_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p13_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p13_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p13_sol ( n )
  if ( xe.size == 0 ):
    fjac = p13_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 13, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p13_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p13_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 13, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p13_title ( ):

#*****************************************************************************80
#
## p13_title() returns the title of problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Broyden tridiagonal function'

  return title

def p14_fx ( n, x ):

#*****************************************************************************80
#
## p14_fx() evaluates the function for problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  ml = 5
  mu = 1

  for k in range ( 0, n ):

    kp1 = k + 1

    k1 = max ( 0, k - ml )
    k2 = min ( n - 1, k + mu )

    temp = 0.0
    for j in range ( k1, k2 + 1 ):
      if ( j != k ):
        temp = temp + x[j] * ( 1.0 + x[j] )

    fx[k] = x[k] * ( 2.0 + 5.0 * x[k] * x[k] ) + 1.0 - temp

  return fx

def p14_jac ( n, x ):

#*****************************************************************************80
#
## p14_jac() sets the jacobian for problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  ml = 5
  mu = 1

  for k in range ( 0, n ):

    k1 = max ( 0, k - ml )
    k2 = min ( n - 1, k + mu )

    for j in range ( k1, k2 + 1 ):
      if ( j != k ):
        fjac[k,j] = - ( 1.0 + 2.0 * x[j] )
      else:
        fjac[k,j] = 2.0 + 15.0 * x[k] * x[k]

  return fjac

def p14_n ( ):

#*****************************************************************************80
#
## p14_n() returns the number of equations for problem 14.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = - 1

  return n

def p14_sol ( n ):

#*****************************************************************************80
#
## p14_sol() returns the solution of problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.array ( [] )

  return x

def p14_start ( n ):

#*****************************************************************************80
#
## p14_start() specifies a standard approximate solution for problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = - np.ones ( n )

  return x

def p14_test ( ):

#*****************************************************************************80
#
## p14_test() tests p14().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p14_title ( )
  print ( '' )
  print ( 'p14 test_nonlin problem:' )
  print ( ' ', title )
  n = p14_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p14_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p14_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p14_sol ( n )
  if ( xe.size == 0 ):
    fjac = p14_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 14, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p14_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p14_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 14, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p14_title ( ):

#*****************************************************************************80
#
## p14_title() returns the title of problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Broyden banded function'

  return title

def p15_fx ( n, x ):

#*****************************************************************************80
#
## p15_fx() evaluates the function for problem 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  fx[0] = ( x[0] * x[0] + x[1] * x[2] ) - 0.0001
  fx[1] = ( x[0] * x[1] + x[1] * x[3] ) - 1.0
  fx[2] = ( x[2] * x[0] + x[3] * x[2] ) - 0.0
  fx[3] = ( x[2] * x[1] + x[3] * x[3] ) - 0.0001

  return fx

def p15_jac ( n, x ):

#*****************************************************************************80
#
## p15_jac() sets the jacobian for problem 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  fjac[0,0] = 2.0 * x[0]
  fjac[0,1] = x[2]
  fjac[0,2] = x[1]
  fjac[0,3] = 0.0

  fjac[1,0] = x[1]
  fjac[1,1] = x[0] + x[3]
  fjac[1,2] = 0.0
  fjac[1,3] = x[1]

  fjac[2,0] = x[2]
  fjac[2,1] = 0.0
  fjac[2,2] = x[0] + x[3]
  fjac[2,3] = x[2]

  fjac[3,0] = 0.0
  fjac[3,1] = x[2]
  fjac[3,2] = x[1]
  fjac[3,3] = 2.0 * x[3]

  return fjac

def p15_n ( ):

#*****************************************************************************80
#
## p15_n() returns the number of equations for problem 15.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = 4

  return n

def p15_sol ( n ):

#*****************************************************************************80
#
## p15_sol() returns the solution of problem 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.array ( [ 0.01, 50.0, 0.0, 0.01 ] )

  return x

def p15_start ( n ):

#*****************************************************************************80
#
## p15_start() specifies a standard approximate solution for problem 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.array ( [ 1.0, 0.0, 0.0, 1.0 ] )

  return x

def p15_test ( ):

#*****************************************************************************80
#
## p15_test() tests p15().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p15_title ( )
  print ( '' )
  print ( 'p15 test_nonlin problem:' )
  print ( ' ', title )
  n = p15_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p15_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p15_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p15_sol ( n )
  if ( xe.size == 0 ):
    fjac = p15_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 15, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p15_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p15_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 15, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p15_title ( ):

#*****************************************************************************80
#
## p15_title() returns the title of problem 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Hammarling 2 by 2 matrix square root problem'

  return title

def p16_fx ( n, x ):

#*****************************************************************************80
#
## p16_fx() evaluates the function for problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  fx[0] = ( x[0] * x[0] + x[1] * x[3] + x[2] * x[6] ) - 0.0001
  fx[1] = ( x[0] * x[1] + x[1] * x[4] + x[2] * x[7] ) - 1.0
  fx[2] = ( x[0] * x[2] + x[1] * x[5] + x[2] * x[8] )

  fx[3] = ( x[3] * x[0] + x[4] * x[3] + x[5] * x[6] )
  fx[4] = ( x[3] * x[1] + x[4] * x[4] + x[5] * x[7] ) - 0.0001
  fx[5] = ( x[3] * x[2] + x[4] * x[5] + x[5] * x[8] )

  fx[6] = ( x[6] * x[0] + x[7] * x[3] + x[8] * x[6] )
  fx[7] = ( x[6] * x[1] + x[7] * x[4] + x[8] * x[7] )
  fx[8] = ( x[6] * x[2] + x[7] * x[5] + x[8] * x[8] ) - 0.0001

  return fx

def p16_jac ( n, x ):

#*****************************************************************************80
#
## p16_jac() sets the jacobian for problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real fjac[N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  fjac[0,0] = 2.0 * x[0]
  fjac[0,1] = x[3]
  fjac[0,2] = x[6]
  fjac[0,3] = x[1]
  fjac[0,6] = x[2]

  fjac[1,0] = x[1]
  fjac[1,1] = x[0] + x[4]
  fjac[1,2] = x[7]
  fjac[1,4] = x[1]
  fjac[1,7] = x[2]

  fjac[2,0] = x[2]
  fjac[2,1] = x[5]
  fjac[2,2] = x[0] + x[8]
  fjac[2,5] = x[1]
  fjac[2,8] = x[2]

  fjac[3,0] = x[3]
  fjac[3,3] = x[0] + x[4]
  fjac[3,4] = x[3]
  fjac[3,5] = x[6]
  fjac[3,6] = x[5]

  fjac[4,1] = x[3]
  fjac[4,3] = x[1]
  fjac[4,4] = 2.0 * x[4]
  fjac[4,5] = x[7]
  fjac[4,7] = x[5]

  fjac[5,2] = x[3]
  fjac[5,3] = x[2]
  fjac[5,4] = x[5]
  fjac[5,5] = x[4] + x[8]
  fjac[5,8] = x[5]

  fjac[6,0] = x[6]
  fjac[6,3] = x[7]
  fjac[6,6] = x[0] + x[8]
  fjac[6,7] = x[3]
  fjac[6,8] = x[6]

  fjac[7,1] = x[6]
  fjac[7,4] = x[7]
  fjac[7,6] = x[1]
  fjac[7,7] = x[4] + x[8]
  fjac[7,8] = x[7]

  fjac[8,2] = x[6]
  fjac[8,5] = x[7]
  fjac[8,6] = x[2]
  fjac[8,7] = x[5]
  fjac[8,8] = 2.0 * x[8]

  return fjac

def p16_n ( ):

#*****************************************************************************80
#
## p16_n() returns the number of equations for problem 16.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = 9

  return n

def p16_sol ( n ):

#*****************************************************************************80
#
## p16_sol() returns the solution of problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.array ( [ 0.01, 50.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.01 ] )

  return x

def p16_start ( n ):

#*****************************************************************************80
#
## p16_start() specifies a standard approximate solution for problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.array ( [ 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0 ] )

  return x

def p16_test ( ):

#*****************************************************************************80
#
## p16_test() tests p16().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p16_title ( )
  print ( '' )
  print ( 'p16 test_nonlin problem:' )
  print ( ' ', title )
  n = p16_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p16_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p16_fx ( n, xs )
  print ( '  Norm of f(xs] = ', norm ( fxs ) )
  xe = p16_sol ( n )
  if ( xe.size == 0 ):
    fjac = p16_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 16, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p16_fx ( n, xe )
    print ( '  Norm of f(xe] = ', norm ( fxe ) )
    fjac = p16_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 16, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p16_title ( ):

#*****************************************************************************80
#
## p16_title() returns the title of problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Hammarling 3 by 3 matrix square root problem'

  return title

def p17_fx ( n, x ):

#*****************************************************************************80
#
## p17_fx() evaluates the function for problem 17.
#
#  Discussion:
#
#    The equations are:
#
#      F1(X) = X(1) + X(2) - 3
#      F2(X) = X(1)^2 + X(2)^2 - 9
#
#    with roots (3,0) and (0,3).
#
#    Using a starting point of (1,5), here are the iterates for Broyden's
#    method and Newton's method:
#
#    Broyden's Method
#
#    0   1.0              5.0
#    1  -0.625            3.625
#    2  -0.0757575757575  3.0757575757575
#    3  -0.0127942681679  3.0127942681679
#    4  -0.0003138243387  3.0003138243387
#    5  -0.0000013325618  3.0000013325618
#    6  -0.0000000001394  3.0000000001394
#    7   0.0              3.0
#
#    Newton's Method
#
#    0   1.0              5.0
#    1  -0.625            3.625
#    2  -0.0919117647059  3.0919117647059
#    3  -0.0026533419372  3.0026533419372
#    4  -0.0000023425973  3.0000023425973
#    5  -0.0000000000018  3.0000000000018
#    6   0.0              3.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Dennis, Robert Schnabel,
#    Numerical Methods for Unconstrained Optimization
#    and Nonlinear Equations,
#    SIAM, 1996,
#    ISBN13: 978-0-898713-64-0,
#    LC: QA402.5.D44.
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  fx[0] = x[0]    + x[1]    - 3.0
  fx[1] = x[0]**2 + x[1]**2 - 9.0

  return fx

def p17_jac ( n, x ):

#*****************************************************************************80
#
## p17_jac() sets the jacobian for problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  fjac[0,0] = 1.0
  fjac[0,1] = 1.0

  fjac[1,0] = 2.0 * x[0]
  fjac[1,1] = 2.0 * x[1]

  return fjac

def p17_n ( ):

#*****************************************************************************80
#
## p17_n() returns the number of equations for problem 17.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = 2

  return n

def p17_sol ( n ):

#*****************************************************************************80
#
## p17_sol() returns the solution of problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.array ( [ 0.0, 3.0 ] )

  return x

def p17_start ( n ):

#*****************************************************************************80
#
## p17_start() specifies a standard approximate solution for problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.array ( [ 1.0, 5.0 ] )

  return x

def p17_test ( ):

#*****************************************************************************80
#
## p17_test() tests p17().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p17_title ( )
  print ( '' )
  print ( 'p17 test_nonlin problem:' )
  print ( ' ', title )
  n = p17_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p17_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p17_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p17_sol ( n )
  if ( xe.size == 0 ):
    fjac = p17_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 17, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p17_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p17_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 17, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p17_title ( ):

#*****************************************************************************80
#
## p17_title() returns the title of problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Dennis and Schnabel 2 by 2 example'

  return title

def p18_fx ( n, x ):

#*****************************************************************************80
#
## p18_fx() evaluates the function for problem 18.
#
#  Discussion:
#
#    This problem has as roots any point (x,y) with x or y equal to
#    zero.  The jacobian is of rank one at all roots, except at the
#    origin, where it completely vanishes.
#
#    Newton iterates can converge to the origin, or to points on
#    the X or Y axes, or can even "converge" to a point at infinity,
#    generating a sequence of ever larger points with ever smaller
#    function values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  if ( x[0] != 0.0 ):
    fx[0] = x[1]**2 * ( 1.0 - np.exp ( - x[0] * x[0] ) ) / x[0]
  else:
    fx[0] = 0.0

  if ( x[1] != 0.0 ):
    fx[1] = x[0] * ( 1.0 - np.exp ( - x[1] * x[1] ) ) / x[1]
  else:
    fx[1] = 0.0

  return fx

def p18_jac ( n, x ):

#*****************************************************************************80
#
## p18_jac() sets the jacobian for problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  if ( x[0] != 0.0 ):
    fjac[0,0] = x[1]**2 * ( 2.0 * np.exp ( - x[0]**2 ) - \
      ( 1.0 - np.exp ( - x[0]**2 ) ) / x[0]**2)
    fjac[0,1] = 2.0 * x[1] * ( 1.0 - np.exp ( - x[0]**2 ) ) / x[0]

  else:

    fjac[0,0] = x[1]**2
    fjac[0,1] = 0.0

  if ( x[1] != 0.0 ):

    fjac[1,0] = ( 1.0 - np.exp ( - x[1]**2 ) ) / x[1]
    fjac[1,1] = x[0] * ( 2.0 * np.exp ( - x[1]**2 ) - \
      ( 1.0 - np.exp ( - x[1]**2 ) ) / x[1]**2 )

  else:

    fjac[1,0] = 0.0
    fjac[1,1] = x[0]

  return fjac

def p18_n ( ):

#*****************************************************************************80
#
## p18_n() returns the number of equations for problem 18.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = 2

  return n

def p18_sol ( n ):

#*****************************************************************************80
#
## p18_sol() returns the solution of problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.zeros ( n )

  return x

def p18_start ( n ):

#*****************************************************************************80
#
## p18_start() specifies a standard approximate solution for problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.array ( [ 2.0, 2.0 ] )

  return x

def p18_test ( ):

#*****************************************************************************80
#
## p18_test() tests p18().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p18_title ( )
  print ( '' )
  print ( 'p18 test_nonlin problem:' )
  print ( ' ', title )
  n = p18_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p18_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p18_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p18_sol ( n )
  if ( xe.size == 0 ):
    fjac = p18_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 18, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p18_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p18_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 18, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p18_title ( ):

#*****************************************************************************80
#
## p18_title() returns the title of problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Sample problem 18'

  return title

def p19_fx ( n, x ):

#*****************************************************************************80
#
## p19_fx() evaluates the function for problem 19.
#
#  Discussion:
#
#    This problem has a single root at the origin.  Convergence of the
#    Newton iterates should be monotonic, but only linear in rate,
#    since the jacobian is singular at the origin.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  fx[0] = x[0] * ( x[0]**2 + x[1]**2 )
  fx[1] = x[1] * ( x[0]**2 + x[1]**2 )

  return fx

def p19_jac ( n, x ):

#*****************************************************************************80
#
## p19_jac() sets the jacobian for problem 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  fjac[0,0] = 3.0 * x[0]**2 + x[1]**2
  fjac[0,1] = 2.0 * x[0] * x[1]

  fjac[1,0] = 2.0 * x[0] * x[1]
  fjac[1,1] = x[0]**2 + 3.0 * x[1]**2

  return fjac

def p19_n ( ):

#*****************************************************************************80
#
## p19_n() returns the number of equations for problem 19.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = 2

  return n

def p19_sol ( n ):

#*****************************************************************************80
#
## p19_sol() returns the solution of problem 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.zeros ( n )

  return x

def p19_start ( n ):

#*****************************************************************************80
#
## p19_start() specifies a standard approximate solution for problem 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.array ( [ 3.0, 3.0 ] )

  return x

def p19_test ( ):

#*****************************************************************************80
#
## p19_test() tests p19().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p19_title ( )
  print ( '' )
  print ( 'p19 test_nonlin problem:' )
  print ( ' ', title )
  n = p19_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p19_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p19_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p19_sol ( n )
  if ( xe.size == 0 ):
    fjac = p19_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 19, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p19_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p19_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 19, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p19_title ( ):

#*****************************************************************************80
#
## p19_title() returns the title of problem 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Sample problem 19'

  return title

def p20_fx ( n, x ):

#*****************************************************************************80
#
## p20_fx() evaluates the function for problem 20.
#
#  Discussion:
#
#    This problem has a single root at the origin, and a multiple root
#    at x = 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  fx[0] = x[0] * ( x[0] - 5.0 ) * ( x[0] - 5.0 )

  return fx

def p20_jac ( n, x ):

#*****************************************************************************80
#
## p20_jac() sets the jacobian for problem 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  fjac[0,0] = ( 3.0 * x[0] - 5.0 ) * ( x[0] - 5.0 )

  return fjac

def p20_n ( ):

#*****************************************************************************80
#
## p20_n() returns the number of equations for problem 20.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = 1

  return n

def p20_sol ( n, rng ):

#*****************************************************************************80
#
## p20_sol() returns the solution of problem 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  if ( rng.random ( ) < 0.5 ):
    x = np.zeros ( n )
  else:
    x = 5.0 * np.ones ( n )

  return x

def p20_start ( n ):

#*****************************************************************************80
#
## p20_start() specifies a standard approximate solution for problem 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.ones ( n )

  return x

def p20_test ( rng ):

#*****************************************************************************80
#
## p20_test() tests p20().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p20_title ( )
  print ( '' )
  print ( 'p20 test_nonlin problem:' )
  print ( ' ', title )
  n = p20_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p20_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p20_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p20_sol ( n, rng )
  if ( xe.size == 0 ):
    fjac = p20_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 20, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p20_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p20_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 20, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p20_title ( ):

#*****************************************************************************80
#
## p20_title() returns the title of problem 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Scalar problem f(x) = x * ( x - 5 ) * ( x - 5 )'

  return title

def p21_fx ( n, x ):

#*****************************************************************************80
#
## p21_fx() evaluates the function for problem 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  fx[0] = x[0] - x[1]**3 + 5.0 * x[1]**2 -  2.0 * x[1] - 13.0
  fx[1] = x[0] + x[1]**3 +       x[1]**2 - 14.0 * x[1] - 29.0

  return fx

def p21_jac ( n, x ):

#*****************************************************************************80
#
## p21_jac() sets the jacobian for problem 21
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  fjac[0,0] = 1.0
  fjac[0,1] = - 3.0 * x[1]**2 + 10.0 * x[1] -  2.0

  fjac[1,0] = 1.0
  fjac[1,1] =   3.0 * x[1]**2 +  2.0 * x[1] - 14.0

  return fjac

def p21_n ( ):

#*****************************************************************************80
#
## p21_n() returns the number of equations for problem 21.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = 2

  return n

def p21_sol ( n ):

#*****************************************************************************80
#
## p21_sol() returns the solution of problem 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.array ( [ 5.0, 4.0 ] )

  return x

def p21_start ( n ):

#*****************************************************************************80
#
## p21_start() specifies a standard approximate solution for problem 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.array ( [ 0.5, -2.0 ] )

  return x

def p21_test ( ):

#*****************************************************************************80
#
## p21_test() tests p21().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p21_title ( )
  print ( '' )
  print ( 'p21 test_nonlin problem:' )
  print ( ' ', title )
  n = p21_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p21_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p21_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p21_sol ( n )
  if ( xe.size == 0 ):
    fjac = p21_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 21, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p21_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p21_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 21, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p21_title ( ):

#*****************************************************************************80
#
## p21_title() returns the title of problem 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Freudenstein-Roth function'

  return title

def p22_fx ( n, x ):

#*****************************************************************************80
#
## p22_fx() evaluates the function for problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  import numpy as np

  fx = np.zeros ( n )

  fx[0] = x[0] * x[0] - x[1] + 1.0
  fx[1] = x[0] - np.cos ( 0.5 * np.pi * x[1] )

  return fx

def p22_jac ( n, x ):

#*****************************************************************************80
#
## p22_jac() sets the jacobian for problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  fjac[0,0] = 2.0 * x[0]
  fjac[0,1] = - 1.0

  fjac[1,0] = 1.0
  fjac[1,1] = 0.5 * np.pi * np.sin ( 0.5 * np.pi * x[1] )

  return fjac

def p22_n ( ):

#*****************************************************************************80
#
## p22_n() returns the number of equations for problem 22.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = 2

  return n

def p22_sol ( n ):

#*****************************************************************************80
#
## p22_sol() returns the solution of problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np

  x = np.array ( [ 0.0, 1.0 ] )

  return x

def p22_start ( n ):

#*****************************************************************************80
#
## p22_start() specifies a standard approximate solution for problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.array ( [ 1.0, 0.0 ] )

  return x

def p22_test ( ):

#*****************************************************************************80
#
## p22_test() tests p22().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p22_title ( )
  print ( '' )
  print ( 'p22 test_nonlin problem:' )
  print ( ' ', title )
  n = p22_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p22_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p22_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p22_sol ( n )
  if ( xe.size == 0 ):
    fjac = p22_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 22, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p22_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p22_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 22, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p22_title ( ):

#*****************************************************************************80
#
## p22_title() returns the title of problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Boggs function'

  return title

def p23_fx ( n, x ):

#*****************************************************************************80
#
## p23_fx() evaluates the function for problem 23.
#
#    The Chandrasekhar H function is
#
#      F(H)(mu) = H(mu)
#        - 1 / ( 1 - c/2
#        * Integral ( 0 <= nu <= 1 ) [ mu * H(mu) / ( mu + nu ) ] dnu )
#
#    Applying the composite midpoint rule, and setting, for i = 1 to N,
#
#      mu(i) = ( i - 0.5 ) / N
#
#    we have the discrete function
#
#      F(h)(i) = h(i)
#        - 1 / ( 1 - c/(2N)
#        * sum ( 1 <= j <= N ) ( mu(i) * h(j) / ( mu(i) + mu(j) ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Subramanyan Chandrasekhar,
#    Radiative Transfer,
#    Dover, 1960,
#    ISBN13: 978-0486605906,
#    LC: QB461.C46.
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
#  Local:
#
#    real C, the constant, which must be between 0 and 1.
#
  import numpy as np

  fx = np.zeros ( n )

  c = 0.9

  fx[0:n] = x[0:n]

  mu = np.zeros ( n )
  for i in range ( 0, n ):
    mu[i] = ( 2 * i + 1 ) / ( 2 * n )

  for i in range ( 0, n ):

    s = 0.0
    for j in range ( 0, n ):
      s = s + ( mu[i] * x[j] ) / ( mu[i] + mu[j] )

    term = 1.0 - c * s / ( 2 * n )

    fx[i] = fx[i] - 1.0 / term

  return fx

def p23_jac ( n, x ):

#*****************************************************************************80
#
## p23_jac() sets the jacobian for problem 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    fjac[i,i] = 1.0

  c = 0.9

  mu = np.zeros ( n )
  for i in range ( 0, n ):
    mu[i] = ( 2 * i + 1 ) / ( 2 * n )

  for i in range ( 0, n ):

    term = 1.0 - c * np.sum ( mu[i] * x[0:n] / ( mu[i] + mu[0:n] ) ) / ( 2 * n )

    for j in range ( 0, n ):

      termp = c * mu[i] / ( mu[i] + mu[j] ) / ( 2 * n )

      fjac[i,j] = fjac[i,j] - ( termp / term ) / term

  return fjac

def p23_n ( ):

#*****************************************************************************80
#
## p23_n() returns the number of equations for problem 23.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  n = -1

  return n

def p23_sol ( n ):

#*****************************************************************************80
#
## p23_sol() returns the solution of problem 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  import numpy as np
  x = np.array ( [] )

  return x

def p23_start ( n ):

#*****************************************************************************80
#
## p23_start() specifies a standard approximate solution for problem 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  import numpy as np

  x = np.ones ( n )

  return x

def p23_test ( ):

#*****************************************************************************80
#
## p23_test() tests p23().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.linalg import norm
  from test_nonlin import p00_dif

  title = p23_title ( )
  print ( '' )
  print ( 'p23 test_nonlin problem:' )
  print ( ' ', title )
  n = p23_n ( )
  print ( '  Nominal value of n = ', n )
  if ( n <= 0 ):
    n = 5
    print ( '  Suggest using n = ', n )
  xs = p23_start ( n )
  print ( '  Suggested starting point xs = ', xs )
  fxs = p23_fx ( n, xs )
  print ( '  Norm of f(xs) = ', norm ( fxs ) )
  xe = p23_sol ( n )
  if ( xe.size == 0 ):
    fjac = p23_jac ( n, xs )
    print ( '  Jacobian at xs:' )
    print ( fjac )
    fdif = p00_dif ( 23, n, xs )
    print ( '  Finite difference jacobian at xs:' )
    print ( fdif )
    print ( '  Exact solution not given.' )
  else:
    print ( '  Approximate root xe = ', xe )
    fxe = p23_fx ( n, xe )
    print ( '  Norm of f(xe) = ', norm ( fxe ) )
    fjac = p23_jac ( n, xe )
    print ( '  Jacobian at xe:' )
    print ( fjac )
    fdif = p00_dif ( 23, n, xe )
    print ( '  Finite difference jacobian at xe:' )
    print ( fdif )

  return

def p23_title ( ):

#*****************************************************************************80
#
## p23_title() returns the title of problem 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Chandrasekhar function'

  return title

def p00_dif ( problem, n, x ):

#*****************************************************************************80
#
## p00_dif() approximates the jacobian via finite differences.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem number.
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the approximante jacobian matrix.
#
  import numpy as np

  fjac = np.zeros ( [ n, n ] )

  eps = 0.0001

  for j in range ( 0, n ):

    if ( 0.0 <= x[j] ):
      dxj = eps * ( x[j] + 1.0 )
    else:
      dxj = eps * ( x[j] - 1.0 )

    xsave = x[j]

    x[j] = xsave - dxj
    fminus = p00_fx ( problem, n, x )

    x[j] = xsave + dxj
    fplus = p00_fx ( problem, n, x )

    fjac[0:n,j] = ( fplus[0:n] - fminus[0:n] ) / 2.0 / dxj

    x[j] = xsave

  return fjac

def p00_fx ( problem, n, x ):

#*****************************************************************************80
#
## p00_fx() evaluates the function for any problem.
#
#  Discussion:
#
#    Most of the problems were originally part of ACM algorithm 566,
#    and were used to test the MINPACK package.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Dennis, David Gay, Phuong Vu,
#    A new nonlinear equations test problem,
#    Technical Report 83-16,
#    Mathematical Sciences Department,
#    Rice University, 1983.
#
#    John Dennis, Robert Schnabel,
#    Numerical Methods for Unconstrained Optimization
#    and Nonlinear Equations,
#    SIAM, 1996,
#    ISBN13: 978-0-898713-64-0,
#    LC: QA402.5.D44.
#
#    Noel deVilliers, David Glasser,
#    A continuation method for nonlinear regression,
#    SIAM Journal on Numerical Analysis,
#    Volume 18, Number 6, December 1981, pages 1139-1154.
#
#    Chris Fraley,
#    Solution of nonlinear least-squares problems,
#    Technical Report STAN-CS-1165,
#    Computer Science Department,
#    Stanford University, 1987.
#
#    Chris Fraley,
#    Software performance on nonlinear least-squares problems,
#    Technical Report SOL 88-17,
#    Systems Optimization Laboratory,
#    Department of Operations Research,
#    Stanford University, 1988.
#
#    JJ McKeown,
#    Specialized versus general-purpose algorithms for functions
#    that are sums of squared terms,
#    Mathematical Programming,
#    Volume 9, 1975, pages 57-68.
#
#    JJ McKeown,
#    On algorithms for sums of squares problems,
#    in Towards Global Optimisation,
#    edited by Laurence Dixon, Gabor Szego,
#    North-Holland, 1975, pages 229-257,
#    ISBN: 0444109552,
#    LC: QA402.5.T7.
#
#    Jorge More, Burton Garbow, Kenneth Hillstrom,
#    Algorithm 566:
#    Testing unconstrained optimization software,
#    ACM Transactions on Mathematical Software,
#    Volume 7, Number 1, March 1981, pages 17-41.
#
#    Douglas Salane,
#    A continuation approach for solving large residual nonlinear
#    least squares problems,
#    SIAM Journal of Scientific and Statistical Computing,
#    Volume 8, Number 4, July 1987, pages 655-671.
#
#  Input:
#
#    integer PROBLEM, the number of the problem.
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FX(N), the function value.
#
  if ( problem == 1 ):
    fx = p01_fx ( n, x )
  elif ( problem == 2 ):
    fx = p02_fx ( n, x )
  elif ( problem == 3 ):
    fx = p03_fx ( n, x )
  elif ( problem == 4 ):
    fx = p04_fx ( n, x )
  elif ( problem == 5 ):
    fx = p05_fx ( n, x )
  elif ( problem == 6 ):
    fx = p06_fx ( n, x )
  elif ( problem == 7 ):
    fx = p07_fx ( n, x )
  elif ( problem == 8 ):
    fx = p08_fx ( n, x )
  elif ( problem == 9 ):
    fx = p09_fx ( n, x )
  elif ( problem == 10 ):
    fx = p10_fx ( n, x )
  elif ( problem == 11 ):
    fx = p11_fx ( n, x )
  elif ( problem == 12 ):
    fx = p12_fx ( n, x )
  elif ( problem == 13 ):
    fx = p13_fx ( n, x )
  elif ( problem == 14 ):
    fx = p14_fx ( n, x )
  elif ( problem == 15 ):
    fx = p15_fx ( n, x )
  elif ( problem == 16 ):
    fx = p16_fx ( n, x )
  elif ( problem == 17 ):
    fx = p17_fx ( n, x )
  elif ( problem == 18 ):
    fx = p18_fx ( n, x )
  elif ( problem == 19 ):
    fx = p19_fx ( n, x )
  elif ( problem == 20 ):
    fx = p20_fx ( n, x )
  elif ( problem == 21 ):
    fx = p21_fx ( n, x )
  elif ( problem == 22 ):
    fx = p22_fx ( n, x )
  elif ( problem == 23 ):
    fx = p23_fx ( n, x )
  else:
    print ( '' )
    print ( 'p00_fx() - Fatal error!' )
    print ( '  Illegal problem number = ', problem )

  return fx

def p00_fx2 ( x, n, problem ):

#*****************************************************************************80
#
## p00_fx2() evaluates the function for any problem.
#
#  Discussion:
#
#    To use fsolve(), we need the first argument of the function to be x.
#    So p00_fx2 provides such an interface between fsolve and p00_fx.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the evaluation point.
#
#    integer N, the number of variables and equations.
#
#    integer PROBLEM, the number of the problem.
#
#  Output:
#
#    real FX(N), the function value.
#
# print ( 'p00_fx2 called with ', problem, ' ', n, ' ', x )

  fx = p00_fx ( problem, n, x )

  return fx

def p00_jac ( problem, n, x ):

#*****************************************************************************80
#
## p00_jac() evaluates the jacobian for any problem.
#
#  Discussion:
#
#    p00_jac evaluates the matrix FJAC(I,J)  =  D F(I) / D X(J)
#    given the problem chosen, the number of equations, and the value
#    of the point X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem number.
#
#    integer N, the number of variables and equations.
#
#    real X(N), the evaluation point.
#
#  Output:
#
#    real FJAC(N,N), the jacobian matrix.
#
  if ( problem == 1 ):
    fjac = p01_jac ( n, x )
  elif ( problem == 2 ):
    fjac = p02_jac ( n, x )
  elif ( problem == 3 ):
    fjac = p03_jac ( n, x )
  elif ( problem == 4 ):
    fjac = p04_jac ( n, x )
  elif ( problem == 5 ):
    fjac = p05_jac ( n, x )
  elif ( problem == 6 ):
    fjac = p06_jac ( n, x )
  elif ( problem == 7 ):
    fjac = p07_jac ( n, x )
  elif ( problem == 8 ):
    fjac = p08_jac ( n, x )
  elif ( problem == 9 ):
    fjac = p09_jac ( n, x )
  elif ( problem == 10 ):
    fjac = p10_jac ( n, x )
  elif ( problem == 11 ):
    fjac = p11_jac ( n, x )
  elif ( problem == 12 ):
    fjac = p12_jac ( n, x )
  elif ( problem == 13 ):
    fjac = p13_jac ( n, x )
  elif ( problem == 14 ):
    fjac = p14_jac ( n, x )
  elif ( problem == 15 ):
    fjac = p15_jac ( n, x )
  elif ( problem == 16 ):
    fjac = p16_jac ( n, x )
  elif ( problem == 17 ):
    fjac = p17_jac ( n, x )
  elif ( problem == 18 ):
    fjac = p18_jac ( n, x )
  elif ( problem == 19 ):
    fjac = p19_jac ( n, x )
  elif ( problem == 20 ):
    fjac = p20_jac ( n, x )
  elif ( problem == 21 ):
    fjac = p21_jac ( n, x )
  elif ( problem == 22 ):
    fjac = p22_jac ( n, x )
  elif ( problem == 23 ):
    fjac = p23_jac ( n, x )
  else:
    print ( '' )
    print ( 'p00_jac(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )
    raise Exception ( 'p00_jac - Fatal error!' )

  return fjac

def p00_n ( problem, rng ):

#*****************************************************************************80
#
## p00_n() returns the number of equations for a problem.
#
#  Discussion:
#
#    If N is positive, then N is the only value for the number
#    of equations for this problem.
#
#    If N is negative, then the absolute value of N is the
#    MINIMUM possible value for the number of equations for
#    this problem, and all larger values may also be used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem number.
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer N, the number of variables and equations.
#
  if ( problem == 1 ):
    n = p01_n ( )
  elif ( problem == 2 ):
    n = p02_n ( )
  elif ( problem == 3 ):
    n = p03_n ( )
  elif ( problem == 4 ):
    n = p04_n ( )
  elif ( problem == 5 ):
    n = p05_n ( )
  elif ( problem == 6 ):
    n = p06_n ( )
  elif ( problem == 7 ):
    n = p07_n ( rng )
  elif ( problem == 8 ):
    n = p08_n ( )
  elif ( problem == 9 ):
    n = p09_n ( )
  elif ( problem == 10 ):
    n = p10_n ( )
  elif ( problem == 11 ):
    n = p11_n ( )
  elif ( problem == 12 ):
    n = p12_n ( )
  elif ( problem == 13 ):
    n = p13_n ( )
  elif ( problem == 14 ):
    n = p14_n ( )
  elif ( problem == 15 ):
    n = p15_n ( )
  elif ( problem == 16 ):
    n = p16_n ( )
  elif ( problem == 17 ):
    n = p17_n ( )
  elif ( problem == 18 ):
    n = p18_n ( )
  elif ( problem == 19 ):
    n = p19_n ( )
  elif ( problem == 20 ):
    n = p20_n ( )
  elif ( problem == 21 ):
    n = p21_n ( )
  elif ( problem == 22 ):
    n = p22_n ( )
  elif ( problem == 23 ):
    n = p23_n ( )
  else:
    n = 0
    print ( '' )
    print ( 'p00_n(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )

  return n

def p00_problem_num ( ):

#*****************************************************************************80
#
## p00_problem_num() returns the number of problems available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer PROBLEM_nUM, the number of problems available.
#
  problem_num = 23

  return problem_num

def p00_sol ( problem, n, rng ):

#*****************************************************************************80
#
## p00_sol() returns the solution of any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem number.
#
#    integer N, the order of the system.  N is primarily
#    needed for problems where N may vary.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X(N), a solution value if known, or [].
#
  if ( problem == 1 ):
    x = p01_sol ( n )
  elif ( problem == 2 ):
    x = p02_sol ( n )
  elif ( problem == 3 ):
    x = p03_sol ( n )
  elif ( problem == 4 ):
    x = p04_sol ( n )
  elif ( problem == 5 ):
    x = p05_sol ( n )
  elif ( problem == 6 ):
    x = p06_sol ( n )
  elif ( problem == 7 ):
    x = p07_sol ( n )
  elif ( problem == 8 ):
    x = p08_sol ( n )
  elif ( problem == 9 ):
    x = p09_sol ( n )
  elif ( problem == 10 ):
    x = p10_sol ( n )
  elif ( problem == 11 ):
    x = p11_sol ( n )
  elif ( problem == 12 ):
    x = p12_sol ( n )
  elif ( problem == 13 ):
    x = p13_sol ( n )
  elif ( problem == 14 ):
    x = p14_sol ( n )
  elif ( problem == 15 ):
    x = p15_sol ( n )
  elif ( problem == 16 ):
    x = p16_sol ( n )
  elif ( problem == 17 ):
    x = p17_sol ( n )
  elif ( problem == 18 ):
    x = p18_sol ( n )
  elif ( problem == 19 ):
    x = p19_sol ( n )
  elif ( problem == 20 ):
    x = p20_sol ( n, rng )
  elif ( problem == 21 ):
    x = p21_sol ( n )
  elif ( problem == 22 ):
    x = p22_sol ( n )
  elif ( problem == 23 ):
    x = p23_sol ( n )
  else:
    print ( '' )
    print ( 'p00_sol - Fatal error!' )
    print ( '  Illegal problem number = ', problem )

  return x

def p00_start ( problem, n ):

#*****************************************************************************80
#
## p00_start() specifies a standard approximate solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, is the problem number.
#
#    integer N, is the number of variables and equations.
#
#  Output:
#
#    real X(N), the starting point.
#
  if ( problem == 1 ):
    x = p01_start ( n )
  elif ( problem == 2 ):
    x = p02_start ( n )
  elif ( problem == 3 ):
    x = p03_start ( n )
  elif ( problem == 4 ):
    x = p04_start ( n )
  elif ( problem == 5 ):
    x = p05_start ( n )
  elif ( problem == 6 ):
    x = p06_start ( n )
  elif ( problem == 7 ):
    x = p07_start ( n )
  elif ( problem == 8 ):
    x = p08_start ( n )
  elif ( problem == 9 ):
    x = p09_start ( n )
  elif ( problem == 10 ):
    x = p10_start ( n )
  elif ( problem == 11 ):
    x = p11_start ( n )
  elif ( problem == 12 ):
    x = p12_start ( n )
  elif ( problem == 13 ):
    x = p13_start ( n )
  elif ( problem == 14 ):
    x = p14_start ( n )
  elif ( problem == 15 ):
    x = p15_start ( n )
  elif ( problem == 16 ):
    x = p16_start ( n )
  elif ( problem == 17 ):
    x = p17_start ( n )
  elif ( problem == 18 ):
    x = p18_start ( n )
  elif ( problem == 19 ):
    x = p19_start ( n )
  elif ( problem == 20 ):
    x = p20_start ( n )
  elif ( problem == 21 ):
    x = p21_start ( n )
  elif ( problem == 22 ):
    x = p22_start ( n )
  elif ( problem == 23 ):
    x = p23_start ( n )
  else:
    print ( '' )
    print ( 'p00_start - Fatal error!' )
    print ( '  Illegal problem number = ', problem )

  return x

def p00_title ( problem ):

#*****************************************************************************80
#
## p00_title() returns the title of the problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem number.
#
#  Output:
#
#    string TITLE, the title of the problem.
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
  elif ( problem == 9 ):
    title = p09_title ( )
  elif ( problem == 10 ):
    title = p10_title ( )
  elif ( problem == 11 ):
    title = p11_title ( )
  elif ( problem == 12 ):
    title = p12_title ( )
  elif ( problem == 13 ):
    title = p13_title ( )
  elif ( problem == 14 ):
    title = p14_title ( )
  elif ( problem == 15 ):
    title = p15_title ( )
  elif ( problem == 16 ):
    title = p16_title ( )
  elif ( problem == 17 ):
    title = p17_title ( )
  elif ( problem == 18 ):
    title = p18_title ( )
  elif ( problem == 19 ):
    title = p19_title ( )
  elif ( problem == 20 ):
    title = p20_title ( )
  elif ( problem == 21 ):
    title = p21_title ( )
  elif ( problem == 22 ):
    title = p22_title ( )
  elif ( problem == 23 ):
    title = p23_title ( )
  else:
    title = ''
    print ( '' )
    print ( 'p00_title(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )

  return title

def nonlin_fsolve_test ( rng ):

#*****************************************************************************80
#
## nonlin_fsolve_test() uses fsolve() to seek a solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  from scipy.linalg import norm
  from scipy.optimize import fsolve

  print ( '' )
  print ( 'nonlin_fsolve_test' )
  print ( '  Seek a root using fsolve()' )
  print ( '' )
  print ( '   #    ------------------------------------------' )
  print ( 'Title    N     ||F(start)||   ||F(root)||' )
  print ( '' )

  problem_num = p00_problem_num ( )

  for problem in range ( 1, problem_num + 1 ):

    title = p00_title ( problem )
    print ( '  %2d  %-50s' % ( problem, title ), end = '' )

    n = p00_n ( problem, rng )
    if ( n < 0 ):
      n = 10

    print ( '  %2d' % ( n ), end = '' )

    x0 = p00_start ( problem, n )
    fx0 = p00_fx ( problem, n, x0 )
    print ( '  %10.6g' % ( norm ( fx0 ) ), end = '' )
#
#  Bizarre interface to fsolve assumes the function has the
#  variable of interest as the first argument, and subsequent
#  arguments given in the args= list.
#
#  I had to create a special interface function p00_fx2() to
#  implement this.
#
    x1 = fsolve ( p00_fx2, x0, args = ( n, problem ) )
    fx1 = p00_fx ( problem, n, x1 )
    print ( '  %10.6g' % ( norm ( fx1 ) ) )

  return

def test_nonlin_test ( ):

#*****************************************************************************80
#
## test_nonlin_test() tests test_nonlin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'test_nonlin_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  test_nonlin() defines a set of sample systems of' )
  print ( '  nonlinear equations.' )

  rng = default_rng ( )
#
#  Call each sample problem.
#
  p01_test ( )
  p02_test ( )
  p03_test ( )
  p04_test ( )
  p05_test ( )
  p06_test ( )
  p07_test ( rng )
  p08_test ( )
  p09_test ( )
  p10_test ( )
  p11_test ( )
  p12_test ( )
  p13_test ( )
  p14_test ( )
  p15_test ( )
  p16_test ( )
  p17_test ( )
  p18_test ( )
  p19_test ( )
  p20_test ( rng )
  p21_test ( )
  p22_test ( )
  p23_test ( )
#
#  Seek a solution using fsolve().
#
  nonlin_fsolve_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_nonlin_test():' )
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
  test_nonlin_test ( )
  timestamp ( )
 
