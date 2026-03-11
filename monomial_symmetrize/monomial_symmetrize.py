#! /usr/bin/env python3
#
def monomial_symmetrize_test ( ):

#*****************************************************************************80
#
## monomial_symmetrize_test() tests monomial_symmetrize().
#
#  Discussion:
#
#    This code implements a gather/scatter operation to symmetrize the coefficients
#    of equivalent monomials in a polynomial.
#
#    In particular, the code will see coefficients for the six equivalent monomials:
#      c123 x1 x2 x3
#      c132 x1 x3 x2
#      c213 x2 x1 x3
#      c231 x2 x3 x1
#      c312 x3 x1 x2
#      c321 x3 x2 x1
#    and compute cave, the average value of c123, c132, c213, c231, c312, c321,
#    and then overwrite the original coefficients by cave.
#
#    This is done separately for every set of equivalent monomials.
#
#    The monomials are assumed to all be of total degree D.
#
#    The number of distince variables x is assumed to be B.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Local:
#
#    integer d: the vector dimension.
#
#    integer b: vector entries range from 1 to b.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'monomial_symmetrize_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  monomial_symmetrize() symmetrizes the coefficients of equivalent' )
  print ( '  monomials, all of degree D, in B variables.' )
  
  for test in [ 1, 2 ]:

    if ( test == 1 ):
      b = 3
      d = 3
    elif ( test == 2 ):
      b = 4
      d = 3

    n = b**d

    print ( '' )
    print ( '  Test #', test )
    print ( '    b = ', b )
    print ( '    d = ', d )
    print ( '    n = ', n )
#
#  Create data vector C.
#
    c = demo_data ( d, b )
#
#  Report C.
#
    print ( '' )
    print ( '  Original data C:' )
    a = np.zeros ( n, dtype = int )
    more = False
    i = 0
  
    while ( True ):

      a, more = vector_lex_next ( d, b, a, more )

      if ( not more ):
        break

      print ( '  #%2d  C=%g, [ %d, %d, %d ]' \
        % ( i, c[i], a[0], a[1], a[2] ) )
      i = i + 1

    c2 = monomial_symmetrize ( d, b, c )
#
#  Report Symmetrized C.
#
    print ( '' )
    print ( '  Symmetric C:' )
    a = np.zeros ( n, dtype = int )
    more = False
    i = 0
  
    while ( True ):

      a, more = vector_lex_next ( d, b, a, more )

      if ( not more ):
        break

      print ( '  #%2d  C=%g, [ %d, %d, %d ]' \
        % ( i, c2[i], a[0], a[1], a[2] ) )
      i = i + 1
#
#  Terminate.
#
  print ( '' )
  print ( 'monomial_symmetrize_test():' )
  print ( '  Normal end of execution.' )

  return

def monomial_symmetrize ( d, b, c ):

#*****************************************************************************80
#
## monomial_symmetrize() symmetrizes the coefficients of equivalent monomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer d: the dimension.
#
#    integer b: the base.
#
#    real c(b^d): the coefficients.
#
#  Output:
#
#    real c2(b^d): the symmetrized coefficients.
#
  import numpy as np

  n = b**d
#
#  Use a sorted copy Z of vector A as a key.
#
  c2 = np.zeros ( n, dtype = float )
  z = np.zeros ( n, dtype = int )
  more = False
  j = 0

  print ( '' )
  print ( '  Data gathered to representatives and averaged:' )
  print ( '' )

  while ( True ):
#
#  Compute the next Z value.
#
    z, more = vector_representative_next ( d, b, z, more )

    if ( not more ):
      break
#
#  Generate all vectors A whose sorted value is Z.
#  Gather those C values into one vector C2.
#
    mult = 0
    a = z.copy ( )
    more2 = False
    while ( True ):
      mult = mult + 1
      i = vector_lex_rank ( d, b, a ) - 1
      c2[j] = c2[j] + c[i]
      a, more2 = vector_equivalent_next ( a )
      if ( not more2 ):
        break
#
#  Average C2 by number of contributors.
#
    c2[j] = c2[j] / mult

    print ( '  #%2d  mult=%d  C2=%g, [ %d, %d, %d ]' \
      % ( j, mult, c2[j], z[0], z[1], z[2] ) )
#
#  Scatter averaged value back to contributors.
#
    a = z.copy ( )
    more2 = False
    while ( True ):
      i = vector_lex_rank ( d, b, a )
      c[i-1] = c2[j]
      a, more2 = vector_equivalent_next ( a )
      if ( not more2 ):
        break

    j = j + 1

  return c

def demo_data ( d, b ):

#*****************************************************************************80
#
## demo_data() defines a data vector for the gather/scatter demo.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer d: the vector dimension.
#
#    integer b: vector entries range from 1 to b.
#
#  Output:
#
#    integer c(b^d): a data value for every unique d-dimensional vector
#    with entries from 1 to b.  Lexicographic order is assumed.
#
  import numpy as np

  n = b**d
  c = np.zeros ( n, dtype = float )
  f = np.arange ( d ) + 1
#
#  Generate each vector A, and compute the corresponding C.
#
  a = np.zeros ( n, dtype = int )
  more = False
  i = 0
  
  while ( True ):

    a, more = vector_lex_next ( d, b, a, more )

    if ( not more ):
      break

    c[i] = np.dot ( f, a )
    i = i + 1

  return c

def vector_lex_next ( d, b, a, more ):

#*****************************************************************************80
#
## vector_lex_next() generates vectors in lexicographic order.
#
#  Discussion:
#
#    The vectors are produced in lexical order, starting with
#    (1,1,...,1),
#    (1,1,...,2),
#    ...
#    (B,B,...,B).
#
#  Example:
#
#    d = 2,
#    b = 3
#
#    1   1
#    1   2
#    1   3
#    2   1
#    2   2
#    2   3
#    3   1
#    3   2
#    3   3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer d: the vector dimension.
#
#    integer b: vector entries range from 1 to b.
#
#    integer A(D): except on the first call, this should
#    be the output value of A on the last call.
#
#    logical MORE: should be FALSE on the first call, and
#    thereafter should be the output value of MORE from the previous call.  
#
#  Output:
#
#    integer A(D): the next vector.
#
#    logical MORE: is TRUE if another vector was computed.
#    If MORE is FALSE on return, then ignore the output value A, and
#    stop calling the routine.
#
  import numpy as np

  if ( not more ):

    a = np.ones ( d, dtype = int )
    more = True

  else:
      
    for i in range ( d - 1, -1, -1 ):

      a[i] = a[i] + 1

      if ( a[i] <= b ):
        return a, more

      a[i] = 1

    more = False

  return a, more

def vector_equivalent_next ( a ):

#*****************************************************************************80
#
## vector_equivalent_next() generates equivalent vectors one at a time.
#
#  Discussion:
#
#    Two vectors are equivalent if one is simply a permuted copy of the 
#    other.  A vector may have no equivalents, or many.
#    This function produces the "next" equivalent vector, so it can
#    produce all the equivalent vectors one at a time.  To do so,
#    start with the vector whose entries are sorted in ascending order.
#
#    For example, here is for vectors of length 3, with digits 1, 2 or 3,
#    the possible sequences are:
#
#      #1  1 1 1 --> 1 1 1
#      #2  1 1 2 --> 1 1 2, 1 2 1, 2 1 1
#      #3  1 1 3 --> 1 1 3, 1 3 1, 3 1 1
#      #4  1 2 2 --> 1 2 2, 2 1 2, 2 2 1
#      #5  1 2 3 --> 1 2 3, 1 3 2, 2 1 3, 2 3 1, 3 1 2, 3 2 1
#      #6  1 3 3 --> 1 3 3, 3 1 3, 3 3 1
#      #7  2 2 2 --> 2 2 2
#      #8  2 2 3 --> 2 2 3, 2 3 2, 3 2 2
#      #9  2 3 3 --> 2 3 3, 3 2 3, 3 3 2
#     #10  3 3 3 --> 3 3 3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer a(d): a vector in the sequence.
#
#  Output:
#
#    integer a(d): the next equivalent vector.  But if the sequence is
#    exhausted, a is returned as [].
#
#    logical MORE: is true if another vector was computed.
#    If MORE is false on return, then ignore the output value A, and
#    stop calling the routine.
#
  more = True

  n = len ( a )
#
#  Starting at the right, seek the highest index I for which A(I) < A(I+1).
#
  i = n - 2

  while ( True ):

    if ( i < 0 ):
      break

    if ( a[i] < a[i+1] ):
      break

    i = i - 1
#
#  If no I could be found, then we have reach the final permutation,
#  N, N-1, ..., 2, 1.  Time to start over again.
#
  if ( i == -1 ):
    a = []
    more = False
  else:
#
#  Otherwise, let J be the greatest index after I such that A(I) < A(J).
#
    j = n - 1
    while ( a[j] <= a[i] ): 
      j = j - 1
#
#  Interchange elements I and J.
#
    t    = a[i]
    a[i] = a[j]
    a[j] = t
#
#  Reverse the elements from I+1 to the end.
#  Boy this really shows how nonintuitive Python's index rules can be!
#
    a[i+1:] = a[:i:-1]

  return a, more

def vector_lex_rank ( d, b, a ):

#*****************************************************************************80
#
## vector_lex_rank() ranks a vector using lexicographic order.
#
#  Example:
#
#    d = 3,
#    b = 3
#    A = ( 2, 1, 3 )
#
#    RANK = 12
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer d: the vector dimension.
#
#    integer b, the upper limit for the array indices.
#
#    integer A(d), the vector to be ranked.
#
#  Output:
#
#    integer RANK, the rank of the index vector.
#
  for i in range ( 0, d ):
    if ( a[i] < 1 or b < a[i] ):
      raise Exception ( 'vector_lex_rank - a[] contains illegal values.' )

  rank = 1
  rang = 1
  for i in range ( d - 1, -1, -1 ):
    rank = rank + ( a[i] - 1 ) * rang
    rang = rang * b

  return rank

def vector_representative_next ( d, b, a, more ):

#*****************************************************************************80
#
## vector_representative_next() generates vector representatives one at a time.
#
#  Example:
#
#    d = 3
#    b = 3
#
#    1: 1  1  1
#    2: 1  1  2
#    3: 1  1  3
#    4: 1  2  2
#    5: 1  2  3
#    6: 1  3  3
#    7: 2  2  2
#    8: 2  2  3
#    9: 2  3  3
#   10: 3  3  3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer d: the vector dimension.
#
#    integer B, the base to be used.  B = 2 will
#    give vectors of 1's and 2's, for instance.
#
#    integer A(D), except on the first call, this should
#    be the output value of A on the last call.
#
#    logical MORE, should be false on the first call, and
#    thereafter should be the output value of MORE from the previous call.  
#
#  Output:
#
#    integer A(D), the next vector.
#
#    logical MORE: true if another vector was computed.
#    If MORE is false on return, then ignore the output value A, and
#    stop calling the routine.
#
  import numpy as np

  if ( not more ):

    a = np.ones ( d, dtype = int )
    more = True

  else:
      
    for i in range ( d - 1, -1, -1 ):

      a[i] = a[i] + 1

      if ( a[i] <= b ):
        for i2 in range ( i + 1, d ):
          a[i2] = a[i]
        return a, more

    more = False

  return a, more

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
  monomial_symmetrize_test ( )
  timestamp ( )

