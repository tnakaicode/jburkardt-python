#! /usr/bin/env python
#
def p00_prob_num ( ):

#*****************************************************************************80
#
## P00_PROB_NUM returns the number of problems.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer VALUE, the number of problems.
#
  value = 8

  return value

def p00_prob_num_test ( ):

#*****************************************************************************80
#
## P00_PROB_NUM_TEST tests P00_PROB_NUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'P00_PROB_NUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_PROB_NUM returns the number of test problems.' )

  num = p00_prob_num ( )
  print ( '' )
  print ( '  TEST_INTERP_1D includes %d test problems.' % ( num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_PROB_NUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  p00_prob_num_test ( )
  timestamp ( )


