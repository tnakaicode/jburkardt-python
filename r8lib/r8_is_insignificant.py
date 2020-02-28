#! /usr/bin/env python3
#
def r8_is_insignificant ( r, s ):

#*****************************************************************************80
#
## R8_IS_INSIGNIFICANT determines if an R8 is insignificant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the number to be compared against.
#
#    Input, real S, the number to be compared.
#
#    Output, logical VALUE, is TRUE if S is insignificant
#    compared to R.
#
  value = True
  r8_epsilon = 2.220446049250313E-016

  t = r + s
  tol = r8_epsilon * abs ( r )

  if ( tol < abs ( r - t ) ):
    value = False
  
  return value

def r8_is_insignificant_test ( ):

#*****************************************************************************80
#
## R8_IS_INSIGNIFICANT_TEST tests R8_IS_INSIGNIFICANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 November 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8_IS_INSIGNIFICANT_TEST:' )
  print ( '  R8_IS_INSIGNIFICANT ( R, S ) is TRUE is S is insignificant' )
  print ( '  compared to R.' )

  r8_epsilon = 2.220446049250313E-016
  r8_huge = 1.0E+30
  r8_one = 1.0
  r8_tiny = 1.0E-30

  print ( '' )
  print ( '               R               S  Insignificant?' )
  print ( '' )

  r = r8_tiny
  s = r8_tiny
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = r8_epsilon
  s = r8_tiny
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = r8_one
  s = r8_tiny
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = r8_huge
  s = r8_tiny
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  print ( '' )

  r = r8_tiny
  s = r8_epsilon
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = r8_epsilon
  s = r8_epsilon
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = r8_one
  s = r8_epsilon
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = r8_huge
  s = r8_epsilon
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  print ( '' )

  r = r8_tiny
  s = r8_one
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = r8_epsilon
  s = r8_one
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = r8_one
  s = r8_one
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = r8_huge
  s = r8_one
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  print ( '' )

  r = r8_tiny
  s = r8_huge
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = r8_epsilon
  s = r8_huge
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = r8_one
  s = r8_huge
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )

  r = r8_huge
  s = r8_huge
  t = r8_is_insignificant ( r, s )
  print ( '  %14.6g  %14.6g  %s' % ( r, s, t ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_IS_INSIGNIFICANT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_is_insignificant_test ( )
  timestamp ( )
