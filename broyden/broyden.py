#! /usr/bin/env python3
#
def broyden_test ( ):

#*****************************************************************************80
#
## broyden_test() tests broyden().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Tim Kelley,
#    Iterative Methods for Linear and Nonlinear Equations,
#    SIAM, 2004,
#    ISBN: 0898713528,
#    LC: QA297.8.K45.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'broyden_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test broyden()' )

  broyden_test01 ( )
  broyden_test02 ( )
  broyden_test03 ( )
  broyden_test04 ( )
  broyden_test05 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'broyden_test():' )
  print ( '  Normal end of execution.' )

  return

def broyden_test01 ( ):

#*****************************************************************************80
#
## broyden_test01() tests broyden() on a single nonlinear equation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'broyden_test01():' )
  print ( '  broyden() solves a system of nonlinear equations' )
  print ( '  using Broyden\'s method.' )
  print ( '  Test it on a single nonlinear equation.' )

  n = 1
  x = np.zeros ( n )
  fx = f1 ( x )
  print ( '  Initial residual norm: ', np.linalg.norm ( fx ) )
 
  atol = 0.000001
  rtol = 0.000001

  maxit = 10
  maxdim = 2

  x, ierr = broyden ( x, f1, atol, rtol, maxit, maxdim )

  fx = f1 ( x )

  print ( '' )
  print ( '  Final residual norm:', np.linalg.norm ( fx ) )

  return

def broyden_test02 ( ):

#*****************************************************************************80
#
## broyden_test02() tests broyden() on 2 nonlinear equations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'broyden_test02():' )
  print ( '  broyden() solves a system of nonlinear equations' )
  print ( '  using Broyden\'s method.' )
  print ( '  Test it on 2 nonlinear equations.' )

  n = 2
  x = np.array ( [ 4.0, 0.0 ] )
  fx = f2 ( x )
  print ( '  Initial residual norm:', np.linalg.norm ( fx ) )
 
  atol = 0.000001
  rtol = 0.000001

  maxit = 10
  maxdim = 2

  x, ierr = broyden ( x, f2, atol, rtol, maxit, maxdim )

  fx = f2 ( x )

  print ( '' )
  print ( '  Final residual norm:', np.linalg.norm ( fx ) )

  return

def broyden_test03 ( ):

#*****************************************************************************80
#
## broyden_test03() tests broyden() on 4 nonlinear equations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'broyden_test03():' )
  print ( '  broyden() solves a system of nonlinear equations' )
  print ( '  using Broyden\'s method.' )
  print ( '  Test it on 4 nonlinear equations.' )

  n = 4
  x = np.zeros ( n )
  fx = f3 ( x )
  print ( '  Initial residual norm:', np.linalg.norm ( fx ) )
 
  atol = 0.000001
  rtol = 0.000001

  maxit = 10
  maxdim = 2

  x, ierr = broyden ( x, f3, atol, rtol, maxit, maxdim )

  fx = f3 ( x )

  print ( '' )
  print ( '  Final residual norm:', np.linalg.norm ( fx ) )

  return

def broyden_test04 ( ):

#*****************************************************************************80
#
## broyden_test04() tests broyden() on 8 nonlinear equations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'broyden_test04():' )
  print ( '  broyden() solves a system of nonlinear equations' )
  print ( '  using Broyden\'s method.' )
  print ( '  Test it on 8 nonlinear equations.' )

  n = 8
  x = np.zeros ( n )
  fx = f4 ( x )
  print ( '  Initial residual norm:', np.linalg.norm ( fx ) )
 
  atol = 0.000001
  rtol = 0.000001

  maxit = 10
  maxdim = 4

  x, ierr = broyden ( x, f4, atol, rtol, maxit, maxdim )

  fx = f4 ( x )

  print ( '' )
  print ( '  Final residual norm:', np.linalg.norm ( fx ) )

  return

def broyden_test05 ( ):

#*****************************************************************************80
#
## broyden_test05() tests broyden() on the Chandrasekhar function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'broyden_test05():' )
  print ( '  broyden() solves a system of nonlinear equations' )
  print ( '  using Broyden\'s method.' )
  print ( '  Test it on the Chandrasekhar function.' )

  n = 100
  x = np.zeros ( n )

  atol = 0.000001
  rtol = 0.000001

  maxit = 10
  maxdim = 2

  x, ierr = broyden ( x, f5, atol, rtol, maxit, maxdim )

  print ( '' )
  print ( '  Error flag IERR = ', ierr )

  fx = f5 ( x )

  print ( '' )
  print ( '  Residual norm:', np.linalg.norm ( fx ) )

  return

def broyden ( x, f, atol, rtol, maxit, maxdim ):

#*****************************************************************************80
#
## broyden() uses Broyden's method for a nonlinear system of equations.
#
#  Discussion:
#
#    Given an initial estimate X0, a point X* is sought for which 
#      |F(X*)| <= ATOL + RTOL * |F(X0)|
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2023
#
#  Author:
#
#    Tim Kelley
#
#  Reference:
#
#    Tim Kelley,
#    Iterative Methods for Linear and Nonlinear Equations,
#    SIAM, 2004,
#    ISBN: 0898713528,
#    LC: QA297.8.K45.
#    
#  Input:
#
#    real X(N): the initial solution estimate.
#
#    function fx = F ( x ): evaluates the function.
#
#    real ATOL, RTOL: error tolerances.
#
#    integer MAXIT: maximum number of nonlinear iterations
#
#    integer MAXDIM: maximum number of Broyden iterations before restart.
#
#  Output:
#
#    real X(N): the estimated solution.
#
#    integer IERR: termination flag.
#    0: success
#    1: the termination criterion was not satisfied after MAXIT iterations,
#       or the ratio of successive nonlinear residuals exceeded 1. 
#
  import numpy as np

  n = len ( x ) 
#
#  Evaluate f at the initial iterate.
#
  fc = f ( x )
  fnrm = np.linalg.norm ( fc ) / np.sqrt ( n )
#
#  Compute the stopping tolerance.
#
  stop_tol = atol + rtol * fnrm
#
#  Initialize the step array.
#
  stp = np.zeros ( [ n, maxdim ] )
  stp[:,0] = - fc
#
#  Initialize the step norm array.
#
  stp_nrm = np.zeros ( maxdim )
  stp_nrm[0] = np.linalg.norm ( stp[:,0] )
#
#  Iteration:
#
  nbroy = 0
  itc = 0 

  while ( itc + 1 < maxit ):

    fnrmo = fnrm
#
#  Next iterate.
#
    x = x + stp[:,nbroy]
    fc = f ( x )
    fnrm = np.linalg.norm ( fc ) / np.sqrt ( n )
#
#  Accept?
#
    if ( fnrm <= stop_tol ):
      ierr = 0
      return x, ierr
#
#  Reject?
#
    if ( fnrmo <= fnrm ):
      ierr = 1
      print ( '' )
      print ( 'broyden(): iteration terminated.' )
      print ( '  Rejected step', itc )
      print ( '  Residual ratio increase = ', fnrm / fnrmo )
      return x, ierr
#
#  Continue. 
#
    if ( nbroy + 1 < maxdim ):

      z = - fc
      if ( 1 < nbroy + 1 ):
        for kbr in range ( 0, nbroy ):
          z = z + stp[:,kbr+1] * np.dot ( stp[:,kbr], z ) / stp_nrm[kbr] ** 2

      zz = np.dot ( stp[:,nbroy], z )
      zz = zz / stp_nrm[nbroy]**2

      nbroy = nbroy + 1
      stp[:,nbroy] = z / ( 1.0 - zz )
      stp_nrm[nbroy] = np.linalg.norm ( stp[:,nbroy] )

    else:
#
#  Out of room, restart.
#
      nbroy = 0
      stp[:,nbroy] = - fc
      stp_nrm[nbroy] = np.linalg.norm ( stp[:,nbroy] )

    itc = itc + 1
#
#  Reached MAXIT iterations.  Did we make it?
#
  if ( stop_tol < fnrm ):
    ierr = 1
    print ( 'broyden(): Requested accuracy was not achieved.' )
  else:
    ierr = 0

  return x, ierr

def f1 ( x ):

#*****************************************************************************80
#
## f1() evaluates a nonlinear system of 1 equation.
#
#  Discussion:
#
#    This is Kepler's equation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the variable values.
#
#  Output:
#
#    real FX(N), the function values at X.
#
  import numpy as np

  fx = np.zeros ( 1 )

  e = 0.8
  m = 5.0
  fx[0] = x[0] - m - e * np.sin ( x[0] )

  return fx

def f2 ( x ):

#*****************************************************************************80
#
## f2() evaluates a nonlinear system of 2 equations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the variable values.
#
#  Output:
#
#    real FX(N), the function values at X.
#
  import numpy as np

  fx = np.zeros ( 2 )

  fx[0] = x[0] * x[0] - 10.0 * x[0] + x[1] * x[1] + 8.0
  fx[1] = x[0] * x[1] * x[1] + x[0] - 10.0 * x[1] + 8.0

  return fx

def f3 ( x ):

#*****************************************************************************80
#
## f3() evaluates a nonlinear system of 4 equations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the variable values.
#
#  Output:
#
#    real FX(N), the function values at X.
#
  import numpy as np

  fx = np.zeros ( 4 )

  for i in range ( 0, 4 ):
    fx[i] = ( x[i] - i - 1 ) ** 2

  return fx

def f4 ( x ):

#*****************************************************************************80
#
## f4() evaluates a nonlinear system of 8 equations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the variable values.
#
#  Output:
#
#    real FX(N), the function values at X.
#
  import numpy as np

  n = len ( x )

  fx = np.zeros ( n )

  for i in range ( 0, n ):
    fx[i] = ( 3.0 - 2.0 * x[i] ) * x[i] + 1.0

  for i in range ( 1, n ):
    fx[i] = fx[i] - x[i-1]
 
  for i in range ( 0, n - 1 ):
    fx[i] = fx[i] - 2.0 * x[i+1]

  return fx

def f5 ( h ):

#*****************************************************************************80
#
## f5() evaluates the discretized Chandrasekhar H function.
#
#  Discussion:
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
#      F(h(i)) = h(i) 
#        - 1 / ( 1 - c/(2N) * sum ( 1 <= j <= N ) 
#        ( mu(i) * h(j) / ( mu(i) + mu(j) ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2023
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
#    Tim Kelley,
#    Iterative Methods for Linear and Nonlinear Equations,
#    SIAM, 2004,
#    ISBN: 0898713528,
#    LC: QA297.8.K45.
#    
#  Input:
#
#    real H(N), the argument of the function.
#
#  Output:
#
#    real FX(N), the value of the function.
#
  import numpy as np

  c = 0.9

  n = len ( h )
  fx = np.zeros ( n )

  fx = h.copy ( )

  mu = np.linspace ( 0.5, n - 0.5, n ) / n

  for i in range ( 0, n ):

    term = 1.0 - c / ( 2.0 * n ) * np.sum ( mu[i] * h / ( mu[i] + mu ) )

    fx[i] = fx[i] - 1.0 / term

  return fx

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
  broyden_test ( )
  timestamp ( )


