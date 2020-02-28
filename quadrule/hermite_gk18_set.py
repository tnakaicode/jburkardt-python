#! /usr/bin/env python
#
def hermite_gk18_set ( n ):

#*****************************************************************************80
#
## HERMITE_GK18_SET sets a Hermite Genz-Keister 18 rule.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -oo <= x <= +oo ) f(x) exp ( - x * x ) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#    A nested family of rules for the Hermite integration problem
#    was produced by Genz and Keister.  The structure of the nested
#    family was denoted by 1+2+6+10+18, that is, it comprised rules 
#    of successive orders O = 1, 3, 9, 19, and 37.
#
#    The precisions of these rules are P = 1, 5, 15, 29, and 55.
#
#    Some of the data in this function was kindly supplied directly by
#    Alan Genz on 24 April 2011.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Genz, Bradley Keister,
#    Fully symmetric interpolatory rules for multiple integrals
#    over infinite regions with Gaussian weight,
#    Journal of Computational and Applied Mathematics,
#    Volume 71, 1996, pages 299-309
#
#    Florian Heiss, Viktor Winschel,
#    Likelihood approximation by numerical integration on sparse grids,
#    Journal of Econometrics,
#    Volume 144, 2008, pages 62-80.
#
#    Thomas Patterson,
#    The Optimal Addition of Points to Quadrature Formulae,
#    Mathematics of Computation,
#    Volume 22, Number 104, October 1968, pages 847-856.
#
#  Parameters:
#
#    Input, integer N, the order.
#    N must be 1, 3, 9, 19, or 37.
#
#    Output, real X(N,1), the abscissas.
#
#    Output, real W(N,1), the weights.
#
  import numpy as np
  from sys import exit

  if ( n == 1 ):

    x = np.array ( [ \
              0.0000000000000000E+00 ] )

    w = np.array ( [ \
              1.7724538509055159E+00 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
             -1.2247448713915889E+00, \
              0.0000000000000000E+00, \
              1.2247448713915889E+00 ] )

    w = np.array ( [ \
              2.9540897515091930E-01, \
              1.1816359006036772E+00, \
              2.9540897515091930E-01 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
             -2.9592107790638380E+00, \
             -2.0232301911005157E+00, \
             -1.2247448713915889E+00, \
             -5.2403354748695763E-01, \
              0.0000000000000000E+00, \
              5.2403354748695763E-01, \
              1.2247448713915889E+00, \
              2.0232301911005157E+00, \
              2.9592107790638380E+00 ] )

    w = np.array ( [ \
              1.6708826306882348E-04, \
              1.4173117873979098E-02, \
              1.6811892894767771E-01, \
              4.7869428549114124E-01, \
              4.5014700975378197E-01, \
              4.7869428549114124E-01, \
              1.6811892894767771E-01, \
              1.4173117873979098E-02, \
              1.6708826306882348E-04 ] )

  elif ( n == 19 ):

    x = np.array ( [ \
             -4.4995993983103881E+00, \
             -3.6677742159463378E+00, \
             -2.9592107790638380E+00, \
             -2.2665132620567876E+00, \
             -2.0232301911005157E+00, \
             -1.8357079751751868E+00, \
             -1.2247448713915889E+00, \
             -8.7004089535290285E-01, \
             -5.2403354748695763E-01, \
              0.0000000000000000E+00, \
              5.2403354748695763E-01, \
              8.7004089535290285E-01, \
              1.2247448713915889E+00, \
              1.8357079751751868E+00, \
              2.0232301911005157E+00, \
              2.2665132620567876E+00, \
              2.9592107790638380E+00, \
              3.6677742159463378E+00, \
              4.4995993983103881E+00 ] )

    w = np.array ( [ \
              1.5295717705322357E-09, \
              1.0802767206624762E-06, \
              1.0656589772852267E-04, \
              5.1133174390883855E-03, \
             -1.1232438489069229E-02, \
              3.2055243099445879E-02, \
              1.1360729895748269E-01, \
              1.0838861955003017E-01, \
              3.6924643368920851E-01, \
              5.3788160700510168E-01, \
              3.6924643368920851E-01, \
              1.0838861955003017E-01, \
              1.1360729895748269E-01, \
              3.2055243099445879E-02, \
             -1.1232438489069229E-02, \
              5.1133174390883855E-03, \
              1.0656589772852267E-04, \
              1.0802767206624762E-06, \
              1.5295717705322357E-09 ] )

  elif ( n == 37 ):

    x = np.array ( [ \
             -6.853200069757519, \
             -6.124527854622158, \
             -5.521865209868350, \
             -4.986551454150765, \
             -4.499599398310388, \
             -4.057956316089741, \
             -3.667774215946338, \
             -3.315584617593290, \
             -2.959210779063838, \
             -2.597288631188366, \
             -2.266513262056788, \
             -2.023230191100516, \
             -1.835707975175187, \
             -1.561553427651873, \
             -1.224744871391589, \
             -0.870040895352903, \
             -0.524033547486958, \
             -0.214618180588171, \
              0.000000000000000, \
              0.214618180588171, \
              0.524033547486958, \
              0.870040895352903, \
              1.224744871391589, \
              1.561553427651873, \
              1.835707975175187, \
              2.023230191100516, \
              2.266513262056788, \
              2.597288631188366, \
              2.959210779063838, \
              3.315584617593290, \
              3.667774215946338, \
              4.057956316089741, \
              4.499599398310388, \
              4.986551454150765, \
              5.521865209868350, \
              6.124527854622158, \
              6.853200069757519 ] )

    w = np.array ( [ \
            0.19030350940130498E-20, \
            0.187781893143728947E-16, \
            0.182242751549129356E-13, \
            0.45661763676186859E-11, \
            0.422525843963111041E-09, \
            0.16595448809389819E-07, \
            0.295907520230744049E-06, \
            0.330975870979203419E-05, \
            0.32265185983739747E-04, \
            0.234940366465975222E-03, \
            0.985827582996483824E-03, \
            0.176802225818295443E-02, \
            0.43334988122723492E-02, \
            0.15513109874859354E-01, \
            0.442116442189845444E-01, \
            0.937208280655245902E-01, \
            0.143099302896833389E+00, \
            0.147655710402686249E+00, \
            0.968824552928425499E-01, \
            0.147655710402686249E+00, \
            0.143099302896833389E+00, \
            0.937208280655245902E-01, \
            0.442116442189845444E-01, \
            0.15513109874859354E-01, \
            0.43334988122723492E-02, \
            0.176802225818295443E-02, \
            0.985827582996483824E-03, \
            0.234940366465975222E-03, \
            0.32265185983739747E-04, \
            0.330975870979203419E-05, \
            0.295907520230744049E-06, \
            0.16595448809389819E-07, \
            0.422525843963111041E-09, \
            0.45661763676186859E-11, \
            0.182242751549129356E-13, \
            0.187781893143728947E-16, \
            0.19030350940130498E-20 ] )

  else:

    print ( '' )
    print ( 'HERMITE_GK18_SET - Fatal error!' )
    print ( '  Illegal input value of N.' )
    print ( '  N must be 1, 3, 9, 19, or 37.' )
    exit ( 'HERMITE_GK18_SET - Fatal error!' )

  return x, w

def hermite_gk18_set_test ( ):

#*****************************************************************************80
#
## HERMITE_GK18_SET_TEST tests HERMITE_GK18_SET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  l_max = 4

  n_list = np.array ( [ 1, 3, 9, 19, 37 ] )

  print ( '' )
  print ( 'HERMITE_GK18_SET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HERMITE_GK18_SET sets up a nested rule' )
  print ( '  for the Hermite integration problem.' )
  print ( '' )
  print ( '  Index       X             W' )

  for l in range ( 0, l_max + 1 ):

    n = n_list[l]

    x, w = hermite_gk18_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'HERMITE_GK18_SET_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hermite_gk18_set_test ( )
  timestamp ( )

