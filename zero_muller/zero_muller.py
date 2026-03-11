#! /usr/bin/env python3
#
def zero_muller ( func, fatol, itmax, x1, x2, x3, xatol, xrtol ):

#*****************************************************************************80
#
## zero_muller() carries out Muller's method, using complex arithmetic.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gisela Engeln-Muellges, Frank Uhlig,
#    Numerical Algorithms with C,
#    Springer, 1996,
#    ISBN: 3-540-60530-4,
#    LC: QA297.E56213.
#
#  Input:
#
#    value = func ( x ): evaluates the function.
#
#    real FATOL, the absolute error tolerance for F(X).
#
#    integer ITMAX, the maximum number of steps allowed.
#
#    complex X1, X2, X3, three distinct points to start the
#    iteration.
#
#    real XATOL, XRTOL, absolute and relative
#    error tolerances for the root.
#
#  Output:
#
#    complex XNEW, the estimated root.
#
#    complex FXNEW, the value of the function at XNEW.
#
  import numpy as np

  xnew = x1
  xmid = x2
  xold = x3

  fxnew = func ( xnew )
  fxmid = func ( xmid )
  fxold = func ( xold )

  print ( "" )
  print ( "zero_muller():" )
  print ( "  Muller's root-finding method (complex root version)" )
  print ( "" )
  print ( "  Iteration     x_real              x_imag             ||fx||           ||disc||" )
  print ( "" )

  iterate = -2
  print ( '%6d%20.10f%20.10f%20.10f' \
    % ( iterate, xold.real, xold.imag, np.abs ( fxold ) ) )
  iterate = -1
  print ( '%6d%20.10f%20.10f%20.10f' \
    % ( iterate, xmid.real, xmid.imag, np.abs ( fxmid ) ) )
  iterate = 0
  print ( '%6d%20.10f%20.10f%20.10f' \
    % ( iterate, xnew.real, xnew.imag, np.abs ( fxnew ) ) )

  if ( np.abs ( fxnew ) < fatol ):
    print ( "" )
    print ( "zero_muller():" )
    print ( "  |F(X)| is below the tolerance." )
    return xnew, fxnew

  while ( True ):
#
#  You may need to swap (XMID,FXMID) and (XNEW,FXNEW).
#
    if ( np.abs ( fxmid ) <= np.abs ( fxnew ) ):

      c8_temp = xnew
      xnew = xmid
      xmid = c8_temp

      c8_temp = fxnew
      fxnew = fxmid
      fxmid = c8_temp

    xlast = xnew
    iterate = iterate + 1

    if ( itmax < iterate ):
      print ( "" )
      print ( "zero_muller(): Warning!" )
      print ( "  Maximum number of steps taken." )
      break

    a =  ( ( xmid - xnew ) * ( fxold - fxnew ) \
         - ( xold - xnew ) * ( fxmid - fxnew ) )

    b = ( ( xold - xnew )**2 * ( fxmid - fxnew ) \
        - ( xmid - xnew )**2 * ( fxold - fxnew ) )

    c = ( ( xold - xnew ) * ( xmid - xnew ) * ( xold - xmid ) * fxnew )

    xold = xmid
    xmid = xnew
#
#  Apply the quadratic formula to get roots XPLUS and XMINUS.
#
    discrm = b**2 - 4.0 * a * c

    if ( a == 0.0 ):
      print ( "" )
      print ( "zero_muller(): Warning!" )
      print ( "  The algorithm has broken down." )
      print ( "  The quadratic coefficient A is zero." )
      break

    xplus = xnew + ( ( - b + np.sqrt ( discrm ) ) / ( 2.0 * a ) )

    fplus = func ( xplus )

    xminus = xnew + ( ( - b - np.sqrt ( discrm ) ) / ( 2.0 * a ) )

    fminus = func ( xminus )
#
#  Choose the root with smallest function value.
#
    if ( np.abs ( fminus ) < np.abs ( fplus ) ):
      xnew = xminus
    else:
      xnew = xplus

    fxold = fxmid
    fxmid = fxnew
    fxnew = func ( xnew )
    print ( '%6d%20.10f%20.10f%20.10f%20.10f' 
      % ( iterate, xnew.real, xnew.imag, np.abs ( fxnew ), np.abs ( discrm ) ) )
#
#  Check for convergence.
#
    x_ave = np.abs ( xnew + xmid + xold ) / 3.0
    x_inc = xnew - xmid

    if ( np.abs ( x_inc ) <= xatol ):
      print ( "" )
      print ( "zero_muller():" )
      print ( "  Absolute convergence of the X increment." )
      break

    if ( np.abs ( x_inc ) <= xrtol * x_ave ):
      print ( "" )
      print ( "zero_muller():" )
      print ( "  Relative convergence of the X increment." )
      break

    if ( abs ( fxnew ) <= fatol ):
      print ( "" )
      print ( "zero_muller():" )
      print ( "  Absolute convergence of |F(X)|." )
      break

  return xnew, fxnew

def zero_muller_test ( ):

#*****************************************************************************80
#
## zero_muller_test() tests zero_muller().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( "" )
  print ( "zero_muller_test():" )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( "  Test zero_muller(), which uses Muller's method," )
  print ( "  with complex arithmeic, to solve a nonlinear equation." )

  test01 ( )
  test02 ( )
  test03 ()
#
#  Terminate.
#
  print ( "" )
  print ( "zero_muller_test():" )
  print ( "  Normal end of execution." )

  return

def test01 ( ):

#*****************************************************************************80
#
## test01() tests zero_muller() on F(X) = X*X+9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( "" )
  print ( "test01():" )
  print ( "  Demonstrate zero_muller() on F(X) = X*X+9." )

  fatol = 1.0E-05
  itmax = 10
  x1 = 1.0 + 0.0j
  x2 = 0.0 + 1.0j
  x3 = 0.5 + 0.5j
  xatol = 1.0E-05
  xrtol = 1.0E-05

  xnew, fxnew = zero_muller ( func01, fatol, itmax, x1, x2, x3, xatol, xrtol )

  print ( "" )
  print ( "     X   = ", xnew.real, xnew.imag )
  print ( "" )
  print ( "  with function value F(X):" )
  print ( "" )
  print ( "    FX   = ", fxnew.real, fxnew.imag )
  print ( "  ||FX|| = ", np.abs ( fxnew ) )

  return

def test02 ( ):

#*****************************************************************************80
#
## test02() tests zero_muller() on F(X) = (X*X+4) * (X-10) * (X+20)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( "" )
  print ( "test02():" )
  print ( "  Demonstrate zero_muller() on F(X) = (X*X+4)*(X-10)*(X+20)." )

  fatol = 1.0E-05
  itmax = 10
  x1 = 1.0 + 0.0j
  x2 = 0.0 + 1.0j
  x3 = 0.5 + 0.5j
  xatol = 1.0E-05
  xrtol = 1.0E-05

  xnew, fxnew = zero_muller ( func02, fatol, itmax, x1, x2, x3, xatol, xrtol )

  print ( "" )
  print ( "     X   = ", xnew.real, xnew.imag )
  print ( "" )
  print ( "  with function value F(X):" )
  print ( "" )
  print ( "    FX   = ", fxnew.real, fxnew.imag )
  print ( "  ||FX|| = ", np.abs ( fxnew ) )

  return

def test03 ( ):

#*****************************************************************************80
#
## test03() tests zero_muller() on Zhelyazkov's function
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( "" )
  print ( "test03():" )
  print ( "  Demonstrate zero_muller() on Zhelyazkov's function." )

  fatol = 1.0E-07
  itmax = 10

  for test in [ 1, 2 ]:
#
#  First set of starting points.
#  Result is X = ( 1.5705798926, 0.0 )
#
    if ( test == 1 ):
      x1 = 1.0 + 0.0j
      x2 = 0.0 + 1.0j
      x3 = 0.5 + 0.5j
#
#  Second set of starting points.
#  Result is X = ( -0.5802520567, 0.0 ).
#
    elif ( test == 2 ):
      x1 =  0.0 + 1.0j
      x2 =  1.0 + 2.0j
      x3 = -1.0 + 2.0j

    xatol = 1.0E-07
    xrtol = 1.0E-07

    xnew, fxnew = zero_muller ( func03, fatol, itmax, x1, x2, x3, xatol, xrtol )

    print ( "" )
    print ( "     X   = ", xnew.real, xnew.imag )
    print ( "" )
    print ( "  with function value F(X):" )
    print ( "" )
    print ( "    FX   = ", fxnew.real, fxnew.imag )
    print ( "  ||FX|| = ", np.abs ( fxnew ) )

  return

def func01 ( x ):

#*****************************************************************************80
#
## func01() evaluates F(X) = X*X+9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex X, the point at which the function is to
#    be evaluated.
#
#  Output:
#
#    complex FX, the function value at X.
#
  fx = x * x + 9.0
 
  return fx

def func02 ( x ):

#*****************************************************************************80
#
## func02() evaluates F(X) = (X*X+4)*(X-1)*(X+2).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex X, the point at which the function is to
#    be evaluated.
#
#  Output:
#
#    complex FX, the function value at X.
#
  fx = ( x * x + 4.0 ) * ( x - 10.0 ) * ( x + 20.0 )
 
  return fx

def func03 ( z ):

#*****************************************************************************80
#
## func03() evaluates Zhelyazkov's function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex ( kind = ck ) Z, the point at which the function is to
#    be evaluated.
#
#  Output:
#
#    complex ( kind = ck ) FZ, the function value at Z.
#
  import numpy as np

  eps = 0.4 + 0.0j
  eta = 0.64 + 0.0j
  me = 0.384
  mo = 0.5
  one = 1.0 + 0.0j
  x = 0.5

  ok = z - me / np.sqrt ( eta )
  of = z - mo

  a = of * of + ( ok * ok ) * eta * np.tanh ( x )

  b = ( of - ok * eta ) / ( of - ok * eta * eta )

  fz = of * of - one + ( eta * ok * ok - one ) * \
    np.tanh ( x ) - x * x * eps * eps * a * b

  return fz

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
  zero_muller_test ( )
  timestamp ( )

