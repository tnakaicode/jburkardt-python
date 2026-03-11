#! /usr/bin/env python3
#
def sympy_derivative ( ):

#*****************************************************************************80
#
## sympy_derivative() uses sympy() to evaluate derivatives.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'sympy_derivative():' )
  print ( '  Demonstrate the computation of derivatives.' )
  print ( '' )

  derivative_humps ( )
  derivative_x_exp_xt ( )
  derivative_biharmonic ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sympy_derivative():' )
  print ( '  Normal end of execution.' )
  print ( '' )

  return

def derivative_humps ( ):

#*****************************************************************************80
#
## derivative_humps() differentiates humps(x)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
  from sympy import diff
  from sympy import symbols

  print ( '' )
  print ( 'derivative_humps():' )
  print ( '  Differentiate humps(x).' )

  x = symbols ( 'x' )

  humps = 100 / ( ( 10 * x - 3 )**2 + 1 ) \
        + 100 / ( ( 10 * x - 9 )**2 + 4 ) \
        - 6

  print ( '' )
  print ( '  humps(x) = ', humps )

  dhumpsdx = diff ( humps, x )
  print ( '  d humps /dx = ', dhumpsdx )

  d2humpsdx2 = diff ( humps, x, 2 )
  print ( '  d2 humps /dx2 = ', d2humpsdx2 )

  return

def derivative_x_exp_xt ( ):

#*****************************************************************************80
#
## derivative_x_exp_xt() differentiates x exp(xt).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
  from sympy import diff
  from sympy import exp
  from sympy import symbols

  print ( '' )
  print ( 'derivative_x_exp_xt():' )
  print ( '  Differentiate z(x,t) = x*exp(x*t).' )

  x = symbols ( 'x' )
  t = symbols ( 't' )
  z = x * exp ( x * t )

  print ( '' )
  print ( '  z(x,t) = ', z )
  dzdx = diff ( z, x )
  print ( '  dzdx = ', dzdx )
  dzdt = diff ( z, t )
  print ( '  dzdt = ', dzdt )
  dz2dt2 = diff ( z, t, 2 )
  print ( '  d2zdt2 = ', dz2dt2 )
  dz2dtdx = diff ( z, t, x )
  print ( '  d2zdtdx = ', dz2dtdx )

  return

def derivative_biharmonic ( ):

#*****************************************************************************80
#
## derivative_biharmonic() differentiates a biharmonic function.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 September 2025
#
#  Author:
#
#    John Burkardt
#
  from sympy import atan
  from sympy import cos
  from sympy import cosh
  from sympy import diff
  from sympy import log
  from sympy import sin
  from sympy import sinh
  from sympy import sqrt
  from sympy import symbols

  print ( '' )
  print ( 'derivative_biharmonic():' )
  print ( '  Differentiate biharmonic function.' )

  a = symbols ( 'a' )
  b = symbols ( 'b' )
  c = symbols ( 'c' )
  d = symbols ( 'd' )
  e = symbols ( 'e' )
  f = symbols ( 'f' )
  g = symbols ( 'g' )
  w = symbols ( 'w' )
  x = symbols ( 'x' )
  y = symbols ( 'y' )
#
#  First function.
#
  w = ( a     * cosh ( g * x ) \
      + b     * sinh ( g * x ) \
      + c * x * cosh ( g * x ) \
      + d * x * sinh ( g * x ) ) \
      * \
      ( e * cos ( g * y ) \
      + f * sin ( g * y ) )

  print ( '' )
  print ( '  w(x,y) = ', w )
  wx = diff ( w, x )
  print ( '' )
  print ( '  wx = ', wx )
  wy = diff ( w, y )
  print ( '' )
  print ( '  wy = ', wy )
  wxxxx = diff ( w, x, 4 )
  print ( '' )
  print ( '  wxxxx = ', wxxxx )
  wxxyy = diff ( w, x, 2, y, 2 )
  print ( '' )
  print ( '  wxxyy = ', wxxyy )
  wyyyy = diff ( w, y, 4 )
  print ( '' )
  print ( '  wyyyy = ', wyyyy )
#
#  Second function.
#
  w = ( a     * cos ( g * x ) \
      + b     * sin ( g * x ) \
      + c * x * cos ( g * x ) \
      + d * x * sin ( g * x ) ) \
      * \
      ( e * cosh ( g * y ) \
      + f * sinh ( g * y ) )

  print ( '' )
  print ( '  w(x,y) = ', w )
  wx = diff ( w, x )
  print ( '' )
  print ( '  wx = ', wx )
  wy = diff ( w, y )
  print ( '' )
  print ( '  wy = ', wy )
  wxxxx = diff ( w, x, 4 )
  print ( '' )
  print ( '  wxxxx = ', wxxxx )
  wxxyy = diff ( w, x, 2, y, 2 )
  print ( '' )
  print ( '  wxxyy = ', wxxyy )
  wyyyy = diff ( w, y, 4 )
  print ( '' )
  print ( '  wyyyy = ', wyyyy )
#
#  Third function.
#
  r = sqrt ( ( x - e )**2 + ( y - f )**2 )

  w =   a * r**2 * log ( r ) \
      + b * r**2 \
      + c * log ( r ) \
      + d

  print ( '' )
  print ( '  r(x,y) = ', r )
  print ( '' )
  print ( '  w(x,y) = ', w )
  wx = diff ( w, x )
  print ( '' )
  print ( '  wx = ', wx )
  wy = diff ( w, y )
  print ( '' )
  print ( '  wy = ', wy )
  wxxxx = diff ( w, x, 4 )
  print ( '' )
  print ( '  wxxxx = ', wxxxx )
  wxxyy = diff ( w, x, 2, y, 2 )
  print ( '' )
  print ( '  wxxyy = ', wxxyy )
  wyyyy = diff ( w, y, 4 )
  print ( '' )
  print ( '  wyyyy = ', wyyyy )
#
#  Fourth function.
#
  w = atan ( x * y )
  print ( '' )
  print ( '  w(x,y) = ', w )
  wx = diff ( w, x )
  print ( '' )
  print ( '  wx = ', wx )
  wy = diff ( w, y )
  print ( '' )
  print ( '  wy = ', wy )
  wxx = diff ( w, x, 2 )
  print ( '' )
  print ( '  wxx = ', wxx )
  wxy = diff ( w, x, y )
  print ( '' )
  print ( '  wxy = ', wxy )
  wyy = diff ( w, y, 2 )
  print ( '' )
  print ( '  wyy = ', wyy )

  return

if ( __name__ == "__main__" ):
  sympy_derivative ( )

