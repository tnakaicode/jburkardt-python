#! /usr/bin/env python
#
def ncoh_set ( n ):

#*****************************************************************************80
#
## NCOH_SET sets abscissas and weights for Newton-Cotes "open half" quadrature.
#
#  Discussion:
#
#    The Newton-Cotes rules use equally spaced abscissas, and
#    hence may be used with equally spaced data.
#
#    The rules are called "open" because the abscissas do not include
#    the interval endpoints.
#
#    For this uncommon type of open Newton-Cotes rule, the abscissas for
#    rule N are found by dividing the interval into N equal subintervals,
#    and using the midpoint of each subinterval as the abscissa.
#
#    Most of the rules involve negative weights.  These can produce loss
#    of accuracy due to the subtraction of large, nearly equal quantities.
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    In Mathematica, the Newton-Cotes "open half" weights and abscissas
#    can be computed by the commands:
#
#      Needs["NumericalDifferentialEquationAnalysis`"]
#      NewtonCotesWeights [ n, -1, 1, QuadratureType -> Open ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 June 2015
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
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996,
#    ISBN: 0-8493-2479-3,
#    LC: QA47.M315.
#
#  Parameters:
#
#    Input, integer N, the order.
#    1 <= N <= 17.
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#
  import numpy as np
  from sys import exit

  if ( n == 1 ):

    w = np.array ( [ \
         2.0 ] )

  elif ( n == 2 ):

    w = np.array ( [ \
          1.0, \
          1.0 ] )

  elif ( n == 3 ):

    d = 4.0

    w = np.array ( [ \
            3.0 / d, \
            2.0 / d, \
            3.0 / d ] )

  elif ( n == 4 ):

    d = 24.0

    w = np.array ( [ \
          13.0 / d, \
          11.0 / d, \
          11.0 / d, \
          13.0 / d ] )

  elif ( n == 5 ):

    d = 576.0

    w = np.array ( [ \
           275.0 / d, \
           100.0 / d, \
           402.0 / d, \
           100.0 / d, \
           275.0 / d ] )

  elif ( n == 6 ):

    d = 640.0

    w = np.array ( [ \
            247.0 / d, \
            139.0 / d, \
            254.0 / d, \
            254.0 / d, \
            139.0 / d, \
            247.0 / d ] )

  elif ( n == 7 ):

    d = 138240.0

    w = np.array ( [ \
            49490.0 / d, \
             1764.0 / d, \
           112014.0 / d, \
           -50056.0 / d, \
           112014.0 / d, \
             1764.0 / d, \
            49490.0 / d ] )

  elif ( n == 8 ):

    d = 967680.0

    w = np.array ( [ \
           295627.0 / d, \
            71329.0 / d, \
           471771.0 / d, \
           128953.0 / d, \
           128953.0 / d, \
           471771.0 / d, \
            71329.0 / d, \
           295627.0 / d ] )

  elif ( n == 9 ):

    d = 2867200.0

    w = np.array ( [ \
             832221.0 / d, \
            -260808.0 / d, \
            2903148.0 / d, \
           -3227256.0 / d, \
            5239790.0 / d, \
           -3227256.0 / d, \
            2903148.0 / d, \
            -260808.0 / d, \
             832221.0 / d ] )

  elif ( n == 10 ):

    d = 18579456.0

    w = np.array ( [ \
             4751285.0 / d, \
             -492755.0 / d, \
            12269956.0 / d, \
            -6274220.0 / d, \
             8325190.0 / d, \
             8325190.0 / d, \
            -6274220.0 / d, \
            12269956.0 / d, \
             -492755.0 / d, \
             4751285.0 / d ] )

  elif ( n == 11 ):

    w = np.array ( [ \
           + 0.246271364278193434009406231628, \
           - 0.167027133984260177836566725456, \
           + 1.27129728179339588844797178131, \
           - 2.19004533609595458553791887125, \
           + 3.91748917836991567460317460317, \
           - 4.15597070872258046737213403880, \
           + 3.91748917836991567460317460317, \
           - 2.19004533609595458553791887125, \
           + 1.27129728179339588844797178131, \
           - 0.167027133984260177836566725456, \
           + 0.246271364278193434009406231628 ] )

  elif ( n == 12 ):

    w = np.array ( [ \
           + 0.221603210581329477813852813853, \
           - 0.103156166902352205086580086580, \
           + 0.889254983348763866341991341991, \
           - 1.08160728355506797889610389610, \
           + 1.49180546087620062229437229437, \
           - 0.417900204348873782467532467532, \
           - 0.417900204348873782467532467532, \
           + 1.49180546087620062229437229437, \
           - 1.08160728355506797889610389610, \
           + 0.889254983348763866341991341991, \
           - 0.103156166902352205086580086580, \
           + 0.221603210581329477813852813853 ] )

  elif ( n == 13 ):

    w = np.array ( [ \
          0.215232356419153566228270676022, \
          -0.227154289276070155983970468097, \
          1.57154640756958579127322926926, \
          -3.60188931740556785445074962271, \
          7.51615534838963020202557032914, \
          -10.7785343238762239297023523214, \
          12.6092876363589847612200042756, \
          -10.7785343238762239297023523214, \
          7.51615534838963020202557032914, \
         -3.60188931740556785445074962271, \
          1.57154640756958579127322926926, \
         -0.227154289276070155983970468097, \
          0.215232356419153566228270676022 ] )

  elif ( n == 14 ):

    w = np.array ( [ \
          0.196600731862944474955289480752, \
          -0.165179242362168469504443173425, \
          1.16085790162743923526801130968, \
          -2.14582271238684154514413484321, \
          3.66584923423684682693019643251, \
          -3.34045051168652382743365816282, \
          1.62814459870830330492873895652, \
          1.62814459870830330492873895652, \
          -3.34045051168652382743365816282, \
          3.66584923423684682693019643251, \
          -2.14582271238684154514413484321, \
          1.16085790162743923526801130968, \
          -0.165179242362168469504443173425, \
          0.196600731862944474955289480752 ] )

  elif ( n == 15 ):

    w = np.array ( [ \
          0.192053656112251156523443074782, \
          -0.277042941258250537556131864168, \
          1.90509434600895135399617123947, \
          -5.39701622989083452471078029114, \
          13.1085281753546466152623727959, \
          -23.3466945206436771323681898459, \
          33.4478422682091702199516443378, \
          -37.2655295077845143021970588935, \
          33.4478422682091702199516443378, \
         -23.3466945206436771323681898459, \
          13.1085281753546466152623727959, \
          -5.39701622989083452471078029114, \
           1.90509434600895135399617123947, \
          -0.277042941258250537556131864168, \
           0.192053656112251156523443074782 ] )

  elif ( n == 16 ):

    w = np.array ( [ \
           0.177408479879589716830780293564, \
          -0.217359399771056183974705378131, \
           1.46740967914595726066296033468, \
          -3.56820982596198712548876407280, \
           7.42429624597447227175662173974, \
         -10.1614344802943189309930887295, \
           9.74825566269696996625640284529, \
          -3.87036636166962697505020703289, \
          -3.87036636166962697505020703289, \
           9.74825566269696996625640284529, \
         -10.1614344802943189309930887295, \
           7.42429624597447227175662173974, \
          -3.56820982596198712548876407280, \
           1.46740967914595726066296033468, \
          -0.217359399771056183974705378131, \
           0.177408479879589716830780293564 ] )

  elif ( n == 17 ):

    w = np.array ( [ \
           0.174021728363203743659784786159, \
          -0.319844636797863622878597303396, \
           2.26685253417620917889510925819, \
          -7.60565246092744264614795072379, \
          21.2205863313196208783745036601, \
         -44.9326914054546061828308816595, \
          76.6598740687724224896458863733, \
        -104.621704713086021393464459433, \
         116.317117107268955109493210084, \
        -104.621704713086021393464459433, \
          76.6598740687724224896458863733, \
         -44.9326914054546061828308816595, \
          21.2205863313196208783745036601, \
          -7.60565246092744264614795072379, \
           2.26685253417620917889510925819, \
          -0.319844636797863622878597303396, \
           0.174021728363203743659784786159 ] )

  else:

    print ( '' )
    print ( 'NCOH_SET - Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 to 17.' )
    exit ( 'NCOH_SET - Fatal error!' )
#
#  Set the abscissas.
#
  a = -1.0
  b = +1.0

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = ( float ( 2 * n - 2 * i - 1 ) * a   \
           + float (         2 * i + 1 ) * b ) \
           / float ( 2 * n             )

  return x, w

def ncoh_set_test ( ):

#*****************************************************************************80
#
## NCOH_SET_TEST tests NCOH_SET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NCOH_SET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NCOH_SET sets up a Newton-Cotes Open half quadrature rule' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = ncoh_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NCOH_SET_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ncoh_set_test ( )
  timestamp ( )

