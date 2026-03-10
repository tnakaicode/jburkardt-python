#! /usr/bin/env python3
#
def collatz ( n ):

#*****************************************************************************80
#
## collatz() applies one step of the Collatz iteration to an integer.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the starting value.
#
#  Output:
#
#    integer n2: the transformed value.
#
  if ( not isinstance ( n, int ) ):
    raise Exception ( 'collatz: type(n) = ', type ( n ), \
      ', but n must be an integer.' )
  elif ( n < 1 ):
    raise Exception ( 'collatz: n =', n, ', but 1 <= n required.' )
  elif ( ( n % 2 ) == 0 ):
    n2 = n // 2
  else:
    n2 = 3 * n + 1

  return n2

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
#    11 June 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'collatz_test():' )
  print ( '  collatz() applies one step of the Collatz iteration.' )
  print ( '' )

  for n in [ 0, 1, 5, 15, 27 ]:
    try:
      n2 = collatz ( n )
      print ( n, n2 )
    except Exception:
      print ( '  collatz(', n,' ) calculation failed.' )

  return

def collatz_dict_test ( ):

#*****************************************************************************80
#
## collatz_dict_test() tests collatz_dict().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'collatz_dict_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  collatz_dict() uses a Python dict() for the Collatz problem.' )

  collatz_test ( )
  collatz_fill_test ( )
  collatz_insert_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'collatz_dict_test():' )
  print ( '  Normal end of execution.' )
  return

def collatz_fill ( collatz_dictionary, n_max ):

#*****************************************************************************80
#
## collatz_fill() ensures that every integer up to n_max is in the dictionary.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    dict collatz_dictionary: the current dict.
#
#    integer n_max: the upper bound for which all integers 1 through n_max
#    must be keys in the dictionary.
#
#  Output:
#
#    dict collatz_dictionary: the updated dict.
#

#
#  Note that a dict is initialized using curly braces!
#
  if ( not collatz_dictionary ):
    collatz_dictionary = {}

  for n in range ( 1, n_max + 1 ):

    while ( not ( n in collatz_dictionary ) ):
      n2 = collatz ( n )
      collatz_dictionary[n] = n2
      n = n2

  return collatz_dictionary

def collatz_fill_test ( ):

#*****************************************************************************80
#
## collatz_fill_test() tests collatz_fill().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 June 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'collatz_fill_test():' )
  print ( '  collatz_fill() ensures that the Collatz dictionary includes' )
  print ( '  all integers from 0 to n_max as keys.' )
#
#  Note that a dict is initialized using curly braces!
#
  collatz_dictionary = {}
#
#  Give the dictionary some initial values.
#
  for n in [ 1, 5, 15 ]:
    collatz_dictionary = collatz_insert ( collatz_dictionary, n )

  print ( '' )
  print ( '  collatz_dictionary after a few inserts:' )
  collatz_print_sorted ( collatz_dictionary )
#
#  Now require that 1 through n_max appear for sure.
#
  n_max = 10
  collatz_dictionary = collatz_fill ( collatz_dictionary, n_max )

  print ( '' )
  print ( '  collatz_dictionary after filling up to ' + str ( n_max ) )
  collatz_print_sorted ( collatz_dictionary )

  return

def collatz_insert ( collatz_dictionary, n ):

#*****************************************************************************80
#
## collatz_insert() adds information about integer n to the dict.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    dict collatz_dictionary: the current dict.
#
#    integer n: the starting value.
#
#  Output:
#
#    dict collatz_dictionary: the updated dict.
#

#
#  Note that a dict is initialized using curly braces!
#
  if ( not collatz_dictionary ):
    collatz_dictionary = {}

  while ( not ( n in collatz_dictionary ) ):
    Tn = collatz ( n )
    collatz_dictionary[n] = Tn
    n = Tn

  return collatz_dictionary

def collatz_insert_test ( ):

#*****************************************************************************80
#
## collatz_insert_test() tests collatz_insert().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 June 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'collatz_insert_test():' )
  print ( '  collatz_insert() updates the Collatz dictionary with the' )
  print ( '  information about integer n, and all its iterates.' )
#
#  Note that a dict is initialized using curly braces!
#
  collatz_dictionary = {}

  for n in [ 1, 5, 15, 27 ]:
    collatz_dictionary = collatz_insert ( collatz_dictionary, n )

  collatz_print_sorted ( collatz_dictionary )

  return

def collatz_print ( collatz_dictionary ):

#*****************************************************************************80
#
## collatz_print() prints the Collatz dictionary.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    dict collatz_dictionary: the current dict.
#
  for key, value in bob.items():
    print ( key, value )

  return

def collatz_print_sorted ( collatz_dictionary ):

#*****************************************************************************80
#
## collatz_print_sorted() prints the Collatz dictionary in sorted order.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    dict collatz_dictionary: the current dict.
#

#
#  Alas, you can't make a sorted dict.  
#  All this does is make a sorted list.
#  It prints out OK, but it's not a dict.
#
  bob = sorted ( collatz_dictionary.items( ), key = lambda x: x[0] )

  print ( bob )

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
  collatz_dict_test ( )
  timestamp ( )
