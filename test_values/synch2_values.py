#! /usr/bin/env python
#
def synch2_values ( n_data ):

#*****************************************************************************80
#
## SYNCH2_VALUES returns some values of the synchrotron radiation function.
#
#  Discussion:
#
#    The function is defined by:
#
#      SYNCH2(x) = x * K(2/3)(x)
#
#    where K(2/3) is a modified Bessel function of order 2/3.
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
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#    special functions,
#    ACM Transactions on Mathematical Software,
#    Volume 22, Number 3, September 1996, pages 288-301.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
     0.13430727275667378338E+00, \
     0.33485265272424176976E+00, \
     0.50404224110911078651E+00, \
     0.60296523236016785113E+00, \
     0.49447506210420826699E+00, \
     0.36036067860473360389E+00, \
     0.24967785497625662113E+00, \
     0.16813830542905833533E+00, \
     0.11117122348556549832E+00, \
     0.46923205826101330711E-01, \
     0.37624545861980001482E-01, \
     0.19222123172484106436E-01, \
     0.12209535343654701398E-01, \
     0.77249644268525771866E-02, \
     0.12029044213679269639E-02, \
     0.18161187569530204281E-03, \
     0.26884338006629353506E-04, \
     0.14942212731345828759E-05, \
     0.11607696854385161390E-07, \
     0.87362343746221526073E-10 ))

  x_vec = np.array ( ( \
       0.0019531250E+00, \
       0.0312500000E+00, \
       0.1250000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       1.5000000000E+00, \
       2.0000000000E+00, \
       2.5000000000E+00, \
       3.0000000000E+00, \
       4.0000000000E+00, \
       4.2500000000E+00, \
       5.0000000000E+00, \
       5.5000000000E+00, \
       6.0000000000E+00, \
       8.0000000000E+00, \
      10.0000000000E+00, \
      12.0000000000E+00, \
      15.0000000000E+00, \
      20.0000000000E+00, \
      25.0000000000E+00 ))

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

def synch2_values_test ( ):

#*****************************************************************************80
#
## SYNCH2_VALUES_TEST demonstrates the use of SYNCH2_VALUES.
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

  print ( '' )
  print ( 'SYNCH2_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SYNCH2_VALUES stores values of the SYNCH2 function.' )
  print ( '' )
  print ( '      X         SYNCH2(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = synch2_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %24.16g' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SYNCH2_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  synch2_values_test ( )
  timestamp ( )

