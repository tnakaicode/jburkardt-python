#! /usr/bin/env python
#
def hermite_gk16_set ( n ):

#*****************************************************************************80
#
## HERMITE_GK16_SET sets a Hermite Genz-Keister 16 rule.
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
#    family was denoted by 1+2+6+10+16, that is, it comprised rules 
#    of successive orders O = 1, 3, 9, 19, and 35.
#
#    The precisions of these rules are P = 1, 5, 15, 29, and 51.
#
#    Consider, however, the special cases where a rule of precision 
#    at least 7, 17, 31 or 33 is desired.  Ordinarily, this would
#    suggest using the nested rule of order 9, 19, 51 or 51 respectively.
#    In these cases, however, the order of the rule that is used exceeds
#    the precision requested.  Hence, it is possible simply to select
#    a subset of the points in the higher precision rule and get a 
#    rule of lower order and the desired precision.  This accounts for
#    the four extra rules in this family.
#
#    The entire list of rules is therefore:
#
#    L   P   N
#
#    0   1   1  <-- Full rule
#    1   5   3  <-- Full rule
#    2   7   7  <-- Partial rule
#    3  15   9  <-- Full rule
#    4  17  17  <-- Partial rule
#    5  29  19  <-- Full rule
#    6  31  31  <-- Partial rule
#    7  33  33  <-- Partial rule
#    8  51  35  <-- Full rule 4
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
#    N must be 1, 3, 7, 9, 17, 19, 31, 33 or 35.
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

  elif ( n == 7 ):

    x = np.array ( [ \
             -2.9592107790638380E+00, \
             -1.2247448713915889E+00, \
             -5.2403354748695763E-01, \
              0.0000000000000000E+00, \
              5.2403354748695763E-01, \
              1.2247448713915889E+00, \
              2.9592107790638380E+00 ] )

    w = np.array ( [ \
              1.2330680655153448E-03, \
              2.4557928535031393E-01, \
              2.3286251787386100E-01, \
              8.1310410832613500E-01, \
              2.3286251787386100E-01, \
              2.4557928535031393E-01, \
              1.2330680655153448E-03 ] )

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

  elif ( n == 17 ):

    x = np.array ( [ \
             -4.4995993983103881E+00, \
             -3.6677742159463378E+00, \
             -2.9592107790638380E+00, \
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
              2.9592107790638380E+00, \
              3.6677742159463378E+00, \
              4.4995993983103881E+00 ] )

    w = np.array ( [ \
              3.7463469943051758E-08, \
             -1.4542843387069391E-06, \
              1.8723818949278350E-04, \
              1.2466519132805918E-02, \
              3.4840719346803800E-03, \
              1.5718298376652240E-01, \
              2.5155825701712934E-02, \
              4.5119803602358544E-01, \
              4.7310733504965385E-01, \
              4.5119803602358544E-01, \
              2.5155825701712934E-02, \
              1.5718298376652240E-01, \
              3.4840719346803800E-03, \
              1.2466519132805918E-02, \
              1.8723818949278350E-04, \
             -1.4542843387069391E-06, \
              3.7463469943051758E-08 ] )

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

  elif ( n == 31 ):

    x = np.array ( [ \
             -6.3759392709822356E+00, \
             -5.6432578578857449E+00, \
             -5.0360899444730940E+00, \
             -4.4995993983103881E+00, \
             -3.6677742159463378E+00, \
             -2.9592107790638380E+00, \
             -2.5705583765842968E+00, \
             -2.2665132620567876E+00, \
             -2.0232301911005157E+00, \
             -1.8357079751751868E+00, \
             -1.5794121348467671E+00, \
             -1.2247448713915889E+00, \
             -8.7004089535290285E-01, \
             -5.2403354748695763E-01, \
             -1.7606414208200893E-01, \
              0.0000000000000000E+00, \
              1.7606414208200893E-01, \
              5.2403354748695763E-01, \
              8.7004089535290285E-01, \
              1.2247448713915889E+00, \
              1.5794121348467671E+00, \
              1.8357079751751868E+00, \
              2.0232301911005157E+00, \
              2.2665132620567876E+00, \
              2.5705583765842968E+00, \
              2.9592107790638380E+00, \
              3.6677742159463378E+00, \
              4.4995993983103881E+00, \
              5.0360899444730940E+00, \
              5.6432578578857449E+00, \
              6.3759392709822356E+00 ] )

    w = np.array ( [ \
              2.2365645607044459E-15, \
             -2.6304696458548942E-13, \
              9.0675288231679823E-12, \
              1.4055252024722478E-09, \
              1.0889219692128120E-06, \
              1.0541662394746661E-04, \
              2.6665159778939428E-05, \
              4.8385208205502612E-03, \
             -9.8566270434610019E-03, \
              2.9409427580350787E-02, \
              3.1210210352682834E-03, \
              1.0939325071860877E-01, \
              1.1594930984853116E-01, \
              3.5393889029580544E-01, \
              4.9855761893293160E-02, \
              4.5888839636756751E-01, \
              4.9855761893293160E-02, \
              3.5393889029580544E-01, \
              1.1594930984853116E-01, \
              1.0939325071860877E-01, \
              3.1210210352682834E-03, \
              2.9409427580350787E-02, \
             -9.8566270434610019E-03, \
              4.8385208205502612E-03, \
              2.6665159778939428E-05, \
              1.0541662394746661E-04, \
              1.0889219692128120E-06, \
              1.4055252024722478E-09, \
              9.0675288231679823E-12, \
             -2.6304696458548942E-13, \
              2.2365645607044459E-15 ] )

  elif ( n == 33 ):

    x = np.array ( [ \
             -6.3759392709822356E+00, \
             -5.6432578578857449E+00, \
             -5.0360899444730940E+00, \
             -4.4995993983103881E+00, \
             -4.0292201405043713E+00, \
             -3.6677742159463378E+00, \
             -2.9592107790638380E+00, \
             -2.5705583765842968E+00, \
             -2.2665132620567876E+00, \
             -2.0232301911005157E+00, \
             -1.8357079751751868E+00, \
             -1.5794121348467671E+00, \
             -1.2247448713915889E+00, \
             -8.7004089535290285E-01, \
             -5.2403354748695763E-01, \
             -1.7606414208200893E-01, \
              0.0000000000000000E+00, \
              1.7606414208200893E-01, \
              5.2403354748695763E-01, \
              8.7004089535290285E-01, \
              1.2247448713915889E+00, \
              1.5794121348467671E+00, \
              1.8357079751751868E+00, \
              2.0232301911005157E+00, \
              2.2665132620567876E+00, \
              2.5705583765842968E+00, \
              2.9592107790638380E+00, \
              3.6677742159463378E+00, \
              4.0292201405043713E+00, \
              4.4995993983103881E+00, \
              5.0360899444730940E+00, \
              5.6432578578857449E+00, \
              6.3759392709822356E+00 ] )

    w = np.array ( [ \
             -1.7602932805372496E-15, \
              4.7219278666417693E-13, \
             -3.4281570530349562E-11, \
              2.7547825138935901E-09, \
             -2.3903343382803510E-08, \
              1.2245220967158438E-06, \
              9.8710009197409173E-05, \
              1.4753204901862772E-04, \
              3.7580026604304793E-03, \
             -4.9118576123877555E-03, \
              2.0435058359107205E-02, \
              1.3032872699027960E-02, \
              9.6913444944583621E-02, \
              1.3726521191567551E-01, \
              3.1208656194697448E-01, \
              1.8411696047725790E-01, \
              2.4656644932829619E-01, \
              1.8411696047725790E-01, \
              3.1208656194697448E-01, \
              1.3726521191567551E-01, \
              9.6913444944583621E-02, \
              1.3032872699027960E-02, \
              2.0435058359107205E-02, \
             -4.9118576123877555E-03, \
              3.7580026604304793E-03, \
              1.4753204901862772E-04, \
              9.8710009197409173E-05, \
              1.2245220967158438E-06, \
             -2.3903343382803510E-08, \
              2.7547825138935901E-09, \
             -3.4281570530349562E-11, \
              4.7219278666417693E-13, \
             -1.7602932805372496E-15 ] )

  elif ( n == 35 ):

    x = np.array ( [ \
             -6.3759392709822356E+00, \
             -5.6432578578857449E+00, \
             -5.0360899444730940E+00, \
             -4.4995993983103881E+00, \
             -4.0292201405043713E+00, \
             -3.6677742159463378E+00, \
             -3.3491639537131945E+00, \
             -2.9592107790638380E+00, \
             -2.5705583765842968E+00, \
             -2.2665132620567876E+00, \
             -2.0232301911005157E+00, \
             -1.8357079751751868E+00, \
             -1.5794121348467671E+00, \
             -1.2247448713915889E+00, \
             -8.7004089535290285E-01, \
             -5.2403354748695763E-01, \
             -1.7606414208200893E-01, \
              0.0000000000000000E+00, \
              1.7606414208200893E-01, \
              5.2403354748695763E-01, \
              8.7004089535290285E-01, \
              1.2247448713915889E+00, \
              1.5794121348467671E+00, \
              1.8357079751751868E+00, \
              2.0232301911005157E+00, \
              2.2665132620567876E+00, \
              2.5705583765842968E+00, \
              2.9592107790638380E+00, \
              3.3491639537131945E+00, \
              3.6677742159463378E+00, \
              4.0292201405043713E+00, \
              4.4995993983103881E+00, \
              5.0360899444730940E+00, \
              5.6432578578857449E+00, \
              6.3759392709822356E+00 ] )

    w = np.array ( [ \
              1.8684014894510604E-18, \
              9.6599466278563243E-15, \
              5.4896836948499462E-12, \
              8.1553721816916897E-10, \
              3.7920222392319532E-08, \
              4.3737818040926989E-07, \
              4.8462799737020461E-06, \
              6.3328620805617891E-05, \
              4.8785399304443770E-04, \
              1.4515580425155904E-03, \
              4.0967527720344047E-03, \
              5.5928828911469180E-03, \
              2.7780508908535097E-02, \
              8.0245518147390893E-02, \
              1.6371221555735804E-01, \
              2.6244871488784277E-01, \
              3.3988595585585218E-01, \
              9.1262675363737921E-04, \
              3.3988595585585218E-01, \
              2.6244871488784277E-01, \
              1.6371221555735804E-01, \
              8.0245518147390893E-02, \
              2.7780508908535097E-02, \
              5.5928828911469180E-03, \
              4.0967527720344047E-03, \
              1.4515580425155904E-03, \
              4.8785399304443770E-04, \
              6.3328620805617891E-05, \
              4.8462799737020461E-06, \
              4.3737818040926989E-07, \
              3.7920222392319532E-08, \
              8.1553721816916897E-10, \
              5.4896836948499462E-12, \
              9.6599466278563243E-15, \
              1.8684014894510604E-18 ] )

  else:

    print ( '' )
    print ( 'HERMITE_GK16_SET - Fatal error!' )
    print ( '  Illegal input value of N.' )
    print ( '  N must be 1, 3, 7, 9, 17, 19, 31, 33 or 35.' )
    exit ( 'HERMITE_GK16_SET - Fatal error!' )

  return x, w

def hermite_gk16_set_test ( ):

#*****************************************************************************80
#
## HERMITE_GK16_SET_TEST tests HERMITE_GK16_SET.
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

  l_max = 8

  n_list = np.array ( [ 1, 3, 7, 9, 17, 19, 31, 33, 35 ] )

  print ( '' )
  print ( 'HERMITE_GK16_SET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HERMITE_GK16_SET sets up a nested rule' )
  print ( '  for the Hermite integration problem.' )
  print ( '' )
  print ( '  Index       X             W' )

  for l in range ( 0, l_max + 1 ):

    n = n_list[l]

    x, w = hermite_gk16_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'HERMITE_GK16_SET_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hermite_gk16_set_test ( )
  timestamp ( )

