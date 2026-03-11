#! /usr/bin/env python3
#
def pyramid_exactness_test ( ):

#*****************************************************************************80
#
## pyramid_exactness_test() tests pyramid_exactness().
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
  print ( 'pyramid_exactness_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test pyramid_exactness().' )

  filename = 'pyramid_l3x3_j3'
  degree_max = 5

  pyramid_exactness ( filename, degree_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'pyramid_exactness_test():' )
  print ( '  Normal end of execution.' )

  return

def pyramid_exactness ( quad_filename, degree_max ):

#*****************************************************************************80
#
## pyramid_exactness() investigates the exactness of a pyramid quadrature rule.
#
#  Discussion:
#
#    This program investigates the polynomial exactness of a quadrature
#    rule for the pyramid.
#
#    The integration region is:
# 
#      - ( 1 - Z ) <= X <= 1 - Z
#      - ( 1 - Z ) <= Y <= 1 - Z
#                0 <= Z <= 1.
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
#  Input:
#
#    character QUAD_FILENAME: the header for the R, W, X filenames.
#
#    integer DEGREE_MAX: the maximum degree to check.
#
  import numpy as np

  print ( '' )
  print ( 'pyramid_exactness():' )
  print ( '  Investigate the polynomial exactness of' )
  print ( '  a quadrature rule for the pyramid.' )
#
#  Create the names of:
#    the quadrature X file
#    the quadrature W file
#
  quad_x_filename = quad_filename + '_x.txt'
  quad_w_filename = quad_filename + '_w.txt'
#
#  Summarize the input.
#
  print ( '' )
  print ( 'pyramid_exactness(): User input:' )
  print ( '  Quadrature rule X file = "' + quad_x_filename + '".' )
  print ( '  Quadrature rule W file = "' + quad_w_filename + '".' )
  print ( '  Maximum total degree to check = ', degree_max )
#
#  Read the X file.
#
  xyz = np.loadtxt ( quad_x_filename )
  order, dim_num = xyz.shape

  print ( '' )
  print ( '  Number of points  = ', order )
  print ( '  Spatial dimension = ', dim_num )

  if ( dim_num != 3 ):
    print ( '' )
    print ( 'pyramid_exactness(): Fatal error!' )
    print ( '  The quadrature abscissas must be 3 dimensional.' )
    raise Exception ( 'pyramid_exactness(): Fatal error!' )
#
#  Read the W file.
#
  w = np.loadtxt ( quad_w_filename )

  order2 = w.shape[0]

  if ( order2 != order ):
    print ( '' )
    print ( 'pyramid_exactness(): Fatal error!' )
    print ( '  The quadrature weight file should have exactly' )
    print ( '  the same number of lines as the abscissa file.' )
    raise Exception ( 'pyramid_exactness(): Fatal error!' )
#
#  Explore the monomials.
#
  print ( '' )
  print ( '      Error    Degree  Exponents' )
  print ( '' )

  for degree in range ( 0, degree_max + 3 ):

    expon = np.zeros ( dim_num, dtype = int )
    more = False
    h = 0
    t = 0
    max_error = 0.0

    while ( True ):

      expon, more, h, t = comp_next ( degree, dim_num, expon, more, h, t )

      v = monomial_value ( expon, xyz )

      quad = pyramid_unit_volume ( ) * np.dot ( w, v )

      exact = pyramid_unit_integral_monomial ( expon )

      quad_error = np.abs ( quad - exact )

      max_error = max ( max_error, quad_error )

      if ( not more ):
        break

    print ( '  %2d  %24.16f' % ( degree, max_error ) )

#
#  Terminate.
#
  print ( '' )
  print ( 'pyramid_exactness():' )
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

def pyramid_unit_integral_monomial ( expon ):

#*****************************************************************************80
#
## pyramid_unit_integral_monomial(): monomial integral in a unit pyramid.
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
  pyramid_exactness_test ( )
  timestamp ( )

