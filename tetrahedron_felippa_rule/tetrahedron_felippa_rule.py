#! /usr/bin/env python3
#
def tetrahedron_felippa_rule_test ( ):

#*****************************************************************************80
#
## tetrahedron_felippa_rule_test() tests tetrahedron_felippa_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 April 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'tetrahedron_felippa_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test tetrahedron_felippa_rule().' )

  degree_max = 4
  tetrahedron_unit_monomial_test ( degree_max )

  degree_max = 4
  tetrahedron_unit_quad_test ( degree_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'tetrahedron_felippa_rule_test():' )
  print ( '  Normal end of execution.' )

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

def monomial_value ( d, n, e, x ):

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
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer D, the spatial dimension.
#
#    integer N, the number of evaluation points.
#
#    integer E(D), the exponents.
#
#    real X(N,D), the point coordinates.
#
#  Output:
#
#    real V(N), the monomial values.
#
  import numpy as np

  v = np.ones ( n )

  for j in range ( 0, d ):
    if ( 0 != e[j] ):
      for i in range ( 0, n ):
        v[i] = v[i] * x[i,j] ** e[j]

  return v

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
  if ( not more2 and n2 == n ):
    more = False

  return a, more, h, t, n2, more2

def tetrahedron_unit_monomial_integral ( expon ):

#*****************************************************************************80
#
## tetrahedron_unit_monomial_integral() integrates a monomial over the unit tetrahedron.
#
#  Discussion:
#
#    This routine integrates a monomial of the form
#
#      product ( 1 <= dim <= 3 ) x(dim)^expon(dim)
#
#    where the exponents are nonnegative integers.  Note that
#    if the combination 0^0 is encountered, it should be treated
#    as 1.
#
#    Integral ( over unit tetrahedron ) x^l y^m z^n dx dy =
#    l! * m! * n! / ( m + n + 3 )!
#
#    The integration region is defined as:
#
#      0 <= X
#      0 <= Y
#      0 <= Z
#      0 <= X + Y + Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON(3), the exponents.
#
#  Output:
#
#    real VALUE, the integral of the monomial.
#

#
#  The first computation ends with VALUE = 1.0
#
  value = 1.0
#
#  The first loop simply calculates 1, so we short circuit it.
#
# k = 0
#
# for i = 1 : expon(1)
#   k = k + 1
#   value = value * i / k
# end

  k = expon[0]
  for i in range ( 0, expon[1] ):
    k = k + 1
    value = value * ( i + 1 ) / k

  for i in range ( 0, expon[2] ):
    k = k + 1
    value = value * ( i + 1 ) / k

  k = k + 1
  value = value / k

  k = k + 1
  value = value / k

  k = k + 1
  value = value / k

  return value

def tetrahedron_unit_monomial_test ( degree_max ):

#*****************************************************************************80
#
## tetrahedron_unit_monomial_integral_test() tests tetrahedron_unit_monomial_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 April 2023
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
  print ( 'tetrahedron_unit_monomial_integral_test():' )
  print ( '  tetrahedron_unit_monomial_integral() returns the exact value of the' )
  print ( '  integral of X^ALPHA Y^BETA Z^GAMMA' )
  print ( '' )
  print ( '  Volume = ', tetrahedron_unit_volume ( ) )
  print ( '' )
  print ( '     ALPHA      BETA     GAMMA      INTEGRAL' )
  print ( '' )

  expon = np.zeros ( 3, dtype = int )

  for alpha in range ( 0, degree_max + 1 ):
    expon[0] = alpha
    for beta in range ( 0, degree_max + 1 - alpha ):
      expon[1] = beta
      for gamma in range ( 0, degree_max + 1 - alpha - beta ):
        expon[2] = gamma
        value = tetrahedron_unit_monomial_integral ( expon )
        print ( '  %8d  %8d  %8d  %14.6e' % ( expon[0], expon[1], expon[2], value ) )

  return

def tetrahedron_unit_o01 ( ):

#*****************************************************************************80
#
## tetrahedron_unit_o01() returns a 1 point quadrature rule for the unit tetrahedron.
#
#  Discussion:
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      0 <= Z
#      X + Y + Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2023
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
#    real xyz[1,3], the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    1.0 ] )

  xyz = np.array ( [ \
    [ 0.25000000000000000000,  0.25000000000000000000,  0.25000000000000000000 ] ] )

  return w, xyz

def tetrahedron_unit_o04 ( ):

#*****************************************************************************80
#
## tetrahedron_unit_o04() returns a 4 point quadrature rule for the unit tetrahedron.
#
#  Discussion:
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      0 <= Z
#      X + Y + Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2023
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
#    real xyz[4,3], the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.25000000000000000000, \
    0.25000000000000000000, \
    0.25000000000000000000, \
    0.25000000000000000000 ] )

  xyz = np.array ( [ \
    [ 0.58541019662496845446,  0.13819660112501051518,  0.13819660112501051518 ], \
    [ 0.13819660112501051518,  0.58541019662496845446,  0.13819660112501051518 ], \
    [ 0.13819660112501051518,  0.13819660112501051518,  0.58541019662496845446 ], \
    [ 0.13819660112501051518,  0.13819660112501051518,  0.13819660112501051518 ] ] )

  return w, xyz

def tetrahedron_unit_o08b ( ):

#*****************************************************************************80
#
## tetrahedron_unit_o08b() returns an 8 point quadrature rule for the unit tetrahedron.
#
#  Discussion:
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      0 <= Z
#      X + Y + Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2023
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
#    real W(8), the weights.
#
#    real xyz[8,3], the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.025000000000000000000, \
    0.025000000000000000000, \
    0.025000000000000000000, \
    0.025000000000000000000, \
    0.22500000000000000000, \
    0.22500000000000000000, \
    0.22500000000000000000, \
    0.22500000000000000000 ] )

  xyz = np.array ( [ \
    [ 1.00000000000000000000,  0.00000000000000000000,  0.00000000000000000000 ], \
    [ 0.00000000000000000000,  1.00000000000000000000,  0.00000000000000000000 ], \
    [ 0.00000000000000000000,  0.00000000000000000000,  1.00000000000000000000 ], \
    [ 0.00000000000000000000,  0.00000000000000000000,  0.00000000000000000000 ], \
    [ 0.00000000000000000000,  0.33333333333333333333,  0.33333333333333333333 ], \
    [ 0.33333333333333333333,  0.00000000000000000000,  0.33333333333333333333 ], \
    [ 0.33333333333333333333,  0.33333333333333333333,  0.00000000000000000000 ], \
    [ 0.33333333333333333333,  0.33333333333333333333,  0.33333333333333333333 ] ] )

  return w, xyz

def tetrahedron_unit_o08 ( ):

#*****************************************************************************80
#
## tetrahedron_unit_o08() returns an 8 point quadrature rule for the unit tetrahedron.
#
#  Discussion:
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      0 <= Z
#      X + Y + Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2023
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
#    real W(8), the weights.
#
#    real xyz[8,3], the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.13852796651186214232, \
    0.13852796651186214232, \
    0.13852796651186214232, \
    0.13852796651186214232, \
    0.11147203348813785768, \
    0.11147203348813785768, \
    0.11147203348813785768, \
    0.11147203348813785768 ] )

  xyz = np.array ( [ \
    [ 0.015835909865720057993,  0.32805469671142664734,  0.32805469671142664734 ], \
    [ 0.32805469671142664734,  0.015835909865720057993,  0.32805469671142664734 ], \
    [ 0.32805469671142664734,  0.32805469671142664734,  0.015835909865720057993 ], \
    [ 0.32805469671142664734,  0.32805469671142664734,  0.32805469671142664734 ], \
    [ 0.67914317820120795168,  0.10695227393293068277,  0.10695227393293068277 ], \
    [ 0.10695227393293068277,  0.67914317820120795168,  0.10695227393293068277 ], \
    [ 0.10695227393293068277,  0.10695227393293068277,  0.67914317820120795168 ], \
    [ 0.10695227393293068277,  0.10695227393293068277,  0.10695227393293068277 ] ] )

  return w, xyz

def tetrahedron_unit_o14b ( ):

#*****************************************************************************80
#
## tetrahedron_unit_o14b() returns a 14 point quadrature rule for the unit tetrahedron.
#
#  Discussion:
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      0 <= Z
#      X + Y + Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2023
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
#    real W(14), the weights.
#
#    real xyz[14,3], the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.13283874668559071814, \
    0.13283874668559071814, \
    0.13283874668559071814, \
    0.13283874668559071814, \
    0.088589824742980710434, \
    0.088589824742980710434, \
    0.088589824742980710434, \
    0.088589824742980710434, \
    0.019047619047619047619, \
    0.019047619047619047619, \
    0.019047619047619047619, \
    0.019047619047619047619, \
    0.019047619047619047619, \
    0.019047619047619047619 ] )

  xyz = np.array ( [ \
    [ 0.056881379520423421748,  0.31437287349319219275,  0.31437287349319219275 ], \
    [ 0.31437287349319219275,  0.056881379520423421748,  0.31437287349319219275 ], \
    [ 0.31437287349319219275,  0.31437287349319219275,  0.056881379520423421748 ], \
    [ 0.31437287349319219275,  0.31437287349319219275,  0.31437287349319219275 ], \
    [ 0.69841970432438656092,  0.10052676522520447969,  0.10052676522520447969 ], \
    [ 0.10052676522520447969,  0.69841970432438656092,  0.10052676522520447969 ], \
    [ 0.10052676522520447969,  0.10052676522520447969,  0.69841970432438656092 ], \
    [ 0.10052676522520447969,  0.10052676522520447969,  0.10052676522520447969 ], \
    [ 0.50000000000000000000,  0.50000000000000000000,  0.00000000000000000000 ], \
    [ 0.50000000000000000000,  0.00000000000000000000,  0.50000000000000000000 ], \
    [ 0.50000000000000000000,  0.00000000000000000000,  0.00000000000000000000 ], \
    [ 0.00000000000000000000,  0.50000000000000000000,  0.50000000000000000000 ], \
    [ 0.00000000000000000000,  0.50000000000000000000,  0.00000000000000000000 ], \
    [ 0.00000000000000000000,  0.00000000000000000000,  0.50000000000000000000 ] ] )

  return w, xyz

def tetrahedron_unit_o14 ( ):

#*****************************************************************************80
#
## tetrahedron_unit_o14() returns a 14 point quadrature rule for the unit tetrahedron.
#
#  Discussion:
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      0 <= Z
#      X + Y + Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2023
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
#    real W(14), the weights.
#
#    real xyz[14,3], the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.073493043116361949544,  \
    0.073493043116361949544,  \
    0.073493043116361949544,  \
    0.073493043116361949544,  \
    0.11268792571801585080,  \
    0.11268792571801585080,  \
    0.11268792571801585080,  \
    0.11268792571801585080,  \
    0.042546020777081466438,  \
    0.042546020777081466438,  \
    0.042546020777081466438,  \
    0.042546020777081466438,  \
    0.042546020777081466438,  \
    0.042546020777081466438 ] )

  xyz = np.array ( [ \
    [ 0.72179424906732632079,  0.092735250310891226402,  0.092735250310891226402 ], \
    [ 0.092735250310891226402,  0.72179424906732632079,  0.092735250310891226402 ], \
    [ 0.092735250310891226402,  0.092735250310891226402,  0.72179424906732632079 ], \
    [ 0.092735250310891226402,  0.092735250310891226402,  0.092735250310891226402 ], \
    [ 0.067342242210098170608,  0.31088591926330060980,  0.31088591926330060980 ], \
    [ 0.31088591926330060980,  0.067342242210098170608,  0.31088591926330060980 ], \
    [ 0.31088591926330060980,  0.31088591926330060980,  0.067342242210098170608 ], \
    [ 0.31088591926330060980,  0.31088591926330060980,  0.31088591926330060980 ], \
    [ 0.045503704125649649492,  0.045503704125649649492,  0.45449629587435035051 ], \
    [ 0.045503704125649649492,  0.45449629587435035051,  0.045503704125649649492 ], \
    [ 0.045503704125649649492,  0.45449629587435035051,  0.45449629587435035051 ], \
    [ 0.45449629587435035051,  0.045503704125649649492,  0.045503704125649649492 ], \
    [ 0.45449629587435035051,  0.045503704125649649492,  0.45449629587435035051 ], \
    [ 0.45449629587435035051,  0.45449629587435035051,  0.045503704125649649492 ] ] )

  return w, xyz

def tetrahedron_unit_o15b ( ):

#*****************************************************************************80
#
## tetrahedron_unit_o15b() returns a 15 point quadrature rule for the unit tetrahedron.
#
#  Discussion:
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      0 <= Z
#      X + Y + Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2023
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
#    real W(15), the weights.
#
#    real xyz[15,3], the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.036160714285714285714, \
    0.036160714285714285714, \
    0.036160714285714285714, \
    0.036160714285714285714, \
    0.069871494516173816465, \
    0.069871494516173816465, \
    0.069871494516173816465, \
    0.069871494516173816465, \
    0.065694849368318756074, \
    0.065694849368318756074, \
    0.065694849368318756074, \
    0.065694849368318756074, \
    0.065694849368318756074, \
    0.065694849368318756074, \
    0.18170206858253505484 ] )

  xyz = np.array ( [ \
    [ 0.00000000000000000000,  0.33333333333333333333,  0.33333333333333333333 ], \
    [ 0.33333333333333333333,  0.00000000000000000000,  0.33333333333333333333 ], \
    [ 0.33333333333333333333,  0.33333333333333333333,  0.00000000000000000000 ], \
    [ 0.33333333333333333333,  0.33333333333333333333,  0.33333333333333333333 ], \
    [ 0.72727272727272727273,  0.090909090909090909091,  0.090909090909090909091 ], \
    [ 0.090909090909090909091,  0.72727272727272727273,  0.090909090909090909091 ], \
    [ 0.090909090909090909091,  0.090909090909090909091,  0.72727272727272727273 ], \
    [ 0.090909090909090909091,  0.090909090909090909091,  0.090909090909090909091 ], \
    [ 0.43344984642633570176,  0.43344984642633570176,  0.066550153573664298240 ], \
    [ 0.43344984642633570176,  0.066550153573664298240,  0.43344984642633570176 ], \
    [ 0.43344984642633570176,  0.066550153573664298240,  0.066550153573664298240 ], \
    [ 0.066550153573664298240,  0.43344984642633570176,  0.43344984642633570176 ], \
    [ 0.066550153573664298240,  0.43344984642633570176,  0.066550153573664298240 ], \
    [ 0.066550153573664298240,  0.066550153573664298240,  0.43344984642633570176 ], \
    [ 0.25000000000000000000,  0.25000000000000000000,  0.250000000000000000 ] ] )

  return w, xyz

def tetrahedron_unit_o15 ( ):

#*****************************************************************************80
#
## tetrahedron_unit_o15() returns a 15 point quadrature rule for the unit tetrahedron.
#
#  Discussion:
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      0 <= Z
#      X + Y + Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2023
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
#    real W(15), the weights.
#
#    real xyz[15,3], the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.071937083779018620010, \
    0.071937083779018620010, \
    0.071937083779018620010, \
    0.071937083779018620010, \
    0.069068207226272385281, \
    0.069068207226272385281, \
    0.069068207226272385281, \
    0.069068207226272385281, \
    0.052910052910052910053, \
    0.052910052910052910053, \
    0.052910052910052910053, \
    0.052910052910052910053, \
    0.052910052910052910053, \
    0.052910052910052910053, \
    0.11851851851851851852 ] )

  xyz = np.array ( [ \
    [ 0.72408676584183090163,  0.091971078052723032789,  0.091971078052723032789 ], \
    [ 0.091971078052723032789,  0.72408676584183090163,  0.091971078052723032789 ], \
    [ 0.091971078052723032789,  0.091971078052723032789,  0.72408676584183090163 ], \
    [ 0.091971078052723032789,  0.091971078052723032789,  0.091971078052723032789 ], \
    [ 0.040619116511110274837,  0.31979362782962990839,  0.31979362782962990839 ], \
    [ 0.31979362782962990839,  0.040619116511110274837,  0.31979362782962990839 ], \
    [ 0.31979362782962990839,  0.31979362782962990839,  0.040619116511110274837 ], \
    [ 0.31979362782962990839,  0.31979362782962990839,  0.31979362782962990839 ], \
    [ 0.44364916731037084426,  0.44364916731037084426,  0.056350832689629155741 ], \
    [ 0.44364916731037084426,  0.056350832689629155741,  0.44364916731037084426 ], \
    [ 0.44364916731037084426,  0.056350832689629155741,  0.056350832689629155741 ], \
    [ 0.056350832689629155741,  0.44364916731037084426,  0.44364916731037084426 ], \
    [ 0.056350832689629155741,  0.44364916731037084426,  0.056350832689629155741 ], \
    [ 0.056350832689629155741,  0.056350832689629155741,  0.44364916731037084426 ], \
    [ 0.25000000000000000000,  0.25000000000000000000,  0.25000000000000000000 ] ] )

  return w, xyz

def tetrahedron_unit_o24 ( ):

#*****************************************************************************80
#
## tetrahedron_unit_o24() returns a 24 point quadrature rule for the unit tetrahedron.
#
#  Discussion:
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      0 <= Z
#      X + Y + Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2023
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
#    real W(24), the weights.
#
#    real xyz[24,3], the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.039922750257869636194,  \
    0.039922750257869636194,  \
    0.039922750257869636194,  \
    0.039922750257869636194,  \
    0.010077211055345822612,  \
    0.010077211055345822612,  \
    0.010077211055345822612,  \
    0.010077211055345822612,  \
    0.055357181543927398338,  \
    0.055357181543927398338,  \
    0.055357181543927398338,  \
    0.055357181543927398338,  \
    0.048214285714285714286,  \
    0.048214285714285714286,  \
    0.048214285714285714286,  \
    0.048214285714285714286,  \
    0.048214285714285714286,  \
    0.048214285714285714286,  \
    0.048214285714285714286,  \
    0.048214285714285714286,  \
    0.048214285714285714286,  \
    0.048214285714285714286,  \
    0.048214285714285714286,  \
    0.048214285714285714286 ] )

  xyz = np.array ( [ \
    [ 0.35619138622025439121,  0.21460287125991520293,  0.21460287125991520293 ], \
    [ 0.21460287125991520293,  0.35619138622025439121,  0.21460287125991520293 ], \
    [ 0.21460287125991520293,  0.21460287125991520293,  0.35619138622025439121 ], \
    [ 0.21460287125991520293,  0.21460287125991520293,  0.21460287125991520293 ], \
    [ 0.87797812439616594065,  0.040673958534611353116,  0.040673958534611353116 ], \
    [ 0.040673958534611353116,  0.87797812439616594065,  0.040673958534611353116 ], \
    [ 0.040673958534611353116,  0.040673958534611353116,  0.87797812439616594065 ], \
    [ 0.040673958534611353116,  0.040673958534611353116,  0.040673958534611353116 ], \
    [ 0.032986329573173468968,  0.32233789014227551034,  0.32233789014227551034 ], \
    [ 0.32233789014227551034,  0.032986329573173468968,  0.32233789014227551034 ], \
    [ 0.32233789014227551034,  0.32233789014227551034,  0.032986329573173468968 ], \
    [ 0.32233789014227551034,  0.32233789014227551034,  0.32233789014227551034 ], \
    [ 0.60300566479164914137,  0.26967233145831580803,  0.063661001875017525299 ], \
    [ 0.60300566479164914137,  0.063661001875017525299,  0.26967233145831580803 ], \
    [ 0.60300566479164914137,  0.063661001875017525299,  0.063661001875017525299 ], \
    [ 0.063661001875017525299,  0.60300566479164914137,  0.26967233145831580803 ], \
    [ 0.063661001875017525299,  0.60300566479164914137,  0.063661001875017525299 ], \
    [ 0.063661001875017525299,  0.063661001875017525299,  0.60300566479164914137 ], \
    [ 0.26967233145831580803,  0.60300566479164914137,  0.063661001875017525299 ], \
    [ 0.26967233145831580803,  0.063661001875017525299,  0.60300566479164914137 ], \
    [ 0.26967233145831580803,  0.063661001875017525299,  0.063661001875017525299 ], \
    [ 0.063661001875017525299,  0.26967233145831580803,  0.60300566479164914137 ], \
    [ 0.063661001875017525299,  0.26967233145831580803,  0.063661001875017525299 ], \
    [ 0.063661001875017525299,  0.063661001875017525299,  0.26967233145831580803 ] ] )

  return w, xyz

def tetrahedron_unit_quad_test ( degree_max ):

#*****************************************************************************80
#
## tetrahedron_unit_quad_test() tests the rules for the unit tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2023
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
  print ( 'tetrahedron_unit_quad_test():' )
  print ( '  we approximate monomial integrals with:' )
  print ( '  tetrahedron_unit_o01(),' )
  print ( '  tetrahedron_unit_o04(),' )
  print ( '  tetrahedron_unit_o08(),' )
  print ( '  tetrahedron_unit_o08b(),' )
  print ( '  tetrahedron_unit_o14(),' )
  print ( '  tetrahedron_unit_o14b(),' )
  print ( '  tetrahedron_unit_o15(),' )
  print ( '  tetrahedron_unit_o15b(),' )
  print ( '  tetrahedron_unit_o24(),' )

  expon = np.zeros ( 3, dtype = int )
  more = False
  h = 0
  t = 0
  degree_max2 = degree_max
  more2 = False

  while ( True ):

    expon, more, h, t, degree_max2, more2 = subcomp_next ( degree_max, \
      dim_num, expon, more, h, t, degree_max2, more2 )

    print ( '' )
    print ( '  Monomial exponents: ', end = '' )
    for dim in range ( 0, dim_num ):
      print ( ' ', expon[dim], end = '' )
    print ( '' )
    print ( '' )

    order = 1
    w, xyz = tetrahedron_unit_o01 ( )
    v = monomial_value ( dim_num, order, expon, xyz )
    quad = tetrahedron_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 4
    w, xyz = tetrahedron_unit_o04 ( )
    v = monomial_value ( dim_num, order, expon, xyz )
    quad = tetrahedron_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 8
    w, xyz = tetrahedron_unit_o08 ( )
    v = monomial_value ( dim_num, order, expon, xyz )
    quad = tetrahedron_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 8
    w, xyz = tetrahedron_unit_o08b ( )
    v = monomial_value ( dim_num, order, expon, xyz )
    quad = tetrahedron_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 14
    w, xyz = tetrahedron_unit_o14 ( )
    v = monomial_value ( dim_num, order, expon, xyz )
    quad = tetrahedron_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 14
    w, xyz = tetrahedron_unit_o14b ( )
    v = monomial_value ( dim_num, order, expon, xyz )
    quad = tetrahedron_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 15
    w, xyz = tetrahedron_unit_o15 ( )
    v = monomial_value ( dim_num, order, expon, xyz )
    quad = tetrahedron_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 15
    w, xyz = tetrahedron_unit_o15b ( )
    v = monomial_value ( dim_num, order, expon, xyz )
    quad = tetrahedron_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    order = 24
    w, xyz = tetrahedron_unit_o24 ( )
    v = monomial_value ( dim_num, order, expon, xyz )
    quad = tetrahedron_unit_volume ( ) * np.dot ( w, v )
    print ( '  %6d  %14f' % ( order, quad ) )

    print ( '' )
    quad = tetrahedron_unit_monomial_integral ( expon )
    print ( '  %6d  %14f' % ( order, quad ) )

    if ( not more ):
      break

  return

def tetrahedron_unit_volume ( ):

#*****************************************************************************80
#
## tetrahedron_unit_volume() returns the volume of the unit tetrahedron.
#
#  Discussion:
#
#    The integration region is:
#
#      0 <= X,
#      0 <= Y,
#      0 <= Z,
#      X + Y + Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the volume.
#
  value = 1.0 / 6.0

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
  tetrahedron_felippa_rule_test ( )
  timestamp ( )

