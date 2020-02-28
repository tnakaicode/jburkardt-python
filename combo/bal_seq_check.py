#! /usr/bin/env python
#
def bal_seq_check ( n, t ):

#*****************************************************************************80
#
## BAL_SEQ_CHECK checks a balanced sequence.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N, the number of 0's (and 1's) in the sequence.
#    N must be positive.
#
#    Input, integer T(2*N), a balanced sequence.
#
#    Output, bool CHECK, error flag.
#    TRUE, T is a legal balanced sequence.
#    FALSE, T is not a legal balanced sequence.
#
  check = True

  if ( n < 1 ):
    check = False
    return check

  one_count = 0
  zero_count = 0

  for i in range ( 0, 2 * n ):

    if ( t[i] == 0 ):
      zero_count = zero_count + 1
    elif ( t[i] == 1 ):
      one_count = one_count + 1
    else:
      check = False
      return check

    if ( zero_count < one_count ):
      check = False
      return check

  if ( one_count != zero_count ):
    check = False

  return check

def bal_seq_check_test ( ):

#*****************************************************************************80
#
## BAL_SEQ_CHECK_TEST tests BAL_SEQ_CHECK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'BAL_SEQ_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BAL_SEQ_CHECK checks N and T(1:2*N).' )
  print ( '' )
  print ( '  Check?   N    T(1:2*N)' )
  print ( '' )
  
  for test in range ( 1, 4 ):

    n = 5

    if ( test == 1 ):
      t = np.array ( [ 0, 0, 1, 0, 1, 0, 0, 1, 1, 1 ] )
    elif ( test == 2 ):
      t = np.array ( [ 1, 1, 0, 1, 0, 1, 1, 0, 0, 0 ] )
    elif ( test == 3 ):
      t = np.array ( [ 0, 0, 1, 0, 1, 0, 0, 1, 0, 1 ] )

    check = bal_seq_check ( n, t )

    print ( '      %2d  %2d' % ( check, n ), end = '' )
    i4vec_transpose_print ( n, t, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'BAL_SEQ_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bal_seq_check_test ( )
  timestamp ( )
 
