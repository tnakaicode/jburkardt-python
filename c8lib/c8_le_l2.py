#! /usr/bin/env python
#
def c8_le_l2 ( c1, c2 ):

#*****************************************************************************80
#
## C8_LE_L2 := C1 <= C1 for C8's, and the L2 norm.
#
#  Discussion:
#
#    The L2 norm can be defined here as:
#
#      C8_NORM_L2(C) = sqrt ( ( real (C) ) ^ 2 + abs ( imag (C) ) ^ 2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, complex C1, C2, the values to be compared.
#
#    Output, boolean VALUE, is TRUE if C1 <= C2.
#
  if ( c1.real ** 2 + c1.imag ** 2 <= c2.real ** 2 + c2.imag ** 2 ) :
    value = True
  else:
    value = False

  return value

def c8_le_l2_test ( ):

#*****************************************************************************80
#
## C8_LE_L2_TEST tests C8_LE_L2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from c8_uniform_01 import c8_uniform_01

  print ( '' )
  print ( 'C8_LE_L2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  C8_LE_L2 evalues (C1 <= C2) using the L2 norm.' )
  print ( '' )
  print ( '       C1=C8_UNIFORM_01          C2=C8_UNIFORM_01          L3=C8_LE_L2(C1,C2)' )
  print ( '     ---------------------     ---------------------     ---------------------' )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2, seed = c8_uniform_01 ( seed )
    l3 = c8_le_l2 ( c1, c2 )
    print ( '  (%12f,%12f)  (%12f,%12f)  %s' \
      % ( c1.real, c1.imag, c2.real, c2.imag, l3 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'C8_LE_L2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_le_l2_test ( )
  timestamp ( )

