#! /usr/bin/env python3
#
def r8_is_inf ( r ):

#*****************************************************************************80
#
## R8_IS_INF determines if an R8 represents an infinite value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the number to be checked.
#
#    Output, bool VALUE, is TRUE if R is an infinite value.
#
  value = ( r == - float ( 'inf' ) or r == float ( 'inf' ) )

  return value

def r8_is_inf_test ( ):

#*****************************************************************************80
#
## R8_IS_INF_TEST tests R8_IS_INF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8_IS_INF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_IS_INF reports whether an R8 is infinite.' )
  print ( '' )
  print ( '  These tests are wasted, since all the arithmetic' )
  print ( '  operations return run time errors.' )
  print ( '' )

  r8 = 1.0
  print ( '  R8_IS_INF(1.0) = %s' % ( r8_is_inf ( r8 ) ) )

  if ( True ):
    print ( '  In Python, 1.0/0.0 causes a run time error!' )
  else:
    r1 = 1.0
    r2 = 0.0
    r8 = r1 / r2
    print ( '  R8_IS_INF(1.0/0.0) = %s' % ( r8_is_inf ( r8 ) ) )

  if ( True ):
    print ( '  In Python, 0.0/0.0 causes a run time error!' )
  else:
    r1 = 0.0
    r2 = 0.0
    r8 = r1 / r2
    print ( '  R8_IS_INF(0.0/0.0) = %s' % ( r8_is_inf ( r8 ) ) )
  
  r1 = 0.0
  r2 = 0.0
  r8 = r1 ** r2
  print ( '  R8_IS_INF(0^0) = %s' % ( r8_is_inf ( r8 ) ) )

  if ( True ):
    print ( '  In Python, arccos(-2.0) causes a run time error!' )
  else:
    r1 = -2.0
    r8 = np.arccos ( r1 )
    print ( '  R8_IS_INF(acos(-2)) = %s' % ( r8_is_inf ( r8 ) ) )

  if ( True ):
    print ( '  In Python, exp(1000) causes a run time overflow warning!' )
  else:
    r1 = 1000.0
    r8 = np.exp ( r1 )
    print ( '  R8_IS_INF(exp(1000)) = %s' % ( r8_is_inf ( r8 ) ) )

  if ( True ):
    print ( '  In Python, log(0) causes a run time error!' )
  else:
    r1 = 0.0
    r8 = np.log ( r1 )
    print ( '  R8_IS_INF(log(0)) = %s' % ( r8_is_inf ( r8 ) ) )

  if ( True ):
    print ( '  In Python, sqrt(-1) causes a run time error!' )
  else:
    r1 = -1.0
    r8 = np.sqrt ( r1 )
    print ( '  R8_IS_INF(sqrt(-1)) = %s' % ( r8_is_inf ( r8 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_IS_INF_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_is_inf_test ( )
  timestamp ( )
 
