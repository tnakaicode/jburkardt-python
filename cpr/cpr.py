#! /usr/bin/env python3
#
def cpr_test ( ):

#*****************************************************************************80
#
## cpr_test() tests cpr().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'cpr_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test cpr(), which uses the Chebyshev Proxy Rootfinder' )
  print ( '  to determine all real zeros of a smooth function' )
  print ( '  over an interval [a,b].' )

  bessel_test ( )
  newton_test ( )
  jenkins_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'cpr_test():' )
  print ( '  Normal end of execution.' )

  return

def bessel_test ( ):

#*****************************************************************************80
#
## bessel_test() tests cpr() on the J0 Bessel function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2024
#
#  Author:
#
#    John Burkardt
#
  from scipy.special import j0
  import numpy as np

  print ( '' )
  print ( 'bessel_test():' )
  print ( '  Seek real roots of the J0 Bessel function.' )
#
#  The search interval:
#
  a = 0.0
  b = 40.0
#
#  Chebyshev degree.
#
  N = 50
#
#  Define the string with the name of the function.
#
  f = lambda x: j0 ( x )
#
#  Request roots in interval.
#
  froots, Einterstitial, root_residuals = cpr ( f, a, b, N )
#
#  Report.
#
  print ( '' )
  print ( '  Interstitial interpolation error norm = ', Einterstitial )
  print ( '  Number of roots = ', len ( froots ) )
  print ( '  Roots computed by CPR:' )
  print ( froots )
  print ( '  Maximum residual at roots = ', np.max ( np.abs ( root_residuals ) ) )
  exact = np.array ( [ \
     2.404825557695773, \
     5.520078110286311, \
     8.653727912911012, \
    11.79153443901428, \
    14.93091770848779, \
    18.07106396791092, \
    21.21163662987926, \
    24.35247153074930, \
    27.49347913204025, \
    30.63460646843198, \
    33.77582021357357, \
    36.91709835366404 ] )
  print ( '  Exact roots:' )
  print ( exact )
  print ( '  Exact f(roots):' )
  print ( f ( exact ) )
  print ( '  f ( froots ):' )
  print ( f ( froots ) )

  return

def newton_test ( ):

#*****************************************************************************80
#
## newton_test() tests cpr() on the Newton example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'newton_test():' )
  print ( '  Seek real roots of the Newton example x^3-2x-5=0.' )
#
#  The search interval:
#
  a = -5.0
  b = +5.0
#
#  Chebyshev degree.
#
  N = 10
#
#  Define the string with the name of the function.
#
  f = lambda x: newton_example ( x )
#
#  Request roots in interval.
#
  froots, Einterstitial, root_residuals = cpr ( f, a, b, N )
#
#  Report.
#
  print ( '' )
  print ( '  Interstitial interpolation error norm = ', Einterstitial )
  print ( '  Number of roots = ', len ( froots ) )
  print ( '  Maximum residual at roots = ', max ( np.abs ( root_residuals ) ) )
  exact = 2.094551481542328 
  print ( '  Exact real root   : ', exact )
  print ( '  Computed real root: ', froots[0] )
  print ( '  Exact f(roots)    : ', f ( exact ) )
  print ( '  Computed f(roots) : ', f ( froots[0] ) )
  print ( '  Error             : ', np.abs ( froots[0] - exact ) )

  return

def newton_example ( x ):

#*****************************************************************************80
#
## newton_example() evaluates the Newton example function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2024
#
#  Author:
#
#    John Burkardt
#
  value = x**3 - 2.0 * x - 5.0

  return value

def jenkins_test ( ):

#*****************************************************************************80
#
## jenkins_test() tests cpr() on the Jenkins function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'jenkins_test():' )
  print ( '  Seek real roots of the Jenkins function.' )
  print ( '  p(x) = x^4 + 5.6562x^3 + 5.8854x^2' )
  print ( '             + 7.3646x   + 6.1354' )
#
#  The search interval:
#
  a = -5.0
  b = 5.0
#
#  Chebyshev degree.
#
  N = 10
#
#  Define the string with the name of the function.
#
  f = lambda x: jenkins_example ( x )
#
#  Request roots in interval.
#
  froots, Einterstitial, root_residuals = cpr ( f, a, b, N )
#
#  Report.
#
  print ( '' )
  print ( '  Interstitial interpolation error norm = ', Einterstitial )
  print ( '  Maximum residual at roots = ', np.max ( np.abs ( root_residuals ) ) )
  print ( '  Number of roots = ', len ( froots ) )
  print ( '  Computed roots:' )
  print ( froots )
  exact = np.array ( [ \
    -4.674054017161709, \
    -1.0000  ] )
  print ( '  Exact roots:' )
  print ( exact )
  print ( '  f ( Computed roots ):' )
  print ( f ( froots ) )
  print ( '  f ( Exact roots):' )
  print ( f ( exact ) )

  return

def jenkins_example ( x ):

#*****************************************************************************80
#
## jenkins_example() evaluates the Jenkins example function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2024
#
#  Author:
#
#    John Burkardt
#
  value = x**4 + 5.6562 * x**3 + 5.8854 * x**2 + 7.3646 * x + 6.1354

  return value

def cpr ( f, a, b, N ):

#*****************************************************************************80
#
## cpr() computes the real roots of f(x) on the real interval [a,b].
#
#  Discussion:
#
#    A Chebyshev Proxy Rootfinder is used.
#
#    f(x) is assumed to be a smooth real-valued scalar function of a scalar
#    argument.
#
#    The code will only search for real roots of f(x), within the
#    user-specified interval.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 March 2024
#
#  Author:
#
#    John Boyd
#
#  Reference:
#
#    John Boyd,
#    Solving Transcendental Equations,
#    The Chebyshev Polynomial Proxy and other Numerical Rootfinders,
#    Perturbation Series, and Oracles,
#    SIAM, 2014,
#    ISBN: 978-1-611973-51-8,
#    LC: QA:353.T7B69
#
#  Input:
#
#    string f: the name of the function.
#
#    real a, b: the endpoints of the search interval.
#
#    integer N: the degree of Chebyshev expansion, using N+1 points.
#
#  Output:
#
#    real froots(nroots): a column vector, contains the computed roots.
#
#    real Einter: ???
#
#    real root_residuals(nroots): a column vector, the function value at 
#    each computed root.
#
#  Local:
#
#    real dyn_range_tol: trigger for warning of small dynamic range.
#
#    real epscutoff: trailing coefficient j is discarded if 
#    abs ( acoeff(j)) < epscutoff * max ( abs ( acoeff() ) ).
#
#    real sigma: Discard any root wih ( 1 + sigma ) < abs ( Re ( root ) )
#    measured in Chebyshev coordinate range [-1,+1].
#
#    real tau: Discard any root with tau < abs ( Im ( root ) ).
#
  from numpy.linalg import eigvals
  import numpy as np

  epscutoff = 1.0E-13
  tau = 1.0E-08
  sigma = 1.0E-06
  dyn_range_tol = 1.0E-08
#
#  Compute trigonometic argument vector T.
#
  t = np.linspace ( 0.0, np.pi, N + 1 )
#
#  Set vector of Chebyshev nodes in [-1,+1].
#
  xi = np.cos ( t )
#
#  Compute vector of interpolation nodes in [a,b].
#
  x = 0.5 * ( b - a ) * xi + ( b + a ) * 0.5
#
#  Create vector of function samples.
#
  fa = np.zeros ( N + 1 )
  for i in range ( 0, N + 1 ):
    fa[i] = f ( x[i] )
#
#  Compute acoeff, the Chebyshev coefficients.
#
  phia = np.zeros ( [ N + 1, N + 1 ] )
  pj = np.ones ( N + 1 )
  pj[0] = 2.0
  pj[N] = 2.0

  for i in range ( 0, N + 1 ):
    phia[i,:] = ( 2.0 / N / pj[i] ) * np.cos ( i * t[:] ) / pj[:]

  acoeff = np.dot ( phia, fa )
#
#  Truncate the tail of the series, if very small.
#  
  acoeffmax = np.max ( np.abs ( acoeff ) )
  Nt = N
  tailnorm = 0.0
  for k in range ( N, 1, -1 ):
    tailnorm = tailnorm + np.abs ( acoeff[k] )
    if ( tailnorm < epscutoff * acoeffmax ):
      Nt = Nt - 1
#
#  Create the Chebyshev companion matrix.
#
  A = np.zeros ( [ Nt, Nt ] )
  A[0,1] = 1.0
  for j in range ( 1, Nt - 1 ):
    A[j,j-1] = 0.5
    A[j,j+1] = 0.5

  A[Nt-1,0:Nt] = - acoeff[0:Nt] / ( 2.0 * acoeff[Nt] )
  A[Nt-1,Nt-2] = A[Nt-1,Nt-2] + 0.5
#
#  eig() returns a column vector of eigenvalues.
#  The roots are in Chebyshev coordinates xi.
#
  all_roots_in_xi = eigvals ( A )
#
#  Accept roots only if within tau of real axis and Chebyshev interval.
#
  nroots = 0
  froots = np.zeros ( 0 )

  for i in range ( 0, Nt ):
    evi = all_roots_in_xi[i]
    if ( np.abs ( evi.imag ) < tau * np.abs ( evi.real ) ):
      if ( np.abs ( evi.real ) <= 1.0 + sigma ):
        nroots = nroots + 1
        new_root = 0.5 * ( b - a ) * evi.real + ( b + a ) / 2.0
        froots = np.append ( froots, new_root )
#
#  Sort the roots.
#
  froots = np.sort ( froots )
#
#  Compute column vector of function residuals at computed roots.
#
  root_residuals = f ( froots )
#
#  Interstitial interpolation residual.
#
  tinter = t[0:N] + 0.5 / N
  xiint = np.cos ( tinter )
  xinter = 0.5 * ( b - a ) * xiint + ( b + a ) * 0.5
  fainter = np.zeros ( N )
  for i in range ( 0, N ):
    fainter[i] = f ( xinter[i] )

  taall = np.concatenate ( [ t, tinter ] )
  faall = np.concatenate ( [ fa, fainter ] )
  xiall = np.concatenate ( [ xi, xiint ] )
  xall = np.concatenate ( [ x, xinter ] )

  fpoly = np.zeros ( 2 * N + 1 )
  for j in range ( 0, N + 1 ):
    fpoly = fpoly + acoeff[j] * np.cos ( j * taall )
  Einter = np.max ( np.abs ( faall[(N+1):(2*N+1)] - fpoly[(N+1):(2*N+1)] ) )
#
#  Compute dynamic range.
#
  fmax = np.max ( np.abs ( faall ) )
  dyn_range = np.min ( np.abs ( faall ) ) / fmax
  if ( dyn_range < dyn_range_tol ):
    print ( '' )
    print ( 'cpr() - Warning!' )
    print ( '  dynamic range = ', dyn_range, ' < ', dyn_range_tol )

  return froots, Einter, root_residuals

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
  cpr_test ( )
  timestamp ( )

