#! /usr/bin/env python
#
def r8vec_bracket5 ( nd, xd, xi ):

#*****************************************************************************80
#
## R8VEC_BRACKET5 brackets data between successive entries of a sorted R8VEC.
#
#  Discussion:
#
#    We assume XD is sorted.
#
#    If XI is contained in the interval [XD(1),XD(N)], then the returned 
#    value B indicates that XI is contained in [ XD(B), XD(B+1) ].
#
#    If XI is not contained in the interval [XD(1),XD(N)], then B = -1.
#
#    This code implements a version of binary search which is perhaps more
#    understandable than the usual ones.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ND, the number of data values.
#
#    Input, real XD(N), the sorted data.
#
#    Input, real XD, the query value.
#
#    Output, integer B, the bracket information.
#
  import numpy as np

  if ( xi < xd[0] or xd[nd-1] < xi ):

    b = -1

  else:

    l = 0
    r = nd - 1

    while ( l + 1 < r ):
      m = int ( ( l + r ) / 2 )
      if ( xi < xd[m] ):
        r = m
      else:
        l = m

    b = l

  return b

def r8vec_bracket5_test ( ):

#*****************************************************************************80
#
## R8VEC_BRACKET5_TEST tests R8VEC_BRACKET5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  n = 10
  test_num = 6;

  xtest = np.array ( [ -10.0, 1.0, 4.5, 5.0, 10.0, 12.0 ] )

  print ( '' )
  print ( 'R8VEC_BRACKET5_TEST' )
  print ( '  R8VEC_BRACKET5 finds a pair of entries in a' )
  print ( '  sorted R8VEC which bracket a value.' )

  x = r8vec_indicator1 ( n )
  x[5] = x[4]

  r8vec_print ( n, x, '  Sorted array:' )

  print ( '' )
  print ( '        LEFT                   RIGHT' )
  print ( '      X(LEFT)       XVAL     X(RIGHT)' )

  for test in range ( 0, test_num ):

    xval = xtest[test]
    left = r8vec_bracket5 ( n, x, xval )

    print ( '' )
    if ( left == -1 ):
      print ( '  %10d' % ( left ) )
      print ( '              %10.4f  (Not bracketed!)' % ( xval ) )
    else:
      right = left + 1
      print ( '  %10d              %10d' % ( left, right ) )
      print ( '  %10.4f  %10.4f  %10.4f' % ( x[left], xval, x[right] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_BRACKET5_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8vec_bracket5_test ( )
  timestamp ( )
