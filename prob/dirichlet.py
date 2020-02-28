#! /usr/bin/env python
#
def dirichlet_check ( n, a ):

#*****************************************************************************80
#
## DIRICHLET_CHECK checks the parameters of the Dirichlet PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components.
#
#    Input, real A(N), the probabilities for each component.
#    Each A(I) should be positive.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True
  positive = False

  for i in range ( 0, n ):

    if ( a[i] <= 0.0 ):
      print ( '' )
      print ( 'DIRICHLET_CHECK - Fatal error!' )
      print ( '  A(I) <= 0.' )
      print ( '  For I = %d' % ( i ) )
      print ( '  A(I) = %f' % ( a[i] ) )
      check = False
      return check
    elif ( 0.0 < a[i] ):
      positive = True

  if ( not positive ):
    print ( '' )
    print ( 'DIRICHLET_CHECK - Fatal error!' )
    print ( '  All parameters are zero!' )
    check = False

  return check

def dirichlet_mean ( n, a ):

#*****************************************************************************80
#
## DIRICHLET_MEAN returns the means of the Dirichlet PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components.
#
#    Input, real A(N), the probabilities for each component.
#    Each A(I) should be positive.
#
#    Output, real MEAN(N), the means of the PDF.
#
  import numpy as np
  from r8vec_sum import r8vec_sum
  
  a_sum = r8vec_sum ( n, a )

  mean = np.zeros ( n )
  for i in range ( 0, n ):
    mean[i] = a[i] / a_sum

  return mean

def dirichlet_moment2 ( n, a ):

#*****************************************************************************80
#
## DIRICHLET_MOMENT2 returns the second moments of the Dirichlet PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components.
#
#    Input, real A(N), the probabilities for each component.
#    Each A(I) should be positive.
#
#    Output, real M2(N,N), the second moments of the PDF.
#
  import numpy as np
  from r8vec_sum import r8vec_sum

  a_sum = r8vec_sum ( n, a )

  m2 = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        m2[i,j] = a[i] * ( a[i] + 1.0 ) / ( a_sum * ( a_sum + 1.0 ) )
      else:
        m2[i,j] = a[i] * a[j] / ( a_sum * ( a_sum + 1.0 ) )

  return m2

def dirichlet_pdf ( x, n, a ):

#*****************************************************************************80
#
## DIRICHLET_PDF evaluates the Dirichlet PDF.
#
#  Discussion:
#
#    PDF(X)(N,A) = Product ( 1 <= I <= N ) X(I)^( A(I) - 1 )
#      * Gamma ( A_SUM ) / A_PROD
#
#    where
#
#      0 < A(I) for all I
#      0 <= X(I) for all I
#      Sum ( 1 <= I <= N ) X(I) = 1
#      A_SUM = Sum ( 1 <= I <= N ) A(I).
#      A_PROD = Product ( 1 <= I <= N ) Gamma ( A(I) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X(N), the argument of the PDF.  Each X(I) should
#    be greater than 0.0, and the X(I)'s must add up to 1.0.
#
#    Input, integer N, the number of components.
#
#    Input, real A(N), the probabilities for each component.
#    Each A(I) should be positive.
#
#    Output, real PDF, the value of the PDF.
#
  from r8_gamma import r8_gamma
  from r8vec_sum import r8vec_sum
  from sys import exit

  tol = 0.0001

  for i in range ( 0, n ):
    if ( x[i] <= 0.0 ):
      print ( '' )
      print ( 'DIRICHLET_PDF - Fatal error!' )
      print ( '  X(I) <= 0.' )
      exit ( 'DIRICHLET_PDF - Fatal error!' )

  x_sum = r8vec_sum ( n, x )

  if ( tol < abs ( x_sum - 1.0 ) ):
    print ( '' )
    print ( 'DIRICHLET_PDF - Fatal error!' )
    print ( '  SUM X(I) =/= 1.' )

  a_sum = r8vec_sum ( n, a )

  a_prod = 1.0
  for i in range ( 0, n ):
    a_prod = a_prod * r8_gamma ( a[i] )

  pdf = r8_gamma ( a_sum ) / a_prod
  for i in range ( 0, n ):
    pdf = pdf * x[i] ** ( a[i] - 1.0 )

  return pdf

def dirichlet_pdf_test ( ):

#*****************************************************************************80
#
## DIRICHLET_PDF_TEST tests DIRICHLET_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print

  n = 3

  print ( '' )
  print ( 'DIRICHLET_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DIRICHLET_PDF evaluates the Dirichlet PDF.' )

  x = np.array ( [ 0.500, 0.125, 0.375 ] )

  a = np.array ( [ 0.250, 0.500, 1.250 ] )

  check = dirichlet_check ( n, a )

  if ( not check ):
    print ( '' )
    print ( 'DIRICHLET_PDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  Number of components N = %6d' % ( n ) )

  r8vec_print ( n, a, '  PDF parameters A:' )
  r8vec_print ( n, x, '  PDF arguments X:' )

  pdf = dirichlet_pdf ( x, n, a )

  print ( '' )
  print ( '  PDF value = %14g' % ( pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DIRICHLET_PDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def dirichlet_sample ( n, a, seed ):

#*****************************************************************************80
#
## DIRICHLET_SAMPLE samples the Dirichlet PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jerry Banks, editor,
#    Handbook of Simulation,
#    Engineering and Management Press Books, 1998, page 169.
#
#  Parameters:
#
#    Input, integer N, the number of components.
#
#    Input, real A(N), the probabilities for each component.
#    Each A(I) should be positive.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), a sample of the PDF.  The entries
#    of X should sum to 1.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from gamma import gamma_sample
  from r8vec_sum import r8vec_sum

  a2 = 0.0
  b2 = 1.0

  x = np.zeros ( n )

  for i in range ( 0, n ):
    c2 = a[i]
    x[i], seed = gamma_sample ( a2, b2, c2, seed )
#
#  Rescale the vector to have unit sum.
#
  x_sum = r8vec_sum ( n, x )
  for i in range ( 0, n ):
    x[i] = x[i] / x_sum

  return x, seed

def dirichlet_sample_test ( ):

#*****************************************************************************80
#
## DIRICHLET_SAMPLE_TEST tests DIRICHLET_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print
  from r8row_max import r8row_max
  from r8row_mean import r8row_mean
  from r8row_min import r8row_min
  from r8row_variance import r8row_variance
  from r8vec_print import r8vec_print

  n = 3
  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'DIRICHLET_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DIRICHLET_SAMPLE samples the Dirichlet distribution' )
  print ( '  DIRICHLET_MEAN computes the Dirichlet mean' )
  print ( '  DIRICHLET_VARIANCE computes the Dirichlet variance.' )

  a = np.array ( [ 0.250, 0.500, 1.250 ] )

  check = dirichlet_check ( n, a )

  if ( not check ):
    print ( '' )
    print ( 'DIRICHLET_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  Number of components N = %6d' % ( n ) )

  r8vec_print ( n, a, '  PDF parameters A:' )

  mean = dirichlet_mean ( n, a )

  variance = dirichlet_variance ( n, a )

  print ( '' )
  print ( '  PDF mean, variance:' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %6d  %14g  %14g' % ( i, mean[i], variance[i] ) )

  m2 = dirichlet_moment2 ( n, a )
  
  r8mat_print ( n, n, m2, '  Second moment matrix:' )

  x = np.zeros ( [ n, nsample ] )
  for j in range ( 0, nsample ):
    v, seed = dirichlet_sample ( n, a, seed )
    for i in range ( 0, n ):
      x[i,j] = v[i]
 
  xmax = r8row_max ( n, nsample, x )
  xmin = r8row_min ( n, nsample, x )
  mean = r8row_mean ( n, nsample, x )
  variance = r8row_variance ( n, nsample, x )

  print ( '' )
  print ( '  Sample size = %d' % ( nsample ) )

  print ( '' )
  print ( '  Observed Min, Max, Mean, Variance:' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %6d  %14g  %14g  %14g  %14g' \
    % ( i, xmin[i], xmax[i], mean[i], variance[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DIRICHLET_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def dirichlet_variance ( n, a ):

#*****************************************************************************80
#
## DIRICHLET_VARIANCE returns the variances of the Dirichlet PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components.
#
#    Input, real A(N), the probabilities for each component.
#    Each A(I) should be positive.
#
#    Output, real VARIANCE(N), the variances of the PDF.
#
  import numpy as np
  from r8vec_sum import r8vec_sum

  a_sum = r8vec_sum ( n, a )

  variance = np.zeros ( n )

  for i in range ( 0, n ):
    variance[i] = a[i] * ( a_sum - a[i] ) / ( a_sum ** 2 * ( a_sum + 1.0 ) )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  dirichlet_pdf_test ( )
  dirichlet_sample_test ( )
  timestamp ( )
 
