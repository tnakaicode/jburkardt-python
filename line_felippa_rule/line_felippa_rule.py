#! /usr/bin/env python3
#
def line_felippa_rule_test ( ):

#*****************************************************************************80
#
## line_felippa_rule_test() tests line_felippa_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 January 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'line_felippa_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test line_felippa_rule().' )

  degree_max = 4
  line_monomial_test ( degree_max )

  degree_max = 11
  line_quad_test ( degree_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'line_felippa_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def line_monomial_integral ( a, b, alpha ):

#*****************************************************************************80
#
## line_monomial_integral(): monomial integral over a line segment in 1D.
#
#  Discussion:
#
#    This function returns the integral of X^ALPHA.
#
#    The integration region is:
#    A <= X <= B
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the lower and upper limits.
#
#    integer ALPHA, the exponent of X.
#    ALPHA must not be -1.
#
#  Output:
#
#    real VALUE, the integral of the monomial.
#
  if ( alpha == - 1 ):
    print ( '' )
    print ( 'line_monomial_integral(): Fatal error!' )
    print ( '  ALPHA = -1 is not a legal input.' )
    raise Exception ( 'line_monomial_integral(): Fatal error!' )

  value = ( b ** ( alpha + 1 ) - a ** ( alpha + 1 ) ) / ( alpha + 1 )

  return value

def line_monomial_test ( degree_max ):

#*****************************************************************************80
#
## line_monomial_test() tests line_monomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DEGREE_MAX, the maximum total degree of the
#    monomials to check.
#
  a = 0.0
  b = 1.0

  print ( '' )
  print ( 'line_monomial_test():' )
  print ( '  line_monomial() returns the exact value of the' )
  print ( '  integral of X^ALPHA Y^BETA' )
  print ( '' )
  print ( '  Volume = ', line_volume ( a, b ) )
  print ( '' )
  print ( '     ALPHA      INTEGRAL' )
  print ( '' )

  for alpha in range ( 0, degree_max + 1 ):
    value = line_monomial_integral ( a, b, alpha )
    print ( '  %8d  %14.6e' % ( alpha, value ) )

  return

def line_quad_test ( degree_max ):

#*****************************************************************************80
#
## line_quad_test() tests the rules for a line segment in 1D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DEGREE_MAX, the maximum total degree of the
#    monomials to check.
#
  import numpy as np

  a = 0.0
  b = 1.0

  print ( '' )
  print ( 'line_quad_test():' )
  print ( '  For a line segment in 1D,' )
  print ( '  we approximate monomial integrals with:' )
  print ( '  line_unit_o01(), a 1 point rule.' )
  print ( '  line_unit_o02(), a 2 point rule.' )
  print ( '  line_unit_o03(), a 3 point rule.' )
  print ( '  line_unit_o04(), a 4 point rule.' )
  print ( '  line_unit_o05(), a 5 point rule.' )

  for expon in range ( 0, degree_max + 1 ):

    print ( '' )
    print ( '  Monomial exponent:  ', expon )
    print ( '' )

    for order in range ( 1, 6 ):
      w, x = line_rule ( a, b, order )
      v = x ** expon
      quad = np.dot ( w, v )
      print ( '  %6d  %14f' % ( order, quad ) )

    print ( '' )
    quad = line_monomial_integral ( a, b, expon )
    print ( '   Exact  %14f' % ( quad ) )

  return

def line_rule ( a, b, order ):

#*****************************************************************************80
#
## line_rule() returns a quadrature rule for a line segment in 1D.
#
#  Discussion:
#
#    The integration region is:
#      A <= X <= B
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Input:
#
#    real A, B, the lower and upper limits.
#
#    integer ORDER, the order of the rule.
#
#  Output:
#
#    real W(ORDER), the weights.
#
#    real X(ORDER), the abscissas.
#
  if ( order == 1 ):
    w, x = line_unit_o01 ( )
  elif ( order == 2 ):
    w, x = line_unit_o02 ( )
  elif ( order == 3 ):
    w, x = line_unit_o03 ( )
  elif ( order == 4 ):
    w, x = line_unit_o04 ( )
  elif ( order == 5 ):
    w, x = line_unit_o05 ( )
  else:
    print ( '' )
    print ( 'LINE_RULE(): Fatal error!' )
    print ( '  Illegal value of ORDER.' )
    raise Exception ( 'LINE_RULE(): Fatal error!' )
#
#  Transform from [-1,+1] to [A,B]
#
  w = w * ( b - a ) / 2.0

  x = ( ( 1.0 - x ) * a   \
      + ( 1.0 + x ) * b ) \
      /   2.0

  return w, x

def line_unit_o01 ( ):

#*****************************************************************************80
#
## line_unit_o01() returns a 1 point quadrature rule for the unit line.
#
#  Discussion:
#
#    The integration region is:
#
#    - 1.0 <= X <= 1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(1), the weights.
#
#    real X(1), the abscissas.
#
  import numpy as np

  w = np.array ( [ 2.0 ] )

  x = np.array ( [ 0.0 ] )

  return w, x

def line_unit_o02 ( ):

#*****************************************************************************80
#
## line_unit_o02() returns a 2 point quadrature rule for the unit line.
#
#  Discussion:
#
#    The integration region is:
#
#    - 1.0 <= X <= 1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(2), the weights.
#
#    real X(2), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    1.0000000000000000000, \
    1.0000000000000000000 ] )

  x = np.array ( [ \
    -0.57735026918962576451, \
     0.57735026918962576451 ] )

  return w, x

def line_unit_o03 ( ):

#*****************************************************************************80
#
## line_unit_o03() returns a 3 point quadrature rule for the unit line.
#
#  Discussion:
#
#    The integration region is:
#
#    - 1.0 <= X <= 1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(3), the weights.
#
#    real X(3), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.55555555555555555556, \
    0.88888888888888888889, \
    0.55555555555555555556 ] )

  x = np.array ( [ \
    -0.77459666924148337704, \
     0.00000000000000000000, \
     0.77459666924148337704 ] )

  return w, x

def line_unit_o04 ( ):

#*****************************************************************************80
#
## line_unit_o04() returns a 4 point quadrature rule for the unit line.
#
#  Discussion:
#
#    The integration region is:
#
#    - 1.0 <= X <= 1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(4), the weights.
#
#    real X(4), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.34785484513745385737, \
    0.65214515486254614263, \
    0.65214515486254614263, \
    0.34785484513745385737 ] )

  x = np.array ( [ \
    -0.86113631159405257522, \
    -0.33998104358485626480, \
     0.33998104358485626480, \
     0.86113631159405257522 ] )

  return w, x

def line_unit_o05 ( ):

#*****************************************************************************80
#
## line_unit_o05() returns a 5 point quadrature rule for the unit line.
#
#  Discussion:
#
#    The integration region is:
#
#    - 1.0 <= X <= 1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(5), the weights.
#
#    real X(5), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.23692688505618908751, \
    0.47862867049936646804, \
    0.56888888888888888889, \
    0.47862867049936646804, \
    0.23692688505618908751 ] )

  x = np.array ( [ \
    -0.90617984593866399280, \
    -0.53846931010568309104, \
     0.00000000000000000000, \
     0.53846931010568309104, \
     0.90617984593866399280 ] )

  return w, x

def line_volume ( a, b ):

#*****************************************************************************80
#
## line_volume(): volume of a line segment in 1D.
#
#  Discussion:
#
#    The integration region is:
#    A <= X <= B
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the lower and upper limits.
#
#  Output:
#
#    real VALUE, the volume.
#
  value = b - a

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
  line_felippa_rule_test ( )
  timestamp ( )

