#! /usr/bin/env python
#
def perm_print ( n, p, title ):

#*****************************************************************************80
#
## PERM_PRINT prints a permutation of (1,...,N).
#
#  Example:
#
#    Input:
#
#      P = 7 2 4 1 5 3 6
#
#    Printed output:
#
#      "This is the permutation:"
#
#      1 2 3 4 5 6 7
#      7 2 4 1 5 3 6
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of objects permuted.
#
#    Input, integer P(N), the permutation, in standard index form.
#
#    Input, string TITLE, an optional title.
#    If no title is supplied, then only the permutation is printed.
#
  inc = 20

  if ( len ( title ) != 0 ):

    print ( '' )
    print ( title )

    for ilo in range ( 0, n, inc ):
      ihi = min ( n, ilo + inc )

      print ( '' )
      print ( '  ', end = '' )
      
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( i + 1 ), end = '' )
      print ( '' )

      print ( '  ', end = '' )
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( p[i] ), end = '' )
      print ( '' )

  else:

    for ilo in range ( 0, n, inc ):
      ihi = min ( n, ilo + inc )
      print ( '  ', end = '' )
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( p[i] ), end = '' )
      print ( '' )

  return

def perm_print_test ( ):

#*****************************************************************************80
#
## PERM_PRINT_TEST tests PERM_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'PERM_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_PRINT prints a permutation of (1,...,N).' )

  n = 7
  p = np.array ( [ 7, 2, 4, 1, 5, 3, 6 ] )
  perm_print ( n, p, '  A 1-based permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_PRINT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_print_test ( )
  timestamp ( )

