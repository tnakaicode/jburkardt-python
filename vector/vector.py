#! /usr/bin/env python3
#
def vector_test ( ):

#*****************************************************************************80
#
## vector_test() tests vector().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'vector_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test vector()' )

  rng = default_rng ( )

  vector_multiplicity_test ( )
  vector_random_test ( rng )

  vector_lex_next_test ( )
  vector_lex_rank_test ( )
  vector_lex_unrank_test ( )

  monotone_vector_next_test ( )
  monotone_vector_random_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'vector_test():' )
  print ( '  Normal end of execution.' )

  return

def monotone_vector_from_vector ( a ):

#*****************************************************************************80
#
## monotone_vector_from_vector() returns the monotone vector corresponding to a vector.
#
#  Example:
#
#    1 1 1 --> 1 1 1  #1  1
#    1 1 2 --> 1 1 2  #2  3
#    1 1 3 --> 1 1 3  #3  3
#    1 2 1 --> 1 1 2  #2  3
#    1 2 2 --> 1 2 2  #4  3
#    1 2 3 --> 1 2 3  #5  6
#    1 3 1 --> 1 1 3  #3  3
#    1 3 2 --> 1 2 3  #5  6
#    1 3 3 --> 1 3 3  #6  3
#    2 1 1 --> 1 1 2  #2  3
#    2 1 2 --> 1 2 2  #4  3
#    2 1 3 --> 1 2 3  #5  6
#    2 2 1 --> 1 2 2  #4  3
#    2 2 2 --> 2 2 2  #7  1
#    2 2 3 --> 2 2 3  #8  3
#    2 3 1 --> 1 2 3  #5  6
#    2 3 2 --> 2 2 3  #8  3
#    2 3 3 --> 2 3 3  #9  3
#    3 1 1 --> 1 1 3  #3  3
#    3 1 2 --> 1 2 3  #5  6
#    3 1 3 --> 1 3 3  #6  3
#    3 2 1 --> 1 2 3  #5  6
#    3 2 2 --> 2 2 3  #8  3
#    3 2 3 --> 2 3 3  #9  3
#    3 3 1 --> 1 3 3  #6  3
#    3 3 2 --> 2 3 3  #9  3
#    3 3 3 --> 3 3 3 #10  1
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
#    integer a(d): a given vector, with digits between 1 and b.
#
#  Output:
#
#    integer z(d): the monotone vector corresponding to a vector.
#
  import numpy as np

  z = np.sort ( a )

  return z

def monotone_vector_next ( d, b, a, more ):

#*****************************************************************************80
#
## monotone_vector_next() generates monotone vectors in lex order.
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
#    integer B, the base to be used.  B = 2 will
#    give vectors of 1's and 2's, for instance.
#
#    integer A(D), except on the first call, this should
#    be the output value of A on the last call.
#
#    logical MORE, should be FALSE on the first call, and
#    thereafter should be the output value of MORE from the previous call.  
#
#  Output:
#
#    integer A(D), the next monotone vector.
#
#    logical MORE, is TRUE if another vector was computed.
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
        for i2 in range ( i + 1, d ):
          a[i2] = a[i]
        return a, more

    more = False

  return a, more

def monotone_vector_next_test ( ):

#*****************************************************************************80
#
## monotone_vector_next_test() tests monotone_vector_next().
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
  import numpy as np

  d = 3
  b = 3
  more = False
  print ( '' )
  print ( 'monotone_vector_next_test():' )
  print ( '  monotone_vector_next() generates monotonically increasing integer' )
  print ( '  vectors of length D, with entries between 1 and B,' )
  print ( '  in lexicographic order.' )
  print ( '' )
  print ( '  The dimension d =', d )
  print ( '  The base b =     ', b )
  print ( '' )
  
  a = np.empty ( d )
  i = 0
  
  while ( True ):

    a, more = monotone_vector_next ( d, b, a, more )

    if ( not more ):
      break

    i = i + 1
    print ( '  #%d:  ' % ( i ), end = '' )
    print ( a )

  return

def monotone_vector_random ( d, b, rng ):

#*****************************************************************************80
#
## monotone_vector_random() generates a random monotone vector.
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
#    integer B, the base to be used.  B = 2 will
#    give vectors of 1's and 2's, for instance.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(D), the random monotone vector.
#
  import numpy as np

  a = np.zeros ( d, dtype = int )
  a[0] = rng.integers ( low = 1, high = b, endpoint = True )
  for i in range ( 1, d ):
    a[i] = rng.integers ( low = a[i-1], high = b, endpoint = True )

  return a

def monotone_vector_random_test ( rng ):

#*****************************************************************************80
#
## monotone_vector_random_test() tests monotone_vector_random().
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
#    rng(): the current random number generator.
#
  d = 3
  b = 3

  print ( '' )
  print ( 'monotone_vector_random_test():' )
  print ( '  monotone_vector_random() generates random monotone integer' )
  print ( '  vectors of length D with entries between 1 and B.' )
  print ( '' )
  print ( '  The dimension d =', d )
  print ( '  The base b =     ', b )
  print ( '' )
   
  for k in range ( 0, 10 ):

    a = monotone_vector_random ( d, b, rng )
    print ( '  #%d  :  ' % ( k ), end = '' )
    print ( a )

  return

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

def vector_lex_next_test ( ):

#*****************************************************************************80
#
## vector_lex_next_test() tests vector_lex_next().
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
  import numpy as np

  d = 3
  b = 3
  more = False
  print ( '' )
  print ( 'vector_lex_next_test():' )
  print ( '  vector_lex_next() generates integer vectors of length D' )
  print ( '  with entries between 1 and B, in lexicographic order.' )
  print ( '' )
  print ( '  The dimension d =', d )
  print ( '  The base b =     ', b )
  print ( '' )
  
  a = np.empty ( d )
  i = 0
  
  while ( True ):

    a, more = vector_lex_next ( d, b, a, more )

    if ( not more ):
      break

    i = i + 1
    print ( '  #%d:  ' % ( i ), end = '' )
    print ( a )

  return

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

def vector_lex_rank_test ( ):

#*****************************************************************************80
#
## vector_lex_rank_test() tests vector_lex_rank().
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
  import numpy as np

  d = 3
  b = 3
  more = False
  print ( '' )
  print ( 'vector_lex_rank_test():' )
  print ( '  vector_lex_rank() ranks an integer vectors o length D' )
  print ( '  with entries between 1 and B.' )
  print ( '' )
  print ( '  The dimension d =', d )
  print ( '  The base b =     ', b )
  print ( '' )
  
  a = np.empty ( d )
  i = 0
  
  while ( True ):

    a, more = vector_lex_next ( d, b, a, more )

    if ( not more ):
      break

    i = i + 1
    print ( '  %d:  ' % ( i ), end = '' )
    print ( a )
    r = vector_lex_rank ( d, b, a )
    print ( '  Computed rank is', r )

  return

def vector_lex_unrank ( d, b, rank ):

#*****************************************************************************80
#
## vector_lex_unrank() unranks a vector using lexicographic order.
#
#  Example:
#
#    d = 3,
#    b = 3
#    RANK = 12
#
#    A = ( 2, 1, 3 )
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
#    The lower limit is 1.
#
#    integer RANK, the rank of the desired index vector.
#
#  Output:
#
#    integer A(d), the index vector of the given rank.
#
  import numpy as np
#
#  The rank might be too small.
#
  if ( rank < 1 ):
    raise Exception ( 'vec_lex_unrank: The rank is less than 1.' )

  rang = b**d
#
#  The rank might be too large.
#
  if ( rang < rank ):
    raise Exception ( 'vec_lex_unrank: The rank is more than b**d.' )

  a = np.zeros ( d, dtype = int )

  k = rank - 1
  for i in range ( 0, d ):
    rang = int ( np.floor ( rang / b ) )
    j = int ( np.floor ( k / rang ) )
    a[i] = j + 1
    k = k - j * rang

  return a

def vector_lex_unrank_test ( ):

#*****************************************************************************80
#
## vector_lex_unrank_test() tests vector_lex_unrank().
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
  d = 3
  b = 3
  more = False
  print ( '' )
  print ( 'vector_lex_unrank_test():' )
  print ( '  vector_lex_unrank() unranks an integer vector of length D' )
  print ( '  with entries between 1 and B.' )
  print ( '' )
  print ( '  The dimension d =', d )
  print ( '  The base b =     ', b )
  print ( '' )
  
  rang = b**d
  for rank in range ( 1, rang + 1 ):

    a = vector_lex_unrank ( d, b, rank )
    print ( '  %d:  ' % ( rank ), end = '' )
    print ( a )

  return

def vector_multiplicity ( a ):

#*****************************************************************************80
#
## vector_multiplicity() computes the multiplicity of a vector.
#
#  Example:
#
#         A        mult
#    -----------   ----
#    ( 7, 7, 7 )     1
#    ( 5, 0, 5 )     3
#    ( 2, 1, 3 )     6
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
#    integer a(d): the vector.
#
#  Output:
#
#    integer mult: the multiplicity of the vector.
#
  import numpy as np

  d = len ( a )

  z = np.sort ( a )

  div = 1
  mult = 1
  for i in range ( 1, d ):
    mult = mult * ( i + 1 )
    if ( z[i] == z[i-1] ):
      div = div + 1
    else:
      div = 1
    mult = mult // div

  return mult

def vector_multiplicity_test ( ):

#*****************************************************************************80
#
## vector_multiplicity_test() tests vector_multiplicity().
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
  import numpy as np

  print ( '' )
  print ( 'vector_multiplicity_test():' )
  print ( '  vector_multiplicity() finds the multiplicity of an integer' )
  print ( '  vector.' )

  d = 3
  b = 3
  more = False
  print ( '' )
  print ( '  The dimension d =', d )
  print ( '  The base b =     ', b )
  print ( '' )
  
  a = np.empty ( d )
  i = 0
  
  while ( True ):

    a, more = vector_lex_next ( d, b, a, more )

    if ( not more ):
      break

    mult = vector_multiplicity ( a )

    i = i + 1
    print ( '  %2d  %d: [ %d, %d, %d ]' % ( i, mult, a[0], a[1], a[2] ) )

  return

def vector_next_equivalent ( a ):

#*****************************************************************************80
#
## vector_next_equivalent() generates the next equivalent vector.
#
#  Discussion:
#
#    Two vectors are equivalent if one is simply a permuted copy of the 
#    other.  A vector may have no equivalents, or many.
#    This function produces the "next" equivalent vector, so it can
#    produce all the equivalent vectors one at a time.  To do so,
#    start with the vector whose entries are sorted in ascending order.
#
#    For example, here is for vectors of length d = 3, with digits 1, 2 or 3,
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
#    01 December 2022
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
#    logical MORE: is TRUE if another vector was computed.
#    If MORE is FALSE on return, then ignore the output value A, and
#    stop calling the routine.
#
  import numpy as np

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
    a = np.empty ( d )
    more = False
  else:
#
#  Otherwise, let J be the greatest index after I such that A(I) < A(J).
#
    j = n - 1
    while ( a[j] <= a[i] ) :
      j = j - 1
#
#  Interchange elements I and J.
#
    t    = a[i]
    a[i] = a[j]
    a[j] = t
#
#  Reverse the elements from I+1 to N.
#
    a[i+1:n] = np.flip ( a[i+1:n] )

  return a, more

def vector_next_equivalent_test ( ):

#*****************************************************************************80
#
## vector_next_equivalent_test() tests vector_next_equivalent().
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
  import numpy as np

  print ( '' )
  print ( 'vector_next_equivalent_test():' )
  print ( '  vector_next_equivalent() finds vector equivalents.' )

  d = 3
  b = 3
  more = False
  print ( '' )
  print ( '  The dimension d =', d )
  print ( '  The base b =     ', b )
  print ( '' )
  
  a = np.empty ( d )
  i = 0
  
  while ( True ):

    a, more = vector_next ( d, b, a, more )

    if ( not more ):
      break

    mult = vector_multiplicity ( d, b, a )

    i = i + 1
    print ( '' )
    print ( '  %2d  %d: [ %d, %d, %d ]' % ( i, mult, a[0], a[1], a[2] ) )
#
#  Generate the equivalence sequence for A.
#
    a2 = np.sort ( a )
    j = 0

    while ( True ):

      print ( '  %2d: [ %d, %d, %d ]', j, a2 )
      j = j + 1
      a2, more2 = vector_next_equivalent_new ( a2 )
      if ( not more2 ):
        break

  return

def vector_random ( d, b, rng ):

#*****************************************************************************80
#
## vector_random() generates a random vector.
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
#    integer B, the base to be used.  B = 2 will
#    give vectors of 1's and 2's, for instance.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(D), the random vector.
#
  a = rng.integers ( low = 1, high = b, size = d, endpoint = True )

  return a

def vector_random_test ( rng ):

#*****************************************************************************80
#
## vector_random_test() tests vector_random().
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
#    rng(): the current random number generator.
#
  d = 3
  b = 3

  print ( '' )
  print ( 'vector_random_test():' )
  print ( '  vector_random() generates random integer vectors of length D' )
  print ( '  with entries between 1 and B.' )
  print ( '' )
  print ( '  The dimension d =', d )
  print ( '  The base b =     ', b )
  print ( '' )
   
  for k in range ( 0, 10 ):

    a = vector_random ( d, b, rng )
    print ( '  %d:  ' % ( k ), end = '' )
    print ( a )

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

if ( __name__ == '__main__' ):
  timestamp ( )
  vector_test ( )
  timestamp ( )

