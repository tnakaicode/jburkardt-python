#! /usr/bin/env python3
#
def best_nearby ( delta, point, prevbest, nvars, f, funevals ):

#*****************************************************************************80
#
## best_nearby() looks for a better nearby point, one coordinate at a time.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2016
#
#  Author:
#
#    Original ALGOL version by Arthur Kaupe.
#    C version by Mark Johnson.
#    This version by John Burkardt.
#
#  Reference:
#
#    M Bell, Malcolm Pike,
#    Remark on Algorithm 178: Direct Search,
#    Communications of the ACM,
#    Volume 9, Number 9, September 1966, page 684.
#
#    Robert Hooke, Terry Jeeves,
#    Direct Search Solution of Numerical and Statistical Problems,
#    Journal of the ACM,
#    Volume 8, Number 2, April 1961, pages 212-229.
#
#    Arthur Kaupe,
#    Algorithm 178:
#    Direct Search,
#    Communications of the ACM,
#    Volume 6, Number 6, June 1963, page 313.
#
#    FK Tomlin, LB Smith,
#    Remark on Algorithm 178: Direct Search,
#    Communications of the ACM,
#    Volume 12, Number 11, November 1969, page 637-638.
#
#  Input:
#
#    real DELTA(NVARS), the size of a step in each direction.
#
#    real POINT(NVARS); on the current candidate.
#    On the value of POINT may have been updated.
#
#    real PREVBEST, the minimum value of the function seen
#    so far.
#
#    integer NVARS, the number of variables.
#
#    function handle F, the name of the function routine,
#    which should have the form:
#      function value = f ( x, n )
#
#    integer FUNEVALS, the number of function evaluations.
#
#  Output:
#
#    real NEWBEST, the minimum value of the function seen
#    after checking the nearby neighbors.
#
#    real POINT(NVARS); the value of POINT may have been updated.
#
#    integer FUNEVALS, the number of function evaluations.
#
  import numpy as np

  z = point.copy ( )

  minf = prevbest

  for i in range ( 0, nvars ):

    z[i] = point[i] + delta[i]

    ftmp = f ( z, nvars )
    funevals = funevals + 1

    if ( ftmp < minf ):

      minf = ftmp

    else:

      delta[i] = - delta[i]
      z[i] = point[i] + delta[i]
      ftmp = f ( z, nvars )
      funevals = funevals + 1

      if ( ftmp < minf ):
        minf = ftmp
      else:
        z[i] = point[i]

  point = z.copy ( )
  newbest = minf

  return newbest, point, funevals

def hooke ( nvars, startpt, rho, eps, itermax, f ):

#*****************************************************************************80
#
## hooke() seeks a minimizer of a scalar function of several variables.
#
#  Discussion:
#
#    This routine find a point X where the nonlinear objective function
#    F(X) has a local minimum.  X is an N-vector and F(X) is a scalar.
#    The objective function F(X) is not required to be differentiable
#    or even continuous.  The program does not use or require derivatives
#    of the objective function.
#
#    The user supplies three things:
#    1) a subroutine that computes F(X),
#    2) an initial "starting guess" of the minimum point X,
#    3) values for the algorithm convergence tolerances.
#
#    The program searches for a local minimum, beginning from the
#    starting guess, using the Direct Search algorithm of Hooke and
#    Jeeves.
#
#    This program is adapted from the Algol pseudocode found in the
#    paper by Kaupe, and includes improvements suggested by Bell and Pike,
#    and by Tomlin and Smith.
#
#    The algorithm works by taking "steps" from one estimate of
#    a minimum, to another (hopefully better) estimate.  Taking
#    big steps gets to the minimum more quickly, at the risk of
#    "stepping right over" an excellent point.  The stepsize is
#    controlled by a user supplied parameter called RHO.  At each
#    iteration, the stepsize is multiplied by RHO  (0 < RHO < 1),
#    so the stepsize is successively reduced.
#
#    Small values of rho correspond to big stepsize changes,
#    which make the algorithm run more quickly.  However, there
#    is a chance (especially with highly nonlinear functions)
#    that these big changes will accidentally overlook a
#    promising search vector, leading to nonconvergence.
#
#    Large values of RHO correspond to small stepsize changes,
#    which force the algorithm to carefully examine nearby points
#    instead of optimistically forging ahead.  This improves the
#    probability of convergence.
#
#    The stepsize is reduced until it is equal to (or smaller
#    than) EPS.  So the number of iterations performed by
#    Hooke-Jeeves is determined by RHO and EPS:
#
#      RHO^(number_of_iterations) = EPS
#
#    In general it is a good idea to set RHO to an aggressively
#    small value like 0.5 (hoping for fast convergence).  Then,
#    if the user suspects that the reported minimum is incorrect
#    (or perhaps not accurate enough), the program can be run
#    again with a larger value of RHO such as 0.85, using the
#    result of the first minimization as the starting guess to
#    begin the second minimization.
#
#    Normal use:
#    (1) Code your function F();
#    (2) Install your starting guess;
#    (3) Run the program.
#
#    If there are doubts about the result, the computed minimizer
#    can be used as the starting point for a second minimization attempt.
#
#    To apply this method to data fitting, code your function F() to be
#    the sum of the squares of the errors (differences) between the
#    computed values and the measured values.  Then minimize F()
#    using Hooke-Jeeves.
#
#    For example, you have 20 datapoints (T(i), Y(i)) and you want to
#    find A, B and C so that:
#
#      A*t*t + B*exp(t) + C*tan(t)
#
#    fits the data as closely as possible.  Then the objective function
#    F() to be minimized is just
#
#      F(A,B,C) = sum ( 1 <= i <= 20 )
#        ( y(i) - A*t(i)*t(i) - B*exp(t(i)) - C*tan(t(i)) )^2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2016
#
#  Author:
#
#    Original ALGOL version by Arthur Kaupe.
#    C version by Mark Johnson.
#    This version by John Burkardt.
#
#  Reference:
#
#    M Bell, Malcolm Pike,
#    Remark on Algorithm 178: Direct Search,
#    Communications of the ACM,
#    Volume 9, Number 9, September 1966, page 684.
#
#    Robert Hooke, Terry Jeeves,
#    Direct Search Solution of Numerical and Statistical Problems,
#    Journal of the ACM,
#    Volume 8, Number 2, April 1961, pages 212-229.
#
#    Arthur Kaupe,
#    Algorithm 178:
#    Direct Search,
#    Communications of the ACM,
#    Volume 6, Number 6, June 1963, page 313.
#
#    FK Tomlin, LB Smith,
#    Remark on Algorithm 178: Direct Search,
#    Communications of the ACM,
#    Volume 12, Number 11, November 1969, page 637-638.
#
#  Input:
#
#    integer NVARS, the number of spatial dimensions.
#
#    real STARTPT(NVARS), the user-supplied
#    initial estimate for the minimizer.
#
#    real RHO, a user-supplied convergence parameter
#    which should be set to a value between 0.0 and 1.0.  Larger values
#    of RHO give greater probability of convergence on highly nonlinear
#    functions, at a cost of more function evaluations.  Smaller
#    values of RHO reduce the number of evaluations and the program
#    running time, but increases the risk of nonconvergence.
#
#    real EPS, the criterion for halting
#    the search for a minimum.  When the algorithm
#    begins to make less and less progress on each
#    iteration, it checks the halting criterion: if
#    the stepsize is below EPS, end the
#    iteration and return the current best estimate
#    of the minimum.  Larger values of EPS (such
#    as 1.0e-4) give quicker running time, but a
#    less accurate estimate of the minimum.  Smaller
#    values of EPS (such as 1.0e-7) give longer
#    running time, but a more accurate estimate of
#    the minimum.
#
#    integer ITERMAX, a limit on the number of iterations.
#
#    function handle F, the name of the function routine,
#    which should have the form:
#      function value = f ( x, n )
#
#  Output:
#
#    integer ITERS, the number of iterations taken.
#
#    real ENDPT(NVARS), the estimate for the
#    minimizer, as calculated by the program.
#
  import numpy as np

  verbose = False

  newx = startpt.copy ( )
  xbefore = startpt.copy ( )
  
  delta = np.zeros ( nvars )

  for i in range ( 0, nvars ):
    if ( startpt[i] == 0.0 ):
      delta[i] = rho
    else:
      delta[i] = rho * abs ( startpt[i] )

  funevals = 0
  steplength = rho
  iters = 0
  fbefore = f ( newx, nvars )
  funevals = funevals + 1
  newf = fbefore

  while ( iters < itermax and eps < steplength ):

    iters = iters + 1

    if ( verbose ):

      print ( '' )
      print ( '  FUNEVALS = %d, F(X) = %g' % ( funevals, fbefore ) )
      for i in range ( 0, nvars ):
        print ( '  %8d  %g' % ( i, xbefore[i] ) )
#
#  Find best new point, one coordinate at a time.
#
    for i in range ( 0, nvars ):
      newx[i] = xbefore[i]

    newf, newx, funevals = best_nearby ( delta, newx, fbefore, nvars, f, funevals )
#
#  If we made some improvements, pursue that direction.
#
    keep = True

    while ( newf < fbefore and keep ):

      for i in range ( 0, nvars ):
#
#  Arrange the sign of DELTA.
#
        if ( newx[i] <= xbefore[i] ):
          delta[i] = - abs ( delta[i] )
        else:
          delta[i] = abs ( delta[i] )
#
#  Now, move further in this direction.
#
        tmp = xbefore[i]
        xbefore[i] = newx[i]
        newx[i] = newx[i] + newx[i] - tmp

      fbefore = newf
      newf, newx, funevals = best_nearby ( delta, newx, fbefore, nvars, f, \
        funevals )
#
#  If the further (optimistic) move was bad...
#
      if ( fbefore <= newf ):
        break
#
#  Make sure that the differences between the new and the old points
#  are due to actual displacements; beware of roundoff errors that
#  might cause NEWF < FBEFORE.
#
      keep = False

      for i in range ( 0, nvars ):
        if ( 0.5 * abs ( delta[i] ) < abs ( newx[i] - xbefore[i] ) ):
          keep = True
          break

    if ( eps <= steplength and fbefore <= newf ):
      steplength = steplength * rho
      for i in range ( 0, nvars ):
        delta[i] = delta[i] * rho

  endpt = xbefore.copy ( )

  return iters, endpt

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def rosenbrock ( x, n ):

#*****************************************************************************80
#
## rosenbrock() evaluates the Rosenbrock function.
#
#  Discussion:
#
#    The Hooke and Jeeves algorithm works reasonably well on
#    Rosenbrock's test function, depending on the value of RHO chosen.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the argument of the function.
#
#    integer N, the spatial dimension.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  value = 100.0 * ( x[1] - x[0] * x[0] ) ** 2 \
             +    ( 1.0 - x[0] ) ** 2

  return value

def rosenbrock_test ( ):

#*****************************************************************************80
#
## rosenbrock_test() tests hooke() with the Rosenbrock function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  nvars = 2

  print ( '' )
  print ( 'rosenbrock_test():' )
  print ( '  hooke() seeks a minimizer of F(X).' )
  print ( '  Here we use the Rosenbrock function.' )
#
#  Starting guess for Rosenbrock.
#
  startpt = np.array ( [ -1.2, 1.0 ] )

  r8vec_print ( nvars, startpt, '  Initial estimate for X:' )

  value = rosenbrock ( startpt, nvars )

  print ( '' )
  print ( '  F(X) = %g' % ( value ) )
#
#  Call HOOKE.
#
  itermax = 5000
  rho = 0.5
  eps = 1.0E-06

  it, endpt = hooke ( nvars, startpt, rho, eps, itermax, rosenbrock )
#
#  Results.
#
  print ( '' )
  print ( '  Number of iterations taken = %d' % ( it ) )

  r8vec_print ( nvars, endpt, '  Final estimate for X:' )

  value = rosenbrock ( endpt, nvars )

  print ( '' )
  print ( '  F(X*) = %g' % ( value ) )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def toms178_test ( ):

#*****************************************************************************80
#
## toms178_test() tests toms178().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'toms178_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test toms178().' )

  rosenbrock_test ( )
  woods_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'toms178_test():' )
  print ( '  Normal end of execution.' )
  return

def woods ( x, n ):

#*****************************************************************************80
#
## woods() evaluates the Woods function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the argument of the function.
#
#    integer N, the spatial dimension.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  s1 = x[1] - x[0] * x[0]
  s2 = 1.0 - x[0]
  s3 = x[1] - 1.0
  t1 = x[3] - x[2] * x[2]
  t2 = 1.0 - x[2]
  t3 = x[3] - 1.0
  t4 = s3 + t3
  t5 = s3 - t3

  value = 100.0 * s1 * s1 \
        +         s2 * s2 \
        +  90.0 * t1 * t1 \
        +         t2 * t2 \
        +  10.0 * t4 * t4 \
        +   0.1 * t5 * t5

  return value

def woods_test ( ):

#*****************************************************************************80
#
## woods_test() tests hooke() with the WOODS function.
#
#  Discussion:
#
#    The Hooke and Jeeves algorithm works well when RHO = 0.5, but
#    does poorly when RHO = 0.6, and better when RHO = 0.8
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  nvars = 4

  print ( '' )
  print ( 'woods_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  hooke() seeks a minimizer of F(X).' )
  print ( '  Here we use the Woods function.' )
#
#  Starting guess.
#
  startpt = np.array ( [ -3.0, -1.0, -3.0,  -1.0 ] )

  r8vec_print ( nvars, startpt, '  Initial estimate for X:' )

  value = woods ( startpt, nvars )

  print ( '' )
  print ( '  F(X) = %g' % ( value ) )
#
#  Call HOOKE.
#
  itermax = 5000
  rho = 0.5
  eps = 1.0E-06

  it, endpt = hooke ( nvars, startpt, rho, eps, itermax, woods )
#
#  Results.
#
  print ( '' )
  print ( '  Number of iterations taken = %d' % ( it ) )
  print ( '' )

  r8vec_print ( nvars, endpt, '  Final estimate for X:' )

  value = woods ( endpt, nvars )

  print ( '' )
  print ( '  F(X*) = %g'% ( value ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  toms178_test ( )
  timestamp ( )

