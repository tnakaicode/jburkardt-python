#! /usr/bin/env python3
#
def i4cf_evaluate ( n, a, b ):

#*****************************************************************************80
#
## I4CF_EVALUATE evaluates a continued fraction with I4 entries.
#
#  Discussion:
#
#    For convenience, we omit the parentheses or multiline display.
#
#    CF = A(0) + B(1) / A(1) + B(2) / A(2) + ... A(N-1) + B(N) / A(N).
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Hart, Ward Cheney, Charles Lawson, Hans Maehly, Charles Mesztenyi,
#    John Rice, Henry Thatcher, Christoph Witzgall,
#    Computer Approximations,
#    Wiley, 1968.
#
#  Parameters:
#
#    Input, integer N, the number of continued fraction
#    coefficients.
#
#    Input, integer A(0:N), B(0:N), the continued fraction 
#    coefficients.
#
#    Output, integer P(0:N), Q(0:N), the N+1 successive 
#    approximations to the value of the continued fraction.
#
  import numpy as np

  p = np.zeros ( n + 1, dtype = np.int32 )
  q = np.zeros ( n + 1, dtype = np.int32 )

  for i in range ( 0, n + 1 ):

    if ( i == 0 ):
      p[i] = a[i] * 1 + 0
      q[i] = a[i] * 0 + 1
    elif ( i == 1 ):
      p[i] = a[i] * p[i-1] + b[i] * 1
      q[i] = a[i] * q[i-1] + b[i] * 0
    else:
      p[i] = a[i] * p[i-1] + b[i] * p[i-2]
      q[i] = a[i] * q[i-1] + b[i] * q[i-2]

  return p, q

def i4cf_evaluate_test ( ):

#*****************************************************************************80
#
## I4CF_EVALUATE_TEST tests I4CF_EVALUATE.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 19

  a = np.array ( [ \
    3, \
    6, 6, 6, 6, 6, \
    6, 6, 6, 6, 6, \
    6, 6, 6, 6, 6, \
    6, 6, 6, 6 ] )

  b = np.array ( [ \
      0, \
      1,    9,   25,   49,   81, \
    121,  169,  225,  289,  361, \
    441,  529,  625,  729,  841, \
    961, 1089, 1225, 1369 ] )

  print ( '' )
  print ( 'I4CF_EVALUATE_TEST:' )

  p, q = i4cf_evaluate ( n, a, b )

  print ( '' )
  print ( '  CF numerators, denominators, ratios:' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    t = float ( p[i] ) / float ( q[i] )
    print ( '  %2d  %12d  %12d  %24.16f' % (  i, p[i], q[i], t ) )

  return

def i4scf_evaluate ( n, a ):

#*****************************************************************************80
#
## I4SCF_EVALUATE evaluates a simple continued fraction with I4 entries.
#
#  Discussion:
#
#    The simple continued fraction with integer coefficients is:
#
#      SCF = A(0) + 1 / ( A(1) + 1 / ( A(2) ... + 1 / A(N) ) )
#
#    This routine returns the successive approximants P[i]/Q[i]
#    to the value of the rational number represented by the continued
#    fraction, with the value exactly equal to the final ratio P(N)/Q(N).
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Hart, Ward Cheney, Charles Lawson, Hans Maehly, Charles Mesztenyi,
#    John Rice, Henry Thatcher, Christoph Witzgall,
#    Computer Approximations,
#    Wiley, 1968.
#
#  Parameters:
#
#    Input, integer N, the number of continued fraction
#    coefficients.
#
#    Input, integer A(0:N), the continued fraction coefficients.
#
#    Output, integer P(0:N), Q(0:N), the numerators and
#    denominators of the successive approximations.
#
  import numpy as np

  p = np.zeros ( n + 1, dtype = np.int32 )
  q = np.zeros ( n + 1, dtype = np.int32 )

  for i in range ( 0, n + 1 ):

    if ( i == 0 ):
      p[i] = a[i] * 1 + 0
      q[i] = a[i] * 0 + 1
    elif ( i == 1 ):
      p[i] = a[i] * p[i-1] + 1
      q[i] = a[i] * q[i-1] + 0
    else:
      p[i] = a[i] * p[i-1] + p[i-2]
      q[i] = a[i] * q[i-1] + q[i-2]

  return p, q

def i4scf_evaluate_test ( ):

#*****************************************************************************80
#
## I4SCF_EVALUATE_TEST tests I4SCF_EVALUATE.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 19

  a = np.array ( [ \
    3, 7, 15, 1, 292, \
    1, 1,  1, 2,   1, \
    3, 1, 14, 2,   1, \
    1, 2,  2, 2,   2 ] )

  print ( '' )
  print ( 'I4SCF_EVALUATE_TEST:' )

  p, q = i4scf_evaluate ( n, a )

  print ( '' )
  print ( '  SCF numerators, denominators, ratios:' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    t = float ( p[i] ) / float ( q[i] )
    print ( '  %2d  %12d  %12d  %24.16f' % (  i, p[i], q[i], t ) )

  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## I4VEC_PRINT prints an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, integer A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_print_test ( ):

#*****************************************************************************80
#
## I4VEC_PRINT_TEST tests I4VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_PRINT prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i8cf_evaluate ( n, a, b ):

#*****************************************************************************80
#
## I8CF_EVALUATE evaluates a continued fraction with I8 entries.
#
#  Discussion:
#
#    For convenience, we omit the parentheses or multiline display.
#
#    CF = A(0) + B(1) / A(1) + B(2) / A(2) + ... A(N-1) + B(N) / A(N).
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Hart, Ward Cheney, Charles Lawson, Hans Maehly, Charles Mesztenyi,
#    John Rice, Henry Thatcher, Christoph Witzgall,
#    Computer Approximations,
#    Wiley, 1968.
#
#  Parameters:
#
#    Input, integer N, the number of continued fraction
#    coefficients.
#
#    Input, integer A(0:N), B(0:N), the continued fraction 
#    coefficients.
#
#    Output, integer P(0:N), Q(0:N), the N successive 
#    approximations to the value of the continued fraction.
#
  import numpy as np

  p = np.zeros ( n + 1, dtype = np.int64 )
  q = np.zeros ( n + 1, dtype = np.int64 )

  for i in range ( 0, n + 1 ):

    if ( i == 0 ):
      p[i] = a[i] * 1 + 0
      q[i] = a[i] * 0 + 1
    elif ( i == 1 ):
      p[i] = a[i] * p[i-1] + b[i] * 1
      q[i] = a[i] * q[i-1] + b[i] * 0
    else:
      p[i] = a[i] * p[i-1] + b[i] * p[i-2]
      q[i] = a[i] * q[i-1] + b[i] * q[i-2]

  return p, q

def i8cf_evaluate_test ( ):

#*****************************************************************************80
#
## I8CF_EVALUATE_TEST tests I8CF_EVALUATE.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 19

  a = np.array ( [ \
    3, \
    6, 6, 6, 6, 6, \
    6, 6, 6, 6, 6, \
    6, 6, 6, 6, 6, \
    6, 6, 6, 6 ] )

  b = np.array ( [ \
      0, \
      1,    9,   25,   49,   81, \
    121,  169,  225,  289,  361, \
    441,  529,  625,  729,  841, \
    961, 1089, 1225, 1369 ] )

  print ( '' )
  print ( 'I8CF_EVALUATE_TEST:' )

  p, q = i8cf_evaluate ( n, a, b )

  print ( '' )
  print ( '  CF numerators, denominators, ratios:' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    t = float ( p[i] ) / float ( q[i] )
    print ( '  %2d  %20d  %20d  %24.16f' % (  i, p[i], q[i], t ) )

  return

def i8scf_evaluate ( n, a ):

#*****************************************************************************80
#
## I8SCF_EVALUATE evaluates a simple continued fraction with I8 entries.
#
#  Discussion:
#
#    The simple continued fraction with integer coefficients is:
#
#      SCF = A(0) + 1 / ( A(1) + 1 / ( A(2) ... + 1 / A(N) ) )
#
#    This routine returns the successive approximants P[i]/Q[i]
#    to the value of the rational number represented by the continued
#    fraction, with the value exactly equal to the final ratio P(N)/Q(N).
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Hart, Ward Cheney, Charles Lawson, Hans Maehly, Charles Mesztenyi,
#    John Rice, Henry Thatcher, Christoph Witzgall,
#    Computer Approximations,
#    Wiley, 1968.
#
#  Parameters:
#
#    Input, integer N, the number of continued fraction
#    coefficients.
#
#    Input, integer A(0:N), the continued fraction coefficients.
#
#    Output, integer P(0:N), Q(0:N), the numerators and
#    denominators of the successive approximations.
#
  import numpy as np

  p = np.zeros ( n + 1, dtype = np.int64 )
  q = np.zeros ( n + 1, dtype = np.int64 )

  for i in range ( 0, n + 1 ):

    if ( i == 0 ):
      p[i] = a[i] * 1 + 0
      q[i] = a[i] * 0 + 1
    elif ( i == 1 ):
      p[i] = a[i] * p[i-1] + 1
      q[i] = a[i] * q[i-1] + 0
    else:
      p[i] = a[i] * p[i-1] + p[i-2]
      q[i] = a[i] * q[i-1] + q[i-2]

  return p, q

def i8scf_evaluate_test ( ):

#*****************************************************************************80
#
## I8SCF_EVALUATE_TEST tests I8SCF_EVALUATE.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 19

  a = np.array ( [ \
    3, 7, 15, 1, 292, \
    1, 1,  1, 2,   1, \
    3, 1, 14, 2,   1, \
    1, 2,  2, 2,   2 ] )

  print ( '' )
  print ( 'I8SCF_EVALUATE_TEST:' )

  p, q = i8scf_evaluate ( n, a )

  print ( '' )
  print ( '  SCF numerators, denominators, ratios:' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    t = float ( p[i] ) / float ( q[i] )
    print ( '  %2d  %20d  %20d  %24.16f' % (  i, p[i], q[i], t ) )

  return

def i8vec_print ( n, a, title ):

#*****************************************************************************80
#
## I8VEC_PRINT prints an I8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, integer A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i8vec_print_test ( ):

#*****************************************************************************80
#
## I8VEC_PRINT_TEST tests I8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I8VEC_PRINT prints an I4VEC.' )

  n = 3
  v = np.array ( [ 123456789, 1234567890987654321, -7 ], dtype = np.int64 )
  i8vec_print ( n, v, '  Here is an I8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_to_i4scf ( r, n ):

#*****************************************************************************80
#
## R8_TO_I4SCF approximates an R8 with an I4 simple continued fraction.
#
#  Discussion:
#
#    The simple continued fraction with real coefficients is:
#
#      SCF = A(0) + 1 / ( A(1) + 1 / ( A(2) ... + 1 / A(N) ) )
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Norman Richert,
#    Strang's Strange Figures,
#    American Mathematical Monthly,
#    Volume 99, Number 2, February 1992, pages 101-107.
#
#  Parameters:
#
#    Input, real R, the real value.
#
#    Input, integer N, the number of convergents to compute.
#
#    Output, integer A(0:N), the partial quotients.
#
  import numpy as np

  a = np.zeros ( n + 1, dtype = np.int32 )

  if ( r == 0.0 ):
    return a

  r2 = r
  a[0] = int ( r2 )

  for i in range ( 1, n + 1 ):
    r2 = 1.0 / ( r2 - float ( a[i-1] ) )
    a[i] = int ( r2 )

  return a

def r8_to_i4scf_test ( ):

#*****************************************************************************80
#
## R8_TO_I4SCF_TEST tests R8_TO_I4SCF.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 19

  print ( '' )
  print ( 'R8_TO_I4SCF_TEST:' )

  r = np.pi

  a = r8_to_i4scf ( r, n )

  i4vec_print ( n + 1, a, '  SCF coefficients:' )

  p, q = i4scf_evaluate ( n, a )

  print ( '' )
  print ( '  SCF numerators, denominators, ratios:' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    t = float ( p[i] ) / float ( q[i] )
    print ( '  %2d  %12d  %12d  %24.16f' % (  i, p[i], q[i], t ) )

  return

def r8_to_i8scf ( r, n ):

#*****************************************************************************80
#
## R8_TO_I8SCF approximates an R8 with an I8 simple continued fraction.
#
#  Discussion:
#
#    The simple continued fraction with real coefficients is:
#
#      SCF = A(0) + 1 / ( A(1) + 1 / ( A(2) ... + 1 / A(N) ) )
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Norman Richert,
#    Strang's Strange Figures,
#    American Mathematical Monthly,
#    Volume 99, Number 2, February 1992, pages 101-107.
#
#  Parameters:
#
#    Input, real R, the real value.
#
#    Input, integer N, the number of convergents to compute.
#
#    Output, integer A(0:N), the partial quotients.
#
  import numpy as np

  a = np.zeros ( n + 1, dtype = np.int64 )

  if ( r == 0.0 ):
    return a

  r2 = r
  a[0] = int ( r2 )

  for i in range ( 1, n + 1 ):
    r2 = 1.0 / ( r2 - float ( a[i-1] ) )
    a[i] = int ( r2 )

  return a

def r8_to_i8scf_test ( ):

#*****************************************************************************80
#
## R8_TO_I8SCF_EVALUATE_TEST tests R8_TO_I8SCF.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 19

  print ( '' )
  print ( 'R8_TO_I8SCF_TEST:' )

  r = np.pi

  a = r8_to_i8scf ( r, n )

  i8vec_print ( n + 1, a, '  SCF coefficients:' )

  p, q = i8scf_evaluate ( n, a )

  print ( '' )
  print ( '  SCF numerators, denominators, ratios:' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    t = float ( p[i] ) / float ( q[i] )
    print ( '  %2d  %20d  %20d  %24.16f' % (  i, p[i], q[i], t ) )

  return

def r8cf_evaluate ( n, a, b ):

#*****************************************************************************80
#
## R8CF_EVALUATE evaluates a continued fraction with R8 entries.
#
#  Discussion:
#
#    For convenience, we omit the parentheses or multiline display.
#
#    CF = A(0) + B(1) / A(1) + B(2) / A(2) + ... A(N-1) + B(N) / A(N).
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of terms.
#
#    Input, real A(0:N), B(0:N), the continued fraction
#    terms.
#
#    Output, real P(0:N), Q(0:N), the numerators
#    and denominators of the successive partial sums of the continued
#    fraction.
#
  import numpy as np

  p = np.zeros ( n + 1, dtype = np.float64 )
  q = np.zeros ( n + 1, dtype = np.float64 )

  for i in range ( 0, n + 1 ):

    if ( i == 0 ):
      p[i] = a[i] * 1.0 + 0.0
      q[i] = a[i] * 0.0 + 1.0
    elif ( i == 1 ):
      p[i] = a[i] * p[i-1] + b[i] * 1.0
      q[i] = a[i] * q[i-1] + b[i] * 0.0
    else:
      p[i] = a[i] * p[i-1] + b[i] * p[i-2]
      q[i] = a[i] * q[i-1] + b[i] * q[i-2]

  return p, q

def r8cf_evaluate_test ( ):

#*****************************************************************************80
#
## R8CF_EVALUATE_TEST tests R8CF_EVALUATE.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 20

  print ( '' )
  print ( 'R8CF_EVALUATE_TEST:' )

  a = np.zeros ( n + 1, dtype = np.float64 )
  a[0] = 3.0
  a[1:n+1] = 6.0

  b = np.zeros ( n + 1, dtype = np.float64 )
  b[0] = 0.0
  for i in range ( 1, n + 1 ):
    t = float ( 2 * i - 1 )
    b[i] = t * t

  p, q = r8cf_evaluate ( n, a, b )

  print ( '' )
  print ( '  CF numerators, denominators, ratios:' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    print ( '  %2d  %28.0f  %28.0f  %24.16f' % (  i, p[i], q[i], p[i] / q[i] ) )

  return

def r8scf_evaluate ( n, a ):

#*****************************************************************************80
#
## R8SCF_EVALUATE evaluates a simple continued fraction with R8 entries.
#
#  Discussion:
#
#    The simple continued fraction with real coefficients is:
#
#      SCF = A(0) + 1 / ( A(1) + 1 / ( A(2) ... + 1 / A(N) ) )
#
#    This routine returns the N successive approximants P[i]/Q[i]
#    to the value of the rational number represented by the continued
#    fraction, with the value exactly equal to the final ratio C(N)/D(N).
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of continued fraction
#    coefficients.
#
#    Input, real A(0:N), the continued fraction coefficients.
#
#    Output, real P(0:N), Q(0:N), the numerators and
#    denominators of the successive approximations.
#
  import numpy as np

  p = np.zeros ( n + 1, dtype = np.float64 )
  q = np.zeros ( n + 1, dtype = np.float64 )

  for i in range ( 0, n + 1 ):

    if ( i == 0 ):
      p[i] = a[i] * 1.0 + 0.0
      q[i] = a[i] * 0.0 + 1.0
    elif ( i == 1 ):
      p[i] = a[i] * p[i-1] + 1.0
      q[i] = a[i] * q[i-1] + 0.0
    else:
      p[i] = a[i] * p[i-1] + p[i-2]
      q[i] = a[i] * q[i-1] + q[i-2]

  return p, q

def r8scf_evaluate_test ( ):

#*****************************************************************************80
#
## R8SCF_EVALUATE_TEST tests R8SCF_EVALUATE.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 19

  a = np.array ( [ \
    3.0, 7.0, 15.0, 1.0, 292.0, \
    1.0, 1.0,  1.0, 2.0,   1.0, \
    3.0, 1.0, 14.0, 2.0,   1.0, \
    1.0, 2.0,  2.0, 2.0,   2.0 ] )

  print ( '' )
  print ( 'R8SCF_EVALUATE_TEST:' )

  p, q = r8scf_evaluate ( n, a )

  print ( '' )
  print ( '  SCF numerators, denominators, ratios:' )
  print ( '' )

  for i in range ( 0, n + 1 ):
    print ( '  %2d  %20f  %20f  %24.16f' % (  i, p[i], q[i], p[i] / q[i] ) )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def continued_fraction_test ( ):

#*****************************************************************************80
#
## CONTINUED_FRACTION_TEST tests the CONTINUED_FRACTION library.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 August 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'CONTINUED_FRACTION_TEST:' )
  print ( '  Python version' )
  print ( '  CONTINUED_FRACTION is a library for dealing with' )
  print ( '  expresssions representing a continued fraction.' )

  i4cf_evaluate_test ( )
  i4scf_evaluate_test ( )
  i8cf_evaluate_test ( )
  i8scf_evaluate_test ( )
  r8_to_i4scf_test ( )
  r8_to_i8scf_test ( )
  r8cf_evaluate_test ( )
  r8scf_evaluate_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONTINUED_FRACTION_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  continued_fraction_test ( )
  timestamp ( )
