#! /usr/bin/env python3
#
def test_opt_test ( ):

#*****************************************************************************80
#
## test_opt_test() tests test_opt().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'test_opt_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test test_opt().' )

  p00_title_test ( )
  p00_n_test ( )
  p00_start_test ( )
  p00_f_test ( )
  p00_sol_test ( )
  p00_gdif_test ( )

# gradient_method_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_opt_test():' )
  print ( '  Normal end of execution.' )

  return

def p00_n ( problem ):

#*****************************************************************************80
#
## p00_n() returns the number of variables for any problem.
#
#  Discussion:
#
#    Some of the problems in this set have only a single appropriate
#    size.  Others can take any value for N.  Others, alas, can take
#    SOME values of N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the number of the problem.
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  if ( problem == 1 ):
    n = p01_n ( )
  elif ( problem == 2 ):
    n = p02_n ( )
  elif ( problem == 3 ):
    n = p03_n ( )
  elif ( problem == 4 ):
    n = p04_n ( )
  elif ( problem == 5 ):
    n = p05_n ( )
  elif ( problem == 6 ):
    n = p06_n ( )
  elif ( problem == 7 ):
    n = p07_n ( )
  elif ( problem == 8 ):
    n = p08_n ( )
  elif ( problem == 9 ):
    n = p09_n ( )
  elif ( problem == 10 ):
    n = p10_n ( )
  elif ( problem == 11 ):
    n = p11_n ( )
  elif ( problem == 12 ):
    n = p12_n ( )
  elif ( problem == 13 ):
    n = p13_n ( )
  elif ( problem == 14 ):
    n = p14_n ( )
  elif ( problem == 15 ):
    n = p15_n ( )
  elif ( problem == 16 ):
    n = p16_n ( )
  elif ( problem == 17 ):
    n = p17_n ( )
  elif ( problem == 18 ):
    n = p18_n ( )
  elif ( problem == 19 ):
    n = p19_n ( )
  elif ( problem == 20 ):
    n = p20_n ( )
  elif ( problem == 21 ):
    n = p21_n ( )
  elif ( problem == 22 ):
    n = p22_n ( )
  elif ( problem == 23 ):
    n = p23_n ( )
  elif ( problem == 24 ):
    n = p24_n ( )
  elif ( problem == 25 ):
    n = p25_n ( )
  elif ( problem == 26 ):
    n = p26_n ( )
  elif ( problem == 27 ):
    n = p27_n ( )
  elif ( problem == 28 ):
    n = p28_n ( )
  elif ( problem == 29 ):
    n = p29_n ( )
  elif ( problem == 30 ):
    n = p30_n ( )
  elif ( problem == 31 ):
    n = p31_n ( )
  elif ( problem == 32 ):
    n = p32_n ( )
  elif ( problem == 33 ):
    n = p33_n ( )
  elif ( problem == 34 ):
    n = p34_n ( )
  elif ( problem == 35 ):
    n = p35_n ( )
  elif ( problem == 36 ):
    n = p43_n ( )
  elif ( problem == 37 ):
    n = p37_n ( )
  elif ( problem == 38 ):
    n = p38_n ( )
  elif ( problem == 39 ):
    n = p39_n ( )
  elif ( problem == 40 ):
    n = p40_n ( )
  elif ( problem == 41 ):
    n = p41_n ( )
  elif ( problem == 42 ):
    n = p42_n ( )
  elif ( problem == 43 ):
    n = p43_n ( )
  else:
    print ( '' )
    print ( 'p00_n(): Fatal error!' )
    print ( '  Illegal problem index = ', problem )
    raise Exception ( 'p00_n(): Fatal error!' )

  return n

def p00_n_test ( ):

#*****************************************************************************80
#
## p00_n_test() returns the problem size.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'p00_n_test():' )
  print ( '  p00_n() returns problem size or a minimum problem size.' )
#
#  Get the number of problems.
#
  problem_num = p00_problem_num ( )

  print ( '' )

  for problem in range ( 1, problem_num + 1 ):

    n = p00_n ( problem )

    title = p00_title ( problem )

    print ( '  ', problem, end = '' )
    if ( n < 0 ):
      print ( '  ' + str ( - n ) + ' (minimum)')
    else:
      print ( '  ' + str ( n ) )

  return

def p00_problem_num ( ):

#*****************************************************************************80
#
## p00_problem_num() returns the number of problems available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#   integer problem_num: the number of problems available.
#
  problem_num = 43

  return problem_num

def p00_title ( problem ):

#*****************************************************************************80
#
## p00_title() returns a title for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the number of the problem.
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  if ( problem == 1 ):
    title = p01_title ( )
  elif ( problem == 2 ):
    title = p02_title ( )
  elif ( problem == 3 ):
    title = p03_title ( )
  elif ( problem == 4 ):
    title = p04_title ( )
  elif ( problem == 5 ):
    title = p05_title ( )
  elif ( problem == 6 ):
    title = p06_title ( )
  elif ( problem == 7 ):
    title = p07_title ( )
  elif ( problem == 8 ):
    title = p08_title ( )
  elif ( problem == 9 ):
    title = p09_title ( )
  elif ( problem == 10 ):
    title = p10_title ( )
  elif ( problem == 11 ):
    title = p11_title ( )
  elif ( problem == 12 ):
    title = p12_title ( )
  elif ( problem == 13 ):
    title = p13_title ( )
  elif ( problem == 14 ):
    title = p14_title ( )
  elif ( problem == 15 ):
    title = p15_title ( )
  elif ( problem == 16 ):
    title = p16_title ( )
  elif ( problem == 17 ):
    title = p17_title ( )
  elif ( problem == 18 ):
    title = p18_title ( )
  elif ( problem == 19 ):
    title = p19_title ( )
  elif ( problem == 20 ):
    title = p20_title ( )
  elif ( problem == 21 ):
    title = p21_title ( )
  elif ( problem == 22 ):
    title = p22_title ( )
  elif ( problem == 23 ):
    title = p23_title ( )
  elif ( problem == 24 ):
    title = p24_title ( )
  elif ( problem == 25 ):
    title = p25_title ( )
  elif ( problem == 26 ):
    title = p26_title ( )
  elif ( problem == 27 ):
    title = p27_title ( )
  elif ( problem == 28 ):
    title = p28_title ( )
  elif ( problem == 29 ):
    title = p29_title ( )
  elif ( problem == 30 ):
    title = p30_title ( )
  elif ( problem == 31 ):
    title = p31_title ( )
  elif ( problem == 32 ):
    title = p32_title ( )
  elif ( problem == 33 ):
    title = p33_title ( )
  elif ( problem == 34 ):
    title = p34_title ( )
  elif ( problem == 35 ):
    title = p35_title ( )
  elif ( problem == 36 ):
    title = p43_title ( )
  elif ( problem == 37 ):
    title = p37_title ( )
  elif ( problem == 38 ):
    title = p38_title ( )
  elif ( problem == 39 ):
    title = p39_title ( )
  elif ( problem == 40 ):
    title = p40_title ( )
  elif ( problem == 41 ):
    title = p41_title ( )
  elif ( problem == 42 ):
    title = p42_title ( )
  elif ( problem == 43 ):
    title = p43_title ( )
  else:
    print ( '' )
    print ( 'p00_title(): Fatal error!' )
    print ( '  Illegal problem index = ', problem )
    raise Exception ( 'p00_title(): Fatal error!' )

  return title

def p00_title_test ( ):

#*****************************************************************************80
#
## p00_title_test() prints the title of each problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'p00_title_test():' )
  print ( '  p00_title() prints the title for any problem.' )
#
#  Get the number of problems.
#
  problem_num = p00_problem_num ( )

  print ( '' )
  print ( '  Problem	 Title' )
  print ( '' )

  for problem in range ( 1, problem_num + 1 ):

    title = p00_title ( problem )

    print ( '  ' + str ( problem ) + '  ' + '"' + title + '"' )

  return

def gradient_method_test ( ):

#*****************************************************************************80
#
## gradient_method_test() carries out a simple gradient method.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
  max_step = 5
  reduce_max = 10

  print ( '' )
  print ( 'gradient_method_test():' )
  print ( '  For each problem, take a few steps of the gradient method.' )
#
#  Get the number of problems.
#
  problem_num = p00_problem_num ( )

  for problem in range ( 1, problem_num + 1 ):

    title = p00_title ( problem )

    n = p00_n ( problem )

    n_min = n

    if ( n < 0 ):
      n_min = np.abs ( n_min )
      n = max ( n_min, 4 )
#
#  Start the gradient method.
#
    print ( '' )
    print ( '  Problem ', problem )
    print ( '  ' + title )
    print ( '  N = ', n )

    x = p00_start ( problem, n )

    f = p00_f ( problem, n, x )
    print ( '  Starting F(X) = ', f )

    terminate = 0
    s = 0.5

    for i in range ( 0, max_step ):
#
#  Be a little more daring than previous step.
#
      s = 2.0 * s
      reduce = 0

      g = p00_g ( problem, n, x )

      if ( np.all ( g == 0.0 ) ):
        print ( '  Terminate because of zero gradient.' )
        break

      x2 = np.zeros ( n )

      while ( True ):

        x2 = x - s * g
 
        f2 = p00_f ( problem, n, x2 )

        if ( f2 < f ):
          break

        reduce = reduce + 1
        print ( '  Reject step, F = %g, S = %g' % ( f2, s ) )

        if ( reduce_max < reduce ):
          print ( '' )
          print ( '  Repeated step reductions do not help.' )
          print ( '  Problem abandoned.' )
          terminate = 1
          break

        s = s / 4.0

      if ( terminate ):
        break

      x = x2.copy ( )
      f = f2

      f = p00_f ( problem, n, x )
      print ( '  New F(X) = %g, S = %g' % ( f, s ) )

  return

def p01_n ( ):

#*****************************************************************************80
#
## p01_n() returns the number of variables for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 3

  return n

def p02_n ( ):

#*****************************************************************************80
#
## p02_n() returns the number of variables for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 6

  return n

def p03_n ( ):

#*****************************************************************************80
#
## p03_n() returns the number of variables for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 3

  return n

def p04_n ( ):

#*****************************************************************************80
#
## p04_n() returns the number of variables for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p05_n ( ):

#*****************************************************************************80
#
## p05_n() returns the number of variables for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 3

  return n

def p06_n ( ):

#*****************************************************************************80
#
## p06_n() returns the number of variables for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = - 1

  return n

def p07_n ( ):

#*****************************************************************************80
#
## p07_n() returns the number of variables for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = - 2

  return n

def p08_n ( ):

#*****************************************************************************80
#
## p08_n() returns the number of variables for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = - 1

  return n

def p09_n ( ):

#*****************************************************************************80
#
## p09_n() returns the number of variables for problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = - 1

  return n

def p10_n ( ):

#*****************************************************************************80
#
## p10_n() returns the number of variables for problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p11_n ( ):

#*****************************************************************************80
#
## p11_n() returns the number of variables for problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 4

  return n

def p12_n ( ):

#*****************************************************************************80
#
## p12_n() returns the number of variables for problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 3

  return n

def p13_n ( ):

#*****************************************************************************80
#
## p13_n() returns the number of variables for problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = - 1

  return n

def p14_n ( ):

#*****************************************************************************80
#
## p14_n() returns the number of variables for problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = - 1

  return n

def p15_n ( ):

#*****************************************************************************80
#
## p15_n() returns the number of variables for problem 15.
#
#  Discussion:
#
#    The number of variables may be any multiple of 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = - 4

  return n

def p16_n ( ):

#*****************************************************************************80
#
## p16_n() returns the number of variables for problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p17_n ( ):

#*****************************************************************************80
#
## p17_n() returns the number of variables for problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 4

  return n

def p18_n ( ):

#*****************************************************************************80
#
## p18_n() returns the number of variables for problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = - 1

  return n

def p19_n ( ):

#*****************************************************************************80
#
## p19_n() returns the number of variables for problem 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p20_n ( ):

#*****************************************************************************80
#
## p20_n() returns the number of variables for problem 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = - 1

  return n

def p21_n ( ):

#*****************************************************************************80
#
## p21_n() returns the number of variables for problem 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = - 1

  return n

def p22_n ( ):

#*****************************************************************************80
#
## p22_n() returns the number of variables for problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 3

  return n

def p23_n ( ):

#*****************************************************************************80
#
## p23_n() returns the number of variables for problem 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p24_n ( ):

#*****************************************************************************80
#
## p24_n() returns the number of variables for problem 24.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 5

  return n

def p25_n ( ):

#*****************************************************************************80
#
## p25_n() returns the number of variables for problem 25.
#
#  Discussion:
#
#    The function is actually well defined for any positive value of N.
#    The value given here is that specified in the reference.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 30

  return n

def p26_n ( ):

#*****************************************************************************80
#
## p26_n() returns the number of variables for problem 26.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p27_n ( ):

#*****************************************************************************80
#
## p27_n() returns the number of variables for problem 27.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p28_n ( ):

#*****************************************************************************80
#
## p28_n() returns the number of variables for problem 28.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p29_n ( ):

#*****************************************************************************80
#
## p29_n() returns the number of variables for problem 29.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p30_n ( ):

#*****************************************************************************80
#
## p30_n() returns the number of variables for problem 30.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p31_n ( ):

#*****************************************************************************80
#
## p31_n() returns the number of variables for problem 31.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 4

  return n

def p32_n ( ):

#*****************************************************************************80
#
## p32_n() returns the number of variables for problem 32.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 4

  return n

def p33_n ( ):

#*****************************************************************************80
#
## p33_n() returns the number of variables for problem 33.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 4

  return n

def p34_n ( ):

#*****************************************************************************80
#
## p34_n() returns the number of variables for problem 34.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p35_n ( ):

#*****************************************************************************80
#
## p35_n() returns the number of variables for problem 35.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p37_n ( ):

#*****************************************************************************80
#
## p37_n() returns the number of variables for problem 37.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p38_n ( ):

#*****************************************************************************80
#
## p38_n() returns the number of variables for problem 38.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p39_n ( ):

#*****************************************************************************80
#
## p39_n() returns the number of variables for problem 39.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p40_n ( ):

#*****************************************************************************80
#
## p40_n() returns the number of variables for problem 40.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p41_n ( ):

#*****************************************************************************80
#
## p41_n() returns the number of variables for problem 41.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 4

  return n

def p42_n ( ):

#*****************************************************************************80
#
## p42_n() returns the number of variables for problem 42.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 3

  return n

def p43_n ( ):

#*****************************************************************************80
#
## p43_n() returns the number of variables for problem 43.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer N.  If N is positive, N represents the
#    only legal value for N for this problem.  If N is
#    negative, the absolute value of N is the least legal
#    value of N, but other values are allowable.
#
  n = 2

  return n

def p01_title ( ):

#*****************************************************************************80
#
## p01_title() returns a title for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Fletcher-Powell helical valley function.'

  return title

def p02_title ( ):

#*****************************************************************************80
#
## p02_title() returns a title for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Biggs EXP6 function.'

  return title

def p03_title ( ):

#*****************************************************************************80
#
## p03_title() returns a title for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Gaussian function.'

  return title

def p04_title ( ):

#*****************************************************************************80
#
## p04_title() returns a title for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Powell badly scaled function.'

  return title

def p05_title ( ):

#*****************************************************************************80
#
## p05_title() returns a title for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Box 3-dimensional function.'

  return title

def p06_title ( ):

#*****************************************************************************80
#
## p06_title() returns a title for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The variably dimensioned function.'

  return title

def p07_title ( ):

#*****************************************************************************80
#
## p07_title() returns a title for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Watson function.'

  return title

def p08_title ( ):

#*****************************************************************************80
#
## p08_title() returns a title for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Penalty Function #1.'

  return title

def p09_title ( ):

#*****************************************************************************80
#
## p09_title() returns a title for problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Penalty Function #2.'

  return title

def p10_title ( ):

#*****************************************************************************80
#
## p10_title() returns a title for problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Brown Badly Scaled Function.'

  return title

def p11_title ( ):

#*****************************************************************************80
#
## p11_title() returns a title for problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Brown and Dennis Function.'

  return title

def p12_title ( ):

#*****************************************************************************80
#
## p12_title() returns a title for problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Gulf R&D Function.'

  return title

def p13_title ( ):

#*****************************************************************************80
#
## p13_title() returns a title for problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Trigonometric Function.'

  return title

def p14_title ( ):

#*****************************************************************************80
#
## p14_title() returns a title for problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Extended Rosenbrock parabolic valley Function.'

  return title

def p15_title ( ):

#*****************************************************************************80
#
## p15_title() returns a title for problem 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Extended Powell Singular Quartic Function.'

  return title

def p16_title ( ):

#*****************************************************************************80
#
## p16_title() returns a title for problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Beale Function.'

  return title

def p17_title ( ):

#*****************************************************************************80
#
## p17_title() returns a title for problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Wood Function.'

  return title

def p18_title ( ):

#*****************************************************************************80
#
## p18_title() returns a title for problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Chebyquad Function'

  return title

def p19_title ( ):

#*****************************************************************************80
#
## p19_title() returns a title for problem 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Leon cubic valley function'

  return title

def p20_title ( ):

#*****************************************************************************80
#
## p20_title() returns a title for problem 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Gregory and Karney Tridiagonal Matrix Function'

  return title

def p21_title ( ):

#*****************************************************************************80
#
## p21_title() returns a title for problem 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Hilbert Matrix Function F = x\'Ax'

  return title

def p22_title ( ):

#*****************************************************************************80
#
## p22_title() returns a title for problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The De Jong Function F1'

  return title

def p23_title ( ):

#*****************************************************************************80
#
## p23_title() returns a title for problem 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The De Jong Function F2'

  return title

def p24_title ( ):

#*****************************************************************************80
#
## p24_title() returns a title for problem 24.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The De Jong Function F3, (discontinuous)'

  return title

def p25_title ( ):

#*****************************************************************************80
#
## p25_title() returns a title for problem 25.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The De Jong Function F4 (with Gaussian noise)'

  return title

def p26_title ( ):

#*****************************************************************************80
#
## p26_title() returns a title for problem 26.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The De Jong Function F5'

  return title

def p27_title ( ):

#*****************************************************************************80
#
## p27_title() returns a title for problem 27.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Schaffer Function F6'

  return title

def p28_title ( ):

#*****************************************************************************80
#
## p28_title() returns a title for problem 28.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Schaffer Function F7'

  return title

def p29_title ( ):

#*****************************************************************************80
#
## p29_title() returns a title for problem 29.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Goldstein Price Polynomial'

  return title

def p30_title ( ):

#*****************************************************************************80
#
## p30_title() returns a title for problem 30.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Branin RCOS Function'

  return title

def p31_title ( ):

#*****************************************************************************80
#
## p31_title() returns a title for problem 31.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Shekel SQRN5 Function'

  return title

def p32_title ( ):

#*****************************************************************************80
#
## p32_title() returns a title for problem 32.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Shekel SQRN7 Function'

  return title

def p33_title ( ):

#*****************************************************************************80
#
## p33_title() returns a title for problem 33.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Shekel SQRN10 Function'

  return title

def p34_title ( ):

#*****************************************************************************80
#
## p34_title() returns a title for problem 34.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Six-Hump Camel-Back Polynomial'

  return title

def p35_title ( ):

#*****************************************************************************80
#
## p35_title() returns a title for problem 35.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Shubert Function'

  return title

def p37_title ( ):

#*****************************************************************************80
#
## p37_title() returns a title for problem 37.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Easom Function'

  return title

def p38_title ( ):

#*****************************************************************************80
#
## p38_title() returns a title for problem 38.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Bohachevsky Function #1'

  return title

def p39_title ( ):

#*****************************************************************************80
#
## p39_title() returns a title for problem 39.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Bohachevsky Function #2'

  return title

def p40_title ( ):

#*****************************************************************************80
#
## p40_title() returns a title for problem 40.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Bohachevsky Function #3'

  return title

def p41_title ( ):

#*****************************************************************************80
#
## p41_title() returns a title for problem 41.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Colville Polynomial'

  return title

def p42_title ( ):

#*****************************************************************************80
#
## p42_title() returns a title for problem 42.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Powell 3D Function'

  return title

def p43_title ( ):

#*****************************************************************************80
#
## p43_title() returns a title for problem 43.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, a title for the problem.
#
  title = 'The Himmelblau function.'

  return title

def p00_start ( problem, n ):

#*****************************************************************************80
#
## p00_start() returns a starting point for optimization for any problem.
#
#  Discussion:
#
#    The point returned by this routine does not produce an optimal
#    value of the objective function.  Instead, it is "reasonably far"
#    from an optimizing point, so that an optimization program has
#    a proper workout.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the number of the problem.
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  if ( problem == 1 ):
    x = p01_start ( n )
  elif ( problem == 2 ):
    x = p02_start ( n )
  elif ( problem == 3 ):
    x = p03_start ( n )
  elif ( problem == 4 ):
    x = p04_start ( n )
  elif ( problem == 5 ):
    x = p05_start ( n )
  elif ( problem == 6 ):
    x = p06_start ( n )
  elif ( problem == 7 ):
    x = p07_start ( n )
  elif ( problem == 8 ):
    x = p08_start ( n )
  elif ( problem == 9 ):
    x = p09_start ( n )
  elif ( problem == 10 ):
    x = p10_start ( n )
  elif ( problem == 11 ):
    x = p11_start ( n )
  elif ( problem == 12 ):
    x = p12_start ( n )
  elif ( problem == 13 ):
    x = p13_start ( n )
  elif ( problem == 14 ):
    x = p14_start ( n )
  elif ( problem == 15 ):
    x = p15_start ( n )
  elif ( problem == 16 ):
    x = p16_start ( n )
  elif ( problem == 17 ):
    x = p17_start ( n )
  elif ( problem == 18 ):
    x = p18_start ( n )
  elif ( problem == 19 ):
    x = p19_start ( n )
  elif ( problem == 20 ):
    x = p20_start ( n )
  elif ( problem == 21 ):
    x = p21_start ( n )
  elif ( problem == 22 ):
    x = p22_start ( n )
  elif ( problem == 23 ):
    x = p23_start ( n )
  elif ( problem == 24 ):
    x = p24_start ( n )
  elif ( problem == 25 ):
    x = p25_start ( n )
  elif ( problem == 26 ):
    x = p26_start ( n )
  elif ( problem == 27 ):
    x = p27_start ( n )
  elif ( problem == 28 ):
    x = p28_start ( n )
  elif ( problem == 29 ):
    x = p29_start ( n )
  elif ( problem == 30 ):
    x = p30_start ( n )
  elif ( problem == 31 ):
    x = p31_start ( n )
  elif ( problem == 32 ):
    x = p32_start ( n )
  elif ( problem == 33 ):
    x = p33_start ( n )
  elif ( problem == 34 ):
    x = p34_start ( n )
  elif ( problem == 35 ):
    x = p35_start ( n )
  elif ( problem == 36 ):
    x = p43_start ( n )
  elif ( problem == 37 ):
    x = p37_start ( n )
  elif ( problem == 38 ):
    x = p38_start ( n )
  elif ( problem == 39 ):
    x = p39_start ( n )
  elif ( problem == 40 ):
    x = p40_start ( n )
  elif ( problem == 41 ):
    x = p41_start ( n )
  elif ( problem == 42 ):
    x = p42_start ( n )
  elif ( problem == 43 ):
    x = p43_start ( n )
  else:
    print ( '' )
    print ( 'p00_start(): Fatal error!' )
    print ( '  Illegal problem index = ', problem )
    raise Exception ( 'p00_start(): Fatal error!' )

  return x

def p00_start_test ( ):

#*****************************************************************************80
#
## p00_start_test() prints a suggested starting point for the minimization.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'p00_start_test():' )
  print ( '  p00_start() provides a starting point for minimization.' )
#
#  Get the number of problems.
#
  problem_num = p00_problem_num ( )

  for problem in range ( 1, problem_num + 1 ):

    title = p00_title ( problem )

    print ( '' )
    print ( '  %d: "%s"' % ( problem, title ) )
#
#  Get or choose the problem size.
#
    n = p00_n ( problem )
    if ( n < 0 ):
      n = max ( abs ( n ), 4 )
 
    x = p00_start ( problem, n )

    pprint.pprint ( x )

  return

def p01_start ( n ):

#*****************************************************************************80
#
## p01_start() returns a starting point for optimization for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ -1.0, 0.0, 0.0 ] )

  return x

def p02_start ( n ):

#*****************************************************************************80
#
## p02_start() returns a starting point for optimization for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 1.0, 2.0, 1.0, 1.0, 1.0, 1.0 ] )

  return x

def p03_start ( n ):

#*****************************************************************************80
#
## p03_start() returns a starting point for optimization for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 0.4, 1.0, 0.0 ] )

  return x

def p04_start ( n ):

#*****************************************************************************80
#
## p04_start() returns a starting point for optimization for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 0.0, 1.0 ] )

  return x

def p05_start ( n ):

#*****************************************************************************80
#
## p05_start() returns a starting point for optimization for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 0.0, 10.0, 5.0 ] )

  return x

def p06_start ( n ):

#*****************************************************************************80
#
## p06_start() returns a starting point for optimization for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = ( n - i - 1 ) / n

  return x

def p07_start ( n ):

#*****************************************************************************80
#
## p07_start() returns a starting point for optimization for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.zeros ( n )

  return x

def p08_start ( n ):

#*****************************************************************************80
#
## p08_start() returns a starting point for optimization for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.linspace ( 1, n, n )

  return x

def p09_start ( n ):

#*****************************************************************************80
#
## p09_start() returns a starting point for optimization for problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = 0.5 * np.ones ( n )

  return x

def p10_start ( n ):

#*****************************************************************************80
#
## p10_start() returns a starting point for optimization for problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 1.0, 1.0 ] )

  return x

def p11_start ( n ):

#*****************************************************************************80
#
## p11_start() returns a starting point for optimization for problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 25.0, 5.0, -5.0, -1.0 ] )

  return x

def p12_start ( n ):

#*****************************************************************************80
#
## p12_start() returns a starting point for optimization for problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 40.0, 20.0, 1.20 ] )

  return x

def p13_start ( n ):

#*****************************************************************************80
#
## p13_start() returns a starting point for optimization for problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.ones ( n ) / n

  return x

def p14_start ( n ):

#*****************************************************************************80
#
## p14_start() returns a starting point for optimization for problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    if ( ( i % 2 ) == 0 ):
      x[i] = - 1.2
    else:
      x[i] = 1.0

  return x

def p15_start ( n ):

#*****************************************************************************80
#
## p15_start() returns a starting point for optimization for problem 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):

    if ( ( i % 4 ) == 0 ):
      x[i] = 3.0
    elif ( ( i % 4 ) == 1 ):
      x[i] = - 1.0
    elif ( ( i % 4 ) == 2 ):
      x[i] = 0.0
    else:
      x[i] = 1.0

  return x

def p16_start ( n ):

#*****************************************************************************80
#
## p16_start() returns a starting point for optimization for problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 1.0, 1.0 ] )

  return x

def p17_start ( n ):

#*****************************************************************************80
#
## p17_start() returns a starting point for optimization for problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ -3.0, -1.0, -3.0, -1.0 ] )

  return x

def p18_start ( n ):

#*****************************************************************************80
#
## p18_start() returns a starting point for optimization for problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = ( i + 1 ) / ( n + 1 )

  return x

def p19_start ( n ):

#*****************************************************************************80
#
## p19_start() returns a starting point for optimization for problem 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ -1.2, -1.0 ] )

  return x

def p20_start ( n ):

#*****************************************************************************80
#
## p20_start() returns a starting point for optimization for problem 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.zeros ( n )

  return x

def p21_start ( n ):

#*****************************************************************************80
#
## p21_start() returns a starting point for optimization for problem 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.ones ( n )

  return x

def p22_start ( n ):

#*****************************************************************************80
#
## p22_start() returns a starting point for optimization for problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.linspace ( - 5.12, + 5.12, n )

  return x

def p23_start ( n ):

#*****************************************************************************80
#
## p23_start() returns a starting point for optimization for problem 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.linspace ( - 2.048, + 2.048, n )

  return x

def p24_start ( n ):

#*****************************************************************************80
#
## p24_start() returns a starting point for optimization for problem 24.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.linspace ( -5.12, +5.12, n )

  return x

def p25_start ( n ):

#*****************************************************************************80
#
## p25_start() returns a starting point for optimization for problem 25.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.linspace ( -1.28, +1.28, n )

  return x

def p26_start ( n ):

#*****************************************************************************80
#
## p26_start() returns a starting point for optimization for problem 26.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ -32.01, -32.02 ] )

  return x

def p27_start ( n ):

#*****************************************************************************80
#
## p27_start() returns a starting point for optimization for problem 27.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ -5.0, +10.0 ] )

  return x

def p28_start ( n ):

#*****************************************************************************80
#
## p28_start() returns a starting point for optimization for problem 28.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ -5.0, +10.0 ] )

  return x

def p29_start ( n ):

#*****************************************************************************80
#
## p29_start() returns a starting point for optimization for problem 29.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ -0.5, +0.25 ] )

  return x

def p30_start ( n ):

#*****************************************************************************80
#
## p30_start() returns a starting point for optimization for problem 30.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ -1.0, 1.0 ] )

  return x

def p31_start ( n ):

#*****************************************************************************80
#
## p31_start() returns a starting point for optimization for problem 31.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 1.0, 3.0, 5.0, 6.0 ] )

  return x

def p32_start ( n ):

#*****************************************************************************80
#
## p32_start() returns a starting point for optimization for problem 32.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 1.0, 3.0, 5.0, 6.0 ] )

  return x

def p33_start ( n ):

#*****************************************************************************80
#
## p33_start() returns a starting point for optimization for problem 33.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 1.0, 3.0, 5.0, 6.0 ] )

  return x

def p34_start ( n ):

#*****************************************************************************80
#
## p34_start() returns a starting point for optimization for problem 34.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ -1.5, 0.5 ] )

  return x

def p35_start ( n ):

#*****************************************************************************80
#
## p35_start() returns a starting point for optimization for problem 35.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 0.5, 1.0 ] )

  return x

def p37_start ( n ):

#*****************************************************************************80
#
## p37_start() returns a starting point for optimization for problem 37.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 0.5, 1.0 ] )

  return x

def p38_start ( n ):

#*****************************************************************************80
#
## p38_start() returns a starting point for optimization for problem 38.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 0.5, 1.0 ] )

  return x

def p39_start ( n ):

#*****************************************************************************80
#
## p39_start() returns a starting point for optimization for problem 39.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 0.6, 1.3 ] )

  return x

def p40_start ( n ):

#*****************************************************************************80
#
## p40_start() returns a starting point for optimization for problem 40.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 0.5, 1.0 ] )

  return x

def p41_start ( n ):

#*****************************************************************************80
#
## p41_start() returns a starting point for optimization for problem 41.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 0.5, 1.0, -0.5, -1.0 ] )

  return x

def p42_start ( n ):

#*****************************************************************************80
#
## p42_start() returns a starting point for optimization for problem 42.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ 0.0, 1.0, 2.0 ] )

  return x

def p43_start ( n ):

#*****************************************************************************80
#
## p43_start() returns a starting point for optimization for problem 43.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables X.
#
#  Output:
#
#    real X(N), a starting point for the optimization.
#
  import numpy as np

  x = np.array ( [ -1.3, 2.7 ] )

  return x

def p00_f ( problem, n, x ):

#*****************************************************************************80
#
## p00_f() evaluates the objective function for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Evelyn Beale,
#    On an Iterative Method for Finding a Local Minimum of a Function
#    of More than One Variable,
#    Technical Report 25,
#    Statistical Techniques Research Group,
#    Princeton University, 1958.
#
#    Richard Brent,
#    Algorithms for Minimization with Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#    John Dennis, David Gay, Phuong Vu,
#    A new nonlinear equations test problem,
#    Technical Report 83-16,
#    Mathematical Sciences Department,
#    Rice University (1983 - revised 1985).
#
#    John Dennis, Robert Schnabel,
#    Numerical Methods for Unconstrained Optimization
#    and Nonlinear Equations,
#    SIAM, 1996,
#    ISBN13: 978-0-898713-64-0,
#    LC: QA402.5.D44.
#
#    Noel deVilliers, David Glasser,
#    A continuation method for nonlinear regression,
#    SIAM Journal on Numerical Analysis,
#    Volume 18, 1981, pages 1139-1154.
#
#    Chris Fraley,
#    Solution of nonlinear least-squares problems,
#    Technical Report STAN-CS-1165,
#    Computer Science Department,
#    Stanford University, 1987.
#
#    Chris Fraley,
#    Software performance on nonlinear least-squares problems,
#    Technical Report SOL 88-17,
#    Systems Optimization Laboratory,
#    Department of Operations Research,
#    Stanford University, 1988.
#
#    A Leon,
#    A Comparison of Eight Known Optimizing Procedures,
#    in Recent Advances in Optimization Techniques,
#    edited by Abraham Lavi, Thomas Vogl,
#    Wiley, 1966.
#
#    JJ McKeown,
#    Specialized versus general-purpose algorithms for functions that are sums
#    of squared terms,
#    Mathematical Programming,
#    Volume 9, 1975a, pages 57-68.
#
#    JJ McKeown,
#    On algorithms for sums of squares problems,
#    in Towards Global Optimization,
#    L. C. W. Dixon and G. Szego (eds.),
#    North-Holland, 1975, pages 229-257.
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#    Jorge More, Burton Garbow, Kenneth Hillstrom,
#    Algorithm 566 - Testing unconstrained optimization software,
#    ACM Transactions on Mathematical Software,
#    Volume 7, 1981, pages 17-41.
#
#    Michael Powell,
#    An Efficient Method for Finding the Minimum of a Function of
#    Several Variables Without Calculating Derivatives,
#    Computer Journal,
#    Volume 7, Number 2, pages 155-162, 1964.
#
#    DE Salane,
#    A continuation approach for solving large residual nonlinear least squares
#    problems,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 8, 1987, pages 655-671.
#
#  Input:
#
#    integer PROBLEM, the problem number.
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  if ( problem == 1 ):
    f = p01_f ( n, x )
  elif ( problem == 2 ):
    f = p02_f ( n, x )
  elif ( problem == 3 ):
    f = p03_f ( n, x )
  elif ( problem == 4 ):
    f = p04_f ( n, x )
  elif ( problem == 5 ):
    f = p05_f ( n, x )
  elif ( problem == 6 ):
    f = p06_f ( n, x )
  elif ( problem == 7 ):
    f = p07_f ( n, x )
  elif ( problem == 8 ):
    f = p08_f ( n, x )
  elif ( problem == 9 ):
    f = p09_f ( n, x )
  elif ( problem == 10 ):
    f = p10_f ( n, x )
  elif ( problem == 11 ):
    f = p11_f ( n, x )
  elif ( problem == 12 ):
    f = p12_f ( n, x )
  elif ( problem == 13 ):
    f = p13_f ( n, x )
  elif ( problem == 14 ):
    f = p14_f ( n, x )
  elif ( problem == 15 ):
    f = p15_f ( n, x )
  elif ( problem == 16 ):
    f = p16_f ( n, x )
  elif ( problem == 17 ):
    f = p17_f ( n, x )
  elif ( problem == 18 ):
    f = p18_f ( n, x )
  elif ( problem == 19 ):
    f = p19_f ( n, x )
  elif ( problem == 20 ):
    f = p20_f ( n, x )
  elif ( problem == 21 ):
    f = p21_f ( n, x )
  elif ( problem == 22 ):
    f = p22_f ( n, x )
  elif ( problem == 23 ):
    f = p23_f ( n, x )
  elif ( problem == 24 ):
    f = p24_f ( n, x )
  elif ( problem == 25 ):
    f = p25_f ( n, x )
  elif ( problem == 26 ):
    f = p26_f ( n, x )
  elif ( problem == 27 ):
    f = p27_f ( n, x )
  elif ( problem == 28 ):
    f = p28_f ( n, x )
  elif ( problem == 29 ):
    f = p29_f ( n, x )
  elif ( problem == 30 ):
    f = p30_f ( n, x )
  elif ( problem == 31 ):
    f = p31_f ( n, x )
  elif ( problem == 32 ):
    f = p32_f ( n, x )
  elif ( problem == 33 ):
    f = p33_f ( n, x )
  elif ( problem == 34 ):
    f = p34_f ( n, x )
  elif ( problem == 35 ):
    f = p35_f ( n, x )
  elif ( problem == 36 ):
    f = p43_f ( n, x )
  elif ( problem == 37 ):
    f = p37_f ( n, x )
  elif ( problem == 38 ):
    f = p38_f ( n, x )
  elif ( problem == 39 ):
    f = p39_f ( n, x )
  elif ( problem == 40 ):
    f = p40_f ( n, x )
  elif ( problem == 41 ):
    f = p41_f ( n, x )
  elif ( problem == 42 ):
    f = p42_f ( n, x )
  elif ( problem == 43 ):
    f = p43_f ( n, x )
  else:
    print ( '' )
    print ( 'p00_f(): Fatal error!' )
    print ( '  Illegal problem index = ', problem )
    raise Exception ( 'p00_f(): Fatal error!' )

  return f

def p00_f_test ( ):

#*****************************************************************************80
#
## p00_f_test() evaluates the objective function at each starting point.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'p00_f_test():' )
  print ( '  p00_f() evaluates the objective function F(X).' )
  print ( '  In this test, we evaluate F at a typical starting point.' )
#
#  Get the number of problems.
#
  problem_num = p00_problem_num ( )

  for problem in range ( 1, problem_num + 1 ):

    title = p00_title ( problem )

    print ( '' )
    print ( '  %d: "%s"' % ( problem, title ) )
#
#  Get or choose the problem size.
#
    n = p00_n ( problem )
    if ( n < 0 ):
      n = max ( abs ( n ), 4 )

    if ( problem == 7 ):
      n = 6
#
#  Get the starting point and objective function value.
#
    x = p00_start ( problem, n )

    f_start = p00_f ( problem, n, x )

    print ( '  f(x_start) = ', f_start )

  return

def p01_f ( n, x ):

#*****************************************************************************80
#
## p01_f() evaluates the objective function for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization with Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  th = p01_th ( x )

  f = 100.0 * ( x[2] - 10.0 * th )**2 \
    + 100.0 * ( np.sqrt ( x[0] * x[0] + x[1] * x[1] ) - 1.0 )**2 \
    + x[2] * x[2]

  return f

def p01_th ( x ):

#*****************************************************************************80
#
## p01_th() evaluates a term used by problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x[*], the values of the variables.
#
#  Output:
#
#    real TH, the value of the term.
#
  import numpy as np

  if ( 0.0 < x[0] ):
    th = 0.5 * np.arctan ( x[1] / x[0] ) / np.pi
  elif ( x[0] < 0.0 ):
    th = 0.5 * np.arctan ( x[1] / x[0] ) / np.pi + 0.5
  elif ( 0.0 < x[1] ):
    th = 0.25
  elif ( x[1] < 0.0 ):
    th = - 0.25
  else:
    th = 0.0

  return th

def p02_f ( n, x ):

#*****************************************************************************80
#
## p02_f() evaluates the objective function for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  f = 0.0

  for i in range ( 1, 14 ):

    c = - i / 10.0

    fi = x[2] * np.exp ( c * x[0] ) \
       - x[3] * np.exp ( c * x[1] ) \
       + x[5] * np.exp ( c * x[4] ) \
       -        np.exp ( c )        \
       + 5.0  * np.exp ( 10.0 * c ) \
       - 3.0  * np.exp ( 4.0 * c )

    f = f + fi * fi

  return f

def p03_f ( n, x ):

#*****************************************************************************80
#
## p03_f() evaluates the objective function for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  y = p03_yvec ( )

  f = 0.0

  for i in range ( 0, 15 ):

    t = x[0] * np.exp ( - 0.5 * x[1] * \
      ( 3.5 - 0.5 * ( i - 1 ) - x[2] )**2 ) - y[i]

    f = f + t * t

  return f

def p03_yvec ( ):

#*****************************************************************************80
#
## p03_yvec() is an auxilliary routine for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real Y(15), data values needed for the
#    objective function.
#
  import numpy as np

  y = np.array ( [ \
        0.0009, 0.0044, 0.0175, 0.0540, 0.1295, \
        0.2420, 0.3521, 0.3989, 0.3521, 0.2420, \
        0.1295, 0.0540, 0.0175, 0.0044, 0.0009 ] )

  return y

def p04_f ( n, x ):

#*****************************************************************************80
#
## p04_f() evaluates the objective function for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization with Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  f1 = 10000.0 * x[0] * x[1] - 1.0
  f2 = np.exp ( - x[0] ) + np.exp ( - x[1] ) - 1.0001

  f = f1 * f1 + f2 * f2

  return f

def p05_f ( n, x ):

#*****************************************************************************80
#
## p05_f() evaluates the objective function for problem 5.
#
#  Discussion:
#
#    The function is formed by the sum of squares of 10 separate terms.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  f = 0.0

  for i in range ( 0, 10 ):

    c = - ( i + 1 ) / 10.0

    fi = \
                 np.exp ( c * x[0] ) \
      -          np.exp ( c * x[1] ) \
      - x[2] * ( np.exp ( c ) - np.exp ( 10.0 * c ) )

    f = f + fi * fi

  return f

def p06_f ( n, x ):

#*****************************************************************************80
#
## p06_f() evaluates the objective function for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization with Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  f1 = 0.0
  for i in range ( 0, n ):
    f1 = f1 + ( i + 1 ) * ( x[i] - 1.0 )

  f2 = 0.0
  for i in range ( 0, n ):
    f2 = f2 + ( x[i] - 1.0 )**2

  f = f1 * f1 * ( 1.0 + f1 * f1 ) + f2

  return f

def p07_f ( n, x ):

#*****************************************************************************80
#
## p07_f() evaluates the objective function for problem 7.
#
#  Discussion:
#
#    For N = 9, the problem of minimizing the Watson function is
#    very ill conditioned.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization with Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  f = 0.0

  for i in range ( 0, 29 ):

    s1 = 0.0
    d = 1.0
    for j in range ( 1, n ):
      s1 = s1 + j * d * x[j]
      d = d * ( i + 1 ) / 29.0

    s2 = 0.0
    d = 1.0
    for j in range ( 0, n ):
      s2 = s2 + d * x[j]
      d = d * ( i + 1 ) / 29.0
 
    f = f + ( s1 - s2 * s2 - 1.0 )**2

  f = f + x[0] * x[0] + ( x[1] - x[0] * x[0] - 1.0 )**2

  return f

def p08_f ( n, x ):

#*****************************************************************************80
#
## p08_f() evaluates the objective function for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  ap = 0.00001

  t1 = - 0.25 + np.sum ( x**2 )

  t2 = np.sum ( ( x - 1.0 )**2 )

  f = ap * t2 + t1 * t1

  return f

def p09_f ( n, x ):

#*****************************************************************************80
#
## p09_f() evaluates the objective function for problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  ap = 0.00001

  t1 = -1.0
  t2 = 0.0
  t3 = 0.0
  d2 = 1.0
  s2 = 0.0

  for j in range ( 0, n ):
    t1 = t1 + ( n - j ) * x[j]**2
    s1 = np.exp ( x[j] / 10.0 )
    if ( 0 < j ):
      s3 = s1 + s2 - d2 * ( np.exp ( 0.1 ) + 1.0 )
      t2 = t2 + s3 * s3
      t3 = t3 + ( s1 - 1.0 / np.exp ( 0.1 ) )**2
    s2 = s1
    d2 = d2 * np.exp ( 0.1 )

  f = ap * ( t2 + t3 ) + t1 * t1 + ( x[0] - 0.2 )**2

  return f

def p10_f ( n, x ):

#*****************************************************************************80
#
## p10_f() evaluates the objective function for problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  f = ( x[0] - 1000000.0 )**2 \
    + ( x[1] - 0.000002 )**2 \
    + ( x[0] * x[1] - 2.0 )**2

  return f

def p11_f ( n, x ):

#*****************************************************************************80
#
## p11_f() evaluates the objective function for problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  f = 0.0

  for i in range ( 1, 21 ):

    c = i / 5.0
    f1 = x[0] + c * x[1] - np.exp ( c )
    f2 = x[2] + np.sin ( c ) * x[3] - np.cos ( c )

    f = f + f1**4 + 2.0 * f1 * f1 * f2 * f2 + f2**4

  return f

def p12_f ( n, x ):

#*****************************************************************************80
#
## p12_f() evaluates the objective function for problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  f = 0.0
  for i in range ( 1, 100 ):
    arg = i / 100.0
    r = abs ( ( - 50.0 * np.log ( arg ) )**( 2.0 / 3.0 ) + 25.0 - x[1] )

    t = np.exp ( - r**x[2] / x[0] ) - arg

    f = f + t * t

  return f

def p13_f ( n, x ):

#*****************************************************************************80
#
## p13_f() evaluates the objective function for problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  s1 = np.sum ( np.cos ( x ) )

  f = 0.0
  for j in range ( 0, n ):
    t =  ( n + j + 1 ) - np.sin ( x[j] ) - s1 - ( j + 1 ) * np.cos ( x[j] )
    f = f + t * t

  return f

def p14_f ( n, x ):

#*****************************************************************************80
#
## p14_f() evaluates the objective function for problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization with Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  f = 0.0
  for j in range ( 0, n ):
    if ( ( j % 2 ) == 0 ):
      f = f + ( 1.0 - x[j] )**2
    else:
      f = f + 100.0 * ( x[j] - x[j-1] * x[j-1] )**2

  return f

def p15_f ( n, x ):

#*****************************************************************************80
#
## p15_f() evaluates the objective function for problem 15.
#
#  Discussion:
#
#    The Hessian matrix is doubly singular at the minimizer,
#    suggesting that most optimization routines will experience
#    a severe slowdown in convergence.
#
#    The problem is usually only defined for N being a multiple of 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization with Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  f = 0.0

  for j in range ( 1, n + 1, 4 ):

    if ( j + 1 <= n ):
      xjp1 = x[j]
    else:
      xjp1 = 0.0

    if ( j + 2 <= n ):
      xjp2 = x[j+1]
    else:
      xjp2 = 0.0

    if ( j + 3 <= n ):
      xjp3 = x[j+2]
    else:
      xjp3 = 0.0

    f1 = x[j-1] + 10.0 * xjp1

    if ( j + 1 <= n ):
      f2 = xjp2 - xjp3
    else:
      f2 = 0.0

    if ( j + 2 <= n ):
      f3 = xjp1 - 2.0 * xjp2
    else:
      f3 = 0.0

    if ( j + 3 <= n ):
      f4 = x[j-1] - xjp3
    else:
      f4 = 0.0

    f = f +        f1 * f1 \
          +  5.0 * f2 * f2 \
          +        f3 * f3 * f3 * f3 \
          + 10.0 * f4 * f4 * f4 * f4

  return f

def p16_f ( n, x ):

#*****************************************************************************80
#
## p16_f() evaluates the objective function for problem 16.
#
#  Discussion:
#
#    This function has a valley approaching the line x[1] = 1.
#
#    The function has a global minimizer:
#
#      X(*) = ( 3.0, 0.5 ), F(X*) = 0.0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Evelyn Beale,
#    On an Iterative Method for Finding a Local Minimum of a Function
#    of More than One Variable,
#    Technical Report 25,
#    Statistical Techniques Research Group,
#    Princeton University, 1958.
#
#    Richard Brent,
#    Algorithms for Minimization with Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  f1 = 1.5   - x[0] * ( 1.0 - x[1]    )
  f2 = 2.25  - x[0] * ( 1.0 - x[1] * x[1] )
  f3 = 2.625 - x[0] * ( 1.0 - x[1] * x[1] * x[1] )

  f = f1 * f1 + f2 * f2 + f3 * f3

  return f

def p17_f ( n, x ):

#*****************************************************************************80
#
## p17_f() evaluates the objective function for problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization with Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  f1 = x[1] - x[0] * x[0]
  f2 = 1.0 - x[0]
  f3 = x[3] - x[2] * x[2]
  f4 = 1.0 - x[2]
  f5 = x[1] + x[3] - 2.0
  f6 = x[1] - x[3]

  f = 100.0 * f1 * f1 \
    +         f2 * f2 \
    +  90.0 * f3 * f3 \
    +         f4 * f4 \
    +  10.0 * f5 * f5 \
    +   0.1 * f6 * f6

  return f

def p18_f ( n, x ):

#*****************************************************************************80
#
## p18_f() evaluates the objective function for problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization with Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np
#
#  Compute FVEC.
#
  fvec = p18_fvec ( n, x )
#
#  Compute F.
#
  f = np.sum ( fvec**2 )

  return f

def p18_fvec ( n, x ):

#*****************************************************************************80
#
## p18_fvec() is an auxilliary routine for problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real FVEC(N), an auxilliary vector.
#
  import numpy as np

  fvec = np.zeros ( n )

  for j in range ( 0, n ):
    t1 = 1.0
    t2 = 2.0 * x[j] - 1.0
    t = 2.0 * t2
    for i in range ( 0, n ):
      fvec[i] = fvec[i] + t2
      th = t * t2 - t1
      t1 = t2
      t2 = th

  for i in range ( 0, n ):
    fvec[i] = fvec[i] / n
    if ( ( i % 2 ) == 1 ):
      fvec[i] = fvec[i] + 1.0 / ( ( i + 1 )**2 - 1.0 )

  return fvec

def p19_f ( n, x ):

#*****************************************************************************80
#
## p19_f() evaluates the objective function for problem 19.
#
#  Discussion:
#
#    The function is similar to Rosenbrock's.  The "valley" follows
#    the curve x[1] = x[0]**3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization with Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#    A Leon,
#    A Comparison of Eight Known Optimizing Procedures,
#    in Recent Advances in Optimization Techniques,
#    edited by Abraham Lavi, Thomas Vogl,
#    Wiley, 1966.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  f1 = x[1] - x[0] * x[0] * x[0]
  f2 = 1.0 - x[0]

  f = 100.0 * f1 * f1 + f2 * f2

  return f

def p20_f ( n, x ):

#*****************************************************************************80
#
## p20_f() evaluates the objective function for problem 20.
#
#  Discussion:
#
#    The function has the form
#      f = x'*A*x - 2*x(1)
#    where A is the (-1,2,-1) tridiagonal matrix, except that A(1,1) is 1.
#    The minimum value of F(X) is -N, which occurs for
#      x = ( n, n-1, \, 2, 1 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization with Derivatives,
#    Prentice Hall, 1973,
#    Reprinted by Dover, 2002.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  f = x[0] * x[0] + 2.0 * np.sum ( x[1:n]**2 )

  for i in range ( 0, n - 1 ):
    f = f - 2.0 * x[i] * x[i+1]

  f = f - 2.0 * x[0]

  return f

def p21_f ( n, x ):

#*****************************************************************************80
#
## p21_f() evaluates the objective function for problem 21.
#
#  Discussion:
#
#    The function has the form
#      f = x'*A*x
#    where A is the Hilbert matrix.  The minimum value
#    of F(X) is 0, which occurs for
#      x = ( 0, 0, \, 0 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization with Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  f = 0.0

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      f = f + x[i] * x[j] / ( i + j + 1 )

  return f

def p22_f ( n, x ):

#*****************************************************************************80
#
## p22_f() evaluates the objective function for problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  f = np.sum ( x**2 )

  return f

def p23_f ( n, x ):

#*****************************************************************************80
#
## p23_f() evaluates the objective function for problem 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  f = 100.0 * ( x[0] * x[0] - x[1] )**2 + ( 1.0 - x[0] )**2

  return f

def p24_f ( n, x ):

#*****************************************************************************80
#
## p24_f() evaluates the objective function for problem 24.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  f = ( np.sum ( np.floor ( x ) ) )

  return f

def p25_f ( n, x, p = 0.0 ):

#*****************************************************************************80
#
## p25_f() evaluates the objective function for problem 25.
#
#  Discussion:
#
#    The function includes Gaussian noise, multiplied by a parameter P.
#
#    If P is zero, then the function is a proper function, and evaluating
#    it twice with the same argument will yield the same results.
#    Moreover, P25_g and P25_h are the correct gradient and hessian routines.
#
#    If P is nonzero, then evaluating the function at the same argument
#    twice will generally yield two distinct values this means the function
#    is not even a well defined mathematical function, let alone continuous
#    the gradient and hessian are not correct.  And yet, at least for small
#    values of P, it may be possible to approximate the minimizer of the
#    (underlying well-defined ) function.
#
#    The value of the parameter P is by default 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  from numpy.random import default_rng
  import numpy as np

  f = 0.0

  if ( p != 0.0 ):
    rng = default_rng ( )
    gauss = rng.standard_normal ( )
    f = f + p * gauss

  for i in range ( 0, n ):
    f = f + ( i + 1 ) * x[i]**4

  return f

def p26_f ( n, x ):

#*****************************************************************************80
#
## p26_f() evaluates the objective function for problem 26.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  jroot = 5
  k = 500.0

  fi = k

  for j in range ( 0, jroot * jroot ):

    j1 = ( j % jroot ) + 1
    a1 = - 32 + j1 * 16

    j2 = j / jroot
    a2 = - 32 + j2 * 16

    fj = ( j + 1 ) + ( x[0] - a1 )**6 + ( x[1] - a2 )**6

    fi = fi + 1.0 / fj

  f = 1.0 / fi

  return f

def p27_f ( n, x ):

#*****************************************************************************80
#
## p27_f() evaluates the objective function for problem 27.
#
#  Discussion:
#
#    F can be regarded as a function of R = SQRT ( x[0]*x[0] + x[1]*x[1] ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  r = np.sqrt ( x[0]**2 + x[1]**2 )

  a = 1.0 / ( 1.0 + 0.001 * r**2 )**2

  b = ( np.sin ( r ) )**2 - 0.5

  f = 0.5 + a * b

  return f

def p28_f ( n, x ):

#*****************************************************************************80
#
## p28_f() evaluates the objective function for problem 28.
#
#  Discussion:
#
#    Note that F is a function of R**2 = x[0]*x[0] + x[1]*x[1]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  r = np.sqrt ( x[0]**2 + x[1]**2 )

  f = np.sqrt ( r ) * ( 1.0 + ( np.sin ( 50.0 * r**0.2 ) )**2 )

  return f

def p29_f ( n, x ):

#*****************************************************************************80
#
## p29_f() evaluates the objective function for problem 29.
#
#  Discussion:
#
#    Note that F is a polynomial in X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  a = x[0] + x[1] + 1.0

  b = 19.0 - 14.0 * x[0] + 3.0 * x[0] * x[0] - 14.0 * x[1] \
    + 6.0 * x[0] * x[1] + 3.0 * x[1] * x[1]

  c = 2.0 * x[0] - 3.0 * x[1]

  d = 18.0 - 32.0 * x[0] + 12.0 * x[0] * x[0] + 48.0 * x[1] \
    - 36.0 * x[0] * x[1] + 27.0 * x[1] * x[1]

  f = ( 1.0 + a * a * b ) * ( 30.0 + c * c * d )

  return f

def p30_f ( n, x ):

#*****************************************************************************80
#
## p30_f() evaluates the objective function for problem 30.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  a = 1.0
  d = 6.0
  e = 10.0

  b = 5.1 / ( 4.0 * np.pi**2 )
  c = 5.0 / np.pi
  ff = 1.0 / ( 8.0 * np.pi )

  f = a * ( x[1] - b * x[0]**2 + c * x[0] - d )**2 \
    + e * ( 1.0 - ff ) * np.cos ( x[0] ) + e

  return f

def p31_f ( n, x ):

#*****************************************************************************80
#
## p31_f() evaluates the objective function for problem 31.
#
#  Discussion:
#
#    The minimal function value is -10.15320.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  m = 5
  A = np.array ( [ \
       [ 4.0, 4.0, 4.0, 4.0 ], \
       [ 1.0, 1.0, 1.0, 1.0 ], \
       [ 8.0, 8.0, 8.0, 8.0 ], \
       [ 6.0, 6.0, 6.0, 6.0 ], \
       [ 3.0, 7.0, 3.0, 7.0 ] ] )

  c = np.array ( [ 0.1, 0.2, 0.2, 0.4, 0.6 ] )

  f = 0.0
  for j in range ( 0, m ):
    f = f - 1.0 / ( c[j] + np.sum ( ( x - A[j,:] )**2 ) )

  return f

def p32_f ( n, x ):

#*****************************************************************************80
#
## p32_f() evaluates the objective function for problem 32.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  m = 7
  A = np.array ( [ \
   [ 4.0, 4.0, 4.0, 4.0 ], \
   [ 1.0, 1.0, 1.0, 1.0 ], \
   [ 8.0, 8.0, 8.0, 8.0 ], \
   [ 6.0, 6.0, 6.0, 6.0 ], \
   [ 3.0, 7.0, 3.0, 7.0 ], \
   [ 2.0, 9.0, 2.0, 9.0 ], \
   [ 5.0, 5.0, 3.0, 3.0 ] ] )

  c = np.array ( [ 0.1, 0.2, 0.2, 0.4, 0.6, 0.6, 0.3 ] )

  f = 0.0
  for j in range ( 0, m ):
    f = f - 1.0 / ( c[j] + np.sum ( ( x - A[j,:] )**2 ) )

  return f

def p33_f ( n, x ):

#*****************************************************************************80
#
## p33_f() evaluates the objective function for problem 33.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  m = 10
  A = np.array ( [ \
      [ 4.0, 4.0, 4.0, 4.0 ], \
      [ 1.0, 1.0, 1.0, 1.0 ], \
      [ 8.0, 8.0, 8.0, 8.0 ], \
      [ 6.0, 6.0, 6.0, 6.0 ], \
      [ 3.0, 7.0, 3.0, 7.0 ], \
      [ 2.0, 9.0, 2.0, 9.0 ], \
      [ 5.0, 5.0, 3.0, 3.0 ], \
      [ 8.0, 1.0, 8.0, 1.0 ], \
      [ 6.0, 2.0, 6.0, 2.0 ], \
      [ 7.0, 3.6, 7.0, 3.6 ] ] )

  c = np.array ( [ 0.1, 0.2, 0.2, 0.4, 0.6, 0.6, 0.3, 0.7, 0.5, 0.5 ] )

  f = 0.0
  for j in range ( 0, m ):
    f = f - 1.0 / ( c[j] + np.sum ( ( x - A[j,:] )**2 ) )

  return f

def p34_f ( n, x ):

#*****************************************************************************80
#
## p34_f() evaluates the objective function for problem 34.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  f = ( 4.0 - 2.1 * x[0]**2 + x[0]**4 / 3.0 ) * x[0]**2 \
    + x[0] * x[1] + 4.0 * ( x[1]**2 - 1.0 ) * x[1]**2

  return f

def p35_f ( n, x ):

#*****************************************************************************80
#
## p35_f() evaluates the objective function for problem 35.
#
#  Discussion:
#
#    For -10 <= X(I) <= 10, the function has 760 local minima, 18 of which
#    are global minima, with minimum value -186.73.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  factor1 = 0.0
  for i in range ( 1, 6 ):
    factor1 = factor1 + i * np.cos ( ( i + 1.0 ) * x[0] + i )

  factor2 = 0.0
  for i in range ( 1, 6 ):
    factor2 = factor2 + i * np.cos ( ( i + 1.0 ) * x[1] + i )

  f = factor1 * factor2

  return f

def p37_f ( n, x ):

#*****************************************************************************80
#
## p37_f() evaluates the objective function for problem 37.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  arg = - ( x[0] - np.pi )**2 - ( x[1] - np.pi )**2
  f = - np.cos ( x[0] ) * np.cos ( x[1] ) * np.exp ( arg )

  return f

def p38_f ( n, x ):

#*****************************************************************************80
#
## p38_f() evaluates the objective function for problem 38.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np
  f = x[0] * x[0] - 0.3 * np.cos ( 3.0 * np.pi * x[0] ) \
    + 2.0 * x[1] * x[1] - 0.4 * np.cos ( 4.0 * np.pi * x[1] ) \
    + 0.7

  return f

def p39_f ( n, x ):

#*****************************************************************************80
#
## p39_f() evaluates the objective function for problem 39.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  f = x[0] * x[0] + 2.0 * x[1] * x[1] \
    - 0.3 * np.cos ( 3.0 * np.pi * x[0] ) \
    * np.cos ( 4.0 * np.pi * x[1] ) + 0.3

  return f

def p40_f ( n, x ):

#*****************************************************************************80
#
## p40_f() evaluates the objective function for problem 40.
#
#  Discussion:
#
#    There is a typo in the reference.  I'm just guessing at the correction.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  f = x[0]**2 + 2.0 * x[1]**2 \
    - 0.3 * np.cos ( 3.0 * np.pi * x[0] ) \
    + np.cos ( 4.0 * np.pi * x[1] ) + 0.3

  return f

def p41_f ( n, x ):

#*****************************************************************************80
#
## p41_f() evaluates the objective function for problem 41.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Zbigniew Michalewicz,
#    Genetic Algorithms + Data Structures = Evolution Programs,
#    Third Edition,
#    Springer Verlag, 1996,
#    ISBN: 3-540-60676-9,
#    LC: QA76.618.M53.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  f = 100.0 * ( x[1] - x[0]**2 )**2 \
    + ( 1.0 - x[0] )**2 \
    + 90.0 * ( x[3] - x[2]**2 )**2 \
    + ( 1.0 - x[2] )**2 \
    + 10.1 * ( ( x[1] - 1.0 )**2 + ( x[3] - 1.0 )**2 ) \
    + 19.8 * ( x[1] - 1.0 ) * ( x[3] - 1.0 )

  return f

def p42_f ( n, x ):

#*****************************************************************************80
#
## p42_f() evaluates the objective function for problem 42.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    MJD Powell,
#    An Efficient Method for Finding the Minimum of a Function of
#    Several Variables Without Calculating Derivatives,
#    Computer Journal,
#    Volume 7, Number 2, pages 155-162, 1964.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  import numpy as np

  if ( x[1] == 0.0 ):
    term = 0.0
  else:
    arg = ( x[0] + 2.0 * x[1] + x[2] ) / x[1]
    term = np.exp ( - arg**2 )

  f = 3.0 \
    - 1.0 / ( 1.0 + ( x[0] - x[1] )**2 ) \
    - np.sin ( 0.5 * np.pi * x[1] * x[2] ) \
    - term

  return f

def p43_f ( n, x ):

#*****************************************************************************80
#
## p43_f() evaluates the objective function for problem 43.
#
#  Discussion:
#
#    This function has 4 global minima:
#
#      X* = (  3,        2       ), F(X*) = 0.
#      X* = (  3.58439, -1.84813 ), F(X*) = 0.
#      X* = ( -3.77934, -3.28317 ), F(X*) = 0.
#      X* = ( -2.80512,  3.13134 ), F(X*) = 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Himmelblau,
#    Applied Nonlinear Programming,
#    McGraw Hill, 1972,
#    ISBN13: 978-0070289215,
#   LC: T57.8.H55.
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the argument of the objective function.
#
#  Output:
#
#    real F, the value of the objective function.
#
  f = ( x[0]**2 + x[1] - 11.0 )**2 + ( x[0] + x[1]**2 - 7.0 )**2

  return f

def p00_sol ( problem, n ):

#*****************************************************************************80
#
## p00_sol() returns the solution for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem number.
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  if ( problem == 1 ):
    know, x = p01_sol ( n )
  elif ( problem == 2 ):
    know, x = p02_sol ( n )
  elif ( problem == 3 ):
    know, x = p03_sol ( n )
  elif ( problem == 4 ):
    know, x = p04_sol ( n )
  elif ( problem == 5 ):
    know, x = p05_sol ( n )
  elif ( problem == 6 ):
    know, x = p06_sol ( n )
  elif ( problem == 7 ):
    know, x = p07_sol ( n )
  elif ( problem == 8 ):
    know, x = p08_sol ( n )
  elif ( problem == 9 ):
    know, x = p09_sol ( n )
  elif ( problem == 10 ):
    know, x = p10_sol ( n )
  elif ( problem == 11 ):
    know, x = p11_sol ( n )
  elif ( problem == 12 ):
    know, x = p12_sol ( n )
  elif ( problem == 13 ):
    know, x = p13_sol ( n )
  elif ( problem == 14 ):
    know, x = p14_sol ( n )
  elif ( problem == 15 ):
    know, x = p15_sol ( n )
  elif ( problem == 16 ):
    know, x = p16_sol ( n )
  elif ( problem == 17 ):
    know, x = p17_sol ( n )
  elif ( problem == 18 ):
    know, x = p18_sol ( n )
  elif ( problem == 19 ):
    know, x = p19_sol ( n )
  elif ( problem == 20 ):
    know, x = p20_sol ( n )
  elif ( problem == 21 ):
    know, x = p21_sol ( n )
  elif ( problem == 22 ):
    know, x = p22_sol ( n )
  elif ( problem == 23 ):
    know, x = p23_sol ( n )
  elif ( problem == 24 ):
    know, x = p24_sol ( n )
  elif ( problem == 25 ):
    know, x = p25_sol ( n )
  elif ( problem == 26 ):
    know, x = p26_sol ( n )
  elif ( problem == 27 ):
    know, x = p27_sol ( n )
  elif ( problem == 28 ):
    know, x = p28_sol ( n )
  elif ( problem == 29 ):
    know, x = p29_sol ( n )
  elif ( problem == 30 ):
    know, x = p30_sol ( n )
  elif ( problem == 31 ):
    know, x = p31_sol ( n )
  elif ( problem == 32 ):
    know, x = p32_sol ( n )
  elif ( problem == 33 ):
    know, x = p33_sol ( n )
  elif ( problem == 34 ):
    know, x = p34_sol ( n )
  elif ( problem == 35 ):
    know, x = p35_sol ( n )
  elif ( problem == 36 ):
    know, x = p43_sol ( n )
  elif ( problem == 37 ):
    know, x = p37_sol ( n )
  elif ( problem == 38 ):
    know, x = p38_sol ( n )
  elif ( problem == 39 ):
    know, x = p39_sol ( n )
  elif ( problem == 40 ):
    know, x = p40_sol ( n )
  elif ( problem == 41 ):
    know, x = p41_sol ( n )
  elif ( problem == 42 ):
    know, x = p42_sol ( n )
  elif ( problem == 43 ):
    know, x = p43_sol ( n )
  else:
    print ( '' )
    print ( 'p00_sol(): Fatal error!' )
    print ( '  Illegal problem index = ', problem )
    raise Exception ( 'p00_sol(): Fatal error!' )

  return know, x

def p00_sol_test ( ):

#*****************************************************************************80
#
## p00_sol_test() evaluates the objective function at a minimizing solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'p00_sol_test():' )
  print ( '  p00_sol() returns a minimizing solution.' )
  print ( '  Print the value of f(x) there.' )
#
#  Get the number of problems.
#
  problem_num = p00_problem_num ( )

  for problem in range ( 1, problem_num + 1 ):

    title = p00_title ( problem )

    print ( '' )
    print ( '  %d: "%s"' % ( problem, title ) )
#
#  Get or choose the problem size.
#
    n = p00_n ( problem )
    if ( n < 0 ):
      n = max ( abs ( n ), 4 )

    if ( problem == 7 ):
      n = 6
#
#  Evaluate f() at starting point and at minimizer.
#
    x = p00_start ( problem, n )
    f_start = p00_f ( problem, n, x )
    print ( '  f(x_start) = ', f_start )

    know, x = p00_sol ( problem, n )
    if ( 0 < know ):
      f_sol = p00_f ( problem, n, x )
      print ( '  f(x_sol)   = ', f_sol )
      g_sol = p00_g ( problem, n, x )
      print ( '  ||f\'(x_sol)||  ', np.linalg.norm ( g_sol ) )
    else:
      print ( '  x_sol not given.' )

  return

def p01_sol ( n ):

#*****************************************************************************80
#
## p01_sol() returns the solution for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ 1.0, 0.0, 0.0 ] )

  return know, x

def p02_sol ( n ):

#*****************************************************************************80
#
## p02_sol() returns the solution for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ 1.0, 10.0, 1.0, 5.0, 4.0, 3.0 ] )

  return know, x

def p03_sol ( n ):

#*****************************************************************************80
#
## p03_sol() returns the solution for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 0

  x = np.zeros ( n )

  return know, x

def p04_sol ( n ):

#*****************************************************************************80
#
## p04_sol() returns the solution for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ 1.098159E-05, 9.106146 ] )

  return know, x

def p05_sol ( n ):

#*****************************************************************************80
#
## p05_sol() returns the solution for problem 5.
#
#  Discussion:
#
#    The function has a minimum of 0 at (1,10,1) and also for
#    any point of the form (x,x,0).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ 1.0, 10.0, 1.0 ] )

  return know, x

def p06_sol ( n ):

#*****************************************************************************80
#
## p06_sol() returns the solution for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.ones ( n )

  return know, x

def p07_sol ( n ):

#*****************************************************************************80
#
## p07_sol() returns the solution for problem 7.
#
#  Discussion:
#
#    The values of the approximate solutions are taken from Brent.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  if ( n == 6 ):
    know = 1
    x = np.array ( [ -0.015725, 1.012435, -0.232992, 1.260430, -1.513729, 0.992996 ] )
  elif ( n == 9 ):
    know = 1
    x = np.array ( [ -0.000015, 0.999790, 0.014764, 0.146342, \
      1.000821, -2.617731, 4.104403, -3.143612, 1.052627 ] )
  else:
    know = 0
    x = np.zeros ( n )

  return know, x

def p08_sol ( n ):

#*****************************************************************************80
#
## p08_sol() returns the solution for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 0

  x = np.zeros ( n )

  return know, x

def p09_sol ( n ):

#*****************************************************************************80
#
## p09_sol() returns the solution for problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 0

  x = np.zeros ( n )

  return know, x

def p10_sol ( n ):

#*****************************************************************************80
#
## p10_sol() returns the solution for problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ 1.0E+06, 2.0E-06 ] )

  return know, x

def p11_sol ( n ):

#*****************************************************************************80
#
## p11_sol() returns the solution for problem 11.
#
#  Discussion:
#
#    A local minimizer is approximately known.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ -11.5844, 13.1999, -0.406200, 0.240998 ] )

  return know, x

def p12_sol ( n ):

#*****************************************************************************80
#
## p12_sol() returns the solution for problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ 50.0, 25.0, 1.5 ] )

  return know, x

def p13_sol ( n ):

#*****************************************************************************80
#
## p13_sol() returns the solution for problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 0

  x = np.zeros ( n )

  return know, x

def p14_sol ( n ):

#*****************************************************************************80
#
## p14_sol() returns the solution for problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.ones ( n )

  return know, x

def p15_sol ( n ):

#*****************************************************************************80
#
## p15_sol() returns the solution for problem 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.zeros ( n )

  return know, x

def p16_sol ( n ):

#*****************************************************************************80
#
## p16_sol() returns the solution for problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ 3.0, 0.5 ] )

  return know, x

def p17_sol ( n ):

#*****************************************************************************80
#
## p17_sol() returns the solution for problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ 1.0, 1.0, 1.0, 1.0 ] )

  return know, x

def p18_sol ( n ):

#*****************************************************************************80
#
## p18_sol() returns the solution for problem 18.
#
#  Discussion:
#
#    The solution values are taken from Brent.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  if ( n == 2 ):
    know = 1
    x = np.array ( [ 0.2113249, 0.7886751 ] )
  elif ( n == 4 ):
    know = 1
    x = np.array ( [ 0.1026728, 0.4062037, 0.5937963, 0.8973272 ] )
  elif ( n == 6 ):
    know = 1
    x = np.array ( [ 0.066877, 0.288741, 0.366682, 0.633318, \
      0.711259, 0.933123 ] )
  elif ( n == 8 ):
    know = 1
    x = np.array ( [ 0.043153, 0.193091, 0.266329, 0.500000, \
      0.500000, 0.733671, 0.806910, 0.956847 ] )
  else:
    know = 0
    x = np.zeros ( n )

  return know, x

def p19_sol ( n ):

#*****************************************************************************80
#
## p19_sol() returns the solution for problem 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ 1.0, 1.0 ] )

  return know, x

def p20_sol ( n ):

#*****************************************************************************80
#
## p20_sol() returns the solution for problem 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = n - i

  return know, x

def p21_sol ( n ):

#*****************************************************************************80
#
## p21_sol() returns the solution for problem 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.zeros ( n )

  return know, x

def p22_sol ( n ):

#*****************************************************************************80
#
## p22_sol() returns the solution for problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.zeros ( n )

  return know, x

def p23_sol ( n ):

#*****************************************************************************80
#
## p23_sol() returns the solution for problem 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.ones ( n )

  return know, x

def p24_sol ( n ):

#*****************************************************************************80
#
## p24_sol() returns the solution for problem 24.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = - 5.0 * np.ones ( n )

  return know, x

def p25_sol ( n ):

#*****************************************************************************80
#
## p25_sol() returns the solution for problem 25.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.zeros ( n )

  return know, x

def p26_sol ( n ):

#*****************************************************************************80
#
## p26_sol() returns the solution for problem 26.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ -32.0, -32.0 ] )

  return know, x

def p27_sol ( n ):

#*****************************************************************************80
#
## p27_sol() returns the solution for problem 27.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.zeros ( n )

  return know, x

def p28_sol ( n ):

#*****************************************************************************80
#
## p28_sol() returns the solution for problem 28.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.zeros ( n )

  return know, x

def p29_sol ( n ):

#*****************************************************************************80
#
## p29_sol() returns the solution for problem 29.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ 0.0, -1.0 ] )

  return know, x

def p30_sol ( n ):

#*****************************************************************************80
#
## p30_sol() returns the solution for problem 30.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  know = 3

  r = rng.integers ( 1, 4 )

  if ( r == 1 ):
    x = np.array ( [ - np.pi, 12.275 ] )
  elif ( r == 2 ):
    x = np.array ( [   np.pi,  2.275 ] )
  else:
    x = np.array ( [ 9.42478, 2.475 ] )

  return know, x

def p31_sol ( n ):

#*****************************************************************************80
#
## p31_sol() returns the solution for problem 31.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = 4.0 * np.ones ( n )

  return know, x

def p32_sol ( n ):

#*****************************************************************************80
#
## p32_sol() returns the solution for problem 32.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = 4.0 * np.ones ( n )

  return know, x

def p33_sol ( n ):

#*****************************************************************************80
#
## p33_sol() returns the solution for problem 33.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = 4.0 * np.ones ( n )

  return know, x

def p34_sol ( n ):

#*****************************************************************************80
#
## p34_sol() returns the solution for problem 34.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  know = 2

  r = rng.integers ( 1, 3 )

  if ( r == 1 ):
    x = np.array ( [ -0.0898,  0.7126 ] )
  else:
    x = np.array ( [  0.0898, -0.7126 ] )

  return know, x

def p35_sol ( n ):

#*****************************************************************************80
#
## p35_sol() returns the solution for problem 35.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ -7.7, -7.1 ] )

  return know, x

def p37_sol ( n ):

#*****************************************************************************80
#
## p37_sol() returns the solution for problem 37.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.pi * np.ones ( n )

  return know, x

def p38_sol ( n ):

#*****************************************************************************80
#
## p38_sol() returns the solution for problem 38.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.zeros ( n )

  return know, x

def p39_sol ( n ):

#*****************************************************************************80
#
## p39_sol() returns the solution for problem 39.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.zeros ( n )

  return know, x

def p40_sol ( n ):

#*****************************************************************************80
#
## p40_sol() returns the solution for problem 40.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.zeros ( n )

  return know, x

def p41_sol ( n ):

#*****************************************************************************80
#
## p41_sol() returns the solution for problem 41.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.ones ( n )

  return know, x

def p42_sol ( n ):

#*****************************************************************************80
#
## p42_sol() returns the solution for problem 42.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.ones ( n )

  return know, x

def p43_sol ( n ):

#*****************************************************************************80
#
## p43_sol() returns the solution for problem 43.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the problem.  This value
#    is only needed for those problems with variable N.
#
#  Output:
#
#    integer KNOW.
#    If KNOW is 0, then the solution is not known.
#    If KNOW is positive, then the solution is known, and is returned in X.
#
#    real X(N), the solution, if known.
#
  import numpy as np

  know = 1

  x = np.array ( [ 3.0, 2.0 ] )

  return know, x

def p00_g ( problem, n, x ):

#*****************************************************************************80
#
## p00_g() evaluates the gradient for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem number.
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  if ( problem == 1 ):
    g = p01_g ( n, x )
  elif ( problem == 2 ):
    g = p02_g ( n, x )
  elif ( problem == 3 ):
    g = p03_g ( n, x )
  elif ( problem == 4 ):
    g = p04_g ( n, x )
  elif ( problem == 5 ):
    g = p05_g ( n, x )
  elif ( problem == 6 ):
    g = p06_g ( n, x )
  elif ( problem == 7 ):
    g = p07_g ( n, x )
  elif ( problem == 8 ):
    g = p08_g ( n, x )
  elif ( problem == 9 ):
    g = p09_g ( n, x )
  elif ( problem == 10 ):
    g = p10_g ( n, x )
  elif ( problem == 11 ):
    g = p11_g ( n, x )
  elif ( problem == 12 ):
    g = p12_g ( n, x )
  elif ( problem == 13 ):
    g = p13_g ( n, x )
  elif ( problem == 14 ):
    g = p14_g ( n, x )
  elif ( problem == 15 ):
    g = p15_g ( n, x )
  elif ( problem == 16 ):
    g = p16_g ( n, x )
  elif ( problem == 17 ):
    g = p17_g ( n, x )
  elif ( problem == 18 ):
    g = p18_g ( n, x )
  elif ( problem == 19 ):
    g = p19_g ( n, x )
  elif ( problem == 20 ):
    g = p20_g ( n, x )
  elif ( problem == 21 ):
    g = p21_g ( n, x )
  elif ( problem == 22 ):
    g = p22_g ( n, x )
  elif ( problem == 23 ):
    g = p23_g ( n, x )
  elif ( problem == 24 ):
    g = p24_g ( n, x )
  elif ( problem == 25 ):
    g = p25_g ( n, x )
  elif ( problem == 26 ):
    g = p26_g ( n, x )
  elif ( problem == 27 ):
    g = p27_g ( n, x )
  elif ( problem == 28 ):
    g = p28_g ( n, x )
  elif ( problem == 29 ):
    g = p29_g ( n, x )
  elif ( problem == 30 ):
    g = p30_g ( n, x )
  elif ( problem == 31 ):
    g = p31_g ( n, x )
  elif ( problem == 32 ):
    g = p32_g ( n, x )
  elif ( problem == 33 ):
    g = p33_g ( n, x )
  elif ( problem == 34 ):
    g = p34_g ( n, x )
  elif ( problem == 35 ):
    g = p35_g ( n, x )
  elif ( problem == 36 ):
    g = p43_g ( n, x )
  elif ( problem == 37 ):
    g = p37_g ( n, x )
  elif ( problem == 38 ):
    g = p38_g ( n, x )
  elif ( problem == 39 ):
    g = p39_g ( n, x )
  elif ( problem == 40 ):
    g = p40_g ( n, x )
  elif ( problem == 41 ):
    g = p41_g ( n, x )
  elif ( problem == 42 ):
    g = p42_g ( n, x )
  elif ( problem == 43 ):
    g = p43_g ( n, x )
  else:
    print ( '' )
    print ( 'p00_g(): Fatal error!' )
    print ( '  Illegal problem index = ', problem )
    raise Exception ( 'p00_g(): Fatal error!' )

  return g

def p01_g ( n, x ):

#*****************************************************************************80
#
## p01_g() evaluates the gradient for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  th = p01_th ( x )

  r = np.sqrt ( x[0] * x[0] + x[1] * x[1] )
  t = x[2] - 10.0 * th
  s1 = 5.0 * t / ( np.pi * r * r )

  g[0] = 200.0 * ( x[0] - x[0] / r + x[1] * s1 )
  g[1] = 200.0 * ( x[1] - x[1] / r - x[0] * s1 )
  g[2] = 2.0 * ( 100.0 * t + x[2] )

  return g

def p02_g ( n, x ):

#*****************************************************************************80
#
## p02_g() evaluates the gradient for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  for i in range ( 0, 13 ):

    c = - ( i + 1 ) / 10.0

    fi =    x[2] * np.exp ( c * x[0] ) \
         -  x[3] * np.exp ( c * x[1] ) \
          + x[5] * np.exp ( c * x[4] ) \
          -        np.exp ( c ) \
          +  5.0 * np.exp ( 10.0 * c ) \
          -  3.0 * np.exp ( 4.0 * c )

    dfdx1 =     c    * x[2] * np.exp ( c * x[0] )
    dfdx2 =   - c    * x[3] * np.exp ( c * x[1] )
    dfdx3 =                   np.exp ( c * x[0] )
    dfdx4 =   -               np.exp ( c * x[1] )
    dfdx5 =     c    * x[5] * np.exp ( c * x[4] )
    dfdx6 =                   np.exp ( c * x[4] )

    g[0] = g[0] + 2.0 * fi * dfdx1
    g[1] = g[1] + 2.0 * fi * dfdx2
    g[2] = g[2] + 2.0 * fi * dfdx3
    g[3] = g[3] + 2.0 * fi * dfdx4
    g[4] = g[4] + 2.0 * fi * dfdx5
    g[5] = g[5] + 2.0 * fi * dfdx6

  return g

def p03_g ( n, x ):

#*****************************************************************************80
#
## p03_g() evaluates the gradient for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  y = p03_yvec ( )

  g = np.zeros ( n )

  for i in range ( 0, 15 ):

    d1 = 0.5 * i
    d2 = 3.5 - d1 - x[2]
    arg = - 0.5 * x[1] * d2 * d2
    t = x[0] * np.exp ( arg ) - y[i]

    g[0] = g[0] + 2.0 * np.exp ( arg ) * t
    g[1] = g[1] - x[0] * np.exp ( arg ) * t * d2 * d2
    g[2] = g[2] + 2.0 * x[0] * x[1] * np.exp ( arg ) * t * d2

  return g

def p04_g ( n, x ):

#*****************************************************************************80
#
## p04_g() evaluates the gradient for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  f1 = 10000.0 * x[0] * x[1] - 1.0
  df1dx1 = 10000.0 * x[1]
  df1dx2 = 10000.0 * x[0]

  f2 = np.exp ( - x[0] ) + np.exp ( - x[1] ) - 1.0001
  df2dx1 = - np.exp ( - x[0] )
  df2dx2 = - np.exp ( - x[1] )

  g[0] = 2.0 * f1 * df1dx1 + 2.0 * f2 * df2dx1
  g[1] = 2.0 * f1 * df1dx2 + 2.0 * f2 * df2dx2

  return g


def p05_g ( n, x ):

#*****************************************************************************80
#
## p05_g() evaluates the gradient for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  for i in range ( 0, 10 ):

    c = - ( i + 1 ) / 10.0

    fi = np.exp ( c * x[0] ) - np.exp ( c * x[1] ) \
      - x[2] * ( np.exp ( c ) - np.exp ( 10.0 * c ) )

    dfidx1 =   c * np.exp ( c * x[0] )
    dfidx2 = - c * np.exp ( c * x[1] )
    dfidx3 = - ( np.exp ( c ) - np.exp ( 10.0 * c ) )

    g[0] = g[0] + 2.0 * fi * dfidx1
    g[1] = g[1] + 2.0 * fi * dfidx2
    g[2] = g[2] + 2.0 * fi * dfidx3

  return g

def p06_g ( n, x ):

#*****************************************************************************80
#
## p06_g() evaluates the gradient for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  f1 = 0.0
  for i in range ( 0, n ):
    f1 = f1 + ( i + 1 ) * ( x[i] - 1.0 )

  for i in range ( 0, n ):
    df1dxi = i + 1
    df2dxi = 2.0 * ( x[i] - 1.0 )
    g[i] = ( 2.0 * f1 + 4.0 * f1**3 ) * df1dxi + df2dxi

  return g


def p07_g ( n, x ):

#*****************************************************************************80
#
## p07_g() evaluates the gradient for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  for i in range ( 0, 29 ):

    d1 = ( i + 1 ) / 29.0
    s1 = 0.0
    d2 = 1.0
    for j in range ( 1, n ):
      s1 = s1 + j * d2 * x[j]
      d2 = d2 * ( i + 1 ) / 29.0

    s2 = 0.0
    d2 = 1.0
    for j in range ( 0, n ):
      s2 = s2 + d2 * x[j]
      d2 = d2 * ( i + 1 ) / 29.0

    t = s1 - s2 * s2 - 1.0
    s3 = 2.0 * s2 * ( i + 1 ) / 29.0
    d2 = 2.0 / d1

    for j in range ( 0, n ):
      g[j] = g[j] + d2 * ( j - s3 ) * t
      d2 = d2 * ( i + 1 ) / 29.0

  t1 = x[1] - x[0] * x[0] - 1.0

  g[0] = g[0] + 2.0 * x[0] - 4.0 * x[0] * t1
  g[1] = g[1] + 2.0 * t1

  return g


def p08_g ( n, x ):

#*****************************************************************************80
#
## p08_g() evaluates the gradient for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  ap = 0.00001

  t1 = - 0.25 + np.sum ( x**2 )

  g = 2.0 * ap * ( x - 1.0 ) + 4.0 * x * t1

  return g


def p09_g ( n, x ):

#*****************************************************************************80
#
## p09_g() evaluates the gradient for problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  ap = 0.00001

  t1 = -1.0
  for j in range ( 0, n ):
    t1 = t1 + ( n - j ) * x[j]**2

  d2 = 1.0
  th = 4.0 * t1
  s2 = 0.0
  for j in range ( 0, n ):
    g[j] = ( n - j ) * x[j] * th
    s1 = np.exp ( x[j] / 10.0 )
    if ( 0 < j ):
      s3 = s1 + s2 - d2 * ( np.exp ( 0.1 ) + 1.0 )
      g[j] = g[j] + ap * s1 * ( s3 + s1 - 1.0 / np.exp ( 0.1 ) ) / 5.0
      g[j-1] = g[j-1] + ap * s2 * s3 / 5.0

    s2 = s1
    d2 = d2 * np.exp ( 0.1 )

  g[0] = g[0] + 2.0 * ( x[0] - 0.2 )

  return g

def p10_g ( n, x ):

#*****************************************************************************80
#
## p10_g() evaluates the gradient for problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  g[0] = 2.0 * x[0] - 2000000.0 + 2.0 * x[0] * x[1] * x[1] - 4.0 * x[1]

  g[1] = 2.0 * x[1] - 0.000004 + 2.0 * x[0]**2 * x[1] - 4.0 * x[0]

  return g

def p11_g ( n, x ):

#*****************************************************************************80
#
## p11_g() evaluates the gradient for problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  for i in range ( 0, 20 ):

    c = ( i + 1 ) / 5.0

    f1 = x[0] + c * x[1] - np.exp ( c )
    f2 = x[2] + np.sin ( c ) * x[3] - np.cos ( c )

    df1dx1 = 1.0
    df1dx2 = c
    df2dx3 = 1.0
    df2dx4 = np.sin ( c )

    g[0] = g[0] + 4.0 * ( f1**3 * df1dx1 + f1 * f2 * f2 * df1dx1 )
    g[1] = g[1] + 4.0 * ( f1**3 * df1dx2 + f1 * f2 * f2 * df1dx2 )
    g[2] = g[2] + 4.0 * ( f1 * f1 * f2 * df2dx3 + f2**3 * df2dx3 )
    g[3] = g[3] + 4.0 * ( f1 * f1 * f2 * df2dx4 + f2**3 * df2dx4 )

  return g

def p12_g ( n, x ):

#*****************************************************************************80
#
## p12_g() evaluates the gradient for problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  for i in range ( 0, 99 ):

    arg = ( i + 1 ) / 100.0
    r = abs ( ( - 50.0 * np.log ( arg ) )**( 2.0 / 3.0 ) + 25.0 - x[1] )
    t1 = r**x[2] / x[0]
    t2 = np.exp ( - t1 )

    t = np.exp ( - r**x[2] / x[0] ) - arg

    g[0] = g[0] + 2.0 * t * t1 * t2 / x[0]
    g[1] = g[1] + 2.0 * t * t1 * t2 * x[2] / r
    g[2] = g[2] - 2.0 * t * t1 * t2 * np.log ( r )

  return g

def p13_g ( n, x ):

#*****************************************************************************80
#
## p13_g() evaluates the gradient for problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  s1 = np.sum ( np.cos ( x ) )

  s2 = 0.0
  for j in range ( 0, n ):
    t =  ( n + j + 1 ) - np.sin ( x[j] ) - s1 - ( j + 1 ) * np.cos ( x[j] )
    s2 = s2 + t
    g[j] = ( ( j + 1 ) * np.sin ( x[j] ) - np.cos ( x[j] ) ) * t

  for j in range ( 0, n ):
    g[j] = 2.0 * ( g[j] + np.sin ( x[j] ) * s2 )

  return g

def p14_g ( n, x ):

#*****************************************************************************80
#
## p14_g() evaluates the gradient for problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  for j in range ( 0, n ):

    if ( ( j % 2 ) == 0 ):
      g[j] = - 2.0 * ( 1.0 - x[j] )
    else:
      g[j] = 200.0 * ( x[j] - x[j-1] * x[j-1] )
      g[j-1] = g[j-1] - 400.0 * x[j-1] * ( x[j] - x[j-1] * x[j-1] )

  return g


def p15_g ( n, x ):

#*****************************************************************************80
#
## p15_g() evaluates the gradient for problem 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  for j in range ( 1, n + 1, 4 ):

    if ( j + 1 <= n ):
      xjp1 = x[j]
    else:
      xjp1 = 0.0

    if ( j + 2 <= n ):
      xjp2 = x[j+1]
    else:
      xjp2 = 0.0

    if ( j + 3 <= n ):
      xjp3 = x[j+2]
    else:
      xjp3 = 0.0

    f1 = x[j-1] + 10.0 * xjp1
    df1dxj = 1.0
    df1dxjp1 = 10.0

    if ( j + 1 <= n ):
      f2 = xjp2 - xjp3
      df2dxjp2 = 1.0
      df2dxjp3 = -1.0
    else:
      f2 = 0.0
      df2dxjp2 = 0.0
      df2dxjp3 = 0.0
 
    if ( j + 2 <= n ):
      f3 = xjp1 - 2.0 * xjp2
      df3dxjp1 = 1.0
      df3dxjp2 = -2.0
    else:
      f3 = 0.0
      df3dxjp1 = 0.0
      df3dxjp2 = 0.0

    if ( j + 3 <= n ):
      f4 = x[j-1] - xjp3
      df4dxj = 1.0
      df4dxjp3 = -1.0
    else:
      f4 = 0.0
      df4dxj = 0.0
      df4dxjp3 = 0.0

    g[j-1] = 2.0 * f1 * df1dxj + 10.0 * 4.0 * f4**3 * df4dxj

    if ( j + 1 <= n ):
      g[j] = 2.0 * f1 * df1dxjp1 + 4.0 * f3**3 * df3dxjp1

    if ( j + 2 <= n ):
      g[j+1] = 2.0 * 5.0 * f2 * df2dxjp2 + 4.0 * f3**3 * df3dxjp2

    if ( j + 3 <= n ):
      g[j+2] = 2.0 * 5.0 * f2 * df2dxjp3 + 10.0 * 4.0 * f4**3 * df4dxjp3

  return g

def p16_g ( n, x ):

#*****************************************************************************80
#
## p16_g() evaluates the gradient for problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  f1 = 1.5   - x[0] * ( 1.0 - x[1]    )
  f2 = 2.25  - x[0] * ( 1.0 - x[1] * x[1] )
  f3 = 2.625 - x[0] * ( 1.0 - x[1] * x[1] * x[1] )

  df1dx1 = - ( 1.0 - x[1] )
  df1dx2 = x[0]
  df2dx1 = - ( 1.0 - x[1] * x[1] )
  df2dx2 = 2.0 * x[0] * x[1]
  df3dx1 = - ( 1.0 - x[1] * x[1] * x[1] )
  df3dx2 = 3.0 * x[0] * x[1] * x[1]

  g[0] = 2.0 * ( f1 * df1dx1 + f2 * df2dx1 + f3 * df3dx1 )
  g[1] = 2.0 * ( f1 * df1dx2 + f2 * df2dx2 + f3 * df3dx2 )

  return g

def p17_g ( n, x ):

#*****************************************************************************80
#
## p17_g() evaluates the gradient for problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  f1 = x[1] - x[0] * x[0]
  f2 = 1.0 - x[0]
  f3 = x[3] - x[2]**2
  f4 = 1.0 - x[2]
  f5 = x[1] + x[3] - 2.0
  f6 = x[1] - x[3]

  df1dx1 = - 2.0 * x[0]
  df1dx2 =   1.0
  df2dx1 = - 1.0
  df3dx3 = - 2.0 * x[2]
  df3dx4 =   1.0
  df4dx3 = - 1.0
  df5dx2 =   1.0
  df5dx4 =   1.0
  df6dx2 =   1.0
  df6dx4 = - 1.0

  g[0] = 2.0 * ( 100.0 * f1 * df1dx1 + f2 * df2dx1 )

  g[1] = 2.0 * ( 100.0 * f1 * df1dx2 + 10.0 * f5 * df5dx2 + 0.1 * f6 * df6dx2 )

  g[2] = 2.0 * ( 90.0 * f3 * df3dx3 + f4 * df4dx3 )

  g[3] = 2.0 * ( 90.0 * f3 * df3dx4 + 10.0 * f5 * df5dx4 + 0.1 * f6 * df6dx4 )

  return g


def p18_g ( n, x ):

#*****************************************************************************80
#
## p18_g() evaluates the gradient for problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )
#
#  Compute FVEC.
#
  fvec = p18_fvec ( n, x )
#
#  Compute G.
#
  for j in range ( 0, n ):
    g[j] = 0.0
    t1 = 1.0
    t2 = 2.0 * x[j] - 1.0
    t = 2.0 * t2
    s1 = 0.0
    s2 = 2.0
    for i in range ( 0, n ):
      g[j] = g[j] + fvec[i] * s2
      th = 4.0 * t2 + t * s2 - s1
      s1 = s2
      s2 = th
      th = t * t2 - t1
      t1 = t2
      t2 = th

  g = 2.0 * g / n

  return g


def p19_g ( n, x ):

#*****************************************************************************80
#
## p19_g() evaluates the gradient for problem 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  g[0] = - 600.0 * ( x[1] - x[0]**3 ) * x[0] * x[0] - 2.0 * ( 1.0 - x[0] )

  g[1] = 200.0 * ( x[1] - x[0]**3 )

  return g


def p20_g ( n, x ):

#*****************************************************************************80
#
## p20_g() evaluates the gradient for problem 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  for i in range ( 0, n ):

    if ( i == 0 ):
      g[i] = x[i]
    else:
      g[i] = 2.0 * x[i]

    if ( 0 < i ):
      g[i] = g[i] - x[i-1]

    if ( i < n - 1 ):
      g[i] = g[i] - x[i+1]

  g[0] = g[0] - 2.0

  return g

def p21_g ( n, x ):

#*****************************************************************************80
#
## p21_g() evaluates the gradient for problem 21.
#
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n  )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      g[i] = g[i] + 2.0 * x[j] / ( i + j + 1 )

  return g

def p22_g ( n, x ):

#*****************************************************************************80
#
## p22_g() evaluates the gradient for problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  g = 2.0 * x

  return g

def p23_g ( n, x ):

#*****************************************************************************80
#
## p23_g() evaluates the gradient for problem 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  g[0] = 400.0 * ( x[0] * x[0] - x[1] ) * x[0] - 2.0 + 2.0 * x[0]
  g[1] = - 200.0 * ( x[0] * x[0] - x[1] )

  return g

def p24_g ( n, x ):

#*****************************************************************************80
#
## p24_g() evaluates the gradient for problem 24.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  return g

def p25_g ( n, x ):

#*****************************************************************************80
#
## p25_g() evaluates the gradient for problem 25.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  for i in range ( 0, n ):
    g[i] = ( i + 1 ) * 4.0 * x[i]**3

  return g

def p26_g ( n, x ):

#*****************************************************************************80
#
## p26_g() evaluates the gradient for problem 26.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  jroot = 5
  k = 500
  fi = k
  dfidx1 = 0.0
  dfidx2 = 0.0

  for j in range ( 0, jroot * jroot ):

    j1 = ( j % jroot ) + 1
    a1 = -32 + j1 * 16

    j2 = j / jroot
    a2 = -32 + j2 * 16

    fj = ( ( j + 1 ) + ( x[0] - a1 )**6 + ( x[1] - a2 )**6 )

    fi = fi + 1.0 / fj

    dfidx1 = dfidx1 - ( 1.0 / fj**2 ) * 6.0 * ( x[0] - a1 )**5
    dfidx2 = dfidx2 - ( 1.0 / fj**2 ) * 6.0 * ( x[1] - a2 )**5

  g[0] = - ( 1.0 / fi**2 ) * dfidx1
  g[1] = - ( 1.0 / fi**2 ) * dfidx2

  return g

def p27_g ( n, x ):

#*****************************************************************************80
#
## p27_g() evaluates the gradient for problem 27.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  r = np.sqrt ( x[0]**2 + x[1]**2 )

  if ( r == 0.0 ):
    g[0] = 0.0
    g[1] = 0.0
    return g
 
  rx1 = x[0] / r
  rx2 = x[1] / r

  a =          1.0 / ( 1.0 + 0.001 * r**2 )**2
  ar = - 0.004 * r / ( 1.0 + 0.001 * r**2 )**3

  b = ( np.sin ( r ) )**2 - 0.5
  br = np.sin ( 2.0 * r )

  g[0] = ( ar * b + a * br ) * rx1
  g[1] = ( ar * b + a * br ) * rx2

  return g

def p28_g ( n, x ):

#*****************************************************************************80
#
## p28_g() evaluates the gradient for problem 28.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  r = np.sqrt ( x[0]**2 + x[1]**2 )

  if ( r == 0.0 ):
    g[0] = 0.0
    g[1] = 0.0
    return g

  a = np.sqrt ( r )
  ar = 0.5 / np.sqrt ( r )

  b = 1.0 + ( np.sin ( 50.0 * r**0.2 ) )**2
  br = 10.0 * np.sin ( 100.0 * r**0.2 ) / r**0.8

  rx1 = x[0] / r
  rx2 = x[1] / r

  g[0] = ( ar * b + a * br ) * rx1
  g[1] = ( ar * b + a * br ) * rx2

  return g

def p29_g ( n, x ):

#*****************************************************************************80
#
## p29_g() evaluates the gradient for problem 29.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  a = x[0] + x[1] + 1.0

  b = 19.0 - 14.0 * x[0] + 3.0 * x[0]**2 - 14.0 * x[1] \
    + 6.0 * x[0] * x[1] + 3.0 * x[1]**2

  dbdx1 = - 14.0 + 6.0 * x[0] + 6.0 * x[1]
  dbdx2 = - 14.0 + 6.0 * x[0] + 6.0 * x[1]

  c = 2.0 * x[0] - 3.0 * x[1]

  d = 18.0 - 32.0 * x[0] + 12.0 * x[0]**2 + 48.0 * x[1] \
    - 36.0 * x[0] * x[1] + 27.0 * x[1]**2
  dddx1 = - 32.0 + 24.0 * x[0] - 36.0 * x[1]
  dddx2 = 48.0 - 36.0 * x[0] + 54.0 * x[1]

  g[0] = ( 1.0 + a**2 * b ) * ( 4.0 * c * d + c**2 * dddx1 ) \
        + ( 2.0 * a * b + a**2 * dbdx1 ) * ( 30.0 + c**2 * d )

  g[1] = ( 1.0 + a**2 * b ) * ( -6.0 * c * d + c**2 * dddx2 ) \
        + ( 2.0 * a * b + a**2 * dbdx2 ) * ( 30.0 + c**2 * d )

  return g

def p30_g ( n, x ):

#*****************************************************************************80
#
## p30_g() evaluates the gradient for problem 30.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  a = 1.0
  d = 6.0
  e = 10.0

  b = 5.1 / ( 4.0 * np.pi**2 )
  c = 5.0 / np.pi
  ff = 1.0 / ( 8.0 * np.pi )

  g[0] = 2.0 * a * ( x[1] - b * x[0]**2 + c * x[0] - d ) \
    * ( - 2.0 * b * x[0] + c ) - e * ( 1.0 - ff ) * np.sin ( x[0] )

  g[1] = 2.0 * a * ( x[1] - b * x[0]**2 + c * x[0] - d )

  return g


def p31_g ( n, x ):

#*****************************************************************************80
#
## p31_g() evaluates the gradient for problem 31.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  m = 5
  A = np.array ( [ \
       [ 4.0, 4.0, 4.0, 4.0 ], \
       [ 1.0, 1.0, 1.0, 1.0 ], \
       [ 8.0, 8.0, 8.0, 8.0 ], \
       [ 6.0, 6.0, 6.0, 6.0 ], \
       [ 3.0, 7.0, 3.0, 7.0 ] ] )

  c = np.array ( [ 0.1, 0.2, 0.2, 0.4, 0.6 ] )

  for k in range ( 0, n ):
    for j in range ( 0, m ):
      d = c[j] + np.sum ( ( x - A[j,:] )**2 )
      g[k] = g[k] + ( 2.0 * ( x[k] - A[j,k] ) ) / d**2

  return g

def p32_g ( n, x ):

#*****************************************************************************80
#
## p32_g() evaluates the gradient for problem 32.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  m = 7
  A = np.array ( [ 
   [ 4.0, 4.0, 4.0, 4.0 ], \
   [ 1.0, 1.0, 1.0, 1.0 ], \
   [ 8.0, 8.0, 8.0, 8.0 ], \
   [ 6.0, 6.0, 6.0, 6.0 ], \
   [ 3.0, 7.0, 3.0, 7.0 ], \
   [ 2.0, 9.0, 2.0, 9.0 ], \
   [ 5.0, 5.0, 3.0, 3.0 ] ] )

  c = np.array ( [ 0.1, 0.2, 0.2, 0.4, 0.6, 0.6, 0.3 ] )

  for k in range ( 0, n ):
    for j in range ( 0, m ):
      d = c[j] + np.sum ( ( x - A[j,:] )**2 )
      g[k] = g[k] + ( 2.0 * ( x[k] - A[j,k] ) ) / d**2

  return g

def p33_g ( n, x ):

#*****************************************************************************80
#
## p33_g() evaluates the gradient for problem 33.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  m = 10
  A = np.array ( [ \
      [ 4.0, 4.0, 4.0, 4.0 ], \
      [ 1.0, 1.0, 1.0, 1.0 ], \
      [ 8.0, 8.0, 8.0, 8.0 ], \
      [ 6.0, 6.0, 6.0, 6.0 ], \
      [ 3.0, 7.0, 3.0, 7.0 ], \
      [ 2.0, 9.0, 2.0, 9.0 ], \
      [ 5.0, 5.0, 3.0, 3.0 ], \
      [ 8.0, 1.0, 8.0, 1.0 ], \
      [ 6.0, 2.0, 6.0, 2.0 ], \
      [ 7.0, 3.6, 7.0, 3.6 ] ] )

  c = np.array ( [ 0.1, 0.2, 0.2, 0.4, 0.6, 0.6, 0.3, 0.7, 0.5, 0.5 ] )

  for k in range ( 0, n ):
    for j in range ( 0, m ):
      d = c[j] + np.sum ( ( x - A[j,:] )**2 )
      g[k] = g[k] + ( 2.0 * ( x[k] - A[j,k] ) ) / d**2

  return g

def p34_g ( n, x ):

#*****************************************************************************80
#
## p34_g() evaluates the gradient for problem 34.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  g[0] = 8.0 * x[0] - 8.4 * x[0]**3 + 2.0 * x[0]**5 + x[1]
  g[1] = x[0] - 8.0 * x[1] + 16.0 * x[1]**3

  return g

def p35_g ( n, x ):

#*****************************************************************************80
#
## p35_g() evaluates the gradient for problem 35.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  factor1 = 0.0
  df1dx1 = 0.0
  for i in range ( 1, 6 ):
    factor1 = factor1 + i               * np.cos ( ( i + 1.0 ) * x[0] + i )
    df1dx1 =  df1dx1  - i * ( i + 1.0 ) * np.sin ( ( i + 1.0 ) * x[0] + i )

  factor2 = 0.0
  df2dx2 = 0.0
  for i in range ( 1, 6 ):
    factor2 = factor2 + i               * np.cos ( ( i + 1.0 ) * x[1] + i )
    df2dx2 =  df2dx2  - i * ( i + 1.0 ) * np.sin ( ( i + 1.0 ) * x[1] + i )

  g[0] = df1dx1 * factor2
  g[1] = factor1 * df2dx2

  return g

def p37_g ( n, x ):

#*****************************************************************************80
#
## p37_g() evaluates the gradient for problem 37.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  arg = - ( x[0] - np.pi )**2 - ( x[1] - np.pi )**2

  g[0] = ( np.sin ( x[0] ) * np.cos ( x[1] ) \
       + 2.0 * np.cos ( x[0] ) * np.cos ( x[1] ) * ( x[0] - np.pi ) ) \
       * np.exp ( arg )

  g[1] = ( np.cos ( x[0] ) * np.sin ( x[1] ) \
       + 2.0 * np.cos ( x[0] ) * np.cos ( x[1] ) * ( x[1] - np.pi ) ) \
       * np.exp ( arg )

  return g

def p38_g ( n, x ):

#*****************************************************************************80
#
## p38_g() evaluates the gradient for problem 38.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  g[0] = 2.0 * x[0] + 0.9 * np.pi * np.sin ( 3.0 * np.pi * x[0] )
  g[1] = 4.0 * x[1] + 1.6 * np.pi * np.sin ( 4.0 * np.pi * x[1] )

  return g

def p39_g ( n, x ):

#*****************************************************************************80
#
## p39_g() evaluates the gradient for problem 39.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  g[0] = 2.0 * x[0] \
    + 0.9 * np.pi * np.sin ( 3.0 * np.pi * x[0] ) \
    * np.cos ( 4.0 * np.pi * x[1] )

  g[1] = 4.0 * x[1] \
    + 1.2 * np.pi * np.cos ( 3.0 * np.pi * x[0] ) \
    * np.sin ( 4.0 * np.pi * x[1] )

  return g

def p40_g ( n, x ):

#*****************************************************************************80
#
## p40_g() evaluates the gradient for problem 40.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  g[0] = 2.0 * x[0] + 0.9 * np.pi * np.sin ( 3.0 * np.pi * x[0] )
  g[1] = 4.0 * x[1] - 4.0 * np.pi * np.sin ( 4.0 * np.pi * x[1] )

  return g

def p41_g ( n, x ):

#*****************************************************************************80
#
## p41_g() evaluates the gradient for problem 41.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  g[0] = 400.0 * x[0]**3 - 400.0 * x[1] * x[0] + 2.0 * x[0] - 2.0

  g[1] = -200.0 * x[0]**2 + 220.2 * x[1] + 19.8 * x[3] - 40.0

  g[2] = -360.0 * x[2] * x[3] + 360.0 * x[2]**3 + 2.0 * x[2] - 2.0

  g[3] = 180.0 * x[3] - 180.0 * x[2]**2 + 20.2 * x[3] + 19.8 * x[1] - 40.0

  return g

def p42_g ( n, x ):

#*****************************************************************************80
#
## p42_g() evaluates the gradient for problem 42.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  g[0] = 2.0 * ( x[0] - x[1] ) / ( 1.0 + ( x[0] - x[1] )**2 )**2

  g[1] = 2.0 * ( x[1] - x[0] ) / ( 1.0 + ( x[0] - x[1] )**2 )**2 \
    - 0.5 * np.pi * x[2] * np.cos ( 0.5 * np.pi * x[1] * x[2] )

  g[2] = - 0.5 * np.pi * x[1] * np.cos ( 0.5 * np.pi * x[1] * x[2] )

  if ( x[1] != 0.0 ):

    arg = ( x[0] + 2.0 * x[1] + x[2] ) / x[1]
    term = np.exp ( - arg**2 )

    g[0] = g[0] + 2.0 * term * ( x[0] + 2.0 * x[1] + x[2] ) / x[1]**2
    g[1] = g[1] - 2.0 * term * ( x[0] + 2.0 * x[1] + x[2] ) \
      * ( x[0] + x[2] ) / x[1]**3
    g[2] = g[2] + 2.0 * term * ( x[0] + 2.0 * x[1] + x[2] ) / x[1]**2

  return g

def p43_g ( n, x ):

#*****************************************************************************80
#
## p43_g() evaluates the gradient for problem 43.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#
#    real X(N), the values of the variables.
#
#  Output:
#
#    real G(N), the gradient of the objective function.
#
  import numpy as np

  g = np.zeros ( n )

  g[0] = 4.0 * ( x[0]**2 + x[1] - 11.0 ) * x[0] \
       + 2.0 * ( x[0] + x[1]**2 - 7.0 )

  g[1] = 2.0 * ( x[0]**2 + x[1] - 11.0 ) \
       + 4.0 * ( x[0] + x[1]**2 - 7.0 ) * x[1]

  return g

def p00_gdif ( problem, n, x ):

#*****************************************************************************80
#
## p00_gdif() approximates the gradient via finite differences.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem number.
#
#    integer N, the number of variables.
#
#    real X(N), the point where the gradient
#    is to be approximated.
#
#  Output:
#
#    real GDIF(N), the approximated gradient vector.
#
  import numpy as np

  gdif = np.zeros ( n )

  eps = np.finfo(float).eps
  xrel = np.sqrt ( eps )

  for i in range ( 0, n ):

    if ( 0.0 <= x[i] ):
      dx = xrel * ( x[i] + 1.0 )
    else:
      dx = xrel * ( x[i] - 1.0 )

    xi = x[i]
    x[i] = xi + dx
    fplus = p00_f ( problem, n, x )

    x[i] = xi - dx
    fminus = p00_f ( problem, n, x )

    gdif[i] = ( fplus - fminus ) / ( 2.0 * dx )

    x[i] = xi

  return gdif

def p00_gdif_test ( ):

#*****************************************************************************80
#
## p00_gdif_test() compares the exact and approximate gradient vectors.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'p00_gdif_test():' )
  print ( '  p00_gdif() estimates the gradient vector G' )
  print ( '  with a finite difference estimate GDIF' )
#
#  Get the number of problems.
#
  problem_num = p00_problem_num ( )

  for problem in range ( 1, problem_num + 1 ):

    title = p00_title ( problem )

    n = p00_n ( problem )
    if ( n < 0 ):
      n = max ( abs ( n ), 4 )

    print ( '' )
    print ( '  Problem %d:  "%s"' % ( problem, title ) )

    x = p00_start ( problem, n )

    f_start = p00_f ( problem, n, x )

    g = p00_g ( problem, n, x )
    g_dif = p00_gdif ( problem, n, x )
    print ( '  %g  %g' % ( np.linalg.norm ( g ), np.linalg.norm ( g_dif ) ) )

  return

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

if ( __name__ == '__main__' ):
  timestamp ( )
  test_opt_test ( )
  timestamp ( )

