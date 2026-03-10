#! /usr/bin/env python3
#
def gradient_descent_test ( ):

#*****************************************************************************80
#
## gradient_descent_test() tests gradient_descent().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2022
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'gradient_descent_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  gradient_descent() seeks the minimizer of a function' )
  print ( '  using the method of gradient descent.' )

  gradient_descent_linear_test ( )
  gradient_descent_nonlinear_test ( )
  gradient_descent_vector_x_test ( )
  gradient_descent_vector_f_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'gradient_descent_test():' )
  print ( '  Normal end of execution.' )

  return

def gradient_descent_linear ( A, b, alpha, tol, it_max ):

#*****************************************************************************80
#
## gradient_descent_linear() solves a least squares problem using gradient descent.
#
#  Discusssion:
#
#    We are given an MxN matrix A and a right hand side M-vector B.
#    We seek an N-vector X which minimizes the L2 norm |A*X-B|.
#    We apply gradient descent to the function f(x) = 1/2 ||A*x-b||^2
#    with derivative f'(x) = A'*x
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2022
#
#  Author:
#
#    Original R code by James Howard
#    This version by John Burkardt.
#
#  Reference:
#
#    James Howard,
#    Computational Methods for Numerical Analysis with R,
#    CRC Press, 2017,
#    ISBN13: 978-1-4987-2363-3.
#
#  Input:
#
#    real A(M,N): the matrix.
#
#    real B(M): the right hand side.
#
#    real ALPHA: the stepsize.
#
#    real TOL: the step tolerance.
#
#    integer IT_MAX: the maximum number of steps.
#
#  Output:
#
#    real X(N): the approximate least squares solution.
#
#    integer IT: the number of steps taken.
#
  import numpy as np

  m, n = A.shape
  x = np.zeros ( n )

  for it in range ( 0, it_max ):

    e = np.dot ( A, x ) - b
    d = np.dot ( np.transpose ( A ), e )
    xold = x
    x = x - alpha * d

    if ( np.linalg.norm ( x - xold ) < tol ):
      break

  return x, it

def gradient_descent_linear_test ( ):

#*****************************************************************************80
#
## gradient_descent_linear_test() tests gradient_descent_linear().
#
#  Discussion:
#
#    This code suggests how slowly a simple gradient descent method will
#    converge to the solution of a linear least squares problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 July 2022
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'gradient_descent_linear_test():' )
  print ( '  gradient_descent_linear() approximates the solution of a linear' )
  print ( '  problem A*x=b, by minimizing ||Ax-b|| using gradient descent.' )

  A = np.array ( [ \
   [ 1.47, 1.0 ], \
   [ 1.50, 1.0 ], \
   [ 1.52, 1.0 ], \
   [ 1.55, 1.0 ], \
   [ 1.57, 1.0 ], \
   [ 1.60, 1.0 ], \
   [ 1.63, 1.0 ], \
   [ 1.65, 1.0 ], \
   [ 1.68, 1.0 ], \
   [ 1.70, 1.0 ], \
   [ 1.73, 1.0 ], \
   [ 1.75, 1.0 ], \
   [ 1.78, 1.0 ], \
   [ 1.80, 1.0 ], \
   [ 1.83, 1.0 ] ] )

  m, n = A.shape

  b = np.array ( [ \
    52.21, \
    53.12, \
    54.48, \
    55.84, \
    57.20, \
    58.57, \
    59.93, \
    61.29, \
    63.11, \
    64.47, \
    66.28, \
    68.10, \
    69.92, \
    72.19, \
    74.46 ] )

  alpha = 0.02
  tol = 1.0e-6
  it_max = 10000

  print ( '' )
  print ( '  Learning rate = ', alpha )
  print ( '  Stepsize tolerance = ', tol )
  print ( '  Maximum iterations = ', it_max )

  x_exact = np.array ( [ 61.272, -39.062 ] )

  x, it = gradient_descent_linear ( A, b, alpha, tol, it_max )

  print ( '' )
  print ( '  Number of iterations = ', it )
  print ( '  Estimated solution:' )
  print ( x )
  print ( '  Exact solution:' )
  print ( x_exact )
  print ( '' )
  print ( '  ||x-x_exact||   = ', np.linalg.norm ( x - x_exact ) )
  print ( '  ||A*x-b||       = ', \
    np.linalg.norm ( b - np.dot ( A, x ) ) )
  print ( '  ||A*x_exact-b|| = ', \
    np.linalg.norm ( b - np.dot ( A, x_exact ) ) )

  return

def gradient_descent_nonlinear ( f, df, x, it_max, eta ):

#*****************************************************************************80
#
## gradient_descent_nonlinear(): gradient descent for scalar nonlinear f(x).
#
#  Discusssion:
#
#    We are given a scalar nonlinear function f(x) and want to estimate
#    the location of a local minimizer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2022
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real value = F(X): evaluates the function.
#
#    real value = DF(X): evaluates the derivative of the function.
#
#    real X: the initial guess for the minimizer.
#
#    integer IT_MAX: the maximum number of steps.
#
#    real ETA: the learning rate.
#
#  Output:
#
#    real X: the estimated minimizer.
#
#    integer IT: the number of steps taken.
#
  print_out = True

  if ( print_out ):
    print ( '' )
    print ( '   it      x               f(x)         f\'(x)' )
    print ( '' )

  for it in range ( 0, it_max + 1 ):

    if ( 0 < it ):
      xold = x
      x = x - eta * df ( x ) * f ( x )

    if ( print_out ):
      print ( '  %3d  %12.8g  %12.8g  %12.8g' % ( it, x, f ( x ), df ( x ) ) )

  return x, it

def gradient_descent_nonlinear_test ( ):

#*****************************************************************************80
#
## gradient_descent_nonlinear_test() tests gradient descent for nonlinear f.
#
#  Discussion:
#
#    The quartic function is
#    f(x) = 2.0 * x ^ 4 - 4.0 * x ^ 2 + x + 20.0
#
#    We seek a minimizer of f(x) in the range -2 <= x <= 2.
#
#    The gradient_descent0() method uses a very simple version of
#    the algorithm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np

  a = -2.0
  b = +2.0

  print ( '' )
  print ( 'gradient_descent_nonlinear_test():' )
  print ( '  Seek local minimizer of a scalar function quartic(x)' )
  print ( '  Minimizer is probably in the interval [', a, ',', b, ']' )
  print ( '  Use a very simple version of the gradient descent method.' )
#
#  Plot the function.
#
  plt.clf ( )
  xvec = np.linspace ( a, b, 101 )
  fxvec = quartic ( xvec )
  plt.plot ( xvec, fxvec, linewidth = 3 )
  plt.plot ( [ a, b ], [ 0, 0 ], 'k', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- X -->' )
  plt.ylabel ( '<-- F(X) -->' )
  plt.title ( 'Quartic function' )
  filename = 'quartic.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Choose a random initial guess, or choose x = -1.5.
#
  rng = default_rng()
  x0 = a + ( b - a ) * rng.random ( )
  x0 = - 1.5
#
#  Maximum number of iterations.
#
  itmax = 40
#
#  Choose a small learning rate.
#
  eta = 0.005
#
#  Seek minimizer.
#
  x, it = gradient_descent_nonlinear ( quartic, quartic_df, x0, itmax, eta )

  print ( '' )
  print ( '  ', it, ' gradient descent steps were taken.' )
  print ( '  Initial x = ', x0, \
          '  f(x) = ', quartic ( x0 ), \
          '  f\'(x) = ', quartic_df(x0) )
  print ( '  Final x = ', x, \
          '  f(x) = ', quartic ( x ), \
          '  f\'(x) = ', quartic_df(x) )
#
#  Plot the function with initial point and local minimizer.
#
  plt.clf ( )
  xvec = np.linspace ( a, b, 101 )
  fxvec = quartic ( xvec )
  plt.plot ( xvec, fxvec, linewidth = 3 )
  plt.plot ( [ x0, x0 ], [ 0, quartic(x0) ], 'b', linewidth = 3 )
  plt.plot ( x0,  0.0, 'bo', markersize = 10 )
  plt.plot ( x0,  quartic ( x0 ), 'bo', markersize = 10 )
  plt.plot ( [ x, x ], [ 0, quartic(x) ], 'r', linewidth = 3 )
  plt.plot ( x,  0.0, 'ro', markersize = 10 )
  plt.plot ( x,  quartic ( x ), 'ro', markersize = 10 )
  plt.plot ( [ a, b ], [ 0, 0 ], 'k', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- X -->' )
  plt.ylabel ( '<-- F(X) -->' )
  plt.title ( 'Initial point blue, minimizer red' )
  filename = 'quartic_minimizer.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def quartic ( x ):

#*****************************************************************************80
#
## quartic() evaluates a quartic function.
#
#  Discussion:
#
#    The quartic function is
#    f(x) = 2.0 * x ^ 4 - 4.0 * x ^ 2 + x + 20.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X: the evaluation point.
#
#  Output:
#
#    real VALUE: the function value.
#
  value = 2.0 * x**4 - 4.0 * x**2 + x + 20.0

  return value

def quartic_df ( x ):

#*****************************************************************************80
#
## quartic_df() evaluates the derivative of a quartic function.
#
#  Discussion:
#
#    The quartic function is
#    f(x) = 2.0 * x ^ 4 - 4.0 * x ^ 2 + x + 20.0
#
#    The quartic function is
#    f'(x) = 8.0 * x ^ 3 - 8.0 * x + 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X: the evaluation point.
#
#  Output:
#
#    real VALUE: the derivative value.
#
  value = 8.0 * x**3 - 8.0 * x + 1.0

  return value

def gradient_descent_vector_x ( f, df, x, it_max, alpha ):

#*****************************************************************************80
#
## gradient_descent_vector_x(): f(x) is scalar, x is a vector.
#
#  Discusssion:
#
#    We are given a scalar nonlinear function f(x) of a vector argument x,
#    and want to estimate the location of a local minimizer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2022
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real value = F(X): evaluates the function.
#
#    real value = DF(X): evaluates the derivative of the function.
#
#    real X(N): the initial guess for the minimizer.
#
#    integer IT_MAX: the maximum number of steps.
#
#    real ALPHA: the learning rate.
#
#  Output:
#
#    real X(N): the estimated minimizer.
#
  import numpy as np

  print_out = False

  if ( print_out ):
    print ( '' )
    print ( '   it      ||x||               f(x)         ||f\'(x)||' )
    print ( '' )

  for it in range ( 0, it_max + 1 ):

    if ( 0 < it ):
      x = x - alpha * df ( x ) * f ( x )

    if ( print_out ):
      print ( '  %3d  %12.8g  %12.8g  %12.8g' \
        % ( it, np.linalg.norm ( x ), f ( x ), np.linalg.norm ( df ( x ) ) ) )

  return x

def gradient_descent_vector_x_test ( ):

#*****************************************************************************80
#
## gradient_descent_vector_x_test() uses gradient descent on a vector problem.
#
#  Discussion:
#
#    We apply gradient descent to minimize the L2 norm of a scalar function 
#    f(x) of a vector argument x.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'gradient_descent_vector_x_test():' )
  print ( '  Seek minimizer of a function z(x,y).' )
#
#  Choose an initial guess.
# 
  x0 = np.array ( [ 1.0, 1.5 ] )
#
#  Choose a small learning rate.
#
  alpha = 0.15
#
#  Maximum number of iterations
#
  it_max = 10000

  x = gradient_descent_vector_x ( hex2, hex2_df, x0, it_max, alpha )

  print ( '' )
  print ( '  Initial x,y = ', x0, \
          '  f(x,y) = ', hex2 ( x0 ), \
          '  f\'(x,y) = ', hex2_df ( x0 ) )

  print ( '  Final x,y = ', x, \
          '  f(x,y) = ', hex2 ( x ), \
          '  f\'(x,y) = ', hex2_df ( x ) )

  return

def hex2 ( xy ):

#*****************************************************************************80
#
## hex2 evaluates the hex2 function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2022
#
#  Input:
#
#    real xy(2): the x and y arguments.
#
#  Output:
#
#    real value: the function value.
#
  x = xy[0]
  y = xy[1]
  value = 2.0 * x**2 - 1.05 * x**4 + x**6 / 6.0 + x * y + y**2

  return value

def hex2_df ( xy ):

#*****************************************************************************80
#
## hex2_df evaluates the hex2 gradient.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2022
#
#  Input:
#
#    real xy(2): the x and y arguments.
#
#  Output:
#
#    real value(2): the gradient vector.
#
  import numpy as np

  x = xy[0]
  y = xy[1]

  value = np.array ( [ \
    4.0 * x - 4.2 * x**3 + x**5 + y,
    x + 2.0 * y ] )

  return value

def gradient_descent_vector_f ( f, df, x, it_max, alpha ):

#*****************************************************************************80
#
## gradient_descent_vector_f(): f(x) is vector, x is a vector.
#
#  Discusssion:
#
#    We are given a nonlinear vector function f(x) of a vector argument x,
#    and want to estimate the location of a local minimizer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2022
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real value = F(X): evaluates the function.
#
#    real value = DF(X): evaluates the derivative of the function.
#
#    real X(N): the initial guess for the minimizer.
#
#    integer IT_MAX: the maximum number of steps.
#
#    real ALPHA: the learning rate.
#
#  Output:
#
#    real X(N): the estimated minimizer.
#
  import numpy as np

  print_out = True

  if ( print_out ):
    print ( '' )
    print ( '   it      ||x||             ||f(x)||       ||J(x)||' )
    print ( '' )

  for it in range ( 0, it_max + 1 ):

    if ( 0 < it ):
      x = x - alpha * np.matmul ( np.transpose ( df ( x ) ), f ( x ) )

    if ( print_out ):
      print ( '  %3d  %12.8g  %12.8g  %12.8g' % ( \
        it, \
        np.linalg.norm ( x ), \
        0.5 * ( np.linalg.norm ( f ( x ) ) )**2, \
        np.linalg.norm ( df ( x ), 'fro' ) ) )

  return x

def gradient_descent_vector_f_test ( ):

#*****************************************************************************80
#
## gradient_descent_vector_f_test() uses gradient descent on a vector problem.
#
#  Discussion:
#
#    We apply gradient descent to minimize the L2 norm of a vector function 
#    f(x) of a vector argument x.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'gradient_descent_vector_f_test():' )
  print ( '  Seek minimizer of vector function f(x).' )
#
#  Choose an initial guess.
# 
# x0 = np.array ( [ [ 0.0 ], [ 0.0 ], [ 0.0 ] ] )
  x0 = np.array ( [ 0.0, 0.0, 0.0 ] )
#
#  Maximum number of iterations
#
  it_max = 83
#
#  Choose a small learning rate.
#
  alpha = 0.001

  x = gradient_descent_vector_f ( wiki3, wiki3_df, x0, it_max, alpha )

  print ( '' )
  print ( '  Initial x = (%g,%g,%g)' % ( x0[0], x0[1], x0[2] ) )
  temp = 0.5 * ( np.linalg.norm ( wiki3 ( x0 ) ) )**2
  print ( '  ||f(x)|| = ', temp )
  temp = np.linalg.norm ( wiki3_df ( x0 ), 'fro' )
  print ( '  ||J(x)|| = ', temp )
  print ( '' )
  print ( '  Final x = (%g,%g,%g)' % ( x[0], x[1], x[2] ) )
  temp = 0.5 * ( np.linalg.norm ( wiki3 ( x ) ) )**2
  print ( '  ||f(x)|| = ', temp )
  temp = np.linalg.norm ( wiki3_df ( x ), 'fro' )
  print ( '  ||J(x)|| = ', temp )

  return

def wiki3 ( xyz ):

#*****************************************************************************80
#
## wiki3() evaluates the wiki3 function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2022
#
#  Input:
#
#    real xyz(3): the arguments.
#
#  Output:
#
#    real value[3): the function value.
#
  import numpy as np

  x = xyz[0]
  y = xyz[1]
  z = xyz[2]

  value = np.zeros ( 3 )

  value[0] = 3.0 * x - np.cos ( y * z ) - 3.0 / 2.0
  value[1] = 4.0 * x**2 - 625.0 * y**2 + 2.0 * y - 1.0
  value[2] = np.exp ( - x * y ) + 20.0 * z + ( 10.0 * np.pi - 3.0 ) / 3.0

  return value

def wiki3_df ( xyz ):

#*****************************************************************************80
#
## wiki3_df() evaluates the wiki3 jacobian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2022
#
#  Input:
#
#    real xyz(3): the arguments.
#
#  Output:
#
#    real value[3,3): the Jacobian matrix.
#
  import numpy as np

  x = xyz[0]
  y = xyz[1]
  z = xyz[2]

  value = np.zeros ( [ 3, 3 ] )

  value[0,0] = 3.0
  value[0,1] = np.sin ( y * z ) * z
  value[0,2] = np.sin ( y * z ) * y
  value[1,0] = 8.0 * x
  value[1,1] =  - 1250.0 * y + 2.0
  value[1,2] = 0.0
  value[2,0] = - y * np.exp ( - x * y )
  value[2,1] = - x * np.exp ( - x * y )
  value[2,2] = 20.0

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
  gradient_descent_test ( )
  timestamp ( )

