#! /usr/bin/env python3
#
def r8poly2_val ( x1, y1, x2, y2, x3, y3, x ):

#*****************************************************************************80
#
## R8POLY2_VAL evaluates a parabola defined by three data values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X1, Y1, X2, Y2, X3, Y3, three pairs of data.
#    If the X values are distinct, then all the Y values represent
#    actual values of the parabola.
#
#    Three special cases are allowed:
#
#      X1 == X2 /= X3: Y2 is the derivative at X1
#      X1 /= X2 == X3: Y3 is the derivative at X3
#      X1 == X2 == X3: Y2 is the derivative at X1, and
#                      Y3 is the second derivative at X1.
#
#    Input, real X, an abscissa at which the parabola is to be
#    evaluated.
#
#    Output, real Y, YP, YPP, the values of the parabola and
#    its first and second derivatives at X.
#
  from sys import exit
#
#  If any X's are equal, put them and the Y data first.
#
  if ( x1 == x2 and x2 == x3 ):
    distinct = 1
  elif ( x1 == x2 ):
    distinct = 2
  elif ( x1 == x3 ):
    print ( '' )
    print ( 'R8POLY2_VAL - Fatal error!' )
    print ( '  X1 = X3 =/= X2.' )
    print ( '  X1 = %f' % ( x1 ) )
    print ( '  X2 = %f' % ( x2 ) )
    print ( '  X3 = %f' % ( x3 ) )
    exit ( 'R8POLY2_VAL - Fatal error!' )
  elif ( x2 == x3 ):
    distinct = 2
    t  = x1
    x1 = x2
    x2 = t
    t  = x2
    x2 = x3
    x3 = t
    t  = y1
    y1 = y2
    y2 = t
    t  = y2
    y2 = y3
    y3 = t
  else:
    distinct = 3
#
#  Set up the coefficients.
#
  if ( distinct == 1 ):

    dif1 = y2
    dif2 = 0.5 * y3

  elif ( distinct == 2 ):

    dif1 = y2
    dif2 = ( ( y3 - y1 ) / ( x3 - x1 ) - y2 ) / ( x3 - x2 )

  elif ( distinct == 3 ):

    dif1 = ( y2 - y1 ) / ( x2 - x1 )
    dif2 =  ( ( y3 - y1 ) / ( x3 - x1 ) \
            - ( y2 - y1 ) / ( x2 - x1 ) ) / ( x3 - x2 )
#
#  Evaluate.
#
  y = y1 + ( x - x1 ) * dif1 + ( x - x1 ) * ( x - x2 ) * dif2
  yp = dif1 + ( 2.0 * x - x1 - x2 ) * dif2
  ypp = 2.0 * dif2

  return y, yp, ypp

def r8poly2_val_test ( ):

#*****************************************************************************80
#
## R8POLY2_VAL_TEST tests R8POLY2_VAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8POLY2_VAL_TEST' )
  print ( '  R8POLY2_VAL evaluates a parabola given' )
  print ( '  3 data points.' )
  print ( '' )
  print ( '  Our parabola will be 2*x^2 + 3 * x + 1.' )
  print ( '' )
  print ( '  Case 1: 3 distinct data points:' )
  print ( '' )

  x1 = -1.0
  x2 = 1.0
  x3 = 3.0

  y1, yp, ypp = r8poly2_val_f ( x1 )
  y2, yp, ypp = r8poly2_val_f ( x2 )
  y3, yp, ypp = r8poly2_val_f ( x3 )

  print ( '  %12f  %12f' % ( x1, y1 ) )
  print ( '  %12f  %12f' % ( x2, y2 ) )
  print ( '  %12f  %12f' % ( x3, y3 ) )

  print ( '' )
  print ( '  Sampled data:' )
  print ( '' )
  print ( '  X, Y, Y'', Y"' )
  print ( '' )
  for i in range ( 0, 4 ):
    x = i
    y, yp, ypp = r8poly2_val ( x1, y1, x2, y2, x3, y3, x )
    print ( '  %12f  %12f  %12f  %12f' % ( x, y, yp, ypp ) )

  print ( '' )
  print ( '  Case 2: X1=X2, X3 distinct:' )
  print ( '' )

  x1 = -1.0
  x2 = -1.0
  x3 = 3.0

  y1, y2, ypp = r8poly2_val_f ( x1 )
  y3, yp, ypp = r8poly2_val_f ( x3 )
  print ( '  %12f  %12f' % ( x1, y1 ) )
  print ( '  %12f  %12f' % ( x2, y2 ) )
  print ( '  %12f  %12f' % ( x3, y3 ) )

  print ( '' )
  print ( '  Sampled data:' )
  print ( '' )
  print ( '  X, Y, Y'', Y"' )
  print ( '' )
  for i in range ( 0, 4 ):
    x = i
    y, yp, ypp = r8poly2_val ( x1, y1, x2, y2, x3, y3, x )
    print ( '  %12f  %12f  %12f  %12f' % ( x, y, yp, ypp ) )

  print ( '' )
  print ( '  Case 3: X1=X2=X3:' )
  print ( '' )

  x1 = -1.0
  x2 = -1.0
  x3 = -1.0

  y1, y2, y3 = r8poly2_val_f ( x1 )

  print ( '  %12f  %12f' % ( x1, y1 ) )
  print ( '  %12f  %12f' % ( x2, y2 ) )
  print ( '  %12f  %12f' % ( x3, y3 ) )

  print ( '' )
  print ( '  Sampled data:' )
  print ( '' )
  print ( '  X, Y, Y'', Y"' )
  print ( '' )
  for i in range ( 0, 4 ):
    x = i
    y, yp, ypp = r8poly2_val ( x1, y1, x2, y2, x3, y3, x )
    print ( '  %12f  %12f  %12f  %12f' % ( x, y, yp, ypp ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY2_VAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8poly2_val_f ( x ):

#*****************************************************************************80
#
## R8POLY2_VAL_F evaluates a parabola for us.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real Y, YP, YPP, the value, and first and second derivatives.
#
  y = 2.0 * x * x + 3.0 * x + 1.0
  yp = 4.0 * x + 3.0
  ypp = 4.0

  return y, yp, ypp

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly2_val_test ( )
  timestamp ( )

