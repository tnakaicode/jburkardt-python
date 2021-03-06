#! /usr/bin/env python
#
def r8_rand ( r, ix0, ix1 ):

#*****************************************************************************80
#
## R8_RAND is a portable pseudorandom number generator.
#
#  Discussion:
#
#    This pseudo-random number generator is portable amoung a wide
#    variety of computers.  It is undoubtedly not as good as many
#    readily available installation dependent versions, and so this
#    routine is not recommended for widespread usage.  Its redeeming
#    feature is that the exact same random numbers (to within final round-
#    off error) can be generated from machine to machine.  Thus, programs
#    that make use of random numbers can be easily transported to and
#    checked in a new environment.
#
#    The random numbers are generated by the linear congruential
#    method described by Knuth in seminumerical methods (p.9),
#    addison-wesley, 1969.  Given the i-th number of a pseudo-random
#    sequence, the i+1 -st number is generated from
#      x(i+1) = (a*x(i) + c) mod m,
#    where here m = 2^22 = 4194304, c = 1731 and several suitable values
#    of the multiplier a are discussed below.  Both the multiplier a and
#    random number x are represented in real as two 11-bit
#    words.  The constants are chosen so that the period is the maximum
#    possible, 4194304.
#
#    In order that the same numbers be generated from machine to
#    machine, it is necessary that 23-bit integers be reducible modulo
#    2^11 exactly, that 23-bit integers be added exactly, and that 11-bit
#    integers be multiplied exactly.  Furthermore, if the restart option
#    is used (where r is between 0 and 1), then the product r*2^22 =
#    r*4194304 must be correct to the nearest integer.
#
#    The first four random numbers should be
#
#      0.0004127026,
#      0.6750836372,
#      0.1614754200,
#      0.9086198807.
#
#    The tenth random number is
#
#      0.5527787209.
#
#    The hundredth random number is
#
#      0.3600893021.
#
#    The thousandth number should be
#
#      0.2176990509.
#
#    In order to generate several effectively independent sequences
#    with the same generator, it is necessary to know the random number
#    for several widely spaced calls.  The I-th random number times 2^22,
#    where I=K*P/8 and P is the period of the sequence (P = 2^22), is
#    still of the form L*P/8.  In particular we find the I-th random
#    number multiplied by 2^22 is given by
#      I   =  0  1*p/8  2*p/8  3*p/8  4*p/8  5*p/8  6*p/8  7*p/8  8*p/8
#      RAND=  0  5*p/8  2*p/8  7*p/8  4*p/8  1*p/8  6*p/8  3*p/8  0
#    thus the 4*P/8 = 2097152 random number is 2097152/2**22.
#
#    Several multipliers have been subjected to the spectral test
#    (see Knuth, p. 82).  Four suitable multipliers roughly in order of
#    goodness according to the spectral test are
#      3146757 = 1536*2048 + 1029 = 2^21 + 2^20 + 2^10 + 5
#      2098181 = 1024*2048 + 1029 = 2^21 + 2^10 + 5
#      3146245 = 1536*2048 +  517 = 2^21 + 2^20 + 2^9 + 5
#      2776669 = 1355*2048 + 1629 = 5^9 + 7^7 + 1
#
#    In the table below log10(NU(I)) gives roughly the number of
#    random decimal digits in the random numbers considered I at a time.
#    C is the primary measure of goodness.  In both cases bigger is better.
#
#                     log10 nu(i)              c(i)
#         a       i=2  i=3  i=4  i=5    i=2  i=3  i=4  i=5
#
#      3146757    3.3  2.0  1.6  1.3    3.1  1.3  4.6  2.6
#      2098181    3.3  2.0  1.6  1.2    3.2  1.3  4.6  1.7
#      3146245    3.3  2.2  1.5  1.1    3.2  4.2  1.1  0.4
#      2776669    3.3  2.1  1.6  1.3    2.5  2.0  1.9  2.6
#     best
#      possible   3.3  2.3  1.7  1.4    3.6  5.9  9.7  14.9
#
#    Note that the original version of this routine used local static
#    variables IX0 and IX1.  In this revised version, IX0 and IX1 are
#    routine arguments.  To duplicate the behavior of the original code,
#    IX0 and IX1 should be set to zero before the first call.  
#    JVB, 04 May 2016.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 May 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, real R, determines the action.
#    * R = 0.0, the next random number of the sequence is generated.
#    * R < 0.0, the last generated number will be returned for
#    possible use in a restart procedure.
#    * R > 0.0, the sequence of random numbers will start with the
#    seed ( R mod 1 ).  This seed is also returned as the value of
#    R8_RAND provided the arithmetic is done exactly.
#
#    Input/output, integer IX0, IX1, two parameters used
#    as seeds for the random number generator.  On first call, these
#    might both be set to 0.
#
#    Output, real VALUE, a pseudo-random number between
#    0.0 and 1.0.
#
  ia0 = 1029
  ia1 = 1536
  ia1ma0 = 507
  ic = 1731

  if ( r == 0.0 ):
    iy0 = ia0 * ix0
    iy1 = ia1 * ix1 + ia1ma0 * ( ix0 - ix1 ) + iy0
    iy0 = iy0 + ic
    ix0 = ( iy0 % 2048 )
    iy1 = iy1 + ( iy0 - ix0 ) // 2048
    ix1 = ( iy1 % 2048 )

  if ( 0.0 < r ):
    ix1 = int ( ( r % 1.0 ) * 4194304.0 + 0.5 )
    ix0 = ( ix1 % 2048 )
    ix1 = ( ix1 - ix0 ) // 2048

  value = float ( ix1 * 2048 + ix0 )
  value = value / 4194304.0

  return value, ix0, ix1

def r8_rand_test ( ):

#*****************************************************************************80
#
## R8_RAND_TEST tests R8_RAND.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  i_value = np.array ( [ 1, 2, 3, 4, 10, 100, 1000 ] )

  r_value = np.array ( [ \
    0.0004127026, \
    0.6750836372, \
    0.1614754200, \
    0.9086198807, \
    0.5527787209, \
    0.3600893021, \
    0.2176990509 ] )

  print ( '' )
  print ( 'R8_RAND_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_RAND is a random number generator.' )
  print ( '' )
  print ( '             I         R8_RAND        Expected' )
  print ( '' )
#
#  Start the sequence with IX0 = IX1 = 0.
#
  ix0 = 0
  ix1 = 0
  s = 0.0

  k = 0

  for i in range ( 0, 1000 ):

    r, ix0, ix1 = r8_rand ( s, ix0, ix1 )

    if ( i + 1 == i_value[k] ):
      print ( '  %14d  %14.6g  %14.6g' % ( i + 1, r, r_value[k] ) )
      k = k + 1
#
#  Restart the sequence with IX0 = IX1 = 0.
#
  ix0 = 0
  ix1 = 0
  s = 0.0

  average = 0.0
  for i in range ( 0, 1000000 ):
    r, ix0, ix1 = r8_rand ( s, ix0, ix1 )
    average = average + r
  average = average / 1000000.0
  print ( '' )
  print ( '       Average =  %14g  %14g' % ( average, 0.5 ) )
#
#  Restart the sequence with IX0 = IX1 = 0.
#
  ix0 = 0
  ix1 = 0
  s = 0.0

  variance = 0.0
  for i in range ( 0, 1000000 ):
    r, ix0, ix1 = r8_rand ( s, ix0, ix1 )
    variance = variance + ( r - average ) ** 2
  variance = variance / 1000000.0
  print ( '       Variance = %14g  %14g' % ( variance, 1.0 / 12.0 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_RAND_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_rand_test ( )
  timestamp ( )

