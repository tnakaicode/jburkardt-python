#! /usr/bin/env python
#
def frobenius_number_data_values ( n_data, order ):

#*****************************************************************************80
#
## FROBENIUS_NUMBER_DATA_VALUES returns data for the Frobenius problem.
#
#  Discussion:
#
#    The user should first call FROBENIUS_NUMBER_ORDER_VALUES to get the
#    order or size of the "C" vector that will be returned by this routine.
#
#    The Frobenius number of order N and data C is the solution of the
#    Frobenius coin sum problem for N coin denominations C(1) through C(N).
#
#    The Frobenius coin sum problem assumes the existence of
#    N coin denominations, and asks for the largest value that cannot
#    be formed by any combination of coins of these denominations.
#
#    The coin denominations are assumed to be distinct positive integers.
#
#    For general N, this problem is fairly difficult to handle.
#
#    For N = 2, it is known that:
#
#    * if C1 and C2 are not relatively prime, then
#      there are infinitely large values that cannot be formed.
#
#    * otherwise, the largest value that cannot be formed is
#      C1 * C2 - C1 - C2, and that exactly half the values between
#      1 and C1 * C2 - C1 - C2 + 1 cannot be represented.
#
#    As a simple example, if C1 = 2 and C2 = 7, then the largest
#    unrepresentable value is 5, and there are (5+1)/2 = 3
#    unrepresentable values, namely 1, 3, and 5.
#
#    For a general N, and a set of coin denominations C1, C2, \, CN,
#    the Frobenius number F(N, C(1:N) ) is defined as the largest value
#    B for which the equation
#
#      C1*X1 + C2*X2 + \ + CN*XN = B
#
#    has no nonnegative integer solution X(1:N).
#
#    In Mathematica, the Frobenius number can be determined by
#
#      FrobeniusNumber[ {C1,...,CN} ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#    Gerard Cornuejols, Regina Urbaniak, Robert Weismantel, Laurence Wolsey,
#    Decomposition of Integer Programs and of Generating Sets,
#    in Algorithms - ESA '97,
#    Lecture Notes in Computer Science 1284,
#    edited by Rainer Burkard, G Woeginger,
#    Springer, 1997, pages 92-103.
#
#    Robert Owens,
#    An Algorithm to Solve the Frobenius Problem,
#    Mathematics Magazine,
#    Volume 76, Number 4, October 2003, 264-275.
#
#    James Sylvester,
#    Question 7382,
#    Mathematical Questions with their Solutions,
#    Educational Times,
#    Volume 41, page 21, 1884.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Parameters:
#
#    Input, integer N_DATA.  Unlike most other routines in this
#    library, this routine assumes that N_DATA has already been processed by a call
#    to FROBENIUS_NUMBER_ORDER_VALUE.  Therefore, this routine will return the
#    next set of data as long as N_DATA is in the expected range.
#
#    Input, integer ORDER, the order of the problem.
#
#    Output, integer C(ORDER), the denominations of the problem.
#
#    Output, integer F, the value of the function.
#
  import numpy as np

  n_max = 19

  c_vec = np.array ( [ \
    [     2,     5,     0,     0,     0,     0,     0,     0 ], \
    [     3,    17,     0,     0,     0,     0,     0,     0 ], \
    [     4,    19,     0,     0,     0,     0,     0,     0 ], \
    [     5,    13,     0,     0,     0,     0,     0,     0 ], \
    [    12,    11,     0,     0,     0,     0,     0,     0 ], \
    [    99,   100,     0,     0,     0,     0,     0,     0 ], \
    [     6,     9,    20,     0,     0,     0,     0,     0 ], \
    [     5,    17,    23,     0,     0,     0,     0,     0 ], \
    [   137,   251,   256,     0,     0,     0,     0,     0 ], \
    [    31,    41,    47,    61,     0,     0,     0,     0 ], \
    [   271,   277,   281,   283,     0,     0,     0,     0 ], \
    [    10,    18,    26,    33,    35,     0,     0,     0 ], \
    [    34,    37,    38,    40,    43,     0,     0,     0 ], \
    [ 12223, 12224, 36674, 61119, 85569,     0,     0,     0 ], \
    [  1000,  1476,  3764,  4864,  4871,  7773,     0,     0 ], \
    [ 12228, 36679, 36682, 46908, 61139, 73365,     0,     0 ], \
    [ 12137, 36405, 24269, 36407, 84545, 60683,     0,     0 ], \
    [ 13211, 13212, 39638, 66060, 52864, 79268, 92482,     0 ], \
    [ 13429, 26850, 26855, 40280, 40281, 53711, 53714, 67141 ] \
  ] )
 
  f_vec = np.array ( ( \
          3, \
         31, \
         53, \
         47, \
        109, \
       9701, \
         43, \
         41, \
       4948, \
        240, \
      13022, \
         67, \
        175, \
   89643481, \
      47350, \
   89716838, \
   58925134, \
  104723595, \
   45094583 ))
#
#  Step NDATA back 1.
#
  n_data = n_data - 1

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    c = []
    f = 0
  else:
    c = np.zeros ( order )
    for j in range ( 0, order ):
      c[j] = c_vec[n_data,j]
    f = f_vec[n_data]

  return c, f

def frobenius_number_data_values_test ( ):

#*****************************************************************************80
#
## FROBENIUS_NUMBER_DATA_VALUES_TEST tests FROBENIUS_NUMBER_DATA_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  from frobenius_number_order_values import frobenius_number_order_values

  print ( '' )
  print ( 'FROBENIUS_NUMBER_DATA_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FROBENIUS_NUMBER_DATA_VALUES returns the coin denominations' )
  print ( '  for a Frobenius problem.' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, order = frobenius_number_order_values ( n_data )

    if ( n_data == 0 ):
      break

    c, f = frobenius_number_data_values ( n_data, order )

    print ( '' )
    print ( '  Order = %d' % ( order ) )
    for i in range ( 0, order ):
      print ( '  %8d' % ( c[i] ) )
    print ( '' )
    print ( '' )
    print ( '  Frobenius number = %d' % ( f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FROBENIUS_NUMBER_DATA_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  frobenius_number_data_values_test ( )
  timestamp ( )

