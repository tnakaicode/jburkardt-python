#! /usr/bin/env python
#
def hermite_gk22_set ( n ):

#*****************************************************************************80
#
## HERMITE_GK22_SET sets a Genz-Keister 22 Hermite rule.
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
#    family was denoted by 1+2+6+10+22, that is, it comprised rules
#    of successive orders O = 1, 3, 9, 19, and 41.
#
#    The precisions of these rules are P = 1, 5, 15, 29, and 63.
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
#    20 June 2015
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
#    Thomas Patterson,
#    The Optimal Addition of Points to Quadrature Formulae,
#    Mathematics of Computation,
#    Volume 22, Number 104, October 1968, pages 847-856.
#
#  Parameters:
#
#    Input, integer N, the order.
#    Legal values are 1, 3, 9, 19, and 41.
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

  elif ( n == 41 ):

    x = np.array ( [ \
             -7.251792998192644, \
             -6.547083258397540, \
             -5.961461043404500, \
             -5.437443360177798, \
             -4.953574342912980, \
             -4.4995993983103881, \
             -4.070919267883068, \
             -3.6677742159463378, \
             -3.296114596212218, \
             -2.9592107790638380, \
             -2.630415236459871, \
             -2.2665132620567876, \
             -2.043834754429505, \
             -2.0232301911005157, \
             -1.8357079751751868, \
             -1.585873011819188, \
             -1.2247448713915889, \
             -0.87004089535290285, \
             -0.52403354748695763, \
             -0.195324784415805, \
              0.0000000000000000, \
              0.195324784415805, \
              0.52403354748695763, \
              0.87004089535290285, \
              1.2247448713915889, \
              1.585873011819188, \
              1.8357079751751868, \
              2.0232301911005157, \
              2.043834754429505, \
              2.2665132620567876, \
              2.630415236459871, \
              2.9592107790638380, \
              3.296114596212218, \
              3.6677742159463378, \
              4.070919267883068, \
              4.4995993983103881, \
              4.953574342912980, \
              5.437443360177798, \
              5.961461043404500, \
              6.547083258397540, \
              7.251792998192644 ] )

    w = np.array ( [ \
              0.664195893812757801E-23, \
              0.860427172512207236E-19, \
              0.1140700785308509E-15, \
              0.408820161202505983E-13, \
              0.581803393170320419E-11, \
              0.400784141604834759E-09, \
              0.149158210417831408E-07, \
              0.315372265852264871E-06, \
              0.381182791749177506E-05, \
              0.288976780274478689E-04, \
              0.189010909805097887E-03, \
              0.140697424065246825E-02, \
            - 0.144528422206988237E-01, \
              0.178852543033699732E-01, \
              0.705471110122962612E-03, \
              0.165445526705860772E-01, \
              0.45109010335859128E-01, \
              0.928338228510111845E-01, \
              0.145966293895926429E+00, \
              0.165639740400529554E+00, \
              0.562793426043218877E-01, \
              0.165639740400529554E+00, \
              0.145966293895926429E+00, \
              0.928338228510111845E-01, \
              0.45109010335859128E-01, \
              0.165445526705860772E-01, \
              0.705471110122962612E-03, \
              0.178852543033699732E-01, \
            - 0.144528422206988237E-01, \
              0.140697424065246825E-02, \
              0.189010909805097887E-03, \
              0.288976780274478689E-04, \
              0.381182791749177506E-05, \
              0.315372265852264871E-06, \
              0.149158210417831408E-07, \
              0.400784141604834759E-09, \
              0.581803393170320419E-11, \
              0.408820161202505983E-13, \
              0.1140700785308509E-15, \
              0.860427172512207236E-19, \
             0.664195893812757801E-23 ] )

  else:

    print ( '' )
    print ( 'HERMITE_GK22_SET - Fatal error!' )
    print ( '  Illegal input value of N.' )
    print ( '  N must be 1, 3, 9, 19, or 41.' )
    exit ( 'HERMITE_GK22_SET - Fatal error!' )

  return x, w

def hermite_gk22_set_test ( ):

#*****************************************************************************80
#
## HERMITE_GK22_SET_TEST tests HERMITE_GK22_SET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  l_max = 4

  n_list = np.array ( [ 1, 3, 9, 19, 41 ] )

  print ( '' )
  print ( 'HERMITE_GK22_SET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HERMITE_GK22_SET sets up a nested rule' )
  print ( '  for the Hermite integration problem.' )
  print ( '' )
  print ( '  Index       X             W' )

  for l in range ( 0, l_max + 1 ):

    n = n_list[l]

    x, w = hermite_gk22_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'HERMITE_GK22_SET_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hermite_gk22_set_test ( )
  timestamp ( )

