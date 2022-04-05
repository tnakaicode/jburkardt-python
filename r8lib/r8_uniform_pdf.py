#! /usr/bin/env python
#
def r8_uniform_pdf ( lower, upper, rval ):

#*****************************************************************************80
#
## R8_UNIFORM_PDF evaluates the PDF of a uniform distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real LOWER, UPPER, the lower and upper range limits.
#    LOWER < UPPER.
#
#    Input, real RVAL, the point where the PDF is evaluated.
#
#    Output, real VALUE, the value of the PDF at RVAL.
#
  from sys import exit

  if ( upper <= lower ):
    print ( '' )
    print ( 'R8_UNIFORM_PDF - Fatal error!' )
    print ( '  For uniform PDF, the lower limit must be ' )
    print ( '  less than the upper limit.' )
    exit ( 'R8_UNIFORM_PDF - Fatal error!' )

  if ( rval < lower ):
    value = 0.0
  elif ( rval <= upper ):
    value = 1.0 / ( upper - lower )
  else:
    value = 0.0

  return value

def r8_uniform_pdf_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_PDF_TEST tests R8_UNIFORM_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt.
#
  import platform
  from r8_uniform_ab import r8_uniform_ab

  print ( '' )
  print ( 'R8_UNIFORM_PDF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_PDF evaluates the uniform pdf over [A,B].' )
  print ( '' )
  print ( '            A               B               X           PDF()' )
  print ( '' )
  
  seed = 123456789

  for i in range ( 0, 10 ):

    a, seed = r8_uniform_ab ( -100.0, +100.0, seed )
    b, seed = r8_uniform_ab ( -100.0, +100.0, seed )
    t = max ( a, b )
    a = min ( a, b )
    b = t
    x, seed = r8_uniform_ab ( -100.0, +100.0, seed )

    pdf = r8_uniform_pdf ( a, b, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( a, b, x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_uniform_pdf_test ( )
  timestamp ( )
 
