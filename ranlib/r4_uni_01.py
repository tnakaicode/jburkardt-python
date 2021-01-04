#! /usr/bin/env python
#
def r4_uni_01 ( ):

#*****************************************************************************80
#
## R4_UNI_01 returns a uniform random real number in [0,1].
#
#  Discussion:
#
#    This procedure returns a random floating point number from a uniform
#    distribution over (0,1), not including the endpoint values, using the
#    current random number generator.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Pierre LEcuyer, Serge Cote,
#    Implementing a Random Number Package with Splitting Facilities,
#    ACM Transactions on Mathematical Software,
#    Volume 17, Number 1, March 1991, pages 98-111.
#
#  Parameters:
#
#    Output, real VALUE, a uniform random value in [0,1].
#
  from i4_uni import i4_uni
  from initialize import initialize
  from initialized_get import initialized_get
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'R4_UNIFORM_01 - Note:' )
    print ( '  Initializing RNGLIB package.' )
    initialize ( )
#
#  Get a random positive integer.
#
  i = i4_uni ( )
#
#  Scale it to a random real in [0,1].
#
  value = i * 4.656613057E-10

  return value

def r4_uni_01_test ( ):

#*****************************************************************************80
#
## R4_UNI_01_TEST tests R4_UNI_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R4_UNI_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4_UNI_01 produces a sequence of random values.' )

  print ( '' )
  print ( '  R4_UNI_01()' )
  print ( '' )
  for i in range ( 0, 10 ):
    x = r4_uni_01 ()
    print ( '  %g' % ( x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4_UNI_01_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r4_uni_01_test ( )
  timestamp ( )
