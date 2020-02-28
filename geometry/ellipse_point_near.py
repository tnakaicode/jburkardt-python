#! /usr/bin/env python
#
def ellipse_point_near ( a, b, p ):

#*****************************************************************************80
#
## ELLIPSE_POINT_NEAR finds the nearest point on an ellipse in 2D.
#
#  Discussion:
#
#    The ellipse is required to have the canonical form:
#
#      (X/A)^2 + (Y/B)^2 = 1
#
#    The nearest point PN on the ellipse has the property that the
#    line from PN to P is normal to the ellipse.  Points on the ellipse
#    can be parameterized by T, to have the form
#
#      ( A * cos ( T ), B * sin ( T ) ).
#
#    The tangent vector to the ellipse has the form
#
#      ( - A * sin ( T ), B * cos ( T ) ) 
#
#    At PN, the dot product of this vector with  ( P - PN ) must be
#    zero:
#
#      - A * sin ( T ) * ( X - A * cos ( T ) )
#      + B * cos ( T ) * ( Y - B * sin ( T ) ) = 0
#
#    This nonlinear equation for T can be solved by Newton's method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the ellipse parameters.  Normally,
#    these are both positive quantities.  Generally, they are also
#    distinct.
#
#    Input, real P(2), the point.
#
#    Output, real PN(2), the point on the ellipse which
#    is closest to P.
#
  import numpy as np
  from r8_sign import r8_sign

  iteration_max = 100
  eps = np.finfo ( float ).eps

  x = abs ( p[0] )
  y = abs ( p[1] )

  if ( y == 0.0 and a * a - b * b <= a * x ):

    t = 0.0

  elif ( x == 0.0 and b * b - a * a <= b * y ):

    t = np.pi / 2.0

  else:

    if ( y == 0.0 ):
      y = np.sqrt ( eps ) * abs ( b )

    if ( x == 0.0 ):
      x = np.sqrt ( eps ) * abs ( a )
#
#  Initial parameter T:
#
    t = np.arctan2 ( y, x )

    iteration = 0

    while ( True ):

      ct = np.cos ( t )
      st = np.sin ( t )

      f = ( x - abs ( a ) * ct ) * abs ( a ) * st \
        - ( y - abs ( b ) * st ) * abs ( b ) * ct

      if ( abs ( f ) <= 100.0 * eps ):
        break

      if ( iteration_max <= iteration ):
        print ( '' )
        print ( 'ELLIPSE_POINT_NEAR - Warning!' )
        print ( '  Reached iteration limit.' )
        print ( '  T = %f' % ( t ) )
        print ( '  F = %f' % ( f ) )
        break

      iteration = iteration + 1

      fp = a * a * st * st + b * b * ct * ct \
         + ( x - abs ( a ) * ct ) * abs ( a ) * ct \
         + ( y - abs ( b ) * st ) * abs ( b ) * st

      t = t - f / fp
#
#  From the T value, we get the nearest point.
#
  pn = np.zeros ( 2 )

  pn[0] = abs ( a ) * np.cos ( t )
  pn[1] = abs ( b ) * np.sin ( t )
#
#  Take care of case where the point was in another quadrant.
#
  pn[0] = r8_sign ( p[0] ) * pn[0]
  pn[1] = r8_sign ( p[1] ) * pn[1]

  return pn

def ellipse_point_near_test ( ):

#*****************************************************************************80
#
## ELLIPSE_POINT_NEAR_TEST tests ELLIPSE_POINT_NEAR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  a = 3.0
  b = 2.0
  n = 10

  print ( '' )
  print ( 'ELLIPSE_POINT_NEAR_TEST:' )
  print ( '  ELLIPSE_POINT_NEAR is given a point P, and' )
  print ( '  finds the nearest point PN on an ellipse in 2D.' )
  print ( '' )
  print ( '  The ellipse is (X/A)^2 + (Y/B)^2 = 1' )
  print ( '' )
  print ( '  A = %f' % ( a ) )
  print ( '  B = %f' % ( b ) )
  print ( '' )
  print ( '           P                PN' )
  print ( '' )

  p = np.zeros ( 2 )

  for i in range ( -3, n + 4 ):

    p[0] = ( float ( n - i ) * 0.0 + float ( i ) * 4.0 ) / float ( n )
    p[1] = ( float ( n - i ) * 3.0 + float ( i ) * 0.0 ) / float ( n )

    pn = ellipse_point_near ( a, b, p )

    print ( '  %10f  %10f    %10f  %10f' % ( p[0], p[1], pn[0], pn[1] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPSE_POINT_NEAR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ellipse_point_near_test ( )
  timestamp ( )

