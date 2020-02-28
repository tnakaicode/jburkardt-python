#! /usr/bin/env python3
#
def disk01_rule ( nr, nt ):

#*****************************************************************************80
#
## DISK01_RULE computes a quadrature rule for the unit disk.
#
#  Discussion:
#
#    The unit disk is the region:
#
#      x * x + y * y <= 1.
#
#    The integral I(f) is then approximated by
#
#      Q(f) = pi * sum ( 1 <= j <= NT ) sum ( 1 <= i <= NR ) 
#        W(i) * F ( R(i) * cos(T(j)), R(i) * sin(T(j)) ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 April 2016
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
#    Output, real W(NR), the weights for the disk rule.
#
#    Output, real R(NR), T(NT), the (R,Theta) points for the rule.
#
  import numpy as np
  from legendre_ek_compute import legendre_ek_compute
#
#  Request a Legendre rule for [-1,+1].
#
  xr, wr = legendre_ek_compute ( nr )
#
#  Shift the rule to [0,1].
#
  for i in range ( 0, nr ):
    xr[i] = ( xr[i] + 1.0 ) / 2.0
    wr[i] = wr[i] / 2.0
#
#  Compute the disk rule.
#
  w = np.zeros ( nr )
  r = np.zeros ( nr )
  t = np.zeros ( nt )

  for it in range ( 0, nt ):
    t[it] = 2.0 * np.pi * float ( it ) / float ( nt )

  for ir in range ( 0, nr ):
    w[ir] = wr[ir] / float ( nt )
    r[ir] = np.sqrt ( xr[ir] )

  return w, r, t

def disk01_rule_test ( ):

#*****************************************************************************80
#
## DISK01_RULE_TEST tests DISK01_RULE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from disk01_monomial_integral import disk01_monomial_integral

  nr = 4
  nt = 8

  print ( '' )
  print ( 'DISK01_RULE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DISK01_RULE can compute a rule Q(f) for the unit disk' )
  print ( '  using NT equally spaced angles and NR radial distances.' )
  print ( '' )
  print ( '  NT = %d' % ( nt ) )
  print ( '  NR = %d' % ( nr ) )
  print ( '' )
  print ( '  Estimate integrals I(f) where f = x^e(1) * y^e(2).' )
#
#  Compute the quadrature rule.
#
  w, r, t = disk01_rule ( nr, nt )
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
      for j in range ( 0, nt ):
        for i in range ( 0, nr ):
          x = r[i] * np.cos ( t[j] )
          y = r[i] * np.sin ( t[j] )
          q = q + w[i] * x ** e[0] * y ** e[1]

      q = np.pi * q

      exact = disk01_monomial_integral ( e )

      print ( '   %2d  %2d  %14.6g  %14.6g' % ( e[0], e[1], exact, q ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DISK01_RULE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  disk01_rule_test ( )
  timestamp ( )

