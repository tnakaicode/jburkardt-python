#! /usr/bin/env python3
#
from mpmath import *

def odefun_test ( ):

#*****************************************************************************80
#
## odefun_test tests odefun()
#
#  Modified:
#
#    05 February 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'odefun_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Demonstrate the mpmath multiple precision function' )
  print ( '  odefun() to solve some simple ordinary differential equations (ODE)' )

  odefun_test01 ( )
  odefun_test02 ( )
  odefun_test03 ( )
  odefun_test04 ( )
  odefun_test05 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'odefun_test():' )
  print ( '  Normal end of execution.' )

  return

def odefun_test01 ( ):

#*****************************************************************************80
#
## odefun_test01() uses odefun() to solve y' = y.
#
#  Discussion:
#
#    Solve dydt = y, y(0) = 1, y(x) = exp(x).
#
#  Modified:
#
#    05 February 2022
#
  print ( '' )
  print ( 'odefun_test01():' )
  print ( '  odefun() solves the ODE: y'' = y' )
  print ( '  Exact solution is y(x) = exp(x)' )

  print ( '' )
  print ( '  Use 15 digit arithmetic:' )

  mp.dps = 15;
  mp.pretty = True

  t0 = mpf ( 0.0 )
  y0 = mpf ( 1.0 )

  f = odefun ( lambda x, y: y, t0, y0 )
  for x in [ 0.0, 1.0, 2.5 ]:
    print ( ( x, f(x), exp(x) ) )

  print ( '' )
  print ( '  Use 50 digit arithmetic:' )

  mp.dps = 50;
  mp.pretty = True
  t0 = mpf ( 0.0 )
  y0 = mpf ( 1.0 )
  f = odefun ( lambda x, y: y, t0, y0 )
  for x in [ 0.0, 1.0, 2.5 ]:
    print ( ( x, f(x), exp(x) ) )

  return

def odefun_test02 ( ):

#*****************************************************************************80
#
## odefun_test02() uses a vectorized form of the ODE.
#
#  Discussion:
#
#    Solve dydt = y, y(0) = 1, y(x) = exp(x).
#
#  Modified:
#
#    05 February 2022
#
  print ( '' )
  print ( 'odefun_test02():' )
  print ( '  ODE: y'' = y' )

  print ( '' )
  print ( '  Use 15 digit arithmetic and vector form of ODE.' )

  mp.dps = 15;
  mp.pretty = True
  t0 = mpf ( 0.0 )
  y0 = [ 1.0 ]
  f = odefun ( lambda x, y: [y[0]], t0, y0 )
  for x in [ 0.0, 1.0, 2.5 ]:
    print((f(x), exp(x)))

  print ( '' )
  print ( '  Use 50 digit arithmetic and vector form of ODE.' )

  mp.dps = 50;
  mp.pretty = True
  t0 = mpf ( 0.0 )
  y0 = [ 1.0 ]
  f = odefun ( lambda x, y: [y[0]], t0, y0 )
  for x in [ 0.0, 1.0, 2.5 ]:
    print((f(x), exp(x)))

  return

def odefun_test03 ( ):

#*****************************************************************************80
#
## odefun_test03() solves a nonlinear ODE.
#
#  Discussion:
#
#    Solve dydt = y, y(0) = pi/2, y(x) = 2*atan(exp(x)**2/2)).
#
#  Modified:
#
#    05 February 2022
#
  print ( '' )
  print ( 'odefun_test03():' )
  print ( '  Solve nonlinear ODE: y'' = x*sin(y)' )

  print ( '' )
  print ( '  Use 15 digit arithmetic.' )

  mp.dps = 15;
  mp.pretty = True
  t0 = mpf ( 0.0 )
  y0 = mpf ( pi / 2.0 )
  f = odefun ( lambda x, y: x*sin(y), t0, y0 )
  for x in [2, 5, 10]:
    print ( (f(x), 2*atan(exp(mpf(x)**2/2))) )

  print ( '' )
  print ( '  Use 50 digit arithmeticE.' )

  mp.dps = 50;
  mp.pretty = True
  t0 = mpf ( 0.0 )
  y0 = mpf ( pi / 2.0 )
  f = odefun ( lambda x, y: x*sin(y), t0, y0 )
  for x in [2, 5, 10]:
    print ( (f(x), 2*atan(exp(mpf(x)**2/2))) )

  return

def odefun_test04 ( ):

#*****************************************************************************80
#
## odefun_test04() solves y' = (1+x**2)/(1+x**3)
#
#  Modified:
#
#    05 February 2022
#
  print ( '' )
  print ( 'odefun_test04():' )
  print ( '  Solve autonomous nonlinear ODE: y'' = (1+x**2)/(1+x**3)' )
  print ( '  Compare solution to quadrature result.' )

  mp.dps = 15;
  mp.pretty = True
  t0 = pi
  y0 = mpf ( 0.0 )
  f = lambda x: ( 1.0+x**2) / (1.0+x**3)
  g = odefun ( lambda x, y: f(x), t0, y0 )
  print ( 'odefun() solution at 2 pi:', g(2*pi) )
  print ( 'quadrature at 2 pi:       ', quad ( f, [pi,2*pi] ) )

  return

def odefun_test05 ( ):

#*****************************************************************************80
#
## odefun_test05() solves a system of equations, and prints with nprint().
#
#  Discussion:
#
#    Use 
#      nprint ( x, digits ) 
#    to print x to the given number of digits.
#
#  Modified:
#
#    05 February 2022
#
  print ( '' )
  print ( 'odefun_test05():' )
  print ( '  ODE: y0'' = -y1' ) 
  print ( '       y1'' =  y0' )

  t0 = mpf ( 0.0 )
  y0 = [ 1.0, 0.0 ]
  f = odefun ( lambda x, y: [-y[1], y[0]], t0, y0 )

  for x in [ 0.0, 1.0, 2.5, 10.0 ]:
    nprint ( f(x), 15 )
    nprint ( [ cos(x), sin(x) ], 15 )
    print("---")

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

if ( __name__ == "__main__" ):
  timestamp ( )
  odefun_test ( )
  timestamp ( )


