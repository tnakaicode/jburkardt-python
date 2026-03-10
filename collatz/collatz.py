#! /usr/bin/env python3
#
def collatz_test ( ):

#*****************************************************************************80
#
## collatz_test() tests collatz().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'collatz_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test collatz().' )

  collatz_test01 ( )
  collatz_count_test ( )
  collatz_test03 ( )
  collatz_test04 ( )
  collatz_inverse_test ( )
  collatz_max_test ( )
  collatz_test06 ( )
  mollatz_test ( )
  nollatz_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'collatz_test():' )
  print ( '  Normal end of execution.' )

  return

def collatz ( key ):

#*****************************************************************************80
#
## collatz() computes the Collatz sequence for a given starting point.
#
#  Discussion:
#
#    The Collatz sequence is defined recursively as follows:
#
#      Let T be the current entry of the sequence, and U the next:
#
#      If T = 1, the sequence terminates (or U = 1, your choice)
#      Else if T is even, U = T / 2
#      Else (if T is odd, and greater than 1) U = 3 * T + 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer key: the starting point for the sequence.
#    key must be positive.
#
#  Output:
#
#    integer S[*]: the Collatz sequence, starting with key.
#    Once the sequence reaches the value 1, no more entries are computed.
#
  import numpy as np

  s = []

  if ( key <= 0 ):
    return s

  t = key
  s.append ( t )

  while ( t != 1 ):

    if ( ( t % 2 ) == 0 ):
      t = t // 2
    else:
      t = 3 * t + 1

    s.append ( t )

  return s

def collatz_count ( key ):

#*****************************************************************************80
#
## collatz_count(): length of the Collatz sequence for a given starting point.
#
#  Discussion:
#
#    The Collatz sequence is defined recursively as follows:
#
#      Let T be the current entry of the sequence, and U the next:
#
#      If T = 1, the sequence terminates (or U = 1, your choice)
#      Else if T is even, U = T / 2
#      Else (if T is odd, and greater than 1) U = 3 * T + 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer key, the starting point for the sequence.
#    key must be positive.
#
#  Output:
#
#    integer N, the length of the sequence.
#
  if ( key <= 0 ):
    n = -1
    return n

  n = 1
  t = key

  while ( t != 1 ):

    if ( ( t % 2 ) == 0 ):
      t = t // 2
    else:
      t = 3 * t + 1

    n = n + 1

  return n

def collatz_count_test ( ):

#*****************************************************************************80
#
## collatz_count_test() tests collatz_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'collatz_count_test():' )
  print ( '  collatz_count() computes the length of the Collatz sequence' )
  print ( '  for a given key.' )

  for key in range ( 1, 101 ):
      
    n = collatz_count ( key )
    print ( '  %4d  %8d' % ( key, n ) )

  return

def collatz_inverse ( n ):

#*****************************************************************************80
#
## collatz_inverse() returns the Collatz preimage of a set of integers.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n[*]: a numpy array of integers.
#
#  Output:
#
#    integer Tn[*]: the Collatz preimages of the values in n.
#
  import numpy as np
#
#  Compute even preimages.
#
  Tn = 2 * n.copy ( )
#
#  We don't count 1-->4
#
  two = ( n % 3 == 1 ) & ( n != 4 )
  S = ( n[two] - 1 ) // 3
#
#  Add odd preimages.
#
  for s in S:
    if ( s % 2 == 1 ):
      Tn = np.append ( Tn, s )
#
#  Unique, sorted list.
#
  Tn = np.unique ( Tn )

  return Tn

def collatz_inverse_test ( ):

#*****************************************************************************80
#
## collatz_inverse_test() tests collatz_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'collatz_inverse_test():' )
  print ( '  collatz_inverse() computes the preimage of a set of' )
  print ( '  integers under the Collatz transformation.' )

  for step in range ( 0, 8 ):
      
    if ( step == 0 ):
      n = np.array ( [ 7 ] )
    else:
      n = collatz_inverse ( n )

    print ( n )

  return

def collatz_max ( key ):

#*****************************************************************************80
#
## collatz_max() returns the largest element of a Collatz sequence.
#
#  Discussion:
#
#    The Collatz sequence is defined recursively as follows:
#
#      Let T be the current entry of the sequence, and U the next:
#
#      If T = 1, the sequence terminates (or U = 1, your choice)
#      Else if T is even, U = T / 2
#      Else (if T is odd, and greater than 1) U = 3 * T + 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer key, the starting point for the sequence.
#    key must be positive.
#
#  Output:
#
#    integer M: the maximum element of the sequence.
#
  m = key

  if ( key <= 0 ):
    return m

  t = key

  while ( t != 1 ):

    if ( ( t % 2 ) == 0 ):
      t = t // 2
    else:
      t = 3 * t + 1

    m = max ( m, t )

  return m

def collatz_max_test ( ):

#*****************************************************************************80
#
## collatz_max_test() tests collatz_max().
#
#  Discussion:
#
#    Plot the maximum value in a Collatz sequence starting at n,
#    for n between 1 and 100.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'collatz_max_test():' )
  print ( '  Plot the Collatz max values' )

  n = 100
  t = np.linspace ( 1, n, n )
  m = np.zeros ( n )

  for key in range ( 1, n + 1 ):
    m[key-1] = collatz_max ( key )

  plt.bar ( t, m ) 
  plt.grid ( True )
  plt.xlabel ( 'Start' )
  plt.ylabel ( 'Maximum Value' )
  plt.title ( 'Maximum value in sequence, for key 1 to' + str ( n ) )
  filename = 'collatz_max.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def collatz_test01 ( ):

#*****************************************************************************80
#
## collatz_test01() tests collatz().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 5
  key_test = np.array ( [ 5, 6, 19, 27, 95 ] )

  print ( '' )
  print ( 'collatz_test01():' )
  print ( '  collatz() computes the Collatz sequence for a given key.' )

  for key in key_test:

    s = collatz ( key )
    n = len ( s )

    print ( '' )
    print ( '  key:', key )
    print ( '  Sequence length:', n )
    print ( '' )
    print ( s )

  return

def collatz_test03 ( ):

#*****************************************************************************80
#
## collatz_test03() tests writes data to files.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'collatz_test03():' )
  print ( '  Write Collatz sequence data to a file.' )

  key = 27
  s = collatz ( key )
 
  filename = 'collatz_27.txt'
  np.savetxt ( filename, s )
  print ( '  Data saved as "' + filename + '"' )
    
  n = 100
  c = np.zeros ( n )
  for key in range ( 1, n + 1 ):
    c[key-1] = collatz_count ( key )

  filename = 'collatz_count.txt'
  np.savetxt ( filename, c )
  print ( '  Data saved as "' + filename + '"' )

  return

def collatz_test04 ( ):

#*****************************************************************************80
#
## collatz_test04() plots the points of a Collatz sequence.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'collatz_test04():' )
  print ( '  Plot the points of a Collatz sequence.' )

  key = 27
  s = collatz ( key )
  n = len ( s )

  plt.plot ( s, 'b.-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( 'Index' )
  plt.ylabel ( 'Value' )
  plt.title ( 'Collatz sequence key = 27, takes ' + str ( n ) + ' steps!' )
  filename = 'collatz_sequence_27.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def collatz_test06 ( ):

#*****************************************************************************80
#
## collatz_test06() plots the Collatz count.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  n = 100

  print ( '' )
  print ( 'collatz_test06():' )
  print ( '  Plot the Collatz count for starting values 1 to', n )

  t = np.linspace ( 1, n, n )
  c = np.zeros ( n )
  for key in range (  1, n + 1 ):
    c[key-1] = collatz_count ( key )

  plt.bar ( t, c )
  plt.grid ( True )
  plt.xlabel ( 'Start' )
  plt.ylabel ( 'Length' )
  plt.title ( 'Length of Collatz sequence for key = 1 to ' + str ( n ) )
  filename = 'collatz_count.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def mollatz ( key ):

#*****************************************************************************80
#
## mollatz() computes the mollatz sequence for a given starting point.
#
#  Discussion:
#
#    The mollatz sequence is defined recursively as follows:
#
#      Let T be the current entry of the sequence, and U the next:
#
#      If T = repeats a previous value, the sequence terminates
#      Else if T is even, U = T / 2
#      Else (if T is odd, and greater than 1) U = 3 * T - 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer key: the starting point for the sequence.
#    key must be positive.
#
#  Output:
#
#    integer S[*]: the mollatz sequence, starting with key.
#
  import numpy as np

  s = []

  if ( key <= 0 ):
    return s

  t = key
  s.append ( t )

  while ( True ):

    if ( ( t % 2 ) == 0 ):
      t = t // 2
    else:
      t = 3 * t - 1
 
    if ( np.any ( s == t ) ):
      s.append ( t )
      break

    s.append ( t )

  return s

def mollatz_test ( ):

#*****************************************************************************80
#
## mollatz_test() tests mollatz().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  key_test = np.array ( [ 5, 6, 19, 27, 95 ] )

  print ( '' )
  print ( 'mollatz_test()' )
  print ( '  mollatz() computes the Mollatz sequence for a given key.' )

  for key in key_test:

    s = mollatz ( key )
    n = len ( s )

    print ( '' )
    print ( '  key:', key )
    print ( '  Sequence length:', n )
    print ( '' )
    print ( s )

  return

def nollatz ( key ):

#*****************************************************************************80
#
## nollatz() computes the "Nollatz" sequence for a given starting point.
#
#  Discussion:
#
#    The Nollatz sequence is defined recursively as follows:
#
#      Let T be the current entry of the sequence, and U the next:
#
#      If T = 1, the sequence terminates (or U = 1, your choice)
#      Else if T is even, U = T / 2
#      Else (if T is odd, and greater than 1) U = T + 1.
#
#    It can be shown that, for any starting point, the sequence always
#    terminates at 1 in finitely many steps.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer key: the starting point for the sequence.
#    key must be positive.
#
#  Output:
#
#    integer S[*]: the Nollatz sequence, starting with key.
#    Once the sequence reaches the value 1, no more entries are computed.
#
  import numpy as np

  s = []

  if ( key <= 0 ):
    return s

  t = key
  s.append ( t )

  while ( t != 1 ):

    if ( ( t % 2 ) == 0 ):
      t = t // 2
    else:
      t = t + 1

    s.append ( t )

  return s

def nollatz_test ( ):

#*****************************************************************************80
#
## nollatz_test() tests nollatz().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  key_test = np.array ( [ 5, 6, 19, 27, 95 ] )

  print ( '' )
  print ( 'nollatz_test():' )
  print ( '  nollatz() computes the Nollatz sequence for a given key.' )

  for key in key_test:

    s = nollatz ( key )
    n = len ( s )

    print ( '' )
    print ( '  key:', key )
    print ( '  Sequence length:', n )
    print ( '' )
    print ( s )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  collatz_test ( )
  timestamp ( )

