#! /usr/bin/env python3
#
class randlc_init:

#*****************************************************************************80
#
## RANDLC_INIT is a class for the RANDLC library.
#
#  Discussion:
#
#    We define RANDLC and RANDLC_JUMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 October 2016
#
#  Author:
#
#    John Burkardt
#
  def __init__ ( self, seed ):
#
#  Deal with a 0 input value of SEED.
#
    if ( seed == 0.0 ):
      seed = 314159265.0
#
#  Deal somewhat arbitrarily with negative input SEED.
#
    if ( seed < 0.0 ):
      seed = - seed

    self.seed = seed

    a = 1220703125.0
#
#  Compute 
#
#    R23 = 2 ^ -23, 
#    R46 = 2 ^ -46,
#    T23 = 2 ^ 23, 
#    T46 = 2 ^ 46.  
#
#  These are computed in loops, rather than by merely using the power operator, 
#  in order to insure that the results are exact on all systems.  
#
    r23 = 1.0
    r46 = 1.0
    t23 = 1.0
    t46 = 1.0

    for i in range ( 0, 23 ):
      r23 = 0.5 * r23
      t23 = 2.0 * t23

    for i in range ( 0, 46 ):
      r46 = 0.50 * r46
      t46 = 2.0 * t46
#
#  Break A into two parts such that A = 2^23 * A1 + A2.
#
    t1 = r23 * a
    a1 = float ( int ( t1 ) )
    a2 = a - t23 * a1

    self.r23 = r23
    self.r46 = r46
    self.t23 = t23
    self.t46 = t46
    self.a1 = a1
    self.a2 = a2

  def randlc ( self ):

#*****************************************************************************80
#
## RANDLC returns a uniform pseudorandom value.
#
#  Discussion:
#
#    The number returned is in the range (0, 1).  
#
#    The algorithm uses the linear congruential generator:
#
#      X(K+1) = A * X(K)  mod 2^46
#
#    This scheme generates 2^44 numbers before repeating.  
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Bailey, Eric Barszcz, John Barton, D Browning, Robert Carter, 
#    Leonardo Dagum, Rod Fatoohi,
#    Samuel Fineberg, Paul Frederickson, Thomas Lasinski, Robert Schreiber, 
#    Horst Simon, V Venkatakrishnan, Sisira Weeratunga,
#    The NAS Parallel Benchmarks,
#    RNR Technical Report RNR-94-007,
#    March 1994.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 2, Seminumerical Algorithms,
#    Third Edition,
#    Addison Wesley, 1997,
#    ISBN: 0201896842,
#    LC: QA76.6.K64.
#
#  Parameters:
#
#    Output, real VALUE, the next pseudorandom value.
#
    if ( self.seed == 0.0 ):
      self.seed = 314159265.0
    elif ( self.seed < 0.0 ):
      self.seed = - self.seed

    x = self.seed
#
#  Break X into two parts X1 and X2 such that:
#
#    X = 2^23 * X1 + X2, 
#
#  then compute
#
#    Z = A1 * X2 + A2 * X1  (mod 2^23)
#    X = 2^23 * Z + A2 * X2  (mod 2^46).
#
    t1 = self.r23 * x
    x1 = float ( int ( t1 ) )
    x2 = x - self.t23 * x1

    t1 = self.a1 * x2 + self.a2 * x1
    t2 = float ( int ( self.r23 * t1 ) )
    z = t1 - self.t23 * t2

    t3 = self.t23 * z + self.a2 * x2
    t4 = float ( int ( self.r46 * t3 ) )
    x = t3 - self.t46 * t4

    self.seed = x

    value = self.r46 * x

    return value

  def randlc_jump ( self, k ):

#*****************************************************************************80
#
## RANDLC_JUMP returns the K-th element of a uniform pseudorandom sequence.
#
#  Discussion:
#
#    The sequence uses the linear congruential generator:
#
#      X(K+1) = A * X(K)  mod 2^46
#
#    The K-th element, which can be represented as
#
#      X(K) = A^K * X(0)  mod 2^46
#
#    is computed directly using the binary algorithm for exponentiation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2010
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Bailey, Eric Barszcz, John Barton, D Browning, Robert Carter, 
#    Leonardo Dagum, Rod Fatoohi,
#    Samuel Fineberg, Paul Frederickson, Thomas Lasinski, Robert Schreiber, 
#    Horst Simon, V Venkatakrishnan, Sisira Weeratunga,
#    The NAS Parallel Benchmarks,
#    RNR Technical Report RNR-94-007,
#    March 1994.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 2, Seminumerical Algorithms,
#    Third Edition,
#    Addison Wesley, 1997,
#    ISBN: 0201896842,
#    LC: QA76.6.K64.
#
#  Parameters:
#
#    Input, integer K, the index of the desired value.
#
#    Output, real VALUE, the K-th value in the sequence.
#
    from sys import exit

    if ( self.seed == 0.0 ):
      self.seed = 314159265.0
    elif ( self.seed < 0.0 ):
      self.seed = - self.seed

    x = self.seed

    if ( k < 0 ):

      print ( '' )
      print ( 'RANDLC_JUMP - Fatal error!' )
      print ( '  K < 0.' )
      exit ( 'RANDLC_JUMP - Fatal error!' )

    elif ( k == 0 ):

      xk = x
#
#  Find M so that K < 2^M.
#
    else:

      a = 1220703125.0
      k2 = k
      xk = x

      m = 1
      twom = 2
      while ( twom <= k ):
        twom = twom * 2
        m = m + 1

      b = a
      b1 = self.a1
      b2 = self.a2

      for i in range ( 0, m ):

        j = ( k2 // 2 )
#
#  Replace X by A * X, if appropriate.
#
        if ( 2 * j != k2 ):

          t1 = self.r23 * xk
          x1 = float ( int ( t1 ) )
          x2 = xk - self.t23 * x1

          t1 = b1 * x2 + b2 * x1
          t2 = float ( int ( self.r23 * t1 ) )
          z = t1 - self.t23 * t2

          t3 = self.t23 * z + b2 * x2
          t4 = float ( int ( self.r46 * t3 ) )
          xk = t3 - self.t46 * t4
#
#  Replace A by A * A mod 2^46.
#
        t1 = self.r23 * b
        x1 = float ( int ( t1 ) )
        x2 = b - self.t23 * x1

        t1 = b1 * x2 + b2 * x1
        t2 = float ( int ( self.r23 * t1 ) )
        z = t1 - self.t23 * t2

        t3 = self.t23 * z + b2 * x2
        t4 = float ( int ( self.r46 * t3 ) )
        b = t3 - self.t46 * t4
#
#  Update A1, A2.
#
        t1 = self.r23 * b
        b1 = float ( int ( t1 ) )
        b2 = b - self.t23 * b1

        k2 = j

    value = self.r46 * xk

    return value

def randlc_test01 ( ):

#*****************************************************************************80
#
## RANDLC_TEST01 tests RANDLC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 August 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'RANDLC_TEST01' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RANDLC computes pseudorandom values ' )
  print ( '  in the interval [0,1].' )

  seed = 123456789.0

  gen = randlc_init ( seed )

  print ( '' )
  print ( '  The initial seed is %g' % ( seed ) )
  print ( '' )
  print ( '         I          RANDLC' )
  print ( '' )
 
  for i in range ( 0, 10 ):
    value = gen.randlc ( )
    print ( '  %8d  %14.6g' % ( i, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RANDLC_TEST01:' )
  print ( '  Normal end of execution.' )
  return

def randlc_test02 ( ):

#*****************************************************************************80
#
## RANDLC_TEST02 tests RANDLC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 1000

  print ( '' )
  print ( 'RANDLC_TEST02' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RANDLC computes a sequence of uniformly' )
  print ( '  distributed pseudorandom numbers.' )

  seed = 123456789.0
  gen = randlc_init ( seed )

  print ( '' )
  print ( '  Initial SEED = %g' % ( seed ) )

  print ( '' )
  print ( '  First 10 values:' )
  print ( '' )
  print ( '       I            Input           Output      RANDLC' )
  print ( '                     SEED             SEED' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_in = gen.seed
    value = gen.randlc ( )
    seed_out = gen.seed
    print ( '  %6d  %15.0f  %15.0f  %10.6f' % ( i, seed_in, seed_out, value ) )

  print ( '' )
  print ( '  Now call RANDLC %d times.' % ( n ) )

  u = np.zeros ( n )

  u_avg = 0.0
  for i in range ( 0, n ):
    u[i] = gen.randlc ( )
    u_avg = u_avg + u[i]

  u_avg = u_avg / float ( n )

  u_var = 0.0
  for i in range ( 0, n ):
    u_var = u_var + ( u[i] - u_avg ) ** 2
  u_var = u_var / float ( n - 1 )

  print ( '' )
  print ( '  Average value = %g' % ( u_avg ) )
  print ( '  Expecting       %g' % ( 0.5 ) )

  print ( '' )
  print ( '  Variance =      %g' % ( u_var ) )
  print ( '  Expecting       %g' % ( 1.0 / 12.0 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RANDLC_TEST02:' )
  print ( '  Normal end of execution.' )
  return

def randlc_test03 ( ):

#*****************************************************************************80
#
## RANDLC_TEST03 tests RANDLC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2010
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'RANDLC_TEST03' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RANDLC computes a sequence of pseudorandom numbers' )
  print ( '  but all computations depend on the seed value.' )
  print ( '  In this test, we show how a sequence of "random"' )
  print ( '  values can be manipulated by accessing the seed.' )

  seed = 1066.0
  gen = randlc_init ( seed )

  print ( '' )
  print ( '  Set SEED to %g' % ( seed ) )
  print ( '' )
  print ( '  Now call RANDLC 10 times, and watch SEED.' )
  print ( '' )
  print ( '       I            Input           Output      RANDLC' )
  print ( '                     SEED             SEED' )
  print ( '' )

  for i in range ( 0, 10 ):

    seed_in = gen.seed

    if ( i == 4 ):
      seed_save = seed

    value = gen.randlc ( )
    seed_out = gen.seed
    print ( '  %6d  %15.0f  %15.0f  %10.6f' % ( i, seed_in, seed_out, value ) )

  seed = seed_save
  gen.seed = seed

  print ( '' )
  print ( '  Reset SEED to its value at step 5, = %g' % ( seed ) )
  print ( '' )
  print ( '  Now call RANDLC 10 times, and watch how SEED' )
  print ( '  and RANDLC restart themselves.' )
  print ( '' )
  print ( '       I            Input           Output      RANDLC' )
  print ( '                     SEED             SEED' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_in = gen.seed
    value = gen.randlc ( )
    seed_out = gen.seed
    print ( '  %6d  %15.0f  %15.0f  %10.6f' % ( i, seed_in, seed_out, value ) )

  seed = 0.0
  gen.seed = seed

  print ( '' )
  print ( '  What happens with an initial zero SEED?' )
  print ( '' )
  print ( '       I            Input           Output      RANDLC' )
  print ( '                     SEED             SEED' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_in = gen.seed
    value = gen.randlc ( )
    seed_out = gen.seed
    print ( '  %6d  %15.0f  %15.0f  %10.6f' % ( i, seed_in, seed_out, value ) )

  seed = -123456789.0
  gen.seed = seed

  print ( '' )
  print ( '  What happens with an initial negative SEED?' )
  print ( '' )
  print ( '       I            Input           Output      RANDLC' )
  print ( '                     SEED             SEED' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_in = gen.seed
    value = gen.randlc ( )
    seed_out = gen.seed
    print ( '  %6d  %15.0f  %15.0f  %10.6f' % ( i, seed_in, seed_out, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RANDLC_TEST03:' )
  print ( '  Normal end of execution.' )
  return

def randlc_jump_test ( ):

#*****************************************************************************80
#
## RANDLC_JUMP_TEST tests RANDLC_JUMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'RANDLC_JUMP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RANDLC_JUMP jumps directly to the K-th value' )
  print ( '  returned by RANDLC.' )
  print ( '' )
  print ( '         K X(hard way)     X(jump)' )
  print ( '' )

  k = 1

  for klog in range ( 0, 10 ):

    seed = 123456789.0
    gen = randlc_init ( seed )

    for i in range ( 0, k ):
      value1 = gen.randlc ( )
    
    seed = 123456789.0
    gen.seed = seed
    value2 = gen.randlc_jump ( k )

    print ( '  %8d  %10.6f  %10.6f' % ( k, value1, value2 ) )

    k = k * 2
#
#  Terminate.
#
  print ( '' )
  print ( 'RANDLC_JUMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def randlc_test ( ):

#*****************************************************************************80
#
## RANDLC_TEST tests the RANDLC library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'RANDLC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the RANDLC library.' )

  randlc_test01 ( )
  randlc_test02 ( )
  randlc_test03 ( )
  randlc_jump_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'RANDLC_TEST' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  randlc_test ( )
  timestamp ( )
 
