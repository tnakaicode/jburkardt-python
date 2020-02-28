#! /usr/bin/env python
#
#! /usr/bin/env python
#
def ignuin ( low, high ):

#*****************************************************************************80
#
## IGNUIN generates a random integer in a given range.
#
#  Discussion:
#
#    Each deviate K satisfies LOW <= K <= HIGH.
#
#    If (HIGH-LOW) > 2,147,483,561, this procedure prints an error message
#    and stops the program.
#
#    IGNLGI generates integers between 1 and 2147483562.
#
#    MAXNUM is 1 less than the maximum generatable value.
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
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, integer LOW, HIGH, the lower and upper bounds.
#
#    Output, integer VALUE, a random deviate from
#    the distribution.
#
  from i4_uni import i4_uni
  from sys import exit

  maxnum = 2147483561

  high = int ( high )
  low = int ( low )

  if ( high < low ):
    print ( ' ' )
    print ( 'IGNUIN - Fatal error!' )
    print ( '  HIGH < LOW.' )
    exit ( 'IGNUIN - Fatal error!' )

  width = high - low

  if ( maxnum < width ):
    print ( ' ' )
    print ( 'IGNUIN - Fatal error!' )
    print ( '  Range HIGH-LOW is too large.' )
    exit ( 'IGNUIN - Fatal error!' )

  if ( low == high ):
    value = low
    return value

  ranp1 = width + 1
  maxnow = ( maxnum / ranp1 ) * ranp1

  while ( True ):

    ign = i4_uni ( ) - 1

    if ( ign <= maxnow ):
      break

  value = int ( low + ( ign % ranp1 ) )

  return value

def ignuin_test ( phrase ):

#*****************************************************************************80
#
## IGNUIN_TEST tests IGNUIN.
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
  import platform
  from genunf import genunf
  from initialize import initialize
  from phrtsd import phrtsd
  from set_initial_seed import set_initial_seed

  print ( '' )
  print ( 'IGNUIN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  IGNUIN generates uniformly distributed integers in a range.' )
#
#  Initialize the generators.
#
  initialize ( )
#
#  Set the seeds based on the phrase.
#
  seed1, seed2 = phrtsd ( phrase )
#
#  Initialize all generators.
#
  set_initial_seed ( seed1, seed2 )

  a = -1000.0
  b = +1000.0
  low = int ( genunf ( a, b ) )

  a = low + 10.0
  b = a + 1000.0
  high = int ( genunf ( a, b ) )

  n = 10

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '' )
  print ( '  Parameters:' )
  print ( '' )
  print ( '  LOW  = %d' % ( low ) )
  print ( '  HIGH = %d' % ( high ) )

  print ( '' )
  for test in range ( 0, n ):
    x = ignuin ( low, high )
    print ( '  %d' % ( x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'IGNUIN_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrase = 'Randomizer'
  ignuin_test ( phrase )
  timestamp ( )

