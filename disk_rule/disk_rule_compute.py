#! /usr/bin/env python3
#
def disk_rule_compute ( nr, nt, xc, yc, rc ):

#*****************************************************************************80
#
## disk_rule_compute computes a quadrature rule for a general disk.
#
#  Discussion:
#
#    The general disk is the region:
#
#      ( x - xc ) ^ 2 + ( y - yc ) ^ 2 <= rc ^ 2.
#
#    The integral I(f) is then approximated by
#
#      S(f) = sum ( 1 <= i <= NT * NR ) W(i) * F ( X(i), Y(i) ).
#
#      Area = pi * RC ^ 2
#
#      Q(f) = Area * S(f)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NR, the number of points in the radial rule.
#
#    Input, integer NT, the number of angles to use.
#
#    Input, real XC, YC, the coordinates of the disk center.
#
#    Input, real RC, the radius of the disk.
#
#    Output, real W(NR*NT), the weights for the rule.
#
#    Output, real X(NR*NT), Y(NR*NT), the points for the rule.
#
  import numpy as np
  from disk01_rule import disk01_rule

  w01, r01, t01 = disk01_rule ( nr, nt )
#
#  Recompute the rule for the general circle in terms of X, Y.
#
  w = np.zeros ( nr * nt )
  x = np.zeros ( nr * nt )
  y = np.zeros ( nr * nt )

  k = 0
  for j in range ( 0, nt ):
    for i in range ( 0, nr ):
      w[k] = w01[i]
      x[k] = xc + rc * r01[i] * np.cos ( t01[j] )
      y[k] = yc + rc * r01[i] * np.sin ( t01[j] )
      k = k + 1

  return w, x, y

def disk_rule_compute_test ( ):

#*****************************************************************************80
#
## disk_rule_compute_test tests disk_rule_compute.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  nr = 4
  nt = 8
#
#  Tabulated exact integrals of 1, x, y, x^2, xy, y^2, x^3, ..., y^4
#  over circle centered at (1,2) with radius 3.
#
  exact = np.pi * np.array ( [ 
       9.0, \
       9.0,        18.0, \
     117.0 / 4.0,  18.0,        225.0 / 4.0, \
     279.0 / 4.0, 117.0 / 2.0,  225.0 / 4.0, 387.0 / 2.0, \
    1773.0 / 8.0, 279.0 / 2.0, 1341.0 / 8.0, 387.0 / 2.0, 5769.0 / 8.0 ] )
 
  print ( '' )
  print ( 'disk_rule_compute_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  disk_rule_compute can compute a rule Q(f) for a general disk' )
  print ( '  centered at (XC,YC) with radius RC,' )
  print ( '  using NT equally spaced angles and NR radial distances.' )
  print ( '' )
  print ( '  NT = %d' % ( nt ) )
  print ( '  NR = %d' % ( nr ) )
  print ( '' )
  print ( '  Estimate integrals I(f) where f = x^ex * y^ey.' )
#
#  Define center and radius of non-unit disk.
#
  xc = 1.0
  yc = 2.0
  rc = 3.0
#
#  Compute the quadrature rule for a unit disk.
#
  w, x, y = disk_rule_compute ( nr, nt, xc, yc, rc )

  print ( '' )
  print ( '   Ex  Ey         I(f)            Q(f)' )
  print ( '' )
#
#  Specify a monomial F(X,Y) = X^Ex * Y^Ey.
#
  e = np.zeros ( 2 )

  i = 0

  for d in range ( 0, 5 ):

    for ex in range ( d, -1, -1 ):

      ey = d - ex
#
#  Evaluate the function at all the quadrature points.
#
      s = 0.0
      for k in range ( 0, nr * nt ):
        f = x[k] ** ex * y[k] ** ey
        s = s + w[k] * f
#
#  Compute the disk area.
#
      area = np.pi * rc ** 2
#
#  Q is the quadrature estimate.
#
      q = area * s

      print ( '   %2d  %2d  %14.6g  %14.6g' % ( ex, ey, exact[i], q ) )

      i = i + 1
#
#  Terminate.
#
  print ( '' )
  print ( 'disk_rule_compute_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  disk_rule_compute_test ( )
  timestamp ( )

