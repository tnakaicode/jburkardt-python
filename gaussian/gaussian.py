#! /usr/bin/env python3
#
def gaussian_test ( ):

#*****************************************************************************80
#
## gaussian_test() tests gaussian().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'gaussian_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  gaussian() evaluates the Gaussian function and its derivatives.' )

  gaussian_antideriv_test ( )
  gaussian_n_test ( )
  gaussian_mu_test ( )
  gaussian_sigma_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'gaussian_test()' )
  print ( '  Normal end of execution.' )

  return

def gaussian_antideriv_test ( ):

#*****************************************************************************80
#
## gaussian_antideriv_test() varies gaussian_antideriv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'gaussian_antideriv_test():' )
  print ( '  Compute the antiderivative of a gaussian function.' )
  print ( '' )

  mu = 0.0
  sigma = 1.0
  a = - 4.0
  b = + 4.0
  x = np.linspace ( a, b, 101 )

  plt.clf ( )

  g = gaussian_antideriv ( mu, sigma, x )

  plt.clf ( )
  plt.plot ( x, g, linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- x -->' )
  plt.ylabel ( '<-- gaussian_antideriv(mu=0,sigma=1;x) -->' )
  plt.title ( 'gaussian_antideriv(mu=0,sigma=1;x)' )
  filename = 'gaussian_antideriv.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def gaussian_mu_test ( ):

#*****************************************************************************80
#
## gaussian_mu_test() varies the mu parameter.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 September 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'gaussian_mu_test():' )
  print ( '  Compute gaussian(n,mu,sigma;x) for various values of mu.' )
  print ( '' )

  n = 0
  sigma = 1.0
  a = - 4.0
  b = + 4.0
  x = np.linspace ( a, b, 101 )

  plt.clf ( )

  for mu in [ -1.0, -0.5, 0.0, 0.5, 1.0 ]:

    g = gaussian_value ( n, mu, sigma, x )

    plt.plot ( x, g, linewidth = 3 )

  plt.grid ( True )
  plt.xlabel ( '<-- x -->' )
  if ( n == 0 ):
    label = '<-- g(x) -->'
  elif ( n == 1 ):
    label = '<-- d g(x)/dx -->'
  else:
    label = ( '<-- d^%d g(x)/dx^%d -->' % ( n, n ) )
  plt.ylabel ( label )

  if ( n == 0 ):
    label = 'g(mu=[-1,-1/2,0,1/2,1],sigma;x)'
  elif ( n == 1 ):
    label = 'd g(mu=[-1,-1/2,0,1/2,1],sigma;x)/dx'
  else:
    label = ( 'd^%d g(mu=[-1,-1/2,0,1/2,1],sigma;x)/dx^%d' % ( n, n ) )

  plt.title ( label )

  filename = 'gaussian_mu.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def gaussian_n_test ( ):

#*****************************************************************************80
#
## gaussian_n_test() varies the n parameter.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 September 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'gaussian_n_test():' )
  print ( '  Compute gaussian(n,mu,sigma;x) for various values of n.' )
  print ( '' )

  mu = 0.0
  sigma = 1.0
  a = - 4.0
  b = + 4.0
  x = np.linspace ( a, b, 101 )

  for n in range ( 0, 6 ):

    g = gaussian_value ( n, mu, sigma, x )

    plt.clf ( )

    plt.plot ( x, g, linewidth = 3 )

    plt.grid ( True )
    plt.xlabel ( '<-- x -->' )
    if ( n == 0 ):
      label = '<-- g(x) -->'
    elif ( n == 1 ):
      label = '<-- d g(x)/dx -->'
    else:
      label =  ( '<-- d^%d g(x)/dx^%d -->' % ( n, n ) )
    plt.ylabel ( label )

    if ( n == 0 ):
      label = 'g(mu,sigma;x)'
    elif ( n == 1 ):
      label = 'd g(mu,sigma;x)/dx'
    else:
      label = ( 'd^%d g(mu,sigma;x)/dx^%d' % ( n, n ) )

    plt.title ( label )
    filename = ( 'gaussian_n%d.png' % ( n ) )
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )

  return

def gaussian_sigma_test ( ):

#*****************************************************************************80
#
## gaussian_sigma_test() varies the sigma parameter.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 September 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'gaussian_sigma_test():' )
  print ( '  Compute gaussian(n,mu,sigma;x) for various values of sigma.' )
  print ( '' )

  n = 0
  mu = 0.0
  a = - 4.0
  b = + 4.0
  x = np.linspace ( a, b, 101 )

  plt.clf ( )

  for sigma in [ 0.25, 0.50, 1.0, 1.5, 2.0 ]:

    g = gaussian_value ( n, mu, sigma, x )

    plt.plot ( x, g, linewidth = 3 )

  plt.grid ( True )
  plt.xlabel ( '<-- x -->' )
  if ( n == 0 ):
    label = '<-- g(x) -->'
  elif ( n == 1 ):
    label = '<-- d g(x)/dx -->'
  else:
    label =  ( '<-- d^%d g(x)/dx^%d -->' % ( n, n ) )
  plt.ylabel ( label )

  if ( n == 0 ):
    label = 'g(mu,sigma=[0.25,0.50,1,1.5,2];x)'
  elif ( n == 1 ):
    label = 'd g(mu,sigma=[0.25,0.50,1,1.5,2];x)/dx'
  else:
    label =  ( 'd^%d g(mu,sigma=[0.25,0.50,1,1.5,2];x)/dx^%d' % ( n, n ) )

  plt.title ( label )
  filename = 'gaussian_sigma.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def gaussian_antideriv ( mu, sigma, x ):

#*****************************************************************************80
#
## gaussian_antideriv() evaluates the antiderivative of a Gaussian function.
#
#  Discussion:
#
#    g_anti(mu,sigma;x) = 1/sigma/sqrt(2*pi) * 
#      integral ( 0 <= z <= x ) exp ( - 0.5 * (( z - mu )/sigma)^2 ) dz
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, the mean.
#
#    real SIGMA: the standard deviation.
#
#    real X(M): evaluation points.
#
#  Output:
#
#    real VALUE: the value of the antiderivative of the Gaussian function.
#
  from scipy.special import erf
  import numpy as np

  z1 =   mu       / np.sqrt ( 2.0 ) / sigma
  z2 = ( mu - x ) / np.sqrt ( 2.0 ) / sigma

  value = erf ( z1 ) - erf ( z2 )

  return value

def gaussian_value ( n, mu, sigma, x ):

#*****************************************************************************80
#
## gaussian_value() evaluates a Gaussian function or a derivative.
#
#  Discussion:
#
#    g(mu,sigma;x) = 1/sigma/sqrt(2*pi) * exp ( - 0.5 * (( x - mu )/sigma)^2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the derivative order.
#    0 <= N.
#
#    real MU, the mean.
#
#    real SIGMA: the standard deviation.
#
#    real X(M): evaluation points.
#
#  Output:
#
#    real VALUE(M): the value of the N-th derivative of the Gaussian function.
#
  import numpy as np

  root2 = np.sqrt ( 2.0 )

  g = np.exp ( - 0.5 * ( ( x - mu ) / sigma )**2 )

  hn = hermite_polynomial_value ( n, ( x - mu ) / np.sqrt ( sigma ) / root2 )

  value = ( -1.0 )**n / ( sigma * root2 )**n * hn * g
  
  return value

def hermite_polynomial_value ( n, x ):

#*****************************************************************************80
#
## hermite_polynomial_value() evaluates He(i,x).
#
#  Discussion:
#
#    He(i,x) represents the probabilist's Hermite polynomial.
#
#  Differential equation:
#
#    ( exp ( - 0.5 * x^2 ) * He(n,x)' )' + n * exp ( - 0.5 * x^2 ) * He(n,x) = 0
#
#  First terms:
#
#   1
#   X
#   X^2  -  1
#   X^3  -  3 X
#   X^4  -  6 X^2 +   3
#   X^5  - 10 X^3 +  15 X
#   X^6  - 15 X^4 +  45 X^2 -   15
#   X^7  - 21 X^5 + 105 X^3 -  105 X
#   X^8  - 28 X^6 + 210 X^4 -  420 X^2 +  105
#   X^9  - 36 X^7 + 378 X^5 - 1260 X^3 +  945 X
#   X^10 - 45 X^8 + 630 X^6 - 3150 X^4 + 4725 X^2 - 945
#
#  Recursion:
#
#    He(0,X) = 1,
#    He(1,X) = X,
#    He(N,X) = X * He(N-1,X) - (N-1) * He(N-2,X)
#
#  Orthogonality:
#
#    Integral ( -oo < X < +oo ) exp ( - 0.5 * X^2 ) * He(M,X) He(N,X) dX 
#    = sqrt ( 2 * pi ) * N! * delta ( N, M )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Frank Olver, Daniel Lozier, Ronald Boisvert, Charles Clark,
#    NIST Handbook of Mathematical Functions,
#    Cambridge University Press, 2010,
#    ISBN: 978-0521192255,
#    LC: QA331.N57.
#
#  Input:
#
#    integer N, the order of the polynomial.
#    0 <= N
#
#    real X(M), the evaluation points.
#
#  Output:
#
#    real VALUE(M), the Hermite polynomial of index N at each X.
#
  import numpy as np

  m = len ( x )

  p = np.zeros ( [ m, n + 1 ] )

  for j in range ( 0, n + 1 ):
    if ( j == 0 ):
      p[0:m,j] = 1.0
    elif ( j == 1 ):
      p[0:m,j] = x[0:m]
    else:
      p[0:m,j] = x[0:m] * p[0:m,j-1] - j * p[0:m,j-2]

  value = p[0:m,n]
 
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
  gaussian_test ( )
  timestamp ( )

