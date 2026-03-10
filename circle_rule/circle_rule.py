#! /usr/bin/env python3
#
def circle01_monomial_integral ( e ):

#*****************************************************************************80
#
## circle01_monomial_integral(): integrals on circumference of unit circle in 2D.
#
#  Discussion:
#
#    The integration region is 
#
#      X^2 + Y^2 = 1.
#
#    The monomial is F(X,Y) = X^E(1) * Y^E(2).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Academic Press, 1984, page 263.
#
#  Input:
#
#    integer E(2), the exponents of X and Y in the 
#    monomial.  Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  from scipy.special import gamma
  import numpy as np

  if ( any ( e < 0 ) ):
    print ( '' )
    print ( 'circle01_monomial_integral(): Fatal error!' )
    print ( '  All exponents must be nonnegative.' )
    raise Exception ( 'circle01_monomial_integral(): Fatal error!' )

  if ( any ( ( e % 2 ) == 1 ) ):

    integral = 0.0

  else:

    integral = 2.0

    for i in range ( 0, 2 ):
      integral = integral * gamma ( 0.5 * ( e[i] + 1 ) )

    integral = integral / gamma ( 0.5 * np.sum ( e + 1 ) )

  return integral

def circle_rule ( nt ):

#*****************************************************************************80
#
## circle_rule() computes a quadrature rule for the unit circle.
#
#  Discussion:
#
#    The unit circle is the region:
#
#      x * x + y * y = 1.
#
#    The integral I(f) is then approximated by
#
#      Q(f) = 2 * pi * sum ( 1 <= i <= NT ) W(i) * F ( cos(T(i)), sin(T(i)) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NT, the number of angles to use.
#
#  Output:
#
#    real W(NT), the weights for the rule.
#
#    real T(NT), the angles for the rule.
#
  import numpy as np

  w = 1.0 / nt * np.ones ( nt )
  t = 2.0 * np.pi * np.linspace ( 0, nt - 1, nt ) / nt

  return w, t

def circle_rule_test01 ( nt ):

#*****************************************************************************80
#
## circle_rule_test01() tests circle_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'circle_rule_test01():' )
  print ( '  circle_rule() computes a rule Q(f) for the unit circle' )
  print ( '  using NT equally spaced angles.' )
  print ( '  Estimate integrals I(f) where f = x^e(1) * y^e(2)' )
  print ( '  using', nt, 'points.' )
#
#  Compute the quadrature rule.
#
  w, t = circle_rule ( nt )
#
#  Apply it to integrands.
#
  print ( '' )
  print ( '  E(1)  E(2)    I(f)            Q(f)' )
  print ( '' )
#
#  Specify a monomial.
#
  e = np.zeros ( 2 )

  for e1 in range ( 0, 7, 2 ):

    e[0] = e1

    for e2 in range ( e1, 7, 2 ):

      e[1] = e2

      q = 0.0
      for i in range ( 0, nt ):
        x = np.cos ( t[i] )
        y = np.sin ( t[i] )
        q = q + w[i] * x ** e[0] * y ** e[1]

      q = 2.0 * np.pi * q

      exact = circle01_monomial_integral ( e )

      print ( '   %2d  %2d  %14.6g  %14.6g' % ( e[0], e[1], exact, q ) )

  return

def circle_rule_test ( ):

#*****************************************************************************80
#
## circle_rule_test() tests circle_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'circle_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test circle_rule().' )

  nt = 8
  circle_rule_test01 ( nt )

  nt = 32
  circle_rule_test01 ( nt )
#
#  Terminate.
#
  print ( '' )
  print ( 'circle_rule_test()' )
  print ( '  Normal end of execution.' )

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
  circle_rule_test ( )
  timestamp ( )

