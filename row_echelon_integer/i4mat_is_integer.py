#! /usr/bin/env python
#
def i4mat_is_integer ( m, n, a ):

#*****************************************************************************80
#
## I4MAT_IS_INTEGER is TRUE if all entries of an I4MAT are integer.
#
#  Discussion:
#
#    An I4MAT is an MxN array of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer A(M,N), the array.
#
#    Output, logical VALUE, is true if all entries are integer.
#
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( a[i,j] != round ( a[i,j] ) ):
        return False

  return True

def i4mat_is_integer_test ( ):

#*****************************************************************************80
#
## I4MAT_IS_INTEGER_TEST tests I4MAT_IS_INTEGER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4MAT_IS_INTEGER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_IS_INTEGER is TRUE if every entry of an I4MAT' )
  print ( '  is an integer.' )

  print ( '' )
  print ( '  Example 1: Obviously integer:' )
  print ( '' )
  m = 2
  n = 3
  a = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 6 ] ] )
  print ( a )
  if ( i4mat_is_integer ( m, n, a ) ):
    print ( '  A is an integer matrix.' )
  else:
    print ( '  A is NOT an integer matrix.' )

  print ( '' )
  print ( '  Example 2: Obviously NOT integer:' )
  print ( '' )
  m = 2
  n = 3
  a = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 6.5 ] ] )
  print ( a )
  if ( i4mat_is_integer ( m, n, a ) ):
    print ( '  A is an integer matrix.' )
  else:
    print ( '  A is NOT an integer matrix.' )

  print ( '' )
  print ( '  Example 3: Not Integer, Not obvious:' )
  print ( '' )
  m = 2
  n = 3
  a = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5.000000001, 6 ] ] )
  print ( a )
  if ( i4mat_is_integer ( m, n, a ) ):
    print ( '  A is an integer matrix.' )
  else:
    print ( '  A is NOT an integer matrix.' )

  print ( '' )
  print ( '  Example 4: Not Integer, Not obvious:' )
  print ( '' )
  m = 2
  n = 3
  a = np.array ( [ \
    [ 1.0, 2, 300000000.2 ], \
    [ 4, 5, 6 ] ] )
  print ( a )
  if ( i4mat_is_integer ( m, n, a ) ):
    print ( '  A is an integer matrix.' )
  else:
    print ( '  A is NOT an integer matrix.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_IS_INTEGER_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_is_integer_test ( )
  timestamp ( )
