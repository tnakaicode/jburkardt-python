#! /usr/bin/env python3
#
def r8_fraction ( i, j ):

#*****************************************************************************80
#
## R8_FRACTION uses real arithmetic on an integer ratio.
#
#  Discussion:
#
#    Given integer variables I and J, both FORTRAN and C will evaluate 
#    an expression such as "I/J" using what is called "integer division",
#    with the result being an integer.  It is often convenient to express
#    the parts of a fraction as integers but expect the result to be computed
#    using real arithmetic.  This function carries out that operation.
#
#  Example:
#
#       I     J   I/J  R8_FRACTION
#
#       1     2     0  0.5
#       7     4     1  1.75
#       8     4     2  2.00
#       9     4     2  2.25
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the arguments.
#
#    Output, real R8_FRACTION, the value of the ratio.
#
  value = float ( i ) / float ( j )

  return value

def r8_fraction_test ( ):

#*****************************************************************************80
#
## R8_FRACTION_TEST tests R8_FRACTION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4_uniform_ab import i4_uniform_ab

  print ( '' )
  print ( 'R8_FRACTION_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_FRACTION computes a ratio of integers using real arithmetic.' )

  print ( '' )
  print ( '       I       J     I/J  R8_FRACTION(I,J)' )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):

    i1, seed = i4_uniform_ab ( 1, 20, seed )
    i2, seed = i4_uniform_ab ( 1, 20, seed )
    print ( '  %6d  %6d  %6d  %g' % ( i1, i2, i1 / i2, r8_fraction ( i1, i2 ) ) )
 
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_FRACTION_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_fraction_test ( )
  timestamp ( )
 
  
