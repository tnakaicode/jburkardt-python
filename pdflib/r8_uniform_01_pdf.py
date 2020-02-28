#! /usr/bin/env python
#
def r8_uniform_01_pdf ( rval ):

#*****************************************************************************80
#
## R8_UNIFORM_01_PDF evaluates the PDF of a standard uniform distribution.
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
#    Input, real RVAL, the point where the PDF is evaluated.
#
#    Output, real VALUE, the value of the PDF at RVAL.
#
  if ( rval < 0.0 ):
    value = 0.0
  elif ( rval <= 1.0 ):
    value = 1.0
  else:
    value = 0.0

  return value

def r8_uniform_01_pdf_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_01_PDF_TEST tests R8_UNIFORM_01_PDF.
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
  print ( 'R8_UNIFORM_01_PDF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_01_PDF evaluates the standard uniform pdf.' )
  print ( '' )
  print ( '            X                           PDF()' )
  print ( '' )
  
  seed = 123456789

  for i in range ( 0, 10 ):

    x, seed = r8_uniform_ab ( -0.5, +1.5, seed )

    pdf = r8_uniform_01_pdf ( x )
    print ( '  %24.16g  %14.6g' % ( x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_01_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_uniform_01_pdf_test ( )
  timestamp ( )
 
