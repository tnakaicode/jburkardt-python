#! /usr/bin/env python
#
def archimedes ( ):

#*****************************************************************************80
#
## ARCHIMEDES returns the 7 by 8 ARCHIMEDES matrix.
#
#  Formula:
#
#      6   -5    0   -6    0    0    0    0
#      0   20   -9  -20    0    0    0    0
#    -13    0   42  -42    0    0    0    0
#      0   -7    0    0   12   -7    0    0
#      0    0   -9    0    0   20   -9    0
#      0    0    0  -11    0    0   30  -11
#    -13    0    0    0  -13    0    0   42
#
#  Discussion:
#
#    "The sun god had a herd of cattle, consisting of bulls and cows,
#    one part of which was white, a second black, a third spotted, and
#    a fourth brown.  Among the bulls, the number of white ones was
#    one half plus one third the number of the black greater than
#    the brown; the number of the black, one quarter plus one fifth
#    the number of the spotted greater than the brown; the number of
#    the spotted, one sixth and one seventh the number of the white
#    greater than the brown.  Among the cows, the number of white ones
#    was one third plus one quarter of the total black cattle; the number
#    of the black, one quarter plus one fifth the total of the spotted
#    cattle; the number of spotted, one fifth plus one sixth the total
#    of the brown cattle; the number of the brown, one sixth plus one
#    seventh the total of the white cattle.  What was the composition
#    of the herd?"
#
#    The 7 relations involving the 8 numbers W, X, Y, Z, w, x, y, z,
#    have the form:
#
#      W = ( 5/ 6) *   X + Z
#      X = ( 9/20) *   Y + Z
#      Y = (13/42) *   W + Z
#      w = ( 7/12) * ( X + x )
#      x = ( 9/20) * ( Y + y )
#      y = (11/30) * ( Z + z )
#      z = (13/42) * ( W + w )
#
#    These equations may be multiplied through to an integral form
#    that is embodied in the above matrix.
#
#    A more complicated second part of the problem imposes additional
#    constraints (W+X must be square, Y+Z must be a triangular number).
#
#  Properties:
#
#    A is integral: int ( A ) = A.
#
#    A has full row rank.
#
#    It is desired to know a solution X in positive integers of
#
#      A * X = 0.
#
#    The null space of A is spanned by multiples of the null vector:
#
#      [ 10,366,482 ]
#      [  7,460,514 ]
#      [  7,358,060 ]
#      [  4,149,387 ]
#      [  7,206,360 ]
#      [  4,893,246 ]
#      [  3,515,820 ]
#      [  5,439,213 ]
#
#    and this is the smallest positive integer solution of the
#    equation A * X = 0.
#
#    Thus, for the "simple" part of Archimedes's problem, the total number
#    of cattle of the Sun is 50,389,082.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1998.
#
#  Parameters:
#
#    Output, integer A(7,8), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
   [   6, -5,  0,  -6,   0,  0,  0,   0 ], \
   [   0, 20, -9, -20,   0,  0,  0,   0 ], \
   [ -13,  0, 42, -42,   0,  0,  0,   0 ], \
   [   0, -7,  0,   0,  12, -7,  0,   0 ], \
   [   0,  0, -9,   0,   0, 20, -9,   0 ], \
   [   0,  0,  0, -11,   0,  0, 30, -11 ], \
   [ -13,  0,  0,   0, -13,  0,  0,  42 ] ] )

  return a

def archimedes_null_right ( ):

#*****************************************************************************80
#
## ARCHIMEDES_NULL_RIGHT returns a right null vector for the ARCHIMEDES matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real X(8), a right null vector.
#
  import numpy as np

  x = np.array ( [  \
    [ 10366482.0 ], \
    [  7460514.0 ], \
    [  7358060.0 ], \
    [  4149387.0 ], \
    [  7206360.0 ], \
    [  4893246.0 ], \
    [  3515820.0 ], \
    [  5439213.0 ] ] )

  return x

def archimedes_test ( ):

#*****************************************************************************80
#
## ARCHIMEDES_TEST tests ARCHIMEDES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'ARCHIMEDES_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ARCHIMEDES computes the ARCHIMEDES matrix.' )

  m = 7
  n = 8
  a = archimedes ( )
  r8mat_print ( m, n, a, '  ARCHIMEDES matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ARCHIMEDES_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  archimedes_test ( )
  timestamp ( )
