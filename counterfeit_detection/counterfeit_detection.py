#! /usr/bin/env python3
#
def counterfeit_detection_brute ( n, coin, correct ):

#*****************************************************************************80
#
## counterfeit_detection_brute detects counterfeit coins.
#
#  Discussion:
#
#    We are given the weights of N coins, and the correct weight of a single 
#    coin.  We are asked to identify the counterfeit coins, that is, those
#    with incorrect weight.  We don't know how many such coins there are.
#
#    We simply use brute force.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 March 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kurt Bryan, Tanya Leise,
#    Making do with less: an introduction to compressed sensing,
#    SIAM Review,
#    Volume 55, Number 3, September 2013, pages 547-566.
#
#  Parameters:
#
#    Input, integer n, the number of coins.
#
#    Input, real coin(n), the weights of the coins.
#
#    Input, real correct, the correct weight of a single coin.
#
#    Output, integer suspect(*), the indices of the suspected counterfeit coins.
#
  import numpy as np

  suspect = np.nonzero ( coin != correct )
  suspect = np.ravel ( suspect )

  return suspect

def counterfeit_detection_brute_test ( ):

#*****************************************************************************80
#
## counterfeit_detection_brute_test tests counterfeit_detection_brute.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 March 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'counterfeit_detection_brute_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test counterfeit_detection_brute,' )
  print ( '  which seeks to identify multiple counterfeit coins among n coins' )
  print ( '  using brute force.' )
#
#  Generate the problem.
#
  n = 100
  correct = 17.0
  coin = correct * np.ones ( n )
  fake_num = np.random.randint ( 3, 11 )
  fake_index = np.random.choice ( n, fake_num, replace = False )
  fake_index.sort( )
  coin[fake_index] = correct + 3.0 * np.random.normal ( fake_num )
#
#  Report the fakes.
#
  print ( '' )
  print ( '  There were %d fakes' % ( fake_num ) )
  print ( '' )
  print ( '  Indices of fakes:' )
  print ( '' )
  for i in range ( 0, fake_num ):
    print ( '  %d:  %d  %g' % ( i, fake_index[i], coin[fake_index[i]] ) )
#
#  Detect and report the fakes.
#
  suspect = counterfeit_detection_brute ( n, coin, correct )
  suspect_num = len ( suspect )

  print ( '' )
  print ( '  The function found %d suspects.' % ( suspect_num ) )
  print ( '' )
  print ( '  Indices of suspects:' )
  print ( '' )
  for i in range ( 0, suspect_num ):
    print ( '  %d:  %d  %g' % ( i, suspect[i], coin[suspect[i]] ) )

  return

def counterfeit_detection_combinatorial ( logn, coin, correct ):

#*****************************************************************************80
#
## counterfeit_detection_combinatorial detects a counterfeit coin.
#
#  Discussion:
#
#    N = 2^(logn) - 1 coins are given.  All but one have the correct weight.
#    Identify the fake coin in logn weighings.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 March 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kurt Bryan, Tanya Leise,
#    Making do with less: an introduction to compressed sensing,
#    SIAM Review,
#    Volume 55, Number 3, September 2013, pages 547-566.
#
#  Parameters:
#
#    Input, integer logn, the number of coins is 2^logn - 1.
#
#    Input, real coin(2^logn-1), the weights of the coins.
#
#    Input, real correct, the correct weight of a single coin.
#
#    Output, integer suspect, the index of the suspected counterfeit coin.
#
  import numpy as np

  n = 2 ** logn - 1
#
#  The PHI matrix encodes the binary representations of 1 through n.
#  For n = 7:
#
#    1 0 1 0 1 0 1
#    0 1 1 0 0 1 1
#    0 0 0 1 1 1 1
#
#  We compute column J of the PHI matrix, and multiply by COIN(J),
#  and add that to W.  W = PHI * COIN.
#
  w = np.zeros ( logn )
  phi = np.zeros ( logn )

  for j in range ( 0, n ):
    for i in range ( 0, logn ):
      if ( phi[i] == 0 ):
        phi[i] = 1
        break
      phi[i] = 0
    w[0:logn] = w[0:logn] + phi[0:logn] * coin[j]
#
#  The suspected coin is found because the incorrect entries in W
#  form the binary representation of the index.
#
  suspect = 0
  good = correct * 2 ** ( logn - 1 )
  factor = 1
  for i in range ( 0, logn ):
    if ( w[i] != good ):
      suspect = suspect + factor
    factor = factor * 2
#
#  Subtract 1 for Python base 0 indexing...
#
  suspect = suspect - 1

  return suspect

def counterfeit_detection_combinatorial_test ( logn ):

#*****************************************************************************80
#
## counterfeit_detection_combinatorial_test tests counterfeit_detection_combinatorial.
#
#  Discussion:
#
#    N = 2^(logn) - 1 coins are given.  All but one have the correct weight.
#    Identify the fake coin in logn weighings.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 March 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kurt Bryan, Tanya Leise,
#    Making do with less: an introduction to compressed sensing,
#    SIAM Review,
#    Volume 55, Number 3, September 2013, pages 547-566.
#
#  Parameters:
#
#    Input, integer logn, the number of coins is 2^logn - 1.
#    A value of 3 is typical.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'counterfeit_detection_combinatorial_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test counterfeit_detection_combinatorial,' )
  print ( '  which can identify one counterfeit coin among 2^logn-1 coins' )
  print ( '  using just logn comparisons.' )

  n = 2 ** logn - 1
#
#  Set the data.
#
  correct = 17.0
  coin = correct * np.ones ( n );
#
#  Select one coin at random to have the wrong weight.
#
  fake = np.random.randint ( 0, n )
  coin[fake] = coin[fake] + 0.5 * np.random.normal ( 1 )

  suspect = counterfeit_detection_combinatorial ( logn, coin, correct )
#
#  Compare actual fake to your suspect.
#
  print ( '' )
  print ( '  %d coins were checked' % ( n ) )
  print ( '  The fake coin was number %d' % ( fake ) )
  print ( '  %d comparisons were made' % ( logn ) )
  print ( '  The suspected coin is number %d' % ( suspect ) )
  return

def counterfeit_detection_compressed ( n, coin, correct, k ):

#*****************************************************************************80
#
## counterfeit_detection_compressed detects counterfeit coins.
#
#  Discussion:
#
#    We are given the weights of N coins, and the correct weight of a single 
#    coin.  We are asked to identify the counterfeit coins, that is, those
#    with incorrect weight.  We don't know how many such coins there are.
#
#    We use techniques from compressed sensing.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kurt Bryan, Tanya Leise,
#    Making do with less: an introduction to compressed sensing,
#    SIAM Review,
#    Volume 55, Number 3, September 2013, pages 547-566.
#
#  Parameters:
#
#    Input, integer n, the number of coins.
#
#    Input, real coin(n), the weights of the coins.
#
#    Input, real correct, the correct weight of a single coin.
#
#    Input, integer k, the number of rows to use in the sensing matrix.
#
#    Output, integer suspect, the index of the suspected counterfeit coin.
#
  import numpy as np
  from scipy.optimize import linprog
  from scipy.optimize import OptimizeWarning
  import warnings

  phi = np.random.randint ( 0, 2, size = ( k, n ) )

  b1 = np.matmul ( phi, coin )
  b2 = correct * np.sum ( phi, axis = 1 )
  b2 = np.reshape ( b2, ( k ) )
  b = b1 - b2
#
#  Find x which minimizes ||x||_1 subject to phi*x=b.
#
  f = np.ones ( n )
#
#  Without this, linprog will warn that the Phi matrix does not have
#  full row rank.  We don't care!
#
  with warnings.catch_warnings():
    warnings.filterwarnings ( 'ignore', category = OptimizeWarning )
    result = linprog ( f, A_ub=None, b_ub=None, A_eq=phi, b_eq=b, bounds = (0,None) )
#   result = linprog ( f, A_ub=None, b_ub=None, A_eq=phi, b_eq=b, bounds = (0,None), options={'tol':1.0e-8} )

  suspect = np.nonzero ( result.x )
  suspect = np.ravel ( suspect )

  return suspect

def counterfeit_detection_compressed_test ( k ):

#*****************************************************************************80
#
## counterfeit_detection_compressed_test tests counterfeit_detection_compressed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kurt Bryan, Tanya Leise,
#    Making do with less: an introduction to compressed sensing,
#    SIAM Review,
#    Volume 55, Number 3, September 2013, pages 547-566.
#
#  Parameters:
#
#    Input, integer k, the number of random subsets to test.
#    If n = 100, k = 20 is reasonable.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'counterfeit_detection_compressed_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test counterfeit_detection_compressed,' )
  print ( '  which seeks to identify multiple counterfeit coins among n coins' )
  print ( '  using compressed sensing techniques.' )

  problem = 2

  if ( problem == 1 ):

    n = 7
    correct = 17.0
    coin = correct * np.ones ( n )
    fake = np.array ( [ 2 ] )
    fake_num = len ( fake )
    coin[fake[0]] = correct + 0.5 * np.random.random ( fake_num )

  else:
#
#  Very strange!  Setting all counterfeits to 17.5 improves chances of
#  getting a solution...
#
    n = 100
    correct = 17.0
    coin = correct * np.ones ( n )

    fake_num = 3
    fake = np.random.choice ( n, fake_num, replace = False )
    fake.sort( )

    for i in range ( 0, fake_num ):
#     coin[fake[i]] = correct + 0.5 * np.random.random ( 1 )
      coin[fake[i]] = correct + 0.5

  print ( '  There are %d coins to check.' % ( n ) )
  print ( '  The correct coin weight is %g' % ( correct ) )
#
#  Report the fakes.
#
  print ( '' )
  print ( '  There were %d fakes' % ( fake_num ) )
  print ( '' )
  print ( '     Fake  Index  Weight::' )
  print ( '' )
  for i in range ( 0, fake_num ):
    print ( '  %7d:  %4d  %g' % ( i, fake[i], coin[fake[i]] ) )
#
#  Detect and report the suspected fakes.
#
  suspect = counterfeit_detection_compressed ( n, coin, correct, k )
  suspect_num = len ( suspect )

  print ( '' )
  print ( '  %d random subsets were weighed.' % ( k ) )
  print ( '  The function found %d suspects.' % ( suspect_num ) )
  print ( '' )
  print ( '  Suspect  Index  Weight:' )
  print ( '' )
  for i in range ( 0, suspect_num ):
    print ( '  %7d:  %4d  %g' % ( i, suspect[i], coin[suspect[i]] ) )
#
#  Declare success or failure.
#
  if ( suspect_num != fake_num ):
    success = False
  elif ( np.array_equal ( fake, suspect ) ):
    success = True
  else:
    success = False

  print ( '' )
  if ( success ):
    print ( '  The test succeeded' )
  else:
    print ( '  The test failed.' )

  return

def counterfeit_detection_test ( ):

#*****************************************************************************80
#
## counterfeit_detection_test tests counterfeit_detection.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 March 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'counterfeit_detection_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test counterfeit_detection.' )

  counterfeit_detection_brute_test ( )
  logn = 3
  counterfeit_detection_combinatorial_test ( logn )
  k = 20
  counterfeit_detection_compressed_test ( k )
#
#  Terminate.
#
  print ( '' )
  print ( 'counterfeit_detection_test:' )
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
  counterfeit_detection_test ( )
  timestamp ( )

