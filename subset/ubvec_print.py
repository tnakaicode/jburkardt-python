#! /usr/bin/env python
#
def ubvec_print ( n, ubvec, title ):

#*****************************************************************************80
#
## UBVEC_PRINT prints a UBVEC, with an optional title.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  UBVEC(1) is the units digit, UBVEC(N)
#    is the coefficient of 2^(N-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, integer UBVEC(N), the vector to be printed.
#
#    Input, character ( len = * ) TITLE, a title to be printed first.
#    TITLE may be blank.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  for ihi in range ( n - 1, -1, -70 ):
    ilo = max ( ihi - 70 + 1, 0 )
    print ( '  ' ),
    for i in range ( ihi, ilo - 1, -1 ):
      print ( '%1d' % ( ubvec[i] ) ),
    print ( '' )

  return

def ubvec_print_test ( ):

#*****************************************************************************80
#
## UBVEC_PRINT_TEST tests UBVEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  ubvec = np.array ( [ 1, 0, 0, 1, 0, 1, 1, 1, 0, 0 ] )

  print ( '' )
  print ( 'UBVEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UBVEC_PRINT prints an unsigned binary vector.' )

  ubvec_print ( n, ubvec, '  UBVEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'UBVEC_PRINT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ubvec_print_test ( )
  timestamp ( )

