#! /usr/bin/env python3.8
#
def agm_values ( n_data ):

#*****************************************************************************80
#
## agm_values() returns some values of the AGM.
#
#  Discussion:
#
#    The AGM is defined for nonnegative A and B.
#
#    The AGM of numbers A and B is defined by setting
#
#      A(0) = A,
#      B(0) = B
#
#      A(N+1) = ( A(N) + B(N) ) / 2
#      B(N+1) = sqrt ( A(N) * B(N) )
#
#    The two sequences both converge to AGM(A,B).
#
#    In Mathematica, the AGM can be evaluated by
#
#      ArithmeticGeometricMean [ a, b ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real A, B, the argument ofs the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 14

  a_vec = np.array ( ( \
     22.0, \
     83.0, \
     42.0, \
     26.0, \
      4.0, \
      6.0, \
     40.0, \
     80.0, \
     90.0, \
      9.0, \
     53.0, \
      1.0, \
      1.0, \
      1.0, \
      1.5 ) )
  b_vec = np.array ( ( \
     96.0, \
     56.0, \
      7.0, \
     11.0, \
     63.0, \
     45.0, \
     75.0, \
      0.0, \
     35.0, \
      1.0, \
     53.0, \
      2.0, \
      4.0, \
      8.0, \
      8.0 ) )
  fx_vec = np.array ( ( \
     52.274641198704240049, \
     68.836530059858524345, \
     20.659301196734009322, \
     17.696854873743648823, \
     23.867049721753300163, \
     20.717015982805991662, \
     56.127842255616681863, \
      0.000000000000000000, \
     59.269565081229636528, \
     3.9362355036495554780, \
     53.000000000000000000, \
     1.4567910310469068692, \
     2.2430285802876025701, \
     3.6157561775973627487, \
     4.0816924080221632670 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    fx = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, fx

def agm_values_test ( ):

#*****************************************************************************80
#
## agm_values_test() tests agm_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2008
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'agm_values_test():' )
  print ( '  agm_values() stores values of' )
  print ( '  the arithmetic geometric mean function.' )
  print ( '' )
  print ( '      A           B         AGM(A,B)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, fx = agm_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16f' % ( a, b, fx ) )

  return

def agud ( g ):

#*****************************************************************************80
#
## agud() evaluates the inverse Gudermannian function.
#
#  Discussion:
#
#    The Gudermannian function relates the hyperbolic and trigonomentric
#    functions.  For any argument X, there is a corresponding value
#    G so that
#
#      SINH(X) = TAN(G).
#
#    This value G(X) is called the Gudermannian of X.  The inverse
#    Gudermannian function is given as input a value G and computes
#    the corresponding value X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real G, the value of the Gudermannian.
#
#    real VALUE, the argument of the Gudermannian.
#
  import numpy as np

  value = np.log ( np.tan ( 0.25 * np.pi + 0.5 * g ) )

  return value

def agud_test ( ):

#*****************************************************************************80
#
## agud_test() tests agud().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'agud_test():' )
  print ( '  agud() evaluates the inverse Gudermannian function.' )
  print ( '' )
  print ( '        X            GUD(X)     AGUD(GUD(X))' )
  print ( '' )

  for i in range ( 0, 11 ):
    x = 1.0 + i / 5.0
    g = gud ( x )
    x2 = agud ( g )
    print ( '  %12f  %12f  %12f' % ( x, g, x2 ) )

  return

def align_enum ( m, n ):

#*****************************************************************************80
#
## align_enum() counts the alignments of two sequences of M and N elements.
#
#  Discussion:
#
#    We assume that we have sequences A and B of M and N characters each.
#    An alignment of the two sequences is a rule matching corresponding
#    elements of one sequence to another.  Some elements of either sequence
#    can be matched to a null element.  If A(I1) and A(I2) are matched
#    to B(J1) and B(J2), and I1 < I2, then it must be the case that J1 < J2.
#
#    The 5 alignments of a sequence of 1 to a sequence of 2 are:
#
#          _1_   _2_   __3__   __4__   __5__
#
#      A:  1 -   - 1   - 1 -   - - 1   1 - -
#      B:  1 2   1 2   1 - 2   1 2 -   - 1 2
#
#    The formula is:
#
#      F(0,0) = 1
#      F(1,0) = 1
#      F(0,1) = 1
#      F(M,N) = F(M-1,N) + F(M-1,N-1) + F(M,N-1)
#
#    To compute F(M,N), it is not necessary to keep an M+1 by N+1
#    array in memory.  A vector of length N will do.
#
#    F(N,N) is approximately ( 1 + sqrt(2) )^(2*N+1) / sqrt ( N )
#
#  Example:
#
#    The initial portion of the table is:
#
#
#  M/N   0    1    2    3    4       5       6       7       8       9      10
#
#   0    1    1    1    1    1       1       1       1       1       1       1
#   1    1    3    5    7    9      11      13      15      17      19      21
#   2    1    5   13   25   41      61      85     113     145     181     221
#   3    1    7   25   63  129     231     377     575     833    1159    1561
#   4    1    9   41  129  321     681    1289    2241    3649    5641    8361
#   5    1   11   61  231  681    1683    3653    7183   13073   22363   36365
#   6    1   13   85  377 1289    3653    8989   19825   40081   75517  134245
#   7    1   15  113  575 2241    7183   19825   48639  108545  224143  433905
#   8    1   17  145  833 3649   13073   40081  108545  265729  598417 1256465
#   9    1   19  181 1159 5641   22363   75517  224143  598417 1462563 3317445
#  10    1   21  221 1561 8361   36365  134245  433905 1256465 3317445 8097453
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Michael Waterman,
#    Introduction to Computational Biology,
#    Chapman and Hall, 1995, pages 186-190.
#
#  Input:
#
#    integer M, N, the number of elements of the two sequences.
#
#  Output:
#
#    integer VALUE, the number of possible alignments of the
#    sequences.
#
  import numpy as np

  if ( m < 0 ):
    value = 0
    return value
  elif ( n < 0 ):
    value = 0
    return value
  elif ( m == 0 ):
    value = 1
    return value
  elif ( n == 0 ):
    value = 1
    return value

  fi = np.zeros ( n + 1 )

  for i in range ( 0, n + 1 ):
    fi[i] = 1

  for i in range ( 0, m ):

    fim1jm1 = 1

    for j in range ( 0, n ):

      fim1j = fi[j+1]

      fi[j+1] = fi[j+1] + fi[j] + fim1jm1

      fim1jm1 = fim1j

  value = fi[n]

  return value

def align_enum_test ( ):

#*****************************************************************************80
#
## align_enum_test() tests align_enum().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m_max = 10
  n_max = 10
  table = np.zeros ( [ m_max + 1, n_max + 1 ] )

  print ( '' )
  print ( 'align_enum_test():' )
  print ( '  align_enum() counts the number of possible' )
  print ( '  alignments of two biological sequences.' )

  for i in range ( 0, m_max + 1 ):
    for j in range ( 0, n_max + 1 ):
      table[i,j] = align_enum ( i, j )

  print ( '' )
  print ( '  Alignment enumeration table:' )
  print ( '' )
  for j in range ( 0, 5 ):
    print ( '%5d' % ( j ) ),
  for j in range ( 5, n_max + 1 ):
    print ( '%8d' % ( j ) ),
  print ( '' )
  print ( '' )
  for i in range ( 0, m_max + 1 ):
    for j in range ( 0, 5 ):
      print ( '%5d' % ( table[i,j] ) ),
    for j in range ( 5, n_max + 1 ):
      print ( '%8d' % ( table[i,j] ) ),
    print ( '' )

  return

def bell_poly_coef ( n ):

#*****************************************************************************80
#
## bell_poly_coef(): Coefficients of a Bell polynomial.
#
#  First terms:
#
#    N    0    1    2    3    4    5    6    7    8
#
#    0    1
#    1    0    1    
#    2    0    1    1
#    3    0    1    3    1
#    4    0    1    7    6    1
#    5    0    1   15   25   10    1
#    6    0    1   31   90   65   15    1
#    7    0    1   63  301  350  140   21    1
#    8    0    1  127  966 1701 1050  266   28    1
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#    integer C[0:N], the coefficients.
#
  import numpy as np

  c = np.zeros ( n + 1 )

  c[0] = 1
 
  for i in range ( 1, n + 1 ):
    for j in range ( i, 0, -1 ):
      c[j] = j * c[j] + c[j-1]
    c[0] = 0
 
  return c

def bell_poly_coef_test ( ):

#*****************************************************************************80
#
## bell_poly_coef_test() tests bell_poly_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2018
#
#  Author:
#
#    John Burkardt
#
  n_max = 10

  print ( '' )
  print ( 'bell_poly_coef_test():' )
  print ( '  bell_poly_coef() returns the coefficients of a Bell polynomial.' )
  print ( '' )
  print ( '  Table of polyomial coefficients:' )
  print ( '' )

  for n in range ( 0, n_max + 1 ):

    c = bell_poly_coef ( n )
    print ( '  %2d:' % ( n ) ),
    for i in range ( 0, n + 1 ):
      print ( '%5d' % ( c[i] ) ),
    print ( '' )

  return

def bell ( n ):

#*****************************************************************************80
#
## bell() returns the Bell numbers from 0 to N.
#
#  Discussion:
#
#    The Bell number B(N) is the number of restricted growth functions
#    on N.
#
#    Note that the Stirling numbers of the second kind, S^m_n, count the
#    number of partitions of N objects into M classes, and so it is
#    true that
#
#      B(N) = S^1_N + S^2_N + ... + S^N_N.
#
#  Definition:
#
#    The Bell number B(N) is defined as the number of partitions (of
#    any size) of a set of N distinguishable objects.
#
#    A partition of a set is a division of the objects of the set into
#    subsets.
#
#  Examples:
#
#    There are 15 partitions of a set of 4 objects:
#
#      (1234), (123)(4), (124)(3), (12)(34), (12)(3)(4),
#      (134)(2), (13)(24), (13)(2)(4), (14)(23), (1)(234),
#      (1)(23)(4), (14)(2)(3), (1)(24)(3), (1)(2)(34), (1)(2)(3)(4)
#
#    and so B(4) = 15.
#
#  First values:
#
#     N         B(N)
#     0           1
#     1           1
#     2           2
#     3           5
#     4          15
#     5          52
#     6         203
#     7         877
#     8        4140
#     9       21147
#    10      115975
#
#  Recursion:
#
#    B(I) = sum ( 1 <= J <= I ) Binomial ( I-1, J-1 ) * B(I-J)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of Bell numbers desired.
#
#    integer B(1:N+1), the Bell numbers from 0 to N.
#
  import numpy as np

  b = np.zeros ( n + 1 )

  b[0] = 1

  for i in range ( 1, n + 1 ):
    b[i] = 0
    for j in range ( 1, i + 1 ):
      b[i] = b[i] + i4_choose ( i - 1, j - 1 ) * b[i-j]

  return b

def bell_test ( ):

#*****************************************************************************80
#
## bell_test() tests bell().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bell_test():' )
  print ( '  bell() computes Bell numbers.' )
  print ( '' )
  print ( '   N  exact C(I)  computed C(I)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = bell_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = bell ( n )

    print ( '  %2d  %8d  %8d' % ( n, c, c2[n] ) )

  return

def bell_values ( n_data ):

#*****************************************************************************80
#
## bell_values() returns some values of the Bell numbers.
#
#  Discussion:
#
#    The Bell number B(N) is the number of restricted growth functions on N.
#
#    Note that the Stirling numbers of the second kind, S^m_n, count the
#    number of partitions of N objects into M classes, and so it is
#    true that
#
#      B(N) = S^1_N + S^2_N + ... + S^N_N.
#
#    The Bell numbers were named for Eric Temple Bell.
#
#    In Mathematica, the function can be evaluated by
#
#      Sum[StirlingS2[n,m],{m,1,n}]
#
#    The Bell number B(N) is defined as the number of partitions (of
#    any size) of a set of N distinguishable objects.  
#
#    A partition of a set is a division of the objects of the set into 
#    subsets.
#
#  Example:
#
#    There are 15 partitions of a set of 4 objects:
#
#      (1234), 
#      (123) (4), 
#      (124) (3), 
#      (12) (34), 
#      (12) (3) (4), 
#      (134) (2), 
#      (13) (24), 
#      (13) (2) (4), 
#      (14) (23), 
#      (1) (234),
#      (1) (23) (4), 
#      (14) (2) (3), 
#      (1) (24) (3), 
#      (1) (2) (34), 
#      (1) (2) (3) (4).
#
#    and so B(4) = 15.
#
#  First values:
#
#     N         B(N)
#     0           1
#     1           1
#     2           2
#     3           5
#     4          15
#     5          52
#     6         203
#     7         877
#     8        4140
#     9       21147
#    10      115975
#
#  Recursion:
#
#    B(I) = sum ( 1 <= J <=I ) Binomial ( I-1, J-1 ) * B(I-J)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the Bell number.
#
#    integer C, the value of the Bell number.
#
  import numpy as np

  n_max = 11

  c_vec = np.array ( ( 1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975 ) )

  n_vec = np.array ( ( 0,  1,  2,  3,  4, 5,  6,  7,  8,  9,  10 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def bell_values_test ( ):

#*****************************************************************************80
#
## bell_values_test() tests bell_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 November 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bell_values_test():' )
  print ( '  bell_values() returns values of' )
  print ( '  the Bell numbers.' )
  print ( '' )
  print ( '     N        BELL(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = bell_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '%6d  %10d' % ( n, c ) )

  return

def benford ( ival ):

#*****************************************************************************80
#
## benford() returns the Benford probability of one or more significant digits.
#
#  Discussion:
#
#    Benford's law is an empirical formula explaining the observed
#    distribution of initial digits in lists culled from newspapers,
#    tax forms, stock market prices, and so on.  It predicts the observed
#    high frequency of the initial digit 1, for instance.
#
#    Note that the probabilities of digits 1 through 9 are guaranteed
#    to add up to 1, since
#      LOG10 ( 2/1 ) + LOG10 ( 3/2) + LOG10 ( 4/3 ) + ... + LOG10 ( 10/9 )
#      = LOG10 ( 2/1 * 3/2 * 4/3 * ... * 10/9 ) = LOG10 ( 10 ) = 1.
#
#  Formula:
#
#    Prob ( First significant digits are IVAL ) =
#      LOG10 ( ( IVAL + 1 ) / IVAL ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frank Benford,
#    The Law of Anomalous Numbers,
#    Proceedings of the American Philosophical Society,
#    Volume 78, pages 551-572, 1938.
#
#    T P Hill,
#    The First Digit Phenomenon,
#    American Scientist,
#    Volume 86, July/August 1998, pages 358 - 363.
#
#    R Raimi,
#    The Peculiar Distribution of First Digits,
#    Scientific American,
#    December 1969, pages 109-119.
#
#  Input:
#
#    integer IVAL, the string of significant digits to be checked.
#    If IVAL is 1, then we are asking for the Benford probability that
#    a value will have first digit 1.  If IVAL is 123, we are asking for
#    the probability that the first three digits will be 123, and so on.
#    Note that IVAL must not be 0 or negative.
#
#    real VALUE, the Benford probability that an item taken from
#    a real world distribution will have the initial digits IVAL.
#
  import numpy as np

  if ( ival <= 0 ):
    print ( '' )
    print ( 'benford(): Fatal error!' )
    print ( '  The input argument must be positive.' )
    print ( '  Your value was %d' % ( ival ) )
    raise Exception ( 'benford(): Fatal error!' )
 
  value = np.log10 ( float ( ival + 1 ) / float ( ival ) )

  return value

def benford_test ( ):

#*****************************************************************************80
#
## benford_test() tests benford().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'benford_test():' )
  print ( '  benford(I) is the Benford probability of the' )
  print ( '  initial digit sequence I.' )
  print ( '' )
  print ( '   I     BENFORD(I)' )
  print ( '' )

  for i in range ( 1, 10 ):
    print ( '  %2d  %12f' % ( i, benford(i) ) )

  return

def bernoulli_number2 ( n ):

#*****************************************************************************80
#
## bernoulli_number2() evaluates the Bernoulli numbers.
#
#  Discussion:
#
#    The Bernoulli numbers are rational.
#
#    If we define the sum of the M-th powers of the first N integers as:
#
#      SIGMA(M,N) = sum ( 0 <= I <= N ) I^M
#
#    and let C(I,J) be the combinatorial coefficient:
#
#      C(I,J) = I! / ( ( I - J )! * J! )
#
#    then the Bernoulli numbers B(J) satisfy:
#
#      SIGMA(M,N) = 1/(M+1) * sum ( 0 <= J <= M ) C(M+1,J) B(J) * (N+1)^(M+1-J)
#
#    Note that the Bernoulli numbers grow rapidly.  Bernoulli number
#    62 is probably the last that can be computed on the VAX without
#    overflow.
#
#  First values:
#
#   B0  1                   =         1.00000000000
#   B1 -1/2                 =        -0.50000000000
#   B2  1/6                 =         1.66666666666
#   B3  0                   =         0
#   B4 -1/30                =        -0.03333333333
#   B5  0                   =         0
#   B6  1/42                =         0.02380952380
#   B7  0                   =         0
#   B8 -1/30                =        -0.03333333333
#   B9  0                   =         0
#  B10  5/66                =         0.07575757575
#  B11  0                   =         0
#  B12 -691/2730            =        -0.25311355311
#  B13  0                   =         0
#  B14  7/6                 =         1.16666666666
#  B15  0                   =         0
#  B16 -3617/510            =        -7.09215686274
#  B17  0                   =         0
#  B18  43867/798           =        54.97117794486
#  B19  0                   =         0
#  B20 -174611/330          =      -529.12424242424
#  B21  0                   =         0
#  B22  854,513/138         =      6192.123
#  B23  0                   =         0
#  B24 -236364091/2730      =    -86580.257
#  B25  0                   =         0
#  B26  8553103/6           =   1425517.16666
#  B27  0                   =         0
#  B28 -23749461029/870     = -27298231.0678
#  B29  0                   =         0
#  B30  8615841276005/14322 = 601580873.901
#
#  Recursion:
#
#    With C(N+1,K) denoting the standard binomial coefficient,
#
#    B(0) = 1.0
#    B(N) = - ( sum ( 0 <= K < N ) C(N+1,K) * B(K) ) / C(N+1,N)
#
#  Special Values:
#
#    Except for B(1), all Bernoulli numbers of odd index are 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the highest order Bernoulli number to compute.
#
#    real B(1:N+1), the requested Bernoulli numbers B(0) through
#    B(N).
#
  import numpy as np

  kmax = 400
  tol = 1.0E-06

  b = np.zeros ( n + 1 )

  b[0] = 1.0

  if ( n < 1 ):
    return b

  b[1] = -0.5

  if ( n < 2 ):
    return b

  altpi = np.log ( 2.0 * np.pi )
#
#  Initial estimates for B(I), I = 2 to N
#
  b[2] = np.log ( 2.0 );
  for i in range ( 3, n + 1 ):
    if ( ( i % 2 ) == 1 ):
      b[i] = 0.0
    else:
      b[i] = np.log ( i * ( i - 1 ) ) + b[i-2]

  b[2] = 1.0 / 6.0

  if ( n <= 3 ):
    return b

  b[4] = - 1.0 / 30.0

  sgn = -1.0
 
  for i in range ( 6, n + 1, 2 ):
 
    sgn = - sgn
    t = 2.0 * sgn * np.exp ( b[i] - i * altpi )
 
    sum2 = 1.0

    for k in range ( 2, kmax + 1 ):

      term = 1.0 / ( k ** i )
      sum2 = sum2 + term

      if ( term <= tol * sum2 ):
        break
 
    b[i] = t * sum2
 
  return b

def bernoulli_number2_test ( ):

#*****************************************************************************80
#
## bernoulli_number2_test() tests bernoulli_number2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bernoulli_number2_test():' )
  print ( '  bernoulli_number2 computes Bernoulli numbers;' )
  print ( '' )
  print ( '   I      Exact        Bernoulli' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c0 = bernoulli_number_values ( n_data )

    if ( n_data == 0 ):
      break

    c1 = bernoulli_number2 ( n )

    print ( '  %2d  %14e  %14e' % ( n, c0, c1[n] ) )

  return

def bernoulli_number3 ( n ):

#*****************************************************************************80
#
## bernoulli_number3() computes the value of the Bernoulli number B(N).
#
#  Discussion:
#
#    The Bernoulli numbers are rational.
#
#    If we define the sum of the M-th powers of the first N integers as:
#
#      SIGMA(M,N) = sum ( 0 <= I <= N ) I^M
#
#    and let C(I,J) be the combinatorial coefficient:
#
#      C(I,J) = I! / ( ( I - J )! * J! )
#
#    then the Bernoulli numbers B(J) satisfy:
#
#      SIGMA(M,N) = 1/(M+1) * sum ( 0 <= J <= M ) C(M+1,J) B(J) * (N+1)^(M+1-J)
#
#  First values:
#
#     B0  1                   =         1.00000000000
#     B1 -1/2                 =        -0.50000000000
#     B2  1/6                 =         1.66666666666
#     B3  0                   =         0
#     B4 -1/30                =        -0.03333333333
#     B5  0                   =         0
#     B6  1/42                =         0.02380952380
#     B7  0                   =         0
#     B8 -1/30                =        -0.03333333333
#     B9  0                   =         0
#    B10  5/66                =         0.07575757575
#    B11  0                   =         0
#    B12 -691/2730            =        -0.25311355311
#    B13  0                   =         0
#    B14  7/6                 =         1.16666666666
#    B15  0                   =         0
#    B16 -3617/510            =        -7.09215686274
#    B17  0                   =         0
#    B18  43867/798           =        54.97117794486
#    B19  0                   =         0
#    B20 -174611/330          =      -529.12424242424
#    B21  0                   =         0
#    B22  854513/138          =      6192.123
#    B23  0                   =         0
#    B24 -236364091/2730      =    -86580.257
#    B25  0                   =         0
#    B26  8553103/6           =   1425517.16666
#    B27  0                   =         0
#    B28 -23749461029/870     = -27298231.0678
#    B29  0                   =         0
#    B30  8615841276005/14322 = 601580873.901
#
#  Recursion:
#
#    With C(N+1,K) denoting the standard binomial coefficient,
#
#    B(0) = 1.0
#    B(N) = - ( sum ( 0 <= K < N ) C(N+1,K) * B(K) ) / C(N+1,N)
#
#  Special Values:
#
#    Except for B(1), all Bernoulli numbers of odd index are 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the Bernoulli number to compute.
#
#    real B, the desired Bernoulli number.
#
  import math
  import numpy as np

  itmax = 1000
  tol = 5.0E-07

  if ( n < 0 ):

    b = 0.0

  elif ( n == 0 ):

    b = 1.0

  elif ( n == 1 ):

    b = -0.5

  elif ( n == 2 ):

    b = 1.0 / 6.0

  elif ( ( n % 2 ) == 1 ):

    b = 0.0

  else:

    sum2 = 0.0
    
    for i in range ( 1, itmax + 1 ):

      term = 1.0 / float ( i ) ** n
      sum2 = sum2 + term

      if ( abs ( term ) < tol or abs ( term ) < tol * abs ( sum2 ) ):
        break

    b = 2.0 * sum2 * math.factorial ( n ) / ( 2.0 * np.pi ) ** n

    if ( ( n % 4 ) == 0 ):
      b = -b

  return b

def bernoulli_number3_test ( ):

#*****************************************************************************80
#
## bernoulli_number3_test() tests bernoulli_number3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bernoulli_number3_test():' )
  print ( '  bernoulli_number3 computes Bernoulli numbers;' )
  print ( '' )
  print ( '   I      Exact        Bernoulli' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c0 = bernoulli_number_values ( n_data )

    if ( n_data == 0 ):
      break

    c1 = bernoulli_number3 ( n )

    print ( '  %2d  %14e  %14e' % ( n, c0, c1 ) )

  return

def bernoulli_number ( n ):

#*****************************************************************************80
#
## bernoulli_number() computes the value of the Bernoulli numbers B(0) through B(N).
#
#  Discussion:
#
#    The Bernoulli numbers are rational.
#
#    If we define the sum of the M-th powers of the first N integers as:
#
#      SIGMA(M,N) = sum ( 0 <= I <= N ) I^M
#
#    and let C(I,J) be the combinatorial coefficient:
#
#      C(I,J) = I! / ( ( I - J )! * J! )
#
#    then the Bernoulli numbers B(J) satisfy:
#
#      SIGMA(M,N) = 1/(M+1) * sum ( 0 <= J <= M ) C(M+1,J) B(J) * (N+1)^(M+1-J)
#
#  First values:
#
#   B0  1                   =         1.00000000000
#   B1 -1/2                 =        -0.50000000000
#   B2  1/6                 =         1.66666666666
#   B3  0                   =         0
#   B4 -1/30                =        -0.03333333333
#   B5  0                   =         0
#   B6  1/42                =         0.02380952380
#   B7  0                   =         0
#   B8 -1/30                =        -0.03333333333
#   B9  0                   =         0
#  B10  5/66                =         0.07575757575
#  B11  0                   =         0
#  B12 -691/2730            =        -0.25311355311
#  B13  0                   =         0
#  B14  7/6                 =         1.16666666666
#  B15  0                   =         0
#  B16 -3617/510            =        -7.09215686274
#  B17  0                   =         0
#  B18  43867/798           =        54.97117794486
#  B19  0                   =         0
#  B20 -174611/330          =      -529.12424242424
#  B21  0                   =         0
#  B22  854,513/138         =      6192.123
#  B23  0                   =         0
#  B24 -236364091/2730      =    -86580.257
#  B25  0                   =         0
#  B26  8553103/6           =   1425517.16666
#  B27  0                   =         0
#  B28 -23749461029/870     = -27298231.0678
#  B29  0                   =         0
#  B30  8615841276005/14322 = 601580873.901
#
#  Recursion:
#
#    With C(N+1,K) denoting the standard binomial coefficient,
#
#    B(0) = 1.0
#    B(N) = - ( sum ( 0 <= K < N ) C(N+1,K) * B(K) ) / C(N+1,N)
#
#  Warning:
#
#    This recursion, which is used in this routine, rapidly results
#    in significant errors.
#
#  Special Values:
#
#    Except for B(1), all Bernoulli numbers of odd index are 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the highest Bernoulli number to compute.
#
#    real B(1:N+1), B(I+1) contains the I-th Bernoulli number.
#
  import numpy as np

  b = np.zeros ( n + 1 );

  b[0] = 1.0

  if ( n < 1 ):
    return b

  b[1] = -0.5

  c = np.zeros ( n + 2 )
  c[0] = 1
  c[1] = 2
  c[2] = 1
 
  for i in range ( 2, n + 1 ):

    c = comb_row_next ( i + 1, c )
 
    if ( ( i % 2 ) == 1 ):
 
      b[i] = 0.0
 
    else:
 
      b_sum = 0.0;
      for j in range ( 0, i ):
        b_sum = b_sum + b[j] * c[j]
 
      b[i] = - b_sum / c[i]

  return b

def bernoulli_number_test ( ):

#*****************************************************************************80
#
## bernoulli_number_test() tests bernoulli_number().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bernoulli_number_test():' )
  print ( '  bernoulli_number() computes Bernoulli numbers;' )
  print ( '' )
  print ( '   I      Exact        Bernoulli' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c0 = bernoulli_number_values ( n_data )

    if ( n_data == 0 ):
      break

    c1 = bernoulli_number ( n )

    print ( '  %2d  %14e  %14e' % ( n, c0, c1[n] ) )

  return

def bernoulli_number_values ( n_data ):

#*****************************************************************************80
#
## bernoulli_number_values() returns some values of the Bernoulli numbers.
#
#  Discussion:
#
#    The Bernoulli numbers are rational.
#
#    If we define the sum of the M-th powers of the first N integers as:
#
#      SIGMA(M,N) = sum ( 0 <= I <= N ) I**M
#
#    and let C(I,J) be the combinatorial coefficient:
#
#      C(I,J) = I! / ( ( I - J )! * J! )
#
#    then the Bernoulli numbers B(J) satisfy:
#
#      SIGMA(M,N) = 1/(M+1) * sum ( 0 <= J <= M ) C(M+1,J) B(J) * (N+1)**(M+1-J)
#
#    In Mathematica, the function can be evaluated by:
#
#      BernoulliB[n]
#
#  First values:
#
#   B0  1                   =         1.00000000000
#   B1 -1/2                 =        -0.50000000000
#   B2  1/6                 =         1.66666666666
#   B3  0                   =         0
#   B4 -1/30                =        -0.03333333333
#   B5  0                   =         0
#   B6  1/42                =         0.02380952380
#   B7  0                   =         0
#   B8 -1/30                =        -0.03333333333
#   B9  0                   =         0
#  B10  5/66                =         0.07575757575
#  B11  0                   =         0
#  B12 -691/2730            =        -0.25311355311
#  B13  0                   =         0
#  B14  7/6                 =         1.16666666666
#  B15  0                   =         0
#  B16 -3617/510            =        -7.09215686274
#  B17  0                   =         0
#  B18  43867/798           =        54.97117794486
#  B19  0                   =         0
#  B20 -174611/330          =      -529.12424242424
#  B21  0                   =         0
#  B22  854,513/138         =      6192.123
#  B23  0                   =         0
#  B24 -236364091/2730      =    -86580.257
#  B25  0                   =         0
#  B26  8553103/6           =   1425517.16666
#  B27  0                   =         0
#  B28 -23749461029/870     = -27298231.0678
#  B29  0                   =         0
#  B30  8615841276005/14322 = 601580873.901
#
#  Recursion:
#
#    With C(N+1,K) denoting the standard binomial coefficient,
#
#    B(0) = 1.0
#    B(N) = - ( sum ( 0 <= K < N ) C(N+1,K) * B(K) ) / C(N+1,N)
#
#  Special Values:
#
#    Except for B(1), all Bernoulli numbers of odd index are 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the Bernoulli number.
#
#    real C, the value of the Bernoulli number.
#
  import numpy as np

  n_max = 10

  c_vec = np.array ( ( 
      0.1000000000000000E+01, \
     -0.5000000000000000E+00, \
      0.1666666666666667E+00, \
      0.0000000000000000E+00, \
     -0.3333333333333333E-01, \
     -0.2380952380952380E-01, \
     -0.3333333333333333E-01, \
      0.7575757575757575E-01, \
     -0.5291242424242424E+03, \
      0.6015808739006424E+09  ) )

  n_vec = np.array ( ( 0,  1,  2,  3,  4, 6,  8, 10, 20, 30 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def bernoulli_number_values_test ( ):

#*****************************************************************************80
#
## bernoulli_number_values_test() tests bernoulli_number_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bernoulli_number_values_test():' )
  print ( '  bernoulli_number_values() returns values of' )
  print ( '  the Bernoulli numbers.' )
  print ( '' )
  print ( '     N        bernoulli_number(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = bernoulli_number_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '%6d  %14.6g' % ( n, c ) )

  return

def bernoulli_poly2 ( n, x ):

#*****************************************************************************80
#
## bernoulli_poly2() evaluates the Bernoulli polynomial of order N at X.
#
#  Discussion:
#
#    Thanks to Bart Vandewoestyne for pointing out an error in the previous
#    documentation, 31 January 2008.
#
#    Special values of the Bernoulli polynomial include:
#
#      B(N,0) = B(N,1) = B(N), the N-th Bernoulli number.
#
#      B'(N,X) = N * B(N-1,X)
#
#      B(N,X+1) - B(N,X) = N * X^(N-1)
#      B(N,X) = (-1)^N * B(N,1-X)
#
#    A formula for the Bernoulli polynomial in terms of the Bernoulli
#    numbers is:
#
#      B(N,X) = sum ( 0 <= K <= N ) B(K) * C(N,K) * X^(N-K)
#
#    The first few polynomials include:
#
#      B(0,X) = 1
#      B(1,X) = X    - 1/2
#      B(2,X) = X^2 -   X      +  1/6
#      B(3,X) = X^3 - 3/2*X^2 +  1/2*X
#      B(4,X) = X^4 - 2*X^3   +      X^2 - 1/30
#      B(5,X) = X^5 - 5/2*X^4 +  5/3*X^3 - 1/6*X
#      B(6,X) = X^6 - 3*X^5   +  5/2*X^4 - 1/2*X^2 + 1/42
#      B(7,X) = X^7 - 7/2*X^6 +  7/2*X^5 - 7/6*X^3 + 1/6*X
#      B(8,X) = X^8 - 4*X^7   + 14/3*X^6 - 7/3*X^4 + 2/3*X^2 - 1/30
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the Bernoulli polynomial to
#    be evaluated.  N must be 0 or greater.
#
#    real X, the value of X at which the polynomial is to
#    be evaluated.
#
#    real BX, the value of B(N,X).
#
  fact = 1.0

  b = bernoulli_number3 ( 0 )

  bx = b

  for i in range ( 1, n + 1 ):
    fact = fact * ( n + 1 - i ) / i
    b = bernoulli_number3 ( i )
    bx = bx * x + fact * b

  return bx

def bernoulli_poly2_test ( ):

#*****************************************************************************80
#
## bernoulli_poly2_test() tests bernoulli_poly2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 December 2014
#
#  Author:
#
#    John Burkardt
#
  n = 15
  x = 0.2

  print ( '' )
  print ( 'bernoulli_poly2_test():' )
  print ( '  bernoulli_poly2() computes Bernoulli polynomials;' )
  print ( '' )
  print ( '  X = %g' % ( x ) )
  print ( '' )
  print ( '   I      B(I,X)' )
  print ( '' )

  for i in range ( 1, n + 1 ):

    bx = bernoulli_poly2 ( i, x )
    print ( '  %2d  %14g' % ( i, bx ) )

  return

def bernoulli_poly ( n, x ):

#*****************************************************************************80
#
## bernoulli_poly() evaluates the Bernoulli polynomial of order N at X.
#
#  Discussion:
#
#    Thanks to Bart Vandewoestyne for pointing out an error in the previous
#    documentation, 31 January 2008.
#
#    Special values of the Bernoulli polynomial include:
#
#      B(N,0) = B(N,1) = B(N), the N-th Bernoulli number.
#
#      B'(N,X) = N * B(N-1,X)
#
#      B(N,X+1) - B(N,X) = N * X^(N-1)
#      B(N,X) = (-1)^N * B(N,1-X)
#
#    A formula for the Bernoulli polynomial in terms of the Bernoulli
#    numbers is:
#
#      B(N,X) = sum ( 0 <= K <= N ) B(K) * C(N,K) * X^(N-K)
#
#    The first few polynomials include:
#
#      B(0,X) = 1
#      B(1,X) = X    - 1/2
#      B(2,X) = X^2 -   X      +  1/6
#      B(3,X) = X^3 - 3/2*X^2 +  1/2*X
#      B(4,X) = X^4 - 2*X^3   +      X^2 - 1/30
#      B(5,X) = X^5 - 5/2*X^4 +  5/3*X^3 - 1/6*X
#      B(6,X) = X^6 - 3*X^5   +  5/2*X^4 - 1/2*X^2 + 1/42
#      B(7,X) = X^7 - 7/2*X^6 +  7/2*X^5 - 7/6*X^3 + 1/6*X
#      B(8,X) = X^8 - 4*X^7   + 14/3*X^6 - 7/3*X^4 + 2/3*X^2 - 1/30
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the Bernoulli polynomial to
#    be evaluated.  N must be 0 or greater.
#
#    real X, the value of X at which the polynomial is to
#    be evaluated.
#
#    real BX, the value of B(N,X).
#
  import numpy as np

  b = bernoulli_number ( n );
#
#  Get row N of Pascal's triangle.
#
  c = np.zeros ( n + 1 )

  for i in range ( 0, n + 1 ):
    c = comb_row_next ( i, c )
 
  bx = 1.0
  for i in range ( 1, n + 1 ):
    bx = bx * x + b[i] * c[i]

  return bx

def bernoulli_poly_test ( ):

#*****************************************************************************80
#
## bernoulli_poly_test() tests bernoulli_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  n = 15
  x = 0.2

  print ( '' )
  print ( 'bernoulli_poly_test():' )
  print ( '  bernoulli_poly() computes Bernoulli polynomials;' )
  print ( '' )
  print ( '  X = %g' % ( x ) )
  print ( '' )
  print ( '   I      B(I,X)' )
  print ( '' )

  for i in range ( 1, n + 1 ):

    bx = bernoulli_poly ( i, x )
    print ( '  %2d  %14g' % ( i, bx ) )

  return

def bernstein_poly_01_values ( n_data ):

#*****************************************************************************80
#
## bernstein_poly_01_values() returns some values of the Bernstein polynomials.
#
#  Discussion:
#
#    The Bernstein polynomials are assumed to be based on [0,1].
#
#    The formula for the Bernstein polynomials is
#
#      B(N,I)(X) = [N!/(I!*(N-I)!)] * (1-X)^(N-I) * X^I
#
#    In Mathematica, the function can be evaluated by:
#
#      Binomial[n,i] * (1-x)^(n-i) * x^i
#
#  First values:
#
#    B(0,0)(X) = 1
#
#    B(1,0)(X) =      1-X
#    B(1,1)(X) =               X
#
#    B(2,0)(X) =     (1-X)^2
#    B(2,1)(X) = 2 * (1-X)   * X
#    B(2,2)(X) =               X^2
#
#    B(3,0)(X) =     (1-X)^3
#    B(3,1)(X) = 3 * (1-X)^2 * X
#    B(3,2)(X) = 3 * (1-X)   * X^2
#    B(3,3)(X) =               X^3
#
#    B(4,0)(X) =     (1-X)^4
#    B(4,1)(X) = 4 * (1-X)^3 * X
#    B(4,2)(X) = 6 * (1-X)^2 * X^2
#    B(4,3)(X) = 4 * (1-X)   * X^3
#    B(4,4)(X) =               X^4
#
#  Special values:
#
#    B(N,I)(X) has a unique maximum value at X = I/N.
#
#    B(N,I)(X) has an I-fold zero at 0 and and N-I fold zero at 1.
#
#    B(N,I)(1/2) = C(N,K) / 2^N
#
#    For a fixed X and N, the polynomials add up to 1:
#
#      Sum ( 0 <= I <= N ) B(N,I)(X) = 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the degree of the polynomial.
#
#    integer K, the index of the polynomial.
#
#    real X, the argument of the polynomial.
#
#    real F, the value of the polynomial B(N,K)(X).
#
  import numpy as np

  n_max = 15

  f_vec = np.array ( ( \
     0.1000000000000000E+01, \
     0.7500000000000000E+00, \
     0.2500000000000000E+00, \
     0.5625000000000000E+00, \
     0.3750000000000000E+00, \
     0.6250000000000000E-01, \
     0.4218750000000000E+00, \
     0.4218750000000000E+00, \
     0.1406250000000000E+00, \
     0.1562500000000000E-01, \
     0.3164062500000000E+00, \
     0.4218750000000000E+00, \
     0.2109375000000000E+00, \
     0.4687500000000000E-01, \
     0.3906250000000000E-02 ) )

  k_vec = np.array ( ( \
    0, \
    0, 1, \
    0, 1, 2, \
    0, 1, 2, 3, \
    0, 1, 2, 3, 4 ))

  n_vec = np.array ( ( \
    0, \
    1, 1, \
    2, 2, 2, \
    3, 3, 3, 3, \
    4, 4, 4, 4, 4 ))

  x_vec = np.array ( ( \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    k = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    k = k_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, k, x, f

def bernstein_poly_01_values_test ( ):

#*****************************************************************************80
#
## bernstein_poly_01_values_test() tests bernstein_poly_01_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bernstein_poly_01_values_test():' )
  print ( '  bernstein_poly_01_values() stores values of Bernstein polynomials.' )
  print ( '' )
  print ( '      N       K            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, k, x, f = bernstein_poly_01_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %6d  %12f  %24.16g' % ( n, k, x, f ) )

  return

def bernstein_poly ( n, x ):

#*****************************************************************************80
#
## bernstein_poly() evaluates the Bernstein polynomials at a point X.
#
#  Discussion:
#
#    The Bernstein polynomials are assumed to be based on [0,1].
#
#  Formula:
#
#    B(N,I)(X) = [N!/(I!*(N-I)!)] * (1-X)^(N-I) * X^I
#
#  First values:
#
#    B(0,0)(X) = 1
#
#    B(1,0)(X) =      1-X
#    B(1,1)(X) =                X
#
#    B(2,0)(X) =     (1-X)^2
#    B(2,1)(X) = 2 * (1-X)    * X
#    B(2,2)(X) =                X^2
#
#    B(3,0)(X) =     (1-X)^3
#    B(3,1)(X) = 3 * (1-X)^2  * X
#    B(3,2)(X) = 3 * (1-X)    * X^2
#    B(3,3)(X) =                X^3
#
#    B(4,0)(X) =     (1-X)^4
#    B(4,1)(X) = 4 * (1-X)^3  * X
#    B(4,2)(X) = 6 * (1-X)^2  * X^2
#    B(4,3)(X) = 4 * (1-X)    * X^3
#    B(4,4)(X) =                X^4
#
#  Special values:
#
#    B(N,I)(X) has a unique maximum value at X = I/N.
#
#    B(N,I)(X) has an I-fold zero at 0 and and N-I fold zero at 1.
#
#    B(N,I)(1/2) = C(N,K) / 2^N
#
#    For a fixed X and N, the polynomials add up to 1:
#
#      Sum ( 0 <= I <= N ) B(N,I)(X) = 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the degree of the Bernstein polynomials to be
#    used.  For any N, there is a set of N+1 Bernstein polynomials,
#    each of degree N, which form a basis for polynomials on [0,1].
#
#    real X, the evaluation point.
#
#    real BERN[0:N], the values of the N+1 Bernstein polynomials at X.
#
  import numpy as np

  bern = np.zeros ( n + 1 );

  if ( n == 0 ):
 
    bern[0] = 1.0
 
  else:
 
    bern[0] = 1.0 - x
    bern[1] = x
 
    for i in range ( 2, n + 1 ):
      bern[i] = x * bern[i-1]
      for j in range ( i - 1, 0, -1 ):
        bern[j] = x * bern[j-1] + ( 1.0 - x ) * bern[j]
      bern[0] = ( 1.0 - x ) * bern[0]

  return bern

def bernstein_poly_test ( ):

#*****************************************************************************80
#
## bernstein_poly_test() tests bernstein_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bernstein_poly_test():' )
  print ( '  bernstein_poly() computes Bernstein polynomials;' )
  print ( '' )
  print ( '   N   K    X             Exact         B(N,K)(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, k, x, b = bernstein_poly_01_values ( n_data )

    if ( n_data == 0 ):
      break

    bvec = bernstein_poly ( n, x )

    print ( '  %2d  %2d  %5g  %12g  %12g' % ( n, k, x, b, bvec[k] ) )

  return

def beta_values ( n_data ):

#*****************************************************************************80
#
## beta_values() returns some values of the Beta function.
#
#  Discussion:
#
#    Beta(X,Y) = ( Gamma(X) * Gamma(Y) ) / Gamma(X+Y)
#
#    Both X and Y must be greater than 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      Beta[X,Y]
#
#  Properties:
#
#    Beta(X,Y) = Beta(Y,X).
#    Beta(X,Y) = Integral ( 0 <= T <= 1 ) T^(X-1) (1-T)^(Y-1) dT.
#    Beta(X,Y) = Gamma(X) * Gamma(Y) / Gamma(X+Y)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, Y, the arguments of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 17

  f_vec = np.array ( ( \
     0.5000000000000000E+01, \
     0.2500000000000000E+01, \
     0.1666666666666667E+01, \
     0.1250000000000000E+01, \
     0.5000000000000000E+01, \
     0.2500000000000000E+01, \
     0.1000000000000000E+01, \
     0.1666666666666667E+00, \
     0.3333333333333333E-01, \
     0.7142857142857143E-02, \
     0.1587301587301587E-02, \
     0.2380952380952381E-01, \
     0.5952380952380952E-02, \
     0.1984126984126984E-02, \
     0.7936507936507937E-03, \
     0.3607503607503608E-03, \
     0.8325008325008325E-04 ) )

  x_vec = np.array ( ( \
     0.2E+00, \
     0.4E+00, \
     0.6E+00, \
     0.8E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     5.0E+00, \
     6.0E+00, \
     6.0E+00, \
     6.0E+00, \
     6.0E+00, \
     6.0E+00, \
     7.0E+00  ) )

  y_vec = np.array ( ( \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     0.2E+00, \
     0.4E+00, \
     1.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     5.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     5.0E+00, \
     6.0E+00, \
     7.0E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    y = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    y = y_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, y, f

def beta_values_test ( ):

#*****************************************************************************80
#
## beta_values_test() tests beta_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'beta_values_test():' )
  print ( '  beta_values() stores values of the Beta function.' )
  print ( '' )
  print ( '      X         Y         Beta(X,Y)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, y, f = beta_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( x, y, f ) )

  return

def bpab ( n, x, a, b ):

#*****************************************************************************80
#
## bpab() evaluates at X the Bernstein polynomials based in [A,B].
#
#  Formula:
#
#    BERN(N,I)(X) = [N!/(I!*(N-I)!)] * (B-X)^(N-I) * (X-A)^I / (B-A)^N
#
#  First values:
#
#    B(0,0)(X) =   1
#
#    B(1,0)(X) = (      B-X              ) / (B-A)
#    B(1,1)(X) = (                X-A    ) / (B-A)
#
#    B(2,0)(X) = (     (B-X)^2           ) / (B-A)^2
#    B(2,1)(X) = ( 2 * (B-X)   * (X-A)   ) / (B-A)^2
#    B(2,2)(X) = (               (X-A)^2 ) / (B-A)^2
#
#    B(3,0)(X) = (     (B-X)^3           ) / (B-A)^3
#    B(3,1)(X) = ( 3 * (B-X)^2 * (X-A)   ) / (B-A)^3
#    B(3,2)(X) = ( 3 * (B-X)   * (X-A)^2 ) / (B-A)^3
#    B(3,3)(X) = (               (X-A)^3 ) / (B-A)^3
#
#    B(4,0)(X) = (     (B-X)^4           ) / (B-A)^4
#    B(4,1)(X) = ( 4 * (B-X)^3 * (X-A)   ) / (B-A)^4
#    B(4,2)(X) = ( 6 * (B-X)^2 * (X-A)^2 ) / (B-A)^4
#    B(4,3)(X) = ( 4 * (B-X)   * (X-A)^3 ) / (B-A)^4
#    B(4,4)(X) = (               (X-A)^4 ) / (B-A)^4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the degree of the Bernstein polynomials to be used.
#    For any N, there is a set of N+1 Bernstein polynomials, each of
#    degree N, which form a basis for polynomials on [A,B].
#
#    real X, the point at which the polynomials are to be evaluated.
#
#    real A, B, the endpoints of the interval on which the
#    polynomials are to be based.  A and B should not be equal.
#
#    real BERN(0:N), the values of the N+1 Bernstein polynomials at X.
#
  import numpy as np

  if ( b == a ):
    print ( '' )
    print ( 'bpab(): Fatal error!' )
    print ( '  A = B = %f' % ( a ) )
    raise Exception ( 'bpab(): Fatal error!' )

  bern = np.zeros ( n + 1 )

  if ( n == 0 ):
 
    bern[0] = 1.0;
 
  else:
 
    bern[0] = ( b - x ) / ( b - a );
    bern[1] = ( x - a ) / ( b - a );
 
    for i in range ( 1, n ):
      bern[i+1] = ( x - a ) * bern[i] / ( b - a )
      for j in range ( i - 1, -1, -1 ):
        bern[j+1] = ( ( b - x ) * bern[j+1] + ( x - a ) * bern[j] ) / ( b - a )
      bern[0] = ( b - x ) * bern[0] / ( b - a )

  return bern

def bpab_test ( ):

#*****************************************************************************80
#
## bpab_test() tests bpab().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2015
#
#  Author:
#
#    John Burkardt
#
  n = 10
  x = 0.3
  a = 0.0
  b = 1.0
  bern = bpab ( n, x, a, b )

  print ( '' )
  print ( 'bpab_test():' )
  print ( '  bpab() computes Bernstein polynomials;' )
  print ( '' )
  print ( '  The Bernstein polynomials of degree %d' % ( n ) )
  print ( '  based on the interval [%f,%f]' % ( a, b ) )
  print ( '  evaluated at X = %g' % ( x ) )
  print ( '' )
  print ( '   I        Bern(I,X)' )
  print ( '' )
  
  for i in range ( 0, n + 1 ):
    print ( '  %2d  %12g' % ( i, bern[i] ) )

  return

def cardan_poly_coef ( n, s ):

#*****************************************************************************80
#
## cardan_poly_coef() computes the coefficients of the N-th Cardan polynomial.
#
#  First terms:
#
#    2
#    0       1
#   -2 S     0      1
#    0      -3 S    0      1
#    2 S^2   0     -4 S    0      1
#    0       5 S^2  0     -5 S    0       1
#   -2 S^3   0      9 S^2  0     -6 S     0       1
#    0       7 S^3  0     14 S^2  0      -7 S     0       1
#    2 S^4   0    -16 S^3  0     20 S^2   0      -8 S     0        1
#    0       9 S^4  0    -30 S^3  0      27 S^2   0      -9 S      0     1
#   -2 S^5   0     25 S^4  0    -50 S^3   0      35 S^2   0      -10 S   0   1
#    0     -11 S^5  0     55 S^4  0     -77 S^3   0     +44 S^2    0   -11 S 0 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Thomas Osler,
#    Cardan Polynomials and the Reduction of Radicals,
#    Mathematics Magazine, 
#    Volume 74, Number 1, February 2001, pages 26-32.
#
#  Input:
#
#    integer N, the order of the polynomial
#
#    real S, the value of the parameter, which must be positive.
#
#    real C(1:N+1), the coefficients.  C(1) is the constant term,
#    and C(N+1) is the coefficient of X^N.
#
  import numpy as np

  c = np.zeros ( n + 1 )

  if ( n < 0 ):
    return c
 
  c[0] = 2.0

  if ( n == 0 ):
    return c

  cm1 = np.zeros ( n + 1 )
  cm2 = np.zeros ( n )

  for i in range ( 0, n + 1 ):
    cm1[i] = c[i]

  c[0] = 0.0
  c[1] = 1.0

  for i in range ( 1, n ):

    for j in range ( 0, i ):
      cm2[j] = cm1[j]
    for j in range ( 0, i + 1 ):
      cm1[j] = c[j]

    c[0] = 0.0
    for j in range ( 1, i + 2 ):
      c[j] = cm1[j-1]
    for j in range ( 0, i ):
      c[j] = c[j] - s * cm2[j]

  return c

def cardan_poly_coef_test ( ):

#*****************************************************************************80
#
## cardan_poly_coef_test() tests cardan_poly_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  n_max = 10
  s = 1.0

  print ( '' )
  print ( 'cardan_poly_coef_test():' )
  print ( '  cardan_poly_coef() returns the coefficients of a Cardan polynomial.' )
  print ( '' )
  print ( '  We use the parameter S = %g' % ( s ) )
  print ( '' )
  print ( '  Table of polyomial coefficients:' )
  print ( '' )

  for n in range ( 0, n_max + 1 ):

    c = cardan_poly_coef ( n, s )
    print ( '  %2d:  ' % ( n ) ),
    for i in range ( 0, n + 1 ):
      print ( '  %9f' % ( c[i] ) ),
    print ( '' )

  return

def cardan_poly ( n, x, s ):

#*****************************************************************************80
#
## cardan_poly() evaluates the Cardan polynomials.
#
#  First terms:
#
#     N  C(N,S,X)
#
#     0  2
#     1  X
#     2  X^2  -  2 S
#     3  X^3  -  3 S X
#     4  X^4  -  4 S X^2 +  2 S^2
#     5  X^5  -  5 S X^3 +  5 S^2 X
#     6  X^6  -  6 S X^4 +  9 S^2 X^2 -  2 S^3
#     7  X^7  -  7 S X^5 + 14 S^2 X^3 -  7 S^3 X
#     8  X^8  -  8 S X^6 + 20 S^2 X^4 - 16 S^3 X^2 +  2 S^4
#     9  X^9  -  9 S X^7 + 27 S^2 X^5 - 30 S^3 X^3 +  9 S^4 X
#    10  X^10 - 10 S X^8 + 35 S^2 X^6 - 50 S^3 X^4 + 25 S^4 X^2 -  2 S^5
#    11  X^11 - 11 S X^9 + 44 S^2 X^7 - 77 S^3 X^5 + 55 S^4 X^3 - 11 S^5 X
#
#  Recursion:
#
#    Writing the N-th polynomial in terms of its coefficients:
#
#      C(N,S,X) = sum ( 0 <= I <= N ) D(N,I) * S^(N-I)/2 * X^I
#
#    then
#
#    D(0,0) = 1
#
#    D(1,1) = 1
#    D(1,0) = 0
#
#    D(N,N) = 1
#    D(N,K) = D(N-1,K-1) - D(N-2,K)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Thomas Osler,
#    Cardan Polynomials and the Reduction of Radicals,
#    Mathematics Magazine, 
#    Volume 74, Number 1, February 2001, pages 26-32.
#
#  Input:
#
#    integer N, the highest polynomial to compute.
#
#    real X, the point at which the polynomials are to be computed.
#
#    real S, the value of the parameter, which must be positive.
#
#    real CX(0:N), the values of the Cardan polynomials at X.
#
  import numpy as np

  s2 = np.sqrt ( s )
  xvec = np.zeros ( 1 )
  xvec[0] = 0.5 * x / s2
#
#  This returns a 1xN matrix!
#
  cmat = cheby_t_poly ( 1, n, xvec )

  cx = np.zeros ( n + 1 );

  fact = 1.0

  for i in range ( 0, n + 1 ):
    cx[i] = 2.0 * fact * cmat[0,i]
    fact = fact * s2

  return cx

def cardan_poly_test ( ):

#*****************************************************************************80
#
## cardan_poly_test() tests cardan_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
  n_max = 10
  s = 0.5
  x = 0.25

  print ( '' )
  print ( 'cardan_poly_test():' )
  print ( '  cardan_poly() evaluates a Cardan polynomial directly.' )
  print ( '' )
  print ( '  Compare cardan_poly_coef() + r8poly_value_horner()' )
  print ( '  versus cardan_poly() alone.' )
  print ( '' )
  print ( '  Evaluate polynomials at X = %f' % ( x ) )
  print ( '  We use the parameter S = %f' % ( s ) )
  print ( '' )
  print ( '  Order    Horner       Direct' )
  print ( '' )

  cx2 = cardan_poly ( n_max, x, s )

  for n in range ( 0, n_max + 1 ):

    c = cardan_poly_coef ( n, s )
    cx1 = r8poly_value_horner ( n, c, x )

    print ( '  %2d  %12g  %12g' % ( n, cx1, cx2[n] ) )

  return

def cardinal_cos ( j, m, n, t ):

#*****************************************************************************80
#
## cardinal_cos() evaluates the J-th cardinal cosine basis function.
#
#  Discussion:
#
#    The base points are T(I) = pi * I / ( M + 1 ), 0 <= I <= M + 1.
#    Basis function J is 1 at T(J), and 0 at T(I) for I /= J
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Boyd,
#    Exponentially convergent Fourier-Chebyshev quadrature schemes on
#    bounded and infinite intervals,
#    Journal of Scientific Computing,
#    Volume 2, Number 2, 1987, pages 99-109.
#
#  Input:
#
#    integer J, the index of the basis function.
#    0 <= J <= M + 1.
#
#    integer M, indicates the size of the basis set.
#
#    integer N, the number of sample points.
#
#    real T(N), one or more points in [0,pi] where the
#    basis function is to be evaluated.
#
#    real C(N), the value of the function at T.
#
  import numpy as np

  epsilon = np.finfo(float).eps

  if ( ( j % ( m + 1 ) ) == 0 ):
    cj = 2.0
  else:
    cj = 1.0

  tj = np.pi * float ( j ) / float ( m + 1 )

  c = np.zeros ( n )

  for i in range ( 0, n ):
    if ( abs ( t[i] - tj ) < 5.0 * epsilon ):
      c[i] = 1.0
    else:
      c[i] = r8_mop ( ( j + 1 ) % 2 ) * np.sin ( t[i] ) * np.sin ( ( m + 1 ) * t[i] ) \
        / cj / ( m + 1 ) / ( np.cos ( t[i] ) - np.cos ( tj ) )

  return c

def cardinal_cos_test ( ):

#*****************************************************************************80
#
## cardinal_cos_test() tests cardinal_cos().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'cardinal_cos_test():' )
  print ( '  cardinal_cos() evaluates cardinal cosine functions.' )
  print ( '  Ci(Tj) = Delta(i,j), where Tj = cos(pi*i/(n+1)).' )
  print ( '  A simple check of all pairs should form the identity matrix.' )

  print ( '' )
  print ( '  The cardinal_cos test matrix:' )
  print ( '' )

  m = 11
  n = m + 2
  c = np.zeros ( [ m + 2, n ] )
  t_lo = 0.0
  t_hi = np.pi
  t = np.linspace ( t_lo, t_hi, n )
 
  for j in range ( 0, m + 2 ):
    v = cardinal_cos ( j, m, n, t )
    for i in range ( 0, n ):
      c[i,j] = v[i]

  for i in range ( 0, n ):
    for j in range ( 0, m + 2 ):
      print ( '  %5.2f' % ( c[i,j] ) ),
    print ( '' )

  return

def cardinal_sin ( j, m, n, t ):

#*****************************************************************************80
#
## cardinal_sin() evaluates the J-th cardinal sine basis function.
#
#  Discussion:
#
#    The base points are T(I) = pi * I / ( M + 1 ), 0 <= I <= M + 1.
#    Basis function J is 1 at T(J), and 0 at T(I) for I /= J
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Boyd,
#    Exponentially convergent Fourier-Chebyshev quadrature schemes on
#    bounded and infinite intervals,
#    Journal of Scientific Computing,
#    Volume 2, Number 2, 1987, pages 99-109.
#
#  Input:
#
#    integer J, the index of the basis function.
#    0 <= J <= M + 1.
#
#    integer M, indicates the size of the basis set.
#
#    integer N, the number of evaluation points.
#
#    real T(N), one or more points in [0,pi] where the
#    basis function is to be evaluated.
#
#    real S(N), the value of the function at T.
#
  import numpy as np

  epsilon = np.finfo(float).eps

  tj = np.pi * float ( j ) / float ( m + 1 )

  s = np.zeros ( n )

  for i in range ( 0, n ):
    if ( abs ( t[i] - tj ) < 5.0 * epsilon ):
      s[i] = 1.0
    else:
      s[i] = r8_mop ( ( j + 1 ) % 2 ) * np.sin ( t[i] ) * np.sin ( ( m + 1 ) * t[i] ) \
        / ( m + 1 ) / ( np.cos ( t[i] ) - np.cos ( tj ) )

  return s

def cardinal_sin_test ( ):

#*****************************************************************************80
#
## cardinal_sin_test() tests cardinal_sin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'cardinal_sin_test():' )
  print ( '  cardinal_sin() evaluates cardinal sine functions.' )
  print ( '  Si(Tj) = Delta(i,j), where Tj = cos(pi*i/(n+1)).' )
  print ( '  A simple check of all pairs should form the identity matrix.' )

  print ( '' )
  print ( '  The cardinal_sin test matrix:' )
  print ( '' )

  m = 11
  n = m + 2
  s = np.zeros ( [ m + 2, n ] )
  t_lo = 0.0
  t_hi = np.pi
  t = np.linspace ( t_lo, t_hi, n )
 
  for j in range ( 0, m + 2 ):
    v = cardinal_sin ( j, m, n, t )
    for i in range ( 0, n ):
      s[i,j] = v[i]

  for i in range ( 0, n ):
    for j in range ( 0, m + 2 ):
      print ( '  %5.2f' % ( s[i,j] ) ),
    print ( '' )

  return

def charlier ( n, a, x ):

#*****************************************************************************80
#
## charlier() evaluates Charlier polynomials at a point.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    J Simoes Pereira,
#    Algorithm 234: Poisson-Charliers Polynomials,
#    Communications of the ACM,
#    Volume 7, Number 7, page 420, July 1964.
#
#    Walter Gautschi,
#    Orthogonal Polynomials: Computation and Approximation,
#    Oxford, 2004,
#    ISBN: 0-19-850672-4,
#    LC: QA404.5 G3555.
#
#    Gabor Szego,
#    Orthogonal Polynomials,
#    American Mathematical Society, 1975,
#    ISBN: 0821810235,
#    LC: QA3.A5.v23.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 2002,
#    Second edition,
#    ISBN: 1584883472,
#    LC: QA5.W45.
#
#  Input:
#
#    integer N, the maximum order of the polynomial.  
#    N must be at least 0.
#
#    real A, the parameter.  A must not be 0.
#
#    real X, the evaluation point.
#
#    real V(0:N), the value of the polynomials at X.
#
  import numpy as np

  if ( a == 0.0 ):
    print ( '' )
    print ( 'charlier(): Fatal error!' )
    print ( '  Parameter A cannot be zero.' )
    raise Exception ( 'charlier(): Fatal error!' );

  if ( n < 0 ):
    print ( '' )
    print ( 'charlier(): Fatal error!' )
    print ( '  Parameter N must be nonnegative.' )
    raise Exception ( 'charlier(): Fatal error!' );

  v = np.zeros ( n + 1 )

  v[0] = 1.0

  if ( 0 < n ):
 
    v[1] = - x / a

    if ( 1 < n ):

      for i in range ( 2, n + 1 ):
        v[i] = ( ( i - 1 + a - x ) * v[i-1] - ( i - 1 ) * v[i-2] ) / a
 
  return v

def charlier_test ( ):

#*****************************************************************************80
#
## charlier_test() tests charlier().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 5
  a_test = np.array ( [ 0.25, 0.5, 1.0, 2.0, 10.0 ] )
  n = 5

  print ( '' )
  print ( 'charlier_test():' )
  print ( '  charlier() evaluates Charlier polynomials.' )
  print ( '' )
  print ( '       N      A         X        P(N,A,X)' )

  for test in range ( 0, test_num ):

    n = 5
    a = a_test[test]

    for j in range ( 0, 6 ):

      x = j / 2.0

      value = charlier ( n, a, x )

      print ( '' )

      for i in range ( 0, n + 1 ):

        print ( '  %8d  %8f  %8f  %14f' % ( i, a, x, value[i] ) )

  return

def chebyshev_discrete ( n, m, x ):

#*****************************************************************************80
#
## chebyshev_discrete() evaluates discrete Chebyshev polynomials at a point.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Walter Gautschi,
#    Orthogonal Polynomials: Computation and Approximation,
#    Oxford, 2004,
#    ISBN: 0-19-850672-4,
#    LC: QA404.5 G3555.
#
#  Input:
#
#    integer N, the highest order of the polynomials to be evaluated.
#    0 <= N <= M.
#
#    integer M, the maximum order of the polynomials.
#    0 <= M.
#
#    real X, the evaluation point.
#
#    real V(N+1), the value of the polynomials at X.
#
  import numpy as np

  if ( m < 0 ):
    print ( '' )
    print ( 'chebyshev_discrete(): Fatal error!' )
    print ( '  Parameter M must be nonnegative.' )
    raise Exception ( 'chebyshev_discrete(): Fatal error!');

  if ( n < 0 ):
    print ( '' )
    print ( 'chebyshev_discrete(): Fatal error!' )
    print ( '  Parameter N must be nonnegative.' )
    raise Exception ( 'chebyshev_discrete(): Fatal error!');

  if ( m < n ):
    print ( '' )
    print ( 'chebyshev_discrete(): Fatal error!' )
    print ( '  Parameter N must be no greater than M.' )
    raise Exception ( 'chebyshev_discrete(): Fatal error!');
 
  v = np.zeros ( n + 1 )

  v[0] = 1.0

  if ( 0 < n ):

    v[1] = 2.0 * x + 1 - m

    if ( 1 < n ):

      for i in range ( 1, n ):
        v[i+1] = ( \
          ( 2 * i + 1 ) * ( 2.0 * x + 1 - m ) * v[i] \
          - i * ( m + i ) * ( m - i ) * v[i-1] \
        ) / ( i + 1 )

  return v

def chebyshev_discrete_test ( ):

#*****************************************************************************80
#
## chebyshev_discrete_test() tests chebyshev_discrete().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  print ( '' )
  print ( 'chebyshev_discrete_test():' )
  print ( '  cheby_discrete evaluates the discrete Chebyshev polynomial.' )
  print ( '' )
  print ( '       N      M         X        T(N,M,X)' )
  print ( '' )

  n = 5
  m = 5

  for j in range ( 0, 6 ):

    x = j / 2.0

    value = chebyshev_discrete ( n, m, x )

    print ( '' )

    for i in range ( 0, n + 1 ): 

      print ( '  %8d  %8d  %12g  %12g' % ( i, m, x, value[i] ) )

  return

def cheby_t_poly_coef ( n ):

#*****************************************************************************80
#
## cheby_t_poly_coef() evaluates coefficients of Chebyshev polynomials T(n,x).
#
#  First terms:
#
#    N/K     0     1      2      3       4     5      6    7      8    9   10
#
#     0      1
#     1      0     1
#     2     -1     0      2
#     3      0    -3      0      4
#     4      1     0     -8      0       8
#     5      0     5      0    -20       0    16
#     6     -1     0     18      0     -48     0     32
#     7      0    -7      0     56       0  -112      0    64
#
#  Recursion:
#
#    T(0)(X) = 1,
#    T(1)(X) = X,
#    T(N)(X) = 2 * X * T(N-1)(X) - T(N-2)(X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    real C[0:N,0:N], the coefficients of the Chebyshev T
#    polynomials.
#
  import numpy as np

  c = np.zeros ( [ n + 1, n + 1 ] )
 
  c[0,0] = 1.0

  if ( 0 < n ):
 
    c[1,1] = 1.0
 
    for i in range ( 1, n ):
      c[i+1,0] = - c[i-1,0]
      for j in range ( 1, i ):
        c[i+1,j] = 2.0 * c[i,j-1] - c[i-1,j]
      c[i+1,  i  ] = 2.0 * c[i,  i-1]
      c[i+1,  i+1] = 2.0 * c[i,  i  ]

  return c

def cheby_t_poly_coef_test ( ):

#*****************************************************************************80
#
## cheby_t_poly_coef_test() tests cheby_t_poly_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'cheby_t_poly_coef_test():' )
  print ( '  cheby_t_poly_coef determines the Chebyshev T' )
  print ( '  polynomial coefficients.' )

  c = cheby_t_poly_coef ( n )
 
  for i in range ( 0, n + 1 ):
    print ( '' )
    print ( '  T(%d)' % ( i ) )
    print ( '' )
    for j in range ( i, -1, -1 ):
      if ( j == 0 ):
        print ( '    %f' % ( c[i,j] ) )
      elif ( j == 1 ):
        print ( '    %f * x' % ( c[i,j] ) )
      else:
        print ( '    %f * x^%d' % ( c[i,j], j ) )

  return

def cheby_t_poly ( m, n, x ):

#*****************************************************************************80
#
## cheby_t_poly() evaluates Chebyshev polynomials T(n,x).
#
#  Discussion:
#
#    Chebyshev polynomials are useful as a basis for representing the
#    approximation of functions since they are well conditioned, in the sense
#    that in the interval [-1,1] they each have maximum absolute value 1.
#    Hence an error in the value of a coefficient of the approximation, of
#    size epsilon, is exactly reflected in an error of size epsilon between
#    the computed approximation and the theoretical approximation.
#
#    Typical usage is as follows, where we assume for the moment
#    that the interval of approximation is [-1,1].  The value
#    of N is chosen, the highest polynomial to be used in the
#    approximation.  Then the function to be approximated is
#    evaluated at the N+1 points XJ which are the zeroes of the N+1-th
#    Chebyshev polynomial.  Let these values be denoted by F(XJ).
#
#    The coefficients of the approximation are now defined by
#
#      C(I) = 2/(N+1) * sum ( 1 <= J <= N+1 ) F(XJ) T(I,XJ)
#
#    except that C(0) is given a value which is half that assigned
#    to it by the above formula,
#
#    and the representation is
#
#    F(X) approximated by sum ( 0 <= J <= N ) C(J) T(J,X)
#
#    Now note that, again because of the fact that the Chebyshev polynomials
#    have maximum absolute value 1, if the higher order terms of the
#    coefficients C are small, then we have the option of truncating
#    the approximation by dropping these terms, and we will have an
#    exact value for maximum perturbation to the approximation that
#    this will cause.
#
#    It should be noted that typically the error in approximation
#    is dominated by the first neglected basis function (some multiple of
#    T(N+1,X) in the example above).  If this term were the exact error,
#    then we would have found the minimax polynomial, the approximating
#    polynomial of smallest maximum deviation from the original function.
#    The minimax polynomial is hard to compute, and another important
#    feature of the Chebyshev approximation is that it tends to behave
#    like the minimax polynomial while being easy to compute.
#
#    To evaluate a sum like 
#
#      sum ( 0 <= J <= N ) C(J) T(J,X), 
#
#    Clenshaw's recurrence formula is recommended instead of computing the
#    polynomial values, forming the products and summing.
#
#    Assuming that the coefficients C(J) have been computed
#    for J = 0 to N, then the coefficients of the representation of the
#    indefinite integral of the function may be computed by
#
#      B(I) = ( C(I-1) - C(I+1))/2*(I-1) for I=1 to N+1, 
#
#    with
# 
#      C(N+1)=0
#      B(0) arbitrary.  
#
#    Also, the coefficients of the representation of the derivative of the 
#    function may be computed by:
#
#      D(I) = D(I+2)+2*I*C(I) for I=N-1, N-2, ..., 0, 
#
#    with
#
#      D(N+1) = D(N)=0.
#
#    Some of the above may have to adjusted because of the irregularity of C(0).
#
#  Differential equation:
#
#    (1-X*X) Y'' - X Y' + N N Y = 0
#
#  Formula:
#
#    T(N,X) = COS(N*ARCCOS(X))
#
#  First terms:
#
#    T(0,X) =  1
#    T(1,X) =  1 X
#    T(2,X) =  2 X^2 -   1
#    T(3,X) =  4 X^3 -   3 X
#    T(4,X) =  8 X^4 -   8 X^2 +  1
#    T(5,X) = 16 X^5 -  20 X^3 +  5 X
#    T(6,X) = 32 X^6 -  48 X^4 + 18 X^2 - 1
#    T(7,X) = 64 X^7 - 112 X^5 + 56 X^3 - 7 X
#
#  Inequality:
#
#    abs ( T(N,X) ) <= 1 for -1 <= X <= 1
#
#  Orthogonality:
#
#    For integration over [-1,1] with weight
#
#      W(X) = 1 / sqrt(1-X*X), 
#
#    if we write the inner product of T(I,X) and T(J,X) as
#
#      < T(I,X), T(J,X) > = integral ( -1 <= X <= 1 ) W(X) T(I,X) T(J,X) dX
#
#    then the result is:
#
#      0 if I /= J
#      PI/2 if I == J /= 0
#      PI if I == J == 0
#
#    A discrete orthogonality relation is also satisfied at each of
#    the N zeroes of T(N,X):  sum ( 1 <= K <= N ) T(I,X) * T(J,X)
#                              = 0 if I /= J
#                              = N/2 if I == J /= 0
#                              = N if I == J == 0
#
#  Recursion:
#
#    T(0,X) = 1,
#    T(1,X) = X,
#    T(N,X) = 2 * X * T(N-1,X) - T(N-2,X)
#
#    T'(N,X) = N * ( -X * T(N,X) + T(N-1,X) ) / ( 1 - X^2 )
#
#  Special values:
#
#    T(N,1) = 1
#    T(N,-1) = (-1)^N
#    T(2N,0) = (-1)^N
#    T(2N+1,0) = 0
#    T(N,X) = (-1)^N * T(N,-X)
#
#  Zeroes:
#
#    M-th zero of T(N,X) is cos((2*M-1)*PI/(2*N)), M = 1 to N
#
#  Extrema:
#
#    M-th extremum of T(N,X) is cos(PI*M/N), M = 0 to N
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest polynomial to compute.
#
#    real X(M), the evaluation points.
#
#    real V(M,N+1), the values of the Chebyshev polynomials 
#    0 through N at X(1:M).
#
  import numpy as np
 
  v = np.zeros ( [ m, n + 1 ] )

  for i in range ( 0, m ):
    v[i,0] = 1.0
 
  if ( n < 1 ):
    return v

  for i in range ( 0, m ):
    v[i,1] = x[i]
 
  for j in range ( 1, n ):
    for i in range ( 0, m ):
      v[i,j+1] = 2.0 * x[i] * v[i,j] - v[i,j-1]
  
  return v

def cheby_t_poly_test ( ):

#*****************************************************************************80
#
## cheby_t_poly_test() tests cheby_t_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n_max = 12
  xv = np.zeros ( 1 )

  print ( '' )
  print ( 'cheby_t_poly_test():' )
  print ( '  cheby_t_poly() evaluates the Chebyshev T polynomial.' )
  print ( '' )
  print ( '     N      X        Exact F       T(N)(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    [ n_data, n, x, fx ] = cheby_t_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    m = 1
    xv[0] = x
    v = cheby_t_poly ( m, n, xv )
    fx2 = v[0,n]

    print ( '  %6d  %8g  %12g  %12g' % ( n, x, fx, fx2 ) )

  return

def cheby_t_poly_values ( n_data ):

#*****************************************************************************80
#
## cheby_t_poly_values() returns values of Chebyshev polynomials T(n,x).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ChebyshevT[n,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  n_max = 13;

  fx_vec = [ \
 ];

  n_vec = [ \
 ];

  x_vec = [ \
 ];

  import numpy as np

  n_max = 13

  fx_vec = np.array ( ( \
      0.1000000000000000E+01, \
      0.8000000000000000E+00, \
      0.2800000000000000E+00, \
     -0.3520000000000000E+00, \
     -0.8432000000000000E+00, \
     -0.9971200000000000E+00, \
     -0.7521920000000000E+00, \
     -0.2063872000000000E+00, \
      0.4219724800000000E+00, \
      0.8815431680000000E+00, \
      0.9884965888000000E+00, \
      0.7000513740800000E+00, \
      0.1315856097280000E+00 ) )

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12 ))

  x_vec = np.array ( ( \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def cheby_t_poly_values_test ( ):

#*****************************************************************************80
#
## cheby_t_poly_values_test() tests cheby_t_poly_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cheby_t_poly_values_test():' )
  print ( '  cheby_t_poly_values() stores values of the Bernoulli polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = cheby_t_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )

  return

def cheby_t_poly_zero ( n ):

#*****************************************************************************80
#
## cheby_t_poly_zero() returns zeroes of Chebyshev polynomials T(n,x).
#
#  Discussion:
#
#    The I-th zero of T(n,x) is cos((2*I-1)*PI/(2*N)), I = 1 to N
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#    real Z(N), the zeroes of T(N)(X).
#
  import numpy as np

  z = np.zeros ( n )

  for i in range ( 0, n ):
    angle = ( 2 * i + 1 ) * np.pi / float ( 2 * n )
    z[i] = np.cos ( angle )

  return z

def cheby_t_poly_zero_test ( ):

#*****************************************************************************80
#
## cheby_t_poly_zero_test() tests cheby_t_poly_zero().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n_max = 4

  print ( '' )
  print ( 'cheby_t_poly_zero_test():' )
  print ( '  cheby_t_poly_zero() returns zeroes of T(N,X).' )
  print ( '' )
  print ( '         N         X        T(N,X)' )
  print ( '' )

  for n in range ( 1, n_max + 1 ):

    z = cheby_t_poly_zero ( n )

    fx = cheby_t_poly ( n, n, z )

    for i in range ( 0, n ):
      print ( '  %8d  %11g  %14g' % ( n, z[i], fx[i,n] ) )

    print ( '' )

  return

def cheby_u_poly_coef ( n ):

#*****************************************************************************80
#
## cheby_u_poly_coef() evaluates coefficients of Chebyshev polynomials U(n,x).
#
#  First terms:
#
#    N/K     0     1      2      3       4     5      6    7      8    9   10
#
#     0      1
#     1      0     2
#     2     -1     0      4
#     3      0    -4      0      8
#     4      1     0    -12      0      16
#     5      0     6      0    -32       0    32
#     6     -1     0     24      0     -80     0     64
#     7      0    -8      0     80       0  -192      0   128
#
#  Recursion:
#
#    U(0)(X) = 1,
#    U(1)(X) = 2 * X,
#    U(N)(X) = 2 * X * U(N-1)(X) - U(N-2)(X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    real C[0:N,0:N], the coefficients of the Chebyshev T
#    polynomials.
#
  import numpy as np

  c = np.zeros ( [ n + 1, n + 1 ] )
 
  c[0,0] = 1.0

  if ( 0 < n ):
 
    c[1,1] = 2.0
 
    for i in range ( 1, n ):
      c[i+1,0] = - c[i-1,0]
      for j in range ( 1, i ):
        c[i+1,j] = 2.0 * c[i,j-1] - c[i-1,j]
      c[i+1,  i  ] = 2.0 * c[i,  i-1]
      c[i+1,  i+1] = 2.0 * c[i,  i  ]

  return c

def cheby_u_poly_coef_test ( ):

#*****************************************************************************80
#
## cheby_u_poly_coef_test() tests cheby_u_poly_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'cheby_u_poly_coef_test():' )
  print ( '  cheby_u_poly_coef() determines the Chebyshev U' )
  print ( '  polynomial coefficients.' )

  c = cheby_u_poly_coef ( n )
 
  for i in range ( 0, n + 1 ):
    print ( '' )
    print ( '  U(%d)' % ( i ) )
    print ( '' )
    for j in range ( i, -1, -1 ):
      if ( j == 0 ):
        print ( '    %f' % ( c[i,j] ) )
      elif ( j == 1 ):
        print ( '    %f * x' % ( c[i,j] ) )
      else:
        print ( '    %f * x^%d' % ( c[i,j], j ) )

  return

def cheby_u_poly ( m, n, x ):

#*****************************************************************************80
#
## cheby_u_poly() evaluates Chebyshev polynomials U(n,x).
#
#  Differential equation:
#
#    (1-X*X) Y'' - 3 X Y' + N (N+2) Y = 0
#
#  First terms:
#
#    U(0,X) =   1
#    U(1,X) =   2 X
#    U(2,X) =   4 X^2 -   1
#    U(3,X) =   8 X^3 -   4 X
#    U(4,X) =  16 X^4 -  12 X^2 +  1
#    U(5,X) =  32 X^5 -  32 X^3 +  6 X
#    U(6,X) =  64 X^6 -  80 X^4 + 24 X^2 - 1
#    U(7,X) = 128 X^7 - 192 X^5 + 80 X^3 - 8X
#
#  Recursion:
#
#    U(0,X) = 1,
#    U(1,X) = 2 * X,
#    U(N,X) = 2 * X * U(N-1,X) - U(N-2,X)
#
#  Norm:
#
#    Integral ( -1 <= X <= 1 ) ( 1 - X^2 ) * U(N,X)^2 dX = PI/2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest polynomial to compute.
#
#    real X(M), the evaluation points.
#
#    real V(M,N+1), the values of the Chebyshev polynomials 
#    0 through N at X(1:M).
#
  import numpy as np
 
  v = np.zeros ( [ m, n + 1 ] )

  for i in range ( 0, m ):
    v[i,0] = 1.0
 
  if ( n < 1 ):
    return v

  for i in range ( 0, m ):
    v[i,1] = 2.0 * x[i]
 
  for j in range ( 1, n ):
    for i in range ( 0, m ):
      v[i,j+1] = 2.0 * x[i] * v[i,j] - v[i,j-1]
  
  return v

def cheby_u_poly_test ( ):

#*****************************************************************************80
#
## cheby_u_poly_test() tests cheby_u_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n_max = 12
  xv = np.zeros ( 1 )

  print ( '' )
  print ( 'cheby_u_poly_test():' )
  print ( '  cheby_u_poly() evaluates the Chebyshev U polynomial.' )
  print ( '' )
  print ( '     N      X        Exact F       U(N)(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    [ n_data, n, x, fx ] = cheby_u_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    m = 1
    xv[0] = x
    v = cheby_u_poly ( m, n, xv )
    fx2 = v[0,n]

    print ( '  %6d  %8g  %12g  %12g' % ( n, x, fx, fx2 ) )

  return

def cheby_u_poly_values ( n_data ):

#*****************************************************************************80
#
## cheby_u_poly_values() returns values of Chebyshev polynomials U(n,x).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ChebyshevU[n,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 13

  fx_vec = np.array ( ( \
      0.1000000000000000E+01, \
      0.1600000000000000E+01, \
      0.1560000000000000E+01, \
      0.8960000000000000E+00, \
     -0.1264000000000000E+00, \
     -0.1098240000000000E+01, \
     -0.1630784000000000E+01, \
     -0.1511014400000000E+01, \
     -0.7868390400000000E+00, \
      0.2520719360000000E+00, \
      0.1190154137600000E+01, \
      0.1652174684160000E+01, \
      0.1453325357056000E+01 ) )

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12 ))

  x_vec = np.array ( ( \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def cheby_u_poly_values_test ( ):

#*****************************************************************************80
#
## cheby_u_poly_values_test() tests cheby_u_poly_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cheby_u_poly_values_test():' )
  print ( '  cheby_u_poly_values() stores values of the Chebyshev U polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = cheby_u_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )

  return

def cheby_u_poly_zero ( n ):

#*****************************************************************************80
#
## cheby_u_poly_zero() returns zeroes of Chebyshev polynomials U(n,x).
#
#  Discussion:
#
#    The I-th zero of U(n,x) is cos(I*PI/(N+1)), I = 1 to N
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#    real Z(N), the zeroes of U(N)(X).
#
  import numpy as np

  z = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( n + 1 )
    z[i] = np.cos ( angle )

  return z

def cheby_u_poly_zero_test ( ):

#*****************************************************************************80
#
## cheby_u_poly_zero_test() tests cheby_u_poly_zero().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n_max = 4

  print ( '' )
  print ( 'cheby_u_poly_zero_test():' )
  print ( '  cheby_u_poly_zero() returns zeroes of U(N,X).' )
  print ( '' )
  print ( '         N         X        U(N,X)' )
  print ( '' )

  for n in range ( 1, n_max + 1 ):

    z = cheby_u_poly_zero ( n )

    fx = cheby_u_poly ( n, n, z )

    for i in range ( 0, n ):
      print ( '  %8d  %11g  %14g' % ( n, z[i], fx[i,n] ) )

    print ( '' )

  return

def collatz_count_max ( n ):

#*****************************************************************************80
#
## collatz_count_max() seeks the maximum Collatz count for 1 through N.
#
#  Discussion:
#
#    For each integer I, we compute a sequence of values that 
#    terminate when we reach 1.  The number of steps required to
#    reach 1 is the "rank" of I, and we are searching the numbers from
#    1 to N for the number with maximum rank.
#
#    For a given I, the sequence is produced by:
#
#    1) J = 1, X(J) = I;
#    2) If X(J) = 1, stop.
#    3) J = J + 1; 
#       if X(J-1) was even, X(J) = X(J-1)/2;
#       else                X(J) = 3 * X(J-1) + 1;
#    4) Go to 3
#
#  Example:
#
#            N    I_max J_max
#
#           10        9    20
#          100       97   119
#        1,000      871   179
#       10,000    6,171   262
#      100,000   77,031   351
#    1,000,000  837,799   525
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2009
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the maximum integer to check.
#
#    integer I_max, J_max, an integer I with the maximum rank,
#    and the value of the maximum rank.
#
  i_max = -1
  j_max = -1

  for i in range ( 1, n + 1 ):

    j = 1
    x = i

    while ( x != 1 ):
      j = j + 1
      if ( ( x % 2 ) == 0 ):
        x = x // 2
      else:
        x = 3 * x + 1

    if ( j_max < j ):
      i_max = i
      j_max = j

  return i_max, j_max

def collatz_count_max_test ( ):

#*****************************************************************************80
#
## collatz_count_max_test() tests collatz_count_max().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'collatz_count_max_test():' )
  print ( '  collatz_count_max(N) returns the maximum length of a' )
  print ( '  Collatz sequence for starts between 1 and N.' )
  print ( '' )
  print ( '       N       I_max         J_max' )
  print ( '' )

  n = 10

  while ( n <= 100000 ):

    i_max, j_max = collatz_count_max ( n )

    print ( '  %8d  %8d  %8d' % ( n, i_max, j_max ) )

    n = n * 10

  return

def collatz_count ( n ):

#*****************************************************************************80
#
## collatz_count() counts the number of terms in a Collatz sequence.
#
#  Discussion:
#
#    The rules for generation of the Collatz sequence are recursive.
#    If T is the current entry of the sequence, (T is
#    assumed to be a positive integer), then the next
#    entry, U is determined as follows:
#
#      if T is 1 (or less)
#        terminate the sequence;
#      else if T is even
#        U = T/2.
#      else (if T is odd and not 1)
#        U = 3*T+1;
#
#     N  Sequence                                                Length
#
#     1                                                               1
#     2   1                                                           2
#     3  10,  5, 16,  8,  4,  2,  1                                   8
#     4   2   1                                                       3
#     5  16,  8,  4,  2,  1                                           6
#     6   3, 10,  5, 16,  8,  4,  2,  1                               9
#     7  22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1   17
#     8   4,  2,  1                                                   4
#     9  28, 14,  7, ...                                             20
#    10   5, 16,  8,  4,  2,  1                                       7
#    11  34, 17, 52, 26, 13, 40, 20, 10,  5, 16, 8, 4, 2, 1          15
#    12   6,  3, 10,  5, 16,  8,  4,  2,  1                          10
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein,
#    "The Collatz Problem",
#    CRC Concise Encyclopedia of Mathematics,
#    CRC 1998.
#
#  Input:
#
#    integer N, the first element of the sequence.
#
#    integer COUNT, the number of elements in
#    the Collatz sequence that begins with N.
#
  value = 1

  while ( True ):

    if ( n <= 1 ):
      break
    elif ( ( n % 2 ) == 0 ):
      n = n // 2
    else:
      n = 3 * n + 1

    value = value + 1

  return value

def collatz_count_test ( ):

#*****************************************************************************80
#
## collatz_count_test() tests collatz_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'collatz_count_test():' )
  print ( '  collatz_count(N) counts the length of the' )
  print ( '  Collatz sequence beginning with N.' )
  print ( '' )
  print ( '       N       COUNT(N)     COUNT(N)' )
  print ( '              (computed)    (table)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, value1 = collatz_count_values ( n_data )

    if ( n_data == 0 ):
      break

    value2 = collatz_count ( n )

    print ( '  %4d  %6d  %6d' % ( n, value1, value2 ) )

  return

def collatz_count_values ( n_data ):

#*****************************************************************************80
#
## collatz_count_values() returns some values of the Collatz count function.
#
#  Discussion:
#
#    The rules for generation of the Collatz sequence are recursive.
#    If T is the current entry of the sequence, (T is
#    assumed to be a positive integer), then the next
#    entry, U is determined as follows:
#
#      if T is 1 (or less)
#        terminate the sequence;
#      else if T is even
#        U = T/2.
#      else (if T is odd and not 1)
#        U = 3*T+1;
#
#    The Collatz count is the length of the Collatz sequence for a given
#    starting value.  By convention, we include the initial value in the
#    count, so the minimum value of the count is 1.
#
#     N  Sequence                                                 Count
#
#     1                                                               1
#     2   1                                                           2
#     3  10,  5, 16,  8,  4,  2,  1                                   8
#     4   2   1                                                       3
#     5  16,  8,  4,  2,  1                                           6
#     6   3, 10,  5, 16,  8,  4,  2,  1                               9
#     7  22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1   17
#     8   4,  2,  1                                                   4
#     9  28, 14,  7, ...                                             20
#    10   5, 16,  8,  4,  2,  1                                       7
#    11  34, 17, 52, 26, 13, 40, 20, 10,  5, 16, 8, 4, 2, 1          15
#    12   6,  3, 10,  5, 16,  8,  4,  2,  1                          10
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein,
#    "The Collatz Problem",
#    CRC Concise Encyclopedia of Mathematics,
#    CRC 1998.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the initial value of a Collatz sequence.
#
#    integer COUNT, the length of the Collatz sequence starting
#    with N.
#
  import numpy as np

  n_max = 20

  count_vec = np.array ( ( \
      1,   2,   8,   3,   6,   9,   17,   4,  20,   7, \
    112,  25,  26,  27,  17,  28,  111,  18,  83,  29 ) )

  n_vec = np.array ( ( \
      1,   2,   3,   4,   5,   6,   7,   8,   9,  10, \
     27,  50, 100, 200, 300, 400, 500, 600, 700, 800 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    count = 0
  else:
    n = n_vec[n_data]
    count = count_vec[n_data]
    n_data = n_data + 1

  return n_data, n, count

def collatz_count_values_test ( ):

#*****************************************************************************80
#
## collatz_count_values_test() tests collatz_count_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'collatz_count_values_test():' )
  print ( '  collatz_count_values() returns values of' )
  print ( '  the length of the Collatz sequence that starts at N.' )
  print ( '' )
  print ( '     N        Count' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, count = collatz_count_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %10d' % ( n, count ) )

  return

def comb_row_next ( n, c ):

#*****************************************************************************80
#
## comb_row_next() computes the next row of Pascal's triangle.
#
#  Discussion:
#
#    Row N contains the combinatorial coefficients
#
#      C(N,0), C(N,1), C(N,2), ... C(N,N)
#
#    The sum of the elements of row N is equal to 2^N.
#
#    C(N,K) = N! / ( K! * (N-K)! )
#
#  First terms:
#
#     N K:0  1   2   3   4   5   6   7  8  9 10
#
#     0   1
#     1   1  1
#     2   1  2   1
#     3   1  3   3   1
#     4   1  4   6   4   1
#     5   1  5  10  10   5   1
#     6   1  6  15  20  15   6   1
#     7   1  7  21  35  35  21   7   1
#     8   1  8  28  56  70  56  28   8  1
#     9   1  9  36  84 126 126  84  36  9  1
#    10   1 10  45 120 210 252 210 120 45 10  1
#
#  Recursion:
#
#    C(N,K) = C(N-1,K-1)+C(N-1,K)
#
#  Special values:
#
#    C(N,0) = C(N,N) = 1
#    C(N,1) = C(N,N-1) = N
#    C(N,N-2) = sum ( 1 <= I <= N ) N
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the desired row.
#
#    Input/integer C(N+1).  On row N-1 is contained in
#    entries 0 through N-1.  On row N is contained in entries 0
#    through N.
#  
  if ( n < 0 ):
    return

  c[n] = 1
  for i in range ( n - 1, 0, -1 ):
    c[i] = c[i] + c[i-1]
  c[0] = 1

  return c

def comb_row_next_test ( ):

#*****************************************************************************80
#
## comb_row_next_test() tests comb_row_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n_max = 10

  print ( '' )
  print ( 'comb_row_next_test():' )
  print ( '  comb_row_next() computes the next row of Pascal\'s triangle.' )
  print ( '' )

  c = np.zeros ( n_max + 1 )

  for n in range ( 0, n_max + 1 ):
    c = comb_row_next ( n, c )
    print ( '  %2d  ' % ( n ) ),
    for i in range ( 0, n + 1 ):
      print ( '  %3d' % ( c[i] ) ),
    print ( '' )

  return

def commul ( n, nfactor, iarray ):

#*****************************************************************************80
#
## commul() computes a multinomial combinatorial coefficient.
#
#  Discussion:
#
#    The multinomial coefficient is a generalization of the binomial
#    coefficient.  It may be interpreted as the number of combinations of
#    N objects, where IARRAY(1) objects are indistinguishable of type 1,
#    ... and IARRAY(K) are indistinguishable of type NFACT.
#
#    The formula is
#
#      NCOMB = N! / ( IARRAY(1)! IARRAY(2)! ... IARRAY(NFACT)! )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, determines the numerator.
#
#    integer NFACTOR, the number of factors in the numerator.
#
#    integer IARRAY(NFACTOR).
#    IARRAY contains the NFACT values used in the denominator.
#    Note that the sum of these entries should be N,
#    and that all entries should be nonnegative.
#
#  Output:
#
#    integer NCOMB, the value of the multinomial coefficient.
#
  import numpy as np
  from scipy.special import gammaln

  for i in range ( 0, nfactor ):

    if ( iarray[i] < 0 ):
      print ( '' )
      print ( 'commul(): Fatal error!' )
      print ( '  Entry %d of IARRAY = %d' % ( i, iarray[i] ) )
      print ( '  But this value must be nonnegative.' )
      raise Exception ( 'commul(): Fatal error!' )

  isum = np.sum ( iarray )

  if ( isum != n ):
    print ( '' )
    print ( 'commul(): Fatal error!' )
    print ( '  The sum of the IARRAY entries is %d' % (isum ) )
    print ( '  But it must equal N = %d' % ( n ) )
    raise Exception ( 'commul(): Fatal error!' )
 
  facn = gammaln ( float ( n + 1 ) )
 
  for i in range ( 0, nfactor ):
 
    fack = gammaln ( float ( iarray[i] + 1 ) )
    facn = facn - fack

  ncomb = int ( np.round ( np.exp ( facn ) ) )

  return ncomb

def commul_test ( ):

#*****************************************************************************80
#
## commul_test() tests commul().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'commul_test():' )
  print ( '  commul() computes a multinomial coefficient.' )

  n = 8
  nfactor = 2
  factor = np.array ( [ 6, 2 ] )
  ncomb = commul ( n, nfactor, factor )
  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '  Number of factors = %d' % ( nfactor ) )
  for i in range ( 0, nfactor ):
    print ( '  %2d  %2d' % ( i, factor[i] ) )
  print ( '  Value of coefficient = %d' % ( ncomb ) )

  n = 8
  nfactor = 3
  factor = np.array ( [ 2, 2, 4 ] )
  ncomb = commul ( n, nfactor, factor )
  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '  Number of factors = %d' % ( nfactor ) )
  for i in range ( 0, nfactor ):
    print ( '  %2d  %2d' % ( i, factor[i] ) )
  print ( '  Value of coefficient = %d' % ( ncomb ) )

  n = 13
  nfactor = 4
  factor = np.array ( [ 5, 3, 3, 2 ] )
  ncomb = commul ( n, nfactor, factor )
  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '  Number of factors = %d' % ( nfactor ) )
  for i in range ( 0, nfactor ):
    print ( '  %2d  %2d' % ( i, factor[i] ) )
  print ( '  Value of coefficient = %d' % ( ncomb ) )

  return

def complete_symmetric_poly ( n, r, x ):

#*****************************************************************************80
#
## complete_symmetric_poly() evaluates a complete symmetric polynomial.
#
#  Discussion:
#
#    N\R  0   1         2               3
#      +--------------------------------------------------------
#    0 |  1   0         0               0
#    1 |  1   X1        X1^2            X1^3
#    2 |  1   X1+X2     X1^2+X1X2+X2^2  X1^3+X1^2X2+X1X2^2+X2^3
#    3 |  1   X1+X2+X3  ...
#
#    If X = ( 1, 2, 3, 4, 5, ... ) then
#
#    N\R  0     1     2     3     4 ...
#      +--------------------------------------------------------
#    0 |  1     0     0     0     0
#    1 |  1     1     1     1     1
#    2 |  1     3     7    15    31
#    3 |  1     6    25    90   301
#    4 |  1    10    65   350  1701
#    5 |  1    15   140  1050  6951
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of variables.
#    0 <= N.
#
#    integer R, the degree of the polynomial.
#    0 <= R.
#
#    real X(N), the value of the variables.
#
#    real VALUE, the value of TAU(N,R)(X).
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'complete_symmetric_poly(): Fatal error!' )
    print ( '  N < 0.' )
    raise Exception ( 'complete_symmetric_poly(): Fatal error!' )

  if ( r < 0 ):
    print ( '' )
    print ( 'complete_symmetric_poly(): Fatal error!' )
    print ( '  R < 0.' )
    raise Exception ( 'complete_symmetric_poly(): Fatal error!' )

  tau_length = max ( n, r ) + 1
  tau = np.zeros ( tau_length )

  tau[0] = 1.0
  for nn in range ( 0, n ):
    for rr in range ( 1, r + 1 ):
      tau[rr] = tau[rr] + x[nn] * tau[rr-1]

  value = tau[r]

  return value

def complete_symmetric_poly_test ( ):

#*****************************************************************************80
#
## complete_symmetric_poly_test() tests complete_symmetric_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'complete_symmetric_poly_test():' )
  print ( '  complete_symmetric_poly() evaluates a complete symmetric' )
  print ( '  polynomial in a given set of variables X.' )
 
  n = 5
  x = np.array ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ] )
  r8vec_print ( n, x, '  Variable vector X:' )

  print ( '' )
  print ( '   N\\R     0       1       2       3       4       5' )
  print ( '' )

  for nn in range ( 0, n + 1 ):
    print ( '  %2d' % ( nn ) ),
    for rr in range ( 0, 6 ):
      value = complete_symmetric_poly ( nn, rr, x )
      print ( '  %6d' % ( value ) ),
    print ( '' )

  return

def conway_sequence_test ( ):

#*****************************************************************************80
#
## conway_sequence_test() tests conway_sequence().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'conway_sequence_test():' )
  print ( '  conway_sequence() returns the first N entries of' )
  print ( '  the Conway challenge sequence.' )

  n = 64
  A = conway_sequence ( n )
  print ( A )

  return

def conway_sequence ( n ):

#*****************************************************************************80
#
## conway_sequence() computes the first terms of the Conway challenge sequence.
#
#  Discussion:
#
#    In an attempt to deal with the 0-based indexing used in Python,
#    I inserted an initial 0-th entry with value 0.
#
#    A(0) = 0
#    A(1) = 1
#    A(2) = 1
#    A(N) = A(A(N-1)) + A(N-A(N-1))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Colin Mallows,
#    Conway's Challenge Sequence,
#    American Mathematical Monthly,
#    Volume 98, Number 1, 1991, pages 5-20.
#
#  Input:
#
#    integer n: the number of elements to compute.
#
#  Output:
#
#    integer A(N+1), the sequence elements.
#
  import numpy as np

  A = np.zeros ( n + 1, dtype = int )
  A[0] = 0
  A[1] = 1
  A[2] = 1
  for i in range ( 3, n + 1 ):
    A[i] = A[A[i-1]] + A[i-A[i-1]]

  return A

def cos_power_int ( a, b, n ):

#*****************************************************************************80
#
## cos_power_int() evaluates the cosine power integral.
#
#  Discussion:
#
#    The function is defined by
#
#      cos_power_int(A,B,N) = Integral ( A <= T <= B ) ( cos ( t ))^n dt
#
#    The algorithm uses the following fact:
#
#      Integral cos^n ( t ) = -(1/n) * (
#        cos^(n-1)(t) * sin(t) + ( n-1 ) * Integral cos^(n-2) ( t ) dt )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the limits of integration.
#
#    integer N, the power of the sine function.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'cos_power_int(): Fatal error!' )
    print ( '  Power N < 0.' )
    raise Exception ( 'cos_power_int(): Fatal error!' )

  sa = np.sin ( a );
  sb = np.sin ( b );
  ca = np.cos ( a );
  cb = np.cos ( b );

  if ( ( n % 2 ) == 0 ):
    value = b - a
    mlo = 2
  else:
    value = sb - sa
    mlo = 3

  for m in range ( mlo, n + 1, 2 ):
    value = ( ( m - 1 ) * value - ca ** ( m - 1 ) * sa \
                                + cb ** ( m - 1 ) * sb ) / float ( m )

  return value

def cos_power_int_test ( ):

#*****************************************************************************80
#
## cos_power_int_test() tests cos_power_int().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cos_power_int_test():' )
  print ( '  cos_power_int() returns values of' )
  print ( '  the integral of COS(X)^N from A to B.' )
  print ( '' )
  print ( '      A         B          N      Exact           Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, n, fx = cos_power_int_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = cos_power_int ( a, b, n )

    print ( '  %8f  %8f  %6d  %14e  %14e' % ( a, b, n, fx, fx2 ) )

  return

def cos_power_int_values ( n_data ):

#*****************************************************************************80
#
## cos_power_int_values() returns some values of the cosine power integral.
#
#  Discussion:
#
#    The function has the form
#
#      cos_power_int(A,B,N) = Integral ( A <= T <= B ) ( cos(T) )^N dt
#
#    In Mathematica, the function can be evaluated by:
#
#      Integrate [ ( Cos[x] )^n, { x, a, b } ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real A, B, the limits of integration.
#
#    integer N, the power.
#
#    real F, the function value.
#
  import numpy as np

  n_max = 11

  a_vec = np.array ( ( \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00 ))

  b_vec = np.array ( ( \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793  ) )

  f_vec = np.array ( ( \
     3.141592653589793, \
     0.0, \
     1.570796326794897, \
     0.0, \
     1.178097245096172, \
     0.0, \
     0.9817477042468104, \
     0.0, \
     0.8590292412159591, \
     0.0, \
     0.7731263170943632 ) )

  n_vec = np.array ( ( \
     0, \
     1, \
     2, \
     3, \
     4, \
     5, \
     6, \
     7, \
     8, \
     9, \
    10  ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    f = 0.0
    n = 0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    f = f_vec[n_data]
    n = n_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, n, f

def cos_power_int_values_test ( ):

#*****************************************************************************80
#
## cos_power_int_values_test() tests cos_power_int_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'cos_power_int_values_test():' )
  print ( '  cos_power_int_values() stores values of the cosine power integral.' )
  print ( '' )
  print ( '        A             B            N           F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, n, f = cos_power_int_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %6d  %24.16g' % ( a, b, n, f ) )

  return

def delannoy ( m, n ):

#*****************************************************************************80
#
## delannoy() returns the Delannoy numbers up to orders (M,N).
#
#  Discussion:
#
#    The Delannoy number A(M,N) counts the number of distinct paths from
#    (0,0) to (M,N) in which the only steps used are
#    (1,1), (1,0) and (0,1).
#
#  First values:
#
#      \N 0  1   2   3    4     5     6      7      8
#     M-+--------------------------------------------
#     0 : 1  1   1   1    1     1     1      1      1
#     1 : 1  3   5   7    9    11    13     15     17
#     2 : 1  5  13  25   41    61    85    113    145
#     3 : 1  7  25  63  129   231   377    575    833
#     4 : 1  9  41 129  321   681  1289   2241   3649
#     5 : 1 11  61 231  681  1683  3653   7183  13073
#     6 : 1 13  85 377 1289  3653  8989  19825  40081
#     7 : 1 15 113 575 2241  7183 19825  48639 108545
#     8 : 1 17 145 833 3649 13073 40081 108545 265729
#
#  Recursion:
#
#    A(0,0) = 1
#    A(M,0) = 1
#    A(0,N) = 1
#    A(M,N) = A(M-1,N) + A(M,N-1) + A(M-1,N-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1998
#
#  Input:
#
#    integer M, N, define the highest order number to compute.
#
#    integer A(1:M+1,1:N+1), the Delannoy numbers.
#
  import numpy as np

  a = np.zeros ( [ m + 1, n + 1 ] )

  a[0,0] = 1

  for i in range ( 1, m + 1 ):
    a[i,0] = 1

  for j in range ( 1, n + 1 ):
    a[0,j] = 1

  for i in range ( 1, m + 1 ):
    for j in range ( 1, n + 1 ):
      a[i,j] = a[i-1,j] + a[i,j-1] + a[i-1,j-1]

  return a

def delannoy_test ( ):

#*****************************************************************************80
#
## delannoy_test() tests delannoy().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 8
  n = 8

  print ( '' )
  print ( 'delannoy_test():' )
  print ( '  delannoy() computes the Delannoy numbers A(0:M,0:N).' )
  print ( '  A(M,N) counts the paths from (0,0) to (M,N).' )
  print ( '' )

  a = delannoy ( m, n )

  for i in range ( 0, m + 1 ):
    print ( '  %2d  ' % ( i ) ),
    for j in range ( 0, n + 1 ):
      print ( '  %6d' % ( a[i,j] ) ),
    print ( '' )

  return

def domino_tiling_num ( m, n ):

#*****************************************************************************80
#
## domino_tiling_num() counts tilings of an MxN rectangle by dominoes.
#
#  Discussion:
#
#    An 8x8 chessboard has 12,988,816 such tilings.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2018
#
#  Author:
#
#    Original Python version by John D Cook.
#    This version by John Burkardt.
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer VALUE, the number of tilings.
#
  import numpy as np

  value = 1
  for k in range ( 1, m + 1 ):
    for l in range ( 1, n + 1 ):
      value = value * 2 * (        np.cos ( np.pi * k / ( m + 1 ) ) 
                            + 1j * np.cos ( np.pi * l / ( n + 1 ) ) )

  value = round ( np.sqrt ( abs ( value ) ) )

  return value
        
def domino_tiling_num_test ( ):

#*****************************************************************************80
#
## domino_tiling_num_test() tests domino_tiling_num().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'domino_tiling_num_test():' )
  print ( '  domino_tiling_num() returns the number of tilings of an' )
  print ( '  MxN rectangle by dominoes.' )
  print ( '' )
  print ( '   M   N    Tilings' )
  for m in range ( 1, 9 ):
    print ( '' )
    for n in range ( 1, m + 1 ):
      value = domino_tiling_num ( m, n )
      print ( '  %d  %d  %d' % ( m, n, value ) )

  return

def erf_values ( n_data ):

#*****************************************************************************80
#
## erf_values() returns some values of the ERF or "error" function.
#
#  Discussion:
#
#    The error function is defined by:
#
#      ERF(X) = ( 2 / sqrt ( PI ) * integral ( 0 <= T <= X ) exp ( - T^2 ) dT
#
#    In Mathematica, the function can be evaluated by:
#
#      Erf[x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  fx_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.1124629160182849E+00, \
     0.2227025892104785E+00, \
     0.3286267594591274E+00, \
     0.4283923550466685E+00, \
     0.5204998778130465E+00, \
     0.6038560908479259E+00, \
     0.6778011938374185E+00, \
     0.7421009647076605E+00, \
     0.7969082124228321E+00, \
     0.8427007929497149E+00, \
     0.8802050695740817E+00, \
     0.9103139782296354E+00, \
     0.9340079449406524E+00, \
     0.9522851197626488E+00, \
     0.9661051464753107E+00, \
     0.9763483833446440E+00, \
     0.9837904585907746E+00, \
     0.9890905016357307E+00, \
     0.9927904292352575E+00, \
     0.9953222650189527E+00 ) )

  x_vec = np.array ( ( \
     0.0E+00, \
     0.1E+00, \
     0.2E+00, \
     0.3E+00, \
     0.4E+00, \
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00, \
     1.1E+00, \
     1.2E+00, \
     1.3E+00, \
     1.4E+00, \
     1.5E+00, \
     1.6E+00, \
     1.7E+00, \
     1.8E+00, \
     1.9E+00, \
     2.0E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def erf_values_test ( ):

#*****************************************************************************80
#
## erf_values_test() tests erf_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'erf_values_test():' )
  print ( '  erf_values() stores values of the error function.' )
  print ( '' )
  print ( '      X         ERF(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = erf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def eulerian ( n ):

#*****************************************************************************80
#
## eulerian() computes the Eulerian number E(N,K).
#
#  Definition:
#
#    A run in a permutation is a sequence of consecutive ascending values.
#
#    E(N,K) is the number of permutations of N objects which contain
#    exactly K runs.
#
#  Examples:
#
#     N = 7
#
#     1     0     0     0     0     0     0
#     1     1     0     0     0     0     0
#     1     4     1     0     0     0     0
#     1    11    11     1     0     0     0
#     1    26    66    26     1     0     0
#     1    57   302   302    57     1     0
#     1   120  1191  2416  1191   120     1
#
#  Recursion:
#
#    E(N,K) = K * E(N-1,K) + (N-K+1) * E(N-1,K-1).
#
#  Properties:
#
#    E(N,1) = E(N,N) = 1.
#    E(N,K) = 0 if K <= 0 or N < K.
#    sum ( 1 <= K <= N ) E(N,K) = N!.
#    X^N = sum ( 0 <= K <= N ) COMB(X+K-1, N ) E(N,K)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton and Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, 1986
#
#  Input:
#
#    integer N, the number of rows desired.
#
#    integer E(N,N), the first N rows of Eulerian numbers.
#
  import numpy as np

  e = np.zeros ( ( n, n ) )
#
#  Construct rows 1, 2, ..., N of the Eulerian triangle.
#
  e[0,0] = 1
  for j in range ( 1, n ):
    e[0,j] = 0

  for i in range ( 1, n ):
    e[i,0] = 1
    for j in range ( 1, n ):
      e[i,j] = ( j + 1 ) * e[i-1,j] + ( i - j + 1 ) * e[i-1,j-1]

  return e

def eulerian_test ( ):

#*****************************************************************************80
#
## eulerian_test() tests eulerian().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'eulerian_test():' )
  print ( '  eulerian() computes Eulerian numbers.' )

  n = 7
  e = eulerian ( n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      print ( '  %4d' % ( e[i,j] ) ),
    print ( '' )

  return

def euler_mascheroni ( ):

#*****************************************************************************80
#
## euler_mascheroni() returns the value of the Euler-Mascheroni constant.
#
#  Discussion:
#
#    The Euler-Mascheroni constant is often denoted by a lower-case
#    Gamma.  Gamma is defined as
#
#      Gamma = limit ( M -> oo )
#        ( sum ( 1 <= N <= M ) 1 / N ) - log ( M )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the value of the Euler-Mascheroni constant.
#
  value = 0.577215664901532860606512090082402431042

  return value

def euler_mascheroni_test ( ):

#*****************************************************************************80
#
## euler_mascheroni_test() tests euler_mascheroni().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  g = euler_mascheroni ( )

  print ( '' )
  print ( 'euler_mascheroni_test():' )
  print ( '  euler_mascheroni() returns the Euler-Mascheroni constant' )
  print ( '  sometimes denoted by "gamma".' )
  print ( '' )
  print ( '  gamma = limit ( N -> oo ) ( sum ( 1 <= I <= N ) 1 / I ) - log ( N )' )
  print ( '' )
  print ( '  Numerically, g = %24.16g' % ( g ) )
  print ( '' )
  print ( '         N      Partial Sum    |gamma - partial sum|' )
  print ( '' )

  n = 1
  for test in range ( 0, 21 ):
    g_approx = - np.log ( n )
    for i in range ( 1, n + 1 ):
      g_approx = g_approx + 1.0 / i
    print ( '  %8d  %14.6g  %14.6g' % ( n, g_approx, abs ( g_approx - g ) ) )
    n = n * 2

  return

def euler_number2 ( n ):

#*****************************************************************************80
#
## euler_number2() computes the Euler numbers.
#
#  Discussion:
#
#    The Euler numbers can be evaluated in Mathematica by the call
#
#      EulerE[n]
#
#    These numbers rapidly get too big to store in an ordinary integer!
#
#    The terms of odd index are 0.
#
#    E(N) = -C(N,N-2) * E(N-2) - C(N,N-4) * E(N-4) - ... - C(N,0) * E(0).
#
#  First terms:
#
#    E0  = 1
#    E1  = 0
#    E2  = -1
#    E3  = 0
#    E4  = 5
#    E5  = 0
#    E6  = -61
#    E7  = 0
#    E8  = 1385
#    E9  = 0
#    E10 = -50521
#    E11 = 0
#    E12 = 2702765
#    E13 = 0
#    E14 = -199360981
#    E15 = 0
#    E16 = 19391512145
#    E17 = 0
#    E18 = -2404879675441
#    E19 = 0
#    E20 = 370371188237525
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N, the index of the Euler number.
#
#    real VALUE, the value of the Euler number.
#
  import numpy as np

  evec = np.array ( ( 1.0, -1.0, 5.0, -61.0, 1385.0, -50521.0, 2702765.0 ) )
  itmax = 1000

  value = 0.0

  if ( ( n % 2 ) == 0 ):

    if ( n <= 12 ):
      i = ( n // 2 )
      value = evec[i]
    else:

      sum1 = 0.0

      for i in range ( 0, itmax ):

        term = 1.0 / float ( ( 2 * i - 1 ) ** ( n + 1 ) )

        if ( ( i % 2 ) == 0 ):
          sum1 = sum1 + term
        else:
          sum1 = sum1 - term

        if ( abs ( term ) < 1.0E-10 ):
          break
        elif ( abs ( term ) < 1.0E-08 * abs ( sum1 ) ):
          break

      value = 2.0 ** ( n + 2 ) * sum1 * math.factorial ( n ) / np.pi ** ( n + 1 )

      if ( ( n % 4 ) != 0 ):
        value = - value

  return value

def euler_number2_test ( ):

#*****************************************************************************80
#
## euler_number2_test() tests euler_number2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'euler_number2_test():' )
  print ( '  euler_number2() computes Euler numbers;' )
  print ( '' )
  print ( '   I      Exact        Euler' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, e1 = euler_number_values ( n_data )

    if ( n_data == 0 ):
      break

    e2 = euler_number2 ( n )

    print ( '  %2d  %14d  %14d' % ( n, e1, e2 ) )

  return

def euler_number ( n ):

#*****************************************************************************80
#
## euler_number() computes the Euler numbers.
#
#  Discussion:
#
#    The Euler numbers can be evaluated in Mathematica by the call
#
#      EulerE[n]
#
#    These numbers rapidly get too big to store in an ordinary integer!
#
#    The terms of odd index are 0.
#
#    E(N) = -C(N,N-2) * E(N-2) - C(N,N-4) * E(N-4) - ... - C(N,0) * E(0).
#
#  First terms:
#
#    E0  = 1
#    E1  = 0
#    E2  = -1
#    E3  = 0
#    E4  = 5
#    E5  = 0
#    E6  = -61
#    E7  = 0
#    E8  = 1385
#    E9  = 0
#    E10 = -50521
#    E11 = 0
#    E12 = 2702765
#    E13 = 0
#    E14 = -199360981
#    E15 = 0
#    E16 = 19391512145
#    E17 = 0
#    E18 = -2404879675441
#    E19 = 0
#    E20 = 370371188237525
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N, the index of the last Euler number to compute.
#
#    integer E[0:N], the Euler numbers.
#
  import numpy as np

  e = np.zeros ( n + 1 )

  e[0] = 1

  if ( 0 < n ):

    e[1] = 0

    if ( 1 < n ):

      e[2] = -1

      for i in range ( 3, n + 1 ):

        e[i] = 0

        if ( ( i % 2 ) == 0 ):

          for j in range ( 2, i + 1, 2 ):
            e[i] = e[i] - i4_choose ( i, j ) * e[i-j]

  return e

def euler_number_test ( ):

#*****************************************************************************80
#
## euler_number_test() tests euler_number().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'euler_number_test():' )
  print ( '  euler_number() computes Euler numbers;' )
  print ( '' )
  print ( '   I      Exact        Euler' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, e1 = euler_number_values ( n_data )

    if ( n_data == 0 ):
      break

    e2 = euler_number ( n )

    print ( '  %2d  %14d  %14d' % ( n, e1, e2[n] ) )

  return

def euler_number_values ( n_data ):

#*****************************************************************************80
#
## euler_number_values() returns some values of the Euler numbers.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      EulerE[n]
#
#    These numbers rapidly get too big to store in an ordinary integer!
#
#    The terms of odd index are 0.
#
#    E(N) = -C(N,N-2) * E(N-2) - C(N,N-4) * E(N-4) - ... - C(N,0) * E(0).
#
#  First terms:
#
#    E0  = 1
#    E1  = 0
#    E2  = -1
#    E3  = 0
#    E4  = 5
#    E5  = 0
#    E6  = -61
#    E7  = 0
#    E8  = 1385
#    E9  = 0
#    E10 = -50521
#    E11 = 0
#    E12 = 2702765
#    E13 = 0
#    E14 = -199360981
#    E15 = 0
#    E16 = 19391512145
#    E17 = 0
#    E18 = -2404879675441
#    E19 = 0
#    E20 = 370371188237525
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the Euler number.
#
#    integer C, the value of the Euler number.
#
  import numpy as np

  n_max = 8

  c_vec = np.array ( (
    1, 0, -1, 5, -61, 1385, -50521, 2702765 ))

  n_vec = np.array ( (
     0, 1, 2, 4, 6, 8, 10, 12 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def euler_number_values_test ( ):

#*****************************************************************************80
#
## euler_number_values_test() tests euler_number_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'euler_number_values_test():' )
  print ( '  euler_number_values() returns values of ' )
  print ( '  the Euler numbers.' )
  print ( '' )
  print ( '     N         euler_number(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = euler_number_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %10d' % ( n, c ) )

  return

def euler_poly ( n, x ):

#*****************************************************************************80
#
## euler_poly() evaluates the N-th Euler polynomial at X.
#
#  First values:
#
#    E(0,X) = 1
#    E(1,X) = X   - 1/2
#    E(2,X) = X^2 -     X
#    E(3,X) = X^3 - 3/2 X^2 + 1/4
#    E(4,X) = X^4 - 2 * X^3 +      X
#    E(5,X) = X^5 - 5/2 X^4 + 5/2  X^2 - 1/2
#    E(6,X) = X^6 - 3   X^5 + 5    X^3 - 3    X
#    E(7,X) = X^7 - 7/2 X^6 + 35/4 X^4 - 21/2 X^2 + 17/8
#    E(8,X) = X^8 - 4   X^7 + 14   X^5 - 28   X^3 + 17    X
#
#  Special values:
#
#    E'(N,X) = N * E(N-1,X)
#
#    E(N,1/2) = E(N) / 2^N, where E(N) is the N-th Euler number.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the Euler polynomial to
#    be evaluated.  N must be 0 or greater.
#
#    real X, the value at which the polynomial is to
#    be evaluated.
#
#    real VALUE, the value of E(N,X).
#
  bx1 = bernoulli_poly2 ( n + 1, x )
  bx2 = bernoulli_poly2 ( n + 1, 0.5 * x )

  value = 2.0  * ( bx1 - bx2 * 2.0 ** ( n + 1 ) ) / float ( n + 1 )

  return value

def euler_poly_test ( ):

#*****************************************************************************80
#
## euler_poly_test() tests euler_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 15
  x = 0.5

  print ( '' )
  print ( 'euler_poly_test():' )
  print ( '  euler_poly() computes Euler polynomials;' )
  print ( '' )
  print ( '  X = %g' % ( x ) )
  print ( '' )
  print ( '  N         X              F(X)' )
  print ( '' )

  for i in range ( 1, n + 1 ):

    value = euler_poly ( i, x )
    print ( '  %2d  %12f  %14g' % ( i, x, value ) )

  return

def f_hofstadter ( n ):

#*****************************************************************************80
#
## f_hofstadter() computes the Hofstadter F sequence.
#
#  Discussion:
#
#    F(N) = 0                if N = 0
#         = N - F ( N - 1 ), otherwise.
#
#    F(N) is defined for all nonnegative integers, and turns out
#    to be equal to int ( ( N + 1 ) / 2 ).
#
#  Table:
#
#     N  F(N)
#    --  ----
#
#     0     0
#     1     1
#     2     1
#     3     2
#     4     2
#     5     3
#     6     3
#     7     4
#     8     4
#     9     5
#    10     5
#    11     6
#    12     6
#    13     7
#    14     7
#    15     8
#    16     8
#    17     9
#    18     9
#    19    10
#    20    10
#    21    11
#    22    11
#    23    12
#    24    12
#    25    13
#    26    13
#    27    14
#    28    14
#    29    15
#    30    15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Douglas Hofstadter,
#    Goedel, Escher, Bach,
#    Basic Books, 1979.
#
#  Input:
#
#    integer N, the argument of the function.
#
#    integer VALUE, the value of the function.
#
  if ( n <= 0 ):
    value = 0
  else:
    value = n - f_hofstadter ( n - 1 )

  return value

def f_hofstadter_test ( ):

#*****************************************************************************80
#
## f_hofstadter_test() tests f_hofstadter().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'f_hofstadter_test():' )
  print ( '  f_hofstadter() evaluates Hofstadter\'s recursive F function.' )
  print ( '' )
  print ( '     N   F(N)' )
  print ( '' )

  for i in range ( 0, 31 ):
    f = f_hofstadter ( i )
    print ( '  %6d  %6d' % ( i, f ) )

  return

def fibonacci_direct ( n ):

#*****************************************************************************80
#
## fibonacci_direct() computes the N-th Fibonacci number directly.
#
#  Formula:
#
#      F(N) = ( PHIP^N - PHIM^N ) / sqrt(5)
#
#    where 
#
#      PHIP = ( 1 + sqrt(5) ) / 2, 
#      PHIM = ( 1 - sqrt(5) ) / 2.
#
#  Example:
#
#     N   F
#    --  --
#     0   0
#     1   1
#     2   1
#     3   2
#     4   3
#     5   5
#     6   8
#     7  13
#     8  21
#     9  34
#    10  55
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the index of the Fibonacci number to compute.
#    N should be nonnegative.
#
#    integer VALUE, the value of the N-th Fibonacci number.
#
  r8_sqrt5 = 2.236067977499790

  r8_phim = -0.618033988749895
  r8_phip =  1.618033988749895

  value = round ( ( r8_phip ** n - r8_phim ** n ) / r8_sqrt5 )

  return value

def fibonacci_direct_test ( ):

#*****************************************************************************80
#
## fibonacci_direct_test() tests fibonacci_direct().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'fibonacci_direct_test():' )
  print ( '  fibonacci_direct() computes a Fibonacci number directly;' )
  print ( '' )
  print ( '   I      F(I)' )
  print ( '' )

  for i in range ( 0, 21 ):
    value = fibonacci_direct ( i )
    print ( '  %2d  %14d' % ( i, value ) )

  return

def fibonacci_floor ( n ):

#*****************************************************************************80
#
## fibonacci_floor() returns the largest Fibonacci number less than or equal to N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the positive integer whose Fibonacci "floor" is desired.
#
#    integer F, the largest Fibonacci number less than or equal to N.
#
#    integer I, the index of the F.
#
  import numpy as np

  i = 0
  f = 0

  if ( 0 < n ):

    i = int ( np.log ( 0.5 * float ( 2 * n + 1 ) * np.sqrt ( 5.0 ) ) \
      / np.log ( 0.5 * ( 1.0 + np.sqrt ( 5.0 ) ) ) )

    f = fibonacci_direct ( i );

    if ( n < f ):
      i = i - 1
      f = fibonacci_direct ( i )

  return f, i

def fibonacci_floor_test ( ):

#*****************************************************************************80
#
## fibonacci_floor_test() tests fibonacci_floor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'fibonacci_floor_test():' )
  print ( '  fibonacci_floor() computes the largest Fibonacci number' )
  print ( '  less than or equal to N.' )
  print ( '' )
  print ( '     N  Fibonacci  Index' )
  print ( '' )

  for n in range ( 0, 21 ):
    f, i = fibonacci_floor ( n )
    print ( '  %4d  %4d  %4d' % ( n, f, i ) )

  return

def fibonacci_recursive ( n ):

#*****************************************************************************80
#
## fibonacci_recursive() computes the first N Fibonacci numbers.
#
#  Algebraic equation:
#
#    The 'golden ratio' PHI = (1+sqrt(5))/2 satisfies the equation
#
#      X*X-X-1=0
#
#    which is often written as:
#
#       X        1
#      --- =  ------
#       1      X - 1
#
#    expressing the fact that a rectangle, whose sides are in proportion X:1,
#    is similar to the rotated rectangle after a square of side 1 is removed.
#
#      <----X---->
#
#      +-----*---*
#      :     :   :  1
#      :     :   :
#      +-----*---+
#      <--1-><X-1>
#
#  Formula:
#
#    Let
#
#      PHIP = ( 1 + sqrt(5) ) / 2
#      PHIM = ( 1 - sqrt(5) ) / 2
#
#    Then
#
#      F(N) = ( PHIP^N + PHIM^N ) / sqrt(5)
#
#    Moreover, F(N) can be computed by computing PHIP**N / sqrt(5) and rounding
#    to the nearest whole number.
#
#  First terms:
#
#      1
#      1
#      2
#      3
#      5
#      8
#     13
#     21
#     34
#     55
#     89
#    144
#
#    The 40th number is                  102,334,155.
#    The 50th number is               12,586,269,025.
#    The 100th number is 354,224,848,179,261,915,075.
#
#  Recursion:
#
#    F(1) = 1
#    F(2) = 1
#
#    F(N) = F(N-1) + F(N-2)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the highest Fibonacci number to compute.
#
#    integer F(N+1), the first N Fibonacci numbers.
#
  import numpy as np

  f = np.zeros ( n + 1 )

  f[0] = 0

  if ( 0 < n ):

    f[1] = 1

    if ( 1 < n ):

      f[2] = 1

      for i in range ( 3, n + 1 ):
        f[i] = f[i-1] + f[i-2]

  return f

def fibonacci_recursive_test ( ):

#*****************************************************************************80
#
## fibonacci_recursive_test() tests fibonacci_recursive().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 20

  print ( '' )
  print ( 'fibonacci_recursive_test():' )
  print ( '  fibonacci_recursive() computes Fibonacci numbers recursively;' )

  f = fibonacci_recursive ( n )

  i4vec_print ( n + 1, f, '  The Fibonacci numbers:' )

  return

def gegenbauer_poly ( n, alpha, x ):

#*****************************************************************************80
#
## gegenbauer_poly() computes the Gegenbauer polynomials C(I,ALPHA)(X).
#
#  Discussion:
#
#    The Gegenbauer polynomial can be evaluated in Mathematica with
#    the command
#
#      GegenbauerC[n,m,x]
#
#  Differential equation:
#
#    (1-X*X) Y'' - (2 ALPHA + 1) X Y' + N (N + 2 ALPHA) Y = 0
#
#  Recursion:
#
#    C(0,ALPHA,X) = 1,
#    C(1,ALPHA,X) = 2*ALPHA*X
#    C(N,ALPHA,X) = (  ( 2*N-2+2*ALPHA) * X * C(N-1,ALPHA,X) 
#                    + (  -N+2-2*ALPHA)   *   C(N-2,ALPHA,X) ) / N
#
#  Restrictions:
#
#    ALPHA must be greater than -0.5.
#
#  Special values:
#
#    If ALPHA = 1, the Gegenbauer polynomials reduce to the Chebyshev
#    polynomials of the second kind.
#
#  Norm:
#
#    Integral ( -1 <= X <= 1 ) 
#      ( 1 - X^2 )^( ALPHA - 0.5 ) * C(N,ALPHA,X)^2 dX
#
#    = PI * 2^( 1 - 2 * ALPHA ) * Gamma ( N + 2 * ALPHA ) 
#      / ( N! * ( N + ALPHA ) * ( Gamma ( ALPHA ) )^2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    real ALPHA, a parameter which is part of the definition of
#    the Gegenbauer polynomials.  It must be greater than -0.5.
#
#    real X, the point at which the polynomials are to be evaluated.
#
#    real CX(1:N+1), the values of the first N+1 Gegenbauer
#    polynomials at the point X.  
#
  import numpy as np

  if ( alpha <= -0.5 ):
    print ( '' )
    print ( 'gegenbauer_poly(): Fatal error!' )
    print ( '  Illegal value of ALPHA = %f' % ( alpha ) )
    print ( '  but ALPHA must be greater than -0.5.' )
    raise Exception ( 'gegenbauer_poly(): Fatal error!' )

  cx = np.zeros ( n + 1 );

  cx[0] = 1.0

  if ( 0 < n ):

    cx[1] = 2.0 * alpha * x

  for i in range ( 2, n + 1 ):
    cx[i] = ( float (     2 * i - 2  + 2.0 * alpha ) * x * cx[i]     \
           +  float (       - i + 2  - 2.0 * alpha ) *     cx[i-1] ) \
           /  float (         i );

  return cx

def gegenbauer_poly_test ( ):

#*****************************************************************************80
#
## gegenbauer_poly_test() tests gegenbauer_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'gegenbauer_poly_test():' )
  print ( '  gegenbauer_poly() computes values of the Gegenbauer polynomial.' )
  print ( '' )
  print ( '       N       A       X       GPV      GEGENBAUER' )
  print ( '' )

  n_data = 0

  while ( True ):

    [ n_data, n, a, x, fx ] = gegenbauer_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    c = gegenbauer_poly ( n, a, x )
    fx2 = c[n];

    print ( '  %6d  %8g  %8g  %12g  %12g' % ( n, a, x, fx, fx2 ) )

  return

def gegenbauer_poly_values ( n_data ):

#*****************************************************************************80
#
## gegenbauer_poly_values() returns some values of the Gegenbauer polynomials.
#
#  Discussion:
#
#    The Gegenbauer polynomials are also known as the "spherical
#    polynomials" or "ultraspherical polynomials".
#
#    In Mathematica, the function can be evaluated by:
#
#      GegenbauerC[n,m,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order parameter of the function.
#
#    real A, the real parameter of the function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 38

  a_vec = np.array ( ( \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.0E+00, \
      1.0E+00, \
      2.0E+00, \
      3.0E+00, \
      4.0E+00, \
      5.0E+00, \
      6.0E+00, \
      7.0E+00, \
      8.0E+00, \
      9.0E+00, \
     10.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00 ))

  f_vec = np.array ( ( \
       1.0000000000E+00, \
       0.2000000000E+00, \
      -0.4400000000E+00, \
      -0.2800000000E+00, \
       0.2320000000E+00, \
       0.3075200000E+00, \
      -0.0805760000E+00, \
      -0.2935168000E+00, \
      -0.0395648000E+00, \
       0.2459712000E+00, \
       0.1290720256E+00, \
       0.0000000000E+00, \
      -0.3600000000E+00, \
      -0.0800000000E+00, \
       0.8400000000E+00, \
       2.4000000000E+00, \
       4.6000000000E+00, \
       7.4400000000E+00, \
      10.9200000000E+00, \
      15.0400000000E+00, \
      19.8000000000E+00, \
      25.2000000000E+00, \
      -9.0000000000E+00, \
      -0.1612800000E+00, \
      -6.6729600000E+00, \
      -8.3750400000E+00, \
      -5.5267200000E+00, \
       0.0000000000E+00, \
       5.5267200000E+00, \
       8.3750400000E+00, \
       6.6729600000E+00, \
       0.1612800000E+00, \
      -9.0000000000E+00, \
     -15.4252800000E+00, \
      -9.6969600000E+00, \
      22.4409600000E+00, \
     100.8892800000E+00, \
     252.0000000000E+00 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  2, \
     2,  2,  2, \
     2,  2,  2, \
     2,  2,  2, \
     2,  5,  5, \
     5,  5,  5, \
     5,  5,  5, \
     5,  5,  5, \
     5,  5,  5, \
     5,  5 ))

  x_vec = np.array ( ( \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
     -0.50E+00, \
     -0.40E+00, \
     -0.30E+00, \
     -0.20E+00, \
     -0.10E+00, \
      0.00E+00, \
      0.10E+00, \
      0.20E+00, \
      0.30E+00, \
      0.40E+00, \
      0.50E+00, \
      0.60E+00, \
      0.70E+00, \
      0.80E+00, \
      0.90E+00, \
      1.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, a, x, f

def gegenbauer_poly_values_test ( ):

#*****************************************************************************80
#
## gegenbauer_poly_values_test() tests gegenbauer_poly_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'gegenbauer_poly_values_test():' )
  print ( '  gegenbauer_poly_values() stores values of the Gegenbauer polynomials.' )
  print ( '' )
  print ( '      N            A         X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, a, x, fx = gegenbauer_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %12f  %24.16g' % ( n, a, x, fx ) )

  return

def gen_hermite_poly ( n, x, mu ):

#*****************************************************************************80
#
## gen_hermite_poly() evaluates the generalized Hermite polynomials at X.
#
#  Discussion:
#
#    The generalized Hermite polynomials are orthogonal under the weight
#    function:
#
#      w(x) = |x|^(2*MU) * exp ( - x^2 )
#
#    over the interval (-oo,+oo).
#
#    When MU = 0, the generalized Hermite polynomial reduces to the standard
#    Hermite polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Theodore Chihara,
#    An Introduction to Orthogonal Polynomials,
#    Gordon and Breach, 1978,
#    ISBN: 0677041500,
#    LC: QA404.5 C44.
#
#  Input:
#
#    integer N, the highest order polynomial to compute.
#
#    real X, the point at which the polynomials are
#    to be evaluated.
#
#    real MU, the parameter.
#    - 1 / 2 < MU.
#
#    real P(1:N+1), the values of the first N+1
#    polynomials at the point X.
#
  import numpy as np

  p = np.zeros ( n + 1 )

  p[0] = 1.0

  if ( 0 < n ):
 
    p[1] = 2.0 * x

    for i in range ( 1, n ):
 
      if ( ( i % 2 ) == 0 ):
        theta = 0.0
      else:
        theta = 2.0 * mu

      p[i+1] = 2.0 * x * p[i] - 2.0 * ( i + theta ) * p[i-1]

  return p

def gen_hermite_poly_test ( ):

#*****************************************************************************80
#
## gen_hermite_poly_test() tests gen_hermite_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10

  mu_test = np.array ( ( 0.0, 0.0, 0.1, 0.1, 0.5, 1.0 ) );
  x_test = np.array ( ( 0.0, 1.0, 0.0, 0.5, 0.5, 0.5 ) )

  print ( '' )
  print ( 'gen_hermite_poly_test():' )
  print ( '  gen_hermite_poly() evaluates the generalized Hermite polynomial.' )

  for i in range ( 0, 6 ):

    x = x_test[i]
    mu = mu_test[i]

    print ( '' )
    print ( '  Table of H(N,MU)(X) for' )
    print ( '' )
    print ( '    N(max) = %d' % ( n ) )
    print ( '    MU =     %f' % ( mu ) )
    print ( '    X =      %f' % ( x ) )
    print ( '' )
  
    c = gen_hermite_poly ( n, x, mu )
 
    for j in range ( 0, n + 1 ):
      print ( '  %4d  %12f' % ( j, c[j] ) )

  return

def gen_laguerre_poly ( n, alpha, x ):

#*****************************************************************************80
#
## gen_laguerre_poly() evaluates generalized Laguerre polynomials.
#
#  Differential equation:
#
#    X * Y'' + (ALPHA+1-X) * Y' + N * Y = 0
#
#  Recursion:
#
#    L(0,ALPHA)(X) = 1
#    L(1,ALPHA)(X) = 1+ALPHA-X
#
#    L(N,ALPHA)(X) = ( (2*N-1+ALPHA-X) * L(N-1,ALPHA)(X) 
#                   - (N-1+ALPHA) * L(N-2,ALPHA)(X) ) / N
#
#  Restrictions:
#
#    -1 < ALPHA
#
#  Special values:
#
#    For ALPHA = 0, the generalized Laguerre polynomial L(N,ALPHA)(X)
#    is equal to the Laguerre polynomial L(N)(X).
#
#    For ALPHA integral, the generalized Laguerre polynomial
#    L(N,ALPHA)(X) equals the associated Laguerre polynomial L(N,ALPHA)(X).
#
#  Norm:
#
#    Integral ( 0 <= X < Infinity ) exp ( - X ) * L(N,ALPHA)(X)**2 dX
#    = Gamma ( N + ALPHA + 1 ) / N!
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the highest order function to compute.
#
#    real ALPHA, the parameter.  -1 < ALPHA is required.
#
#    real X, the point at which the functions are to be
#    evaluated.
#
#    real CX(1:N+1), the polynomials of 
#    degrees 0 through N evaluated at the point X.
#
  import numpy as np

  if ( alpha <= -1.0 ):
    print ( '' )
    print ( 'gen_laguerre_poly(): Fatal error!' )
    print ( '  The input value of ALPHA is %f' % ( alpha ) )
    print ( '  but ALPHA must be greater than -1.' )
    raise Exception ( 'gen_laguerre_poly(): Fatal error!' )
 
  cx = np.zeros ( n + 1 )

  cx[0] = 1.0

  if ( 0 < n ):

    cx[1] = 1.0 + alpha - x

    for i in range ( 2, n ):
      cx[i] = ( ( float ( 2 * i - 1 ) + alpha - x ) * cx[i-1]     \
              + ( float (   - i + 1 ) - alpha     ) * cx[i-2] ) \
                / float (     i )

  return cx

def gen_laguerre_poly_test ( ):

#*****************************************************************************80
#
## gen_laguerre_poly_test() tests gen_laguerre_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10

  alpha_test = np.array ( ( 0.0, 0.0, 0.1, 0.1, 0.5, 1.0 ) );
  x_test = np.array ( ( 0.0, 1.0, 0.0, 0.5, 0.5, 0.5 ) )

  print ( '' )
  print ( 'gen_laguerre_poly_test():' )
  print ( '  gen_laguerre_poly() evaluates the generalized Laguerre polynomial.' )

  for i in range ( 0, 6 ):

    x = x_test[i]
    alpha = alpha_test[i]

    print ( '' )
    print ( '  Table of L(N,ALPHA)(X) for' )
    print ( '' )
    print ( '    N(max) = %d' % ( n ) )
    print ( '    ALPHA =  %f' % ( alpha ) )
    print ( '    X =      %f' % ( x ) )
    print ( '' )
  
    c = gen_laguerre_poly ( n, alpha, x )
 
    for j in range ( 0, n + 1 ):
      print ( '  %4d  %12f' % ( j, c[j] ) )

  return

def g_hofstadter ( n ):

#*****************************************************************************80
#
## g_hofstadter() computes the Hofstadter G sequence.
#
#  Discussion:
#
#    G(N) = 0                      if N = 0
#         = N - G ( G ( N - 1 ) ), otherwise.
#
#    G(N) is defined for all nonnegative integers.
#
#    The value of G(N) turns out to be related to the Zeckendorf
#    representation of N as a sum of non-consecutive Fibonacci numbers.
#    To compute G(N), determine the Zeckendorf representation:
#
#      N = sum ( 1 <= I <= M ) F(I)
#
#    and reduce the index of each Fibonacci number by 1:
#
#      G(N) = sum ( 1 <= I <= M ) F(I-1)
#
#    However, this is NOT how the computation is done in this routine.
#    Instead, a straightforward recursive function call is defined
#    to correspond to the definition of the mathematical function.
#
#  Table:
#
#     N  G(N)  Zeckendorf   Decremented
#    --  ----  ----------   -----------
#
#     1   1    1            1
#     2   1    2            1
#     3   2    3            2
#     4   3    3 + 1        2 + 1
#     5   3    5            3
#     6   4    5 + 1        3 + 1
#     7   4    5 + 2        3 + 1
#     8   5    8            5
#     9   6    8 + 1        5 + 1
#    10   6    8 + 2        5 + 1
#    11   7    8 + 3        5 + 2
#    12   8    8 + 3 + 1    5 + 2 + 1
#    13   8    13           8
#    14   9    13 + 1       8 + 1
#    15   9    13 + 2       8 + 1
#    16  10    13 + 3       8 + 2
#    17  11    13 + 3 + 1   8 + 2 + 1
#    18  11    13 + 5       8 + 3
#    19  12    13 + 5 + 1   8 + 3 + 1
#    20  12    13 + 5 + 2   8 + 3 + 1
#    21  13    21           13
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Douglas Hofstadter,
#    Goedel, Escher, Bach,
#    Basic Books, 1979.
#
#  Input:
#
#    integer N, the argument of the function.
#
#    integer VALUE, the value of the function.
#
  if ( n <= 0 ):
    value = 0
  else:
    value = n - g_hofstadter ( g_hofstadter ( n - 1 ) )

  return value

def g_hofstadter_test ( ):

#*****************************************************************************80
#
## g_hofstadter_test() tests g_hofstadter().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'g_hofstadter_test():' )
  print ( '  g_hofstadter() evaluates Hofstadter\'s recursive G function.' )
  print ( '' )
  print ( '     N   G(N)' )
  print ( '' )

  for i in range ( 0, 31 ):
    g = g_hofstadter ( i )
    print ( '  %6d  %6d' % ( i, g ) )

  return

def gud ( x ):

#*****************************************************************************80
#
## gud() evaluates the Gudermannian function.
#
#  Discussion:
#
#    The Gudermannian function relates the hyperbolic and trigonometric
#    functions.  For any argument X, there is a corresponding value
#    G so that
#
#      sinh(x) = tan(g).
#
#    The value G is called the Gudermannian of X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the Gudermannian.
#
#    real VALUE, the value of the Gudermannian.
#
  import numpy as np

  value = 2.0 * np.arctan ( np.tanh ( 0.5 * x ) )

  return value

def gud_test ( ):

#*****************************************************************************80
#
## gud_test() tests gud().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'gud_test():' )
  print ( '  gud() evaluates the Gudermannian function.' )
  print ( '' )
  print ( '     X      Exact F       GUD(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = gud_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = gud ( x )

    print ( '  %10.6f  %24.16f  %24.16f  %10.4g' % ( x, fx, fx2, abs ( fx - fx2 ) ) )

  return

def gud_values ( n_data ):

#*****************************************************************************80
#
## gud_values() returns some values of the Gudermannian function.
#
#  Discussion:
#
#    The Gudermannian function relates the hyperbolic and trigonomentric
#    functions.  For any argument X, there is a corresponding value
#    GD so that
#
#      SINH(X) = TAN(GD).
#
#    This value GD is called the Gudermannian of X and symbolized
#    GD(X).  The inverse Gudermannian function is given as input a value 
#    GD and computes the corresponding value X.
#
#    GD(X) = 2 * arctan ( exp ( X ) ) - PI / 2
#
#    In Mathematica, the function can be evaluated by:
#
#      2 * Atan[Exp[x]] - Pi/2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 13

  fx_vec = np.array ( ( \
     -0.1301760336046015E+01, \
     -0.8657694832396586E+00, \
      0.0000000000000000E+00, \
      0.9983374879348662E-01, \
      0.1986798470079397E+00, \
      0.4803810791337294E+00, \
      0.8657694832396586E+00, \
      0.1131728345250509E+01, \
      0.1301760336046015E+01, \
      0.1406993568936154E+01, \
      0.1471304341117193E+01, \
      0.1510419907545700E+01, \
      0.1534169144334733E+01 ) )

  x_vec = np.array ( ( \
     -2.0E+00, \
     -1.0E+00, \
      0.0E+00, \
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      1.5E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      3.5E+00, \
      4.0E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def gud_values_test ( ):

#*****************************************************************************80
#
## gud_value_test() tests gud_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'gud_values:' )
  print ( '  gud_values() stores values of the Gudermannian function.' )
  print ( '' )
  print ( '      X              GUD(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = gud_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )

  return

def hail ( n ):

#*****************************************************************************80
#
## hail() computes the hail function.
#
#  Discussion:
#
#    Starting with a positive integer N, we divide it by 2 if it is
#    even, or triple and add 1 if odd, and repeat this process until
#    reaching the value 1.  The number of times the process is carried
#    out is the value of the hail function for the given starting value.
#
#    Actually, HAIL is not well defined, since it is not known if
#    the above process actually terminates at 1 for every starting value N.
#
#  Example:
#
#     N  Sequence                                                  Hail
#
#     1                                                               0
#     2   1                                                           1
#     3  10,  5, 16,  8,  4,  2,  1                                   7
#     4   2   1                                                       2
#     5  16,  8,  4,  2,  1                                           5
#     6   3, 10,  5, 16,  8,  4,  2,  1                               8
#     7  22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1   16
#     8   4,  2,  1                                                   3
#     9  28, 14,  7, ...                                             19
#    10   5, 16,  8,  4,  2,  1                                       6
#    11  34, 17, 52, 26, 13, 40, 20, 10,  5, 16, 8, 4, 2, 1          14
#    12   6,  3, 10,  5, 16,  8,  4,  2,  1                           9
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the starting value for the hail sequence.
#
#    integer VALUE, the number of steps before the hail sequence 
#    reached 1.
#
  k = 0
  m = n

  if ( 0 < n ):

    while ( m != 1 ):
      k = k + 1
      if ( ( m % 2 ) == 0 ):
        m = ( m // 2 )
      else:
        m = 3 * m + 1

  value = k

  return value

def hail_test ( ):

#*****************************************************************************80
#
## hail_test() tests hail().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hail_test():' )
  print ( '  hail(I) computes the length of the hail sequence' )
  print ( '  for I, also known as the 3*N+1 sequence.' )
  print ( '' )
  print ( '     I   HAIL(I))' )
  print ( '' )

  for i in range ( 0, 21 ):
    h = hail ( i )
    print ( '  %6d  %6d' % ( i, h ) )

  return

def harmonic ( n ):

#*****************************************************************************80
#
## harmonic() evaluates a Harmonic sequence number.
#
#  Discussion:
#
#    H(N) = Sum ( 1 <= I <= N ) 1 / I
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the index of the harmonic number.
#
#  Output:
#
#    real VALUE, the value of the harmonic number.
#
  value = 0.0
  for i in range ( 1, n + 1 ):
    value = value + 1.0 / float ( i )

  return value

def harmonic_test ( ):

#*****************************************************************************80
#
## harmonic_test() tests harmonic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 May 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'harmonic_test():' )
  print ( '  harmonic() evaluates a harmonic sequence number.' )
  print ( '' )
  print ( '      N                      H(N)             H(N)' )
  print ( '                          tabulate            computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, h1 = harmonic_values ( n_data )

    if ( n_data == 0 ):
      break

    h2 = harmonic ( n )

    print ( '  %5d  %24.16g  %24.16g' % ( n, h1, h2 ) )

  return

def harmonic_estimate ( n ):

#*****************************************************************************80
#
## harmonic_estimate() estimates the Nth harmonic number.
#
#  Discussion:
#
#    H(N) = Sum ( 1 <= I <= N ) 1 / I
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the index of the harmonic number.
#
#  Output:
#
#    real VALUE: the estimated value of the harmonic number.
#
  import numpy as np

  value = np.log ( n ) + euler_mascheroni ( ) \
    + 0.5 / n \
    - 1.0 / 12.0 / n**2 \
    + 1.0 / 120.0 / n**4

  return value

def harmonic_estimate_test ( ):

#*****************************************************************************80
#
## harmonic_estimate_test() tests harmonic_estimate().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'harmonic_estimate_test():' )
  print ( '  harmonic_estimate() estimates a harmonic sequence number.' )
  print ( '' )
  print ( '      N                      H(N)                 H(N)             H(N)' )
  print ( '                          estimated           tabulated           computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, h2 = harmonic_values ( n_data )

    if ( n_data == 0 ):
      break

    h1 = harmonic_estimate ( n )

    h3 = harmonic ( n )

    print ( '  %5d  %24.16g  %24.16g  %24.16g' % ( n, h1, h2, h3 ) )

  return

def harmonic_values ( n_data ):

#*****************************************************************************80
#
## harmonic_values() returns some values of the Harmonic number sequence.
#
#  Discussion:
#
#    H(N) = sum ( 1 <= I <= N ) 1 / I
#
#    In Mathematica, the function can be evaluated by:
#
#      HarmonicNumber[n]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_data.  The user sets N_data to 0 before the first call.  
#
#  Output:
#
#    integer N_data.  On each call, the routine increments N_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_data will be 0 again.
#
#    integer N, the index of the Harmonic number.
#
#    real H, the value of the Harmonic number.
#
  import numpy as np

  n_max = 40

  n_vec = np.array ( ( \
     1, \
     2, \
     3, \
     4, \
     5, \
     6, \
     7, \
     8, \
     9, \
    10, \
    11, \
    12, \
    13, \
    14, \
    15, \
    16, \
    17, \
    18, \
    19, \
    20, \
    21, \
    22, \
    23, \
    24, \
    25, \
    26, \
    27, \
    28, \
    29, \
    30, \
    31, \
    32, \
    33, \
    34, \
    35, \
    36, \
    37, \
    38, \
    39, \
    40 ))

  h_vec = np.array ( ( \
    1.000000000000000, \
    1.500000000000000, \
    1.833333333333333, \
    2.083333333333333, \
    2.283333333333333, \
    2.450000000000000, \
    2.592857142857143, \
    2.717857142857143, \
    2.828968253968254, \
    2.928968253968254, \
    3.019877344877345, \
    3.103210678210678, \
    3.180133755133755, \
    3.251562326562327, \
    3.318228993228993, \
    3.380728993228993, \
    3.439552522640758, \
    3.495108078196313, \
    3.547739657143682, \
    3.597739657143682, \
    3.645358704762730, \
    3.690813250217275, \
    3.734291511086840, \
    3.775958177753507, \
    3.815958177753507, \
    3.854419716215045, \
    3.891456753252082, \
    3.927171038966368, \
    3.961653797587058, \
    3.994987130920391, \
    4.027245195436520, \
    4.058495195436520, \
    4.088798225739550, \
    4.118209990445433, \
    4.146781419016861, \
    4.174559196794639, \
    4.201586223821666, \
    4.227902013295350, \
    4.253543038936376, \
    4.278543038936376 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    h = 0.0
  else:
    n = n_vec[n_data]
    h = h_vec[n_data]
    n_data = n_data + 1

  return n_data, n, h

def harmonic_values_test ( ):

#*****************************************************************************80
#
## harmonic_values_test() tests harmonic_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 May 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'harmonic_values_test():' )
  print ( '  harmonic_values() stores values of the Harmonic number sequence.' )
  print ( '' )
  print ( '      N            H(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, h = harmonic_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %24.16f' % ( n, h ) )

  return

def hermite_poly_phys_coef ( n ):

#*****************************************************************************80
#
## hermite_poly_phys_coef(): coefficients of the physicist's Hermite polynomial H(n,x).
#
#  First terms:
#
#    N/K     0     1      2      3       4     5      6    7      8    9   10
#
#     0      1
#     1      0     2
#     2     -2     0      4
#     3      0   -12      0      8
#     4     12     0    -48      0      16
#     5      0   120      0   -160       0    32
#     6   -120     0    720      0    -480     0     64
#     7      0 -1680      0   3360       0 -1344      0   128
#     8   1680     0 -13440      0   13440     0  -3584     0    256
#     9      0 30240      0 -80640       0 48384      0 -9216      0 512
#    10 -30240     0 302400      0 -403200     0 161280     0 -23040   0 1024 
#
#  Recursion:
#
#    H(0,X) = 1,
#    H(1,X) = 2*X,
#    H(N,X) = 2*X * H(N-1,X) - 2*(N-1) * H(N-2,X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    real C(1:N+1,1:N+1), the coefficients of the Hermite
#    polynomials.
#
  import numpy as np

  c = np.zeros ( ( n + 1, n + 1 ) )

  c[0,0] = 1.0

  if ( 0 < n ):

    c[1,1] = 2.0
 
    for i in range ( 1, n ):
      c[i+1,0]     =  -2.0 * float ( i ) * c[i-1,0]
      for j in range ( 1, i ):
        c[i+1,j] =   2.0 * c[i,j-1] -2.0 * float ( i ) * c[i-1,j]
      c[i+1,i  ] =   2.0 * c[i  ,  i-1]
      c[i+1,i+1] =   2.0 * c[i  ,  i  ]

  return c

def hermite_poly_phys_coef_test ( ):

#*****************************************************************************80
#
## hermite_poly_phys_coef_test() tests hermite_poly_phys_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'hermite_poly_phys_coef_test():' )
  print ( '  hermite_poly_phys_coef() determines the Hermite' )
  print ( '  physicist\'s polynomial coefficients.' )

  c = hermite_poly_phys_coef ( n )
 
  for i in range ( 0, n + 1 ):
    print ( '' )
    print ( '  H(%d)' % ( i ) )
    print ( '' )
    for j in range ( i, -1, -1 ):
      if ( j == 0 ):
        print ( '    %f' % ( c[i,j] ) )
      elif ( j == 1 ):
        print ( '    %f * x' % ( c[i,j] ) )
      else:
        print ( '    %f * x^%d' % ( c[i,j], j ) )

  return

def hermite_poly_phys ( n, x ):

#*****************************************************************************80
#
## hermite_poly_phys() evaluates the Hermite polynomials at X.
#
#  Differential equation:
#
#    Y'' - 2 X Y' + 2 N Y = 0
#
#  First terms:
#
#      1
#      2 X
#      4 X^2     -  2
#      8 X^3     - 12 X
#     16 X^4     - 48 X^2     + 12
#     32 X^5    - 160 X^3    + 120 X
#     64 X^6    - 480 X^4    + 720 X^2    - 120
#    128 X^7   - 1344 X^5   + 3360 X^3   - 1680 X
#    256 X^8   - 3584 X^6  + 13440 X^4  - 13440 X^2   + 1680
#    512 X^9   - 9216 X^7  + 48384 X^5  - 80640 X^3  + 30240 X
#   1024 X^10 - 23040 X^8 + 161280 X^6 - 403200 X^4 + 302400 X^2 - 30240
#
#  Recursion:
#
#    H(0,X) = 1,
#    H(1,X) = 2*X,
#    H(N,X) = 2*X * H(N-1,X) - 2*(N-1) * H(N-2,X)
#
#  Norm:
#
#    Integral ( -oo < X < oo ) exp ( - X^2 ) * H(N,X)^2 dX
#    = sqrt ( pi ) * 2^N * N!
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    real X, the point at which the polynomials are to be evaluated.
#
#    real CX[0:N], the values of the first N+1 Hermite
#    polynomials at the point X.
#
  import numpy as np

  cx = np.zeros ( n + 1 )

  cx[0] = 1.0

  if ( 0 < n ):

    cx[1] = 2.0 * x
 
    for i in range ( 2, n + 1 ):
      cx[i] = 2.0 * x * cx[i-1] - 2.0 * ( i - 1 ) * cx[i-2]

  return cx

def hermite_poly_phys_test ( ):

#*****************************************************************************80
#
## hermite_poly_phys_test() tests hermite_poly_phys().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
 
  print ( '' )
  print ( 'hermite_poly_phys_test():' )
  print ( '  hermite_poly_phys() computes the Hermite physicist polynomials;' )
  print ( '' )
  print ( '       N      X        Exact F       H(N)(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = hermite_poly_phys_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = hermite_poly_phys ( n, x )

    print ( '  %2d  %12f  %14g  %14g' % ( n, x, fx, fx2[n] ) )

  return

def hermite_poly_phys_values ( n_data ):

#*****************************************************************************80
#
## hermite_poly_phys_values() returns some values of the physicist's Hermite polynomial.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      HermiteH[n,x]
#
#  Differential equation:
#
#    Y'' - 2 X Y' + 2 N Y = 0
#
#  First terms:
#
#      1
#      2 X
#      4 X^2     -  2
#      8 X^3     - 12 X
#     16 X^4     - 48 X^2     + 12
#     32 X^5    - 160 X^3    + 120 X
#     64 X^6    - 480 X^4    + 720 X^2    - 120
#    128 X^7   - 1344 X^5   + 3360 X^3   - 1680 X
#    256 X^8   - 3584 X^6  + 13440 X^4  - 13440 X^2   + 1680
#    512 X^9   - 9216 X^7  + 48384 X^5  - 80640 X^3  + 30240 X
#   1024 X^10 - 23040 X^8 + 161280 X^6 - 403200 X^4 + 302400 X^2 - 30240
#
#  Recursion:
#
#    H(0,X) = 1,
#    H(1,X) = 2*X,
#    H(N,X) = 2*X * H(N-1,X) - 2*(N-1) * H(N-2,X)
#
#  Norm:
#
#    Integral ( -oo < X < +oo ) exp ( - X^2 ) * H(N,X)^2 dX
#    = sqrt ( PI ) * 2^N * N!
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the polynomial.
#
#    real X, the point where the polynomial is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 18

  f_vec = np.array ( ( \
      0.1000000000000000E+01, \
      0.1000000000000000E+02, \
      0.9800000000000000E+02, \
      0.9400000000000000E+03, \
      0.8812000000000000E+04, \
      0.8060000000000000E+05, \
      0.7178800000000000E+06, \
      0.6211600000000000E+07, \
      0.5206568000000000E+08, \
      0.4212712000000000E+09, \
      0.3275529760000000E+10, \
      0.2432987360000000E+11, \
      0.1712370812800000E+12, \
      0.0000000000000000E+00, \
      0.4100000000000000E+02, \
     -0.8000000000000000E+01, \
      0.3816000000000000E+04, \
      0.3041200000000000E+07 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  5,  5, \
     5,  5,  5 ))

  x_vec = np.array ( ( \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     5.0E+00, \
     0.0E+00, \
     0.5E+00, \
     1.0E+00, \
     3.0E+00, \
     1.0E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def hermite_poly_phys_values_test ( ):

#*****************************************************************************80
#
## hermite_poly_phys_values_test() tests hermite_poly_phys_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hermite_poly_phys_values_test():' )
  print ( '  hermite_poly_phys_values() stores values of the Hermite physicist polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = hermite_poly_phys_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )

  return

def h_hofstadter ( n ):

#*****************************************************************************80
#
## h_hofstadter() computes the Hofstadter H sequence.
#
#  Discussion:
#
#    H(N) = 0                          if N = 0
#         = N - H ( H ( H ( N - 1 ) ), otherwise.
#
#    H(N) is defined for all nonnegative integers.
#
#  Table:
#
#     N  H(N)
#    --  ----
#
#     0     0
#     1     1
#     2     1
#     3     2
#     4     3
#     5     4
#     6     4
#     7     5
#     8     5
#     9     6
#    10     7
#    11     7
#    12     8
#    13     9
#    14    10
#    15    10
#    16    11
#    17    12
#    18    13
#    19    13
#    20    14
#    21    14
#    22    15
#    23    16
#    24    17
#    25    17
#    26    18
#    27    18
#    28    19
#    29    20
#    30    20
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Douglas Hofstadter,
#    Goedel, Escher, Bach,
#    Basic Books, 1979.
#
#  Input:
#
#    integer N, the argument of the function.
#
#    integer VALUE, the value of the function.
#
  if ( n <= 0 ):
    value = 0
  else:
    value = n - h_hofstadter ( h_hofstadter ( h_hofstadter ( n - 1 ) ) )

  return value

def h_hofstadter_test ( ):

#*****************************************************************************80
#
## h_hofstadter_test() tests h_hofstadter().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'h_hofstadter_test():' )
  print ( '  h_hofstadter() evaluates Hofstadter\'s recursive G function.' )
  print ( '' )
  print ( '     N   G(N)' )
  print ( '' )

  for i in range ( 0, 31 ):
    value = h_hofstadter ( i )
    print ( '  %6d  %6d' % ( i, value ) )

  return

def hyper_2f1_values ( n_data ):

#*****************************************************************************80
#
## hyper_2f1_values() returns some values of the hypergeometric 2f1 function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      fx = Hypergeometric2f1 [ a, b, c, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996,
#    ISBN: 0-8493-2479-3,
#    LC: QA47.M315.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real A, B, C, X, the parameter values.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 24

  a_vec = np.array ( ( \
   -2.5, \
   -0.5, \
    0.5, \
    2.5, \
   -2.5, \
   -0.5, \
    0.5, \
    2.5, \
   -2.5, \
   -0.5, \
    0.5, \
    2.5, \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    3.3, \
    1.1, \
    1.1, \
    3.3 ))

  b_vec = np.array ( ( \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7 ))

  c_vec = np.array ( ( \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
   -5.5, \
   -0.5, \
    0.5, \
    4.5, \
   -5.5, \
   -0.5, \
    0.5, \
    4.5, \
   -5.5, \
   -0.5, \
    0.5, \
    4.5 ))

  f_vec = np.array ( ( \
    0.72356129348997784913, \
    0.97911109345277961340, \
    1.0216578140088564160, \
    1.4051563200112126405, \
    0.46961431639821611095, \
    0.95296194977446325454, \
    1.0512814213947987916, \
    2.3999062904777858999, \
    0.29106095928414718320, \
    0.92536967910373175753, \
    1.0865504094806997287, \
    5.7381565526189046578, \
    15090.669748704606754, \
   -104.31170067364349677, \
    21.175050707768812938, \
    4.1946915819031922850, \
    1.0170777974048815592E+10, \
   -24708.635322489155868, \
    1372.2304548384989560, \
    58.092728706394652211, \
    5.8682087615124176162E+18, \
   -4.4635010147295996680E+08, \
    5.3835057561295731310E+06, \
    20396.913776019659426 ))

  x_vec = np.array ( ( \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.55, \
    0.55, \
    0.55, \
    0.55, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.55, \
    0.55, \
    0.55, \
    0.55, \
    0.85, \
    0.85, \
    0.85, \
    0.85 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0
    b = 0
    c = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    c = c_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, c, x, f

def hyper_2f1_values_test ( ):

#*****************************************************************************80
#
## hyper_2f1_values_test() tests hyper_2f1_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hyper_2f1_values_test():' )
  print ( '  hyper_2f1_values() stores values of the hypergeometric function 2f1' )
  print ( '' )
  print ( '     A     B        C           X               F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, c, x, f = hyper_2f1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %4d  %12f  %12f  %24.16g' % ( a, b, c, x, f ) )

  return

def i4_choose ( n, k ):

#*****************************************************************************80
#
## i4_choose() computes the binomial coefficient C(N,K) as an I4.
#
#  Discussion:
#
#    The value is calculated in such a way as to avoid overflow and
#    roundoff.  The calculation is done in integer arithmetic.
#
#    The formula used is:
#
#      C(N,K) = N! / ( K! * (N-K)! )
#
#    Instead of i4_choose(), you could use scipy.special.comb ( n, k ),
#    except that that function uses real arithmetic.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    ML Wolfson, HV Wright,
#    Algorithm 160:
#    Combinatorial of M Things Taken N at a Time,
#    Communications of the ACM,
#    Volume 6, Number 4, April 1963, page 161.
#
#  Input:
#
#    integer N, K, are the values of N and K.
#
#  Output:
#
#    integer VALUE, the number of combinations of N
#    things taken K at a time.
#
  mn = min ( k, n - k )
  mx = max ( k, n - k )

  if ( mn < 0 ):

    value = 0

  elif ( mn == 0 ):

    value = 1

  else:

    value = mx + 1

    for i in range ( 2, mn + 1 ):
      value = ( value * ( mx + i ) ) // i

  return value

def i4_choose_test ( ):

#*****************************************************************************80
#
## i4_choose_test() tests i4_choose().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_choose_test():' )
  print ( '  i4_choose() evaluates C(N,K).' )
  print ( '' )
  print ( '       N       K     CNK' )

  for n in range ( 0, 5 ):
    print ( '' )
    for k in range ( 0, n + 1 ):
      cnk = i4_choose ( n, k )

      print ( '  %6d  %6d  %6d' % ( n, k, cnk ) )

  return

def i4_factorial2 ( n ) :

#*****************************************************************************80
#
## i4_factorial2() computes the double factorial function.
#
#  Discussion:
#
#    FACTORIAL2( N ) = Product ( N * (N-2) * (N-4) * ... * 2 )  (N even)
#                    = Product ( N * (N-2) * (N-4) * ... * 1 )  (N odd)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the argument of the double factorial function.
#    If N is less than 1, the value is returned as 1.
#
#    integer VALUE, the value of N!!.
#
  if ( n < 1 ):
    value = 1
    return value

  value = 1

  for i in range ( n, 1, -2 ):
    value = value * i

  return value

def i4_factorial2_test ( ):

#*****************************************************************************80
#
## i4_factorial2_test() tests i4_factorial2().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_factorial2_test():' )
  print ( '  i4_factorial2() evaluates the double factorial function.' )
  print ( '' )
  print ( '         N      Exact         i4_factorial2(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, f1 = i4_factorial2_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = i4_factorial2 ( n )

    print ( '  %8d  %12d  %12d' % ( n, f1, f2 ) ) 

  return

def i4_factorial2_values ( n_data ):

#*****************************************************************************80
#
## i4_factorial2_values() returns values of the double factorial function.
#
#  Formula:
#
#    FACTORIAL2( N ) = Product ( N * (N-2) * (N-4) * \ * 2 )  (N even)
#                    = Product ( N * (N-2) * (N-4) * \ * 1 )  (N odd)
#
#    In Mathematica, the function can be evaluated by:
#
#      n!!
#
#  Example:
#
#     N    N!!
#
#     0     1
#     1     1
#     2     2
#     3     3
#     4     8
#     5    15
#     6    48
#     7   105
#     8   384
#     9   945
#    10  3840
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996, page 16.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the function.
#
#    integer FN, the value of the function.
# 
  import numpy as np

  n_max = 16

  fn_vec = np.array ( ( 
          1, \
          1, \
          2, \
          3, \
          8, \
         15, \
         48, \
        105, \
        384, \
        945, \
       3840, \
      10395, \
      46080, \
     135135, \
     645120, \
    2027025 ) )

  n_vec = np.array ( ( 
    0, \
     1,  2,  3,  4,  5, \
     6,  7,  8,  9, 10, \
    11, 12, 13, 14, 15 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    fn = 0
  else:
    n = n_vec[n_data]
    fn = fn_vec[n_data]
    n_data = n_data + 1

  return n_data, n, fn

def i4_factorial2_values_test ( ):

#*****************************************************************************80
#
## i4_factorial2_values_test() tests i4_factorial2_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_factorial2_values_test():' )
  print ( '  i4_factorial2_values() returns values of the double factorial function.' )
  print ( '' )
  print ( '     N        N!!' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = i4_factorial2_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '%6d  %10d' % ( n, fn ) )

  return

def i4_factor ( n ):

#*****************************************************************************80
#
## i4_factor() factors an integer into prime factors.
#
#  Formula:
#
#    N = NLEFT * Product ( 1 <= I <= NFACTOR ) FACTOR(I)^POWER(I).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be factored.  N may be positive,
#    negative, or 0.
#
#    integer NFACTOR, the number of prime factors of N discovered
#    by the routine.
#
#    integer FACTOR(NFACTOR), the prime factors of N.
#
#    integer POWER(NFACTOR).  POWER(I) is the power of
#    the FACTOR(I) in the representation of N.
#
#    integer NLEFT, the factor of N that the routine could not
#    divide out.  If NLEFT is 1, then N has been completely factored.
#    Otherwise, NLEFT represents factors of N involving large primes.
#
  nfactor = 0
  factor = []
  power = []
  nleft = n

  if ( n == 0 ):
    return nfactor, factor, power, nleft

  if ( abs ( n ) == 1 ):
    nfactor = 1
    factor.append ( 1 )
    power.append ( 1 )
    return nfactor, factor, power, nleft
#
#  Find out how many primes we stored.
#
  maxprime = prime ( -1 )
#
#  Try dividing the remainder by each prime.
#
  for i in range ( 1, maxprime + 1 ):

    p = prime ( i )

    if ( ( ( abs ( nleft ) ) % p ) == 0 ):

      nfactor = nfactor + 1
      factor.append ( p )
      power.append ( 0 )

      while ( True ):

        power[nfactor-1] = power[nfactor-1] + 1
        nleft =  ( nleft // p )

        if ( ( ( abs ( nleft ) ) % p ) != 0 ):
          break

      if ( abs ( nleft ) == 1 ):
        break

  return nfactor, factor, power, nleft

def i4_factor_test ( ):

#*****************************************************************************80
#
## i4_factor_test() tests i4_factor().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n_test = [ 60, 664048, 8466763 ]

  print ( '' )
  print ( 'i4_factor_test():' )
  print ( '  i4_factor() tries to factor an I4.' )

  for i in range ( 0, 3 ):
    n = n_test[i]
    nfactor, factor, power, nleft = i4_factor ( n )
    print ( '' )
    print ( '  Factors of N = %d' % ( n ) )
    for j in range ( 0, nfactor ):
      print ( '    %d^%d' % ( factor[j], power[j] ) )
    if ( nleft != 1 ):
      print ( '  Unresolved factor NLEFT = %d' % ( nleft ) )

  return

def i4_is_fibonacci ( i4 ):

#*****************************************************************************80
#
## i4_is_fibonacci() reports whether an integer is a Fibonacci number.
#
#  Discussion:
#
#    The positive integer i4 is a Fibonacci number if and only if
#    5*I4^2+4 or 5*I4^2-4 is a perfect square.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the index of the Fibonacci number to compute.
#    N should be nonnegative.
#
#    integer F, the value of the N-th Fibonacci number.
#
  import numpy as np

  value = False
#
#  Must be an integer.
#
  if ( i4 != int ( i4 ) ):
    return value
#
#  Must be positive.
#
  if ( i4 <= 0 ):
    return value

  t1 = 5 * i4 ** 2 + 4
  t2 = np.sqrt ( t1 )
  t3 = int ( t2 )
  if ( t3 * t3 == t1 ):
    value = True
    return value

  t1 = 5 * i4 ** 2 - 4
  t2 = np.sqrt ( t1 )
  t3 = int ( t2 )
  if ( t3 * t3 == t1 ):
    value = True
    return value

  return value

def i4_is_fibonacci_test ( ):

#*****************************************************************************80
#
## i4_is_fibonacci_test() tests i4_is_fibonacci().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 10
  i4_test = np.array ( [ - 13, 0, 1, 8, 10, 50, 55, 100, 144, 200 ] )
  print ( '' )
  print ( 'i4_is_fibonacci_test():' )
  print ( '  i4_is_fibonacci returns T or F depending on' )
  print ( '  whether I4 is a Fibonacci number.' )
  print ( '' )
  print ( '   I4     T/F' )
  print ( '' )

  for i in range ( 0, test_num ):

    i4 = i4_test[i]
    l = i4_is_fibonacci ( i4 )
    print ( '  %4d    %s' % ( i4, l ) )

  return

def i4_is_prime ( n ) :

#*****************************************************************************80
#
## i4_is_prime() reports whether an I4 is prime.
#
#  Discussion:
#
#    A simple, unoptimized sieve of Erasthosthenes is used to
#    check whether N can be divided by any integer between 2
#    and SQRT(N).
#
#    Note that negative numbers, 0 and 1 are not considered prime.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer to be tested.
#
#    bool VALUE, is TRUE if N is prime, and FALSE
#    otherwise.
#
  import numpy as np

  if ( n <= 0 ):
    value = False
    return value

  if ( n == 1 ):
    value = False
    return value

  if ( n <= 3 ):
    value = True
    return value

  nhi = int ( np.sqrt ( float ( n ) ) )

  for i in range ( 2, nhi + 1 ):
    if ( ( n % i ) == 0 ):
      value = False
      return value

  value = True

  return value

def i4_is_prime_test ( ) :

#*****************************************************************************80
#
## i4_is_prime_test() tests i4_is_prime().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_is_prime_test():' )
  print ( '  i4_is_prime() reports whether an I4 is prime.' )
  print ( '' )
  print ( '         I  i4_is_prime(I)' )
  print ( '' )

  for i in range ( -2, 26 ):
    j = i4_is_prime ( i )
    print ( '  %8d  %r' % ( i, j ) )

  return

def i4_is_triangular ( i ) :

#*****************************************************************************80
#
## i4_is_triangular() determines whether an integer is triangular.
#
#  Discussion:
#
#    The N-th triangular number is equal to the sum of the first
#    N integers.
#
#  First Values:
#
#    Index  Value
#     0      0
#     1      1
#     2      3
#     3      6
#     4     10
#     5     15
#     6     21
#     7     28
#     8     36
#     9     45
#    10     55
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the integer to be checked.
#
#    boolean VALUE, is TRUE if I is triangular.
#
  if ( i < 0 ):

    value = False

  elif ( i == 0 ):

    value = True

  else:

    j, k = i4_to_triangle_lower ( i )

    if ( j == k ):
      value = True
    else:
      value = False

  return value

def i4_is_triangular_test ( ) :

#*****************************************************************************80
#
## i4_is_triangular_test() tests i4_is_triangular().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_is_triangular_test():' )
  print ( '  i4_is_triangular() reports whether an I4 is prime.' )
  print ( ' ' )
  print ( '         I  i4_is_triangular(I)' )
  print ( ' ' )

  for i in range ( 0, 21 ):
    j = i4_is_triangular ( i )
    print ( '  %8d  %r' % ( i, j ) )

  return

def i4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## i4mat_print() prints an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    integer A(M,N), the matrix.
#
#    string TITLE, a title.
#
  i4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def i4mat_print_test ( ):

#*****************************************************************************80
#
## i4mat_print_test() tests i4mat_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4mat_print_test():' )
  print ( '  i4mat_print() prints an I4MAT.' )

  m = 5
  n = 6
  a = np.array ( ( \
    ( 11, 12, 13, 14, 15, 16 ), \
    ( 21, 22, 23, 24, 25, 26 ), \
    ( 31, 32, 33, 34, 35, 36 ), \
    ( 41, 42, 43, 44, 45, 46 ), \
    ( 51, 52, 53, 54, 55, 56 ) ) )
  title = '  A 5 x 6 integer matrix:'
  i4mat_print ( m, n, a, title )

  return

def i4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## i4mat_print_some() prints out a portion of an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 10

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d  ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( ' %4d: ' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%7d  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def i4mat_print_some_test ( ):

#*****************************************************************************80
#
## i4mat_print_some_test() tests i4mat_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4mat_print_some_test():' )
  print ( '  i4mat_print_some() prints some of an I4MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11, 12, 13, 14, 15, 16 ], 
    [ 21, 22, 23, 24, 25, 26 ], 
    [ 31, 32, 33, 34, 35, 36 ], 
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = np.int32 )
  i4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is I4MAT, rows 0:2, cols 3:5:' )

  return

def i4_partition_distinct_count ( n ):

#*****************************************************************************80
#
## i4_partition_distinct_count() returns any value of Q(N).
#
#  Discussion:
#
#    A partition of an integer N is a representation of the integer
#    as the sum of nonzero positive integers.  The order of the summands
#    does not matter.  The number of partitions of N is symbolized
#    by P(N).  Thus, the number 5 has P(N) = 7, because it has the 
#    following partitions:
#
#    5 = 5
#      = 4 + 1 
#      = 3 + 2 
#      = 3 + 1 + 1 
#      = 2 + 2 + 1 
#      = 2 + 1 + 1 + 1 
#      = 1 + 1 + 1 + 1 + 1
#
#    However, if we require that each member of the partition
#    be distinct, we are computing something symbolized by Q(N).
#    The number 5 has Q(N) = 3, because it has the following partitions 
#    into distinct parts:
#
#    5 = 5
#      = 4 + 1 
#      = 3 + 2 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the integer to be partitioned.
#
#    integer VALUE, the number of partitions of the integer
#    into distinct parts.
#
  import numpy as np

  c = np.zeros ( n + 1 );

  c[0] = 1

  for i in range ( 1, n + 1 ):

    if ( i4_is_triangular ( i ) ):
      c[i] = 1
    else:
      c[i] = 0

    k = 0
    k_sign = -1

    while ( True ):

      k = k + 1
      k_sign = - k_sign
      k2 = k * ( 3 * k + 1 )

      if ( i < k2 ):
        break

      c[i] = c[i] + k_sign * c[i-k2]

    k = 0
    k_sign = -1

    while ( 1 ):

      k = k + 1
      k_sign = -k_sign
      k2 = k * ( 3 * k - 1 )

      if ( i < k2 ):
        break

      c[i] = c[i] + k_sign * c[i-k2]

  value = c[n]

  return value

def i4_partition_distinct_count_test ( ):

#*****************************************************************************80
#
## i4_partition_distinct_count_test() tests i4_partition_distinct_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_partition_distinct_count_test():' )
  print ( '  For the number of partitions of an integer' )
  print ( '  into distinct parts,' )
  print ( '  i4_partition_distinct_count() computes any value;' )
  print ( '' )
  print ( '     N       Exact F    Q(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = partition_distinct_count_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = i4_partition_distinct_count ( n )

    print ( '  %8d  %8d  %8d' % ( n, c, c2 ) )

  return

def i4_to_triangle_lower ( k ):

#*****************************************************************************80
#
## i4_to_triangle_lower() converts an integer to lower triangular coordinates.
#
#  Discussion:
#
#    Triangular coordinates are handy when storing a naturally triangular
#    array (such as the lower half of a matrix) in a linear array.
#
#    Thus, for example, we might consider storing
#
#    (1,1)
#    (2,1) (2,2)
#    (3,1) (3,2) (3,3)
#    (4,1) (4,2) (4,3) (4,4)
#
#    as the linear array
#
#    (1,1) (2,1) (2,2) (3,1) (3,2) (3,3) (4,1) (4,2) (4,3) (4,4)
#
#    Here, the quantities in parenthesis represent the natural row and
#    column indices of a single number when stored in a rectangular array.
#
#    In this routine, we are given the location K of an item in the
#    linear array, and wish to determine the row I and column J
#    of the item when stored in the triangular array.
#
#  First Values:
#
#     K  I  J
#
#     0  0  0
#     1  1  1
#     2  2  1
#     3  2  2
#     4  3  1
#     5  3  2
#     6  3  3
#     7  4  1
#     8  4  2
#     9  4  3
#    10  4  4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer K, the linear index of the (I,J) element, which
#    must be nonnegative.
#
#    integer I, J, the row and column indices.
#
  import numpy as np

  if ( k < 0 ):
    print ( '' )
    print ( 'i4_to_triangle_lower(): Fatal error!' )
    print ( '  K < 0.' )
    print ( '  K = %d' % ( k ) )
    raise Exception ( 'i4_to_triangle_lower(): Fatal error!' )

  if ( k == 0 ):
    i = 0
    j = 0
  else:
    i = int ( np.sqrt ( float ( 2 * k ) ) )

    if ( i * i + i < 2 * k ):
      i = i + 1

    j = k - ( i * ( i - 1 ) ) // 2

  return i, j

def i4_to_triangle_lower_test ( ):

#*****************************************************************************80
#
## i4_to_triangle_lower_test() tests i4_to_triangle_lower().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_to_triangle_lower_test():' )
  print ( '  i4_to_triangle_lower() converts a linear index to a lower triangular one.' )
  print ( '' )
  print ( '     K  ==>  ( I  J )' )
  print ( '' )

  for k in range ( 1, 21 ):
 
    i, j = i4_to_triangle_lower ( k )

    print ( '  %4d    %4d  %4d' % ( k, i, j )   )    

  return

def i4_to_triangle_upper ( k ):

#*****************************************************************************80
#
## i4_to_triangle_upper() converts an integer to upper triangular coordinates.
#
#  Discussion:
#
#    Triangular coordinates are handy when storing a naturally triangular
#    array (such as the upper half of a matrix) in a linear array.
#
#    Thus, for example, we might consider storing
#
#    (1,1) (1,2) (1,3) (1,4)
#          (2,2) (2,3) (2,4)
#                (3,3) (3,4)
#                      (4,4)
#
#    as the linear array
#
#    (1,1) (1,2) (2,2) (1,3) (2,3) (3,3) (1,4) (2,4) (3,4) (4,4)
#
#    Here, the quantities in parenthesis represent the natural row and
#    column indices of a single number when stored in a rectangular array.
#
#    In this routine, we are given the location K of an item in the
#    linear array, and wish to determine the row I and column J
#    of the item when stored in the triangular array.
#
#  First Values:
#
#     K  I  J
#
#     0  0  0
#     1  1  1
#     2  1  2
#     3  2  2
#     4  1  3
#     5  2  3
#     6  3  3
#     7  1  4
#     8  2  4
#     9  3  4
#    10  4  4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer K, the linear index of the (I,J) element, which
#    must be nonnegative.
#
#    integer I, J, the row and column indices.
#
  import numpy as np

  if ( k < 0 ):
    print ( '' )
    print ( 'i4_to_triangle_upper(): Fatal error!' )
    print ( '  K < 0.' )
    print ( '  K = %d' % ( k ) )
    raise Exception ( 'i4_to_triangle_upper(): Fatal error!' )

  if ( k == 0 ):
    i = 0
    j = 0
  else:
    j = int ( np.sqrt ( float ( 2 * k ) ) )

    if ( j * j + j < 2 * k ):
      j = j + 1

    i = k - ( j * ( j - 1 ) ) // 2

  return i, j

def i4_to_triangle_upper_test ( ):

#*****************************************************************************80
#
## i4_to_triangle_upper_test() tests i4_to_triangle_upper().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 March 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_to_triangle_upper_test():' )
  print ( '  i4_to_triangle_upper() converts a linear index to an upper triangular one.' )
  print ( '' )
  print ( '     K  ==>  ( I  J )' )
  print ( '' )

  for k in range ( 1, 21 ):
 
    i, j = i4_to_triangle_upper ( k )

    print ( '  %4d    %4d  %4d' % ( k, i, j )   )    

  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_print() prints an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
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
## i4vec_print_test() tests i4vec_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'i4vec_print_test():' )
  print ( '  i4vec_print() prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )

  return

def jacobi_poly ( n, alpha, beta, x ):

#*****************************************************************************80
#
## jacobi_poly() evaluates the Jacobi polynomials at X.
#
#  Differential equation:
#
#    (1-X*X) Y'' + (BETA-ALPHA-(ALPHA+BETA+2) X) Y' + N (N+ALPHA+BETA+1) Y = 0
#
#  Recursion:
#
#    P(0,ALPHA,BETA,X) = 1,
#
#    P(1,ALPHA,BETA,X) = ( (2+ALPHA+BETA)*X + (ALPHA-BETA) ) / 2
#
#    P(N,ALPHA,BETA,X)  = 
#      ( 
#        (2*N+ALPHA+BETA-1) 
#        * ((ALPHA**2-BETA**2)+(2*N+ALPHA+BETA)*(2*N+ALPHA+BETA-2)*X) 
#        * P(N-1,ALPHA,BETA,X)
#        -2*(N-1+ALPHA)*(N-1+BETA)*(2*N+ALPHA+BETA) * P(N-2,ALPHA,BETA,X)
#      ) / 2*N*(N+ALPHA+BETA)*(2*N-2+ALPHA+BETA)
#
#  Restrictions:
#
#    -1 < ALPHA
#    -1 < BETA
#
#  Norm:
#
#    Integral ( -1 <= X <= 1 ) ( 1 - X )^ALPHA * ( 1 + X )^BETA 
#      * P(N,ALPHA,BETA,X)^2 dX 
#    = 2^(ALPHA+BETA+1) * Gamma ( N + ALPHA + 1 ) * Gamma ( N + BETA + 1 ) /
#      ( 2 * N + ALPHA + BETA ) * N! * Gamma ( N + ALPHA + BETA + 1 )
#
#  Special values:
#
#    P(N,ALPHA,BETA)(1) = (N+ALPHA)!/(N!*ALPHA!) for integer ALPHA.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the highest order polynomial to compute.  Note
#    that polynomials 0 through N will be computed.
#
#    real ALPHA, one of the parameters defining the Jacobi
#    polynomials, ALPHA must be greater than -1.
#
#    real BETA, the second parameter defining the Jacobi
#    polynomials, BETA must be greater than -1.
#
#    real X, the point at which the polynomials are to be evaluated.
#
#    real CX(1:N+1), the values of the first N+1 Jacobi
#    polynomials at the point X.
#
  import numpy as np

  if ( alpha <= -1.0 ):
    print ( '' )
    print ( 'jacobi_poly(): Fatal error!' )
    print ( '  Illegal input value of ALPHA = %f' % ( alpha ) )
    print ( '  But ALPHA must be greater than -1.' )
    raise Exception ( 'jacobi_poly(): Fatal error!' )
 
  if ( beta <= -1.0 ):
    print ( '' )
    print ( 'jacobi_poly(): Fatal error!' )
    print ( '  Illegal input value of BETA = %f' % ( beta ) )
    print ( '  But BETA must be greater than -1.' )
    raise Exception ( 'jacobi_poly(): Fatal error!' )
  
  cx = np.zeros ( n + 1 );

  cx[0] = 1.0

  if ( 0 < n ):

    cx[1] = ( 1.0 + 0.5 * ( alpha + beta ) ) * x  + 0.5 * ( alpha - beta );
 
    for i in range ( 2, n + 1 ):

      c1 = 2 * i * ( i + alpha + beta ) * ( 2 * i - 2 + alpha + beta )

      c2 = ( 2 * i - 1 + alpha + beta ) * ( 2 * i + alpha + beta ) \
        * ( 2 * i - 2 + alpha + beta )

      c3 = ( 2 * i - 1 + alpha + beta ) * ( alpha + beta ) * ( alpha - beta )

      c4 = - 2 * ( i - 1 + alpha ) * ( i - 1 + beta )  * ( 2 * i + alpha + beta )

      cx[i] = ( ( c3 + c2 * x ) * cx[i-1] + c4 * cx[i-2] ) / c1

  return cx

def jacobi_poly_test ( ):

#*****************************************************************************80
#
## jacobi_poly_test() tests jacobi_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'jacobi_poly_test():' )
  print ( '  jacobi_poly() computes values of the Jacobi polynomial.' )
  print ( '' )
  print ( '       N       A       B        X       GPV      JACOBI' )
  print ( '' )

  n_data = 0

  while ( True ):

    [ n_data, n, a, b, x, fx ] = jacobi_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    c = jacobi_poly ( n, a, b, x )
    fx2 = c[n];

    print ( '  %6d  %8g  %8g  %8g  %12g  %12g' % ( n, a, b, x, fx, fx2 ) )

  return

def jacobi_poly_values ( n_data ):

#*****************************************************************************80
#
## jacobi_poly_values() returns some values of the Jacobi polynomial.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      JacobiP[ n, a, b, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the degree of the polynomial.
#
#    real A, B, parameters of the function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 26

  a_vec = np.array ( (\
     0.0, 0.0, 0.0, 0.0, \
     0.0, 0.0, 1.0, 2.0, \
     3.0, 4.0, 5.0, 0.0, \
     0.0, 0.0, 0.0, 0.0, \
     0.0, 0.0, 0.0, 0.0, \
     0.0, 0.0, 0.0, 0.0, \
     0.0, 0.0 ))

  b_vec = np.array ( (\
    1.0, 1.0, 1.0, 1.0, \
    1.0, 1.0, 1.0, 1.0, \
    1.0, 1.0, 1.0, 2.0, \
    3.0, 4.0, 5.0, 1.0, \
    1.0, 1.0, 1.0, 1.0, \
    1.0, 1.0, 1.0, 1.0, \
    1.0, 1.0 ))

  f_vec = np.array ( (\
      1.000000000000000, \
      0.2500000000000000, \
     -0.3750000000000000, \
     -0.4843750000000000, \
     -0.1328125000000000, \
      0.2753906250000000, \
     -0.1640625000000000, \
     -1.174804687500000, \
     -2.361328125000000, \
     -2.616210937500000, \
      0.1171875000000000, \
      0.4218750000000000, \
      0.5048828125000000, \
      0.5097656250000000, \
      0.4306640625000000, \
     -6.000000000000000, \
      0.03862000000000000, \
      0.8118400000000000, \
      0.03666000000000000, \
     -0.4851200000000000, \
     -0.3125000000000000, \
      0.1891200000000000, \
      0.4023400000000000, \
      0.01216000000000000, \
     -0.4396200000000000, \
      1.000000000000000 ))

  n_vec = np.array ( (\
     0, 1, 2, 3, \
     4, 5, 5, 5, \
     5, 5, 5, 5, \
     5, 5, 5, 5, \
     5, 5, 5, 5, \
     5, 5, 5, 5, \
     5, 5 ))

  x_vec = np.array ( (\
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
     -1.0, \
     -0.8, \
     -0.6, \
     -0.4, \
     -0.2, \
      0.0, \
      0.2, \
      0.4, \
      0.6, \
      0.8, \
      1.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    a = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, a, b, x, f

def jacobi_poly_values_test ( ):

#*****************************************************************************80
#
## jacobi_poly_values_test() tests jacobi_poly_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'jacobi_poly_values_test():' )
  print ( '  jacobi_poly_values() stores values of the Jacobi polynomials.' )
  print ( '' )
  print ( '       N        A             B             X              F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, a, b, x, f = jacobi_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %12f  %12f  %24.16g' % ( n, a, b, x, f ) )

  return

def jacobi_symbol ( q, p ):

#*****************************************************************************80
#
## jacobi_symbol() evaluates the Jacobi symbol (Q/P).
#
#  Definition:
#
#    If P is prime, then
#
#      Jacobi Symbol (Q/P) = Legendre Symbol (Q/P)
#
#    Else 
#
#      let P have the prime factorization
#
#        P = Product ( 1 <= I <= N ) P(I)^E(I)
#
#      Jacobi Symbol (Q/P) =
#
#        Product ( 1 <= I <= N ) Legendre Symbol (Q/P(I))^E(I)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996, pages 86-87.
#
#  Input:
#
#    integer Q, an integer whose Jacobi symbol with
#    respect to P is desired.
#
#    integer P, the number with respect to which the Jacobi
#    symbol of Q is desired.  P should be 2 or greater.
#
#    integer J, the Jacobi symbol (Q/P).
#    Ordinarily, J will be -1, 0 or 1.
#    -2, not enough factorization space.
#    -3, an error during Legendre symbol calculation.
#

#
#  P must be greater than 1.
#
  if ( p <= 1 ):
    print ( '' )
    print ( 'jacobi_symbol(): Fatal error!' )
    print ( '  P must be greater than 1.' )
    j = -2
    return l
#
#  Decompose P into factors of prime powers.
#
  nfactor, factor, power, nleft = i4_factor ( p )

  if ( nleft != 1 ):
    print ( '' )
    print ( 'jacobi_symbol(): Fatal error!' )
    print ( '  Not enough factorization space.' )
    j = -2
    return j
#
#  Force Q to be nonnegative.
#
  qq = q

  while ( qq < 0 ):
    qq = qq + p
#
#  For each prime factor, compute the Legendre symbol, and
#  multiply the Jacobi symbol by the appropriate factor.
#
  j = 1
  for i in range ( 0, nfactor ):
    pp = factor[i]
    l = legendre_symbol ( qq, pp )
    if ( l < -1 ):
      print ( '' )
      print ( 'jacobi_symbol(): Fatal error!' )
      print ( '  Error during Legendre symbol calculation.' )
      j = -3

    j = j * l ** power[i]

  return j

def jacobi_symbol_test ( ):

#*****************************************************************************80
#
## jacobi_symbol_test_test() tests jacobi_symbol_test().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  ntest = 4
  ptest = [ 3, 9, 10, 12 ]

  print ( '' )
  print ( 'jacobi_symbol_test():' )
  print ( '  jacobi_symbol() computes the Jacobi symbol' )
  print ( '  (Q/P) which records whether Q is' )
  print ( '  a quadratic residue modulo the number P.' )

  for i in range ( 0, ntest ):
    p = ptest[i]
    print ( '' )
    print ( '  Jacobi Symbols for P = %d' % ( p ) )
    print ( '' )
    for q in range ( 0, p + 1 ):
      l = jacobi_symbol ( q, p )
      print ( '  %6d  %6d  %6d' % ( p, q, l ) )

  return

def krawtchouk ( n, p, x, m ):

#*****************************************************************************80
#
## krawtchouk() evaluates the Krawtchouk polynomials at X.
#
#  Discussion:
#
#    The polynomial has a parameter P, which must be strictly between
#    0 and 1, and a parameter M which must be a nonnegative integer.
#
#    The Krawtchouk polynomial of order N, with parameters P and M,
#    evaluated at X, may be written K(N,P,X,M).
#
#    The first two terms are:
#
#      K(0,P,X,M) = 1
#      K(1,P,X,M) = X - P * M
#
#    and the recursion, for fixed P and M is
#
#                             ( N + 1 ) * K(N+1,P,X,M) =
#        ( X - ( N + P * ( M - 2 * N))) * K(N,  P,X,M)
#       - ( M - N + 1 ) * P * ( 1 - P ) * K(N-1,P,X,M)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Walter Gautschi,
#    Orthogonal Polynomials: Computation and Approximation,
#    Oxford, 2004,
#    ISBN: 0-19-850672-4,
#    LC: QA404.5 G3555.
#
#  Input:
#
#    integer N, the highest order polynomial to evaluate.
#    0 <= N.
#
#    real P, the parameter.  0 < P < 1.
#
#    real X, the evaluation parameter.
#
#    integer M, the parameter.  0 <= M.
#
#    real V[0:N], the values of the Krawtchouk polynomials
#    of orders 0 through N at X.
#
  import numpy as np

  v = []

  if ( n < 0 ):
    print ( '' )
    print ( 'krawtchouk(): Fatal error!' )
    print ( '  0 <= N is required.' )
    return v

  if ( p <= 0.0 or 1.0 <= p ):
    print ( '' )
    print ( 'krawtchouk(): Fatal error!' )
    print ( '  0 < P < 1 is required.' )
    return v

  if ( m < 0 ):
    print ( '' )
    print ( 'krawtchouk(): Fatal error!' )
    print ( '  0 <= M is required.' )
    return v

  v = np.zeros ( n + 1 )

  v[0] = 1.0

  if ( 1 <= n ):

    v[1] = x - p * m

    for i in range ( 1, n ):
      v[i+1] = ( ( x - float ( i + p * ( m - 2 * i ) ) )       * v[i] \
                     - float ( ( m - i + 1 ) * p * ( 1 - p ) ) * v[i-1]  ) \
                     / float ( i + 1 )

  return v

def krawtchouk_test ( ):

#*****************************************************************************80
#
## krawtchouk_test() tests krawtchouk().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 2
  p_test = np.array ( ( 0.25, 0.5 ) )
  m = 5

  print ( '' )
  print ( 'krawtchouk_test():' )
  print ( '  krawtchouk() computes Krawtchouk polynomials;' )
  print ( '' )
  print ( '         N      P         X          M     K(N,P,X,M)' )

  for test in range ( 0, test_num ):

    n = 5
    p = p_test[test]

    print ( '' )

    for j in range ( 0, 6 ):

      x = float ( j ) / 2.0

      value = krawtchouk ( n, p, x, m )

      print ( '' )

      for i in range ( 0, n + 1 ):

        print ( '  %8d  %8f  %8f  %8d  %14f' % ( i, p, x, m, value[i] ) )

  return

def laguerre_associated ( n, m, x ):

#*****************************************************************************80
#
## laguerre_associated() evaluates the associated Laguerre polynomials L(N,M)(X) at X.
#
#  Differential equation:
#
#    X Y'' + (M+1-X) Y' + (N-M) Y = 0
#
#  First terms:
#
#    M = 0
#
#    L(0,0)(X) =   1
#    L(1,0)(X) =  -X    +  1
#    L(2,0)(X) =   X^2 -  4 X     +  2
#    L(3,0)(X) =  -X^3 +  9 X^2 -  18 X    +    6
#    L(4,0)(X) =   X^4 - 16 X^3 +  72 X^2 -   96 X +      24
#    L(5,0)(X) =  -X^5 + 25 X^4 - 200 X^3 +  600 X^2 -  600 x    +  120
#    L(6,0)(X) =   X^6 - 36 X^5 + 450 X^4 - 2400 X^3 + 5400 X^2 - 4320 X + 720
#
#    M = 1
#
#    L(0,1)(X) =    0
#    L(1,1)(X) =   -1,
#    L(2,1)(X) =    2 X - 4,
#    L(3,1)(X) =   -3 X^2 + 18 X - 18,
#    L(4,1)(X) =    4 X^3 - 48 X^2 + 144 X - 96
#
#    M = 2
#
#    L(0,2)(X) =    0
#    L(1,2)(X) =    0,
#    L(2,2)(X) =    2,
#    L(3,2)(X) =   -6 X + 18,
#    L(4,2)(X) =   12 X^2 - 96 X + 144
#
#    M = 3
#
#    L(0,3)(X) =    0
#    L(1,3)(X) =    0,
#    L(2,3)(X) =    0,
#    L(3,3)(X) =   -6,
#    L(4,3)(X) =   24 X - 96
#
#    M = 4
#
#    L(0,4)(X) =    0
#    L(1,4)(X) =    0
#    L(2,4)(X) =    0
#    L(3,4)(X) =    0
#    L(4,4)(X) =   24
#
#  Recursion:
#
#    if N = 0:
#
#      L(N,M)(X)   = 0 
#
#    if N = 1:
#
#      L(N,M)(X)   = (M+1-X)
#
#    if 2 <= N:
#
#      L(N,M)(X)   = ( (M+2*N-1-X) * L(N-1,M)(X) 
#                  +   (1-M-N)     * L(N-2,M)(X) ) / N
#
#  Special values:
#
#    For M = 0, the associated Laguerre polynomials L(N,M)(X) are equal 
#    to the Laguerre polynomials L(N)(X).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    integer M, the parameter.  M must be nonnegative.
#
#    real X, the point at which the polynomials are to be evaluated.
#
#    real CX(1:N+1), the associated Laguerre polynomials of 
#    degrees 0 through N evaluated at the point X.
#
  import numpy as np

  if ( m < 0 ):
    print ( '' )
    print ( 'laguerre_associated(): Fatal error!' )
    print ( '  Input value of M = %d' % ( m ) )
    print ( '  but M must be nonnegative.' )
    raise Exception ( 'laguerre_associated(): Fatal error!' )

  cx = np.zeros ( n + 1 )

  cx[0] = 1.0

  if ( 0 < n ):

    cx[1] = float ( m + 1 ) - x

    for i in range ( 2, n + 1 ):
      cx[i] = ( ( float (   m + 2 * i - 1 ) - x ) * cx[i-1]    \
              +   float ( - m     - i + 1       ) * cx[i-2] ) \
              /   float (           i )

  return cx

def laguerre_associated_test ( ):

#*****************************************************************************80
#
## laguerre_associated_test() tests laguerre_associated().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 6
  m_test = np.array ( [ 0, 0, 1, 2, 3, 1 ] )
  x_test = np.array ( [ 0.0, 1.0, 0.0, 0.5, 0.5, 0.5 ] )

  print ( '' )
  print ( 'laguerre_associated_test():' )
  print ( '  laguerre_associated() evaluates the associated Laguerre polynomials;' )

  for i in range ( 0, 6 ):

    m = m_test[i]
    x = x_test[i]

    print ( '' )
    print ( '  Table of L(N,M)(X) for' )
    print ( '' )
    print ( '  N(max) = %d' % ( n ) )
    print ( '  M      = %d' % ( m ) )
    print ( '  X =      %f' % ( x ) )
    print ( '' )
 
    c = laguerre_associated ( n, m, x )
 
    for j in range ( 0, n + 1 ):
      print ( '  %4d  %12g' % ( j, c[j] ) )

  return

def laguerre_poly_coef ( n ):

#*****************************************************************************80
#
## laguerre_poly_coef() evaluates the Laguerre polynomial coefficients.
#
#  First terms:
#
#    0: 1
#    1: 1  -1
#    2: 1  -2  1/2
#    3: 1  -3  3/2  1/6
#    4: 1  -4  4   -2/3  1/24
#    5: 1  -5  5   -5/3  5/24  -1/120
#
#  Recursion:
#
#    L(0) = ( 1,  0, 0, ..., 0 )
#    L(1) = ( 1, -1, 0, ..., 0 )
#    L(N) = (2*N-1-X) * L(N-1) - (N-1) * L(N-2) / N
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    real C(1:N+1,1:N+1), the coefficients of the Laguerre polynomials 
#    of degree 0 through N.  Each polynomial is stored as a row.
#
  import numpy as np

  c = np.zeros ( ( n + 1, n + 1 ) )

  for i in range ( 0, n + 1 ):
    c[i,0] = 1.0
 
  if ( 0 < n ):

    c[1,1] = -1.0
 
    for i in range ( 2, n + 1 ):
      for j in range ( 1, n + 1 ):
        c[i,j] = ( \
            float ( 2 * i - 1 ) * c[i-1,j] \
          + float (   - i + 1 ) * c[i-2,j] \
          -                       c[i-1,j-1] ) / float ( i )

  return c

def laguerre_poly_coef_test ( ):

#*****************************************************************************80
#
## laguerre_poly_coef_test() tests laguerre_poly_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'laguerre_poly_coef_test():' )
  print ( '  laguerre_poly_coef() determines the Laguerre' )
  print ( '  polynomial coefficients.' )

  c = laguerre_poly_coef ( n )
 
  for i in range ( 0, n + 1 ):
    print ( '' )
    print ( '  L(%d)' % ( i ) )
    print ( '' )
    for j in range ( i, -1, -1 ):
      if ( j == 0 ):
        print ( '    %f' % ( c[i,j] ) )
      elif ( j == 1 ):
        print ( '    %f * x' % ( c[i,j] ) )
      else:
        print ( '    %f * x^%d' % ( c[i,j], j ) )

  fact = 1.0

  for i in range ( 0, n + 1 ):

    if ( 0 < i ):
      fact = fact * i

    print ( '' )
    print ( '  Factorially scaled L(%d)' % ( i ) )
    print ( '' )
    for j in range ( i, -1, -1 ):
      if ( j == 0 ):
        print ( '    %f' % ( fact * c[i,j] ) )
      elif ( j == 1 ):
        print ( '    %f * x' % ( fact * c[i,j] ) )
      else:
        print ( '    %f * x^%d' % ( fact * c[i,j], j ) )

  return

def laguerre_polynomial_values ( n_data ):

#*****************************************************************************80
#
## laguerre_polynomial_values() returns some values of the Laguerre polynomial.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      LaguerreL[n,x]
#
#  Differential equation:
#
#    X * Y'' + (1-X) * Y' + N * Y = 0
#
#  First terms:
#
#      1
#     -X   +  1
#   (  X^2 -  4 X   +   2 ) / 2
#   ( -X^3 +  9 X^2 -  18 X   +    6 ) / 6
#   (  X^4 - 16 X^3 +  72 X^2 -   96 X +      24 ) / 24
#   ( -X^5 + 25 X^4 - 200 X^3 +  600 X^2 -   600 X   +   120 ) / 120
#   (  X^6 - 36 X^5 + 450 X^4 - 2400 X^3 +  5400 X^2 -  4320 X   +   720 ) / 720
#   ( -X^7 + 49 X^6 - 882 X^5 + 7350 X^4 - 29400 X^3 + 52920 X^2 - 35280 X + 5040 ) / 5040
#
#  Recursion:
#
#    L(0)(X) = 1,
#    L(1)(X) = 1-X,
#    N * L(N)(X) = (2*N-1-X) * L(N-1)(X) - (N-1) * L(N-2)(X)
#
#  Orthogonality:
#
#    Integral ( 0 <= X < oo ) exp ( - X ) * L(N)(X) * L(M)(X) dX
#    = 0 if N /= M
#    = 1 if N == M
#
#  Special values:
#
#    L(N)(0) = 1.
#
#  Relations:
#
#    L(N)(X) = (-1)^N / N! * exp ( x ) * (d/dx)^n ( exp ( - x ) * X^n )  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the polynomial.
#
#    real X, the point where the polynomial is evaluated.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 17

  f_vec = np.array ( ( \
      0.1000000000000000E+01, \
      0.0000000000000000E+00, \
     -0.5000000000000000E+00, \
     -0.6666666666666667E+00, \
     -0.6250000000000000E+00, \
     -0.4666666666666667E+00, \
     -0.2569444444444444E+00, \
     -0.4047619047619048E-01, \
      0.1539930555555556E+00, \
      0.3097442680776014E+00, \
      0.4189459325396825E+00, \
      0.4801341790925124E+00, \
      0.4962122235082305E+00, \
     -0.4455729166666667E+00, \
      0.8500000000000000E+00, \
     -0.3166666666666667E+01, \
      0.3433333333333333E+02 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  5,  5, \
     5,  5 ))

  x_vec = np.array ( ( \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     0.5E+00, \
     3.0E+00, \
     5.0E+00, \
     1.0E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def laguerre_polynomial_values_test ( ):

#*****************************************************************************80
#
## laguerre_polynomial_values_test() tests laguerre_polynomial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'laguerre_polynomial_values_test():' )
  print ( '  laguerre_polynomial_values() stores values of' )
  print ( '  the Laguerre polynomials.' )
  print ( '' )
  print ( '     N    X            L(N)(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    [ n_data, n, x, f ] = laguerre_polynomial_values ( n_data );

    if ( n_data == 0 ):
      break

    print ( '  %4d  %12f  %24.16f' % (  n, x, f ) )

  return

def laguerre_poly ( n, x ):

#*****************************************************************************80
#
## laguerre_poly() evaluates the Laguerre polynomials at X.
#
#  Differential equation:
#
#    X * Y'' + (1-X) * Y' + N * Y = 0
#
#  First terms:
#
#      1
#     -X    +  1
#   (  X^2 -  4 X     +  2 ) / 2
#   ( -X^3 +  9 X^2 -  18 X    +    6 ) / 6
#   (  X^4 - 16 X^3 +  72 X^2 -   96 X +      24 ) / 24
#   ( -X^5 + 25 X^4 - 200 X^3 +  600 X^2 -  600 x    +  120 ) / 120
#   (  X^6 - 36 X^5 + 450 X^4 - 2400 X^3 + 5400 X^2 - 4320 X + 720 ) / 720
#   ( -X^7 + 49 X^6 - 882 X^5 + 7350 X^4 - 29400 X^3 
#      + 52920 X^2 - 35280 X + 5040 ) / 5040
#
#  Recursion:
#
#    L(0)(X) = 1,
#    L(1)(X) = 1-X,
#    N * L(N)(X) = (2*N-1-X) * L(N-1)(X) - (N-1) * L(N-2)(X)
#
#  Orthogonality:
#
#    Integral ( 0 <= X < Infinity ) exp ( - X ) * L(N)(X) * L(M)(X) dX
#    = 0 if N /= M
#    = 1 if N == M
#
#  Special values:
#
#    L(N)(0) = 1.
#
#  Relations:
#
#    L(N)(X) = (-1)^N / N! * exp ( x ) * (d/dx)^n ( exp ( - x ) * X^n )  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    real X, the point at which the polynomials are to be evaluated.
#
#    real CX(1:N+1), the Laguerre polynomials of degree 0 through 
#    N evaluated at the point X.
#
  import numpy as np

  cx = np.zeros ( n + 1 )

  cx[0] = 1.0

  if ( 0 < n ):
 
    cx[1] = 1.0 - x
 
    for i in range ( 2, n + 1 ):

      cx[i] = ( ( float ( 2 * i - 1 ) - x ) * cx[i-1]   \
                - float (     i - 1 )       * cx[i-2] ) \
                / float (     i )

  return cx

def laguerre_poly_test ( ):

#*****************************************************************************80
#
## laguerre_poly_test() tests laguerre_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'laguerre_poly_test():' )
  print ( '  laguerre_poly() computes Laguerre polynomials;' )
  print ( '' )
  print ( '     N      X        Exact F       L(N)(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = laguerre_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = laguerre_poly ( n, x )

    print ( '  %6d  %6f  %12f  %12f' % ( n, x, f, f2[n] ) )

  return

def lambert_w ( x ):

#*****************************************************************************80
#
## lambert_w() computes the Lambert W function.
#
#  Discussion:
#
#    The function W(X) is defined implicitly by:
#
#      W(X) * e^W(X) = X
#
#    The function is also known as the "Omega" function.
#
#    In Mathematica, the function can be evaluated by:
#
#      W = ProductLog [ X ]
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 May 2005
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Corless, Gaston Gonnet, David Hare, David Jeffrey, Donald Knuth,
#    On the Lambert W Function,
#    Advances in Computational Mathematics,
#    Volume 5, 1996, pages 329-359.
#
#    Brian Hayes,
#    "Why W?",
#    The American Scientist,
#    Volume 93, March-April 2005, pages 104-108.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 2002,
#    Second edition,
#    ISBN: 1584883472,
#    LC: QA5.W45
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Input:
#
#    real X, the argument of the function.
#
#  Output:
#
#    real w: the value of the Lambert W function.
#
  import numpy as np

  it_max = 100
  tol = 1.0E-10

  w = lambert_w_estimate ( x )

  it = 0

  while ( it <= it_max ):

    if ( np.abs ( ( x - w * np.exp ( w ) ) ) < \
      tol * np.abs ( ( w + 1.0 ) * np.exp ( w ) ) ):
      break
 
    w = w - ( w * np.exp ( w ) - x ) \
      / ( ( w + 1.0 ) * np.exp ( w ) \
      - ( w + 2.0 ) * ( w * np.exp ( w ) - x ) \
      / ( 2.0 * w + 2.0 ) )

    it = it + 1

  return w

def lambert_w_test ( ):

#*****************************************************************************80
#
## lambert_w_test() tests lambert_w().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 October 2006
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'lambert_w_test():' )
  print ( '  lambert_w() estimates the Lambert W function.' )
  print ( '' )
  print ( '           X           W(X)        W(X)' )
  print ( '                   Tabulated   Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = lambert_w_values ( n_data )

    if ( n_data == 0 ):
      break
 
    fx2 = lambert_w ( x )

    print ( ' %14.6g %14.6g %14.6g' % ( x, fx, fx2 ) )

  return

def lambert_w_estimate ( x ):

#*****************************************************************************80
#
## lambert_w_estimate() is estimates the Lambert W function.
#
#  Discussion:
#
#    This crude approximation can be used as a good starting point
#    for an iterative process.
#
#    The function W(X) is defined implicitly by:
#
#      W(X) * e^W(X) = X
#
#    The function is also known as the "Omega" function.
#
#    In Mathematica, the function can be evaluated by:
#
#      W = ProductLog [ X ]
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Corless, Gaston Gonnet, David Hare, David Jeffrey, Donald Knuth,
#    On the Lambert W Function,
#    Advances in Computational Mathematics,
#    Volume 5, 1996, pages 329-359.
#
#    Brian Hayes,
#    "Why W?",
#    The American Scientist,
#    Volume 93, March-April 2005, pages 104-108.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 2002,
#    Second edition,
#    ISBN: 1584883472,
#    LC: QA5.W45
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Input:
#
#    real X: the argument of the function.
#
#  Output:
#
#    real value: an estimate for the Lambert W function.
#
  import numpy as np

  if ( x <= 500.0 ):

    value = 0.04 + 0.665 * ( 1.0 + 0.0195 * np.log ( x + 1.0 ) ) * np.log ( x + 1.0 )

  else:

    value = np.log ( x - 4.0 ) - ( 1.0 - 1.0 / np.log ( x ) ) * np.log ( np.log ( x ) )

  return value

def lambert_w_estimate_test ( ):

#*****************************************************************************80
#
## lambert_w_estimate_test() tests lambert_w_estimate().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 June 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'lambert_w_estimate_test():' )
  print ( '  lambert_w_estimate() estimates the Lambert W function.' )
  print ( '' )
  print ( '           X           W(X)        W(X)' )
  print ( '                   Tabulated       Estimate' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = lambert_w_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = lambert_w_estimate ( x )

    print ( ' %14.6g %14.6g %14.6g' % ( x, fx, fx2 ) )

  return

def lambert_w_values ( n_data ):

#*****************************************************************************80
#
## lambert_w_values() returns some values of the Lambert W function.
#
#  Discussion:
#
#    The function W(X) is defined implicitly by:
#
#      W(X) * e^W(X) = X
#
#    The function is also known as the "Omega" function.
#
#    In Mathematica, the function can be evaluated by:
#
#      W = ProductLog [ X ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Brian Hayes,
#    "Why W?",
#    The American Scientist,
#    Volume 93, March-April 2005, pages 104-108.
#
#    Eric Weisstein,
#    "Lambert's W-Function",
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1998.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_data.  The user sets N_data to 0 before the first call.  
#
#  Output:
#
#    integer N_data.  On each call, the routine increments N_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_data will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 22

  f_vec = np.array ( ( \
    0.0000000000000000E+00, \
    0.3517337112491958E+00, \
    0.5671432904097839E+00, \
    0.7258613577662263E+00, \
    0.8526055020137255E+00, \
    0.9585863567287029E+00, \
    0.1000000000000000E+01, \
    0.1049908894964040E+01, \
    0.1130289326974136E+01, \
    0.1202167873197043E+01, \
    0.1267237814307435E+01, \
    0.1326724665242200E+01, \
    0.1381545379445041E+01, \
    0.1432404775898300E+01, \
    0.1479856830173851E+01, \
    0.1524345204984144E+01, \
    0.1566230953782388E+01, \
    0.1605811996320178E+01, \
    0.1745528002740699E+01, \
    0.3385630140290050E+01, \
    0.5249602852401596E+01, \
    0.1138335808614005E+02 ))

  x_vec = np.array ( ( \
    0.0000000000000000E+00, \
    0.5000000000000000E+00, \
    0.1000000000000000E+01, \
    0.1500000000000000E+01, \
    0.2000000000000000E+01, \
    0.2500000000000000E+01, \
    0.2718281828459045E+01, \
    0.3000000000000000E+01, \
    0.3500000000000000E+01, \
    0.4000000000000000E+01, \
    0.4500000000000000E+01, \
    0.5000000000000000E+01, \
    0.5500000000000000E+01, \
    0.6000000000000000E+01, \
    0.6500000000000000E+01, \
    0.7000000000000000E+01, \
    0.7500000000000000E+01, \
    0.8000000000000000E+01, \
    0.1000000000000000E+02, \
    0.1000000000000000E+03, \
    0.1000000000000000E+04, \
    0.1000000000000000E+07 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def legendre_associated_normalized ( n, m, x ):

#*****************************************************************************80
#
## legendre_associated_normalized() evaluates the associated Legendre functions.
#
#  Discussion:
#
#    The unnormalized associated Legendre functions P_N^M(X) have
#    the property that
#
#      Integral ( -1 <= X <= 1 ) ( P_N^M(X) )^2 dX
#      = 2 * ( N + M )! / ( ( 2 * N + 1 ) * ( N - M )! )
#
#    By dividing the function by the square root of this term,
#    the normalized associated Legendre functions have norm 1.
#
#    However, we plan to use these functions to build spherical
#    harmonics, so we use a slightly different normalization factor of
#
#      sqrt ( ( ( 2 * N + 1 ) * ( N - M )! ) / ( 4 * pi * ( N + M )! ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the maximum first index of the Legendre
#    function, which must be at least 0.
#
#    integer M, the second index of the Legendre function,
#    which must be at least 0, and no greater than N.
#
#    real X, the point at which the function is to be
#    evaluated.  X must satisfy -1 <= X <= 1.
#
#    real CX(1:N+1), the values of the first N+1 function.
#
  import math
  import numpy as np

  if ( m < 0 ):
    print ( '' )
    print ( 'legendre_associated_normalized(): Fatal error!' )
    print ( '  Input value of M is %d' % ( m ) )
    print ( '  but M must be nonnegative.' )
 
  if ( n < m ):
    print ( '' )
    print ( 'legendre_associated_normalized(): Fatal error!' )
    print ( '  Input value of M = %d' % ( m ) )
    print ( '  Input value of N = %d' % ( n ) )
    print ( '  but M must be less than or equal to N.' )
 
  if ( x < -1.0 ):
    print ( '' )
    print ( 'legendre_associated_normalized(): Fatal error!' )
    print ( '  Input value of X = %f' % ( x ) )
    print ( '  but X must be no less than -1.' )

  if ( 1.0 < x ):
    print ( '' )
    print ( 'legendre_associated_normalized(): Fatal error!' )
    print ( '  Input value of X = %f' % ( x ) )
    print ( '  but X must be no more than 1.' )
  
  cx = np.zeros ( n + 1 )

  cx[m] = 1.0
  somx2 = np.sqrt ( 1.0 - x * x )
 
  fact = 1.0
  for i in range ( 0, m ):
    cx[m] = - cx[m] * fact * somx2
    fact = fact + 2.0
 
  if ( m != n ):

    cx[m+1] = x * float ( 2 * m + 1 ) * cx[m]

    for i in range ( m + 2, n + 1 ):
      cx[i] = ( float ( 2 * i     - 1 ) * x * cx[i-1] \
              + float (   - i - m + 1 ) *     cx[i-2] ) \
              / float (     i - m     )
#
#  Normalization.
#
  for mm in range ( m, n + 1 ):

    factor = np.sqrt ( ( ( 2 * mm + 1 ) * math.factorial ( mm - m ) ) \
      / ( 4.0 * np.pi * math.factorial ( mm + m ) ) )

    cx[mm] = cx[mm] * factor

  return cx

def legendre_associated_normalized_test ( ):

#*****************************************************************************80
#
## legendre_associated_normalized_test() tests legendre_associated_normalized().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'legendre_associated_normalized_test():' )
  print ( '  legendre_associated_normalized() evaluates the associated Legendre functions;' )

  print ( '' )
  print ( '      N       M    X     Exact F     PNM(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, x, f = legendre_associated_normalized_sphere_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = legendre_associated_normalized ( n, m, x )

    print ( '  %6d  %6d  %6f  %12f  %12f' % ( n, m, x, f, f2[n] ) )

  return

def legendre_associated_normalized_sphere_values ( n_data ):

#*****************************************************************************80
#
## legendre_associated_normalized_sphere_values() does what it says.
#
#  Discussion:
#
#    The function considered is the associated Legendre polynomial P^M_N(X).
#
#    In Mathematica, the function can be evaluated by:
#
#      LegendreP [ n, m, x ]
#
#    The function is normalized for the unit sphere by dividing by
#
#      sqrt ( 4 * pi * ( n + m )! / ( 2 * n + 1 ) / ( n - m )! )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, integer M, real X, 
#    the arguments of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 21

  f_vec = np.array ( ( \
     0.2820947917738781, \
     0.2443012559514600, \
    -0.2992067103010745, \
    -0.07884789131313000, \
    -0.3345232717786446, \
     0.2897056515173922, \
    -0.3265292910163510, \
    -0.06997056236064664, \
     0.3832445536624809, \
    -0.2709948227475519, \
    -0.2446290772414100, \
     0.2560660384200185, \
     0.1881693403754876, \
    -0.4064922341213279, \
     0.2489246395003027, \
     0.08405804426339821, \
     0.3293793022891428, \
    -0.1588847984307093, \
    -0.2808712959945307, \
     0.4127948151484925, \
    -0.2260970318780046  ))

  m_vec = np.array ( ( \
    0, 0, 1, 0, \
    1, 2, 0, 1, \
    2, 3, 0, 1, \
    2, 3, 4, 0, \
    1, 2, 3, 4, \
    5 ))

  n_vec = np.array ( ( \
    0,  1,  1,  2, \
    2,  2,  3,  3, \
    3,  3,  4,  4, \
    4,  4,  4,  5, \
    5,  5,  5,  5, \
    5 ))

  x_vec = np.array ( ( \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    m = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    m = m_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, m, x, f

def legendre_associated_normalized_sphere_values_test ( ):

#*****************************************************************************80
#
## legendre_associated_normalized_sphere_values_test() tests legendre_associated_normalized_sphere_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#

  print ( '' )
  print ( 'legendre_associated_normalized_sphere_values_test():' )
  print ( '  legendre_associated_normalized_sphere_values() stores values of the ' )
  print ( '  associated Legendre function normalized for the surface of a sphere.' )
  print ( '' )
  print ( '      N       M            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, x, f = legendre_associated_normalized_sphere_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %6d  %12f  %24.16g' % ( n, m, x, f ) )

  return

def legendre_associated ( n, m, x ):

#*****************************************************************************80
#
## legendre_associated() evaluates the associated Legendre functions.
#
#  Differential equation:
#
#    (1-X*X) * Y'' - 2 * X * Y + ( N (N+1) - (M*M/(1-X*X)) * Y = 0
#
#  First terms:
#
#    M = 0  ( = Legendre polynomials of first kind P(N)(X) )
#
#    P00 =    1
#    P10 =    1 X
#    P20 = (  3 X^2 -   1)/2
#    P30 = (  5 X^3 -   3 X)/2
#    P40 = ( 35 X^4 -  30 X^2 +   3)/8
#    P50 = ( 63 X^5 -  70 X^3 +  15 X)/8
#    P60 = (231 X^6 - 315 X^4 + 105 X^2 -  5)/16
#    P70 = (429 X^7 - 693 X^5 + 315 X^3 - 35 X)/16
#
#    M = 1
#
#    P01 =   0
#    P11 =   1 * SQRT(1-X*X)
#    P21 =   3 * SQRT(1-X*X) * X
#    P31 = 1.5 * SQRT(1-X*X) * (5*X*X-1)
#    P41 = 2.5 * SQRT(1-X*X) * (7*X*X*X-3*X)
#
#    M = 2
#
#    P02 =   0
#    P12 =   0
#    P22 =   3 * (1-X*X)
#    P32 =  15 * (1-X*X) * X
#    P42 = 7.5 * (1-X*X) * (7*X*X-1)
#
#    M = 3
#
#    P03 =   0
#    P13 =   0
#    P23 =   0
#    P33 =  15 * (1-X*X)^1.5
#    P43 = 105 * (1-X*X)^1.5 * X
#
#    M = 4
#
#    P04 =   0
#    P14 =   0
#    P24 =   0
#    P34 =   0
#    P44 = 105 * (1-X*X)^2
#
#  Recursion:
#
#    if N < M:
#      P(N,M) = 0
#    if N = M:
#      P(N,M) = (2*M-1)!! * (1-X*X)^(M/2) where N!! means the product of
#      all the odd integers less than or equal to N.
#    if N = M+1:
#      P(N,M) = X*(2*M+1)*P(M,M)
#    if M+1 < N:
#      P(N,M) = ( X*(2*N-1)*P(N-1,M) - (N+M-1)*P(N-2,M) )/(N-M)
#
#  Restrictions:
#
#    -1 <= X <= 1
#     0 <= M <= N
#
#  Special values:
#
#    P(N,0)(X) = P(N)(X), that is, for M=0, the associated Legendre
#    function of the first kind equals the Legendre polynomial of the
#    first kind.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the maximum first index of the Legendre
#    function, which must be at least 0.
#
#    integer M, the second index of the Legendre function,
#    which must be at least 0, and no greater than N.
#
#    real X, the point at which the function is to be
#    evaluated.  X must satisfy -1 <= X <= 1.
#
#    real CX(1:N+1), the values of the first N+1 function.
#
  import numpy as np

  if ( m < 0 ):
    print ( '' )
    print ( 'legendre_associated(): Fatal error!' )
    print ( '  Input value of M is %d' % ( m ) )
    print ( '  but M must be nonnegative.' )
 
  if ( n < m ):
    print ( '' )
    print ( 'legendre_associated(): Fatal error!' )
    print ( '  Input value of M = %d' % ( m ) )
    print ( '  Input value of N = %d' % ( n ) )
    print ( '  but M must be less than or equal to N.' )
 
  if ( x < -1.0 ):
    print ( '' )
    print ( 'legendre_associated(): Fatal error!' )
    print ( '  Input value of X = %f' % ( x ) )
    print ( '  but X must be no less than -1.' )

  if ( 1.0 < x ):
    print ( '' )
    print ( 'legendre_associated(): Fatal error!' )
    print ( '  Input value of X = %f' % ( x ) )
    print ( '  but X must be no more than 1.' )
  
  cx = np.zeros ( n + 1 )

  cx[m] = 1.0
  somx2 = np.sqrt ( 1.0 - x * x )
 
  fact = 1.0
  for i in range ( 0, m ):
    cx[m] = - cx[m] * fact * somx2
    fact = fact + 2.0
 
  if ( m != n ):

    cx[m+1] = x * float ( 2 * m + 1 ) * cx[m]

    for i in range ( m + 2, n + 1 ):
      cx[i] = ( float ( 2 * i     - 1 ) * x * cx[i-1] \
              + float (   - i - m + 1 ) *     cx[i-2] ) \
              / float (     i - m     )

  return cx

def legendre_associated_test ( ):

#*****************************************************************************80
#
## legendre_associated_test() tests legendre_associated().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'legendre_associated_test():' )
  print ( '  legendre_associated() evaluates the associated Legendre functions;' )

  print ( '' )
  print ( '      N       M    X     Exact F     PNM(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, x, f = legendre_associated_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = legendre_associated ( n, m, x )

    print ( '  %6d  %6d  %6f  %12f  %12f' % ( n, m, x, f, f2[n] ) )

  return

def legendre_associated_values ( n_data ):

#*****************************************************************************80
#
## legendre_associated_values() returns values of associated Legendre functions.
#
#  Discussion:
#
#    The function considered is the associated Legendre polynomial P^M_N(X).
#
#    In Mathematica, the function can be evaluated by:
#
#      LegendreP [ n, m, x ]
#
#  Differential equation:
#
#    (1-X*X) * Y'' - 2 * X * Y + ( N (N+1) - (M*M/(1-X*X)) * Y = 0
#
#  First terms:
#
#    M = 0  ( = Legendre polynomials of first kind P(N)(X) )
#
#    P00 =    1
#    P10 =    1 X
#    P20 = (  3 X^2 -   1)/2
#    P30 = (  5 X^3 -   3 X)/2
#    P40 = ( 35 X^4 -  30 X^2 +   3)/8
#    P50 = ( 63 X^5 -  70 X^3 +  15 X)/8
#    P60 = (231 X^6 - 315 X^4 + 105 X^2 -  5)/16
#    P70 = (429 X^7 - 693 X^5 + 315 X^3 - 35 X)/16
#
#    M = 1
#
#    P01 =   0
#    P11 =   1 * SQRT(1-X*X)
#    P21 =   3 * SQRT(1-X*X) * X
#    P31 = 1.5 * SQRT(1-X*X) * (5*X*X-1)
#    P41 = 2.5 * SQRT(1-X*X) * (7*X*X*X-3*X)
#
#    M = 2
#
#    P02 =   0
#    P12 =   0
#    P22 =   3 * (1-X*X)
#    P32 =  15 * (1-X*X) * X
#    P42 = 7.5 * (1-X*X) * (7*X*X-1)
#
#    M = 3
#
#    P03 =   0
#    P13 =   0
#    P23 =   0
#    P33 =  15 * (1-X*X)^1.5
#    P43 = 105 * (1-X*X)^1.5 * X
#
#    M = 4
#
#    P04 =   0
#    P14 =   0
#    P24 =   0
#    P34 =   0
#    P44 = 105 * (1-X*X)^2
#
#  Recursion:
#
#    if N < M:
#      P(N,M) = 0
#    if N = M:
#      P(N,M) = (2*M-1)!! * (1-X*X)^(M/2) where N!! means the product of
#      all the odd integers less than or equal to N.
#    if N = M+1:
#      P(N,M) = X*(2*M+1)*P(M,M)
#    if M+1 < N:
#      P(N,M) = ( X*(2*N-1)*P(N-1,M) - (N+M-1)*P(N-2,M) )/(N-M)
#
#  Restrictions:
#
#    -1 <= X <= 1
#     0 <= M <= N
#
#  Special values:
#
#    P(N,0)(X) = P(N)(X), that is, for M=0, the associated Legendre
#    polynomial of the first kind equals the Legendre polynomial of the
#    first kind.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, integer M, real X, 
#    the arguments of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
      0.0000000000000000E+00, \
     -0.5000000000000000E+00, \
      0.0000000000000000E+00, \
      0.3750000000000000E+00, \
      0.0000000000000000E+00, \
     -0.8660254037844386E+00, \
     -0.1299038105676658E+01, \
     -0.3247595264191645E+00, \
      0.1353164693413185E+01, \
     -0.2800000000000000E+00, \
      0.1175755076535925E+01, \
      0.2880000000000000E+01, \
     -0.1410906091843111E+02, \
     -0.3955078125000000E+01, \
     -0.9997558593750000E+01, \
      0.8265311444100484E+02, \
      0.2024442836815152E+02, \
     -0.4237997531890869E+03, \
      0.1638320624828339E+04, \
     -0.2025687389227225E+05  ))

  m_vec = np.array ( ( \
    0, 0, 0, 0, \
    0, 1, 1, 1, \
    1, 0, 1, 2, \
    3, 2, 2, 3, \
    3, 4, 4, 5 ))

  n_vec = np.array ( ( \
    1,  2,  3,  4, \
    5,  1,  2,  3, \
    4,  3,  3,  3, \
    3,  4,  5,  6, \
    7,  8,  9, 10 ))

  x_vec = np.array ( ( \
     0.00E+00, \
     0.00E+00, \
     0.00E+00, \
     0.00E+00, \
     0.00E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00 ))
  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    m = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    m = m_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, m, x, f

def legendre_associated_values_test ( ):

#*****************************************************************************80
#
## legendre_associated_values_test() tests legendre_associated_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'legendre_associated_values_test():' )
  print ( '  legendre_associated_values() stores values of the associated Legendre function.' )
  print ( '' )
  print ( '      N       M            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, x, f = legendre_associated_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %6d  %12f  %24.16g' % ( n, m, x, f ) )

  return

def legendre_function_q ( n, x ):

#*****************************************************************************80
#
## legendre_function_q() evaluates the Legendre QN functions.
#
#  Differential equation:
#
#    (1-X*X) Y'' - 2 X Y' + N (N+1) = 0
#
#  First terms:
#
#    Q(0)(X) = 0.5 * log((1+X)/(1-X))
#    Q(1)(X) = Q(0)(X)*X - 1 
#    Q(2)(X) = Q(0)(X)*(3*X*X-1)/4 - 1.5*X
#    Q(3)(X) = Q(0)(X)*(5*X*X*X-3*X)/4 - 2.5*X^2 + 2/3
#    Q(4)(X) = Q(0)(X)*(35*X^4-30*X^2+3)/16 - 35/8 * X^3 + 55/24 * X
#    Q(5)(X) = Q(0)(X)*(63*X^5-70*X^3+15*X)/16 - 63/8*X^4 + 49/8*X^2 - 8/15
#
#  Recursion:
#
#    Q(0) = 0.5 * log ( (1+X) / (1-X) )
#    Q(1) = 0.5 * X * log ( (1+X) / (1-X) ) - 1.0
#
#    Q(N) = ( (2*N-1) * X * Q(N-1) - (N-1) * Q(N-2) ) / N
#
#  Restrictions:
#
#    -1 < X < 1
#
#  Special values:
#
#    Note that the Legendre function Q(N)(X) is equal to the
#    associated Legendre function of the second kind,
#    Q(N,M)(X) with M = 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the highest order function to evaluate.
#
#    real X, the point at which the functions are to be
#    evaluated.  X must satisfy -1 < X < 1.
#
#    real CX(1:N+1), the values of the first N+1 Legendre
#    functions at the point X.
#
  import numpy as np
#
#  Check the value of X.
#
  if ( x <= -1.0 or 1.0 <= x ):
    print ( '' )
    print ( 'legendre_function_q(): Fatal error!' )
    print ( '  Illegal input value of X = %f' % ( x ) )
    print ( '  But X must be between -1 and 1.' )

  cx = np.zeros ( n + 1 )

  cx[0] = 0.5 * np.log ( ( 1.0 + x ) / ( 1.0 - x ) )

  if ( 0 < n ):

    cx[1] = x * cx[0] - 1.0

    for i in range ( 2, n + 1 ):
      cx[i] = ( float ( 2 * i - 1 ) * x * cx[i]     \
            +   float (   - i + 1 )     * cx[i-1] ) \
            /   float (     i     )

  return cx

def legendre_function_q_test ( ):

#*****************************************************************************80
#
## legendre_function_q_test() tests legendre_function_q().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'legendre_function_q_test():' )
  print ( '  legendre_function_q() computes Legendre QN functions' )
  print ( '' )
  print ( '     N      X        Exact F       Q(N)(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = legendre_function_q_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = legendre_function_q ( n, x )

    print ( '  %6d  %6f  %12f  %12f' % ( n, x, f, f2[n] ) )

  return

def legendre_function_q_values ( n_data ):

#*****************************************************************************80
#
## legendre_function_q_values() returns values of the Legendre Q function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      LegendreQ[n,x]
#
#  Differential equation:
#
#    (1-X*X) Y'' - 2 X Y' + N (N+1) = 0
#
#  First terms:
#
#    Q(0)(X) = 0.5 * log((1+X)/(1-X))
#    Q(1)(X) = Q(0)(X)*X - 1 
#    Q(2)(X) = Q(0)(X)*(3*X*X-1)/4 - 1.5*X
#    Q(3)(X) = Q(0)(X)*(5*X*X*X-3*X)/4 - 2.5*X^2 + 2/3
#    Q(4)(X) = Q(0)(X)*(35*X^4-30*X^2+3)/16 - 35/8 * X^3 + 55/24 * X
#    Q(5)(X) = Q(0)(X)*(63*X^5-70*X^3+15*X)/16 - 63/8*X^4 + 49/8*X^2 - 8/15
#
#  Recursion:
#
#    Q(0) = 0.5 * log ( (1+X) / (1-X) )
#    Q(1) = 0.5 * X * log ( (1+X) / (1-X) ) - 1.0
#
#    Q(N) = ( (2*N-1) * X * Q(N-1) - (N-1) * Q(N-2) ) / N
#
#  Restrictions:
#
#    -1 < X < 1
#
#  Special values:
#
#    Note that the Legendre function Q(N)(X) is equal to the
#    associated Legendre function of the second kind,
#    Q(N,M)(X) with M = 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 21

  f_vec = np.array ( ( \
      0.2554128118829953E+00, \
     -0.9361467970292512E+00, \
     -0.4787614548274669E+00, \
      0.4246139251747229E+00, \
      0.5448396833845414E+00, \
     -0.9451328261673470E-01, \
     -0.4973516573531213E+00, \
     -0.1499018843853194E+00, \
      0.3649161918783626E+00, \
      0.3055676545072885E+00, \
     -0.1832799367995643E+00, \
      0.6666666666666667E+00, \
      0.6268672028763330E+00, \
      0.5099015515315237E+00, \
      0.3232754180589764E+00, \
      0.8026113738148187E-01, \
     -0.1986547714794823E+00, \
     -0.4828663183349136E+00, \
     -0.7252886849144386E+00, \
     -0.8454443502398846E+00, \
     -0.6627096245052618E+00 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3 ))

  x_vec = np.array ( ( \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.00E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.90E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def legendre_function_q_values_test ( ):

#*****************************************************************************80
#
## legendre_function_q_values_test() tests legendre_function_q_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'legendre_function_q_values_test():' )
  print ( '  legendre_function_q_values() stores values of the Legendre Q function' )
  print ( '' )
  print ( '      N            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = legendre_function_q_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, f ) )

  return

def legendre_poly_coef ( n ):

#*****************************************************************************80
#
## legendre_poly_coef() evaluates the Legendre polynomial coefficients.
#
#  First terms:
#
#     1
#     0     1
#    -1/2   0      3/2
#     0    -3/2    0     5/2
#     3/8   0    -30/8   0     35/8
#     0    15/8    0   -70/8    0     63/8
#    -5/16  0    105/16  0   -315/16   0    231/16
#     0   -35/16   0   315/16   0   -693/16   0    429/16
#
#     1.00000
#     0.00000  1.00000
#    -0.50000  0.00000  1.50000
#     0.00000 -1.50000  0.00000  2.5000
#     0.37500  0.00000 -3.75000  0.00000  4.37500
#     0.00000  1.87500  0.00000 -8.75000  0.00000  7.87500
#    -0.31250  0.00000  6.56250  0.00000 -19.6875  0.00000  14.4375
#     0.00000 -2.1875   0.00000  19.6875  0.00000 -43.3215  0.00000  26.8125
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    real C(1:N+1,1:N+1), the coefficients of the Legendre polynomials 
#    of degree 0 through N.  Each polynomial is stored as a row.
#
  import numpy as np

  c = np.zeros ( ( n + 1, n + 1 ) )

  c[0,0] = 1.0

  if ( 0 < n ):

    c[1,1] = 1.0
 
    for i in range ( 2, n + 1 ):
      for j in range ( 0, i ):
        c[i,j] =          float (   - i + 1 ) * c[i-2,j] / float ( i )
      for j in range ( 1, i + 1 ):
        c[i,j] = c[i,j] + float ( i + i - 1 ) * c[i-1,j-1] / float ( i )

  return c

def legendre_poly_coef_test ( ):

#*****************************************************************************80
#
## legendre_poly_coef_test() tests legendre_poly_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'legendre_poly_coef_test():' )
  print ( '  legendre_poly_coef() determines the Legendre' )
  print ( '  polynomial coefficients.' )

  c = legendre_poly_coef ( n )
 
  for i in range ( 0, n + 1 ):
    print ( '' )
    print ( '  L(%d)' % ( i ) )
    print ( '' )
    for j in range ( i, -1, -1 ):
      if ( j == 0 ):
        print ( '    %f' % ( c[i,j] ) )
      elif ( j == 1 ):
        print ( '    %f * x' % ( c[i,j] ) )
      else:
        print ( '    %f * x^%d' % ( c[i,j], j ) )

  return

def legendre_poly ( n, x ):

#*****************************************************************************80
#
## legendre_poly() evaluates the Legendre polynomials P(N)(X) at X.
#
#  Discussion:
#
#    P(N)(1) = 1.
#    P(N)(-1) = (-1)^N.
#    abs ( P(N)(X) ) <= 1 in [-1,1].
#
#    P(N,0)(X) = P(N)(X), that is, for M=0, the associated Legendre
#    function of the first kind and order N equals the Legendre polynomial
#    of the first kind and order N.
#
#    The N zeroes of P(N)(X) are the abscissas used for Gauss-Legendre
#    quadrature of the integral of a function F(X) with weight function 1
#    over the interval [-1,1].
#
#    The Legendre polynomials are orthogonal under the inner product defined
#    as integration from -1 to 1:
#
#      Integral ( -1 <= X <= 1 ) P(I)(X) * P(J)(X) dX 
#        = 0 if I =/= J
#        = 2 / ( 2*I+1 ) if I = J.
#
#    Except for P(0)(X), the integral of P(I)(X) from -1 to 1 is 0.
#
#    A function F(X) defined on [-1,1] may be approximated by the series
#      C0*P(0)(X) + C1*P(1)(X) + ... + CN*P(N)(X)
#    where
#      C(I) = (2*I+1)/(2) * Integral ( -1 <= X <= 1 ) F(X) P(I)(X) dx.
#
#  Differential equation:
#
#    (1-X*X) * P(N)(X)'' - 2 * X * P(N)(X)' + N * (N+1) = 0
#
#  First terms:
#
#    P( 0)(X) =      1
#    P( 1)(X) =      1 X
#    P( 2)(X) = (    3 X^2 -       1)/2
#    P( 3)(X) = (    5 X^3 -     3 X)/2
#    P( 4)(X) = (   35 X^4 -    30 X^2 +     3)/8
#    P( 5)(X) = (   63 X^5 -    70 X^3 +    15 X)/8
#    P( 6)(X) = (  231 X^6 -   315 X^4 +   105 X^2 -     5)/16
#    P( 7)(X) = (  429 X^7 -   693 X^5 +   315 X^3 -    35 X)/16
#    P( 8)(X) = ( 6435 X^8 - 12012 X^6 +  6930 X^4 -  1260 X^2 +   35)/128
#    P( 9)(X) = (12155 X^9 - 25740 X^7 + 18018 X^5 -  4620 X^3 +  315 X)/128
#    P(10)(X) = (46189 X^10-109395 X^8 + 90090 X^6 - 30030 X^4 + 3465 X^2-63 )/256
#
#  Recursion:
#
#    P(0)(X) = 1
#    P(1)(X) = X
#    P(N)(X) = ( (2*N-1)*X*P(N-1)(X)-(N-1)*P(N-2)(X) ) / N
#
#    P'(0)(X) = 0
#    P'(1)(X) = 1
#    P'(N)(X) = ( (2*N-1)*(P(N-1)(X)+X*P'(N-1)(X)-(N-1)*P'(N-2)(X) ) / N
#
#  Formula:
#
#    P(N)(X) = (1/2**N) * sum ( 0 <= M <= N/2 ) C(N,M) C(2N-2M,N) X^(N-2*M)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    real X, the point at which the polynomials are to be evaluated.
#
#    real CX(1:N+1), the values of the Legendre polynomials 
#    of order 0 through N at the point X.
#
#    real CPX(1:N+1), the values of the derivatives of the
#    Legendre polynomials of order 0 through N at the point X.
#
  import numpy as np

  cx = np.zeros ( n + 1 )
  cpx = np.zeros ( n + 1 )

  cx[0] = 1.0
  cpx[0] = 0.0

  if ( 0 < n ):

    cx[1] = x
    cpx[1] = 1.0
 
    for i in range ( 2, n + 1 ):
 
      cx[i] = ( float ( 2 * i - 1 ) * x * cx[i-1] \
              - float (     i - 1 ) *   cx[i-2] ) \
              / float (     i     )
 
      cpx[i] = ( float ( 2 * i - 1 ) * ( cx[i-1] + x * cpx[i-1] ) \
               - float (     i - 1 ) *   cpx[i-2]               ) \
               / float (     i     )

  return cx, cpx

def legendre_poly_test ( ):

#*****************************************************************************80
#
## legendre_poly_test() tests legendre_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'legendre_poly_test():' )
  print ( '  legendre_poly() computes Legendre polynomials;' )
  print ( '' )
  print ( '     N      X        Exact F       L(N)(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = legendre_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    f2, fp2 = legendre_poly ( n, x )

    print ( '  %6d  %6f  %12f  %12f' % ( n, x, f, f2[n] ) )

  return

def legendre_poly_values ( n_data ):

#*****************************************************************************80
#
## legendre_poly_values() returns values of the Legendre polynomials.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      LegendreP [ n, x ]
#
#  Differential equation:
#
#    (1-X*X) * P(N,X)'' - 2 * X * P(N,X)' + N * (N+1) = 0
#
#  First terms:
#
#    P( 0,X) =       1
#    P( 1,X) =       1 X
#    P( 2,X) =  (    3 X^2 -       1)/2
#    P( 3,X) =  (    5 X^3 -     3 X)/2
#    P( 4,X) =  (   35 X^4 -    30 X^2 +     3)/8
#    P( 5,X) =  (   63 X^5 -    70 X^3 +    15 X)/8
#    P( 6,X) =  (  231 X^6 -   315 X^4 +   105 X^2 -     5)/16
#    P( 7,X) =  (  429 X^7 -   693 X^5 +   315 X^3 -    35 X)/16
#    P( 8,X) =  ( 6435 X^8 - 12012 X^6 +  6930 X^4 -  1260 X^2 +   35)/128
#    P( 9,X) =  (12155 X^9 - 25740 X^7 + 18018 X^5 -  4620 X^3 +  315 X)/128
#    P(10,X) =  (46189 X^10-109395 X^8 + 90090 X^6 - 30030 X^4 + 3465 X^2-63 ) /256
#
#  Recursion:
#
#    P(0,X) = 1
#    P(1,X) = X
#    P(N,X) = ( (2*N-1)*X*P(N-1,X)-(N-1)*P(N-2,X) ) / N
#
#    P'(0,X) = 0
#    P'(1,X) = 1
#    P'(N,X) = ( (2*N-1)*(P(N-1,X)+X*P'(N-1,X)-(N-1)*P'(N-2,X) ) / N
#
#  Formula:
#
#    P(N,X) = (1/2^N) * sum ( 0 <= M <= N/2 ) C(N,M) C(2N-2M,N) X^(N-2*M)
#
#  Orthogonality:
#
#    Integral ( -1 <= X <= 1 ) P(I,X) * P(J,X) dX
#      = 0 if I =/= J
#      = 2 / ( 2*I+1 ) if I = J.
#
#  Approximation:
#
#    A function F(X) defined on [-1,1] may be approximated by the series
#
#      C0*P(0,X) + C1*P(1,X) + \ + CN*P(N,X)
#
#    where
#
#      C(I) = (2*I+1)/(2) * Integral ( -1 <= X <= 1 ) F(X) P(I,X) dx.
#
#  Special values:
#
#    P(N,1) = 1.
#    P(N,-1) = (-1)^N.
#    | P(N,X) | <= 1 in [-1,1].
#
#    P(N,0,X) = P(N,X), that is, for M=0, the associated Legendre
#    function of the first kind and order N equals the Legendre polynomial
#    of the first kind and order N.
#
#    The N zeroes of P(N,X) are the abscissas used for Gauss-Legendre
#    quadrature of the integral of a function F(X) with weight function 1
#    over the interval [-1,1].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 22

  f_vec = np.array ( ( \
      0.1000000000000000E+01, \
      0.2500000000000000E+00, \
     -0.4062500000000000E+00, \
     -0.3359375000000000E+00, \
      0.1577148437500000E+00, \
      0.3397216796875000E+00, \
      0.2427673339843750E-01, \
     -0.2799186706542969E+00, \
     -0.1524540185928345E+00, \
      0.1768244206905365E+00, \
      0.2212002165615559E+00, \
      0.0000000000000000E+00, \
     -0.1475000000000000E+00, \
     -0.2800000000000000E+00, \
     -0.3825000000000000E+00, \
     -0.4400000000000000E+00, \
     -0.4375000000000000E+00, \
     -0.3600000000000000E+00, \
     -0.1925000000000000E+00, \
      0.8000000000000000E-01, \
      0.4725000000000000E+00, \
      0.1000000000000000E+01 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3 ))

  x_vec = np.array ( ( \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.00E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.90E+00, \
     1.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def legendre_poly_values_test ( ):

#*****************************************************************************80
#
## legendre_poly_values_test() tests legendre_poly_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'legendre_poly_values_test():' )
  print ( '  legendre_poly_values() stores values of the Legendre polynomials.' )
  print ( '' )
  print ( '      N            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = legendre_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, f ) )

  return

def legendre_symbol ( q, p ):

#*****************************************************************************80
#
## legendre_symbol() evaluates the Legendre symbol (Q/P).
#
#  Definition:
#
#    Let P be an odd prime.  Q is a QUADRATIC RESIDUE modulo P
#    if there is an integer R such that R^2 = Q ( mod P ).
#    The Legendre symbol ( Q / P ) is defined to be:
#
#      + 1 if Q ( mod P ) /= 0 and Q is a quadratic residue modulo P,
#      - 1 if Q ( mod P ) /= 0 and Q is not a quadratic residue modulo P,
#        0 if Q ( mod P ) == 0.
#
#    We can also define ( Q / P ) for P = 2 by:
#
#      + 1 if Q ( mod P ) /= 0
#        0 if Q ( mod P ) == 0
#
#  Example:
#
#    (0/7) =   0
#    (1/7) = + 1  ( 1^2 = 1 mod 7 )
#    (2/7) = + 1  ( 3^2 = 2 mod 7 )
#    (3/7) = - 1
#    (4/7) = + 1  ( 2^2 = 4 mod 7 )
#    (5/7) = - 1
#    (6/7) = - 1
#
#  Note:
#
#    For any prime P, exactly half of the integers from 1 to P-1
#    are quadratic residues.
#
#    ( 0 / P ) = 0.
#
#    ( Q / P ) = ( mod ( Q, P ) / P ).
#
#    ( Q / P ) = ( Q1 / P ) * ( Q2 / P ) if Q = Q1 * Q2.
#
#    If Q is prime, and P is prime and greater than 2, then:
#
#      if ( Q == 1 ) then
#
#        ( Q / P ) = 1
#
#      else if ( Q == 2 ) then
#
#        ( Q / P ) = + 1 if mod ( P, 8 ) = 1 or mod ( P, 8 ) = 7,
#        ( Q / P ) = - 1 if mod ( P, 8 ) = 3 or mod ( P, 8 ) = 5.
#
#      else
#
#        ( Q / P ) = - ( P / Q ) if Q = 3 ( mod 4 ) and P = 3 ( mod 4 ),
#                  =   ( P / Q ) otherwise.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Pinter,
#    A Book of Abstract Algebra,
#    McGraw Hill, 1982, pages 236-237.
#
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996, pages 86-87.
#
#  Input:
#
#    integer Q, an integer whose Legendre symbol with
#    respect to P is desired.
#
#    integer P, a prime number, greater than 1, with respect
#    to which the Legendre symbol of Q is desired.
#
#    integer L, the Legendre symbol (Q/P).
#    Ordinarily, L will be -1, 0 or 1.
#    L = -2, P is less than or equal to 1.
#    L = -3, P is not prime.
#    L = -4, the internal stack of factors overflowed.
#    L = -5, not enough factorization space.
#
  import numpy as np

  l = 0
#
#  P must be greater than 1.
#
  if ( p <= 1 ):
    print ( '' )
    print ( 'legendre_symbol(): Fatal error!' )
    print ( '  P must be greater than 1.' )
    l = -2
    raise Exception ( 'legendre_symbol(): Fatal error!' )
#
#  P must be prime.
#
  if ( not ( i4_is_prime ( p ) ) ):
    print ( '' )
    print ( 'legendre_symbol(): Fatal error!' )
    print ( '  P is not prime.' )
    l = -3
    raise Exception ( 'legendre_symbol(): Fatal error!' )
#
#  ( k*P / P ) = 0.
#
  if ( ( q % p ) == 0 ):
    l = 0
    return l
#
#  For the special case P = 2, (Q/P) = 1 for all odd numbers.
#
  if ( p == 2 ):
    l = 1
    return l

#
#  Make a copy of Q, and force it to be nonnegative.
#
  qq = q

  while ( qq < 0 ):
    qq = qq + p

  nstack = 0
  pstack = np.zeros ( 100 )
  qstack = np.zeros ( 100 )
  pp = p
  l = 1

  while ( True ):

    qq = ( qq % pp )
#
#  Decompose QQ into factors of prime powers.
#
    nfactor, factor, power, nleft = i4_factor ( qq )

    if ( nleft != 1 ):
      print ( '' )
      print ( 'legendre_symbol(): Fatal error!' )
      print ( '  Not enough factorization space.' )
      l = -5
      raise Exception ( 'legendre_symbol(): Fatal error!' )
#
#  Each factor which is an odd power is added to the stack.
#
    nmore = 0

    for i in range ( 0, nfactor ):

      if ( ( power[i] % 2 ) == 1 ):

        nmore = nmore + 1
        pstack[nstack] = pp
        qstack[nstack] = factor[i]
        nstack = nstack + 1

    hop = False

    if ( nmore != 0 ):

      nstack = nstack - 1
      qq = qstack[nstack]
#
#  Check for a QQ of 1 or 2.
#
      if ( qq == 1 ):

        l = + 1 * l

      elif ( qq == 2 and ( ( pp % 8 ) == 1 or ( pp % 8 ) == 7 ) ):

        l = + 1 * l

      elif ( qq == 2 and ( ( pp % 8 ) == 3 or ( pp % 8 ) == 5 ) ):

        l = - 1 * l

      else:

        if ( ( pp % 4 ) == 3 and ( qq % 4 ) == 3 ):
          l = - 1 * l

        rr = pp
        pp = qq
        qq = rr

        hop = True
#
#  If the stack is empty, we're done.
#
    if ( not hop ):

      if ( nstack == 0 ):
        break
#
#  Otherwise, get the last P and Q from the stack, and process them.
#
      nstack = nstack - 1
      pp = pstack[nstack]
      qq = qstack[nstack]

  return l

def legendre_symbol_test ( ):

#*****************************************************************************80
#
## legendre_symbol_test_test() tests legendre_symbol_test().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  ntest = 4
  ptest = [ 7, 11, 13, 17 ]

  print ( '' )
  print ( 'legendre_symbol_test():' )
  print ( '  legendre_symbol() computes the Legendre' )
  print ( '  symbol (Q/P) which records whether Q is' )
  print ( '  a quadratic residue modulo the prime P.' )

  for i in range ( 0, ntest ):
    p = ptest[i]
    print ( '' )
    print ( '  Legendre Symbols for P = %d' % ( p ) )
    print ( '' )
    for q in range ( 0, p + 1 ):
      l = legendre_symbol ( q, p )
      print ( '  %6d  %6d  %6d' % ( p, q, l ) )

  return

def lerch ( z, s, a ):

#*****************************************************************************80
#
## lerch() estimates the Lerch transcendent function.
#
#  Discussion:
#
#    The Lerch transcendent function is defined as:
#
#      LERCH ( Z, S, A ) = Sum ( 0 <= K < Infinity ) Z^K / ( A + K )^S
#
#    excluding any term with ( A + K ) = 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      LerchPhi[z,s,a]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein, editor,
#    CRC Concise Encylopedia of Mathematics,
#    CRC Press, 1998.
#
#  Thanks:
#
#    Oscar van Vlijmen
#
#  Input:
#
#    real Z, integer S, real A,
#    the parameters of the function.
#
#    real VALUE, an approximation to the Lerch
#    transcendent function.
#
  value = 0.0

  if ( z <= 0.0 ):
    return value

  eps = 1.0E-10
  k = 0
  z_k = 1.0

  while ( True ):

    if ( a + k != 0.0 ):

      term = z_k / ( a + k ) ** s
      value = value + term

      if ( abs ( term ) <= eps * ( 1.0 + abs ( value ) ) ):
        break

    k = k + 1
    z_k = z_k * z

  return value

def lerch_test ( ):

#*****************************************************************************80
#
## lerch_test() tests lerch().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'lerch_test():' )
  print ( '  lerch() evaluates the Lerch function;' )
  print ( '' )
  print ( '       Z       S       A         Lerch           Lerch' )
  print ( '                             Tabulated        Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, z, s, a, f = lerch_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = lerch ( z, s, a )

    print ( '  %8g  %4d  %8g  %14g  %14g' % ( z, s, a, f, f2 ) )

  return

def lerch_values ( n_data ):

#*****************************************************************************80
#
## lerch_values() returns some values of the Lerch transcendent function.
#
#  Discussion:
#
#    The Lerch function is defined as
#
#      Phi(z,s,a) = Sum ( 0 <= k < Infinity ) z^k / ( a + k )^s
#
#    omitting any terms with ( a + k ) = 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      LerchPhi[z,s,a]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real Z, the parameters of the function.
#
#    integer S, the parameters of the function.
#
#    real A, the parameters of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 12

  a_vec = np.array ( ( \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     2.0E+00, \
     2.0E+00, \
     2.0E+00, \
     3.0E+00, \
     3.0E+00, \
     3.0E+00 ))

  f_vec = np.array ( ( \
     0.1644934066848226E+01, \
     0.1202056903159594E+01, \
     0.1000994575127818E+01, \
     0.1164481052930025E+01, \
     0.1074426387216080E+01, \
     0.1000492641212014E+01, \
     0.2959190697935714E+00, \
     0.1394507503935608E+00, \
     0.9823175058446061E-03, \
     0.1177910993911311E+00, \
     0.3868447922298962E-01, \
     0.1703149614186634E-04 ))

  s_vec = np.array ( ( \
     2, 3, 10, \
     2, 3, 10, \
     2, 3, 10, \
     2, 3, 10 ))

  z_vec = np.array ( ( \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.5000000000000000E+00, \
     0.5000000000000000E+00, \
     0.5000000000000000E+00, \
     0.3333333333333333E+00, \
     0.3333333333333333E+00, \
     0.3333333333333333E+00, \
     0.1000000000000000E+00, \
     0.1000000000000000E+00, \
     0.1000000000000000E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    z = 0.0
    s = 0
    a = 0.0
    f = 0.0
  else:
    z = z_vec[n_data]
    s = s_vec[n_data]
    a = a_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, z, s, a, f

def lerch_values_test ( ):

#*****************************************************************************80
#
## lerch_values_test() tests lerch_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'lerch_values_test():' )
  print ( '  lerch_values() stores values of the Lerch function.' )
  print ( '' )
  print ( '        Z            S        A               F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, z, s, a, f = lerch_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %6d  %12f  %24.16f' % ( z, s, a, f ) )

  return

def lock ( n ):

#*****************************************************************************80
#
## lock() returns the number of codes for a lock with N buttons.
#
#  Discussion:
#
#    A button lock has N numbered buttons.  To open the lock, groups
#    of buttons must be pressed in the correct order.  Each button
#    may be pushed no more than once.  Thus, a code for the lock is
#    an ordered list of the groups of buttons to be pushed.
#
#    For this discussion, we will assume that EVERY button is pushed
#    at some time, as part of the code.  To count the total number
#    of codes, including those which don't use all the buttons, then
#    the number is 2 * A(N), or 2 * A(N) - 1 if we don't consider the
#    empty code to be valid.
#
#  Examples:
#
#    If there are 3 buttons, then there are 13 possible "full button" codes:
#
#      (123)
#      (12) (3)
#      (13) (2)
#      (23) (1)
#      (1) (23)
#      (2) (13)
#      (3) (12)
#      (1) (2) (3)
#      (1) (3) (2)
#      (2) (1) (3)
#      (2) (3) (1)
#      (3) (1) (2)
#      (3) (2) (1)
#
#    and, if we don't need to push all the buttons, every "full button" code above
#    yields a distinct "partial button" code by dropping the last set of buttons:
#
#      ()
#      (12)
#      (13)
#      (23)
#      (1)
#      (2)
#      (3)
#      (1) (2)
#      (1) (3)
#      (2) (1)
#      (2) (3)
#      (3) (1)
#      (3) (2)
#
#  First values:
#
#     N         A(N)
#     0           1
#     1           1
#     2           3
#     3          13
#     4          75
#     5         541
#     6        4683
#     7       47293
#     8      545835
#     9     7087261
#    10   102247563
#
#  Recursion:
#
#    A(I) = sum ( 0 <= J < I ) Binomial ( I, N-J ) * A(J)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Velleman, Gregory Call,
#    Permutations and Combination Locks,
#    Mathematics Magazine,
#    Volume 68, Number 4, October 1995, pages 243-253.
#
#  Input:
#
#    integer N, the maximum number of lock buttons.
#
#  Output:
#
#    integer A(1:N+1), the number of lock codes.
#
  import numpy as np

  a = np.zeros ( n + 1 )

  a[0] = 1

  for i in range ( 1, n + 1 ):
    a[i] = 0
    for j in range ( 0, i ):
      a[i] = a[i] + i4_choose ( i, i - j ) * a[j]

  return a

def lock_test ( ):

#*****************************************************************************80
#
## lock_test() tests lock().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'lock_test():' )
  print ( '  lock() counts the combinations on a button lock.' )
  print ( '' )
  print ( '  I   LOCK(I)' )
  print ( '' )

  a = lock ( n )

  for i in range ( 0, n + 1 ):
    print ( '  %2d  %10d' % ( i, a[i] ) )

  return

def meixner ( n, beta, c, x ):

#*****************************************************************************80
#
## meixner() evaluates Meixner polynomials at a point.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2010
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Walter Gautschi,
#    Orthogonal Polynomials: Computation and Approximation,
#    Oxford, 2004,
#    ISBN: 0-19-850672-4,
#    LC: QA404.5 G3555.
#
#  Input:
#
#    integer N, the maximum order of the polynomial.  
#    N must be at least 0.
#
#    real BETA, the Beta parameter.  0 < BETA.
#
#    real C, the C parameter.  0 < C < 1.
#
#    real X, the evaluation point.
#
#    real VALUE(N+1), the value of the polynomials at X.
#
  import numpy as np

  value = np.zeros ( n + 1 )

  if ( beta <= 0.0 ):
    print ( '' )
    print ( 'meixner(): Fatal error!' )
    print ( '  Parameter BETA must be positive.' )

  if ( c <= 0.0 or 1.0 <= c ):
    print ( '' )
    print ( 'meixner(): Fatal error!' )
    print ( '  Parameter C must be strictly between 0 and 1.' )

  if ( n < 0 ):
    print ( '' )
    print ( 'meixner(): Fatal error!' )
    print ( '  Parameter N must be nonnegative.' )

  value[0] = 1.0

  if ( 0 < n ):

    value[1] = ( c - 1.0 ) * x / beta / c + 1.0

    for i in range ( 1, n ):
      value[i+1] = ( \
        ( ( c - 1.0 ) * x + ( 1.0 + c ) * float ( i ) + beta * c ) * value[i] \
        - float ( i ) * value[i-1] \
        ) / ( float ( i ) + beta )

  return value

def meixner_test ( ):

#*****************************************************************************80
#
## meixner_test() tests meixner().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 3
  beta_test = np.array ( [ 0.5, 1.0, 2.0 ] )
  c_test = np.array ( [ 0.125, 0.25, 0.5 ] )
 
  print ( '' )
  print ( 'meixner_test():' )
  print ( '  meixner() evaluates Meixner polynomials.' )
  print ( '' )
  print ( '       N      BETA         C         X        M(N,BETA,C,X)' )

  for test in range ( 0, test_num ):

    n = 5
    beta = beta_test[test]
    c = c_test[test]

    for j in range ( 0, 6 ):

      x = float ( j ) / 2.0

      value = meixner ( n, beta, c, x )

      print ( '' )

      for i in range ( 0, n + 1 ):

        print ( '  %8d  %8g  %8g  %8g  %14g' % ( i, beta, c, x, value[i] ) )

  return

def mertens ( n ):

#*****************************************************************************80
#
## mertens() evaluates the Mertens function.
#
#  Discussion:
#
#    The Mertens function M(N) is the sum from 1 to N of the Moebius
#    function MU.  That is,
#
#    M(N) = sum ( 1 <= I <= N ) MU(I)
#
#        N   M(N)
#        --  ----
#         1     1
#         2     0
#         3    -1
#         4    -1
#         5    -2
#         6    -1
#         7    -2
#         8    -2
#         9    -2
#        10    -1
#        11    -2
#        12    -2
#       100     1
#      1000     2
#     10000   -23
#    100000   -48
#
#    The determinant of the Redheffer matrix of order N is equal
#    to the Mertens function M(N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    M Deleglise, J Rivat,
#    Computing the Summation of the Moebius Function,
#    Experimental Mathematics,
#    Volume 5, 1996, pages 291-295.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 2002,
#    Second edition,
#    ISBN: 1584883472,
#    LC: QA5.W45
#
#  Input:
#
#    integer N, the argument.
#
#    integer VALUE, the value.
#
  value = 0

  for i in range ( 1, n + 1 ):
    value = value + moebius ( i )

  return value

def mertens_test ( ):

#*****************************************************************************80
#
## mertens_test() tests mertens().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'mertens_test():' )
  print ( '  mertens() computes the Mertens function.' )
  print ( '' )
  print ( '    N   Exact   MERTENS(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = mertens_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = mertens ( n )

    print ( '  %4d  %8d  %8d' % ( n, c, c2 ) )

  return

def mertens_values ( n_data ):

#*****************************************************************************80
#
## mertens_values() returns some values of the Mertens function.
#
#  Discussion:
#
#    The Mertens function M(N) is the sum from 1 to N of the Moebius
#    function MU.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    M Deleglise, J Rivat,
#    Computing the Summation of the Moebius Function,
#    Experimental Mathematics,
#    Volume 5, 1996, pages 291-295.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 2002,
#    Second edition,
#    ISBN: 1584883472,
#    LC: QA5.W45.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the Mertens function.
#
#    integer C, the value of the Mertens function.
#
  import numpy as np

  n_max = 15

  c_vec = np.array ( ( \
      1,   0,  -1,   -1,  -2,  -1,  -2,  -2,   -2,  -1, \
     -2,  -2,   1,    2, -23 ))

  n_vec = np.array ( ( \
      1,   2,   3,   4,   5,   6,   7,   8,   9,  10, \
     11,  12,  100, 1000, 10000 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def mertens_values_test ( ):

#*****************************************************************************80
#
## mertens_values_test() tests mertens_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'mertens_values_test():' )
  print ( '  mertens_values() stores values of the Mertens function.' )
  print ( '' )
  print ( '             N    MERTENS(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = mertens_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12d' % ( n, c ) )

  return

def moebius ( n ):

#*****************************************************************************80
#
## moebius() returns the value of MU(N), the Moebius function of N.
#
#  Definition:
#
#    MU(N) is defined as follows:
#
#      MU(N) = 1 if N = 1;
#              0 if N is divisible by the square of a prime;
#              (-1)^K, if N is the product of K distinct primes.
#
#  First values:
#
#     N  MU(N)
#
#     1    1
#     2   -1
#     3   -1
#     4    0
#     5   -1
#     6    1
#     7   -1
#     8    0
#     9    0
#    10    1
#    11   -1
#    12    0
#    13   -1
#    14    1
#    15    1
#    16    0
#    17   -1
#    18    0
#    19   -1
#    20    0
#
#    As special cases, MU(N) is -1 if N is a prime, and MU(N) is 0
#    if N is a square, cube, etc.
#
#    The Moebius function is related to Euler's totient function:
#
#      PHI(N) = Sum ( D divides N ) MU(D) * ( N / D ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the value to be analyzed.
#
#    integer VALUE, the value of MU(N).
#    If N is less than or equal to 0, MU will be returned as -2.
#    If there was not enough internal space for factoring, MU
#    is returned as -3.
#
  if ( n <= 0 ):
    value = -2
    return value

  if ( n == 1 ):
    value = 1
    return value
#
#  Factor N.
#
  nfactor, factor, power, nleft = i4_factor ( n )

  if ( nleft != 1 ):
    print ( '' )
    print ( 'moebius(): Fatal error!' )
    print ( '  Incomplete factorization.' )
    value = -3

  value = 1

  for i in range ( 0, nfactor ):
 
    value = - value

    if ( 1 < power[i] ):
      value = 0
      return value

  return value

def moebius_test ( ):

#*****************************************************************************80
#
## moebius_test() tests moebius().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'moebius_test():' )
  print ( '  moebius() computes the Moebius function.' )
  print ( '' )
  print ( '    N   Exact   MOEBIUS(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = moebius_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = moebius ( n )

    print ( '  %4d  %8d  %8d' % ( n, c, c2 ) )

  return

def moebius_values ( n_data ):

#*****************************************************************************80
#
## moebius_values() returns some values of the Moebius function.
#
#  Discussion:
#
#    MU(N) is defined as follows:
#
#      MU(N) = 1 if N = 1;
#              0 if N is divisible by the square of a prime;
#              (-1)^K, if N is the product of K distinct primes.
#
#    In Mathematica, the function can be evaluated by:
#
#      MoebiusMu[n]
#
#  First values:
#
#     N  MU(N)
#
#     1    1
#     2   -1
#     3   -1
#     4    0
#     5   -1
#     6    1
#     7   -1
#     8    0
#     9    0
#    10    1
#    11   -1
#    12    0
#    13   -1
#    14    1
#    15    1
#    16    0
#    17   -1
#    18    0
#    19   -1
#    20    0
#
#    As special cases, MU(N) is -1 if N is a prime, and MU(N) is 0
#    if N is a square, cube, etc.
#
#  Formula:
#
#    The Moebius function is related to Euler's totient function:
#
#      PHI(N) = Sum ( D divides N ) MU(D) * ( N / D ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the Moebius function.
#
#    integer C, the value of the Moebius function.
#
  import numpy as np

  n_max = 20

  c_vec = np.array ( ( \
      1,  -1,  -1,   0,  -1,   1,  -1,   0,   0,   1, \
     -1,   0,  -1,   1,   1,   0,  -1,   0,  -1,   0 ))

  n_vec = np.array ( ( \
      1,   2,   3,   4,   5,   6,   7,   8,   9,  10, \
     11,  12,  13,  14,  15,  16,  17,  18,  19,  20 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def moebius_values_test ( ):

#*****************************************************************************80
#
## moebius_values_test() tests moebius_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'moebius_values_test():' )
  print ( '  moebius_values() stores values of the MOEBIUS function.' )
  print ( '' )
  print ( '             N    MOEBIUS(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = moebius_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12d' % ( n, c ) )

  return

def motzkin ( n ):

#*****************************************************************************80
#
## motzkin() returns the Motzkin numbers up to order N.
#
#  Discussion:
#
#    The Motzkin number A(N) counts the number of distinct paths from
#    (0,0) to (0,N) in which the only steps used are
#    (1,1), (1,-1) and (1,0), and the path is never allowed to
#    go below the X axis.
#
#  First values:
#
#     N  A(N)
#
#     0    1
#     1    1
#     2    2
#     3    4
#     4    9
#     5   21
#     6   51
#     7  127
#     8  323
#     9  835
#    10 2188
#
#  Recursion:
#
#    A(N) = A(N-1) + sum ( 0 <= K <= N-2 ) A(K) * A(N-2-K)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1998
#
#  Input:
#
#    integer N, the highest order Motzkin number to compute.
#
#    integer A(1:N+1), the Motzkin numbers.
#
  import numpy as np

  a = np.zeros ( n + 1 )

  a[0] = 1

  for i in range ( 1, n + 1 ):
    a[i] = a[i-1]
    for j in range ( 0, i - 1 ):
      a[i] = a[i] + a[j] * a[i-j-2]

  return a

def motzkin_test ( ):

#*****************************************************************************80
#
## motzkin_test() tests motzkin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'motzkin_test():' )
  print ( '  motzkin() computes the Motzkin numbers A(0:N).' )
  print ( '  A(N) counts the paths from (0,0) to (N,0).' )
  print ( '' )
  print ( '     I  A(I)' )
  print ( '' )

  a = motzkin ( n )

  for i in range ( 0, n + 1 ):
    print ( '  %4d  %10d' % ( i, a[i] ) )

  return

def normal_01_cdf_inverse ( p ):

#*****************************************************************************80
#
## normal_01_cdf_inverse() inverts the standard normal CDF.
#
#  Discussion:
#
#    The result is accurate to about 1 part in 10^16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    Original FORTRAN77 version by Michael Wichura.
#    This version by John Burkardt.
#
#  Reference:
#
#    Michael Wichura,
#    The Percentage Points of the Normal Distribution,
#    Algorithm AS 241,
#    Applied Statistics,
#    Volume 37, Number 3, pages 477-484, 1988.
#
#  Input:
#
#    real P, the value of the cumulative probability 
#    densitity function.  0 < P < 1.  If P is not in this range, an "infinite"
#    result is returned.
#
#    real VALUE, the normal deviate value with the 
#    property that the probability of a standard normal deviate being 
#    less than or equal to the value is P.
#
  import numpy as np

  a = np.array ( (\
        3.3871328727963666080,      1.3314166789178437745e+2, \
        1.9715909503065514427e+3,   1.3731693765509461125e+4, \
        4.5921953931549871457e+4,   6.7265770927008700853e+4, \
        3.3430575583588128105e+4,   2.5090809287301226727e+3 ))

  b = np.array ( (\
        1.0,                        4.2313330701600911252e+1, \
        6.8718700749205790830e+2,   5.3941960214247511077e+3, \
        2.1213794301586595867e+4,   3.9307895800092710610e+4, \
        2.8729085735721942674e+4,   5.2264952788528545610e+3 ))

  c = np.array ( (\
        1.42343711074968357734,     4.63033784615654529590, \
        5.76949722146069140550,     3.64784832476320460504, \
        1.27045825245236838258,     2.41780725177450611770e-1, \
        2.27238449892691845833e-2,  7.74545014278341407640e-4 ))

  const1 = 0.180625

  const2 = 1.6

  d = np.array ( (\
        1.0,                        2.05319162663775882187,    \
        1.67638483018380384940,     6.89767334985100004550e-1, \
        1.48103976427480074590e-1,  1.51986665636164571966e-2, \
        5.47593808499534494600e-4,  1.05075007164441684324e-9 ))

  e = np.array ( (\
        6.65790464350110377720,     5.46378491116411436990,    \
        1.78482653991729133580,     2.96560571828504891230e-1, \
        2.65321895265761230930e-2,  1.24266094738807843860e-3, \
        2.71155556874348757815e-5,  2.01033439929228813265e-7 ))

  f = np.array ( (\
        1.0,               5.99832206555887937690e-1, \
        1.36929880922735805310e-1,  1.48753612908506148525e-2, \
        7.86869131145613259100e-4,  1.84631831751005468180e-5, \
        1.42151175831644588870e-7,  2.04426310338993978564e-15 ))

  split1 = 0.425
  split2 = 5.0

  if ( p <= 0.0 ):
    value = - np.finfo(float).max
    return value
 
  if ( 1.0 <= p ):
    value = np.finfo(float).max
    return value

  q = p - 0.5

  if ( abs ( q ) <= split1 ):

    r = const1 - q * q
    value = q * r8poly_value_horner ( 7, a, r ) \
              / r8poly_value_horner ( 7, b, r )

  else:

    if ( q < 0.0 ):
      r = p
    else:
      r = 1.0 - p

    if ( r <= 0.0 ):

      value = np.finfo(float).max

    else:

      r = np.sqrt ( - np.log ( r ) )

      if ( r <= split2 ):

        r = r - const2
        value = r8poly_value_horner ( 7, c, r ) \
              / r8poly_value_horner ( 7, d, r )

      else:

        r = r - split2
        value = r8poly_value_horner ( 7, e, r ) \
              / r8poly_value_horner ( 7, f, r )

    if ( q < 0.0 ):
      value = - value

  return value

def normal_01_cdf_inverse_test ( ):

#*****************************************************************************80
#
## normal_01_cdf_inverse_test() tests normal_01_cdf_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'normal_01_cdf_inverse_test():' )
  print ( '  normal_01_cdf_inverse() inverts the error function.' )
  print ( '' )
  print ( '       FX                       X         normal_01_cdf_inverse(FX)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x1, fx = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    x2 = normal_01_cdf_inverse ( fx )

    print ( '  %12g  %24.16g  %24.16g' % ( fx, x1, x2 ) )

  return

def normal_01_cdf_values ( n_data ):

#*****************************************************************************80
#
## normal_01_cdf_values() returns some values of the Normal 01 CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NormalDistribution [ 0, 1 ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 17

  f_vec = np.array ( (\
     0.5000000000000000E+00, \
     0.5398278372770290E+00, \
     0.5792597094391030E+00, \
     0.6179114221889526E+00, \
     0.6554217416103242E+00, \
     0.6914624612740131E+00, \
     0.7257468822499270E+00, \
     0.7580363477769270E+00, \
     0.7881446014166033E+00, \
     0.8159398746532405E+00, \
     0.8413447460685429E+00, \
     0.9331927987311419E+00, \
     0.9772498680518208E+00, \
     0.9937903346742239E+00, \
     0.9986501019683699E+00, \
     0.9997673709209645E+00, \
     0.9999683287581669E+00 ))

  x_vec = np.array ((\
     0.0000000000000000E+00, \
     0.1000000000000000E+00, \
     0.2000000000000000E+00, \
     0.3000000000000000E+00, \
     0.4000000000000000E+00, \
     0.5000000000000000E+00, \
     0.6000000000000000E+00, \
     0.7000000000000000E+00, \
     0.8000000000000000E+00, \
     0.9000000000000000E+00, \
     0.1000000000000000E+01, \
     0.1500000000000000E+01, \
     0.2000000000000000E+01, \
     0.2500000000000000E+01, \
     0.3000000000000000E+01, \
     0.3500000000000000E+01, \
     0.4000000000000000E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def normal_01_cdf_values_test ( ):

#*****************************************************************************80
#
## normal_01_cdf_values_test() tests normal_01_cdf_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'normal_01_cdf_values_test():' )
  print ( '  normal_01_cdf_values() stores values of the unit normal CDF.' )
  print ( '' )
  print ( '      X         normal_01_cdf(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def omega ( n ) :

#*****************************************************************************80
#
## omega() returns OMEGA(N), the number of distinct prime divisors of N.
#
#  First values:
#
#     N   OMEGA(N)
#
#     1    1
#     2    1
#     3    1
#     4    1
#     5    1
#     6    2
#     7    1
#     8    1
#     9    1
#    10    2
#    11    1
#    12    2
#    13    1
#    14    2
#    15    2
#    16    1
#    17    1
#    18    2
#    19    1
#    20    2
#
#  Formula:
#
#    If N = 1, then
#
#      OMEGA(N) = 1
#
#    else if the prime factorization of N is
#
#      N = P1^E1 * P2^E2 * ... * PM^EM,
#
#    then
#
#      OMEGA(N) = M
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the value to be analyzed.  N must be 1 or
#    greater.
#
#    integer VALUE, the value of OMEGA(N).  But if N is 0 or
#    less, NDIV is returned as 0, a nonsense value.  If there is
#    not enough room for factoring, NDIV is returned as -1.
#
  if ( n <= 0 ):
    value = 0
    return value

  if ( n == 1 ):
    value = 1
    return value
#
#  Factor N.
#
  nfactor, factor, power, nleft = i4_factor ( n )

  if ( nleft != 1 ):
    print ( '' )
    print ( 'omega(): Fatal error!' )
    print ( '  Not enough factorization space.' )

  value = nfactor

  return value

def omega_test ( ):

#*****************************************************************************80
#
## omega_test() tests omega().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'omega_test():' )
  print ( '  omega() counts the distinct prime divisors of an integer N.' )
  print ( '' )
  print ( '         N      Exact         OMEGA(N)' )

  n_data = 0

  while ( True ):

    n_data, n, c1 = omega_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = omega ( n )

    print ( '  %8d  %12d  %12d' % ( n, c1, c2 ) ) 

  return

def omega_values ( n_data ):

#*****************************************************************************80
#
## omega_values() returns some values of the OMEGA function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by
#
#      Length [ FactorInteger [ n ] ]
#
#  First values:
#
#     N   OMEGA(N)
#
#     1    0
#     2    1
#     3    1
#     4    1
#     5    1
#     6    2
#     7    1
#     8    1
#     9    1
#    10    2
#    11    1
#    12    2
#    13    1
#    14    2
#    15    2
#    16    1
#    17    1
#    18    2
#    19    1
#    20    2
#
#  Formula:
#
#    If N = 1, then
#
#      OMEGA(N) = 0
#
#    else if the prime factorization of N is
#
#      N = P1^E1 * P2^E2 * \ * PM^EM,
#
#    then
#
#      OMEGA(N) = M
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the OMEGA function.
#
#    integer C, the value of the OMEGA function.
#
  import numpy as np

  n_max = 23

  c_vec = np.array ( ( \
      0,   1,   1,   1,   1, \
      2,   1,   1,   1,   2, \
      3,   1,   4,   4,   3, \
      1,   5,   2,   2,   1, \
      6,   7,   8 ))

  n_vec = np.array ( ( \
           1, \
           2, \
           3, \
           4, \
           5, \
           6, \
           7, \
           8, \
           9, \
          10, \
          30, \
         101, \
         210, \
        1320, \
        1764, \
        2003, \
        2310, \
        2827, \
        8717, \
       12553, \
       30030, \
      510510, \
     9699690 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def omega_values_test ( ):

#*****************************************************************************80
#
## omega_values_test() tests omega_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'omega_values_test():' )
  print ( '  omega_values() stores values of the OMEGA function.' )
  print ( '' )
  print ( '             N    OMEGA(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = omega_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12d' % ( n, c ) )

  return

def partition_distinct_count_values ( n_data ):

#*****************************************************************************80
#
## partition_distinct_count_values() returns some values of Q(N).
#
#  Discussion:
#
#    A partition of an integer N is a representation of the integer
#    as the sum of nonzero positive integers.  The order of the summands
#    does not matter.  The number of partitions of N is symbolized
#    by P(N).  Thus, the number 5 has P(N) = 7, because it has the
#    following partitions:
#
#    5 = 5
#      = 4 + 1
#      = 3 + 2
#      = 3 + 1 + 1
#      = 2 + 2 + 1
#      = 2 + 1 + 1 + 1
#      = 1 + 1 + 1 + 1 + 1
#
#    However, if we require that each member of the partition
#    be distinct, so that no nonzero summand occurs more than once,
#    we are computing something symbolized by Q(N).
#    The number 5 has Q(N) = 3, because it has the following partitions
#    into distinct parts:
#
#    5 = 5
#      = 4 + 1
#      = 3 + 2
#
#    In Mathematica, the function can be evaluated by
#
#      PartitionsQ[n]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the integer.
#
#    integer C, the number of partitions of the integer
#    into distinct parts.
#
  import numpy as np

  n_max = 21

  c_vec = np.array ( ( \
      1, \
      1,   1,   2,   2,   3,   4,   5,   6,   8,  10, \
     12,  15,  18,  22,  27,  32,  38,  46,  54,  64 ) )

  n_vec = np.array ( ( \
     0,  \
     1,  2,  3,  4,  5,  6,  7,  8,  9, 10, \
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def partition_distinct_count_values_test ( ):

#*****************************************************************************80
#
## partition_distinct_count_values_test(): test partition_distinct_count_values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'partition_distinct_count_values_test():' )
  print ( '  partition_distinct_count_values() returns values of ' )
  print ( '  the integer partition count function for distinct parts' )
  print ( '' )
  print ( '     N         P(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = partition_distinct_count_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %10d' % ( n, fn ) )

  return

def pentagon_num ( n ) :

#*****************************************************************************80
#
## pentagon_num() computes the N-th pentagonal number.
#
#  Definition:
#
#    The pentagonal number P(N) counts the number of dots in a figure of
#    N nested pentagons.  The pentagonal numbers are defined for both
#    positive and negative N.
#
#  First values:
#
#    N   P
#
#   -5  40
#   -4  26
#   -3  15
#   -2   7
#   -1   2
#    0   0
#    1   1
#    2   5
#    3  12
#    4  22
#    5  35
#
#  Formula:
#
#    P(N) = ( N * ( 3 * N - 1 ) ) / 2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the index of the pentagonal number desired.
#
#    integer P, the value of the N-th pentagonal number.
#
  value = ( n * ( 3 * n - 1 ) ) / 2

  return value

def pentagon_num_test ( ):

#*****************************************************************************80
#
## pentagon_num_test() tests pentagon_num().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pentagon_num_test():' )
  print ( '  pentagon_num() computes the pentagonal numbers.' )
  print ( '' )
  print ( '     N      pentagon_num(N)' )
  print ( '' )

  for n in range ( 1, 11 ):
    value = pentagon_num ( n )
    print ( '  %4d  %12d' % ( n, value ) )

  return

def phi ( n ):

#*****************************************************************************80
#
## phi() computes the number of relatively prime predecessors of an integer.
#
#  Definition:
#
#    PHI(N) is the number of integers between 1 and N which are
#    relatively prime to N.  I and J are relatively prime if they
#    have no common factors.  The function PHI(N) is known as
#    "Euler's totient function".
#
#    By convention, 1 and N are relatively prime.
#
#  First values:
#
#     N  PHI(N)
#
#     1    1
#     2    1
#     3    2
#     4    2
#     5    4
#     6    2
#     7    6
#     8    4
#     9    6
#    10    4
#    11   10
#    12    4
#    13   12
#    14    6
#    15    8
#    16    8
#    17   16
#    18    6
#    19   18
#    20    8
#
#  Formula:
#
#    PHI(U*V) = PHI(U) * PHI(V) if U and V are relatively prime.
#
#    PHI(P^K) = P^(K-1) * ( P - 1 ) if P is prime.
#
#    PHI(N) = N * Product ( P divides N ) ( 1 - 1 / P )
#
#    N = Sum ( D divides N ) PHI(D).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the value to be analyzed.
#
#    integer VALUE, the value of PHI(N).  If N is less than
#    or equal to 0, PHI will be returned as 0.  If there is not enough
#    room for full factoring of N, PHI will be returned as -1.
#
  if ( n <= 0 ):
    value = 0
    return value

  if ( n == 1 ):
    value = 1
    return value
#
#  Factor N.
#
  nfactor, factor, power, nleft = i4_factor ( n )

  if ( nleft != 1 ):
    print ( '' )
    print ( 'phi(): Fatal error!' )
    print ( '  Not enough factorization space.' )
 
  value = 1
  for i in range ( 0, nfactor ):
    value = value * factor[i] ** ( power[i] - 1 ) * ( factor[i] - 1 )

  return value

def phi_test ( ):

#*****************************************************************************80
#
## phi_test() tests phi().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'phi_test():' )
  print ( '  phi() computes the PHI function.' )
  print ( '' )
  print ( '         N      Exact         PHI(N)' )

  n_data = 0

  while ( True ):

    n_data, n, c1 = phi_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = phi ( n )

    print ( '  %8d  %12d  %12d' % ( n, c1, c2 ) )

  return

def phi_values ( n_data ):

#*****************************************************************************80
#
## phi_values() returns some values of the PHI function.
#
#  Discussion:
#
#    PHI(N) is the number of integers between 1 and N which are
#    relatively prime to N.  I and J are relatively prime if they
#    have no common factors.  The function PHI(N) is known as
#    "Euler's totient function".
#
#    By convention, 1 and N are relatively prime.
#
#    In Mathematica, the function can be evaluated by:
#
#      EulerPhi[n]
#
#  First values:
#
#     N  PHI(N)
#
#     1    1
#     2    1
#     3    2
#     4    2
#     5    4
#     6    2
#     7    6
#     8    4
#     9    6
#    10    4
#    11   10
#    12    4
#    13   12
#    14    6
#    15    8
#    16    8
#    17   16
#    18    6
#    19   18
#    20    8
#
#  Formula:
#
#    PHI(U*V) = PHI(U) * PHI(V) if U and V are relatively prime.
#
#    PHI(P^K) = P^(K-1) * ( P - 1 ) if P is prime.
#
#    PHI(N) = N * Product ( P divides N ) ( 1 - 1 / P )
#
#    N = Sum ( D divides N ) PHI(D).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the PHI function.
#
#    integer C, the value of the PHI function.
#
  import numpy as np

  n_max = 20

  c_vec = np.array ( ( \
      1,   1,   2,   2,   4,   2,   6,   4,   6,   4, \
      8,   8,  16,  20,  16,  40, 148, 200, 200, 648 ))

  n_vec = np.array ( ( \
      1,   2,   3,   4,   5,   6,   7,   8,   9,  10, \
     20,  30,  40,  50,  60, 100, 149, 500, 750, 999 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def phi_values_test ( ):

#*****************************************************************************80
#
## phi_values_test() tests phi_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'phi_values_test():' )
  print ( '  phi_values() stores values of the PHI function.' )
  print ( '' )
  print ( '             N    PHI(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = phi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12d' % ( n, c ) )

  return

def pi_estimate ( n ):

#*****************************************************************************80
#
## pi_estimate() estimates Pi(n), the number of primes less than or equal to n. 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2022
#
#  Input:
#
#    integer N: the argument.
#
#  Output:
#
#    real value: the estimate for Pi(n).
#
  import numpy as np

  value = n / np.log ( n )

  return value

def pi_estimate_test ( ):

#*****************************************************************************80
#
## pi_estimate_test() tests pi_estimate().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pi_estimate_test():' )
  print ( '  pi_estimate() estimates Pi(n), the number of primes' )
  print ( '  less than or equal to n.' )
  print ( '' )
  print ( '       N                Pi(n)                   Pi(n)                  Ratio' )
  print ( '                        estimated               tabulated' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, pi2 = pi_values ( n_data )

    if ( n_data == 0 ):
      break

    pi1 = pi_estimate ( n )

    r = pi1 / pi2

    print ( n, pi1, pi2, r )

  return

def pi_values ( n_data ):

#*****************************************************************************80
#
## pi_values() returns values of the Pi function.
#
#  Discussion:
#
#    Pi[n] is the number of primes less than or equal to n.
#
#    In Mathematica, the function can be evaluated by:
#
#      PrimePi[n]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_data.  The user sets N_data to 0 before the first call.  
#
#  Output:
#
#    integer N_data.  On each call, the routine increments N_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_data will be 0 again.
#
#    integer N, the argument.
#
#    integer P, the value of the function.
#
  import numpy as np

  n_max = 17

  n_vec = np.array ( ( \
            10, \
            20, \
            30, \
            40, \
            50, \
            60, \
            70, \
            80, \
            90, \
           100, \
          1000, \
         10000, \
        100000, \
       1000000, \
      10000000, \
     100000000, \
    1000000000 ))

  p_vec = np.array ( ( \
             4, \
             8, \
            10, \
            12, \
            15, \
            17, \
            19, \
            22, \
            24, \
            25, \
           168, \
          1229, \
          9592, \
         78498, \
        664579, \
       5761455, \
      50847534 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    p = 0
  else:
    n = n_vec[n_data]
    p = p_vec[n_data]
    n_data = n_data + 1

  return n_data, n, p

def plane_partition_num ( n ):

#*****************************************************************************80
#
## plane_partition_num() returns the number of plane partitions of the integer N.
#
#  Discussion:
#
#    A plane partition of a positive integer N is a partition of N in which
#    the parts have been arranged in a 2D array that is nonincreasing across
#    rows and columns.  There are six plane partitions of 3:
#
#      3   2 1   2   1 1 1   1 1   1
#                1           1     1
#                                  1
#
#  First Values:
#
#     N PP(N)
#     0    1
#     1    1
#     2    3
#     3    6
#     4   13
#     5   24
#     6   48
#     7   86
#     8  160
#     9  282
#    10  500
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 April 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frank Olver, Daniel Lozier, Ronald Boisvert, Charles Clark,
#    NIST Handbook of Mathematical Functions,
#    Cambridge University Press, 2010,
#    ISBN: 978-0521140638,
#    LC: QA331.N57.
#    
#  Input:
#
#    integer N, the number, which must be at least 0.
#
#    integer VALUE, the number of plane partitions of N.
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'plane_partition_num(): Fatal error!' )
    print ( '  0 <= N is required.' )

  pp = np.zeros ( n + 1 )

  nn = 0
  pp[nn] = 1

  nn = 1
  if ( nn <= n ):
    pp[nn] = 1

  for nn in range ( 2, n + 1 ):
    for j in range ( 1, nn + 1 ):
      s2 = 0
      for k in range ( 1, j + 1 ):
        if ( ( j % k ) == 0 ):
          s2 = s2 + k * k
      pp[nn] = pp[nn] + pp[nn-j] * s2
    pp[nn] = pp[nn] / nn

  value = pp[n]

  return value

def plane_partition_num_test ( ):

#*****************************************************************************80
#
## plane_partition_num_test() tests plane_partition_num().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'plane_partition_num_test():' )
  print ( '  plane_partition_num() computes the number of plane' )
  print ( '  partitions of an integer.' )
  print ( '' )
 
  for n in range ( 1, 11 ):
    p = plane_partition_num ( n )
    print ( '  %2d  %6d' % ( n, p ) )

  return

def polpak_test ( ):

#*****************************************************************************80
#
## polpak_test() tests polpak().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'polpak_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polpak().' )

  rng = default_rng ( )
#
#  Utilities.
#
  agm_values_test ( )
  bell_values_test ( )
  bernoulli_number_values_test ( )
  bernstein_poly_01_values_test ( )
  cheby_t_poly_values_test ( )
  cheby_u_poly_values_test ( )
  collatz_count_values_test ( )
  cos_power_int_values_test ( )
  erf_values_test ( )
  euler_number_values_test ( )
  gegenbauer_poly_values_test ( )
  gud_values_test ( )
  harmonic_values_test ( )
  hermite_poly_phys_values_test ( )
  hyper_2f1_values_test ( )
  i4_factorial2_values_test ( )
  i4mat_print_test ( )
  i4mat_print_some_test ( )
  i4vec_print_test ( )
  jacobi_poly_values_test ( )
  laguerre_polynomial_values_test ( )
  legendre_associated_values_test ( )
  lambert_w_test ( )
  lambert_w_estimate_test ( )
  legendre_associated_normalized_sphere_values_test ( )
  legendre_function_q_values_test ( )
  legendre_poly_values_test ( )
  lerch_values_test ( )
  mertens_values_test ( )
  moebius_values_test ( )
  normal_01_cdf_inverse_test ( )
  normal_01_cdf_values_test ( )
  omega_values_test ( )
  partition_distinct_count_values_test ( )
  phi_values_test ( )
  psi_values_test ( )
  r8_factorial_values_test ( )
  r8_factorial_log_values_test ( )
  r8_mop_test ( rng )
  r8_nint_test ( rng )
  r8poly_degree_test ( )
  r8poly_print_test ( )
  r8poly_value_horner_test ( )
  sigma_values_test ( )
  sin_power_int_values_test ( )
  spherical_harmonic_values_test ( )
#
#  Interesting stuff.
#
  agud_test ( )
  align_enum_test ( )
  bell_test ( )
  bell_poly_coef_test ( )
  benford_test ( )
  bernoulli_number_test ( )
  bernoulli_number2_test ( )
  bernoulli_number3_test ( )
  bernoulli_poly_test ( )
  bernoulli_poly2_test ( )
  bernstein_poly_test ( )
  bpab_test ( )
  cardan_poly_test ( )
  cardan_poly_coef_test ( )
  cardinal_cos_test ( )
  cardinal_sin_test ( )
  charlier_test ( )
  cheby_t_poly_test ( )
  cheby_t_poly_coef_test ( )
  cheby_t_poly_zero_test ( )
  cheby_u_poly_test ( )
  cheby_u_poly_coef_test ( )
  chebyshev_discrete_test ( )
  collatz_count_test ( )
  comb_row_next_test ( )
  commul_test ( )
  complete_symmetric_poly_test ( )
  conway_sequence_test ( )
  cos_power_int_test ( )
  delannoy_test ( )
  domino_tiling_num_test ( )
  euler_mascheroni_test ( )
  euler_number_test ( )
  euler_number2_test ( )
  euler_poly_test ( )
  eulerian_test ( )
  f_hofstadter_test ( )
  fibonacci_direct_test ( )
  fibonacci_floor_test ( )
  fibonacci_recursive_test ( )
  g_hofstadter_test ( )
  gegenbauer_poly_test ( )
  gen_hermite_poly_test ( )
  gen_laguerre_poly_test ( )
  gud_test ( )
  h_hofstadter_test ( )
  hail_test ( )
  harmonic_test ( )
  harmonic_estimate_test ( )
  hermite_poly_phys_test ( )
  hermite_poly_phys_coef_test ( )
  i4_choose_test ( )
  i4_factor_test ( )
  i4_factorial2_test ( )
  i4_is_fibonacci_test ( )
  i4_is_prime_test ( )
  i4_is_triangular_test ( )
  i4_partition_distinct_count_test ( )
  i4_to_triangle_lower_test ( )
  i4_to_triangle_upper_test ( )
  jacobi_poly_test ( )
  jacobi_symbol_test ( )
  krawtchouk_test ( )
  laguerre_associated_test ( )
  laguerre_poly_test ( )
  laguerre_poly_coef_test ( )
  legendre_associated_test ( )
  legendre_associated_normalized_test ( )
  legendre_function_q_test ( )
  legendre_poly_test ( )
  legendre_poly_coef_test ( )
  legendre_symbol_test ( )
  lerch_test ( )
  lock_test ( )
  meixner_test ( )
  mertens_test ( )
  moebius_test ( )
  motzkin_test ( )
  omega_test ( )
  pentagon_num_test ( )
  phi_test ( )
  pi_estimate_test ( )
  plane_partition_num_test ( )
  poly_bernoulli_test ( )
  poly_coef_count_test ( )
  prime_test ( )
  pyramid_num_test ( )
  pyramid_square_num_test ( )
  r8_agm_test ( )
  r8_beta_test ( )
  r8_choose_test ( )
  r8_erf_test ( )
  r8_erf_inverse_test ( )
  r8_factorial_test ( )
  r8_factorial_log_test ( )
  r8_hyper_2f1_test ( )
  r8_psi_test ( )
  sigma_test ( )
  simplex_num_test ( )
  sin_power_int_test ( )
  slices_test ( )
  spherical_harmonic_test ( )
  stirling_estimate_test ( )
  stirling1_table_test ( )
  stirling2_number_test ( )
  stirling2_table_test ( )
  tau_test ( )
  tetrahedron_num_test ( )
  triangle_num_test ( )
  triangle_lower_to_i4_test ( )
  triangle_upper_to_i4_test ( )
  tribonacci_direct_test ( )
  tribonacci_recursive_test ( )
  tribonacci_roots_test ( )
  trinomial_test ( )
  v_hofstadter_test ( )
  vibonacci_test ( rng )
  zeckendorf_test ( )
  zernike_poly_test ( )
  zernike_poly_coef_test ( )
  zeta_m1_test ( )
  zeta_naive_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polpak_test():' )
  print ( '  Normal end of execution.' )
  return

def poly_bernoulli ( n, k ):

#*****************************************************************************80
#
## poly_bernoulli() evaluates the poly-Bernolli numbers with negative index.
#
#  Discussion:
#
#    The poly-Bernoulli numbers B_n^k were defined by M Kaneko
#    formally as the coefficients of X^n/n! in a particular power
#    series.  He also showed that, when the super-index is negative,
#    we have
#
#      B_n^(-k) = Sum ( 0 <= j <= min ( n, k ) )
#        (j!)^2 * S(n+1,j+1) * S(k+1,j+1)
#
#    where S(n,k) is the Stirling number of the second kind, the number of
#    ways to partition a set of size n into k nonempty subset.
#
#    B_n^(-k) is also the number of "lonesum matrices", that is, 0-1
#    matrices of n rows and k columns which are uniquely reconstructable from
#    their row and column sums.
#
#    The poly-Bernoulli numbers get large very quickly.
#
#  Table:
#
#    \ K 0  1    2     3      4       5        6
#    N
#    0   1  1    1     1      1       1        1
#    1   1  2    4     8     16      32       64
#    2   1  4   14    46    146     454     1394
#    3   1  8   46   230   1066    4718    20266
#    4   1 16  146  1066   6902   41506   237686
#    5   1 32  454  4718  41506  329462  2441314
#    6   1 64 1394 20266 237686 2441314 22934774
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Chad Brewbaker,
#    Lonesum (0,1) Matrices and Poly-Bernoulli Numbers of Negative Index,
#    MS Thesis,
#    Iowa State University, 2005.
#
#    M Kaneko,
#    Poly-Bernoulli Numbers,
#    Journal Theorie des Nombres Bordeaux,
#    Volume 9, 1997, pages 221-228.
#
#  Input:
#
#    integer N, K, the indices.  N and K should be nonnegative.
#
#    integer VALUE, the value of B_N^(-K).
#
  if ( n < 0 ):
    value = 0
    return value

  if ( n == 0 ):
    value = 1
    return value

  if ( k < 0 ):
    value = 0
    return value

  if ( k == 0 ):
    value = 1
    return value

  jhi = min ( n, k )
  m = max ( n, k ) + 1

  s = stirling2_table ( m, m )

  jfact = 1
  value = 0

  for j in range ( 0, jhi + 1 ):

    value = value + jfact * jfact * s[n,j] * s[k,j]

    jfact = jfact * ( j + 1 )

  return value

def poly_bernoulli_test ( ):

#*****************************************************************************80
#
## poly_bernoulli_test() tests poly_bernoulli().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'poly_bernoulli_test():' )
  print ( '  poly_bernoulli() computes the poly-Bernoulli numbers' )
  print ( '  of negative index, B_n^(-k)' )
  print ( '' )
  print ( '     N     K    B_N^(-K)' )
  print ( '' )

  for k in range ( 0, 7 ):
    print ( '' )
    for n in range ( 0, 7 ):
      b = poly_bernoulli ( n, k )

      print ( '  %6d  %6d  %6d' % ( n, k, b ) )

  return

def poly_coef_count ( dim, degree ):

#*****************************************************************************80
#
## poly_coef_count(): polynomial coefficient count given dimension and degree.
#
#  Discussion:
#
#    To count all monomials of degree 5 or less in dimension 3,
#    we can count all monomials of degree 5 in dimension 4.
#
#    To count all monomials of degree 5 in dimension 4, we imagine
#    that each of the variables X, Y, Z and W is a "box" and that
#    we need to drop 5 pebbles into these boxes.  Every distinct
#    way of doing this represents a degree 5 monomial in dimension 4.
#    Ignoring W gives us monomials up to degree five in dimension 3.
#
#    To count them, we draw 3 lines as separators to indicate the
#    4 boxes, and then imagine all disctinct sequences involving
#    the three lines and the 5 pebbles.  Indicate the lines by 1's
#    and the pebbles by 0's and we're asking for the number of
#    permutations of 3 1's and 5 0's, which is 8! / (3! 5!)
#
#    In other words, 56 = 8! / (3! 5!) is:
#    * the number of monomials of degree exactly 5 in dimension 4,
#    * the number of monomials of degree 5 or less in dimension 3,
#    * the number of polynomial coefficients of a polynomial of
#      degree 5 in (X,Y,Z).
#
#    In general, the formula for the number of monomials of degree DEG
#    or less in dimension DIM is
#
#      (DEG+DIM)! / (DEG! * DIM!)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIM, the dimension of the polynomial.
#    0 <= DIM.
#
#    integer DEGREE, the degree of the polynomnial
#    0 <= DEGREE
#
#    integer VALUE, the number of coefficients
#    in the general polynomial of dimension DIM and degree DEGREE.
#
  if ( dim < 0 ):
    value = -1
  elif ( degree < 0 ):
    count = -1
  else:
    value = i4_choose ( degree + dim, degree )

  return value

def poly_coef_count_test ( ):

#*****************************************************************************80
#
## poly_coef_count_test() tests poly_coef_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'poly_coef_count_test():' )
  print ( '  poly_coef_count() counts the number of coefficients' )
  print ( '  in a polynomial of degree DEGREE and dimension DIM' )
  print ( '' )
  print ( ' Dimension    Degree     Count' )
  print ( '' )
 
  for dim in range ( 1, 11, 3 ):
    print ( '' )
    for degree in range ( 0, 6 ):
      value = poly_coef_count ( dim, degree )
      print ( '  %8d  %8d  %8d' % ( dim, degree, value ) )

  return

def prime ( n ):

#*****************************************************************************80
#
## prime() returns returns any of the first prime_max prime numbers.
#
#  Discussion:
#
#    prime_max is 1600, and the largest prime stored is 13499.
#
#    Thanks to Bart Vandewoestyne for pointing out a typo, 18 February 2005.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964, pages 870-873.
#
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996, pages 95-98.
#
#  Input:
#
#    integer N, the index of the desired prime number.
#    In general, is should be true that 0 <= N <= prime_max.
#    N = -1 returns prime_max, the index of the largest prime available.
#    N = 0 is legal, returning PRIME = 1.
#
#    integer P, the N-th prime.  If N is out of range, P
#    is returned as -1.
#
  prime_max = 1600

  prime_vector = ( (
        2,    3,    5,    7,   11,   13,   17,   19,   23,   29, \
       31,   37,   41,   43,   47,   53,   59,   61,   67,   71, \
       73,   79,   83,   89,   97,  101,  103,  107,  109,  113, \
      127,  131,  137,  139,  149,  151,  157,  163,  167,  173, \
      179,  181,  191,  193,  197,  199,  211,  223,  227,  229, \
      233,  239,  241,  251,  257,  263,  269,  271,  277,  281, \
      283,  293,  307,  311,  313,  317,  331,  337,  347,  349, \
      353,  359,  367,  373,  379,  383,  389,  397,  401,  409, \
      419,  421,  431,  433,  439,  443,  449,  457,  461,  463, \
      467,  479,  487,  491,  499,  503,  509,  521,  523,  541, \
      547,  557,  563,  569,  571,  577,  587,  593,  599,  601, \
      607,  613,  617,  619,  631,  641,  643,  647,  653,  659, \
      661,  673,  677,  683,  691,  701,  709,  719,  727,  733, \
      739,  743,  751,  757,  761,  769,  773,  787,  797,  809, \
      811,  821,  823,  827,  829,  839,  853,  857,  859,  863, \
      877,  881,  883,  887,  907,  911,  919,  929,  937,  941, \
      947,  953,  967,  971,  977,  983,  991,  997, 1009, 1013, \
     1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, \
     1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, \
     1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, \
     1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, \
     1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, \
     1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, \
     1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, \
     1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, \
     1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, \
     1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, \
     1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, \
     1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, \
     1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, \
     1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, \
     2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, \
     2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, \
     2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, \
     2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, \
     2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, \
     2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, \
     2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, \
     2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, \
     2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, \
     2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, \
     2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, \
     2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, \
     3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, \
     3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, \
     3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, \
     3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, \
     3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, \
     3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, \
     3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, \
     3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, \
     3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, \
     3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, \
     3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, \
     3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, \
     4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, \
     4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, \
     4153, 4157, 4159, 4177, 4201, 4211, 4217, 4219, 4229, 4231, \
     4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, \
     4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409, \
     4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, \
     4507, 4513, 4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, \
     4591, 4597, 4603, 4621, 4637, 4639, 4643, 4649, 4651, 4657, \
     4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729, 4733, 4751, \
     4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813, 4817, 4831, \
     4861, 4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937, \
     4943, 4951, 4957, 4967, 4969, 4973, 4987, 4993, 4999, 5003, \
     5009, 5011, 5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087, \
     5099, 5101, 5107, 5113, 5119, 5147, 5153, 5167, 5171, 5179, \
     5189, 5197, 5209, 5227, 5231, 5233, 5237, 5261, 5273, 5279, \
     5281, 5297, 5303, 5309, 5323, 5333, 5347, 5351, 5381, 5387, \
     5393, 5399, 5407, 5413, 5417, 5419, 5431, 5437, 5441, 5443, \
     5449, 5471, 5477, 5479, 5483, 5501, 5503, 5507, 5519, 5521, \
     5527, 5531, 5557, 5563, 5569, 5573, 5581, 5591, 5623, 5639, \
     5641, 5647, 5651, 5653, 5657, 5659, 5669, 5683, 5689, 5693, \
     5701, 5711, 5717, 5737, 5741, 5743, 5749, 5779, 5783, 5791, \
     5801, 5807, 5813, 5821, 5827, 5839, 5843, 5849, 5851, 5857, \
     5861, 5867, 5869, 5879, 5881, 5897, 5903, 5923, 5927, 5939, \
     5953, 5981, 5987, 6007, 6011, 6029, 6037, 6043, 6047, 6053, \
     6067, 6073, 6079, 6089, 6091, 6101, 6113, 6121, 6131, 6133, \
     6143, 6151, 6163, 6173, 6197, 6199, 6203, 6211, 6217, 6221, \
     6229, 6247, 6257, 6263, 6269, 6271, 6277, 6287, 6299, 6301, \
     6311, 6317, 6323, 6329, 6337, 6343, 6353, 6359, 6361, 6367, \
     6373, 6379, 6389, 6397, 6421, 6427, 6449, 6451, 6469, 6473, \
     6481, 6491, 6521, 6529, 6547, 6551, 6553, 6563, 6569, 6571, \
     6577, 6581, 6599, 6607, 6619, 6637, 6653, 6659, 6661, 6673, \
     6679, 6689, 6691, 6701, 6703, 6709, 6719, 6733, 6737, 6761, \
     6763, 6779, 6781, 6791, 6793, 6803, 6823, 6827, 6829, 6833, \
     6841, 6857, 6863, 6869, 6871, 6883, 6899, 6907, 6911, 6917, \
     6947, 6949, 6959, 6961, 6967, 6971, 6977, 6983, 6991, 6997, \
     7001, 7013, 7019, 7027, 7039, 7043, 7057, 7069, 7079, 7103, \
     7109, 7121, 7127, 7129, 7151, 7159, 7177, 7187, 7193, 7207, \
     7211, 7213, 7219, 7229, 7237, 7243, 7247, 7253, 7283, 7297, \
     7307, 7309, 7321, 7331, 7333, 7349, 7351, 7369, 7393, 7411, \
     7417, 7433, 7451, 7457, 7459, 7477, 7481, 7487, 7489, 7499, \
     7507, 7517, 7523, 7529, 7537, 7541, 7547, 7549, 7559, 7561, \
     7573, 7577, 7583, 7589, 7591, 7603, 7607, 7621, 7639, 7643, \
     7649, 7669, 7673, 7681, 7687, 7691, 7699, 7703, 7717, 7723, \
     7727, 7741, 7753, 7757, 7759, 7789, 7793, 7817, 7823, 7829, \
     7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919, \
     7927, 7933, 7937, 7949, 7951, 7963, 7993, 8009, 8011, 8017, \
     8039, 8053, 8059, 8069, 8081, 8087, 8089, 8093, 8101, 8111, \
     8117, 8123, 8147, 8161, 8167, 8171, 8179, 8191, 8209, 8219, \
     8221, 8231, 8233, 8237, 8243, 8263, 8269, 8273, 8287, 8291, \
     8293, 8297, 8311, 8317, 8329, 8353, 8363, 8369, 8377, 8387, \
     8389, 8419, 8423, 8429, 8431, 8443, 8447, 8461, 8467, 8501, \
     8513, 8521, 8527, 8537, 8539, 8543, 8563, 8573, 8581, 8597, \
     8599, 8609, 8623, 8627, 8629, 8641, 8647, 8663, 8669, 8677, \
     8681, 8689, 8693, 8699, 8707, 8713, 8719, 8731, 8737, 8741, \
     8747, 8753, 8761, 8779, 8783, 8803, 8807, 8819, 8821, 8831, \
     8837, 8839, 8849, 8861, 8863, 8867, 8887, 8893, 8923, 8929, \
     8933, 8941, 8951, 8963, 8969, 8971, 8999, 9001, 9007, 9011, \
     9013, 9029, 9041, 9043, 9049, 9059, 9067, 9091, 9103, 9109, \
     9127, 9133, 9137, 9151, 9157, 9161, 9173, 9181, 9187, 9199, \
     9203, 9209, 9221, 9227, 9239, 9241, 9257, 9277, 9281, 9283, \
     9293, 9311, 9319, 9323, 9337, 9341, 9343, 9349, 9371, 9377, \
     9391, 9397, 9403, 9413, 9419, 9421, 9431, 9433, 9437, 9439, \
     9461, 9463, 9467, 9473, 9479, 9491, 9497, 9511, 9521, 9533, \
     9539, 9547, 9551, 9587, 9601, 9613, 9619, 9623, 9629, 9631, \
     9643, 9649, 9661, 9677, 9679, 9689, 9697, 9719, 9721, 9733, \
     9739, 9743, 9749, 9767, 9769, 9781, 9787, 9791, 9803, 9811, \
     9817, 9829, 9833, 9839, 9851, 9857, 9859, 9871, 9883, 9887, \
     9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973,10007, \
    10009,10037,10039,10061,10067,10069,10079,10091,10093,10099, \
    10103,10111,10133,10139,10141,10151,10159,10163,10169,10177, \
    10181,10193,10211,10223,10243,10247,10253,10259,10267,10271, \
    10273,10289,10301,10303,10313,10321,10331,10333,10337,10343, \
    10357,10369,10391,10399,10427,10429,10433,10453,10457,10459, \
    10463,10477,10487,10499,10501,10513,10529,10531,10559,10567, \
    10589,10597,10601,10607,10613,10627,10631,10639,10651,10657, \
    10663,10667,10687,10691,10709,10711,10723,10729,10733,10739, \
    10753,10771,10781,10789,10799,10831,10837,10847,10853,10859, \
    10861,10867,10883,10889,10891,10903,10909,10937,10939,10949, \
    10957,10973,10979,10987,10993,11003,11027,11047,11057,11059, \
    11069,11071,11083,11087,11093,11113,11117,11119,11131,11149, \
    11159,11161,11171,11173,11177,11197,11213,11239,11243,11251, \
    11257,11261,11273,11279,11287,11299,11311,11317,11321,11329, \
    11351,11353,11369,11383,11393,11399,11411,11423,11437,11443, \
    11447,11467,11471,11483,11489,11491,11497,11503,11519,11527, \
    11549,11551,11579,11587,11593,11597,11617,11621,11633,11657, \
    11677,11681,11689,11699,11701,11717,11719,11731,11743,11777, \
    11779,11783,11789,11801,11807,11813,11821,11827,11831,11833, \
    11839,11863,11867,11887,11897,11903,11909,11923,11927,11933, \
    11939,11941,11953,11959,11969,11971,11981,11987,12007,12011, \
    12037,12041,12043,12049,12071,12073,12097,12101,12107,12109, \
    12113,12119,12143,12149,12157,12161,12163,12197,12203,12211, \
    12227,12239,12241,12251,12253,12263,12269,12277,12281,12289, \
    12301,12323,12329,12343,12347,12373,12377,12379,12391,12401, \
    12409,12413,12421,12433,12437,12451,12457,12473,12479,12487, \
    12491,12497,12503,12511,12517,12527,12539,12541,12547,12553, \
    12569,12577,12583,12589,12601,12611,12613,12619,12637,12641, \
    12647,12653,12659,12671,12689,12697,12703,12713,12721,12739, \
    12743,12757,12763,12781,12791,12799,12809,12821,12823,12829, \
    12841,12853,12889,12893,12899,12907,12911,12917,12919,12923, \
    12941,12953,12959,12967,12973,12979,12983,13001,13003,13007, \
    13009,13033,13037,13043,13049,13063,13093,13099,13103,13109, \
    13121,13127,13147,13151,13159,13163,13171,13177,13183,13187, \
    13217,13219,13229,13241,13249,13259,13267,13291,13297,13309, \
    13313,13327,13331,13337,13339,13367,13381,13397,13399,13411, \
    13417,13421,13441,13451,13457,13463,13469,13477,13487,13499 ) )

  if ( n == -1 ):
    p = prime_max
  elif ( n == 0 ):
    p = 1
  elif ( n <= prime_max ):
    p = prime_vector[n-1]
  else:
    p = -1

  return p

def prime_test ( ):

#*****************************************************************************80
#
## prime_test() tests prime().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'prime_test():' )
  print ( '  prime() returns primes from a table.' )

  n = -1
  prime_max = prime ( n )
  print ( '' )
  print ( '  Number of primes stored is %d' % ( prime_max ) )
  print ( '' )
  print ( '     I    Prime(I)' )
  print ( '' )
  for i in range ( 1, 11 ):
    print ( '    %4d  %6d' % ( i, prime(i) ) )
  print ( '' )
  for i in range ( prime_max - 10, prime_max + 1 ):
    print ( '    %4d  %6d' % ( i, prime(i) ) )

  return

def psi_values ( n_data ):

#*****************************************************************************80
#
## psi_values() returns some values of the Psi or Digamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      PolyGamma[x]
#
#    or
#
#      PolyGamma[0,x]
#
#    PSI(X) = d ln ( Gamma ( X ) ) / d X = Gamma'(X) / Gamma(X)
#
#    PSI(1) = -Euler's constant.
#
#    PSI(X+1) = PSI(X) + 1 / X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
    -10.42375494041108E+00, \
     -5.289039896592188E+00, \
     -3.502524222200133E+00, \
     -2.561384544585116E+00, \
     -1.963510026021423E+00, \
     -1.540619213893190E+00, \
     -1.220023553697935E+00, \
     -0.9650085667061385E+00, \
     -0.7549269499470514E+00, \
     -0.5772156649015329E+00, \
     -0.4237549404110768E+00, \
     -0.2890398965921883E+00, \
     -0.1691908888667997E+00, \
     -0.6138454458511615E-01, \
      0.3648997397857652E-01, \
      0.1260474527734763E+00, \
      0.2085478748734940E+00, \
      0.2849914332938615E+00, \
      0.3561841611640597E+00, \
      0.4227843350984671E+00 ))

  x_vec = np.array ( ( \
     0.1E+00, \
     0.2E+00, \
     0.3E+00, \
     0.4E+00, \
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00, \
     1.1E+00, \
     1.2E+00, \
     1.3E+00, \
     1.4E+00, \
     1.5E+00, \
     1.6E+00, \
     1.7E+00, \
     1.8E+00, \
     1.9E+00, \
     2.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def psi_values_test ( ):

#*****************************************************************************80
#
## psi_values_test() tests psi_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'psi_values_test():' )
  print ( '  psi_values() stores values of the PSI function.' )
  print ( '' )
  print ( '      X         PSI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def pyramid_num ( n ):

#*****************************************************************************80
#
## pyramid_num() returns the N-th pyramidal number.
#
#  Discussion:
#
#    The N-th pyramidal number P(N) is formed by the sum of the first
#    N triangular numbers T(J):
#
#      T(J) = sum ( 1 <= J <= N ) J
#
#      P(N) = sum ( 1 <= I <= N ) T(I)
#
#    By convention, T(0) = 0.
#
#    P(N) = ( (N+1)^3 - (N+1) ) / 6
#
#    Note that this pyramid will have a triangular base.
#
#    The first values are:
#
#      0
#      1
#      4
#     10
#     20
#     35
#     56
#     84
#    120
#    165
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the index of the desired number, which must be
#    at least 0.
#
#    integer VALUE, the N-th pyramidal number.
#
  value = ( ( n + 1 ) ** 3 - ( n + 1 ) ) / 6

  return value

def pyramid_num_test ( ):

#*****************************************************************************80
#
## pyramid_num_test() tests pyramid_num().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pyramid_num_test():' )
  print ( '  pyramid_num() computes the pyramidal numbers.' )
  print ( '' )
 
  for n in range ( 1, 11 ):
    print ( '  %2d  %6d' % ( n, pyramid_num ( n ) ) )

  return

def pyramid_square_num ( n ):

#*****************************************************************************80
#
## pyramid_square_num() returns the N-th pyramidal square number.
#
#  Discussion:
#
#    The N-th pyramidal square number PS(N) is formed by the sum of the first
#    N squares S:
#
#      S(I) = I^2
#
#      PS(N) = sum ( 1 <= I <= N ) S(I)
#
#    By convention, PS(0) = 0.
#
#    The formula is:
#
#      PS(N) = ( N * ( N + 1 ) * ( 2*N+1 ) ) / 6
#
#    Note that geometrically, this pyramid will have a square base.
#
#  Example:
#
#    0    0
#    1    1
#    2    5
#    3   14
#    4   30
#    5   55
#    6   91
#    7  140
#    8  204
#    9  285
#   10  385
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer  N, the index.
#    0 <= N.
#
#    integer pyramid_square_num, the N-th 
#    pyramid square number.
#
  value = ( n * ( n + 1 ) * ( 2 * n + 1 ) ) / 6

  return value

def pyramid_square_num_test ( ):

#*****************************************************************************80
#
## pyramid_square_num_test() tests pyramid_square_num().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pyramid_square_num_test():' )
  print ( '  pyramid_square_num() computes the pyramidal square numbers.' )
  print ( '' )
 
  for n in range ( 1, 11 ):
    print ( '  %2d  %6d' % ( n, pyramid_square_num ( n ) ) )

  return

def r8_agm ( a, b ):

#*****************************************************************************80
#
## r8_agm() computes the arithmetic-geometric mean of A and B.
#
#  Discussion:
#
#    The AGM is defined for nonnegative A and B.
#
#    The AGM of numbers A and B is defined by setting
#
#      A(0) = A,
#      B(0) = B
#
#      A(N+1) = ( A(N) + B(N) ) / 2
#      B(N+1) = sqrt ( A(N) * B(N) )
#
#    The two sequences both converge to AGM(A,B).
#
#    In Mathematica, the AGM can be evaluated by
#
#      ArithmeticGeometricMean [ a, b ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    real A, B, the arguments whose AGM is to be computed.
#    0 <= A, 0 <= B.
#
#    real VALUE, the arithmetic-geometric mean of A and B.
#
  import numpy as np

  it_max = 1000
  eps = 2.220446049250313E-016

  if ( a < 0.0 ):
    print ( '' )
    print ( 'r8_agm(): Fatal error!' )
    print ( '  Argument A < 0.' )
    raise Exception ( 'r8_agm(): Fatal error!' )

  if ( b < 0.0 ):
    print ( '' )
    print ( 'r8_agm(): Fatal error!' )
    print ( '  Argument B < 0.' )
    raise Exception ( 'r8_agm(): Fatal error!' )

  if ( a == 0.0 or b == 0.0 ):
    value = 0.0
    return value

  it = 0
  tol = 100.0 * eps

  a1 = a
  b1 = b

  while ( True ):

    it = it + 1

    a2 = ( a1 + b1 ) / 2.0
    b2 = np.sqrt ( a1 * b1 )

    if ( abs ( a2 - b2 ) <= tol * ( a2 + b2 ) ):
      break

    if ( it_max < it ):
      print ( '' )
      print ( 'r8_agm(): Warning!' )
      print ( '  No convergence.' )
      break

    a1 = a2
    b1 = b2

  value = a2

  return value

def r8_agm_test ( ):

#*****************************************************************************80
#
## r8_agm_test() tests r8_agm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_agm_test():' )
  print ( '  r8_agm() computes the arithmetic geometric mean.' )
  print ( '' )
  print ( '      A           B          ' ),
  print ( '   AGM                       AGM                   Diff' )
  print ( '                             ' ),
  print ( '  (Tabulated)             r8_agm(A,B)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, fx = agm_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_agm ( a, b )

    print ( '  %10.6f  %10.6f  %24.16f  %24.16f  %10.4g' % ( a, b, fx, fx2, abs ( fx - fx2 ) ) )

  return

def r8_beta ( x, y ):

#*****************************************************************************80
#
## r8_beta() returns the value of the Beta function.
#
#  Discussion:
#
#    The formula is
#
#      BETA(X,Y) = ( GAMMA(X) * GAMMA(Y) ) / GAMMA(X+Y)
#
#    Both X and Y must be greater than 0.
#
#  Properties:
#
#    BETA(X,Y) = BETA(Y,X).
#    BETA(X,Y) = Integral ( 0 <= T <= 1 ) T^(X-1) (1-T)^(Y-1) dT.
#    BETA(X,Y) = GAMMA(X) * GAMMA(Y) / GAMMA(X+Y)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, the two parameters that define the Beta function.
#    X and Y must be greater than 0.
#
#  Output:
#
#    real VALUE, the value of the Beta function.
#
  from scipy.special import gamma

  if ( x <= 0.0 or y <= 0.0 ):
    print ( '' )
    print ( 'r8_beta(): Fatal error!' )
    print ( '  Both X and Y must be greater than 0.' )
    raise Exception ( 'r8_beta(): Fatal error!' )

  value = gamma ( x ) * gamma ( y ) / gamma ( x + y )

  return value

def r8_beta_test ( ):

#*****************************************************************************80
#
## r8_beta_test() tests r8_beta().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_beta_test():' )
  print ( '  r8_beta() evaluates the Beta function.' )
  print ( '' )
  print ( '         X         Y                 BETA(X,Y)            r8_beta(X,Y)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, y, fx1 = beta_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_beta ( x, y )

    print ( '  %8.4g  %8.4g  %24.16g  %24.16g' % ( x, y, fx1, fx2 ) )

  return

def r8_choose ( n, k ):

#*****************************************************************************80
#
## r8_choose() computes the binomial coefficient C(N,K) as an R8.
#
#  Discussion:
#
#    The value is calculated in such a way as to avoid overflow and
#    roundoff.  The calculation is done in R8 arithmetic.
#
#    The formula used is:
#
#      C(N,K) = N! / ( K! * (N-K)! )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, K, are the values of N and K.
#
#  Output:
#
#    real VALUE, the number of combinations of N things taken K at a time.
#
  import numpy as np
  from scipy.special import gammaln

  if ( n < 0 ):

    value = 0.0

  elif ( k == 0 ):

    value = 1.0

  elif ( k == 1 ):

    value = float ( n )

  elif ( 1 < k and k < n - 1 ):

    facn = gammaln ( float ( n + 1 ) )
    fack = gammaln ( float ( k + 1 ) )
    facnmk = gammaln ( float ( n - k + 1 ) )

    value = round ( np.exp ( facn - fack - facnmk ) )

  elif ( k == n - 1 ):

    value = float ( n )

  elif ( k == n ):

    value = 1.0

  else:

    value = 0.0

  return value

def r8_choose_test ( ):

#*****************************************************************************80
#
## r8_choose_test() tests r8_choose().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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
  print ( 'r8_choose_test():' )
  print ( '  r8_choose() evaluates C(N,K).' )
  print ( '' )
  print ( '         N         K       CNK' )
 
  for n in range ( 0, 6 ):
    print ( '' )
    for k in range ( 0, n + 1 ):
      cnk = r8_choose ( n, k )
      print ( '  %8d  %8d  %14.6g' % ( n, k, cnk ) )

  return

def r8_erf_inverse ( y ):

#*****************************************************************************80
#
## r8_erf_inverse() inverts the error function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Y, the value of the error function.
#
#  Output:
#
#    real VALUE, the value such that r8_erf(VALUE) = Y.
#
  import numpy as np

  z = ( y + 1.0 ) / 2.0

  value = normal_01_cdf_inverse ( z )

  value = value / np.sqrt ( 2.0 )

  return value

def r8_erf_inverse_test ( ):

#*****************************************************************************80
#
## r8_erf_inverse_test() tests r8_erf_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_erf_inverse_test():' )
  print ( '  r8_erf_inverse inverts the error function.' )
  print ( '' )
  print ( '     FX              X    r8_erf_inverse(FX)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x1, fx = erf_values ( n_data )

    if ( n_data == 0 ):
      break

    x2 = r8_erf_inverse ( fx )

    print ( '  %12g  %24.16g  %24.16g' % ( fx, x1, x2 ) )

  return

def r8_erf ( x ):

#*****************************************************************************80
#
## r8_erf() evaluates the error function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    W J Cody,
#    Mathematics and Computer Science Division,
#    Argonne National Laboratory,
#    Argonne, Illinois, 60439.
#
#  Reference:
#
#    W J Cody,
#    "Rational Chebyshev approximations for the error function",
#    Mathematics of Computation, 
#    1969, pages 631-638.
#
#  Input:
#
#    real X, the argument of the error function.
#
#  Output:
#
#    real VALUE, the value of the error function.
#
  import numpy as np

  a = np.array ( ( \
    3.16112374387056560E+00, \
    1.13864154151050156E+02, \
    3.77485237685302021E+02, \
    3.20937758913846947E+03, \
    1.85777706184603153E-01 ))
  b = np.array ( ( \
    2.36012909523441209E+01, \
    2.44024637934444173E+02, \
    1.28261652607737228E+03, \
    2.84423683343917062E+03 ))
  c = np.array ( ( \
    5.64188496988670089E-01, \
    8.88314979438837594E+00, \
    6.61191906371416295E+01, \
    2.98635138197400131E+02, \
    8.81952221241769090E+02, \
    1.71204761263407058E+03, \
    2.05107837782607147E+03, \
    1.23033935479799725E+03, \
    2.15311535474403846E-08 ))
  d = np.array ( ( \
    1.57449261107098347E+01, \
    1.17693950891312499E+02, \
    5.37181101862009858E+02, \
    1.62138957456669019E+03, \
    3.29079923573345963E+03, \
    4.36261909014324716E+03, \
    3.43936767414372164E+03, \
    1.23033935480374942E+03 ))
  p = np.array ( ( \
    3.05326634961232344E-01, \
    3.60344899949804439E-01, \
    1.25781726111229246E-01, \
    1.60837851487422766E-02, \
    6.58749161529837803E-04, \
    1.63153871373020978E-02 ))
  q = np.array ( ( \
    2.56852019228982242E+00, \
    1.87295284992346047E+00, \
    5.27905102951428412E-01, \
    6.05183413124413191E-02, \
    2.33520497626869185E-03 ))
  sqrpi = 0.56418958354775628695E+00
  thresh = 0.46875E+00
  xbig = 26.543E+00
  xsmall = 1.11E-16

  xabs = abs ( x )
#
#  Evaluate ERF(X) for |X| <= 0.46875.
#
  if ( xabs <= thresh ):

    if ( xsmall < xabs ):
      xsq = xabs * xabs
    else:
      xsq = 0.0

    xnum = a[4] * xsq
    xden = xsq
    for i in range ( 0, 3 ):
      xnum = ( xnum + a[i] ) * xsq
      xden = ( xden + b[i] ) * xsq

    value = x * ( xnum + a[3] ) / ( xden + b[3] )
#
#  Evaluate ERFC(X) for 0.46875 <= |X| <= 4.0.
#
  elif ( xabs <= 4.0 ):

    xnum = c[8] * xabs
    xden = xabs
    for i in range ( 0, 7 ):
      xnum = ( xnum + c[i] ) * xabs
      xden = ( xden + d[i] ) * xabs

    value = ( xnum + c[7] ) / ( xden + d[7] )
    xsq = np.floor ( xabs * 16.0 ) / 16.0
    delt = ( xabs - xsq ) * ( xabs + xsq )
    value = np.exp ( - xsq * xsq ) * np.exp ( - delt ) * value

    value = ( 0.5 - value ) + 0.5

    if ( x < 0.0 ):
      value = -value
#
#  Evaluate ERFC(X) for 4.0 < |X|.
#
  else:

    if ( xbig <= xabs ):

      if ( 0.0 < x ):
        value = 1.0
      else:
        value = -1.0;

    else:

      xsq = 1.0 / ( xabs * xabs )

      xnum = p[5] * xsq
      xden = xsq
      for i in range ( 0, 4 ):
        xnum = ( xnum + p[i] ) * xsq
        xden = ( xden + q[i] ) * xsq

      value = xsq * ( xnum + p[4] ) / ( xden + q[4] )
      value = ( sqrpi -  value ) / xabs
      xsq = np.floor ( xabs * 16.0 ) / 16.0
      delt = ( xabs - xsq ) * ( xabs + xsq )
      value = np.exp ( - xsq * xsq ) * np.exp ( - delt ) * value

      value = ( 0.5 - value ) + 0.5

      if ( x < 0.0 ):
        value = -value;

  return value

def r8_erf_test ( ):

#*****************************************************************************80
#
## r8_erf_test() tests r8_erf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_erf_test():' )
  print ( '  r8_erf() evaluates the error function.' )
  print ( '' )
  print ( '      X            ERF(X)    r8_erf(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = erf_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_erf ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )

  return

def r8_factorial_log ( n ):

#*****************************************************************************80
#
## r8_factorial_log() computes the natural logarithm of the factorial N!
#
#  Discussion:
#
#    LOG ( FACTORIAL ( N ) )
#      = LOG ( product ( 1 <= I <= N ) I )
#      = sum ( ( 1 <= I <= N ) LOG ( I ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the argument of the factorial function.
#    If N is less than 1, VALUE is returned as 0.
#
#  Output:
#
#    real VALUE, the logarithm of the factorial of N.
#
  from scipy.special import gammaln

  value = gammaln ( float ( n + 1 ) )

  return value

def r8_factorial_log_test ( ):

#*****************************************************************************80
#
## r8_factorial_log_test() tests r8_factorial_log().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_factorial_log_test():' )
  print ( '  r8_factorial_log() evaluates the factorial log function.' )
  print ( '' )
  print ( '      N                     Exact' ),
  print ( '                  Computed' )

  n_data = 0

  while ( True ):

    n_data, n, f1 = r8_factorial_log_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_factorial_log ( n )

    print ( '  %4d  %24.16g  %24.16g' % ( n, f1, f2 ) )

  return

def r8_factorial_log_values ( n_data ):

#*****************************************************************************80
#
## r8_factorial_log_values() returns values of log(n!).
#
#  Discussion:
#
#    The function log(n!) can be written as
#
#     log(n!) = sum ( 1 <= i <= n ) log ( i )
#
#    In Mathematica, the function can be evaluated by:
#
#      Log[n!]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 27

  f_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.0000000000000000E+00, \
     0.6931471805599453E+00, \
     0.1791759469228055E+01, \
     0.3178053830347946E+01, \
     0.4787491742782046E+01, \
     0.6579251212010101E+01, \
     0.8525161361065414E+01, \
     0.1060460290274525E+02, \
     0.1280182748008147E+02, \
     0.1510441257307552E+02, \
     0.1750230784587389E+02, \
     0.1998721449566189E+02, \
     0.2255216385312342E+02, \
     0.2519122118273868E+02, \
     0.2789927138384089E+02, \
     0.3067186010608067E+02, \
     0.3350507345013689E+02, \
     0.3639544520803305E+02, \
     0.3933988418719949E+02, \
     0.4233561646075349E+02, \
     0.5800360522298052E+02, \
     0.1484777669517730E+03, \
     0.3637393755555635E+03, \
     0.6050201058494237E+03, \
     0.2611330458460156E+04, \
     0.5912128178488163E+04 ))

  n_vec = np.array ( ( \
       0, \
       1, \
       2, \
       3, \
       4, \
       5, \
       6, \
       7, \
       8, \
       9, \
      10, \
      11, \
      12, \
      13, \
      14, \
      15, \
      16, \
      17, \
      18, \
      19, \
      20, \
      25, \
      50, \
     100, \
     150, \
     500, \
    1000 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    f = 0
  else:
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, f

def r8_factorial_log_values_test ( ):

#*****************************************************************************80
#
## r8_factorial_log_values_test() tests r8_factorial_log_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_factorial_log_values_test():' )
  print ( '  r8_factorial_log_values() returns values of the log factorial function.' )
  print ( '' )
  print ( '          N          r8_factorial_log(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = r8_factorial_log_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8d  %14.6g' % ( n, fn ) )

  return

def r8_factorial ( n ):

#*****************************************************************************80
#
## r8_factorial() returns N factorial.
#
#  Discussion:
#
#    factorial ( N ) = Product ( 1 <= I <= N ) I
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the argument of the function.
#    0 <= N.
#
#  Output:
#
#    real VALUE, the factorial of N.
#
  if ( n < 0 ):
    print ( '' )
    print ( 'r8_factorial(): Fatal error!' )
    print ( '  N < 0.' )
    raise Exception ( 'r8_factorial(): Fatal error!' )

  value = 1.0

  for i in range ( 2, n + 1 ):
    value = value * i

  return value

def r8_factorial_test ( ):

#*****************************************************************************80
#
## r8_factorial_test() tests r8_factorial().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_factorial_test():' )
  print ( '  r8_factorial() evaluates the factorial function.' )
  print ( '' )
  print ( '      N                     Exact' ),
  print ( '                  Computed' )

  n_data = 0

  while ( True ):

    n_data, n, f1 = r8_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_factorial ( n )

    print ( '  %4d  %24.16g  %24.16g' % ( n, f1, f2 ) )

  return

def r8_factorial_values ( n_data ):

#*****************************************************************************80
#
## r8_factorial_values() returns values of the real factorial function.
#
#  Discussion:
#
#    0! = 1
#    I! = Product ( 1 <= J <= I ) J
#
#    Although the factorial is an integer valued function, it quickly
#    becomes too large for an integer to hold.  This routine still accepts
#    an integer as the input argument, but returns the function value
#    as a real number.
#
#    In Mathematica, the function can be evaluated by:
#
#      n!
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the function.
#
#    real FN, the value of the function.
#
  import numpy as np

  n_max = 25

  fn_vec = np.array ( [ \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.2000000000000000E+01, \
     0.6000000000000000E+01, \
     0.2400000000000000E+02, \
     0.1200000000000000E+03, \
     0.7200000000000000E+03, \
     0.5040000000000000E+04, \
     0.4032000000000000E+05, \
     0.3628800000000000E+06, \
     0.3628800000000000E+07, \
     0.3991680000000000E+08, \
     0.4790016000000000E+09, \
     0.6227020800000000E+10, \
     0.8717829120000000E+11, \
     0.1307674368000000E+13, \
     0.2092278988800000E+14, \
     0.3556874280960000E+15, \
     0.6402373705728000E+16, \
     0.1216451004088320E+18, \
     0.2432902008176640E+19, \
     0.1551121004333099E+26, \
     0.3041409320171338E+65, \
     0.9332621544394415E+158, \
     0.5713383956445855E+263 ] )

  n_vec = np.array ( [ \
       0, \
       1, \
       2, \
       3, \
       4, \
       5, \
       6, \
       7, \
       8, \
       9, \
      10, \
      11, \
      12, \
      13, \
      14, \
      15, \
      16, \
      17, \
      18, \
      19, \
      20, \
      25, \
      50, \
     100, \
     150 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    fn = 0
  else:
    n = n_vec[n_data]
    fn = fn_vec[n_data]
    n_data = n_data + 1

  return n_data, n, fn

def r8_factorial_values_test ( ):

#*****************************************************************************80
#
## r8_factorial_values_test() tests r8_factorial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_factorial_values_test():' )
  print ( '  r8_factorial_values() returns values of the real factorial function.' )
  print ( '' )
  print ( '          N          r8_factorial(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = r8_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8d  %14.6g' % ( n, fn ) )

  return

def r8_hyper_2f1 ( a, b, c, x ):

#*****************************************************************************80
#
## r8_hyper_2f1() evaluates the hypergeometric function F(A,B,C,X).
#
#  Discussion:
#
#    A minor bug was corrected.  The HW variable, used in several places as
#    the "old" value of a quantity being iteratively improved, was not
#    being initialized.  JVB, 11 February 2008.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    Original FORTRAN77 version by Shanjie Zhang, Jianming Jin.
#    This version by John Burkardt.
#
#    The F77 original version of this routine is copyrighted by
#    Shanjie Zhang and Jianming Jin.  However, they give permission to
#    incorporate this routine into a user program provided that the copyright
#    is acknowledged.
#
#  Reference:
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45
#
#  Input:
#
#    real A, B, C, X, the arguments of the function.
#    C must not be equal to a nonpositive integer.
#    X < 1.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np
  from scipy.special import gamma

  el = 0.5772156649015329

  l0 = ( c == int ( c ) ) and ( c < 0.0 )
  l1 = ( 1.0 - x < 1.0E-15 ) and ( c - a - b <= 0.0 )
  l2 = ( a == int ( a ) ) and ( a < 0.0 )
  l3 = ( b == int ( b ) ) and ( b < 0.0 )
  l4 = ( c - a == int ( c - a ) ) and ( c - a <= 0.0 )
  l5 = ( c - b == int ( c - b ) ) and ( c - b <= 0.0 )

  if ( l0 ):
    print ( '' )
    print ( 'r8_hyper_2f1(): Fatal error!' )
    print ( '  The hypergeometric series is divergent.' )
    print ( '  C is integral and negative.' )
    print ( '  C = %f' % ( c ) )
    raise Exception ( 'r8_hyper_2f1(): Fatal error!' )

  if ( l1 ):
    print ( '' )
    print ( 'r8_hyper_2f1(): Fatal error!' )
    print ( '  The hypergeometric series is divergent.' )
    print ( '  1 = X < 0, C - A - B <= 0.' )
    print ( '  A = %f' % ( a ) )
    print ( '  B = %f' % ( b ) )
    print ( '  C = %f' % ( c ) )
    print ( '  X = %f' % ( x ) )
    raise Exception ( 'r8_hyper_2f1(): Fatal error!' )

  if ( 0.95 < x ):
    eps = 1.0E-08
  else:
    eps = 1.0E-15

  if ( x == 0.0 or a == 0.0 or b == 0.0 ):

    value = 1.0
    return value

  elif ( 1.0 - x == eps and 0.0 < c - a - b ):

    gc = gamma ( c )
    gcab = gamma ( c - a - b )
    gca = gamma ( c - a )
    gcb = gamma ( c - b )
    value = gc * gcab / ( gca * gcb )
    return value

  elif ( 1.0 + x <= eps and abs ( c - a + b - 1.0 ) <= eps ):

    g0 = np.sqrt ( np.pi ) * 2.0 ** ( - a )
    g1 = gamma ( c )
    g2 = gamma ( 1.0 + a / 2.0 - b )
    g3 = gamma ( 0.5 + 0.5 * a )
    value = g0 * g1 / ( g2 * g3 )
    return value

  elif ( l2 or l3 ):

    if ( l2 ):
      nm = int ( abs ( a ) )

    if ( l3 ):
      nm = int ( abs ( b ) )

    value = 1.0
    r = 1.0

    for k in range ( 1, nm + 1 ):
      r = r * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
        / ( float ( k ) * ( c + float ( k ) - 1.0 ) ) * x
      value = value + r

    return value

  elif ( l4 or l5 ):

    if ( l4 ):
      nm = int ( abs ( c - a ) )
 
    if ( l5 ):
      nm = int ( abs ( c - b ) )

    value = 1.0
    r  = 1.0
    for k in range ( 1, nm + 1 ):
      r = r * ( c - a + float ( k ) - 1.0 ) * ( c - b + float ( k ) - 1.0 ) \
        / ( float ( k ) * ( c + float ( k ) - 1.0 ) ) * x
      value = value + r
    value = ( 1.0 - x ) ** ( c - a - b ) * hf
    return value

  aa = a
  bb = b
  x1 = x

  if ( x < 0.0 ):
    x = x / ( x - 1.0 )
    if ( a < c and b < a and 0.0 < b ):
      a = bb
      b = aa
    b = c - b

  if ( 0.75 <= x ):

    gm = 0.0

    if ( abs ( c - a - b - int ( c - a - b ) ) < 1.0E-15 ):

      m = int ( c - a - b )
      ga = gamma ( a )
      gb = gamma ( b )
      gc = gamma ( c )
      gam = gamma ( a + float ( m ) )
      gbm = gamma ( b + float ( m ) )

      pa = r8_psi ( a )
      pb = r8_psi ( b )

      if ( m != 0 ):
        gm = 1.0

      for j in range ( 1, abs ( m ) ):
        gm = gm * float ( j )

      rm = 1.0
      for j in range ( 1, abs ( m ) + 1 ):
        rm = rm * float ( j )
 
      f0 = 1.0
      r0 = 1.0
      r1 = 1.0
      sp0 = 0.0
      sp = 0.0

      if ( 0 <= m ):

        c0 = gm * gc / ( gam * gbm )
        c1 = - gc * ( x - 1.0 ) ** m / ( ga * gb * rm )

        for k in range ( 1, m ):
          r0 = r0 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
            / float ( k * ( k - m ) ) * ( 1.0 - x )
          f0 = f0 + r0
 
        for k in range ( 1, m + 1 ):
          sp0 = sp0 + 1.0 / ( a + float ( k ) - 1.0 ) \
            + 1.0 / ( b + float ( k ) - 1.0 ) - 1.0 / float ( k )

        f1 = pa + pb + sp0 + 2.0 * el + np.log ( 1.0 - x )
        hw = f1

        for k in range ( 1, 251 ):

          sp = sp + ( 1.0 - a ) / ( float ( k ) * ( a + float ( k ) - 1.0 ) ) \
            + ( 1.0 - b ) / ( float ( k ) * ( b + float ( k ) - 1.0 ) )

          sm = 0.0
          for j in range ( 1, m + 1 ):
            sm = sm + ( 1.0 - a ) \
              / ( float ( j + k ) * ( a + float ( j + k ) - 1.0 ) ) \
              + 1.0 / ( b + float ( j + k ) - 1.0 )

          rp = pa + pb + 2.0 * el + sp + sm + np.log ( 1.0 - x )

          r1 = r1 * ( a + m + float ( k ) - 1.0 ) * ( b + m + float ( k ) - 1.0 ) \
            / ( float ( k ) * float ( m + k ) ) * ( 1.0 - x )

          f1 = f1 + r1 * rp

          if ( abs ( f1 - hw ) < abs ( f1 ) * eps ):
            break
 
          hw = f1

        value = f0 * c0 + f1 * c1

      elif ( m < 0 ):

        m = - m
        c0 = gm * gc / ( ga * gb * ( 1.0 - x ) ** m )
        c1 = - ( - 1 ) ** m * gc / ( gam * gbm * rm )

        for k in range ( 1, m ):
          r0 = r0 * ( a - float ( m ) + float ( k ) - 1.0 ) \
            * ( b - float ( m ) + float ( k ) - 1.0 ) \
            / ( float ( k ) * float ( k - m ) ) * ( 1.0 - x )
          f0 = f0 + r0

        for k in range ( 1, m + 1 ):
          sp0 = sp0 + 1.0 / float ( k )

        f1 = pa + pb - sp0 + 2.0 * el + np.log ( 1.0 - x )
        hw = f1

        for k in range ( 1, 251 ):

          sp = sp + ( 1.0 - a ) \
            / ( float ( k ) * ( a + float ( k ) - 1.0 ) ) \
            + ( 1.0 - b ) / ( float ( k ) * ( b + float ( k ) - 1.0 ) )

          sm = 0.0
          for j in range ( 1, m + 1 ):
            sm = sm + 1.0 / float ( j + k )

          rp = pa + pb + 2.0 * el + sp - sm + np.log ( 1.0 - x )

          r1 = r1 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
            / float ( k * ( m + k ) ) * ( 1.0 - x )

          f1 = f1 + r1 * rp

          if ( abs ( f1 - hw ) < abs ( f1 ) * eps ):
            break

          hw = f1

        value = f0 * c0 + f1 * c1

    else:

      ga = gamma ( a )
      gb = gamma ( b )
      gc = gamma ( c )
      gca = gamma ( c - a )
      gcb = gamma ( c - b )
      gcab = gamma ( c - a - b )
      gabc = gamma ( a + b - c )
      c0 = gc * gcab / ( gca * gcb )
      c1 = gc * gabc / ( ga * gb ) * ( 1.0 - x ) ** ( c - a - b )
      value = 0.0
      hw = value
      r0 = c0
      r1 = c1

      for k in range ( 1, 251 ):

        r0 = r0 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
          / ( float ( k ) * ( a + b - c + float ( k ) ) ) * ( 1.0 - x )

        r1 = r1 * ( c - a + float ( k ) - 1.0 ) \
          * ( c - b + float ( k ) - 1.0 ) \
          / ( float ( k ) * ( c - a - b + float ( k ) ) ) * ( 1.0 - x )

        value = value + r0 + r1

        if ( abs ( value - hw ) < abs ( value ) * eps ):
          break

        hw = value

      value = value + c0 + c1

  else:

    a0 = 1.0

    if ( a < c and c < 2.0 * a and b < c and c < 2.0 * b ):

      a0 = ( 1.0 - x ) ** ( c - a - b )
      a = c - a
      b = c - b

    value = 1.0
    hw = value
    r = 1.0

    for k in range ( 1, 251 ):

      r = r * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
        / ( k * ( c + float ( k ) - 1.0 ) ) * x

      value = value + r

      if ( abs ( value - hw ) <= abs ( value ) * eps ):
        break

      hw = value

    value = a0 * value

  if ( x1 < 0.0 ):
    x = x1
    c0 = 1.0 / ( 1.0 - x ) ** aa
    value = c0 * value

  if ( 120 < k ):
    print ( '' )
    print ( 'r8_hyper_2f1 - Warning!' )
    print ( '  A large number of iterations were needed.' )
    print ( '  The accuracy of the results should be checked.' )

  return value

def r8_hyper_2f1_test ( ):

#*****************************************************************************80
#
## r8_hyper_2f1_test() tests r8_hyper_2f1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8_hyper_2f1_test():' )
  print ( '  r8_hyper_2f1() evaluates the hypergeometric 2f1 function.' )
  print ( '' )
  print ( '      A       B       C       X      ' ),
  print ( ' 2f1                       2f1                     DIFF' )
  print ( '                                     ' ),
  print ( '(tabulated)               (computed)' )
  print ( '' )

  n_data = 0

  while ( True ):

    [ n_data, a, b, c, x, fx1 ] = hyper_2f1_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_hyper_2f1 ( a, b, c, x )
 
    diff = abs ( fx1 - fx2 )
    print ( '  %6g  %6g  %6g  %6g  %24g  %24g  %10g' \
      % ( a, b, c, x, fx1, fx2, diff ) )

  return

def r8_mop ( i ):

#*****************************************************************************80
#
## r8_mop() returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the power of -1.
#
#  Output:
#
#    real VALUE, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( rng ):

#*****************************************************************************80
#
## r8_mop_test() tests r8_mop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r8_mop_test():' )
  print ( '  r8_mop evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  r8_mop(I4)' )
  print ( '' )

  for test in range ( 0, 10 ):
    i4 = rng.integers ( low = -100, high = +100, endpoint = True )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )

  return

def r8_nint ( x ):

#*****************************************************************************80
#
## r8_nint() returns the nearest integer to an R8.
#
#  Example:
#
#        X        r8_nint
#
#      1.3         1
#      1.4         1
#      1.5         1 or 2
#      1.6         2
#      0.0         0
#     -0.7        -1
#     -1.1        -1
#     -1.6        -2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the value.
#
#  Output:
#
#    integer VALUE, the nearest integer to X.
#
  if ( x < 0.0 ):
    s = -1
  else:
    s = 1

  value = s * round ( abs ( x ) + 0.5 )

  return value

def r8_nint_test ( rng ):

#*****************************************************************************80
#
## r8_nint_test() tests r8_nint()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  test_num = 10

  print ( '' )
  print ( 'r8_nint_test():' )
  print ( '  r8_nint() produces the nearest integer.' )
  print ( '' )
  print ( '      X      r8_nint(X)' )
  print ( '' )

  b = -10.0
  c = +10.0

  for test  in range ( 0, test_num ):
    x = b + ( c - b ) * rng.random ( )
    print ( '  %10f  %6d' % ( x, r8_nint ( x ) ) )

  return

def r8poly_degree ( m, a ):

#*****************************************************************************80
#
## r8poly_degree() returns the degree of a polynomial.
#
#  Discussion:
#
#    The degree of a polynomial is the index of the highest power
#    of X with a nonzero coefficient.
#
#    The degree of a constant polynomial is 0.  The degree of the
#    zero polynomial is debatable, but this routine returns the
#    degree as 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the nominal degree of A.
#
#    real A(M+1), the coefficients of the polynomials.
#
#  Output:
#
#    integer VALUE, the degree of A.
#
  value = m

  while ( 0 < value ):
    if ( a[value] != 0.0 ):
      break
    value = value - 1

  return value

def r8poly_degree_test ( ):

#*****************************************************************************80
#
## r8poly_degree_test() tests r8poly_degree().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  c1 = np.array ( [ 1.0, 2.0, 3.0, 4.0 ] )
  c2 = np.array ( [ 1.0, 2.0, 3.0, 0.0 ] )
  c3 = np.array ( [ 1.0, 2.0, 0.0, 4.0 ] )
  c4 = np.array ( [ 1.0, 0.0, 0.0, 0.0 ] )
  c5 = np.array ( [ 0.0, 0.0, 0.0, 0.0 ] )

  print ( '' )
  print ( 'r8poly_degree_test():' )
  print ( '  r8poly_degree() determines the degree of an R8POLY.' )

  m = 3

  r8poly_print ( m, c1, '  The R8POLY:' )
  d = r8poly_degree ( m, c1 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  r8poly_print ( m, c2, '  The R8POLY:' )
  d = r8poly_degree ( m, c2 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  r8poly_print ( m, c3, '  The R8POLY:' )
  d = r8poly_degree ( m, c3 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  r8poly_print ( m, c4, '  The R8POLY:' )
  d = r8poly_degree ( m, c4 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  r8poly_print ( m, c5, '  The R8POLY:' )
  d = r8poly_degree ( m, c5 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  return

def r8poly_print ( m, a, title ):

#*****************************************************************************80
#
## r8poly_print() prints out a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the nominal degree of the polynomial.
#
#    real A[0:M], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
  print ( '' )

  if ( a[m] < 0.0 ):
    plus_minus = '-'
  else:
    plus_minus = ' '

  mag = abs ( a[m] )

  if ( 2 <= m ):
    print ( '  p(x) = %c %g * x^%d' % ( plus_minus, mag, m ) )
  elif ( m == 1 ):
    print ( '  p(x) = %c %g * x' % ( plus_minus, mag ) )
  elif ( m == 0 ):
    print ( '  p(x) = %c %g' % ( plus_minus, mag ) )

  for i in range ( m - 1, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( 2 <= i ):
        print ( '         %c %g * x^%d' % ( plus_minus, mag, i ) )
      elif ( i == 1 ):
        print ( '         %c %g * x' % ( plus_minus, mag ) )
      elif ( i == 0 ):
        print ( '         %c %g' % ( plus_minus, mag ) )

def r8poly_print_test ( ):

#*****************************************************************************80
#
## r8poly_print_test() tests r8poly_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8poly_print_test():' )
  print ( '  r8poly_print() prints an R8POLY.' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )

  r8poly_print ( m, c, '  The R8POLY:' )

  return

def r8poly_value_horner ( m, c, x ):

#*****************************************************************************80
#
## r8poly_value_horner() evaluates a polynomial using Horner's method.
#
#  Discussion:
#
#    The polynomial 
#
#      p(x) = c0 + c1 * x + c2 * x^2 + ... + cm * x^m
#
#    is to be evaluated at the value X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the degree.
#
#    real C(0:M), the polynomial coefficients.  
#    C(I) is the coefficient of X^I.
#
#    real X, the evaluation point.
#
#  Output:
#
#    real VALUE, the polynomial value.
#
  value = c[m]
  for i in range ( m - 1, -1, -1 ):
    value = value * x + c[i]

  return value

def r8poly_value_horner_test ( ):

#*****************************************************************************80
#
## r8poly_value_horner_test() tests r8poly_value_horner().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 4
  n = 16
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )

  print ( '' )
  print ( 'r8poly_value_horner_test():' )
  print ( '  r8poly_value_horner() evaluates a polynomial at a point' )
  print ( '  using Horner\'s method.' )

  r8poly_print ( m, c, '  The polynomial coefficients:' )

  x_lo = 0.0
  x_hi = 5.0
  x = np.linspace ( x_lo, x_hi, n )

  print ( '' )
  print ( '   I    X    P(X)' )
  print ( '' )

  for i in range ( 0, n ):
    p = r8poly_value_horner ( m, c, x[i] )
    print ( '  %2d  %8.4f  %14.6g' % ( i, x[i], p ) )

  return

def r8_psi ( x ):

#*****************************************************************************80
#
## r8_psi() evaluates the function Psi(X).
#
#  Discussion:
#
#    This routine evaluates the logarithmic derivative of the
#    Gamma function,
#
#      PSI(X) = d/dX ( GAMMA(X) ) / GAMMA(X)
#             = d/dX LN ( GAMMA(X) )
#
#    for real X, where either
#
#      - XMAX1 < X < - XMIN, and X is not a negative integer,
#
#    or
#
#      XMIN < X.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    Original FORTRAN77 version by William Cody.
#    This version by John Burkardt.
#
#  Reference:
#
#    William Cody, Anthony Strecok, Henry Thacher,
#    Chebyshev Approximations for the Psi Function,
#    Mathematics of Computation,
#    Volume 27, Number 121, January 1973, pages 123-127.
#
#  Input:
#
#    real X, the argument of the function.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np

  p1 = np.array ( ( \
   4.5104681245762934160E-03, \
   5.4932855833000385356, \
   3.7646693175929276856E+02, \
   7.9525490849151998065E+03, \
   7.1451595818951933210E+04, \
   3.0655976301987365674E+05, \
   6.3606997788964458797E+05, \
   5.8041312783537569993E+05, \
   1.6585695029761022321E+05 ))

  p2 = np.array ( ( \
  -2.7103228277757834192, \
  -1.5166271776896121383E+01, \
  -1.9784554148719218667E+01, \
  -8.8100958828312219821, \
  -1.4479614616899842986, \
  -7.3689600332394549911E-02, \
  -6.5135387732718171306E-21 ))

  piov4 = 0.78539816339744830962

  q1 = np.array ( ( \
   9.6141654774222358525E+01, \
   2.6287715790581193330E+03, \
   2.9862497022250277920E+04, \
   1.6206566091533671639E+05, \
   4.3487880712768329037E+05, \
   5.4256384537269993733E+05, \
   2.4242185002017985252E+05, \
   6.4155223783576225996E-08 ))

  q2 = np.array ( ( \
   4.4992760373789365846E+01, \
   2.0240955312679931159E+02, \
   2.4736979003315290057E+02, \
   1.0742543875702278326E+02, \
   1.7463965060678569906E+01, \
   8.8427520398873480342E-01 ))

  x01 = 187.0
  x01d = 128.0
  x02 = 6.9464496836234126266E-04
  xinf = 1.70E+38
  xlarge = 2.04E+15
  xmax1 = 3.60E+16
  xmin1 = 5.89E-39
  xsmall = 2.05E-09

  w = abs ( x )
  aug = 0.0
#
#  Check for valid arguments, then branch to appropriate algorithm.
#
  if ( xmax1 <= - x or w < xmin1 ):

    if ( 0.0 < x ):
      value = - xinf
    else:
      value = xinf;

    return value

  if ( x < 0.5 ):
#
#  X < 0.5, use reflection formula: psi(1-x) = psi(x) + pi * cot(pi*x)
#  Use 1/X for PI*COTAN(PI*X)  when  XMIN1 < |X| <= XSMALL.
#
    if ( w <= xsmall ):

      aug = - 1.0 / x
#
#  Argument reduction for cotangent.
#
    else:

      if ( x < 0.0 ):
        sgn = piov4
      else:
        sgn = - piov4

      w = w - int ( w )
      nq = int ( w * 4.0 )
      w = 4.0 * ( w - float ( nq ) * 0.25 )
#
#  W is now related to the fractional part of 4.0 * X.
#  Adjust argument to correspond to values in the first
#  quadrant and determine the sign.
#
      n = ( nq // 2 )

      if ( n + n != nq ):
        w = 1.0 - w

      z = piov4 * w

      if ( ( n % 2 ) != 0 ):
        sgn = - sgn
#
#  Determine the final value for  -pi * cotan(pi*x).
#
      n = ( ( nq + 1 ) // 2 )
      if ( ( n % 2 ) == 0 ):
#
#  Check for singularity.
#
        if ( z == 0.0 ):

          if ( 0.0 < x ):
            value = - xinf
          else:
            value = xinf

          return value

        aug = sgn * ( 4.0 / np.tan ( z ) )

      else:

        aug = sgn * ( 4.0 * np.tan ( z ) )

    x = 1.0 - x
#
#  0.5 <= X <= 3.0.
#
  if ( x <= 3.0 ):

    den = x
    upper = p1[0] * x
    for i in range ( 0, 7 ):
      den = ( den + q1[i] ) * x
      upper = ( upper + p1[i+1] ) * x

    den = ( upper + p1[8] ) / ( den + q1[7] )
    x = ( x - x01 / x01d ) - x02
    value = den * x + aug
    return value
#
#  3.0 < X.
#
  if ( x < xlarge ):
    w = 1.0 / ( x * x )
    den = w
    upper = p2[0] * w
    for i in range ( 0, 5 ):
      den = ( den + q2[i] ) * w
      upper = ( upper + p2[i+1] ) * w
    aug = ( upper + p2[6] ) / ( den + q2[5] ) - 0.5 / x + aug

  value = aug + np.log ( x )

  return value

def r8_psi_test ( ):

#*****************************************************************************80
#
## r8_psi_test() tests r8_psi().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_psi_test():' )
  print ( '  r8_psi() evaluates the Psi() function.' )
  print ( '' )
  print ( '      X            PSI(X)    r8_psi(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_psi ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )

  return

def r8vec_linspace ( n, a, b ):

#*****************************************************************************80
#
## r8vec_linspace() creates a column vector of linearly spaced values.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    While MATLAB has the built in command 
#
#      x = linspace ( a, b, n )
#
#    that command has the distinct disadvantage of returning a ROW vector.
#
#    4 points evenly spaced between 0 and 12 will yield 0, 4, 8, 12.
#
#    In other words, the interval is divided into N-1 even subintervals,
#    and the endpoints of intervals are used as the points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A, B, the first and last entries.
#
#  Output:
#
#    real X(N), a vector of linearly spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):
     x[i] = ( ( n - 1 - i ) * a \
            + (         i ) * b ) \
            / ( n - 1     )
 
  return x

def r8vec_linspace_test ( ):

#*****************************************************************************80
#
## r8vec_linspace_test() tests r8vec_linspace().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_linspace_test():' )
  print ( '  r8vec_linspace() returns evenly spaced values between A and B.' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_linspace ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The linspace vector:' )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def sigma ( n ):

#*****************************************************************************80
#
## sigma() returns the value of SIGMA(N), the divisor sum.
#
#  Definition:
#
#    SIGMA(N) is the sum of the distinct divisors of N, including 1 and N.
#
#  First values:
#
#     N  SIGMA(N)
#
#     1    1
#     2    3
#     3    4
#     4    7
#     5    6
#     6   12
#     7    8
#     8   15
#     9   13
#    10   18
#    11   12
#    12   28
#    13   14
#    14   24
#    15   24
#    16   31
#    17   18
#    18   39
#    19   20
#    20   42
#
#  Formula:
#
#    SIGMA(U*V) = SIGMA(U) * SIGMA(V) if U and V are relatively prime.
#
#    SIGMA(P^K) = ( P^(K+1) - 1 ) / ( P - 1 ) if P is prime.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the value to be analyzed.
#
#  Output:
#
#    integer VALUE, the value of SIGMA(N).  If N is less than
#    or equal to 0, VALUE will be returned as 0.  If there is not
#    enough room for factoring N, VALUE is returned as -1.
#
  maxfactor = 20

  if ( n <= 0 ):
    value = 0
    return value

  if ( n == 1 ):
    value = 1
    return value
#
#  Factor N.
#
  nfactor, factor, power, nleft = i4_factor ( n )

  if ( nleft != 1 ):
    print ( '' )
    print ( 'sigma(): Fatal error!' )
    print ( '  Not enough factorization space.' )

  value = 1
  for i in range ( 0, nfactor ):
    value = ( value * ( factor[i] ** ( power[i] + 1 ) - 1 ) ) \
      / ( factor[i] - 1 )

  return value

def sigma_test ( ):

#*****************************************************************************80
#
## sigma_test() tests sigma().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sigma_test():' )
  print ( '  sigma() computes the SIGMA function.' )
  print ( '' )
  print ( '         N      Exact         SIGMA(N)' )

  n_data = 0

  while ( True ):

    n_data, n, c1 = sigma_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = sigma ( n )

    print ( '  %8d  %12d  %12d' % ( n, c1, c2 ) )

  return

def sigma_values ( n_data ):

#*****************************************************************************80
#
## sigma_values() returns some values of the Sigma function.
#
#  Discussion:
#
#    SIGMA(N) is the sum of the distinct divisors of N, including 1 and N.
#
#    In Mathematica, the function can be evaluated by:
#
#      DivisorSigma[1,n]
#
#  First values:
#
#     N  SIGMA(N)
#
#     1    1
#     2    3
#     3    4
#     4    7
#     5    6
#     6   12
#     7    8
#     8   15
#     9   13
#    10   18
#    11   12
#    12   28
#    13   14
#    14   24
#    15   24
#    16   31
#    17   18
#    18   39
#    19   20
#    20   42
#
#  Formula:
#
#    SIGMA(U*V) = SIGMA(U) * SIGMA(V) if U and V are relatively prime.
#
#    SIGMA(P^K) = ( P^(K+1) - 1 ) / ( P - 1 ) if P is prime.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the Sigma function.
#
#    integer C, the value of the Sigma function.
#
  import numpy as np

  n_max = 20

  c_vec = np.array ( ( \
     1,    3,    4,    7,    6,   12,    8,   15,   13,   18, \
    72,  128,  255,  176,  576, 1170,  618,  984, 2232, 2340 ))

  n_vec = np.array ( ( \
      1,   2,   3,   4,   5,   6,   7,   8,   9,   10, \
     30, 127, 128, 129, 210, 360, 617, 815, 816, 1000 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def sigma_values_test ( ):

#*****************************************************************************80
#
## sigma_values_test() tests sigma_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sigma_values_test():' )
  print ( '  sigma_values() stores values of the SIGMA function.' )
  print ( '' )
  print ( '             N    SIGMA(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = sigma_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12d' % ( n, c ) )

  return

def simplex_num ( m, n ):

#*****************************************************************************80
#
## simplex_num() evaluates the N-th Simplex number in M dimensions.
#
#  Discussion:
#
#     N\M: 1    2    3    4    5
#    --   --   --   --   --   --
#     0    0    0    0    0    0
#     1    1    1    1    1    1
#     2    2    3    4    5    6
#     3    3    6   10   15   21
#     4    4   10   20   35   56
#     5    5   15   35   70  126
#     6    6   21   56  126  252
#     7    7   28   84  210  462
#     8    8   36  120  330  792
#     9    9   45  165  495 1287
#    10   10   55  220  715 2002
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the index of the number.
#
#  Output:
#
#    integer VALUE, the desired value.
#
  value = 1
  for i in range ( 1, m + 1 ):
    value = ( value * ( n + i - 1 ) ) / i

  return value

def simplex_num_test ( ):

#*****************************************************************************80
#
## simplex_num_test() tests simplex_num().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'simplex_num_test():' )
  print ( '  simplex_num() computes the N-th simplex number' )
  print ( '  in M dimensions.' )
  print ( '' )
  print ( '      M:  0      1      2      3      4      5' )
  print ( '   N' )
 
  for n in range ( 1, 11 ):
    print ( '  %2d' % ( n ) ),
    for m in range ( 0, 6 ):
      value = simplex_num ( m, n )
      print ( '  %4d' % ( value ) ),
    print ( '' )

  return

def sin_power_int ( a, b, n ):

#*****************************************************************************80
#
## sin_power_int() evaluates the sine power integral.
#
#  Discussion:
#
#    The function is defined by
#
#      sin_power_int(A,B,N) = Integral ( A <= T <= B ) ( sin ( t ))^n dt
#
#    The algorithm uses the following fact:
#
#      Integral sin^n ( t ) = (1/n) * (
#        sin^(n-1)(t) * cos(t) + ( n-1 ) * Integral sin^(n-2) ( t ) dt )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the limits of integration.
#
#    integer N, the power of the sine function.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'sin_power_int(): Fatal error!' )
    print ( '  Power N < 0.' )
    raise Exception ( 'sin_power_int(): Fatal error!' )

  sa = np.sin ( a );
  sb = np.sin ( b );
  ca = np.cos ( a );
  cb = np.cos ( b );

  if ( ( n % 2 ) == 0 ):
    value = b - a
    mlo = 2
  else:
    value = ca - cb
    mlo = 3

  for m in range ( mlo, n + 1, 2 ):
    value = ( ( m - 1 ) * value \
            + sa ** ( m - 1 ) * ca \
            - sb ** ( m - 1 ) * cb ) / float ( m )

  return value

def sin_power_int_test ( ):

#*****************************************************************************80
#
## sin_power_int_test() tests sin_power_int().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sin_power_int_test():' )
  print ( '  sin_power_int() returns values of' )
  print ( '  the integral of SIN(X)^N from A to B.' )
  print ( '' )
  print ( '      A         B          N      Exact           Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, n, fx = sin_power_int_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = sin_power_int ( a, b, n )

    print ( '  %8f  %8f  %6d  %14e  %14e' % ( a, b, n, fx, fx2 ) )

  return

def sin_power_int_values ( n_data ):

#*****************************************************************************80
#
## sin_power_int_values() returns some values of the sine power integral.
#
#  Discussion:
#
#    The function has the form
#
#      sin_power_int(A,B,N) = Integral ( A <= T <= B ) ( sin(T) )^N dt
#
#    In Mathematica, the function can be evaluated by:
#
#      Integrate [ ( Sin[x] )^n, { x, a, b } ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real A, B, the limits of integration.
#
#    integer N, the power.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 10

  a_vec = np.array ( ( \
      0.10E+02, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.00E+00, \
      0.10E+01, \
      0.00E+00, \
      0.00E+00 ))

  b_vec = np.array ( ( \
      0.20E+02, \
      0.10E+01, \
      0.10E+01, \
      0.10E+01, \
      0.10E+01, \
      0.10E+01, \
      0.20E+01, \
      0.20E+01, \
      0.10E+01, \
      0.10E+01 ))

  f_vec = np.array ( ( \
     0.10000000000000000000E+02, \
     0.45969769413186028260E+00, \
     0.27267564329357957615E+00, \
     0.17894056254885809051E+00, \
     0.12402556531520681830E+00, \
     0.88974396451575946519E-01, \
     0.90393123848149944133E+00, \
     0.81495684202992349481E+00, \
     0.21887522421729849008E-01, \
     0.17023439374069324596E-01 ))

  n_vec = np.array ( ( \
     0, \
     1, \
     2, \
     3, \
     4, \
     5, \
     5, \
     5, \
    10, \
    11 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    f = 0.0
    n = 0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    f = f_vec[n_data]
    n = n_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, n, f

def sin_power_int_values_test ( ):

#*****************************************************************************80
#
## sin_power_int_values_test() tests sin_power_int_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'sin_power_int_values_test():' )
  print ( '  sin_power_int_values() stores values of the cosine power integral.' )
  print ( '' )
  print ( '        A             B            N           F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, n, f = sin_power_int_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %6d  %24.16g' % ( a, b, n, f ) )

  return

def slices ( dim_num, slice_num ):

#*****************************************************************************80
#
## slices(): maximum number of pieces created by a given number of slices.
#
#  Discussion:
#
#    If we imagine slicing a pizza, each slice produce more pieces.  
#    The position of the slice affects the number of pieces created, but there
#    is a maximum.  
#
#    This function determines the maximum number of pieces created by a given
#    number of slices, applied to a space of a given dimension.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Banks,
#    Slicing Pizzas, Racing Turtles, and Further Adventures in 
#    Applied Mathematics,
#    Princeton, 1999,
#    ISBN13: 9780691059471,
#    LC: QA93.B358.
#
#  Input:
#
#    integer DIM_num, the spatial dimension.
#
#    integer SLICE_num, the number of slices.
#
#  Output:
#
#    integer VALUE, the maximum number of pieces that can
#    be created by the given number of slices applied in the given dimension.
#
  value = 0
  j_hi = min ( dim_num, slice_num ) + 1
  for j in range ( 0, j_hi ):
    value = value + i4_choose ( slice_num, j )

  return value

def slices_test ( ):

#*****************************************************************************80
#
## slices_test() tests slices().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  dim_max = 5
  slice_max = 8

  print ( '' )
  print ( 'slices_test():' )
  print ( '  slices() determines the maximum number of pieces created' )
  print ( '  by slice_num slices in a dim_num space.' )
  print ( '' )
  print ( '  SLICES' ),
  for slice_num in range ( 1, slice_max + 1 ):
    print ( '  %4d' % ( slice_num ) ),
  print ( '' )

  print ( '  DIM' )

  for dim_num in range ( 1, dim_max + 1 ):
    print ( '  %2d  : ' % ( dim_num ) ),
    for slice_num in range ( 1, slice_max + 1 ):
      value = slices ( dim_num, slice_num )
      print ( '  %4d' % ( value ) ),
    print ( '' )

  return

def spherical_harmonic ( l, m, theta, phi ):

#*****************************************************************************80
#
## spherical_harmonic() evaluates spherical harmonic functions.
#
#  Discussion:
#
#    The spherical harmonic function Y(L,M,THETA,PHI)(X) is the
#    angular part of the solution to Laplace's equation in spherical
#    coordinates.
#
#    Y(L,M,THETA,PHI)(X) is related to the associated Legendre
#    function as follows:
#
#      Y(L,M,THETA,PHI)(X) = FACTOR * P(L,M)(cos(THETA)) * exp ( i * M * PHI )
#
#    Here, FACTOR is a normalization factor:
#
#      FACTOR = sqrt ( ( 2 * L + 1 ) * ( L - M )! / ( 4 * PI * ( L + M )! ) )
#
#    In Mathematica, a spherical harmonic function can be evaluated by
#
#      SphericalHarmonicY [ l, m, theta, phi ]
#
#    Note that notational tradition in physics requires that THETA
#    and PHI represent the reverse of what they would normally mean
#    in mathematical notation; that is, THETA goes up and down, and
#    PHI goes around.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1999.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer L, the first index of the spherical harmonic function.
#    Normally, 0 <= L.
#
#    integer M, the second index of the spherical harmonic function.
#    Normally, -L <= M <= L.
#
#    real THETA, the polar angle, for which
#    0 <= THETA <= PI.
#
#    real PHI, the longitudinal angle, for which
#    0 <= PHI <= 2*PI.
#
#  Output:
#
#    real C(1:L+1), S(1:L+1), the real and imaginary
#    parts of the functions Y(L,0:L,THETA,PHI).
#
  import numpy as np

  m_abs = abs ( m )

  plm = legendre_associated_normalized ( l, m_abs, np.cos ( theta ) )

  c = np.zeros ( l + 1 )
  s = np.zeros ( l + 1 )

  for i in range ( 0, l + 1 ):
    c[i] = plm[i] * np.cos ( float ( m ) * phi )
    s[i] = plm[i] * np.sin ( float ( m ) * phi )

  if ( m < 0 ):
    for i in range ( 0, l + 1 ):
      c[i] = - c[i]
      s[i] = - s[i]

  return c, s

def spherical_harmonic_test ( ):

#*****************************************************************************80
#
## spherical_harmonic_test() tests spherical_harmonic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'spherical_harmonic_test():' )
  print ( '  spherical_harmonic() evaluates the spherical harmonic function;' )
  print ( '' )
  print ( '      L       M    THETA   PHI   YR   YI' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, l, m, theta, phi, yr, yi = spherical_harmonic_values ( n_data )

    if ( n_data == 0 ):
      break

    c, s = spherical_harmonic ( l, m, theta, phi )

    print ( '  %6d  %6d  %6f  %6f  %12f  %12f' % ( l, m, theta, phi, yr, yi ) )
    print ( '                                      %12f  %12f' % ( c[l], s[l] ) )

  return

def spherical_harmonic_values ( n_data ):

#*****************************************************************************80
#
## spherical_harmonic_values() returns values of spherical harmonic functions.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      SphericalHarmonicY [ l, m, theta, phi ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1998.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer L, integer M, real THETA, PHI, the arguments
#    of the function.
#
#    real YR, YI, the real and imaginary parts of
#    the function.
#
  import numpy as np

  n_max = 20

  l_vec = np.array ( ( \
     0,  1,  2,  \
     3,  4,  5,  \
     5,  5,  5,  \
     5,  4,  4,  \
     4,  4,  4,  \
     3,  3,  3,  \
     3,  3 ))
  m_vec = np.array ( ( \
     0,  0,  1,  \
     2,  3,  5,  \
     4,  3,  2,  \
     1,  2,  2,  \
     2,  2,  2,  \
    -1, -1, -1,  \
    -1, -1 ))
  phi_vec = np.array ( ( \
    0.1047197551196598E+01, 0.1047197551196598E+01, 0.1047197551196598E+01, \
    0.1047197551196598E+01, 0.1047197551196598E+01, 0.6283185307179586E+00, \
    0.6283185307179586E+00, 0.6283185307179586E+00, 0.6283185307179586E+00, \
    0.6283185307179586E+00, 0.7853981633974483E+00, 0.7853981633974483E+00, \
    0.7853981633974483E+00, 0.7853981633974483E+00, 0.7853981633974483E+00, \
    0.4487989505128276E+00, 0.8975979010256552E+00, 0.1346396851538483E+01, \
    0.1795195802051310E+01, 0.2243994752564138E+01 ))
  theta_vec = np.array ( ( \
    0.5235987755982989E+00, 0.5235987755982989E+00, 0.5235987755982989E+00, \
    0.5235987755982989E+00, 0.5235987755982989E+00, 0.2617993877991494E+00, \
    0.2617993877991494E+00, 0.2617993877991494E+00, 0.2617993877991494E+00, \
    0.2617993877991494E+00, 0.6283185307179586E+00, 0.1884955592153876E+01, \
    0.3141592653589793E+01, 0.4398229715025711E+01, 0.5654866776461628E+01, \
    0.3926990816987242E+00, 0.3926990816987242E+00, 0.3926990816987242E+00, \
    0.3926990816987242E+00, 0.3926990816987242E+00 ))
  yi_vec = np.array ( ( \
    0.0000000000000000E+00,  0.0000000000000000E+00, -0.2897056515173922E+00, \
    0.1916222768312404E+00,  0.0000000000000000E+00,  0.0000000000000000E+00, \
    0.3739289485283311E-02, -0.4219517552320796E-01,  0.1876264225575173E+00, \
   -0.3029973424491321E+00,  0.4139385503112256E+00, -0.1003229830187463E+00, \
    0.0000000000000000E+00, -0.1003229830187463E+00,  0.4139385503112256E+00, \
   -0.1753512375142586E+00, -0.3159720118970196E+00, -0.3940106541811563E+00, \
   -0.3940106541811563E+00, -0.3159720118970196E+00 ))
  yr_vec = np.array ( ( \
   0.2820947917738781E+00,  0.4231421876608172E+00, -0.1672616358893223E+00, \
  -0.1106331731112457E+00,  0.1354974113737760E+00,  0.5390423109043568E-03, \
  -0.5146690442951909E-02,  0.1371004361349490E-01,  0.6096352022265540E-01, \
  -0.4170400640977983E+00,  0.0000000000000000E+00,  0.0000000000000000E+00, \
   0.0000000000000000E+00,  0.0000000000000000E+00,  0.0000000000000000E+00, \
   0.3641205966137958E+00,  0.2519792711195075E+00,  0.8993036065704300E-01, \
  -0.8993036065704300E-01, -0.2519792711195075E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    l = 0
    m = 0
    theta = 0.0
    phi = 0.0
    yr = 0.0
    yi = 0.0
  else:
    l = l_vec[n_data]
    m = m_vec[n_data]
    theta = theta_vec[n_data]
    phi = phi_vec[n_data]
    yr = yr_vec[n_data]
    yi = yi_vec[n_data]
    n_data = n_data + 1

  return n_data, l, m, theta, phi, yr, yi

def spherical_harmonic_values_test ( ):

#*****************************************************************************80
#
## spherical_harmonic_values_test() tests spherical_harmonic_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'spherical_harmonic_values_test():' )
  print ( '  spherical_harmonic_values() stores values of the spherical_harmonic function.' )
  print ( '' )
  print ( '   L   M    THETA   PHI               YR                YI' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, l, m, theta, phi, yr, yi = spherical_harmonic_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %2d  %2d  %8f  %8f  %24.16f  %24.16f' % ( l, m, theta, phi, yr, yi ) )

  return

def stirling_estimate ( n ):

#*****************************************************************************80
#
## stirling_estimate() estimates log(n!) by Stirling's approximation. 
#
#  Discussion:
#
#    Originally, this function approximated n!, but suffered overflow
#    for relatively small n, such as 16.  Hence, we reverted to the
#    estimation of log(n!).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2022
#
#  Author:
#
#    Paul Nahin
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
#  Input:
#
#    integer N: the argument.
#
#  Output:
#
#    real value: Stirling's estimate for log(n!).
#
  import numpy as np

  value = 0.5 * np.log ( 2.0 * np.pi * n ) + n * ( np.log ( n ) - 1.0 )

  return value

def stirling_estimate_test ( ):

#*****************************************************************************80
#
## stirling_estimate_test() tests stirling_estimate(). 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2022
#
#  Author:
#
#    Paul Nahin
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import scipy as sp

  print ( '' )
  print ( 'stirling_estimate_test():' )
  print ( '  stirling_estimate() uses Stirling\'s approximation' )
  print ( '  to estimate n!.' )

  n = np.arange ( 1, 151 )
  f = sp.special.gammaln ( n + 1 )
  s = stirling_estimate ( n )

  fig = plt.figure ( )

  axes1 = fig.add_subplot ( 1, 2, 1 )
  axes1.semilogy ( f - s, linewidth = 3 )
  axes1.grid ( True )
  axes1.set_xlabel ( 'n' )
  axes1.set_ylabel ( 'Absolute Error' )
  axes1.set_title ( 'log(n!) - Stirling' )

  axes2 = fig.add_subplot ( 1, 2, 2 )
  axes2.plot ( f / s, linewidth = 3 )
  axes2.grid ( True )
  axes2.set_xlabel ( 'n' )
  axes2.set_ylabel ( 'Relative Error' )
  axes2.set_title ( 'log(n!) / Stirling' )

  filename = 'stirling_estimate.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def stirling1_table ( n, m ):

#*****************************************************************************80
#
## stirling1_table() tabulates the Stirling numbers of the first kind.
#
#  Discussion:
#
#    The absolute value of the Stirling number S1(N,M) gives the number
#    of permutations on N objects having exactly M cycles, while the
#    sign of the Stirling number records the sign (odd or even) of
#    the permutations.  For example, there are six permutations on 3 objects:
#
#      A B C   3 cycles (A) (B) (C)
#      A C B   2 cycles (A) (BC)
#      B A C   2 cycles (AB) (C)
#      B C A   1 cycle  (ABC)
#      C A B   1 cycle  (ABC)
#      C B A   2 cycles (AC) (B)
#
#    There are
#
#      2 permutations with 1 cycle, and S1(3,1) = 2
#      3 permutations with 2 cycles, and S1(3,2) = -3,
#      1 permutation with 3 cycles, and S1(3,3) = 1.
#
#    Since there are N! permutations of N objects, the sum of the absolute
#    values of the Stirling numbers in a given row,
#
#      sum ( 1 <= I <= N ) abs ( S1(N,I) ) = N!
#
#  First terms:
#
#    N/M:  1     2      3     4     5    6    7    8
#
#    1     1     0      0     0     0    0    0    0
#    2    -1     1      0     0     0    0    0    0
#    3     2    -3      1     0     0    0    0    0
#    4    -6    11     -6     1     0    0    0    0
#    5    24   -50     35   -10     1    0    0    0
#    6  -120   274   -225    85   -15    1    0    0
#    7   720 -1764   1624  -735   175  -21    1    0
#    8 -5040 13068 -13132  6769 -1960  322  -28    1
#
#  Recursion:
#
#    S1(N,1) = (-1)^(N-1) * (N-1)! for all N.
#    S1(I,I) = 1 for all I.
#    S1(I,J) = 0 if I < J.
#
#    S1(N,M) = S1(N-1,M-1) - (N-1) * S1(N-1,M)
#
#  Properties:
#
#    sum ( 1 <= K <= M ) S2(I,K) * S1(K,J) = Delta(I,J)
#
#    X_N = sum ( 0 <= K <= N ) S1(N,K) X^K
#    where X_N is the falling factorial function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows of the table.
#
#    integer M, the number of columns of the table.
#
#  Output:
#
#    integer S1(N,M), the Stirling numbers of the first kind.
#
  import numpy as np

  s1 = np.zeros ( ( n, m ) )

  if ( n <= 0 ):
    return s1

  if ( m <= 0 ):
    return s1

  s1[0,0] = 1
  for j in range ( 1, m ):
    s1[0,j] = 0

  for i in range ( 1, n ):

    s1[i,0] = - i * s1[i-1,0]

    for j in range ( 1, m ):
      s1[i,j] = s1[i-1,j-1] - i * s1[i-1,j]

  return s1

def stirling1_table_test ( ):

#*****************************************************************************80
#
## stirling1_table_test() tests stirling1_table().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'stirling1_table_test():' )
  print ( '  stirling1_table() tabulates Stirling numbers of the first kind.' )

  m = 8
  n = 8
  s1 = stirling1_table ( m, n )
  i4mat_print ( m, n, s1, '  Table of stirling1 numbers:' )

  return

def stirling2_number ( n, k ):

#*****************************************************************************80
#
## stirling2_number() computes a Stirling number S2(N,K) of the second kind.
#
#  Discussion:
#
#    S2(N,K) represents the number of distinct partitions of N elements
#    into K nonempty sets.  For a fixed N, the sum of the Stirling
#    numbers S2(N,K) is represented by B(N), called "Bell's number",
#    and represents the number of distinct partitions of N elements.
#
#    For example, with 4 objects, there are:
#
#    1 partition into 1 set:
#
#      (A,B,C,D)
#
#    7 partitions into 2 sets:
#
#      (A,B,C) (D)
#      (A,B,D) (C)
#      (A,C,D) (B)
#      (A) (B,C,D)
#      (A,B) (C,D)
#      (A,C) (B,D)
#      (A,D) (B,C)
#
#    6 partitions into 3 sets:
#
#      (A,B) (C) (D)
#      (A) (B,C) (D)
#      (A) (B) (C,D)
#      (A,C) (B) (D)
#      (A,D) (B) (C)
#      (A) (B,D) (C)
#
#    1 partition into 4 sets:
#
#      (A) (B) (C) (D)
#
#    So S2(4,1) = 1, S2(4,2) = 7, S2(4,3) = 6, S2(4,4) = 1, and B(4) = 15.
#
#  First terms:
#
#    N/K: 1    2    3    4    5    6    7    8
#
#    1    1    0    0    0    0    0    0    0
#    2    1    1    0    0    0    0    0    0
#    3    1    3    1    0    0    0    0    0
#    4    1    7    6    1    0    0    0    0
#    5    1   15   25   10    1    0    0    0
#    6    1   31   90   65   15    1    0    0
#    7    1   63  301  350  140   21    1    0
#    8    1  127  966 1701 1050  266   28    1
#
#  Recursion:
#
#    S2(N,1) = 1 for all N.
#    S2(I,I) = 1 for all I.
#    S2(I,J) = 0 if I < J.
#
#    S2(N,K) = K * S2(N-1,K) + S2(N-1,K-1)
#
#  Direct Formula:
#
#    s2(n,k) = 1/k! sum ( 0 <= i <= k ) (-1)^i k-choose-i ( k - i )^n
#
#  Properties:
#
#    sum ( 1 <= K <= M ) S2(I,K) * S1(K,J) = Delta(I,J)
#
#    X^N = sum ( 0 <= K <= N ) S2(N,K) X_K
#    where X_K is the falling factorial function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows of the table.
#
#    integer K, the number of columns of the table.
#
#  Output:
#
#    integer S2, the Stirling number of the second kind.
#
  import math
  import numpy as np

  s2 = 0
  mop = -1
  for i in range ( 0, k + 1 ):
    mop = - mop
    s2 = s2 + mop * i4_choose ( k, i ) * ( k - i ) ** n

  s2 = s2 / math.factorial ( k )

  return s2

def stirling2_number_test ( ):

#*****************************************************************************80
#
## stirling2_number_test() tests stirling2_number().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'stirling2_number_test():' )
  print ( '  stirling2_number() calculates a Stirling number S2(n,k)' )
  print ( '  of the second kind.' )
  print ( '' )

  for n in range ( 0, 9 ):
    for k in range ( 0, 9 ):
      s2 = stirling2_number ( n, k )
      print ( '%6d' % ( s2 ), end = '' )
    print ( '' )

  return

def stirling2_table ( n, k ):

#*****************************************************************************80
#
## stirling2_table() computes the Stirling numbers of the second kind.
#
#  Discussion:
#
#    S2(N,K) represents the number of distinct partitions of N elements
#    into K nonempty sets.  For a fixed N, the sum of the Stirling
#    numbers S2(N,K) is represented by B(N), called "Bell's number",
#    and represents the number of distinct partitions of N elements.
#
#    For example, with 4 objects, there are:
#
#    1 partition into 1 set:
#
#      (A,B,C,D)
#
#    7 partitions into 2 sets:
#
#      (A,B,C) (D)
#      (A,B,D) (C)
#      (A,C,D) (B)
#      (A) (B,C,D)
#      (A,B) (C,D)
#      (A,C) (B,D)
#      (A,D) (B,C)
#
#    6 partitions into 3 sets:
#
#      (A,B) (C) (D)
#      (A) (B,C) (D)
#      (A) (B) (C,D)
#      (A,C) (B) (D)
#      (A,D) (B) (C)
#      (A) (B,D) (C)
#
#    1 partition into 4 sets:
#
#      (A) (B) (C) (D)
#
#    So S2(4,1) = 1, S2(4,2) = 7, S2(4,3) = 6, S2(4,4) = 1, and B(4) = 15.
#
#
#  First terms:
#
#    N/K: 1    2    3    4    5    6    7    8
#
#    1    1    0    0    0    0    0    0    0
#    2    1    1    0    0    0    0    0    0
#    3    1    3    1    0    0    0    0    0
#    4    1    7    6    1    0    0    0    0
#    5    1   15   25   10    1    0    0    0
#    6    1   31   90   65   15    1    0    0
#    7    1   63  301  350  140   21    1    0
#    8    1  127  966 1701 1050  266   28    1
#
#  Recursion:
#
#    S2(N,1) = 1 for all N.
#    S2(I,I) = 1 for all I.
#    S2(I,J) = 0 if I < J.
#
#    S2(N,K) = K * S2(N-1,K) + S2(N-1,K-1)
#
#  Direct Formula:
#
#    s2(n,k) = 1/k! sum ( 0 <= i <= k ) (-1)^i k-choose-i ( k - i )^n
#
#  Properties:
#
#    sum ( 1 <= K <= M ) S2(I,K) * S1(K,J) = Delta(I,J)
#
#    X^N = sum ( 0 <= K <= N ) S2(N,K) X_K
#    where X_K is the falling factorial function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows of the table.
#
#    integer K, the number of columns of the table.
#
#  Output:
#
#    integer S2(N,K), the Stirling numbers of the second kind.
#
  import numpy as np

  s2 = np.zeros ( ( n, k ) )

  if ( n <= 0 ):
    return s2

  if ( k <= 0 ):
    return s2

  s2[0,0] = 1
  for j in range ( 1, k ):
    s2[0,j] = 0

  for i in range ( 1, n ):

    s2[i,0] = 1

    for j in range ( 1, k ):
      s2[i,j] = ( j + 1 ) * s2[i-1,j] + s2[i-1,j-1]

  return s2

def stirling2_table_test ( ):

#*****************************************************************************80
#
## stirling2_table_test() tests stirling2_table().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'stirling2_table_test():' )
  print ( '  stirling2_table() tabulates Stirling numbers of the second kind.' )

  n = 8
  k = 8
  s2 = stirling2_table ( n, k )
  i4mat_print ( n, k, s2, '  Table of Stirling2 numbers:' )

  return

def tau ( n ):

#*****************************************************************************80
#
## tau() returns the value of TAU(N), the number of distinct divisors of N.
#
#  Discussion:
#
#    TAU(N) is the number of divisors of N, including 1 and N.
#
#  First values:
#
#     N   TAU(N)
#
#     1    1
#     2    2
#     3    2
#     4    3
#     5    2
#     6    4
#     7    2
#     8    4
#     9    3
#    10    4
#    11    2
#    12    6
#    13    2
#    14    4
#    15    4
#    16    5
#    17    2
#    18    6
#    19    2
#    20    6
#
#  Formula:
#
#    If the prime factorization of N is
#
#      N = P1^E1 * P2^E2 * ... * PM^EM,
#
#    then
#
#      TAU(N) = ( E1 + 1 ) * ( E2 + 1 ) * ... * ( EM + 1 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the value to be analyzed.  N must be 1 or
#    greater.
#
#  Output:
#
#    integer TAUN, the value of TAU(N).  But if N is 0 or
#    less, TAUN is returned as 0, a nonsense value.  If there is
#    not enough room for factoring, TAUN is returned as -1.
#
  if ( n <= 0 ):
    value = 0
    return value

  if ( n == 1 ):
    value = 1
    return value
#
#  Factor N.
#
  nfactor, factor, power, nleft = i4_factor ( n )

  if ( nleft != 1 ):
    print ( '' )
    print ( 'tau(): Fatal error!' )
    print ( '  Not enough factorization space.' )

  value = 1
  for i in range ( 0, nfactor ):
    value = value * ( power[i] + 1 )

  return value

def tau_test ( ):

#*****************************************************************************80
#
## tau_test() tests tau().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'tau_test():' )
  print ( '  tau() computes the TAU function.' )
  print ( '' )
  print ( '         N      Exact         TAU(N)' )

  n_data = 0

  while ( True ):

    n_data, n, c1 = tau_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = tau ( n )

    print ( '  %8d  %12d  %12d' % ( n, c1, c2 ) )

  return

def tau_values ( n_data ):

#*****************************************************************************80
#
## tau_values() returns some values of the Tau function.
#
#  Discussion:
#
#    TAU(N) is the number of divisors of N, including 1 and N.
#
#    In Mathematica, the function can be evaluated by:
#
#      DivisorSigma[1,n]
#
#  First values:
#
#     N   TAU(N)
#
#     1    1
#     2    2
#     3    2
#     4    3
#     5    2
#     6    4
#     7    2
#     8    4
#     9    3
#    10    4
#    11    2
#    12    6
#    13    2
#    14    4
#    15    4
#    16    5
#    17    2
#    18    6
#    19    2
#    20    6
#
#  Formula:
#
#    If the prime factorization of N is
#
#      N = P1^E1 * P2^E2 * ... * PM^EM,
#
#    then
#
#      TAU(N) = ( E1 + 1 ) * ( E2 + 1 ) * ... * ( EM + 1 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the Tau function.
#
#    integer C, the value of the Tau function.
#
  import numpy as np

  n_max = 20

  c_vec = np.array ( ( \
    1,  2,  2,  3,  2,  4,  2,  4,  3,  4, \
    2, 12, 12,  4, 18, 24,  2,  8, 14, 28 ))

  n_vec = np.array ( ( \
      1,   2,   3,   4,   5,   6,   7,   8,   9,  10, \
     23,  72, 126, 226, 300, 480, 521, 610, 832, 960 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def tau_values_test ( ):

#*****************************************************************************80
#
## tau_values_test() tests tau_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'tau_values_test():' )
  print ( '  tau_values() stores values of the TAU function.' )
  print ( '' )
  print ( '             N    TAU(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = tau_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12d' % ( n, c ) )

  return

def tetrahedron_num ( n ):

#*****************************************************************************80
#
## tetrahedron_num() returns the N-th tetrahedron number.
#
#  Discussion:
#
#    The N-th tetrahedral number T3(N) is formed by the sum of the first
#    N triangular numbers:
#
#      T3(N) = sum ( 1 <= I <= N ) T2(I)
#            = sum ( 1 <= I <= N ) sum ( 1 <= J < I ) J
#
#    By convention, T3(0) = 0.
#
#    T3(N) = ( N * ( N + 1 ) * ( N + 2 ) ) / 6
#
#  First Values:
#
#     0
#     1
#     4
#    10
#    20
#    35
#    56
#    84
#   120
#   165
#   220
#   275
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the index of the desired number, which must be
#    at least 0.
#
#  Output:
#
#    integer VALUE, the N-th tetrahedronal number.
#
  value = ( n * ( n + 1 ) * ( n + 2 ) ) / 6

  return value

def tetrahedron_num_test ( ):

#*****************************************************************************80
#
## tetrahedron_num_test() tests tetrahedron_num().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'tetrahedron_num_test():' )
  print ( '  tetrahedron_num() computes the tetrahedral numbers.' )
  print ( '' )
 
  for n in range ( 1, 11 ):
    print ( '  %2d  %6d' % ( n, tetrahedron_num ( n ) ) )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def triangle_lower_to_i4 ( i, j ):

#*****************************************************************************80
#
## triangle_lower_to_i4() converts a lower triangular coordinate to an integer.
#
#  Discussion:
#
#    Triangular coordinates are handy when storing a naturally triangular
#    array (such as the lower half of a matrix) in a linear array.
#
#    Thus, for example, we might consider storing
#
#    (1,1)
#    (2,1) (2,2)
#    (3,1) (3,2) (3,3)
#    (4,1) (4,2) (4,3) (4,4)
#
#    as the linear array
#
#    (1,1) (2,1) (2,2) (3,1) (3,2) (3,3) (4,1) (4,2) (4,3) (4,4)
#
#    Here, the quantities in parenthesis represent the natural row and
#    column indices of a single number when stored in a rectangular array.
#
#    Thus, our goal is, given the row I and column J of the data,
#    to produce the value K which indicates its position in the linear
#    array.
#
#    The triangular numbers are the indices associated with the
#    diagonal elements of the original array, T(1,1), T(2,2), T(3,3)
#    and so on.
#
#  Formula:
#
#    K = J + ( (I-1) * I ) / 2
#
#  First Values:
#
#     I  J  K
#
#     0  0  0
#     1  1  1
#     2  1  2
#     2  2  3
#     3  1  4
#     3  2  5
#     3  3  6
#     4  1  7
#     4  2  8
#     4  3  9
#     4  4 10
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the row and column indices.  I and J must
#    be nonnegative, and J must not be greater than I.
#
#  Output:
#
#    integer VALUE, the linear index of the (I,J) element.
#
  if ( i < 0 ):
    print ( '' )
    print ( 'triangle_lower_to_i4(): Fatal error!' )
    print ( '  I < 0.' )
    print ( '  I = %d' % ( i ) )
    raise Exception ( 'triangle_lower_to_i4(): Fatal error!' )

  if ( j < 0 ):
    print ( '' )
    print ( 'triangle_lower_to_i4(): Fatal error!' )
    print ( '  J < 0.' )
    print ( '  J = %d' % ( j ) )
    raise Exception ( 'triangle_lower_to_i4(): Fatal error!' )

  if ( i < j ):
    print ( '' )
    print ( 'triangle_lower_to_i4(): Fatal error!' )
    print ( '  I < J.' )
    print ( '  I = %d' % ( i ) )
    print ( '  J = %d' % ( j ) )
    raise Exception ( 'triangle_lower_to_i4(): Fatal error!' )

  value = j + ( ( i - 1 ) * i ) // 2

  return value

def triangle_lower_to_i4_test ( ):

#*****************************************************************************80
#
## triangle_lower_to_i4_test() tests triangle_lower_to_i4().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'triangle_lower_to_i4_test():' )
  print ( '  triangle_lower_to_i4() converts a lower triangular index to a linear one.' )
  print ( '' )
  print ( '   ( I,    J ) ==> K' )
  print ( '' )

  for i in range ( 1, 5 ):
    for j in range ( 1, i + 1 ):
      k = triangle_lower_to_i4 ( i,j )  
      print ( '  %4d  %4d    %4d' % ( i, j, k ) )

  return

def triangle_num ( n ):

#*****************************************************************************80
#
## triangle_num() returns the N-th triangular  number.
#
#  Discussion:
#
#    The N-th triangular number T(N) is formed by the sum of the first
#    N integers:
#
#      T(N) = sum ( 1 <= I <= N ) I
#
#    By convention, T(0) = 0.
#
#    T(N) = ( N * ( N + 1 ) ) / 2
#
#  First Values:
#
#     0
#     1
#     3
#     6
#    10
#    15
#    21
#    28
#    36
#    45
#    55
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the index of the desired number, which must be
#    at least 0.
#
#  Output:
#
#    integer VALUE, the N-th triangleal number.
#
  value = ( n * ( n + 1 ) ) / 2

  return value

def triangle_num_test ( ):

#*****************************************************************************80
#
## triangle_num_test() tests triangle_num().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'triangle_num_test():' )
  print ( '  triangle_num() computes the triangular numbers.' )
  print ( '' )
 
  for n in range ( 1, 11 ):
    print ( '  %2d  %6d' % ( n, triangle_num ( n ) ) )

  return

def triangle_upper_to_i4 ( i, j ):

#*****************************************************************************80
#
## triangle_upper_to_i4() converts an upper triangular coordinate to an integer.
#
#  Discussion:
#
#    Triangular coordinates are handy when storing a naturally triangular
#    array (such as the upper half of a matrix) in a linear array.
#
#    Thus, for example, we might consider storing
#
#    (1,1) (1,2) (1,3) (1,4)
#          (2,2) (2,3) (2,4)
#                (3,3) (3,4)
#                      (4,4)
#
#    as the linear array
#
#    (1,1) (1,2) (2,2) (1,3) (2,3) (3,3) (1,4) (2,4) (3,4) (4,4)
#
#    Here, the quantities in parenthesis represent the natural row and
#    column indices of a single number when stored in a rectangular array.
#
#    Thus, our goal is, given the row I and column J of the data,
#    to produce the value K which indicates its position in the linear
#    array.
#
#    The triangular numbers are the indices associated with the
#    diagonal elements of the original array, T(1,1), T(2,2), T(3,3)
#    and so on.
#
#  Formula:
#
#    K = I + ( (J-1) * J ) / 2
#
#  First Values:
#
#     I  J  K
#
#     0  0  0
#     1  1  1
#     1  2  2
#     2  2  3
#     1  3  4
#     2  3  5
#     3  3  6
#     1  4  7
#     2  4  8
#     3  4  9
#     4  4 10
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the row and column indices.  I and J must
#    be nonnegative, and J must not be greater than I.
#
#  Output:
#
#    integer VALUE, the linear index of the (I,J) element.
#
  if ( i < 0 ):
    print ( '' )
    print ( 'triangle_upper_to_i4(): Fatal error!' )
    print ( '  I < 0.' )
    print ( '  I = %d' % ( i ) )
    raise Exception ( 'triangle_upper_to_i4(): Fatal error!' )

  if ( j < 0 ):
    print ( '' )
    print ( 'triangle_upper_to_i4(): Fatal error!' )
    print ( '  J < 0.' )
    print ( '  J = %d' % ( j ) )
    raise Exception ( 'triangle_upper_to_i4(): Fatal error!' )

  if ( i < j ):
    print ( '' )
    print ( 'triangle_upper_to_i4(): Fatal error!' )
    print ( '  I < J.' )
    print ( '  I = %d' % ( i ) )
    print ( '  J = %d' % ( j ) )
    raise Exception ( 'triangle_upper_to_i4(): Fatal error!' )

  value = i + ( ( j - 1 ) * j ) // 2

  return value

def triangle_upper_to_i4_test ( ):

#*****************************************************************************80
#
## triangle_upper_to_i4_test() tests triangle_upper_to_i4().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 March 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'triangle_upper_to_i4_test():' )
  print ( '  triangle_upper_to_i4() converts an upper triangular index to a linear one.' )
  print ( '' )
  print ( '   ( I,    J ) ==> K' )
  print ( '' )

  for i in range ( 1, 5 ):
    for j in range ( 1, i + 1 ):
      k = triangle_upper_to_i4 ( i,j )  
      print ( '  %4d  %4d    %4d' % ( i, j, k ) )

  return

def tribonacci_direct ( n ):

#*****************************************************************************80
#
## tribonacci_direct() computes the N-th Tribonacci number directly.
#
#  Example:
#
#     N   T
#    --  --
#     1   0
#     2   0
#     3   1
#     4   1
#     5   2
#     6   4
#     7   7
#     8  13
#     9  24
#    10  44
#    11  81
#    12 149
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the index of the number to compute.
#
#  Output:
#
#    integer T, the Nth Tribonacci number.
#
  import numpy as np

  alpha, beta, gamma = tribonacci_roots ( )

  if ( n <= 0 ):
    t = 0
  else:
    t = np.rint \
    ( \
      np.real \
      ( \
          alpha**n / ( - alpha**2 + 4.0 * alpha - 1.0 ) \
        + beta**n  / ( - beta**2  + 4.0 * beta  - 1.0 ) \
        + gamma**n / ( - gamma**2 + 4.0 * gamma - 1.0 ) \
      ) \
    )
    t = t.astype ( int )

  return t

def tribonacci_direct_test ( ):

#*****************************************************************************80
#
## tribonacci_direct_test() tests tribonacci_direct().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2021
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'tribonacci_direct_test():' )
  print ( '  tribonacci_direct() computes the Tribonacci sequence.' )
  print ( '' )
  
  n = 20
  for i in range ( 1, n + 1 ):
    t = tribonacci_direct ( i )
    print ( '  ', i, '  ', t )

  return

def tribonacci_recursive ( n ):

#*****************************************************************************80
#
## tribonacci_recursive() computes the first N Tribonacci numbers.
#
#  Recursion:
#
#    F(1) = 0
#    F(2) = 0
#    F(3) = 1
#    F(N) = F(N-1) + F(N-2) + F(N-3)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the highest number to compute.
#
#  Output:
#
#    integer F(N+1), the first N Tribonacci numbers.
#
  import numpy as np

  f = np.zeros ( n + 1 )

  f[0] = 0

  if ( 0 < n ):

    f[0] = 1

    if ( 1 < n ):

      f[0] = 1
      
      if ( 2 < n ):
      
        f[3] = 1

        for i in range ( 4, n + 1 ):
          f[i] = f[i-1] + f[i-2] + f[i-3]

  return f

def tribonacci_recursive_test ( ):

#*****************************************************************************80
#
## tribonacci_recursive_test() tests tribonacci_recursive().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 20

  print ( '' )
  print ( 'tribonacci_recursive_test():' )
  print ( '  tribonacci_recursive() computes Tribonacci numbers recursively;' )

  f = tribonacci_recursive ( n )

  i4vec_print ( n + 1, f, '  The Tribonacci numbers:' )

  return

def tribonacci_roots ( ):

#*****************************************************************************80
#
## tribonacci_roots() returns the Tribonacci roots.
#
#  Discussion:
#
#    The Nth Tribonacci number is defined by:
#      T(N) = T(N-1) + T(N-2) + T(N-3)
#    with
#      T(1) = 0, T(2) = 0, T(3) = 1.
#
#    The related polynomial equation
#      x^3 - x^2 - x - 1 = 0
#
#     ALPHA, BETA, and GAMMA are the roots of this equation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    W R Spickerman,
#    Binet's formula for the Tribonacci sequence,
#    Fibonacci Quarterly, 
#    Volume 20, Number 2, pages 118-120, May 1982.
#
#  Output:
#
#    real ALPHA, complex BETA, complex GAMMA, the roots.
#
  import numpy as np

  rho = np.cbrt ( 19.0 + 3.0 * np.sqrt ( 33.0 ) )
  tau = np.cbrt ( 19.0 - 3.0 * np.sqrt ( 33.0 ) )

  a = 2.0 - rho - tau
  b = np.sqrt ( 3.0 ) * ( rho - tau )

  alpha = ( 1.0 + rho + tau ) / 3.0
  beta =  ( a + b * 1j ) / 6.0
  gamma = ( a - b * 1j ) / 6.0

  return alpha, beta, gamma

def tribonacci_roots_test ( ):

#*****************************************************************************80
#
## tribonacci_roots_test() tests tribonacci_roots().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2021
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'tribonacci_roots_test():' )
  print ( '  tribonacci_roots() computes the Tribonacci roots.' )
  print ( '' );

  alpha, beta, gamma = tribonacci_roots ( )

  p = alpha**3 - alpha**2 - alpha - 1.0
  print ( '  alpha = ', alpha, ', p(alpha) = ', p )

  p = beta**3 - beta**2 - beta - 1.0
  print ( '  beta = ', beta, ', p(beta) = ', p )

  p = gamma**3 - gamma**2 - gamma - 1.0
  print ( '  gamma = ', gamma, ', p(gamma) = ', p )

  return

def trinomial ( i, j, k ):

#*****************************************************************************80
#
## trinomial() computes a trinomial coefficient.
#
#  Discussion:
#
#    The trinomial coefficient is a generalization of the binomial
#    coefficient.  It may be interpreted as the number of combinations of
#    N objects, where I objects are of type 1, J of type 2, and K of type 3.
#    and N = I + J + K.
#
#    T(I,J,K) = N! / ( I! J! K! )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, K, the factors.
#    All should be nonnegative.
#
#  Output:
#
#    integer VALUE, the trinomial coefficient.
#

#
#  Each factor must be nonnegative.
#
  if ( i < 0 or j < 0 or k < 0 ):
    print ( '' )
    print ( 'trinomial(): Fatal error!' )
    print ( '  Negative factor encountered.' )
    raise Exception ( 'trinomial(): Fatal error!' )

  value = 1

  t = 1

  for l in range ( 1, i + 1 ):
#   value = value * t // l
    t = t + 1

  for l in range ( 1, j + 1 ):
    value = value * t // l
    t = t + 1

  for l in range ( 1, k + 1 ):
    value = value * t // l
    t = t + 1
  
  return value

def trinomial_test ( ):

#*****************************************************************************80
#
## trinomial_test() tests trinomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'trinomial_test():' )
  print ( '  trinomial() evaluates the trinomial coefficient:' )
  print ( '' )
  print ( '  T(I,J,K) = (I+J+K)! / I! / J! / K!' )
  print ( '' )
  print ( '     I     J     K    T(I,J,K)' )
  print ( '' )
 
  for k in range ( 0, 5 ):
    for j in range ( 0, 5 ):
      for i in range ( 0, 5 ):
        t = trinomial ( i, j, k )
        print ( '  %4d  %4d  %4d  %8d' % ( i, j, k, t ) )

  return

def v_hofstadter ( n ):

#*****************************************************************************80
#
## v_hofstadter() computes the Hofstadter V sequence.
#
#  Discussion:
#
#    V(N) = 0                          if N = 0
#         = 1                          if 1 <= N <= 4
#         = V(N-V(N-1)) + V(N-V(N-4)), otherwise.
#
#    V(N) is defined for all nonnegative integers.
#
#  Table:
#
#     N  V(N)
#    --  ----
#
#     0     0
#     1     1
#     2     1
#     3     1
#     4     1
#     5     2
#     6     3
#     7     4
#     8     5
#     9     5
#    10     6
#    11     6
#    12     7
#    13     8
#    14     8
#    15     9
#    16     9
#    17    10
#    18    11
#    19    11
#    20    11
#    21    12
#    22    12
#    23    13
#    24    14
#    25    14
#    26    15
#    27    15
#    28    16
#    29    17
#    30    17
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the argument of the function.
#
#  Output:
#
#    integer VALUE, the value of the function.
#
  if ( n <= 0 ):
    value = 0
  elif ( n <= 4 ):
    value = 1
  else:
    value = v_hofstadter ( n - v_hofstadter(n-1) ) \
          + v_hofstadter ( n - v_hofstadter(n-4) )

  return value

def v_hofstadter_test ( ):

#*****************************************************************************80
#
## v_hofstadter_test() tests v_hofstadter().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'v_hofstadter_test():' )
  print ( '  v_hofstadter() evaluates Hofstadter\'s recursive V function.' )
  print ( '' )
  print ( '     N   V(N)' )
  print ( '' )

  for i in range ( 0, 31 ):
    v = v_hofstadter ( i )
    print ( '  %6d  %6d' % ( i, v ) )

  return

def vibonacci ( n, rng ):

#*****************************************************************************80
#
## vibonacci() computes the first N Vibonacci numbers.
#
#  Discussion:
#
#    The "Vibonacci numbers" are a generalization of the Fibonacci numbers:
#      V(N+1) = +/- V(N) +/- V(N-1)
#    where the signs are chosen randomly.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Brian Hayes,
#    The Vibonacci Numbers,
#    American Scientist,
#    July-August 1999, Volume 87, Number 4.
#
#    Divakar Viswanath,
#    Random Fibonacci sequences and the number 1.13198824,
#    Mathematics of Computation, 1998.
#
#  Input:
#
#    integer N, the highest number to compute.
#
#    rng: the current random number generator.
#
#  Output:
#
#    integer V(N), the first N Vibonacci numbers.  By convention,
#    V(1) and V(2) are taken to be 1.
#
  import numpy as np

  v = np.zeros ( n )

  if ( n <= 0 ):
    return v
 
  v[0] = 1

  if ( n <= 1 ):
    return v

  v[1] = 1

  for i in range ( 2, n ):
   
    j = rng.integers ( low = 0, high = 1, endpoint = True )

    if ( j == 0 ):
      s1 = -1
    else:
      s1 = +1

    j = rng.integers ( low = 0, high = 1, endpoint = True )

    if ( j == 0 ):
      s2 = -1
    else:
      s2 = +1

    v[i] = s1 * v[i-1] + s2 * v[i-2]

  return v

def vibonacci_test ( rng ):

#*****************************************************************************80
#
## vibonacci_test() tests vibonacci().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 January 2024
#
#  Author:
#
#    John Burkardt
#
  n = 20
  n_time = 3

  print ( '' )
  print ( 'vibonacci_test():' )
  print ( '  vibonacci() computes a Vibonacci sequence.' )
  print ( '' )
  print ( '  Compute the sequence 3 times.' )

  v1 = vibonacci ( n, rng )
  v2 = vibonacci ( n, rng )
  v3 = vibonacci ( n, rng )

  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d:  %6d  %6d  %6d' % ( i, v1[i], v2[i], v3[i] ) )

  return

def zeckendorf ( n ):

#*****************************************************************************80
#
## zeckendorf() produces the Zeckendorf decomposition of a positive integer.
#
#  Discussion:
#
#    Zeckendorf proved that every positive integer can be represented
#    uniquely as the sum of non-consecutive Fibonacci numbers.
#
#    N = sum ( 1 <= I <= M ) F_LIST(I)
#
#  Example:
#
#     N    Decomposition
#
#    50    34 + 13 + 3
#    51    34 + 13 + 3 + 1
#    52    34 + 13 + 5
#    53    34 + 13 + 5 + 1
#    54    34 + 13 + 5 + 2
#    55    55
#    56    55 + 1
#    57    55 + 2
#    58    55 + 3
#    59    55 + 3 + 1
#    60    55 + 5
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the positive integer to be decomposed.
#
#  Output:
#
#    integer M, the number of parts in the decomposition.
#
#    integer I_LIST(M), the index of the Fibonacci numbers.
#
#    integer F_LIST(M), the value of the Fibonacci numbers.
#
  import numpy as np

  m = 0
  i_list = []
#
#  Extract a sequence of Fibonacci numbers.
#
  while ( 0 < n ):
    [ f, i ] = fibonacci_floor ( n )
    i_list.append ( i )
    m = m + 1
    n = n - f
#
#  Replace any pair of consecutive indices ( I, I-1 ) by I+1.
#
  for i in range ( m - 1, 0, -1 ):

    if ( i_list[i-1] == i_list[i] + 1 ):
      i_list[i-1] = i_list[i-1] + 1
      for j in range ( i, m - 1 ):
        i_list[j] = i_list[j+1]
      m = m - 1
      i_list[m] = 0
#
#  Fill in the actual values of the Fibonacci numbers.
#
  f_list = np.zeros ( m )
  for i in range ( 0, m ):
    f_list[i] = fibonacci_direct ( i_list[i] )

  return m, i_list, f_list

def zeckendorf_test ( ):

#*****************************************************************************80
#
## zeckendorf_test() tests zeckendorf().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'zeckendorf_test():' )
  print ( '  zeckendorf() computes the Zeckendorf decomposition of' )
  print ( '  an integer N into nonconsecutive Fibonacci numbers.' )
  print ( '' )
  print ( '   N Sum M Parts' )
  print ( '' )

  for n in range ( 1, 101 ):

    m, i_list, f_list = zeckendorf ( n )

    print ( '  %3d' % ( n ) ),
    for j in range ( 0, m ):
      print ( '  %d' % ( f_list[j] ) ),
    print ( '' )

  return

def zernike_poly_coef ( m, n ):

#*****************************************************************************80
#
## zernike_poly_coef(): coefficients of a Zernike polynomial.
#
#  Discussion:
#
#    With our coefficients stored in COEFS(1:N+1), the
#    radial function R^M_N(RHO) is given by
#
#      R^M_N(RHO) = COEFS(1) 
#                 + COEFS(2) * RHO
#                 + COEFS(3) * RHO^2
#                 + ...
#                 + COEFS(N+1) * RHO^N
#
#    and the odd and even Zernike polynomials are
#
#      Z^M_N(RHO,PHI,odd)  = R^M_N(RHO) * sin(PHI)
#      Z^M_N(RHO,PHI,even) = R^M_N(RHO) * cos(PHI)
#
#    The first few "interesting" values of R are:
#
#    R^0_0 = 1
#
#    R^1_1 = RHO
#
#    R^0_2 = 2 * RHO^2 - 1
#    R^2_2 =     RHO^2
#
#    R^1_3 = 3 * RHO^3 - 2 * RHO
#    R^3_3 =     RHO^3
#
#    R^0_4 = 6 * RHO^4 - 6 * RHO^2 + 1
#    R^2_4 = 4 * RHO^4 - 3 * RHO^2
#    R^4_4 =     RHO^4
#
#    R^1_5 = 10 * RHO^5 - 12 * RHO^3 + 3 * RHO
#    R^3_5 =  5 * RHO^5 -  4 * RHO^3
#    R^5_5 =      RHO^5
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2005
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein,
#    Zernike Polynomials,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1998,
#    QA5.W45
#
#  Input:
#
#    integer M, N, the parameters of the polynomial.
#    Normally, 0 <= M <= N and 0 <= N.
#
#  Output:
#
#    real C(1:N+1), the coefficients of the polynomial.
#
  import numpy as np

  c = np.zeros ( n + 1 )

  if ( n < 0 ):
    return c

  if ( m < 0 ):
    return c
      
  if ( n < m ):
    return c

  if ( ( ( m - n ) % 2 ) == 1 ):
    return c

  nm_plus = ( ( m + n ) // 2 )
  nm_minus = ( ( n - m ) // 2 )

  c[n] = i4_choose ( n, nm_plus )

  for l in range ( 0, nm_minus ):

    c[n-2*l-2] = - float ( ( nm_plus - l ) * ( nm_minus - l ) ) * c[n-2*l] \
      / float ( ( n - l ) * ( l + 1 ) )

  return c

def zernike_poly_coef_test ( ):

#*****************************************************************************80
#
## zernike_poly_coef_test() tests zernike_poly_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'zernike_poly_coef_test():' )
  print ( '  zernike_poly_coef() determines the Zernike' )
  print ( '  polynomial coefficients.' )

  for m in range ( 0, n + 1 ):

    c = zernike_poly_coef ( m, n )
 
    r8poly_print ( n, c, '  Zernike polynomial:' )

  return

def zernike_poly ( m, n, rho ):

#*****************************************************************************80
#
## zernike_poly() evaluates a Zernike polynomial at RHO.
#
#  Discussion:
#
#    This routine uses the facts that:
#
#    *) R^M_N = 0 if M < 0, or N < 0, or N < M.
#    *) R^M_M = RHO^M
#    *) R^M_N = 0 if mod ( N - M, 2 ) = 1.
#
#    and the recursion:
#
#    R^M_(N+2) = A * [ ( B * RHO^2 - C ) * R^M_N - D * R^M_(N-2) ]
#
#    where
#
#    A = ( N + 2 ) / ( ( N + 2 )^2 - M^2 )
#    B = 4 * ( N + 1 )
#    C = ( N + M )^2 / N + ( N - M + 2 )^2 / ( N + 2 )
#    D = ( N^2 - M^2 ) / N
#
#    I wish I could clean up the recursion in the code, but for
#    now, I have to treat the case M = 0 specially.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein,
#    "Zernike Polynomials",
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1999,
#    QA5.W45
#
#  Input:
#
#    integer M, the upper index.
#
#    integer N, the lower index.
#
#    real RHO, the radial coordinate.
#
#  Output:
#
#    real Z, the value of the Zernike
#    polynomial R^M_N at the point RHO.
#

#
#  Do checks.
#
  if ( m < 0 ):
    z = 0.0
    return z

  if ( n < 0 ):
    z = 0.0
    return z

  if ( n < m ):
    z = 0.0
    return z

  if ( ( ( n - m ) % 2 ) == 1 ):
    z = 0.0
    return z

  zm2 = 0.0
  z = rho ** m

  if ( m == 0 ):

    if ( n == 0 ):
      return z

    zm2 = z
    z = 2.0 * rho * rho - 1.0

    for nn in range ( m + 2, n - 1, 2 ):

      a = float ( nn + 2 ) / float ( ( nn + 2 ) * ( nn + 2 ) - m * m )

      b = 4.0 * float ( nn + 1 )

      c = float ( ( nn + m ) * ( nn + m ) ) / float ( nn ) \
        + float ( ( nn - m + 2 ) * ( nn - m + 2 ) ) / float ( nn + 2 )

      d = float ( nn * nn - m * m ) / float ( nn )

      zp2 = a * ( ( b * rho * rho - c ) * z - d * zm2 )
      zm2 = z
      z = zp2

  else:

    for nn in range ( m, n - 1, 2 ):

      a = float ( nn + 2 ) / float ( ( nn + 2 ) * ( nn + 2 ) - m * m )

      b = 4.0 * float ( nn + 1 )

      c = float ( ( nn + m ) * ( nn + m ) ) / float ( nn ) \
        + float ( ( nn - m + 2 ) * ( nn - m + 2 ) ) / float ( nn + 2 )

      d = float ( nn * nn - m * m ) / float ( nn )

      zp2 = a * ( ( b * rho * rho - c ) * z - d * zm2 )
      zm2 = z
      z = zp2

  return z

def zernike_poly_test ( ):

#*****************************************************************************80
#
## zernike_poly_test() tests zernike_poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'zernike_poly_test():' )
  print ( '  zernike_poly() evaluates a Zernike polynomial directly.' )
  print ( '' )
  print ( '  Table of polynomial coefficients:' )
  print ( '' )
  print ( '   N   M' )
  print ( '' )

  for n in range ( 0, 6 ):

    print ( '' )

    for m in range ( 0, n + 1 ):
      c = zernike_poly_coef ( m, n )
      print ( '  %2d  %2d' % ( n, m ) ),
      for i in range ( 0, n + 1 ):
        print ( '  %7f' % ( c[i] ) ),
      print ( '' )

  rho = 0.987654321

  print ( '' )
  print ( '  Z1: Compute polynomial coefficients,' )
  print ( '  then evaluate by Horner\'s method;' )
  print ( '  Z2: Evaluate directly by recursion.' )
  print ( '' )
  print ( '   N   M       Z1              Z2' )
  print ( '' )

  for n in range ( 0, 6 ):

    print ( '' )

    for m in range ( 0, n + 1 ):

      c = zernike_poly_coef ( m, n )
      z1 = r8poly_value_horner ( n, c, rho )

      z2 = zernike_poly ( m, n, rho )

      print ( '  %2d  %2d  %16f  %16f' % ( n, m, z1, z2 ) )

  return

def zeta_m1 ( p, tol ):

#*****************************************************************************80
#
## zeta_m1() estimates the Riemann Zeta function minus 1.
#
#  Discussion:
#
#    This function includes the Euler-McLaurin correction.
#
#    zeta_M1 ( P ) = ZETA ( P ) - 1
#
#    ZETA(P) has the form 1 + small terms.  Computing ZETA(P)-1
#    allows for greater accuracy in the small terms.
#
#  Definition:
#
#    For 1 < P, the Riemann Zeta function is defined as:
#
#      ZETA ( P ) = Sum ( 1 <= N < Infinity ) 1 / N^P
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Thompson,
#    Atlas for Computing Mathematical Functions,
#    Wiley, 1997,
#    ISBN: 0471181714,
#    LC: QA331 T385
#
#  Input:
#
#    real P, the power to which the integers are raised.
#    P must be greater than 1.
#
#    real TOL, the requested relative tolerance.
#
#  Output:
#
#    real VALUE, an approximation to the Riemann
#    Zeta function minus 1.
#
  if ( p <= 1.0 ):
    print ( '' )
    print ( 'zeta_m1(): Fatal error!' )
    print ( '  Exponent P <= 1.0.' )

  nsterm = p * ( p + 1.0 ) * ( p + 2.0 ) * ( p + 3.0 ) * ( p + 4.0 ) \
    / 30240.0
    
  base = nsterm * ( 2.0 ** p ) / tol
  
  n = int ( base ** ( 1.0 / ( p + 5.0 ) ) )
  n = max ( n, 10 )
  negp = - p
  t = 0.0
  for k in range ( 2, n ):
    base = float ( k )
    t = t + base ** negp
#
#  Euler-McLaurin correction.
#
  base = float ( n )
  t = t + base ** negp \
    * ( 0.5 + float ( n ) / ( p - 1.0 ) \
    + p * ( 1.0 - \
    ( p + 1.0 ) * ( p + 2.0 ) / float ( 60 * n * n ) ) / float ( 12 * n ) \
    + nsterm / base ** ( p + 5.0 ) )
    
  return t
  
def zeta_m1_test ( ):

#*****************************************************************************80
#
## zeta_m1_test() tests zeta_m1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2017
#
#  Author:
#
#    John Burkardt
#
  import platform
  
  tol = 1.0E-10
  
  print ( '' )
  print ( 'zeta_m1_test():' )
  print ( '  zeta_m1() evaluates the Riemann Zeta function minus 1.' )
  print ( '  Relative accuracy requested is TOL = %g' % ( tol ) )
  print ( '' )
  print ( '         P                zeta_M1(P)                zeta_M1(P)' )
  print ( '                          tabulated                 computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, p, z1 = zeta_m1_values ( n_data )

    if ( n_data == 0 ):
      break

    z2 = zeta_m1 ( p, tol )

    print ( '  %8.4g  %24.16e  %24.16e' % ( p, z1, z2 ) )

  return
  
def zeta_m1_values ( n_data ):

#*****************************************************************************80
#
## zeta_m1_values() returns some values of the Riemann Zeta function minus 1.
#
#  Discussion:
#
#    zeta_M1(N) = ZETA(N) - 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real P, the argument.
#
#    real F, the value.
#
  import numpy as np

  n_max = 17

  p_vec = np.array ( ( \
     2.0, \
     2.5, \
     3.0, \
     3.5, \
     4.0, \
     5.0, \
     6.0, \
     7.0, \
     8.0, \
     9.0, \
    10.0, \
    11.0, \
    12.0, \
    16.0, \
    20.0, \
    30.0, \
    40.0 ))

  f_vec = np.array ( ( \
     0.64493406684822643647E+00, \
     0.3414872573E+00, \
     0.20205690315959428540E+00, \
     0.1267338673E+00, \
     0.8232323371113819152E-01, \
     0.3692775514336992633E-01, \
     0.1734306198444913971E-01, \
     0.834927738192282684E-02, \
     0.407735619794433939E-02, \
     0.200839292608221442E-02, \
     0.99457512781808534E-03, \
     0.49418860411946456E-03, \
     0.24608655330804830E-03, \
     0.1528225940865187E-04, \
     0.95396203387280E-06, \
     0.93132743242E-10, \
     0.90949478E-12 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    p = 0.0
    f = 0.0
  else:
    p = p_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, p, f
  
def zeta_naive ( p ):

#*****************************************************************************80
#
## zeta_naive() estimates the Riemann Zeta function.
#
#  Definition:
#
#    For 1 < P, the Riemann Zeta function is defined as:
#
#      ZETA ( P ) = Sum ( 1 <= N < Infinity ) 1 / N^P
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    real P, the power to which the integers are raised.
#    P must be greater than 1.
#
#  Output:
#
#    real VALUE, an approximation to the Riemann
#    Zeta function.
#
  if ( p <= 1.0 ):
    print ( '' )
    print ( 'zeta_naive(): Fatal error!' )
    print ( '  Exponent P <= 1.0.' )

  value = 0.0
  n = 0

  while ( True ):

    n = n + 1
    value_old = value
    value = value + 1.0 / n ** p

    if ( value <= value_old or 10000 <= n ):
      break

  return value

def zeta_naive_test ( ):

#*****************************************************************************80
#
## zeta_naive_test() tests zeta_naive().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'zeta_naive_test():' )
  print ( '  zeta() evaluates the Riemann Zeta function using a naive approach.' )
  print ( '' )
  print ( '      N                   ZETA(N)             zeta_naive(N)' )
  print ( '                          tabulate            computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, z1 = zeta_values ( n_data )

    if ( n_data == 0 ):
      break

    n_real = float ( n )
    z2 = zeta_naive ( n_real )

    print ( '  %5d  %24.16g  %24.16g' % ( n, z1, z2 ) )

  return
  
def zeta_values ( n_data ):

#*****************************************************************************80
#
## zeta_values() returns some values of the Riemann Zeta function.
#
#  Discussion:
#
#    ZETA(N) = sum ( 1 <= I < Infinity ) 1 / I^N
#
#    In Mathematica, the function can be evaluated by:
#
#      Zeta[n]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the argument of the Zeta function.
#
#    real F, the value of the Zeta function.
#
  import numpy as np

  n_max = 15

  n_vec = np.array ( ( \
     2, \
     3, \
     4, \
     5, \
     6, \
     7, \
     8, \
     9, \
    10, \
    11, \
    12, \
    16, \
    20, \
    30, \
    40 ))

  f_vec = np.array ( ( \
     0.164493406684822643647E+01, \
     0.120205690315959428540E+01, \
     0.108232323371113819152E+01, \
     0.103692775514336992633E+01, \
     0.101734306198444913971E+01, \
     0.100834927738192282684E+01, \
     0.100407735619794433939E+01, \
     0.100200839292608221442E+01, \
     0.100099457512781808534E+01, \
     0.100049418860411946456E+01, \
     0.100024608655330804830E+01, \
     0.100001528225940865187E+01, \
     0.100000095396203387280E+01, \
     0.100000000093132743242E+01, \
     0.100000000000090949478E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    f = 0.0
  else:
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, f

if ( __name__ == '__main__' ):
  timestamp ( )
  polpak_test ( )
  timestamp ( )

