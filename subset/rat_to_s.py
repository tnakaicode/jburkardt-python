#! /usr/bin/env python
#
def rat_to_s ( a, b ):

#*****************************************************************************80
#
## RAT_TO_S returns a left-justified representation of A/B.
#
#  Discussion:
#
#    If the ratio is negative, a minus sign precedes A.
#    A slash separates A and B.
#
#    Note that if A is nonzero and B is 0, S will
#    be returned as "Inf" or "-Inf" (Infinity), and if both
#    A and B are zero, S will be returned as "NaN"
#    (Not-a-Number).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, B, the numerator and denominator.
#
#    Output, character S(*), a left-justified string
#    containing the representation of A/B.
#

#
#  Take care of simple cases right away.
#
  if ( a == 0 ):

    if ( b != 0 ):
      s = '0'
    else:
      s = 'NaN'

  elif ( b == 0 ):

    if ( 0 < a ):
      s = 'Inf'
    else:
      s = '-Inf'

  else:

    s = str ( a ) + '/' + str ( b )

  return s

def rat_to_s_test ( ):

#*****************************************************************************80
#
#% RAT_TO_S_TEST tests RAT_TO_S.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'RAT_TO_S_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RAT_TO_S converts a rational to a string.' )

  rat_num = 7
  rat_top = np.array ( [ 3, 1,    20,  8, -10,   9, -11 ] )
  rat_bot = np.array ( [ 4, 1000,  1,  4,   7, -15, -11 ] )

  print ( '' )
  print ( '           A           B    A/B' )
  print ( '' )

  for i in range ( 0, rat_num ):
    a = rat_top[i]
    b = rat_bot[i]
    s = rat_to_s ( a, b )
    print ( '  %10d  %10d    %s' % ( a, b, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RAT_TO_S_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rat_to_s_test ( )
  timestamp ( )

