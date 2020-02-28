#! /usr/bin/env python
#
def coupon_mean ( j, n ):

#*****************************************************************************80
#
## COUPON_MEAN returns the mean of the Coupon PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer J, the number of distinct coupons to be collected.
#    J must be between 1 and N.
#
#    Input, integer N, the number of distinct coupons.
#
#    Output, real MEAN, the mean number of coupons that
#    must be collected in order to just get J distinct kinds.
#
  from sys import exit

  if ( n < j ):
    print ( '' )
    print ( 'COUPON_MEAN - Fatal error!' )
    print ( '  Number of distinct coupons desired must be no more' )
    print ( '  than the total number of distinct coupons.' )
    exit ( 'COUPON_MEAN - Fatal error!' )

  mean = 0.0
  for i in range ( 1, j + 1 ):
    mean = mean + 1.0 / float ( n - i + 1 )
  mean = mean * float ( n )

  return mean

def coupon_sample ( n_type, seed ):

#*****************************************************************************80
#
## COUPON_SAMPLE simulates the coupon collector's problem.
#
#  Discussion:
#
#    The coupon collector needs to collect one of each of N_TYPE
#    coupons.  The collector may draw one coupon on each trial,
#    and takes as many trials as necessary to complete the task.
#    On each trial, the probability of picking any particular type
#    of coupon is always 1 / N_TYPE.
#
#    The most interesting question is, what is the expected number
#    of drawings necessary to complete the collection?
#    how does this number vary as N_TYPE increases?  What is the
#    distribution of the numbers of each type of coupon in a typical
#    collection when it is just completed?
#
#    As N increases, the number of coupons necessary to be
#    collected in order to get a complete set in any simulation
#    strongly tends to the value N_TYPE * LOG ( N_TYPE ).
#
#    If N_TYPE is 1, the simulation ends with a single drawing.
#
#    If N_TYPE is 2, then we may call the coupon taken on the first drawing
#    a "Head", say, and the process then is similar to the question of the
#    length, plus one, of a run of Heads or Tails in coin flipping.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N_TYPE, the number of types of coupons.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer COUPON(N_TYPE), the number of coupons of each type
#    that were collected during the simulation.
#
#    Output, integer N_COUPON, the total number of coupons collected.
#
#    Output, integer SEED, a seed for the random number generator.
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab

  max_coupon = 2000

  coupon = np.zeros ( n_type )

  straight = 0
  n_coupon = 0
#
#  Draw another coupon.
#
  while ( n_coupon < max_coupon ):

    i, seed = i4_uniform_ab ( 1, n_type, seed )
#
#  Increment the number of I coupons.
#
    coupon[i-1] = coupon[i-1] + 1
    n_coupon = n_coupon + 1
#
#  If I is the next one we needed, increase STRAIGHT by 1.
#
    if ( i == straight + 1 ):

      while ( True ):

        straight = straight + 1
#
#  If STRAIGHT = N_TYPE, we have all of them.
#
        if ( n_type <= straight ):
          return coupon, n_coupon, seed
#
#  If the next coupon has not been collected, our straight is over.
#
        if ( coupon[straight] <= 0 ):
          break

  print ( '' )
  print ( 'COUPON_SAMPLE - Fatal error!' )
  print ( '  Maximum number of coupons drawn without success.' )

  return coupon, n_coupon, seed

def coupon_sample_test ( ):

#*****************************************************************************80
#
## COUPON_SAMPLE_TEST tests COUPON_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n_trial = 10
  max_type = 25

  print ( '' )
  print ( 'COUPON_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  COUPON_SAMPLE samples the coupon PDF.' )
  print ( '' )

  for n_type in range ( 5, max_type + 1, 5 ):

    print ( '' )
    print ( '  Number of coupon types is %d' % ( n_type ) )

    expect = n_type * np.log ( float ( n_type ) )

    print ( '  Expected wait is about %g' % ( expect ) )
    print ( '' )

    seed = 123456789

    average = 0.0
    for i in range ( 0, n_trial ):
      coupon, n_coupon, seed = coupon_sample ( n_type, seed )
      print ( '  %6d  %6d' % ( i, n_coupon ) )
      average = average + n_coupon

    average = average / float ( n_trial )

    print ( '' )
    print ( '  Average wait was %g' % ( average ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'COUPON_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def coupon_variance ( j, n ):

#*****************************************************************************80
#
## COUPON_VARIANCE returns the variance of the Coupon PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer J, the number of distinct coupons to be collected.
#    J must be between 1 and N.
#
#    Input, integer N, the number of distinct coupons.
#
#    Output, real VARIANCE, the variance of the number of
#    coupons that must be collected in order to just get J distinct kinds.
#
  if ( n < j ):
    print ( '' )
    print ( 'COUPON_VARIANCE - Fatal error!' )
    print ( '  Number of distinct coupons desired must be no more' )
    print ( '  than the total number of distinct coupons.' )
    exit ( 'COUPON_VARIANCE - Fatal error!' )

  variance = 0.0
  for i in range ( 1, j + 1 ):
    variance = variance + float ( i - 1 ) / float ( ( n - i + 1 ) ** 2 )
  variance = variance * float ( n )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  coupon_sample_test ( )
  timestamp ( )
 
