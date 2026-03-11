#! /usr/bin/env python3
#
def sympy_ode ( ):

#*****************************************************************************80
#
## sympy_ode() uses sympy() to solve differential equations.
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
  from sympy import dsolve
  from sympy import Function
  from sympy import symbols

  print ( '' )
  print ( 'sympy_ode():' )
  print ( '  Demonstrate solving differential equations.' )
  print ( '' )

  t = symbols ( 't' )
  y = symbols ( 'y', cls = Function )
#
#  Solve y - y*(1-y) = 0.
#
  sol = dsolve ( y(t).diff(t) + y(t)*(1-y(t)), y(t) )
  print ( '  y-y(1-y)=0 solved by ', sol )
#
#  Solve y'' + y = 0.
#
  sol = dsolve ( y(t).diff(t,2) + y(t), y(t) )
  print ( '  y"+y=0 solved by ', sol )
#
#  Solve ty' + y -y**2= 0.
#
  sol = dsolve ( t*y(t).diff(t) + y(t) - y(t)**2, y(t) )
  print ( '  ty\'+y-y**2=0 solved by ', sol )
#
#  Solve y' - a * ( cos(t) - y) = 0.
#
  a = symbols ( 'a' )
  from sympy import cos

  sol = dsolve ( y(t).diff(t) - a * ( cos(t) - y(t) ), y(t) )
  print ( '  y\'-a*(cos(t)-y)=0 solved by ', sol )

  return

if ( __name__ == "__main__" ):
  sympy_ode ( )

