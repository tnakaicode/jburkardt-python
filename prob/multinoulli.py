#! /usr/bin/env python
#
def multinoulli_pdf ( x, n, theta ):

#*****************************************************************************80
#
## MULTINOULLI_PDF evaluates the Multinoulli PDF.
#
#  Discussion:
#
#    PDF(X) = THETA(X) for 0 <= X < N.
#           = 0 otherwise
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the index of the outcome.
#    0 <= X < N.
#
#    Input, integer N, the number of legal outcomes.
#
#    Input, real THETA[N], the probability of each outcome.
#
#    Output, real VALUE, the probability of outcome X.
#
  if ( 0 <= x and x < n ):
    value = theta[x]
  else:
    value = 0.0

  return value

def multinoulli_pdf_test ( ):

#*****************************************************************************80
#
## MULTINOULLLI_PDF_TEST tests MULTINOULLI_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_uniform_01 import r8vec_uniform_01

  print ( '' )
  print ( 'MULTINOULLI_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MULTINOULLI_PDF evaluates the Multinoulli PDF.' )

  n = 5
  seed = 123456789
  theta, seed = r8vec_uniform_01 ( n, seed )
  theta_sum = np.sum ( theta )
  theta[0:n] = theta[0:n] / theta_sum

  print ( '' )
  print ( '   X     pdf(X)' )
  print ( '' )
  for x in range ( -1, n + 1 ):
    pdf = multinoulli_pdf ( x, n, theta )
    print ( '  %2d  %14g' % ( x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'MULTINOULLI_PDF_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  multinoulli_pdf_test ( )
  timestamp ( )
 
