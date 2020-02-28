#! /usr/bin/env python
#
def i4_lcm_12n ( n ):

#*****************************************************************************80
#
## I4_LCM_12N computes the least common multiple of the integers 1 through N.
#
#  Examples:
#
#    N    LCM_12N
#
#    1          1
#    2          2
#    3          3
#    4         12
#    5         60
#    6         60
#    7        420
#    8        840
#    9       2520
#   10       2520
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the value of N.
#
#    Output, integer VALUE, the least common multiple of
#    the integers 1 to N.
#
  value = 1

  for i in range ( 2, n + 1 ):

    mult = i

    for j in range ( 1, i ):

      if ( ( mult % ( i - j ) ) == 0 ):
        mult = mult / ( i - j )

    value = value * mult

  return value

def i4_lcm_12n_test ( ):

#*****************************************************************************80
#
## I4_LCM_12N_TEST tests I4_LCM_12N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 August 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'I4_LCM_12N_TEST' )
  print ( '  I4_LCM_12N computes the least common multiple' )
  print ( '  of integer 1 through N' )
  print ( '' )
  print ( '     N   I4_LCM_12N' )
  print ( '' )

  for n in range ( 1, 11 ):
    print ( '  %2d  %10d' % ( n, i4_lcm_12n ( n ) ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_lcm_12n_test ( )
  timestamp ( )