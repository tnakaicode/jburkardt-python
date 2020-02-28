#! /usr/bin/env python
#
def i4_uni ( ):

#*****************************************************************************80
#
## I4_UNI generates a random positive integer.
#
#  Discussion:
#
#    This procedure returns a random integer following a uniform distribution
#    over (1, 2147483562) using the current generator.
#
#    The original name of this function was "random()", but this conflicts
#    with a standard library function name in C.
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
#    Output, integer VALUE, the random integer.
#
  from antithetic_get import antithetic_get
  from cg_get import cg_get
  from cg_set import cg_set
  from cgn_get import cgn_get
  from initialize import initialize
  from initialized_get import initialized_get

  a1 = 40014
  a2 = 40692
  m1 = 2147483563
  m2 = 2147483399
#
#  Check whether the package must be initialized.
#
  if ( not initialized_get ( ) ):
    print ( '' )
    print ( 'I4_UNI - Note:' )
    print ( '  Initializing RNGLIB package.' )
    initialize ( )
#
#  Get the current generator index.
#
  g = cgn_get ( )
#
#  Retrieve the seeds for the current generator.
#
  cg1, cg2 = cg_get ( g )
#
#  Update the seeds.
#
  k = ( cg1 // 53668 )
  cg1 = a1 * ( cg1 - k * 53668 ) - k * 12211

  if ( cg1 < 0 ):
    cg1 = cg1 + m1

  k = ( cg2 // 52774 )
  cg2 = a2 * ( cg2 - k * 52774 ) - k * 3791

  if ( cg2 < 0 ):
    cg2 = cg2 + m2
#
#  Store the updated seeds.
#
  cg_set ( g, cg1, cg2 )
#
#  Construct the random integer from the seeds.
#
  z = cg1 - cg2

  if ( z < 1 ):
    z = z + m1 - 1
#
#  If the generator is in antithetic mode, we must reflect the value.
#
  value = antithetic_get ( )

  if ( value ):
    z = m1 - z

  return z

def i4_uni_test ( ):

#*****************************************************************************80
#
## I4_UNI_TEST tests I4_UNI.
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
  import platform

  print ( '' )
  print ( 'I4_UNI_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_UNI returns a random positive integer.' )
  print ( '' )

  for i in range ( 1, 21 ):
    value = i4_uni ( )
    print ( '  %d' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_UNI_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_uni_test ( )
  timestamp ( )


