#! /usr/bin/env python3
#
def wedge_exactness_test ( ):

#*****************************************************************************80
#
## wedge_exactness_test() tests wedge_exactness().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'wedge_exactness_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test wedge_exactness()' )

  wedge_exactness ( 'wedge_felippa_3x2', 4 )
#
#  Terminate.
#
  print ( '' )
  print ( 'wedge_exactness_test():' )
  print ( '  Normal end of execution.' )

  return
def wedge_exactness ( quad_filename, degree_max ):

#*****************************************************************************80
#
## wedge_exactness() determines exactness of unit wedge quadrature rules.
#
#  Discussion:
#
#    This program investigates the polynomial exactness of a quadrature
#    rule for the unit wedge.
#
#    The interior of the unit wedge in 3D is defined by the constraints:
#      0 <= X
#      0 <= Y
#           X + Y <= 1
#     -1 <= Z <= +1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character QUAD_FILENAME, the root name of the quadrature files.
#
#    integer DEGREE_MAX, the maximum polynomial degree to check.
#
  import numpy as np

  print ( '' )
  print ( 'wedge_exactness():' )
  print ( '  Investigate the polynomial exactness of' )
  print ( '  a quadrature rule for the unit wedge.' )
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
  print ( 'wedge_exactness(): User input:' )
  print ( '  Quadrature rule X file = "' + quad_x_filename + '".' )
  print ( '  Quadrature rule W file = "' + quad_w_filename + '".' )
  print ( '  Maximum total degree to check = ', degree_max )
#
#  Read the X file.
#
  x = np.loadtxt ( quad_x_filename )
  order = x.shape[0]
  print ( '  Number of quadrature points = ', order )
#
#  Read the W file.
#
  w = np.loadtxt ( quad_w_filename )
#
#  Explore the monomials.
#
  print ( '' )
  print ( '    Exponents  Degree  Error ' )
  print ( '' )

  dim_num = 3
  expon = np.zeros ( dim_num, dtype = int )

  for degree in range ( 0, degree_max + 1 ):

    more = False
    h = 0
    t = 0

    while ( True ):

      expon, more, h, t = comp_next ( degree, dim_num, expon, more, h, t )

      v = monomial_value ( dim_num, order, expon, x )

      quad = wedge01_volume ( ) * np.dot ( w, v )

      exact = wedge01_integral ( expon )

      quad_error = np.abs ( quad - exact )

      print ( '  (%2d,%2d,%2d)  %2d  %24.16f' \
        % ( expon[0], expon[1], expon[2], degree, quad_error ) )

      if ( not more ):
        break

    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'wedge_exactness():' )
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
#      product ( 1 <= i <= d ) x(i)^e(i)
#
#    The combination 0.0^0, if encountered, is treated as 1.0.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 October 2021
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
        if ( x[i,j] == 0.0 ):
          v[i] = 0.0
        elif ( e[j] != 0 ):
          v[i] = v[i] * x[i,j] ** e[j]

  return v

def wedge01_integral ( e ):

#*****************************************************************************80
#
## wedge01_integral() returns the integral of a monomial in the unit wedge in 3D.
#
#  Discussion:
#
#    This routine returns the integral of
#
#      product ( 1 <= I <= 3 ) X(I)^E(I)
#
#    over the unit wedge.
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1
#      -1 <= Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2023
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
#    integer E(3), the exponents.
#
#  Output:
#
#    real VALUE, the integral of the monomial.
#
  value = 1.0

  k = e[0]

  for i in range ( 1, e[1] + 1 ):
    k = k + 1
    value = value * i / k

  k = k + 1
  value = value / k

  k = k + 1
  value = value / k
#
#  Now account for integration in Z.
#
  if ( e[2] == - 1 ):
    print ( '' )
    print ( 'wedge01_integral(): Fatal error!' )
    print ( '  E[2] = -1 is not a legal input.' )
    raise Exception ( 'wedge01_integral(): Fatal error!' )
  elif ( ( e[2] % 2 ) == 1 ):
    value = 0.0
  else:
    value = value * 2.0 / ( e[2] + 1 )

  return value

def wedge01_volume ( ):

#*****************************************************************************80
#
## wedge01_volume() returns the volume of the unit wedge in 3D.
#
#  Discussion:
#
#    The unit wedge is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1
#      -1 <= Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the volume of the unit wedge.
#
  value = 1.0

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
  wedge_exactness_test ( )
  timestamp ( )

