#! /usr/bin/env python3
#
def pyramid_felippa_rule_test ( ):

#*****************************************************************************80
#
## pyramid_felippa_rule_test() tests pyramid_felippa_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'pyramid_felippa_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test pyramid_felippa_rule().' )

  degree_max = 4
  pyramid_unit_monomial_test ( degree_max )

  degree_max = 5
  pyramid_unit_quad_test ( degree_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'pyramid_felippa_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def pyramid_unit_monomial_test ( degree_max ):

#*****************************************************************************80
#
## pyramid_unit_monomial_test() tests pyramid_unit_monomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 May 2023
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

  print ( '' )
  print ( 'pyramid_unit_monomial_test():' )
  print ( '  pyramid_unit_monomial() returns the exact value of the' )
  print ( '  integral of X^ALPHA Y^BETA Z^GAMMA' )
  print ( '' )
  print ( '  Volume = ', pyramid_unit_volume ( ) )
  print ( '' )
  print ( '     ALPHA      BETA     GAMMA      INTEGRAL' )
  print ( '' )

  expon = np.zeros ( 3, dtype = int )

  for alpha in range ( 0, degree_max + 1 ):
    expon[0] = alpha
    for beta in range ( 0, degree_max - alpha + 1 ):
      expon[1] = beta
      for gamma in range ( 0, degree_max - alpha - beta + 1 ):
        expon[2] = gamma
        value = pyramid_unit_monomial ( expon )
        print ( '  %8d  %8d  %8d  %14.6e' \
          % ( expon[0], expon[1], expon[2], value ) )

  return

def pyramid_unit_quad_test ( degree_max ):

#*****************************************************************************80
#
## pyramid_unit_quad_test() tests the rules for the unit pyramid.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2023
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

  dim_num = 3

  print ( '' )
  print ( 'pyramid_unit_quad_test():' )
  print ( '  Approximate monomial integrals in the unit pyramid.' )

  expon = np.zeros ( dim_num, dtype = int )
  more = False
  h = 0
  t = 0
  n2 = 0
  more2 = False

  while ( True ):

    expon, more, h, t, n2, more2 = subcomp_next ( degree_max, dim_num, \
      expon, more, h, t, n2, more2 )

    if ( ( expon[0] % 2 ) == 1 or ( expon[1] % 2 ) == 1 ):
      continue

    print ( '' )
    print ( '  Monomial exponents: ', expon )
    print ( '' )

    order = 1
    x, y, z, w = pyramid_unit_o01 ( )
    xyz = np.transpose ( np.array ( [ x, y, z ] ) )
    v = monomial_value ( expon, xyz )
    quad = pyramid_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 5
    x, y, z, w = pyramid_unit_o05 ( )
    xyz = np.transpose ( np.array ( [ x, y, z ] ) )
    v = monomial_value ( expon, xyz )
    quad = pyramid_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 6
    x, y, z, w = pyramid_unit_o06 ( )
    xyz = np.transpose ( np.array ( [ x, y, z ] ) )
    v = monomial_value ( expon, xyz )
    quad = pyramid_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 8
    x, y, z, w = pyramid_unit_o08 ( )
    xyz = np.transpose ( np.array ( [ x, y, z ] ) )
    v = monomial_value ( expon, xyz )
    quad = pyramid_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 8
    x, y, z, w = pyramid_unit_o08b ( )
    xyz = np.transpose ( np.array ( [ x, y, z ] ) )
    v = monomial_value ( expon, xyz )
    quad = pyramid_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 9
    x, y, z, w = pyramid_unit_o09 ( )
    xyz = np.transpose ( np.array ( [ x, y, z ] ) )
    v = monomial_value ( expon, xyz )
    quad = pyramid_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 13
    x, y, z, w = pyramid_unit_o13 ( )
    xyz = np.transpose ( np.array ( [ x, y, z ] ) )
    v = monomial_value ( expon, xyz )
    quad = pyramid_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 18
    x, y, z, w = pyramid_unit_o18 ( )
    xyz = np.transpose ( np.array ( [ x, y, z ] ) )
    v = monomial_value ( expon, xyz )
    quad = pyramid_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 27
    x, y, z, w = pyramid_unit_o27 ( )
    xyz = np.transpose ( np.array ( [ x, y, z ] ) )
    v = monomial_value ( expon, xyz )
    quad = pyramid_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 48
    x, y, z, w = pyramid_unit_o48 ( )
    xyz = np.transpose ( np.array ( [ x, y, z ] ) )
    v = monomial_value ( expon, xyz )
    quad = pyramid_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    print ( '' )
    quad = pyramid_unit_monomial ( expon )
    print ( '   Exact  %14f' % ( quad ) )

    if ( not more ):
      break

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
#    16 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer e(d), the exponents.
#
#    real x(n,d): the point coordinates.
#
#  Output:
#
#    real v(n), the monomial values.
#
  import numpy as np

  n, d = x.shape

  v = np.ones ( n )

  for j in range ( 0, d ):
    if ( 0 != e[j] ):
      for i in range ( 0, n ):
        if ( x[i,j] == 0.0 ):
          v[i] = 0.0
        elif ( e[j] != 0 ):
          v[i] = v[i] * x[i,j] ** e[j]

  return v

def pyramid_unit_monomial ( expon ):

#*****************************************************************************80
#
## pyramid_unit_monomial(): monomial integral in a unit pyramid.
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
#    16 May 2023
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
#    integer EXPON(3), the exponents.
#
#  Output:
#
#    real VALUE, the integral of the monomial.
#
  from scipy.special import comb

  value = 0.0

  if ( ( expon[0] % 2 ) == 0 and ( expon[1] % 2 ) == 0 ):

    i_hi = 2 + expon[0] + expon[1]

    mop = 1.0
    for i in range ( 0, i_hi + 1 ):
      value = value + mop * comb ( i_hi, i ) / ( i + expon[2] + 1 )
      mop = - mop

    value = value * 2.0 / ( expon[0] + 1 ) * 2.0 / ( expon[1] + 1 )

  return value

def pyramid_unit_o01 ( ):

#*****************************************************************************80
#
## pyramid_unit_o01() returns a 1 point quadrature rule for the unit pyramid.
#
#  Discussion:
#
#    The integration region is defined as:
#
#    - ( 1 - Z ) <= X <= 1 - Z
#    - ( 1 - Z ) <= Y <= 1 - Z
#              0 <= Z <= 1.
#
#    When Z is zero, the integration region is a square lying in the (X,Y) 
#    plane, centered at (0,0,0) with "radius" 1.  As Z increases to 1, the 
#    radius of the square diminishes, and when Z reaches 1, the square has 
#    contracted to the single point (0,0,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 May 2023
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
#    real x(), y(), z(): the abscissas.
#
#    real w(): the weights.
#
  import numpy as np

  w = np.array ( [ 1.0 ] )

  x = np.array ( [ 0.0 ] )

  y = np.array ( [ 0.0 ] )

  z = np.array ( [ 0.25 ] )

  return x, y, z, w

def pyramid_unit_o05 ( ):

#*****************************************************************************80
#
## pyramid_unit_o05() returns a 5 point quadrature rule for the unit pyramid.
#
#  Discussion:
#
#    The integration region is defined as:
#
#    - ( 1 - Z ) <= X <= 1 - Z
#    - ( 1 - Z ) <= Y <= 1 - Z
#              0 <= Z <= 1.
#
#    When Z is zero, the integration region is a square lying in the (X,Y) 
#    plane, centered at (0,0,0) with "radius" 1.  As Z increases to 1, the 
#    radius of the square diminishes, and when Z reaches 1, the square has 
#    contracted to the single point (0,0,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 May 2023
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
#    real x(), y(), z(): the abscissas.
#
#    real w(): the weights.
#
  import numpy as np

  x = np.array ( [ \
  -0.48686449556014765641, \
   0.48686449556014765641, \
   0.48686449556014765641, \
  -0.48686449556014765641, \
   0.00000000000000000000 ] )

  y = np.array ( [ \
   -0.48686449556014765641, \
   -0.48686449556014765641, \
    0.48686449556014765641, \
    0.48686449556014765641, \
    0.00000000000000000000 ] )

  z = np.array ( [ \
    0.16666666666666666667, \
    0.16666666666666666667, \
    0.16666666666666666667, \
    0.16666666666666666667, \
    0.70000000000000000000 ] )

  w = np.array ( [ \
   0.21093750000000000000, \
   0.21093750000000000000, \
   0.21093750000000000000, \
   0.21093750000000000000, \
   0.15625000000000000000 ] )

  return x, y, z, w

def pyramid_unit_o06 ( ):

#*****************************************************************************80
#
## pyramid_unit_o06() returns a 6 point quadrature rule for the unit pyramid.
#
#  Discussion:
#
#    The integration region is defined as:
#
#    - ( 1 - Z ) <= X <= 1 - Z
#    - ( 1 - Z ) <= Y <= 1 - Z
#              0 <= Z <= 1.
#
#    When Z is zero, the integration region is a square lying in the (X,Y) 
#    plane, centered at (0,0,0) with "radius" 1.  As Z increases to 1, the 
#    radius of the square diminishes, and when Z reaches 1, the square has 
#    contracted to the single point (0,0,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 May 2023
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
#    real x(), y(), z(): the abscissas.
#
#    real w(): the weights.
#
  import numpy as np

  x = np.array ( [ \
  -0.48795003647426658968, \
   0.48795003647426658968, \
   0.48795003647426658968, \
  -0.48795003647426658968, \
   0.00000000000000000000, \
   0.00000000000000000000 ] )

  y = np.array ( [ \
  -0.48795003647426658968, \
  -0.48795003647426658968, \
   0.48795003647426658968, \
   0.48795003647426658968, \
   0.00000000000000000000, \
   0.00000000000000000000 ] )

  z = np.array ( [ \
   0.16666666666666666667, \
   0.16666666666666666667, \
   0.16666666666666666667, \
   0.16666666666666666667, \
   0.58333333333333333333, \
   0.75000000000000000000 ] )

  w = np.array ( [ \
   0.21000000000000000000, \
   0.21000000000000000000, \
   0.21000000000000000000, \
   0.21000000000000000000, \
   0.06000000000000000000, \
   0.10000000000000000000 ] )

  return x, y, z, w

def pyramid_unit_o08b ( ):

#*****************************************************************************80
#
## pyramid_unit_o08b() returns an 8 point quadrature rule for the unit pyramid.
#
#  Discussion:
#
#    The integration region is defined as:
#
#    - ( 1 - Z ) <= X <= 1 - Z
#    - ( 1 - Z ) <= Y <= 1 - Z
#              0 <= Z <= 1.
#
#    When Z is zero, the integration region is a square lying in the (X,Y) 
#    plane, centered at (0,0,0) with "radius" 1.  As Z increases to 1, the 
#    radius of the square diminishes, and when Z reaches 1, the square has 
#    contracted to the single point (0,0,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 May 2023
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
#    real x(), y(), z(): the abscissas.
#
#    real w(): the weights.
#
  import numpy as np

  x = np.array ( [ \
  -0.51197009372656270107, \
   0.51197009372656270107, \
   0.51197009372656270107, \
  -0.51197009372656270107, \
  -0.28415447557052037456, \
   0.28415447557052037456, \
   0.28415447557052037456, \
  -0.28415447557052037456 ] )

  y = np.array ( [ \
  -0.51197009372656270107, \
  -0.51197009372656270107, \
   0.51197009372656270107, \
   0.51197009372656270107, \
  -0.28415447557052037456, \
  -0.28415447557052037456, \
   0.28415447557052037456, \
   0.28415447557052037456 ] )

  z = np.array ( [ \
   0.11024490204163285720, \
   0.11024490204163285720, \
   0.11024490204163285720, \
   0.11024490204163285720, \
   0.518326526529795714229, \
   0.518326526529795714229, \
   0.518326526529795714229, \
   0.518326526529795714229 ] )

  w = np.array ( [ \
   0.16438287736328777572, \
   0.16438287736328777572, \
   0.16438287736328777572, \
   0.16438287736328777572, \
   0.085617122636712224276, \
   0.085617122636712224276, \
   0.085617122636712224276, \
   0.085617122636712224276 ] )

  return x, y, z, w

def pyramid_unit_o08 ( ):

#*****************************************************************************80
#
## pyramid_unit_o08() returns an 8 point quadrature rule for the unit pyramid.
#
#  Discussion:
#
#    The integration region is defined as:
#
#    - ( 1 - Z ) <= X <= 1 - Z
#    - ( 1 - Z ) <= Y <= 1 - Z
#              0 <= Z <= 1.
#
#    When Z is zero, the integration region is a square lying in the (X,Y) 
#    plane, centered at (0,0,0) with "radius" 1.  As Z increases to 1, the 
#    radius of the square diminishes, and when Z reaches 1, the square has 
#    contracted to the single point (0,0,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 May 2023
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
#    real x(), y(), z(): the abscissas.
#
#    real w(): the weights.
#
  import numpy as np

  x = np.array ( [ \
  -0.26318405556971359557, \
   0.26318405556971359557, \
   0.26318405556971359557, \
  -0.26318405556971359557, \
  -0.50661630334978742377, \
   0.50661630334978742377, \
   0.50661630334978742377, \
  -0.50661630334978742377  ] )

  y = np.array ( [ \
  -0.26318405556971359557, \
  -0.26318405556971359557, \
   0.26318405556971359557, \
   0.26318405556971359557, \
  -0.50661630334978742377, \
  -0.50661630334978742377, \
   0.50661630334978742377, \
   0.50661630334978742377 ] )

  z = np.array ( [ \
   0.54415184401122528880, \
   0.54415184401122528880, \
   0.54415184401122528880, \
   0.54415184401122528880, \
   0.12251482265544137787, \
   0.12251482265544137787, \
   0.12251482265544137787, \
   0.12251482265544137787 ] )

  w = np.array ( [ \
   0.075589411559869072938, \
   0.075589411559869072938, \
   0.075589411559869072938, \
   0.075589411559869072938, \
   0.17441058844013092706, \
   0.17441058844013092706, \
   0.17441058844013092706, \
   0.17441058844013092706 ] )

  return x, y, z, w

def pyramid_unit_o09 ( ):

#*****************************************************************************80
#
## pyramid_unit_o09() returns a 9 point quadrature rule for the unit pyramid.
#
#  Discussion:
#
#    The integration region is defined as:
#
#    - ( 1 - Z ) <= X <= 1 - Z
#    - ( 1 - Z ) <= Y <= 1 - Z
#              0 <= Z <= 1.
#
#    When Z is zero, the integration region is a square lying in the (X,Y) 
#    plane, centered at (0,0,0) with "radius" 1.  As Z increases to 1, the 
#    radius of the square diminishes, and when Z reaches 1, the square has 
#    contracted to the single point (0,0,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 May 2023
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
#    real x(), y(), z(): the abscissas.
#
#    real w(): the weights.
#
  import numpy as np

  x = np.array ( [ \
  -0.52966422253852215131, \
   0.52966422253852215131, \
   0.52966422253852215131, \
  -0.52966422253852215131, \
  -0.34819753825720418039, \
   0.34819753825720418039, \
   0.34819753825720418039, \
  -0.34819753825720418039, \
   0.00000000000000000000 ] )

  y = np.array ( [ \
  -0.52966422253852215131, \
  -0.52966422253852215131, \
   0.52966422253852215131, \
   0.52966422253852215131, \
  -0.34819753825720418039, \
  -0.34819753825720418039, \
   0.34819753825720418039, \
   0.34819753825720418039, \
   0.00000000000000000000 ] )

  z = np.array ( [ \
   0.08176876558246862335, \
   0.08176876558246862335, \
   0.08176876558246862335, \
   0.08176876558246862335, \
   0.400374091560388519511, \
   0.400374091560388519511, \
   0.400374091560388519511, \
   0.400374091560388519511, \
   0.83333333333333333333 ] )

  w = np.array ( [ \
   0.13073389672275944791, \
   0.13073389672275944791, \
   0.13073389672275944791, \
   0.13073389672275944791, \
   0.10989110327724055209, \
   0.10989110327724055209, \
   0.10989110327724055209, \
   0.10989110327724055209, \
   0.03750000000000000000 ] )

  return x, y, z, w

def pyramid_unit_o13 ( ):

#*****************************************************************************80
#
## pyramid_unit_o13() returns a 13 point quadrature rule for the unit pyramid.
#
#  Discussion:
#
#    The integration region is defined as:
#
#    - ( 1 - Z ) <= X <= 1 - Z
#    - ( 1 - Z ) <= Y <= 1 - Z
#              0 <= Z <= 1.
#
#    When Z is zero, the integration region is a square lying in the (X,Y) 
#    plane, centered at (0,0,0) with "radius" 1.  As Z increases to 1, the 
#    radius of the square diminishes, and when Z reaches 1, the square has 
#    contracted to the single point (0,0,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 May 2023
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
#    real x(), y(), z(): the abscissas.
#
#    real w(): the weights.
#
  import numpy as np

  x = np.array ( [ \
  -0.38510399211870384331, \
   0.38510399211870384331, \
   0.38510399211870384331, \
  -0.38510399211870384331, \
  -0.40345831960728204766, \
   0.40345831960728204766, \
   0.00000000000000000000, \
   0.00000000000000000000, \
  -0.53157877436961973359, \
   0.53157877436961973359, \
   0.53157877436961973359, \
  -0.53157877436961973359, \
   0.00000000000000000000 ] )

  y = np.array ( [ \
  -0.38510399211870384331, \
  -0.38510399211870384331, \
   0.38510399211870384331, \
   0.38510399211870384331, \
   0.00000000000000000000, \
   0.00000000000000000000, \
  -0.40345831960728204766, \
   0.40345831960728204766, \
  -0.53157877436961973359, \
  -0.53157877436961973359, \
   0.53157877436961973359, \
   0.53157877436961973359, \
   0.00000000000000000000 ] )

  z = np.array ( [ \
  0.428571428571428571429, \
  0.428571428571428571429, \
  0.428571428571428571429, \
  0.428571428571428571429, \
  0.33928571428571428571, \
  0.33928571428571428571, \
  0.33928571428571428571, \
  0.33928571428571428571, \
  0.08496732026143790850, \
  0.08496732026143790850, \
  0.08496732026143790850, \
  0.08496732026143790850, \
  0.76219701803768503595 ] )

  w = np.array ( [ \
   0.063061594202898550725, \
   0.063061594202898550725, \
   0.063061594202898550725, \
   0.063061594202898550725, \
   0.042101946815575556199, \
   0.042101946815575556199, \
   0.042101946815575556199, \
   0.042101946815575556199, \
   0.13172030707666776585, \
   0.13172030707666776585, \
   0.13172030707666776585, \
   0.13172030707666776585, \
   0.05246460761943250889 ] )

  return x, y, z, w

def pyramid_unit_o18 ( ):

#*****************************************************************************80
#
## pyramid_unit_o18() returns an 18 point quadrature rule for the unit pyramid.
#
#  Discussion:
#
#    The integration region is defined as:
#
#    - ( 1 - Z ) <= X <= 1 - Z
#    - ( 1 - Z ) <= Y <= 1 - Z
#              0 <= Z <= 1.
#
#    When Z is zero, the integration region is a square lying in the (X,Y) 
#    plane, centered at (0,0,0) with "radius" 1.  As Z increases to 1, the 
#    radius of the square diminishes, and when Z reaches 1, the square has 
#    contracted to the single point (0,0,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 May 2023
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
#    real x(), y(), z(): the abscissas.
#
#    real w(): the weights.
#
  import numpy as np

  x = np.array ( [ \
  -0.35309846330877704481, \
   0.00000000000000000000, \
   0.35309846330877704481, \
  -0.35309846330877704481, \
   0.00000000000000000000, \
   0.35309846330877704481, \
  -0.35309846330877704481, \
   0.00000000000000000000, \
   0.35309846330877704481, \
  -0.67969709567986745790, \
   0.00000000000000000000, \
   0.67969709567986745790, \
  -0.67969709567986745790, \
   0.00000000000000000000, \
   0.67969709567986745790, \
  -0.67969709567986745790, \
   0.00000000000000000000, \
   0.67969709567986745790 ] )

  y = np.array ( [ \
  -0.35309846330877704481, \
  -0.35309846330877704481, \
  -0.35309846330877704481, \
   0.00000000000000000000, \
   0.00000000000000000000, \
   0.00000000000000000000, \
   0.35309846330877704481, \
   0.35309846330877704481, \
   0.35309846330877704481, \
  -0.67969709567986745790, \
  -0.67969709567986745790, \
  -0.67969709567986745790, \
   0.00000000000000000000, \
   0.00000000000000000000, \
   0.00000000000000000000, \
   0.67969709567986745790, \
   0.67969709567986745790, \
   0.67969709567986745790 ] )

  z = np.array ( [ \
  0.544151844011225288800, \
  0.544151844011225288800, \
  0.544151844011225288800, \
  0.544151844011225288800, \
  0.544151844011225288800, \
  0.544151844011225288800, \
  0.544151844011225288800, \
  0.544151844011225288800, \
  0.544151844011225288800, \
  0.12251482265544137787, \
  0.12251482265544137787, \
  0.12251482265544137787, \
  0.12251482265544137787, \
  0.12251482265544137787, \
  0.12251482265544137787, \
  0.12251482265544137787, \
  0.12251482265544137787, \
   0.12251482265544137787 ] )

  w = np.array ( [ \
   0.023330065296255886709, \
   0.037328104474009418735, \
   0.023330065296255886709, \
   0.037328104474009418735, \
   0.059724967158415069975, \
   0.037328104474009418735, \
   0.023330065296255886709, \
   0.037328104474009418735, \
   0.023330065296255886709, \
   0.05383042853090460712, \
   0.08612868564944737139, \
   0.05383042853090460712, \
   0.08612868564944737139, \
   0.13780589703911579422, \
   0.08612868564944737139, \
   0.05383042853090460712, \
   0.08612868564944737139, \
   0.05383042853090460712 ] )

  return x, y, z, w

def pyramid_unit_o27 ( ):

#*****************************************************************************80
#
## pyramid_unit_o27() returns a 27 point quadrature rule for the unit pyramid.
#
#  Discussion:
#
#    The integration region is defined as:
#
#    - ( 1 - Z ) <= X <= 1 - Z
#    - ( 1 - Z ) <= Y <= 1 - Z
#              0 <= Z <= 1.
#
#    When Z is zero, the integration region is a square lying in the (X,Y) 
#    plane, centered at (0,0,0) with "radius" 1.  As Z increases to 1, the 
#    radius of the square diminishes, and when Z reaches 1, the square has 
#    contracted to the single point (0,0,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 May 2023
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
#    real x(), y(), z(): the abscissas.
#
#    real w(): the weights.
#
  import numpy as np

  x = np.array ( [ \
  -0.7180557413198889387, \
   0.00000000000000000000, \
   0.7180557413198889387, \
  -0.7180557413198889387, \
   0.00000000000000000000, \
   0.7180557413198889387, \
  -0.7180557413198889387, \
   0.00000000000000000000, \
   0.7180557413198889387, \
  -0.50580870785392503961, \
   0.00000000000000000000, \
   0.50580870785392503961, \
  -0.50580870785392503961, \
   0.00000000000000000000, \
   0.50580870785392503961, \
  -0.50580870785392503961, \
   0.00000000000000000000, \
   0.50580870785392503961, \
  -0.22850430565396735360, \
   0.00000000000000000000, \
   0.22850430565396735360, \
  -0.22850430565396735360, \
   0.00000000000000000000, \
   0.22850430565396735360, \
  -0.22850430565396735360, \
   0.00000000000000000000, \
   0.22850430565396735360 ] )

  y = np.array ( [ \
  -0.7180557413198889387, \
  -0.7180557413198889387, \
  -0.7180557413198889387, \
   0.00000000000000000000, \
   0.00000000000000000000, \
   0.00000000000000000000, \
   0.7180557413198889387, \
   0.7180557413198889387, \
   0.7180557413198889387, \
  -0.50580870785392503961, \
  -0.50580870785392503961, \
  -0.50580870785392503961, \
   0.00000000000000000000, \
   0.00000000000000000000, \
   0.00000000000000000000, \
   0.50580870785392503961, \
   0.50580870785392503961, \
   0.50580870785392503961, \
  -0.22850430565396735360, \
  -0.22850430565396735360, \
  -0.22850430565396735360, \
   0.00000000000000000000, \
   0.00000000000000000000, \
   0.00000000000000000000, \
   0.22850430565396735360, \
   0.22850430565396735360, \
   0.22850430565396735360 ] )

  z = np.array ( [ \
  0.07299402407314973216, \
  0.07299402407314973216, \
  0.07299402407314973216, \
  0.07299402407314973216, \
  0.07299402407314973216, \
  0.07299402407314973216, \
  0.07299402407314973216, \
  0.07299402407314973216, \
  0.07299402407314973216, \
  0.34700376603835188472, \
  0.34700376603835188472, \
  0.34700376603835188472, \
  0.34700376603835188472, \
  0.34700376603835188472, \
  0.34700376603835188472, \
  0.34700376603835188472, \
  0.34700376603835188472, \
  0.34700376603835188472, \
  0.70500220988849838312, \
  0.70500220988849838312, \
  0.70500220988849838312, \
  0.70500220988849838312, \
  0.70500220988849838312, \
  0.70500220988849838312, \
  0.70500220988849838312, \
  0.70500220988849838312, \
  0.70500220988849838312 ] )

  w = np.array ( [ \
   0.036374157653908938268, \
   0.05819865224625430123, \
   0.036374157653908938268, \
   0.05819865224625430123, \
   0.09311784359400688197, \
   0.05819865224625430123, \
   0.036374157653908938268, \
   0.05819865224625430123, \
   0.036374157653908938268, \
   0.033853303069413431019, \
   0.054165284911061489631, \
   0.033853303069413431019, \
   0.054165284911061489631, \
   0.08666445585769838341, \
   0.054165284911061489631, \
   0.033853303069413431019, \
   0.054165284911061489631, \
   0.033853303069413431019, \
   0.006933033103838124540, \
   0.011092852966140999264, \
   0.006933033103838124540, \
   0.011092852966140999264, \
   0.017748564745825598822, \
   0.011092852966140999264, \
   0.006933033103838124540, \
   0.011092852966140999264, \
   0.006933033103838124540 ] )

  return x, y, z, w

def pyramid_unit_o48 ( ):

#*****************************************************************************80
#
## pyramid_unit_o48() returns a 48 point quadrature rule for the unit pyramid.
#
#  Discussion:
#
#    The integration region is defined as:
#
#    - ( 1 - Z ) <= X <= 1 - Z
#    - ( 1 - Z ) <= Y <= 1 - Z
#              0 <= Z <= 1.
#
#    When Z is zero, the integration region is a square lying in the (X,Y) 
#    plane, centered at (0,0,0) with "radius" 1.  As Z increases to 1, the 
#    radius of the square diminishes, and when Z reaches 1, the square has 
#    contracted to the single point (0,0,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 May 2023
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
#    real x(), y(), z(): the abscissas.
#
#    real w(): the weights.
#
  import numpy as np

  x = np.array ( [ \
  0.88091731624450909, \
 -0.88091731624450909, \
   0.0000000000000000, \
   0.0000000000000000, \
  0.70491874112648223, \
 -0.70491874112648223, \
   0.0000000000000000, \
   0.0000000000000000, \
  0.44712732143189760, \
 -0.44712732143189760, \
   0.0000000000000000, \
   0.0000000000000000, \
  0.18900486065123448, \
 -0.18900486065123448, \
   0.0000000000000000, \
   0.0000000000000000, \
  0.36209733410322176, \
 -0.36209733410322176, \
 -0.36209733410322176, \
  0.36209733410322176, \
  0.76688932060387538, \
 -0.76688932060387538, \
 -0.76688932060387538, \
  0.76688932060387538, \
  0.28975386476618070, \
 -0.28975386476618070, \
 -0.28975386476618070, \
  0.28975386476618070, \
  0.61367241226233160, \
 -0.61367241226233160, \
 -0.61367241226233160, \
  0.61367241226233160, \
  0.18378979287798017, \
 -0.18378979287798017, \
 -0.18378979287798017, \
  0.18378979287798017, \
  0.38925011625173161, \
 -0.38925011625173161, \
 -0.38925011625173161, \
  0.38925011625173161, \
  7.76896479525748113E-02, \
 -7.76896479525748113E-02, \
 -7.76896479525748113E-02, \
  7.76896479525748113E-02, \
  0.16453962988669860, \
 -0.16453962988669860, \
 -0.16453962988669860, \
  0.16453962988669860 ] )

  y = np.array ( [ \
   0.0000000000000000, \
   0.0000000000000000, \
   0.88091731624450909, \
  -0.88091731624450909, \
   0.0000000000000000, \
   0.0000000000000000, \
   0.70491874112648223, \
  -0.70491874112648223, \
   0.0000000000000000, \
   0.0000000000000000, \
   0.44712732143189760, \
  -0.44712732143189760, \
   0.0000000000000000, \
   0.0000000000000000, \
   0.18900486065123448, \
  -0.18900486065123448, \
   0.36209733410322176, \
   0.36209733410322176, \
  -0.36209733410322176, \
  -0.36209733410322176, \
   0.76688932060387538, \
   0.76688932060387538, \
  -0.76688932060387538, \
  -0.76688932060387538, \
   0.28975386476618070, \
   0.28975386476618070, \
  -0.28975386476618070, \
  -0.28975386476618070, \
   0.61367241226233160, \
   0.61367241226233160, \
  -0.61367241226233160, \
  -0.61367241226233160, \
   0.18378979287798017, \
   0.18378979287798017, \
  -0.18378979287798017, \
  -0.18378979287798017, \
   0.38925011625173161, \
   0.38925011625173161, \
  -0.38925011625173161, \
  -0.38925011625173161, \
   7.76896479525748113E-02, \
   7.76896479525748113E-02, \
  -7.76896479525748113E-02, \
  -7.76896479525748113E-02, \
   0.16453962988669860, \
   0.16453962988669860, \
  -0.16453962988669860, \
  -0.16453962988669860 ] )

  z = np.array ( [ \
    4.85005494469969989E-02, \
    4.85005494469969989E-02, \
   4.85005494469969989E-02, \
   4.85005494469969989E-02, \
    0.23860073755186201, \
    0.23860073755186201, \
   0.23860073755186201, \
   0.23860073755186201, \
    0.51704729510436798, \
    0.51704729510436798, \
   0.51704729510436798, \
   0.51704729510436798, \
    0.79585141789677305, \
    0.79585141789677305, \
   0.79585141789677305, \
   0.79585141789677305, \
   4.85005494469969989E-02, \
   4.85005494469969989E-02, \
   4.85005494469969989E-02, \
   4.85005494469969989E-02, \
   4.85005494469969989E-02, \
   4.85005494469969989E-02, \
   4.85005494469969989E-02, \
   4.85005494469969989E-02, \
   0.23860073755186201, \
   0.23860073755186201, \
   0.23860073755186201, \
   0.23860073755186201, \
   0.23860073755186201, \
   0.23860073755186201, \
   0.23860073755186201, \
   0.23860073755186201, \
   0.51704729510436798, \
   0.51704729510436798, \
   0.51704729510436798, \
   0.51704729510436798, \
   0.51704729510436798, \
   0.51704729510436798, \
   0.51704729510436798, \
   0.51704729510436798, \
   0.79585141789677305, \
   0.79585141789677305, \
   0.79585141789677305, \
   0.79585141789677305, \
   0.79585141789677305, \
   0.79585141789677305, \
   0.79585141789677305, \
   0.79585141789677305 ] )

  w = np.array ( [ \
  2.01241939442682455E-002, \
  2.01241939442682455E-002, \
  2.01241939442682455E-002, \
  2.01241939442682455E-002, \
  2.60351137043010779E-002, \
  2.60351137043010779E-002, \
  2.60351137043010779E-002, \
  2.60351137043010779E-002, \
  1.24557795239745531E-002, \
  1.24557795239745531E-002, \
  1.24557795239745531E-002, \
  1.24557795239745531E-002, \
  1.87873998794808156E-003, \
  1.87873998794808156E-003, \
  1.87873998794808156E-003, \
  1.87873998794808156E-003, \
  4.32957927807745280E-002, \
  4.32957927807745280E-002, \
  4.32957927807745280E-002, \
  4.32957927807745280E-002, \
  1.97463249834127288E-002, \
  1.97463249834127288E-002, \
  1.97463249834127288E-002, \
  1.97463249834127288E-002, \
  5.60127223523590526E-002, \
  5.60127223523590526E-002, \
  5.60127223523590526E-002, \
  5.60127223523590526E-002, \
  2.55462562927473852E-002, \
  2.55462562927473852E-002, \
  2.55462562927473852E-002, \
  2.55462562927473852E-002, \
  2.67977366291788643E-002, \
  2.67977366291788643E-002, \
  2.67977366291788643E-002, \
  2.67977366291788643E-002, \
  1.22218992265373354E-002, \
  1.22218992265373354E-002, \
  1.22218992265373354E-002, \
  1.22218992265373354E-002, \
  4.04197740453215038E-003, \
  4.04197740453215038E-003, \
  4.04197740453215038E-003, \
  4.04197740453215038E-003, \
  1.84346316995826843E-003, \
  1.84346316995826843E-003, \
  1.84346316995826843E-003, \
  1.84346316995826843E-003 ] )

  return x, y, z, w

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
#    16 May 2023
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

def subcomp_next ( n, k, a, more, h, t, n2, more2 ):

#*****************************************************************************80
#
## subcomp_next() computes the next subcomposition of N into K parts.
#
#  Discussion:
#
#    A composition of the integer N into K parts is an ordered sequence
#    of K nonnegative integers which sum to a value of N.
#
#    A subcomposition of the integer N into K parts is a composition
#    of M into K parts, where 0 <= M <= N.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer whose subcompositions are desired.
#
#    integer K, the number of parts in the subcomposition.
#
#    integer A(K), the parts of the subcomposition.
#
#    bool MORE, set to FALSE by the user to start the computation.
#
#    integer H, T, N2, internal parameters needed for the
#    computation.  The user may need to initialize these before the
#    very first call, but these initial values are not important.
#    The user should not alter these parameters once the computation
#    begins.
#
#    bool MORE2, an internal parameter needed for the
#    computation.  The user may need to initialize this before the
#    very first call, but the initial value is not important.
#    The user should not alter this parameter once the computation
#    begins.
#
#  Output:
#
#    integer A(K), the parts of the subcomposition.
#
#    bool MORE, set to FALSE by the routine to end the computation.
#
#    integer H, T, N2, updated values.
#
#    bool MORE2, an updated value.
#

#
#  The first computation.
#
  if ( not more ):

    for i in range ( 0, k ):
      a[i] = 0
    more = True
    h = 0
    t = 0
    n2 = 0
    more2 = False
#
#  Do the next element at the current value of N.
#
  elif ( more2 ):

    a, more2, h, t = comp_next ( n2, k, a, more2, h, t )

  else:

    more2 = False
    n2 = n2 + 1

    a, more2, h, t = comp_next ( n2, k, a, more2, h, t )
#
#  Termination occurs if MORE2 = FALSE and N2 = N.
#
  if ( ( not more2 ) and ( n2 == n ) ):
    more = False

  return a, more, h, t, n2, more2

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  pyramid_felippa_rule_test ( )
  timestamp ( )

