#! /usr/bin/env python
#
def bal_seq_enum ( n ):

#*****************************************************************************80
#
## BAL_SEQ_ENUM enumerates the balanced sequences.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 November 2015
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
#    N must be nonnegative.
#
#    Output, integer NSEQ, the number of balanced sequences.
#
  from i4_choose import i4_choose

  nseq = i4_choose ( 2 * n, n ) / ( n + 1 )

  return nseq

def bal_seq_enum_test ( ):

#*****************************************************************************80
#
## BAL_SEQ_ENUM_TEST tests BAL_SEQ_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BAL_SEQ_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BAL_SEQ_ENUM enumerates balanced sequences of N terms.' )
  print ( '' )
  print ( '   N       #' )
  print ( '' )

  for n in range ( 0, 11 ):
    nseq = bal_seq_enum ( n )
    print ( '  %2d  %6d' % ( n, nseq ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BAL_SEQ_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bal_seq_enum_test ( )
  timestamp ( )
 
