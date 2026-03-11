#! /usr/bin/env python3
#
def zoomin_test ( ):

#*****************************************************************************80
#
## zoomin_test() tests zoomin().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'zoomin_test(' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test zoomin().' )

  test01 ( )
  test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'zoomin_test():' )
  print ( '  Normal end of execution.' )

  return

def test01 ( ):

#*****************************************************************************80
#
## test01() runs the tests on a polynomial function.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
  a = 1.0
  b = 1.5
  c = 4.0
#
#  Set the error tolerance.
#
  abserr = 0.00001
#
#  Tell the program how many derivatives are available.
#
  nder = 3
#
#  IPOLY is the order of the polynomial function
#  or -1 if the function is not a polynomial.
#
  ipoly = 3
#
#  KMAX is the maximum number of iterations.
#
  kmax = 30
#
#  MULT is the multiplicity of the root.
#  If not known, set MULT to 1.
#
  mult = 1
#
#  For modified Newton methods, set the number of substeps.
#
  nsub = 3

  print ( '' )
  print ( 'test01():' )
  print ( '  Seek a root of a polynomial function F(X).' )
  print ( '  F(X) = (X+3) * (X+3) * (X-2)' )

  zoomin_all_test ( a, b, c, abserr, kmax, func01, ipoly, mult, nder, nsub )

  return

def test02 ( ):

#*****************************************************************************80
#
## test02() runs the tests on a nonpolynomial function.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
  a = 0.9
  b = 0.4
  c = 0.5
#
#  Set the error tolerance.
#
  abserr = 0.00001
#
#  Tell the program how many derivatives are available.
#
  nder = 3
#
#  IPOLY is the order of the polynomial function
#  or -1 if the function is not a polynomial.
#
  ipoly = - 1
#
#  KMAX is the maximum number of iterations.
#
  kmax = 60
#
#  MULT is the multiplicity of the root.
#  If not known, just set MULT to 1.
#
  mult = 1
#
#  For modified Newton methods, set the number of substeps.
#
  nsub = 3

  print ( '' )
  print ( 'test02():' )
  print ( '  Nonpolynomial function F(X)' )
  print ( '  Find a root of F(X) = COS(X) - X' )

  zoomin_all_test ( a, b, c, abserr, kmax, func02, ipoly, mult, nder, nsub )

  return


def zoomin_all_test ( a, b, c, abserr, kmax, f, ipoly, mult, nder, nsub ):

#*****************************************************************************80
#
## zoomin_all_test() calls all the zero finders for a given problem.
#
#  Discussion:
#
#    The original code was written by Harold Deiss in BASIC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, three estimates for a root of the
#    function.  The bisection routines will only be called if the function
#    evaluated at A, B and C includes both positive and negative values.
#
#    real ABSERR, an error tolerance.
#
#    function value = F(x,ider), the name of the routine that
#    evaluates the function or its derivatives.
#
#    integer IPOLY, is 0 if the function is not known to be
#    a polynomial, or is equal to the polynomial degree otherwise.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    integer MULT, the multiplicity of the root being 
#    sought.  If the multiplicity of the root is not known, set MULT to 1.
#
#    integer NDER, the highest order derivative that can be
#    computed by the user function.  NDER = 0 means only the function
#    value itself is available, for instance.  NDER must be at least 0,
#    and no algorithm needs a derivative higher than 3.
#
#    integer NSUB, the number of substeps to take.  A few
#    algorithms include a "sub-iteration".  For instance, the modified
#    Newton method evaluates the derivative function only before
#    steps 1, NSUB+1, 2*NSUB+1 and so on, and uses that derivative
#    value for NSUB iterations in a row.  This option is useful when
#    the derivative evaluation is expensive.
#
  import numpy as np

  print ( '' )
  print ( 'zoomin_all_test():' )
  print ( '  A compilation of scalar zero finders,' )
  print ( '  based on the work of Joseph Traub.' )

  fa = f ( a, 0 )
  fb = f ( b, 0 )
  fc = f ( c, 0 )
#
#  Rearrange the data, if necessary, so that the pair (A,FA) has
#  the smallest function value of the three sets of data.
#
  if ( np.abs ( fb ) < np.abs ( fa ) ):
    t = a
    a = b
    b = t
    t = fa
    fa = fb
    fb = t

  if ( np.abs ( fc ) < np.abs ( fa ) ):
    t = a
    a = c
    c = t
    t = fa
    fa = fc
    fc = t
#
#  If necessary, switch B and C, so that FB is of opposite sign to FA,
#  if possible.
#
  sa = np.sign ( fa )
  sb = np.sign ( fb )
  sc = np.sign ( fc )

  if ( sa != sb ):
    change = True
  elif ( sa != sc ):
    t = b
    b = c
    c = t
    t = fb
    fb = fc
    fc = t
    change = True
  else:
    change = False
#
#  Check other input.
#
  if ( mult < 1 ):
    mult = 1

  if ( nder < 0 ):
    print ( '' )
    print ( 'zoomin_all_test(): Fatal error!' )
    print ( '  The input quantity NDER = ', nder )
    print ( '  But NDER must be at least 0.' )
    return

  if ( nsub < 1 ):
    nsub = 1
#
#  Report start up conditions.
#
  print ( '  1 point formulas use:' )
  print ( '    x1 = ', a )
  print ( '    fx1= ', fa )
  print ( '  2 point formulas add:' )
  print ( '    x2 = ', b )
  print ( '    fx2= ', fb )
  print ( '  3 point formulas add:' )
  print ( '    x3 = ', c )
  print ( '    fx3= ', fc )
  print ( '' )
  print ( '  User estimated multiplicity = ', mult )
  if ( 0 <= ipoly ):
    print ( '  Polynomial degree = ', ipoly )
  else:
    print ( '  The function is not known to be polynomial.' )

  print ( '  Highest derivative supplied = ', nder )
  print ( '  Error tolerance = #g', abserr )
  print ( '  Maximum number of steps = ', kmax )
  print ( '  Newton method substep parameter  = ', nsub )
  print ( '' )
  print ( '' )
  print ( '  Technique                           Root        Steps' )
  print ( '   Error     Multiplicity' )

  print ( '' )
  print ( '  1.  One point iteration functions with memory:' )
  print ( '' )
#
#  Secant algorithm.
#
  name = 'Secant'
  x = a
  x1 = b
  x, x1, ierror, k = secant ( x, x1, abserr, kmax, f )

  if ( ierror != 0 ):
    print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
  else:
    print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Extended secant algorithm.
#
  name = 'Extended secant'
  x = a
  x1 = b
  x2 = c
  x, x1, x2, ierror, k = secant_extended ( x, x1, x2, abserr, kmax, f )

  if ( ierror != 0 ):
    print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
  else:
    print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Capital Phi(2,1).
#
  name = 'Capital Phi(2,1)'
  x = a
  x1 = b
  x2 = c
  x, x1, x2, ierror, k = cap_phi_21 ( x, x1, x2, abserr, kmax, f )

  if ( ierror != 0 ):
    print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
  else:
    print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Muller's algorithm.
#
  name = 'R8_Muller'
  x = a
  x1 = b
  x2 = c
  x, x1, x2, ierror, k = r8_muller ( x, x1, x2, abserr, kmax, f )

  if ( ierror != 0 ):
    print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
  else:
    print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Perp E(2,1).
#
  if ( 1 <= nder ):

    name = 'Perp E(2,1)'
    x = a
    x1 = b
    x2 = c
    x, x1, x2, ierror, k = perp_e_21 ( x, x1, x2, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Star E(2,1).
#
  name = 'Star E(2,1)'
  x = a
  x1 = b
  x2 = c
  x, x1, x2, ierror, k = star_e21 ( x, x1, x2, abserr, kmax, f )

  if ( ierror != 0 ):
    print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
  else:
    print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Finite difference Halley's method.
#
  name = 'Finite difference Halley'
  x = a
  x1 = b
  x2 = c
  x, x1, x2, ierror, k = halley2 ( x, x1, x2, abserr, kmax, f )

  if ( ierror != 0 ):
    print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
  else:
    print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Phi(1,2).
#
  if ( 1 <= nder ):

    name = 'Phi(1,2)'
    x = a
    x1 = b
    x, x1, ierror, k = phi_12 ( x, x1, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Perp E(1,2).
#
  if ( 1 <= nder ):

    name = 'Perp E(1,2)'
    x = a
    x1 = b
    x, x1, ierror, k = perp_e_12 ( x, x1, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Star E(1,2).
#
  if ( 1 <= nder ):

    name = 'Star E(1,2)'
    x = a
    x1 = b
    x, x1, ierror, k = star_e12 ( x, x1, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Dagger E(1,2).
#
  if ( 1 <= nder ):

    name = 'Dagger E(1,2)'
    x = a
    x1 = b
    x, x1, ierror, k = dagger_e12 ( x, x1, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )

  print ( '' )
  print ( '  2. One point iteration functions.' )
  print ( '' )
#
#  Newton method.
#
  if ( 1 <= nder ):

    name = 'Newton'
    x = a
    x, ierror, k = newton ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Steffenson's method.
#
  name = 'Steffenson'
  x = a
  x, ierror, k = steffenson ( x, abserr, kmax, f )

  if ( ierror != 0 ):
    print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
  else:
    print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Stirling's method.
#
  if ( 1 <= nder ):

    name = 'Stirling'
    x = a
    x, ierror, k = stirling ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Midpoint method.
#
  if ( 1 <= nder ):

    name = 'midpoint'
    x = a
    x, ierror, k = midpoint ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Traub-Ostrowski method.
#
  name = 'Traub-Ostrowski'
  x = a
  x, ierror, k = traub_ostrowski ( x, abserr, kmax, f )

  if ( ierror != 0 ):
    print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
  else:
    print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Chebyshev method.
#
  if ( 2 <= nder ):

    name = 'Chebyshev'
    x = a
    x, ierror, k = chebyshev ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Halley Super method.
#
  if ( 2 <= nder ):

    name = 'Halley Super'
    x = a
    x, ierror, k = halley_super ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Whittaker convex acceleration method.
#
  if ( 2 <= nder ):

    name = 'Whittaker'
    x = a
    x, ierror, k = whittaker ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Whittaker double convex acceleration method.
#
  if ( 2 <= nder ):

    name = 'Whittaker2'
    x = a
    x, ierror, k = whittaker2 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  E3.
#
  if ( 2 <= nder ):

    name = 'E3'
    x = a
    x, ierror, k = e3 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  E4.
#
  if ( 3 <= nder ):

    name = 'E4'
    x = a
    x, ierror, k = e4 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Halley's method.
#
  if ( 2 <= nder ):

    name = 'Halley'
    x = a
    x, ierror, k = halley1 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  PSI(2,1).
#
  if ( 3 <= nder ):

    name = 'Psi(2,1)'
    x = a
    x, ierror, k = psi_21 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  PSI(1,2).
#
  if ( 3 <= nder ):

    name = 'Psi(1,2)'
    x = a
    x, ierror, k = psi_i2 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Capital PHI(0,3).
#
  if ( 2 <= nder ):

    name = 'Capital Phi(0,3)'
    x = a
    x, ierror, k = cap_phi_03 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Reduced capital PHI(0,4).
#
  if ( 3 <= nder ):

    name = 'Reduced Capital Phi(0,4)'
    x = a
    x, ierror, k = red_cap_phi_04 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Functions from Hansen and Patrick.
#
#  The Ostrowski square root formula is the Hansen family member with BETA = 0.
#
  if ( 2 <= nder ):
    name = 'Ostrowski square root'
    x = a
    x, ierror, k = ostrowski_sqrt ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  The Euler method.
#
  if ( 2 <= nder ):

    name = 'Euler'
    x = a
    x, ierror, k = euler ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  The Laguerre method.
#
  if ( 2 <= nder and 2 <= ipoly ):

    name = 'Laguerre'
    x0 = a
    x, ierror, k = laguerre ( x0, ipoly, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )

  print ( '' )
  print ( '  3.  Multipoint iteration functions.' )
  print ( '' )
#
#  First function in Traub, page 236.
#
  if ( 1 <= nder ):

    name = 'Traub first'
    x = a
    x, ierror, k = traub1 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  A family of iteration functions including
#  forms 2, 12, and 13 of Traub, pages 236 - 237.
#
  if ( 1 <= nder ):

    name = 'Traub second'
    e = 0.5
    d = 1.0
    x = a
    x, ierror, k = t_family1 ( x, e, d, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )

  if ( 1 <= nder ):

    name = 'Traub twelfth'
    e = 0.25
    d = 2.0 / 3.0
    x = a
    x, ierror, k = t_family1 ( x, e, d, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )

  if ( 1 <= nder ):

    name = 'Traub thirteenth'
    e = 5.0 / 12.0
    d = 6.0 / 7.0
    x = a
    x, ierror, k = t_family1 ( x, e, d, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Modified Newton method.
#
  if ( 1 <= nder and 1 <= nsub ):

    name = 'Modified Newton, NSUB = ' + str ( nsub )
    x = a
    x, ierror, k = newton_mod ( x, nsub, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Fourth function in Traub.
#
  if ( 1 <= nder and 1 <= nsub ):

    name =  'Traub fourth, NSUB = ' + str ( nsub )
    x = a
    x, ierror, k = traub4 ( x, nsub, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Newton - secant.
#
  if ( 1 <= nder ):

    name = 'Newton - secant'
    x = a
    x, ierror, k = newton_secant ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  A family of iteration functions including
#  forms 6 and 7 of Traub, pages 236 - 237.
#
  if ( 1 <= nder ):

    name = 'Traub sixth'
    e = 2.0
    ff = 3.0
    g = 1.0
    h = 1.0
    x = a
    x, ierror, k = t_family2 ( x, e, ff, g, h, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )

  if ( 1 <= nder ):

    name = 'Traub seventh'
    e = 4.0
    ff = 7.0
    g = 3.0
    h = 2.0 / 3.0
    x = a
    x, ierror, k = t_family2 ( x, e, ff, g, h, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Eighth function in Traub, page 237.
#
  if ( 1 <= nder ):

    name = 'Traub eighth'
    x = a
    x, ierror, k = traub8 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Ninth function in Traub, page 237.
#
  if ( 1 <= nder ):

    name = 'Traub ninth'
    x = a
    x, ierror, k = traub9 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Type 1 family of iteration functions including
#  forms 10 and 11 of Traub, pages 237.
#
  if ( 1 <= nder ):

    name = 'Traub type 1, form 10'
    rho = ( 1.0 - np.sqrt ( 5.0 ) ) / 2.0
    e = 0.0
    x = a
    x, ierror, k = tt1f ( x, e, rho, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )

  if ( 1 <= nder ):

    name = 'Traub type 1, form 11'
    e = 1.0
    x = a
    x, ierror, k = tt1f ( x, e, rho, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Fourteenth function in Traub, page 237
#
  if ( 1 <= nder ):

    name = 'Traub fourteenth'
    x = a
    x, ierror, k = t14 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Fifteenth function in Traub, page 238.
#
  if ( 1 <= nder ):

    name = 'Traub fifteenth'
    x = a
    x, ierror, k = t15 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Sixteenth function in Traub, page 238.
#
  if ( 1 <= nder ):

    name = 'Traub sixteenth'
    x = a
    x, ierror, k = t16 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  A family of fourth order methods by Richard King.
#
  if ( 1 <= nder ):

    name = 'King, BETA=0'
    beta = 0.0
    x = a
    x, ierror, k = king ( x, beta, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )

  if ( 1 <= nder ):

    name = 'King, BETA=1'
    beta = 1.0
    x = a
    x, ierror, k = king ( x, beta, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )

  if ( 1 <= nder ):

    name = 'King, BETA=2'
    beta = 2.0
    x = a
    x, ierror, k = king ( x, beta, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Jarratt iterative technique.
#
  if ( 1 <= nder ):

    name = 'Jarratt'
    x = a
    x, ierror, k = jarratt ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Jarratt inverse-free iterative technique.
#
  if ( 1 <= nder ):

    name = 'Jarratt inverse-free'
    x = a
    x, ierror, k = jarratt2 ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
  print ( '' )
  print ( '  4.  Multiple root methods, multiplicity given.' )
  print ( '' )
#
#  Script E2.
#
  if ( 1 <= nder ):

    name = 'Script E2'
    x = a
    x, ierror, k = script_e2 ( x, mult, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Script E3.
#
  if ( 2 <= nder ):

    name = 'Script E3'
    x = a
    x, ierror, k = script_e3 ( x, mult, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Script E4.
#
  if ( 3 <= nder ):

    name = 'Script E4'
    x = a
    x, ierror, k = script_e4 ( x, mult, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Star E - 1,1(f) function in Traub, page 235.
#
  name = 'Star E 1,1(f)'
  x = a
  x1 = b
  x, x1, ierror, k = te11f ( x, x1, mult, abserr, kmax, f )

  if ( ierror != 0 ):
    print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
  else:
    print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Routines which determine the root and multiplicity
#
  print ( '' )
  print ( '  5.  Multiple root methods,' )
  print ( '      multiplicity not given.' )
  print ( '' )
#
#  E2(U).
#
  if ( 2 <= nder ):

    name = 'E2(U)'
    x = a
    x, em, ierror, k = te2u ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d%15.6g' % ( name, x, k, em ) )
#
#  Phi - 1,1(u) function in Traub, page 235.
#
  if ( 1 <= nder ):

    name = 'Phi 1,1(U)'
    x = a
    x, em, ierror, k = tphi1u ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d%15.6g' % ( name, x, k, em ) )
#
#  Third function in Traub, page 235 bottom.
#
  if ( 1 <= nder ):

    name = 'Traub third'
    x = a
    x, em, ierror, k = tthip ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d%15.6g' % ( name, x, k, em ) )
#
#  Van de Vel iteration.
#
  if ( 1 <= nder ):
    name = 'Van de Vel'
    x = a
    x, em, ierror, k = vandevel ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d%15.6g' % ( name, x, k, em ) )
#
#  Improved Van de Vel iteration.
#
  if ( 1 <= nder ):
    name = 'Van de Vel improved'
    x = a
    x, em, ierror, k = vandevel_improved ( x, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d%15.6g' % ( name, x, k, em ) )
#
#  Bisection methods
#
  print ( '' )
  print ( '  6. Bisection methods' )
  print ( '' )
#
#  Bisection methods may only be used if there is a change of sign.
#
  if ( not change ):

    print ( '' )
    print ( 'zoomin_all_test():' )
    print ( '  Bisection methods will not be called since' )
    print ( '  there is no change of sign interval.' )

  else:
#
#  Bisection.
#
    name = 'Bisection'
    x = a
    x1 = b
    x, x1, ierror, k = bisect ( x, x1, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Regula falsi.
#
    name = 'Regula falsi'
    x = a
    x1 = b
    x, x1, ierror, k = regula ( x, x1, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Brent.
#
    name = 'Brent'
    x = a
    x1 = b
    x, x1, ierror, k = brent ( x, x1, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Bisection + secant.
#
    name = 'Bisection + secant'
    x = a
    x1 = b
    x, x1, ierror, k = rhein1 ( x, x1, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )
#
#  Bisection + secant + inverse quadratic.
#
    name = 'Bisection + secant + inv quad'
    x = a
    x1 = b
    x, x1, ierror, k = rhein2 ( x, x1, abserr, kmax, f )

    if ( ierror != 0 ):
      print ( '%30s%15.6g%8d error=%5d' % ( name, x, k, ierror ) )
    else:
      print ( '%30s%15.6g%8d' % ( name, x, k ) )

  return

def bisect ( x, x1, abserr, kmax, f ):

#*****************************************************************************80
#
## bisect() carries out the bisection method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, X1, two points defining the interval
#    in which the search will take place.  F(X) and F(X1) should have
#    opposite signs.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      value = function f ( x, ider )
#
#  Output:
#
#    real X, X1: X is the best estimate for the root, and X1 is
#    a recently computed point such that F changes sign in the interval
#    between X and X1.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
#
#  Evaluate the function at the starting points.
#
  fx = f ( x, 0 )
  fx1 = f ( x1, 0 )
#
#  Set XPOS and XNEG to the X values for which F(X) is positive
#  and negative, respectively.
#
  if ( 0.0 <= fx and fx1 <= 0.0 ):
    pass
  elif ( fx <= 0.0 and 0.0 <= fx1 ):
    t = x
    x = x1
    x1 = t
    t = fx
    fx = fx1
    fx1 = t
  else:
    ierror = 1
    return x, x1, ierror, k
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      break
#
#  Set the increment.
#
    dx = 0.5 * ( x1 - x )
#
#  Update the iterate and function values.
#
    x2 = x + dx
    fx2 = f ( x2, 0 )

    if ( 0.0 <= fx2 ):
      x = x2
      fx = fx2
    else:
      x1 = x2
      fx1 = fx2

  return x, x1, ierror, k

def brent ( x, x1, abserr, kmax, f ):

#*****************************************************************************80
#
## brent() implements the Brent bisection-based zero finder.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization without Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#  Input:
#
#    real X, X1.  Two points defining
#    the interval in which the search will take place.  F(X) and F(X1)
#    should have opposite signs.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1.  X is the best estimate for
#    the root, and X1 is a recently computed point such that F changes
#    sign in the interval between X and X1.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  fx1 = f ( x1, 0 )
  x2 = x1
  fx2 = fx1
#
#  Iteration
#
  while ( True ):

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, ierror, k

    if ( ( 0.0 < fx1 ) == ( 0.0 < fx2 ) ):
      x2 = x
      fx2 = fx
      d = x1 - x
      e = x1 - x

    if ( np.abs ( fx2 ) < np.abs ( fx1 ) ):
      t = x1
      x1 = x2
      x2 = t
      t = fx1
      fx1 = fx2
      fx2 = t

    eps = np.finfo ( float ).eps
    tol = 2.0 * eps * np.abs ( x1 ) + abserr
    em = 0.5 * ( x2 - x1 )

    if ( np.abs ( em ) <= tol or fx1 == 0.0 ):
      x = x1
      return x, x1, ierror, k

    if ( np.abs ( e ) < tol or np.abs ( fx ) <= np.abs ( fx1 ) ):

      d = em
      e = em

    else:

      s = fx1 / fx

      if ( x == x2 ):
        p = 2.0 * em * s
        q = 1.0 - s
      else:
        q = fx / fx2
        r = fx1 / fx2
        p = s * ( 2.0 * em * q * ( q - r ) - ( x1 - x ) * ( r - 1.0 ) )
        q = ( q - 1.0 ) * ( r - 1.0 ) * ( s - 1.0 )

      if ( 0 < p ):
        q = - q
      else:
        p = - p

      s = e
      e = d

      if ( 2.0 * p < 3.0 * em * q - np.abs ( tol * q ) or p < np.abs ( 0.5 * s * q ) ):
        d = p / q
      else:
        d = em
        e = em
#
#  Set the increment.
#
    if ( tol < np.abs ( d ) ):
      dx = + d
    elif ( 0.0 < em ):
      dx = + tol
    else:
      dx = - tol
#
#  Remember current data for next step.
#
    x = x1
    fx = fx1
#
#  Update the iterate and function values.
#
    x1 = x1 + dx
    fx1 = f ( x1, 0 )

  return x, x1, ierror, k

def c8_muller ( func, fatol, itmax, x1, x2, x3, xatol, xrtol ):

#*****************************************************************************80
#
## c8_muller() carries out Muller's method, using C8 arithmetic.
#
#  Discussion:
#
#    "C8" arithmetic is complex double precision arithmetic.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
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
#    external FUNC, the name of the routine that evaluates the function.
#    FUNC should have the form:
#      function func ( x, fx )
#      complex fx
#      complex x
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

  print ( '' )
  print ( 'c8_muller():' )
  print ( '  Muller method (complex root version)' )
  print ( '' )
  print ( '  Iteration     x_real              x_imag', end = 'None' )
  print ( '             orfxor           ordiscor' )
  print ( '' )

  iterate = -2
  print ( '%d6,%20.10f,%20.10f,%20.10f' % ( iterate, xold, np.abs ( fxold ) ) )
  iterate = -1
  print ( '%d6,%20.10f,%20.10f,%20.10f' % ( iterate, xmid, np.abs ( fxmid ) ) )
  iterate = 0
  print ( '%d6,%20.10f,%20.10f,%20.10f' % ( iterate, xnew, np.abs ( fxnew ) ) )

  if ( np.abs ( fxnew ) < fatol ):
    print ( '' )
    print ( 'c8_muller():' )
    print ( '  |F(X)| is below the tolerance.' )
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
      print ( '' )
      print ( 'c8_muller():' )
      print ( '  Maximum number of steps taken.' )
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
    discrm = b * b - 4.0 * a * c

    if ( a == 0.0 ):
      print ( '' )
      print ( 'c8_muller():' )
      print ( '  The algorithm has broken down.' )
      print ( '  The quadratic coefficient A is zero.' )
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
    print ( '(d6,20.10f,20.10f,20.10f,20.10f)', \
      iterate, xnew, np.abs ( fxnew ), np.abs ( discrm ) )
#
#  Check for convergence.
#
    x_ave = np.abs ( xnew + xmid + xold ) / 3.0
    x_inc = xnew - xmid

    if ( np.abs ( x_inc ) <= xatol ):
      print ( '' )
      print ( 'c8_muller():' )
      print ( '  Absolute convergence of the X increment.' )
      break

    if ( np.abs ( x_inc ) <= xrtol * x_ave ):
      print ( '' )
      print ( 'c8_muller():' )
      print ( '  Relative convergence of the X increment.' )
      break

    if ( np.abs ( fxnew ) <= fatol ):
      print ( '' )
      print ( 'c8_muller():' )
      print ( '  Absolute convergence of |F(X)|.' )
      return xnew, fxnew

  return xnew, fxnew

def cap_phi_03 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## cap_phi_03() implements the Traub capital Phi(0,3) method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 232.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: if IERROR = 0, X is an approximate root for which
#    abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
  d2fx = f ( x, 2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    z = 1.0 - 2.0 * fx * d2fx / ( dfx * dfx )
#
#  Set the increment.
#
    if ( 0.0 < z ):
      dx = - 2.0 * ( fx / dfx ) / ( 1.0 + np.sqrt ( z ) )
    else:
      dx = - fx / dfx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )

  return x, ierror, k

def cap_phi_21 ( x, x1, x2, abserr, kmax, f ):

#*****************************************************************************80
#
## cap_phi_21() implements the Traub capital PHI(2,1) function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964.
#
#  Input:
#
#    real X, X1, X2: three distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1, X2: X is an approximation which satisfies
#    abs ( F(X) ) < ABSERR, and X1 and X2 are the previous estimates.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    Output, integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = -2
  fx2 = f ( x2, 0 )
  k = -1
  fx1 = f ( x1, 0 )
  k = 0
  fx = f ( x, 0 )

  if ( x1 == x2 ):
    ierror = 3
    return x, x1, x2, ierror, k

  d1 = ( fx1 - fx2 ) / ( x1 - x2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, x2, ierror, k

    d2 = d1

    if ( x == x1 ):
      ierror = 3
      return x, x1, x2, ierror, k

    d1 = ( fx - fx1 ) / ( x - x1 )

    if ( x == x2 ):
      ierror = 3
      return x, x1, x2, ierror, k

    d2 = ( d1 - d2 ) / ( x - x2 )

    z = d1 + ( x - x1 ) * d2
    det = z * z - 4.0 * fx * d2
    det = max ( det, 0.0 )
#
#  Set the increment.
#
    if ( z + np.sqrt ( det ) == 0.0 ):
      ierror = 4
      return x, x1, x2, ierror, k

    dx = - 2.0 * fx / ( z + np.sqrt ( det ) )
#
#  Remember current data for next step.
#
    x2 = x1
    fx2 = fx1

    x1 = x
    fx1 = fx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, x1, x2, ierror, k

def chebyshev ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## chebyshev() implements Chebyshev's method.
#
#  Discussion:
#
#    This is also known as the Euler-Chebyshev method.
#
#    x(n+1) = x(n) - ( f(x(n)) / f'(x(n)) ) * ( 1 + 0.5 * L(x(n)) )
#
#    where
#
#      L(x) = f(x) * f''(x) / f'(x)**2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: if IERROR = 0, X is an approximate root for which
#    abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
  d2fx = f ( x, 2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = d2fx * fx / dfx / dfx

    if ( 1.0 + 0.5 * u == 0.0 ):
      ierror = 4
      return x, ierror, k
#
#  Set the increment.
#
    dx = - ( fx / dfx ) * ( 1.0 + 0.5 * u )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )

  return x, ierror, k

def dagger_e12 ( x, x1, abserr, kmax, f ):

#*****************************************************************************80
#
## dagger_e12() implements the dagger E 1,2 algorithm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 234.
#
#  Input:
#
#    real X, X1, distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1: X is an approximation to a root of the equation
#    which satisfies abs ( F(X) ) < ABSERR, and X1 is the
#    previous estimate.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )

  dfx1 = f ( x1, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, x1, ierror, k

    if ( x - x1 == 0.0 ):
      ierror = 3
      return x, x1, ierror, k

    d = ( dfx - dfx1 ) / ( x - x1 )
#
#  Set the increment.
#
    dx = - ( fx / dfx ) - 0.5 * ( fx / dfx ) * ( fx / dfx ) * d / dfx
#
#  Remember current data for next step.
#
    x1 = x
    dfx1 = dfx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, x1, ierror, k

def e3 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## e3() implements the Traub E3 method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 232.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which
#    abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = fx / dfx
    v = d2fx / ( 2.0 * dfx )
#
#  Set the increment.
#
    dx = - ( fx / dfx ) * ( 1.0 + v * u )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def e4 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## e4() implements the Traub E4 method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 232.
#
#  Input:
#
#    real X, an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    Ireal X: an approximate root for which
#    abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
  d2fx = f ( x, 2 )
  d3fx = f ( x, 3 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = fx / dfx
    v = d2fx / ( 2.0 * dfx )
    w = d3fx / ( 6.0 * dfx )
#
#  Set the increment.
#
    dx = - u * ( 1.0 + u * ( v + u * ( 2.0 * v * v - w ) ) )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )
    d3fx = f ( x, 3 )

  return x, ierror, k

def euler ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## euler() implements the Euler method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: f IERROR = 0, X is an approximate root for which
#    abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
  d2fx = f ( x, 2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    z = dfx * dfx - 2.0 * fx * d2fx
#
#  Set the increment.
#
    if ( 0.0 < z ):

      if ( dfx + np.sqrt ( z ) == 0.0 ):
        ierror = 3
        return x, ierror, k

      dx = - 2.0 * fx / ( dfx + np.sqrt ( z ) )

    else:

      if ( dfx == 0.0 ):
        ierror = 3
        return x, ierror, k

      dx = - fx / dfx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )

  return x, ierror, k

def func01 ( x, ider ):

#*****************************************************************************80
#
## func01() computes the function value for the first test.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which the evaluation is to take place.
#
#    integer IDER, specifies what is to be evaluated:
#    0, evaluate the function.
#    1, evaluate the first derivative.
#    2, evaluate the second derivative.
#    3, evaluate the third derivative.
#
#  Output:
#
#    real value: the value of the function or derivative.
#
  if ( ider == 0 ):
    value = ( x + 3.0 ) * ( x + 3.0 ) * ( x - 2.0 )
  elif ( ider == 1 ):
    value = ( x + 3.0 ) * ( 3.0 * x - 1.0 )
  elif ( ider == 2 ):
    value = 6.0 * x + 8.0
  elif ( ider == 3 ):
    value = 6.0
  else:
    print ( '' )
    print ( 'func01(): Fatal error' )
    print ( '  Requested derivative of order IDER = ', ider )
    raise Exception ( 'func01(): Fatal error!' )

  return value

def func02 ( x, ider ):

#*****************************************************************************80
#
## func02() computes the function value for the second test.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which the evaluation is to take place.
#
#    integer IDER, specifies what is to be evaluated:
#    0, evaluate the function.
#    1, evaluate the first derivative.
#    2, evaluate the second derivative.
#    3, evaluate the third derivative.
#
#  Output:
#
#    real value: the value of the function or derivative.
#
  import numpy as np

  if ( ider == 0 ):
    value = np.cos ( x ) - x
  elif ( ider == 1 ):
    value = - np.sin ( x ) - 1.0
  elif ( ider == 2 ):
    value = - np.cos ( x )
  elif ( ider == 3 ):
    value = np.sin ( x )
  else:
    print ( '' )
    print ( 'func02(): Fatal error!' )
    print ( '  Requested derivative of order IDER = ', ider )
    raise Exception ( 'func02(): Fatal error!' )

  return value

def halley1 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## halley1() implements Halley's method.
#
#  Discussion:
#
#    x(n+1) = x(n) - ( f(x(n)) / f'(x(n)) ) / ( 1 - 0.5 * L(x(n)) )
#
#    where
#
#      L(x) = f(x) * f''(x) / f'(x)**2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which
#    abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
  d2fx = f ( x, 2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = d2fx * fx / dfx / dfx

    if ( 2.0 - u == 0.0 ):
      ierror = 4
      return x, ierror, k
#
#  Set the increment.
#
    dx = - ( fx / dfx ) / ( 1.0 - 0.5 * u )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )

  return x, ierror, k

def halley2 ( x, x1, x2, abserr, kmax, f ):

#*****************************************************************************80
#
## halley2() implements Halley's method, with finite differences.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, X1, X2: three distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1, X2: X is an approximate root of the equation
#    which satisfies abs ( F(X) ) < ABSERR, and X1 and X2 are the
#    previous estimates.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  fx1 = f ( x1, 0 )
  fx2 = f ( x2, 0 )

  d1 = ( fx1 - fx2 ) / ( x1 - x2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, x2, ierror, k

    d2 = d1

    if ( x == x1 ):
      ierror = 3
      return x, x1, x2, ierror, k

    d1 = ( fx - fx1 ) / ( x - x1 )

    if ( x == x2 ):
      ierror = 3
      return x, x1, x2, ierror, k

    d2 = ( d1 - d2 ) / ( x - x2 )

    if ( d1 == 0.0 ):
      ierror = 3
      return x, x1, x2, ierror, k

    z = d1 - fx1 * d2 / d1

    if ( z == 0.0 ):
      ierror = 3
      return x, x1, x2, ierror, k
#
#  Set the increment.
#
    dx = - fx / z
#
#  Remember current data for next step.
#
    x2 = x1
    fx2 = fx1
    x1 = x
    fx1 = fx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, x1, x2, ierror, k

def halley_super ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## halley_super() implements the super Halley method.
#
#  Discussion:
#
#    x(n+1) = x(n) - 0.5 * ( f(x(n)) / f'(x(n)) )
#      * ( 2 - L(x(n)) ) / ( 1 - L(x(n)) )
#
#    where
#
#      L(x) = f(x) * f''(x) / f'(x)**2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
  d2fx = f ( x, 2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = d2fx * fx / dfx /dfx

    if ( 1.0 - u == 0.0 ):
      ierror = 4
      return x, ierror, k
#
#  Set the increment.
#
    dx = - 0.5 * ( fx / dfx ) * ( 2.0 - u ) / ( 1.0 - u )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )

  return x, ierror, k

def hansen ( x, beta, abserr, kmax, f ):

#*****************************************************************************80
#
## hansen() implements the Hansen and Patrick method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eldon Hansen, Merrell Patrick,
#    A Family of Root Finding Methods,
#    Numerische Mathematik,
#    Volume 27, 1977, pages 257 - 269.
#
#  Input:
#
#    real X, an estimate for the root of the equation.
#
#    real BETA, ???
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: if IERROR = 0, X is an approximate root for which
#    abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
  d2fx = f ( x, 2 )

  print ( 'hansen: %d  %g  %g' % ( k, x, fx ) )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    z = dfx * dfx - ( beta + 1.0 ) * fx * d2fx
    z = max ( z, 0.0 )

    bot = beta * dfx + np.sqrt ( z )

    if ( bot == 0.0 ):
      ierror = 3
      return x, ierror, k
#
#  Set the increment.
#
    dx = - ( beta + 1.0 ) * fx / bot
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )

    print ( 'hansen: %d  %g  %g' % ( k, x, fx ) )

  return x, ierror, k

def jarratt2 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## jarratt2() implements the inverse-free Jarratt fourth order method.
#
#  Discussion:
#
#    Jarratt's inverse-free method is of fourth order.
#
#    x(n+1) = x(n) - u(x(n)) + (3/4) * u(x(n)) * h(x(n)) * ( 1-(3/2)*h(x(n)) )
#
#    where
#
#      u(x) = f(x) / f'(x)
#      h(x) = ( f'(x-(2/3)*u(x)) - f'(x) ) / f'(x)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    P Jarratt,
#    Some fourth-order multipoint iterative methods for solving equations,
#    Mathematics of Computation,
#    Volume 20, Number 95, 1966, pages 434 - 437.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    ux = fx / dfx

    hx = ( f ( x - 2.0 / 3.0 * ux, 1 ) - dfx ) / dfx
#
#  Set the increment.
#
    dx = - ux + 0.75 * ux * hx * ( 1.0 - 1.5 * hx )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, ierror, k

def jarratt ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## jarratt() implements the Jarratt fourth order method.
#
#  Discussion:
#
#    Jarratt's method is of fourth order.
#
#    x(n+1) = x(n) - 1/2 * ( f(x(n) / f'(x(n)) )
#      + f(x(n)) / ( f'(x(n)) - 3*f'( x(n)-(2/3)*f(x(n))/f'(x(n)) ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    P Jarratt,
#    Some fourth-order multipoint iterative methods for solving equations,
#    Mathematics of Computation,
#    Volume 20, Number 95, 1966, pages 434 - 437.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    z = x - 2.0 * fx / ( 3.0 * dfx )
    dfz = f ( z, 1 )

    if ( dfx - 3.0 * dfz == 0.0 ):
      ierror = 3
      return x, ierror, k
#
#  Set the increment.
#
    dx = ( - 0.5 / dfx + 1.0 / ( dfx - 3.0 * dfz ) ) * fx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, ierror, k

def king ( x, beta, abserr, kmax, f ):

#*****************************************************************************80
#
## king() implements a family of fourth order methods.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard King,
#    A family of fourth order methods,
#    SIAM Journal on Numerical Analysis,
#    Volume 10, 1973, pages 876 - 879.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real BETA, a parameter in the algorithm.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    w = x - fx / dfx
    fw = f ( w, 0 )

    if ( fx + ( beta - 2.0 ) * fw == 0.0 ):
      ierror = 3
      return x, ierror, k
#
#  Set the increment.
#
    dx = - ( fx / dfx ) - ( fw / dfx ) \
      * ( fx + beta * fw ) / ( fx + ( beta - 2.0 ) * fw )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, ierror, k

def laguerre ( x0, ipoly, abserr, kmax, f ):

#*****************************************************************************80
#
## laguerre() implements the Laguerre rootfinding method for polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eldon Hansen, Merrell Patrick,
#    A Family of Root Finding Methods,
#    Numerische Mathematik,
#    Volume 27, 1977, pages 257 - 269.
#
#  Input:
#
#    real X0.
#    An initial estimate for the root of the equation.
#
#    integer IPOLY: the polynomial degree of the function.
#    IPOLY must be at least 2.
#
#    real ABSERR: an error tolerance.
#
#    integer KMAX: the maximum number of iterations allowed.
#
#    real external F: the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: the estimated solution, if IERROR=0.
#
#    integer IERROR: error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K: the number of steps taken.
#
  import numpy as np
#
#  Check.
#
  if ( ipoly < 2 ):
    ierror = 1
    print ( '' )
    print ( 'laguerre(): Fatal error!' )
    print ( '  IPOLY < 2' )
    raise Exception ( 'laguerre(): Fatal error!' )
#
#  Initialization.
#
  ierror = 0
  x = x0

  beta = 1.0 / ( ipoly - 1 )

  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
  d2fx = f ( x, 2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    z = dfx * dfx - ( beta + 1.0 ) * fx * d2fx
    z = max ( z, 0.0 )

    bot = beta * dfx + np.sqrt ( z )

    if ( bot == 0.0 ):
      ierror = 3
      return x, ierror, k
#
#  Set the increment.
#
    dx = - ( beta + 1.0 ) * fx / bot
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )

  return x, ierror, k

def midpoint ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## midpoint() implements the midpoint method.
#
#  Discussion:
#
#    The midpoint method is of order 3.
#
#    x(n+1) = x(n) - f(x(n)) / g(x(n))
#
#    where
#
#    g(x) = f'( x - f(x) / ( 2 * f'(x) ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 164.
#
#  Input:
#
#    real X, the point that starts the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root satisfying abs ( F(X) ) < ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0

  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    dfx = f ( x, 1 )

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k
 
    arg = x - fx / ( 2.0 * dfx )
    gx = f ( arg, 1 )

    if ( gx == 0.0 ):
      ierror = 4
      return x, ierror, k
#
#  Set the increment.
#
    dx = - fx / gx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def newton ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## newton() implements Newton's method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    dfx = f ( x, 1 )

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k
#
#  Set the increment.
#
    dx = - fx / dfx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def newton_mod ( x, nsub, abserr, kmax, f ):

#*****************************************************************************80
#
## newton_mod() implements the modified Newton method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 236.
#
#  Input:
#
#    real X: n estimate for the root of the equation.
#
#    integer NSUB, the number of steps in the sub-iteration.
#    The derivative is only evaluated before the first step,
#    and after every subsequent NSUB steps.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( ( k - 1 ) % nsub == 0 ):

      dfx = f ( x, 1 )

      if ( dfx == 0.0 ):
        ierror = 3
        return x, ierror, k
#
#  Set the increment.
#
    dx = - fx / dfx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def newton_secant ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## newton_secant() implements the Newton - secant method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 236.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR: an error tolerance.
#
#    integer KMAX: the maximum number of iterations allowed.
#
#    real external F: the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR: error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K: the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    dfx = f ( x, 1 )

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    x1 = x - fx / dfx
    fxu = f ( x1, 0 )

    if ( fxu - fx == 0.0 ):
      ierror = 3
      return x, ierror, k
#
#  Set the increment.
#
    dx = - ( fx / dfx ) * ( 1.0 - fxu / ( fxu - fx ) )
#
#  Remember current data for next step.
#
    x1 = x
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def ostrowski_sqrt ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## ostrowski_sqrt() implements the Ostrowski square root method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eldon Hansen, Merrell Patrick,
#    A Family of Root Finding Methods,
#    Numerische Mathematik,
#    Volume 27, 1977, pages 257 - 269.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
  d2fx = f ( x, 2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    z = dfx * dfx - fx * d2fx
#
#  Set the increment.
#
    if ( 0.0 < z ):
      bot = np.sqrt ( z )
    else:
      bot = dfx

    dx = - fx / bot
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )

  return x, ierror, k

def perp_e_12 ( x, x1, abserr, kmax, f ):

#*****************************************************************************80
#
## perp_e_12() implements the Traub E 1,2 algorithm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 234.
#
#  Input:
#
#    real X, X1: two distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1: X is an approximate root
#    satisfiying abs ( F(X) ) < ABSERR, and X1 is the previous
#    estimate.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
  fx1 = f ( x1, 0 )
  dfx1 = f ( x1, 1 )

  if ( dfx1 == 0.0 ):
    ierror = 3
    return x, x1, ierror, k
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, x1, ierror, k

    if ( dfx1 == 0.0 ):
      ierror = 3
      return x, x1, ierror, k

    if ( fx == fx1 ):
      ierror = 3
      return x, x1, ierror, k

    z = 2.0 / dfx + 1.0 / dfx1 - 3.0 * ( x - x1 ) / ( fx - fx1 )
#
#  Set the increment.
#
    dx = - fx / dfx + fx * fx * z / ( fx - fx1 )
#
#  Remember current data for next step.
#
    x1 = x
    fx1 = fx
    dfx1 = dfx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, x1, ierror, k

def perp_e_21 ( x, x1, x2, abserr, kmax, f ):

#*****************************************************************************80
#
## perp_e_21() implements the Traub perp E 21 method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 233.
#
#  Input:
#
#    real X, X1, X2: three distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1, X2: X is an approximate root satisfying
#    abs ( F(X) ) < ABSERR, and X1 and X2 are the previous estimates.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  fx1 = f ( x1, 0 )
  fx2 = f ( x2, 0 )

  if ( x1 == x2 ):
    ierror = 3
    return x, x1, x2, ierror, k

  d1 = ( fx1 - fx2 ) / ( x1 - x2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, x2, ierror, k

    d2 = d1

    if ( x == x1 ):
      ierror = 3
      return x, x1, x2, ierror, k

    if ( x == x2 ):
      ierror = 3
      return x, x1, x2, ierror, k

    d1 = ( fx - fx1 ) / ( x - x1 )
    d = ( fx - fx2 ) / ( x - x2 )
#
#  Set the increment.
#
    dx = - fx * ( 1.0 / d1 + 1.0 / d - 1.0 / d2 )
#
#  Remember current data for next step.
#
    x2 = x1
    fx2 = fx1
    x1 = x
    fx1 = fx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, x1, x2, ierror, k

def phi_12 ( x, x1, abserr, kmax, f ):

#*****************************************************************************80
#
## phi_12() implements the Traub capital PHI(1,2) method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 233.
#
#  Input:
#
#    real X, X1: two distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1: X is an approximate root satisfying
#    abs ( F(X) ) < ABSERR, and X1 is the previous estimate.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  fx1 = f ( x1, 0 )
  dfx1 = f ( x1, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, ierror, k

    dfx = f ( x, 1 )

    if ( dfx == 0.0 ):
      ierror = 3
      return x, x1, ierror, k

    c = fx - fx1

    if ( x == x1 ):
      ierror = 3
      return x, x1, ierror, k

    d = ( fx - fx1 ) / ( x - x1 )

    h = 1.0 / c * ( 1.0 / dfx - 1.0 / d ) - ( fx1 / c / c ) * \
      ( 1.0 / dfx + 1.0 / dfx1 - 2.0 / d )
#
#  Set the increment.
#
    dx = - ( fx / dfx ) + fx * fx * h
#
#  Remember current data for next step.
#
    x1 = x
    fx1 = fx
    dfx1 = dfx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, x1, ierror, k

def psi_21 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## psi_21() implements the Traub PSI 2,1 method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 232.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )
    d3fx = f ( x, 3 )

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = fx / dfx
    v = d2fx / ( 2.0 * dfx )
    w = d3fx / ( 6.0 * dfx )
#
#  Set the increment.
#
    dx = - u * ( v - u * ( v * v - w ) ) / ( v - u * ( 2.0 * v * v - w ) )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def psi_i2 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## psi_12() implements the Traub PSI 1,2 method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 232.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )
    d3fx = f ( x, 3 )

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = fx / dfx
    v = d2fx / ( 2.0 * dfx )
    w = d3fx / ( 6.0 * dfx )
#
#  Set the increment.
#
    dx = - u / ( 1.0 - u * v + ( v * v - w ) * u * u )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def r8_muller ( x, x1, x2, abserr, kmax, f ):

#*****************************************************************************80
#
## r8_muller() implements Muller's method for real arithmetic.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, X1, X2: three distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1, X2: X is an approximate root satisfying
#    abs ( F(X) ) < ABSERR, and X1 and X2 are the previous estimates.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx2 = f ( x2, 0 )
  fx1 = f ( x1, 0 )
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, x2, ierror, k

    q = ( x - x1 ) / ( x1 - x2 )

    a = q * fx - q * ( 1.0 + q ) * fx1 + q * q * fx2
    b = ( 2.0 * q + 1.0 ) * fx - ( 1.0 + q ) * ( 1.0 + q ) * fx1 + q * q * fx2
    c = ( 1.0 + q ) * fx

    term = b * b - 4.0 * a * c
    term = max ( term, 0.0 )
    term = np.sqrt ( term )
    if ( b < 0.0 ):
      term = - term
#
#  Set the increment.
#
    dx = - ( x - x1 ) * 2.0 * c / ( b + term )
#
#  Remember current data for next step.
#
    x2 = x1
    fx2 = fx1
    x1 = x
    fx1 = fx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, x1, x2, ierror, k

def red_cap_phi_04 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## red_cap_phi_04() implements the Traub reduced capital PHI(0,4) method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 232.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )
    d3fx = f ( x, 3 )

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = fx / dfx
    v = d2fx / ( 2.0 * dfx )
    w = d3fx / ( 6.0 * dfx )
    z = 1.0 - 4.0 * u * ( v - u * w )
#
#  Set the increment.
#
    if ( 0.0 < z ):
      dx = - 2.0 * u / ( 1.0 + np.sqrt ( z ) )
    else:
      dx = - fx / dfx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def regula ( x, x1, abserr, kmax, f ):

#*****************************************************************************80
#
## regula() implements the Regula Falsi method.
#
#  Discussion:
#
#    The algorithm was modified to guarantee that f(x) <= f(x1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, X1: two distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1: X is an approximate root satisfying
#    abs ( F(X) ) < ABSERR, and X1 is the previous estimate.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0

  fx = f ( x, 0 )
  fx1 = f ( x1, 0 )

  if ( fx < 0.0  ):
    t = x
    x = x1
    x1 = t
    t = fx
    fx = fx1
    fx1 = t
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, ierror, k
#
#  Set the increment.
#
    dx = - fx1 * ( x - x1 ) / ( fx - fx1 )
#
#  Update the iterate and function values.
#
    x2 = x1 + dx
    fx2 = f ( x2, 0 )

    if ( 0.0 <= fx2 ):
      x = x2
      fx = fx2
    else:
      x1 = x2
      fx1 = fx2
#
#  Let x,fx be minimal.
#
    if ( np.abs ( fx1 ) < np.abs ( fx ) ):
      t = x
      x = x1
      x1 = t
      t = fx
      fx = fx1
      fx1 = t

  return x, x1, ierror, k

def rhein1 ( x, x1, abserr, kmax, f ):

#*****************************************************************************80
#
## rhein1() implements the Rheinboldt bisection - secant method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Werner Rheinboldt,
#    Algorithms for finding zeros of a function,
#    UMAP Journal,
#    Volume 2, Number 1, 1981, pages 43 - 72.
#
#  Input:
#
#    real X, X1: two distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1: X is an approximate root satisfying
#    abs ( F(X) ) < ABSERR, and X1 is the previous estimate.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  i = 0
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  fx1 = f ( x1, 0 )

  if ( np.abs ( fx1 ) < np.abs ( fx ) ):
    t = x
    x = x1
    x1 = t
    t = fx
    fx = fx1
    fx1 = t

  x2 = x1
  fx2 = fx1
  t = 0.5 * np.abs ( x - x1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, ierror, k
#
#  Force ABS ( FX ) <= ABS ( FX1 ).
#
    if ( np.abs ( fx1 ) < np.abs ( fx ) ):

      x2 = x
      x = x1
      x1 = x2

      fx2 = fx
      fx = fx1
      fx1 = fx2

    em = 0.5 * ( x1 - x )
#
#  Compute the numerator and denominator for secant step.
#
    p = ( x - x2 ) * fx
    q = fx2 - fx

    if ( p < 0.0 ):
      p = - p
      q = - q
#
#  Save the old minimum residual point.
#
    x2 = x
    fx2 = fx
#
#  Test for forced bisection.
#
    i = i + 1
    forced = False

    if ( 3 < i ):
      if ( t < 8.0 * np.abs ( em ) ):
        forced = True
      else:
        i = 0
        t = em
#
#  Set the increment.
#
    if ( forced ):
      dx = em
    elif ( p <= np.abs ( q ) * abserr ):
      dx = np.sign ( em ) * abserr
    elif ( p < q * em ):
      dx = p / q
    else:
      dx = em
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
#
#  Preserve the change of sign interval.
#
    if ( np.sign ( fx ) == np.sign ( fx1 ) ):
      x1 = x2
      fx1 = fx2

  return x, x1, ierror, k

def rhein2 ( x, x1, abserr, kmax, f ):

#*****************************************************************************80
#
## rhein2() implements the Rheinboldt bisection/secant/inverse quadratic method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Werner Rheinboldt,
#    Algorithms for Finding Zeros of a Function,
#    UMAP Journal,
#    Volume 2, Number 1, 1981, pages 43 - 72.
#
#  Input:
#
#    real X, X1: two distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1: X is an approximate root satisfying
#    abs ( F(X) ) < ABSERR, and X1 is the previous estimate.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  i = 0
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  fx1 = f ( x1, 0 )

  if ( np.abs ( fx1 ) < np.abs ( fx ) ):
    s = x
    x = x1
    x1 = s
    s = fx
    fx = fx1
    fx1 = s

  x2 = x1
  fx2 = fx1
  k = 0
  t = 0.5 * np.abs ( x - x1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, ierror, k

    i = i + 1

    em = 0.5 * ( x1 - x )
#
#  Compute the numerator and denominator for secant step.
#
    if ( 2.0 * np.abs ( x2 - x ) < np.abs ( x1 - x ) ):
      ps = ( x - x2 ) * fx
      qs = fx2 - fx
    else:
      ps = ( x - x1 ) * fx
      qs = fx1 - fx
 
    if ( ps < 0.0 ):
      ps = - ps
      qs = - qs
#
#  Compute the numerator and denominator for inverse quadratic.
#
    piq = 0.0
    qiq = 0.0

    if ( x1 != x2 ):
      u = fx / fx2
      v = fx2 / fx1
      w = fx / fx1
      piq = u * ( 2.0 * em * v * ( v - w ) - ( x - x2 ) * ( w - 1.0 ) )
      qiq = ( u - 1.0 ) * ( v - 1.0 ) * ( w - 1.0 )

      if ( 0.0 < piq ):
        qiq =  - qiq

      piq = np.abs ( piq )
#
#  Save the old minimum residual point.
#
    x2 = x
    fx2 = fx

    stpmin = ( np.abs ( x ) + np.abs ( em ) + 1.0 ) * abserr
#
#  Choose bisection, secant or inverse quadratic step.
#
    forced = False

    if ( 3 < i ):
      if ( t < 8.0 * np.abs ( em ) ):
        forced = True
      else:
        i = 0
        t = em
#
#  Set the increment.
#
    if ( forced ):
      dx = em
    elif ( piq < 1.5 * em * qiq and np.abs ( qiq ) * stpmin < np.abs ( piq ) ):
      dx = piq / qiq
    elif ( ps < qs * em and np.abs ( qs ) * stpmin < np.abs ( ps ) ):
      dx = ps / qs
    else:
      dx = em
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
#
#  Set the new X1 as either X1 or X2, depending on whether
#  F(X1) or F(X2) has the opposite sign from F(X).
#
    if ( np.sign ( fx ) == np.sign ( fx1 ) ):
      x1 = x2
      fx1 = fx2
#
#  Force ABS ( FX ) <= ABS ( FX1 ).
#
    if ( np.abs ( fx1 ) < np.abs ( fx ) ):
      s = x
      x = x1
      x1 = s
      s = fx
      fx = fx1
      fx1 = s

  return x, x1, ierror, k

def script_e2 ( x, m, abserr, kmax, f ):

#*****************************************************************************80
#
## script_e2() implements the Traub script E - 2 function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 234.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    integer M, the multiplicity of the root.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k
#
#  Set the increment.
#
    dx = - m * fx / dfx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, ierror, k

def script_e3 ( x, m, abserr, kmax, f ):

#*****************************************************************************80
#
## script_e3() implements the Traub script E - 3 function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 235.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    integer M, the multiplicity of the root.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  em = m
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = fx / dfx
    a2 = d2fx / ( 2.0 * dfx )
#
#  Set the increment.
#
    dx = - em * u * ( ( 3.0 - em ) / 2.0 + em * a2 * u )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def script_e4 ( x, m, abserr, kmax, f ):

#*****************************************************************************80
#
## script_e4() implements the Traub script E - 4 function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 235.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    integer M, the multiplicity of the root.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  em = m
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )
    d3fx = f ( x, 3 )

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = fx / dfx
    a2 = d2fx / ( 2.0 * dfx )
    a3 = d3fx / ( 6.0 * dfx )
#
#  Set the increment.
#
    dx = - em * u * ( ( em * em - 6.0 * em + 11.0 ) / 6.0 \
       + em * ( 2.0 - em ) * a2 * u \
       + em * em * ( 2.0 * a2 * a2 - a3 ) * u * u )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def secant_extended ( x, x1, x2, abserr, kmax, f ):

#*****************************************************************************80
#
## secant_extended() carries out the extended secant algorithm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, X1, X3: three distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1, X3: X is an approximate root satisfying
#    abs ( F(X) ) < ABSERR, and X1 and X2 are two previous estimates.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0

  fx1 = f ( x1, 0 )
  fx2 = f ( x2, 0 )
  d1 = ( fx1 - fx2 ) / ( x1 - x2 )

  if ( d1 == 0.0 ):
    ierror = 3
    return x, x1, x2, ierror, k

  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, x2, ierror, k

    d2 = d1

    if ( x == x1 ):
      ierror = 3
      return x, x1, x2, ierror, k
 
    d1 = ( fx - fx1 ) / ( x - x1 )

    if ( d1 == 0.0 ):
      ierror = 3
      return x, x1, x2, ierror, k

    if ( fx2 == fx1 ):
      ierror = 3
      return x, x1, x2, ierror, k
#
#  Set the increment.
#
    dx = - fx / d1 + ( fx * fx1 / ( fx - fx2 ) ) * ( 1.0 / d1 - 1.0 / d2 )
#
#  Remember current data for next step.
#
    x2 = x1
    fx2 = fx1
    x1 = x
    fx1 = fx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, x1, x2, ierror, k

def secant ( x, x1, abserr, kmax, f ):

#*****************************************************************************80
#
## secant() implements the secant method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964.
#
#  Input:
#
#    real X, X1: two distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1: X is an approximate root satisfying
#    abs ( F(X) ) < ABSERR, and X1 is the previous estimate.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  fx1 = f ( x1, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, ierror, k

    if ( fx - fx1 == 0.0 ):
      ierror = 3
      return x, x1, ierror, k
#
#  Set the increment.
#
    dx = - fx * ( x - x1 ) / ( fx - fx1 )
#
#  Remember current data for next step.
#
    x1 = x
    fx1 = fx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, x1, ierror, k

def star_e12 ( x, x1, abserr, kmax, f ):

#*****************************************************************************80
#
## star_e12() implements the Traub *E12 method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 234.
#
#  Input:
#
#    real X, X1: two distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1: X is an approximate root satisfying
#    abs ( F(X) ) < ABSERR, and X1 is the previous estimate.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )

  fx1 = f ( x1, 0 )
  dfx1 = f ( x1, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, x1, ierror, k

    u = fx / dfx

    if ( x == x1 ):
      ierror = 3
      return x, x1, ierror, k

    d = ( fx - fx1 ) / ( x - x1 )
    z = 2.0 * dfx + dfx1 - 3.0 * d
#
#  Set the increment.
#
    dx = - u - u * u * z / ( dfx * ( x - x1 ) )
#
#  Remember current data for next step.
#
    x1 = x
    fx1 = fx
    dfx1 = dfx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, x1, ierror, k

def star_e21 ( x, x1, x2, abserr, kmax, f ):

#*****************************************************************************80
#
## star_e21() implements the Traub *E21 method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 234.
#
#  Input:
#
#    real X, X1, X2: three distinct points that start the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1, X2: X is an approximate root satisfying
#    abs ( F(X) ) < ABSERR, X1 and X2 are the previous estimates.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  fx1 = f ( x1, 0 )
  fx2 = f ( x2, 0 )
  d1 = ( fx1 - fx2 ) / ( x1 - x2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, x2, ierror, k

    d2 = d1

    if ( x == x1 ):
      ierror = 3
      return x, x1, x2, ierror, k

    d1 = ( fx - fx1 ) / ( x - x1 )

    if ( x == x2 ):
      ierror = 3
      return x, x1, x2, ierror, k

    d = ( fx - fx2 ) / ( x - x2 )

    if ( d1 + d - d2 == 0.0 ):
      ierror = 3
      return x, x1, x2, ierror, k
#
#  Set the increment.
#
    dx = - fx / ( d1 + d - d2 )
#
#  Remember current data for next step.
#
    x2 = x1
    fx2 = fx1

    x1 = x
    fx1 = fx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, x1, x2, ierror, k

def steffenson ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## steffenson() implements Steffenson's method.
#
#  Discussion:
#
#    Steffenson's method is of order 2.
#
#    x(n+1) = x(n) - f(x(n)) / g(x(n))
#
#    where
#
#    g(x) = ( f(x+f(x)) - f(x) ) / f(x)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 178.
#
#  Input:
#
#    real X: the point that starts the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root satisfying abs ( F(X) ) < ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    gx = ( f ( x + fx, 0 ) - fx ) / fx

    if ( gx == 0.0 ):
      ierror = 3
      return x, ierror, k
#
#  Set the increment.
#
    dx = - fx / gx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def stirling ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## stirling() implements Stirling's method.
#
#  Discussion:
#
#    Stirling's method is of order 2.
#
#    x(n+1) = x(n) - f(x(n)) / f'( x(n) - f(x(n) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X: the point that starts the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root satisfying abs ( F(X) ) < ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0

  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    gx = f ( x - fx, 1 )

    if ( gx == 0.0 ):
      ierror = 3
      return x, ierror, k
#
#  Set the increment.
#
    dx = - fx / gx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def t14 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## t14() implements the Traub fourteenth function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 237.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    dfxu = f ( x - ( fx / dfx ), 1 )

    if ( dfxu == 0.0 ):
      ierror = 3
      return x, ierror, k

    z = x - 0.25 * ( fx / dfx + fx / dfxu  )
    dfz = f ( z, 1 )
#
#  Set the increment.
#
    dx = - ( fx / dfx + ( fx / dfxu ) + 4.0 * ( fx / dfz ) ) / 6.0
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, ierror, k

def t15 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## t15() implements the Traub fifteenth function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 238.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    dfx = f ( x, 1 )

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = fx / dfx
    dfxu = f ( x - ( fx / dfx ), 1 )

    if ( dfxu == 0.0 ):
      ierror = 3
      return x, ierror, k

    z = x - 2.0 * ( 2.0 * u + fx / dfxu ) / 9.0
    dfz = f ( z, 1 )

    if ( dfz == 0.0 ):
      ierror = 3
      return x, ierror, k
#
#  Set the increment.
#
    dx = - 0.25 * ( fx / dfx + 3.0 * fx / dfz )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def t16 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## t16() implements the Traub sixteenth function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 238.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break
 
    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    dfx = f ( x, 1 )

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    dfxu = f ( x - ( fx / ( 3.0 * dfx ) ), 1 )

    if ( dfxu == 0.0 ):
      ierror = 3
      return x, ierror, k

    z = x - 2.0 * fx / ( 3.0 * dfxu )
    dfz = f ( z, 1 )

    if ( dfz == 0.0 ):
      ierror = 3
      return x, ierror, k
 #
#  Set the increment.
#
    dx = - 0.25 * ( fx / dfx + 3.0 * fx / dfz )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def te11f ( x, x1, m, abserr, kmax, f ):

#*****************************************************************************80
#
## te11f() implements the Traub *E - 1,1(f) function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 235.
#
#  Input:
#
#    real X, X1: two distinct points that start the method.
#
#    integer M, the multiplicity of the root.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X, X1: X is an approximate root satisfying
#    abs ( F(X) ) < ABSERR, and X1 is the previous estimate.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  expon = 1.0 / m
  fx1 = f ( x1, 0 )

  fnorm = np.abs ( fx1 )
  gx1 = np.sign ( fx1 ) * fnorm ** expon
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, x1, ierror, k

    fnorm = np.abs ( fx )
    gx = np.sign ( fx ) * fnorm ** expon

    if ( x == x1 ):
      ierror = 3
      return x, x1, ierror, k

    d = ( gx - gx1 ) / ( x - x1 )
#
#  Set the increment.
#
    dx = - gx / d
#
#  Remember current data for next step.
#
    gx1 = gx
    x1 = x
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, x1, ierror, k

def te2u ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## te2u() implements the Traub E - 2(u) function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 235.
#
#  Input:
#
#    real X: an estimate for the root.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    real EM, an estimate of the multiplicity of the root.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
  d2fx = f ( x, 2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, em, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, em, ierror, k

    if ( dfx * dfx - fx * d2fx == 0.0 ):
      ierror = 3
      return x, em, ierror, k

    em = dfx * dfx / ( dfx * dfx - fx * d2fx )
    em = max ( em, 1.0 )
#
#  Set the increment.
#
    dx = - em * fx / dfx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )

  return x, em, ierror, k

def t_family1 ( x, c, d, abserr, kmax, f ):

#*****************************************************************************80
#
## t_family1() implements the Traub first family of iterations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, pages 236 - 237.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real C, D, ???
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    z = x - d * fx / dfx
    dfz = f ( z, 1 )

    if ( dfz == 0.0 ):
      ierror = 3
      return x, ierror, k
#
#  Set the increment.
#
    dx = - ( c / dfx + ( 1.0 - c ) / dfz ) * fx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, ierror, k

def t_family2 ( x, a, b, c, d, abserr, kmax, f ):

#*****************************************************************************80
#
## t_family2() implements the Traub second family of iterations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 236 - 237.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real A, B, C, D, ???
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    z = x - d * fx / dfx
    dfz = f ( z, 1 )
#
#  Set the increment.
#
    dx = - fx * ( b * dfx - c * dfz ) / ( a * dfx * dfx )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, ierror, k

def tphi1u ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## tphi1u() implements the Traub phi - 1,1(u) function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 235.
#
#  Input:
#
#    real X: an estimate for the root.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X:  an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    real EM, an estimate of the multiplicity of the root.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  u1 = f ( x, 0 ) / f ( x, 1 )
  x = x - u1
  fx = f ( x, 0 )
  dfx = f ( x, 1 )

  fu1 = f ( u1, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, em, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, em, ierror, k

    u = fx / dfx
    fu = f ( u, 0 )

    em = ( u - u1 ) / ( fu - fu1 )
    em = max ( em, 1.0 )
#
#  Set the increment
#
    dx = - em * fx / dfx
#
#  Remember current data for next step.
#
    u1 = u
    fu1 = fu
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, em, ierror, k

def traub1 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## traub1() implements the Traub first method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 236.
#
#  Input:
#
#    real X: an estimate for the root.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    z = x - fx / dfx
    dfz = f ( z, 1 )

    if ( dfz == 0.0 ):
      ierror = 3
      return x, ierror, k
#
#  Set the increment.
#
    dx = - fx / dfz
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, ierror, k

def traub4 ( x, nsub, abserr, kmax, f ):

#*****************************************************************************80
#
## traub4() implements the Traub fourth method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 236.
#
#  Input:
#
#    real X: an estimate for the root.
#
#    integer NSUB, the number of steps in the sub-iteration.
#    The derivatives are only evaluated before the first step,
#    and after every subsequent NSUB steps.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( ( k - 1 ) % nsub == 0 ):

      dfx = f ( x, 1 )
      d2fx = f ( x, 2 )

      if ( dfx == 0.0 ):
        ierror = 3
        return x, ierror, k

      if ( dfx - d2fx * fx / dfx == 0.0 ):
        ierror = 3
        return x, ierror, k
#
#  Set the increment.
#
    dx = - fx / ( dfx - d2fx * fx / dfx )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def traub8 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## traub8() implements the Traub eighth function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964.
#
#  Input:
#
#    real X: an estimate for the root.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    dfxu = f ( x - 2.0 * fx / ( 3.0 * dfx ), 1 )
#
#  Set the increment.
#
    dx = - 4.0 * fx / ( dfx + 3.0 * dfxu )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, ierror, k

def traub9 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## traub9() implements the Traub ninth method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 237.
#
#  Input:
#
#    real X: an estimate for the root.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = fx / dfx
    xu = x - fx / dfx
    fxu = f ( xu, 0 )

    if ( 2.0 * fxu - fx == 0.0 ):
      ierror = 4
      return x, ierror, k
#
#  Set the increment.
#
    dx = - fx / dfx + u * fxu / ( 2.0 * fxu - fx )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, ierror, k

def traub_ostrowski ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## traub_ostrowski() implements the Traub-Ostrowksi method.
#
#  Discussion:
#
#    The Traub-Ostrowski method is of order 4.
#
#    x(n+1) = x(n) - u(x(n)) * ( f ( x(n) - u(x(n)) - f(x(n)) ) /
#      ( 2 * f ( x(n) - u(x(n)) - f(x(n)) )
#
#    where
#
#    u(x) = f(x) / f'(x)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 184.
#
#  Input:
#
#    real X: the point that starts the method.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root satisfying abs ( F(X) ) < ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0

  fx = f ( x, 0 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    dfx = f ( x, 1 )

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    ux = f ( x, 0 ) / dfx

    fx1 = f ( x - ux, 0 )

    if ( 2.0 * fx1 - fx == 0.0 ):
      ierror = 4
      return x, ierror, k
#
#  Set the increment.
#
    dx = - ux * ( fx1 - fx ) / ( 2.0 * fx1 - fx )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )

  return x, ierror, k

def tt1f ( x, a, rho, abserr, kmax, f ):

#*****************************************************************************80
#
## tt1f() implements the Traub type 1 functions 10 and 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 237.
#
#  Input:
#
#    real X: an estimate for the root.
#
#    real A, ???
#
#    real RHO, ???
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0

  if ( rho == 0.0 ):
    ierror = 3
    return x, ierror, k

  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    z = x + rho * fx / dfx
    fxu = f ( z, 0 )

    z = x - fxu / ( rho * rho * dfx )
    fz = f ( z, 0 )
#
#  Set the increment.
#
    dx = - ( a * fz + fxu / rho / rho ) / dfx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, ierror, k

def tthip ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## tthip() implements the Traub third function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joseph Traub,
#    Iterative Methods for the Solution of Equations,
#    ISBN: 0828403120,
#    LC: QA297.T7.
#    Prentice Hall, 1964, page 235.
#
#  Input:
#
#    real X: an estimate for the root.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    real EM, an estimate of the multiplicity of the root.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, em, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, em, ierror, k
 
    if ( fx == 0.0 ):
      em = 1.0
    elif ( np.log ( np.abs ( fx / dfx ) ) == 0.0 ):
      em = 1.0
    else:
      em = np.log ( np.abs ( fx ) ) / np.log ( np.abs ( fx / dfx ) )

    em = max ( em, 1.0 )
#
#  Set the increment.
#
    dx = - em * fx / dfx
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, em, ierror, k

def vandevel_improved ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## vandevel_improved() implements the improved Van de Vel iteration.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard King,
#    Improving the van de Vel root-finding method,
#    Computing,
#    Volume 30, 1983, pages 373 - 378.
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which
#    abs ( F(X) ) <= ABSERR.
#
#    real EM, an estimate of the multiplicity of the root.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  em1 = 1.0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )

  if ( dfx == 0.0 ):
    ierror = 3
    return

  u1 = fx / dfx

  x = x - fx / dfx
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, em, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, em, ierror, k

    u = fx / dfx

    if ( u1 - u != 0.0 ):
      em = em1 * u1 / ( u1 - u )
    else:
      em = em1

    em = max ( em, 1.0 )
#
#  Set the increment.
#
    dx = - em * fx / dfx
#
#  Remember current data for next step.
#
    em1 = em
    u1 = u
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, em, ierror, k

def vandevel ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## vandevel() implements the Van de Vel iteration.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hugo vandeVel,
#    A method for computing a root of a single nonlinear equation,
#    including its multiplicity,
#    Computing,
#    Volume 14, 1975, pages 167 - 171.
#
#  Input:
#
#    real X: an estimate for the root.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    real EM, an estimate of the multiplicity of the root.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  em1 = 1.0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, em, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, em, ierror, k

    u = fx / dfx
    z = x - em1 * fx / dfx
    fz = f ( z, 0 )
    dfz = f ( z, 1 )

    if ( dfz == 0.0 ):
      ierror = 3
      return x, em, ierror, k

    u1 = fz / dfz

    if ( u - u1 != 0.0 ):
      em = em1 * u / ( u - u1 )
    else:
      em = em1

    em = max ( em, 1.0 )
#
#  Set the increment.
#
    dx = - em1 * fx / dfx - em * fz / dfz
#
#  Remember current data for next step.
#
    em1 = em
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )

  return x, em, ierror, k

def whittaker2 ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## whittaker2() implements the double convex acceleeration of Whittaker's method.
#
#  Discussion:
#
#    x(n+1) = x(n) - (1/4) * ( f(x(n)) / f'(x(n)) ) *
#      ( 2 - L(x(n)) + ( 2 + L(x(n)) ) / ( 1 - L(x(n)) + 0.5 * L(x(n))**2 ) )
#
#    where
#
#      L(x) = f(x) * f''(x) / f'(x)**2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
  d2fx = f ( x, 2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = d2fx * fx / dfx / dfx

    if ( 1.0 - u + 0.5 * u * u == 0.0 ):
      ierror = 4
      return x, ierror, k
#
#  Set the increment.
#
    dx = - 0.25 * ( fx / dfx ) \
      * ( 2.0 - u + ( 2.0 + u ) / ( 1.0 - u + 0.5 * u * u ) )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )

  return x, ierror, k

def whittaker ( x, abserr, kmax, f ):

#*****************************************************************************80
#
## whittaker() implements the convex acceleeration of Whittaker's method.
#
#  Discussion:
#
#    x(n+1) = x(n) - ( f(x(n)) / f'(x(n)) ) * ( 1 - 0.5 * L(x(n)) )
#
#    where
#
#      L(x) = f(x) * f''(x) / f'(x)**2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X: an estimate for the root of the equation.
#
#    real ABSERR, an error tolerance.
#
#    integer KMAX, the maximum number of iterations allowed.
#
#    real external F, the name of the routine that
#    evaluates the function or its derivatives, of the form
#      function f ( x, ider )
#
#  Output:
#
#    real X: an approximate root for which abs ( F(X) ) <= ABSERR.
#
#    integer IERROR, error indicator.
#    0, no error occurred.
#    nonzero, an error occurred, and the iteration was halted.
#
#    integer K, the number of steps taken.
#
  import numpy as np
#
#  Initialization.
#
  ierror = 0
  k = 0
  fx = f ( x, 0 )
  dfx = f ( x, 1 )
  d2fx = f ( x, 2 )
#
#  Iteration
#
  while ( True ):
#
#  If the error tolerance is satisfied, then exit.
#
    if ( np.abs ( fx ) <= abserr ):
      break

    k = k + 1

    if ( kmax < k ):
      ierror = 2
      return x, ierror, k

    if ( dfx == 0.0 ):
      ierror = 3
      return x, ierror, k

    u = d2fx * fx / dfx /dfx
#
#  Set the increment.
#
    dx = - ( fx / dfx ) * ( 1.0 - 0.5 * u )
#
#  Update the iterate and function values.
#
    x = x + dx
    fx = f ( x, 0 )
    dfx = f ( x, 1 )
    d2fx = f ( x, 2 )

  return x, ierror, k

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
  zoomin_test ( )
  timestamp ( )

