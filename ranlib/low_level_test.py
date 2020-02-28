#! /usr/bin/env python
#
def low_level_test ( ):

#*****************************************************************************80
#
## LOW_LEVEL_TEST is a test program for the low level random generators.
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
  import numpy as np
  import platform
  from cgn_set import cgn_set
  from i4_uni import i4_uni
  from init_generator import init_generator
  from initialize import initialize
  from set_initial_seed import set_initial_seed

  genlst = np.array ( [ 1, 5, 10, 20, 32 ] )

  print ( '' )
  print ( 'LOW_LEVEL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the lower level random number generators.' )
  print ( '' )
  print ( '  Five of the 32 generators will be tested.' )
  print ( '  We generate 100000 numbers, reset the block' )
  print ( '  and do it again.  No disagreements should occur.' )
#
#  Initialize the generators.
#
  initialize ( )
#
#  Set up all generators.
#
  seed1 = 12345
  seed2 = 54321
  set_initial_seed ( seed1, seed2 )
#
#  For a selected set of generators
#
  nbad = 0
  answer = np.zeros ( 10000 )

  for ixgen in range ( 0, 5 ):

    igen = genlst[ixgen]
    cgn_set ( igen )
    print ( '  Testing generator %d' % ( igen ) )
#
#  Use 10 blocks, and generate 1000 numbers per block
#
    init_generator ( 0 )

    for iblock in range ( 1, 11 ):
      for ians in range ( 1, 1001 ):
        ix = ians + ( iblock - 1 ) * 1000
        answer[ix-1] = i4_uni ( )
      init_generator ( 2 )
#
#  Do it again and compare answers
#  Use 10 blocks, and generate 1000 numbers.
#
    init_generator ( 0 )

    for iblock in range ( 1, 11 ):
      for ians in range ( 1, 1001 ):
        ix = ians + ( iblock - 1 ) * 1000
        itmp = i4_uni ( )

        if ( itmp != answer[ix-1] ):

          print ( '' )
          print ( 'RANLIB_TEST_BOT - Warning!' )
          print ( '  Data disagreement:' )
          print ( '  Block = %d' % ( iblock ) )
          print ( '  N within block = %d' % ( ians ) )
          print ( '  Index in ANSWER = %d' % ( ix ) )
          print ( '  First value =  %d' % ( answer[ix] ) )
          print ( '  Second value = %d' % ( itmp ) )

          nbad = nbad + 1

          if ( 10 < nbad ):
            print ( '' )
            print ( 'RANLIB_TEST_BOT - Warning!' )
            print ( '  More than 10 mismatches.' )
            print ( '  Tests terminated early.' )
            return

      init_generator ( 2 )

  print ( '' )
  print ( '  Number of disagreements found was %d' % ( nbad ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LOW_LEVEL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  low_level_test ( )
  timestamp ( )

