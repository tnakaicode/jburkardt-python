#! /usr/bin/env python
#
def phrtsd ( phrase ):

#*****************************************************************************80
#
## PHRTSD converts a phrase to a pair of random number generator seeds.
#
#  Discussion:
#
#    This procedure uses a character string to generate two seeds for the RGN
#    random number generator.
#
#    Trailing blanks are eliminated before the seeds are generated.
#
#    Generated seed values will fall in the range 1 to 2^30 = 1,073,741,824.
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
#    Input, string PHRASE, a phrase to be used for the random number generation.
#
#    Output, integer SEED1, SEED2, the two seeds for the
#    random number generator, based on PHRASE.
#
  import numpy as np
  from lennob import lennob

  table = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#@#$#^...*()_+[]:''"<>?,./'

  twop30 = 1073741824

  shift = np.array ( [ 1, 64, 4096, 262144, 16777216 ] )

  seed1 = 1234567890
  seed2 = 123456789

  values = np.zeros ( 5 )

  lphr = lennob ( phrase )

  for i in range ( 0, lphr ):

    c = phrase[i]
    ichr = table.find ( c )

    if ( ichr == -1 ):
      ichr = 0
    else:
      ichr = ichr + 1

    ichr = ( ichr % 64 )

    if ( ichr == 0 ):
      ichr = 63

    for j in range ( 0, 5 ):
      values[j] = ichr - j - 1
      if ( values[j] < 1 ):
        values[j] = values[j] + 63

    for j in range ( 0, 5 ):
      seed1 = ( ( seed1 + shift[j] * values[j]   ) % twop30 )
      seed2 = ( ( seed2 + shift[j] * values[4-j] ) % twop30 )

  return seed1, seed2

def phrtsd_test ( ):

#*****************************************************************************80
#
## PHRTSD_TEST tests PHRTSD.
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

  print ( '' )
  print ( 'PHRTSD_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PHRTSD converts a phrase into two numeric seeds.' )

  s = 'A1'
  seed1, seed2 = phrtsd ( s )
  print ( '' )
  print ( '  Phrase: "%s"' % ( s ) )
  print ( '  Seeds:  %d  %d' % ( seed1, seed2 ) )

  s = 'shazam'
  seed1, seed2 = phrtsd ( s )
  print ( '' )
  print ( '  Phrase: "%s"' % ( s ) )
  print ( '  Seeds:  %d  %d' % ( seed1, seed2 ) )

  s = 'Happy birthday'
  seed1, seed2 = phrtsd ( s )
  print ( '' )
  print ( '  Phrase: "%s"' % ( s ) )
  print ( '  Seeds:  %d  %d' % ( seed1, seed2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PHRTSD_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phrtsd_test ( )
  timestamp ( )

