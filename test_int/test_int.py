#! /usr/bin/env python3
#
def test_int_test ( ):

#*****************************************************************************80
#
## test_int_test() tests test_int().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'test_int_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test test_int().' )

  gauss_legendre4_test ( )
  midpoint_test ( )
  monte_carlo_test ( )
  trapezoid_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_int_test()' )
  print ( '  Normal end of execution.' )

  return

def gauss_legendre4_test ( ):

#*****************************************************************************80
#
## gauss_legendre4_test() applies a composite Gauss-Legendre rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'gauss_legendre4_test():' )
  print ( '  Composite 4-point Gauss-Legendre quadrature rule.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '         N          Approx      Error         Ratio' )
#
#  Pick a problem.
#
  for prob in range ( 1, prob_num + 1 ):

    exact = p00_exact ( prob )

    print ( '' )
    print ( 'Problem ', prob )
#
#  Pick a number of subintervals.
#
    for int_log in range ( 0, 11 ):

      int_num = 2 ** int_log

      result = p00_gauss_legendre4 ( prob, int_num )

      err = np.abs ( exact - result );

      if ( 0 < int_log ):
        if ( err == 0.0 ):
          print ( '   %4d  %14.10f  %14e  */0' \
            % ( int_num, result, err ) )
        else:
          ratio = err_old / err
          print ( '   %4d  %14.10f  %14e  %8g' \
            % ( int_num, result, err, ratio ) )
      else:
        print ( '   %4d  %14.10f  %14e' \
          % ( int_num, result, err ) )
      err_old = err

    print ( '  Exact  %14.10f' % ( exact ) )

  return

def midpoint_test ( ):

#*****************************************************************************80
#
## midpoint_test() applies a composite midpoint rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'midpoint_test():' )
  print ( '  Composite midpoint quadrature rule.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '         N          Approx      Error         Ratio' )
#
#  Pick a problem.
#
  for prob in range ( 1, prob_num + 1 ):

    exact = p00_exact ( prob )

    print ( '' )
    print ( 'Problem ', prob )
#
#  Pick a number of subintervals.
#
    for int_log in range ( 0, 21 ):

      int_num = 2 ** int_log

      result = p00_midpoint ( prob, int_num )

      err = np.abs ( exact - result );

      if ( 0 < int_log ):
        if ( err != 0.0 ):
          ratio = err_old / err
          print ( '   %7d  %14.10f  %14e  %8g' \
            % ( int_num, result, err, ratio ) )
        else:
          print ( '   %7d  %14.10f  %14e  (*/0)' \
            % ( int_num, result, err ) )
      else:
        print ( '   %7d  %14.10f  %14e' \
          % ( int_num, result, err ) )
      err_old = err

    print ( '     Exact  %14.10f' % ( exact ) )

  return

def monte_carlo_test ( ):

#*****************************************************************************80
#
## monte_carlo_test() applies a monte carlo rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'monte_carlo_test():' )
  print ( '  Monte Carlo quadrature rule.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '         N          Approx      Error         Ratio' )
#
#  Pick a problem.
#
  for prob in range ( 1, prob_num + 1 ):

    exact = p00_exact ( prob )

    print ( '' )
    print ( 'Problem ', prob )
#
#  Pick a number of subintervals.
#
    for int_log in range ( 0, 21 ):

      int_num = 2 ** int_log

      result = p00_monte_carlo ( prob, int_num )

      err = np.abs ( exact - result );

      if ( 0 < int_log ):
        if ( err != 0.0 ):
          ratio = err_old / err
          print ( '   %7d  %14.10f  %14e  %8g' \
            % ( int_num, result, err, ratio ) )
        else:
          print ( '   %7d  %14.10f  %14e  (*/0)' \
            % ( int_num, result, err ) )
      else:
        print ( '   %7d  %14.10f  %14e' \
          % ( int_num, result, err ) )
      err_old = err

    print ( '     Exact  %14.10f' % ( exact ) )

  return

def trapezoid_test ( ):

#*****************************************************************************80
#
## trapezoid_test() applies a composite trapezoid rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'trapezoid_test():' )
  print ( '  Composite trapezoid quadrature rule.' )

  prob_num = p00_prob_num ( )

  print ( '' )
  print ( '         N          Approx      Error         Ratio' )
#
#  Pick a problem.
#
  for prob in range ( 1, prob_num + 1 ):

    exact = p00_exact ( prob )

    print ( '' )
    print ( 'Problem ', prob )
#
#  Pick a number of subintervals.
#
    for int_log in range ( 0, 21 ):

      int_num = 2 ** int_log

      result = p00_trapezoid ( prob, int_num )

      err = np.abs ( exact - result );

      if ( 0 < int_log ):
        if ( err != 0.0 ):
          ratio = err_old / err
          print ( '   %7d  %14.10f  %14e  %8g' \
            % ( int_num, result, err, ratio ) )
        else:
          print ( '   %7d  %14.10f  %14e  (*/0)' \
            % ( int_num, result, err ) )
      else:
        print ( '   %7d  %14.10f  %14e' \
          % ( int_num, result, err ) )
      err_old = err

    print ( '     Exact  %14.10f' % ( exact ) )

  return

def p00_exact ( prob ):

#*****************************************************************************80
#
## p00_exact() returns the exact integral for any problem.
#
#  Discussion:
#
#    This routine provides a "generic" interface to the exact integral
#    routines for the various problems, and allows a problem to be called
#    by number (PROB) rather than by name.
#
#    In some cases, the "exact" value of the integral is in fact
#    merely a respectable approximation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the desired test problem.
#
#  Output:
#
#    real EXACT, the exact value of the integral.
#
  if ( prob == 1 ):
    exact = p01_exact ( )
  elif ( prob == 2 ):
    exact = p02_exact ( )
  elif ( prob == 3 ):
    exact = p03_exact ( )
  elif ( prob == 4 ):
    exact = p04_exact ( )
  elif ( prob == 5 ):
    exact = p05_exact ( )
  elif ( prob == 6 ):
    exact = p06_exact ( )
  elif ( prob == 7 ):
    exact = p07_exact ( )
  elif ( prob == 8 ):
    exact = p08_exact ( )
  elif ( prob == 9 ):
    exact = p09_exact ( )
  elif ( prob == 10 ):
    exact = p10_exact ( )
  elif ( prob == 11 ):
    exact = p11_exact ( )
  elif ( prob == 12 ):
    exact = p12_exact ( )
  elif ( prob == 13 ):
    exact = p13_exact ( )
  elif ( prob == 14 ):
    exact = p14_exact ( )
  elif ( prob == 15 ):
    exact = p15_exact ( )
  elif ( prob == 16 ):
    exact = p16_exact ( )
  elif ( prob == 17 ):
    exact = p17_exact ( )
  elif ( prob == 18 ):
    exact = p18_exact ( )
  elif ( prob == 19 ):
    exact = p19_exact ( )
  elif ( prob == 20 ):
    exact = p20_exact ( )
  elif ( prob == 21 ):
    exact = p21_exact ( )
  elif ( prob == 22 ):
    exact = p22_exact ( )
  elif ( prob == 23 ):
    exact = p23_exact ( )
  elif ( prob == 24 ):
    exact = p24_exact ( )
  elif ( prob == 25 ):
    exact = p25_exact ( )
  elif ( prob == 26 ):
    exact = p26_exact ( )
  elif ( prob == 27 ):
    exact = p27_exact ( )
  elif ( prob == 28 ):
    exact = p28_exact ( )
  elif ( prob == 29 ):
    exact = p29_exact ( )
  elif ( prob == 30 ):
    exact = p30_exact ( )
  elif ( prob == 31 ):
    exact = p31_exact ( )
  elif ( prob == 32 ):
    exact = p32_exact ( )
  elif ( prob == 33 ):
    exact = p33_exact ( )
  elif ( prob == 34 ):
    exact = p34_exact ( )
  elif ( prob == 35 ):
    exact = p35_exact ( )
  elif ( prob == 36 ):
    exact = p36_exact ( )
  elif ( prob == 37 ):
    exact = p37_exact ( )
  elif ( prob == 38 ):
    exact = p38_exact ( )
  elif ( prob == 39 ):
    exact = p39_exact ( )
  elif ( prob == 40 ):
    exact = p40_exact ( )
  elif ( prob == 41 ):
    exact = p41_exact ( )
  elif ( prob == 42 ):
    exact = p42_exact ( )
  elif ( prob == 43 ):
    exact = p43_exact ( )
  elif ( prob == 44 ):
    exact = p44_exact ( )
  elif ( prob == 45 ):
    exact = p45_exact ( )
  elif ( prob == 46 ):
    exact = p46_exact ( )
  elif ( prob == 47 ):
    exact = p47_exact ( )
  elif ( prob == 48 ):
    exact = p48_exact ( )
  elif ( prob == 49 ):
    exact = p49_exact ( )
  elif ( prob == 50 ):
    exact = p50_exact ( )
  elif ( prob == 51 ):
    exact = p51_exact ( )
  elif ( prob == 52 ):
    exact = p52_exact ( )
  elif ( prob == 53 ):
    exact = p53_exact ( )
  elif ( prob == 54 ):
    exact = p54_exact ( )
  elif ( prob == 55 ):
    exact = p55_exact ( )
  elif ( prob == 56 ):
    exact = p56_exact ( )
  elif ( prob == 57 ):
    exact = p57_exact ( )
  else:
    print ( '' )
    print ( 'p00_exact(): Fatal error!' )
    print ( '  Illegal problem number = ', prob )
    raise Exception ( 'p00_exact(): Fatal error!' )

  return exact

def p00_fun ( prob, x ):

#*****************************************************************************80
#
## p00_fun() evaluates the integrand for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the desired test problem.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  if ( prob == 1 ):
    fx = p01_fun ( x )
  elif ( prob == 2 ):
    fx = p02_fun ( x )
  elif ( prob == 3 ):
    fx = p03_fun ( x )
  elif ( prob == 4 ):
    fx = p04_fun ( x )
  elif ( prob == 5 ):
    fx = p05_fun ( x )
  elif ( prob == 6 ):
    fx = p06_fun ( x )
  elif ( prob == 7 ):
    fx = p07_fun ( x )
  elif ( prob == 8 ):
    fx = p08_fun ( x )
  elif ( prob == 9 ):
    fx = p09_fun ( x )
  elif ( prob == 10 ):
    fx = p10_fun ( x )
  elif ( prob == 11 ):
    fx = p11_fun ( x )
  elif ( prob == 12 ):
    fx = p12_fun ( x )
  elif ( prob == 13 ):
    fx = p13_fun ( x )
  elif ( prob == 14 ):
    fx = p14_fun ( x )
  elif ( prob == 15 ):
    fx = p15_fun ( x )
  elif ( prob == 16 ):
    fx = p16_fun ( x )
  elif ( prob == 17 ):
    fx = p17_fun ( x )
  elif ( prob == 18 ):
    fx = p18_fun ( x )
  elif ( prob == 19 ):
    fx = p19_fun ( x )
  elif ( prob == 20 ):
    fx = p20_fun ( x )
  elif ( prob == 21 ):
    fx = p21_fun ( x )
  elif ( prob == 22 ):
    fx = p22_fun ( x )
  elif ( prob == 23 ):
    fx = p23_fun ( x )
  elif ( prob == 24 ):
    fx = p24_fun ( x )
  elif ( prob == 25 ):
    fx = p25_fun ( x )
  elif ( prob == 26 ):
    fx = p26_fun ( x )
  elif ( prob == 27 ):
    fx = p27_fun ( x )
  elif ( prob == 28 ):
    fx = p28_fun ( x )
  elif ( prob == 29 ):
    fx = p29_fun ( x )
  elif ( prob == 30 ):
    fx = p30_fun ( x )
  elif ( prob == 31 ):
    fx = p31_fun ( x )
  elif ( prob == 32 ):
    fx = p32_fun ( x )
  elif ( prob == 33 ):
    fx = p33_fun ( x )
  elif ( prob == 34 ):
    fx = p34_fun ( x )
  elif ( prob == 35 ):
    fx = p35_fun ( x )
  elif ( prob == 36 ):
    fx = p36_fun ( x )
  elif ( prob == 37 ):
    fx = p37_fun ( x )
  elif ( prob == 38 ):
    fx = p38_fun ( x )
  elif ( prob == 39 ):
    fx = p39_fun ( x )
  elif ( prob == 40 ):
    fx = p40_fun ( x )
  elif ( prob == 41 ):
    fx = p41_fun ( x )
  elif ( prob == 42 ):
    fx = p42_fun ( x )
  elif ( prob == 43 ):
    fx = p43_fun ( x )
  elif ( prob == 44 ):
    fx = p44_fun ( x )
  elif ( prob == 45 ):
    fx = p45_fun ( x )
  elif ( prob == 46 ):
    fx = p46_fun ( x )
  elif ( prob == 47 ):
    fx = p47_fun ( x )
  elif ( prob == 48 ):
    fx = p48_fun ( x )
  elif ( prob == 49 ):
    fx = p49_fun ( x )
  elif ( prob == 50 ):
    fx = p50_fun ( x )
  elif ( prob == 51 ):
    fx = p51_fun ( x )
  elif ( prob == 52 ):
    fx = p52_fun ( x )
  elif ( prob == 53 ):
    fx = p53_fun ( x )
  elif ( prob == 54 ):
    fx = p54_fun ( x )
  elif ( prob == 55 ):
    fx = p55_fun ( x )
  elif ( prob == 56 ):
    fx = p56_fun ( x )
  elif ( prob == 57 ):
    fx = p57_fun ( x )
  else:
    print ( '' )
    print ( 'p00_fun(): Fatal error!' )
    print ( '  Illegal problem number = ', prob )
    raise Exception ( 'p00_fun(): Fatal error!' )

  return fx

def p00_gauss_legendre4 ( prob, int_num ):

#*****************************************************************************80
#
## p00_gauss_legendre4() applies a 4-point composite Gauss-Legendre rule.
#
#  Discussion:
#
#    A 4 point rule is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer INT_NUM, the number of subintervals.
#
#  Output:
#
#    real RESULT, the approximate integral.
#
  import numpy as np

  gauss_num = 4

  gauss_abs = np.array ( [ \
    -0.861136311594052575223946488893, \
    -0.339981043584856264802665759103, \
     0.339981043584856264802665759103, \
     0.861136311594052575223946488893 ] )

  gauss_weight = np.array ( [ \
    0.347854845137453857373063949222, \
    0.652145154862546142626936050778, \
    0.652145154862546142626936050778, \
     0.347854845137453857373063949222 ] )

  a, b = p00_limits ( prob )

  h = ( b - a ) / ( int_num )

  ab = np.linspace ( a, b, int_num + 1 )
 
  result = 0.0

  for i in range ( 0, gauss_num ):

    x = 0.5 * ( ( 1.0 - gauss_abs[i] ) * ab[0:int_num] \
               + ( 1.0 + gauss_abs[i] ) * ab[1:int_num+1] )

    result = result + 0.5 * gauss_weight[i] * h * np.sum ( p00_fun ( prob, x ) )

  return result

def p00_limits ( prob ):

#*****************************************************************************80
#
## p00_limits() returns the integration limits for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the number of the desired test problem.
#
#  Output:
#
#    real A, B, the limits of integration.
#
  if ( prob == 1 ):
    [ a, b ] = p01_limits ( )
  elif ( prob == 2 ):
    [ a, b ] = p02_limits ( )
  elif ( prob == 3 ):
    [ a, b ] = p03_limits ( )
  elif ( prob == 4 ):
    [ a, b ] = p04_limits ( )
  elif ( prob == 5 ):
    [ a, b ] = p05_limits ( )
  elif ( prob == 6 ):
    [ a, b ] = p06_limits ( )
  elif ( prob == 7 ):
    [ a, b ] = p07_limits ( )
  elif ( prob == 8 ):
    [ a, b ] = p08_limits ( )
  elif ( prob == 9 ):
    [ a, b ] = p09_limits ( )
  elif ( prob == 10 ):
    [ a, b ] = p10_limits ( )
  elif ( prob == 11 ):
    [ a, b ] = p11_limits ( )
  elif ( prob == 12 ):
    [ a, b ] = p12_limits ( )
  elif ( prob == 13 ):
    [ a, b ] = p13_limits ( )
  elif ( prob == 14 ):
    [ a, b ] = p14_limits ( )
  elif ( prob == 15 ):
    [ a, b ] = p15_limits ( )
  elif ( prob == 16 ):
    [ a, b ] = p16_limits ( )
  elif ( prob == 17 ):
    [ a, b ] = p17_limits ( )
  elif ( prob == 18 ):
    [ a, b ] = p18_limits ( )
  elif ( prob == 19 ):
    [ a, b ] = p19_limits ( )
  elif ( prob == 20 ):
    [ a, b ] = p20_limits ( )
  elif ( prob == 21 ):
    [ a, b ] = p21_limits ( )
  elif ( prob == 22 ):
    [ a, b ] = p22_limits ( )
  elif ( prob == 23 ):
    [ a, b ] = p23_limits ( )
  elif ( prob == 24 ):
    [ a, b ] = p24_limits ( )
  elif ( prob == 25 ):
    [ a, b ] = p25_limits ( )
  elif ( prob == 26 ):
    [ a, b ] = p26_limits ( )
  elif ( prob == 27 ):
    [ a, b ] = p27_limits ( )
  elif ( prob == 28 ):
    [ a, b ] = p28_limits ( )
  elif ( prob == 29 ):
    [ a, b ] = p29_limits ( )
  elif ( prob == 30 ):
    [ a, b ] = p30_limits ( )
  elif ( prob == 31 ):
    [ a, b ] = p31_limits ( )
  elif ( prob == 32 ):
    [ a, b ] = p32_limits ( )
  elif ( prob == 33 ):
    [ a, b ] = p33_limits ( )
  elif ( prob == 34 ):
    [ a, b ] = p34_limits ( )
  elif ( prob == 35 ):
    [ a, b ] = p35_limits ( )
  elif ( prob == 36 ):
    [ a, b ] = p36_limits ( )
  elif ( prob == 37 ):
    [ a, b ] = p37_limits ( )
  elif ( prob == 38 ):
    [ a, b ] = p38_limits ( )
  elif ( prob == 39 ):
    [ a, b ] = p39_limits ( )
  elif ( prob == 40 ):
    [ a, b ] = p40_limits ( )
  elif ( prob == 41 ):
    [ a, b ] = p41_limits ( )
  elif ( prob == 42 ):
    [ a, b ] = p42_limits ( )
  elif ( prob == 43 ):
    [ a, b ] = p43_limits ( )
  elif ( prob == 44 ):
    [ a, b ] = p44_limits ( )
  elif ( prob == 45 ):
    [ a, b ] = p45_limits ( )
  elif ( prob == 46 ):
    [ a, b ] = p46_limits ( )
  elif ( prob == 47 ):
    [ a, b ] = p47_limits ( )
  elif ( prob == 48 ):
    [ a, b ] = p48_limits ( )
  elif ( prob == 49 ):
    [ a, b ] = p49_limits ( )
  elif ( prob == 50 ):
    [ a, b ] = p50_limits ( )
  elif ( prob == 51 ):
    [ a, b ] = p51_limits ( )
  elif ( prob == 52 ):
    [ a, b ] = p52_limits ( )
  elif ( prob == 53 ):
    [ a, b ] = p53_limits ( )
  elif ( prob == 54 ):
    [ a, b ] = p54_limits ( )
  elif ( prob == 55 ):
    [ a, b ] = p55_limits ( )
  elif ( prob == 56 ):
    [ a, b ] = p56_limits ( )
  elif ( prob == 57 ):
    [ a, b ] = p57_limits ( )
  else:
    print ( '' )
    print ( 'p00_limits(): Fatal error!' )
    print ( '  Illegal problem number =', prob )
    raise Exception ( 'p00_limits(): Fatal error!' )

  return a, b

def p00_midpoint ( prob, int_num ):

#*****************************************************************************80
#
## p00_midpoint() applies the composite midpoint rule to integrate a function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 December 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer INT_NUM, the number of subintervals.
#
#  Output:
#
#    real RESULT, the approximate integral.
#
  import numpy as np

  a, b = p00_limits ( prob )

  x = np.linspace ( a, b, 2 * int_num + 1 )

  xm = x[1:-1:2]

  result = np.sum ( p00_fun ( prob, xm ) )

  result = result * ( b - a ) / int_num

  return result

def p00_monte_carlo ( prob, int_num ):

#*****************************************************************************80
#
## p00_monte_carlo() applies the Monte Carlo rule to integrate a function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer INT_NUM, the number of sample points.
#
#  Output:
#
#    real RESULT, the approximate integral.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a, b = p00_limits ( prob )

  x = rng.uniform ( low = a, high = b, size = int_num )
  fx = p00_fun ( prob, x )
  result = np.sum ( fx ) * ( b - a ) / int_num

  return result

def p00_prob_num ( ):

#*****************************************************************************80
#
## p00_prob_num() returns the number of test integration problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer PROB_NUM, the number of tests.
#
  prob_num = 57

  return prob_num

def p00_trapezoid ( prob, int_num ):

#*****************************************************************************80
#
## p00_trapezoid() applies the composite trapezoid rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROB, the problem index.
#
#    integer INT_NUM, the number of subintervals.
#
#  Output:
#
#    real RESULT, the approximate integral.
#
  import numpy as np

  a, b = p00_limits ( prob )

  x = np.linspace ( a, b, int_num + 1 )

  result = \
      0.5 *          p00_fun ( prob, x[0]           )   \
    +       np.sum ( p00_fun ( prob, x[1:int_num] ) ) \
    + 0.5 *          p00_fun ( prob, x[int_num]   )

  result = result * ( b - a ) / int_num

  return result

def p01_exact ( ):

#*****************************************************************************80
#
## p01_exact() returns the exact integral for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = np.exp ( 1.0 ) - 1.0

  return exact

def p01_fun ( x ):

#*****************************************************************************80
#
## p01_fun() evaluates the integrand for problem 1.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    exp ( x )
#
#  Antiderivative:
#
#    exp ( x )
#
#  Exact Integral:
#
#    exp ( 1 ) - 1
#
#  Approximate Integral (25 digits):
#
#    1.718281828459045235360287...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.exp ( x )

  return fx

def p01_limits ( ):

#*****************************************************************************80
#
## p01_limits() returns the integration limits for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p02_exact ( ):

#*****************************************************************************80
#
## p02_exact() returns the exact integral for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 0.7

  return exact

def p02_fun ( x ):

#*****************************************************************************80
#
## p02_fun() evaluates the integrand for problem 2.
#
#  Discussion:
#
#    The integrand is discontinuous at X = 0.3.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    if ( x < 0.3 )
#      f(x) = 0
#    else
#      f(x) = 1
#
#  Antiderivative:
#
#    if ( x < 0.3 )
#      g(x) = 0
#    else
#      g(x) = X - 0.3
#
#  Exact Integral:
#
#    0.7
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  fx = ( 0.3 <= x ).astype(float)

  return fx

def p02_limits ( ):

#*****************************************************************************80
#
## p02_limits() returns the integration limits for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p03_exact ( ):

#*****************************************************************************80
#
## p03_exact() returns the exact integral for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2009
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 2.0 / 3.0

  return exact

def p03_fun ( x ):

#*****************************************************************************80
#
## p03_fun() evaluates the integrand for problem 3.
#
#  Discussion:
#
#    The integrand is not differentiable at X = 0.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    sqrt ( x )
#
#  Antiderivative:
#
#    ( 2 / 3 ) * x^(3/2)
#
#  Exact Integral:
#
#    2 / 3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.sqrt ( x )

  return fx

def p03_limits ( ):

#*****************************************************************************80
#
## p03_limits() returns the integration limits for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p04_exact ( ):

#*****************************************************************************80
#
## p04_exact() returns the estimated integral for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.47942822668880166736

  return exact

def p04_fun ( x ):

#*****************************************************************************80
#
## p04_fun() evaluates the integrand for problem 4.
#
#  Interval:
#
#    -1 <= x <= 1
#
#  Integrand:
#
#    0.92 * cosh ( x ) - cos ( x )
#
#  Antiderivative:
#
#    0.92 * sinh ( x ) - sin ( x )
#
#  Exact Integral:
#
#    1.84 * sinh ( 1 ) - 2 * sin ( 1 )
#
#  Approximate Integral (20 digits):
#
#    0.47942822668880166736...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Clenshaw, Alan Curtis,
#    A Method for Numerical Integration on an Automatic Computer,
#    Numerische Mathematik,
#    Volume 2, Number 1, December 1960, pages 197-205.
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = 0.92 * np.cosh ( x ) - np.cos ( x )

  return fx

def p04_limits ( ):

#*****************************************************************************80
#
## p04_limits() returns the integration limits for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = -1.0
  b = 1.0

  return a, b

def p05_exact ( ):

#*****************************************************************************80
#
## p05_exact() returns the estimated integral for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 1.5822329637296729331

  return exact

def p05_fun ( x ):

#*****************************************************************************80
#
## p05_fun() evaluates the integrand for problem 5.
#
#  Interval:
#
#    -1 <= x <= 1
#
#  Integrand:
#
#    1 / ( x^4 + x^2 + 0.9 )
#
#  Approximate Integral (20 digits):
#
#    1.5822329637296729331...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Clenshaw, Alan Curtis,
#    A Method for Numerical Integration on an Automatic Computer,
#    Numerische Mathematik,
#    Volume 2, Number 1, December 1960, pages 197-205.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  fx = 1.0 / ( x**4 + x**2 + 0.9 )

  return fx

def p05_limits ( ):

#*****************************************************************************80
#
## p05_limits() returns the integration limits for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = -1.0
  b = 1.0

  return a, b

def p06_exact ( ):

#*****************************************************************************80
#
## p06_exact() returns the exact integral for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 1.460447131787105

  return exact

def p06_fun ( x ):

#*****************************************************************************80
#
## p06_fun() evaluates the integrand for problem 6.
#
#  Interval:
#
#    -1 <= x <= 1
#
#  Integrand:
#
#    sqrt ( abs ( x + 0.5 ) )
#
#  Exact Integral:
#
#    ( sqrt ( 2 ) + 3 * sqrt ( 6 ) ) / 6 = 1.460447131787105
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Clenshaw, Alan Curtis,
#    A Method for Numerical Integration on an Automatic Computer,
#    Numerische Mathematik,
#    Volume 2, Number 1, December 1960, pages 197-205.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.sqrt ( np.abs ( x + 0.5 ) )

  return fx

def p06_limits ( ):

#*****************************************************************************80
#
## p06_limits() returns the integration limits for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = -1.0
  b = 1.0

  return a, b

def p07_exact ( ):

#*****************************************************************************80
#
## p07_exact() returns the exact integral for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 2.0

  return exact

def p07_fun ( x ):

#*****************************************************************************80
#
## p07_fun() evaluates the integrand for problem 7.
#
#  Discussion:
#
#    The integrand is singular at x = 0.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    1 / sqrt ( x )
#
#  Antiderivative:
#
#    2 * sqrt ( x )
#
#  Exact Integral:
#
#    2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = 1.0 / np.sqrt ( x )

  return fx

def p07_limits ( ):

#*****************************************************************************80
#
## p07_limits() returns the integration limits for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p08_exact ( ):

#*****************************************************************************80
#
## p08_exact() returns the estimated integral for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.86697298733991103757

  return exact

def p08_fun ( x ):

#*****************************************************************************80
#
## p08_fun() evaluates the integrand for problem 8.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    1 / ( 1 + x^4 )
#
#  Antiderivative:
#
#    (1/8) * sqrt ( 2 )
#    * ln ( ( X^2 + sqrt ( 2 ) * X+ 1 ) / ( X^2 - sqrt ( 2 ) * X + 1 ) )
#    + (1/4) * sqrt ( 2 ) * arctan ( sqrt ( 2 ) * X / ( 1 - X^2 ) )
#
#  Approximate Integral (20 digits):
#
#    0.86697298733991103757...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  fx = 1.0 / ( 1.0 + x**4 )

  return fx

def p08_limits ( ):

#*****************************************************************************80
#
## p08_limits() returns the integration limits for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p09_exact ( ):

#*****************************************************************************80
#
## p09_exact() returns the estimated integral for problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 1.1547005383792515290

  return exact

def p09_fun ( x ):

#*****************************************************************************80
#
## p09_fun() evaluates the integrand for problem 9.
#
#  Discussion:
#
#    The integrand is oscillatory, going through 5 periods in [0,1].
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    2 / ( 2 + sin ( 10 * pi * X ) )
#
#  Antiderivative:
#
#    1 / ( 5 * pi * sqrt ( 3 ) ) *
#    arctan ( ( 1 + 2 * tan ( 5 * pi * X ) ) / sqrt ( 3 ) )
#
#  Exact Integral:
#
#    2 / sqrt ( 3 )
#
#  Approximate Integral (20 digits):
#
#    1.1547005383792515290...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = 2.0 / ( 2.0 + np.sin ( 10.0 * np.pi * x ) )

  return fx

def p09_limits ( ):

#*****************************************************************************80
#
## p09_limits() returns the integration limits for problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p10_exact ( ):

#*****************************************************************************80
#
## p10_exact() returns the estimated integral for problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.6931471805599453094172321

  return exact

def p10_fun ( x ):

#*****************************************************************************80
#
## p10_fun() evaluates the integrand for problem 10.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    1 / ( 1 + x )
#
#  Antiderivative:
#
#    ln ( 1 + x )
#
#  Exact Integral:
#
#    ln ( 2 )
#
#  Approximate Integral (25 digits):
#
#    0.6931471805599453094172321...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  fx = 1.0 / ( 1.0 + x )

  return fx

def p10_limits ( ):

#*****************************************************************************80
#
## p10_limits() returns the integration limits for problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p11_exact ( ):

#*****************************************************************************80
#
## p11_exact() returns the estimated integral for problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.37988549304172247537

  return exact

def p11_fun ( x ):

#*****************************************************************************80
#
## p11_fun() evaluates the integrand for problem 11.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    1 / ( 1 + exp ( x ) )
#
#  Antiderivative:
#
#    ln ( exp ( x ) / ( 1 + exp ( x ) ) )
#
#  Exact Integral:
#
#    ln ( 2 * E / ( 1 + E ) )
#
#  Approximate Integral (20 digits):
#
#    0.37988549304172247537...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = 1.0 / ( 1.0 + np.exp ( x ) )

  return fx

def p11_limits ( ):

#*****************************************************************************80
#
## p11_limits() returns the integration limits for problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p12_exact ( ):

#*****************************************************************************80
#
## p12_exact() returns the estimated integral for problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.77750463411224827642

  return exact

def p12_fun ( x ):

#*****************************************************************************80
#
## p12_fun() evaluates the integrand for problem 12.
#
#  Discussion:
#
#    The integrand has a removable singularity at X = 0.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    x / ( exp ( x) - 1 )
#
#  Antiderivative:
#
#    The Debye function.
#
#  Approximate Integral (20 digits):
#
#    0.77750463411224827642...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = x / ( np.exp ( x - 1.0 ) )

  return fx

def p12_limits ( ):

#*****************************************************************************80
#
## p12_limits() returns the integration limits for problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p13_exact ( ):

#*****************************************************************************80
#
## p13_exact() returns the estimated integral for problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 1.6583475942188740493

  return exact

def p13_fun ( x ):

#*****************************************************************************80
#
## p13_fun() evaluates the integrand for problem 13.
#
#  Interval:
#
#    0 <= x <= 10
#
#  Integrand:
#
#    sin ( x ) / x
#
#  Approximate Integral (20 digits):
#
#    1.6583475942188740493...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.sin ( x ) / x

  return fx

def p13_limits ( ):

#*****************************************************************************80
#
## p13_limits() returns the integration limits for problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 10.0

  return a, b

def p14_exact ( ):

#*****************************************************************************80
#
## p14_exact() returns the estimated integral for problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.500000211166

  return exact

def p14_fun ( x ):

#*****************************************************************************80
#
## p14_fun() evaluates the integrand for problem 14.
#
#  Discussion:
#
#    For X's that aren't actually very big, the function becomes very
#    small.  Some compilers may product code that fails in these cases.
#    An attempt has been made to return a value of 0 when the computed
#    value of F(X) would be extremely small.
#
#  Interval:
#
#    0 <= x <= 10
#
#  Integrand:
#
#    sqrt ( 50 ) * exp ( - 50 * pi * x * x )
#
#  Exact Integral:
#
#    0.5 * erf ( 50 * sqrt ( 2 * pi ) )
#
#  Approximate Integral:
#
#    0.500000211166...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.sqrt ( 50.0 ) * np.exp ( - 50.0 * np.pi * x**2 )

  return fx

def p14_limits ( ):

#*****************************************************************************80
#
## p14_limits() returns the integration limits for problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 10.0

  return a, b

def p15_exact ( ):

#*****************************************************************************80
#
## p15_exact() returns the exact integral for problem 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 1.0

  return exact

def p15_fun ( x ):

#*****************************************************************************80
#
## p15_fun() evaluates the integrand for problem 15.
#
#  Interval:
#
#    0 <= x <= 10
#
#  Integrand:
#
#    25 * exp ( - 25 * x )
#
#  Antiderivative:
#
#    - exp ( - 25 * X )
#
#  Exact Integral:
#
#    1 - exp ( - 250 )
#
#  Approximate Integral:
#
#    1.00000000...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = 25.0 * np.exp ( - 25.0 * x )

  return fx

def p15_limits ( ):

#*****************************************************************************80
#
## p15_limits() returns the integration limits for problem 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 10.0

  return a, b

def p16_exact ( ):

#*****************************************************************************80
#
## p16_exact() returns the exact integral for problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 0.49363465089902720332

  return exact

def p16_fun ( x ):

#*****************************************************************************80
#
## p16_fun() evaluates the integrand for problem 16.
#
#  Interval:
#
#    0 <= x <= 10
#
#  Integrand:
#
#    50.0 / ( pi * ( 2500.0 * x * x + 1.0 ) )
#
#  Antiderivative:
#
#    ( 1 / PI ) * arctan ( 50 * X )
#
#  Approximate Integral (20 digits):
#
#    0.49363465089902720332
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = 50.0 / np.pi / ( 2500.0 * x**2 + 1.0 )

  return fx

def p16_limits ( ):

#*****************************************************************************80
#
## p16_limits() returns the integration limits for problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p17_exact ( ):

#*****************************************************************************80
#
## p17_exact() returns the estimated integral for problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.5

  return exact

def p17_fun ( x ):

#*****************************************************************************80
#
## p17_fun() evaluates the integrand for problem 17.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    ( sin ( 50 * pi * x ) )^2
#
#  Antiderivative:
#
#    1/2 X - sin ( 100 * PI * X ) / ( 200 * PI )
#
#  Approximate Integral:
#
#    0.5
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = ( np.sin ( 50.0 * np.pi * x ) )**2

  return fx

def p17_limits ( ):

#*****************************************************************************80
#
## p17_limits() returns the integration limits for problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p18_exact ( ):

#*****************************************************************************80
#
## p18_exact() returns the estimated integral for problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.17055734950243820437

  return exact

def p18_fun ( x ):

#*****************************************************************************80
#
## p18_fun() evaluates the integrand for problem 18.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    x / ( exp ( x ) + 1 )
#
#  Approximate Integral (20 digits):
#
#    0.17055734950243820437...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hermann Engels,
#    Numerical Quadrature and Cubature,
#    Academic Press, 1980.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = x / ( np.exp ( x ) + 1.0 )

  return fx

def p18_limits ( ):

#*****************************************************************************80
#
## p18_limits() returns the integration limits for problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p19_exact ( ):

#*****************************************************************************80
#
## p19_exact() returns the exact integral for problem 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = - 1.0

  return exact

def p19_fun ( x ):

#*****************************************************************************80
#
## p19_fun() evaluates the integrand for problem 19.
#
#  Discussion:
#
#    The integrand is singular at X = 0.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    ln ( x )
#
#  Antiderivative:
#
#    x * ln ( x ) - x
#
#  Exact Integral:
#
#    -1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.log ( x )

  return fx

def p19_limits ( ):

#*****************************************************************************80
#
## p19_limits() returns the integration limits for problem 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p20_exact ( ):

#*****************************************************************************80
#
## p20_exact() returns the estimated integral for problem 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 1.5643964440690497731

  return exact

def p20_fun ( x ):

#*****************************************************************************80
#
## p20_fun() evaluates the integrand for problem 20.
#
#  Interval:
#
#    -1 <= x <= 1
#
#  Integrand:
#
#    1 / ( X^2 + 1.005 )
#
#  Antiderivative:
#
#    ( 1 / sqrt ( 1.005 ) ) * arctan ( X / sqrt ( 1.005 ) )
#
#  Approximate Integral (20 digits):
#
#    1.5643964440690497731...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2009
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  fx = 1.0 / ( x**2 + 1.005 )

  return fx

def p20_limits ( ):

#*****************************************************************************80
#
## p20_limits() returns the integration limits for problem 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = -1.0
  b = 1.0

  return a, b

def p21_exact ( ):

#*****************************************************************************80
#
## p21_exact() returns the estimated integral for problem 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.21080273631018169851

  return exact

def p21_fun ( x ):

#*****************************************************************************80
#
## p21_fun() evaluates the integrand for problem 21.
#
#  Interval:
#
#    0 <= X <= 1
#
#  Integrand:
#
#       ( sech (   10.0 * ( x - 0.2 ) ) )^2
#     + ( sech (  100.0 * ( x - 0.4 ) ) )^4
#     + ( sech ( 1000.0 * ( x - 0.6 ) ) )^6
#
#  Exact Integral:
#
#    ( 1 + tanh ( 8 ) * tanh ( 2 ) ) / 10.0 + 2 / 150 + 2 / 1875
#
#  Approximate Integral (20 digits):
#
#    0.21080273631018169851...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = \
      ( 1.0 / np.cosh (   10.0 * ( x - 0.2 ) ) )**2 \
    + ( 1.0 / np.cosh (  100.0 * ( x - 0.4 ) ) )**4 \
    + ( 1.0 / np.cosh ( 1000.0 * ( x - 0.6 ) ) )**6

  return fx

def p21_limits ( ):

#*****************************************************************************80
#
## p21_limits() returns the integration limits for problem 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p22_exact ( ):

#*****************************************************************************80
#
## p22_exact() returns the estimated integral for problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  import numpy as np

  exact = 0.125 * np.log ( 9.0 ) + np.pi / np.sqrt ( 48.0 )

  return exact

def p22_fun ( x ):

#*****************************************************************************80
#
## p22_fun() evaluates the integrand for problem 22.
#
#  Interval:
#
#    0 <= X <= 1
#
#  Integrand:
#
#    1 / ( X^4 + X^2 + 1 )
#
#  Exact integral:
#
#    ln ( 9 ) / 8 + pi / sqrt ( 48 )
#
#  Approximate Integral (20 digits):
#
#    0.72810291322558188550...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  fx = 1.0 / ( x**4 + x**2 + 1.0 )

  return fx

def p22_limits ( ):

#*****************************************************************************80
#
## p22_limits() returns the integration limits for problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p23_exact ( ):

#*****************************************************************************80
#
## p23_exact() returns the estimated integral for problem 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.62471325642771360429

  return exact

def p23_fun ( x ):

#*****************************************************************************80
#
## p23_fun() evaluates the integrand for problem 23.
#
#  Discussion:
#
#    The integrand has a singularity at X = 0.
#    The integrand is discontinuous at X = 0.
#    The integrand is arbitrarily oscillatory as X decreases to 0.
#    The integrand becomes unbounded as X decreases to 0.
#
#    Integral ( 0 < X < 1 ) ( 1 / X ) sin ( 1 / X ) dX
#    = Integral ( 1 < X < Infinity ) ( 1 / X ) * sin ( X ) dX.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    ( 1 / x ) sin ( 1 / x )
#
#  Approximate Integral (20 digits):
#
#    0.62471325642771360429...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = ( 1.0 / x ) * np.sin ( 1.0 / x )

  return fx

def p23_limits ( ):

#*****************************************************************************80
#
## p23_limits() returns the integration limits for problem 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p24_exact ( ):

#*****************************************************************************80
#
## p24_exact() returns the estimated integral for problem 24.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = - 0.0067547455

  return exact

def p24_fun ( x ):

#*****************************************************************************80
#
## p24_fun() evaluates the integrand for problem 24.
#
#  Discussion:
#
#    The integrand is continuous, but nowhere differentiable.
#
#  Interval:
#
#    0 <= x <= 0.5
#
#  Integrand:
#
#    ( 1 / pi ) * sum ( 1 <= I < +oo ) 2^(-I) * cos ( 7^I * pi * X )
#
#  Approximate Integral:
#
#    - 0.0067547455
#
#  Antiderivative:
#
#    ( 1 / pi^2 ) * sum ( 1 <= I < +oo ) 14^(-I) * sin ( 7^I * pi * X )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#    Herbert Salzer, Norman Levine,
#    Table of a Weierstrass Continuous Nondifferentiable Function,
#    Mathematics of Computation,
#    Volume 15, pages 120 - 130, 1961.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  n_term = 40

  fx = x * 0

  for i in range ( 1, n_term + 1 ):
    fx = fx + np.cos ( 7.0**i * np.pi * x ) / 2.0**i
  fx = fx / np.pi

  return fx

def p24_limits ( ):

#*****************************************************************************80
#
## p24_limits() returns the integration limits for problem 24.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 0.5

  return a, b

def p25_exact ( ):

#*****************************************************************************80
#
## p25_exact() returns the estimated integral for problem 25.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  import numpy as np

  exact = 0.3 * np.log ( 0.3 ) + 0.7 * np.log ( 0.7 ) - 1.0

  return exact

def p25_fun ( x ):

#*****************************************************************************80
#
## p25_fun() evaluates the integrand for problem 25.
#
#  Interval:
#
#    0 <= x <= 1.
#
#  Integrand:
#
#    ln ( abs ( x - 0.7 ) )
#
#  Exact Integral:
#
#    0.3 * ln ( 0.3 ) + 0.7 * ln ( 0.7 ) - 1
#
#  Approximate Integral (20 digits):
#
#    -1.6108643020548934630
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kendall Atkinson,
#    An Introduction to Numerical Analysis,
#    Prentice Hall, 1984, page 303.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.log ( np.abs ( x - 0.7 ) )

  return fx

def p25_limits ( ):

#*****************************************************************************80
#
## p25_limits() returns the integration limits for problem 25.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p26_exact ( ):

#*****************************************************************************80
#
## p26_exact() returns the exact integral for problem 26.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 7.9549265210128452745

  return exact

def p26_fun ( x ):

#*****************************************************************************80
#
## p26_fun() evaluates the integrand for problem 26.
#
#  Interval:
#
#    0 <= x <= 2 pi
#
#  Integrand:
#
#    exp ( cos ( x ) )
#
#  Approximate Integral (20 digits):
#
#    7.9549265210128452745...
#
#  Exact Integral:
#
#    2 * pi * I0(1.0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kendall Atkinson,
#    An Introduction to Numerical Analysis,
#    Prentice Hall, 1984, page 262.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.exp ( np.cos ( x ) )

  return fx

def p26_limits ( ):

#*****************************************************************************80
#
## p26_limits() returns the integration limits for problem 26.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  import numpy as np

  a = 0.0
  b = 2.0 * np.pi

  return a, b

def p27_exact ( ):

#*****************************************************************************80
#
## p27_exact() returns the exact integral for problem 27.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = 5.0 - 6.0 * np.log ( 2.0 )

  return exact

def p27_fun ( x ):

#*****************************************************************************80
#
## p27_fun() evaluates the integrand for problem 27.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    1 / ( x^(1/2) + x^(1/3) )
#
#  Exact Integral:
#
#    5 - 6 * ln ( 2 )
#
#  Approximate Integral (20 digits):
#
#    0.84111691664032814350...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = 1.0 / ( np.sqrt ( x ) + x**(1.0/3.0) )

  return fx

def p27_limits ( ):

#*****************************************************************************80
#
## p27_limits() returns the integration limits for problem 27.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p28_exact ( ):

#*****************************************************************************80
#
## p28_exact() returns the exact integral for problem 28.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = ( 50.0 / 2501.0 ) * ( 1.0 - np.exp ( - 2.0 * np.pi ) )

  return exact

def p28_fun ( x ):

#*****************************************************************************80
#
## p28_fun() evaluates the integrand for problem 28.
#
#  Interval:
#
#    0 <= x <= 2 pi
#
#  Integrand:
#
#    exp ( - x ) * sin ( 50 * x )
#
#  Exact Integral:
#
#    50 / ( 2501 ) * ( 1 - exp ( - 2 * pi ) )
#
#  Approximate Integral (20 digits):
#
#    0.019954669277654778312...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kendall Atkinson,
#    An Introduction to Numerical Analysis,
#    Prentice Hall, 1984, page 303.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.exp ( - x ) * np.sin ( 50.0 * x )

  return fx

def p28_limits ( ):

#*****************************************************************************80
#
## p28_limits() returns the integration limits for problem 28.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the lower and upper limits of integration.
#
  import numpy as np

  a = 0.0
  b = 2.0 * np.pi

  return a, b

def p29_exact ( ):

#*****************************************************************************80
#
## p29_exact() returns the exact integral for problem 29.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = 1.0 - np.log ( 2.0 )

  return exact

def p29_fun ( x ):

#*****************************************************************************80
#
## p29_fun() evaluates the integrand for problem 29.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    1 / ( x + 2 )   for 0 < x < e - 2
#    0               otherwise
#
#  Exact Integral:
#
#    1 - ln ( 2 )
#
#  Approximate Integral (20 digits):
#
#    0.30685281944005469058...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2009
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = 1.0 / ( x + 2.0 )

  return fx

def p29_limits ( ):

#*****************************************************************************80
#
## p29_limits() returns the integration limits for problem 29.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  import numpy as np

  a = 0.0
  b = 1.0

  return a, b

def p30_antiderivative ( x ):

#*****************************************************************************80
#
## p30_antiderivate() evaluates the antiderivative for problem 30.
#
#  Interval:
#
#    2 <= x <= 7
#
#  Integrand:
#
#          cos (       x )
#    + 5 * cos ( 1.6 * x )
#    - 2 * cos ( 2.0 * x )
#    + 5 * cos ( 4.5 * x )
#    + 7 * cos ( 9.0 * x )
#
#  Antiderivative:
#
#          sin (       x )
#    + 5 * sin ( 1.6 * x ) / 1.6
#    - 2 * sin ( 2.0 * x ) / 2.0
#    + 5 * sin ( 4.5 * x ) / 4.5
#    + 7 * sin ( 9.0 * x ) / 9.0
#
#  Exact Integral:
#
#    -4.5275696251606720278
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne OLeary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#     LC: QA401.O44.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real ANTI(N), the antiderivative values.
#
  import numpy as np

  anti =  np.sin (       x ) \
    + 5.0 * np.sin ( 1.6 * x ) / 1.6 \
    - 2.0 * np.sin ( 2.0 * x ) / 2.0 \
    + 5.0 * np.sin ( 4.5 * x ) / 4.5 \
    + 7.0 * np.sin ( 9.0 * x ) / 9.0

  return anti

def p30_exact ( ):

#*****************************************************************************80
#
## p30_exact() returns the exact integral for problem 30.
#
#  Exact Integral:
#
#    -4.5275696251606720278
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  a, b = p30_limits ( )
  exact = p30_antiderivative ( b ) - p30_antiderivative ( a )

  return exact

def p30_fun ( x ):

#*****************************************************************************80
#
## p30_fun() evaluates the integrand for problem 30.
#
#  Interval:
#
#    2 <= x <= 7
#
#  Integrand:
#
#          cos (       x )
#    + 5 * cos ( 1.6 * x )
#    - 2 * cos ( 2.0 * x )
#    + 5 * cos ( 4.5 * x )
#    + 7 * cos ( 9.0 * x )
#
#  Antiderivative:
#
#          sin (       x )
#    + 5 * sin ( 1.6 * x ) / 1.6
#    - 2 * sin ( 2.0 * x ) / 2.0
#    + 5 * sin ( 4.5 * x ) / 4.5
#    + 7 * sin ( 9.0 * x ) / 9.0
#
#  Exact Integral:
#
#    -4.5275696251606720278
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne OLeary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#     LC: QA401.O44.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx =      np.cos (       x ) \
    + 5.0 * np.cos ( 1.6 * x ) \
    - 2.0 * np.cos ( 2.0 * x ) \
    + 5.0 * np.cos ( 4.5 * x ) \
    + 7.0 * np.cos ( 9.0 * x )

  return fx

def p30_limits ( ):

#*****************************************************************************80
#
## p30_limits() returns the integration limits for problem 30.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the lower and upper limits of integration.
#
  a = 2.0
  b = 7.0

  return a, b

def p31_exact ( ):

#*****************************************************************************80
#
## p31_exact() returns the exact integral for problem 31.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = 2.0 * np.arctan ( 4.0 )

  return exact

def p31_fun ( x ):

#*****************************************************************************80
#
## p31_fun() evaluates the integrand for problem 31.
#
#  Discussion:
#
#    A simple Newton-Cotes quadrature rule, in which the order of the
#    rule is increased, but the interval is not subdivided, diverges
#    for this integrand.
#
#    This is Runge's function, a standard example of the perils of
#    using high order polynomial interpolation at equally spaced nodes.
#    Since this is exactly what is really going on in a Newton Cotes
#    rule, it is little wonder that the result is so poor.
#
#  Interval:
#
#    -4 <= x <= 4
#
#  Integrand:
#
#    1 / ( 1 + x^2 )
#
#  Antiderivative:
#
#    arctan ( x )
#
#  Exact Integral:
#
#    2 * arctan ( 4 )
#
#  Approximate Integral (20 digits):
#
#    2.6516353273360649301...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kendall Atkinson,
#    An Introduction to Numerical Analysis,
#    Prentice Hall, 1984, page 266.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  fx = 1.0 / ( 1.0 + x**2 )

  return fx

def p31_limits ( ):

#*****************************************************************************80
#
## p31_limits() returns the integration limits for problem 31.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = - 4.0
  b =   4.0

  return a, b

def p32_exact ( ):

#*****************************************************************************80
#
## p32_exact() returns the exact integral for problem 32.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = - 0.5 * ( np.exp ( np.pi ) + 1.0 )

  return exact

def p32_fun ( x ):

#*****************************************************************************80
#
## p32_fun() evaluates the integrand for problem 32.
#
#  Interval:
#
#    0 <= x <= pi
#
#  Integrand:
#
#    exp ( x ) * cos ( x )
#
#  Antiderivative:
#
#    0.5 * exp ( x ) * ( sin ( X ) + cos ( x ) )
#
#  Exact Integral:
#
#    - 0.5 * ( exp ( PI ) + 1 )
#
#  Approximate Integral (20 digits):
#
#    -12.070346316389634503...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kendall Atkinson,
#    An Introduction to Numerical Analysis,
#    Prentice Hall, 1984, page 254, 277, 297.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.exp ( x ) * np.cos ( x )

  return fx

def p32_limits ( ):

#*****************************************************************************80
#
## p32_limits() returns the integration limits for problem 32.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  import numpy as np

  a = 0.0
  b = np.pi

  return a, b

def p33_exact ( ):

#*****************************************************************************80
#
## p33_exact() returns the exact integral for problem 33.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = 0.5 * np.sqrt ( np.pi )

  return exact

def p33_fun ( x ):

#*****************************************************************************80
#
## p33_fun() evaluates the integrand for problem 33.
#
#  Discussion:
#
#    The integrand is singular at both endpoints of the interval.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    sqrt ( - ln ( x ) )
#
#  Exact Integral:
#
#    sqrt ( pi ) / 2
#
#  Approximate Integral (20 digits):
#
#    0.88622692545275801365...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kendall Atkinson,
#    An Introduction to Numerical Analysis,
#    Prentice Hall, 1984, page 307.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.sqrt ( - np.log ( x ) )

  return fx

def p33_limits ( ):

#*****************************************************************************80
#
## p33_limits() returns the integration limits for problem 33.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p34_exact ( ):

#*****************************************************************************80
#
## p34_exact() returns the exact integral for problem 34.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 1627879.0 / 1500.0

  return exact

def p34_fun ( x ):

#*****************************************************************************80
#
## p34_fun() evaluates the integrand for problem 34.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    ( 10 * x - 1 ) * ( 10 * x - 1.1 ) * ( 10 * x - 1.2 ) * ( 10 * x - 1.3 )
#
#  Exact Integral:
#
#    1627879 / 1500
#
#  Approximate Integral (20 digits):
#
#    1085.2526666666666666...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hermann Engels,
#    Numerical Quadrature and Cubature,
#    Academic Press, 1980.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  fx = ( 10.0 * x - 1.0 ) * \
       ( 10.0 * x - 1.1 ) * \
       ( 10.0 * x - 1.2 ) * \
       ( 10.0 * x - 1.3 )

  return fx

def p34_limits ( ):

#*****************************************************************************80
#
## p34_limits() returns the integration limits for problem 34.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p35_exact ( ):

#*****************************************************************************80
#
## p35_exact() returns the exact integral for problem 35.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 26.0

  return exact

def p35_fun ( x ):

#*****************************************************************************80
#
## p35_fun() evaluates the integrand for problem 35.
#
#  Interval:
#
#    -9 <= x <= 100
#
#  Integrand:
#
#    1 / sqrt ( abs ( x ) )
#
#  Exact Integral:
#
#    26
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hermann Engels,
#    Numerical Quadrature and Cubature,
#    Academic Press, 1980.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = 1.0 / np.sqrt ( np.abs ( x ) )

  return fx

def p35_limits ( ):

#*****************************************************************************80
#
## p35_limits() returns the integration limits for problem 35.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = -9.0
  b = 100.0

  return a, b

def p36_exact ( ):

#*****************************************************************************80
#
## p36_exact() returns the exact integral for problem 36.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  alpha = p36_parameters ( )

  exact = 1.0 / ( alpha + 1.0 )**2

  return exact

def p36_fun ( x ):

#*****************************************************************************80
#
## p36_fun() evaluates the integrand for problem 36.
#
#  Discussion:
#
#    The problem has a parameter ALPHA.
#
#    The integrand has an endpoint singularity at X=0.
#
#    Suggested values of ALPHA include -0.9 through 2.6.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    x^alpha * ln ( 1 / x )
#
#  Exact Integral:
#
#    1 / ( alpha + 1 )^2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 83.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  alpha = p36_parameters ( )

  fx = x**alpha * np.log ( 1.0 / x )

  return fx

def p36_limits ( ):

#*****************************************************************************80
#
## p36_limits() returns the integration limits for problem 36.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p36_parameters ( alpha_user = None ):

#*****************************************************************************80
#
## p36_parameters() sets or gets the p36 parameters.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real alpha_user: a new default value for alpha, if supplied.
#
#  Output:
#
#    real alpha: the current default value of alpha.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( p36_parameters, "alpha_default" ):
    p36_parameters.alpha_default = - 0.9
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    p36_parameters.alpha_default = alpha_user
#
#  Return values.
#
  alpha = p36_parameters.alpha_default

  return alpha

def p37_exact ( ):

#*****************************************************************************80
#
## p37_exact() returns the exact integral for problem 37.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  alpha = p37_parameters ( )

  exact = np.arctan ( ( 4.0 - np.pi ) * 4.0**( alpha - 1.0 ) ) \
        + np.arctan (         np.pi   * 4.0**( alpha - 1.0 ) )

  return exact

def p37_fun ( x ):

#*****************************************************************************80
#
## p37_fun() evaluates the integrand for problem 37.
#
#  Discussion:
#
#    The problem has a parameter ALPHA that can be set by calling
#    P37_param_set.  It had a default value of 5.0.
#
#    The integrand has a peak of height 4^ALPHA at X = PI/4.
#
#    Suggested values of ALPHA include 0 through 20.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    4^(-ALPHA) / ( ( x - PI/4 )^2 + 16^(-ALPHA) )
#
#  Exact Integral:
#
#    atan ( ( 4 - PI ) * 4^(ALPHA-1) ) + atan ( PI * 4^(ALPHA-1) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 83.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  alpha = p37_parameters ( )

  fx = 4.0 ** ( - alpha ) / ( ( x - 0.25 * np.pi )**2 + 16.0**(-alpha) )

  return fx

def p37_limits ( ):

#*****************************************************************************80
#
## p37_limits() returns the integration limits for problem 37.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p37_parameters ( alpha_user = None ):

#*****************************************************************************80
#
## p37_parameters() sets or gets the p37 parameters.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real alpha_user: a new default value for alpha, if supplied.
#
#  Output:
#
#    real alpha: the current default value of alpha.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( p37_parameters, "alpha_default" ):
    p37_parameters.alpha_default = 5.0
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    p37_parameters.alpha_default = alpha_user
#
#  Return values.
#
  alpha = p37_parameters.alpha_default

  return alpha

def p38_exact ( ):

#*****************************************************************************80
#
## p38_exact() returns the exact integral for problem 38.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  from scipy.special import j0
  import numpy as np

  alpha = p38_parameters ()

  x = 2.0**alpha

  exact = np.pi * j0 ( x )

  return exact

def p38_fun ( x ):

#*****************************************************************************80
#
## p38_fun() evaluates the integrand for problem 38.
#
#  Discussion:
#
#    The problem has a parameter ALPHA that can be set by calling
#    P38_param_set.
#
#    The integrand oscillates more strongly as ALPHA is increased.
#
#    The suggested range for ALPHA is 0 to 10.
#
#  Interval:
#
#    0 <= x <= pi
#
#  Integrand:
#
#    cos ( 2^ALPHA * sin ( x ) )
#
#  Exact Integral:
#
#    pi * J0 ( 2^ALPHA )
#
#    where J0 ( x ) is the J Bessel function of order 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 83.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  alpha = p38_parameters ( )

  fx = np.cos ( 2.0**alpha * np.sin ( x ) )

  return fx

def p38_limits ( ):

#*****************************************************************************80
#
## p38_limits() returns the integration limits for problem 38.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  import numpy as np

  a = 0.0
  b = np.pi

  return a, b

def p38_parameters ( alpha_user = None ):

#*****************************************************************************80
#
## p38_parameters() sets or gets the p38 parameters.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real alpha_user: a new default value for alpha, if supplied.
#
#  Output:
#
#    real alpha: the current default value of alpha.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( p38_parameters, "alpha_default" ):
    p38_parameters.alpha_default = 3.0
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    p38_parameters.alpha_default = alpha_user
#
#  Return values.
#
  alpha = p38_parameters.alpha_default

  return alpha

def p39_exact ( ):

#*****************************************************************************80
#
## p39_exact() returns the exact integral for problem 39.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  alpha = p39_parameters ( )

  exact = ( ( 2.0 / 3.0 )**( alpha + 1.0 ) \
          + ( 1.0 / 3.0 )**( alpha + 1.0 ) ) / ( alpha + 1.0 )

  return exact

def p39_fun ( x ):

#*****************************************************************************80
#
## p39_fun() evaluates the integrand for problem 39.
#
#  Discussion:
#
#    The problem has a parameter ALPHA.
#
#    The integrand has a singularity at an internal point ( x = 1/3 )
#    with small binary period.
#
#    The suggested range for ALPHA is -0.8 through 2.1.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    ( abs ( x - 1/3 ) )^alpha
#
#  Exact Integral:
#
#    ( (2/3)^(alpha+1) + (1/3)^(alpha+1) ) / ( alpha + 1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 83.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  alpha = p39_parameters ( )

  fx = ( np.abs ( x - 1.0 / 3.0 ) )**alpha

  return fx

def p39_limits ( ):

#*****************************************************************************80
#
## p39_limits() returns the integration limits for problem 39.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p39_parameters ( alpha_user = None ):

#*****************************************************************************80
#
## p39_parameters() sets or gets the p39 parameters.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real alpha_user: a new default value for alpha, if supplied.
#
#  Output:
#
#    real alpha: the current default value of alpha.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( p39_parameters, "alpha_default" ):
    p39_parameters.alpha_default = -0.5
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    p39_parameters.alpha_default = alpha_user
#
#  Return values.
#
  alpha = p39_parameters.alpha_default

  return alpha

def p40_exact ( ):

#*****************************************************************************80
#
## p40_exact() returns the exact integral for problem 40.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  alpha = p40_parameters ( )

  exact = ( ( 1.0 - 0.25 * np.pi )**( alpha + 1.0 ) \
          + (     + 0.25 * np.pi )**( alpha + 1.0 ) ) \
          / ( alpha + 1.0 )

  return exact

def p40_fun ( x ):

#*****************************************************************************80
#
## p40_fun() evaluates the integrand for problem 40.
#
#  Discussion:
#
#    The problem has a parameter ALPHA that can be set by calling
#    P40_param_set.
#
#    The integrand has a singularity at an internal point ( x = pi/4 ).
#
#    The suggested range for ALPHA is -0.8 through 2.1.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    ( abs ( x - pi/4 ) )^alpha
#
#  Exact Integral:
#
#    ( (1-pi/4)^(alpha+1) + (pi/4)^(alpha+1) ) / ( alpha + 1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 83.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  alpha = p40_parameters ( )

  fx = ( np.abs ( x - 0.25 * np.pi ) )**alpha

  return fx

def p40_limits ( ):

#*****************************************************************************80
#
## p40_limits() returns the integration limits for problem 40.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p40_parameters ( alpha_user = None ):

#*****************************************************************************80
#
## p40_parameters() sets or gets the p40 parameters.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real alpha_user: a new default value for alpha, if supplied.
#
#  Output:
#
#    real alpha: the current default value of alpha.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( p40_parameters, "alpha_default" ):
    p40_parameters.alpha_default = -0.5
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    p40_parameters.alpha_default = alpha_user
#
#  Return values.
#
  alpha = p40_parameters.alpha_default

  return alpha

def p41_exact ( ):

#*****************************************************************************80
#
## p41_exact() returns the exact integral for problem 41.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  alpha = p41_parameters ( )

  exact = np.pi / np.sqrt ( ( 1.0 + 2.0**(-alpha) )**2 - 1.0 )

  return exact

def p41_fun ( x ):

#*****************************************************************************80
#
## p41_fun() evaluates the integrand for problem 41.
#
#  Discussion:
#
#    The problem has a parameter ALPHA.
#
#    The integrand has a singularity at both endpoints, whose
#    severity increases with ALPHA.
#
#    The suggested range for ALPHA is 1 through 20.
#
#  Interval:
#
#    -1 <= x <= 1
#
#  Integrand:
#
#    1 / ( sqrt ( 1 - x^2 ) * ( x + 1 + 2^(-alpha) ) )
#
#  Exact Integral:
#
#    pi / sqrt ( ( 1 + 2^(-alpha) ) - 1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 84.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  alpha = p41_parameters ( )

  fx = 1.0 / ( np.sqrt ( 1.0 - x**2 ) * ( x + 1.0 + 0.5**alpha ) )

  return fx

def p41_limits ( ):

#*****************************************************************************80
#
## p41_limits() returns the integration limits for problem 41.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = -1.0
  b = 1.0

  return a, b

def p41_parameters ( alpha_user = None ):

#*****************************************************************************80
#
## p41_parameters() sets or gets the p41 parameters.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real alpha_user: a new default value for alpha, if supplied.
#
#  Output:
#
#    real alpha: the current default value of alpha.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( p41_parameters, "alpha_default" ):
    p41_parameters.alpha_default = 3.0
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    p41_parameters.alpha_default = alpha_user
#
#  Return values.
#
  alpha = p41_parameters.alpha_default

  return alpha

def p42_exact ( ):

#*****************************************************************************80
#
## p42_exact() returns the exact integral for problem 42.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  from scipy.special import gamma

  alpha = p42_parameters ( )

  exact = 2.0**( alpha - 2.0 ) * ( gamma ( alpha / 2.0 ) )**2 / gamma ( alpha )

  return exact

def p42_fun ( x ):

#*****************************************************************************80
#
## p42_fun() evaluates the integrand for problem 42.
#
#  Discussion:
#
#    The problem has a parameter ALPHA.
#
#    The integrand has a singularity at X = 0 if ALPHA < 1.
#
#    The suggested range for ALPHA is 0.1 through 2.
#
#  Interval:
#
#    0 <= x <= pi/2
#
#  Integrand:
#
#    ( sin(x) )^( alpha - 1 )
#
#  Exact Integral:
#
#    2^( alpha - 2 ) * ( Gamma(alpha/2) )^2 / Gamma(alpha)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 84.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  alpha = p42_parameters ( )

  fx = np.sin ( x )**( alpha - 1.0 )

  return fx

def p42_limits ( ):

#*****************************************************************************80
#
## p42_limits() returns the integration limits for problem 42.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  import numpy as np

  a = 0.0
  b = np.pi / 2.0

  return a, b

def p42_parameters ( alpha_user = None ):

#*****************************************************************************80
#
## p42_parameters() sets or gets the p42 parameters.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real alpha_user: a new default value for alpha, if supplied.
#
#  Output:
#
#    real alpha: the current default value of alpha.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( p42_parameters, "alpha_default" ):
    p42_parameters.alpha_default = 0.3
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    p42_parameters.alpha_default = alpha_user
#
#  Return values.
#
  alpha = p42_parameters.alpha_default

  return alpha

def p43_exact ( ):

#*****************************************************************************80
#
## p43_exact() returns the exact integral for problem 43.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  from scipy.special import gamma

  alpha = p43_parameters ()

  exact = gamma ( alpha )

  return exact

def p43_fun ( x ):

#*****************************************************************************80
#
## p43_fun() evaluates the integrand for problem 43.
#
#  Discussion:
#
#    The problem has a parameter ALPHA that can be set by calling
#    P43_param_set.
#
#    The suggested parameter range is 0.1 <= ALPHA <= 2.0.
#
#    The integrand has an algebraic endpoint singularity at X = 1
#    times a singular factor.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    ( ln ( 1 / x ) )^( alpha - 1 )
#
#  Exact Integral:
#
#    Gamma(alpha)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 84.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  alpha = p43_parameters ( )

  fx = ( np.log ( 1.0 / x ) )**( alpha - 1.0 )

  return fx

def p43_limits ( ):

#*****************************************************************************80
#
## p43_limits() returns the integration limits for problem 43.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p43_parameters ( alpha_user = None ):

#*****************************************************************************80
#
## p43_parameters() sets or gets the p43 parameters.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real alpha_user: a new default value for alpha, if supplied.
#
#  Output:
#
#    real alpha: the current default value of alpha.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( p43_parameters, "alpha_default" ):
    p43_parameters.alpha_default = 0.3
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    p43_parameters.alpha_default = alpha_user
#
#  Return values.
#
  alpha = p43_parameters.alpha_default

  return alpha

def p44_exact ( ):

#*****************************************************************************80
#
## p44_exact() returns the exact integral for problem 44.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  alpha = p44_parameters ( )

  exact = ( 20.0 * np.sin ( 2.0**alpha ) \
    - 2.0**alpha * np.cos ( 2.0**alpha ) \
    + 2.0**alpha * np.exp ( -20.0 ) ) / ( 400.0 + 4.0**alpha )

  return exact

def p44_fun ( x ):

#*****************************************************************************80
#
## p44_fun() evaluates the integrand for problem 44.
#
#  Discussion:
#
#    The problem has a parameter ALPHA that can be set by calling
#    P44_param_set.
#
#    The suggested parameter range is 0.0 <= ALPHA <= 9.0.
#
#    As ALPHA increases, the integrand becomes more oscillatory.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    exp ( 20 * ( x - 1 ) ) * sin ( 2^alpha * x )
#
#  Exact Integral:
#
#    ( 20 sin ( 2^alpha ) - 2^alpha cos ( 2^alpha )
#    + 2^alpha exp ( -20 ) ) / ( 400 + 4^alpha )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 84.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  alpha = p44_parameters ( )

  fx = np.exp ( 20.0 * ( x - 1.0 ) ) * np.sin ( 2.0**alpha * x )

  return fx

def p44_limits ( ):

#*****************************************************************************80
#
## p44_limits() returns the integration limits for problem 44.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p44_parameters ( alpha_user = None ):

#*****************************************************************************80
#
## p44_parameters() sets or gets the p44 parameters.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real alpha_user: a new default value for alpha, if supplied.
#
#  Output:
#
#    real alpha: the current default value of alpha.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( p44_parameters, "alpha_default" ):
    p44_parameters.alpha_default = 2.0
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    p44_parameters.alpha_default = alpha_user
#
#  Return values.
#
  alpha = p44_parameters.alpha_default

  return alpha

def p45_exact ( ):

#*****************************************************************************80
#
## p45_exact() returns the exact integral for problem 45.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  from scipy.special import j0
  import numpy as np

  alpha = p45_parameters ( )

  exact = np.pi * np.cos ( 2.0**( alpha - 1.0 ) ) * j0 ( 2.0**( alpha - 1.0 ) )

  return exact

def p45_fun ( x ):

#*****************************************************************************80
#
## p45_fun() evaluates the integrand for problem 45.
#
#  Discussion:
#
#    The problem has a parameter ALPHA that can be set by calling
#    P45_param_set.
#
#    The suggested parameter range is 0.0 <= ALPHA <= 8.0.
#
#  Interval:
#
#    0 <= X <= 1
#
#  Integrand:
#
#    cos ( 2^alpha * x ) / sqrt ( x * ( 1 - x ) )
#
#  Exact Integral:
#
#    pi * cos ( 2^(alpha-1) ) * J0 ( 2^(alpha-1) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 84.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  alpha = p45_parameters ( )

  fx = np.cos ( 2.0**alpha * x ) / np.sqrt ( x * ( 1.0 - x ) )

  return fx

def p45_limits ( ):

#*****************************************************************************80
#
## p45_limits() returns the integration limits for problem 45.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p45_parameters ( alpha_user = None ):

#*****************************************************************************80
#
## p45_parameters() sets or gets the p45 parameters.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real alpha_user: a new default value for alpha, if supplied.
#
#  Output:
#
#    real alpha: the current default value of alpha.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( p45_parameters, "alpha_default" ):
    p45_parameters.alpha_default = 2.0
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    p45_parameters.alpha_default = alpha_user
#
#  Return values.
#
  alpha = p45_parameters.alpha_default

  return alpha

def p46_exact ( ):

#*****************************************************************************80
#
## p46_exact() returns the exact integral for problem 46.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 6.0690909595647754101

  return exact

def p46_fun ( x ):

#*****************************************************************************80
#
## p46_fun() evaluates the integrand for problem 46.
#
#  Discussion:
#
#    The problem has a parameter ALPHA.
#
#    The integrand is the radius of an ellipse as a function of angle.
#
#    The integral represents the arc length of the ellipse.
#
#    The suggested parameter range is 0.0 <= ALPHA < 1.0.  ALPHA is
#    the eccentricity of the ellipse.
#
#  Interval:
#
#    0 <= theta <= 2 pi
#
#  Integrand:
#
#    r(theta) = ( 1 - alpha^2 ) / ( 1 - alpha * cos ( theta ) )
#
#  Exact Integral:
#
#    When alpha = sin ( pi / 12 ), then
#
#      6.0690909595647754101
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Crandall,
#    Projects in Scientific Computing,
#    Springer, 2000, page 47.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  alpha = p46_parameters ( )

  fx = ( 1.0 - alpha**2 ) / ( 1.0 - alpha * np.cos ( x ) )

  return fx

def p46_limits ( ):

#*****************************************************************************80
#
## p46_limits() returns the integration limits for problem 46.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  import numpy as np

  a = 0.0
  b = 2.0 * np.pi

  return a, b

def p46_parameters ( alpha_user = None ):

#*****************************************************************************80
#
## p46_parameters() sets or gets the p46 parameters.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real alpha_user: a new default value for alpha, if supplied.
#
#  Output:
#
#    real alpha: the current default value of alpha.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( p46_parameters, "alpha_default" ):
    p46_parameters.alpha_default = np.sin ( np.pi / 12.0 )
#
#  Update defaults if input was supplied.
#
  if ( alpha_user is not None ):
    p46_parameters.alpha_default = alpha_user
#
#  Return values.
#
  alpha = p46_parameters.alpha_default

  return alpha

def p47_exact ( ):

#*****************************************************************************80
#
## p47_exact() returns the exact integral for problem 47.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = - 4.0 / 9.0

  return exact

def p47_fun ( x ):

#*****************************************************************************80
#
## p47_fun() evaluates the integrand for problem 47.
#
#  Discussion:
#
#    The function is singular at the left endpoint.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    sqrt ( x ) * ln ( x )
#
#  Exact Integral:
#
#    -4/9 = -0.4444...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 101.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.sqrt ( x ) * np.log ( x )

  return fx

def p47_limits ( ):

#*****************************************************************************80
#
## p47_limits() returns the integration limits for problem 47.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p48_exact ( ):

#*****************************************************************************80
#
## p48_exact() returns the exact integral for problem 48.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = -4.0

  return exact

def p48_fun ( x ):

#*****************************************************************************80
#
## p48_fun() evaluates the integrand for problem 48.
#
#  Discussion:
#
#    The function is singular at the left endpoint.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    ln ( x ) / sqrt ( x )
#
#  Exact Integral:
#
#    -4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 103.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.log ( x ) / np.sqrt ( x )

  return fx

def p48_limits ( ):

#*****************************************************************************80
#
## p48_limits() returns the integration limits for problem 48.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p49_exact ( ):

#*****************************************************************************80
#
## p49_exact() returns the exact integral for problem 49.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = 61.0 * np.log ( 2.0 ) + 77.0 * np.log ( 7.0 ) / 4.0 - 27.0

  return exact

def p49_fun ( x ):

#*****************************************************************************80
#
## p49_fun() evaluates the integrand for problem 49.
#
#  Discussion:
#
#    The function is singular at two internal points, 1 and sqrt(2).
#
#  Interval:
#
#    0 <= x <= 3
#
#  Integrand:
#
#    x^3 * log ( abs ( ( x^2 - 1 ) * ( x^2 - 2 ) ) )
#
#  Exact Integral:
#
#    61 log ( 2 ) + (77/4) log ( 7 ) - 27 = 52.7408...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 104.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  gx = np.abs ( ( x**2 - 1.0 ) * ( x**2 - 2.0 ) )
  fx = x**3 * np.log ( gx )

  return fx

def p49_limits ( ):

#*****************************************************************************80
#
## p49_limits() returns the integration limits for problem 49.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 3.0

  return a, b

def p50_exact ( ):

#*****************************************************************************80
#
## p50_exact() returns the exact integral for problem 50.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  from scipy.special import sici
  import numpy as np

  euler_mascheroni = 0.5772156649015328

  t = 10.0 * np.pi

  si, ci = sici ( t )
  exact = ( - euler_mascheroni - np.log ( t ) + ci ) / t

  return exact

def p50_fun ( x ):

#*****************************************************************************80
#
## p50_fun() evaluates the integrand for problem 50.
#
#  Discussion:
#
#    The function has a removable singularity at x = 0.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    log ( x ) * sin ( 10 * pi * x )
#
#  Exact Integral:
#
#    ( - gamma - log ( 10 * pi ) + Ci ( 10 * pi ) ) / ( 10 * pi ) 
#      = -0.12813684839916734...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#      Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 106.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.log ( x ) * np.sin ( 10.0 * np.pi * x )

  return fx

def p50_limits ( ):

#*****************************************************************************80
#
## p50_limits() returns the integration limits for problem 50.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p51_exact ( ):

#*****************************************************************************80
#
## p51_exact() returns the exact integral for problem 51.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  from scipy.special import sici
  import numpy as np

  si, ci = sici ( 1.0 )

  exact = - ( ci * np.sin ( 1.0 ) \
    + ( 0.5 * np.pi  - si ) * np.cos ( 1.0 ) ) / np.pi

  return exact

def p51_fun ( x ):

#*****************************************************************************80
#
## p51_fun() evaluates the integrand for problem 51.
#
#  Discussion:
#
#    The function has a removable singularity at x = 0.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    ln ( x ) / ( 1 + ( ln(x) )^2 )^2
#
#  Exact Integral:
#
#    - ( ci(1) * sin(1) + ( pi/2 - si(1) ) * cos(1) ) / pi = - 0.1892752...
#    ??? -0.19781355915946125
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 108.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.log ( x ) / ( 1.0 + ( np.log ( x ) )**2 )**2

  return fx

def p51_limits ( ):

#*****************************************************************************80
#
## p51_limits() returns the integration limits for problem 51.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p52_exact ( ):

#*****************************************************************************80
#
## p52_exact() returns the exact integral for problem 52.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = np.log ( 125.0 / 631.0 ) / 18.0

  return exact

def p52_fun ( x ):

#*****************************************************************************80
#
## p52_fun() evaluates the integrand for problem 52.
#
#  Discussion:
#
#    The function has a singularity at x = 0.
#
#  Interval:
#
#    -1 <= x <= 5
#
#  Integrand:
#
#    1 / ( x * ( 5 * x^3 + 6 ) )
#
#  Exact Integral:
#
#    ln ( 125 / 631 ) / 18 = -0.089944006957717...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 109.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = 1.0 / x / ( 5.0 * x**3 + 6.0 )
 
  return fx

def p52_limits ( ):

#*****************************************************************************80
#
## p52_limits() returns the integration limits for problem 52.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = -1.0
  b = 5.0

  return a, b

def p53_exact ( ):

#*****************************************************************************80
#
## p53_exact() returns the exact integral for problem 53.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = 0.5 * np.pi \
        - np.arctan ( 1.0 / np.sqrt ( 2.0 ) ) \
        + np.log ( 3.0 ) / 2.0

  return exact

def p53_fun ( x ):

#*****************************************************************************80
#
## p53_fun() evaluates the integrand for problem 53.
#
#  Discussion:
#
#    The integrand is singular at x = -1 + sqrt ( 3 ) = 0.732...
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    1 / sqrt ( abs ( x^2 + 2 * x - 2 ) )
#
#  Exact Integral:
#
#    pi / 2 - arctan ( 1 / sqrt ( 2 ) ) + ln ( 3 ) / 2 = 1.504622762458564...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#      Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 110.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = 1.0 / np.sqrt ( np.abs ( x**2 + 2.0 * x - 2.0 ) )

  return fx

def p53_limits ( ):

#*****************************************************************************80
#
## p53_limits() returns the integration limits for problem 53.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p54_exact ( ):

#*****************************************************************************80
#
## p54_exact() returns the exact integral for problem 54.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = 2.0 / np.sqrt ( 3.0 )

  return exact

def p54_fun ( x ):

#*****************************************************************************80
#
## p54_fun() evaluates the integrand for problem 54.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    2 / ( 2 + sin ( 10 * PI * x ) )
#
#  Exact Integral:
#
#    2 / sqrt ( 3 ) = 1.154700538379252...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Prem Kythe, Pratap Puri,
#    Computational Methods for Linear Integral Equations,
#    Birkhaeuser, 2002.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = 2.0 / ( 2.0 + np.sin ( 10.0 * np.pi * x ) )

  return fx

def p54_limits ( ):

#*****************************************************************************80
#
## p54_limits() returns the integration limits for problem 54.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p55_exact ( ):

#*****************************************************************************80
#
## p55_exact() returns the exact integral for problem 55.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  from scipy.special import erf
  import numpy as np

  a, b = p55_limits ( )
  c, x0 = p55_parameters ( )

  exact = np.sqrt ( np.pi ) \
    * ( erf ( c * ( b - x0 ) ) - erf ( c * ( a - x0 ) ) ) \
    / ( 2.0 * c )

  return exact

def p55_fun ( x ):

#*****************************************************************************80
#
## p55_fun() evaluates the integrand for problem 55.
#
#  Interval:
#
#    a = 0 <= x <= 1 = b
#
#  Integrand:
#
#    exp ( - c^2 * ( x - x0 )^2 )
#
#  Exact Integral:
#
#    sqrt ( pi )
#    * ( erf ( c * ( b - x0 ) ) - erf ( c * ( a - x0 ) ) )
#    / ( 2 * c )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  c, x0 = p55_parameters ( )
 
  fx = np.exp ( - c * c * ( x - x0 )**2 )

  return fx

def p55_limits ( ):

#*****************************************************************************80
#
## p55_limits() returns the integration limits for problem 55.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2009
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def p55_parameters ( c_user = None, x0_user = None ):

#*****************************************************************************80
#
## p55_parameters() sets or gets the p55 parameters.
#
#  Discussion:
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real c_user: a new default value for c, if supplied.
#
#    real x0_user: a new default value for x0, if supplied.
#
#  Output:
#
#    real c: the current default value of c.
#
#    real x0: the current default value of x0.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( p55_parameters, "c_default" ):
    p55_parameters.c_default = 3.0

  if not hasattr ( p55_parameters, "x0_default" ):
    p55_parameters.x0_default = 0.75
#
#  Update defaults if input was supplied.
#
  if ( c_user is not None ):
    p55_parameters.c_default = c_user

  if ( x0_user is not None ):
    p55_parameters.x0_default = x0_user
#
#  Return values.
#
  c = p55_parameters.c_default
  x0 = p55_parameters.x0_default

  return c, x0

def p56_exact ( ):

#*****************************************************************************80
#
## p56_exact() returns the estimated integral for problem 56.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 1.9922524079504000171

  return exact

def p56_fun ( x ):

#*****************************************************************************80
#
## p56_fun() evaluates the integrand for problem 56.
#
#  Interval:
#
#    -1 <= x <= 1
#
#  Integrand:
#
#    1 / ( x^6 + 0.9 )
#
#  Approximate Integral (20 digits):
#
#    1.9922524079504000171...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software,
#    edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  fx = 1.0 / ( x**6 + 0.9 )

  return fx

def p56_limits ( ):

#*****************************************************************************80
#
## p56_limits() returns the integration limits for problem 56.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = - 1.0
  b = 1.0

  return a, b

def p57_exact ( ):

#*****************************************************************************80
#
## p57_exact() returns the exact integral for problem 57.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.4

  return exact

def p57_fun ( x ):

#*****************************************************************************80
#
## p57_fun() evaluates the integrand for problem 57.
#
#  Interval:
#
#    0 <= x <= 1
#
#  Integrand:
#
#    x^(3/2)
#
#  Antiderivative:
#
#    (2/5) * x^(5/2)
#
#  Exact Integral:
#
#    0.4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner,
#    Comparison of Numerical Quadrature Formulas,
#    in Mathematical Software, edited by John R Rice,
#    Academic Press, 1971.
#
#  Input:
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the integrand values.
#
  import numpy as np

  fx = np.sqrt ( x**3 )

  return fx

def p57_limits ( ):

#*****************************************************************************80
#
## p57_limits() returns the integration limits for problem 57.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B, the limits of integration.
#
  a = 0.0
  b = 1.0

  return a, b

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == "__main__" ):
  timestamp ( )
  test_int_test ( )
  timestamp ( )

