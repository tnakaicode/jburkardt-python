#! /usr/bin/env python
#
def lcrg_seed ( a, b, c, n, seed ):

#*****************************************************************************80
#
## LCRG_SEED computes the N-th seed of a linear congruential generator.
#
#  Discussion:
#
#    We are considering a linear congruential random number generator.
#    The LCRG takes as input an integer value called SEED, and returns
#    an updated value of SEED, 
#
#      SEED(out) = a * SEED(in) + b, mod c.
#
#    and an associated pseudorandom real value
#
#      U = SEED(out) / c.
#
#    In most cases, a user is content to call the LCRG repeatedly, with
#    the updating of SEED being taken care of automatically.
#
#    The purpose of this routine is to determine the value of SEED that
#    would be output after N successive applications of the LCRG.  This
#    allows the user to know, in advance, what the 1000-th value of
#    SEED would be, for instance.  Obviously, one way to do this is to
#    apply the LCRG formula 1,000 times.  However, it is possible to
#    do this in a more direct and efficient way.
#
#    One use for such a facility would be to do random number computations
#    in parallel.  If each processor is to compute 1,000 values, you can
#    guarantee that they work with distinct random values by starting the
#    first processor with SEED, the second with the value of SEED after 
#    1,000 applications of the LCRG, and so on.
#
#    To evaluate the N-th value of SEED directly, we start by ignoring 
#    the modular arithmetic, and working out the sequence of calculations
#    as follows:
#
#      SEED(0) =     SEED.
#      SEED(1) = a * SEED      + b
#      SEED(2) = a * SEED(1)   + b = a^2 * SEED + a * b + b
#      SEED(3) = a * SEED(2)   + b = a^3 * SEED + a^2 * b + a * b + b
#      ...
#      SEED(N) = a * SEED(N-1) + b = a^N * SEED 
#                                    + ( a^(n-1) + a^(n-2) + ... + a + 1 ) * b
#
#    or, using the geometric series,
#
#      SEED(N) = a^N * SEED + ( a^N - 1) / ( a - 1 ) * b
#
#    Therefore, we can determine SEED(N) directly if we can solve
#
#      ( a - 1 ) * BN = ( a^N - 1 ) * b in modular arithmetic,
#
#    and evaluated:
#
#      AN = a^N
#
#    Using the formula:
#
#      SEED(N) = AN * SEED + BN, mod c
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the multiplier for the LCRG.
#
#    Input, integer B, the added value for the LCRG.
#
#    Input, integer C, the base for the modular arithmetic.  For 32 bit
#    arithmetic, this is often 2^31 - 1, or 2147483647.  It is required
#    that 0 < C.
#
#    Input, integer N, the "index", or number of times that the LCRG
#    is to be applied.  It is required that 0 <= N.
#
#    Input, integer SEED, the starting value of SEED.  It is customary
#    that 0 < SEED.
#
#    Output, integer SEED_LCRG, the value of SEED that would be output
#    if the LCRG were applied to the starting value N times.
#
  from congruence import congruence
  from power_mod import power_mod
  from sys import exit

  if ( n < 0 ):
    print ( '' )
    print ( 'LCRG_SEED - Fatal error!' )
    print ( '  Illegal input value of N = %d' % ( n ) )
    exit ( 'LCRG_SEED - Fatal error!' )

  if ( c <= 0 ):
    print ( '' )
    print ( 'LCRG_SEED - Fatal error!' )
    print ( '  Illegal input value of C = %d' % ( c ) )
    exit ( 'LCRG_SEED - Fatal error!' )

  if ( n == 0 ):
    seed_lcrg = ( seed % c )
    if ( seed_lcrg < 0 ):
      seed_lcrg = seed_lcrg + c
    return seed_lcrg
#
#  Get A^N.
#
  an = power_mod ( a, n, c )
#
#  Solve ( a - 1 ) * BN = ( a^N - 1 ) for BN.
#
#  The LCRG I have been investigating uses B = 0, so this code
#  has not been properly tested yet.
#
  bn, ierror = congruence ( a-1, c, ( an - 1 ) * b )

  if ( ierror != 0 ):
    print ( '' )
    print ( 'LCRG_SEED - Fatal error!' )
    print ( '  An error occurred in the CONGRUENCE routine.' )
    print ( '  The error code was IERROR = %d' % ( ierror ) )
    exit ( 'LCRG_SEED - Fatal error!' )
#
#  Set the new SEED.
#
  value2 = an * seed + bn

  value2 = ( value2 % c )
#
#  Guarantee that the value is positive.
#
  if ( value2 < 0 ):
    value2 = value2 + c

  seed_lcrg = value2

  return seed_lcrg

def lcrg_seed_test ( ):

#*****************************************************************************80
#
## LCRG_SEED_TEST tests LCRG_SEED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r4_uniform_01 import r4_uniform_01

  print ( '' )
  print ( 'LCRG_SEED_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LCRG_SEED directly computes the updated value of a' )
  print ( '  seed used by an linear congruential random number' )
  print ( '  generator.' )
  print ( '' )
  print ( '       I          SEED          SEED          SEED    U' )
  print ( '                 Input        Output          LCRG' )
  print ( '' )
#
#  These parameters define the old (1969) IBM 360 random number generator:
#
  a = 16807
  b = 0
  c = 2147483647
#
#  This seed value was used in Pierre L'Ecuyer's article.
#
  seed_start = 12345

  seed = seed_start
#
#  Compute 1000 random numbers "the hard way", that is, sequentially.
#  Every now and then, call LCRG_SEED to compute SEED directly.
#
  for i in range ( 1, 1001 ):

    seed_in = seed
    u, seed = r4_uniform_01 ( seed )
    seed_out = seed

    if ( i <= 10 or i == 100 or i == 1000 ):

      seed_lcrg = lcrg_seed ( a, b, c, i, seed_start )

      print ( '  %6d  %12d  %12d  %12d  %14f' \
        % ( i, seed_in, seed_out, seed_lcrg, u ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LCRG_SEED_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lcrg_seed_test ( )
  timestamp ( )


