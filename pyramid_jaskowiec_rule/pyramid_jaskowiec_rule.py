#! /usr/bin/env python3
#
def pyramid_jaskowiec_rule_test ( ):

#*****************************************************************************80
#
## pyramid_jaskowiec_rule_test() tests pyramid_jaskowiec_rule().
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    12 July 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'pyramid_jaskowiec_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test pyramid_jaskowiec_rule().' )

  p = 5
  pyramid_jaskowiec_rule_test01 ( p )

  p = 5
  pyramid_jaskowiec_rule_test02 ( p )

  p_lo = 0
  p_hi = 20
  pyramid_jaskowiec_rule_test03 ( p_lo, p_hi )
#
#  Terminate.
#
  print ( '' )
  print ( 'pyramid_jaskowiec_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def pyramid_jaskowiec_rule_test01 ( p ):

#*****************************************************************************80
#
## pyramid_jaskowiec_rule_test01() computes a quadrature rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    25 May 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'pyramid_jaskowiec_rule_test01():' )
  print ( '  Quadrature rule for the unit pyramid,' )
  print ( '  Precision p = ', p )
#
#  Retrieve the rule.
#
  n, x, y, z, w = pyramid_jaskowiec_rule ( p )
#
#  Print the rule.
#
  print ( '' )
  print ( '     I      W          X           Y           Z' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %10.6f  %10.6f  %10.6f  %10.6f' \
      % ( i, w[i], x[i], y[i], z[i] ) )
#
#  Verify that weights sum to 1.
#
  w_sum = np.sum ( w )

  print ( '' )
  print ( '  Weight Sum   ', w_sum )

  return

def pyramid_jaskowiec_rule_test02 ( p ):

#*****************************************************************************80
#
## pyramid_jaskowiec_rule_test02() tests a quadrature rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    12 July 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'pyramid_jaskowiec_rule_test02():' )
  print ( '  Test the precision of a quadrature rule for the unit pyramid.' )

  dim_num = 3
#
#  Retrieve the rule.
#
  n, x, y, z, w = pyramid_jaskowiec_rule ( p )
#
#  Pack the x, y, z vectors as rows of an array.
#
  xyz = np.transpose ( np.array ( [ x, y, z ] ) )

  print ( '' )
  print ( '  Stated precision of rule    = ', p )
  print ( '  Number of quadrature points = ', n )
  print ( '' )
  print ( '  Degree  Maximum error' )
  print ( '' )

  for degree in range ( 0, p + 3 ):

    expon = np.zeros ( dim_num, dtype = int )
    more = False
    h = 0
    t = 0
    max_error = 0.0

    while ( True ):

      expon, more, h, t = comp_next ( degree, dim_num, expon, more, h, t )

      v = monomial_value ( expon, xyz )

      quad = pyramid_unit_volume ( ) * np.dot ( w, v )

      exact = pyramid_unit_monomial_integral ( expon )

      quad_error = np.abs ( quad - exact )

      max_error = max ( max_error, quad_error )

      if ( not more ):
        break

    print ( '  %2d  %24.16g' % ( degree, max_error ) )

  return

def pyramid_jaskowiec_rule_test03 ( p_lo, p_hi ):

#*****************************************************************************80
#
## pyramid_jaskowiec_rule_test03() tests absolute and relative precision.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    12 July 2023
#
#  Author:
#
#    John Burkardt.
#
#    integer p_lo, p_hi: the lowest and highest rules to check.
# 
  import numpy as np

  print ( '' )
  print ( 'pyramid_jaskowiec_rule_test03():' )
  print ( '  Test the precision of quadrature rules for the unit pyramid.' )
  print ( '  Check rules of precision p =', p_lo, 'through', p_hi )
  print ( '  for error in approximating integrals of monomials.' )

  dim_num = 3

  print ( '' )
  print ( '              maximum                   maximum' )
  print ( '   p          absolute                  relative' )
  print ( '              error                     error' )
  print ( '' )

  for p in range ( p_lo, p_hi + 1 ):

    n, x, y, z, w = pyramid_jaskowiec_rule ( p )
#
#  Pack the x, y, z vectors as rows of an array.
#
    xyz = np.transpose ( np.array ( [ x, y, z ] ) )

    max_abs = 0.0
    max_rel = 0.0

    for degree in range ( 0, p + 1 ):

      expon = np.zeros ( dim_num, dtype = int )
      more = False
      h = 0
      t = 0

      while ( True ):

        expon, more, h, t = comp_next ( degree, dim_num, expon, more, h, t )

        v = monomial_value ( expon, xyz )

        quad = pyramid_unit_volume ( ) * np.dot ( w, v )

        exact = pyramid_unit_monomial_integral ( expon )

        quad_error = np.abs ( quad - exact )

        max_abs = max ( max_abs, quad_error )

        if ( exact != 0.0 ):
          max_rel = max ( max_rel, quad_error / abs ( exact ) )

        if ( not more ):
          break

    print ( '  %2d  %24.16g  %24.16g' % ( p, max_abs, max_rel ) )

  return

def comp_next ( n, k, a, more, h, t ):

#*****************************************************************************80
#
## comp_next() computes the compositions of the integer N into K parts.
#
#  Discussion:
#
#    A composition of the integer N into K parts is an ordered sequence
#    of K nonnegative integers which sum to N.  The compositions (1,2,1)
#    and (1,1,2) are considered to be distinct.
#
#    The routine computes one composition on each call until there are no more.
#    For instance, one composition of 6 into 3 parts is
#    3+2+1, another would be 6+0+0.
#
#    On the first call to this routine, set MORE = FALSE.  The routine
#    will compute the first element in the sequence of compositions, and
#    return it, as well as setting MORE = TRUE.  If more compositions
#    are desired, call again, and again.  Each time, the routine will
#    return with a new composition.
#
#    However, when the LAST composition in the sequence is computed 
#    and returned, the routine will reset MORE to FALSE, signaling that
#    the end of the sequence has been reached.
#
#    This routine originally used a SAVE statement to maintain the
#    variables H and T.  I have decided that it is safer
#    to pass these variables as arguments, even though the user should
#    never alter them.  This allows this routine to safely shuffle
#    between several ongoing calculations.
#
#    There are 28 compositions of 6 into three parts.  This routine will
#    produce those compositions in the following order:
#
#     I         A
#     -     ---------
#     1     6   0   0
#     2     5   1   0
#     3     4   2   0
#     4     3   3   0
#     5     2   4   0
#     6     1   5   0
#     7     0   6   0
#     8     5   0   1
#     9     4   1   1
#    10     3   2   1
#    11     2   3   1
#    12     1   4   1
#    13     0   5   1
#    14     4   0   2
#    15     3   1   2
#    16     2   2   2
#    17     1   3   2
#    18     0   4   2
#    19     3   0   3
#    20     2   1   3
#    21     1   2   3
#    22     0   3   3
#    23     2   0   4
#    24     1   1   4
#    25     0   2   4
#    26     1   0   5
#    27     0   1   5
#    28     0   0   6
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 May 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms for Computers and Calculators,
#    Second Edition,
#    Academic Press, 1978,
#    ISBN: 0-12-519260-6,
#    LC: QA164.N54.
#
#  Input:
#
#    integer N, the integer whose compositions are desired.
#
#    integer K, the number of parts in the composition.
#
#    integer A(K), the previous composition.  On the first call,
#    with MORE = FALSE, set A = [].  Thereafter, A should be the 
#    value of A output from the previous call.
#
#    bool MORE.  The input value of MORE on the first
#    call should be FALSE, which tells the program to initialize.
#    On subsequent calls, MORE should be TRUE, or simply the
#    output value of MORE from the previous call.
#
#    integer H, T, two internal parameters needed for the
#    computation.  The user may need to initialize these before the
#    very first call, but these initial values are not important.
#    The user should not alter these parameters once the computation
#    begins.
#
#  Output:
#
#    integer A(K), the next composition.
#
#    bool MORE, will be TRUE unless the composition 
#    that is being returned is the final one in the sequence.
#
#    integer H, T, the updated values of the two internal 
#    variables.
#
  if ( k == 0 ):
    a = []
    more = False
    t = n
    h = 0
    return a, more, h, t

  if ( not more ):

    t = n
    h = 0
    a[0] = n
    for i in range ( 1, k ):
      a[i] = 0

  else:
      
    if ( 1 < t ):
      h = 0

    t = a[h]
    a[h] = 0
    a[0] = t - 1
    a[h+1] = a[h+1] + 1
    h = h + 1

  more = ( a[k-1] != n )

  return a, more, h, t

def monomial_value ( e, x ):

#*****************************************************************************80
#
## monomial_value() evaluates a monomial.
#
#  Discussion:
#
#    This routine evaluates a monomial of the form
#
#      product ( 1 <= i <= m ) x(i)^e(i)
#
#    The combination 0.0^0, if encountered, is treated as 1.0.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer E(D): the exponents.
#
#    real X(N,D): the point coordinates.
#
#  Output:
#
#    real V(N): the monomial values.
#
  import numpy as np

  n, d = x.shape

  v = np.ones ( n )

  for j in range ( 0, d ):
    if ( 0 != e[j] ):
      v[0:n] = v[0:n] * x[0:n,j] ** e[j]

  return v

def pyramid_jaskowiec_rule ( p ):

#*****************************************************************************80
#
## pyramid_jaskowiec_rule() returns a pyramid quadrature rule of given precision.
#
#  Discussion:
#
#    The unit pyramid with square base is the region
#
#      -1 <= X <= 1
#      -1 <= Y <= 1
#       0 <= Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal of Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Input:
#
#    integer p: the precision, 0 <= p <= 20.
#
#  Output:
#
#    integer n: the order of the rule.
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  if ( p < 0 ):
    raise Exception ( 'pyramid_jaskowiec_rule(): Input p < 0.' )
 
  if ( 20 < p ):
    raise Exception ( 'pyramid_jaskowiec_rule(): Input 20 < p.' )

  n = rule_order ( p )

  if ( p == 0 ):
    x, y, z, w = rule00 ( )
  elif ( p == 1 ):
    x, y, z, w = rule01 ( )
  elif ( p == 2 ):
    x, y, z, w = rule02 ( )
  elif ( p == 3 ):
    x, y, z, w = rule03 ( )
  elif ( p == 4 ):
    x, y, z, w = rule04 ( )
  elif ( p == 5 ):
    x, y, z, w = rule05 ( )
  elif ( p == 6 ):
    x, y, z, w = rule06 ( )
  elif ( p == 7 ):
    x, y, z, w = rule07 ( )
  elif ( p == 8 ):
    x, y, z, w = rule08 ( )
  elif ( p == 9 ):
    x, y, z, w = rule09 ( )
  elif ( p == 10 ):
    x, y, z, w = rule10 ( )
  elif ( p == 11 ):
    x, y, z, w = rule11 ( )
  elif ( p == 12 ):
    x, y, z, w = rule12 ( )
  elif ( p == 13 ):
    x, y, z, w = rule13 ( )
  elif ( p == 14 ):
    x, y, z, w = rule14 ( )
  elif ( p == 15 ):
    x, y, z, w = rule15 ( )
  elif ( p == 16 ):
    x, y, z, w = rule16 ( )
  elif ( p == 17 ):
    x, y, z, w = rule17 ( )
  elif ( p == 18 ):
    x, y, z, w = rule18 ( )
  elif ( p == 19 ):
    x, y, z, w = rule19 ( )
  elif ( p == 20 ):
    x, y, z, w = rule20 ( )

  return n, x, y, z, w

def pyramid_unit_monomial_integral ( expon ):

#*****************************************************************************80
#
## pyramid_unit_monomial_integral(): monomial integral in a unit pyramid.
#
#  Discussion:
#
#    This routine returns the integral of
#
#      product ( 1 <= I <= 3 ) X(I)^EXPON(I)
#
#    over the unit pyramid.
#
#    The unit pyramid is defined as:
#
#    - ( 1 - Z ) <= X <= 1 - Z
#    - ( 1 - Z ) <= Y <= 1 - Z
#              0 <= Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Arthur Stroud,
#    Approximate Calculation of Multiple Integrals,
#    Prentice Hall, 1971,
#    ISBN: 0130438936,
#    LC: QA311.S85.
#
#  Input:
#
#    integer EXPON(3): the exponents.
#
#  Output:
#
#    real VALUE: the integral of the monomial.
#
  from scipy.special import comb

  if ( ( ( expon[0] % 2 ) == 0 ) and ( ( expon[1] % 2 ) == 0 ) ):

    i_hi = 2 + expon[0] + expon[1]

    value = 0.0
    mop = 1.0
    for i in range ( 0, i_hi + 1 ):
      value = value + mop * comb ( i_hi, i ) / float ( i + expon[2] + 1 )
      mop = - mop

    value = value * 2.0 / float ( expon[0] + 1 ) * 2.0 / float ( expon[1] + 1 )

  else:

    value = 0.0

  return value

def pyramid_unit_volume ( ):

#*****************************************************************************80
#
## pyramid_unit_volume() returns the volume of a unit pyramid.
#
#  Discussion:
#
#    A pyramid with square base can be regarded as the upper half of a
#    3D octahedron.
#
#    The integration region:
#
#      - ( 1 - Z ) <= X <= 1 - Z
#      - ( 1 - Z ) <= Y <= 1 - Z
#                0 <= Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 March 2008
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the volume of the pyramid.
#
  value = 4.0 / 3.0

  return value

def pyramid_volume ( r, h ):

#*****************************************************************************80
#
## pyramid_volume() returns the volume of a pyramid with square base in 3D.
#
#  Discussion:
#
#    A pyramid with square base can be regarded as the upper half of a
#    3D octahedron.
#
#    Z - R <= X <= R - Z
#    Z - R <= Y <= R - Z
#    0 <= Z <= H.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the "radius" of the pyramid, that is, half the
#    length of one of the sides of the square base.
#
#    real H, the height of the pyramid.
#
#  Output:
#
#    real VALUE, the volume of the pyramid.
#
  value = ( 4.0 / 3.0 ) * h * r * r

  return value

def pyramid_volume_test ( ):

#*****************************************************************************80
#
## pyramid_volume_test() tests pyramid_volume().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2023
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng

  rng = default_rng ( )

  print ( '' )
  print ( 'pyramid_volume_test():' )
  print ( '  pyramid_volume() returns the volume of a pyramid.' )
  print ( '' )
  print ( '     Radius     Height     Volume' )
  print ( '' )

  for i in range ( 0, 5 ):
    r = 1.0 + 9.0 * rng.random ( )
    h = 1.0 + 9.0 * rng.random ( )
    volume = pyramid_volume ( r, h )
    print ( '  %8.4f  %8.4f  %8.4f' % ( r, h, volume ) )

  return

def rule_order ( p ):

#*****************************************************************************80
#
## rule_order() returns the order of a pyramid quadrature rule of given precision.
#
#  Discussion:
#
#    The "order" of a quadrature rule is the number of points involved.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Input:
#
#    integer p: the precision, 0 <= p <= 20.
#
#  Output:
#
#    integer order: the order of the rule.
#
  if ( p < 0 ):
    raise Exception ( 'rule_order(): Input p < 0.' )

  if ( 20 < p ):
    raise Exception ( 'rule_order(): Input 20 < p.' )

  order_vec = [ \
      1, \
      1,   5,   6,  10,  15, \
     23,  31,  47,  62,  80, \
    103, 127, 152, 184, 234, \
    285, 319, 357, 418, 489 ]

  order = order_vec[p]

  return order

def rule00 ( ):

#*****************************************************************************80
#
## rule00() returns the pyramid quadrature rule of precision 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000 ] )

  y = np.array ( [ \
      0.00000000000000000000 ] )

  z = np.array ( [ \
      0.25000000000000000000 ] )

  w= np.array ( [ \
      1.00000000000000000000 ] )

  return x, y, z, w

def rule01 ( ):

#*****************************************************************************80
#
## rule01() returns the pyramid quadrature rule of precision 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000 ] )

  y = np.array ( [ \
      0.00000000000000000000 ] )

  z = np.array ( [ \
      0.25000000000000000000 ] )

  w= np.array ( [ \
      1.00000000000000000000 ] )

  return x, y, z, w

def rule02 ( ):

#*****************************************************************************80
#
## rule02() returns the pyramid quadrature rule of precision 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.52699748736717488828, \
     -0.52699748736717488828, \
      0.52699748736717488828, \
     -0.52699748736717488828 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.52699748736717488828, \
      0.52699748736717488828, \
     -0.52699748736717488828, \
     -0.52699748736717488828 ] )

  z = np.array ( [ \
      0.56063221253561712487, \
      0.12927845700902559911, \
      0.12927845700902559911, \
      0.12927845700902559911, \
      0.12927845700902559911 ] )

  w= np.array ( [ \
      0.27986667890163369199, \
      0.18003333027459159088, \
      0.18003333027459159088, \
      0.18003333027459159088, \
      0.18003333027459159088 ] )

  return x, y, z, w

def rule03 ( ):

#*****************************************************************************80
#
## rule03() returns the pyramid quadrature rule of precision 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.58459636639471157515, \
     -0.58459636639471157515, \
      0.58459636639471157515, \
     -0.58459636639471157515 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.58459636639471157515, \
      0.58459636639471157515, \
     -0.58459636639471157515, \
     -0.58459636639471157515 ] )

  z = np.array ( [ \
      0.03032132711145601317, \
      0.56560718797897435728, \
      0.16666666666666665741, \
      0.16666666666666665741, \
      0.16666666666666665741, \
      0.16666666666666665741 ] )

  w= np.array ( [ \
      0.15345064748545933497, \
      0.26133122207480513621, \
      0.14630453260993386833, \
      0.14630453260993386833, \
      0.14630453260993386833, \
      0.14630453260993386833 ] )

  return x, y, z, w

def rule04 ( ):

#*****************************************************************************80
#
## rule04() returns the pyramid quadrature rule of precision 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.65058155639823256333, \
      0.00000000000000000000, \
     -0.65058155639823256333, \
      0.00000000000000000000, \
      0.65796699712169004481, \
     -0.65796699712169004481, \
      0.65796699712169004481, \
     -0.65796699712169004481 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.65058155639823256333, \
      0.00000000000000000000, \
     -0.65058155639823256333, \
      0.65796699712169004481, \
      0.65796699712169004481, \
     -0.65796699712169004481, \
     -0.65796699712169004481 ] )

  z = np.array ( [ \
      0.12513695310874645150, \
      0.67723278888613736015, \
      0.32238414957821365237, \
      0.32238414957821365237, \
      0.32238414957821365237, \
      0.32238414957821365237, \
      0.03924828389881535040, \
      0.03924828389881535040, \
      0.03924828389881535040, \
      0.03924828389881535040 ] )

  w= np.array ( [ \
      0.20688340258955226214, \
      0.11374188317064193310, \
      0.10632458788932550031, \
      0.10632458788932550031, \
      0.10632458788932550031, \
      0.10632458788932550031, \
      0.06351909067062594394, \
      0.06351909067062594394, \
      0.06351909067062594394, \
      0.06351909067062594394 ] )

  return x, y, z, w

def rule05 ( ):

#*****************************************************************************80
#
## rule05() returns the pyramid quadrature rule of precision 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.75344061307932941318, \
      0.00000000000000000000, \
     -0.75344061307932941318, \
      0.00000000000000000000, \
      0.41715200242575134482, \
     -0.41715200242575134482, \
      0.41715200242575134482, \
     -0.41715200242575134482, \
      0.67402251647787037037, \
     -0.67402251647787037037, \
      0.67402251647787037037, \
     -0.67402251647787037037 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.75344061307932941318, \
      0.00000000000000000000, \
     -0.75344061307932941318, \
      0.41715200242575134482, \
      0.41715200242575134482, \
     -0.41715200242575134482, \
     -0.41715200242575134482, \
      0.67402251647787037037, \
      0.67402251647787037037, \
     -0.67402251647787037037, \
     -0.67402251647787037037 ] )

  z = np.array ( [ \
      0.73070946955479043616, \
      0.00619723285819058847, \
      0.26844580953431373960, \
      0.12500000000000000000, \
      0.12500000000000000000, \
      0.12500000000000000000, \
      0.12500000000000000000, \
      0.42182171100285947851, \
      0.42182171100285947851, \
      0.42182171100285947851, \
      0.42182171100285947851, \
      0.06579572180745926757, \
      0.06579572180745926757, \
      0.06579572180745926757, \
      0.06579572180745926757 ] )

  w= np.array ( [ \
      0.06773442693037112772, \
      0.06470893518150579171, \
      0.17727154901514516339, \
      0.05910777216655192096, \
      0.05910777216655192096, \
      0.05910777216655192096, \
      0.05910777216655192096, \
      0.06537546219121122271, \
      0.06537546219121122271, \
      0.06537546219121122271, \
      0.06537546219121122271, \
      0.04808803786048133910, \
      0.04808803786048133910, \
      0.04808803786048133910, \
      0.04808803786048133910 ] )

  return x, y, z, w

def rule06 ( ):

#*****************************************************************************80
#
## rule06() returns the pyramid quadrature rule of precision 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.42104595182782333929, \
      0.00000000000000000000, \
     -0.42104595182782333929, \
      0.00000000000000000000, \
      0.83584092506524387822, \
      0.00000000000000000000, \
     -0.83584092506524387822, \
      0.00000000000000000000, \
      0.51341781341302172859, \
     -0.51341781341302172859, \
      0.51341781341302172859, \
     -0.51341781341302172859, \
      0.87197953364266822529, \
     -0.87197953364266822529, \
      0.87197953364266822529, \
     -0.87197953364266822529, \
      0.47733155776773072976, \
     -0.47733155776773072976, \
      0.47733155776773072976, \
     -0.47733155776773072976 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.42104595182782333929, \
      0.00000000000000000000, \
     -0.42104595182782333929, \
      0.00000000000000000000, \
      0.83584092506524387822, \
      0.00000000000000000000, \
     -0.83584092506524387822, \
      0.51341781341302172859, \
      0.51341781341302172859, \
     -0.51341781341302172859, \
     -0.51341781341302172859, \
      0.87197953364266822529, \
      0.87197953364266822529, \
     -0.87197953364266822529, \
     -0.87197953364266822529, \
      0.47733155776773072976, \
      0.47733155776773072976, \
     -0.47733155776773072976, \
     -0.47733155776773072976 ] )

  z = np.array ( [ \
      0.13353121706321477435, \
      0.80839181878746035892, \
      0.37840352066355309457, \
      0.55635774022808082151, \
      0.55635774022808082151, \
      0.55635774022808082151, \
      0.55635774022808082151, \
      0.09682668434012106640, \
      0.09682668434012106640, \
      0.09682668434012106640, \
      0.09682668434012106640, \
      0.25547807503740499468, \
      0.25547807503740499468, \
      0.25547807503740499468, \
      0.25547807503740499468, \
      0.03348911098405843445, \
      0.03348911098405843445, \
      0.03348911098405843445, \
      0.03348911098405843445, \
      0.02776222122928558023, \
      0.02776222122928558023, \
      0.02776222122928558023, \
      0.02776222122928558023 ] )

  w= np.array ( [ \
      0.10236994192337051102, \
      0.02544552509057920395, \
      0.10744358342269332007, \
      0.03715744178992643615, \
      0.03715744178992643615, \
      0.03715744178992643615, \
      0.03715744178992643615, \
      0.03663269740345383857, \
      0.03663269740345383857, \
      0.03663269740345383857, \
      0.03663269740345383857, \
      0.07134885171305939411, \
      0.07134885171305939411, \
      0.07134885171305939411, \
      0.07134885171305939411, \
      0.00865946139444006419, \
      0.00865946139444006419, \
      0.00865946139444006419, \
      0.00865946139444006419, \
      0.03738678508995950389, \
      0.03738678508995950389, \
      0.03738678508995950389, \
      0.03738678508995950389 ] )

  return x, y, z, w

def rule07 ( ):

#*****************************************************************************80
#
## rule07() returns the pyramid quadrature rule of precision 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.61721339984836764980, \
      0.00000000000000000000, \
     -0.61721339984836764980, \
      0.00000000000000000000, \
      0.86409875978771466531, \
      0.00000000000000000000, \
     -0.86409875978771466531, \
      0.00000000000000000000, \
      0.52488756030374572603, \
     -0.52488756030374572603, \
      0.52488756030374572603, \
     -0.52488756030374572603, \
      0.25419682219463812789, \
     -0.25419682219463812789, \
      0.25419682219463812789, \
     -0.25419682219463812789, \
      0.35405111881016937403, \
     -0.35405111881016937403, \
      0.35405111881016937403, \
     -0.35405111881016937403, \
      0.61427194545119712110, \
     -0.61427194545119712110, \
      0.61427194545119712110, \
     -0.61427194545119712110, \
      0.80282248626994900942, \
     -0.80282248626994900942, \
      0.80282248626994900942, \
     -0.80282248626994900942 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.61721339984836764980, \
      0.00000000000000000000, \
     -0.61721339984836764980, \
      0.00000000000000000000, \
      0.86409875978771466531, \
      0.00000000000000000000, \
     -0.86409875978771466531, \
      0.52488756030374572603, \
      0.52488756030374572603, \
     -0.52488756030374572603, \
     -0.52488756030374572603, \
      0.25419682219463812789, \
      0.25419682219463812789, \
     -0.25419682219463812789, \
     -0.25419682219463812789, \
      0.35405111881016937403, \
      0.35405111881016937403, \
     -0.35405111881016937403, \
     -0.35405111881016937403, \
      0.61427194545119712110, \
      0.61427194545119712110, \
     -0.61427194545119712110, \
     -0.61427194545119712110, \
      0.80282248626994900942, \
      0.80282248626994900942, \
     -0.80282248626994900942, \
     -0.80282248626994900942 ] )

  z = np.array ( [ \
      0.39365048525928414413, \
      0.83863414272299030561, \
      0.00001985131073852604, \
      0.33333333333333331483, \
      0.33333333333333331483, \
      0.33333333333333331483, \
      0.33333333333333331483, \
      0.06666666666666666574, \
      0.06666666666666666574, \
      0.06666666666666666574, \
      0.06666666666666666574, \
      0.29045491084254104752, \
      0.29045491084254104752, \
      0.29045491084254104752, \
      0.29045491084254104752, \
      0.60547835568141594731, \
      0.60547835568141594731, \
      0.60547835568141594731, \
      0.60547835568141594731, \
      0.12931884631055998169, \
      0.12931884631055998169, \
      0.12931884631055998169, \
      0.12931884631055998169, \
      0.00010086339268113571, \
      0.00010086339268113571, \
      0.00010086339268113571, \
      0.00010086339268113571, \
      0.08012951317750569014, \
      0.08012951317750569014, \
      0.08012951317750569014, \
      0.08012951317750569014 ] )

  w= np.array ( [ \
      0.10051398177493840735, \
      0.01571901760701541889, \
      0.02499658963028165634, \
      0.02871093749999999861, \
      0.02871093749999999861, \
      0.02871093749999999861, \
      0.02871093749999999861, \
      0.02669175929300291600, \
      0.02669175929300291600, \
      0.02669175929300291600, \
      0.02669175929300291600, \
      0.03572750182264943647, \
      0.03572750182264943647, \
      0.03572750182264943647, \
      0.03572750182264943647, \
      0.02951904528668866309, \
      0.02951904528668866309, \
      0.02951904528668866309, \
      0.02951904528668866309, \
      0.06594160872648228977, \
      0.06594160872648228977, \
      0.06594160872648228977, \
      0.06594160872648228977, \
      0.01333274388639105884, \
      0.01333274388639105884, \
      0.01333274388639105884, \
      0.01333274388639105884, \
      0.01476900623172677438, \
      0.01476900623172677438, \
      0.01476900623172677438, \
      0.01476900623172677438 ] )

  return x, y, z, w

def rule08 ( ):

#*****************************************************************************80
#
## rule08() returns the pyramid quadrature rule of precision 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.25367856157821822016, \
      0.00000000000000000000, \
     -0.25367856157821822016, \
      0.00000000000000000000, \
      0.71027375776907275551, \
      0.00000000000000000000, \
     -0.71027375776907275551, \
      0.00000000000000000000, \
      0.63643362359838895337, \
      0.00000000000000000000, \
     -0.63643362359838895337, \
      0.00000000000000000000, \
      0.62337928196226433109, \
      0.00000000000000000000, \
     -0.62337928196226433109, \
      0.00000000000000000000, \
      0.51225968171005897833, \
     -0.51225968171005897833, \
      0.51225968171005897833, \
     -0.51225968171005897833, \
      0.37965901379429650708, \
     -0.37965901379429650708, \
      0.37965901379429650708, \
     -0.37965901379429650708, \
      0.69140086940529510429, \
     -0.69140086940529510429, \
      0.69140086940529510429, \
     -0.69140086940529510429, \
      0.86742190798549856368, \
     -0.86742190798549856368, \
      0.86742190798549856368, \
     -0.86742190798549856368, \
      0.31712322629106232119, \
     -0.31712322629106232119, \
      0.31712322629106232119, \
     -0.31712322629106232119, \
      0.89374797161835639603, \
      0.40528326346564669258, \
     -0.89374797161835639603, \
      0.40528326346564669258, \
      0.89374797161835639603, \
     -0.40528326346564669258, \
     -0.89374797161835639603, \
     -0.40528326346564669258 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.25367856157821822016, \
      0.00000000000000000000, \
     -0.25367856157821822016, \
      0.00000000000000000000, \
      0.71027375776907275551, \
      0.00000000000000000000, \
     -0.71027375776907275551, \
      0.00000000000000000000, \
      0.63643362359838895337, \
      0.00000000000000000000, \
     -0.63643362359838895337, \
      0.00000000000000000000, \
      0.62337928196226433109, \
      0.00000000000000000000, \
     -0.62337928196226433109, \
      0.51225968171005897833, \
      0.51225968171005897833, \
     -0.51225968171005897833, \
     -0.51225968171005897833, \
      0.37965901379429650708, \
      0.37965901379429650708, \
     -0.37965901379429650708, \
     -0.37965901379429650708, \
      0.69140086940529510429, \
      0.69140086940529510429, \
     -0.69140086940529510429, \
     -0.69140086940529510429, \
      0.86742190798549856368, \
      0.86742190798549856368, \
     -0.86742190798549856368, \
     -0.86742190798549856368, \
      0.31712322629106232119, \
      0.31712322629106232119, \
     -0.31712322629106232119, \
     -0.31712322629106232119, \
      0.40528326346564669258, \
      0.89374797161835639603, \
      0.40528326346564669258, \
     -0.89374797161835639603, \
     -0.40528326346564669258, \
      0.89374797161835639603, \
     -0.40528326346564669258, \
     -0.89374797161835639603 ] )

  z = np.array ( [ \
      0.07395194949759914538, \
      0.48064180778578036168, \
      0.89787700126494018882, \
      0.70399494392200201442, \
      0.70399494392200201442, \
      0.70399494392200201442, \
      0.70399494392200201442, \
      0.15999762291015326432, \
      0.15999762291015326432, \
      0.15999762291015326432, \
      0.15999762291015326432, \
      0.34740846408160180880, \
      0.34740846408160180880, \
      0.34740846408160180880, \
      0.34740846408160180880, \
      0.01127682420195143774, \
      0.01127682420195143774, \
      0.01127682420195143774, \
      0.01127682420195143774, \
      0.06351022006373874262, \
      0.06351022006373874262, \
      0.06351022006373874262, \
      0.06351022006373874262, \
      0.46284226887006968409, \
      0.46284226887006968409, \
      0.46284226887006968409, \
      0.46284226887006968409, \
      0.19177130509938980496, \
      0.19177130509938980496, \
      0.19177130509938980496, \
      0.19177130509938980496, \
      0.01630913438364359896, \
      0.01630913438364359896, \
      0.01630913438364359896, \
      0.01630913438364359896, \
      0.23681987030130632887, \
      0.23681987030130632887, \
      0.23681987030130632887, \
      0.23681987030130632887, \
      0.05005997974535449785, \
      0.05005997974535449785, \
      0.05005997974535449785, \
      0.05005997974535449785, \
      0.05005997974535449785, \
      0.05005997974535449785, \
      0.05005997974535449785, \
      0.05005997974535449785 ] )

  w= np.array ( [ \
      0.05595524252285600381, \
      0.06694668391641565852, \
      0.00475252306983395441, \
      0.01488586682102476834, \
      0.01488586682102476834, \
      0.01488586682102476834, \
      0.01488586682102476834, \
      0.02455698624881830563, \
      0.02455698624881830563, \
      0.02455698624881830563, \
      0.02455698624881830563, \
      0.01608138988371909592, \
      0.01608138988371909592, \
      0.01608138988371909592, \
      0.01608138988371909592, \
      0.01442915622061930955, \
      0.01442915622061930955, \
      0.01442915622061930955, \
      0.01442915622061930955, \
      0.02488836268558412140, \
      0.02488836268558412140, \
      0.02488836268558412140, \
      0.02488836268558412140, \
      0.03016542061786949003, \
      0.03016542061786949003, \
      0.03016542061786949003, \
      0.03016542061786949003, \
      0.01825943823062004326, \
      0.01825943823062004326, \
      0.01825943823062004326, \
      0.01825943823062004326, \
      0.00405270511408486935, \
      0.00405270511408486935, \
      0.00405270511408486935, \
      0.00405270511408486935, \
      0.05109969513593878160, \
      0.05109969513593878160, \
      0.05109969513593878160, \
      0.05109969513593878160, \
      0.00983368333222240688, \
      0.00983368333222240688, \
      0.00983368333222240688, \
      0.00983368333222240688, \
      0.00983368333222240688, \
      0.00983368333222240688, \
      0.00983368333222240688, \
      0.00983368333222240688 ] )

  return x, y, z, w

def rule09 ( ):

#*****************************************************************************80
#
## rule09() returns the pyramid quadrature rule of precision 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.21993584526338003093, \
      0.00000000000000000000, \
     -0.21993584526338003093, \
      0.00000000000000000000, \
      0.25580155737930071469, \
      0.00000000000000000000, \
     -0.25580155737930071469, \
      0.00000000000000000000, \
      0.87392422284165005575, \
      0.00000000000000000000, \
     -0.87392422284165005575, \
      0.00000000000000000000, \
      0.62069706482035569284, \
      0.00000000000000000000, \
     -0.62069706482035569284, \
      0.00000000000000000000, \
      0.48088720239801563405, \
      0.00000000000000000000, \
     -0.48088720239801563405, \
      0.00000000000000000000, \
      0.54766337559892563913, \
      0.00000000000000000000, \
     -0.54766337559892563913, \
      0.00000000000000000000, \
      0.31716782120661740629, \
     -0.31716782120661740629, \
      0.31716782120661740629, \
     -0.31716782120661740629, \
      0.58114214633277661015, \
     -0.58114214633277661015, \
      0.58114214633277661015, \
     -0.58114214633277661015, \
      0.52308134436113074006, \
     -0.52308134436113074006, \
      0.52308134436113074006, \
     -0.52308134436113074006, \
      0.87278863855859856180, \
     -0.87278863855859856180, \
      0.87278863855859856180, \
     -0.87278863855859856180, \
      0.27447830261314615230, \
     -0.27447830261314615230, \
      0.27447830261314615230, \
     -0.27447830261314615230, \
      0.45787401929460586070, \
      0.76874559686548982196, \
     -0.45787401929460586070, \
      0.76874559686548982196, \
      0.45787401929460586070, \
     -0.76874559686548982196, \
     -0.45787401929460586070, \
     -0.76874559686548982196, \
      0.52945920866195028687, \
      0.86516329503292388470, \
     -0.52945920866195028687, \
      0.86516329503292388470, \
      0.52945920866195028687, \
     -0.86516329503292388470, \
     -0.52945920866195028687, \
     -0.86516329503292388470 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.21993584526338003093, \
      0.00000000000000000000, \
     -0.21993584526338003093, \
      0.00000000000000000000, \
      0.25580155737930071469, \
      0.00000000000000000000, \
     -0.25580155737930071469, \
      0.00000000000000000000, \
      0.87392422284165005575, \
      0.00000000000000000000, \
     -0.87392422284165005575, \
      0.00000000000000000000, \
      0.62069706482035569284, \
      0.00000000000000000000, \
     -0.62069706482035569284, \
      0.00000000000000000000, \
      0.48088720239801563405, \
      0.00000000000000000000, \
     -0.48088720239801563405, \
      0.00000000000000000000, \
      0.54766337559892563913, \
      0.00000000000000000000, \
     -0.54766337559892563913, \
      0.31716782120661740629, \
      0.31716782120661740629, \
     -0.31716782120661740629, \
     -0.31716782120661740629, \
      0.58114214633277661015, \
      0.58114214633277661015, \
     -0.58114214633277661015, \
     -0.58114214633277661015, \
      0.52308134436113074006, \
      0.52308134436113074006, \
     -0.52308134436113074006, \
     -0.52308134436113074006, \
      0.87278863855859856180, \
      0.87278863855859856180, \
     -0.87278863855859856180, \
     -0.87278863855859856180, \
      0.27447830261314615230, \
      0.27447830261314615230, \
     -0.27447830261314615230, \
     -0.27447830261314615230, \
      0.76874559686548982196, \
      0.45787401929460586070, \
      0.76874559686548982196, \
     -0.45787401929460586070, \
     -0.76874559686548982196, \
      0.45787401929460586070, \
     -0.76874559686548982196, \
     -0.45787401929460586070, \
      0.86516329503292388470, \
      0.52945920866195028687, \
      0.86516329503292388470, \
     -0.52945920866195028687, \
     -0.86516329503292388470, \
      0.52945920866195028687, \
     -0.86516329503292388470, \
     -0.52945920866195028687 ] )

  z = np.array ( [ \
      0.90338060334285785746, \
      0.56496444359597119966, \
      0.74856124635194676298, \
      0.74856124635194676298, \
      0.74856124635194676298, \
      0.74856124635194676298, \
      0.13469976629555441283, \
      0.13469976629555441283, \
      0.13469976629555441283, \
      0.13469976629555441283, \
      0.05467616134251215843, \
      0.05467616134251215843, \
      0.05467616134251215843, \
      0.05467616134251215843, \
      0.18946269484050054510, \
      0.18946269484050054510, \
      0.18946269484050054510, \
      0.18946269484050054510, \
      0.02248423582708249449, \
      0.02248423582708249449, \
      0.02248423582708249449, \
      0.02248423582708249449, \
      0.41340822589276282617, \
      0.41340822589276282617, \
      0.41340822589276282617, \
      0.41340822589276282617, \
      0.55077233639120526387, \
      0.55077233639120526387, \
      0.55077233639120526387, \
      0.55077233639120526387, \
      0.31914147555912980581, \
      0.31914147555912980581, \
      0.31914147555912980581, \
      0.31914147555912980581, \
      0.08935238781868591607, \
      0.08935238781868591607, \
      0.08935238781868591607, \
      0.08935238781868591607, \
      0.06151583405729108001, \
      0.06151583405729108001, \
      0.06151583405729108001, \
      0.06151583405729108001, \
      0.32642198515966086569, \
      0.32642198515966086569, \
      0.32642198515966086569, \
      0.32642198515966086569, \
      0.17557242043675652665, \
      0.17557242043675652665, \
      0.17557242043675652665, \
      0.17557242043675652665, \
      0.17557242043675652665, \
      0.17557242043675652665, \
      0.17557242043675652665, \
      0.17557242043675652665, \
      0.01570840570495662947, \
      0.01570840570495662947, \
      0.01570840570495662947, \
      0.01570840570495662947, \
      0.01570840570495662947, \
      0.01570840570495662947, \
      0.01570840570495662947, \
      0.01570840570495662947 ] )

  w= np.array ( [ \
      0.00351798245822128233, \
      0.04216520928063208912, \
      0.00852104325745563912, \
      0.00852104325745563912, \
      0.00852104325745563912, \
      0.00852104325745563912, \
      0.02087072229798967934, \
      0.02087072229798967934, \
      0.02087072229798967934, \
      0.02087072229798967934, \
      0.01073969585101612438, \
      0.01073969585101612438, \
      0.01073969585101612438, \
      0.01073969585101612438, \
      0.02521321637389669496, \
      0.02521321637389669496, \
      0.02521321637389669496, \
      0.02521321637389669496, \
      0.01961258547003659133, \
      0.01961258547003659133, \
      0.01961258547003659133, \
      0.01961258547003659133, \
      0.01643323197880764905, \
      0.01643323197880764905, \
      0.01643323197880764905, \
      0.01643323197880764905, \
      0.01830589291063876300, \
      0.01830589291063876300, \
      0.01830589291063876300, \
      0.01830589291063876300, \
      0.01130841811263377274, \
      0.01130841811263377274, \
      0.01130841811263377274, \
      0.01130841811263377274, \
      0.02507245299443831496, \
      0.02507245299443831496, \
      0.02507245299443831496, \
      0.02507245299443831496, \
      0.00441940990434765493, \
      0.00441940990434765493, \
      0.00441940990434765493, \
      0.00441940990434765493, \
      0.04065272607298718588, \
      0.04065272607298718588, \
      0.04065272607298718588, \
      0.04065272607298718588, \
      0.01219793270502279002, \
      0.01219793270502279002, \
      0.01219793270502279002, \
      0.01219793270502279002, \
      0.01219793270502279002, \
      0.01219793270502279002, \
      0.01219793270502279002, \
      0.01219793270502279002, \
      0.00651697071549649839, \
      0.00651697071549649839, \
      0.00651697071549649839, \
      0.00651697071549649839, \
      0.00651697071549649839, \
      0.00651697071549649839, \
      0.00651697071549649839, \
      0.00651697071549649839 ] )

  return x, y, z, w

def rule10 ( ):

#*****************************************************************************80
#
## rule10() returns the pyramid quadrature rule of precision 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.65420170176119341043, \
      0.00000000000000000000, \
     -0.65420170176119341043, \
      0.00000000000000000000, \
      0.76633927991746164654, \
      0.00000000000000000000, \
     -0.76633927991746164654, \
      0.00000000000000000000, \
      0.80421056101815546757, \
      0.00000000000000000000, \
     -0.80421056101815546757, \
      0.00000000000000000000, \
      0.21719757883626783501, \
      0.00000000000000000000, \
     -0.21719757883626783501, \
      0.00000000000000000000, \
      0.20937347351036650345, \
      0.00000000000000000000, \
     -0.20937347351036650345, \
      0.00000000000000000000, \
      0.52830709053289259813, \
      0.00000000000000000000, \
     -0.52830709053289259813, \
      0.00000000000000000000, \
      0.34681490190497532566, \
     -0.34681490190497532566, \
      0.34681490190497532566, \
     -0.34681490190497532566, \
      0.54234774233239257946, \
     -0.54234774233239257946, \
      0.54234774233239257946, \
     -0.54234774233239257946, \
      0.42965769544556714488, \
     -0.42965769544556714488, \
      0.42965769544556714488, \
     -0.42965769544556714488, \
      0.71871414601724947779, \
     -0.71871414601724947779, \
      0.71871414601724947779, \
     -0.71871414601724947779, \
      0.76244008578748778682, \
     -0.76244008578748778682, \
      0.76244008578748778682, \
     -0.76244008578748778682, \
      0.96427350086319296718, \
     -0.96427350086319296718, \
      0.96427350086319296718, \
     -0.96427350086319296718, \
      0.27897388698743774693, \
     -0.27897388698743774693, \
      0.27897388698743774693, \
     -0.27897388698743774693, \
      0.73124529835235163588, \
      0.37115067890003261564, \
     -0.73124529835235163588, \
      0.37115067890003261564, \
      0.73124529835235163588, \
     -0.37115067890003261564, \
     -0.73124529835235163588, \
     -0.37115067890003261564, \
      0.92194807057971739361, \
      0.41966522833393532510, \
     -0.92194807057971739361, \
      0.41966522833393532510, \
      0.92194807057971739361, \
     -0.41966522833393532510, \
     -0.92194807057971739361, \
     -0.41966522833393532510, \
      0.19954261519157223681, \
      0.44340097447242488027, \
     -0.19954261519157223681, \
      0.44340097447242488027, \
      0.19954261519157223681, \
     -0.44340097447242488027, \
     -0.19954261519157223681, \
     -0.44340097447242488027 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.65420170176119341043, \
      0.00000000000000000000, \
     -0.65420170176119341043, \
      0.00000000000000000000, \
      0.76633927991746164654, \
      0.00000000000000000000, \
     -0.76633927991746164654, \
      0.00000000000000000000, \
      0.80421056101815546757, \
      0.00000000000000000000, \
     -0.80421056101815546757, \
      0.00000000000000000000, \
      0.21719757883626783501, \
      0.00000000000000000000, \
     -0.21719757883626783501, \
      0.00000000000000000000, \
      0.20937347351036650345, \
      0.00000000000000000000, \
     -0.20937347351036650345, \
      0.00000000000000000000, \
      0.52830709053289259813, \
      0.00000000000000000000, \
     -0.52830709053289259813, \
      0.34681490190497532566, \
      0.34681490190497532566, \
     -0.34681490190497532566, \
     -0.34681490190497532566, \
      0.54234774233239257946, \
      0.54234774233239257946, \
     -0.54234774233239257946, \
     -0.54234774233239257946, \
      0.42965769544556714488, \
      0.42965769544556714488, \
     -0.42965769544556714488, \
     -0.42965769544556714488, \
      0.71871414601724947779, \
      0.71871414601724947779, \
     -0.71871414601724947779, \
     -0.71871414601724947779, \
      0.76244008578748778682, \
      0.76244008578748778682, \
     -0.76244008578748778682, \
     -0.76244008578748778682, \
      0.96427350086319296718, \
      0.96427350086319296718, \
     -0.96427350086319296718, \
     -0.96427350086319296718, \
      0.27897388698743774693, \
      0.27897388698743774693, \
     -0.27897388698743774693, \
     -0.27897388698743774693, \
      0.37115067890003261564, \
      0.73124529835235163588, \
      0.37115067890003261564, \
     -0.73124529835235163588, \
     -0.37115067890003261564, \
      0.73124529835235163588, \
     -0.37115067890003261564, \
     -0.73124529835235163588, \
      0.41966522833393532510, \
      0.92194807057971739361, \
      0.41966522833393532510, \
     -0.92194807057971739361, \
     -0.41966522833393532510, \
      0.92194807057971739361, \
     -0.41966522833393532510, \
     -0.92194807057971739361, \
      0.44340097447242488027, \
      0.19954261519157223681, \
      0.44340097447242488027, \
     -0.19954261519157223681, \
     -0.44340097447242488027, \
      0.19954261519157223681, \
     -0.44340097447242488027, \
     -0.19954261519157223681 ] )

  z = np.array ( [ \
      0.91766654896784238815, \
      0.70900937404687269794, \
      0.22713967401042231553, \
      0.06874011069480644165, \
      0.12392544997399050632, \
      0.12392544997399050632, \
      0.12392544997399050632, \
      0.12392544997399050632, \
      0.02096299791450871586, \
      0.02096299791450871586, \
      0.02096299791450871586, \
      0.02096299791450871586, \
      0.16577313546766450636, \
      0.16577313546766450636, \
      0.16577313546766450636, \
      0.16577313546766450636, \
      0.49340520933953563310, \
      0.49340520933953563310, \
      0.49340520933953563310, \
      0.49340520933953563310, \
      0.78969767134839341516, \
      0.78969767134839341516, \
      0.78969767134839341516, \
      0.78969767134839341516, \
      0.47169288904858786005, \
      0.47169288904858786005, \
      0.47169288904858786005, \
      0.47169288904858786005, \
      0.02011394567580290782, \
      0.02011394567580290782, \
      0.02011394567580290782, \
      0.02011394567580290782, \
      0.36822101998927786459, \
      0.36822101998927786459, \
      0.36822101998927786459, \
      0.36822101998927786459, \
      0.12661594867701117528, \
      0.12661594867701117528, \
      0.12661594867701117528, \
      0.12661594867701117528, \
      0.02433819982878694319, \
      0.02433819982878694319, \
      0.02433819982878694319, \
      0.02433819982878694319, \
      0.12701442502569038062, \
      0.12701442502569038062, \
      0.12701442502569038062, \
      0.12701442502569038062, \
      0.01067692573406054529, \
      0.01067692573406054529, \
      0.01067692573406054529, \
      0.01067692573406054529, \
      0.59704297313030385563, \
      0.59704297313030385563, \
      0.59704297313030385563, \
      0.59704297313030385563, \
      0.21756166315495037433, \
      0.21756166315495037433, \
      0.21756166315495037433, \
      0.21756166315495037433, \
      0.21756166315495037433, \
      0.21756166315495037433, \
      0.21756166315495037433, \
      0.21756166315495037433, \
      0.04137857207280886546, \
      0.04137857207280886546, \
      0.04137857207280886546, \
      0.04137857207280886546, \
      0.04137857207280886546, \
      0.04137857207280886546, \
      0.04137857207280886546, \
      0.04137857207280886546, \
      0.32615365723990619173, \
      0.32615365723990619173, \
      0.32615365723990619173, \
      0.32615365723990619173, \
      0.32615365723990619173, \
      0.32615365723990619173, \
      0.32615365723990619173, \
      0.32615365723990619173 ] )

  w= np.array ( [ \
      0.00222688724675269151, \
      0.01676862119517166794, \
      0.05218524659101939772, \
      0.02912684113372536118, \
      0.02061250827144200243, \
      0.02061250827144200243, \
      0.02061250827144200243, \
      0.02061250827144200243, \
      0.01001318317045431922, \
      0.01001318317045431922, \
      0.01001318317045431922, \
      0.01001318317045431922, \
      0.00380589471978953851, \
      0.00380589471978953851, \
      0.00380589471978953851, \
      0.00380589471978953851, \
      0.01603356460939567643, \
      0.01603356460939567643, \
      0.01603356460939567643, \
      0.01603356460939567643, \
      0.00421057398582402181, \
      0.00421057398582402181, \
      0.00421057398582402181, \
      0.00421057398582402181, \
      0.00812973230941097316, \
      0.00812973230941097316, \
      0.00812973230941097316, \
      0.00812973230941097316, \
      0.01345646795638386767, \
      0.01345646795638386767, \
      0.01345646795638386767, \
      0.01345646795638386767, \
      0.01016376299548378027, \
      0.01016376299548378027, \
      0.01016376299548378027, \
      0.01016376299548378027, \
      0.02981645762492043245, \
      0.02981645762492043245, \
      0.02981645762492043245, \
      0.02981645762492043245, \
      0.00865712783423741410, \
      0.00865712783423741410, \
      0.00865712783423741410, \
      0.00865712783423741410, \
      0.00953199916493123987, \
      0.00953199916493123987, \
      0.00953199916493123987, \
      0.00953199916493123987, \
      0.00071395826747580517, \
      0.00071395826747580517, \
      0.00071395826747580517, \
      0.00071395826747580517, \
      0.01519293397619959039, \
      0.01519293397619959039, \
      0.01519293397619959039, \
      0.01519293397619959039, \
      0.01008533639437561233, \
      0.01008533639437561233, \
      0.01008533639437561233, \
      0.01008533639437561233, \
      0.01008533639437561233, \
      0.01008533639437561233, \
      0.01008533639437561233, \
      0.01008533639437561233, \
      0.00585933822996072967, \
      0.00585933822996072967, \
      0.00585933822996072967, \
      0.00585933822996072967, \
      0.00585933822996072967, \
      0.00585933822996072967, \
      0.00585933822996072967, \
      0.00585933822996072967, \
      0.02134779341185568530, \
      0.02134779341185568530, \
      0.02134779341185568530, \
      0.02134779341185568530, \
      0.02134779341185568530, \
      0.02134779341185568530, \
      0.02134779341185568530, \
      0.02134779341185568530 ] )

  return x, y, z, w

def rule11 ( ):

#*****************************************************************************80
#
## rule11() returns the pyramid quadrature rule of precision 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.30959144111215058937, \
      0.00000000000000000000, \
     -0.30959144111215058937, \
      0.00000000000000000000, \
      0.76993922081029786408, \
      0.00000000000000000000, \
     -0.76993922081029786408, \
      0.00000000000000000000, \
      0.70027038117446127607, \
      0.00000000000000000000, \
     -0.70027038117446127607, \
      0.00000000000000000000, \
      0.46095035429072822586, \
      0.00000000000000000000, \
     -0.46095035429072822586, \
      0.00000000000000000000, \
      0.29928938216959510843, \
      0.00000000000000000000, \
     -0.29928938216959510843, \
      0.00000000000000000000, \
      0.59114943757155702375, \
      0.00000000000000000000, \
     -0.59114943757155702375, \
      0.00000000000000000000, \
      0.01861308147704909821, \
      0.00000000000000000000, \
     -0.01861308147704909821, \
      0.00000000000000000000, \
      0.16034290975464657314, \
      0.00000000000000000000, \
     -0.16034290975464657314, \
      0.00000000000000000000, \
      0.14450753554447465232, \
     -0.14450753554447465232, \
      0.14450753554447465232, \
     -0.14450753554447465232, \
      0.59369450979675508773, \
     -0.59369450979675508773, \
      0.59369450979675508773, \
     -0.59369450979675508773, \
      0.27490141802950085470, \
     -0.27490141802950085470, \
      0.27490141802950085470, \
     -0.27490141802950085470, \
      0.29680077247241393179, \
     -0.29680077247241393179, \
      0.29680077247241393179, \
     -0.29680077247241393179, \
      0.59849263706569033605, \
     -0.59849263706569033605, \
      0.59849263706569033605, \
     -0.59849263706569033605, \
      0.61031415307328662490, \
     -0.61031415307328662490, \
      0.61031415307328662490, \
     -0.61031415307328662490, \
      0.37345023081856359992, \
     -0.37345023081856359992, \
      0.37345023081856359992, \
     -0.37345023081856359992, \
      0.26245991463277401623, \
     -0.26245991463277401623, \
      0.26245991463277401623, \
     -0.26245991463277401623, \
      0.36860635719790568743, \
     -0.36860635719790568743, \
      0.36860635719790568743, \
     -0.36860635719790568743, \
      0.87026293442361135622, \
     -0.87026293442361135622, \
      0.87026293442361135622, \
     -0.87026293442361135622, \
      0.81025745002423155139, \
     -0.81025745002423155139, \
      0.81025745002423155139, \
     -0.81025745002423155139, \
      0.78967657467472973654, \
      0.35527213835047594115, \
     -0.78967657467472973654, \
      0.35527213835047594115, \
      0.78967657467472973654, \
     -0.35527213835047594115, \
     -0.78967657467472973654, \
     -0.35527213835047594115, \
      0.92805034944130604391, \
      0.41484210234755791724, \
     -0.92805034944130604391, \
      0.41484210234755791724, \
      0.92805034944130604391, \
     -0.41484210234755791724, \
     -0.92805034944130604391, \
     -0.41484210234755791724, \
      0.23313789083599262275, \
      0.55628779191329114084, \
     -0.23313789083599262275, \
      0.55628779191329114084, \
      0.23313789083599262275, \
     -0.55628779191329114084, \
     -0.23313789083599262275, \
     -0.55628779191329114084 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.30959144111215058937, \
      0.00000000000000000000, \
     -0.30959144111215058937, \
      0.00000000000000000000, \
      0.76993922081029786408, \
      0.00000000000000000000, \
     -0.76993922081029786408, \
      0.00000000000000000000, \
      0.70027038117446127607, \
      0.00000000000000000000, \
     -0.70027038117446127607, \
      0.00000000000000000000, \
      0.46095035429072822586, \
      0.00000000000000000000, \
     -0.46095035429072822586, \
      0.00000000000000000000, \
      0.29928938216959510843, \
      0.00000000000000000000, \
     -0.29928938216959510843, \
      0.00000000000000000000, \
      0.59114943757155702375, \
      0.00000000000000000000, \
     -0.59114943757155702375, \
      0.00000000000000000000, \
      0.01861308147704909821, \
      0.00000000000000000000, \
     -0.01861308147704909821, \
      0.00000000000000000000, \
      0.16034290975464657314, \
      0.00000000000000000000, \
     -0.16034290975464657314, \
      0.14450753554447465232, \
      0.14450753554447465232, \
     -0.14450753554447465232, \
     -0.14450753554447465232, \
      0.59369450979675508773, \
      0.59369450979675508773, \
     -0.59369450979675508773, \
     -0.59369450979675508773, \
      0.27490141802950085470, \
      0.27490141802950085470, \
     -0.27490141802950085470, \
     -0.27490141802950085470, \
      0.29680077247241393179, \
      0.29680077247241393179, \
     -0.29680077247241393179, \
     -0.29680077247241393179, \
      0.59849263706569033605, \
      0.59849263706569033605, \
     -0.59849263706569033605, \
     -0.59849263706569033605, \
      0.61031415307328662490, \
      0.61031415307328662490, \
     -0.61031415307328662490, \
     -0.61031415307328662490, \
      0.37345023081856359992, \
      0.37345023081856359992, \
     -0.37345023081856359992, \
     -0.37345023081856359992, \
      0.26245991463277401623, \
      0.26245991463277401623, \
     -0.26245991463277401623, \
     -0.26245991463277401623, \
      0.36860635719790568743, \
      0.36860635719790568743, \
     -0.36860635719790568743, \
     -0.36860635719790568743, \
      0.87026293442361135622, \
      0.87026293442361135622, \
     -0.87026293442361135622, \
     -0.87026293442361135622, \
      0.81025745002423155139, \
      0.81025745002423155139, \
     -0.81025745002423155139, \
     -0.81025745002423155139, \
      0.35527213835047594115, \
      0.78967657467472973654, \
      0.35527213835047594115, \
     -0.78967657467472973654, \
     -0.35527213835047594115, \
      0.78967657467472973654, \
     -0.35527213835047594115, \
     -0.78967657467472973654, \
      0.41484210234755791724, \
      0.92805034944130604391, \
      0.41484210234755791724, \
     -0.92805034944130604391, \
     -0.41484210234755791724, \
      0.92805034944130604391, \
     -0.41484210234755791724, \
     -0.92805034944130604391, \
      0.55628779191329114084, \
      0.23313789083599262275, \
      0.55628779191329114084, \
     -0.23313789083599262275, \
     -0.55628779191329114084, \
      0.23313789083599262275, \
     -0.55628779191329114084, \
     -0.23313789083599262275 ] )

  z = np.array ( [ \
      0.69295639647508833203, \
      0.91101523446275922691, \
      0.25032929072548470995, \
      0.05040798390564713710, \
      0.05040798390564713710, \
      0.05040798390564713710, \
      0.05040798390564713710, \
      0.01178348626907169128, \
      0.01178348626907169128, \
      0.01178348626907169128, \
      0.01178348626907169128, \
      0.10103940902556154957, \
      0.10103940902556154957, \
      0.10103940902556154957, \
      0.10103940902556154957, \
      0.34272757605804599068, \
      0.34272757605804599068, \
      0.34272757605804599068, \
      0.34272757605804599068, \
      0.62869898216776509692, \
      0.62869898216776509692, \
      0.62869898216776509692, \
      0.62869898216776509692, \
      0.25822848523085090156, \
      0.25822848523085090156, \
      0.25822848523085090156, \
      0.25822848523085090156, \
      0.43583449548328001555, \
      0.43583449548328001555, \
      0.43583449548328001555, \
      0.43583449548328001555, \
      0.21928319414297889334, \
      0.21928319414297889334, \
      0.21928319414297889334, \
      0.21928319414297889334, \
      0.78797433053468768360, \
      0.78797433053468768360, \
      0.78797433053468768360, \
      0.78797433053468768360, \
      0.30892958869107134401, \
      0.30892958869107134401, \
      0.30892958869107134401, \
      0.30892958869107134401, \
      0.01781185684646453826, \
      0.01781185684646453826, \
      0.01781185684646453826, \
      0.01781185684646453826, \
      0.11127033608982600521, \
      0.11127033608982600521, \
      0.11127033608982600521, \
      0.11127033608982600521, \
      0.02444716310077480956, \
      0.02444716310077480956, \
      0.02444716310077480956, \
      0.02444716310077480956, \
      0.12041875519309763742, \
      0.12041875519309763742, \
      0.12041875519309763742, \
      0.12041875519309763742, \
      0.57752532555241498091, \
      0.57752532555241498091, \
      0.57752532555241498091, \
      0.57752532555241498091, \
      0.49169801908816329616, \
      0.49169801908816329616, \
      0.49169801908816329616, \
      0.49169801908816329616, \
      0.26311325712772259955, \
      0.26311325712772259955, \
      0.26311325712772259955, \
      0.26311325712772259955, \
      0.01908681361607608359, \
      0.01908681361607608359, \
      0.01908681361607608359, \
      0.01908681361607608359, \
      0.11692619926762114202, \
      0.11692619926762114202, \
      0.11692619926762114202, \
      0.11692619926762114202, \
      0.17968095390177224457, \
      0.17968095390177224457, \
      0.17968095390177224457, \
      0.17968095390177224457, \
      0.17968095390177224457, \
      0.17968095390177224457, \
      0.17968095390177224457, \
      0.17968095390177224457, \
      0.03535559961728908934, \
      0.03535559961728908934, \
      0.03535559961728908934, \
      0.03535559961728908934, \
      0.03535559961728908934, \
      0.03535559961728908934, \
      0.03535559961728908934, \
      0.03535559961728908934, \
      0.41464402024224555898, \
      0.41464402024224555898, \
      0.41464402024224555898, \
      0.41464402024224555898, \
      0.41464402024224555898, \
      0.41464402024224555898, \
      0.41464402024224555898, \
      0.41464402024224555898 ] )

  w= np.array ( [ \
      0.01286363653695535118, \
      0.00259572122542773513, \
      0.00817638570047552610, \
      0.00511941439804289126, \
      0.00511941439804289126, \
      0.00511941439804289126, \
      0.00511941439804289126, \
      0.00684699666646234988, \
      0.00684699666646234988, \
      0.00684699666646234988, \
      0.00684699666646234988, \
      0.02021405278036775971, \
      0.02021405278036775971, \
      0.02021405278036775971, \
      0.02021405278036775971, \
      0.01240017518258633086, \
      0.01240017518258633086, \
      0.01240017518258633086, \
      0.01240017518258633086, \
      0.01050060859922616330, \
      0.01050060859922616330, \
      0.01050060859922616330, \
      0.01050060859922616330, \
      0.01207523991498536502, \
      0.01207523991498536502, \
      0.01207523991498536502, \
      0.01207523991498536502, \
      0.00794549439937168242, \
      0.00794549439937168242, \
      0.00794549439937168242, \
      0.00794549439937168242, \
      0.00897930801963979161, \
      0.00897930801963979161, \
      0.00897930801963979161, \
      0.00897930801963979161, \
      0.00432861007717266853, \
      0.00432861007717266853, \
      0.00432861007717266853, \
      0.00432861007717266853, \
      0.00959150593850333251, \
      0.00959150593850333251, \
      0.00959150593850333251, \
      0.00959150593850333251, \
      0.00845889607542490291, \
      0.00845889607542490291, \
      0.00845889607542490291, \
      0.00845889607542490291, \
      0.02093917618186586990, \
      0.02093917618186586990, \
      0.02093917618186586990, \
      0.02093917618186586990, \
      0.01007335618421271312, \
      0.01007335618421271312, \
      0.01007335618421271312, \
      0.01007335618421271312, \
      0.01474935950898293054, \
      0.01474935950898293054, \
      0.01474935950898293054, \
      0.01474935950898293054, \
      0.00405432020025909591, \
      0.00405432020025909591, \
      0.00405432020025909591, \
      0.00405432020025909591, \
      0.01768012056788626288, \
      0.01768012056788626288, \
      0.01768012056788626288, \
      0.01768012056788626288, \
      0.02349367280688881635, \
      0.02349367280688881635, \
      0.02349367280688881635, \
      0.02349367280688881635, \
      0.00300355345952720053, \
      0.00300355345952720053, \
      0.00300355345952720053, \
      0.00300355345952720053, \
      0.00433057971890565482, \
      0.00433057971890565482, \
      0.00433057971890565482, \
      0.00433057971890565482, \
      0.00788297764391489818, \
      0.00788297764391489818, \
      0.00788297764391489818, \
      0.00788297764391489818, \
      0.00788297764391489818, \
      0.00788297764391489818, \
      0.00788297764391489818, \
      0.00788297764391489818, \
      0.00509491185532656536, \
      0.00509491185532656536, \
      0.00509491185532656536, \
      0.00509491185532656536, \
      0.00509491185532656536, \
      0.00509491185532656536, \
      0.00509491185532656536, \
      0.00509491185532656536, \
      0.00667542222774531943, \
      0.00667542222774531943, \
      0.00667542222774531943, \
      0.00667542222774531943, \
      0.00667542222774531943, \
      0.00667542222774531943, \
      0.00667542222774531943, \
      0.00667542222774531943 ] )

  return x, y, z, w

def rule12 ( ):

#*****************************************************************************80
#
## rule12() returns the pyramid quadrature rule of precision 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.61752408228797095457, \
      0.00000000000000000000, \
     -0.61752408228797095457, \
      0.00000000000000000000, \
      0.95383417813475923630, \
      0.00000000000000000000, \
     -0.95383417813475923630, \
      0.00000000000000000000, \
      0.59503005801385822071, \
      0.00000000000000000000, \
     -0.59503005801385822071, \
      0.00000000000000000000, \
      0.43539359820232903520, \
      0.00000000000000000000, \
     -0.43539359820232903520, \
      0.00000000000000000000, \
      0.13291355561208040292, \
      0.00000000000000000000, \
     -0.13291355561208040292, \
      0.00000000000000000000, \
      0.79714363482446959353, \
      0.00000000000000000000, \
     -0.79714363482446959353, \
      0.00000000000000000000, \
      0.31078295049399401462, \
      0.00000000000000000000, \
     -0.31078295049399401462, \
      0.00000000000000000000, \
      0.46896896703369211901, \
      0.00000000000000000000, \
     -0.46896896703369211901, \
      0.00000000000000000000, \
      0.06329314929065793516, \
      0.00000000000000000000, \
     -0.06329314929065793516, \
      0.00000000000000000000, \
      0.11694124473665239161, \
     -0.11694124473665239161, \
      0.11694124473665239161, \
     -0.11694124473665239161, \
      0.47710850655214198657, \
     -0.47710850655214198657, \
      0.47710850655214198657, \
     -0.47710850655214198657, \
      0.34796735400888462175, \
     -0.34796735400888462175, \
      0.34796735400888462175, \
     -0.34796735400888462175, \
      0.21748093989891267852, \
     -0.21748093989891267852, \
      0.21748093989891267852, \
     -0.21748093989891267852, \
      0.67426207541025851011, \
     -0.67426207541025851011, \
      0.67426207541025851011, \
     -0.67426207541025851011, \
      0.65415312577816908668, \
     -0.65415312577816908668, \
      0.65415312577816908668, \
     -0.65415312577816908668, \
      0.26043868995957136780, \
     -0.26043868995957136780, \
      0.26043868995957136780, \
     -0.26043868995957136780, \
      0.27442107868377230151, \
     -0.27442107868377230151, \
      0.27442107868377230151, \
     -0.27442107868377230151, \
      0.51259022737109982693, \
     -0.51259022737109982693, \
      0.51259022737109982693, \
     -0.51259022737109982693, \
      0.86878873539049084052, \
     -0.86878873539049084052, \
      0.86878873539049084052, \
     -0.86878873539049084052, \
      0.71181681800308360675, \
     -0.71181681800308360675, \
      0.71181681800308360675, \
     -0.71181681800308360675, \
      0.36754569532388259301, \
     -0.36754569532388259301, \
      0.36754569532388259301, \
     -0.36754569532388259301, \
      0.84896937482456835689, \
      0.51203646317203110883, \
     -0.84896937482456835689, \
      0.51203646317203110883, \
      0.84896937482456835689, \
     -0.51203646317203110883, \
     -0.84896937482456835689, \
     -0.51203646317203110883, \
      0.97385403135997028468, \
      0.74670340940557777820, \
     -0.97385403135997028468, \
      0.74670340940557777820, \
      0.97385403135997028468, \
     -0.74670340940557777820, \
     -0.97385403135997028468, \
     -0.74670340940557777820, \
      0.32302405518012644592, \
      0.62555613253804132068, \
     -0.32302405518012644592, \
      0.62555613253804132068, \
      0.32302405518012644592, \
     -0.62555613253804132068, \
     -0.32302405518012644592, \
     -0.62555613253804132068, \
      0.19450076345283720536, \
      0.69805959364273262313, \
     -0.19450076345283720536, \
      0.69805959364273262313, \
      0.19450076345283720536, \
     -0.69805959364273262313, \
     -0.19450076345283720536, \
     -0.69805959364273262313, \
      0.32894885387189143344, \
      0.85383152896625225114, \
     -0.32894885387189143344, \
      0.85383152896625225114, \
      0.32894885387189143344, \
     -0.85383152896625225114, \
     -0.32894885387189143344, \
     -0.85383152896625225114 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.61752408228797095457, \
      0.00000000000000000000, \
     -0.61752408228797095457, \
      0.00000000000000000000, \
      0.95383417813475923630, \
      0.00000000000000000000, \
     -0.95383417813475923630, \
      0.00000000000000000000, \
      0.59503005801385822071, \
      0.00000000000000000000, \
     -0.59503005801385822071, \
      0.00000000000000000000, \
      0.43539359820232903520, \
      0.00000000000000000000, \
     -0.43539359820232903520, \
      0.00000000000000000000, \
      0.13291355561208040292, \
      0.00000000000000000000, \
     -0.13291355561208040292, \
      0.00000000000000000000, \
      0.79714363482446959353, \
      0.00000000000000000000, \
     -0.79714363482446959353, \
      0.00000000000000000000, \
      0.31078295049399401462, \
      0.00000000000000000000, \
     -0.31078295049399401462, \
      0.00000000000000000000, \
      0.46896896703369211901, \
      0.00000000000000000000, \
     -0.46896896703369211901, \
      0.00000000000000000000, \
      0.06329314929065793516, \
      0.00000000000000000000, \
     -0.06329314929065793516, \
      0.11694124473665239161, \
      0.11694124473665239161, \
     -0.11694124473665239161, \
     -0.11694124473665239161, \
      0.47710850655214198657, \
      0.47710850655214198657, \
     -0.47710850655214198657, \
     -0.47710850655214198657, \
      0.34796735400888462175, \
      0.34796735400888462175, \
     -0.34796735400888462175, \
     -0.34796735400888462175, \
      0.21748093989891267852, \
      0.21748093989891267852, \
     -0.21748093989891267852, \
     -0.21748093989891267852, \
      0.67426207541025851011, \
      0.67426207541025851011, \
     -0.67426207541025851011, \
     -0.67426207541025851011, \
      0.65415312577816908668, \
      0.65415312577816908668, \
     -0.65415312577816908668, \
     -0.65415312577816908668, \
      0.26043868995957136780, \
      0.26043868995957136780, \
     -0.26043868995957136780, \
     -0.26043868995957136780, \
      0.27442107868377230151, \
      0.27442107868377230151, \
     -0.27442107868377230151, \
     -0.27442107868377230151, \
      0.51259022737109982693, \
      0.51259022737109982693, \
     -0.51259022737109982693, \
     -0.51259022737109982693, \
      0.86878873539049084052, \
      0.86878873539049084052, \
     -0.86878873539049084052, \
     -0.86878873539049084052, \
      0.71181681800308360675, \
      0.71181681800308360675, \
     -0.71181681800308360675, \
     -0.71181681800308360675, \
      0.36754569532388259301, \
      0.36754569532388259301, \
     -0.36754569532388259301, \
     -0.36754569532388259301, \
      0.51203646317203110883, \
      0.84896937482456835689, \
      0.51203646317203110883, \
     -0.84896937482456835689, \
     -0.51203646317203110883, \
      0.84896937482456835689, \
     -0.51203646317203110883, \
     -0.84896937482456835689, \
      0.74670340940557777820, \
      0.97385403135997028468, \
      0.74670340940557777820, \
     -0.97385403135997028468, \
     -0.74670340940557777820, \
      0.97385403135997028468, \
     -0.74670340940557777820, \
     -0.97385403135997028468, \
      0.62555613253804132068, \
      0.32302405518012644592, \
      0.62555613253804132068, \
     -0.32302405518012644592, \
     -0.62555613253804132068, \
      0.32302405518012644592, \
     -0.62555613253804132068, \
     -0.32302405518012644592, \
      0.69805959364273262313, \
      0.19450076345283720536, \
      0.69805959364273262313, \
     -0.19450076345283720536, \
     -0.69805959364273262313, \
      0.19450076345283720536, \
     -0.69805959364273262313, \
     -0.19450076345283720536, \
      0.85383152896625225114, \
      0.32894885387189143344, \
      0.85383152896625225114, \
     -0.32894885387189143344, \
     -0.85383152896625225114, \
      0.32894885387189143344, \
     -0.85383152896625225114, \
     -0.32894885387189143344 ] )

  z = np.array ( [ \
      0.45700700424071905026, \
      0.96248480104808953328, \
      0.02656531684537740551, \
      0.00537472082577391923, \
      0.00537472082577391923, \
      0.00537472082577391923, \
      0.00537472082577391923, \
      0.03942123626649530338, \
      0.03942123626649530338, \
      0.03942123626649530338, \
      0.03942123626649530338, \
      0.07619184421748394220, \
      0.07619184421748394220, \
      0.07619184421748394220, \
      0.07619184421748394220, \
      0.52461875533620183631, \
      0.52461875533620183631, \
      0.52461875533620183631, \
      0.52461875533620183631, \
      0.83871994031142604875, \
      0.83871994031142604875, \
      0.83871994031142604875, \
      0.83871994031142604875, \
      0.20075189777897944898, \
      0.20075189777897944898, \
      0.20075189777897944898, \
      0.20075189777897944898, \
      0.68265469105314702247, \
      0.68265469105314702247, \
      0.68265469105314702247, \
      0.68265469105314702247, \
      0.31713382467521444852, \
      0.31713382467521444852, \
      0.31713382467521444852, \
      0.31713382467521444852, \
      0.12709629034671870995, \
      0.12709629034671870995, \
      0.12709629034671870995, \
      0.12709629034671870995, \
      0.67124174294922867023, \
      0.67124174294922867023, \
      0.67124174294922867023, \
      0.67124174294922867023, \
      0.45862802718642248223, \
      0.45862802718642248223, \
      0.45862802718642248223, \
      0.45862802718642248223, \
      0.11938890613701966248, \
      0.11938890613701966248, \
      0.11938890613701966248, \
      0.11938890613701966248, \
      0.25741784866521960629, \
      0.25741784866521960629, \
      0.25741784866521960629, \
      0.25741784866521960629, \
      0.02260502558938975656, \
      0.02260502558938975656, \
      0.02260502558938975656, \
      0.02260502558938975656, \
      0.08746307755558260788, \
      0.08746307755558260788, \
      0.08746307755558260788, \
      0.08746307755558260788, \
      0.67140164127972612462, \
      0.67140164127972612462, \
      0.67140164127972612462, \
      0.67140164127972612462, \
      0.47604255048878973966, \
      0.47604255048878973966, \
      0.47604255048878973966, \
      0.47604255048878973966, \
      0.22777955815540271156, \
      0.22777955815540271156, \
      0.22777955815540271156, \
      0.22777955815540271156, \
      0.05850272176027389998, \
      0.05850272176027389998, \
      0.05850272176027389998, \
      0.05850272176027389998, \
      0.22053995731942055425, \
      0.22053995731942055425, \
      0.22053995731942055425, \
      0.22053995731942055425, \
      0.02548724290196442005, \
      0.02548724290196442005, \
      0.02548724290196442005, \
      0.02548724290196442005, \
      0.11145836537804799937, \
      0.11145836537804799937, \
      0.11145836537804799937, \
      0.11145836537804799937, \
      0.11145836537804799937, \
      0.11145836537804799937, \
      0.11145836537804799937, \
      0.11145836537804799937, \
      0.00339220824679912656, \
      0.00339220824679912656, \
      0.00339220824679912656, \
      0.00339220824679912656, \
      0.00339220824679912656, \
      0.00339220824679912656, \
      0.00339220824679912656, \
      0.00339220824679912656, \
      0.32725151644051669875, \
      0.32725151644051669875, \
      0.32725151644051669875, \
      0.32725151644051669875, \
      0.32725151644051669875, \
      0.32725151644051669875, \
      0.32725151644051669875, \
      0.32725151644051669875, \
      0.14805166861898322317, \
      0.14805166861898322317, \
      0.14805166861898322317, \
      0.14805166861898322317, \
      0.14805166861898322317, \
      0.14805166861898322317, \
      0.14805166861898322317, \
      0.14805166861898322317, \
      0.02487563023274973195, \
      0.02487563023274973195, \
      0.02487563023274973195, \
      0.02487563023274973195, \
      0.02487563023274973195, \
      0.02487563023274973195, \
      0.02487563023274973195, \
      0.02487563023274973195 ] )

  w= np.array ( [ \
      0.02715854620871203245, \
      0.00043531424244899530, \
      0.01391222140872406220, \
      0.00387288146649252939, \
      0.00387288146649252939, \
      0.00387288146649252939, \
      0.00387288146649252939, \
      0.00217967971593618394, \
      0.00217967971593618394, \
      0.00217967971593618394, \
      0.00217967971593618394, \
      0.01267133485574918096, \
      0.01267133485574918096, \
      0.01267133485574918096, \
      0.01267133485574918096, \
      0.00873464163035380693, \
      0.00873464163035380693, \
      0.00873464163035380693, \
      0.00873464163035380693, \
      0.00289146731615850605, \
      0.00289146731615850605, \
      0.00289146731615850605, \
      0.00289146731615850605, \
      0.00336686848511522736, \
      0.00336686848511522736, \
      0.00336686848511522736, \
      0.00336686848511522736, \
      0.00147603803134411875, \
      0.00147603803134411875, \
      0.00147603803134411875, \
      0.00147603803134411875, \
      0.01998444773599242219, \
      0.01998444773599242219, \
      0.01998444773599242219, \
      0.01998444773599242219, \
      0.00618927170644437228, \
      0.00618927170644437228, \
      0.00618927170644437228, \
      0.00618927170644437228, \
      0.00820078705478863301, \
      0.00820078705478863301, \
      0.00820078705478863301, \
      0.00820078705478863301, \
      0.00509651546458162342, \
      0.00509651546458162342, \
      0.00509651546458162342, \
      0.00509651546458162342, \
      0.01739298850473944280, \
      0.01739298850473944280, \
      0.01739298850473944280, \
      0.01739298850473944280, \
      0.01948797782027694020, \
      0.01948797782027694020, \
      0.01948797782027694020, \
      0.01948797782027694020, \
      0.00538896243467025700, \
      0.00538896243467025700, \
      0.00538896243467025700, \
      0.00538896243467025700, \
      0.00676911731451347500, \
      0.00676911731451347500, \
      0.00676911731451347500, \
      0.00676911731451347500, \
      0.00467587609366508332, \
      0.00467587609366508332, \
      0.00467587609366508332, \
      0.00467587609366508332, \
      0.01838172037009152757, \
      0.01838172037009152757, \
      0.01838172037009152757, \
      0.01838172037009152757, \
      0.01407964506457294943, \
      0.01407964506457294943, \
      0.01407964506457294943, \
      0.01407964506457294943, \
      0.00283370063460703292, \
      0.00283370063460703292, \
      0.00283370063460703292, \
      0.00283370063460703292, \
      0.00479137222817773486, \
      0.00479137222817773486, \
      0.00479137222817773486, \
      0.00479137222817773486, \
      0.00990680633819146332, \
      0.00990680633819146332, \
      0.00990680633819146332, \
      0.00990680633819146332, \
      0.00535574363023301383, \
      0.00535574363023301383, \
      0.00535574363023301383, \
      0.00535574363023301383, \
      0.00535574363023301383, \
      0.00535574363023301383, \
      0.00535574363023301383, \
      0.00535574363023301383, \
      0.00081681851071822213, \
      0.00081681851071822213, \
      0.00081681851071822213, \
      0.00081681851071822213, \
      0.00081681851071822213, \
      0.00081681851071822213, \
      0.00081681851071822213, \
      0.00081681851071822213, \
      0.00854175372189276694, \
      0.00854175372189276694, \
      0.00854175372189276694, \
      0.00854175372189276694, \
      0.00854175372189276694, \
      0.00854175372189276694, \
      0.00854175372189276694, \
      0.00854175372189276694, \
      0.01018769584471248754, \
      0.01018769584471248754, \
      0.01018769584471248754, \
      0.01018769584471248754, \
      0.01018769584471248754, \
      0.01018769584471248754, \
      0.01018769584471248754, \
      0.01018769584471248754, \
      0.00572367792672661812, \
      0.00572367792672661812, \
      0.00572367792672661812, \
      0.00572367792672661812, \
      0.00572367792672661812, \
      0.00572367792672661812, \
      0.00572367792672661812, \
      0.00572367792672661812 ] )

  return x, y, z, w

def rule13 ( ):

#*****************************************************************************80
#
## rule13() returns the pyramid quadrature rule of precision 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.41223892088328983885, \
      0.00000000000000000000, \
     -0.41223892088328983885, \
      0.00000000000000000000, \
      0.94482408797958883362, \
      0.00000000000000000000, \
     -0.94482408797958883362, \
      0.00000000000000000000, \
      0.15012306550295120844, \
      0.00000000000000000000, \
     -0.15012306550295120844, \
      0.00000000000000000000, \
      0.36338283577562219273, \
      0.00000000000000000000, \
     -0.36338283577562219273, \
      0.00000000000000000000, \
      0.32897122373450704558, \
      0.00000000000000000000, \
     -0.32897122373450704558, \
      0.00000000000000000000, \
      0.55704935891608620135, \
      0.00000000000000000000, \
     -0.55704935891608620135, \
      0.00000000000000000000, \
      0.71060354437421247020, \
      0.00000000000000000000, \
     -0.71060354437421247020, \
      0.00000000000000000000, \
      0.88531748708681257121, \
      0.00000000000000000000, \
     -0.88531748708681257121, \
      0.00000000000000000000, \
      0.48884754503841615358, \
     -0.48884754503841615358, \
      0.48884754503841615358, \
     -0.48884754503841615358, \
      0.45031772456672747307, \
     -0.45031772456672747307, \
      0.45031772456672747307, \
     -0.45031772456672747307, \
      0.65872956915547864476, \
     -0.65872956915547864476, \
      0.65872956915547864476, \
     -0.65872956915547864476, \
      0.62588271911798842861, \
     -0.62588271911798842861, \
      0.62588271911798842861, \
     -0.62588271911798842861, \
      0.25178960033193620305, \
     -0.25178960033193620305, \
      0.25178960033193620305, \
     -0.25178960033193620305, \
      0.91338191280449132492, \
     -0.91338191280449132492, \
      0.91338191280449132492, \
     -0.91338191280449132492, \
      0.11117861641720541699, \
     -0.11117861641720541699, \
      0.11117861641720541699, \
     -0.11117861641720541699, \
      0.37814924987375336807, \
     -0.37814924987375336807, \
      0.37814924987375336807, \
     -0.37814924987375336807, \
      0.23146195691577758913, \
     -0.23146195691577758913, \
      0.23146195691577758913, \
     -0.23146195691577758913, \
      0.18598667282576661353, \
     -0.18598667282576661353, \
      0.18598667282576661353, \
     -0.18598667282576661353, \
      0.72941490542892961635, \
     -0.72941490542892961635, \
      0.72941490542892961635, \
     -0.72941490542892961635, \
      0.80419241777926819825, \
     -0.80419241777926819825, \
      0.80419241777926819825, \
     -0.80419241777926819825, \
      0.47036082838417470064, \
     -0.47036082838417470064, \
      0.47036082838417470064, \
     -0.47036082838417470064, \
      0.27535657520011547206, \
     -0.27535657520011547206, \
      0.27535657520011547206, \
     -0.27535657520011547206, \
      0.25840443662578793660, \
     -0.25840443662578793660, \
      0.25840443662578793660, \
     -0.25840443662578793660, \
      0.77456301686419115615, \
      0.43978938971942055369, \
     -0.77456301686419115615, \
      0.43978938971942055369, \
      0.77456301686419115615, \
     -0.43978938971942055369, \
     -0.77456301686419115615, \
     -0.43978938971942055369, \
      0.72014146551340840752, \
      0.22174790443082656455, \
     -0.72014146551340840752, \
      0.22174790443082656455, \
      0.72014146551340840752, \
     -0.22174790443082656455, \
     -0.72014146551340840752, \
     -0.22174790443082656455, \
      0.17509849556381359981, \
      0.58560797514860796209, \
     -0.17509849556381359981, \
      0.58560797514860796209, \
      0.17509849556381359981, \
     -0.58560797514860796209, \
     -0.17509849556381359981, \
     -0.58560797514860796209, \
      0.93762547318055500245, \
      0.73982675325131319610, \
     -0.93762547318055500245, \
      0.73982675325131319610, \
      0.93762547318055500245, \
     -0.73982675325131319610, \
     -0.93762547318055500245, \
     -0.73982675325131319610, \
      0.92588822421370353677, \
      0.50002093145521131490, \
     -0.92588822421370353677, \
      0.50002093145521131490, \
      0.92588822421370353677, \
     -0.50002093145521131490, \
     -0.92588822421370353677, \
     -0.50002093145521131490, \
      0.26820739210416322251, \
      0.56185198689199644662, \
     -0.26820739210416322251, \
      0.56185198689199644662, \
      0.26820739210416322251, \
     -0.56185198689199644662, \
     -0.26820739210416322251, \
     -0.56185198689199644662, \
      0.36207959439737902319, \
      0.79245628070986395830, \
     -0.36207959439737902319, \
      0.79245628070986395830, \
      0.36207959439737902319, \
     -0.79245628070986395830, \
     -0.36207959439737902319, \
     -0.79245628070986395830 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.41223892088328983885, \
      0.00000000000000000000, \
     -0.41223892088328983885, \
      0.00000000000000000000, \
      0.94482408797958883362, \
      0.00000000000000000000, \
     -0.94482408797958883362, \
      0.00000000000000000000, \
      0.15012306550295120844, \
      0.00000000000000000000, \
     -0.15012306550295120844, \
      0.00000000000000000000, \
      0.36338283577562219273, \
      0.00000000000000000000, \
     -0.36338283577562219273, \
      0.00000000000000000000, \
      0.32897122373450704558, \
      0.00000000000000000000, \
     -0.32897122373450704558, \
      0.00000000000000000000, \
      0.55704935891608620135, \
      0.00000000000000000000, \
     -0.55704935891608620135, \
      0.00000000000000000000, \
      0.71060354437421247020, \
      0.00000000000000000000, \
     -0.71060354437421247020, \
      0.00000000000000000000, \
      0.88531748708681257121, \
      0.00000000000000000000, \
     -0.88531748708681257121, \
      0.48884754503841615358, \
      0.48884754503841615358, \
     -0.48884754503841615358, \
     -0.48884754503841615358, \
      0.45031772456672747307, \
      0.45031772456672747307, \
     -0.45031772456672747307, \
     -0.45031772456672747307, \
      0.65872956915547864476, \
      0.65872956915547864476, \
     -0.65872956915547864476, \
     -0.65872956915547864476, \
      0.62588271911798842861, \
      0.62588271911798842861, \
     -0.62588271911798842861, \
     -0.62588271911798842861, \
      0.25178960033193620305, \
      0.25178960033193620305, \
     -0.25178960033193620305, \
     -0.25178960033193620305, \
      0.91338191280449132492, \
      0.91338191280449132492, \
     -0.91338191280449132492, \
     -0.91338191280449132492, \
      0.11117861641720541699, \
      0.11117861641720541699, \
     -0.11117861641720541699, \
     -0.11117861641720541699, \
      0.37814924987375336807, \
      0.37814924987375336807, \
     -0.37814924987375336807, \
     -0.37814924987375336807, \
      0.23146195691577758913, \
      0.23146195691577758913, \
     -0.23146195691577758913, \
     -0.23146195691577758913, \
      0.18598667282576661353, \
      0.18598667282576661353, \
     -0.18598667282576661353, \
     -0.18598667282576661353, \
      0.72941490542892961635, \
      0.72941490542892961635, \
     -0.72941490542892961635, \
     -0.72941490542892961635, \
      0.80419241777926819825, \
      0.80419241777926819825, \
     -0.80419241777926819825, \
     -0.80419241777926819825, \
      0.47036082838417470064, \
      0.47036082838417470064, \
     -0.47036082838417470064, \
     -0.47036082838417470064, \
      0.27535657520011547206, \
      0.27535657520011547206, \
     -0.27535657520011547206, \
     -0.27535657520011547206, \
      0.25840443662578793660, \
      0.25840443662578793660, \
     -0.25840443662578793660, \
     -0.25840443662578793660, \
      0.43978938971942055369, \
      0.77456301686419115615, \
      0.43978938971942055369, \
     -0.77456301686419115615, \
     -0.43978938971942055369, \
      0.77456301686419115615, \
     -0.43978938971942055369, \
     -0.77456301686419115615, \
      0.22174790443082656455, \
      0.72014146551340840752, \
      0.22174790443082656455, \
     -0.72014146551340840752, \
     -0.22174790443082656455, \
      0.72014146551340840752, \
     -0.22174790443082656455, \
     -0.72014146551340840752, \
      0.58560797514860796209, \
      0.17509849556381359981, \
      0.58560797514860796209, \
     -0.17509849556381359981, \
     -0.58560797514860796209, \
      0.17509849556381359981, \
     -0.58560797514860796209, \
     -0.17509849556381359981, \
      0.73982675325131319610, \
      0.93762547318055500245, \
      0.73982675325131319610, \
     -0.93762547318055500245, \
     -0.73982675325131319610, \
      0.93762547318055500245, \
     -0.73982675325131319610, \
     -0.93762547318055500245, \
      0.50002093145521131490, \
      0.92588822421370353677, \
      0.50002093145521131490, \
     -0.92588822421370353677, \
     -0.50002093145521131490, \
      0.92588822421370353677, \
     -0.50002093145521131490, \
     -0.92588822421370353677, \
      0.56185198689199644662, \
      0.26820739210416322251, \
      0.56185198689199644662, \
     -0.26820739210416322251, \
     -0.56185198689199644662, \
      0.26820739210416322251, \
     -0.56185198689199644662, \
     -0.26820739210416322251, \
      0.79245628070986395830, \
      0.36207959439737902319, \
      0.79245628070986395830, \
     -0.36207959439737902319, \
     -0.79245628070986395830, \
      0.36207959439737902319, \
     -0.79245628070986395830, \
     -0.36207959439737902319 ] )

  z = np.array ( [ \
      0.92974005864256004106, \
      0.58387036044479012631, \
      0.10942458150673148309, \
      0.30043598129646631456, \
      0.40351765144169587929, \
      0.40351765144169587929, \
      0.40351765144169587929, \
      0.40351765144169587929, \
      0.00554139647030791119, \
      0.00554139647030791119, \
      0.00554139647030791119, \
      0.00554139647030791119, \
      0.84979294403286831372, \
      0.84979294403286831372, \
      0.84979294403286831372, \
      0.84979294403286831372, \
      0.60719504362173426504, \
      0.60719504362173426504, \
      0.60719504362173426504, \
      0.60719504362173426504, \
      0.02033792783786766978, \
      0.02033792783786766978, \
      0.02033792783786766978, \
      0.02033792783786766978, \
      0.10601199873730246526, \
      0.10601199873730246526, \
      0.10601199873730246526, \
      0.10601199873730246526, \
      0.24910419915320258788, \
      0.24910419915320258788, \
      0.24910419915320258788, \
      0.24910419915320258788, \
      0.08107956240970674855, \
      0.08107956240970674855, \
      0.08107956240970674855, \
      0.08107956240970674855, \
      0.00950815168106079051, \
      0.00950815168106079051, \
      0.00950815168106079051, \
      0.00950815168106079051, \
      0.48819360509214093646, \
      0.48819360509214093646, \
      0.48819360509214093646, \
      0.48819360509214093646, \
      0.27690831156608641805, \
      0.27690831156608641805, \
      0.27690831156608641805, \
      0.27690831156608641805, \
      0.12248093820428122835, \
      0.12248093820428122835, \
      0.12248093820428122835, \
      0.12248093820428122835, \
      0.22323057279864513824, \
      0.22323057279864513824, \
      0.22323057279864513824, \
      0.22323057279864513824, \
      0.01207165002118426068, \
      0.01207165002118426068, \
      0.01207165002118426068, \
      0.01207165002118426068, \
      0.75518724716690510679, \
      0.75518724716690510679, \
      0.75518724716690510679, \
      0.75518724716690510679, \
      0.08424825204838617965, \
      0.08424825204838617965, \
      0.08424825204838617965, \
      0.08424825204838617965, \
      0.63188577231776799081, \
      0.63188577231776799081, \
      0.63188577231776799081, \
      0.63188577231776799081, \
      0.39892977659234107879, \
      0.39892977659234107879, \
      0.39892977659234107879, \
      0.39892977659234107879, \
      0.02502635713295603415, \
      0.02502635713295603415, \
      0.02502635713295603415, \
      0.02502635713295603415, \
      0.12038000765135539738, \
      0.12038000765135539738, \
      0.12038000765135539738, \
      0.12038000765135539738, \
      0.29270359357039776871, \
      0.29270359357039776871, \
      0.29270359357039776871, \
      0.29270359357039776871, \
      0.70742748921558806785, \
      0.70742748921558806785, \
      0.70742748921558806785, \
      0.70742748921558806785, \
      0.52832746509410000169, \
      0.52832746509410000169, \
      0.52832746509410000169, \
      0.52832746509410000169, \
      0.19538409012904675577, \
      0.19538409012904675577, \
      0.19538409012904675577, \
      0.19538409012904675577, \
      0.19538409012904675577, \
      0.19538409012904675577, \
      0.19538409012904675577, \
      0.19538409012904675577, \
      0.02260035188498128386, \
      0.02260035188498128386, \
      0.02260035188498128386, \
      0.02260035188498128386, \
      0.02260035188498128386, \
      0.02260035188498128386, \
      0.02260035188498128386, \
      0.02260035188498128386, \
      0.21608520533637087802, \
      0.21608520533637087802, \
      0.21608520533637087802, \
      0.21608520533637087802, \
      0.21608520533637087802, \
      0.21608520533637087802, \
      0.21608520533637087802, \
      0.21608520533637087802, \
      0.06232437306564607427, \
      0.06232437306564607427, \
      0.06232437306564607427, \
      0.06232437306564607427, \
      0.06232437306564607427, \
      0.06232437306564607427, \
      0.06232437306564607427, \
      0.06232437306564607427, \
      0.01929314718254383776, \
      0.01929314718254383776, \
      0.01929314718254383776, \
      0.01929314718254383776, \
      0.01929314718254383776, \
      0.01929314718254383776, \
      0.01929314718254383776, \
      0.01929314718254383776, \
      0.40102466550487736452, \
      0.40102466550487736452, \
      0.40102466550487736452, \
      0.40102466550487736452, \
      0.40102466550487736452, \
      0.40102466550487736452, \
      0.40102466550487736452, \
      0.40102466550487736452, \
      0.09200529105614789482, \
      0.09200529105614789482, \
      0.09200529105614789482, \
      0.09200529105614789482, \
      0.09200529105614789482, \
      0.09200529105614789482, \
      0.09200529105614789482, \
      0.09200529105614789482 ] )

  w= np.array ( [ \
      0.00120366956557754735, \
      0.01890734566258640142, \
      0.02412883548353303431, \
      0.01430958560741040810, \
      0.01462233467606358257, \
      0.01462233467606358257, \
      0.01462233467606358257, \
      0.01462233467606358257, \
      0.00131047133506746131, \
      0.00131047133506746131, \
      0.00131047133506746131, \
      0.00131047133506746131, \
      0.00131534859459711507, \
      0.00131534859459711507, \
      0.00131534859459711507, \
      0.00131534859459711507, \
      0.00604172938779333306, \
      0.00604172938779333306, \
      0.00604172938779333306, \
      0.00604172938779333306, \
      0.00828934369195859742, \
      0.00828934369195859742, \
      0.00828934369195859742, \
      0.00828934369195859742, \
      0.01293341373858935758, \
      0.01293341373858935758, \
      0.01293341373858935758, \
      0.01293341373858935758, \
      0.00563885419154383245, \
      0.00563885419154383245, \
      0.00563885419154383245, \
      0.00563885419154383245, \
      0.00450499139881360439, \
      0.00450499139881360439, \
      0.00450499139881360439, \
      0.00450499139881360439, \
      0.00363618420610894565, \
      0.00363618420610894565, \
      0.00363618420610894565, \
      0.00363618420610894565, \
      0.00388842116802182820, \
      0.00388842116802182820, \
      0.00388842116802182820, \
      0.00388842116802182820, \
      0.00402365320826360111, \
      0.00402365320826360111, \
      0.00402365320826360111, \
      0.00402365320826360111, \
      0.00955901949244871221, \
      0.00955901949244871221, \
      0.00955901949244871221, \
      0.00955901949244871221, \
      0.01938656716858040696, \
      0.01938656716858040696, \
      0.01938656716858040696, \
      0.01938656716858040696, \
      0.00096875488373819618, \
      0.00096875488373819618, \
      0.00096875488373819618, \
      0.00096875488373819618, \
      0.00502214350286199571, \
      0.00502214350286199571, \
      0.00502214350286199571, \
      0.00502214350286199571, \
      0.01448769412031481602, \
      0.01448769412031481602, \
      0.01448769412031481602, \
      0.01448769412031481602, \
      0.00459976431383042356, \
      0.00459976431383042356, \
      0.00459976431383042356, \
      0.00459976431383042356, \
      0.01107636061349879207, \
      0.01107636061349879207, \
      0.01107636061349879207, \
      0.01107636061349879207, \
      0.00469260200432727610, \
      0.00469260200432727610, \
      0.00469260200432727610, \
      0.00469260200432727610, \
      0.00285194982449880072, \
      0.00285194982449880072, \
      0.00285194982449880072, \
      0.00285194982449880072, \
      0.01323033835935080553, \
      0.01323033835935080553, \
      0.01323033835935080553, \
      0.01323033835935080553, \
      0.00111972343972882474, \
      0.00111972343972882474, \
      0.00111972343972882474, \
      0.00111972343972882474, \
      0.00918246462138119605, \
      0.00918246462138119605, \
      0.00918246462138119605, \
      0.00918246462138119605, \
      0.00456490653701050169, \
      0.00456490653701050169, \
      0.00456490653701050169, \
      0.00456490653701050169, \
      0.00456490653701050169, \
      0.00456490653701050169, \
      0.00456490653701050169, \
      0.00456490653701050169, \
      0.00547503483442879964, \
      0.00547503483442879964, \
      0.00547503483442879964, \
      0.00547503483442879964, \
      0.00547503483442879964, \
      0.00547503483442879964, \
      0.00547503483442879964, \
      0.00547503483442879964, \
      0.00992261207645742799, \
      0.00992261207645742799, \
      0.00992261207645742799, \
      0.00992261207645742799, \
      0.00992261207645742799, \
      0.00992261207645742799, \
      0.00992261207645742799, \
      0.00992261207645742799, \
      0.00110382912156457261, \
      0.00110382912156457261, \
      0.00110382912156457261, \
      0.00110382912156457261, \
      0.00110382912156457261, \
      0.00110382912156457261, \
      0.00110382912156457261, \
      0.00110382912156457261, \
      0.00236228293958670472, \
      0.00236228293958670472, \
      0.00236228293958670472, \
      0.00236228293958670472, \
      0.00236228293958670472, \
      0.00236228293958670472, \
      0.00236228293958670472, \
      0.00236228293958670472, \
      0.00630666584934871672, \
      0.00630666584934871672, \
      0.00630666584934871672, \
      0.00630666584934871672, \
      0.00630666584934871672, \
      0.00630666584934871672, \
      0.00630666584934871672, \
      0.00630666584934871672, \
      0.00675492513102409885, \
      0.00675492513102409885, \
      0.00675492513102409885, \
      0.00675492513102409885, \
      0.00675492513102409885, \
      0.00675492513102409885, \
      0.00675492513102409885, \
      0.00675492513102409885 ] )

  return x, y, z, w

def rule14 ( ):

#*****************************************************************************80
#
## rule14() returns the pyramid quadrature rule of precision 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.42182613673485974681, \
      0.00000000000000000000, \
     -0.42182613673485974681, \
      0.00000000000000000000, \
      0.08465613435886885918, \
      0.00000000000000000000, \
     -0.08465613435886885918, \
      0.00000000000000000000, \
      0.95167131965923157377, \
      0.00000000000000000000, \
     -0.95167131965923157377, \
      0.00000000000000000000, \
      0.12212881781145627780, \
      0.00000000000000000000, \
     -0.12212881781145627780, \
      0.00000000000000000000, \
      0.34597557868730360875, \
      0.00000000000000000000, \
     -0.34597557868730360875, \
      0.00000000000000000000, \
      0.32500209212470398956, \
      0.00000000000000000000, \
     -0.32500209212470398956, \
      0.00000000000000000000, \
      0.85274656175184737616, \
      0.00000000000000000000, \
     -0.85274656175184737616, \
      0.00000000000000000000, \
      0.63827756477152641779, \
      0.00000000000000000000, \
     -0.63827756477152641779, \
      0.00000000000000000000, \
      0.67231147414585012978, \
      0.00000000000000000000, \
     -0.67231147414585012978, \
      0.00000000000000000000, \
      0.85374960595109017358, \
      0.00000000000000000000, \
     -0.85374960595109017358, \
      0.00000000000000000000, \
      0.32351828528149095821, \
      0.00000000000000000000, \
     -0.32351828528149095821, \
      0.00000000000000000000, \
      0.49697514832376565863, \
      0.00000000000000000000, \
     -0.49697514832376565863, \
      0.00000000000000000000, \
      0.50417062955844949013, \
     -0.50417062955844949013, \
      0.50417062955844949013, \
     -0.50417062955844949013, \
      0.63853202881303905425, \
     -0.63853202881303905425, \
      0.63853202881303905425, \
     -0.63853202881303905425, \
      0.76432244824860651189, \
     -0.76432244824860651189, \
      0.76432244824860651189, \
     -0.76432244824860651189, \
      0.56133306193833287789, \
     -0.56133306193833287789, \
      0.56133306193833287789, \
     -0.56133306193833287789, \
      0.28786805395155073972, \
     -0.28786805395155073972, \
      0.28786805395155073972, \
     -0.28786805395155073972, \
      0.90163083827576329110, \
     -0.90163083827576329110, \
      0.90163083827576329110, \
     -0.90163083827576329110, \
      0.09459747575878657555, \
     -0.09459747575878657555, \
      0.09459747575878657555, \
     -0.09459747575878657555, \
      0.26275744057316757774, \
     -0.26275744057316757774, \
      0.26275744057316757774, \
     -0.26275744057316757774, \
      0.38640915363814193340, \
     -0.38640915363814193340, \
      0.38640915363814193340, \
     -0.38640915363814193340, \
      0.22823005779855418118, \
     -0.22823005779855418118, \
      0.22823005779855418118, \
     -0.22823005779855418118, \
      0.70578722692835427210, \
     -0.70578722692835427210, \
      0.70578722692835427210, \
     -0.70578722692835427210, \
      0.91478755244276455105, \
     -0.91478755244276455105, \
      0.91478755244276455105, \
     -0.91478755244276455105, \
      0.50883064513682729757, \
     -0.50883064513682729757, \
      0.50883064513682729757, \
     -0.50883064513682729757, \
      0.21833905510549736495, \
     -0.21833905510549736495, \
      0.21833905510549736495, \
     -0.21833905510549736495, \
      0.20524210043072979581, \
     -0.20524210043072979581, \
      0.20524210043072979581, \
     -0.20524210043072979581, \
      0.29109013901653718603, \
     -0.29109013901653718603, \
      0.29109013901653718603, \
     -0.29109013901653718603, \
      0.74865402480464293689, \
     -0.74865402480464293689, \
      0.74865402480464293689, \
     -0.74865402480464293689, \
      0.73782464660583058080, \
      0.49284956480916058963, \
     -0.73782464660583058080, \
      0.49284956480916058963, \
      0.73782464660583058080, \
     -0.49284956480916058963, \
     -0.73782464660583058080, \
     -0.49284956480916058963, \
      0.85890606200982022589, \
      0.37381968226304934655, \
     -0.85890606200982022589, \
      0.37381968226304934655, \
      0.85890606200982022589, \
     -0.37381968226304934655, \
     -0.85890606200982022589, \
     -0.37381968226304934655, \
      0.22436150649227576404, \
      0.63179494567048766207, \
     -0.22436150649227576404, \
      0.63179494567048766207, \
      0.22436150649227576404, \
     -0.63179494567048766207, \
     -0.22436150649227576404, \
     -0.63179494567048766207, \
      0.90017577589364738966, \
      0.62618678850176523465, \
     -0.90017577589364738966, \
      0.62618678850176523465, \
      0.90017577589364738966, \
     -0.62618678850176523465, \
     -0.90017577589364738966, \
     -0.62618678850176523465, \
      0.97895018498408203911, \
      0.62565783993238355265, \
     -0.97895018498408203911, \
      0.62565783993238355265, \
      0.97895018498408203911, \
     -0.62565783993238355265, \
     -0.97895018498408203911, \
     -0.62565783993238355265, \
      0.25607583733637889756, \
      0.51194810665765877467, \
     -0.25607583733637889756, \
      0.51194810665765877467, \
      0.25607583733637889756, \
     -0.51194810665765877467, \
     -0.25607583733637889756, \
     -0.51194810665765877467, \
      0.29741762068713811784, \
      0.77553958650832321986, \
     -0.29741762068713811784, \
      0.77553958650832321986, \
      0.29741762068713811784, \
     -0.77553958650832321986, \
     -0.29741762068713811784, \
     -0.77553958650832321986, \
      0.29079659566096877077, \
      0.61926152278826551711, \
     -0.29079659566096877077, \
      0.61926152278826551711, \
      0.29079659566096877077, \
     -0.61926152278826551711, \
     -0.29079659566096877077, \
     -0.61926152278826551711 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.42182613673485974681, \
      0.00000000000000000000, \
     -0.42182613673485974681, \
      0.00000000000000000000, \
      0.08465613435886885918, \
      0.00000000000000000000, \
     -0.08465613435886885918, \
      0.00000000000000000000, \
      0.95167131965923157377, \
      0.00000000000000000000, \
     -0.95167131965923157377, \
      0.00000000000000000000, \
      0.12212881781145627780, \
      0.00000000000000000000, \
     -0.12212881781145627780, \
      0.00000000000000000000, \
      0.34597557868730360875, \
      0.00000000000000000000, \
     -0.34597557868730360875, \
      0.00000000000000000000, \
      0.32500209212470398956, \
      0.00000000000000000000, \
     -0.32500209212470398956, \
      0.00000000000000000000, \
      0.85274656175184737616, \
      0.00000000000000000000, \
     -0.85274656175184737616, \
      0.00000000000000000000, \
      0.63827756477152641779, \
      0.00000000000000000000, \
     -0.63827756477152641779, \
      0.00000000000000000000, \
      0.67231147414585012978, \
      0.00000000000000000000, \
     -0.67231147414585012978, \
      0.00000000000000000000, \
      0.85374960595109017358, \
      0.00000000000000000000, \
     -0.85374960595109017358, \
      0.00000000000000000000, \
      0.32351828528149095821, \
      0.00000000000000000000, \
     -0.32351828528149095821, \
      0.00000000000000000000, \
      0.49697514832376565863, \
      0.00000000000000000000, \
     -0.49697514832376565863, \
      0.50417062955844949013, \
      0.50417062955844949013, \
     -0.50417062955844949013, \
     -0.50417062955844949013, \
      0.63853202881303905425, \
      0.63853202881303905425, \
     -0.63853202881303905425, \
     -0.63853202881303905425, \
      0.76432244824860651189, \
      0.76432244824860651189, \
     -0.76432244824860651189, \
     -0.76432244824860651189, \
      0.56133306193833287789, \
      0.56133306193833287789, \
     -0.56133306193833287789, \
     -0.56133306193833287789, \
      0.28786805395155073972, \
      0.28786805395155073972, \
     -0.28786805395155073972, \
     -0.28786805395155073972, \
      0.90163083827576329110, \
      0.90163083827576329110, \
     -0.90163083827576329110, \
     -0.90163083827576329110, \
      0.09459747575878657555, \
      0.09459747575878657555, \
     -0.09459747575878657555, \
     -0.09459747575878657555, \
      0.26275744057316757774, \
      0.26275744057316757774, \
     -0.26275744057316757774, \
     -0.26275744057316757774, \
      0.38640915363814193340, \
      0.38640915363814193340, \
     -0.38640915363814193340, \
     -0.38640915363814193340, \
      0.22823005779855418118, \
      0.22823005779855418118, \
     -0.22823005779855418118, \
     -0.22823005779855418118, \
      0.70578722692835427210, \
      0.70578722692835427210, \
     -0.70578722692835427210, \
     -0.70578722692835427210, \
      0.91478755244276455105, \
      0.91478755244276455105, \
     -0.91478755244276455105, \
     -0.91478755244276455105, \
      0.50883064513682729757, \
      0.50883064513682729757, \
     -0.50883064513682729757, \
     -0.50883064513682729757, \
      0.21833905510549736495, \
      0.21833905510549736495, \
     -0.21833905510549736495, \
     -0.21833905510549736495, \
      0.20524210043072979581, \
      0.20524210043072979581, \
     -0.20524210043072979581, \
     -0.20524210043072979581, \
      0.29109013901653718603, \
      0.29109013901653718603, \
     -0.29109013901653718603, \
     -0.29109013901653718603, \
      0.74865402480464293689, \
      0.74865402480464293689, \
     -0.74865402480464293689, \
     -0.74865402480464293689, \
      0.49284956480916058963, \
      0.73782464660583058080, \
      0.49284956480916058963, \
     -0.73782464660583058080, \
     -0.49284956480916058963, \
      0.73782464660583058080, \
     -0.49284956480916058963, \
     -0.73782464660583058080, \
      0.37381968226304934655, \
      0.85890606200982022589, \
      0.37381968226304934655, \
     -0.85890606200982022589, \
     -0.37381968226304934655, \
      0.85890606200982022589, \
     -0.37381968226304934655, \
     -0.85890606200982022589, \
      0.63179494567048766207, \
      0.22436150649227576404, \
      0.63179494567048766207, \
     -0.22436150649227576404, \
     -0.63179494567048766207, \
      0.22436150649227576404, \
     -0.63179494567048766207, \
     -0.22436150649227576404, \
      0.62618678850176523465, \
      0.90017577589364738966, \
      0.62618678850176523465, \
     -0.90017577589364738966, \
     -0.62618678850176523465, \
      0.90017577589364738966, \
     -0.62618678850176523465, \
     -0.90017577589364738966, \
      0.62565783993238355265, \
      0.97895018498408203911, \
      0.62565783993238355265, \
     -0.97895018498408203911, \
     -0.62565783993238355265, \
      0.97895018498408203911, \
     -0.62565783993238355265, \
     -0.97895018498408203911, \
      0.51194810665765877467, \
      0.25607583733637889756, \
      0.51194810665765877467, \
     -0.25607583733637889756, \
     -0.51194810665765877467, \
      0.25607583733637889756, \
     -0.51194810665765877467, \
     -0.25607583733637889756, \
      0.77553958650832321986, \
      0.29741762068713811784, \
      0.77553958650832321986, \
     -0.29741762068713811784, \
     -0.77553958650832321986, \
      0.29741762068713811784, \
     -0.77553958650832321986, \
     -0.29741762068713811784, \
      0.61926152278826551711, \
      0.29079659566096877077, \
      0.61926152278826551711, \
     -0.29079659566096877077, \
     -0.61926152278826551711, \
      0.29079659566096877077, \
     -0.61926152278826551711, \
     -0.29079659566096877077 ] )

  z = np.array ( [ \
      0.94550960783801574205, \
      0.61382435648399280570, \
      0.24540497180596210214, \
      0.41832825390859845749, \
      0.40175363160567706400, \
      0.40175363160567706400, \
      0.40175363160567706400, \
      0.40175363160567706400, \
      0.08958821481037450296, \
      0.08958821481037450296, \
      0.08958821481037450296, \
      0.08958821481037450296, \
      0.03128290548598175458, \
      0.03128290548598175458, \
      0.03128290548598175458, \
      0.03128290548598175458, \
      0.86562635222401107526, \
      0.86562635222401107526, \
      0.86562635222401107526, \
      0.86562635222401107526, \
      0.56154915636029745230, \
      0.56154915636029745230, \
      0.56154915636029745230, \
      0.56154915636029745230, \
      0.01398939848661482320, \
      0.01398939848661482320, \
      0.01398939848661482320, \
      0.01398939848661482320, \
      0.00165571829628404746, \
      0.00165571829628404746, \
      0.00165571829628404746, \
      0.00165571829628404746, \
      0.06493816225859559699, \
      0.06493816225859559699, \
      0.06493816225859559699, \
      0.06493816225859559699, \
      0.32265244995852410126, \
      0.32265244995852410126, \
      0.32265244995852410126, \
      0.32265244995852410126, \
      0.14284602353229125526, \
      0.14284602353229125526, \
      0.14284602353229125526, \
      0.14284602353229125526, \
      0.66509821819012426847, \
      0.66509821819012426847, \
      0.66509821819012426847, \
      0.66509821819012426847, \
      0.19278467665636450645, \
      0.19278467665636450645, \
      0.19278467665636450645, \
      0.19278467665636450645, \
      0.05324772752904030626, \
      0.05324772752904030626, \
      0.05324772752904030626, \
      0.05324772752904030626, \
      0.34999224799132661046, \
      0.34999224799132661046, \
      0.34999224799132661046, \
      0.34999224799132661046, \
      0.16096112315804175785, \
      0.16096112315804175785, \
      0.16096112315804175785, \
      0.16096112315804175785, \
      0.16039988924094228384, \
      0.16039988924094228384, \
      0.16039988924094228384, \
      0.16039988924094228384, \
      0.13732763905737063737, \
      0.13732763905737063737, \
      0.13732763905737063737, \
      0.13732763905737063737, \
      0.01032358209500776509, \
      0.01032358209500776509, \
      0.01032358209500776509, \
      0.01032358209500776509, \
      0.76779179416407739023, \
      0.76779179416407739023, \
      0.76779179416407739023, \
      0.76779179416407739023, \
      0.04943554173327800727, \
      0.04943554173327800727, \
      0.04943554173327800727, \
      0.04943554173327800727, \
      0.55602661412166731747, \
      0.55602661412166731747, \
      0.55602661412166731747, \
      0.55602661412166731747, \
      0.49627919975552486909, \
      0.49627919975552486909, \
      0.49627919975552486909, \
      0.49627919975552486909, \
      0.00200880715410161345, \
      0.00200880715410161345, \
      0.00200880715410161345, \
      0.00200880715410161345, \
      0.04956231677804342345, \
      0.04956231677804342345, \
      0.04956231677804342345, \
      0.04956231677804342345, \
      0.34635586968731740809, \
      0.34635586968731740809, \
      0.34635586968731740809, \
      0.34635586968731740809, \
      0.74542883631057244020, \
      0.74542883631057244020, \
      0.74542883631057244020, \
      0.74542883631057244020, \
      0.64153164712892607469, \
      0.64153164712892607469, \
      0.64153164712892607469, \
      0.64153164712892607469, \
      0.30622738335271937338, \
      0.30622738335271937338, \
      0.30622738335271937338, \
      0.30622738335271937338, \
      0.04936880562940795109, \
      0.04936880562940795109, \
      0.04936880562940795109, \
      0.04936880562940795109, \
      0.23699400699902964385, \
      0.23699400699902964385, \
      0.23699400699902964385, \
      0.23699400699902964385, \
      0.23699400699902964385, \
      0.23699400699902964385, \
      0.23699400699902964385, \
      0.23699400699902964385, \
      0.02776225858911670133, \
      0.02776225858911670133, \
      0.02776225858911670133, \
      0.02776225858911670133, \
      0.02776225858911670133, \
      0.02776225858911670133, \
      0.02776225858911670133, \
      0.02776225858911670133, \
      0.25928305502878512545, \
      0.25928305502878512545, \
      0.25928305502878512545, \
      0.25928305502878512545, \
      0.25928305502878512545, \
      0.25928305502878512545, \
      0.25928305502878512545, \
      0.25928305502878512545, \
      0.07806621986847779582, \
      0.07806621986847779582, \
      0.07806621986847779582, \
      0.07806621986847779582, \
      0.07806621986847779582, \
      0.07806621986847779582, \
      0.07806621986847779582, \
      0.07806621986847779582, \
      0.00443001451925785755, \
      0.00443001451925785755, \
      0.00443001451925785755, \
      0.00443001451925785755, \
      0.00443001451925785755, \
      0.00443001451925785755, \
      0.00443001451925785755, \
      0.00443001451925785755, \
      0.45428572768859826203, \
      0.45428572768859826203, \
      0.45428572768859826203, \
      0.45428572768859826203, \
      0.45428572768859826203, \
      0.45428572768859826203, \
      0.45428572768859826203, \
      0.45428572768859826203, \
      0.11761104673332581361, \
      0.11761104673332581361, \
      0.11761104673332581361, \
      0.11761104673332581361, \
      0.11761104673332581361, \
      0.11761104673332581361, \
      0.11761104673332581361, \
      0.11761104673332581361, \
      0.00783483739567485994, \
      0.00783483739567485994, \
      0.00783483739567485994, \
      0.00783483739567485994, \
      0.00783483739567485994, \
      0.00783483739567485994, \
      0.00783483739567485994, \
      0.00783483739567485994 ] )

  w= np.array ( [ \
      0.00060098284109148011, \
      0.01255487583666288487, \
      0.02319377258130698310, \
      0.01905556551345680832, \
      0.01191795956205729361, \
      0.01191795956205729361, \
      0.01191795956205729361, \
      0.01191795956205729361, \
      0.00386718441233280599, \
      0.00386718441233280599, \
      0.00386718441233280599, \
      0.00386718441233280599, \
      0.00192376309517474221, \
      0.00192376309517474221, \
      0.00192376309517474221, \
      0.00192376309517474221, \
      0.00123417980449306002, \
      0.00123417980449306002, \
      0.00123417980449306002, \
      0.00123417980449306002, \
      0.00471664803911589926, \
      0.00471664803911589926, \
      0.00471664803911589926, \
      0.00471664803911589926, \
      0.00513404497338453437, \
      0.00513404497338453437, \
      0.00513404497338453437, \
      0.00513404497338453437, \
      0.00115456474640818034, \
      0.00115456474640818034, \
      0.00115456474640818034, \
      0.00115456474640818034, \
      0.01181264118995303640, \
      0.01181264118995303640, \
      0.01181264118995303640, \
      0.01181264118995303640, \
      0.00243693783463101070, \
      0.00243693783463101070, \
      0.00243693783463101070, \
      0.00243693783463101070, \
      0.00244218039395145909, \
      0.00244218039395145909, \
      0.00244218039395145909, \
      0.00244218039395145909, \
      0.00276027206518877129, \
      0.00276027206518877129, \
      0.00276027206518877129, \
      0.00276027206518877129, \
      0.01491875937488000743, \
      0.01491875937488000743, \
      0.01491875937488000743, \
      0.01491875937488000743, \
      0.00860788548052002223, \
      0.00860788548052002223, \
      0.00860788548052002223, \
      0.00860788548052002223, \
      0.00092010540262242146, \
      0.00092010540262242146, \
      0.00092010540262242146, \
      0.00092010540262242146, \
      0.00350658071335885509, \
      0.00350658071335885509, \
      0.00350658071335885509, \
      0.00350658071335885509, \
      0.01184517921997258437, \
      0.01184517921997258437, \
      0.01184517921997258437, \
      0.01184517921997258437, \
      0.01517200950119655840, \
      0.01517200950119655840, \
      0.01517200950119655840, \
      0.01517200950119655840, \
      0.00079885709646654790, \
      0.00079885709646654790, \
      0.00079885709646654790, \
      0.00079885709646654790, \
      0.00346532205672137571, \
      0.00346532205672137571, \
      0.00346532205672137571, \
      0.00346532205672137571, \
      0.00564901752891650531, \
      0.00564901752891650531, \
      0.00564901752891650531, \
      0.00564901752891650531, \
      0.00314499257654337911, \
      0.00314499257654337911, \
      0.00314499257654337911, \
      0.00314499257654337911, \
      0.01042467052306092316, \
      0.01042467052306092316, \
      0.01042467052306092316, \
      0.01042467052306092316, \
      0.00135335334419937545, \
      0.00135335334419937545, \
      0.00135335334419937545, \
      0.00135335334419937545, \
      0.00068639460491782677, \
      0.00068639460491782677, \
      0.00068639460491782677, \
      0.00068639460491782677, \
      0.00848846646315219895, \
      0.00848846646315219895, \
      0.00848846646315219895, \
      0.00848846646315219895, \
      0.00138976471399791693, \
      0.00138976471399791693, \
      0.00138976471399791693, \
      0.00138976471399791693, \
      0.00564687172166134736, \
      0.00564687172166134736, \
      0.00564687172166134736, \
      0.00564687172166134736, \
      0.01822286920356053219, \
      0.01822286920356053219, \
      0.01822286920356053219, \
      0.01822286920356053219, \
      0.00475553584446375757, \
      0.00475553584446375757, \
      0.00475553584446375757, \
      0.00475553584446375757, \
      0.00330839378673254258, \
      0.00330839378673254258, \
      0.00330839378673254258, \
      0.00330839378673254258, \
      0.00330839378673254258, \
      0.00330839378673254258, \
      0.00330839378673254258, \
      0.00330839378673254258, \
      0.00407004510316002176, \
      0.00407004510316002176, \
      0.00407004510316002176, \
      0.00407004510316002176, \
      0.00407004510316002176, \
      0.00407004510316002176, \
      0.00407004510316002176, \
      0.00407004510316002176, \
      0.00826848930450256592, \
      0.00826848930450256592, \
      0.00826848930450256592, \
      0.00826848930450256592, \
      0.00826848930450256592, \
      0.00826848930450256592, \
      0.00826848930450256592, \
      0.00826848930450256592, \
      0.00222137881102773540, \
      0.00222137881102773540, \
      0.00222137881102773540, \
      0.00222137881102773540, \
      0.00222137881102773540, \
      0.00222137881102773540, \
      0.00222137881102773540, \
      0.00222137881102773540, \
      0.00053414917220099471, \
      0.00053414917220099471, \
      0.00053414917220099471, \
      0.00053414917220099471, \
      0.00053414917220099471, \
      0.00053414917220099471, \
      0.00053414917220099471, \
      0.00053414917220099471, \
      0.00487946234737815943, \
      0.00487946234737815943, \
      0.00487946234737815943, \
      0.00487946234737815943, \
      0.00487946234737815943, \
      0.00487946234737815943, \
      0.00487946234737815943, \
      0.00487946234737815943, \
      0.00789729756886463005, \
      0.00789729756886463005, \
      0.00789729756886463005, \
      0.00789729756886463005, \
      0.00789729756886463005, \
      0.00789729756886463005, \
      0.00789729756886463005, \
      0.00789729756886463005, \
      0.00269662856611711495, \
      0.00269662856611711495, \
      0.00269662856611711495, \
      0.00269662856611711495, \
      0.00269662856611711495, \
      0.00269662856611711495, \
      0.00269662856611711495, \
      0.00269662856611711495 ] )

  return x, y, z, w

def rule15 ( ):

#*****************************************************************************80
#
## rule15() returns the pyramid quadrature rule of precision 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.70014035742397184858, \
      0.00000000000000000000, \
     -0.70014035742397184858, \
      0.00000000000000000000, \
      0.91936314848339839578, \
      0.00000000000000000000, \
     -0.91936314848339839578, \
      0.00000000000000000000, \
      0.11013348894423610758, \
      0.00000000000000000000, \
     -0.11013348894423610758, \
      0.00000000000000000000, \
      0.44650085670154981976, \
      0.00000000000000000000, \
     -0.44650085670154981976, \
      0.00000000000000000000, \
      0.80205385758014868802, \
      0.00000000000000000000, \
     -0.80205385758014868802, \
      0.00000000000000000000, \
      0.53015124527324641868, \
      0.00000000000000000000, \
     -0.53015124527324641868, \
      0.00000000000000000000, \
      0.97322734428927526462, \
      0.00000000000000000000, \
     -0.97322734428927526462, \
      0.00000000000000000000, \
      0.50557186634064188446, \
      0.00000000000000000000, \
     -0.50557186634064188446, \
      0.00000000000000000000, \
      0.04618938260051261985, \
      0.00000000000000000000, \
     -0.04618938260051261985, \
      0.00000000000000000000, \
      0.62301364063828001960, \
      0.00000000000000000000, \
     -0.62301364063828001960, \
      0.00000000000000000000, \
      0.29509310458272342004, \
      0.00000000000000000000, \
     -0.29509310458272342004, \
      0.00000000000000000000, \
      0.47760058576112396356, \
      0.00000000000000000000, \
     -0.47760058576112396356, \
      0.00000000000000000000, \
      0.36898015805621120489, \
      0.00000000000000000000, \
     -0.36898015805621120489, \
      0.00000000000000000000, \
      0.37237829048305948199, \
     -0.37237829048305948199, \
      0.37237829048305948199, \
     -0.37237829048305948199, \
      0.53419020022883723087, \
     -0.53419020022883723087, \
      0.53419020022883723087, \
     -0.53419020022883723087, \
      0.06063808134784291065, \
     -0.06063808134784291065, \
      0.06063808134784291065, \
     -0.06063808134784291065, \
      0.47770687706587527943, \
     -0.47770687706587527943, \
      0.47770687706587527943, \
     -0.47770687706587527943, \
      0.19875431205737298379, \
     -0.19875431205737298379, \
      0.19875431205737298379, \
     -0.19875431205737298379, \
      0.75996956110375202265, \
     -0.75996956110375202265, \
      0.75996956110375202265, \
     -0.75996956110375202265, \
      0.50554584202664287762, \
     -0.50554584202664287762, \
      0.50554584202664287762, \
     -0.50554584202664287762, \
      0.22064824236265745405, \
     -0.22064824236265745405, \
      0.22064824236265745405, \
     -0.22064824236265745405, \
      0.34405034181784766023, \
     -0.34405034181784766023, \
      0.34405034181784766023, \
     -0.34405034181784766023, \
      0.19624129641007534430, \
     -0.19624129641007534430, \
      0.19624129641007534430, \
     -0.19624129641007534430, \
      0.91947901583738034237, \
     -0.91947901583738034237, \
      0.91947901583738034237, \
     -0.91947901583738034237, \
      0.26209258399888046842, \
     -0.26209258399888046842, \
      0.26209258399888046842, \
     -0.26209258399888046842, \
      0.17448879428144709047, \
     -0.17448879428144709047, \
      0.17448879428144709047, \
     -0.17448879428144709047, \
      0.13256324285803838814, \
     -0.13256324285803838814, \
      0.13256324285803838814, \
     -0.13256324285803838814, \
      0.30777107074463094794, \
     -0.30777107074463094794, \
      0.30777107074463094794, \
     -0.30777107074463094794, \
      0.45437881454568046502, \
     -0.45437881454568046502, \
      0.45437881454568046502, \
     -0.45437881454568046502, \
      0.18203893212319594008, \
     -0.18203893212319594008, \
      0.18203893212319594008, \
     -0.18203893212319594008, \
      0.18804430068288069400, \
     -0.18804430068288069400, \
      0.18804430068288069400, \
     -0.18804430068288069400, \
      0.85285866036694601977, \
     -0.85285866036694601977, \
      0.85285866036694601977, \
     -0.85285866036694601977, \
      0.19395358431436507396, \
     -0.19395358431436507396, \
      0.19395358431436507396, \
     -0.19395358431436507396, \
      0.63620569449244868121, \
     -0.63620569449244868121, \
      0.63620569449244868121, \
     -0.63620569449244868121, \
      0.71609629503236627013, \
     -0.71609629503236627013, \
      0.71609629503236627013, \
     -0.71609629503236627013, \
      0.72970588623268628492, \
     -0.72970588623268628492, \
      0.72970588623268628492, \
     -0.72970588623268628492, \
      0.85828508770542477624, \
      0.57684038354992128728, \
     -0.85828508770542477624, \
      0.57684038354992128728, \
      0.85828508770542477624, \
     -0.57684038354992128728, \
     -0.85828508770542477624, \
     -0.57684038354992128728, \
      0.76336766190340221705, \
      0.21167809325271402798, \
     -0.76336766190340221705, \
      0.21167809325271402798, \
      0.76336766190340221705, \
     -0.21167809325271402798, \
     -0.76336766190340221705, \
     -0.21167809325271402798, \
      0.21613035096350702302, \
      0.58392235225835387169, \
     -0.21613035096350702302, \
      0.58392235225835387169, \
      0.21613035096350702302, \
     -0.58392235225835387169, \
     -0.21613035096350702302, \
     -0.58392235225835387169, \
      0.95615842996744093707, \
      0.64241827941687201786, \
     -0.95615842996744093707, \
      0.64241827941687201786, \
      0.95615842996744093707, \
     -0.64241827941687201786, \
     -0.95615842996744093707, \
     -0.64241827941687201786, \
      0.87592219252594005763, \
      0.37797565831285062643, \
     -0.87592219252594005763, \
      0.37797565831285062643, \
      0.87592219252594005763, \
     -0.37797565831285062643, \
     -0.87592219252594005763, \
     -0.37797565831285062643, \
      0.24453940621889402873, \
      0.46719416054032014696, \
     -0.24453940621889402873, \
      0.46719416054032014696, \
      0.24453940621889402873, \
     -0.46719416054032014696, \
     -0.24453940621889402873, \
     -0.46719416054032014696, \
      0.37060589700094320742, \
      0.54852690614804233693, \
     -0.37060589700094320742, \
      0.54852690614804233693, \
      0.37060589700094320742, \
     -0.54852690614804233693, \
     -0.37060589700094320742, \
     -0.54852690614804233693, \
      0.61567982840573709513, \
      0.00714017158789090767, \
     -0.61567982840573709513, \
      0.00714017158789090767, \
      0.61567982840573709513, \
     -0.00714017158789090767, \
     -0.61567982840573709513, \
     -0.00714017158789090767, \
      0.71013273965512191399, \
      0.27918941987191842058, \
     -0.71013273965512191399, \
      0.27918941987191842058, \
      0.71013273965512191399, \
     -0.27918941987191842058, \
     -0.71013273965512191399, \
     -0.27918941987191842058, \
      0.82587110596774426785, \
      0.35683026213317575737, \
     -0.82587110596774426785, \
      0.35683026213317575737, \
      0.82587110596774426785, \
     -0.35683026213317575737, \
     -0.82587110596774426785, \
     -0.35683026213317575737, \
      0.47557663390649029811, \
      0.69286495782397328203, \
     -0.47557663390649029811, \
      0.69286495782397328203, \
      0.47557663390649029811, \
     -0.69286495782397328203, \
     -0.47557663390649029811, \
     -0.69286495782397328203 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.70014035742397184858, \
      0.00000000000000000000, \
     -0.70014035742397184858, \
      0.00000000000000000000, \
      0.91936314848339839578, \
      0.00000000000000000000, \
     -0.91936314848339839578, \
      0.00000000000000000000, \
      0.11013348894423610758, \
      0.00000000000000000000, \
     -0.11013348894423610758, \
      0.00000000000000000000, \
      0.44650085670154981976, \
      0.00000000000000000000, \
     -0.44650085670154981976, \
      0.00000000000000000000, \
      0.80205385758014868802, \
      0.00000000000000000000, \
     -0.80205385758014868802, \
      0.00000000000000000000, \
      0.53015124527324641868, \
      0.00000000000000000000, \
     -0.53015124527324641868, \
      0.00000000000000000000, \
      0.97322734428927526462, \
      0.00000000000000000000, \
     -0.97322734428927526462, \
      0.00000000000000000000, \
      0.50557186634064188446, \
      0.00000000000000000000, \
     -0.50557186634064188446, \
      0.00000000000000000000, \
      0.04618938260051261985, \
      0.00000000000000000000, \
     -0.04618938260051261985, \
      0.00000000000000000000, \
      0.62301364063828001960, \
      0.00000000000000000000, \
     -0.62301364063828001960, \
      0.00000000000000000000, \
      0.29509310458272342004, \
      0.00000000000000000000, \
     -0.29509310458272342004, \
      0.00000000000000000000, \
      0.47760058576112396356, \
      0.00000000000000000000, \
     -0.47760058576112396356, \
      0.00000000000000000000, \
      0.36898015805621120489, \
      0.00000000000000000000, \
     -0.36898015805621120489, \
      0.37237829048305948199, \
      0.37237829048305948199, \
     -0.37237829048305948199, \
     -0.37237829048305948199, \
      0.53419020022883723087, \
      0.53419020022883723087, \
     -0.53419020022883723087, \
     -0.53419020022883723087, \
      0.06063808134784291065, \
      0.06063808134784291065, \
     -0.06063808134784291065, \
     -0.06063808134784291065, \
      0.47770687706587527943, \
      0.47770687706587527943, \
     -0.47770687706587527943, \
     -0.47770687706587527943, \
      0.19875431205737298379, \
      0.19875431205737298379, \
     -0.19875431205737298379, \
     -0.19875431205737298379, \
      0.75996956110375202265, \
      0.75996956110375202265, \
     -0.75996956110375202265, \
     -0.75996956110375202265, \
      0.50554584202664287762, \
      0.50554584202664287762, \
     -0.50554584202664287762, \
     -0.50554584202664287762, \
      0.22064824236265745405, \
      0.22064824236265745405, \
     -0.22064824236265745405, \
     -0.22064824236265745405, \
      0.34405034181784766023, \
      0.34405034181784766023, \
     -0.34405034181784766023, \
     -0.34405034181784766023, \
      0.19624129641007534430, \
      0.19624129641007534430, \
     -0.19624129641007534430, \
     -0.19624129641007534430, \
      0.91947901583738034237, \
      0.91947901583738034237, \
     -0.91947901583738034237, \
     -0.91947901583738034237, \
      0.26209258399888046842, \
      0.26209258399888046842, \
     -0.26209258399888046842, \
     -0.26209258399888046842, \
      0.17448879428144709047, \
      0.17448879428144709047, \
     -0.17448879428144709047, \
     -0.17448879428144709047, \
      0.13256324285803838814, \
      0.13256324285803838814, \
     -0.13256324285803838814, \
     -0.13256324285803838814, \
      0.30777107074463094794, \
      0.30777107074463094794, \
     -0.30777107074463094794, \
     -0.30777107074463094794, \
      0.45437881454568046502, \
      0.45437881454568046502, \
     -0.45437881454568046502, \
     -0.45437881454568046502, \
      0.18203893212319594008, \
      0.18203893212319594008, \
     -0.18203893212319594008, \
     -0.18203893212319594008, \
      0.18804430068288069400, \
      0.18804430068288069400, \
     -0.18804430068288069400, \
     -0.18804430068288069400, \
      0.85285866036694601977, \
      0.85285866036694601977, \
     -0.85285866036694601977, \
     -0.85285866036694601977, \
      0.19395358431436507396, \
      0.19395358431436507396, \
     -0.19395358431436507396, \
     -0.19395358431436507396, \
      0.63620569449244868121, \
      0.63620569449244868121, \
     -0.63620569449244868121, \
     -0.63620569449244868121, \
      0.71609629503236627013, \
      0.71609629503236627013, \
     -0.71609629503236627013, \
     -0.71609629503236627013, \
      0.72970588623268628492, \
      0.72970588623268628492, \
     -0.72970588623268628492, \
     -0.72970588623268628492, \
      0.57684038354992128728, \
      0.85828508770542477624, \
      0.57684038354992128728, \
     -0.85828508770542477624, \
     -0.57684038354992128728, \
      0.85828508770542477624, \
     -0.57684038354992128728, \
     -0.85828508770542477624, \
      0.21167809325271402798, \
      0.76336766190340221705, \
      0.21167809325271402798, \
     -0.76336766190340221705, \
     -0.21167809325271402798, \
      0.76336766190340221705, \
     -0.21167809325271402798, \
     -0.76336766190340221705, \
      0.58392235225835387169, \
      0.21613035096350702302, \
      0.58392235225835387169, \
     -0.21613035096350702302, \
     -0.58392235225835387169, \
      0.21613035096350702302, \
     -0.58392235225835387169, \
     -0.21613035096350702302, \
      0.64241827941687201786, \
      0.95615842996744093707, \
      0.64241827941687201786, \
     -0.95615842996744093707, \
     -0.64241827941687201786, \
      0.95615842996744093707, \
     -0.64241827941687201786, \
     -0.95615842996744093707, \
      0.37797565831285062643, \
      0.87592219252594005763, \
      0.37797565831285062643, \
     -0.87592219252594005763, \
     -0.37797565831285062643, \
      0.87592219252594005763, \
     -0.37797565831285062643, \
     -0.87592219252594005763, \
      0.46719416054032014696, \
      0.24453940621889402873, \
      0.46719416054032014696, \
     -0.24453940621889402873, \
     -0.46719416054032014696, \
      0.24453940621889402873, \
     -0.46719416054032014696, \
     -0.24453940621889402873, \
      0.54852690614804233693, \
      0.37060589700094320742, \
      0.54852690614804233693, \
     -0.37060589700094320742, \
     -0.54852690614804233693, \
      0.37060589700094320742, \
     -0.54852690614804233693, \
     -0.37060589700094320742, \
      0.00714017158789090767, \
      0.61567982840573709513, \
      0.00714017158789090767, \
     -0.61567982840573709513, \
     -0.00714017158789090767, \
      0.61567982840573709513, \
     -0.00714017158789090767, \
     -0.61567982840573709513, \
      0.27918941987191842058, \
      0.71013273965512191399, \
      0.27918941987191842058, \
     -0.71013273965512191399, \
     -0.27918941987191842058, \
      0.71013273965512191399, \
     -0.27918941987191842058, \
     -0.71013273965512191399, \
      0.35683026213317575737, \
      0.82587110596774426785, \
      0.35683026213317575737, \
     -0.82587110596774426785, \
     -0.35683026213317575737, \
      0.82587110596774426785, \
     -0.35683026213317575737, \
     -0.82587110596774426785, \
      0.69286495782397328203, \
      0.47557663390649029811, \
      0.69286495782397328203, \
     -0.47557663390649029811, \
     -0.69286495782397328203, \
      0.47557663390649029811, \
     -0.69286495782397328203, \
     -0.47557663390649029811 ] )

  z = np.array ( [ \
      0.95167840606392661851, \
      0.29890092144247565331, \
      0.10372522326204723642, \
      0.10372522326204723642, \
      0.10372522326204723642, \
      0.10372522326204723642, \
      0.06052669044962753070, \
      0.06052669044962753070, \
      0.06052669044962753070, \
      0.06052669044962753070, \
      0.87767072134508183900, \
      0.87767072134508183900, \
      0.87767072134508183900, \
      0.87767072134508183900, \
      0.33061431908844512995, \
      0.33061431908844512995, \
      0.33061431908844512995, \
      0.33061431908844512995, \
      0.18913057164406818500, \
      0.18913057164406818500, \
      0.18913057164406818500, \
      0.18913057164406818500, \
      0.15549793195551472880, \
      0.15549793195551472880, \
      0.15549793195551472880, \
      0.15549793195551472880, \
      0.00490511032939973824, \
      0.00490511032939973824, \
      0.00490511032939973824, \
      0.00490511032939973824, \
      0.06238803484862592841, \
      0.06238803484862592841, \
      0.06238803484862592841, \
      0.06238803484862592841, \
      0.53284146417918532013, \
      0.53284146417918532013, \
      0.53284146417918532013, \
      0.53284146417918532013, \
      0.37695593807084121218, \
      0.37695593807084121218, \
      0.37695593807084121218, \
      0.37695593807084121218, \
      0.68148251405524751245, \
      0.68148251405524751245, \
      0.68148251405524751245, \
      0.68148251405524751245, \
      0.23097535663334242684, \
      0.23097535663334242684, \
      0.23097535663334242684, \
      0.23097535663334242684, \
      0.50335666905043052743, \
      0.50335666905043052743, \
      0.50335666905043052743, \
      0.50335666905043052743, \
      0.42353675293216364039, \
      0.42353675293216364039, \
      0.42353675293216364039, \
      0.42353675293216364039, \
      0.41296679793793455993, \
      0.41296679793793455993, \
      0.41296679793793455993, \
      0.41296679793793455993, \
      0.78640579578998992538, \
      0.78640579578998992538, \
      0.78640579578998992538, \
      0.78640579578998992538, \
      0.32653775213007651956, \
      0.32653775213007651956, \
      0.32653775213007651956, \
      0.32653775213007651956, \
      0.05291423306214974864, \
      0.05291423306214974864, \
      0.05291423306214974864, \
      0.05291423306214974864, \
      0.00693099618919339969, \
      0.00693099618919339969, \
      0.00693099618919339969, \
      0.00693099618919339969, \
      0.01799129130112891647, \
      0.01799129130112891647, \
      0.01799129130112891647, \
      0.01799129130112891647, \
      0.00830477370838420340, \
      0.00830477370838420340, \
      0.00830477370838420340, \
      0.00830477370838420340, \
      0.61788739915987689333, \
      0.61788739915987689333, \
      0.61788739915987689333, \
      0.61788739915987689333, \
      0.19265498366863681445, \
      0.19265498366863681445, \
      0.19265498366863681445, \
      0.19265498366863681445, \
      0.01617257265834035757, \
      0.01617257265834035757, \
      0.01617257265834035757, \
      0.01617257265834035757, \
      0.59548810603233670591, \
      0.59548810603233670591, \
      0.59548810603233670591, \
      0.59548810603233670591, \
      0.76735204589989336466, \
      0.76735204589989336466, \
      0.76735204589989336466, \
      0.76735204589989336466, \
      0.64457148839122024864, \
      0.64457148839122024864, \
      0.64457148839122024864, \
      0.64457148839122024864, \
      0.26823389272477243805, \
      0.26823389272477243805, \
      0.26823389272477243805, \
      0.26823389272477243805, \
      0.19249663769902353172, \
      0.19249663769902353172, \
      0.19249663769902353172, \
      0.19249663769902353172, \
      0.35451205561493442930, \
      0.35451205561493442930, \
      0.35451205561493442930, \
      0.35451205561493442930, \
      0.13784397009929885702, \
      0.13784397009929885702, \
      0.13784397009929885702, \
      0.13784397009929885702, \
      0.08819642588395044946, \
      0.08819642588395044946, \
      0.08819642588395044946, \
      0.08819642588395044946, \
      0.44126341704052479686, \
      0.44126341704052479686, \
      0.44126341704052479686, \
      0.44126341704052479686, \
      0.18126706536632553046, \
      0.18126706536632553046, \
      0.18126706536632553046, \
      0.18126706536632553046, \
      0.06273138420630826328, \
      0.06273138420630826328, \
      0.06273138420630826328, \
      0.06273138420630826328, \
      0.22238800479499257201, \
      0.22238800479499257201, \
      0.22238800479499257201, \
      0.22238800479499257201, \
      0.12311329897268918909, \
      0.12311329897268918909, \
      0.12311329897268918909, \
      0.12311329897268918909, \
      0.12311329897268918909, \
      0.12311329897268918909, \
      0.12311329897268918909, \
      0.12311329897268918909, \
      0.02653658688975024313, \
      0.02653658688975024313, \
      0.02653658688975024313, \
      0.02653658688975024313, \
      0.02653658688975024313, \
      0.02653658688975024313, \
      0.02653658688975024313, \
      0.02653658688975024313, \
      0.32949702529445068500, \
      0.32949702529445068500, \
      0.32949702529445068500, \
      0.32949702529445068500, \
      0.32949702529445068500, \
      0.32949702529445068500, \
      0.32949702529445068500, \
      0.32949702529445068500, \
      0.02375108271645150898, \
      0.02375108271645150898, \
      0.02375108271645150898, \
      0.02375108271645150898, \
      0.02375108271645150898, \
      0.02375108271645150898, \
      0.02375108271645150898, \
      0.02375108271645150898, \
      0.01156156746353601689, \
      0.01156156746353601689, \
      0.01156156746353601689, \
      0.01156156746353601689, \
      0.01156156746353601689, \
      0.01156156746353601689, \
      0.01156156746353601689, \
      0.01156156746353601689, \
      0.50478124488277686943, \
      0.50478124488277686943, \
      0.50478124488277686943, \
      0.50478124488277686943, \
      0.50478124488277686943, \
      0.50478124488277686943, \
      0.50478124488277686943, \
      0.50478124488277686943, \
      0.09182493970820698737, \
      0.09182493970820698737, \
      0.09182493970820698737, \
      0.09182493970820698737, \
      0.09182493970820698737, \
      0.09182493970820698737, \
      0.09182493970820698737, \
      0.09182493970820698737, \
      0.01061641469954416848, \
      0.01061641469954416848, \
      0.01061641469954416848, \
      0.01061641469954416848, \
      0.01061641469954416848, \
      0.01061641469954416848, \
      0.01061641469954416848, \
      0.01061641469954416848, \
      0.18699248305545079774, \
      0.18699248305545079774, \
      0.18699248305545079774, \
      0.18699248305545079774, \
      0.18699248305545079774, \
      0.18699248305545079774, \
      0.18699248305545079774, \
      0.18699248305545079774, \
      0.07551964039133612916, \
      0.07551964039133612916, \
      0.07551964039133612916, \
      0.07551964039133612916, \
      0.07551964039133612916, \
      0.07551964039133612916, \
      0.07551964039133612916, \
      0.07551964039133612916, \
      0.28631001132523614672, \
      0.28631001132523614672, \
      0.28631001132523614672, \
      0.28631001132523614672, \
      0.28631001132523614672, \
      0.28631001132523614672, \
      0.28631001132523614672, \
      0.28631001132523614672 ] )

  w= np.array ( [ \
      0.00042533015548600539, \
      0.01525748792328103336, \
      0.00528017662585705642, \
      0.00528017662585705642, \
      0.00528017662585705642, \
      0.00528017662585705642, \
      0.00244639458990403638, \
      0.00244639458990403638, \
      0.00244639458990403638, \
      0.00244639458990403638, \
      0.00097370603129723528, \
      0.00097370603129723528, \
      0.00097370603129723528, \
      0.00097370603129723528, \
      0.00777612495382315819, \
      0.00777612495382315819, \
      0.00777612495382315819, \
      0.00777612495382315819, \
      0.00267697092767919202, \
      0.00267697092767919202, \
      0.00267697092767919202, \
      0.00267697092767919202, \
      0.00619081284266621932, \
      0.00619081284266621932, \
      0.00619081284266621932, \
      0.00619081284266621932, \
      0.00065618656167288063, \
      0.00065618656167288063, \
      0.00065618656167288063, \
      0.00065618656167288063, \
      0.00656994056618269082, \
      0.00656994056618269082, \
      0.00656994056618269082, \
      0.00656994056618269082, \
      0.00267308743214515841, \
      0.00267308743214515841, \
      0.00267308743214515841, \
      0.00267308743214515841, \
      0.00175949530216048481, \
      0.00175949530216048481, \
      0.00175949530216048481, \
      0.00175949530216048481, \
      0.00331285760856183092, \
      0.00331285760856183092, \
      0.00331285760856183092, \
      0.00331285760856183092, \
      0.00751034506572093984, \
      0.00751034506572093984, \
      0.00751034506572093984, \
      0.00751034506572093984, \
      0.00893166529089345351, \
      0.00893166529089345351, \
      0.00893166529089345351, \
      0.00893166529089345351, \
      0.00556841825996671948, \
      0.00556841825996671948, \
      0.00556841825996671948, \
      0.00556841825996671948, \
      0.00264945739278132876, \
      0.00264945739278132876, \
      0.00264945739278132876, \
      0.00264945739278132876, \
      0.00197028999055473379, \
      0.00197028999055473379, \
      0.00197028999055473379, \
      0.00197028999055473379, \
      0.00513483903966016272, \
      0.00513483903966016272, \
      0.00513483903966016272, \
      0.00513483903966016272, \
      0.00742192548155929527, \
      0.00742192548155929527, \
      0.00742192548155929527, \
      0.00742192548155929527, \
      0.00164485721629859362, \
      0.00164485721629859362, \
      0.00164485721629859362, \
      0.00164485721629859362, \
      0.00553453693910099451, \
      0.00553453693910099451, \
      0.00553453693910099451, \
      0.00553453693910099451, \
      0.00325628156420546379, \
      0.00325628156420546379, \
      0.00325628156420546379, \
      0.00325628156420546379, \
      0.00151506082426114191, \
      0.00151506082426114191, \
      0.00151506082426114191, \
      0.00151506082426114191, \
      0.00591126556727756668, \
      0.00591126556727756668, \
      0.00591126556727756668, \
      0.00591126556727756668, \
      0.00083923797814166039, \
      0.00083923797814166039, \
      0.00083923797814166039, \
      0.00083923797814166039, \
      0.00402240401025226024, \
      0.00402240401025226024, \
      0.00402240401025226024, \
      0.00402240401025226024, \
      0.00223169575519892738, \
      0.00223169575519892738, \
      0.00223169575519892738, \
      0.00223169575519892738, \
      0.00615688200816193708, \
      0.00615688200816193708, \
      0.00615688200816193708, \
      0.00615688200816193708, \
      0.00864232058920194786, \
      0.00864232058920194786, \
      0.00864232058920194786, \
      0.00864232058920194786, \
      0.00745270338750553870, \
      0.00745270338750553870, \
      0.00745270338750553870, \
      0.00745270338750553870, \
      0.00502880383507017109, \
      0.00502880383507017109, \
      0.00502880383507017109, \
      0.00502880383507017109, \
      0.00879638512225545434, \
      0.00879638512225545434, \
      0.00879638512225545434, \
      0.00879638512225545434, \
      0.00174781246088704756, \
      0.00174781246088704756, \
      0.00174781246088704756, \
      0.00174781246088704756, \
      0.00918989383822925963, \
      0.00918989383822925963, \
      0.00918989383822925963, \
      0.00918989383822925963, \
      0.00620807391936788796, \
      0.00620807391936788796, \
      0.00620807391936788796, \
      0.00620807391936788796, \
      0.00568398055245949909, \
      0.00568398055245949909, \
      0.00568398055245949909, \
      0.00568398055245949909, \
      0.00183658571623211762, \
      0.00183658571623211762, \
      0.00183658571623211762, \
      0.00183658571623211762, \
      0.00221869264777755162, \
      0.00221869264777755162, \
      0.00221869264777755162, \
      0.00221869264777755162, \
      0.00221869264777755162, \
      0.00221869264777755162, \
      0.00221869264777755162, \
      0.00221869264777755162, \
      0.00260988740586402639, \
      0.00260988740586402639, \
      0.00260988740586402639, \
      0.00260988740586402639, \
      0.00260988740586402639, \
      0.00260988740586402639, \
      0.00260988740586402639, \
      0.00260988740586402639, \
      0.00616875610859360119, \
      0.00616875610859360119, \
      0.00616875610859360119, \
      0.00616875610859360119, \
      0.00616875610859360119, \
      0.00616875610859360119, \
      0.00616875610859360119, \
      0.00616875610859360119, \
      0.00122995761226799547, \
      0.00122995761226799547, \
      0.00122995761226799547, \
      0.00122995761226799547, \
      0.00122995761226799547, \
      0.00122995761226799547, \
      0.00122995761226799547, \
      0.00122995761226799547, \
      0.00195493878423380618, \
      0.00195493878423380618, \
      0.00195493878423380618, \
      0.00195493878423380618, \
      0.00195493878423380618, \
      0.00195493878423380618, \
      0.00195493878423380618, \
      0.00195493878423380618, \
      0.00346763933769407258, \
      0.00346763933769407258, \
      0.00346763933769407258, \
      0.00346763933769407258, \
      0.00346763933769407258, \
      0.00346763933769407258, \
      0.00346763933769407258, \
      0.00346763933769407258, \
      0.00677026604334400768, \
      0.00677026604334400768, \
      0.00677026604334400768, \
      0.00677026604334400768, \
      0.00677026604334400768, \
      0.00677026604334400768, \
      0.00677026604334400768, \
      0.00677026604334400768, \
      0.00167829416355688515, \
      0.00167829416355688515, \
      0.00167829416355688515, \
      0.00167829416355688515, \
      0.00167829416355688515, \
      0.00167829416355688515, \
      0.00167829416355688515, \
      0.00167829416355688515, \
      0.00713079759016688013, \
      0.00713079759016688013, \
      0.00713079759016688013, \
      0.00713079759016688013, \
      0.00713079759016688013, \
      0.00713079759016688013, \
      0.00713079759016688013, \
      0.00713079759016688013, \
      0.00467547289885053390, \
      0.00467547289885053390, \
      0.00467547289885053390, \
      0.00467547289885053390, \
      0.00467547289885053390, \
      0.00467547289885053390, \
      0.00467547289885053390, \
      0.00467547289885053390, \
      0.00253420752420773854, \
      0.00253420752420773854, \
      0.00253420752420773854, \
      0.00253420752420773854, \
      0.00253420752420773854, \
      0.00253420752420773854, \
      0.00253420752420773854, \
      0.00253420752420773854 ] )

  return x, y, z, w

def rule16 ( ):

#*****************************************************************************80
#
## rule16() returns the pyramid quadrature rule of precision 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.51870388022974789344, \
      0.00000000000000000000, \
     -0.51870388022974789344, \
      0.00000000000000000000, \
      0.91531292456766799592, \
      0.00000000000000000000, \
     -0.91531292456766799592, \
      0.00000000000000000000, \
      0.01655472656731888509, \
      0.00000000000000000000, \
     -0.01655472656731888509, \
      0.00000000000000000000, \
      0.36912135575078097727, \
      0.00000000000000000000, \
     -0.36912135575078097727, \
      0.00000000000000000000, \
      0.02060330211667108294, \
      0.00000000000000000000, \
     -0.02060330211667108294, \
      0.00000000000000000000, \
      0.87194193710104261896, \
      0.00000000000000000000, \
     -0.87194193710104261896, \
      0.00000000000000000000, \
      0.31538420787936460865, \
      0.00000000000000000000, \
     -0.31538420787936460865, \
      0.00000000000000000000, \
      0.61399555563153074278, \
      0.00000000000000000000, \
     -0.61399555563153074278, \
      0.00000000000000000000, \
      0.09765007634893953237, \
      0.00000000000000000000, \
     -0.09765007634893953237, \
      0.00000000000000000000, \
      0.73176464480784220168, \
      0.00000000000000000000, \
     -0.73176464480784220168, \
      0.00000000000000000000, \
      0.84054220943522905962, \
      0.00000000000000000000, \
     -0.84054220943522905962, \
      0.00000000000000000000, \
      0.55574609505629035677, \
      0.00000000000000000000, \
     -0.55574609505629035677, \
      0.00000000000000000000, \
      0.26438021717351822826, \
      0.00000000000000000000, \
     -0.26438021717351822826, \
      0.00000000000000000000, \
      0.13755031468645742554, \
     -0.13755031468645742554, \
      0.13755031468645742554, \
     -0.13755031468645742554, \
      0.55599929975376194413, \
     -0.55599929975376194413, \
      0.55599929975376194413, \
     -0.55599929975376194413, \
      0.68037602529077279012, \
     -0.68037602529077279012, \
      0.68037602529077279012, \
     -0.68037602529077279012, \
      0.68987074662201319786, \
     -0.68987074662201319786, \
      0.68987074662201319786, \
     -0.68987074662201319786, \
      0.46656016616381063011, \
     -0.46656016616381063011, \
      0.46656016616381063011, \
     -0.46656016616381063011, \
      0.93657427078716448676, \
     -0.93657427078716448676, \
      0.93657427078716448676, \
     -0.93657427078716448676, \
      0.10668464068510881415, \
     -0.10668464068510881415, \
      0.10668464068510881415, \
     -0.10668464068510881415, \
      0.56362866319030435758, \
     -0.56362866319030435758, \
      0.56362866319030435758, \
     -0.56362866319030435758, \
      0.08721470315267314255, \
     -0.08721470315267314255, \
      0.08721470315267314255, \
     -0.08721470315267314255, \
      0.28826482911237666373, \
     -0.28826482911237666373, \
      0.28826482911237666373, \
     -0.28826482911237666373, \
      0.23503249705404929970, \
     -0.23503249705404929970, \
      0.23503249705404929970, \
     -0.23503249705404929970, \
      0.24508582185951371946, \
     -0.24508582185951371946, \
      0.24508582185951371946, \
     -0.24508582185951371946, \
      0.50030649786215641850, \
     -0.50030649786215641850, \
      0.50030649786215641850, \
     -0.50030649786215641850, \
      0.05973130190403576345, \
     -0.05973130190403576345, \
      0.05973130190403576345, \
     -0.05973130190403576345, \
      0.36285963939710730308, \
     -0.36285963939710730308, \
      0.36285963939710730308, \
     -0.36285963939710730308, \
      0.83163011923015617288, \
     -0.83163011923015617288, \
      0.83163011923015617288, \
     -0.83163011923015617288, \
      0.59815151207893801910, \
     -0.59815151207893801910, \
      0.59815151207893801910, \
     -0.59815151207893801910, \
      0.32452468623385005708, \
     -0.32452468623385005708, \
      0.32452468623385005708, \
     -0.32452468623385005708, \
      0.18400437828694599096, \
     -0.18400437828694599096, \
      0.18400437828694599096, \
     -0.18400437828694599096, \
      0.80685585076678034699, \
     -0.80685585076678034699, \
      0.80685585076678034699, \
     -0.80685585076678034699, \
      0.39038172839426421579, \
     -0.39038172839426421579, \
      0.39038172839426421579, \
     -0.39038172839426421579, \
      0.16205656720464603482, \
     -0.16205656720464603482, \
      0.16205656720464603482, \
     -0.16205656720464603482, \
      0.79557791018541468286, \
      0.52651319421754327887, \
     -0.79557791018541468286, \
      0.52651319421754327887, \
      0.79557791018541468286, \
     -0.52651319421754327887, \
     -0.79557791018541468286, \
     -0.52651319421754327887, \
      0.82001165757451899285, \
      0.58763897947885146422, \
     -0.82001165757451899285, \
      0.58763897947885146422, \
      0.82001165757451899285, \
     -0.58763897947885146422, \
     -0.82001165757451899285, \
     -0.58763897947885146422, \
      0.48106775949054608743, \
      0.14913701615330382522, \
     -0.48106775949054608743, \
      0.14913701615330382522, \
      0.48106775949054608743, \
     -0.14913701615330382522, \
     -0.48106775949054608743, \
     -0.14913701615330382522, \
      0.91698017235976392314, \
      0.63033943569284833774, \
     -0.91698017235976392314, \
      0.63033943569284833774, \
      0.91698017235976392314, \
     -0.63033943569284833774, \
     -0.91698017235976392314, \
     -0.63033943569284833774, \
      0.95781996021629389748, \
      0.33277831868591489783, \
     -0.95781996021629389748, \
      0.33277831868591489783, \
      0.95781996021629389748, \
     -0.33277831868591489783, \
     -0.95781996021629389748, \
     -0.33277831868591489783, \
      0.21226792819096282350, \
      0.42143671745401867224, \
     -0.21226792819096282350, \
      0.42143671745401867224, \
      0.21226792819096282350, \
     -0.42143671745401867224, \
     -0.21226792819096282350, \
     -0.42143671745401867224, \
      0.24859573800356360440, \
      0.62623217679932552393, \
     -0.24859573800356360440, \
      0.62623217679932552393, \
      0.24859573800356360440, \
     -0.62623217679932552393, \
     -0.24859573800356360440, \
     -0.62623217679932552393, \
      0.55347901385730624568, \
      0.18815805920102898763, \
     -0.55347901385730624568, \
      0.18815805920102898763, \
      0.55347901385730624568, \
     -0.18815805920102898763, \
     -0.55347901385730624568, \
     -0.18815805920102898763, \
      0.82422827852456481690, \
      0.36376205736175593053, \
     -0.82422827852456481690, \
      0.36376205736175593053, \
      0.82422827852456481690, \
     -0.36376205736175593053, \
     -0.82422827852456481690, \
     -0.36376205736175593053, \
      0.14606542728759722150, \
      0.44268310223761137001, \
     -0.14606542728759722150, \
      0.44268310223761137001, \
      0.14606542728759722150, \
     -0.44268310223761137001, \
     -0.14606542728759722150, \
     -0.44268310223761137001, \
      0.38810720735022874450, \
      0.62355125720878634699, \
     -0.38810720735022874450, \
      0.62355125720878634699, \
      0.38810720735022874450, \
     -0.62355125720878634699, \
     -0.38810720735022874450, \
     -0.62355125720878634699, \
      0.95674484283290128772, \
      0.79844517503668932523, \
     -0.95674484283290128772, \
      0.79844517503668932523, \
      0.95674484283290128772, \
     -0.79844517503668932523, \
     -0.95674484283290128772, \
     -0.79844517503668932523, \
      0.60984849485865177954, \
      0.31205150762818156807, \
     -0.60984849485865177954, \
      0.31205150762818156807, \
      0.60984849485865177954, \
     -0.31205150762818156807, \
     -0.60984849485865177954, \
     -0.31205150762818156807, \
      0.24847427215400066935, \
      0.13406531787546346890, \
     -0.24847427215400066935, \
      0.13406531787546346890, \
      0.24847427215400066935, \
     -0.13406531787546346890, \
     -0.24847427215400066935, \
     -0.13406531787546346890, \
      0.69918943535356659069, \
      0.17767876450874769967, \
     -0.69918943535356659069, \
      0.17767876450874769967, \
      0.69918943535356659069, \
     -0.17767876450874769967, \
     -0.69918943535356659069, \
     -0.17767876450874769967, \
      0.36015415281659141078, \
      0.43011776020837644285, \
     -0.36015415281659141078, \
      0.43011776020837644285, \
      0.36015415281659141078, \
     -0.43011776020837644285, \
     -0.36015415281659141078, \
     -0.43011776020837644285, \
      0.73668742050512570074, \
      0.30298735173674529175, \
     -0.73668742050512570074, \
      0.30298735173674529175, \
      0.73668742050512570074, \
     -0.30298735173674529175, \
     -0.73668742050512570074, \
     -0.30298735173674529175, \
      0.31424806302114011158, \
      0.02522065148266495332, \
     -0.31424806302114011158, \
      0.02522065148266495332, \
      0.31424806302114011158, \
     -0.02522065148266495332, \
     -0.31424806302114011158, \
     -0.02522065148266495332 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.51870388022974789344, \
      0.00000000000000000000, \
     -0.51870388022974789344, \
      0.00000000000000000000, \
      0.91531292456766799592, \
      0.00000000000000000000, \
     -0.91531292456766799592, \
      0.00000000000000000000, \
      0.01655472656731888509, \
      0.00000000000000000000, \
     -0.01655472656731888509, \
      0.00000000000000000000, \
      0.36912135575078097727, \
      0.00000000000000000000, \
     -0.36912135575078097727, \
      0.00000000000000000000, \
      0.02060330211667108294, \
      0.00000000000000000000, \
     -0.02060330211667108294, \
      0.00000000000000000000, \
      0.87194193710104261896, \
      0.00000000000000000000, \
     -0.87194193710104261896, \
      0.00000000000000000000, \
      0.31538420787936460865, \
      0.00000000000000000000, \
     -0.31538420787936460865, \
      0.00000000000000000000, \
      0.61399555563153074278, \
      0.00000000000000000000, \
     -0.61399555563153074278, \
      0.00000000000000000000, \
      0.09765007634893953237, \
      0.00000000000000000000, \
     -0.09765007634893953237, \
      0.00000000000000000000, \
      0.73176464480784220168, \
      0.00000000000000000000, \
     -0.73176464480784220168, \
      0.00000000000000000000, \
      0.84054220943522905962, \
      0.00000000000000000000, \
     -0.84054220943522905962, \
      0.00000000000000000000, \
      0.55574609505629035677, \
      0.00000000000000000000, \
     -0.55574609505629035677, \
      0.00000000000000000000, \
      0.26438021717351822826, \
      0.00000000000000000000, \
     -0.26438021717351822826, \
      0.13755031468645742554, \
      0.13755031468645742554, \
     -0.13755031468645742554, \
     -0.13755031468645742554, \
      0.55599929975376194413, \
      0.55599929975376194413, \
     -0.55599929975376194413, \
     -0.55599929975376194413, \
      0.68037602529077279012, \
      0.68037602529077279012, \
     -0.68037602529077279012, \
     -0.68037602529077279012, \
      0.68987074662201319786, \
      0.68987074662201319786, \
     -0.68987074662201319786, \
     -0.68987074662201319786, \
      0.46656016616381063011, \
      0.46656016616381063011, \
     -0.46656016616381063011, \
     -0.46656016616381063011, \
      0.93657427078716448676, \
      0.93657427078716448676, \
     -0.93657427078716448676, \
     -0.93657427078716448676, \
      0.10668464068510881415, \
      0.10668464068510881415, \
     -0.10668464068510881415, \
     -0.10668464068510881415, \
      0.56362866319030435758, \
      0.56362866319030435758, \
     -0.56362866319030435758, \
     -0.56362866319030435758, \
      0.08721470315267314255, \
      0.08721470315267314255, \
     -0.08721470315267314255, \
     -0.08721470315267314255, \
      0.28826482911237666373, \
      0.28826482911237666373, \
     -0.28826482911237666373, \
     -0.28826482911237666373, \
      0.23503249705404929970, \
      0.23503249705404929970, \
     -0.23503249705404929970, \
     -0.23503249705404929970, \
      0.24508582185951371946, \
      0.24508582185951371946, \
     -0.24508582185951371946, \
     -0.24508582185951371946, \
      0.50030649786215641850, \
      0.50030649786215641850, \
     -0.50030649786215641850, \
     -0.50030649786215641850, \
      0.05973130190403576345, \
      0.05973130190403576345, \
     -0.05973130190403576345, \
     -0.05973130190403576345, \
      0.36285963939710730308, \
      0.36285963939710730308, \
     -0.36285963939710730308, \
     -0.36285963939710730308, \
      0.83163011923015617288, \
      0.83163011923015617288, \
     -0.83163011923015617288, \
     -0.83163011923015617288, \
      0.59815151207893801910, \
      0.59815151207893801910, \
     -0.59815151207893801910, \
     -0.59815151207893801910, \
      0.32452468623385005708, \
      0.32452468623385005708, \
     -0.32452468623385005708, \
     -0.32452468623385005708, \
      0.18400437828694599096, \
      0.18400437828694599096, \
     -0.18400437828694599096, \
     -0.18400437828694599096, \
      0.80685585076678034699, \
      0.80685585076678034699, \
     -0.80685585076678034699, \
     -0.80685585076678034699, \
      0.39038172839426421579, \
      0.39038172839426421579, \
     -0.39038172839426421579, \
     -0.39038172839426421579, \
      0.16205656720464603482, \
      0.16205656720464603482, \
     -0.16205656720464603482, \
     -0.16205656720464603482, \
      0.52651319421754327887, \
      0.79557791018541468286, \
      0.52651319421754327887, \
     -0.79557791018541468286, \
     -0.52651319421754327887, \
      0.79557791018541468286, \
     -0.52651319421754327887, \
     -0.79557791018541468286, \
      0.58763897947885146422, \
      0.82001165757451899285, \
      0.58763897947885146422, \
     -0.82001165757451899285, \
     -0.58763897947885146422, \
      0.82001165757451899285, \
     -0.58763897947885146422, \
     -0.82001165757451899285, \
      0.14913701615330382522, \
      0.48106775949054608743, \
      0.14913701615330382522, \
     -0.48106775949054608743, \
     -0.14913701615330382522, \
      0.48106775949054608743, \
     -0.14913701615330382522, \
     -0.48106775949054608743, \
      0.63033943569284833774, \
      0.91698017235976392314, \
      0.63033943569284833774, \
     -0.91698017235976392314, \
     -0.63033943569284833774, \
      0.91698017235976392314, \
     -0.63033943569284833774, \
     -0.91698017235976392314, \
      0.33277831868591489783, \
      0.95781996021629389748, \
      0.33277831868591489783, \
     -0.95781996021629389748, \
     -0.33277831868591489783, \
      0.95781996021629389748, \
     -0.33277831868591489783, \
     -0.95781996021629389748, \
      0.42143671745401867224, \
      0.21226792819096282350, \
      0.42143671745401867224, \
     -0.21226792819096282350, \
     -0.42143671745401867224, \
      0.21226792819096282350, \
     -0.42143671745401867224, \
     -0.21226792819096282350, \
      0.62623217679932552393, \
      0.24859573800356360440, \
      0.62623217679932552393, \
     -0.24859573800356360440, \
     -0.62623217679932552393, \
      0.24859573800356360440, \
     -0.62623217679932552393, \
     -0.24859573800356360440, \
      0.18815805920102898763, \
      0.55347901385730624568, \
      0.18815805920102898763, \
     -0.55347901385730624568, \
     -0.18815805920102898763, \
      0.55347901385730624568, \
     -0.18815805920102898763, \
     -0.55347901385730624568, \
      0.36376205736175593053, \
      0.82422827852456481690, \
      0.36376205736175593053, \
     -0.82422827852456481690, \
     -0.36376205736175593053, \
      0.82422827852456481690, \
     -0.36376205736175593053, \
     -0.82422827852456481690, \
      0.44268310223761137001, \
      0.14606542728759722150, \
      0.44268310223761137001, \
     -0.14606542728759722150, \
     -0.44268310223761137001, \
      0.14606542728759722150, \
     -0.44268310223761137001, \
     -0.14606542728759722150, \
      0.62355125720878634699, \
      0.38810720735022874450, \
      0.62355125720878634699, \
     -0.38810720735022874450, \
     -0.62355125720878634699, \
      0.38810720735022874450, \
     -0.62355125720878634699, \
     -0.38810720735022874450, \
      0.79844517503668932523, \
      0.95674484283290128772, \
      0.79844517503668932523, \
     -0.95674484283290128772, \
     -0.79844517503668932523, \
      0.95674484283290128772, \
     -0.79844517503668932523, \
     -0.95674484283290128772, \
      0.31205150762818156807, \
      0.60984849485865177954, \
      0.31205150762818156807, \
     -0.60984849485865177954, \
     -0.31205150762818156807, \
      0.60984849485865177954, \
     -0.31205150762818156807, \
     -0.60984849485865177954, \
      0.13406531787546346890, \
      0.24847427215400066935, \
      0.13406531787546346890, \
     -0.24847427215400066935, \
     -0.13406531787546346890, \
      0.24847427215400066935, \
     -0.13406531787546346890, \
     -0.24847427215400066935, \
      0.17767876450874769967, \
      0.69918943535356659069, \
      0.17767876450874769967, \
     -0.69918943535356659069, \
     -0.17767876450874769967, \
      0.69918943535356659069, \
     -0.17767876450874769967, \
     -0.69918943535356659069, \
      0.43011776020837644285, \
      0.36015415281659141078, \
      0.43011776020837644285, \
     -0.36015415281659141078, \
     -0.43011776020837644285, \
      0.36015415281659141078, \
     -0.43011776020837644285, \
     -0.36015415281659141078, \
      0.30298735173674529175, \
      0.73668742050512570074, \
      0.30298735173674529175, \
     -0.73668742050512570074, \
     -0.30298735173674529175, \
      0.73668742050512570074, \
     -0.30298735173674529175, \
     -0.73668742050512570074, \
      0.02522065148266495332, \
      0.31424806302114011158, \
      0.02522065148266495332, \
     -0.31424806302114011158, \
     -0.02522065148266495332, \
      0.31424806302114011158, \
     -0.02522065148266495332, \
     -0.31424806302114011158 ] )

  z = np.array ( [ \
      0.95860354636208366941, \
      0.14065559413657438559, \
      0.14065559413657438559, \
      0.14065559413657438559, \
      0.14065559413657438559, \
      0.04316491102619297859, \
      0.04316491102619297859, \
      0.04316491102619297859, \
      0.04316491102619297859, \
      0.39522832646013361657, \
      0.39522832646013361657, \
      0.39522832646013361657, \
      0.39522832646013361657, \
      0.29890125561593927639, \
      0.29890125561593927639, \
      0.29890125561593927639, \
      0.29890125561593927639, \
      0.06870461262955433746, \
      0.06870461262955433746, \
      0.06870461262955433746, \
      0.06870461262955433746, \
      0.11193495967860304929, \
      0.11193495967860304929, \
      0.11193495967860304929, \
      0.11193495967860304929, \
      0.56665435040432854397, \
      0.56665435040432854397, \
      0.56665435040432854397, \
      0.56665435040432854397, \
      0.15957732786354647536, \
      0.15957732786354647536, \
      0.15957732786354647536, \
      0.15957732786354647536, \
      0.89220214923004481644, \
      0.89220214923004481644, \
      0.89220214923004481644, \
      0.89220214923004481644, \
      0.24754993371512326594, \
      0.24754993371512326594, \
      0.24754993371512326594, \
      0.24754993371512326594, \
      0.01014565417563986251, \
      0.01014565417563986251, \
      0.01014565417563986251, \
      0.01014565417563986251, \
      0.42885512420774396514, \
      0.42885512420774396514, \
      0.42885512420774396514, \
      0.42885512420774396514, \
      0.71649796495360695836, \
      0.71649796495360695836, \
      0.71649796495360695836, \
      0.71649796495360695836, \
      0.17877523402579234557, \
      0.17877523402579234557, \
      0.17877523402579234557, \
      0.17877523402579234557, \
      0.29295501084965730465, \
      0.29295501084965730465, \
      0.29295501084965730465, \
      0.29295501084965730465, \
      0.27447523572941867620, \
      0.27447523572941867620, \
      0.27447523572941867620, \
      0.27447523572941867620, \
      0.15714127239405312197, \
      0.15714127239405312197, \
      0.15714127239405312197, \
      0.15714127239405312197, \
      0.25035924766443973244, \
      0.25035924766443973244, \
      0.25035924766443973244, \
      0.25035924766443973244, \
      0.02983913639912040561, \
      0.02983913639912040561, \
      0.02983913639912040561, \
      0.02983913639912040561, \
      0.70189657043113384827, \
      0.70189657043113384827, \
      0.70189657043113384827, \
      0.70189657043113384827, \
      0.05534643995880605266, \
      0.05534643995880605266, \
      0.05534643995880605266, \
      0.05534643995880605266, \
      0.58803180785949038523, \
      0.58803180785949038523, \
      0.58803180785949038523, \
      0.58803180785949038523, \
      0.35760040041294161028, \
      0.35760040041294161028, \
      0.35760040041294161028, \
      0.35760040041294161028, \
      0.63808499834946807994, \
      0.63808499834946807994, \
      0.63808499834946807994, \
      0.63808499834946807994, \
      0.11180046767985268863, \
      0.11180046767985268863, \
      0.11180046767985268863, \
      0.11180046767985268863, \
      0.45799604201643168144, \
      0.45799604201643168144, \
      0.45799604201643168144, \
      0.45799604201643168144, \
      0.81600939659279747573, \
      0.81600939659279747573, \
      0.81600939659279747573, \
      0.81600939659279747573, \
      0.05597294995869231404, \
      0.05597294995869231404, \
      0.05597294995869231404, \
      0.05597294995869231404, \
      0.12573106601315930941, \
      0.12573106601315930941, \
      0.12573106601315930941, \
      0.12573106601315930941, \
      0.10680199134354546875, \
      0.10680199134354546875, \
      0.10680199134354546875, \
      0.10680199134354546875, \
      0.64658620070888050968, \
      0.64658620070888050968, \
      0.64658620070888050968, \
      0.64658620070888050968, \
      0.25409417136336337473, \
      0.25409417136336337473, \
      0.25409417136336337473, \
      0.25409417136336337473, \
      0.05465918013108818363, \
      0.05465918013108818363, \
      0.05465918013108818363, \
      0.05465918013108818363, \
      0.45345939462310336232, \
      0.45345939462310336232, \
      0.45345939462310336232, \
      0.45345939462310336232, \
      0.78917660780490361816, \
      0.78917660780490361816, \
      0.78917660780490361816, \
      0.78917660780490361816, \
      0.18689788541072827055, \
      0.18689788541072827055, \
      0.18689788541072827055, \
      0.18689788541072827055, \
      0.18689788541072827055, \
      0.18689788541072827055, \
      0.18689788541072827055, \
      0.18689788541072827055, \
      0.01494308906905271982, \
      0.01494308906905271982, \
      0.01494308906905271982, \
      0.01494308906905271982, \
      0.01494308906905271982, \
      0.01494308906905271982, \
      0.01494308906905271982, \
      0.01494308906905271982, \
      0.39770246065633879651, \
      0.39770246065633879651, \
      0.39770246065633879651, \
      0.39770246065633879651, \
      0.39770246065633879651, \
      0.39770246065633879651, \
      0.39770246065633879651, \
      0.39770246065633879651, \
      0.06620609897561705037, \
      0.06620609897561705037, \
      0.06620609897561705037, \
      0.06620609897561705037, \
      0.06620609897561705037, \
      0.06620609897561705037, \
      0.06620609897561705037, \
      0.06620609897561705037, \
      0.01432824105432797292, \
      0.01432824105432797292, \
      0.01432824105432797292, \
      0.01432824105432797292, \
      0.01432824105432797292, \
      0.01432824105432797292, \
      0.01432824105432797292, \
      0.01432824105432797292, \
      0.55099638203681522430, \
      0.55099638203681522430, \
      0.55099638203681522430, \
      0.55099638203681522430, \
      0.55099638203681522430, \
      0.55099638203681522430, \
      0.55099638203681522430, \
      0.55099638203681522430, \
      0.28000300498314673048, \
      0.28000300498314673048, \
      0.28000300498314673048, \
      0.28000300498314673048, \
      0.28000300498314673048, \
      0.28000300498314673048, \
      0.28000300498314673048, \
      0.28000300498314673048, \
      0.24363304655846618196, \
      0.24363304655846618196, \
      0.24363304655846618196, \
      0.24363304655846618196, \
      0.24363304655846618196, \
      0.24363304655846618196, \
      0.24363304655846618196, \
      0.24363304655846618196, \
      0.07506931441576017439, \
      0.07506931441576017439, \
      0.07506931441576017439, \
      0.07506931441576017439, \
      0.07506931441576017439, \
      0.07506931441576017439, \
      0.07506931441576017439, \
      0.07506931441576017439, \
      0.05795059845476016602, \
      0.05795059845476016602, \
      0.05795059845476016602, \
      0.05795059845476016602, \
      0.05795059845476016602, \
      0.05795059845476016602, \
      0.05795059845476016602, \
      0.05795059845476016602, \
      0.35631158631326498298, \
      0.35631158631326498298, \
      0.35631158631326498298, \
      0.35631158631326498298, \
      0.35631158631326498298, \
      0.35631158631326498298, \
      0.35631158631326498298, \
      0.35631158631326498298, \
      0.00597525511512164969, \
      0.00597525511512164969, \
      0.00597525511512164969, \
      0.00597525511512164969, \
      0.00597525511512164969, \
      0.00597525511512164969, \
      0.00597525511512164969, \
      0.00597525511512164969, \
      0.01006650964023972882, \
      0.01006650964023972882, \
      0.01006650964023972882, \
      0.01006650964023972882, \
      0.01006650964023972882, \
      0.01006650964023972882, \
      0.01006650964023972882, \
      0.01006650964023972882, \
      0.47619683731341805322, \
      0.47619683731341805322, \
      0.47619683731341805322, \
      0.47619683731341805322, \
      0.47619683731341805322, \
      0.47619683731341805322, \
      0.47619683731341805322, \
      0.47619683731341805322, \
      0.05836635447459245785, \
      0.05836635447459245785, \
      0.05836635447459245785, \
      0.05836635447459245785, \
      0.05836635447459245785, \
      0.05836635447459245785, \
      0.05836635447459245785, \
      0.05836635447459245785, \
      0.16495562918454476087, \
      0.16495562918454476087, \
      0.16495562918454476087, \
      0.16495562918454476087, \
      0.16495562918454476087, \
      0.16495562918454476087, \
      0.16495562918454476087, \
      0.16495562918454476087, \
      0.15963984721353552398, \
      0.15963984721353552398, \
      0.15963984721353552398, \
      0.15963984721353552398, \
      0.15963984721353552398, \
      0.15963984721353552398, \
      0.15963984721353552398, \
      0.15963984721353552398, \
      0.01331460692424766938, \
      0.01331460692424766938, \
      0.01331460692424766938, \
      0.01331460692424766938, \
      0.01331460692424766938, \
      0.01331460692424766938, \
      0.01331460692424766938, \
      0.01331460692424766938 ] )

  w= np.array ( [ \
      0.00027672120207682897, \
      0.00734944257707945050, \
      0.00734944257707945050, \
      0.00734944257707945050, \
      0.00734944257707945050, \
      0.00148740437072881278, \
      0.00148740437072881278, \
      0.00148740437072881278, \
      0.00148740437072881278, \
      0.00387693638421187639, \
      0.00387693638421187639, \
      0.00387693638421187639, \
      0.00387693638421187639, \
      0.01030614824039441553, \
      0.01030614824039441553, \
      0.01030614824039441553, \
      0.01030614824039441553, \
      0.00272673198843895789, \
      0.00272673198843895789, \
      0.00272673198843895789, \
      0.00272673198843895789, \
      0.00244629213408558690, \
      0.00244629213408558690, \
      0.00244629213408558690, \
      0.00244629213408558690, \
      0.00554924399761744409, \
      0.00554924399761744409, \
      0.00554924399761744409, \
      0.00554924399761744409, \
      0.00502262417466419701, \
      0.00502262417466419701, \
      0.00502262417466419701, \
      0.00502262417466419701, \
      0.00067111170084793834, \
      0.00067111170084793834, \
      0.00067111170084793834, \
      0.00067111170084793834, \
      0.00316873518673754882, \
      0.00316873518673754882, \
      0.00316873518673754882, \
      0.00316873518673754882, \
      0.00230707268685653678, \
      0.00230707268685653678, \
      0.00230707268685653678, \
      0.00230707268685653678, \
      0.00223355434035575010, \
      0.00223355434035575010, \
      0.00223355434035575010, \
      0.00223355434035575010, \
      0.00228685693132126217, \
      0.00228685693132126217, \
      0.00228685693132126217, \
      0.00228685693132126217, \
      0.00583888699964928409, \
      0.00583888699964928409, \
      0.00583888699964928409, \
      0.00583888699964928409, \
      0.00412038756118528714, \
      0.00412038756118528714, \
      0.00412038756118528714, \
      0.00412038756118528714, \
      0.00173037948168740284, \
      0.00173037948168740284, \
      0.00173037948168740284, \
      0.00173037948168740284, \
      0.00410680906602167630, \
      0.00410680906602167630, \
      0.00410680906602167630, \
      0.00410680906602167630, \
      0.00635438948067259222, \
      0.00635438948067259222, \
      0.00635438948067259222, \
      0.00635438948067259222, \
      0.00043262101844333546, \
      0.00043262101844333546, \
      0.00043262101844333546, \
      0.00043262101844333546, \
      0.00345263292981801964, \
      0.00345263292981801964, \
      0.00345263292981801964, \
      0.00345263292981801964, \
      0.00424071455736505301, \
      0.00424071455736505301, \
      0.00424071455736505301, \
      0.00424071455736505301, \
      0.00340526631678994204, \
      0.00340526631678994204, \
      0.00340526631678994204, \
      0.00340526631678994204, \
      0.00700942929302337137, \
      0.00700942929302337137, \
      0.00700942929302337137, \
      0.00700942929302337137, \
      0.00371184509938299149, \
      0.00371184509938299149, \
      0.00371184509938299149, \
      0.00371184509938299149, \
      0.00655769989421819445, \
      0.00655769989421819445, \
      0.00655769989421819445, \
      0.00655769989421819445, \
      0.00169996297833195664, \
      0.00169996297833195664, \
      0.00169996297833195664, \
      0.00169996297833195664, \
      0.00134740004835729398, \
      0.00134740004835729398, \
      0.00134740004835729398, \
      0.00134740004835729398, \
      0.00363396950461261376, \
      0.00363396950461261376, \
      0.00363396950461261376, \
      0.00363396950461261376, \
      0.00121619462900863910, \
      0.00121619462900863910, \
      0.00121619462900863910, \
      0.00121619462900863910, \
      0.00549579708316756677, \
      0.00549579708316756677, \
      0.00549579708316756677, \
      0.00549579708316756677, \
      0.00097330273562793888, \
      0.00097330273562793888, \
      0.00097330273562793888, \
      0.00097330273562793888, \
      0.00725393003232855348, \
      0.00725393003232855348, \
      0.00725393003232855348, \
      0.00725393003232855348, \
      0.00261600067059077025, \
      0.00261600067059077025, \
      0.00261600067059077025, \
      0.00261600067059077025, \
      0.00548333692337083910, \
      0.00548333692337083910, \
      0.00548333692337083910, \
      0.00548333692337083910, \
      0.00150187064516151079, \
      0.00150187064516151079, \
      0.00150187064516151079, \
      0.00150187064516151079, \
      0.00224211276351870626, \
      0.00224211276351870626, \
      0.00224211276351870626, \
      0.00224211276351870626, \
      0.00224211276351870626, \
      0.00224211276351870626, \
      0.00224211276351870626, \
      0.00224211276351870626, \
      0.00254357012140252583, \
      0.00254357012140252583, \
      0.00254357012140252583, \
      0.00254357012140252583, \
      0.00254357012140252583, \
      0.00254357012140252583, \
      0.00254357012140252583, \
      0.00254357012140252583, \
      0.00536144481406866224, \
      0.00536144481406866224, \
      0.00536144481406866224, \
      0.00536144481406866224, \
      0.00536144481406866224, \
      0.00536144481406866224, \
      0.00536144481406866224, \
      0.00536144481406866224, \
      0.00150566238487620605, \
      0.00150566238487620605, \
      0.00150566238487620605, \
      0.00150566238487620605, \
      0.00150566238487620605, \
      0.00150566238487620605, \
      0.00150566238487620605, \
      0.00150566238487620605, \
      0.00112651998000158019, \
      0.00112651998000158019, \
      0.00112651998000158019, \
      0.00112651998000158019, \
      0.00112651998000158019, \
      0.00112651998000158019, \
      0.00112651998000158019, \
      0.00112651998000158019, \
      0.00283697215367184055, \
      0.00283697215367184055, \
      0.00283697215367184055, \
      0.00283697215367184055, \
      0.00283697215367184055, \
      0.00283697215367184055, \
      0.00283697215367184055, \
      0.00283697215367184055, \
      0.00423443304160556894, \
      0.00423443304160556894, \
      0.00423443304160556894, \
      0.00423443304160556894, \
      0.00423443304160556894, \
      0.00423443304160556894, \
      0.00423443304160556894, \
      0.00423443304160556894, \
      0.00318414785741326324, \
      0.00318414785741326324, \
      0.00318414785741326324, \
      0.00318414785741326324, \
      0.00318414785741326324, \
      0.00318414785741326324, \
      0.00318414785741326324, \
      0.00318414785741326324, \
      0.00402977998773114843, \
      0.00402977998773114843, \
      0.00402977998773114843, \
      0.00402977998773114843, \
      0.00402977998773114843, \
      0.00402977998773114843, \
      0.00402977998773114843, \
      0.00402977998773114843, \
      0.00366973681687540396, \
      0.00366973681687540396, \
      0.00366973681687540396, \
      0.00366973681687540396, \
      0.00366973681687540396, \
      0.00366973681687540396, \
      0.00366973681687540396, \
      0.00366973681687540396, \
      0.00248888728757531682, \
      0.00248888728757531682, \
      0.00248888728757531682, \
      0.00248888728757531682, \
      0.00248888728757531682, \
      0.00248888728757531682, \
      0.00248888728757531682, \
      0.00248888728757531682, \
      0.00048888922605729013, \
      0.00048888922605729013, \
      0.00048888922605729013, \
      0.00048888922605729013, \
      0.00048888922605729013, \
      0.00048888922605729013, \
      0.00048888922605729013, \
      0.00048888922605729013, \
      0.00325264515509947555, \
      0.00325264515509947555, \
      0.00325264515509947555, \
      0.00325264515509947555, \
      0.00325264515509947555, \
      0.00325264515509947555, \
      0.00325264515509947555, \
      0.00325264515509947555, \
      0.00495505909145715732, \
      0.00495505909145715732, \
      0.00495505909145715732, \
      0.00495505909145715732, \
      0.00495505909145715732, \
      0.00495505909145715732, \
      0.00495505909145715732, \
      0.00495505909145715732, \
      0.00457024218025166729, \
      0.00457024218025166729, \
      0.00457024218025166729, \
      0.00457024218025166729, \
      0.00457024218025166729, \
      0.00457024218025166729, \
      0.00457024218025166729, \
      0.00457024218025166729, \
      0.00481061764241353957, \
      0.00481061764241353957, \
      0.00481061764241353957, \
      0.00481061764241353957, \
      0.00481061764241353957, \
      0.00481061764241353957, \
      0.00481061764241353957, \
      0.00481061764241353957, \
      0.00538791794721728626, \
      0.00538791794721728626, \
      0.00538791794721728626, \
      0.00538791794721728626, \
      0.00538791794721728626, \
      0.00538791794721728626, \
      0.00538791794721728626, \
      0.00538791794721728626, \
      0.00246928056742645339, \
      0.00246928056742645339, \
      0.00246928056742645339, \
      0.00246928056742645339, \
      0.00246928056742645339, \
      0.00246928056742645339, \
      0.00246928056742645339, \
      0.00246928056742645339 ] )

  return x, y, z, w

def rule17 ( ):

#*****************************************************************************80
#
## rule17() returns the pyramid quadrature rule of precision 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.95241408581244602072, \
      0.00000000000000000000, \
     -0.95241408581244602072, \
      0.00000000000000000000, \
      0.08275692125030435775, \
      0.00000000000000000000, \
     -0.08275692125030435775, \
      0.00000000000000000000, \
      0.26578545043127727032, \
      0.00000000000000000000, \
     -0.26578545043127727032, \
      0.00000000000000000000, \
      0.81155940028479511827, \
      0.00000000000000000000, \
     -0.81155940028479511827, \
      0.00000000000000000000, \
      0.35232799954016802424, \
      0.00000000000000000000, \
     -0.35232799954016802424, \
      0.00000000000000000000, \
      0.60303771218972423984, \
      0.00000000000000000000, \
     -0.60303771218972423984, \
      0.00000000000000000000, \
      0.78402604202159054125, \
      0.00000000000000000000, \
     -0.78402604202159054125, \
      0.00000000000000000000, \
      0.49346472198646390561, \
      0.00000000000000000000, \
     -0.49346472198646390561, \
      0.00000000000000000000, \
      0.35038751648906635294, \
      0.00000000000000000000, \
     -0.35038751648906635294, \
      0.00000000000000000000, \
      0.00336404312107426752, \
      0.00000000000000000000, \
     -0.00336404312107426752, \
      0.00000000000000000000, \
      0.43074512679067450405, \
      0.00000000000000000000, \
     -0.43074512679067450405, \
      0.00000000000000000000, \
      0.59254801282947688890, \
      0.00000000000000000000, \
     -0.59254801282947688890, \
      0.00000000000000000000, \
      0.22550686036585329552, \
      0.00000000000000000000, \
     -0.22550686036585329552, \
      0.00000000000000000000, \
      0.63975863740336180729, \
     -0.63975863740336180729, \
      0.63975863740336180729, \
     -0.63975863740336180729, \
      0.16463474879631256886, \
     -0.16463474879631256886, \
      0.16463474879631256886, \
     -0.16463474879631256886, \
      0.49303563319629611916, \
     -0.49303563319629611916, \
      0.49303563319629611916, \
     -0.49303563319629611916, \
      0.74791280396309745004, \
     -0.74791280396309745004, \
      0.74791280396309745004, \
     -0.74791280396309745004, \
      0.26251317864285966808, \
     -0.26251317864285966808, \
      0.26251317864285966808, \
     -0.26251317864285966808, \
      0.17484215589868074003, \
     -0.17484215589868074003, \
      0.17484215589868074003, \
     -0.17484215589868074003, \
      0.27602468785670569718, \
     -0.27602468785670569718, \
      0.27602468785670569718, \
     -0.27602468785670569718, \
      0.43512552408987620334, \
     -0.43512552408987620334, \
      0.43512552408987620334, \
     -0.43512552408987620334, \
      0.95307694157738065410, \
     -0.95307694157738065410, \
      0.95307694157738065410, \
     -0.95307694157738065410, \
      0.48425597905194911474, \
     -0.48425597905194911474, \
      0.48425597905194911474, \
     -0.48425597905194911474, \
      0.29381061843327571648, \
     -0.29381061843327571648, \
      0.29381061843327571648, \
     -0.29381061843327571648, \
      0.16057200503692023452, \
     -0.16057200503692023452, \
      0.16057200503692023452, \
     -0.16057200503692023452, \
      0.81014529214207364749, \
     -0.81014529214207364749, \
      0.81014529214207364749, \
     -0.81014529214207364749, \
      0.18009325754915589402, \
     -0.18009325754915589402, \
      0.18009325754915589402, \
     -0.18009325754915589402, \
      0.50136799407459931022, \
     -0.50136799407459931022, \
      0.50136799407459931022, \
     -0.50136799407459931022, \
      0.92284407855436589863, \
     -0.92284407855436589863, \
      0.92284407855436589863, \
     -0.92284407855436589863, \
      0.32077249570607596629, \
     -0.32077249570607596629, \
      0.32077249570607596629, \
     -0.32077249570607596629, \
      0.02145401504974505866, \
     -0.02145401504974505866, \
      0.02145401504974505866, \
     -0.02145401504974505866, \
      0.65293078741937671250, \
     -0.65293078741937671250, \
      0.65293078741937671250, \
     -0.65293078741937671250, \
      0.38109206736816036987, \
     -0.38109206736816036987, \
      0.38109206736816036987, \
     -0.38109206736816036987, \
      0.41413124714030785656, \
     -0.41413124714030785656, \
      0.41413124714030785656, \
     -0.41413124714030785656, \
      0.14311887945931867083, \
     -0.14311887945931867083, \
      0.14311887945931867083, \
     -0.14311887945931867083, \
      0.06816745760360433393, \
     -0.06816745760360433393, \
      0.06816745760360433393, \
     -0.06816745760360433393, \
      0.22977242422012536527, \
     -0.22977242422012536527, \
      0.22977242422012536527, \
     -0.22977242422012536527, \
      0.78211200270072955831, \
     -0.78211200270072955831, \
      0.78211200270072955831, \
     -0.78211200270072955831, \
      0.47646421490609353055, \
     -0.47646421490609353055, \
      0.47646421490609353055, \
     -0.47646421490609353055, \
      0.66550056762002873789, \
     -0.66550056762002873789, \
      0.66550056762002873789, \
     -0.66550056762002873789, \
      0.15755371600385464914, \
     -0.15755371600385464914, \
      0.15755371600385464914, \
     -0.15755371600385464914, \
      0.74760255490899130137, \
      0.13357335558335847736, \
     -0.74760255490899130137, \
      0.13357335558335847736, \
      0.74760255490899130137, \
     -0.13357335558335847736, \
     -0.74760255490899130137, \
     -0.13357335558335847736, \
      0.64024497237564748087, \
      0.36978998725981265805, \
     -0.64024497237564748087, \
      0.36978998725981265805, \
      0.64024497237564748087, \
     -0.36978998725981265805, \
     -0.64024497237564748087, \
     -0.36978998725981265805, \
      0.27725002720745439699, \
      0.65880359279798383909, \
     -0.27725002720745439699, \
      0.65880359279798383909, \
      0.27725002720745439699, \
     -0.65880359279798383909, \
     -0.27725002720745439699, \
     -0.65880359279798383909, \
      0.88435969563492811130, \
      0.76901445510268306993, \
     -0.88435969563492811130, \
      0.76901445510268306993, \
      0.88435969563492811130, \
     -0.76901445510268306993, \
     -0.88435969563492811130, \
     -0.76901445510268306993, \
      0.95432083454417460100, \
      0.27565292566365701132, \
     -0.95432083454417460100, \
      0.27565292566365701132, \
      0.95432083454417460100, \
     -0.27565292566365701132, \
     -0.95432083454417460100, \
     -0.27565292566365701132, \
      0.19610686376179234380, \
      0.48815934289407264535, \
     -0.19610686376179234380, \
      0.48815934289407264535, \
      0.19610686376179234380, \
     -0.48815934289407264535, \
     -0.19610686376179234380, \
     -0.48815934289407264535, \
      0.52539286886562275303, \
      0.90365402298313357576, \
     -0.52539286886562275303, \
      0.90365402298313357576, \
      0.52539286886562275303, \
     -0.90365402298313357576, \
     -0.52539286886562275303, \
     -0.90365402298313357576, \
      0.78710506457062645591, \
      0.53056669085425134380, \
     -0.78710506457062645591, \
      0.53056669085425134380, \
      0.78710506457062645591, \
     -0.53056669085425134380, \
     -0.78710506457062645591, \
     -0.53056669085425134380, \
      0.87305124922384047537, \
      0.58249614598785404151, \
     -0.87305124922384047537, \
      0.58249614598785404151, \
      0.87305124922384047537, \
     -0.58249614598785404151, \
     -0.87305124922384047537, \
     -0.58249614598785404151, \
      0.49539855010659772372, \
      0.21910184606142177333, \
     -0.49539855010659772372, \
      0.21910184606142177333, \
      0.49539855010659772372, \
     -0.21910184606142177333, \
     -0.49539855010659772372, \
     -0.21910184606142177333, \
      0.86957254282469464979, \
      0.30557223260338794990, \
     -0.86957254282469464979, \
      0.30557223260338794990, \
      0.86957254282469464979, \
     -0.30557223260338794990, \
     -0.86957254282469464979, \
     -0.30557223260338794990, \
      0.82556821539161207024, \
      0.18201665219265533713, \
     -0.82556821539161207024, \
      0.18201665219265533713, \
      0.82556821539161207024, \
     -0.18201665219265533713, \
     -0.82556821539161207024, \
     -0.18201665219265533713, \
      0.22633675831897015485, \
      0.35538499166679399233, \
     -0.22633675831897015485, \
      0.35538499166679399233, \
      0.22633675831897015485, \
     -0.35538499166679399233, \
     -0.22633675831897015485, \
     -0.35538499166679399233, \
      0.55136786560508410648, \
      0.74868759522365924131, \
     -0.55136786560508410648, \
      0.74868759522365924131, \
      0.55136786560508410648, \
     -0.74868759522365924131, \
     -0.55136786560508410648, \
     -0.74868759522365924131, \
      0.64168041273857601148, \
      0.25896549169892302267, \
     -0.64168041273857601148, \
      0.25896549169892302267, \
      0.64168041273857601148, \
     -0.25896549169892302267, \
     -0.64168041273857601148, \
     -0.25896549169892302267, \
      0.48623936010342988512, \
      0.11286859018565884027, \
     -0.48623936010342988512, \
      0.11286859018565884027, \
      0.48623936010342988512, \
     -0.11286859018565884027, \
     -0.48623936010342988512, \
     -0.11286859018565884027, \
      0.42728691837450794022, \
      0.62836164145805561976, \
     -0.42728691837450794022, \
      0.62836164145805561976, \
      0.42728691837450794022, \
     -0.62836164145805561976, \
     -0.42728691837450794022, \
     -0.62836164145805561976, \
      0.97870776397134839897, \
      0.73410552715894472620, \
     -0.97870776397134839897, \
      0.73410552715894472620, \
      0.97870776397134839897, \
     -0.73410552715894472620, \
     -0.97870776397134839897, \
     -0.73410552715894472620, \
      0.70585052586641572336, \
      0.41358916179473048658, \
     -0.70585052586641572336, \
      0.41358916179473048658, \
      0.70585052586641572336, \
     -0.41358916179473048658, \
     -0.70585052586641572336, \
     -0.41358916179473048658 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.95241408581244602072, \
      0.00000000000000000000, \
     -0.95241408581244602072, \
      0.00000000000000000000, \
      0.08275692125030435775, \
      0.00000000000000000000, \
     -0.08275692125030435775, \
      0.00000000000000000000, \
      0.26578545043127727032, \
      0.00000000000000000000, \
     -0.26578545043127727032, \
      0.00000000000000000000, \
      0.81155940028479511827, \
      0.00000000000000000000, \
     -0.81155940028479511827, \
      0.00000000000000000000, \
      0.35232799954016802424, \
      0.00000000000000000000, \
     -0.35232799954016802424, \
      0.00000000000000000000, \
      0.60303771218972423984, \
      0.00000000000000000000, \
     -0.60303771218972423984, \
      0.00000000000000000000, \
      0.78402604202159054125, \
      0.00000000000000000000, \
     -0.78402604202159054125, \
      0.00000000000000000000, \
      0.49346472198646390561, \
      0.00000000000000000000, \
     -0.49346472198646390561, \
      0.00000000000000000000, \
      0.35038751648906635294, \
      0.00000000000000000000, \
     -0.35038751648906635294, \
      0.00000000000000000000, \
      0.00336404312107426752, \
      0.00000000000000000000, \
     -0.00336404312107426752, \
      0.00000000000000000000, \
      0.43074512679067450405, \
      0.00000000000000000000, \
     -0.43074512679067450405, \
      0.00000000000000000000, \
      0.59254801282947688890, \
      0.00000000000000000000, \
     -0.59254801282947688890, \
      0.00000000000000000000, \
      0.22550686036585329552, \
      0.00000000000000000000, \
     -0.22550686036585329552, \
      0.63975863740336180729, \
      0.63975863740336180729, \
     -0.63975863740336180729, \
     -0.63975863740336180729, \
      0.16463474879631256886, \
      0.16463474879631256886, \
     -0.16463474879631256886, \
     -0.16463474879631256886, \
      0.49303563319629611916, \
      0.49303563319629611916, \
     -0.49303563319629611916, \
     -0.49303563319629611916, \
      0.74791280396309745004, \
      0.74791280396309745004, \
     -0.74791280396309745004, \
     -0.74791280396309745004, \
      0.26251317864285966808, \
      0.26251317864285966808, \
     -0.26251317864285966808, \
     -0.26251317864285966808, \
      0.17484215589868074003, \
      0.17484215589868074003, \
     -0.17484215589868074003, \
     -0.17484215589868074003, \
      0.27602468785670569718, \
      0.27602468785670569718, \
     -0.27602468785670569718, \
     -0.27602468785670569718, \
      0.43512552408987620334, \
      0.43512552408987620334, \
     -0.43512552408987620334, \
     -0.43512552408987620334, \
      0.95307694157738065410, \
      0.95307694157738065410, \
     -0.95307694157738065410, \
     -0.95307694157738065410, \
      0.48425597905194911474, \
      0.48425597905194911474, \
     -0.48425597905194911474, \
     -0.48425597905194911474, \
      0.29381061843327571648, \
      0.29381061843327571648, \
     -0.29381061843327571648, \
     -0.29381061843327571648, \
      0.16057200503692023452, \
      0.16057200503692023452, \
     -0.16057200503692023452, \
     -0.16057200503692023452, \
      0.81014529214207364749, \
      0.81014529214207364749, \
     -0.81014529214207364749, \
     -0.81014529214207364749, \
      0.18009325754915589402, \
      0.18009325754915589402, \
     -0.18009325754915589402, \
     -0.18009325754915589402, \
      0.50136799407459931022, \
      0.50136799407459931022, \
     -0.50136799407459931022, \
     -0.50136799407459931022, \
      0.92284407855436589863, \
      0.92284407855436589863, \
     -0.92284407855436589863, \
     -0.92284407855436589863, \
      0.32077249570607596629, \
      0.32077249570607596629, \
     -0.32077249570607596629, \
     -0.32077249570607596629, \
      0.02145401504974505866, \
      0.02145401504974505866, \
     -0.02145401504974505866, \
     -0.02145401504974505866, \
      0.65293078741937671250, \
      0.65293078741937671250, \
     -0.65293078741937671250, \
     -0.65293078741937671250, \
      0.38109206736816036987, \
      0.38109206736816036987, \
     -0.38109206736816036987, \
     -0.38109206736816036987, \
      0.41413124714030785656, \
      0.41413124714030785656, \
     -0.41413124714030785656, \
     -0.41413124714030785656, \
      0.14311887945931867083, \
      0.14311887945931867083, \
     -0.14311887945931867083, \
     -0.14311887945931867083, \
      0.06816745760360433393, \
      0.06816745760360433393, \
     -0.06816745760360433393, \
     -0.06816745760360433393, \
      0.22977242422012536527, \
      0.22977242422012536527, \
     -0.22977242422012536527, \
     -0.22977242422012536527, \
      0.78211200270072955831, \
      0.78211200270072955831, \
     -0.78211200270072955831, \
     -0.78211200270072955831, \
      0.47646421490609353055, \
      0.47646421490609353055, \
     -0.47646421490609353055, \
     -0.47646421490609353055, \
      0.66550056762002873789, \
      0.66550056762002873789, \
     -0.66550056762002873789, \
     -0.66550056762002873789, \
      0.15755371600385464914, \
      0.15755371600385464914, \
     -0.15755371600385464914, \
     -0.15755371600385464914, \
      0.13357335558335847736, \
      0.74760255490899130137, \
      0.13357335558335847736, \
     -0.74760255490899130137, \
     -0.13357335558335847736, \
      0.74760255490899130137, \
     -0.13357335558335847736, \
     -0.74760255490899130137, \
      0.36978998725981265805, \
      0.64024497237564748087, \
      0.36978998725981265805, \
     -0.64024497237564748087, \
     -0.36978998725981265805, \
      0.64024497237564748087, \
     -0.36978998725981265805, \
     -0.64024497237564748087, \
      0.65880359279798383909, \
      0.27725002720745439699, \
      0.65880359279798383909, \
     -0.27725002720745439699, \
     -0.65880359279798383909, \
      0.27725002720745439699, \
     -0.65880359279798383909, \
     -0.27725002720745439699, \
      0.76901445510268306993, \
      0.88435969563492811130, \
      0.76901445510268306993, \
     -0.88435969563492811130, \
     -0.76901445510268306993, \
      0.88435969563492811130, \
     -0.76901445510268306993, \
     -0.88435969563492811130, \
      0.27565292566365701132, \
      0.95432083454417460100, \
      0.27565292566365701132, \
     -0.95432083454417460100, \
     -0.27565292566365701132, \
      0.95432083454417460100, \
     -0.27565292566365701132, \
     -0.95432083454417460100, \
      0.48815934289407264535, \
      0.19610686376179234380, \
      0.48815934289407264535, \
     -0.19610686376179234380, \
     -0.48815934289407264535, \
      0.19610686376179234380, \
     -0.48815934289407264535, \
     -0.19610686376179234380, \
      0.90365402298313357576, \
      0.52539286886562275303, \
      0.90365402298313357576, \
     -0.52539286886562275303, \
     -0.90365402298313357576, \
      0.52539286886562275303, \
     -0.90365402298313357576, \
     -0.52539286886562275303, \
      0.53056669085425134380, \
      0.78710506457062645591, \
      0.53056669085425134380, \
     -0.78710506457062645591, \
     -0.53056669085425134380, \
      0.78710506457062645591, \
     -0.53056669085425134380, \
     -0.78710506457062645591, \
      0.58249614598785404151, \
      0.87305124922384047537, \
      0.58249614598785404151, \
     -0.87305124922384047537, \
     -0.58249614598785404151, \
      0.87305124922384047537, \
     -0.58249614598785404151, \
     -0.87305124922384047537, \
      0.21910184606142177333, \
      0.49539855010659772372, \
      0.21910184606142177333, \
     -0.49539855010659772372, \
     -0.21910184606142177333, \
      0.49539855010659772372, \
     -0.21910184606142177333, \
     -0.49539855010659772372, \
      0.30557223260338794990, \
      0.86957254282469464979, \
      0.30557223260338794990, \
     -0.86957254282469464979, \
     -0.30557223260338794990, \
      0.86957254282469464979, \
     -0.30557223260338794990, \
     -0.86957254282469464979, \
      0.18201665219265533713, \
      0.82556821539161207024, \
      0.18201665219265533713, \
     -0.82556821539161207024, \
     -0.18201665219265533713, \
      0.82556821539161207024, \
     -0.18201665219265533713, \
     -0.82556821539161207024, \
      0.35538499166679399233, \
      0.22633675831897015485, \
      0.35538499166679399233, \
     -0.22633675831897015485, \
     -0.35538499166679399233, \
      0.22633675831897015485, \
     -0.35538499166679399233, \
     -0.22633675831897015485, \
      0.74868759522365924131, \
      0.55136786560508410648, \
      0.74868759522365924131, \
     -0.55136786560508410648, \
     -0.74868759522365924131, \
      0.55136786560508410648, \
     -0.74868759522365924131, \
     -0.55136786560508410648, \
      0.25896549169892302267, \
      0.64168041273857601148, \
      0.25896549169892302267, \
     -0.64168041273857601148, \
     -0.25896549169892302267, \
      0.64168041273857601148, \
     -0.25896549169892302267, \
     -0.64168041273857601148, \
      0.11286859018565884027, \
      0.48623936010342988512, \
      0.11286859018565884027, \
     -0.48623936010342988512, \
     -0.11286859018565884027, \
      0.48623936010342988512, \
     -0.11286859018565884027, \
     -0.48623936010342988512, \
      0.62836164145805561976, \
      0.42728691837450794022, \
      0.62836164145805561976, \
     -0.42728691837450794022, \
     -0.62836164145805561976, \
      0.42728691837450794022, \
     -0.62836164145805561976, \
     -0.42728691837450794022, \
      0.73410552715894472620, \
      0.97870776397134839897, \
      0.73410552715894472620, \
     -0.97870776397134839897, \
     -0.73410552715894472620, \
      0.97870776397134839897, \
     -0.73410552715894472620, \
     -0.97870776397134839897, \
      0.41358916179473048658, \
      0.70585052586641572336, \
      0.41358916179473048658, \
     -0.70585052586641572336, \
     -0.41358916179473048658, \
      0.70585052586641572336, \
     -0.41358916179473048658, \
     -0.70585052586641572336 ] )

  z = np.array ( [ \
      0.97220323387036922114, \
      0.63870352926681406291, \
      0.68020043208055336326, \
      0.04194980824924493534, \
      0.04194980824924493534, \
      0.04194980824924493534, \
      0.04194980824924493534, \
      0.90141183204156405395, \
      0.90141183204156405395, \
      0.90141183204156405395, \
      0.90141183204156405395, \
      0.68432529322768964608, \
      0.68432529322768964608, \
      0.68432529322768964608, \
      0.68432529322768964608, \
      0.00000008245324867689, \
      0.00000008245324867689, \
      0.00000008245324867689, \
      0.00000008245324867689, \
      0.55417390873649197136, \
      0.55417390873649197136, \
      0.55417390873649197136, \
      0.55417390873649197136, \
      0.36258805988768089135, \
      0.36258805988768089135, \
      0.36258805988768089135, \
      0.36258805988768089135, \
      0.13875708503462674814, \
      0.13875708503462674814, \
      0.13875708503462674814, \
      0.13875708503462674814, \
      0.24260167486456202246, \
      0.24260167486456202246, \
      0.24260167486456202246, \
      0.24260167486456202246, \
      0.40130775806887936108, \
      0.40130775806887936108, \
      0.40130775806887936108, \
      0.40130775806887936108, \
      0.38152973269372325582, \
      0.38152973269372325582, \
      0.38152973269372325582, \
      0.38152973269372325582, \
      0.11901456915448617446, \
      0.11901456915448617446, \
      0.11901456915448617446, \
      0.11901456915448617446, \
      0.04928012549325393871, \
      0.04928012549325393871, \
      0.04928012549325393871, \
      0.04928012549325393871, \
      0.76206391519358240849, \
      0.76206391519358240849, \
      0.76206391519358240849, \
      0.76206391519358240849, \
      0.31153469497121605292, \
      0.31153469497121605292, \
      0.31153469497121605292, \
      0.31153469497121605292, \
      0.25650991726217964306, \
      0.25650991726217964306, \
      0.25650991726217964306, \
      0.25650991726217964306, \
      0.07449733603189459541, \
      0.07449733603189459541, \
      0.07449733603189459541, \
      0.07449733603189459541, \
      0.00130788548084566922, \
      0.00130788548084566922, \
      0.00130788548084566922, \
      0.00130788548084566922, \
      0.52858580218461959088, \
      0.52858580218461959088, \
      0.52858580218461959088, \
      0.52858580218461959088, \
      0.00955221072473505343, \
      0.00955221072473505343, \
      0.00955221072473505343, \
      0.00955221072473505343, \
      0.34142989905969745035, \
      0.34142989905969745035, \
      0.34142989905969745035, \
      0.34142989905969745035, \
      0.00027022925967801637, \
      0.00027022925967801637, \
      0.00027022925967801637, \
      0.00027022925967801637, \
      0.04692242455320395911, \
      0.04692242455320395911, \
      0.04692242455320395911, \
      0.04692242455320395911, \
      0.34449713283505384309, \
      0.34449713283505384309, \
      0.34449713283505384309, \
      0.34449713283505384309, \
      0.66811923014208407512, \
      0.66811923014208407512, \
      0.66811923014208407512, \
      0.66811923014208407512, \
      0.67391287157124502016, \
      0.67391287157124502016, \
      0.67391287157124502016, \
      0.67391287157124502016, \
      0.03437584591482227558, \
      0.03437584591482227558, \
      0.03437584591482227558, \
      0.03437584591482227558, \
      0.15542872578297051156, \
      0.15542872578297051156, \
      0.15542872578297051156, \
      0.15542872578297051156, \
      0.26971828733855934823, \
      0.26971828733855934823, \
      0.26971828733855934823, \
      0.26971828733855934823, \
      0.01181428825288092545, \
      0.01181428825288092545, \
      0.01181428825288092545, \
      0.01181428825288092545, \
      0.06366317285532444026, \
      0.06366317285532444026, \
      0.06366317285532444026, \
      0.06366317285532444026, \
      0.06762724457801919109, \
      0.06762724457801919109, \
      0.06762724457801919109, \
      0.06762724457801919109, \
      0.20149664605408518225, \
      0.20149664605408518225, \
      0.20149664605408518225, \
      0.20149664605408518225, \
      0.48586744666719888786, \
      0.48586744666719888786, \
      0.48586744666719888786, \
      0.48586744666719888786, \
      0.19071052464250978775, \
      0.19071052464250978775, \
      0.19071052464250978775, \
      0.19071052464250978775, \
      0.51037375853206956577, \
      0.51037375853206956577, \
      0.51037375853206956577, \
      0.51037375853206956577, \
      0.80351245513246505325, \
      0.80351245513246505325, \
      0.80351245513246505325, \
      0.80351245513246505325, \
      0.04121355156423638089, \
      0.04121355156423638089, \
      0.04121355156423638089, \
      0.04121355156423638089, \
      0.17760016176122497833, \
      0.17760016176122497833, \
      0.17760016176122497833, \
      0.17760016176122497833, \
      0.48439012439328182902, \
      0.48439012439328182902, \
      0.48439012439328182902, \
      0.48439012439328182902, \
      0.04796979480806326523, \
      0.04796979480806326523, \
      0.04796979480806326523, \
      0.04796979480806326523, \
      0.80108123458344093759, \
      0.80108123458344093759, \
      0.80108123458344093759, \
      0.80108123458344093759, \
      0.24101422703502115019, \
      0.24101422703502115019, \
      0.24101422703502115019, \
      0.24101422703502115019, \
      0.24101422703502115019, \
      0.24101422703502115019, \
      0.24101422703502115019, \
      0.24101422703502115019, \
      0.01069891762813818432, \
      0.01069891762813818432, \
      0.01069891762813818432, \
      0.01069891762813818432, \
      0.01069891762813818432, \
      0.01069891762813818432, \
      0.01069891762813818432, \
      0.01069891762813818432, \
      0.23988631383389671936, \
      0.23988631383389671936, \
      0.23988631383389671936, \
      0.23988631383389671936, \
      0.23988631383389671936, \
      0.23988631383389671936, \
      0.23988631383389671936, \
      0.23988631383389671936, \
      0.08514410320936129095, \
      0.08514410320936129095, \
      0.08514410320936129095, \
      0.08514410320936129095, \
      0.08514410320936129095, \
      0.08514410320936129095, \
      0.08514410320936129095, \
      0.08514410320936129095, \
      0.00847110534891616467, \
      0.00847110534891616467, \
      0.00847110534891616467, \
      0.00847110534891616467, \
      0.00847110534891616467, \
      0.00847110534891616467, \
      0.00847110534891616467, \
      0.00847110534891616467, \
      0.49562245065536153499, \
      0.49562245065536153499, \
      0.49562245065536153499, \
      0.49562245065536153499, \
      0.49562245065536153499, \
      0.49562245065536153499, \
      0.49562245065536153499, \
      0.49562245065536153499, \
      0.04642983560786508729, \
      0.04642983560786508729, \
      0.04642983560786508729, \
      0.04642983560786508729, \
      0.04642983560786508729, \
      0.04642983560786508729, \
      0.04642983560786508729, \
      0.04642983560786508729, \
      0.19656151852896430743, \
      0.19656151852896430743, \
      0.19656151852896430743, \
      0.19656151852896430743, \
      0.19656151852896430743, \
      0.19656151852896430743, \
      0.19656151852896430743, \
      0.19656151852896430743, \
      0.00687572309208568308, \
      0.00687572309208568308, \
      0.00687572309208568308, \
      0.00687572309208568308, \
      0.00687572309208568308, \
      0.00687572309208568308, \
      0.00687572309208568308, \
      0.00687572309208568308, \
      0.38670513013019941484, \
      0.38670513013019941484, \
      0.38670513013019941484, \
      0.38670513013019941484, \
      0.38670513013019941484, \
      0.38670513013019941484, \
      0.38670513013019941484, \
      0.38670513013019941484, \
      0.10896106798490250156, \
      0.10896106798490250156, \
      0.10896106798490250156, \
      0.10896106798490250156, \
      0.10896106798490250156, \
      0.10896106798490250156, \
      0.10896106798490250156, \
      0.10896106798490250156, \
      0.04416884971526349735, \
      0.04416884971526349735, \
      0.04416884971526349735, \
      0.04416884971526349735, \
      0.04416884971526349735, \
      0.04416884971526349735, \
      0.04416884971526349735, \
      0.04416884971526349735, \
      0.62489254847899400325, \
      0.62489254847899400325, \
      0.62489254847899400325, \
      0.62489254847899400325, \
      0.62489254847899400325, \
      0.62489254847899400325, \
      0.62489254847899400325, \
      0.62489254847899400325, \
      0.11727329599993376041, \
      0.11727329599993376041, \
      0.11727329599993376041, \
      0.11727329599993376041, \
      0.11727329599993376041, \
      0.11727329599993376041, \
      0.11727329599993376041, \
      0.11727329599993376041, \
      0.11958436259454885420, \
      0.11958436259454885420, \
      0.11958436259454885420, \
      0.11958436259454885420, \
      0.11958436259454885420, \
      0.11958436259454885420, \
      0.11958436259454885420, \
      0.11958436259454885420, \
      0.01562091696416078104, \
      0.01562091696416078104, \
      0.01562091696416078104, \
      0.01562091696416078104, \
      0.01562091696416078104, \
      0.01562091696416078104, \
      0.01562091696416078104, \
      0.01562091696416078104, \
      0.35132620557004257122, \
      0.35132620557004257122, \
      0.35132620557004257122, \
      0.35132620557004257122, \
      0.35132620557004257122, \
      0.35132620557004257122, \
      0.35132620557004257122, \
      0.35132620557004257122, \
      0.01323405399603627339, \
      0.01323405399603627339, \
      0.01323405399603627339, \
      0.01323405399603627339, \
      0.01323405399603627339, \
      0.01323405399603627339, \
      0.01323405399603627339, \
      0.01323405399603627339, \
      0.02986233869137579211, \
      0.02986233869137579211, \
      0.02986233869137579211, \
      0.02986233869137579211, \
      0.02986233869137579211, \
      0.02986233869137579211, \
      0.02986233869137579211, \
      0.02986233869137579211 ] )

  w= np.array ( [ \
      0.00012216821078901854, \
      0.00563943629581533951, \
      0.00187116838043227779, \
      0.00087900554061397717, \
      0.00087900554061397717, \
      0.00087900554061397717, \
      0.00087900554061397717, \
      0.00063973688323901037, \
      0.00063973688323901037, \
      0.00063973688323901037, \
      0.00063973688323901037, \
      0.00191942477958428285, \
      0.00191942477958428285, \
      0.00191942477958428285, \
      0.00191942477958428285, \
      0.00108856800183791767, \
      0.00108856800183791767, \
      0.00108856800183791767, \
      0.00108856800183791767, \
      0.00579178348482820276, \
      0.00579178348482820276, \
      0.00579178348482820276, \
      0.00579178348482820276, \
      0.00333567983247391557, \
      0.00333567983247391557, \
      0.00333567983247391557, \
      0.00333567983247391557, \
      0.00483993401414843216, \
      0.00483993401414843216, \
      0.00483993401414843216, \
      0.00483993401414843216, \
      0.01171223275540323253, \
      0.01171223275540323253, \
      0.01171223275540323253, \
      0.01171223275540323253, \
      0.00781803283741232084, \
      0.00781803283741232084, \
      0.00781803283741232084, \
      0.00781803283741232084, \
      0.00316389891636655388, \
      0.00316389891636655388, \
      0.00316389891636655388, \
      0.00316389891636655388, \
      0.00813627882273969955, \
      0.00813627882273969955, \
      0.00813627882273969955, \
      0.00813627882273969955, \
      0.00471982615752600254, \
      0.00471982615752600254, \
      0.00471982615752600254, \
      0.00471982615752600254, \
      0.00096237134938021330, \
      0.00096237134938021330, \
      0.00096237134938021330, \
      0.00096237134938021330, \
      0.00162378774013503748, \
      0.00162378774013503748, \
      0.00162378774013503748, \
      0.00162378774013503748, \
      0.00871345927599746599, \
      0.00871345927599746599, \
      0.00871345927599746599, \
      0.00871345927599746599, \
      0.00412008618466326321, \
      0.00412008618466326321, \
      0.00412008618466326321, \
      0.00412008618466326321, \
      0.00052206472289359268, \
      0.00052206472289359268, \
      0.00052206472289359268, \
      0.00052206472289359268, \
      0.00389716456343351799, \
      0.00389716456343351799, \
      0.00389716456343351799, \
      0.00389716456343351799, \
      0.00222992187534444422, \
      0.00222992187534444422, \
      0.00222992187534444422, \
      0.00222992187534444422, \
      0.00941806762258396400, \
      0.00941806762258396400, \
      0.00941806762258396400, \
      0.00941806762258396400, \
      0.00066158322303103113, \
      0.00066158322303103113, \
      0.00066158322303103113, \
      0.00066158322303103113, \
      0.00010739422189895962, \
      0.00010739422189895962, \
      0.00010739422189895962, \
      0.00010739422189895962, \
      0.00303147852588211194, \
      0.00303147852588211194, \
      0.00303147852588211194, \
      0.00303147852588211194, \
      0.00081932641066923071, \
      0.00081932641066923071, \
      0.00081932641066923071, \
      0.00081932641066923071, \
      0.00465121449070608067, \
      0.00465121449070608067, \
      0.00465121449070608067, \
      0.00465121449070608067, \
      0.00167606716811515987, \
      0.00167606716811515987, \
      0.00167606716811515987, \
      0.00167606716811515987, \
      0.00825768957465656227, \
      0.00825768957465656227, \
      0.00825768957465656227, \
      0.00825768957465656227, \
      0.00397545859544364086, \
      0.00397545859544364086, \
      0.00397545859544364086, \
      0.00397545859544364086, \
      0.00051722520547986095, \
      0.00051722520547986095, \
      0.00051722520547986095, \
      0.00051722520547986095, \
      0.00624136348038179748, \
      0.00624136348038179748, \
      0.00624136348038179748, \
      0.00624136348038179748, \
      0.00249954122416236671, \
      0.00249954122416236671, \
      0.00249954122416236671, \
      0.00249954122416236671, \
      0.00344134582405346756, \
      0.00344134582405346756, \
      0.00344134582405346756, \
      0.00344134582405346756, \
      0.00373085764189791565, \
      0.00373085764189791565, \
      0.00373085764189791565, \
      0.00373085764189791565, \
      0.00985379501780648571, \
      0.00985379501780648571, \
      0.00985379501780648571, \
      0.00985379501780648571, \
      0.00736757952028449341, \
      0.00736757952028449341, \
      0.00736757952028449341, \
      0.00736757952028449341, \
      0.00178048730560625978, \
      0.00178048730560625978, \
      0.00178048730560625978, \
      0.00178048730560625978, \
      0.00242313168519621295, \
      0.00242313168519621295, \
      0.00242313168519621295, \
      0.00242313168519621295, \
      0.00105734008948304265, \
      0.00105734008948304265, \
      0.00105734008948304265, \
      0.00105734008948304265, \
      0.00145036343491798387, \
      0.00145036343491798387, \
      0.00145036343491798387, \
      0.00145036343491798387, \
      0.00271057993574526021, \
      0.00271057993574526021, \
      0.00271057993574526021, \
      0.00271057993574526021, \
      0.00112014566884451267, \
      0.00112014566884451267, \
      0.00112014566884451267, \
      0.00112014566884451267, \
      0.00120917104359697324, \
      0.00120917104359697324, \
      0.00120917104359697324, \
      0.00120917104359697324, \
      0.00120917104359697324, \
      0.00120917104359697324, \
      0.00120917104359697324, \
      0.00120917104359697324, \
      0.00162471395073617649, \
      0.00162471395073617649, \
      0.00162471395073617649, \
      0.00162471395073617649, \
      0.00162471395073617649, \
      0.00162471395073617649, \
      0.00162471395073617649, \
      0.00162471395073617649, \
      0.00620858966914663961, \
      0.00620858966914663961, \
      0.00620858966914663961, \
      0.00620858966914663961, \
      0.00620858966914663961, \
      0.00620858966914663961, \
      0.00620858966914663961, \
      0.00620858966914663961, \
      0.00135724577802302663, \
      0.00135724577802302663, \
      0.00135724577802302663, \
      0.00135724577802302663, \
      0.00135724577802302663, \
      0.00135724577802302663, \
      0.00135724577802302663, \
      0.00135724577802302663, \
      0.00077688230182242947, \
      0.00077688230182242947, \
      0.00077688230182242947, \
      0.00077688230182242947, \
      0.00077688230182242947, \
      0.00077688230182242947, \
      0.00077688230182242947, \
      0.00077688230182242947, \
      0.00190538850038805656, \
      0.00190538850038805656, \
      0.00190538850038805656, \
      0.00190538850038805656, \
      0.00190538850038805656, \
      0.00190538850038805656, \
      0.00190538850038805656, \
      0.00190538850038805656, \
      0.00183635585567423158, \
      0.00183635585567423158, \
      0.00183635585567423158, \
      0.00183635585567423158, \
      0.00183635585567423158, \
      0.00183635585567423158, \
      0.00183635585567423158, \
      0.00183635585567423158, \
      0.00173312265591197071, \
      0.00173312265591197071, \
      0.00173312265591197071, \
      0.00173312265591197071, \
      0.00173312265591197071, \
      0.00173312265591197071, \
      0.00173312265591197071, \
      0.00173312265591197071, \
      0.00087558681440168869, \
      0.00087558681440168869, \
      0.00087558681440168869, \
      0.00087558681440168869, \
      0.00087558681440168869, \
      0.00087558681440168869, \
      0.00087558681440168869, \
      0.00087558681440168869, \
      0.00529919935281060114, \
      0.00529919935281060114, \
      0.00529919935281060114, \
      0.00529919935281060114, \
      0.00529919935281060114, \
      0.00529919935281060114, \
      0.00529919935281060114, \
      0.00529919935281060114, \
      0.00190923140339424222, \
      0.00190923140339424222, \
      0.00190923140339424222, \
      0.00190923140339424222, \
      0.00190923140339424222, \
      0.00190923140339424222, \
      0.00190923140339424222, \
      0.00190923140339424222, \
      0.00333270329648946212, \
      0.00333270329648946212, \
      0.00333270329648946212, \
      0.00333270329648946212, \
      0.00333270329648946212, \
      0.00333270329648946212, \
      0.00333270329648946212, \
      0.00333270329648946212, \
      0.00137258273942558089, \
      0.00137258273942558089, \
      0.00137258273942558089, \
      0.00137258273942558089, \
      0.00137258273942558089, \
      0.00137258273942558089, \
      0.00137258273942558089, \
      0.00137258273942558089, \
      0.00440562895172808174, \
      0.00440562895172808174, \
      0.00440562895172808174, \
      0.00440562895172808174, \
      0.00440562895172808174, \
      0.00440562895172808174, \
      0.00440562895172808174, \
      0.00440562895172808174, \
      0.00690265770456989416, \
      0.00690265770456989416, \
      0.00690265770456989416, \
      0.00690265770456989416, \
      0.00690265770456989416, \
      0.00690265770456989416, \
      0.00690265770456989416, \
      0.00690265770456989416, \
      0.00202734469527626228, \
      0.00202734469527626228, \
      0.00202734469527626228, \
      0.00202734469527626228, \
      0.00202734469527626228, \
      0.00202734469527626228, \
      0.00202734469527626228, \
      0.00202734469527626228, \
      0.00204643595334019031, \
      0.00204643595334019031, \
      0.00204643595334019031, \
      0.00204643595334019031, \
      0.00204643595334019031, \
      0.00204643595334019031, \
      0.00204643595334019031, \
      0.00204643595334019031, \
      0.00034532641662137929, \
      0.00034532641662137929, \
      0.00034532641662137929, \
      0.00034532641662137929, \
      0.00034532641662137929, \
      0.00034532641662137929, \
      0.00034532641662137929, \
      0.00034532641662137929, \
      0.00242508950332979241, \
      0.00242508950332979241, \
      0.00242508950332979241, \
      0.00242508950332979241, \
      0.00242508950332979241, \
      0.00242508950332979241, \
      0.00242508950332979241, \
      0.00242508950332979241 ] )

  return x, y, z, w

def rule18 ( ):

#*****************************************************************************80
#
## rule18() returns the pyramid quadrature rule of precision 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.73869275831950009792, \
      0.00000000000000000000, \
     -0.73869275831950009792, \
      0.00000000000000000000, \
      0.76806657302952874300, \
      0.00000000000000000000, \
     -0.76806657302952874300, \
      0.00000000000000000000, \
      0.31673944809898013641, \
      0.00000000000000000000, \
     -0.31673944809898013641, \
      0.00000000000000000000, \
      0.61877572218072185439, \
      0.00000000000000000000, \
     -0.61877572218072185439, \
      0.00000000000000000000, \
      0.37235294402955443349, \
      0.00000000000000000000, \
     -0.37235294402955443349, \
      0.00000000000000000000, \
      0.50387193570782862206, \
      0.00000000000000000000, \
     -0.50387193570782862206, \
      0.00000000000000000000, \
      0.72207836507269651527, \
      0.00000000000000000000, \
     -0.72207836507269651527, \
      0.00000000000000000000, \
      0.39403113359582681019, \
      0.00000000000000000000, \
     -0.39403113359582681019, \
      0.00000000000000000000, \
      0.11819479806124476295, \
      0.00000000000000000000, \
     -0.11819479806124476295, \
      0.00000000000000000000, \
      0.51179862044264223808, \
      0.00000000000000000000, \
     -0.51179862044264223808, \
      0.00000000000000000000, \
      0.09344056049843052492, \
      0.00000000000000000000, \
     -0.09344056049843052492, \
      0.00000000000000000000, \
      0.97786305288383967849, \
      0.00000000000000000000, \
     -0.97786305288383967849, \
      0.00000000000000000000, \
      0.26893118028825491184, \
      0.00000000000000000000, \
     -0.26893118028825491184, \
      0.00000000000000000000, \
      0.18588876717193755783, \
      0.00000000000000000000, \
     -0.18588876717193755783, \
      0.00000000000000000000, \
      0.88032062123229137818, \
     -0.88032062123229137818, \
      0.88032062123229137818, \
     -0.88032062123229137818, \
      0.68145212136761557087, \
     -0.68145212136761557087, \
      0.68145212136761557087, \
     -0.68145212136761557087, \
      0.49699036434274163065, \
     -0.49699036434274163065, \
      0.49699036434274163065, \
     -0.49699036434274163065, \
      0.30634018082228819946, \
     -0.30634018082228819946, \
      0.30634018082228819946, \
     -0.30634018082228819946, \
      0.58539966455385050725, \
     -0.58539966455385050725, \
      0.58539966455385050725, \
     -0.58539966455385050725, \
      0.77694395476943478585, \
     -0.77694395476943478585, \
      0.77694395476943478585, \
     -0.77694395476943478585, \
      0.18695368401965414829, \
     -0.18695368401965414829, \
      0.18695368401965414829, \
     -0.18695368401965414829, \
      0.64402844061291575350, \
     -0.64402844061291575350, \
      0.64402844061291575350, \
     -0.64402844061291575350, \
      0.19939684409397287479, \
     -0.19939684409397287479, \
      0.19939684409397287479, \
     -0.19939684409397287479, \
      0.49151662722959021945, \
     -0.49151662722959021945, \
      0.49151662722959021945, \
     -0.49151662722959021945, \
      0.21971883736597888626, \
     -0.21971883736597888626, \
      0.21971883736597888626, \
     -0.21971883736597888626, \
      0.38181860275292400786, \
     -0.38181860275292400786, \
      0.38181860275292400786, \
     -0.38181860275292400786, \
      0.13233574436496933768, \
     -0.13233574436496933768, \
      0.13233574436496933768, \
     -0.13233574436496933768, \
      0.26434906680031583504, \
     -0.26434906680031583504, \
      0.26434906680031583504, \
     -0.26434906680031583504, \
      0.26259016722585765136, \
     -0.26259016722585765136, \
      0.26259016722585765136, \
     -0.26259016722585765136, \
      0.63683049968859806178, \
     -0.63683049968859806178, \
      0.63683049968859806178, \
     -0.63683049968859806178, \
      0.50333230035733345087, \
     -0.50333230035733345087, \
      0.50333230035733345087, \
     -0.50333230035733345087, \
      0.43053066487698737896, \
     -0.43053066487698737896, \
      0.43053066487698737896, \
     -0.43053066487698737896, \
      0.44121177996231647489, \
     -0.44121177996231647489, \
      0.44121177996231647489, \
     -0.44121177996231647489, \
      0.12338526534910826404, \
     -0.12338526534910826404, \
      0.12338526534910826404, \
     -0.12338526534910826404, \
      0.28196466746787440805, \
     -0.28196466746787440805, \
      0.28196466746787440805, \
     -0.28196466746787440805, \
      0.12302065942509179952, \
     -0.12302065942509179952, \
      0.12302065942509179952, \
     -0.12302065942509179952, \
      0.96995340856169265376, \
     -0.96995340856169265376, \
      0.96995340856169265376, \
     -0.96995340856169265376, \
      0.15367597423015844083, \
     -0.15367597423015844083, \
      0.15367597423015844083, \
     -0.15367597423015844083, \
      0.32324916002943732130, \
     -0.32324916002943732130, \
      0.32324916002943732130, \
     -0.32324916002943732130, \
      0.07979061002341172881, \
     -0.07979061002341172881, \
      0.07979061002341172881, \
     -0.07979061002341172881, \
      0.05572751587573096521, \
     -0.05572751587573096521, \
      0.05572751587573096521, \
     -0.05572751587573096521, \
      0.80407180079417317486, \
     -0.80407180079417317486, \
      0.80407180079417317486, \
     -0.80407180079417317486, \
      0.10630794929321137066, \
     -0.10630794929321137066, \
      0.10630794929321137066, \
     -0.10630794929321137066, \
      0.14968116552008028930, \
     -0.14968116552008028930, \
      0.14968116552008028930, \
     -0.14968116552008028930, \
      0.72179802358977040999, \
     -0.72179802358977040999, \
      0.72179802358977040999, \
     -0.72179802358977040999, \
      0.81797170822487763608, \
      0.64320215485058829241, \
     -0.81797170822487763608, \
      0.64320215485058829241, \
      0.81797170822487763608, \
     -0.64320215485058829241, \
     -0.81797170822487763608, \
     -0.64320215485058829241, \
      0.45477772302529712034, \
      0.16636418997995866542, \
     -0.45477772302529712034, \
      0.16636418997995866542, \
      0.45477772302529712034, \
     -0.16636418997995866542, \
     -0.45477772302529712034, \
     -0.16636418997995866542, \
      0.22077509021471022899, \
      0.64919419286301172090, \
     -0.22077509021471022899, \
      0.64919419286301172090, \
      0.22077509021471022899, \
     -0.64919419286301172090, \
     -0.22077509021471022899, \
     -0.64919419286301172090, \
      0.85849144377065222944, \
      0.26442320916257716634, \
     -0.85849144377065222944, \
      0.26442320916257716634, \
      0.85849144377065222944, \
     -0.26442320916257716634, \
     -0.85849144377065222944, \
     -0.26442320916257716634, \
      0.19087247051624386951, \
      0.45655985846318541954, \
     -0.19087247051624386951, \
      0.45655985846318541954, \
      0.19087247051624386951, \
     -0.45655985846318541954, \
     -0.19087247051624386951, \
     -0.45655985846318541954, \
      0.37787816613860053527, \
      0.66406293254753101518, \
     -0.37787816613860053527, \
      0.66406293254753101518, \
      0.37787816613860053527, \
     -0.66406293254753101518, \
     -0.37787816613860053527, \
     -0.66406293254753101518, \
      0.89395556646395457623, \
      0.17283329178347239807, \
     -0.89395556646395457623, \
      0.17283329178347239807, \
      0.89395556646395457623, \
     -0.17283329178347239807, \
     -0.89395556646395457623, \
     -0.17283329178347239807, \
      0.40991415053935187363, \
      0.05003413197772252352, \
     -0.40991415053935187363, \
      0.05003413197772252352, \
      0.40991415053935187363, \
     -0.05003413197772252352, \
     -0.40991415053935187363, \
     -0.05003413197772252352, \
      0.93198108654420652730, \
      0.10662173986061880548, \
     -0.93198108654420652730, \
      0.10662173986061880548, \
      0.93198108654420652730, \
     -0.10662173986061880548, \
     -0.93198108654420652730, \
     -0.10662173986061880548, \
      0.28018220607206512085, \
      0.84993195986801317598, \
     -0.28018220607206512085, \
      0.84993195986801317598, \
      0.28018220607206512085, \
     -0.84993195986801317598, \
     -0.28018220607206512085, \
     -0.84993195986801317598, \
      0.57728165413613941048, \
      0.46201429744731292715, \
     -0.57728165413613941048, \
      0.46201429744731292715, \
      0.57728165413613941048, \
     -0.46201429744731292715, \
     -0.57728165413613941048, \
     -0.46201429744731292715, \
      0.84451580808527704214, \
      0.61756791755060624904, \
     -0.84451580808527704214, \
      0.61756791755060624904, \
      0.84451580808527704214, \
     -0.61756791755060624904, \
     -0.84451580808527704214, \
     -0.61756791755060624904, \
      0.52941572893811861267, \
      0.23348533584682021336, \
     -0.52941572893811861267, \
      0.23348533584682021336, \
      0.52941572893811861267, \
     -0.23348533584682021336, \
     -0.52941572893811861267, \
     -0.23348533584682021336, \
      0.92827521801894674613, \
      0.67941786279817284466, \
     -0.92827521801894674613, \
      0.67941786279817284466, \
      0.92827521801894674613, \
     -0.67941786279817284466, \
     -0.92827521801894674613, \
     -0.67941786279817284466, \
      0.96836516384095050469, \
      0.46144251438466377113, \
     -0.96836516384095050469, \
      0.46144251438466377113, \
      0.96836516384095050469, \
     -0.46144251438466377113, \
     -0.96836516384095050469, \
     -0.46144251438466377113, \
      0.16744571840030086918, \
      0.31430414794159466929, \
     -0.16744571840030086918, \
      0.31430414794159466929, \
      0.16744571840030086918, \
     -0.31430414794159466929, \
     -0.16744571840030086918, \
     -0.31430414794159466929, \
      0.49232718454496093852, \
      0.73988842925403419670, \
     -0.49232718454496093852, \
      0.73988842925403419670, \
      0.49232718454496093852, \
     -0.73988842925403419670, \
     -0.49232718454496093852, \
     -0.73988842925403419670, \
      0.85659974228270108210, \
      0.54061065617200576572, \
     -0.85659974228270108210, \
      0.54061065617200576572, \
      0.85659974228270108210, \
     -0.54061065617200576572, \
     -0.85659974228270108210, \
     -0.54061065617200576572, \
      0.26702277361260906563, \
      0.57531393529153806998, \
     -0.26702277361260906563, \
      0.57531393529153806998, \
      0.26702277361260906563, \
     -0.57531393529153806998, \
     -0.26702277361260906563, \
     -0.57531393529153806998, \
      0.41506457665342233465, \
      0.71731018735152574095, \
     -0.41506457665342233465, \
      0.71731018735152574095, \
      0.41506457665342233465, \
     -0.71731018735152574095, \
     -0.41506457665342233465, \
     -0.71731018735152574095, \
      0.94466239579161759288, \
      0.81619080186595505122, \
     -0.94466239579161759288, \
      0.81619080186595505122, \
      0.94466239579161759288, \
     -0.81619080186595505122, \
     -0.94466239579161759288, \
     -0.81619080186595505122, \
      0.71450522624081691525, \
      0.31179783227055996031, \
     -0.71450522624081691525, \
      0.31179783227055996031, \
      0.71450522624081691525, \
     -0.31179783227055996031, \
     -0.71450522624081691525, \
     -0.31179783227055996031 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.73869275831950009792, \
      0.00000000000000000000, \
     -0.73869275831950009792, \
      0.00000000000000000000, \
      0.76806657302952874300, \
      0.00000000000000000000, \
     -0.76806657302952874300, \
      0.00000000000000000000, \
      0.31673944809898013641, \
      0.00000000000000000000, \
     -0.31673944809898013641, \
      0.00000000000000000000, \
      0.61877572218072185439, \
      0.00000000000000000000, \
     -0.61877572218072185439, \
      0.00000000000000000000, \
      0.37235294402955443349, \
      0.00000000000000000000, \
     -0.37235294402955443349, \
      0.00000000000000000000, \
      0.50387193570782862206, \
      0.00000000000000000000, \
     -0.50387193570782862206, \
      0.00000000000000000000, \
      0.72207836507269651527, \
      0.00000000000000000000, \
     -0.72207836507269651527, \
      0.00000000000000000000, \
      0.39403113359582681019, \
      0.00000000000000000000, \
     -0.39403113359582681019, \
      0.00000000000000000000, \
      0.11819479806124476295, \
      0.00000000000000000000, \
     -0.11819479806124476295, \
      0.00000000000000000000, \
      0.51179862044264223808, \
      0.00000000000000000000, \
     -0.51179862044264223808, \
      0.00000000000000000000, \
      0.09344056049843052492, \
      0.00000000000000000000, \
     -0.09344056049843052492, \
      0.00000000000000000000, \
      0.97786305288383967849, \
      0.00000000000000000000, \
     -0.97786305288383967849, \
      0.00000000000000000000, \
      0.26893118028825491184, \
      0.00000000000000000000, \
     -0.26893118028825491184, \
      0.00000000000000000000, \
      0.18588876717193755783, \
      0.00000000000000000000, \
     -0.18588876717193755783, \
      0.88032062123229137818, \
      0.88032062123229137818, \
     -0.88032062123229137818, \
     -0.88032062123229137818, \
      0.68145212136761557087, \
      0.68145212136761557087, \
     -0.68145212136761557087, \
     -0.68145212136761557087, \
      0.49699036434274163065, \
      0.49699036434274163065, \
     -0.49699036434274163065, \
     -0.49699036434274163065, \
      0.30634018082228819946, \
      0.30634018082228819946, \
     -0.30634018082228819946, \
     -0.30634018082228819946, \
      0.58539966455385050725, \
      0.58539966455385050725, \
     -0.58539966455385050725, \
     -0.58539966455385050725, \
      0.77694395476943478585, \
      0.77694395476943478585, \
     -0.77694395476943478585, \
     -0.77694395476943478585, \
      0.18695368401965414829, \
      0.18695368401965414829, \
     -0.18695368401965414829, \
     -0.18695368401965414829, \
      0.64402844061291575350, \
      0.64402844061291575350, \
     -0.64402844061291575350, \
     -0.64402844061291575350, \
      0.19939684409397287479, \
      0.19939684409397287479, \
     -0.19939684409397287479, \
     -0.19939684409397287479, \
      0.49151662722959021945, \
      0.49151662722959021945, \
     -0.49151662722959021945, \
     -0.49151662722959021945, \
      0.21971883736597888626, \
      0.21971883736597888626, \
     -0.21971883736597888626, \
     -0.21971883736597888626, \
      0.38181860275292400786, \
      0.38181860275292400786, \
     -0.38181860275292400786, \
     -0.38181860275292400786, \
      0.13233574436496933768, \
      0.13233574436496933768, \
     -0.13233574436496933768, \
     -0.13233574436496933768, \
      0.26434906680031583504, \
      0.26434906680031583504, \
     -0.26434906680031583504, \
     -0.26434906680031583504, \
      0.26259016722585765136, \
      0.26259016722585765136, \
     -0.26259016722585765136, \
     -0.26259016722585765136, \
      0.63683049968859806178, \
      0.63683049968859806178, \
     -0.63683049968859806178, \
     -0.63683049968859806178, \
      0.50333230035733345087, \
      0.50333230035733345087, \
     -0.50333230035733345087, \
     -0.50333230035733345087, \
      0.43053066487698737896, \
      0.43053066487698737896, \
     -0.43053066487698737896, \
     -0.43053066487698737896, \
      0.44121177996231647489, \
      0.44121177996231647489, \
     -0.44121177996231647489, \
     -0.44121177996231647489, \
      0.12338526534910826404, \
      0.12338526534910826404, \
     -0.12338526534910826404, \
     -0.12338526534910826404, \
      0.28196466746787440805, \
      0.28196466746787440805, \
     -0.28196466746787440805, \
     -0.28196466746787440805, \
      0.12302065942509179952, \
      0.12302065942509179952, \
     -0.12302065942509179952, \
     -0.12302065942509179952, \
      0.96995340856169265376, \
      0.96995340856169265376, \
     -0.96995340856169265376, \
     -0.96995340856169265376, \
      0.15367597423015844083, \
      0.15367597423015844083, \
     -0.15367597423015844083, \
     -0.15367597423015844083, \
      0.32324916002943732130, \
      0.32324916002943732130, \
     -0.32324916002943732130, \
     -0.32324916002943732130, \
      0.07979061002341172881, \
      0.07979061002341172881, \
     -0.07979061002341172881, \
     -0.07979061002341172881, \
      0.05572751587573096521, \
      0.05572751587573096521, \
     -0.05572751587573096521, \
     -0.05572751587573096521, \
      0.80407180079417317486, \
      0.80407180079417317486, \
     -0.80407180079417317486, \
     -0.80407180079417317486, \
      0.10630794929321137066, \
      0.10630794929321137066, \
     -0.10630794929321137066, \
     -0.10630794929321137066, \
      0.14968116552008028930, \
      0.14968116552008028930, \
     -0.14968116552008028930, \
     -0.14968116552008028930, \
      0.72179802358977040999, \
      0.72179802358977040999, \
     -0.72179802358977040999, \
     -0.72179802358977040999, \
      0.64320215485058829241, \
      0.81797170822487763608, \
      0.64320215485058829241, \
     -0.81797170822487763608, \
     -0.64320215485058829241, \
      0.81797170822487763608, \
     -0.64320215485058829241, \
     -0.81797170822487763608, \
      0.16636418997995866542, \
      0.45477772302529712034, \
      0.16636418997995866542, \
     -0.45477772302529712034, \
     -0.16636418997995866542, \
      0.45477772302529712034, \
     -0.16636418997995866542, \
     -0.45477772302529712034, \
      0.64919419286301172090, \
      0.22077509021471022899, \
      0.64919419286301172090, \
     -0.22077509021471022899, \
     -0.64919419286301172090, \
      0.22077509021471022899, \
     -0.64919419286301172090, \
     -0.22077509021471022899, \
      0.26442320916257716634, \
      0.85849144377065222944, \
      0.26442320916257716634, \
     -0.85849144377065222944, \
     -0.26442320916257716634, \
      0.85849144377065222944, \
     -0.26442320916257716634, \
     -0.85849144377065222944, \
      0.45655985846318541954, \
      0.19087247051624386951, \
      0.45655985846318541954, \
     -0.19087247051624386951, \
     -0.45655985846318541954, \
      0.19087247051624386951, \
     -0.45655985846318541954, \
     -0.19087247051624386951, \
      0.66406293254753101518, \
      0.37787816613860053527, \
      0.66406293254753101518, \
     -0.37787816613860053527, \
     -0.66406293254753101518, \
      0.37787816613860053527, \
     -0.66406293254753101518, \
     -0.37787816613860053527, \
      0.17283329178347239807, \
      0.89395556646395457623, \
      0.17283329178347239807, \
     -0.89395556646395457623, \
     -0.17283329178347239807, \
      0.89395556646395457623, \
     -0.17283329178347239807, \
     -0.89395556646395457623, \
      0.05003413197772252352, \
      0.40991415053935187363, \
      0.05003413197772252352, \
     -0.40991415053935187363, \
     -0.05003413197772252352, \
      0.40991415053935187363, \
     -0.05003413197772252352, \
     -0.40991415053935187363, \
      0.10662173986061880548, \
      0.93198108654420652730, \
      0.10662173986061880548, \
     -0.93198108654420652730, \
     -0.10662173986061880548, \
      0.93198108654420652730, \
     -0.10662173986061880548, \
     -0.93198108654420652730, \
      0.84993195986801317598, \
      0.28018220607206512085, \
      0.84993195986801317598, \
     -0.28018220607206512085, \
     -0.84993195986801317598, \
      0.28018220607206512085, \
     -0.84993195986801317598, \
     -0.28018220607206512085, \
      0.46201429744731292715, \
      0.57728165413613941048, \
      0.46201429744731292715, \
     -0.57728165413613941048, \
     -0.46201429744731292715, \
      0.57728165413613941048, \
     -0.46201429744731292715, \
     -0.57728165413613941048, \
      0.61756791755060624904, \
      0.84451580808527704214, \
      0.61756791755060624904, \
     -0.84451580808527704214, \
     -0.61756791755060624904, \
      0.84451580808527704214, \
     -0.61756791755060624904, \
     -0.84451580808527704214, \
      0.23348533584682021336, \
      0.52941572893811861267, \
      0.23348533584682021336, \
     -0.52941572893811861267, \
     -0.23348533584682021336, \
      0.52941572893811861267, \
     -0.23348533584682021336, \
     -0.52941572893811861267, \
      0.67941786279817284466, \
      0.92827521801894674613, \
      0.67941786279817284466, \
     -0.92827521801894674613, \
     -0.67941786279817284466, \
      0.92827521801894674613, \
     -0.67941786279817284466, \
     -0.92827521801894674613, \
      0.46144251438466377113, \
      0.96836516384095050469, \
      0.46144251438466377113, \
     -0.96836516384095050469, \
     -0.46144251438466377113, \
      0.96836516384095050469, \
     -0.46144251438466377113, \
     -0.96836516384095050469, \
      0.31430414794159466929, \
      0.16744571840030086918, \
      0.31430414794159466929, \
     -0.16744571840030086918, \
     -0.31430414794159466929, \
      0.16744571840030086918, \
     -0.31430414794159466929, \
     -0.16744571840030086918, \
      0.73988842925403419670, \
      0.49232718454496093852, \
      0.73988842925403419670, \
     -0.49232718454496093852, \
     -0.73988842925403419670, \
      0.49232718454496093852, \
     -0.73988842925403419670, \
     -0.49232718454496093852, \
      0.54061065617200576572, \
      0.85659974228270108210, \
      0.54061065617200576572, \
     -0.85659974228270108210, \
     -0.54061065617200576572, \
      0.85659974228270108210, \
     -0.54061065617200576572, \
     -0.85659974228270108210, \
      0.57531393529153806998, \
      0.26702277361260906563, \
      0.57531393529153806998, \
     -0.26702277361260906563, \
     -0.57531393529153806998, \
      0.26702277361260906563, \
     -0.57531393529153806998, \
     -0.26702277361260906563, \
      0.71731018735152574095, \
      0.41506457665342233465, \
      0.71731018735152574095, \
     -0.41506457665342233465, \
     -0.71731018735152574095, \
      0.41506457665342233465, \
     -0.71731018735152574095, \
     -0.41506457665342233465, \
      0.81619080186595505122, \
      0.94466239579161759288, \
      0.81619080186595505122, \
     -0.94466239579161759288, \
     -0.81619080186595505122, \
      0.94466239579161759288, \
     -0.81619080186595505122, \
     -0.94466239579161759288, \
      0.31179783227055996031, \
      0.71450522624081691525, \
      0.31179783227055996031, \
     -0.71450522624081691525, \
     -0.31179783227055996031, \
      0.71450522624081691525, \
     -0.31179783227055996031, \
     -0.71450522624081691525 ] )

  z = np.array ( [ \
      0.96891318773147550036, \
      0.11218085315386774892, \
      0.11218085315386774892, \
      0.11218085315386774892, \
      0.11218085315386774892, \
      0.20952037314221555464, \
      0.20952037314221555464, \
      0.20952037314221555464, \
      0.20952037314221555464, \
      0.45043339209409832824, \
      0.45043339209409832824, \
      0.45043339209409832824, \
      0.45043339209409832824, \
      0.36713809241502448621, \
      0.36713809241502448621, \
      0.36713809241502448621, \
      0.36713809241502448621, \
      0.51496945555138884387, \
      0.51496945555138884387, \
      0.51496945555138884387, \
      0.51496945555138884387, \
      0.24658740648660407158, \
      0.24658740648660407158, \
      0.24658740648660407158, \
      0.24658740648660407158, \
      0.03347288009925680763, \
      0.03347288009925680763, \
      0.03347288009925680763, \
      0.03347288009925680763, \
      0.17604915946010571415, \
      0.17604915946010571415, \
      0.17604915946010571415, \
      0.17604915946010571415, \
      0.12627670900302459533, \
      0.12627670900302459533, \
      0.12627670900302459533, \
      0.12627670900302459533, \
      0.01146186842907397259, \
      0.01146186842907397259, \
      0.01146186842907397259, \
      0.01146186842907397259, \
      0.82865571811563620841, \
      0.82865571811563620841, \
      0.82865571811563620841, \
      0.82865571811563620841, \
      0.00411477663570613411, \
      0.00411477663570613411, \
      0.00411477663570613411, \
      0.00411477663570613411, \
      0.66431760085930258164, \
      0.66431760085930258164, \
      0.66431760085930258164, \
      0.66431760085930258164, \
      0.80714531646844267510, \
      0.80714531646844267510, \
      0.80714531646844267510, \
      0.80714531646844267510, \
      0.06759778909905436728, \
      0.06759778909905436728, \
      0.06759778909905436728, \
      0.06759778909905436728, \
      0.29403431132680074578, \
      0.29403431132680074578, \
      0.29403431132680074578, \
      0.29403431132680074578, \
      0.49665508093160370962, \
      0.49665508093160370962, \
      0.49665508093160370962, \
      0.49665508093160370962, \
      0.27911320549015106174, \
      0.27911320549015106174, \
      0.27911320549015106174, \
      0.27911320549015106174, \
      0.07876704807666434771, \
      0.07876704807666434771, \
      0.07876704807666434771, \
      0.07876704807666434771, \
      0.04825635484814582571, \
      0.04825635484814582571, \
      0.04825635484814582571, \
      0.04825635484814582571, \
      0.00881247486166711683, \
      0.00881247486166711683, \
      0.00881247486166711683, \
      0.00881247486166711683, \
      0.02005872107121197886, \
      0.02005872107121197886, \
      0.02005872107121197886, \
      0.02005872107121197886, \
      0.75639094968056375112, \
      0.75639094968056375112, \
      0.75639094968056375112, \
      0.75639094968056375112, \
      0.15155505938254110188, \
      0.15155505938254110188, \
      0.15155505938254110188, \
      0.15155505938254110188, \
      0.60842758819371955958, \
      0.60842758819371955958, \
      0.60842758819371955958, \
      0.60842758819371955958, \
      0.52569545459372502005, \
      0.52569545459372502005, \
      0.52569545459372502005, \
      0.52569545459372502005, \
      0.40281226004252063122, \
      0.40281226004252063122, \
      0.40281226004252063122, \
      0.40281226004252063122, \
      0.04148931197347632133, \
      0.04148931197347632133, \
      0.04148931197347632133, \
      0.04148931197347632133, \
      0.14661700764838450639, \
      0.14661700764838450639, \
      0.14661700764838450639, \
      0.14661700764838450639, \
      0.25661597420550030790, \
      0.25661597420550030790, \
      0.25661597420550030790, \
      0.25661597420550030790, \
      0.25552367243392443141, \
      0.25552367243392443141, \
      0.25552367243392443141, \
      0.25552367243392443141, \
      0.36981856719481731588, \
      0.36981856719481731588, \
      0.36981856719481731588, \
      0.36981856719481731588, \
      0.01554708555805913925, \
      0.01554708555805913925, \
      0.01554708555805913925, \
      0.01554708555805913925, \
      0.04951092940950102550, \
      0.04951092940950102550, \
      0.04951092940950102550, \
      0.04951092940950102550, \
      0.45729924127195364925, \
      0.45729924127195364925, \
      0.45729924127195364925, \
      0.45729924127195364925, \
      0.25865392811548787444, \
      0.25865392811548787444, \
      0.25865392811548787444, \
      0.25865392811548787444, \
      0.01471561063742727986, \
      0.01471561063742727986, \
      0.01471561063742727986, \
      0.01471561063742727986, \
      0.84302938509543134948, \
      0.84302938509543134948, \
      0.84302938509543134948, \
      0.84302938509543134948, \
      0.64221316316195331542, \
      0.64221316316195331542, \
      0.64221316316195331542, \
      0.64221316316195331542, \
      0.70815468949755844275, \
      0.70815468949755844275, \
      0.70815468949755844275, \
      0.70815468949755844275, \
      0.90756616766447684164, \
      0.90756616766447684164, \
      0.90756616766447684164, \
      0.90756616766447684164, \
      0.15801098912608321778, \
      0.15801098912608321778, \
      0.15801098912608321778, \
      0.15801098912608321778, \
      0.55864014423757180072, \
      0.55864014423757180072, \
      0.55864014423757180072, \
      0.55864014423757180072, \
      0.76553411212536370822, \
      0.76553411212536370822, \
      0.76553411212536370822, \
      0.76553411212536370822, \
      0.12038628177040819334, \
      0.12038628177040819334, \
      0.12038628177040819334, \
      0.12038628177040819334, \
      0.16540042455816997280, \
      0.16540042455816997280, \
      0.16540042455816997280, \
      0.16540042455816997280, \
      0.16540042455816997280, \
      0.16540042455816997280, \
      0.16540042455816997280, \
      0.16540042455816997280, \
      0.07191647566286844817, \
      0.07191647566286844817, \
      0.07191647566286844817, \
      0.07191647566286844817, \
      0.07191647566286844817, \
      0.07191647566286844817, \
      0.07191647566286844817, \
      0.07191647566286844817, \
      0.24369366228681560438, \
      0.24369366228681560438, \
      0.24369366228681560438, \
      0.24369366228681560438, \
      0.24369366228681560438, \
      0.24369366228681560438, \
      0.24369366228681560438, \
      0.24369366228681560438, \
      0.03997911405124788403, \
      0.03997911405124788403, \
      0.03997911405124788403, \
      0.03997911405124788403, \
      0.03997911405124788403, \
      0.03997911405124788403, \
      0.03997911405124788403, \
      0.03997911405124788403, \
      0.52403522696450499652, \
      0.52403522696450499652, \
      0.52403522696450499652, \
      0.52403522696450499652, \
      0.52403522696450499652, \
      0.52403522696450499652, \
      0.52403522696450499652, \
      0.52403522696450499652, \
      0.06332251756914623886, \
      0.06332251756914623886, \
      0.06332251756914623886, \
      0.06332251756914623886, \
      0.06332251756914623886, \
      0.06332251756914623886, \
      0.06332251756914623886, \
      0.06332251756914623886, \
      0.00627167365301165187, \
      0.00627167365301165187, \
      0.00627167365301165187, \
      0.00627167365301165187, \
      0.00627167365301165187, \
      0.00627167365301165187, \
      0.00627167365301165187, \
      0.00627167365301165187, \
      0.34612550470442166040, \
      0.34612550470442166040, \
      0.34612550470442166040, \
      0.34612550470442166040, \
      0.34612550470442166040, \
      0.34612550470442166040, \
      0.34612550470442166040, \
      0.34612550470442166040, \
      0.04934944134498662344, \
      0.04934944134498662344, \
      0.04934944134498662344, \
      0.04934944134498662344, \
      0.04934944134498662344, \
      0.04934944134498662344, \
      0.04934944134498662344, \
      0.04934944134498662344, \
      0.12050259192784877615, \
      0.12050259192784877615, \
      0.12050259192784877615, \
      0.12050259192784877615, \
      0.12050259192784877615, \
      0.12050259192784877615, \
      0.12050259192784877615, \
      0.12050259192784877615, \
      0.39428120571642771841, \
      0.39428120571642771841, \
      0.39428120571642771841, \
      0.39428120571642771841, \
      0.39428120571642771841, \
      0.39428120571642771841, \
      0.39428120571642771841, \
      0.39428120571642771841, \
      0.00838019453790634500, \
      0.00838019453790634500, \
      0.00838019453790634500, \
      0.00838019453790634500, \
      0.00838019453790634500, \
      0.00838019453790634500, \
      0.00838019453790634500, \
      0.00838019453790634500, \
      0.37991521751516699190, \
      0.37991521751516699190, \
      0.37991521751516699190, \
      0.37991521751516699190, \
      0.37991521751516699190, \
      0.37991521751516699190, \
      0.37991521751516699190, \
      0.37991521751516699190, \
      0.06658426856019065976, \
      0.06658426856019065976, \
      0.06658426856019065976, \
      0.06658426856019065976, \
      0.06658426856019065976, \
      0.06658426856019065976, \
      0.06658426856019065976, \
      0.06658426856019065976, \
      0.01360996700708025364, \
      0.01360996700708025364, \
      0.01360996700708025364, \
      0.01360996700708025364, \
      0.01360996700708025364, \
      0.01360996700708025364, \
      0.01360996700708025364, \
      0.01360996700708025364, \
      0.67377911630059594827, \
      0.67377911630059594827, \
      0.67377911630059594827, \
      0.67377911630059594827, \
      0.67377911630059594827, \
      0.67377911630059594827, \
      0.67377911630059594827, \
      0.67377911630059594827, \
      0.15122396864513820702, \
      0.15122396864513820702, \
      0.15122396864513820702, \
      0.15122396864513820702, \
      0.15122396864513820702, \
      0.15122396864513820702, \
      0.15122396864513820702, \
      0.15122396864513820702, \
      0.05960704457999711076, \
      0.05960704457999711076, \
      0.05960704457999711076, \
      0.05960704457999711076, \
      0.05960704457999711076, \
      0.05960704457999711076, \
      0.05960704457999711076, \
      0.05960704457999711076, \
      0.15557252093495238521, \
      0.15557252093495238521, \
      0.15557252093495238521, \
      0.15557252093495238521, \
      0.15557252093495238521, \
      0.15557252093495238521, \
      0.15557252093495238521, \
      0.15557252093495238521, \
      0.26467312835339185106, \
      0.26467312835339185106, \
      0.26467312835339185106, \
      0.26467312835339185106, \
      0.26467312835339185106, \
      0.26467312835339185106, \
      0.26467312835339185106, \
      0.26467312835339185106, \
      0.01193065095103094247, \
      0.01193065095103094247, \
      0.01193065095103094247, \
      0.01193065095103094247, \
      0.01193065095103094247, \
      0.01193065095103094247, \
      0.01193065095103094247, \
      0.01193065095103094247, \
      0.00729413025649284976, \
      0.00729413025649284976, \
      0.00729413025649284976, \
      0.00729413025649284976, \
      0.00729413025649284976, \
      0.00729413025649284976, \
      0.00729413025649284976, \
      0.00729413025649284976 ] )

  w= np.array ( [ \
      0.00013400520132544013, \
      0.00653282923653435328, \
      0.00653282923653435328, \
      0.00653282923653435328, \
      0.00653282923653435328, \
      0.00246267782986044981, \
      0.00246267782986044981, \
      0.00246267782986044981, \
      0.00246267782986044981, \
      0.00236266319877590381, \
      0.00236266319877590381, \
      0.00236266319877590381, \
      0.00236266319877590381, \
      0.00241284626019594179, \
      0.00241284626019594179, \
      0.00241284626019594179, \
      0.00241284626019594179, \
      0.00563939918988414120, \
      0.00563939918988414120, \
      0.00563939918988414120, \
      0.00563939918988414120, \
      0.00530879464537392220, \
      0.00530879464537392220, \
      0.00530879464537392220, \
      0.00530879464537392220, \
      0.00330320967760970065, \
      0.00330320967760970065, \
      0.00330320967760970065, \
      0.00330320967760970065, \
      0.00715709687293028703, \
      0.00715709687293028703, \
      0.00715709687293028703, \
      0.00715709687293028703, \
      0.00356020900079922868, \
      0.00356020900079922868, \
      0.00356020900079922868, \
      0.00356020900079922868, \
      0.00286908910615377545, \
      0.00286908910615377545, \
      0.00286908910615377545, \
      0.00286908910615377545, \
      0.00119238795542696220, \
      0.00119238795542696220, \
      0.00119238795542696220, \
      0.00119238795542696220, \
      0.00023570897730274608, \
      0.00023570897730274608, \
      0.00023570897730274608, \
      0.00023570897730274608, \
      0.00332415202652309181, \
      0.00332415202652309181, \
      0.00332415202652309181, \
      0.00332415202652309181, \
      0.00064424498387906620, \
      0.00064424498387906620, \
      0.00064424498387906620, \
      0.00064424498387906620, \
      0.00093040828397316332, \
      0.00093040828397316332, \
      0.00093040828397316332, \
      0.00093040828397316332, \
      0.00061531263855177734, \
      0.00061531263855177734, \
      0.00061531263855177734, \
      0.00061531263855177734, \
      0.00028907482286127771, \
      0.00028907482286127771, \
      0.00028907482286127771, \
      0.00028907482286127771, \
      0.00957928057788382838, \
      0.00957928057788382838, \
      0.00957928057788382838, \
      0.00957928057788382838, \
      0.00256243378291242307, \
      0.00256243378291242307, \
      0.00256243378291242307, \
      0.00256243378291242307, \
      0.00197009710848232650, \
      0.00197009710848232650, \
      0.00197009710848232650, \
      0.00197009710848232650, \
      0.00224853801623185919, \
      0.00224853801623185919, \
      0.00224853801623185919, \
      0.00224853801623185919, \
      0.00178378503667077598, \
      0.00178378503667077598, \
      0.00178378503667077598, \
      0.00178378503667077598, \
      0.00046154884778758861, \
      0.00046154884778758861, \
      0.00046154884778758861, \
      0.00046154884778758861, \
      0.00383567352584877853, \
      0.00383567352584877853, \
      0.00383567352584877853, \
      0.00383567352584877853, \
      0.00424323389268952030, \
      0.00424323389268952030, \
      0.00424323389268952030, \
      0.00424323389268952030, \
      0.00297709850925886605, \
      0.00297709850925886605, \
      0.00297709850925886605, \
      0.00297709850925886605, \
      0.00750097658421174009, \
      0.00750097658421174009, \
      0.00750097658421174009, \
      0.00750097658421174009, \
      0.00208064231905125911, \
      0.00208064231905125911, \
      0.00208064231905125911, \
      0.00208064231905125911, \
      0.00676296550091519920, \
      0.00676296550091519920, \
      0.00676296550091519920, \
      0.00676296550091519920, \
      0.00300587484767854103, \
      0.00300587484767854103, \
      0.00300587484767854103, \
      0.00300587484767854103, \
      0.00569473175276393340, \
      0.00569473175276393340, \
      0.00569473175276393340, \
      0.00569473175276393340, \
      0.00329345228074993208, \
      0.00329345228074993208, \
      0.00329345228074993208, \
      0.00329345228074993208, \
      0.00319343074693561636, \
      0.00319343074693561636, \
      0.00319343074693561636, \
      0.00319343074693561636, \
      0.00300785963957934336, \
      0.00300785963957934336, \
      0.00300785963957934336, \
      0.00300785963957934336, \
      0.00621018081426024000, \
      0.00621018081426024000, \
      0.00621018081426024000, \
      0.00621018081426024000, \
      0.00690380129393601029, \
      0.00690380129393601029, \
      0.00690380129393601029, \
      0.00690380129393601029, \
      0.00010061838637633462, \
      0.00010061838637633462, \
      0.00010061838637633462, \
      0.00010061838637633462, \
      0.00013563078282338245, \
      0.00013563078282338245, \
      0.00013563078282338245, \
      0.00013563078282338245, \
      0.00077893767219553941, \
      0.00077893767219553941, \
      0.00077893767219553941, \
      0.00077893767219553941, \
      0.00267441470336475876, \
      0.00267441470336475876, \
      0.00267441470336475876, \
      0.00267441470336475876, \
      0.00047754594130653132, \
      0.00047754594130653132, \
      0.00047754594130653132, \
      0.00047754594130653132, \
      0.00074066104011807129, \
      0.00074066104011807129, \
      0.00074066104011807129, \
      0.00074066104011807129, \
      0.00529137043945265752, \
      0.00529137043945265752, \
      0.00529137043945265752, \
      0.00529137043945265752, \
      0.00150066461105524858, \
      0.00150066461105524858, \
      0.00150066461105524858, \
      0.00150066461105524858, \
      0.00262627399936291505, \
      0.00262627399936291505, \
      0.00262627399936291505, \
      0.00262627399936291505, \
      0.00106543689917693658, \
      0.00106543689917693658, \
      0.00106543689917693658, \
      0.00106543689917693658, \
      0.00106543689917693658, \
      0.00106543689917693658, \
      0.00106543689917693658, \
      0.00106543689917693658, \
      0.00608072256149797419, \
      0.00608072256149797419, \
      0.00608072256149797419, \
      0.00608072256149797419, \
      0.00608072256149797419, \
      0.00608072256149797419, \
      0.00608072256149797419, \
      0.00608072256149797419, \
      0.00531002301058563358, \
      0.00531002301058563358, \
      0.00531002301058563358, \
      0.00531002301058563358, \
      0.00531002301058563358, \
      0.00531002301058563358, \
      0.00531002301058563358, \
      0.00531002301058563358, \
      0.00202003342483236250, \
      0.00202003342483236250, \
      0.00202003342483236250, \
      0.00202003342483236250, \
      0.00202003342483236250, \
      0.00202003342483236250, \
      0.00202003342483236250, \
      0.00202003342483236250, \
      0.00216470393083745358, \
      0.00216470393083745358, \
      0.00216470393083745358, \
      0.00216470393083745358, \
      0.00216470393083745358, \
      0.00216470393083745358, \
      0.00216470393083745358, \
      0.00216470393083745358, \
      0.00435330698915271062, \
      0.00435330698915271062, \
      0.00435330698915271062, \
      0.00435330698915271062, \
      0.00435330698915271062, \
      0.00435330698915271062, \
      0.00435330698915271062, \
      0.00435330698915271062, \
      0.00068634034778216149, \
      0.00068634034778216149, \
      0.00068634034778216149, \
      0.00068634034778216149, \
      0.00068634034778216149, \
      0.00068634034778216149, \
      0.00068634034778216149, \
      0.00068634034778216149, \
      0.00401906783115373901, \
      0.00401906783115373901, \
      0.00401906783115373901, \
      0.00401906783115373901, \
      0.00401906783115373901, \
      0.00401906783115373901, \
      0.00401906783115373901, \
      0.00401906783115373901, \
      0.00079127284739705225, \
      0.00079127284739705225, \
      0.00079127284739705225, \
      0.00079127284739705225, \
      0.00079127284739705225, \
      0.00079127284739705225, \
      0.00079127284739705225, \
      0.00079127284739705225, \
      0.00244671052896765998, \
      0.00244671052896765998, \
      0.00244671052896765998, \
      0.00244671052896765998, \
      0.00244671052896765998, \
      0.00244671052896765998, \
      0.00244671052896765998, \
      0.00244671052896765998, \
      0.00195038190205695967, \
      0.00195038190205695967, \
      0.00195038190205695967, \
      0.00195038190205695967, \
      0.00195038190205695967, \
      0.00195038190205695967, \
      0.00195038190205695967, \
      0.00195038190205695967, \
      0.00110591593882085814, \
      0.00110591593882085814, \
      0.00110591593882085814, \
      0.00110591593882085814, \
      0.00110591593882085814, \
      0.00110591593882085814, \
      0.00110591593882085814, \
      0.00110591593882085814, \
      0.00503011482374766256, \
      0.00503011482374766256, \
      0.00503011482374766256, \
      0.00503011482374766256, \
      0.00503011482374766256, \
      0.00503011482374766256, \
      0.00503011482374766256, \
      0.00503011482374766256, \
      0.00065967081570031318, \
      0.00065967081570031318, \
      0.00065967081570031318, \
      0.00065967081570031318, \
      0.00065967081570031318, \
      0.00065967081570031318, \
      0.00065967081570031318, \
      0.00065967081570031318, \
      0.00061321639781390126, \
      0.00061321639781390126, \
      0.00061321639781390126, \
      0.00061321639781390126, \
      0.00061321639781390126, \
      0.00061321639781390126, \
      0.00061321639781390126, \
      0.00061321639781390126, \
      0.00089657142446607598, \
      0.00089657142446607598, \
      0.00089657142446607598, \
      0.00089657142446607598, \
      0.00089657142446607598, \
      0.00089657142446607598, \
      0.00089657142446607598, \
      0.00089657142446607598, \
      0.00363983560477118984, \
      0.00363983560477118984, \
      0.00363983560477118984, \
      0.00363983560477118984, \
      0.00363983560477118984, \
      0.00363983560477118984, \
      0.00363983560477118984, \
      0.00363983560477118984, \
      0.00211128919028042220, \
      0.00211128919028042220, \
      0.00211128919028042220, \
      0.00211128919028042220, \
      0.00211128919028042220, \
      0.00211128919028042220, \
      0.00211128919028042220, \
      0.00211128919028042220, \
      0.00570062224543081177, \
      0.00570062224543081177, \
      0.00570062224543081177, \
      0.00570062224543081177, \
      0.00570062224543081177, \
      0.00570062224543081177, \
      0.00570062224543081177, \
      0.00570062224543081177, \
      0.00195532776601042716, \
      0.00195532776601042716, \
      0.00195532776601042716, \
      0.00195532776601042716, \
      0.00195532776601042716, \
      0.00195532776601042716, \
      0.00195532776601042716, \
      0.00195532776601042716, \
      0.00062384953506176009, \
      0.00062384953506176009, \
      0.00062384953506176009, \
      0.00062384953506176009, \
      0.00062384953506176009, \
      0.00062384953506176009, \
      0.00062384953506176009, \
      0.00062384953506176009, \
      0.00151792165402074965, \
      0.00151792165402074965, \
      0.00151792165402074965, \
      0.00151792165402074965, \
      0.00151792165402074965, \
      0.00151792165402074965, \
      0.00151792165402074965, \
      0.00151792165402074965 ] )

  return x, y, z, w

def rule19 ( ):

#*****************************************************************************80
#
## rule19() returns the pyramid quadrature rule of precision 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.37365721634528792361, \
      0.00000000000000000000, \
     -0.37365721634528792361, \
      0.00000000000000000000, \
      0.43752827030428453892, \
      0.00000000000000000000, \
     -0.43752827030428453892, \
      0.00000000000000000000, \
      0.55782756293242685697, \
      0.00000000000000000000, \
     -0.55782756293242685697, \
      0.00000000000000000000, \
      0.27275879229149846417, \
      0.00000000000000000000, \
     -0.27275879229149846417, \
      0.00000000000000000000, \
      0.28872411753825932834, \
      0.00000000000000000000, \
     -0.28872411753825932834, \
      0.00000000000000000000, \
      0.11277465623250763904, \
      0.00000000000000000000, \
     -0.11277465623250763904, \
      0.00000000000000000000, \
      0.65470230415224206499, \
      0.00000000000000000000, \
     -0.65470230415224206499, \
      0.00000000000000000000, \
      0.22295101282662088682, \
      0.00000000000000000000, \
     -0.22295101282662088682, \
      0.00000000000000000000, \
      0.35176689121153298379, \
      0.00000000000000000000, \
     -0.35176689121153298379, \
      0.00000000000000000000, \
      0.20697735413665671600, \
      0.00000000000000000000, \
     -0.20697735413665671600, \
      0.00000000000000000000, \
      0.93111189027726670719, \
      0.00000000000000000000, \
     -0.93111189027726670719, \
      0.00000000000000000000, \
      0.84303358445951348532, \
      0.00000000000000000000, \
     -0.84303358445951348532, \
      0.00000000000000000000, \
      0.07303948013428374075, \
      0.00000000000000000000, \
     -0.07303948013428374075, \
      0.00000000000000000000, \
      0.67807351338628540915, \
      0.00000000000000000000, \
     -0.67807351338628540915, \
      0.00000000000000000000, \
      0.88198482628664209848, \
      0.00000000000000000000, \
     -0.88198482628664209848, \
      0.00000000000000000000, \
      0.38587811686103651310, \
      0.00000000000000000000, \
     -0.38587811686103651310, \
      0.00000000000000000000, \
      0.13708884737518356456, \
      0.00000000000000000000, \
     -0.13708884737518356456, \
      0.00000000000000000000, \
      0.52558521108268729805, \
     -0.52558521108268729805, \
      0.52558521108268729805, \
     -0.52558521108268729805, \
      0.45301642570589800707, \
     -0.45301642570589800707, \
      0.45301642570589800707, \
     -0.45301642570589800707, \
      0.67125116320175959306, \
     -0.67125116320175959306, \
      0.67125116320175959306, \
     -0.67125116320175959306, \
      0.36951418649168821240, \
     -0.36951418649168821240, \
      0.36951418649168821240, \
     -0.36951418649168821240, \
      0.28838223435586252119, \
     -0.28838223435586252119, \
      0.28838223435586252119, \
     -0.28838223435586252119, \
      0.82857238389465803774, \
     -0.82857238389465803774, \
      0.82857238389465803774, \
     -0.82857238389465803774, \
      0.67246070085447195996, \
     -0.67246070085447195996, \
      0.67246070085447195996, \
     -0.67246070085447195996, \
      0.48736689338962557727, \
     -0.48736689338962557727, \
      0.48736689338962557727, \
     -0.48736689338962557727, \
      0.95036644315079843448, \
     -0.95036644315079843448, \
      0.95036644315079843448, \
     -0.95036644315079843448, \
      0.09132353058612172059, \
     -0.09132353058612172059, \
      0.09132353058612172059, \
     -0.09132353058612172059, \
      0.15520695551416591185, \
     -0.15520695551416591185, \
      0.15520695551416591185, \
     -0.15520695551416591185, \
      0.05052806321356113906, \
     -0.05052806321356113906, \
      0.05052806321356113906, \
     -0.05052806321356113906, \
      0.39781392804166187949, \
     -0.39781392804166187949, \
      0.39781392804166187949, \
     -0.39781392804166187949, \
      0.37607913140641990868, \
     -0.37607913140641990868, \
      0.37607913140641990868, \
     -0.37607913140641990868, \
      0.16436382679828262510, \
     -0.16436382679828262510, \
      0.16436382679828262510, \
     -0.16436382679828262510, \
      0.34688925556861166521, \
     -0.34688925556861166521, \
      0.34688925556861166521, \
     -0.34688925556861166521, \
      0.11913325793719439782, \
     -0.11913325793719439782, \
      0.11913325793719439782, \
     -0.11913325793719439782, \
      0.74545838141881970440, \
     -0.74545838141881970440, \
      0.74545838141881970440, \
     -0.74545838141881970440, \
      0.76104952097303479874, \
     -0.76104952097303479874, \
      0.76104952097303479874, \
     -0.76104952097303479874, \
      0.24208120588771878112, \
     -0.24208120588771878112, \
      0.24208120588771878112, \
     -0.24208120588771878112, \
      0.84457983815668913330, \
     -0.84457983815668913330, \
      0.84457983815668913330, \
     -0.84457983815668913330, \
      0.16456465781662479864, \
     -0.16456465781662479864, \
      0.16456465781662479864, \
     -0.16456465781662479864, \
      0.27478423472388602278, \
     -0.27478423472388602278, \
      0.27478423472388602278, \
     -0.27478423472388602278, \
      0.58499194505600049521, \
     -0.58499194505600049521, \
      0.58499194505600049521, \
     -0.58499194505600049521, \
      0.14897381246033866709, \
     -0.14897381246033866709, \
      0.14897381246033866709, \
     -0.14897381246033866709, \
      0.43892903976173064384, \
     -0.43892903976173064384, \
      0.43892903976173064384, \
     -0.43892903976173064384, \
      0.87981971200037256686, \
     -0.87981971200037256686, \
      0.87981971200037256686, \
     -0.87981971200037256686, \
      0.11685331930792351718, \
     -0.11685331930792351718, \
      0.11685331930792351718, \
     -0.11685331930792351718, \
      0.34287164858560836844, \
     -0.34287164858560836844, \
      0.34287164858560836844, \
     -0.34287164858560836844, \
      0.86433279841860011228, \
      0.64222367435367522237, \
     -0.86433279841860011228, \
      0.64222367435367522237, \
      0.86433279841860011228, \
     -0.64222367435367522237, \
     -0.86433279841860011228, \
     -0.64222367435367522237, \
      0.57840479596659710726, \
      0.15700371479211361336, \
     -0.57840479596659710726, \
      0.15700371479211361336, \
      0.57840479596659710726, \
     -0.15700371479211361336, \
     -0.57840479596659710726, \
     -0.15700371479211361336, \
      0.31087991149352928177, \
      0.53916009809927645247, \
     -0.31087991149352928177, \
      0.53916009809927645247, \
      0.31087991149352928177, \
     -0.53916009809927645247, \
     -0.31087991149352928177, \
     -0.53916009809927645247, \
      0.20472565121250529963, \
      0.56505069862686030380, \
     -0.20472565121250529963, \
      0.56505069862686030380, \
      0.20472565121250529963, \
     -0.56505069862686030380, \
     -0.20472565121250529963, \
     -0.56505069862686030380, \
      0.15477148314547456431, \
      0.80087300859132681818, \
     -0.15477148314547456431, \
      0.80087300859132681818, \
      0.15477148314547456431, \
     -0.80087300859132681818, \
     -0.15477148314547456431, \
     -0.80087300859132681818, \
      0.91122224850183075606, \
      0.36196927102445491942, \
     -0.91122224850183075606, \
      0.36196927102445491942, \
      0.91122224850183075606, \
     -0.36196927102445491942, \
     -0.91122224850183075606, \
     -0.36196927102445491942, \
      0.23763934442358639054, \
      0.46054474775257370212, \
     -0.23763934442358639054, \
      0.46054474775257370212, \
      0.23763934442358639054, \
     -0.46054474775257370212, \
     -0.23763934442358639054, \
     -0.46054474775257370212, \
      0.93026675012099768747, \
      0.32159807642681254025, \
     -0.93026675012099768747, \
      0.32159807642681254025, \
      0.93026675012099768747, \
     -0.32159807642681254025, \
     -0.93026675012099768747, \
     -0.32159807642681254025, \
      0.27330670991417554960, \
      0.75417578802823215245, \
     -0.27330670991417554960, \
      0.75417578802823215245, \
      0.27330670991417554960, \
     -0.75417578802823215245, \
     -0.27330670991417554960, \
     -0.75417578802823215245, \
      0.61977908311233775862, \
      0.40094999523846291956, \
     -0.61977908311233775862, \
      0.40094999523846291956, \
      0.61977908311233775862, \
     -0.40094999523846291956, \
     -0.61977908311233775862, \
     -0.40094999523846291956, \
      0.96731797310728928618, \
      0.71750306782387462956, \
     -0.96731797310728928618, \
      0.71750306782387462956, \
      0.96731797310728928618, \
     -0.71750306782387462956, \
     -0.96731797310728928618, \
     -0.71750306782387462956, \
      0.28107596241726462427, \
      0.14469640753388121612, \
     -0.28107596241726462427, \
      0.14469640753388121612, \
      0.28107596241726462427, \
     -0.14469640753388121612, \
     -0.28107596241726462427, \
     -0.14469640753388121612, \
      0.95723494789717944453, \
      0.80544313431837344375, \
     -0.95723494789717944453, \
      0.80544313431837344375, \
      0.95723494789717944453, \
     -0.80544313431837344375, \
     -0.95723494789717944453, \
     -0.80544313431837344375, \
      0.93415043892659577196, \
      0.56426321835446102693, \
     -0.93415043892659577196, \
      0.56426321835446102693, \
      0.93415043892659577196, \
     -0.56426321835446102693, \
     -0.93415043892659577196, \
     -0.56426321835446102693, \
      0.22124438393817494330, \
      0.27637233377156195102, \
     -0.22124438393817494330, \
      0.27637233377156195102, \
      0.22124438393817494330, \
     -0.27637233377156195102, \
     -0.22124438393817494330, \
     -0.27637233377156195102, \
      0.51440860154860901243, \
      0.67110969363741279636, \
     -0.51440860154860901243, \
      0.67110969363741279636, \
      0.51440860154860901243, \
     -0.67110969363741279636, \
     -0.51440860154860901243, \
     -0.67110969363741279636, \
      0.84669681763194848401, \
      0.64763095243614277052, \
     -0.84669681763194848401, \
      0.64763095243614277052, \
      0.84669681763194848401, \
     -0.64763095243614277052, \
     -0.84669681763194848401, \
     -0.64763095243614277052, \
      0.58372340157348212575, \
      0.75878491584810681125, \
     -0.58372340157348212575, \
      0.75878491584810681125, \
      0.58372340157348212575, \
     -0.75878491584810681125, \
     -0.58372340157348212575, \
     -0.75878491584810681125, \
      0.23125484278203506383, \
      0.75795786639659157302, \
     -0.23125484278203506383, \
      0.75795786639659157302, \
      0.23125484278203506383, \
     -0.75795786639659157302, \
     -0.23125484278203506383, \
     -0.75795786639659157302, \
      0.65351981646876278198, \
      0.21186490812432900999, \
     -0.65351981646876278198, \
      0.21186490812432900999, \
      0.65351981646876278198, \
     -0.21186490812432900999, \
     -0.65351981646876278198, \
     -0.21186490812432900999, \
      0.69534501524896896729, \
      0.18605131637198926708, \
     -0.69534501524896896729, \
      0.18605131637198926708, \
      0.69534501524896896729, \
     -0.18605131637198926708, \
     -0.69534501524896896729, \
     -0.18605131637198926708, \
      0.08127234831798690884, \
      0.52410330742380673019, \
     -0.08127234831798690884, \
      0.52410330742380673019, \
      0.08127234831798690884, \
     -0.52410330742380673019, \
     -0.08127234831798690884, \
     -0.52410330742380673019, \
      0.67316244188134488624, \
      0.47074593361034250405, \
     -0.67316244188134488624, \
      0.47074593361034250405, \
      0.67316244188134488624, \
     -0.47074593361034250405, \
     -0.67316244188134488624, \
     -0.47074593361034250405, \
      0.82977152170712553669, \
      0.38456345752643983360, \
     -0.82977152170712553669, \
      0.38456345752643983360, \
      0.82977152170712553669, \
     -0.38456345752643983360, \
     -0.82977152170712553669, \
     -0.38456345752643983360, \
      0.85308428733291663537, \
      0.48551299054356161777, \
     -0.85308428733291663537, \
      0.48551299054356161777, \
      0.85308428733291663537, \
     -0.48551299054356161777, \
     -0.85308428733291663537, \
     -0.48551299054356161777, \
      0.44670731850691264286, \
      0.17757095991022572856, \
     -0.44670731850691264286, \
      0.17757095991022572856, \
      0.44670731850691264286, \
     -0.17757095991022572856, \
     -0.44670731850691264286, \
     -0.17757095991022572856, \
      0.67009672120301455589, \
      0.46199941611318601220, \
     -0.67009672120301455589, \
      0.46199941611318601220, \
      0.67009672120301455589, \
     -0.46199941611318601220, \
     -0.67009672120301455589, \
     -0.46199941611318601220, \
      0.97673360371074724462, \
      0.26790019276269744219, \
     -0.97673360371074724462, \
      0.26790019276269744219, \
      0.97673360371074724462, \
     -0.26790019276269744219, \
     -0.97673360371074724462, \
     -0.26790019276269744219, \
      0.31887900072125263673, \
      0.45381764631367643714, \
     -0.31887900072125263673, \
      0.45381764631367643714, \
      0.31887900072125263673, \
     -0.45381764631367643714, \
     -0.31887900072125263673, \
     -0.45381764631367643714 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.37365721634528792361, \
      0.00000000000000000000, \
     -0.37365721634528792361, \
      0.00000000000000000000, \
      0.43752827030428453892, \
      0.00000000000000000000, \
     -0.43752827030428453892, \
      0.00000000000000000000, \
      0.55782756293242685697, \
      0.00000000000000000000, \
     -0.55782756293242685697, \
      0.00000000000000000000, \
      0.27275879229149846417, \
      0.00000000000000000000, \
     -0.27275879229149846417, \
      0.00000000000000000000, \
      0.28872411753825932834, \
      0.00000000000000000000, \
     -0.28872411753825932834, \
      0.00000000000000000000, \
      0.11277465623250763904, \
      0.00000000000000000000, \
     -0.11277465623250763904, \
      0.00000000000000000000, \
      0.65470230415224206499, \
      0.00000000000000000000, \
     -0.65470230415224206499, \
      0.00000000000000000000, \
      0.22295101282662088682, \
      0.00000000000000000000, \
     -0.22295101282662088682, \
      0.00000000000000000000, \
      0.35176689121153298379, \
      0.00000000000000000000, \
     -0.35176689121153298379, \
      0.00000000000000000000, \
      0.20697735413665671600, \
      0.00000000000000000000, \
     -0.20697735413665671600, \
      0.00000000000000000000, \
      0.93111189027726670719, \
      0.00000000000000000000, \
     -0.93111189027726670719, \
      0.00000000000000000000, \
      0.84303358445951348532, \
      0.00000000000000000000, \
     -0.84303358445951348532, \
      0.00000000000000000000, \
      0.07303948013428374075, \
      0.00000000000000000000, \
     -0.07303948013428374075, \
      0.00000000000000000000, \
      0.67807351338628540915, \
      0.00000000000000000000, \
     -0.67807351338628540915, \
      0.00000000000000000000, \
      0.88198482628664209848, \
      0.00000000000000000000, \
     -0.88198482628664209848, \
      0.00000000000000000000, \
      0.38587811686103651310, \
      0.00000000000000000000, \
     -0.38587811686103651310, \
      0.00000000000000000000, \
      0.13708884737518356456, \
      0.00000000000000000000, \
     -0.13708884737518356456, \
      0.52558521108268729805, \
      0.52558521108268729805, \
     -0.52558521108268729805, \
     -0.52558521108268729805, \
      0.45301642570589800707, \
      0.45301642570589800707, \
     -0.45301642570589800707, \
     -0.45301642570589800707, \
      0.67125116320175959306, \
      0.67125116320175959306, \
     -0.67125116320175959306, \
     -0.67125116320175959306, \
      0.36951418649168821240, \
      0.36951418649168821240, \
     -0.36951418649168821240, \
     -0.36951418649168821240, \
      0.28838223435586252119, \
      0.28838223435586252119, \
     -0.28838223435586252119, \
     -0.28838223435586252119, \
      0.82857238389465803774, \
      0.82857238389465803774, \
     -0.82857238389465803774, \
     -0.82857238389465803774, \
      0.67246070085447195996, \
      0.67246070085447195996, \
     -0.67246070085447195996, \
     -0.67246070085447195996, \
      0.48736689338962557727, \
      0.48736689338962557727, \
     -0.48736689338962557727, \
     -0.48736689338962557727, \
      0.95036644315079843448, \
      0.95036644315079843448, \
     -0.95036644315079843448, \
     -0.95036644315079843448, \
      0.09132353058612172059, \
      0.09132353058612172059, \
     -0.09132353058612172059, \
     -0.09132353058612172059, \
      0.15520695551416591185, \
      0.15520695551416591185, \
     -0.15520695551416591185, \
     -0.15520695551416591185, \
      0.05052806321356113906, \
      0.05052806321356113906, \
     -0.05052806321356113906, \
     -0.05052806321356113906, \
      0.39781392804166187949, \
      0.39781392804166187949, \
     -0.39781392804166187949, \
     -0.39781392804166187949, \
      0.37607913140641990868, \
      0.37607913140641990868, \
     -0.37607913140641990868, \
     -0.37607913140641990868, \
      0.16436382679828262510, \
      0.16436382679828262510, \
     -0.16436382679828262510, \
     -0.16436382679828262510, \
      0.34688925556861166521, \
      0.34688925556861166521, \
     -0.34688925556861166521, \
     -0.34688925556861166521, \
      0.11913325793719439782, \
      0.11913325793719439782, \
     -0.11913325793719439782, \
     -0.11913325793719439782, \
      0.74545838141881970440, \
      0.74545838141881970440, \
     -0.74545838141881970440, \
     -0.74545838141881970440, \
      0.76104952097303479874, \
      0.76104952097303479874, \
     -0.76104952097303479874, \
     -0.76104952097303479874, \
      0.24208120588771878112, \
      0.24208120588771878112, \
     -0.24208120588771878112, \
     -0.24208120588771878112, \
      0.84457983815668913330, \
      0.84457983815668913330, \
     -0.84457983815668913330, \
     -0.84457983815668913330, \
      0.16456465781662479864, \
      0.16456465781662479864, \
     -0.16456465781662479864, \
     -0.16456465781662479864, \
      0.27478423472388602278, \
      0.27478423472388602278, \
     -0.27478423472388602278, \
     -0.27478423472388602278, \
      0.58499194505600049521, \
      0.58499194505600049521, \
     -0.58499194505600049521, \
     -0.58499194505600049521, \
      0.14897381246033866709, \
      0.14897381246033866709, \
     -0.14897381246033866709, \
     -0.14897381246033866709, \
      0.43892903976173064384, \
      0.43892903976173064384, \
     -0.43892903976173064384, \
     -0.43892903976173064384, \
      0.87981971200037256686, \
      0.87981971200037256686, \
     -0.87981971200037256686, \
     -0.87981971200037256686, \
      0.11685331930792351718, \
      0.11685331930792351718, \
     -0.11685331930792351718, \
     -0.11685331930792351718, \
      0.34287164858560836844, \
      0.34287164858560836844, \
     -0.34287164858560836844, \
     -0.34287164858560836844, \
      0.64222367435367522237, \
      0.86433279841860011228, \
      0.64222367435367522237, \
     -0.86433279841860011228, \
     -0.64222367435367522237, \
      0.86433279841860011228, \
     -0.64222367435367522237, \
     -0.86433279841860011228, \
      0.15700371479211361336, \
      0.57840479596659710726, \
      0.15700371479211361336, \
     -0.57840479596659710726, \
     -0.15700371479211361336, \
      0.57840479596659710726, \
     -0.15700371479211361336, \
     -0.57840479596659710726, \
      0.53916009809927645247, \
      0.31087991149352928177, \
      0.53916009809927645247, \
     -0.31087991149352928177, \
     -0.53916009809927645247, \
      0.31087991149352928177, \
     -0.53916009809927645247, \
     -0.31087991149352928177, \
      0.56505069862686030380, \
      0.20472565121250529963, \
      0.56505069862686030380, \
     -0.20472565121250529963, \
     -0.56505069862686030380, \
      0.20472565121250529963, \
     -0.56505069862686030380, \
     -0.20472565121250529963, \
      0.80087300859132681818, \
      0.15477148314547456431, \
      0.80087300859132681818, \
     -0.15477148314547456431, \
     -0.80087300859132681818, \
      0.15477148314547456431, \
     -0.80087300859132681818, \
     -0.15477148314547456431, \
      0.36196927102445491942, \
      0.91122224850183075606, \
      0.36196927102445491942, \
     -0.91122224850183075606, \
     -0.36196927102445491942, \
      0.91122224850183075606, \
     -0.36196927102445491942, \
     -0.91122224850183075606, \
      0.46054474775257370212, \
      0.23763934442358639054, \
      0.46054474775257370212, \
     -0.23763934442358639054, \
     -0.46054474775257370212, \
      0.23763934442358639054, \
     -0.46054474775257370212, \
     -0.23763934442358639054, \
      0.32159807642681254025, \
      0.93026675012099768747, \
      0.32159807642681254025, \
     -0.93026675012099768747, \
     -0.32159807642681254025, \
      0.93026675012099768747, \
     -0.32159807642681254025, \
     -0.93026675012099768747, \
      0.75417578802823215245, \
      0.27330670991417554960, \
      0.75417578802823215245, \
     -0.27330670991417554960, \
     -0.75417578802823215245, \
      0.27330670991417554960, \
     -0.75417578802823215245, \
     -0.27330670991417554960, \
      0.40094999523846291956, \
      0.61977908311233775862, \
      0.40094999523846291956, \
     -0.61977908311233775862, \
     -0.40094999523846291956, \
      0.61977908311233775862, \
     -0.40094999523846291956, \
     -0.61977908311233775862, \
      0.71750306782387462956, \
      0.96731797310728928618, \
      0.71750306782387462956, \
     -0.96731797310728928618, \
     -0.71750306782387462956, \
      0.96731797310728928618, \
     -0.71750306782387462956, \
     -0.96731797310728928618, \
      0.14469640753388121612, \
      0.28107596241726462427, \
      0.14469640753388121612, \
     -0.28107596241726462427, \
     -0.14469640753388121612, \
      0.28107596241726462427, \
     -0.14469640753388121612, \
     -0.28107596241726462427, \
      0.80544313431837344375, \
      0.95723494789717944453, \
      0.80544313431837344375, \
     -0.95723494789717944453, \
     -0.80544313431837344375, \
      0.95723494789717944453, \
     -0.80544313431837344375, \
     -0.95723494789717944453, \
      0.56426321835446102693, \
      0.93415043892659577196, \
      0.56426321835446102693, \
     -0.93415043892659577196, \
     -0.56426321835446102693, \
      0.93415043892659577196, \
     -0.56426321835446102693, \
     -0.93415043892659577196, \
      0.27637233377156195102, \
      0.22124438393817494330, \
      0.27637233377156195102, \
     -0.22124438393817494330, \
     -0.27637233377156195102, \
      0.22124438393817494330, \
     -0.27637233377156195102, \
     -0.22124438393817494330, \
      0.67110969363741279636, \
      0.51440860154860901243, \
      0.67110969363741279636, \
     -0.51440860154860901243, \
     -0.67110969363741279636, \
      0.51440860154860901243, \
     -0.67110969363741279636, \
     -0.51440860154860901243, \
      0.64763095243614277052, \
      0.84669681763194848401, \
      0.64763095243614277052, \
     -0.84669681763194848401, \
     -0.64763095243614277052, \
      0.84669681763194848401, \
     -0.64763095243614277052, \
     -0.84669681763194848401, \
      0.75878491584810681125, \
      0.58372340157348212575, \
      0.75878491584810681125, \
     -0.58372340157348212575, \
     -0.75878491584810681125, \
      0.58372340157348212575, \
     -0.75878491584810681125, \
     -0.58372340157348212575, \
      0.75795786639659157302, \
      0.23125484278203506383, \
      0.75795786639659157302, \
     -0.23125484278203506383, \
     -0.75795786639659157302, \
      0.23125484278203506383, \
     -0.75795786639659157302, \
     -0.23125484278203506383, \
      0.21186490812432900999, \
      0.65351981646876278198, \
      0.21186490812432900999, \
     -0.65351981646876278198, \
     -0.21186490812432900999, \
      0.65351981646876278198, \
     -0.21186490812432900999, \
     -0.65351981646876278198, \
      0.18605131637198926708, \
      0.69534501524896896729, \
      0.18605131637198926708, \
     -0.69534501524896896729, \
     -0.18605131637198926708, \
      0.69534501524896896729, \
     -0.18605131637198926708, \
     -0.69534501524896896729, \
      0.52410330742380673019, \
      0.08127234831798690884, \
      0.52410330742380673019, \
     -0.08127234831798690884, \
     -0.52410330742380673019, \
      0.08127234831798690884, \
     -0.52410330742380673019, \
     -0.08127234831798690884, \
      0.47074593361034250405, \
      0.67316244188134488624, \
      0.47074593361034250405, \
     -0.67316244188134488624, \
     -0.47074593361034250405, \
      0.67316244188134488624, \
     -0.47074593361034250405, \
     -0.67316244188134488624, \
      0.38456345752643983360, \
      0.82977152170712553669, \
      0.38456345752643983360, \
     -0.82977152170712553669, \
     -0.38456345752643983360, \
      0.82977152170712553669, \
     -0.38456345752643983360, \
     -0.82977152170712553669, \
      0.48551299054356161777, \
      0.85308428733291663537, \
      0.48551299054356161777, \
     -0.85308428733291663537, \
     -0.48551299054356161777, \
      0.85308428733291663537, \
     -0.48551299054356161777, \
     -0.85308428733291663537, \
      0.17757095991022572856, \
      0.44670731850691264286, \
      0.17757095991022572856, \
     -0.44670731850691264286, \
     -0.17757095991022572856, \
      0.44670731850691264286, \
     -0.17757095991022572856, \
     -0.44670731850691264286, \
      0.46199941611318601220, \
      0.67009672120301455589, \
      0.46199941611318601220, \
     -0.67009672120301455589, \
     -0.46199941611318601220, \
      0.67009672120301455589, \
     -0.46199941611318601220, \
     -0.67009672120301455589, \
      0.26790019276269744219, \
      0.97673360371074724462, \
      0.26790019276269744219, \
     -0.97673360371074724462, \
     -0.26790019276269744219, \
      0.97673360371074724462, \
     -0.26790019276269744219, \
     -0.97673360371074724462, \
      0.45381764631367643714, \
      0.31887900072125263673, \
      0.45381764631367643714, \
     -0.31887900072125263673, \
     -0.45381764631367643714, \
      0.31887900072125263673, \
     -0.45381764631367643714, \
     -0.31887900072125263673 ] )

  z = np.array ( [ \
      0.96739133523703502160, \
      0.54366532464638728239, \
      0.41887560622759456574, \
      0.41887560622759456574, \
      0.41887560622759456574, \
      0.41887560622759456574, \
      0.29774894445685839983, \
      0.29774894445685839983, \
      0.29774894445685839983, \
      0.29774894445685839983, \
      0.43632558904359264318, \
      0.43632558904359264318, \
      0.43632558904359264318, \
      0.43632558904359264318, \
      0.13123475865230219140, \
      0.13123475865230219140, \
      0.13123475865230219140, \
      0.13123475865230219140, \
      0.56882169546815719574, \
      0.56882169546815719574, \
      0.56882169546815719574, \
      0.56882169546815719574, \
      0.66230573631886058283, \
      0.66230573631886058283, \
      0.66230573631886058283, \
      0.66230573631886058283, \
      0.21963789124598576130, \
      0.21963789124598576130, \
      0.21963789124598576130, \
      0.21963789124598576130, \
      0.22732696332834559372, \
      0.22732696332834559372, \
      0.22732696332834559372, \
      0.22732696332834559372, \
      0.00541751512625303269, \
      0.00541751512625303269, \
      0.00541751512625303269, \
      0.00541751512625303269, \
      0.79294906136483345183, \
      0.79294906136483345183, \
      0.79294906136483345183, \
      0.79294906136483345183, \
      0.04180662980331771583, \
      0.04180662980331771583, \
      0.04180662980331771583, \
      0.04180662980331771583, \
      0.13615518064579532065, \
      0.13615518064579532065, \
      0.13615518064579532065, \
      0.13615518064579532065, \
      0.91875475602806166986, \
      0.91875475602806166986, \
      0.91875475602806166986, \
      0.91875475602806166986, \
      0.30191905621780101843, \
      0.30191905621780101843, \
      0.30191905621780101843, \
      0.30191905621780101843, \
      0.00938749984908901144, \
      0.00938749984908901144, \
      0.00938749984908901144, \
      0.00938749984908901144, \
      0.60658598457462375997, \
      0.60658598457462375997, \
      0.60658598457462375997, \
      0.60658598457462375997, \
      0.75353482202105526166, \
      0.75353482202105526166, \
      0.75353482202105526166, \
      0.75353482202105526166, \
      0.44086853690608979184, \
      0.44086853690608979184, \
      0.44086853690608979184, \
      0.44086853690608979184, \
      0.41889775081556313019, \
      0.41889775081556313019, \
      0.41889775081556313019, \
      0.41889775081556313019, \
      0.01251810432139164979, \
      0.01251810432139164979, \
      0.01251810432139164979, \
      0.01251810432139164979, \
      0.62460148383811031625, \
      0.62460148383811031625, \
      0.62460148383811031625, \
      0.62460148383811031625, \
      0.05439973273857341696, \
      0.05439973273857341696, \
      0.05439973273857341696, \
      0.05439973273857341696, \
      0.16191862193166678408, \
      0.16191862193166678408, \
      0.16191862193166678408, \
      0.16191862193166678408, \
      0.29300331383428240839, \
      0.29300331383428240839, \
      0.29300331383428240839, \
      0.29300331383428240839, \
      0.26342658893870185555, \
      0.26342658893870185555, \
      0.26342658893870185555, \
      0.26342658893870185555, \
      0.01127614473867753070, \
      0.01127614473867753070, \
      0.01127614473867753070, \
      0.01127614473867753070, \
      0.35807984614999605055, \
      0.35807984614999605055, \
      0.35807984614999605055, \
      0.35807984614999605055, \
      0.47141886716708586436, \
      0.47141886716708586436, \
      0.47141886716708586436, \
      0.47141886716708586436, \
      0.85446407112095401626, \
      0.85446407112095401626, \
      0.85446407112095401626, \
      0.85446407112095401626, \
      0.12930311691456014556, \
      0.12930311691456014556, \
      0.12930311691456014556, \
      0.12930311691456014556, \
      0.07899233073306564934, \
      0.07899233073306564934, \
      0.07899233073306564934, \
      0.07899233073306564934, \
      0.01672886065733771022, \
      0.01672886065733771022, \
      0.01672886065733771022, \
      0.01672886065733771022, \
      0.38850504372376110096, \
      0.38850504372376110096, \
      0.38850504372376110096, \
      0.38850504372376110096, \
      0.84754739757493258168, \
      0.84754739757493258168, \
      0.84754739757493258168, \
      0.84754739757493258168, \
      0.16263602800181631292, \
      0.16263602800181631292, \
      0.16263602800181631292, \
      0.16263602800181631292, \
      0.07862268330374026781, \
      0.07862268330374026781, \
      0.07862268330374026781, \
      0.07862268330374026781, \
      0.32028064376194109730, \
      0.32028064376194109730, \
      0.32028064376194109730, \
      0.32028064376194109730, \
      0.01382133423647079022, \
      0.01382133423647079022, \
      0.01382133423647079022, \
      0.01382133423647079022, \
      0.76877522504357953537, \
      0.76877522504357953537, \
      0.76877522504357953537, \
      0.76877522504357953537, \
      0.53014024087305255950, \
      0.53014024087305255950, \
      0.53014024087305255950, \
      0.53014024087305255950, \
      0.30089238244412036538, \
      0.30089238244412036538, \
      0.30089238244412036538, \
      0.30089238244412036538, \
      0.61673192700785928189, \
      0.61673192700785928189, \
      0.61673192700785928189, \
      0.61673192700785928189, \
      0.01376377254881575897, \
      0.01376377254881575897, \
      0.01376377254881575897, \
      0.01376377254881575897, \
      0.07210305012229555055, \
      0.07210305012229555055, \
      0.07210305012229555055, \
      0.07210305012229555055, \
      0.06238118616203952582, \
      0.06238118616203952582, \
      0.06238118616203952582, \
      0.06238118616203952582, \
      0.58557953491658876199, \
      0.58557953491658876199, \
      0.58557953491658876199, \
      0.58557953491658876199, \
      0.11791920647798490029, \
      0.11791920647798490029, \
      0.11791920647798490029, \
      0.11791920647798490029, \
      0.11791920647798490029, \
      0.11791920647798490029, \
      0.11791920647798490029, \
      0.11791920647798490029, \
      0.11142523412928505289, \
      0.11142523412928505289, \
      0.11142523412928505289, \
      0.11142523412928505289, \
      0.11142523412928505289, \
      0.11142523412928505289, \
      0.11142523412928505289, \
      0.11142523412928505289, \
      0.27502672812187933804, \
      0.27502672812187933804, \
      0.27502672812187933804, \
      0.27502672812187933804, \
      0.27502672812187933804, \
      0.27502672812187933804, \
      0.27502672812187933804, \
      0.27502672812187933804, \
      0.34728469726559213493, \
      0.34728469726559213493, \
      0.34728469726559213493, \
      0.34728469726559213493, \
      0.34728469726559213493, \
      0.34728469726559213493, \
      0.34728469726559213493, \
      0.34728469726559213493, \
      0.07549551730236130076, \
      0.07549551730236130076, \
      0.07549551730236130076, \
      0.07549551730236130076, \
      0.07549551730236130076, \
      0.07549551730236130076, \
      0.07549551730236130076, \
      0.07549551730236130076, \
      0.03464296962031117311, \
      0.03464296962031117311, \
      0.03464296962031117311, \
      0.03464296962031117311, \
      0.03464296962031117311, \
      0.03464296962031117311, \
      0.03464296962031117311, \
      0.03464296962031117311, \
      0.20441529779235670383, \
      0.20441529779235670383, \
      0.20441529779235670383, \
      0.20441529779235670383, \
      0.20441529779235670383, \
      0.20441529779235670383, \
      0.20441529779235670383, \
      0.20441529779235670383, \
      0.06972695561067981940, \
      0.06972695561067981940, \
      0.06972695561067981940, \
      0.06972695561067981940, \
      0.06972695561067981940, \
      0.06972695561067981940, \
      0.06972695561067981940, \
      0.06972695561067981940, \
      0.21998980465815576313, \
      0.21998980465815576313, \
      0.21998980465815576313, \
      0.21998980465815576313, \
      0.21998980465815576313, \
      0.21998980465815576313, \
      0.21998980465815576313, \
      0.21998980465815576313, \
      0.36462254947959177320, \
      0.36462254947959177320, \
      0.36462254947959177320, \
      0.36462254947959177320, \
      0.36462254947959177320, \
      0.36462254947959177320, \
      0.36462254947959177320, \
      0.36462254947959177320, \
      0.00458633496122378467, \
      0.00458633496122378467, \
      0.00458633496122378467, \
      0.00458633496122378467, \
      0.00458633496122378467, \
      0.00458633496122378467, \
      0.00458633496122378467, \
      0.00458633496122378467, \
      0.66642300488713057671, \
      0.66642300488713057671, \
      0.66642300488713057671, \
      0.66642300488713057671, \
      0.66642300488713057671, \
      0.66642300488713057671, \
      0.66642300488713057671, \
      0.66642300488713057671, \
      0.03975302308577006311, \
      0.03975302308577006311, \
      0.03975302308577006311, \
      0.03975302308577006311, \
      0.03975302308577006311, \
      0.03975302308577006311, \
      0.03975302308577006311, \
      0.03975302308577006311, \
      0.03073598825835915579, \
      0.03073598825835915579, \
      0.03073598825835915579, \
      0.03073598825835915579, \
      0.03073598825835915579, \
      0.03073598825835915579, \
      0.03073598825835915579, \
      0.03073598825835915579, \
      0.72077351789673316240, \
      0.72077351789673316240, \
      0.72077351789673316240, \
      0.72077351789673316240, \
      0.72077351789673316240, \
      0.72077351789673316240, \
      0.72077351789673316240, \
      0.72077351789673316240, \
      0.14036094696120685055, \
      0.14036094696120685055, \
      0.14036094696120685055, \
      0.14036094696120685055, \
      0.14036094696120685055, \
      0.14036094696120685055, \
      0.14036094696120685055, \
      0.14036094696120685055, \
      0.05264191965632582237, \
      0.05264191965632582237, \
      0.05264191965632582237, \
      0.05264191965632582237, \
      0.05264191965632582237, \
      0.05264191965632582237, \
      0.05264191965632582237, \
      0.05264191965632582237, \
      0.22702332489421667150, \
      0.22702332489421667150, \
      0.22702332489421667150, \
      0.22702332489421667150, \
      0.22702332489421667150, \
      0.22702332489421667150, \
      0.22702332489421667150, \
      0.22702332489421667150, \
      0.02881326163838642679, \
      0.02881326163838642679, \
      0.02881326163838642679, \
      0.02881326163838642679, \
      0.02881326163838642679, \
      0.02881326163838642679, \
      0.02881326163838642679, \
      0.02881326163838642679, \
      0.00532138936818496097, \
      0.00532138936818496097, \
      0.00532138936818496097, \
      0.00532138936818496097, \
      0.00532138936818496097, \
      0.00532138936818496097, \
      0.00532138936818496097, \
      0.00532138936818496097, \
      0.15917093130673495849, \
      0.15917093130673495849, \
      0.15917093130673495849, \
      0.15917093130673495849, \
      0.15917093130673495849, \
      0.15917093130673495849, \
      0.15917093130673495849, \
      0.15917093130673495849, \
      0.04286780869626788393, \
      0.04286780869626788393, \
      0.04286780869626788393, \
      0.04286780869626788393, \
      0.04286780869626788393, \
      0.04286780869626788393, \
      0.04286780869626788393, \
      0.04286780869626788393, \
      0.22819215603891684907, \
      0.22819215603891684907, \
      0.22819215603891684907, \
      0.22819215603891684907, \
      0.22819215603891684907, \
      0.22819215603891684907, \
      0.22819215603891684907, \
      0.22819215603891684907, \
      0.11497584756253050042, \
      0.11497584756253050042, \
      0.11497584756253050042, \
      0.11497584756253050042, \
      0.11497584756253050042, \
      0.11497584756253050042, \
      0.11497584756253050042, \
      0.11497584756253050042, \
      0.00654660357363916808, \
      0.00654660357363916808, \
      0.00654660357363916808, \
      0.00654660357363916808, \
      0.00654660357363916808, \
      0.00654660357363916808, \
      0.00654660357363916808, \
      0.00654660357363916808, \
      0.48896580613114126734, \
      0.48896580613114126734, \
      0.48896580613114126734, \
      0.48896580613114126734, \
      0.48896580613114126734, \
      0.48896580613114126734, \
      0.48896580613114126734, \
      0.48896580613114126734, \
      0.05843691849737928795, \
      0.05843691849737928795, \
      0.05843691849737928795, \
      0.05843691849737928795, \
      0.05843691849737928795, \
      0.05843691849737928795, \
      0.05843691849737928795, \
      0.05843691849737928795, \
      0.00610498541327420680, \
      0.00610498541327420680, \
      0.00610498541327420680, \
      0.00610498541327420680, \
      0.00610498541327420680, \
      0.00610498541327420680, \
      0.00610498541327420680, \
      0.00610498541327420680, \
      0.53408664015576723383, \
      0.53408664015576723383, \
      0.53408664015576723383, \
      0.53408664015576723383, \
      0.53408664015576723383, \
      0.53408664015576723383, \
      0.53408664015576723383, \
      0.53408664015576723383 ] )

  w= np.array ( [ \
      0.00012870022397472401, \
      0.00539076125430030910, \
      0.00666687105780559754, \
      0.00666687105780559754, \
      0.00666687105780559754, \
      0.00666687105780559754, \
      0.00619801121379879964, \
      0.00619801121379879964, \
      0.00619801121379879964, \
      0.00619801121379879964, \
      0.00119690394217259041, \
      0.00119690394217259041, \
      0.00119690394217259041, \
      0.00119690394217259041, \
      0.00900035197624313339, \
      0.00900035197624313339, \
      0.00900035197624313339, \
      0.00900035197624313339, \
      0.00416463710538401977, \
      0.00416463710538401977, \
      0.00416463710538401977, \
      0.00416463710538401977, \
      0.00182449720872727593, \
      0.00182449720872727593, \
      0.00182449720872727593, \
      0.00182449720872727593, \
      0.00452371868333050885, \
      0.00452371868333050885, \
      0.00452371868333050885, \
      0.00452371868333050885, \
      0.00816111606481412406, \
      0.00816111606481412406, \
      0.00816111606481412406, \
      0.00816111606481412406, \
      0.00164832682863707940, \
      0.00164832682863707940, \
      0.00164832682863707940, \
      0.00164832682863707940, \
      0.00055714923095003237, \
      0.00055714923095003237, \
      0.00055714923095003237, \
      0.00055714923095003237, \
      0.00111821525219482697, \
      0.00111821525219482697, \
      0.00111821525219482697, \
      0.00111821525219482697, \
      0.00188581015876115280, \
      0.00188581015876115280, \
      0.00188581015876115280, \
      0.00188581015876115280, \
      0.00028281012262636759, \
      0.00028281012262636759, \
      0.00028281012262636759, \
      0.00028281012262636759, \
      0.00181586354615248828, \
      0.00181586354615248828, \
      0.00181586354615248828, \
      0.00181586354615248828, \
      0.00124708244822032614, \
      0.00124708244822032614, \
      0.00124708244822032614, \
      0.00124708244822032614, \
      0.00107416255302727809, \
      0.00107416255302727809, \
      0.00107416255302727809, \
      0.00107416255302727809, \
      0.00257977077737831396, \
      0.00257977077737831396, \
      0.00257977077737831396, \
      0.00257977077737831396, \
      0.00091701544972603221, \
      0.00091701544972603221, \
      0.00091701544972603221, \
      0.00091701544972603221, \
      0.00306877872117356605, \
      0.00306877872117356605, \
      0.00306877872117356605, \
      0.00306877872117356605, \
      0.00187105817191728823, \
      0.00187105817191728823, \
      0.00187105817191728823, \
      0.00187105817191728823, \
      0.00015369093908062739, \
      0.00015369093908062739, \
      0.00015369093908062739, \
      0.00015369093908062739, \
      0.00384529073211040779, \
      0.00384529073211040779, \
      0.00384529073211040779, \
      0.00384529073211040779, \
      0.00022431161642440681, \
      0.00022431161642440681, \
      0.00022431161642440681, \
      0.00022431161642440681, \
      0.00084020876261339610, \
      0.00084020876261339610, \
      0.00084020876261339610, \
      0.00084020876261339610, \
      0.00304195767454043140, \
      0.00304195767454043140, \
      0.00304195767454043140, \
      0.00304195767454043140, \
      0.00022948417669879317, \
      0.00022948417669879317, \
      0.00022948417669879317, \
      0.00022948417669879317, \
      0.00418242059186963843, \
      0.00418242059186963843, \
      0.00418242059186963843, \
      0.00418242059186963843, \
      0.00632709108150545339, \
      0.00632709108150545339, \
      0.00632709108150545339, \
      0.00632709108150545339, \
      0.00075928340059512709, \
      0.00075928340059512709, \
      0.00075928340059512709, \
      0.00075928340059512709, \
      0.00459683666227672476, \
      0.00459683666227672476, \
      0.00459683666227672476, \
      0.00459683666227672476, \
      0.00276636427423579932, \
      0.00276636427423579932, \
      0.00276636427423579932, \
      0.00276636427423579932, \
      0.00214485080151055087, \
      0.00214485080151055087, \
      0.00214485080151055087, \
      0.00214485080151055087, \
      0.00528314448618283795, \
      0.00528314448618283795, \
      0.00528314448618283795, \
      0.00528314448618283795, \
      0.00048810523226141780, \
      0.00048810523226141780, \
      0.00048810523226141780, \
      0.00048810523226141780, \
      0.00212069545834849948, \
      0.00212069545834849948, \
      0.00212069545834849948, \
      0.00212069545834849948, \
      0.00161506019948201812, \
      0.00161506019948201812, \
      0.00161506019948201812, \
      0.00161506019948201812, \
      0.00694225709294844437, \
      0.00694225709294844437, \
      0.00694225709294844437, \
      0.00694225709294844437, \
      0.00100268302008121369, \
      0.00100268302008121369, \
      0.00100268302008121369, \
      0.00100268302008121369, \
      0.00092077531674916973, \
      0.00092077531674916973, \
      0.00092077531674916973, \
      0.00092077531674916973, \
      0.00355616947744542573, \
      0.00355616947744542573, \
      0.00355616947744542573, \
      0.00355616947744542573, \
      0.00218617871329652470, \
      0.00218617871329652470, \
      0.00218617871329652470, \
      0.00218617871329652470, \
      0.00269165166203209818, \
      0.00269165166203209818, \
      0.00269165166203209818, \
      0.00269165166203209818, \
      0.00301674010475732127, \
      0.00301674010475732127, \
      0.00301674010475732127, \
      0.00301674010475732127, \
      0.00074666452415505266, \
      0.00074666452415505266, \
      0.00074666452415505266, \
      0.00074666452415505266, \
      0.00299748233690233252, \
      0.00299748233690233252, \
      0.00299748233690233252, \
      0.00299748233690233252, \
      0.00144784702606324633, \
      0.00144784702606324633, \
      0.00144784702606324633, \
      0.00144784702606324633, \
      0.00107280962935336075, \
      0.00107280962935336075, \
      0.00107280962935336075, \
      0.00107280962935336075, \
      0.00107280962935336075, \
      0.00107280962935336075, \
      0.00107280962935336075, \
      0.00107280962935336075, \
      0.00483903734837801830, \
      0.00483903734837801830, \
      0.00483903734837801830, \
      0.00483903734837801830, \
      0.00483903734837801830, \
      0.00483903734837801830, \
      0.00483903734837801830, \
      0.00483903734837801830, \
      0.00274709905982003805, \
      0.00274709905982003805, \
      0.00274709905982003805, \
      0.00274709905982003805, \
      0.00274709905982003805, \
      0.00274709905982003805, \
      0.00274709905982003805, \
      0.00274709905982003805, \
      0.00433501688902940795, \
      0.00433501688902940795, \
      0.00433501688902940795, \
      0.00433501688902940795, \
      0.00433501688902940795, \
      0.00433501688902940795, \
      0.00433501688902940795, \
      0.00433501688902940795, \
      0.00271810015984954700, \
      0.00271810015984954700, \
      0.00271810015984954700, \
      0.00271810015984954700, \
      0.00271810015984954700, \
      0.00271810015984954700, \
      0.00271810015984954700, \
      0.00271810015984954700, \
      0.00091685473986105473, \
      0.00091685473986105473, \
      0.00091685473986105473, \
      0.00091685473986105473, \
      0.00091685473986105473, \
      0.00091685473986105473, \
      0.00091685473986105473, \
      0.00091685473986105473, \
      0.00680895101968847279, \
      0.00680895101968847279, \
      0.00680895101968847279, \
      0.00680895101968847279, \
      0.00680895101968847279, \
      0.00680895101968847279, \
      0.00680895101968847279, \
      0.00680895101968847279, \
      0.00040138568966109102, \
      0.00040138568966109102, \
      0.00040138568966109102, \
      0.00040138568966109102, \
      0.00040138568966109102, \
      0.00040138568966109102, \
      0.00040138568966109102, \
      0.00040138568966109102, \
      0.00215500289545228485, \
      0.00215500289545228485, \
      0.00215500289545228485, \
      0.00215500289545228485, \
      0.00215500289545228485, \
      0.00215500289545228485, \
      0.00215500289545228485, \
      0.00215500289545228485, \
      0.00161154257302305293, \
      0.00161154257302305293, \
      0.00161154257302305293, \
      0.00161154257302305293, \
      0.00161154257302305293, \
      0.00161154257302305293, \
      0.00161154257302305293, \
      0.00161154257302305293, \
      0.00027434552667444364, \
      0.00027434552667444364, \
      0.00027434552667444364, \
      0.00027434552667444364, \
      0.00027434552667444364, \
      0.00027434552667444364, \
      0.00027434552667444364, \
      0.00027434552667444364, \
      0.00230008297506218524, \
      0.00230008297506218524, \
      0.00230008297506218524, \
      0.00230008297506218524, \
      0.00230008297506218524, \
      0.00230008297506218524, \
      0.00230008297506218524, \
      0.00230008297506218524, \
      0.00029458357590517713, \
      0.00029458357590517713, \
      0.00029458357590517713, \
      0.00029458357590517713, \
      0.00029458357590517713, \
      0.00029458357590517713, \
      0.00029458357590517713, \
      0.00029458357590517713, \
      0.00060073122167725204, \
      0.00060073122167725204, \
      0.00060073122167725204, \
      0.00060073122167725204, \
      0.00060073122167725204, \
      0.00060073122167725204, \
      0.00060073122167725204, \
      0.00060073122167725204, \
      0.00026201750375773298, \
      0.00026201750375773298, \
      0.00026201750375773298, \
      0.00026201750375773298, \
      0.00026201750375773298, \
      0.00026201750375773298, \
      0.00026201750375773298, \
      0.00026201750375773298, \
      0.00419283249870963659, \
      0.00419283249870963659, \
      0.00419283249870963659, \
      0.00419283249870963659, \
      0.00419283249870963659, \
      0.00419283249870963659, \
      0.00419283249870963659, \
      0.00419283249870963659, \
      0.00173629430868813472, \
      0.00173629430868813472, \
      0.00173629430868813472, \
      0.00173629430868813472, \
      0.00173629430868813472, \
      0.00173629430868813472, \
      0.00173629430868813472, \
      0.00173629430868813472, \
      0.00094391016694345316, \
      0.00094391016694345316, \
      0.00094391016694345316, \
      0.00094391016694345316, \
      0.00094391016694345316, \
      0.00094391016694345316, \
      0.00094391016694345316, \
      0.00094391016694345316, \
      0.00217551360850374046, \
      0.00217551360850374046, \
      0.00217551360850374046, \
      0.00217551360850374046, \
      0.00217551360850374046, \
      0.00217551360850374046, \
      0.00217551360850374046, \
      0.00217551360850374046, \
      0.00128339469018335490, \
      0.00128339469018335490, \
      0.00128339469018335490, \
      0.00128339469018335490, \
      0.00128339469018335490, \
      0.00128339469018335490, \
      0.00128339469018335490, \
      0.00128339469018335490, \
      0.00272615049960569979, \
      0.00272615049960569979, \
      0.00272615049960569979, \
      0.00272615049960569979, \
      0.00272615049960569979, \
      0.00272615049960569979, \
      0.00272615049960569979, \
      0.00272615049960569979, \
      0.00318533960385062025, \
      0.00318533960385062025, \
      0.00318533960385062025, \
      0.00318533960385062025, \
      0.00318533960385062025, \
      0.00318533960385062025, \
      0.00318533960385062025, \
      0.00318533960385062025, \
      0.00266309286664456963, \
      0.00266309286664456963, \
      0.00266309286664456963, \
      0.00266309286664456963, \
      0.00266309286664456963, \
      0.00266309286664456963, \
      0.00266309286664456963, \
      0.00266309286664456963, \
      0.00232666846528824418, \
      0.00232666846528824418, \
      0.00232666846528824418, \
      0.00232666846528824418, \
      0.00232666846528824418, \
      0.00232666846528824418, \
      0.00232666846528824418, \
      0.00232666846528824418, \
      0.00097346311519703153, \
      0.00097346311519703153, \
      0.00097346311519703153, \
      0.00097346311519703153, \
      0.00097346311519703153, \
      0.00097346311519703153, \
      0.00097346311519703153, \
      0.00097346311519703153, \
      0.00348345685139948022, \
      0.00348345685139948022, \
      0.00348345685139948022, \
      0.00348345685139948022, \
      0.00348345685139948022, \
      0.00348345685139948022, \
      0.00348345685139948022, \
      0.00348345685139948022, \
      0.00406195421696304172, \
      0.00406195421696304172, \
      0.00406195421696304172, \
      0.00406195421696304172, \
      0.00406195421696304172, \
      0.00406195421696304172, \
      0.00406195421696304172, \
      0.00406195421696304172, \
      0.00033245593568842263, \
      0.00033245593568842263, \
      0.00033245593568842263, \
      0.00033245593568842263, \
      0.00033245593568842263, \
      0.00033245593568842263, \
      0.00033245593568842263, \
      0.00033245593568842263, \
      0.00092328174175319150, \
      0.00092328174175319150, \
      0.00092328174175319150, \
      0.00092328174175319150, \
      0.00092328174175319150, \
      0.00092328174175319150, \
      0.00092328174175319150, \
      0.00092328174175319150 ] )

  return x, y, z, w

def rule20 ( ):

#*****************************************************************************80
#
## rule20() returns the pyramid quadrature rule of precision 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.00000000000000000000, \
      0.48169354344312520499, \
      0.00000000000000000000, \
     -0.48169354344312520499, \
      0.00000000000000000000, \
      0.69858038869870031640, \
      0.00000000000000000000, \
     -0.69858038869870031640, \
      0.00000000000000000000, \
      0.53468657951770970360, \
      0.00000000000000000000, \
     -0.53468657951770970360, \
      0.00000000000000000000, \
      0.42228380878442672852, \
      0.00000000000000000000, \
     -0.42228380878442672852, \
      0.00000000000000000000, \
      0.30680451888779119995, \
      0.00000000000000000000, \
     -0.30680451888779119995, \
      0.00000000000000000000, \
      0.22877498497689821577, \
      0.00000000000000000000, \
     -0.22877498497689821577, \
      0.00000000000000000000, \
      0.55389687412807175892, \
      0.00000000000000000000, \
     -0.55389687412807175892, \
      0.00000000000000000000, \
      0.38489228042331330437, \
      0.00000000000000000000, \
     -0.38489228042331330437, \
      0.00000000000000000000, \
      0.25711056873844140291, \
      0.00000000000000000000, \
     -0.25711056873844140291, \
      0.00000000000000000000, \
      0.94954208334711565076, \
      0.00000000000000000000, \
     -0.94954208334711565076, \
      0.00000000000000000000, \
      0.09635090648066924057, \
      0.00000000000000000000, \
     -0.09635090648066924057, \
      0.00000000000000000000, \
      0.91044931261818451418, \
      0.00000000000000000000, \
     -0.91044931261818451418, \
      0.00000000000000000000, \
      0.26830824357428106897, \
      0.00000000000000000000, \
     -0.26830824357428106897, \
      0.00000000000000000000, \
      0.82744656686299722370, \
      0.00000000000000000000, \
     -0.82744656686299722370, \
      0.00000000000000000000, \
      0.03789270083108932374, \
      0.00000000000000000000, \
     -0.03789270083108932374, \
      0.00000000000000000000, \
      0.57352052408158127328, \
      0.00000000000000000000, \
     -0.57352052408158127328, \
      0.00000000000000000000, \
      0.74231157227003041754, \
      0.00000000000000000000, \
     -0.74231157227003041754, \
      0.00000000000000000000, \
      0.28469096413200573048, \
      0.00000000000000000000, \
     -0.28469096413200573048, \
      0.00000000000000000000, \
      0.11281627950690893691, \
      0.00000000000000000000, \
     -0.11281627950690893691, \
      0.00000000000000000000, \
      0.45356762399670425001, \
     -0.45356762399670425001, \
      0.45356762399670425001, \
     -0.45356762399670425001, \
      0.33361103852611595499, \
     -0.33361103852611595499, \
      0.33361103852611595499, \
     -0.33361103852611595499, \
      0.37733375278222114346, \
     -0.37733375278222114346, \
      0.37733375278222114346, \
     -0.37733375278222114346, \
      0.30611174916927796907, \
     -0.30611174916927796907, \
      0.30611174916927796907, \
     -0.30611174916927796907, \
      0.29044600765245415230, \
     -0.29044600765245415230, \
      0.29044600765245415230, \
     -0.29044600765245415230, \
      0.59141068840923671779, \
     -0.59141068840923671779, \
      0.59141068840923671779, \
     -0.59141068840923671779, \
      0.76605496491352953470, \
     -0.76605496491352953470, \
      0.76605496491352953470, \
     -0.76605496491352953470, \
      0.44962169263179840861, \
     -0.44962169263179840861, \
      0.44962169263179840861, \
     -0.44962169263179840861, \
      0.61256910754587590162, \
     -0.61256910754587590162, \
      0.61256910754587590162, \
     -0.61256910754587590162, \
      0.96517775637880776074, \
     -0.96517775637880776074, \
      0.96517775637880776074, \
     -0.96517775637880776074, \
      0.18509443085238544424, \
     -0.18509443085238544424, \
      0.18509443085238544424, \
     -0.18509443085238544424, \
      0.13053399140728452754, \
     -0.13053399140728452754, \
      0.13053399140728452754, \
     -0.13053399140728452754, \
      0.08713330755302489683, \
     -0.08713330755302489683, \
      0.08713330755302489683, \
     -0.08713330755302489683, \
      0.11626579551616780805, \
     -0.11626579551616780805, \
      0.11626579551616780805, \
     -0.11626579551616780805, \
      0.03353132384174680597, \
     -0.03353132384174680597, \
      0.03353132384174680597, \
     -0.03353132384174680597, \
      0.63007044649757071308, \
     -0.63007044649757071308, \
      0.63007044649757071308, \
     -0.63007044649757071308, \
      0.10081553511278160129, \
     -0.10081553511278160129, \
      0.10081553511278160129, \
     -0.10081553511278160129, \
      0.09712721271803037570, \
     -0.09712721271803037570, \
      0.09712721271803037570, \
     -0.09712721271803037570, \
      0.65036744612024988133, \
     -0.65036744612024988133, \
      0.65036744612024988133, \
     -0.65036744612024988133, \
      0.78816705553909693904, \
     -0.78816705553909693904, \
      0.78816705553909693904, \
     -0.78816705553909693904, \
      0.46326102535176988395, \
     -0.46326102535176988395, \
      0.46326102535176988395, \
     -0.46326102535176988395, \
      0.87426225625453524160, \
     -0.87426225625453524160, \
      0.87426225625453524160, \
     -0.87426225625453524160, \
      0.09693365579654888986, \
     -0.09693365579654888986, \
      0.09693365579654888986, \
     -0.09693365579654888986, \
      0.52651234369915456135, \
     -0.52651234369915456135, \
      0.52651234369915456135, \
     -0.52651234369915456135, \
      0.21058018350559978837, \
     -0.21058018350559978837, \
      0.21058018350559978837, \
     -0.21058018350559978837, \
      0.48341786018142590686, \
     -0.48341786018142590686, \
      0.48341786018142590686, \
     -0.48341786018142590686, \
      0.27232398053992901144, \
     -0.27232398053992901144, \
      0.27232398053992901144, \
     -0.27232398053992901144, \
      0.88748390701146573356, \
     -0.88748390701146573356, \
      0.88748390701146573356, \
     -0.88748390701146573356, \
      0.34004340177081920915, \
     -0.34004340177081920915, \
      0.34004340177081920915, \
     -0.34004340177081920915, \
      0.24657134521158877161, \
     -0.24657134521158877161, \
      0.24657134521158877161, \
     -0.24657134521158877161, \
      0.72032611852462202773, \
     -0.72032611852462202773, \
      0.72032611852462202773, \
     -0.72032611852462202773, \
      0.86934672471843543740, \
      0.66053776743762293577, \
     -0.86934672471843543740, \
      0.66053776743762293577, \
      0.86934672471843543740, \
     -0.66053776743762293577, \
     -0.86934672471843543740, \
     -0.66053776743762293577, \
      0.51657003644145271792, \
      0.12681144322431647797, \
     -0.51657003644145271792, \
      0.12681144322431647797, \
      0.51657003644145271792, \
     -0.12681144322431647797, \
     -0.51657003644145271792, \
     -0.12681144322431647797, \
      0.21419492835914627493, \
      0.53514205206517340141, \
     -0.21419492835914627493, \
      0.53514205206517340141, \
      0.21419492835914627493, \
     -0.53514205206517340141, \
     -0.21419492835914627493, \
     -0.53514205206517340141, \
      0.38606155250360069120, \
      0.14309874624364349316, \
     -0.38606155250360069120, \
      0.14309874624364349316, \
      0.38606155250360069120, \
     -0.14309874624364349316, \
     -0.38606155250360069120, \
     -0.14309874624364349316, \
      0.31482652231165053625, \
      0.57887349054423364869, \
     -0.31482652231165053625, \
      0.57887349054423364869, \
      0.31482652231165053625, \
     -0.57887349054423364869, \
     -0.31482652231165053625, \
     -0.57887349054423364869, \
      0.13337762200744199270, \
      0.86857348087766383937, \
     -0.13337762200744199270, \
      0.86857348087766383937, \
      0.13337762200744199270, \
     -0.86857348087766383937, \
     -0.13337762200744199270, \
     -0.86857348087766383937, \
      0.89334514265657827270, \
      0.29700939611864535239, \
     -0.89334514265657827270, \
      0.29700939611864535239, \
      0.89334514265657827270, \
     -0.29700939611864535239, \
     -0.89334514265657827270, \
     -0.29700939611864535239, \
      0.64207321281802853807, \
      0.21859043909362887992, \
     -0.64207321281802853807, \
      0.21859043909362887992, \
      0.64207321281802853807, \
     -0.21859043909362887992, \
     -0.64207321281802853807, \
     -0.21859043909362887992, \
      0.90155669259026749440, \
      0.28504501057958070431, \
     -0.90155669259026749440, \
      0.28504501057958070431, \
      0.90155669259026749440, \
     -0.28504501057958070431, \
     -0.90155669259026749440, \
     -0.28504501057958070431, \
      0.17950781738619853156, \
      0.67966060973500286302, \
     -0.17950781738619853156, \
      0.67966060973500286302, \
      0.17950781738619853156, \
     -0.67966060973500286302, \
     -0.17950781738619853156, \
     -0.67966060973500286302, \
      0.52877164545115751260, \
      0.37525379145011561466, \
     -0.52877164545115751260, \
      0.37525379145011561466, \
      0.52877164545115751260, \
     -0.37525379145011561466, \
     -0.52877164545115751260, \
     -0.37525379145011561466, \
      0.85684776838109344421, \
      0.70614261226539476457, \
     -0.85684776838109344421, \
      0.70614261226539476457, \
      0.85684776838109344421, \
     -0.70614261226539476457, \
     -0.85684776838109344421, \
     -0.70614261226539476457, \
      0.23744649710478388238, \
      0.09039264484495425356, \
     -0.23744649710478388238, \
      0.09039264484495425356, \
      0.23744649710478388238, \
     -0.09039264484495425356, \
     -0.23744649710478388238, \
     -0.09039264484495425356, \
      0.94065987701065645332, \
      0.74375119609914763785, \
     -0.94065987701065645332, \
      0.74375119609914763785, \
      0.94065987701065645332, \
     -0.74375119609914763785, \
     -0.94065987701065645332, \
     -0.74375119609914763785, \
      0.96544985579484265958, \
      0.55816486672448317741, \
     -0.96544985579484265958, \
      0.55816486672448317741, \
      0.96544985579484265958, \
     -0.55816486672448317741, \
     -0.96544985579484265958, \
     -0.55816486672448317741, \
      0.11859977159394578805, \
      0.19730553454891092136, \
     -0.11859977159394578805, \
      0.19730553454891092136, \
      0.11859977159394578805, \
     -0.19730553454891092136, \
     -0.11859977159394578805, \
     -0.19730553454891092136, \
      0.43836828746731176798, \
      0.68010534456895455069, \
     -0.43836828746731176798, \
      0.68010534456895455069, \
      0.43836828746731176798, \
     -0.68010534456895455069, \
     -0.43836828746731176798, \
     -0.68010534456895455069, \
      0.85015015838954666183, \
      0.57767859879985306026, \
     -0.85015015838954666183, \
      0.57767859879985306026, \
      0.85015015838954666183, \
     -0.57767859879985306026, \
     -0.85015015838954666183, \
     -0.57767859879985306026, \
      0.40977883537749759668, \
      0.59926491678603310831, \
     -0.40977883537749759668, \
      0.59926491678603310831, \
      0.40977883537749759668, \
     -0.59926491678603310831, \
     -0.40977883537749759668, \
     -0.59926491678603310831, \
      0.62540250575452105419, \
      0.77938113963987465382, \
     -0.62540250575452105419, \
      0.77938113963987465382, \
      0.62540250575452105419, \
     -0.77938113963987465382, \
     -0.62540250575452105419, \
     -0.77938113963987465382, \
      0.16587947711557049502, \
      0.65137881658599783297, \
     -0.16587947711557049502, \
      0.65137881658599783297, \
      0.16587947711557049502, \
     -0.65137881658599783297, \
     -0.16587947711557049502, \
     -0.65137881658599783297, \
      0.50625591443667894431, \
      0.24708268775667227568, \
     -0.50625591443667894431, \
      0.24708268775667227568, \
      0.50625591443667894431, \
     -0.24708268775667227568, \
     -0.50625591443667894431, \
     -0.24708268775667227568, \
      0.74292936328073289065, \
      0.16823593457058672040, \
     -0.74292936328073289065, \
      0.16823593457058672040, \
      0.74292936328073289065, \
     -0.16823593457058672040, \
     -0.74292936328073289065, \
     -0.16823593457058672040, \
      0.01867609649526593210, \
      0.25362045997818172260, \
     -0.01867609649526593210, \
      0.25362045997818172260, \
      0.01867609649526593210, \
     -0.25362045997818172260, \
     -0.01867609649526593210, \
     -0.25362045997818172260, \
      0.26086005279281720970, \
      0.40946055588941798753, \
     -0.26086005279281720970, \
      0.40946055588941798753, \
      0.26086005279281720970, \
     -0.40946055588941798753, \
     -0.26086005279281720970, \
     -0.40946055588941798753, \
      0.79388083129835063101, \
      0.46918818998244915530, \
     -0.79388083129835063101, \
      0.46918818998244915530, \
      0.79388083129835063101, \
     -0.46918818998244915530, \
     -0.79388083129835063101, \
     -0.46918818998244915530, \
      0.79301165544060303603, \
      0.29864577765030031475, \
     -0.79301165544060303603, \
      0.29864577765030031475, \
      0.79301165544060303603, \
     -0.29864577765030031475, \
     -0.79301165544060303603, \
     -0.29864577765030031475, \
      0.44929996069833155747, \
      0.16967965727402492537, \
     -0.44929996069833155747, \
      0.16967965727402492537, \
      0.44929996069833155747, \
     -0.16967965727402492537, \
     -0.44929996069833155747, \
     -0.16967965727402492537, \
      0.76873831458793862037, \
      0.39677450550481596636, \
     -0.76873831458793862037, \
      0.39677450550481596636, \
      0.76873831458793862037, \
     -0.39677450550481596636, \
     -0.76873831458793862037, \
     -0.39677450550481596636, \
      0.97859975977571478367, \
      0.19094705775922465874, \
     -0.97859975977571478367, \
      0.19094705775922465874, \
      0.97859975977571478367, \
     -0.19094705775922465874, \
     -0.97859975977571478367, \
     -0.19094705775922465874, \
      0.21358909276843840441, \
      0.36041615296155676829, \
     -0.21358909276843840441, \
      0.36041615296155676829, \
      0.21358909276843840441, \
     -0.36041615296155676829, \
     -0.21358909276843840441, \
     -0.36041615296155676829, \
      0.79625257738750132575, \
      0.15628526976368214974, \
     -0.79625257738750132575, \
      0.15628526976368214974, \
      0.79625257738750132575, \
     -0.15628526976368214974, \
     -0.79625257738750132575, \
     -0.15628526976368214974, \
      0.91939856562697519493, \
      0.41486074510619452838, \
     -0.91939856562697519493, \
      0.41486074510619452838, \
      0.91939856562697519493, \
     -0.41486074510619452838, \
     -0.91939856562697519493, \
     -0.41486074510619452838, \
      0.51507330251609151350, \
      0.68962930070823635909, \
     -0.51507330251609151350, \
      0.68962930070823635909, \
      0.51507330251609151350, \
     -0.68962930070823635909, \
     -0.51507330251609151350, \
     -0.68962930070823635909, \
      0.96361213891168562284, \
      0.85957679427925348659, \
     -0.96361213891168562284, \
      0.85957679427925348659, \
      0.96361213891168562284, \
     -0.85957679427925348659, \
     -0.96361213891168562284, \
     -0.85957679427925348659, \
      0.72140711490936071382, \
      0.49209543700208141503, \
     -0.72140711490936071382, \
      0.49209543700208141503, \
      0.72140711490936071382, \
     -0.49209543700208141503, \
     -0.72140711490936071382, \
     -0.49209543700208141503 ] )

  y = np.array ( [ \
      0.00000000000000000000, \
      0.00000000000000000000, \
      0.48169354344312520499, \
      0.00000000000000000000, \
     -0.48169354344312520499, \
      0.00000000000000000000, \
      0.69858038869870031640, \
      0.00000000000000000000, \
     -0.69858038869870031640, \
      0.00000000000000000000, \
      0.53468657951770970360, \
      0.00000000000000000000, \
     -0.53468657951770970360, \
      0.00000000000000000000, \
      0.42228380878442672852, \
      0.00000000000000000000, \
     -0.42228380878442672852, \
      0.00000000000000000000, \
      0.30680451888779119995, \
      0.00000000000000000000, \
     -0.30680451888779119995, \
      0.00000000000000000000, \
      0.22877498497689821577, \
      0.00000000000000000000, \
     -0.22877498497689821577, \
      0.00000000000000000000, \
      0.55389687412807175892, \
      0.00000000000000000000, \
     -0.55389687412807175892, \
      0.00000000000000000000, \
      0.38489228042331330437, \
      0.00000000000000000000, \
     -0.38489228042331330437, \
      0.00000000000000000000, \
      0.25711056873844140291, \
      0.00000000000000000000, \
     -0.25711056873844140291, \
      0.00000000000000000000, \
      0.94954208334711565076, \
      0.00000000000000000000, \
     -0.94954208334711565076, \
      0.00000000000000000000, \
      0.09635090648066924057, \
      0.00000000000000000000, \
     -0.09635090648066924057, \
      0.00000000000000000000, \
      0.91044931261818451418, \
      0.00000000000000000000, \
     -0.91044931261818451418, \
      0.00000000000000000000, \
      0.26830824357428106897, \
      0.00000000000000000000, \
     -0.26830824357428106897, \
      0.00000000000000000000, \
      0.82744656686299722370, \
      0.00000000000000000000, \
     -0.82744656686299722370, \
      0.00000000000000000000, \
      0.03789270083108932374, \
      0.00000000000000000000, \
     -0.03789270083108932374, \
      0.00000000000000000000, \
      0.57352052408158127328, \
      0.00000000000000000000, \
     -0.57352052408158127328, \
      0.00000000000000000000, \
      0.74231157227003041754, \
      0.00000000000000000000, \
     -0.74231157227003041754, \
      0.00000000000000000000, \
      0.28469096413200573048, \
      0.00000000000000000000, \
     -0.28469096413200573048, \
      0.00000000000000000000, \
      0.11281627950690893691, \
      0.00000000000000000000, \
     -0.11281627950690893691, \
      0.45356762399670425001, \
      0.45356762399670425001, \
     -0.45356762399670425001, \
     -0.45356762399670425001, \
      0.33361103852611595499, \
      0.33361103852611595499, \
     -0.33361103852611595499, \
     -0.33361103852611595499, \
      0.37733375278222114346, \
      0.37733375278222114346, \
     -0.37733375278222114346, \
     -0.37733375278222114346, \
      0.30611174916927796907, \
      0.30611174916927796907, \
     -0.30611174916927796907, \
     -0.30611174916927796907, \
      0.29044600765245415230, \
      0.29044600765245415230, \
     -0.29044600765245415230, \
     -0.29044600765245415230, \
      0.59141068840923671779, \
      0.59141068840923671779, \
     -0.59141068840923671779, \
     -0.59141068840923671779, \
      0.76605496491352953470, \
      0.76605496491352953470, \
     -0.76605496491352953470, \
     -0.76605496491352953470, \
      0.44962169263179840861, \
      0.44962169263179840861, \
     -0.44962169263179840861, \
     -0.44962169263179840861, \
      0.61256910754587590162, \
      0.61256910754587590162, \
     -0.61256910754587590162, \
     -0.61256910754587590162, \
      0.96517775637880776074, \
      0.96517775637880776074, \
     -0.96517775637880776074, \
     -0.96517775637880776074, \
      0.18509443085238544424, \
      0.18509443085238544424, \
     -0.18509443085238544424, \
     -0.18509443085238544424, \
      0.13053399140728452754, \
      0.13053399140728452754, \
     -0.13053399140728452754, \
     -0.13053399140728452754, \
      0.08713330755302489683, \
      0.08713330755302489683, \
     -0.08713330755302489683, \
     -0.08713330755302489683, \
      0.11626579551616780805, \
      0.11626579551616780805, \
     -0.11626579551616780805, \
     -0.11626579551616780805, \
      0.03353132384174680597, \
      0.03353132384174680597, \
     -0.03353132384174680597, \
     -0.03353132384174680597, \
      0.63007044649757071308, \
      0.63007044649757071308, \
     -0.63007044649757071308, \
     -0.63007044649757071308, \
      0.10081553511278160129, \
      0.10081553511278160129, \
     -0.10081553511278160129, \
     -0.10081553511278160129, \
      0.09712721271803037570, \
      0.09712721271803037570, \
     -0.09712721271803037570, \
     -0.09712721271803037570, \
      0.65036744612024988133, \
      0.65036744612024988133, \
     -0.65036744612024988133, \
     -0.65036744612024988133, \
      0.78816705553909693904, \
      0.78816705553909693904, \
     -0.78816705553909693904, \
     -0.78816705553909693904, \
      0.46326102535176988395, \
      0.46326102535176988395, \
     -0.46326102535176988395, \
     -0.46326102535176988395, \
      0.87426225625453524160, \
      0.87426225625453524160, \
     -0.87426225625453524160, \
     -0.87426225625453524160, \
      0.09693365579654888986, \
      0.09693365579654888986, \
     -0.09693365579654888986, \
     -0.09693365579654888986, \
      0.52651234369915456135, \
      0.52651234369915456135, \
     -0.52651234369915456135, \
     -0.52651234369915456135, \
      0.21058018350559978837, \
      0.21058018350559978837, \
     -0.21058018350559978837, \
     -0.21058018350559978837, \
      0.48341786018142590686, \
      0.48341786018142590686, \
     -0.48341786018142590686, \
     -0.48341786018142590686, \
      0.27232398053992901144, \
      0.27232398053992901144, \
     -0.27232398053992901144, \
     -0.27232398053992901144, \
      0.88748390701146573356, \
      0.88748390701146573356, \
     -0.88748390701146573356, \
     -0.88748390701146573356, \
      0.34004340177081920915, \
      0.34004340177081920915, \
     -0.34004340177081920915, \
     -0.34004340177081920915, \
      0.24657134521158877161, \
      0.24657134521158877161, \
     -0.24657134521158877161, \
     -0.24657134521158877161, \
      0.72032611852462202773, \
      0.72032611852462202773, \
     -0.72032611852462202773, \
     -0.72032611852462202773, \
      0.66053776743762293577, \
      0.86934672471843543740, \
      0.66053776743762293577, \
     -0.86934672471843543740, \
     -0.66053776743762293577, \
      0.86934672471843543740, \
     -0.66053776743762293577, \
     -0.86934672471843543740, \
      0.12681144322431647797, \
      0.51657003644145271792, \
      0.12681144322431647797, \
     -0.51657003644145271792, \
     -0.12681144322431647797, \
      0.51657003644145271792, \
     -0.12681144322431647797, \
     -0.51657003644145271792, \
      0.53514205206517340141, \
      0.21419492835914627493, \
      0.53514205206517340141, \
     -0.21419492835914627493, \
     -0.53514205206517340141, \
      0.21419492835914627493, \
     -0.53514205206517340141, \
     -0.21419492835914627493, \
      0.14309874624364349316, \
      0.38606155250360069120, \
      0.14309874624364349316, \
     -0.38606155250360069120, \
     -0.14309874624364349316, \
      0.38606155250360069120, \
     -0.14309874624364349316, \
     -0.38606155250360069120, \
      0.57887349054423364869, \
      0.31482652231165053625, \
      0.57887349054423364869, \
     -0.31482652231165053625, \
     -0.57887349054423364869, \
      0.31482652231165053625, \
     -0.57887349054423364869, \
     -0.31482652231165053625, \
      0.86857348087766383937, \
      0.13337762200744199270, \
      0.86857348087766383937, \
     -0.13337762200744199270, \
     -0.86857348087766383937, \
      0.13337762200744199270, \
     -0.86857348087766383937, \
     -0.13337762200744199270, \
      0.29700939611864535239, \
      0.89334514265657827270, \
      0.29700939611864535239, \
     -0.89334514265657827270, \
     -0.29700939611864535239, \
      0.89334514265657827270, \
     -0.29700939611864535239, \
     -0.89334514265657827270, \
      0.21859043909362887992, \
      0.64207321281802853807, \
      0.21859043909362887992, \
     -0.64207321281802853807, \
     -0.21859043909362887992, \
      0.64207321281802853807, \
     -0.21859043909362887992, \
     -0.64207321281802853807, \
      0.28504501057958070431, \
      0.90155669259026749440, \
      0.28504501057958070431, \
     -0.90155669259026749440, \
     -0.28504501057958070431, \
      0.90155669259026749440, \
     -0.28504501057958070431, \
     -0.90155669259026749440, \
      0.67966060973500286302, \
      0.17950781738619853156, \
      0.67966060973500286302, \
     -0.17950781738619853156, \
     -0.67966060973500286302, \
      0.17950781738619853156, \
     -0.67966060973500286302, \
     -0.17950781738619853156, \
      0.37525379145011561466, \
      0.52877164545115751260, \
      0.37525379145011561466, \
     -0.52877164545115751260, \
     -0.37525379145011561466, \
      0.52877164545115751260, \
     -0.37525379145011561466, \
     -0.52877164545115751260, \
      0.70614261226539476457, \
      0.85684776838109344421, \
      0.70614261226539476457, \
     -0.85684776838109344421, \
     -0.70614261226539476457, \
      0.85684776838109344421, \
     -0.70614261226539476457, \
     -0.85684776838109344421, \
      0.09039264484495425356, \
      0.23744649710478388238, \
      0.09039264484495425356, \
     -0.23744649710478388238, \
     -0.09039264484495425356, \
      0.23744649710478388238, \
     -0.09039264484495425356, \
     -0.23744649710478388238, \
      0.74375119609914763785, \
      0.94065987701065645332, \
      0.74375119609914763785, \
     -0.94065987701065645332, \
     -0.74375119609914763785, \
      0.94065987701065645332, \
     -0.74375119609914763785, \
     -0.94065987701065645332, \
      0.55816486672448317741, \
      0.96544985579484265958, \
      0.55816486672448317741, \
     -0.96544985579484265958, \
     -0.55816486672448317741, \
      0.96544985579484265958, \
     -0.55816486672448317741, \
     -0.96544985579484265958, \
      0.19730553454891092136, \
      0.11859977159394578805, \
      0.19730553454891092136, \
     -0.11859977159394578805, \
     -0.19730553454891092136, \
      0.11859977159394578805, \
     -0.19730553454891092136, \
     -0.11859977159394578805, \
      0.68010534456895455069, \
      0.43836828746731176798, \
      0.68010534456895455069, \
     -0.43836828746731176798, \
     -0.68010534456895455069, \
      0.43836828746731176798, \
     -0.68010534456895455069, \
     -0.43836828746731176798, \
      0.57767859879985306026, \
      0.85015015838954666183, \
      0.57767859879985306026, \
     -0.85015015838954666183, \
     -0.57767859879985306026, \
      0.85015015838954666183, \
     -0.57767859879985306026, \
     -0.85015015838954666183, \
      0.59926491678603310831, \
      0.40977883537749759668, \
      0.59926491678603310831, \
     -0.40977883537749759668, \
     -0.59926491678603310831, \
      0.40977883537749759668, \
     -0.59926491678603310831, \
     -0.40977883537749759668, \
      0.77938113963987465382, \
      0.62540250575452105419, \
      0.77938113963987465382, \
     -0.62540250575452105419, \
     -0.77938113963987465382, \
      0.62540250575452105419, \
     -0.77938113963987465382, \
     -0.62540250575452105419, \
      0.65137881658599783297, \
      0.16587947711557049502, \
      0.65137881658599783297, \
     -0.16587947711557049502, \
     -0.65137881658599783297, \
      0.16587947711557049502, \
     -0.65137881658599783297, \
     -0.16587947711557049502, \
      0.24708268775667227568, \
      0.50625591443667894431, \
      0.24708268775667227568, \
     -0.50625591443667894431, \
     -0.24708268775667227568, \
      0.50625591443667894431, \
     -0.24708268775667227568, \
     -0.50625591443667894431, \
      0.16823593457058672040, \
      0.74292936328073289065, \
      0.16823593457058672040, \
     -0.74292936328073289065, \
     -0.16823593457058672040, \
      0.74292936328073289065, \
     -0.16823593457058672040, \
     -0.74292936328073289065, \
      0.25362045997818172260, \
      0.01867609649526593210, \
      0.25362045997818172260, \
     -0.01867609649526593210, \
     -0.25362045997818172260, \
      0.01867609649526593210, \
     -0.25362045997818172260, \
     -0.01867609649526593210, \
      0.40946055588941798753, \
      0.26086005279281720970, \
      0.40946055588941798753, \
     -0.26086005279281720970, \
     -0.40946055588941798753, \
      0.26086005279281720970, \
     -0.40946055588941798753, \
     -0.26086005279281720970, \
      0.46918818998244915530, \
      0.79388083129835063101, \
      0.46918818998244915530, \
     -0.79388083129835063101, \
     -0.46918818998244915530, \
      0.79388083129835063101, \
     -0.46918818998244915530, \
     -0.79388083129835063101, \
      0.29864577765030031475, \
      0.79301165544060303603, \
      0.29864577765030031475, \
     -0.79301165544060303603, \
     -0.29864577765030031475, \
      0.79301165544060303603, \
     -0.29864577765030031475, \
     -0.79301165544060303603, \
      0.16967965727402492537, \
      0.44929996069833155747, \
      0.16967965727402492537, \
     -0.44929996069833155747, \
     -0.16967965727402492537, \
      0.44929996069833155747, \
     -0.16967965727402492537, \
     -0.44929996069833155747, \
      0.39677450550481596636, \
      0.76873831458793862037, \
      0.39677450550481596636, \
     -0.76873831458793862037, \
     -0.39677450550481596636, \
      0.76873831458793862037, \
     -0.39677450550481596636, \
     -0.76873831458793862037, \
      0.19094705775922465874, \
      0.97859975977571478367, \
      0.19094705775922465874, \
     -0.97859975977571478367, \
     -0.19094705775922465874, \
      0.97859975977571478367, \
     -0.19094705775922465874, \
     -0.97859975977571478367, \
      0.36041615296155676829, \
      0.21358909276843840441, \
      0.36041615296155676829, \
     -0.21358909276843840441, \
     -0.36041615296155676829, \
      0.21358909276843840441, \
     -0.36041615296155676829, \
     -0.21358909276843840441, \
      0.15628526976368214974, \
      0.79625257738750132575, \
      0.15628526976368214974, \
     -0.79625257738750132575, \
     -0.15628526976368214974, \
      0.79625257738750132575, \
     -0.15628526976368214974, \
     -0.79625257738750132575, \
      0.41486074510619452838, \
      0.91939856562697519493, \
      0.41486074510619452838, \
     -0.91939856562697519493, \
     -0.41486074510619452838, \
      0.91939856562697519493, \
     -0.41486074510619452838, \
     -0.91939856562697519493, \
      0.68962930070823635909, \
      0.51507330251609151350, \
      0.68962930070823635909, \
     -0.51507330251609151350, \
     -0.68962930070823635909, \
      0.51507330251609151350, \
     -0.68962930070823635909, \
     -0.51507330251609151350, \
      0.85957679427925348659, \
      0.96361213891168562284, \
      0.85957679427925348659, \
     -0.96361213891168562284, \
     -0.85957679427925348659, \
      0.96361213891168562284, \
     -0.85957679427925348659, \
     -0.96361213891168562284, \
      0.49209543700208141503, \
      0.72140711490936071382, \
      0.49209543700208141503, \
     -0.72140711490936071382, \
     -0.49209543700208141503, \
      0.72140711490936071382, \
     -0.49209543700208141503, \
     -0.72140711490936071382 ] )

  z = np.array ( [ \
      0.60412613281560589851, \
      0.12832541213701875726, \
      0.12832541213701875726, \
      0.12832541213701875726, \
      0.12832541213701875726, \
      0.23636452793876766565, \
      0.23636452793876766565, \
      0.23636452793876766565, \
      0.23636452793876766565, \
      0.36948143968736257836, \
      0.36948143968736257836, \
      0.36948143968736257836, \
      0.36948143968736257836, \
      0.57413522292238361455, \
      0.57413522292238361455, \
      0.57413522292238361455, \
      0.57413522292238361455, \
      0.57097027691958568418, \
      0.57097027691958568418, \
      0.57097027691958568418, \
      0.57097027691958568418, \
      0.44532726334384131750, \
      0.44532726334384131750, \
      0.44532726334384131750, \
      0.44532726334384131750, \
      0.18507199264697138386, \
      0.18507199264697138386, \
      0.18507199264697138386, \
      0.18507199264697138386, \
      0.28281898722495468768, \
      0.28281898722495468768, \
      0.28281898722495468768, \
      0.28281898722495468768, \
      0.00745381355051214466, \
      0.00745381355051214466, \
      0.00745381355051214466, \
      0.00745381355051214466, \
      0.00273060888853154026, \
      0.00273060888853154026, \
      0.00273060888853154026, \
      0.00273060888853154026, \
      0.89474683073191085825, \
      0.89474683073191085825, \
      0.89474683073191085825, \
      0.89474683073191085825, \
      0.05489260378459437373, \
      0.05489260378459437373, \
      0.05489260378459437373, \
      0.05489260378459437373, \
      0.17890547617113325418, \
      0.17890547617113325418, \
      0.17890547617113325418, \
      0.17890547617113325418, \
      0.14438727929533640149, \
      0.14438727929533640149, \
      0.14438727929533640149, \
      0.14438727929533640149, \
      0.96005329029751285130, \
      0.96005329029751285130, \
      0.96005329029751285130, \
      0.96005329029751285130, \
      0.42262373956574911249, \
      0.42262373956574911249, \
      0.42262373956574911249, \
      0.42262373956574911249, \
      0.00937341178432237430, \
      0.00937341178432237430, \
      0.00937341178432237430, \
      0.00937341178432237430, \
      0.70511644808626805503, \
      0.70511644808626805503, \
      0.70511644808626805503, \
      0.70511644808626805503, \
      0.80976037637526798729, \
      0.80976037637526798729, \
      0.80976037637526798729, \
      0.80976037637526798729, \
      0.52107002257796464217, \
      0.52107002257796464217, \
      0.52107002257796464217, \
      0.52107002257796464217, \
      0.47622191262040014514, \
      0.47622191262040014514, \
      0.47622191262040014514, \
      0.47622191262040014514, \
      0.04553198949867700435, \
      0.04553198949867700435, \
      0.04553198949867700435, \
      0.04553198949867700435, \
      0.68236516778452971366, \
      0.68236516778452971366, \
      0.68236516778452971366, \
      0.68236516778452971366, \
      0.36766518307523687881, \
      0.36766518307523687881, \
      0.36766518307523687881, \
      0.36766518307523687881, \
      0.03140155892114703667, \
      0.03140155892114703667, \
      0.03140155892114703667, \
      0.03140155892114703667, \
      0.20854763179877680579, \
      0.20854763179877680579, \
      0.20854763179877680579, \
      0.20854763179877680579, \
      0.32095943995186076991, \
      0.32095943995186076991, \
      0.32095943995186076991, \
      0.32095943995186076991, \
      0.35590541054356356065, \
      0.35590541054356356065, \
      0.35590541054356356065, \
      0.35590541054356356065, \
      0.01963481046583391565, \
      0.01963481046583391565, \
      0.01963481046583391565, \
      0.01963481046583391565, \
      0.58110848325376152079, \
      0.58110848325376152079, \
      0.58110848325376152079, \
      0.58110848325376152079, \
      0.22030183551151610866, \
      0.22030183551151610866, \
      0.22030183551151610866, \
      0.22030183551151610866, \
      0.70743374610149956094, \
      0.70743374610149956094, \
      0.70743374610149956094, \
      0.70743374610149956094, \
      0.49754618392934674143, \
      0.49754618392934674143, \
      0.49754618392934674143, \
      0.49754618392934674143, \
      0.90197994879909670907, \
      0.90197994879909670907, \
      0.90197994879909670907, \
      0.90197994879909670907, \
      0.15830174812382535876, \
      0.15830174812382535876, \
      0.15830174812382535876, \
      0.15830174812382535876, \
      0.34703489296133355202, \
      0.34703489296133355202, \
      0.34703489296133355202, \
      0.34703489296133355202, \
      0.87727590777505048969, \
      0.87727590777505048969, \
      0.87727590777505048969, \
      0.87727590777505048969, \
      0.25098088788741812483, \
      0.25098088788741812483, \
      0.25098088788741812483, \
      0.25098088788741812483, \
      0.12287487061124809096, \
      0.12287487061124809096, \
      0.12287487061124809096, \
      0.12287487061124809096, \
      0.21569557215246823456, \
      0.21569557215246823456, \
      0.21569557215246823456, \
      0.21569557215246823456, \
      0.04316688220319717106, \
      0.04316688220319717106, \
      0.04316688220319717106, \
      0.04316688220319717106, \
      0.10724275430905566564, \
      0.10724275430905566564, \
      0.10724275430905566564, \
      0.10724275430905566564, \
      0.32964277824701476716, \
      0.32964277824701476716, \
      0.32964277824701476716, \
      0.32964277824701476716, \
      0.71600680775916891729, \
      0.71600680775916891729, \
      0.71600680775916891729, \
      0.71600680775916891729, \
      0.41973631072686923282, \
      0.41973631072686923282, \
      0.41973631072686923282, \
      0.41973631072686923282, \
      0.10771970940234577852, \
      0.10771970940234577852, \
      0.10771970940234577852, \
      0.10771970940234577852, \
      0.09137076099343852120, \
      0.09137076099343852120, \
      0.09137076099343852120, \
      0.09137076099343852120, \
      0.57433224555240058873, \
      0.57433224555240058873, \
      0.57433224555240058873, \
      0.57433224555240058873, \
      0.29652789568067272619, \
      0.29652789568067272619, \
      0.29652789568067272619, \
      0.29652789568067272619, \
      0.06861567128774997970, \
      0.06861567128774997970, \
      0.06861567128774997970, \
      0.06861567128774997970, \
      0.12112687504129497629, \
      0.12112687504129497629, \
      0.12112687504129497629, \
      0.12112687504129497629, \
      0.12112687504129497629, \
      0.12112687504129497629, \
      0.12112687504129497629, \
      0.12112687504129497629, \
      0.06232922095164156878, \
      0.06232922095164156878, \
      0.06232922095164156878, \
      0.06232922095164156878, \
      0.06232922095164156878, \
      0.06232922095164156878, \
      0.06232922095164156878, \
      0.06232922095164156878, \
      0.28878375602826145130, \
      0.28878375602826145130, \
      0.28878375602826145130, \
      0.28878375602826145130, \
      0.28878375602826145130, \
      0.28878375602826145130, \
      0.28878375602826145130, \
      0.28878375602826145130, \
      0.41981996327982368244, \
      0.41981996327982368244, \
      0.41981996327982368244, \
      0.41981996327982368244, \
      0.41981996327982368244, \
      0.41981996327982368244, \
      0.41981996327982368244, \
      0.41981996327982368244, \
      0.36719716335126328932, \
      0.36719716335126328932, \
      0.36719716335126328932, \
      0.36719716335126328932, \
      0.36719716335126328932, \
      0.36719716335126328932, \
      0.36719716335126328932, \
      0.36719716335126328932, \
      0.03539982573087990109, \
      0.03539982573087990109, \
      0.03539982573087990109, \
      0.03539982573087990109, \
      0.03539982573087990109, \
      0.03539982573087990109, \
      0.03539982573087990109, \
      0.03539982573087990109, \
      0.00689409549706292753, \
      0.00689409549706292753, \
      0.00689409549706292753, \
      0.00689409549706292753, \
      0.00689409549706292753, \
      0.00689409549706292753, \
      0.00689409549706292753, \
      0.00689409549706292753, \
      0.18034097822548403323, \
      0.18034097822548403323, \
      0.18034097822548403323, \
      0.18034097822548403323, \
      0.18034097822548403323, \
      0.18034097822548403323, \
      0.18034097822548403323, \
      0.18034097822548403323, \
      0.08701177937660883877, \
      0.08701177937660883877, \
      0.08701177937660883877, \
      0.08701177937660883877, \
      0.08701177937660883877, \
      0.08701177937660883877, \
      0.08701177937660883877, \
      0.08701177937660883877, \
      0.30184034189885056154, \
      0.30184034189885056154, \
      0.30184034189885056154, \
      0.30184034189885056154, \
      0.30184034189885056154, \
      0.30184034189885056154, \
      0.30184034189885056154, \
      0.30184034189885056154, \
      0.46375316476153072287, \
      0.46375316476153072287, \
      0.46375316476153072287, \
      0.46375316476153072287, \
      0.46375316476153072287, \
      0.46375316476153072287, \
      0.46375316476153072287, \
      0.46375316476153072287, \
      0.01259447070049873885, \
      0.01259447070049873885, \
      0.01259447070049873885, \
      0.01259447070049873885, \
      0.01259447070049873885, \
      0.01259447070049873885, \
      0.01259447070049873885, \
      0.01259447070049873885, \
      0.68464554842762070930, \
      0.68464554842762070930, \
      0.68464554842762070930, \
      0.68464554842762070930, \
      0.68464554842762070930, \
      0.68464554842762070930, \
      0.68464554842762070930, \
      0.68464554842762070930, \
      0.04669618994654996941, \
      0.04669618994654996941, \
      0.04669618994654996941, \
      0.04669618994654996941, \
      0.04669618994654996941, \
      0.04669618994654996941, \
      0.04669618994654996941, \
      0.04669618994654996941, \
      0.00997909979720432855, \
      0.00997909979720432855, \
      0.00997909979720432855, \
      0.00997909979720432855, \
      0.00997909979720432855, \
      0.00997909979720432855, \
      0.00997909979720432855, \
      0.00997909979720432855, \
      0.79170760938063011736, \
      0.79170760938063011736, \
      0.79170760938063011736, \
      0.79170760938063011736, \
      0.79170760938063011736, \
      0.79170760938063011736, \
      0.79170760938063011736, \
      0.79170760938063011736, \
      0.23239746807120234551, \
      0.23239746807120234551, \
      0.23239746807120234551, \
      0.23239746807120234551, \
      0.23239746807120234551, \
      0.23239746807120234551, \
      0.23239746807120234551, \
      0.23239746807120234551, \
      0.06212941698545271230, \
      0.06212941698545271230, \
      0.06212941698545271230, \
      0.06212941698545271230, \
      0.06212941698545271230, \
      0.06212941698545271230, \
      0.06212941698545271230, \
      0.06212941698545271230, \
      0.10250007471008426574, \
      0.10250007471008426574, \
      0.10250007471008426574, \
      0.10250007471008426574, \
      0.10250007471008426574, \
      0.10250007471008426574, \
      0.10250007471008426574, \
      0.10250007471008426574, \
      0.19638105364011448906, \
      0.19638105364011448906, \
      0.19638105364011448906, \
      0.19638105364011448906, \
      0.19638105364011448906, \
      0.19638105364011448906, \
      0.19638105364011448906, \
      0.19638105364011448906, \
      0.03807225396126873163, \
      0.03807225396126873163, \
      0.03807225396126873163, \
      0.03807225396126873163, \
      0.03807225396126873163, \
      0.03807225396126873163, \
      0.03807225396126873163, \
      0.03807225396126873163, \
      0.00969993829969578725, \
      0.00969993829969578725, \
      0.00969993829969578725, \
      0.00969993829969578725, \
      0.00969993829969578725, \
      0.00969993829969578725, \
      0.00969993829969578725, \
      0.00969993829969578725, \
      0.08712730173221996943, \
      0.08712730173221996943, \
      0.08712730173221996943, \
      0.08712730173221996943, \
      0.08712730173221996943, \
      0.08712730173221996943, \
      0.08712730173221996943, \
      0.08712730173221996943, \
      0.04169093747605617795, \
      0.04169093747605617795, \
      0.04169093747605617795, \
      0.04169093747605617795, \
      0.04169093747605617795, \
      0.04169093747605617795, \
      0.04169093747605617795, \
      0.04169093747605617795, \
      0.18982222362689099571, \
      0.18982222362689099571, \
      0.18982222362689099571, \
      0.18982222362689099571, \
      0.18982222362689099571, \
      0.18982222362689099571, \
      0.18982222362689099571, \
      0.18982222362689099571, \
      0.12762173979455287975, \
      0.12762173979455287975, \
      0.12762173979455287975, \
      0.12762173979455287975, \
      0.12762173979455287975, \
      0.12762173979455287975, \
      0.12762173979455287975, \
      0.12762173979455287975, \
      0.19550632719707150553, \
      0.19550632719707150553, \
      0.19550632719707150553, \
      0.19550632719707150553, \
      0.19550632719707150553, \
      0.19550632719707150553, \
      0.19550632719707150553, \
      0.19550632719707150553, \
      0.49356773754307026181, \
      0.49356773754307026181, \
      0.49356773754307026181, \
      0.49356773754307026181, \
      0.49356773754307026181, \
      0.49356773754307026181, \
      0.49356773754307026181, \
      0.49356773754307026181, \
      0.03472481178210238412, \
      0.03472481178210238412, \
      0.03472481178210238412, \
      0.03472481178210238412, \
      0.03472481178210238412, \
      0.03472481178210238412, \
      0.03472481178210238412, \
      0.03472481178210238412, \
      0.01518094278770998860, \
      0.01518094278770998860, \
      0.01518094278770998860, \
      0.01518094278770998860, \
      0.01518094278770998860, \
      0.01518094278770998860, \
      0.01518094278770998860, \
      0.01518094278770998860, \
      0.61542031522620999073, \
      0.61542031522620999073, \
      0.61542031522620999073, \
      0.61542031522620999073, \
      0.61542031522620999073, \
      0.61542031522620999073, \
      0.61542031522620999073, \
      0.61542031522620999073, \
      0.12575204752531654595, \
      0.12575204752531654595, \
      0.12575204752531654595, \
      0.12575204752531654595, \
      0.12575204752531654595, \
      0.12575204752531654595, \
      0.12575204752531654595, \
      0.12575204752531654595, \
      0.04457888016467764086, \
      0.04457888016467764086, \
      0.04457888016467764086, \
      0.04457888016467764086, \
      0.04457888016467764086, \
      0.04457888016467764086, \
      0.04457888016467764086, \
      0.04457888016467764086, \
      0.30170781950633751567, \
      0.30170781950633751567, \
      0.30170781950633751567, \
      0.30170781950633751567, \
      0.30170781950633751567, \
      0.30170781950633751567, \
      0.30170781950633751567, \
      0.30170781950633751567, \
      0.00577128438055363874, \
      0.00577128438055363874, \
      0.00577128438055363874, \
      0.00577128438055363874, \
      0.00577128438055363874, \
      0.00577128438055363874, \
      0.00577128438055363874, \
      0.00577128438055363874, \
      0.00239530919218184334, \
      0.00239530919218184334, \
      0.00239530919218184334, \
      0.00239530919218184334, \
      0.00239530919218184334, \
      0.00239530919218184334, \
      0.00239530919218184334, \
      0.00239530919218184334 ] )

  w= np.array ( [ \
      0.00537430973147919565, \
      0.00567173429377825552, \
      0.00567173429377825552, \
      0.00567173429377825552, \
      0.00567173429377825552, \
      0.00324886088172405109, \
      0.00324886088172405109, \
      0.00324886088172405109, \
      0.00324886088172405109, \
      0.00345209452668273666, \
      0.00345209452668273666, \
      0.00345209452668273666, \
      0.00345209452668273666, \
      0.00066660334447695205, \
      0.00066660334447695205, \
      0.00066660334447695205, \
      0.00066660334447695205, \
      0.00399579246038160064, \
      0.00399579246038160064, \
      0.00399579246038160064, \
      0.00399579246038160064, \
      0.00499277895953007846, \
      0.00499277895953007846, \
      0.00499277895953007846, \
      0.00499277895953007846, \
      0.00246962297642099688, \
      0.00246962297642099688, \
      0.00246962297642099688, \
      0.00246962297642099688, \
      0.00706615575413061577, \
      0.00706615575413061577, \
      0.00706615575413061577, \
      0.00706615575413061577, \
      0.00191698003537197552, \
      0.00191698003537197552, \
      0.00191698003537197552, \
      0.00191698003537197552, \
      0.00023875415581936437, \
      0.00023875415581936437, \
      0.00023875415581936437, \
      0.00023875415581936437, \
      0.00016802396701300472, \
      0.00016802396701300472, \
      0.00016802396701300472, \
      0.00016802396701300472, \
      0.00099443273732332323, \
      0.00099443273732332323, \
      0.00099443273732332323, \
      0.00099443273732332323, \
      0.00345494167713882722, \
      0.00345494167713882722, \
      0.00345494167713882722, \
      0.00345494167713882722, \
      0.00137778065777168987, \
      0.00137778065777168987, \
      0.00137778065777168987, \
      0.00137778065777168987, \
      0.00006135678341459227, \
      0.00006135678341459227, \
      0.00006135678341459227, \
      0.00006135678341459227, \
      0.00099615960761120759, \
      0.00099615960761120759, \
      0.00099615960761120759, \
      0.00099615960761120759, \
      0.00173468884468413759, \
      0.00173468884468413759, \
      0.00173468884468413759, \
      0.00173468884468413759, \
      0.00064089052901790020, \
      0.00064089052901790020, \
      0.00064089052901790020, \
      0.00064089052901790020, \
      0.00174770174992903656, \
      0.00174770174992903656, \
      0.00174770174992903656, \
      0.00174770174992903656, \
      0.00053561830982834806, \
      0.00053561830982834806, \
      0.00053561830982834806, \
      0.00053561830982834806, \
      0.00374412815566966747, \
      0.00374412815566966747, \
      0.00374412815566966747, \
      0.00374412815566966747, \
      0.00364849854393893731, \
      0.00364849854393893731, \
      0.00364849854393893731, \
      0.00364849854393893731, \
      0.00027221046304926988, \
      0.00027221046304926988, \
      0.00027221046304926988, \
      0.00027221046304926988, \
      0.00403805862793428852, \
      0.00403805862793428852, \
      0.00403805862793428852, \
      0.00403805862793428852, \
      0.00284945501315263380, \
      0.00284945501315263380, \
      0.00284945501315263380, \
      0.00284945501315263380, \
      0.00049463185151189392, \
      0.00049463185151189392, \
      0.00049463185151189392, \
      0.00049463185151189392, \
      0.00343575024351558140, \
      0.00343575024351558140, \
      0.00343575024351558140, \
      0.00343575024351558140, \
      0.00076547936426975662, \
      0.00076547936426975662, \
      0.00076547936426975662, \
      0.00076547936426975662, \
      0.00009270297025443059, \
      0.00009270297025443059, \
      0.00009270297025443059, \
      0.00009270297025443059, \
      0.00444044740059815115, \
      0.00444044740059815115, \
      0.00444044740059815115, \
      0.00444044740059815115, \
      0.00499528418027490092, \
      0.00499528418027490092, \
      0.00499528418027490092, \
      0.00499528418027490092, \
      0.00232760564344115621, \
      0.00232760564344115621, \
      0.00232760564344115621, \
      0.00232760564344115621, \
      0.00305846111057695401, \
      0.00305846111057695401, \
      0.00305846111057695401, \
      0.00305846111057695401, \
      0.00027167033342833963, \
      0.00027167033342833963, \
      0.00027167033342833963, \
      0.00027167033342833963, \
      0.00359204041455288758, \
      0.00359204041455288758, \
      0.00359204041455288758, \
      0.00359204041455288758, \
      0.00450623232462683300, \
      0.00450623232462683300, \
      0.00450623232462683300, \
      0.00450623232462683300, \
      0.00026620595222711166, \
      0.00026620595222711166, \
      0.00026620595222711166, \
      0.00026620595222711166, \
      0.00172242225189580926, \
      0.00172242225189580926, \
      0.00172242225189580926, \
      0.00172242225189580926, \
      0.00152990216308249529, \
      0.00152990216308249529, \
      0.00152990216308249529, \
      0.00152990216308249529, \
      0.00433172345565203346, \
      0.00433172345565203346, \
      0.00433172345565203346, \
      0.00433172345565203346, \
      0.00086984955905943873, \
      0.00086984955905943873, \
      0.00086984955905943873, \
      0.00086984955905943873, \
      0.00316655761594148268, \
      0.00316655761594148268, \
      0.00316655761594148268, \
      0.00316655761594148268, \
      0.00145516775846500309, \
      0.00145516775846500309, \
      0.00145516775846500309, \
      0.00145516775846500309, \
      0.00113761603493167554, \
      0.00113761603493167554, \
      0.00113761603493167554, \
      0.00113761603493167554, \
      0.00188490438846629360, \
      0.00188490438846629360, \
      0.00188490438846629360, \
      0.00188490438846629360, \
      0.00604980306252401318, \
      0.00604980306252401318, \
      0.00604980306252401318, \
      0.00604980306252401318, \
      0.00027850531603908424, \
      0.00027850531603908424, \
      0.00027850531603908424, \
      0.00027850531603908424, \
      0.00164429091495763209, \
      0.00164429091495763209, \
      0.00164429091495763209, \
      0.00164429091495763209, \
      0.00438466987463943282, \
      0.00438466987463943282, \
      0.00438466987463943282, \
      0.00438466987463943282, \
      0.00250821736032557372, \
      0.00250821736032557372, \
      0.00250821736032557372, \
      0.00250821736032557372, \
      0.00064031929971637594, \
      0.00064031929971637594, \
      0.00064031929971637594, \
      0.00064031929971637594, \
      0.00064031929971637594, \
      0.00064031929971637594, \
      0.00064031929971637594, \
      0.00064031929971637594, \
      0.00274360981913367684, \
      0.00274360981913367684, \
      0.00274360981913367684, \
      0.00274360981913367684, \
      0.00274360981913367684, \
      0.00274360981913367684, \
      0.00274360981913367684, \
      0.00274360981913367684, \
      0.00442513215733170758, \
      0.00442513215733170758, \
      0.00442513215733170758, \
      0.00442513215733170758, \
      0.00442513215733170758, \
      0.00442513215733170758, \
      0.00442513215733170758, \
      0.00442513215733170758, \
      0.00379353354761960502, \
      0.00379353354761960502, \
      0.00379353354761960502, \
      0.00379353354761960502, \
      0.00379353354761960502, \
      0.00379353354761960502, \
      0.00379353354761960502, \
      0.00379353354761960502, \
      0.00259873188089142833, \
      0.00259873188089142833, \
      0.00259873188089142833, \
      0.00259873188089142833, \
      0.00259873188089142833, \
      0.00259873188089142833, \
      0.00259873188089142833, \
      0.00259873188089142833, \
      0.00110056207140428312, \
      0.00110056207140428312, \
      0.00110056207140428312, \
      0.00110056207140428312, \
      0.00110056207140428312, \
      0.00110056207140428312, \
      0.00110056207140428312, \
      0.00110056207140428312, \
      0.00075594512745462764, \
      0.00075594512745462764, \
      0.00075594512745462764, \
      0.00075594512745462764, \
      0.00075594512745462764, \
      0.00075594512745462764, \
      0.00075594512745462764, \
      0.00075594512745462764, \
      0.00416443295717523060, \
      0.00416443295717523060, \
      0.00416443295717523060, \
      0.00416443295717523060, \
      0.00416443295717523060, \
      0.00416443295717523060, \
      0.00416443295717523060, \
      0.00416443295717523060, \
      0.00079864720063192577, \
      0.00079864720063192577, \
      0.00079864720063192577, \
      0.00079864720063192577, \
      0.00079864720063192577, \
      0.00079864720063192577, \
      0.00079864720063192577, \
      0.00079864720063192577, \
      0.00127477283170923661, \
      0.00127477283170923661, \
      0.00127477283170923661, \
      0.00127477283170923661, \
      0.00127477283170923661, \
      0.00127477283170923661, \
      0.00127477283170923661, \
      0.00127477283170923661, \
      0.00077420720151948649, \
      0.00077420720151948649, \
      0.00077420720151948649, \
      0.00077420720151948649, \
      0.00077420720151948649, \
      0.00077420720151948649, \
      0.00077420720151948649, \
      0.00077420720151948649, \
      0.00107986786877537822, \
      0.00107986786877537822, \
      0.00107986786877537822, \
      0.00107986786877537822, \
      0.00107986786877537822, \
      0.00107986786877537822, \
      0.00107986786877537822, \
      0.00107986786877537822, \
      0.00155093578240393421, \
      0.00155093578240393421, \
      0.00155093578240393421, \
      0.00155093578240393421, \
      0.00155093578240393421, \
      0.00155093578240393421, \
      0.00155093578240393421, \
      0.00155093578240393421, \
      0.00049937862088166734, \
      0.00049937862088166734, \
      0.00049937862088166734, \
      0.00049937862088166734, \
      0.00049937862088166734, \
      0.00049937862088166734, \
      0.00049937862088166734, \
      0.00049937862088166734, \
      0.00042623664206464421, \
      0.00042623664206464421, \
      0.00042623664206464421, \
      0.00042623664206464421, \
      0.00042623664206464421, \
      0.00042623664206464421, \
      0.00042623664206464421, \
      0.00042623664206464421, \
      0.00052445285235233835, \
      0.00052445285235233835, \
      0.00052445285235233835, \
      0.00052445285235233835, \
      0.00052445285235233835, \
      0.00052445285235233835, \
      0.00052445285235233835, \
      0.00052445285235233835, \
      0.00295483873714207741, \
      0.00295483873714207741, \
      0.00295483873714207741, \
      0.00295483873714207741, \
      0.00295483873714207741, \
      0.00295483873714207741, \
      0.00295483873714207741, \
      0.00295483873714207741, \
      0.00154064844826157059, \
      0.00154064844826157059, \
      0.00154064844826157059, \
      0.00154064844826157059, \
      0.00154064844826157059, \
      0.00154064844826157059, \
      0.00154064844826157059, \
      0.00154064844826157059, \
      0.00484986123625866239, \
      0.00484986123625866239, \
      0.00484986123625866239, \
      0.00484986123625866239, \
      0.00484986123625866239, \
      0.00484986123625866239, \
      0.00484986123625866239, \
      0.00484986123625866239, \
      0.00074953722109848120, \
      0.00074953722109848120, \
      0.00074953722109848120, \
      0.00074953722109848120, \
      0.00074953722109848120, \
      0.00074953722109848120, \
      0.00074953722109848120, \
      0.00074953722109848120, \
      0.00167732903590775981, \
      0.00167732903590775981, \
      0.00167732903590775981, \
      0.00167732903590775981, \
      0.00167732903590775981, \
      0.00167732903590775981, \
      0.00167732903590775981, \
      0.00167732903590775981, \
      0.00224204091471395155, \
      0.00224204091471395155, \
      0.00224204091471395155, \
      0.00224204091471395155, \
      0.00224204091471395155, \
      0.00224204091471395155, \
      0.00224204091471395155, \
      0.00224204091471395155, \
      0.00305423895198708934, \
      0.00305423895198708934, \
      0.00305423895198708934, \
      0.00305423895198708934, \
      0.00305423895198708934, \
      0.00305423895198708934, \
      0.00305423895198708934, \
      0.00305423895198708934, \
      0.00236370915044872495, \
      0.00236370915044872495, \
      0.00236370915044872495, \
      0.00236370915044872495, \
      0.00236370915044872495, \
      0.00236370915044872495, \
      0.00236370915044872495, \
      0.00236370915044872495, \
      0.00412477376791669549, \
      0.00412477376791669549, \
      0.00412477376791669549, \
      0.00412477376791669549, \
      0.00412477376791669549, \
      0.00412477376791669549, \
      0.00412477376791669549, \
      0.00412477376791669549, \
      0.00252281437387082835, \
      0.00252281437387082835, \
      0.00252281437387082835, \
      0.00252281437387082835, \
      0.00252281437387082835, \
      0.00252281437387082835, \
      0.00252281437387082835, \
      0.00252281437387082835, \
      0.00114336403720023422, \
      0.00114336403720023422, \
      0.00114336403720023422, \
      0.00114336403720023422, \
      0.00114336403720023422, \
      0.00114336403720023422, \
      0.00114336403720023422, \
      0.00114336403720023422, \
      0.00278500419257705868, \
      0.00278500419257705868, \
      0.00278500419257705868, \
      0.00278500419257705868, \
      0.00278500419257705868, \
      0.00278500419257705868, \
      0.00278500419257705868, \
      0.00278500419257705868, \
      0.00222262578256617873, \
      0.00222262578256617873, \
      0.00222262578256617873, \
      0.00222262578256617873, \
      0.00222262578256617873, \
      0.00222262578256617873, \
      0.00222262578256617873, \
      0.00222262578256617873, \
      0.00026099460442016807, \
      0.00026099460442016807, \
      0.00026099460442016807, \
      0.00026099460442016807, \
      0.00026099460442016807, \
      0.00026099460442016807, \
      0.00026099460442016807, \
      0.00026099460442016807, \
      0.00125217421068957169, \
      0.00125217421068957169, \
      0.00125217421068957169, \
      0.00125217421068957169, \
      0.00125217421068957169, \
      0.00125217421068957169, \
      0.00125217421068957169, \
      0.00125217421068957169, \
      0.00127967033864278819, \
      0.00127967033864278819, \
      0.00127967033864278819, \
      0.00127967033864278819, \
      0.00127967033864278819, \
      0.00127967033864278819, \
      0.00127967033864278819, \
      0.00127967033864278819, \
      0.00079904956567299025, \
      0.00079904956567299025, \
      0.00079904956567299025, \
      0.00079904956567299025, \
      0.00079904956567299025, \
      0.00079904956567299025, \
      0.00079904956567299025, \
      0.00079904956567299025, \
      0.00078122198597418405, \
      0.00078122198597418405, \
      0.00078122198597418405, \
      0.00078122198597418405, \
      0.00078122198597418405, \
      0.00078122198597418405, \
      0.00078122198597418405, \
      0.00078122198597418405, \
      0.00021725880518099310, \
      0.00021725880518099310, \
      0.00021725880518099310, \
      0.00021725880518099310, \
      0.00021725880518099310, \
      0.00021725880518099310, \
      0.00021725880518099310, \
      0.00021725880518099310, \
      0.00075955776144381827, \
      0.00075955776144381827, \
      0.00075955776144381827, \
      0.00075955776144381827, \
      0.00075955776144381827, \
      0.00075955776144381827, \
      0.00075955776144381827, \
      0.00075955776144381827 ] )

  return x, y, z, w

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
  pyramid_jaskowiec_rule_test ( )
  timestamp ( )

