#! /usr/bin/env python3
#
def colored_noise_test ( ):

#*****************************************************************************80
#
## COLORED_NOISE_TEST tests the COLORED_NOISE library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 July 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'COLORED_NOISE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the COLORED_NOISE library.' )

  r8vec_sftf_test ( )

  n = 128
  q_d = 1.0
  alpha = 0.00
  seed_init = 123456789

  for i in range ( 0, 9 ):
    alpha = 0.25 * float ( i )
    colored_noise_test01 ( n, q_d, alpha, seed_init )

  alpha = 0.0
  colored_noise_test02 ( alpha, 'alpha_0.00_paths.png' )

  alpha = 0.5
  colored_noise_test02 ( alpha, 'alpha_0.50_paths.png' )

  alpha = 1.0
  colored_noise_test02 ( alpha, 'alpha_1.00_paths.png' )

  alpha = 1.5
  colored_noise_test02 ( alpha, 'alpha_1.50_paths.png' )

  alpha = 2.0
  colored_noise_test02 ( alpha, 'alpha_2.00_paths.png' )
#
#  Terminate.
#
  print ( '' )
  print ( 'COLORED_NOISE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def colored_noise_test01 ( n, q_d, alpha, seed_init ):

#*****************************************************************************80
#
## COLORED_NOISE_TEST01 calls F_ALPHA with particular parameters.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements of the sequence 
#    to generate.
#
#    Input, real Q_D, the variance of the sequence.
#
#    Input, real ALPHA, the exponent of the power law.
#
#    Input, integer SEED_INIT, the initial seed for the 
#    random number generator.
#
  output_filename = 'alpha_%4.2f.txt' % ( alpha )
#
#  Report parameters.
#
  print ( '' )
  print ( 'COLORED_NOISE_TEST01:' )
  print ( '  Generating %d sample points.' % ( n ) )
  print ( '  1/F^ALPHA noise has ALPHA = %f' % ( alpha ) )
  print ( '  Variance is %f' % ( q_d ) )
  print ( '  Initial random number seed = %d' % ( seed_init ) )

  seed = seed_init

  x, seed = f_alpha ( n, q_d, alpha, seed )
#
#  Print no more than 10 entries of the data.
#
  r8vec_print_some ( n, x, 10, '  Noise sample:' )
#
#  Write the data to a file.
#
  output = open ( output_filename, 'w' )

  for i in range ( 0, n ):
    s = '  %g\n' % ( x[i] )
    output.write ( s )

  output.close ( )

  print ( '  Data written to file "%s".' % ( output_filename ) )

  return

def colored_noise_test02 ( alpha, filename ):

#*****************************************************************************80
#
## COLORED_NOISE_TEST02 calls F_ALPHA with different random seeds.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the exponent of the power law.
#
#    Input, string FILENAME, the output filename.
#
#  Local parameters:
#
#    Local, integer N, the number of elements of the sequence 
#    to generate.
#
#    Local, real Q_D, the variance of the sequence.
#
#    Local, integer SEED, the seed for the random number generator.
#
#    Local, real X(N), the sequence.
#
  import matplotlib.pyplot as plt
  import numpy as np

  n_reals = 200
  n = 128
  q_d = 1.0
  seed_init = 123456789
  seed = seed_init
#
#  Report parameters.
#
  print ( '' )
  print ( 'COLORED_NOISE_TEST02:' )
  print ( '  Generating %d realizations' % ( n_reals ) )
  print ( '  Generating %d sample points.' % ( n ) )
  print ( '  1/F^ALPHA noise has ALPHA = %f' % ( alpha ) )
  print ( '  Variance is %f' % ( q_d ) )
  print ( '  Initial random number seed = %d' % ( seed ) )
#
#  To get 1, 2, ..., N, Python makes you follow their atrocious
#  off by one convention.
#
  x = np.arange ( 1, n + 1 )

  yave = np.zeros ( n )

  for i in range ( 0, n_reals ):
    y, seed = f_alpha ( n, q_d, alpha, seed )
    yave = yave + y
    if ( i < 5 ):
      plt.plot ( x, y, linewidth = 1, color = 'b' ) 
  yave = yave / float ( n_reals )
  plt.plot ( x, yave, linewidth = 2, color = 'k' )
  plt.grid ( True )
  s = 'ALPHA = %g,    5 realizations (blue), 200 averaged realizations (black)' % ( alpha )
  plt.title ( s )

  plt.savefig ( filename )
  print ( '' )
  print ( '  Plot saved as "%s"' % ( filename ) )
# plt.show ( )
  return

def f_alpha ( n, q_d, alpha, seed ):

#*****************************************************************************80
#
## F_ALPHA generates a 1/F^ALPHA noise sequence.
#
#  Discussion:
#
#    Thanks to Miro Stoyanov for pointing out that the second half of
#    the data returned by the inverse Fourier transform should be
#    discarded, 24 August 2010.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 July 2017
#
#  Author:
#
#    Original C version by Todd Walter.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Jeremy Kasdin,
#    Discrete Simulation of Colored Noise and Stochastic Processes
#    and 1/f^a Power Law Noise Generation,
#    Proceedings of the IEEE,
#    Volume 83, Number 5, 1995, pages 802-827.
#
#  Parameters:
#
#    Input, integer N, the number of samples to generate.
#
#    Input, real Q_D, the variance of the noise.
#
#    Input, real ALPHA, the exponent for the noise.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), a sequence sampled with the given power law.
#
#    Output, integer SEED, a seed for the random number generator.
#
  import numpy as np
#
#  Set the deviation of the noise.
#
  q_d = np.sqrt ( q_d )
#
#  Generate the coefficients Hk.
#
  hfa = np.zeros ( 2 * n )

  hfa[0] = 1.0 
  for i in range ( 1, n ):
    hfa[i] = hfa[i-1] * ( 0.5 * alpha + float ( i - 1 ) ) / float ( i )
#
#  Fill Wk with white noise.
#
  wfa = np.zeros ( 2 * n )
  for i in range ( 0, n ):
    wfa[i], seed = r8_normal_01 ( seed )
    wfa[i] = wfa[i] * q_d
#
#  Perform the discrete Fourier transforms of Hk and Wk.
#
  h_azero, h_a, h_b = r8vec_sftf ( 2 * n, hfa )

  w_azero, w_a, w_b = r8vec_sftf ( 2 * n, wfa )
#
#  Multiply the two complex vectors.
#
  w_azero = w_azero * h_azero

  for i in range ( 0, n ):
    wr = w_a[i]
    wi = w_b[i]
    w_a[i] = wr * h_a[i] - wi * h_b[i]
    w_b[i] = wi * h_a[i] + wr * h_b[i]
#
#  This scaling is introduced only to match the behavior
#  of the Numerical Recipes code...
#
  w_azero = w_azero * 2 * n

  for i in range ( 0, n - 1 ):
    w_a[i] = w_a[i] * float ( n )
    w_b[i] = w_b[i] * float ( n )

  w_a[n-1] = w_a[n-1] * float ( 2 * n )
  w_b[n-1] = w_b[n-1] * float ( 2 * n )
#
#  Take the inverse Fourier transform of the result.
#
  xlong = r8vec_sftb ( 2 * n, w_azero, w_a, w_b )
#
#  Discard the second half of the inverse Fourier transform.
#
  x = xlong[0:n]

  return x, seed

def r8_normal_01 ( seed ):

#*****************************************************************************80
#
## R8_NORMAL_01 samples the standard normal probability distribution.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#    The Box-Muller method is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the standard normal PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  r1, seed = r8_uniform_01 ( seed )
  r2, seed = r8_uniform_01 ( seed )

  x = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )

  return x, seed

def r8_normal_01_test ( ):

#*****************************************************************************80
#
## R8_NORMAL_01_TEST tests R8_NORMAL_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  seed = 123456789
  test_num = 20

  print ( '' )
  print ( 'R8_NORMAL_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_NORMAL_01 generates normally distributed' )
  print ( '  random values.' )
  print ( '  Using initial random number seed = %d' % ( seed ) )
  print ( '' )

  for test in range ( 0, test_num ):

    x, seed = r8_normal_01 ( seed )
    print ( '  %f' % ( x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_NORMAL_01_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_uniform_01 ( seed ):

#*****************************************************************************80
#
## R8_UNIFORM_01 returns a unit pseudorandom R8.
#
#  Discussion:
#
#    This routine implements the recursion
#
#      seed = 16807 * seed mod ( 2^31 - 1 )
#      r8_uniform_01 = seed / ( 2^31 - 1 )
#
#    The integer arithmetic never requires more than 32 bits,
#    including a sign bit.
#
#    If the initial seed is 12345, then the first three computations are
#
#      Input     Output      R8_UNIFORM_01
#      SEED      SEED
#
#         12345   207482415  0.096616
#     207482415  1790989824  0.833995
#    1790989824  2035175616  0.947702
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.  SEED should not be 0.
#
#    Output, real R, a random value between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8_UNIFORM_01 - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10

  return r, seed

def r8_uniform_01_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_01 produces a sequence of random values.' )

  seed = 123456789

  print ( '' )
  print ( '  Using random seed %d' % ( seed ) )

  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )
  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )

  print ( '' )
  print ( '  Verify that the sequence can be restarted.' )
  print ( '  Set the seed back to its original value, and see that' )
  print ( '  we generate the same sequence.' )

  seed = 123456789
  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Normal end of execution.' )
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

def r8vec_print_some ( n, a, max_print, title ):

#*****************************************************************************80
#
## R8VEC_PRINT_SOME prints "some" of an R8VEC.
#
#  Discussion:
#
#    The user specifies MAX_PRINT, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_PRINT, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, integer MAX_PRINT, the maximum number of lines
#    to print.
#
#    Input, string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '  %6d  %14g' % ( i, a[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    print ( '  ......  ..............' )
    i = n - 1
    print ( '  %6d  %14g' % ( i, a[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    i = max_print - 1
    print ( '  %6d  %14g  ...more entries...' % ( i, a[i] ) )

  return

def r8vec_print_some_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_SOME_TEST tests R8VEC_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_indicator1 import r8vec_indicator1

  print ( '' )
  print ( 'R8VEC_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT_SOME prints some of an R8VEC.' )

  n = 100
  a = r8vec_indicator1 ( n )

  max_print = 10

  r8vec_print_some ( n, a, max_print, '  No more than 10 lines of this vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_sftb ( n, azero, a, b ):

#*****************************************************************************80
#
## R8VEC_SFTB computes a "slow" backward Fourier transform of real data.
#
#  Discussion:
#
#    SFTB and SFTF are inverses of each other.  If we begin with data
#    AZERO, A, and B, and apply SFTB to it, and then apply SFTF to the
#    resulting R vector, we should get back the original AZERO, A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of data values.
#
#    Input, real AZERO, the constant Fourier coefficient.
#
#    Input, real A(N/2), B(N/2), the Fourier coefficients.
#
#    Output, real R(N), the reconstructed data sequence.
#
  import numpy as np

  r = np.zeros ( n )
  r[0:n] = azero

  for i in range ( 0, n ):
    k_hi = int ( n / 2 )
    for k in range ( 0, k_hi ):
      theta = float ( k * i * 2 ) * np.pi / float ( n )
      r[i] = r[i] + a[k] * np.cos ( theta ) + b[k] * np.sin ( theta )

  return r

def r8vec_sftf ( n, r ):

#*****************************************************************************80
#
## R8VEC_SFTF computes a "slow" forward Fourier transform of real data.
#
#  Discussion:
#
#    SFTF and SFTB are inverses of each other.  If we begin with data
#    R and apply SFTB to it, and then apply SFTB to the resulting AZERO, 
#    A, and B, we should get back the original R.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of data values.
#
#    Input, real R(N), the data to be transformed.
#
#    Output, real AZERO, = sum ( 1 <= I <= N ) R(I) / N.
#
#    Output, real A(N/2), B(N/2), the Fourier coefficients.
#
  import numpy as np

  azero = np.sum ( r ) / float ( n )
  nhalf = int ( n / 2 )
  a = np.zeros ( nhalf )
  b = np.zeros ( nhalf )

  for i in range ( 0, nhalf ):

    for j in range ( 0, n ):
      theta = float ( 2 * ( i + 1 ) * j ) * np.pi / float ( n )
      a[i] = a[i] + r[j] * np.cos ( theta )
      b[i] = b[i] + r[j] * np.sin ( theta )

    a[i] = a[i] / float ( n )
    b[i] = b[i] / float ( n )

    if ( ( n % 2 ) == 1 or i < nhalf - 1 ):
      a[i] = 2.0 * a[i]
      b[i] = 2.0 * b[i]

  return azero, a, b

def r8vec_sftf_test ( ):

#*****************************************************************************80
#
## R8VEC_SFTF_TEST tests R8VEC_SFTF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 July 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_SFTF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_SFTF computes the "slow" Fourier transform (forward)' )
  print ( '  of a vector of real data.' )
  print ( '  The original data can be recovered using R8VEC_SFTB.' )

  n = 15
  seed = 123456789

  r, seed = r8vec_uniform_01 ( n, seed )

  azero, a, b = r8vec_sftf ( n, r )
  nhalf = int ( n / 2 )
  
  print ( '' )
  print ( '  Fourier coefficients:' )
  print ( '' )
  print ( '  %10f' % ( azero ) )
  for i in range ( 0, nhalf ):
    print ( '  %10f  %10f' % ( a[i], b[i] ) )

  r2 = r8vec_sftb ( n, azero, a, b )

  print ( '' )
  print ( '  Compare data R and recovered data R2:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %10f  %10f' % ( r[i], r2[i] ) )  
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_SFTF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
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
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_01 - Fatal error!' )

  x = np.zeros ( n );

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
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

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_01 computes a random R8VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_01 ( n, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST:' )
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

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  colored_noise_test ( )
  timestamp ( )
