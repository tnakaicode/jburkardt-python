#! /usr/bin/env python3
#
def bashforth_set ( n ):

#*****************************************************************************80
#
## bashforth_set() sets abscissas and weights for Adams-Bashforth quadrature.
#
#  Discussion:
#
#    Adams-Bashforth quadrature formulas are normally used in solving
#    ordinary differential equations, and are not really suitable for
#    general quadrature computations.  However, an Adams-Bashforth formula
#    is equivalent to approximating the integral of F(Y(X)) between X(M)
#    and X(M+1), using an explicit formula that relies only on known values
#    of F(Y(X)) at X(M-N+1) through X(M).  For this reason, the formulas
#    have been included here.
#
#    Suppose the unknown function is denoted by Y(X), with derivative
#    F(Y(X)), and that approximate values of the function are known at a
#    series of X values, which we write as X(1), X(2), ..., X(M).  We write
#    the value Y(X(1)) as Y(1) and so on.
#
#    Then the solution of the ODE Y'=F(X,Y) at the next point X(M+1) is
#    computed by:
#
#      Y(M+1) = Y(M) + Integral ( X(M) < X < X(M+1) ) F(Y(X)) dX
#             = Y(M) + H * Sum ( 1 <= I <= N ) W(I) * F(Y(M+1-I)) approximately.
#
#    In the documentation that follows, we replace F(Y(X)) by F(X).
#
#    The integral:
#
#      Integral ( 0 <= X <= 1 ) F(X) dX.
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( 1 - I ),
#
#    The Adams-Bashforth formulas require equally spaced data.
#
#    Here is how the formula is applied in the case with non-unit spacing:
#
#      Integral ( A <= X <= A+H ) F(X) dX =
#      H * Sum ( 1 <= I <= N ) W(I) * F ( A - (I-1)*H ),
#      approximately.
#
#    The reference lists the second coefficient of the order 8 Adams-Bashforth
#    formula as
#      w(2) =  -1162169.0 / 120960.0
#    but this should be
#      w(2) =  -1152169.0 / 120960.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964.
#
#    Jean Lapidus, John Seinfeld,
#    Numerical Solution of Ordinary Differential Equations,
#    Academic Press, 1971.
#
#    Daniel Zwillinger, editor,
#    Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer N, the order.  
#    N should be between 1 and 10, or 12, 14, 16, 18 or 20.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#    W(1) is the weight at X = 0, W(2) the weight at X = -1,
#    and so on.  The weights are rational, and should sum to 1.  Some
#    weights may be negative.
#
  import numpy as np

  x = np.zeros ( n )
  w = np.zeros ( n )

  if ( n == 1 ):

    d = 1.0

    w = np.array ( [ \
       1.0 \
    ] )

  elif ( n == 2 ):

    d = 2.0

    w = np.array ( [ \
       3.0, \
     - 1.0 \
    ] )

  elif ( n == 3 ):

    d = 12.0

    w = np.array ( [ \
       23.0, \
     - 16.0, \
        5.0 \
    ] )

  elif ( n == 4 ):

    d = 24.0

    w = np.array ( [ \
       55.0, \
     - 59.0, \
       37.0, \
      - 9.0 \
    ] )

  elif ( n == 5 ):

    d = 720.0

    w = np.array ( [ \
       1901.0, \
     - 2774.0, \
       2616.0, \
     - 1274.0, \
        251.0 \
    ] )

  elif ( n == 6 ):

    d = 1440.0

    w = np.array ( [ \
       4277.0, \
     - 7923.0, \
       9982.0, \
     - 7298.0, \
       2877.0, \
      - 475.0 \
    ] )

  elif ( n == 7 ):

    d = 60480.0

    w = np.array ( [ \
        198721.0, \
      - 447288.0, \
        705549.0, \
      - 688256.0, \
        407139.0, \
      - 134472.0, \
         19087.0 \
    ] )

  elif ( n == 8 ):

    d = 120960.0

    w = np.array ( [ \
         434241.0, \
      - 1152169.0, \
        2183877.0, \
      - 2664477.0, \
        2102243.0, \
      - 1041723.0, \
         295767.0, \
        - 36799.0 \
    ] )

  elif ( n == 9 ):
  
    d = 3628800.0

    w = np.array ( [ \
       14097247.0, \
      -43125206.0, \
       95476786.0, \
     -139855262.0, \
      137968480.0, \
      -91172642.0, \
       38833486.0, \
       -9664106.0, \
        1070017.0 \
    ] )
  
  elif ( n == 10 ):
  
    d = 7257600.0

    w = np.array ( [ \
       30277247.0, \
     -104995189.0, \
      265932680.0, \
     -454661776.0, \
      538363838.0, \
     -444772162.0, \
      252618224.0, \
      -94307320.0, \
       20884811.0, \
       -2082753.0 \
    ] )
  
  elif ( n == 12 ):
  
    d = 958003200.0

    w = np.array ( [ \
        4527766399.0, \
      -19433810163.0, \
       61633227185.0, \
     -135579356757.0, \
      214139355366.0, \
     -247741639374.0, \
      211103573298.0, \
     -131365867290.0, \
       58189107627.0, \
      -17410248271.0, \
        3158642445.0, \
        -262747265.0 \
    ] )
  
  elif ( n == 14 ):
  
    d = 5230697472000.0

    w = np.array ( [ \
        27511554976875.0, \
      -140970750679621.0, \
       537247052515662.0, \
     -1445313351681906.0, \
      2854429571790805.0, \
     -4246767353305755.0, \
      4825671323488452.0, \
     -4204551925534524.0, \
      2793869602879077.0, \
     -1393306307155755.0, \
       505586141196430.0, \
      -126174972681906.0, \
        19382853593787.0, \
        -1382741929621.0 \
    ] )
  
  elif ( n == 16 ):
  
    d = 62768369664000.0

    w = np.array ( [ \
         362555126427073.0, \
       -2161567671248849.0, \
        9622096909515337.0, \
      -30607373860520569.0, \
       72558117072259733.0, \
     -131963191940828581.0, \
      187463140112902893.0, \
     -210020588912321949.0, \
      186087544263596643.0, \
     -129930094104237331.0, \
       70724351582843483.0, \
      -29417910911251819.0, \
        9038571752734087.0, \
       -1934443196892599.0, \
         257650275915823.0, \
         -16088129229375.0 \
    ] )
  
  elif ( n == 18 ):
  
    d = 64023737057280000.0

    w = np.array ( [ \
         401972381695456831.0, \
       -2735437642844079789.0, \
       13930159965811142228.0, \
      -51150187791975812900.0, \
      141500575026572531760.0, \
     -304188128232928718008.0, \
      518600355541383671092.0, \
     -710171024091234303204.0, \
      786600875277595877750.0, \
     -706174326992944287370.0, \
      512538584122114046748.0, \
     -298477260353977522892.0, \
      137563142659866897224.0, \
      -49070094880794267600.0, \
       13071639236569712860.0, \
       -2448689255584545196.0, \
         287848942064256339.0, \
         -15980174332775873.0 \
    ] )
  
  elif ( n == 20 ):
  
    d = 102181884343418880000.0

    w = np.array ( [ \
          691668239157222107697.0, \
        -5292843584961252933125.0, \
        30349492858024727686755.0, \
      -126346544855927856134295.0, \
       399537307669842150996468.0, \
      -991168450545135070835076.0, \
      1971629028083798845750380.0, \
     -3191065388846318679544380.0, \
      4241614331208149947151790.0, \
     -4654326468801478894406214.0, \
      4222756879776354065593786.0, \
     -3161821089800186539248210.0, \
      1943018818982002395655620.0, \
      -970350191086531368649620.0, \
       387739787034699092364924.0, \
      -121059601023985433003532.0, \
        28462032496476316665705.0, \
        -4740335757093710713245.0, \
          498669220956647866875.0, \
          -24919383499187492303.0 \
      ] )

  else:

    print ( '' )
    print ( 'BASHFORTH_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 through 10,' )
    print ( '  or 12, 14, 16, 18 or 20.' )
    raise Exception ( 'BASHFORTH_SET(): Fatal error!' )

  for i in range ( 0, n ):
    w[i] = w[i] / d

  for i in range ( 0, n ):
    x[i] = - float ( i )

  return x, w

def bashforth_set_test ( ):

#*****************************************************************************80
#
## bashforth_set_test() tests bashforth_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'bashforth_set_test():' )
  print ( '  bashforth_set() sets the abscissas and weights' )
  print ( '  for an Adams-Bashforth quadrature rule.' )
  print ( '' )
  print ( '    Order  W             X' )

  for n in range ( 1, 11 ):

    x, w = bashforth_set ( n )

    print ( '' )
    print ( '  %8d' % ( n ) )

    for i in range ( 0, n ):
      print ( '            %12g  %12g' % ( w[i], x[i] ) )

  return

def chebyshev1_compute ( n ):

#*****************************************************************************80
#
## chebyshev1_compute() computes a Gauss-Chebyshev type 1 quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) / sqrt ( 1 - x^2 ) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2010
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
#    integer N, the order.
#    N must be greater than 0.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  x = np.zeros ( n )
  w = np.zeros ( n )

  for i in range ( 0, n ):
    w[i] = np.pi / float ( n )

  for i in range ( 0, n ):
    x[i] = np.cos ( np.pi * float ( 2 * n - 1 - 2 * i ) / float ( 2 * n ) )

  return x, w

def chebyshev1_compute_test ( ):

#*****************************************************************************80
#
## chebyshev1_compute_test() tests chebyshev1_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev1_compute_test():' )
  print ( '  chebyshev1_compute() computes' )
  print ( '  a Chebyshev Type 1 quadrature rule over [-1,1].' )

  print ( '' )
  print ( '     Index       X                       W' )
  print ( '' )

  for n in range ( 1, 11 ):

    x, w = chebyshev1_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def chebyshev1_integral ( expon ):

#*****************************************************************************80
#
## chebyshev1_integral() evaluates a monomial Chebyshev type 1 integral.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x <= +1 ) x^n / sqrt ( 1 - x^2 ) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#
#  Output:
#
#    real EXACT, the value of the exact integral.
#
  import numpy as np
#
#  Get the exact value of the integral.
#
  if ( ( expon % 2 ) == 0 ):

    top = 1.0
    bot = 1.0
    for i in range ( 2, expon + 1, 2 ):
      top = top * float ( i - 1 )
      bot = bot * float ( i     )

    value = np.pi * float ( top ) / float ( bot )

  else:

    value = 0.0

  return value

def chebyshev1_integral_test ( ):

#*****************************************************************************80
#
## chebyshev1_integral_test() tests chebyshev1_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev1_integral_test():' )
  print ( '  chebyshev1_integral() evaluates' )
  print ( '  Integral ( -1 < x < +1 ) x^n / (1-x*x) dx' )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = chebyshev1_integral ( n )

    print ( '  %8d  %24.16g' % ( n, value ) )

  return

def chebyshev1_set ( n ):

#*****************************************************************************80
#
## chebyshev1_set() sets a Chebyshev Type 1 quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      integral  (-1 <= x <= 1 ) f(x) / sqrt  (1 - x * x ) dx
#
#    The quadrature rule:
#
#      sum  (1 <= i <= n )  (i) * f  ( (i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order.
#    N must be between 1 and 10.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
           0.0 ] )

    w = np.array ( [ \
            3.141592653589793 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
          -0.7071067811865475, \
           0.7071067811865476 ] )

    w = np.array ( [ \
               1.570796326794897, \
               1.570796326794897 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
             -0.8660254037844387, \
              0.0, \
              0.8660254037844387 ] )

    w = np.array ( [ \
               1.047197551196598, \
               1.047197551196598, \
               1.047197551196598 ] )

  elif ( n == 4 ):

    x = np.array ( [ \
             -0.9238795325112867, \
             -0.3826834323650897, \
              0.3826834323650898, \
              0.9238795325112867 ] )

    w = np.array ( [ \
              0.7853981633974483, \
              0.7853981633974483, \
              0.7853981633974483, \
              0.7853981633974483 ] )

  elif ( n == 5 ):

    x = np.array ( [ \
             -0.9510565162951535, \
             -0.5877852522924730, \
              0.0, \
              0.5877852522924731, \
              0.9510565162951535 ] )

    w = np.array ( [ \
              0.6283185307179586, \
              0.6283185307179586, \
              0.6283185307179586, \
              0.6283185307179586, \
              0.6283185307179586 ] )

  elif ( n == 6 ):

    x = np.array ( [ \
             -0.9659258262890682, \
             -0.7071067811865475, \
             -0.2588190451025206, \
              0.2588190451025207, \
              0.7071067811865476, \
              0.9659258262890683 ] )

    w = np.array ( [ \
              0.5235987755982988, \
              0.5235987755982988, \
              0.5235987755982988, \
              0.5235987755982988, \
              0.5235987755982988, \
              0.5235987755982988 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
             -0.9749279121818237, \
             -0.7818314824680295, \
             -0.4338837391175581, \
              0.0, \
              0.4338837391175582, \
              0.7818314824680298, \
              0.9749279121818236  ] )
   
    w = np.array ( [ \
              0.4487989505128276, \
              0.4487989505128276, \
              0.4487989505128276, \
              0.4487989505128276, \
              0.4487989505128276, \
              0.4487989505128276, \
              0.4487989505128276 ] )

  elif ( n == 8 ):

    x = np.array ( [ \
             -0.9807852804032304, \
             -0.8314696123025453, \
             -0.5555702330196020, \
             -0.1950903220161282, \
              0.1950903220161283, \
              0.5555702330196023, \
              0.8314696123025452, \
              0.9807852804032304 ] )

    w = np.array ( [ \
              0.3926990816987241, \
              0.3926990816987241, \
              0.3926990816987241, \
              0.3926990816987241, \
              0.3926990816987241, \
              0.3926990816987241, \
              0.3926990816987241, \
              0.3926990816987241 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
             -0.9848077530122080, \
             -0.8660254037844385, \
             -0.6427876096865394, \
             -0.3420201433256688, \
              0.0, \
              0.3420201433256688, \
              0.6427876096865394, \
              0.8660254037844387, \
              0.9848077530122080 ] )

    w = np.array ( [ \
              0.3490658503988659, \
              0.3490658503988659, \
              0.3490658503988659, \
              0.3490658503988659, \
              0.3490658503988659, \
              0.3490658503988659, \
              0.3490658503988659, \
              0.3490658503988659, \
              0.3490658503988659 ] )

  elif ( n == 10 ):

    x = np.array ( [ \
             -0.9876883405951377, \
             -0.8910065241883678, \
             -0.7071067811865475, \
             -0.4539904997395467, \
             -0.1564344650402306, \
              0.1564344650402309, \
              0.4539904997395468, \
              0.7071067811865476, \
              0.8910065241883679, \
              0.9876883405951378 ] )

    w = np.array ( [ \
              0.3141592653589793, \
              0.3141592653589793, \
              0.3141592653589793, \
              0.3141592653589793, \
              0.3141592653589793, \
              0.3141592653589793, \
              0.3141592653589793, \
              0.3141592653589793, \
              0.3141592653589793, \
              0.3141592653589793 ] )

  else:

    print ( '' )
    print ( 'CHEBYSHEV1_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' %  ( n ) )
    print ( '  Legal values are 1 through 10.' )
    raise Exception ( 'CHEBYSHEV1_SET(): Fatal error!' )

  return x, w

def chebyshev1_set_test ( ):

#*****************************************************************************80
#
## chebyshev1_set_test() tests chebyshev1_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev1_set_test():' )
  print ( '  chebyshev1_set() sets' )
  print ( '  a Chebyshev Type 1 quadrature rule over [-1,1]' )

  print ( '' )
  print ( '  Index       X             W' )
  print ( '' )

  for n in range ( 1, 11 ):

    x, w = chebyshev1_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def chebyshev2_compute ( n ):

#*****************************************************************************80
#
## chebyshev2_compute() computes a Gauss-Chebyshev type 2 quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X)  sqrt ( 1 - x^2 )  dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 June 2015
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
#    integer N, the order.
#    N must be greater than 0.
#
#  Output:
#
#    real X(N,1), the abscissas.
#
#    real W(N,1), the weights.
#
  import numpy as np

  if ( n < 1 ):
    print ( '' )
    print ( 'CHEBYSHEV2_COMPUTE(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    raise Exception ( 'CHEBYSHEV2_COMPUTE(): Fatal error!' )

  x = np.zeros ( n )
  w = np.zeros ( n )

  for i in range ( 0, n ):
    angle = np.pi * float ( n - i ) / float ( n + 1 )
    w[i] = np.pi / float ( n + 1 ) * ( np.sin ( angle ) ) ** 2
    x[i] = np.cos ( angle )

  return x, w

def chebyshev2_compute_test ( ):

#*****************************************************************************80
#
## chebyshev2_compute_test() tests chebyshev2_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev2_compute_test():' )
  print ( '  chebyshev2_compute() computes' )
  print ( '  a Chebyshev Type 2 quadrature rule over [-1,1].' )
  print ( '' )
  print ( '     Index       X                       W' )

  for n in range ( 1, 11 ):

    x, w = chebyshev2_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def chebyshev2_integral ( expon ):

#*****************************************************************************80
#
## chebyshev2_integral() evaluates a monomial Chebyshev type 2 integral.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x <= +1 ) x^n * sqrt ( 1 - x^2 ) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#
#  Output:
#
#    real EXACT, the value of the exact integral.
#
  import numpy as np
#
#  Get the exact value of the integral.
#
  if ( ( expon % 2 ) == 0 ):

    top = 1.0
    bot = 1.0
    for i in range ( 2, expon + 1, 2 ):
      top = top * float ( i - 1 )
      bot = bot * float (  i    )

      bot = bot * float ( expon + 2 )

    exact = np.pi * top / bot

  else:

    exact = 0.0

  return exact

def chebyshev2_integral_test ( ):

#*****************************************************************************80
#
## chebyshev2_integral_test() tests chebyshev2_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev2_integral_test():' )
  print ( '  chebyshev2_integral() evaluates' )
  print ( '  Integral ( -1 < x < +1 ) x^n * (1-x*x) dx' )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = chebyshev2_integral ( n )

    print ( '  %8d  %24.16g' % ( n, value ) )

  return

def chebyshev2_set ( n ):

#*****************************************************************************80
#
## chebyshev2_set() sets a Chebyshev Type 2 quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x <= 1 ) f(x) * sqrt ( 1 - x * x ) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order.
#    N must be between 1 and 10.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np
  
  if ( n == 1 ):

    x = np.array ( [ \
              0.0 ] )

    w = np.array ( [ \
               1.570796326794897 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
             -0.5000000000000000, \
              0.5000000000000000 ] )

    w = np.array ( [ \
              0.7853981633974484, \
              0.7853981633974481 ] )
 
  elif ( n == 3 ):

    x = np.array ( [ \
             -0.7071067811865475, \
              0.0, \
              0.7071067811865476 ] )

    w = np.array ( [ \
              0.3926990816987243, \
              0.7853981633974483, \
              0.3926990816987240 ] )

  elif ( n == 4 ):

    x = np.array ( [ \
             -0.8090169943749473, \
             -0.3090169943749473, \
              0.3090169943749475, \
              0.8090169943749475 ] )

    w = np.array ( [ \
              0.2170787134227061, \
              0.5683194499747424, \
              0.5683194499747423, \
              0.2170787134227060 ] )

  elif ( n == 5 ):

    x = np.array ( [ \
             -0.8660254037844387, \
             -0.5000000000000000, \
              0.0, \
              0.5000000000000000, \
              0.8660254037844387 ] )

    w = np.array ( [ \
              0.1308996938995747, \
              0.3926990816987242, \
              0.5235987755982988, \
              0.3926990816987240, \
              0.1308996938995747 ] )

  elif ( n == 6 ):

    x = np.array ( [ \
             -0.9009688679024190, \
             -0.6234898018587335, \
             -0.2225209339563143, \
              0.2225209339563144, \
              0.6234898018587336, \
              0.9009688679024191 ] )

    w = np.array ( [ \
              0.08448869089158863, \
              0.2743330560697779, \
              0.4265764164360819, \
              0.4265764164360819, \
              0.2743330560697778, \
              0.08448869089158857 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
             -0.9238795325112867, \
             -0.7071067811865475, \
             -0.3826834323650897, \
              0.0, \
              0.3826834323650898, \
              0.7071067811865476, \
              0.9238795325112867 ] )

    w = np.array ( [ \
              0.05750944903191316, \
              0.1963495408493621, \
              0.3351896326668110, \
              0.3926990816987241, \
              0.3351896326668110, \
              0.1963495408493620, \
              0.05750944903191313 ] )

  elif ( n == 8 ):

    x = np.array ( [ \
             -0.9396926207859083, \
             -0.7660444431189779, \
             -0.5000000000000000, \
             -0.1736481776669303, \
              0.1736481776669304, \
              0.5000000000000000, \
              0.7660444431189780, \
              0.9396926207859084 ] ) 

    w = np.array ( [ \
              0.04083294770910712, \
              0.1442256007956728, \
              0.2617993877991495, \
              0.3385402270935190, \
              0.3385402270935190, \
              0.2617993877991494, \
              0.1442256007956727, \
              0.04083294770910708 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
             -0.9510565162951535, \
             -0.8090169943749473, \
             -0.5877852522924730, \
             -0.3090169943749473, \
              0.0, \
              0.3090169943749475, \
              0.5877852522924731, \
              0.8090169943749475, \
              0.9510565162951535 ] )

    w = np.array ( [ \
              0.02999954037160818, \
              0.1085393567113530, \
              0.2056199086476263, \
              0.2841597249873712, \
              0.3141592653589793, \
              0.2841597249873711, \
              0.2056199086476263, \
              0.1085393567113530, \
              0.02999954037160816 ] )

  elif ( n == 10 ):

    x = np.array ( [ \
             -0.9594929736144974, \
             -0.8412535328311811, \
             -0.6548607339452850, \
             -0.4154150130018863, \
             -0.1423148382732850, \
              0.1423148382732851, \
              0.4154150130018864, \
              0.6548607339452851, \
              0.8412535328311812, \
              0.9594929736144974 ] )   

    w = np.array ( [ \
              0.02266894250185884, \
              0.08347854093418908, \
              0.1631221774548166, \
              0.2363135602034873, \
              0.2798149423030966, \
              0.2798149423030965, \
              0.2363135602034873, \
              0.1631221774548166, \
              0.08347854093418902, \
              0.02266894250185884 ] )

  else:

    print ( '' )
    print ( 'CHEBYSHEV2_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 through 10.' )
    raise Exception ( 'CHEBYSHEV2_SET(): Fatal error!' )

  return x, w

def chebyshev2_set_test ( ):

#*****************************************************************************80
#
## chebyshev2_set_test() tests chebyshev2_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev2_set_test():' )
  print ( '  chebyshev2_set() sets' )
  print ( '  a Chebyshev Type 2 quadrature rule over [-1,1]' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = chebyshev2_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def chebyshev3_compute ( n ):

#*****************************************************************************80
#
## chebyshev3_compute() computes a closed Gauss-Chebyshev (first kind) quadrature.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) / sqrt ( 1 - x^2 ) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    If N points are used, then Gauss-Chebyshev quadrature
#    will compute the integral exactly, whenever F(X) is a polynomial
#    of degree 2*N-3 or less.
#
#    The abscissas include -1 and 1.
#
#    If the order is doubled, the abscissas of the new rule include
#    all the points of the old rule.  This fact can be used to
#    efficiently implement error estimation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Zwillinger, editor,
#    Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer N, the order.
#    2 <= N.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  x = np.zeros ( n )
  w = np.zeros ( n )

  if ( n == 1 ):

    x[0] = 0.0
    w[0] = np.pi

  else:

    for i in range ( 0, n ):
      angle = float ( i ) * np.pi / float ( n - 1 )
      x[i] = np.cos ( angle )

    for i in range ( 0, n ):
      w[i] = np.pi / float ( n - 1 )

    w[0]   = 0.5 * w[0]
    w[n-1] = 0.5 * w[n-1]

  return x, w

def chebyshev3_compute_test ( ):

#*****************************************************************************80
#
## chebyshev3_compute_test() tests chebyshev3_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev3_compute_test():' )
  print ( '  chebyshev3_compute() computes' )
  print ( '  a Chebyshev Type 3 quadrature rule over [-1,1].' )
  print ( '' )
  print ( '     Index       X                       W' )

  for n in range ( 1, 11 ):

    x, w = chebyshev3_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def chebyshev3_integral ( expon ):

#*****************************************************************************80
#
## chebyshev3_integral() evaluates a monomial Chebyshev type 3 integral.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x <= +1 ) x^n / sqrt ( 1 - x^2 ) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#
#  Output:
#
#    real EXACT, the value of the exact integral.
#
  import numpy as np
#
#  Get the exact value of the integral.
#
  if ( ( expon % 2 ) == 0 ):

    top = 1.0
    bot = 1.0
    for i in range ( 2, expon + 1, 2 ):
      top = top * float ( i - 1 )
      bot = bot * float ( i     )

    value = np.pi * float ( top ) / float ( bot )

  else:

    value = 0.0

  return value

def chebyshev3_integral_test ( ):

#*****************************************************************************80
#
## chebyshev3_integral_test() tests chebyshev3_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev3_integral_test():' )
  print ( '  chebyshev3_integral() evaluates' )
  print ( '  Integral ( -1 < x < +1 ) x^n / (1-x*x) dx' )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = chebyshev3_integral ( n )

    print ( '  %8d  %24.16g' % ( n, value ) )

  return

def chebyshev3_set ( n ):

#*****************************************************************************80
#
## chebyshev3_set() sets a Chebyshev Type 3 quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x <= 1 ) f(x) / sqrt ( 1 - x * x ) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order.
#    N must be between 1 and 10.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
               0.000000000000000 ] )

    w = np.array ( [ \
               3.141592653589793 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
              -1.000000000000000, \
               1.000000000000000 ] )

    w = np.array ( [ \
               1.570796326794897, \
               1.570796326794897 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
              -1.000000000000000, \
              0.0, \
               1.000000000000000 ] )

    w = np.array ( [ \
              0.7853981633974483, \
               1.570796326794897, \
              0.7853981633974483 ] )

  elif ( n == 4 ):

    x = np.array ( [ \
              -1.000000000000000, \
             -0.5000000000000000, \
              0.5000000000000000, \
               1.000000000000000 ] )

    w = np.array ( [ \
              0.5235987755982988, \
               1.047197551196598, \
               1.047197551196598, \
              0.5235987755982988 ] )

  elif ( n == 5 ):

    x = np.array ( [ \
              -1.000000000000000, \
             -0.7071067811865475, \
              0.0, \
              0.7071067811865476, \
               1.000000000000000 ] )

    w = np.array ( [ \
              0.3926990816987241, \
              0.7853981633974483, \
              0.7853981633974483, \
              0.7853981633974483, \
              0.3926990816987241 ] )

  elif ( n == 6 ):

    x = np.array ( [ \
              -1.000000000000000, \
             -0.8090169943749473, \
             -0.3090169943749473, \
              0.3090169943749475, \
              0.8090169943749475, \
               1.000000000000000 ] )

    w = np.array ( [ \
              0.3141592653589793, \
              0.6283185307179586, \
              0.6283185307179586, \
              0.6283185307179586, \
              0.6283185307179586, \
              0.3141592653589793 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
              -1.000000000000000, \
             -0.8660254037844387, \
             -0.5000000000000000, \
              0.0, \
              0.5000000000000001, \
              0.8660254037844387, \
               1.000000000000000 ] )

    w = np.array ( [ \
              0.2617993877991494, \
              0.5235987755982988, \
              0.5235987755982988, \
              0.5235987755982988, \
              0.5235987755982988, \
              0.5235987755982988, \
              0.2617993877991494 ] )

  elif ( n == 8 ):

    x = np.array ( [ \
              -1.000000000000000, \
             -0.9009688679024190, \
             -0.6234898018587335, \
             -0.2225209339563143, \
              0.2225209339563144, \
              0.6234898018587336, \
              0.9009688679024191, \
               1.000000000000000 ] )

    w = np.array ( [ \
              0.2243994752564138, \
              0.4487989505128276, \
              0.4487989505128276, \
              0.4487989505128276, \
              0.4487989505128276, \
              0.4487989505128276, \
              0.4487989505128276, \
              0.2243994752564138 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
              -1.000000000000000, \
             -0.9238795325112867, \
             -0.7071067811865475, \
             -0.3826834323650897, \
              0.0, \
              0.3826834323650898, \
              0.7071067811865476, \
              0.9238795325112867, \
               1.000000000000000 ] )

    w = np.array ( [ \
              0.1963495408493621, \
              0.3926990816987241, \
              0.3926990816987241, \
              0.3926990816987241, \
              0.3926990816987241, \
              0.3926990816987241, \
              0.3926990816987241, \
              0.3926990816987241, \
              0.1963495408493621 ] )

  elif ( n == 10 ):

    x = np.array ( [ \
              -1.000000000000000, \
             -0.9396926207859083, \
             -0.7660444431189779, \
             -0.5000000000000000, \
             -0.1736481776669303, \
              0.1736481776669304, \
              0.5000000000000001, \
              0.7660444431189780, \
              0.9396926207859084, \
               1.000000000000000 ] )

    w = np.array ( [ \
              0.1745329251994329, \
              0.3490658503988659, \
              0.3490658503988659, \
              0.3490658503988659, \
              0.3490658503988659, \
              0.3490658503988659, \
              0.3490658503988659, \
              0.3490658503988659, \
              0.3490658503988659, \
              0.1745329251994329 ] )

  else:

    print ( '' )
    print ( 'CHEBYSHEV3_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 through 10.' )
    raise Exception ( 'CHEBYSHEV3_SET(): Fatal error!' )

  return x, w

def chebyshev3_set_test ( ):

#*****************************************************************************80
#
## chebyshev3_set_test() tests chebyshev3_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev3_set_test():' )
  print ( '  chebyshev3_set() sets' )
  print ( '  a Chebyshev Type 3 quadrature rule over [-1,1].' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = chebyshev3_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def chebyshev_set ( n ):

#*****************************************************************************80
#
## chebyshev_set() sets abscissas and weights for Chebyshev quadrature.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    The Chebyshev rule is distinguished by using equal weights.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964.
#
#    Hermann Engels,
#    Numerical Quadrature and Cubature,
#    Academic Press, 1980.
#
#    Zdenek Kopal,
#    Numerical Analysis,
#    John Wiley, 1955.
#
#    Daniel Zwillinger, editor,
#    Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer N, the order.
#    N may only have the values 1, 2, 3, 4, 5, 6, 7 or 9.
#    There are NO other Chebyshev rules with real abscissas.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
      0.0 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
      - 1.0 / np.sqrt ( 3.0 ), \
        1.0 / np.sqrt ( 3.0 ) ] )

  elif ( n == 3 ):

    x = np.array ( [ \
      - 1.0 / np.sqrt ( 2.0 ), \
        0.0, \
        1.0 / np.sqrt ( 2.0 ) ] )

  elif ( n == 4 ):

    x = np.array ( [ \
        - np.sqrt ( ( 1.0 + 2.0 / np.sqrt ( 5.0 ) ) / 3.0 ), \
        - np.sqrt ( ( 1.0 - 2.0 / np.sqrt ( 5.0 ) ) / 3.0 ), \
          np.sqrt ( ( 1.0 - 2.0 / np.sqrt ( 5.0 ) ) / 3.0 ), \
          np.sqrt ( ( 1.0 + 2.0 / np.sqrt ( 5.0 ) ) / 3.0 ) ] )

  elif ( n == 5 ):

    x = np.array ( [ \
      - np.sqrt ( ( 5.0 + np.sqrt ( 11.0) ) / 12.0 ), \
      - np.sqrt ( ( 5.0 - np.sqrt ( 11.0) ) / 12.0 ), \
        0.0, \
        np.sqrt ( ( 5.0 - np.sqrt ( 11.0) ) / 12.0 ), \
        np.sqrt ( ( 5.0 + np.sqrt ( 11.0) ) / 12.0 ) ] )

  elif ( n == 6 ):

    x = np.array ( [ \
      - 0.866246818107820591383598, \
      - 0.422518653761111529118546, \
      - 0.266635401516704720331534, \
        0.266635401516704720331534, \
        0.422518653761111529118546, \
        0.866246818107820591383598 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
      - 0.883861700758049035704224, \
      - 0.529656775285156811385048, \
      - 0.323911810519907637519673, \
        0.0, \
        0.323911810519907637519673, \
        0.529656775285156811385048, \
        0.883861700758049035704224 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
      - 0.911589307728434473664949, \
      - 0.601018655380238071428128, \
      - 0.528761783057879993260181, \
      - 0.167906184214803943068031, \
        0.0, \
        0.167906184214803943068031, \
        0.528761783057879993260181, \
        0.601018655380238071428128, \
        0.911589307728434473664949 ] )

  else:

    print ( '' )
    print ( 'CHEBYSHEV_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 through 7, and 9.' )
    raise Exception ( 'CHEBYSHEV_SET(): Fatal error!' )

  w = np.zeros ( n )
  for i in range ( 0, n ):
    w[i] = 2.0 / float ( n )

  return x, w

def chebyshev_set_test ( ):

#*****************************************************************************80
#
## chebyshev_set_test() tests chebyshev_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev_set_test():' )
  print ( '  chebyshev_set() sets' )
  print ( '  a Chebyshev quadrature rule over [-1,1]' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 10 ):

    if ( n == 8 ):
      continue

    x, w = chebyshev_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def clenshaw_curtis_compute ( n ):

#*****************************************************************************80
#
## clenshaw_curtis_compute() computes a Clenshaw Curtis quadrature rule.
#
#  Discussion:
#
#    This method uses a direct approach.  The paper by Waldvogel
#    exhibits a more efficient approach using Fourier transforms.
#
#    The integral:
#
#      integral ( -1 <= x <= 1 ) f(x) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#    The abscissas for the rule of order N can be regarded
#    as the cosines of equally spaced angles between 180 and 0 degrees:
#
#      X(I) = cos ( ( N - I ) * PI / ( N - 1 ) )
#
#    except for the basic case N = 1, when
#
#      X(1) = 0.
#
#    A Clenshaw-Curtis rule that uses N points will integrate
#    exactly all polynomials of degrees 0 through N-1.  If N
#    is odd, then by symmetry the polynomial of degree N will
#    also be integrated exactly.
#
#    If the value of N is increased in a sensible way, then
#    the new set of abscissas will include the old ones.  One such
#    sequence would be N(K) = 2*K+1 for K = 0, 1, 2, ...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2015
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
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#    Joerg Waldvogel,
#    Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
#    BIT Numerical Mathematics,
#    Volume 43, Number 1, 2003, pages 1-18.
#
#  Input:
#
#    integer N, the order.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.zeros ( n )
    w = np.zeros ( n )

    w[0] = 2.0

  else:

    theta = np.zeros ( n )

    for i in range ( 0, n ):
      theta[i] = float ( n - 1 - i ) * np.pi / float ( n - 1 )

    x = np.cos ( theta )
    w = np.zeros ( n )

    for i in range ( 0, n ):

      w[i] = 1.0

      jhi = ( ( n - 1 ) // 2 )

      for j in range ( 0, jhi ):

        if ( 2 * ( j + 1 ) == ( n - 1 ) ):
          b = 1.0
        else:
          b = 2.0

        w[i] = w[i] - b * np.cos ( 2.0 * float ( j + 1 ) * theta[i] ) \
             / float ( 4 * j * ( j + 2 ) + 3 )

    w[0] = w[0] / float ( n - 1 )
    for i in range ( 1, n - 1 ):
      w[i] = 2.0 * w[i] / float ( n - 1 )
    w[n-1] = w[n-1] / float ( n - 1 )

  return x, w

def clenshaw_curtis_compute_test ( ):

#*****************************************************************************80
#
## clenshaw_curtis_compute_test() tests clenshaw_curtis_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'clenshaw_curtis_compute_test():' )
  print ( '  clenshaw_curtis_compute() computes' )
  print ( '  a Clenshaw-Curtis quadrature rule over [-1,1].' )
  print ( '' )
  print ( '     Index       X                       W' )

  for n in range ( 1, 11 ):

    [ x, w ] = clenshaw_curtis_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def clenshaw_curtis_set ( n ):

#*****************************************************************************80
#
## clenshaw_curtis_set() sets a Clenshaw-Curtis quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    The abscissas for the rule of order N can be regarded 
#    as the cosines of equally spaced angles between 180 and 0 degrees:
#
#      X(I) = cos ( ( I - 1 ) * PI / ( N - 1 ) )
#
#    except for the basic case N = 1, when
#
#      X(1) = 0.
#
#    A Clenshaw-Curtis rule that uses N points will integrate
#    exactly all polynomials of degrees 0 through N-1.  If N
#    is odd, then by symmetry the polynomial of degree N will
#    also be integrated exactly.
#
#    If the value of N is increased in a sensible way, then
#    the new set of abscissas will include the old ones.  One such
#    sequence would be N(K) = 2*K+1 for K = 0, 1, 2, ...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
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
#    integer N, the order.
#    N must be between 1 and 17, 33, 65 or 129.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
      0.00000000000000000000 \
    ] )

    w = np.array ( [ \
      2.00000000000000000000 \
    ] )

  elif ( n == 2 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      1.00000000000000000000, \
      1.00000000000000000000 \
    ] )

  elif ( n == 3 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
      0.00000000000000000000, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.33333333333333333333, \
      1.33333333333333333333, \
      0.33333333333333333333 \
    ] )

  elif ( n == 4 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.50000000000000000000, \
      0.50000000000000000000, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.11111111111111111111, \
      0.88888888888888888889, \
      0.88888888888888888889, \
      0.11111111111111111111 \
    ] )

  elif ( n == 5 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.70710678118654752440, \
      0.00000000000000000000, \
      0.70710678118654752440, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.06666666666666666667, \
      0.53333333333333333333, \
      0.80000000000000000000, \
      0.53333333333333333333, \
      0.06666666666666666667 \
    ] )

  elif ( n == 6 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.80901699437494742410, \
     -0.30901699437494742410, \
      0.30901699437494742410, \
      0.80901699437493732410, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.04000000000000000000, \
      0.36074304120001121619, \
      0.59925695879998878381, \
      0.59925695879998878381, \
      0.36074304120001121619, \
      0.04000000000000000000 \
    ] )

  elif ( n == 7 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.86602540378443864676, \
     -0.50000000000000000000, \
      0.00000000000000000000, \
      0.50000000000000000000, \
      0.86602540378443864676, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.02857142857142857143, \
      0.25396825396825396825, \
      0.45714285714285714286, \
      0.52063492063492063492, \
      0.45714285714285714286, \
      0.25396825396825396825, \
      0.02857142857142857143 \
    ] )

  elif ( n == 8 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.90096886790241912624, \
     -0.62348980185873353053, \
     -0.22252093395631440429, \
      0.22252093395631440429, \
      0.62348980185873353053, \
      0.90096886790241910624, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.02040816326530612245, \
      0.19014100721820835178, \
      0.35224242371815911533, \
      0.43720840579832641044, \
      0.43720840579832641044, \
      0.35224242371815911533, \
      0.19014100721820835178, \
      0.02040816326530612245 \
    ] )

  elif ( n == 9 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.92387953251128675613, \
     -0.70710678118654752440, \
     -0.38268343236508977173, \
      0.00000000000000000000, \
      0.38268343236508977173, \
      0.70710678118654752440, \
      0.92387953251128675613, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.01587301587301587302, \
      0.14621864921601815501, \
      0.27936507936507936508, \
      0.36171785872048978150, \
      0.39365079365079365079, \
      0.36171785872048978150, \
      0.27936507936507936508, \
      0.14621864921601815501, \
      0.01587301587301587302 \
    ] )

  elif ( n == 10 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.93969262078590838405, \
     -0.76604444311897903520, \
     -0.50000000000000000000, \
     -0.17364817766693034885, \
      0.17364817766693034885, \
      0.50000000000000000000, \
      0.76604444311897903520, \
      0.93969262078590838405, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.01234567901234567901, \
      0.11656745657203712296, \
      0.22528432333810440813, \
      0.30194003527336860670, \
      0.34386250580414418320, \
      0.34386250580414418320, \
      0.30194003527336860670, \
      0.22528432333810440813, \
      0.11656745657203712296, \
      0.01234567901234567901 \
    ] )

  elif ( n == 11 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.95105651629515357212, \
     -0.80901699437494742410, \
     -0.58778525229247312917, \
     -0.30901699437494742410, \
      0.00000000000000000000, \
      0.30901699437494742410, \
      0.58778525229247312917, \
      0.80901699437494742410, \
      0.95105651629515357212, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.01010101010101010101, \
      0.09457905488370156116, \
      0.18563521442424776529, \
      0.25358833328368660623, \
      0.29921327042423708320, \
      0.31376623376623376623, \
      0.29921327042423708320, \
      0.25358833328368660623, \
      0.18563521442424776529, \
      0.09457905488370156116, \
      0.01010101010101010101 \
    ] )

  elif ( n == 12 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.95949297361449738989, \
     -0.84125353283118116886, \
     -0.65486073394528506406, \
     -0.41541501300188642553, \
     -0.14231483827328514044, \
      0.14231483827328514044, \
      0.41541501300188642553, \
      0.65486073394528506406, \
      0.84125353283118116886, \
      0.95949297361449738989, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.00826446280991735537, \
      0.07856015374620000543, \
      0.15504045508256136552, \
      0.21556254600086858099, \
      0.25991734106691617602, \
      0.28265504129353651666, \
      0.28265504129353651666, \
      0.25991734106691617602, \
      0.21556254600086858099, \
      0.15504045508256136552, \
      0.07856015374620000543, \
      0.00826446280991735537 \
    ] )

  elif ( n == 13 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.96592582628906828675, \
     -0.86602540378443864676, \
     -0.70710678118654752440, \
     -0.50000000000000000000, \
     -0.25881904510252076235, \
      0.00000000000000000000, \
      0.25881904510252076235, \
      0.50000000000000000000, \
      0.70710678118654752440, \
      0.86602540378443864676, \
      0.96592582628906828675, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.00699300699300699301, \
      0.06605742495207439452, \
      0.13154253154253154253, \
      0.18476338476338476338, \
      0.22697302697302697303, \
      0.25267569378104433860, \
      0.26198986198986198986, \
      0.25267569378104433860, \
      0.22697302697302697303, \
      0.18476338476338476338, \
      0.13154253154253154253, \
      0.06605742495207439452, \
      0.00699300699300699301 \
    ] )

  elif ( n == 14 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.97094181742605202716, \
     -0.88545602565320989590, \
     -0.74851074817110109863, \
     -0.56806474673115580251, \
     -0.35460488704253562597, \
     -0.12053668025532305335, \
      0.12053668025532305335, \
      0.35460488704253562597, \
      0.56806474673115580251, \
      0.74851074817110109863, \
      0.88545602565320989590, \
      0.97094181742605202716, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.00591715976331360947, \
      0.05646531376341444627, \
      0.11276867248985655881, \
      0.16003802611671868523, \
      0.19899241036578321848, \
      0.22590304977856444935, \
      0.23991536772234903239, \
      0.23991536772234903239, \
      0.22590304977856444935, \
      0.19899241036578321848, \
      0.16003802611671868523, \
      0.11276867248985655881, \
      0.05646531376341444627, \
      0.00591715976331360947 \
    ] )

  elif ( n == 15 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.97492791218182360702, \
     -0.90096886790241912624, \
     -0.78183148246802980871, \
     -0.62348980185873353053, \
     -0.43388373911755812048, \
     -0.22252093395631440429, \
      0.00000000000000000000, \
      0.22252093395631440429, \
      0.43388373911755812048, \
      0.62348980185873353053, \
      0.78183148246802980871, \
      0.90096886790241912624, \
      0.97492791218182360702, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.00512820512820512821, \
      0.04869938729508823855, \
      0.09782039167605215913, \
      0.13966507849560431803, \
      0.17560578900106674677, \
      0.20205146748238357364, \
      0.21888151163057340180, \
      0.22429633858205286777, \
      0.21888151163057340180, \
      0.20205146748238357364, \
      0.17560578900106674677, \
      0.13966507849560431803, \
      0.09782039167605215913, \
      0.04869938729508823855, \
      0.00512820512820512821 \
    ] )

  elif ( n == 16 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.97814760073380563793, \
     -0.91354545764260089550, \
     -0.80901699437494742410, \
     -0.66913060635885821383, \
     -0.50000000000000000000, \
     -0.30901699437494742410, \
     -0.10452846326765347140, \
      0.10452846326765347140, \
      0.30901699437494742410, \
      0.50000000000000000000, \
      0.66913060635885821383, \
      0.80901699437494742410, \
      0.91354545764260089550, \
      0.97814760073380563793, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.00444444444444444444, \
      0.04251476624752508988, \
      0.08553884025933288291, \
      0.12294010082849361533, \
      0.15573317603967369176, \
      0.18132978132978132978, \
      0.19921478132638853955, \
      0.20828410952436040635, \
      0.20828410952436040635, \
      0.19921478132638853955, \
      0.18132978132978132978, \
      0.15573317603967369176, \
      0.12294010082849361533, \
      0.08553884025933288291, \
      0.04251476624752508988, \
      0.00444444444444444444 \
    ] )

  elif ( n == 17 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.98078528040323044913, \
     -0.92387953251128675613, \
     -0.83146961230254523708, \
     -0.70710678118654752440, \
     -0.55557023301960222474, \
     -0.38268343236508977173, \
     -0.19509032201612826785, \
      0.00000000000000000000, \
      0.19509032201612826785, \
      0.38268343236508977173, \
      0.55557023301960222474, \
      0.70710678118654752440, \
      0.83146961230254523708, \
      0.92387953251128675613, \
      0.98078528040323044913, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.00392156862745098039, \
      0.03736870283720561032, \
      0.07548233154315183441, \
      0.10890555258189093044, \
      0.13895646836823307412, \
      0.16317266428170330256, \
      0.18147378423649335700, \
      0.19251386461292564687, \
      0.19641012582189052777, \
      0.19251386461292564687, \
      0.18147378423649335700, \
      0.16317266428170330256, \
      0.13895646836823307412, \
      0.10890555258189093044, \
      0.07548233154315183441, \
      0.03736870283720561032, \
      0.00392156862745098039 \
    ] )

  elif ( n == 33 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.99518472667219688624, \
     -0.98078528040323044913, \
     -0.95694033573220886494, \
     -0.92387953251128675613, \
     -0.88192126434835502971, \
     -0.83146961230254523708, \
     -0.77301045336273696081, \
     -0.70710678118654752440, \
     -0.63439328416364549822, \
     -0.55557023301960222474, \
     -0.47139673682599764856, \
     -0.38268343236508977173, \
     -0.29028467725446236764, \
     -0.19509032201612826785, \
     -0.098017140329560601994, \
      0.000000000000000000000, \
      0.098017140329560601994, \
      0.19509032201612826785, \
      0.29028467725446236764, \
      0.38268343236508977173, \
      0.47139673682599764856, \
      0.55557023301960222474, \
      0.63439328416364549822, \
      0.70710678118654752440, \
      0.77301045336273696081, \
      0.83146961230254523708, \
      0.88192126434835502971, \
      0.92387953251128675613, \
      0.95694033573220886494, \
      0.98078528040323044913, \
      0.99518472667219688624, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.00097751710654936461, \
      0.00939319796295501470, \
      0.01923424513268114918, \
      0.02845791667723369009, \
      0.03759434191404720602, \
      0.04626276283775174949, \
      0.05455501630398031044, \
      0.06227210954529400455, \
      0.06942757563043545090, \
      0.07588380044138847048, \
      0.08163481765493851023, \
      0.08657753844182743544, \
      0.09070611286772099874, \
      0.09394324443876873573, \
      0.09629232594548817919, \
      0.09769818820805558182, \
      0.09817857778176829677, \
      0.09769818820805558182, \
      0.09629232594548817919, \
      0.09394324443876873573, \
      0.09070611286772099874, \
      0.08657753844182743544, \
      0.08163481765493851023, \
      0.07588380044138847048, \
      0.06942757563043545090, \
      0.06227210954529400455, \
      0.05455501630398031044, \
      0.04626276283775174949, \
      0.03759434191404720602, \
      0.02845791667723369009, \
      0.01923424513268114918, \
      0.00939319796295501470, \
      0.00097751710654936461 \
    ] )

  elif ( n == 65 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.99879545620517239271, \
     -0.99518472667219688624, \
     -0.98917650996478097345, \
     -0.98078528040323044913, \
     -0.97003125319454399260, \
     -0.95694033573220886494, \
     -0.94154406518302077841, \
     -0.92387953251128675613, \
     -0.90398929312344333159, \
     -0.88192126434835502971, \
     -0.85772861000027206990, \
     -0.83146961230254523708, \
     -0.80320753148064490981, \
     -0.77301045336273696081, \
     -0.74095112535495909118, \
     -0.70710678118654752440, \
     -0.67155895484701840063, \
     -0.63439328416364549822, \
     -0.59569930449243334347, \
     -0.55557023301960222474, \
     -0.51410274419322172659, \
     -0.47139673682599764856, \
     -0.42755509343028209432, \
     -0.38268343236508977173, \
     -0.33688985339222005069, \
     -0.29028467725446236764, \
     -0.24298017990326388995, \
     -0.19509032201612826785, \
     -0.14673047445536175166, \
     -0.098017140329560601994, \
     -0.049067674327418014255, \
      0.000000000000000000000, \
      0.049067674327418014255, \
      0.098017140329560601994, \
      0.14673047445536175166, \
      0.19509032201612826785, \
      0.24298017990326388995, \
      0.29028467725446236764, \
      0.33688985339222005069, \
      0.38268343236508977173, \
      0.42755509343028209432, \
      0.47139673682599764856, \
      0.51410274419322172659, \
      0.55557023301960222474, \
      0.59569930449243334347, \
      0.63439328416364549822, \
      0.67155895484701840063, \
      0.70710678118654752440, \
      0.74095112535495909118, \
      0.77301045336273696081, \
      0.80320753148064490981, \
      0.83146961230254523708, \
      0.85772861000027206990, \
      0.88192126434835502971, \
      0.90398929312344333159, \
      0.92387953251128675613, \
      0.94154406518302077841, \
      0.95694033573220886494, \
      0.97003125319454399260, \
      0.98078528040323044913, \
      0.98917650996478097345, \
      0.99518472667219688624, \
      0.99879545620517239271, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.00024420024420024420, \
      0.00235149067531170332, \
      0.00483146544879091264, \
      0.00719269316173611402, \
      0.00958233879528379039, \
      0.01192339471421277160, \
      0.01425206043235199679, \
      0.01653498765728958965, \
      0.01878652974179578354, \
      0.02098627442973743378, \
      0.02314069493435819848, \
      0.02523506498175476590, \
      0.02727225714146838686, \
      0.02924065319746833770, \
      0.03114129710406762447, \
      0.03296454656997632997, \
      0.03471049818092511427, \
      0.03637092028663918309, \
      0.03794545992128481711, \
      0.03942698871295609976, \
      0.04081501340035783384, \
      0.04210333111141810203, \
      0.04329151496169082935, \
      0.04437417923925731580, \
      0.04535110955166067221, \
      0.04621766751092557684, \
      0.04697395904661414870, \
      0.04761604458525019296, \
      0.04814443257251220341, \
      0.04855584485714105274, \
      0.04885125664306609371, \
      0.04902801843102555294, \
      0.04908762351494245585, \
      0.04902801843102555294, \
      0.04885125664306609371, \
      0.04855584485714105274, \
      0.04814443257251220341, \
      0.04761604458525019296, \
      0.04697395904661414870, \
      0.04621766751092557684, \
      0.04535110955166067221, \
      0.04437417923925731580, \
      0.04329151496169082935, \
      0.04210333111141810203, \
      0.04081501340035783384, \
      0.03942698871295609976, \
      0.03794545992128481711, \
      0.03637092028663918309, \
      0.03471049818092511427, \
      0.03296454656997632997, \
      0.03114129710406762447, \
      0.02924065319746833770, \
      0.02727225714146838686, \
      0.02523506498175476590, \
      0.02314069493435819848, \
      0.02098627442973743378, \
      0.01878652974179578354, \
      0.01653498765728958965, \
      0.01425206043235199679, \
      0.01192339471421277160, \
      0.00958233879528379039, \
      0.00719269316173611402, \
      0.00483146544879091264, \
      0.00235149067531170332, \
      0.00024420024420024420 \
    ] )

  elif ( n == 129 ):

    x = np.array ( [ \
     -1.00000000000000000000, \
     -0.99969881869620422012, \
     -0.99879545620517239271, \
     -0.99729045667869021614, \
     -0.99518472667219688624, \
     -0.99247953459870999816, \
     -0.98917650996478097345, \
     -0.98527764238894124477, \
     -0.98078528040323044913, \
     -0.97570213003852854446, \
     -0.97003125319454399260, \
     -0.96377606579543986669, \
     -0.95694033573220886494, \
     -0.94952818059303666720, \
     -0.94154406518302077841, \
     -0.93299279883473888771, \
     -0.92387953251128675613, \
     -0.91420975570353065464, \
     -0.90398929312344333159, \
     -0.89322430119551532034, \
     -0.88192126434835502971, \
     -0.87008699110871141865, \
     -0.85772861000027206990, \
     -0.84485356524970707326, \
     -0.83146961230254523708, \
     -0.81758481315158369650, \
     -0.80320753148064490981, \
     -0.78834642762660626201, \
     -0.77301045336273696081, \
     -0.75720884650648454758, \
     -0.74095112535495909118, \
     -0.72424708295146692094, \
     -0.70710678118654752440, \
     -0.68954054473706692462, \
     -0.67155895484701840063, \
     -0.65317284295377676408, \
     -0.63439328416364549822, \
     -0.61523159058062684548, \
     -0.59569930449243334347, \
     -0.57580819141784530075, \
     -0.55557023301960222474, \
     -0.53499761988709721066, \
     -0.51410274419322172659, \
     -0.49289819222978403687, \
     -0.47139673682599764856, \
     -0.44961132965460660005, \
     -0.42755509343028209432, \
     -0.40524131400498987091, \
     -0.38268343236508977173, \
     -0.35989503653498814878, \
     -0.33688985339222005069, \
     -0.31368174039889147666, \
     -0.29028467725446236764, \
     -0.26671275747489838633, \
     -0.24298017990326388995, \
     -0.21910124015686979723, \
     -0.19509032201612826785, \
     -0.17096188876030122636, \
     -0.14673047445536175166, \
     -0.12241067519921619850, \
     -0.098017140329560601994, \
     -0.073564563599667423529, \
     -0.049067674327418014255, \
     -0.024541228522912288032, \
      0.00000000000000000000, \
      0.024541228522912288032, \
      0.049067674327418014255, \
      0.073564563599667423529, \
      0.098017140329560601994, \
      0.12241067519921619850, \
      0.14673047445536175166, \
      0.17096188876030122636, \
      0.19509032201612826785, \
      0.21910124015686979723, \
      0.24298017990326388995, \
      0.26671275747489838633, \
      0.29028467725446236764, \
      0.31368174039889147666, \
      0.33688985339222005069, \
      0.35989503653498814878, \
      0.38268343236508977173, \
      0.40524131400498987091, \
      0.42755509343028209432, \
      0.44961132965460660005, \
      0.47139673682599764856, \
      0.49289819222978403687, \
      0.51410274419322172659, \
      0.53499761988709721066, \
      0.55557023301960222474, \
      0.57580819141784530075, \
      0.59569930449243334347, \
      0.61523159058062684548, \
      0.63439328416364549822, \
      0.65317284295377676408, \
      0.67155895484701840063, \
      0.68954054473706692462, \
      0.70710678118654752440, \
      0.72424708295146692094, \
      0.74095112535495909118, \
      0.75720884650648454758, \
      0.77301045336273696081, \
      0.78834642762660626201, \
      0.80320753148064490981, \
      0.81758481315158369650, \
      0.83146961230254523708, \
      0.84485356524970707326, \
      0.85772861000027206990, \
      0.87008699110871141865, \
      0.88192126434835502971, \
      0.89322430119551532034, \
      0.90398929312344333159, \
      0.91420975570353065464, \
      0.92387953251128675613, \
      0.93299279883473888771, \
      0.94154406518302077841, \
      0.94952818059303666720, \
      0.95694033573220886494, \
      0.96377606579543986669, \
      0.97003125319454399260, \
      0.97570213003852854446, \
      0.98078528040323044913, \
      0.98527764238894124477, \
      0.98917650996478097345, \
      0.99247953459870999816, \
      0.99518472667219688624, \
      0.99729045667869021614, \
      0.99879545620517239271, \
      0.99969881869620422012, \
      1.00000000000000000000 \
    ] )

    w = np.array ( [ \
      0.00006103888176768602, \
      0.00058807215382869754, \
      0.00120930061875273991, \
      0.00180308126695362360, \
      0.00240715327877140915, \
      0.00300345869904497128, \
      0.00360197835812614147, \
      0.00419553798718534675, \
      0.00478862143341336763, \
      0.00537724746840184621, \
      0.00596388034730799521, \
      0.00654590843862298928, \
      0.00712483332325489785, \
      0.00769875778896082811, \
      0.00826865154203087108, \
      0.00883303867470133581, \
      0.00939256583934814871, \
      0.00994602784923457905, \
      0.01049386202576892125, \
      0.01103504877427254184, \
      0.01156988348290849967, \
      0.01209748052807164113, \
      0.01261803597977743271, \
      0.01313076516693974630, \
      0.01363579321293772047, \
      0.01413241437853094133, \
      0.01462070254634350205, \
      0.01510001572479266783, \
      0.01557039073899425960, \
      0.01603123858745057916, \
      0.01648256956220377909, \
      0.01692383985846499368, \
      0.01735504125411394958, \
      0.01777566938875279997, \
      0.01818570377926339481, \
      0.01858467519566908661, \
      0.01897255587067948426, \
      0.01934890842392451844, \
      0.01971370183700155725, \
      0.02006652805198357604, \
      0.02040735612003867863, \
      0.02073580533490147816, \
      0.02105184759002011131, \
      0.02135512797425970725, \
      0.02164562356712882440, \
      0.02192300400598756892, \
      0.02218725355897195088, \
      0.02243806539722630184, \
      0.02267543270456671718, \
      0.02289907134390605882, \
      0.02310898491627407168, \
      0.02330491126131143273, \
      0.02348686571193163505, \
      0.02365460746057766523, \
      0.02380816473024258975, \
      0.02394731750476901502, \
      0.02407210792327850000, \
      0.02418233623893147567, \
      0.02427805942075745923, \
      0.02435909748927643184, \
      0.02442552306156708690, \
      0.02447717542743444284, \
      0.02451414358881568292, \
      0.02453628559651495473, \
      0.02454370750551418263, \
      0.02453628559651495473, \
      0.02451414358881568292, \
      0.02447717542743444284, \
      0.02442552306156708690, \
      0.02435909748927643184, \
      0.02427805942075745923, \
      0.02418233623893147567, \
      0.02407210792327850000, \
      0.02394731750476901502, \
      0.02380816473024258975, \
      0.02365460746057766523, \
      0.02348686571193163505, \
      0.02330491126131143273, \
      0.02310898491627407168, \
      0.02289907134390605882, \
      0.02267543270456671718, \
      0.02243806539722630184, \
      0.02218725355897195088, \
      0.02192300400598756892, \
      0.02164562356712882440, \
      0.02135512797425970725, \
      0.02105184759002011131, \
      0.02073580533490147816, \
      0.02040735612003867863, \
      0.02006652805198357604, \
      0.01971370183700155725, \
      0.01934890842392451844, \
      0.01897255587067948426, \
      0.01858467519566908661, \
      0.01818570377926339481, \
      0.01777566938875279997, \
      0.01735504125411394958, \
      0.01692383985846499368, \
      0.01648256956220377909, \
      0.01603123858745057916, \
      0.01557039073899425960, \
      0.01510001572479266783, \
      0.01462070254634350205, \
      0.01413241437853094133, \
      0.01363579321293772047, \
      0.01313076516693974630, \
      0.01261803597977743271, \
      0.01209748052807164113, \
      0.01156988348290849967, \
      0.01103504877427254184, \
      0.01049386202576892125, \
      0.00994602784923457905, \
      0.00939256583934814871, \
      0.00883303867470133581, \
      0.00826865154203087108, \
      0.00769875778896082811, \
      0.00712483332325489785, \
      0.00654590843862298928, \
      0.00596388034730799521, \
      0.00537724746840184621, \
      0.00478862143341336763, \
      0.00419553798718534675, \
      0.00360197835812614147, \
      0.00300345869904497128, \
      0.00240715327877140915, \
      0.00180308126695362360, \
      0.00120930061875273991, \
      0.00058807215382869754, \
      0.00006103888176768602 \
    ] )

  else:

    print ( '' )
    print ( 'CLENSHAW_CURTIS_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 to 17, 33, 65 or 129.' )
    raise Exception ( 'CLENSHAW_CURTIS_SET(): Fatal error!' )

  return x, w

def clenshaw_curtis_set_test ( ):

#*****************************************************************************80
#
## clenshaw_curtis_set_test() tests clenshaw_curtis_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'clenshaw_curtis_set_test():' )
  print ( '  clenshaw_curtis_set() sets up a Clenshaw Curtis' )
  print ( '  quadrature rule over [-1,1].' )
  print ( '' )
  print ( '     Index       X                       W' )

  for n in range ( 1, 11 ):

    x, w = clenshaw_curtis_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def fejer1_compute ( n ):

#*****************************************************************************80
#
## fejer1_compute() computes a Fejer type 1 quadrature rule.
#
#  Discussion:
#
#    This method uses a direct approach.  The paper by Waldvogel
#    exhibits a more efficient approach using Fourier transforms.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2015
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
#    Walter Gautschi,
#    Numerical Quadrature in the Presence of a Singularity,
#    SIAM Journal on Numerical Analysis,
#    Volume 4, Number 3, 1967, pages 357-362.
#
#    Joerg Waldvogel,
#    Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
#    BIT Numerical Mathematics,
#    Volume 43, Number 1, 2003, pages 1-18.
#
#  Input:
#
#    integer N, the order.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  theta = np.zeros ( n )

  for i in range ( 0, n ):
    theta[i] = float ( 2 * n - 1 - 2 * i ) * np.pi / float ( 2 * n )

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = np.cos ( theta[i] )

  w = np.zeros ( n )

  for i in range ( 0, n ):
    w[i] = 1.0
    jhi = ( n // 2 )
    for j in range ( 0, jhi ):
      angle = 2.0 * float ( j + 1 ) * theta[i]
      w[i] = w[i] - 2.0 * np.cos ( angle ) / float ( 4 * ( j + 1 ) ** 2 - 1 )

  for i in range ( 0, n ):
    w[i] = 2.0 * w[i] / float ( n )

  return x, w

def fejer1_compute_test ( ):

#*****************************************************************************80
#
## fejer1_compute_test() tests fejer1_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'fejer1_compute_test():' )
  print ( '  fejer1_compute() computes the abscissas and weights' )
  print ( '  of a Fejer type 1 quadrature rule.' )
  print ( '' )
  print ( '    Order  W             X' )

  for n in range ( 1, 11 ):

    x, w = fejer1_compute ( n )

    print ( '' )
    print ( '  %8d' % ( n ) )

    for i in range ( 0, n ):
      print ( '            %12g  %12g' % ( w[i], x[i] ) )

  return

def fejer1_set ( n ):

#*****************************************************************************80
#
## fejer1_set() sets abscissas and weights for Fejer type 1 quadrature.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2015
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
#    Walter Gautschi,
#    Numerical Quadrature in the Presence of a Singularity,
#    SIAM Journal on Numerical Analysis,
#    Volume 4, Number 3, 1967, pages 357-362.
#
#    Joerg Waldvogel,
#    Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
#    BIT Numerical Mathematics,
#    Volume 43, Number 1, 2003, pages 1-18.
#
#  Input:
#
#    integer N, the order.
#    N should be between 1 and 10.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
      0.000000000000000 \
    ] )

    w = np.array ( [ \
      2.000000000000000 \
    ] )

  elif ( n == 2 ):

    x = np.array ( [ \
       -0.7071067811865475, \
        0.7071067811865475 \
    ] )

    w = np.array ( [ \
      1.000000000000000, \
      1.000000000000000 \
    ] )

  elif ( n == 3 ):

    x = np.array ( [ \
      -0.8660254037844387, \
       0.0000000000000000, \
       0.8660254037844387 \
    ] )

    w = np.array ( [ \
      0.4444444444444444, \
      1.111111111111111, \
      0.4444444444444444 \
    ] )

  elif ( n == 4 ):

    x = np.array ( [ \
      -0.9238795325112867, \
      -0.3826834323650897, \
       0.3826834323650898, \
       0.9238795325112867 \
    ] )

    w = np.array ( [ \
     0.2642977396044841, \
     0.7357022603955158, \
     0.7357022603955158, \
     0.2642977396044841 \
    ] )

  elif ( n == 5 ):

    x = np.array ( [ \
      -0.9510565162951535, \
      -0.5877852522924730, \
       0.0000000000000000, \
       0.5877852522924731, \
       0.9510565162951535 \
    ] )

    w = np.array ( [ \
      0.1677812284666835, \
      0.5255521048666498, \
      0.6133333333333333, \
      0.5255521048666498, \
      0.1677812284666835 \
    ] )

  elif ( n == 6 ):

    x = np.array ( [ \
       -0.9659258262890682, \
       -0.7071067811865475, \
       -0.2588190451025206, \
        0.2588190451025207, \
        0.7071067811865476, \
        0.9659258262890683 \
    ] )

    w = np.array ( [ \
      0.1186610213812358, \
      0.3777777777777778, \
      0.5035612008409863, \
      0.5035612008409863, \
      0.3777777777777778, \
      0.1186610213812358 \
    ] )

  elif ( n == 7 ):

    x = np.array ( [ \
       -0.9749279121818237, \
       -0.7818314824680295, \
       -0.4338837391175581, \
        0.0000000000000000, \
        0.4338837391175582, \
        0.7818314824680298, \
        0.9749279121818236 \
    ] )

    w = np.array ( [ \
     0.08671618072672234, \
     0.2878313947886919, \
     0.3982415401308441, \
     0.4544217687074830, \
     0.3982415401308441, \
     0.2878313947886919, \
     0.08671618072672234 \
    ] )

  elif ( n == 8 ):

    x = np.array ( [ \
      -0.9807852804032304, \
      -0.8314696123025453, \
      -0.5555702330196020, \
      -0.1950903220161282, \
       0.1950903220161283, \
       0.5555702330196023, \
       0.8314696123025452, \
       0.9807852804032304 \
    ] )

    w = np.array ( [ \
     0.06698294569858981, \
     0.2229879330145788, \
     0.3241525190645244, \
     0.3858766022223071, \
     0.3858766022223071, \
     0.3241525190645244, \
     0.2229879330145788, \
     0.06698294569858981 \
    ] )

  elif ( n == 9 ):

    x = np.array ( [ \
      -0.9848077530122080, \
      -0.8660254037844385, \
      -0.6427876096865394, \
      -0.3420201433256685, \
       0.0000000000000000, \
       0.3420201433256688, \
       0.6427876096865394, \
       0.8660254037844387, \
       0.9848077530122080 \
    ] )

    w = np.array ( [ \
     0.05273664990990676, \
     0.1791887125220458, \
     0.2640372225410044, \
     0.3308451751681364, \
     0.3463844797178130, \
     0.3308451751681364, \
     0.2640372225410044, \
     0.1791887125220458, \
     0.05273664990990676 \
    ] )

  elif ( n == 10 ):

    x = np.array ( [ \
      -0.9876883405951377, \
      -0.8910065241883678, \
      -0.7071067811865475, \
      -0.4539904997395467, \
      -0.1564344650402306, \
       0.1564344650402309, \
       0.4539904997395468, \
       0.7071067811865476, \
       0.8910065241883679, \
       0.9876883405951378 \
    ] )

    w = np.array ( [ \
     0.04293911957413078, \
     0.1458749193773909, \
     0.2203174603174603, \
     0.2808792186638755, \
     0.3099892820671425, \
     0.3099892820671425, \
     0.2808792186638755, \
     0.2203174603174603, \
     0.1458749193773909, \
     0.04293911957413078 \
    ] )

  else:

    print ( '' )
    print ( 'FEJER1_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 through 10.' )
    raise Exception ( 'FEJER1_SET(): Fatal error!' )

  return x, w

def fejer1_set_test ( ):

#*****************************************************************************80
#
## fejer1_set_test() tests fejer1_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'fejer1_set_test():' )
  print ( '  fejer1_set() sets the abscissas and weights' )
  print ( '  of a Fejer type 1 quadrature rule.' )
  print ( '' )
  print ( '    Order  W             X' )

  for n in range ( 1, 11 ):

    x, w = fejer1_set ( n )

    print ( '' )
    print ( '  %8d' % ( n ) )

    for i in range ( 0, n ):
      print ( '            %12g  %12g' % ( w[i], x[i] ) )

  return

def fejer2_compute ( n ):

#*****************************************************************************80
#
## fejer2_compute() computes a Fejer type 2 quadrature rule.
#
#  Discussion:
#
#    This method uses a direct approach.  The paper by Waldvogel
#    exhibits a more efficient approach using Fourier transforms.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2015
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
#    Walter Gautschi,
#    Numerical Quadrature in the Presence of a Singularity,
#    SIAM Journal on Numerical Analysis,
#    Volume 4, Number 3, 1967, pages 357-362.
#
#    Joerg Waldvogel,
#    Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
#    BIT Numerical Mathematics,
#    Volume 43, Number 1, 2003, pages 1-18.
#
#  Input:
#
#    integer N, the order.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ 0.0 ] )
    w = np.array ( [ 2.0 ] )

  elif ( n == 2 ):

    x = np.array ( [ -0.5, +0.5 ] )
    w = np.array ( [  1.0,  1.0 ] )

  else:

    theta = np.zeros ( n )

    for i in range ( 0, n ):
      theta[i] = float ( n - i ) * np.pi / float ( n + 1 )

    x = np.zeros ( n )
    for i in range ( 0, n ):
      x[i] = np.cos ( theta[i] )

    w = np.zeros ( n )

    for i in range ( 0, n ):

      w[i] = 1.0
      jhi = ( ( n - 1 ) // 2 )
      for j in range ( 0, jhi ):
        angle = 2.0 * float ( j + 1 ) * theta[i]
        w[i] = w[i] - 2.0 * np.cos ( angle ) / float ( 4 * ( j + 1 ) ** 2 - 1 )
        p = 2 *  ( ( n + 1 ) // 2 ) - 1

      w[i] = w[i] - np.cos ( float ( p + 1 ) * theta[i] ) / float ( p )

    for i in range ( 0, n ):
      w[i] = 2.0 * w[i] / float ( n + 1 )

  return x, w

def fejer2_compute_test ( ):

#*****************************************************************************80
#
## fejer2_compute_test() tests fejer2_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'fejer2_compute_test():' )
  print ( '  fejer2_compute() computes the abscissas and weights' )
  print ( '  of a Fejer type 2 quadrature rule.' )
  print ( '' )
  print ( '    Order  W             X' )

  for n in range ( 1, 11 ):

    x, w = fejer2_compute ( n )

    print ( '' )
    print ( '  %8d' % ( n ) )

    for i in range ( 0, n ):
      print ( '            %12g  %12g' % ( w[i], x[i] ) )

  return

def fejer2_set ( n ):

#*****************************************************************************80
#
## fejer2_set() sets abscissas and weights for Fejer type 2 quadrature.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2015
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
#    Walter Gautschi,
#    Numerical Quadrature in the Presence of a Singularity,
#    SIAM Journal on Numerical Analysis,
#    Volume 4, Number 3, 1967, pages 357-362.
#
#    Joerg Waldvogel,
#    Fast Construction of the Fejer and Clenshaw-Curtis Quadrature Rules,
#    BIT Numerical Mathematics,
#    Volume 43, Number 1, 2003, pages 1-18.
#
#  Input:
#
#    integer N, the order.
#    N should be between 1 and 10.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
      0.000000000000000 \
    ] )

    w = np.array ( [ \
      2.000000000000000 \
    ] )

  elif ( n == 2 ):

    x = np.array ( [ \
       -0.5000000000000000, \
        0.5000000000000000 \
    ] )

    w = np.array ( [ \
      1.0000000000000000, \
      1.0000000000000000 \
    ] )

  elif ( n == 3 ):

    x = np.array ( [ \
      -0.7071067811865476, \
       0.0000000000000000, \
       0.7071067811865476 \
    ] )

    w = np.array ( [ \
      0.6666666666666666, \
      0.6666666666666666, \
      0.6666666666666666 \
    ] )

  elif ( n == 4 ):

    x = np.array ( [ \
      -0.8090169943749475, \
      -0.3090169943749475, \
       0.3090169943749475, \
       0.8090169943749475 \
    ] )

    w = np.array ( [ \
     0.4254644007500070, \
     0.5745355992499930, \
     0.5745355992499930, \
     0.4254644007500070 \
    ] )

  elif ( n == 5 ):

    x = np.array ( [ \
      -0.8660254037844387, \
      -0.5000000000000000, \
       0.0000000000000000, \
       0.5000000000000000, \
       0.8660254037844387 \
    ] )

    w = np.array ( [ \
     0.3111111111111111, \
     0.4000000000000000, \
     0.5777777777777777, \
     0.4000000000000000, \
     0.3111111111111111 \
    ] )

  elif ( n == 6 ):

    x = np.array ( [ \
      -0.9009688679024191, \
      -0.6234898018587336, \
      -0.2225209339563144, \
       0.2225209339563144, \
       0.6234898018587336, \
       0.9009688679024191 \
    ] )

    w = np.array ( [ \
     0.2269152467244296, \
     0.3267938603769863, \
     0.4462908928985841, \
     0.4462908928985841, \
     0.3267938603769863, \
     0.2269152467244296 \
    ] )

  elif ( n == 7 ):

    x = np.array ( [ \
      -0.9238795325112867, \
      -0.7071067811865476, \
      -0.3826834323650898, \
       0.0000000000000000, \
       0.3826834323650898, \
       0.7071067811865476, \
       0.9238795325112867 \
    ] )

    w = np.array ( [ \
     0.1779646809620499, \
     0.2476190476190476, \
     0.3934638904665215, \
     0.3619047619047619, \
     0.3934638904665215, \
     0.2476190476190476, \
     0.1779646809620499 \
    ] )

  elif ( n == 8 ):

    x = np.array ( [ \
      -0.9396926207859084, \
      -0.7660444431189780, \
      -0.5000000000000000, \
      -0.1736481776669304, \
       0.1736481776669304, \
       0.5000000000000000, \
       0.7660444431189780, \
       0.9396926207859084 \
    ] )

    w = np.array ( [ \
     0.1397697435050225, \
     0.2063696457302284, \
     0.3142857142857143, \
     0.3395748964790348, \
     0.3395748964790348, \
     0.3142857142857143, \
     0.2063696457302284, \
     0.1397697435050225 \
    ] )

  elif ( n == 9 ):

    x = np.array ( [ \
      -0.9510565162951535, \
      -0.8090169943749475, \
      -0.5877852522924731, \
      -0.3090169943749475, \
       0.0000000000000000, \
       0.3090169943749475, \
       0.5877852522924731, \
       0.8090169943749475, \
       0.9510565162951535 \
    ] )

    w = np.array ( [ \
     0.1147810750857217, \
     0.1654331942222276, \
     0.2737903534857068, \
     0.2790112502222170, \
     0.3339682539682539, \
     0.2790112502222170, \
     0.2737903534857068, \
     0.1654331942222276, \
     0.1147810750857217 \
    ] )

  elif ( n == 10 ):

    x = np.array ( [ \
      -0.9594929736144974, \
      -0.8412535328311812, \
      -0.6548607339452851, \
      -0.4154150130018864, \
      -0.1423148382732851, \
       0.1423148382732851, \
       0.4154150130018864, \
       0.6548607339452851, \
       0.8412535328311812, \
       0.9594929736144974 \
    ] )

    w = np.array ( [ \
     0.09441954173982806, \
     0.1411354380109716, \
     0.2263866903636005, \
     0.2530509772156453, \
     0.2850073526699544, \
     0.2850073526699544, \
     0.2530509772156453, \
     0.2263866903636005, \
     0.1411354380109716, \
     0.09441954173982806 \
    ] )

  else:

    print ( '' )
    print ( 'FEJER2_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 through 10.' )
    raise Exception ( 'FEJER2_SET(): Fatal error!' )

  return x, w

def fejer2_set_test ( ):

#*****************************************************************************80
#
## fejer2_set_test() tests fejer2_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'fejer2_set_test():' )
  print ( '  fejer2_set() sets the abscissas and weights' )
  print ( '  of a Fejer type 2 quadrature rule.' )
  print ( '' )
  print ( '    Order  W             X' )

  for n in range ( 1, 11 ):

    x, w = fejer2_set ( n )

    print ( '' )
    print ( '  %8d' % ( n ) )

    for i in range ( 0, n ):
      print ( '            %12g  %12g' % ( w[i], x[i] ) )

  return

def gegenbauer_integral ( expon, alpha ):

#*****************************************************************************80
#
## gegenbauer_integral() integrates a monomial with Gegenbauer weight.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= +1 ) x^EXPON (1-x^2)^ALPHA dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#
#    real ALPHA, the exponent of (1-X^2) in the weight factor.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import gamma

  if ( ( expon % 2 ) == 1 ):
    value = 0.0
    return value

  c = expon

  arg1 = - alpha
  arg2 =   1.0 + c
  arg3 =   2.0 + alpha + c
  arg4 = - 1.0

  value1 = r8_hyper_2f1 ( arg1, arg2, arg3, arg4 )

  value = 2.0 * gamma ( 1.0 + c ) * gamma ( 1.0 + alpha ) \
    * value1 / gamma ( 2.0 + alpha  + c )

  return value

def gegenbauer_integral_test ( ):

#*****************************************************************************80
#
## gegenbauer_integral_test() tests gegenbauer_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  alpha = 0.25

  print ( '' )
  print ( 'gegenbauer_integral_test():' )
  print ( '  gegenbauer_integral() evaluates' )
  print ( '  Integral ( -1 < x < +1 ) x^n * (1-x*x)^alpha dx' )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = gegenbauer_integral ( n, alpha )

    print ( '  %8d  %24.16g' % ( n, value ) )

  return

def gegenbauer_ss_compute ( n, alpha ):

#*****************************************************************************80
#
## gegenbauer_ss_compute() computes a Gauss-Gegenbauer quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) (1-X^2)^ALPHA * F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    Thanks to Janiki Raman for pointing out a problem in an earlier
#    version of the code that occurred when ALPHA was -0.5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    Original FORTRAN77 version by Arthur Stroud, Don Secrest.
#    This version by John Burkardt.
#
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    integer N, the order.
#
#    real ALPHA, the exponent of (1-X^2) in the weight.  
#    -1.0 < ALPHA is required.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np
  from scipy.special import gamma
#
#  Check N.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'GEGENBAUER_SS_COMPUTE(): Fatal error!' )
    print ( '  1 <= N is required.' )
    raise Exception ( 'GEGENBAUER_SS_COMPUTE(): Fatal error!' )
#
#  Check ALPHA.
#
  if ( alpha <= -1.0 ):
    print ( '' )
    print ( 'GEGENBAUER_SS_COMPUTE(): Fatal error!' )
    print ( '  -1.0 < ALPHA is required.' )
    raise Exception ( 'GEGENBAUER_SS_COMPUTE(): Fatal error!' )

  x = np.zeros ( n )
  w = np.zeros ( n )
#
#  Set the recursion coefficients.
#
  c = np.zeros ( n )

  c[0] = 0.0;
  if ( 2 <= n ):
    c[1] = 1.0 / ( 2.0 * alpha + 3.0 )

  for i in range ( 2, n ):

    c[i] = float ( i ) \
      * ( alpha + alpha + i ) / \
      ( ( alpha + alpha + 2 * i + 1 ) \
      * ( alpha + alpha + 2 * i - 1 ) )

  delta = gamma ( alpha         + 1.0 ) \
        * gamma (         alpha + 1.0 ) \
        / gamma ( alpha + alpha + 2.0 )

  c_product = 1.0
  for i in range ( 1, n ):
    c_product = c_product * c[i]

  cc = delta * 2.0 ** ( 2.0 * alpha + 1.0 ) * c_product

  for i in range ( 0, n ):

    if ( i == 0 ):

      an = alpha / float ( n )

      r1 = ( 1.0 + alpha ) * ( 2.78 / ( 4.0 + n * n ) + 0.768 * an / n )

      r2 = 1.0 + 2.44 * an + 1.281 * an ** 2

      xval = ( r2 - r1 ) / r2

    elif ( i == 1 ):

      r1 = ( 4.1 + alpha ) / ( ( 1.0 + alpha ) * ( 1.0 + 0.156 * alpha ) )

      r2 = 1.0 + 0.06 * ( n - 8.0 ) * ( 1.0 + 0.12 * alpha ) / n

      r3 = 1.0 + 0.012 * alpha * ( 1.0 + 0.25 * abs ( alpha ) ) / n

      xval = xval - r1 * r2 * r3 * ( 1.0 - xval )

    elif ( i == 2 ):

      r1 = ( 1.67 + 0.28 * alpha ) / ( 1.0 + 0.37 * alpha )

      r2 = 1.0 + 0.22 * ( n - 8.0 ) / n

      r3 = 1.0 + 8.0 * alpha / ( ( 6.28 + alpha ) * n * n )

      xval = xval - r1 * r2 * r3 * ( x[0] - xval )

    elif ( i < n - 2 ):

      xval = 3.0 * x[i-1] - 3.0 * x[i-2] + x[i-3]

    elif ( i == n - 2 ):

      r1 = ( 1.0 + 0.235 * alpha ) / ( 0.766 + 0.119 * alpha )

      r2 = 1.0 / ( 1.0 + 0.639 * ( n - 4.0 ) / ( 1.0 + 0.71 * ( n - 4.0 ) ) )

      r3 = 1.0 / ( 1.0 + 20.0 * alpha / ( ( 7.5 + alpha ) * n * n ) )

      xval = xval + r1 * r2 * r3 * ( xval - x[i-2] )

    elif ( i == n - 1 ):

      r1 = ( 1.0 + 0.37 * alpha ) / ( 1.67 + 0.28 * alpha )

      r2 = 1.0 / ( 1.0 + 0.22 * ( n - 8.0 ) / n )

      r3 = 1.0 / ( 1.0 + 8.0 * alpha / ( ( 6.28 + alpha ) * n * n ) )

      xval = xval + r1 * r2 * r3 * ( xval - x[i-2] )

    xval, dp2, p1 = gegenbauer_ss_root ( xval, n, alpha, c )
 
    x[i] = xval
    w[i] = cc / ( dp2 * p1 )
#
#  Reverse the order of the values.
#
  x = r8vec_reverse ( n, x );
  w = r8vec_reverse ( n, w );

  return x, w

def gegenbauer_ss_recur ( x, n, alpha, c ):

#*****************************************************************************80
#
## gegenbauer_ss_recur(): value and derivative of a Gegenbauer polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    Original FORTRAN77 version by Arthur Stroud, Don Secrest,
#    This version by John Burkardt,
#
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    real X, the point at which polynomials are evaluated.
#
#    integer N, the order of the polynomial to be computed.
#
#    real ALPHA, the exponent of (1-X^2) in the quadrature rule.
#
#    real C(N), the recursion coefficients.
#
#  Output:
#
#    real P2, the value of J(N)(X).
#
#    real DP2, the value of J'(N)(X).
#
#    real P1, the value of J(N-1)(X).
#
  p1 = 1.0
  dp1 = 0.0

  p2 = x
  dp2 = 1.0

  for i in range ( 1, n ):

    p0 = p1
    dp0 = dp1

    p1 = p2
    dp1 = dp2

    p2 = x * p1 - c[i] * p0
    dp2 = x * dp1 + p1 - c[i] * dp0

  return p2, dp2, p1

def gegenbauer_ss_root ( x, n, alpha, c ):

#*****************************************************************************80
#
## gegenbauer_ss_root() improves an approximate root of a Gegenbauer polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    real X, the approximate root.
#
#    integer N, the order of the polynomial to be computed.
#
#    real ALPHA, the exponent of (1-X^2) in the quadrature rule.
#
#    real C(N), the recursion coefficients.
#
#  Output:
#
#    real X, the improved approximate root.
#
#    real DP2, the value of J'(N)(X).
#
#    real P1, the value of J(N-1)(X).
#
  maxstep = 10
  eps = 2.220446049250313E-016

  for i in range ( 0, maxstep ):

    p2, dp2, p1 = gegenbauer_ss_recur ( x, n, alpha, c )

    d = p2 / dp2
    x = x - d

    if ( abs ( d ) <= eps * ( abs ( x ) + 1.0 ) ):
      break

  return x, dp2, p1

def gegenbauer_ss_compute_test ( ):

#*****************************************************************************80
#
## gegenbauer_ss_compute_test() compares gegenbauer_ss_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  alpha = 0.5

  print ( '' )
  print ( 'gegenbauer_ss_compute_test():' )
  print ( '  gegenbauer_ss_compute() computes Gauss-Gegenbauer rules;' )
  print ( '' )
  print ( '  Abscissas and weights for a generalized Gauss Gegenbauer rule' )
  print ( '  with ALPHA = %g' % ( alpha ) )
  print ( '' )
  print ( '   #                         W                         X' )
  print ( '' )

  for n in range ( 1, 11 ):

    x, w = gegenbauer_ss_compute ( n, alpha )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, w[i], x[i] ) )

  return

def gen_hermite_ek_compute ( n, alpha ):

#*****************************************************************************80
#
## gen_hermite_ek_compute(): generalized Gauss-Hermite, Elhay-Kautsky method.
#
#  Discussion:
#
#    The code uses an algorithm by Elhay and Kautsky.
#
#    The integral:
#
#      integral ( -oo < x < +oo ) |x|^alpha exp ( -x^2 ) * f(x) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#  Input:
#
#    integer N, the number of abscissas.
#
#    real ALPHA, the parameter.
#    -1.0 < ALPHA.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  from scipy.special import gamma
#
#  Define the zero-th moment.
#
  arg = ( alpha + 1.0 ) / 2.0
  zemu = gamma ( arg )
#
#  Define the Jacobi matrix.
#
  bj = np.zeros ( n )
  for i in range ( 0, n ):
    if ( ( i % 2 ) == 0 ):
      bj[i] = ( float ( i + 1 ) + alpha ) / 2.0
    else:
      bj[i] =   float ( i + 1 ) / 2.0
    bj[i] = np.sqrt ( bj[i] )

  x = np.zeros ( n )

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )
#
#  If N is odd, force the center X to be exactly 0.
#
  if ( ( n % 2 ) == 1 ):
    x[(n-1)//2] = 0.0

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return x, w

def gen_hermite_ek_compute_test ( ):

#*****************************************************************************80
#
## gen_hermite_ek_compute_test() tests gen_hermite_ek_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
  alpha = 0.5

  print ( '' )
  print ( 'gen_hermite_ek_compute_test():' )
  print ( '  gen_hermite_ek_compute() computes' )
  print ( '  a generalized Hermite quadrature rule' )
  print ( '  using the Elhay-Kautsky algorithm.' )
  print ( '' )
  print ( '  Using ALPHA = %g' % ( alpha ) )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = gen_hermite_ek_compute ( n, alpha )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def gen_hermite_integral ( expon, alpha ):

#*****************************************************************************80
#
## gen_hermite_integral() evaluates a monomial generalized Hermite integral.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -oo < x < +oo ) x^n |x|^alpha exp(-x^2) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    int EXPON, the exponent of the monomial.
#
#    real ALPHA, the exponent of |X| in the integral.
#    -1.0 < ALPHA.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import gamma

  if ( ( expon % 2 ) == 1 ):

    value = 0.0

  else:

    a = alpha + float ( expon )

    if ( a <= -1.0 ):

      value = - np.finfo(float).max

    else:

      arg = ( a + 1.0 ) / 2.0
      value = gamma ( arg )

  return value

def gen_hermite_integral_test ( ):

#*****************************************************************************80
#
## gen_hermite_integral_test() tests gen_hermite_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  alpha = 0.5

  print ( '' )
  print ( 'gen_hermite_integral_test():' )
  print ( '  gen_hermite_integral() evaluates' )
  print ( '  Integral ( -oo < x < +oo ) exp(-x^2) x^n |x|^alpha dx' )
  print ( '' )
  print ( '  Use ALPHA = %g' % ( alpha ) )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = gen_hermite_integral ( n, alpha )

    print ( '  %8d  %24.16g' % ( n, value ) )

  return

def gen_laguerre_ek_compute ( n, alpha ):

#*****************************************************************************80
#
## gen_laguerre_ek_compute(): generalized Gauss-Laguerre, Elhay-Kautsky method.
#
#  Discussion:
#
#    The integral:
#
#      integral ( 0 < x < +oo ) x^alpha exp ( -x ) * f(x) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#  Input:
#
#    integer N, the number of abscissas.
#
#    real ALPHA, the parameter.
#    0.0 < ALPHA.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np
  from scipy.special import gamma
#
#  Define the zero-th moment.
#
  arg = alpha + 1.0
  zemu = gamma ( arg )
#
#  Define the Jacobi matrix.
#
  bj = np.zeros ( n )
  for i in range ( 0, n ):
    ip1_r8 = float ( i + 1 )
    bj[i] = np.sqrt ( ip1_r8 * ( ip1_r8 + alpha ) )

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( 2 * i + 1 ) + alpha

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return x, w

def gen_laguerre_ek_compute_test ( ):

#*****************************************************************************80
#
## gen_laguerre_ek_compute_test() tests gen_laguerre_ek_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
  alpha = 0.5

  print ( '' )
  print ( 'gen_laguerre_ek_compute_test():' )
  print ( '  gen_laguerre_ek_compute() computes' )
  print ( '  a generalized Laguerre quadrature rule' )
  print ( '  using the Elhay-Kautsky algorithm.' )
  print ( '' )
  print ( '  Using ALPHA = %g' % ( alpha ) )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = gen_laguerre_ek_compute ( n, alpha )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def gen_laguerre_integral ( expon, alpha ):

#*****************************************************************************80
#
## gen_laguerre_integral() evaluates a monomial generalized Laguerre integral.
#
#  Discussion:
#
#    The integral:
#
#      integral ( 0 <= x < +oo ) x^n * x^alpha * exp ( -x ) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#    0 <= EXPON.
#
#    real ALPHA, the exponent of X in the weight function.
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  from scipy.special import gamma

  arg = alpha + float ( expon + 1 )

  exact = gamma ( arg )
 
  return exact

def gen_laguerre_integral_test ( ):

#*****************************************************************************80
#
## gen_laguerre_integral_test() tests gen_laguerre_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  alpha = 0.5

  print ( '' )
  print ( 'gen_laguerre_integral_test():' )
  print ( '  gen_laguerre_integral() evaluates' )
  print ( '  Integral ( 0 < x < +oo ) exp(-x) x^n x^alpha dx' )
  print ( '' )
  print ( '  Use ALPHA = %g' % ( alpha ) )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = gen_laguerre_integral ( n, alpha )

    print ( '  %8d  %24.16g' % ( n, value ) )

  return

def hermite_1_set ( n ):

#*****************************************************************************80
#
## hermite_1_set() sets abscissas and weights for Hermite quadrature.
#
#  Discussion:
#
#    This routine is for the case with unit density:
#      integral ( -oo < x < +oo ) f(x) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order.
#    N must be between 1 and 10.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
           0.0 ] )

    w = np.array ( [ \
           1.7724538509055161 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
           - 0.707106781186547524400844362105, \
             0.707106781186547524400844362105 ] )

    w = np.array ( [ \
           1.4611411826611391, \
           1.4611411826611391 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
           - 1.22474487139158904909864203735, \
             0.0, \
             1.22474487139158904909864203735 ] )

    w = np.array ( [ \
           1.3239311752136438, \
           1.1816359006036774, \
           1.3239311752136438 ] )

  elif ( n == 4 ):

    x = np.array ( [ \
           - 1.65068012388578455588334111112, \
           - 0.524647623275290317884060253835, \
             0.524647623275290317884060253835, \
             1.65068012388578455588334111112 ] )

    w = np.array ( [ \
           1.2402258176958150, \
           1.0599644828949693, \
           1.0599644828949693, \
           1.2402258176958150 ] )

  elif ( n == 5 ):

    x = np.array ( [ \
           - 2.02018287045608563292872408814, \
           - 0.958572464613818507112770593893, \
             0.0, \
             0.958572464613818507112770593893, \
             2.02018287045608563292872408814 ] )

    w = np.array ( [ \
           1.1814886255359869, \
           0.98658099675142830, \
           0.94530872048294190, \
           0.98658099675142830, \
           1.1814886255359869 ] )

  elif ( n == 6 ):

    x = np.array ( [ \
           - 2.35060497367449222283392198706, \
           - 1.33584907401369694971489528297, \
           - 0.436077411927616508679215948251, \
             0.436077411927616508679215948251, \
             1.33584907401369694971489528297, \
             2.35060497367449222283392198706 ] )

    w = np.array ( [ \
           1.1369083326745253, \
           0.93558055763118075, \
           0.87640133443623058, \
           0.87640133443623058, \
           0.93558055763118075, \
           1.1369083326745253 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
           - 2.65196135683523349244708200652, \
           - 1.67355162876747144503180139830, \
           - 0.816287882858964663038710959027, \
             0.0, \
             0.816287882858964663038710959027, \
             1.67355162876747144503180139830, \
             2.65196135683523349244708200652 ] )

    w = np.array ( [ \
           1.1013307296103216, \
           0.89718460022518409, \
           0.82868730328363926, \
           0.81026461755680734, \
           0.82868730328363926, \
           0.89718460022518409, \
           1.1013307296103216 ] )

  elif ( n == 8 ):

    x = np.array ( [ \
           - 2.93063742025724401922350270524, \
           - 1.98165675669584292585463063977, \
           - 1.15719371244678019472076577906, \
           - 0.381186990207322116854718885584, \
             0.381186990207322116854718885584, \
             1.15719371244678019472076577906, \
             1.98165675669584292585463063977, \
             2.93063742025724401922350270524 ] )

    w = np.array ( [ \
           1.0719301442479805, \
           0.86675260656338138, \
           0.79289004838640131, \
           0.76454412865172916, \
           0.76454412865172916, \
           0.79289004838640131, \
           0.86675260656338138, \
           1.0719301442479805 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
           - 3.19099320178152760723004779538, \
           - 2.26658058453184311180209693284, \
           - 1.46855328921666793166701573925, \
           - 0.723551018752837573322639864579, \
             0.0, \
             0.723551018752837573322639864579, \
             1.46855328921666793166701573925, \
             2.26658058453184311180209693284, \
             3.19099320178152760723004779538 ] )

    w = np.array ( [ \
           1.0470035809766838, \
           0.84175270147867043, \
           0.76460812509455023, \
           0.73030245274509220, \
           0.72023521560605097, \
           0.73030245274509220, \
           0.76460812509455023, \
           0.84175270147867043, \
           1.0470035809766838 ] )

  elif ( n == 10 ):

    x = np.array ( [ \
            - 3.43615911883773760332672549432, \
            - 2.53273167423278979640896079775, \
            - 1.75668364929988177345140122011, \
            - 1.03661082978951365417749191676, \
            - 0.342901327223704608789165025557, \
              0.342901327223704608789165025557, \
              1.03661082978951365417749191676, \
              1.75668364929988177345140122011, \
              2.53273167423278979640896079775, \
              3.43615911883773760332672549432 ] )

    w = np.array ( [ \
           1.0254516913657352, \
           0.82066612640481640, \
           0.74144193194356511, \
           0.70329632310490608, \
           0.68708185395127341, \
           0.68708185395127341, \
           0.70329632310490608, \
           0.74144193194356511, \
           0.82066612640481640, \
            1.0254516913657352 ] )
    
  else:

    print ( '' )
    print ( 'HERMITE_1_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 to 10.' )
    raise Exception ( 'HERMITE_1_SET(): Fatal error!' )

  return x, w

def hermite_1_set_test ( ):

#*****************************************************************************80
#
## hermite_1_set_test() tests hermite_1_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_1_set_test():' )
  print ( '  hermite_1_set() sets a unit density Hermite quadrature rule.' )
  print ( '  The interval is (-oo,+oo).' )
  print ( '  The density is 1.0.' )

  print ( '' )
  print ( '  Index       X             W' )
  print ( '' )

  for n in range ( 1, 11 ):

    x, w = hermite_1_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def hermite_ek_compute ( n ):

#*****************************************************************************80
#
## hermite_ek_compute() computes a Gauss-Hermite quadrature rule.
#
#  Discussion:
#
#    The code uses an algorithm by Elhay and Kautsky.
#
#    The abscissas are the zeros of the N-th order Hermite polynomial.
#
#    The integral:
#
#      integral ( -oo < x < +oo ) exp ( - x * x ) * f(x) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#  Input:
#
#    integer N, the number of abscissas.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np
  from scipy.special import gamma
#
#  Define the zero-th moment.
#
  zemu = gamma ( 0.5 )
#
#  Define the Jacobi matrix.
#
  bj = np.zeros ( n )
  for i in range ( 0, n ):
    bj[i] = np.sqrt ( float ( i + 1 ) / 2.0 )

  x = np.zeros ( n )

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )
#
#  If N is odd, force the center X to be exactly 0.
#
  if ( ( n % 2 ) == 1 ):
    x[(n-1)//2] = 0.0

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return x, w

def hermite_ek_compute_test ( ):

#*****************************************************************************80
#
## hermite_ek_compute_test() tests hermite_ek_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_ek_compute_test():' )
  print ( '  hermite_ek_compute() computes a Hermite quadrature rule' )
  print ( '  using the Elhay-Kautsky algorithm.' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = hermite_ek_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def hermite_gk16_set ( n ):

#*****************************************************************************80
#
## hermite_gk16_set() sets a Hermite Genz-Keister 16 rule.
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
#    This code is distributed under the MIT license. 
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
#  Input:
#
#    integer N, the order.
#    N must be 1, 3, 7, 9, 17, 19, 31, 33 or 35.
#
#  Output:
#
#    real X(N,1), the abscissas.
#
#    real W(N,1), the weights.
#
  import numpy as np

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
    print ( 'HERMITE_GK16_SET(): Fatal error!' )
    print ( '  Illegal input value of N.' )
    print ( '  N must be 1, 3, 7, 9, 17, 19, 31, 33 or 35.' )
    raise Exception ( 'HERMITE_GK16_SET(): Fatal error!' )

  return x, w

def hermite_gk16_set_test ( ):

#*****************************************************************************80
#
## hermite_gk16_set_test() tests hermite_gk16_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
 
  l_max = 8

  n_list = np.array ( [ 1, 3, 7, 9, 17, 19, 31, 33, 35 ] )

  print ( '' )
  print ( 'hermite_gk16_set_test():' )
  print ( '  hermite_gk16_set() sets up a nested rule' )
  print ( '  for the Hermite integration problem.' )
  print ( '' )
  print ( '  Index       X             W' )

  for l in range ( 0, l_max + 1 ):

    n = n_list[l]

    x, w = hermite_gk16_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def hermite_gk18_set ( n ):

#*****************************************************************************80
#
## hermite_gk18_set() sets a Hermite Genz-Keister 18 rule.
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
#    This code is distributed under the MIT license. 
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
#  Input:
#
#    integer N, the order.
#    N must be 1, 3, 9, 19, or 37.
#
#  Output:
#
#    real X(N,1), the abscissas.
#
#    real W(N,1), the weights.
#
  import numpy as np

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
    print ( 'HERMITE_GK18_SET(): Fatal error!' )
    print ( '  Illegal input value of N.' )
    print ( '  N must be 1, 3, 9, 19, or 37.' )
    raise Exception ( 'HERMITE_GK18_SET(): Fatal error!' )

  return x, w

def hermite_gk18_set_test ( ):

#*****************************************************************************80
#
## hermite_gk18_set_test() tests hermite_gk18_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  l_max = 4

  n_list = np.array ( [ 1, 3, 9, 19, 37 ] )

  print ( '' )
  print ( 'hermite_gk18_set_test():' )
  print ( '  hermite_gk18_set() sets up a nested rule' )
  print ( '  for the Hermite integration problem.' )
  print ( '' )
  print ( '  Index       X             W' )

  for l in range ( 0, l_max + 1 ):

    n = n_list[l]

    x, w = hermite_gk18_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def hermite_gk22_set ( n ):

#*****************************************************************************80
#
## hermite_gk22_set() sets a Genz-Keister 22 Hermite rule.
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
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N, the order.
#    Legal values are 1, 3, 9, 19, and 41.
#
#  Output:
#
#    real X(N,1), the abscissas.
#
#    real W(N,1), the weights.
#
  import numpy as np

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
    print ( 'HERMITE_GK22_SET(): Fatal error!' )
    print ( '  Illegal input value of N.' )
    print ( '  N must be 1, 3, 9, 19, or 41.' )
    raise Exception ( 'HERMITE_GK22_SET(): Fatal error!' )

  return x, w

def hermite_gk22_set_test ( ):

#*****************************************************************************80
#
## hermite_gk22_set_test() tests hermite_gk22_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  l_max = 4

  n_list = np.array ( [ 1, 3, 9, 19, 41 ] )

  print ( '' )
  print ( 'hermite_gk22_set_test():' )
  print ( '  hermite_gk22_set() sets up a nested rule' )
  print ( '  for the Hermite integration problem.' )
  print ( '' )
  print ( '  Index       X             W' )

  for l in range ( 0, l_max + 1 ):

    n = n_list[l]

    x, w = hermite_gk22_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def hermite_gk24_set ( n ):

#*****************************************************************************80
#
## hermite_gk24_set() sets a Genz-Keister 24 Hermite rule.
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
#    family was denoted by 1+2+6+10+24, that is, it comprised rules
#    of successive orders O = 1, 3, 9, 19, and 43.
#
#    The precisions of these rules are P = 1, 5, 15, 29, and 67.
#
#    Some of the data in this function was kindly supplied directly by
#    Alan Genz on 24 April 2011.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N, the order.
#    Legal values are 1, 3, 9, 19, and 43.
#
#  Output:
#
#    real X(N,1), the abscissas.
#
#    real W(N,1), the weights.
#
  import numpy as np

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

  elif ( n == 43 ):

    x = np.array ( [ \
            -10.167574994881873, \
             -7.231746029072501, \
             -6.535398426382995, \
             -5.954781975039809, \
             -5.434053000365068, \
             -4.952329763008589, \
             -4.4995993983103881, \
             -4.071335874253583, \
             -3.6677742159463378, \
             -3.295265921534226, \
             -2.9592107790638380, \
             -2.633356763661946, \
             -2.2665132620567876, \
             -2.089340389294661, \
             -2.0232301911005157, \
             -1.8357079751751868, \
             -1.583643465293944, \
             -1.2247448713915889, \
             -0.87004089535290285, \
             -0.52403354748695763, \
             -0.196029453662011, \
              0.0000000000000000, \
              0.196029453662011, \
              0.52403354748695763, \
              0.87004089535290285, \
              1.2247448713915889, \
              1.583643465293944, \
              1.8357079751751868, \
              2.0232301911005157, \
              2.089340389294661, \
              2.2665132620567876, \
              2.633356763661946, \
              2.9592107790638380, \
              3.295265921534226, \
              3.6677742159463378, \
              4.071335874253583, \
              4.4995993983103881, \
              4.952329763008589, \
              5.434053000365068, \
              5.954781975039809, \
              6.535398426382995, \
              7.231746029072501, \
             10.167574994881873 ] )

    w = np.array ( [ \
              0.546191947478318097E-37, \
              0.87544909871323873E-23, \
              0.992619971560149097E-19, \
              0.122619614947864357E-15, \
              0.421921851448196032E-13, \
              0.586915885251734856E-11, \
              0.400030575425776948E-09, \
              0.148653643571796457E-07, \
              0.316018363221289247E-06, \
              0.383880761947398577E-05, \
              0.286802318064777813E-04, \
              0.184789465688357423E-03, \
              0.150909333211638847E-02, \
            - 0.38799558623877157E-02, \
              0.67354758901013295E-02, \
              0.139966252291568061E-02, \
              0.163616873493832402E-01, \
              0.450612329041864976E-01, \
              0.928711584442575456E-01, \
              0.145863292632147353E+00, \
              0.164880913687436689E+00, \
              0.579595986101181095E-01, \
              0.164880913687436689E+00, \
              0.145863292632147353E+00, \
              0.928711584442575456E-01, \
              0.450612329041864976E-01, \
              0.163616873493832402E-01, \
              0.139966252291568061E-02, \
              0.67354758901013295E-02, \
            - 0.38799558623877157E-02, \
              0.150909333211638847E-02, \
              0.184789465688357423E-03, \
              0.286802318064777813E-04, \
              0.383880761947398577E-05, \
              0.316018363221289247E-06, \
              0.148653643571796457E-07, \
              0.400030575425776948E-09, \
              0.586915885251734856E-11, \
              0.421921851448196032E-13, \
              0.122619614947864357E-15, \
              0.992619971560149097E-19, \
              0.87544909871323873E-23, \
              0.546191947478318097E-37 ] )

  else:

    print ( '' )
    print ( 'HERMITE_GK24_SET(): Fatal error!' )
    print ( '  Illegal input value of N.' )
    print ( '  N must be 1, 3, 9, 19, or 43.' )
    raise Exception ( 'HERMITE_GK24_SET(): Fatal error!' )

  return x, w

def hermite_gk24_set_test ( ):

#*****************************************************************************80
#
## hermite_gk24_set_test() tests hermite_gk24_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  l_max = 4

  n_list = np.array ( [ 1, 3, 9, 19, 43 ] )

  print ( '' )
  print ( 'hermite_gk24_set_test():' )
  print ( '  hermite_gk24_set() sets up a nested rule' )
  print ( '  for the Hermite integration problem.' )
  print ( '' )
  print ( '  Index       X             W' )

  for l in range ( 0, l_max + 1 ):

    n = n_list[l]

    x, w = hermite_gk24_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def hermite_integral ( n ):

#*****************************************************************************80
#
## hermite_integral() evaluates a monomial Hermite integral.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -oo < x < +oo ) x^n exp(-x^2) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the integral.
#    0 <= N.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import factorial2
  import numpy as np

  if ( n < 0 ):

    value = - np.finfo(float).max

  elif ( ( n % 2 ) == 1 ):

    value = 0.0

  else:

    value = factorial2 ( n - 1 ) * np.sqrt ( np.pi ) / 2.0 ** ( n // 2 )

  return value

def hermite_integral_test ( ):

#*****************************************************************************80
#
## hermite_integral_test() tests hermite_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_integral_test():' )
  print ( '  hermite_integral() evaluates' )
  print ( '  Integral ( -oo < x < +oo ) exp(-x^2) x^m dx' )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = hermite_integral ( n )

    print ( '  %8d  %24.16g' % ( n, value ) )

  return

def hermite_probabilist_set ( n ):

#*****************************************************************************80
#
## hermite_probabilist_set(): probabilist Hermite quadrature.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -oo < x < +oo ) f(x) * rho(x) dx
#
#    The weight:
#
#      rho(x) = exp ( - x * x / 2 ) / sqrt ( 2 * pi ) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2015
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
#    integer N, the order.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
           0.0 ] )

    w = np.array ( [ \
           1.00000000000000000000000000000 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
           -1.00000000000000000000000000000, \
           +1.00000000000000000000000000000 ] )

    w = np.array ( [ \
           0.50000000000000000000000000000, \
           0.50000000000000000000000000000 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
           -1.73205080756887729352744634151, \
            0.0, \
           +1.73205080756887729352744634151 ] )

    w = np.array ( [ \
           0.166666666666666666666666666667, \
           0.666666666666666666666666666667, \
           0.166666666666666666666666666667 ] )

  elif ( n == 4 ):

    x = np.array ( [ \
           -2.33441421833897723931751226721, \
           -0.741963784302725857648513596726, \
           +0.741963784302725857648513596726, \
           +2.33441421833897723931751226721 ] )

    w = np.array ( [ \
           0.0458758547680684918168929937745, \
           0.454124145231931508183107006225, \
           0.454124145231931508183107006225, \
           0.0458758547680684918168929937745 ] )

  elif ( n == 5 ):

    x = np.array ( [ \
           -2.85697001387280565416230426401, \
           -1.35562617997426586583052129087, \
            0.0, \
           +1.35562617997426586583052129087, \
           +2.85697001387280565416230426401 ] )

    w = np.array ( [ \
           0.0112574113277206889333702151856, \
           0.222075922005612644399963118148, \
           0.533333333333333333333333333333, \
           0.222075922005612644399963118148, \
           0.0112574113277206889333702151856 ] )

  elif ( n == 6 ):

    x = np.array ( [ \
           -3.32425743355211895236183546247, \
           -1.88917587775371067550566789858, \
           -0.616706590192594152193686099399, \
           +0.616706590192594152193686099399, \
           +1.88917587775371067550566789858, \
           +3.32425743355211895236183546247 ] )

    w = np.array ( [ \
           0.00255578440205624643060629074383, \
           0.0886157460419145274808558830057, \
           0.40882846955602922608853782625, \
           0.40882846955602922608853782625, \
           0.0886157460419145274808558830057, \
           0.00255578440205624643060629074383 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
           -3.75043971772574225630392202571, \
           -2.36675941073454128861885646856, \
           -1.15440539473996812723959775884, \
            0.0, \
           +1.15440539473996812723959775884, \
           +2.36675941073454128861885646856, \
           +3.75043971772574225630392202571 ] )

    w = np.array ( [ \
           0.000548268855972217791621570532802, \
           0.0307571239675864970396450057164, \
           0.240123178605012713740161995179, \
           0.457142857142857142857142857143, \
           0.240123178605012713740161995179, \
           0.0307571239675864970396450057164, \
           0.000548268855972217791621570532802 ] )

  elif ( n == 8 ):

    x = np.array ( [ \
           -4.14454718612589433206019783917, \
           -2.80248586128754169911301080618, \
           -1.63651904243510799922544657297, \
           -0.539079811351375108072461918694, \
           +0.539079811351375108072461918694, \
           +1.63651904243510799922544657297, \
           +2.80248586128754169911301080618, \
           +4.14454718612589433206019783917 ] )

    w = np.array ( [ \
           0.00011261453837536777039380201687, \
           0.00963522012078826718691913771988, \
           0.117239907661759015117137525962, \
           0.373012257679077349925549534301, \
           0.373012257679077349925549534301, \
           0.117239907661759015117137525962, \
           0.00963522012078826718691913771988, \
           0.00011261453837536777039380201687 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
           -4.51274586339978266756667884317, \
           -3.20542900285646994336567590292, \
           -2.07684797867783010652215614374, \
           -1.02325566378913252482814822581, \
            0.0, \
           +1.02325566378913252482814822581, \
           +2.07684797867783010652215614374, \
           +3.20542900285646994336567590292, \
           +4.51274586339978266756667884317 ] )

    w = np.array ( [ \
           0.0000223458440077465836484639907118, \
           0.00278914132123176862881344575164, \
           0.0499164067652178740433414693826, \
           0.2440975028949394361410220177, \
           0.406349206349206349206349206349, \
           0.2440975028949394361410220177, \
           0.0499164067652178740433414693826, \
           0.00278914132123176862881344575164, \
           0.0000223458440077465836484639907118 ] )

  elif ( n == 10 ):

    x = np.array ( [ \
            -4.85946282833231215015516494660, \
            -3.58182348355192692277623675546, \
            -2.48432584163895458087625118368, \
            -1.46598909439115818325066466416, \
            -0.484935707515497653046233483105, \
            +0.484935707515497653046233483105, \
            +1.46598909439115818325066466416, \
            +2.48432584163895458087625118368, \
            +3.58182348355192692277623675546, \
            +4.85946282833231215015516494660 ] )

    w = np.array ( [ \
            0.0000043106526307182867322209547262, \
            0.000758070934312217670069636036508, \
            0.0191115805007702856047383687629, \
            0.135483702980267735563431657727, \
            0.344642334932019042875028116518, \
            0.344642334932019042875028116518, \
            0.135483702980267735563431657727, \
            0.0191115805007702856047383687629, \
            0.000758070934312217670069636036508, \
            0.0000043106526307182867322209547262 ] )

  else:

    print ( '' )
    print ( 'HERMITE_PROBABILIST_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1:10.' )
    raise Exception ( 'HERMITE_PROBABILIST_SET(): Fatal error!' )

  return x, w

def hermite_probabilist_set_test ( ):

#*****************************************************************************80
#
## hermite_probabilist_set_test() tests hermite_probabilist_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_probabilist_set_test():' )
  print ( '  hermite_probabilist_set() sets a Hermite quadrature rule.' )
  print ( '  The integration interval is ( -oo, +oo ).' )
  print ( '  The weight is exp ( - x * x / 2 ) / sqrt ( 2 * pi ).' )

  print ( '' )
  print ( '  Index       X             W' )
  print ( '' )

  for n in range ( 1, 11 ):

    x, w = hermite_probabilist_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def hermite_set ( n ):

#*****************************************************************************80
#
## hermite_set() sets abscissas and weights for Hermite quadrature.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -oo < x < +oo ) f(x) * rho(x) dx
#
#    The weight:
#
#      rho(x)   exp ( - x * x )
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) ).
#
#    Mathematica can numerically estimate the abscissas of the rule
#    of order N to P digits by the command:
#
#      NSolve [ HermiteH [ n, x ] == 0, x, p ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2015
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
#    Vladimir Krylov,
#    Approximate Calculation of Integrals,
#    Dover, 2006,
#    ISBN: 0486445798,
#    LC: QA311.K713.
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65
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
#    integer N, the order.
#    N must be between 1 and 20, 31/32/33, 63/64/65, 127/128/129.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
           0.0 ] )

    w = np.array ( [ \
           1.77245385090551602729816748334 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
           - 0.707106781186547524400844362105, \
             0.707106781186547524400844362105 ] )

    w = np.array ( [ \
           0.886226925452758013649083741671, \
           0.886226925452758013649083741671 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
           - 0.122474487139158904909864203735E+01, \
             0.0, \
             0.122474487139158904909864203735E+01 ] )

    w = np.array ( [ \
           0.295408975150919337883027913890, \
           0.118163590060367735153211165556E+01, \
           0.295408975150919337883027913890 ] )

  elif ( n == 4 ):

    x = np.array ( [ \
           - 0.165068012388578455588334111112E+01, \
           - 0.524647623275290317884060253835, \
             0.524647623275290317884060253835, \
             0.165068012388578455588334111112E+01 ] )

    w = np.array ( [ \
           0.813128354472451771430345571899E-01, \
           0.804914090005512836506049184481, \
           0.804914090005512836506049184481, \
           0.813128354472451771430345571899E-01 ] )

  elif ( n == 5 ):

    x = np.array ( [ \
           - 0.202018287045608563292872408814E+01, \
           - 0.958572464613818507112770593893, \
             0.0, \
             0.958572464613818507112770593893, \
             0.202018287045608563292872408814E+01 ] )

    w = np.array ( [ \
           0.199532420590459132077434585942E-01, \
           0.393619323152241159828495620852, \
           0.945308720482941881225689324449, \
           0.393619323152241159828495620852, \
           0.199532420590459132077434585942E-01 ] )

  elif ( n == 6 ):

    x = np.array ( [ \
           - 0.235060497367449222283392198706E+01, \
           - 0.133584907401369694971489528297E+01, \
           - 0.436077411927616508679215948251, \
             0.436077411927616508679215948251, \
             0.133584907401369694971489528297E+01, \
             0.235060497367449222283392198706E+01 ] )

    w = np.array ( [ \
           0.453000990550884564085747256463E-02, \
           0.157067320322856643916311563508, \
           0.724629595224392524091914705598, \
           0.724629595224392524091914705598, \
           0.157067320322856643916311563508, \
           0.453000990550884564085747256463E-02 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
           - 0.265196135683523349244708200652E+01, \
           - 0.167355162876747144503180139830E+01, \
           - 0.816287882858964663038710959027, \
             0.0, \
             0.816287882858964663038710959027, \
             0.167355162876747144503180139830E+01, \
             0.265196135683523349244708200652E+01 ] )

    w = np.array ( [ \
           0.971781245099519154149424255939E-03, \
           0.545155828191270305921785688417E-01, \
           0.425607252610127800520317466666, \
           0.810264617556807326764876563813, \
           0.425607252610127800520317466666, \
           0.545155828191270305921785688417E-01, \
           0.971781245099519154149424255939E-03 ] )

  elif ( n == 8 ):

    x = np.array ( [ \
           - 0.293063742025724401922350270524E+01, \
           - 0.198165675669584292585463063977E+01, \
           - 0.115719371244678019472076577906E+01, \
           - 0.381186990207322116854718885584, \
             0.381186990207322116854718885584, \
             0.115719371244678019472076577906E+01, \
             0.198165675669584292585463063977E+01, \
             0.293063742025724401922350270524E+01 ] )

    w = np.array ( [ \
           0.199604072211367619206090452544E-03, \
           0.170779830074134754562030564364E-01, \
           0.207802325814891879543258620286, \
           0.661147012558241291030415974496, \
           0.661147012558241291030415974496, \
           0.207802325814891879543258620286, \
           0.170779830074134754562030564364E-01, \
           0.199604072211367619206090452544E-03 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
           - 0.319099320178152760723004779538E+01, \
           - 0.226658058453184311180209693284E+01, \
           - 0.146855328921666793166701573925E+01, \
           - 0.723551018752837573322639864579, \
             0.0, \
             0.723551018752837573322639864579, \
             0.146855328921666793166701573925E+01, \
             0.226658058453184311180209693284E+01, \
             0.319099320178152760723004779538E+01 ] )

    w = np.array ( [ \
           0.396069772632643819045862946425E-04, \
           0.494362427553694721722456597763E-02, \
           0.884745273943765732879751147476E-01, \
           0.432651559002555750199812112956, \
           0.720235215606050957124334723389, \
           0.432651559002555750199812112956, \
           0.884745273943765732879751147476E-01, \
           0.494362427553694721722456597763E-02, \
           0.396069772632643819045862946425E-04 ] )

  elif ( n == 10 ):

    x = np.array ( [ \
            - 0.343615911883773760332672549432E+01, \
            - 0.253273167423278979640896079775E+01, \
            - 0.175668364929988177345140122011E+01, \
            - 0.103661082978951365417749191676E+01, \
            - 0.342901327223704608789165025557, \
              0.342901327223704608789165025557, \
              0.103661082978951365417749191676E+01, \
              0.175668364929988177345140122011E+01, \
              0.253273167423278979640896079775E+01, \
              0.343615911883773760332672549432E+01 ] )

    w = np.array ( [ \
            0.764043285523262062915936785960E-05, \
            0.134364574678123269220156558585E-02, \
            0.338743944554810631361647312776E-01, \
            0.240138611082314686416523295006, \
            0.610862633735325798783564990433, \
            0.610862633735325798783564990433, \
            0.240138611082314686416523295006, \
            0.338743944554810631361647312776E-01, \
            0.134364574678123269220156558585E-02, \
            0.764043285523262062915936785960E-05 ] )

  elif ( n == 11 ):

    x = np.array ( [ \
            - 0.366847084655958251845837146485E+01, \
            - 0.278329009978165177083671870152E+01, \
            - 0.202594801582575533516591283121E+01, \
            - 0.132655708449493285594973473558E+01, \
            - 0.656809566882099765024611575383, \
              0.0, \
              0.656809566882099765024611575383, \
              0.132655708449493285594973473558E+01, \
              0.202594801582575533516591283121E+01, \
              0.278329009978165177083671870152E+01, \
              0.366847084655958251845837146485E+01 ] )

    w = np.array ( [ \
            0.143956039371425822033088366032E-05, \
            0.346819466323345510643413772940E-03, \
            0.119113954449115324503874202916E-01, \
            0.117227875167708503381788649308, \
            0.429359752356125028446073598601, \
            0.654759286914591779203940657627, \
            0.429359752356125028446073598601, \
            0.117227875167708503381788649308, \
            0.119113954449115324503874202916E-01, \
            0.346819466323345510643413772940E-03, \
            0.143956039371425822033088366032E-05 ] )

  elif ( n == 12 ):

    x = np.array ( [ \
            - 0.388972489786978191927164274724E+01, \
            - 0.302063702512088977171067937518E+01, \
            - 0.227950708050105990018772856942E+01, \
            - 0.159768263515260479670966277090E+01, \
            - 0.947788391240163743704578131060, \
            - 0.314240376254359111276611634095, \
              0.314240376254359111276611634095, \
              0.947788391240163743704578131060, \
              0.159768263515260479670966277090E+01, \
              0.227950708050105990018772856942E+01, \
              0.302063702512088977171067937518E+01, \
              0.388972489786978191927164274724E+01 ] )

    w = np.array ( [ \
            0.265855168435630160602311400877E-06, \
            0.857368704358785865456906323153E-04, \
            0.390539058462906185999438432620E-02, \
            0.516079856158839299918734423606E-01, \
            0.260492310264161129233396139765, \
            0.570135236262479578347113482275, \
            0.570135236262479578347113482275, \
            0.260492310264161129233396139765, \
            0.516079856158839299918734423606E-01, \
            0.390539058462906185999438432620E-02, \
            0.857368704358785865456906323153E-04, \
            0.265855168435630160602311400877E-06 ] )

  elif ( n == 13 ):

    x = np.array ( [ \
            - 0.410133759617863964117891508007E+01, \
            - 0.324660897837240998812205115236E+01, \
            - 0.251973568567823788343040913628E+01, \
            - 0.185310765160151214200350644316E+01, \
            - 0.122005503659074842622205526637E+01, \
            - 0.605763879171060113080537108602, \
              0.0, \
              0.605763879171060113080537108602, \
              0.122005503659074842622205526637E+01, \
              0.185310765160151214200350644316E+01, \
              0.251973568567823788343040913628E+01, \
              0.324660897837240998812205115236E+01, \
              0.410133759617863964117891508007E+01 ] )

    w = np.array ( [ \
            0.482573185007313108834997332342E-07, \
            0.204303604027070731248669432937E-04, \
            0.120745999271938594730924899224E-02, \
            0.208627752961699392166033805050E-01, \
            0.140323320687023437762792268873, \
            0.421616296898543221746893558568, \
            0.604393187921161642342099068579, \
            0.421616296898543221746893558568, \
            0.140323320687023437762792268873, \
            0.208627752961699392166033805050E-01, \
            0.120745999271938594730924899224E-02, \
            0.204303604027070731248669432937E-04, \
            0.482573185007313108834997332342E-07 ] )

  elif ( n == 14 ):

    x = np.array ( [ \
            - 0.430444857047363181262129810037E+01, \
            - 0.346265693360227055020891736115E+01, \
            - 0.274847072498540256862499852415E+01, \
            - 0.209518325850771681573497272630E+01, \
            - 0.147668273114114087058350654421E+01, \
            - 0.878713787329399416114679311861, \
            - 0.291745510672562078446113075799, \
              0.291745510672562078446113075799, \
              0.878713787329399416114679311861, \
              0.147668273114114087058350654421E+01, \
              0.209518325850771681573497272630E+01, \
              0.274847072498540256862499852415E+01, \
              0.346265693360227055020891736115E+01, \
              0.430444857047363181262129810037E+01 ] )

    w = np.array ( [ \
            0.862859116812515794532041783429E-08, \
            0.471648435501891674887688950105E-05, \
            0.355092613551923610483661076691E-03, \
            0.785005472645794431048644334608E-02, \
            0.685055342234652055387163312367E-01, \
            0.273105609064246603352569187026, \
            0.536405909712090149794921296776, \
            0.536405909712090149794921296776, \
            0.273105609064246603352569187026, \
            0.685055342234652055387163312367E-01, \
            0.785005472645794431048644334608E-02, \
            0.355092613551923610483661076691E-03, \
            0.471648435501891674887688950105E-05, \
            0.862859116812515794532041783429E-08 ] )

  elif ( n == 15 ):

    x = np.array ( [ \
            - 0.449999070730939155366438053053E+01, \
            - 0.366995037340445253472922383312E+01, \
            - 0.296716692790560324848896036355E+01, \
            - 0.232573248617385774545404479449E+01, \
            - 0.171999257518648893241583152515E+01, \
            - 0.113611558521092066631913490556E+01, \
            - 0.565069583255575748526020337198, \
              0.0, \
              0.565069583255575748526020337198, \
              0.113611558521092066631913490556E+01, \
              0.171999257518648893241583152515E+01, \
              0.232573248617385774545404479449E+01, \
              0.296716692790560324848896036355E+01, \
              0.366995037340445253472922383312E+01, \
              0.449999070730939155366438053053E+01 ] )

    w = np.array ( [ \
            0.152247580425351702016062666965E-08, \
            0.105911554771106663577520791055E-05, \
            0.100004441232499868127296736177E-03, \
            0.277806884291277589607887049229E-02, \
            0.307800338725460822286814158758E-01, \
            0.158488915795935746883839384960, \
            0.412028687498898627025891079568, \
            0.564100308726417532852625797340, \
            0.412028687498898627025891079568, \
            0.158488915795935746883839384960, \
            0.307800338725460822286814158758E-01, \
            0.277806884291277589607887049229E-02, \
            0.100004441232499868127296736177E-03, \
            0.105911554771106663577520791055E-05, \
            0.152247580425351702016062666965E-08 ] )

  elif ( n == 16 ):

    x = np.array ( [ \
            - 0.468873893930581836468849864875E+01, \
            - 0.386944790486012269871942409801E+01, \
            - 0.317699916197995602681399455926E+01, \
            - 0.254620215784748136215932870545E+01, \
            - 0.195178799091625397743465541496E+01, \
            - 0.138025853919888079637208966969E+01, \
            - 0.822951449144655892582454496734, \
            - 0.273481046138152452158280401965, \
              0.273481046138152452158280401965, \
              0.822951449144655892582454496734, \
              0.138025853919888079637208966969E+01, \
              0.195178799091625397743465541496E+01, \
              0.254620215784748136215932870545E+01, \
              0.317699916197995602681399455926E+01, \
              0.386944790486012269871942409801E+01, \
              0.468873893930581836468849864875E+01 ] )

    w = np.array ( [ \
            0.265480747401118224470926366050E-09, \
            0.232098084486521065338749423185E-06, \
            0.271186009253788151201891432244E-04, \
            0.932284008624180529914277305537E-03, \
            0.128803115355099736834642999312E-01, \
            0.838100413989858294154207349001E-01, \
            0.280647458528533675369463335380, \
            0.507929479016613741913517341791, \
            0.507929479016613741913517341791, \
            0.280647458528533675369463335380, \
            0.838100413989858294154207349001E-01, \
            0.128803115355099736834642999312E-01, \
            0.932284008624180529914277305537E-03, \
            0.271186009253788151201891432244E-04, \
            0.232098084486521065338749423185E-06, \
            0.265480747401118224470926366050E-09 ] )

  elif ( n == 17 ):

    x = np.array ( [ \
            - 0.487134519367440308834927655662E+01, \
            - 0.406194667587547430689245559698E+01, \
            - 0.337893209114149408338327069289E+01, \
            - 0.275776291570388873092640349574E+01, \
            - 0.217350282666662081927537907149E+01, \
            - 0.161292431422123133311288254454E+01, \
            - 0.106764872574345055363045773799E+01, \
            - 0.531633001342654731349086553718, \
              0.0, \
              0.531633001342654731349086553718, \
              0.106764872574345055363045773799E+01, \
              0.161292431422123133311288254454E+01, \
              0.217350282666662081927537907149E+01, \
              0.275776291570388873092640349574E+01, \
              0.337893209114149408338327069289E+01, \
              0.406194667587547430689245559698E+01, \
              0.487134519367440308834927655662E+01 ] )

    w = np.array ( [ \
            0.458057893079863330580889281222E-10, \
            0.497707898163079405227863353715E-07, \
            0.711228914002130958353327376218E-05, \
            0.298643286697753041151336643059E-03, \
            0.506734995762753791170069495879E-02, \
            0.409200341495762798094994877854E-01, \
            0.172648297670097079217645196219, \
            0.401826469470411956577635085257, \
            0.530917937624863560331883103379, \
            0.401826469470411956577635085257, \
            0.172648297670097079217645196219, \
            0.409200341495762798094994877854E-01, \
            0.506734995762753791170069495879E-02, \
            0.298643286697753041151336643059E-03, \
            0.711228914002130958353327376218E-05, \
            0.497707898163079405227863353715E-07, \
            0.458057893079863330580889281222E-10 ] )

  elif ( n == 18 ):

    x = np.array ( [ \
            - 0.504836400887446676837203757885E+01, \
            - 0.424811787356812646302342016090E+01, \
            - 0.357376906848626607950067599377E+01, \
            - 0.296137750553160684477863254906E+01, \
            - 0.238629908916668600026459301424E+01, \
            - 0.183553160426162889225383944409E+01, \
            - 0.130092085838961736566626555439E+01, \
            - 0.776682919267411661316659462284, \
            - 0.258267750519096759258116098711, \
              0.258267750519096759258116098711, \
              0.776682919267411661316659462284, \
              0.130092085838961736566626555439E+01, \
              0.183553160426162889225383944409E+01, \
              0.238629908916668600026459301424E+01, \
              0.296137750553160684477863254906E+01, \
              0.357376906848626607950067599377E+01, \
              0.424811787356812646302342016090E+01, \
              0.504836400887446676837203757885E+01 ] )

    w = np.array ( [ \
            0.782819977211589102925147471012E-11, \
            0.104672057957920824443559608435E-07, \
            0.181065448109343040959702385911E-05, \
            0.918112686792940352914675407371E-04, \
            0.188852263026841789438175325426E-02, \
            0.186400423875446519219315221973E-01, \
            0.973017476413154293308537234155E-01, \
            0.284807285669979578595606820713, \
            0.483495694725455552876410522141, \
            0.483495694725455552876410522141, \
            0.284807285669979578595606820713, \
            0.973017476413154293308537234155E-01, \
            0.186400423875446519219315221973E-01, \
            0.188852263026841789438175325426E-02, \
            0.918112686792940352914675407371E-04, \
            0.181065448109343040959702385911E-05, \
            0.104672057957920824443559608435E-07, \
            0.782819977211589102925147471012E-11 ] )

  elif ( n == 19 ):

    x = np.array ( [ \
            - 0.522027169053748216460967142500E+01, \
            - 0.442853280660377943723498532226E+01, \
            - 0.376218735196402009751489394104E+01, \
            - 0.315784881834760228184318034120E+01, \
            - 0.259113378979454256492128084112E+01, \
            - 0.204923170985061937575050838669E+01, \
            - 0.152417061939353303183354859367E+01, \
            - 0.101036838713431135136859873726E+01, \
            - 0.503520163423888209373811765050, \
              0.0, \
              0.503520163423888209373811765050, \
              0.101036838713431135136859873726E+01, \
              0.152417061939353303183354859367E+01, \
              0.204923170985061937575050838669E+01, \
              0.259113378979454256492128084112E+01, \
              0.315784881834760228184318034120E+01, \
              0.376218735196402009751489394104E+01, \
              0.442853280660377943723498532226E+01, \
              0.522027169053748216460967142500E+01 ] )

    w = np.array ( [ \
            0.132629709449851575185289154385E-11, \
            0.216305100986355475019693077221E-08, \
            0.448824314722312295179447915594E-06, \
            0.272091977631616257711941025214E-04, \
            0.670877521407181106194696282100E-03, \
            0.798886677772299020922211491861E-02, \
            0.508103869090520673569908110358E-01, \
            0.183632701306997074156148485766, \
            0.391608988613030244504042313621, \
            0.502974888276186530840731361096, \
            0.391608988613030244504042313621, \
            0.183632701306997074156148485766, \
            0.508103869090520673569908110358E-01, \
            0.798886677772299020922211491861E-02, \
            0.670877521407181106194696282100E-03, \
            0.272091977631616257711941025214E-04, \
            0.448824314722312295179447915594E-06, \
            0.216305100986355475019693077221E-08, \
            0.132629709449851575185289154385E-11 ] )

  elif ( n == 20 ):

    x = np.array ( [ \
            - 0.538748089001123286201690041068E+01, \
            - 0.460368244955074427307767524898E+01, \
            - 0.394476404011562521037562880052E+01, \
            - 0.334785456738321632691492452300E+01, \
            - 0.278880605842813048052503375640E+01, \
            - 0.225497400208927552308233334473E+01, \
            - 0.173853771211658620678086566214E+01, \
            - 0.123407621539532300788581834696E+01, \
            - 0.737473728545394358705605144252, \
            - 0.245340708300901249903836530634, \
              0.245340708300901249903836530634, \
              0.737473728545394358705605144252, \
              0.123407621539532300788581834696E+01, \
              0.173853771211658620678086566214E+01, \
              0.225497400208927552308233334473E+01, \
              0.278880605842813048052503375640E+01, \
              0.334785456738321632691492452300E+01, \
              0.394476404011562521037562880052E+01, \
              0.460368244955074427307767524898E+01, \
              0.538748089001123286201690041068E+01 ] )

    w = np.array ( [ \
            0.222939364553415129252250061603E-12, \
            0.439934099227318055362885145547E-09, \
            0.108606937076928169399952456345E-06, \
            0.780255647853206369414599199965E-05, \
            0.228338636016353967257145917963E-03, \
            0.324377334223786183218324713235E-02, \
            0.248105208874636108821649525589E-01, \
            0.109017206020023320013755033535, \
            0.286675505362834129719659706228, \
            0.462243669600610089650328639861, \
            0.462243669600610089650328639861, \
            0.286675505362834129719659706228, \
            0.109017206020023320013755033535, \
            0.248105208874636108821649525589E-01, \
            0.324377334223786183218324713235E-02, \
            0.228338636016353967257145917963E-03, \
            0.780255647853206369414599199965E-05, \
            0.108606937076928169399952456345E-06, \
            0.439934099227318055362885145547E-09, \
            0.222939364553415129252250061603E-12 ] )

  elif ( n == 30 ):

    x = np.array ( [ \
              -6.86334529352989158106110835756, \
              -6.13827922012393462039499237854, \
              -5.53314715156749572511833355558, \
              -4.98891896858994394448649710633, \
              -4.48305535709251834188703761971, \
              -4.00390860386122881522787601332, \
              -3.54444387315534988692540090217, \
              -3.09997052958644174868873332237, \
              -2.66713212453561720057110646422, \
              -2.24339146776150407247297999483, \
              -1.82674114360368803883588048351, \
              -1.41552780019818851194072510555, \
              -1.00833827104672346180498960870, \
              -0.603921058625552307778155678757, \
              -0.201128576548871485545763013244, \
               0.201128576548871485545763013244, \
               0.603921058625552307778155678757, \
               1.00833827104672346180498960870, \
               1.41552780019818851194072510555, \
               1.82674114360368803883588048351, \
               2.24339146776150407247297999483, \
               2.66713212453561720057110646422, \
               3.09997052958644174868873332237, \
               3.54444387315534988692540090217, \
               4.00390860386122881522787601332, \
               4.48305535709251834188703761971, \
               4.98891896858994394448649710633, \
               5.53314715156749572511833355558, \
               6.13827922012393462039499237854, \
               6.86334529352989158106110835756 ] )

    w = np.array ( [ \
              0.290825470013122622941102747365E-20, \
              0.281033360275090370876277491534E-16, \
              0.287860708054870606219239791142E-13, \
              0.810618629746304420399344796173E-11, \
              0.917858042437852820850075742492E-09, \
              0.510852245077594627738963204403E-07, \
              0.157909488732471028834638794022E-05, \
              0.293872522892298764150118423412E-04, \
              0.348310124318685523420995323183E-03, \
              0.273792247306765846298942568953E-02, \
              0.147038297048266835152773557787E-01, \
              0.551441768702342511680754948183E-01, \
              0.146735847540890099751693643152, \
              0.280130930839212667413493211293, \
              0.386394889541813862555601849165, \
              0.386394889541813862555601849165, \
              0.280130930839212667413493211293, \
              0.146735847540890099751693643152, \
              0.551441768702342511680754948183E-01, \
              0.147038297048266835152773557787E-01, \
              0.273792247306765846298942568953E-02, \
              0.348310124318685523420995323183E-03, \
              0.293872522892298764150118423412E-04, \
              0.157909488732471028834638794022E-05, \
              0.510852245077594627738963204403E-07, \
              0.917858042437852820850075742492E-09, \
              0.810618629746304420399344796173E-11, \
              0.287860708054870606219239791142E-13, \
              0.281033360275090370876277491534E-16, \
              0.290825470013122622941102747365E-20 ] )

  elif ( n == 31 ):

    x = np.array ( [ \
           -6.99568012371854027532485214732E+00, \
           -6.27507870494286014270365678125E+00, \
           -5.67396144461858832963325587893E+00, \
           -5.13359557711238070458629689140E+00, \
           -4.63155950631285994206679976543E+00, \
           -4.15627175581814517248313523153E+00, \
           -3.70074340323146942244971645897E+00, \
           -3.26032073231354081046454015096E+00, \
           -2.83168045339020545570156401514E+00, \
           -2.41231770548042010517401845821E+00, \
           -2.00025854893563896579755625986E+00, \
           -1.59388586047213982613884194556E+00, \
           -1.19182699835004642608213586492E+00, \
           -0.792876976915308939685930329988E+00, \
           -0.395942736471423110946700416634E+00, \
            0.0E+00, \
            0.395942736471423110946700416634E+00, \
            0.792876976915308939685930329988E+00, \
            1.19182699835004642608213586492E+00, \
            1.59388586047213982613884194556E+00, \
            2.00025854893563896579755625986E+00, \
            2.41231770548042010517401845821E+00, \
            2.83168045339020545570156401514E+00, \
            3.26032073231354081046454015096E+00, \
            3.70074340323146942244971645897E+00, \
            4.15627175581814517248313523153E+00, \
            4.63155950631285994206679976543E+00, \
            5.13359557711238070458629689140E+00, \
            5.67396144461858832963325587893E+00, \
            6.27507870494286014270365678125E+00, \
            6.99568012371854027532485214732E+00 ] )

    w = np.array ( [ \
            4.61896839446420502132944426974E-22, \
            5.11060900792715640739422641166E-18, \
            5.89955649875387299038431589378E-15, \
            1.86037352145214652437380892603E-12, \
            2.35249200320864163398597795323E-10, \
            1.46119883449105307352780323055E-08, \
            5.04371255893979974253745671633E-07, \
            0.0000104986027576756063228123279208E+00, \
            0.000139520903950470433823653754396E+00, \
            0.00123368330730688826551750402319E+00, \
            0.00748279991403519848345678003016E+00, \
            0.0318472307313003327772087235339E+00, \
            0.0967179481608704535580338478886E+00, \
            0.212132788668764779877735637343E+00, \
            0.338772657894107724675701919878E+00, \
            0.395778556098609545141783810611E+00, \
            0.338772657894107724675701919878E+00, \
            0.212132788668764779877735637343E+00, \
            0.0967179481608704535580338478886E+00, \
            0.0318472307313003327772087235339E+00, \
            0.00748279991403519848345678003016E+00, \
            0.00123368330730688826551750402319E+00, \
            0.000139520903950470433823653754396E+00, \
            0.0000104986027576756063228123279208E+00, \
            5.04371255893979974253745671633E-07, \
            1.46119883449105307352780323055E-08, \
            2.35249200320864163398597795323E-10, \
            1.86037352145214652437380892603E-12, \
            5.89955649875387299038431589378E-15, \
            5.11060900792715640739422641166E-18, \
            4.61896839446420502132944426974E-22 ] )

  elif ( n == 32 ):

    x = np.array ( [ \
            -7.12581390983072757279520760342E+00, \
            -6.40949814926966041217376374153E+00, \
            -5.81222594951591383276596615366E+00, \
            -5.27555098651588012781906048140E+00, \
            -4.77716450350259639303579405689E+00, \
            -4.30554795335119844526348653193E+00, \
            -3.85375548547144464388787292109E+00, \
            -3.41716749281857073587392729564E+00, \
            -2.99249082500237420628549407606E+00, \
            -2.57724953773231745403092930114E+00, \
            -2.16949918360611217330570559502E+00, \
            -1.76765410946320160462767325853E+00, \
            -1.37037641095287183816170564864E+00, \
            -0.976500463589682838484704871982E+00, \
            -0.584978765435932448466957544011E+00, \
            -0.194840741569399326708741289532E+00, \
             0.194840741569399326708741289532E+00, \
             0.584978765435932448466957544011E+00, \
             0.976500463589682838484704871982E+00, \
             1.37037641095287183816170564864E+00, \
             1.76765410946320160462767325853E+00, \
             2.16949918360611217330570559502E+00, \
             2.57724953773231745403092930114E+00, \
             2.99249082500237420628549407606E+00, \
             3.41716749281857073587392729564E+00, \
             3.85375548547144464388787292109E+00, \
             4.30554795335119844526348653193E+00, \
             4.77716450350259639303579405689E+00, \
             5.27555098651588012781906048140E+00, \
             5.81222594951591383276596615366E+00, \
             6.40949814926966041217376374153E+00, \
             7.12581390983072757279520760342E+00 ] )

    w = np.array ( [ \
             7.31067642738416239327427845506E-23, \
             9.23173653651829223349442007207E-19, \
             1.19734401709284866582868189951E-15, \
             4.21501021132644757296944521183E-13, \
             5.93329146339663861451156821558E-11, \
             4.0988321647708966182350410138E-09, \
             1.57416779254559402926869257929E-07, \
             3.65058512956237605737032418746E-06, \
             0.0000541658406181998255800193939267E+00, \
             0.000536268365527972045970238101501E+00, \
             0.00365489032665442807912565712241E+00, \
             0.017553428831573430303437844611E+00, \
             0.0604581309559126141865857607833E+00, \
             0.151269734076642482575147114614E+00, \
             0.277458142302529898137698918542E+00, \
             0.375238352592802392866818388907E+00, \
             0.375238352592802392866818388907E+00, \
             0.277458142302529898137698918542E+00, \
             0.151269734076642482575147114614E+00, \
             0.0604581309559126141865857607833E+00, \
             0.017553428831573430303437844611E+00, \
             0.00365489032665442807912565712241E+00, \
             0.000536268365527972045970238101501E+00, \
             0.0000541658406181998255800193939267E+00, \
             3.65058512956237605737032418746E-06, \
             1.57416779254559402926869257929E-07, \
             4.0988321647708966182350410138E-09, \
             5.93329146339663861451156821558E-11, \
             4.21501021132644757296944521183E-13, \
             1.19734401709284866582868189951E-15, \
             9.23173653651829223349442007207E-19, \
             7.31067642738416239327427845506E-23 ] )

  elif ( n == 33 ):

    x = np.array ( [ \
            -7.25385182201520064607977244465E+00, \
            -6.54165544573807726095826608811E+00, \
            -5.94807118208714447981366477584E+00, \
            -5.41492900261419253992709076454E+00, \
            -4.92002852059500829241139910265E+00, \
            -4.45191114883282719009473876206E+00, \
            -4.00367160995693141451378357174E+00, \
            -3.57072198023271828561890330658E+00, \
            -3.14979668170382538461281438786E+00, \
            -2.73844582435135490694887052899E+00, \
            -2.33475115152951517708536069773E+00, \
            -1.93715458182220661643452220908E+00, \
            -1.54434826124312180914304288754E+00, \
            -1.15520020412678961356412482063E+00, \
            -0.768701379758868598107224561306E+00, \
            -0.383926014508409083771145488401E+00, \
             0.0E+00, \
             0.383926014508409083771145488401E+00, \
             0.768701379758868598107224561306E+00, \
             1.15520020412678961356412482063E+00, \
             1.54434826124312180914304288754E+00, \
             1.93715458182220661643452220908E+00, \
             2.33475115152951517708536069773E+00, \
             2.73844582435135490694887052899E+00, \
             3.14979668170382538461281438786E+00, \
             3.57072198023271828561890330658E+00, \
             4.00367160995693141451378357174E+00, \
             4.45191114883282719009473876206E+00, \
             4.92002852059500829241139910265E+00, \
             5.41492900261419253992709076454E+00, \
             5.94807118208714447981366477584E+00, \
             6.54165544573807726095826608811E+00, \
             7.25385182201520064607977244465E+00 ] )

    w = np.array ( [ \
            1.15331621854588454082208890757E-23, \
            1.65709474153369051048226040291E-19, \
            2.40778567955799442824587707068E-16, \
            9.43481415901497503451931586527E-14, \
            1.47398093709248867676655543441E-11, \
            1.12892224710833129085848357165E-09, \
            4.8077456763231909801575826594E-08, \
            1.23769336720121013593677278301E-06, \
            0.000020423684051423773240532989618E+00, \
            0.000225442770596327415479556999963E+00, \
            0.00171845463776092445684897958755E+00, \
            0.00926568997068523330372581072023E+00, \
            0.0359879823185769744486866448437E+00, \
            0.102069079995541500792505520921E+00, \
            0.213493931150291836488258605194E+00, \
            0.331552000750741282288352789764E+00, \
            0.383785266519863801349608543622E+00, \
            0.331552000750741282288352789764E+00, \
            0.213493931150291836488258605194E+00, \
            0.102069079995541500792505520921E+00, \
            0.0359879823185769744486866448437E+00, \
            0.00926568997068523330372581072023E+00, \
            0.00171845463776092445684897958755E+00, \
            0.000225442770596327415479556999963E+00, \
            0.000020423684051423773240532989618E+00, \
            1.23769336720121013593677278301E-06, \
            4.8077456763231909801575826594E-08, \
            1.12892224710833129085848357165E-09, \
            1.47398093709248867676655543441E-11, \
            9.43481415901497503451931586527E-14, \
            2.40778567955799442824587707068E-16, \
            1.65709474153369051048226040291E-19, \
            1.15331621854588454082208890757E-23 ] )

  elif ( n == 63 ):

    x = np.array ( [ \
           -10.4354998778541680534681154273E+00, \
            -9.80287599129749636352239352865E+00, \
            -9.27920195430503913194047455065E+00, \
            -8.81185814372845464425266282756E+00, \
            -8.38076834518632193430106510438E+00, \
            -7.97559508014203731815418062985E+00, \
            -7.59013951986410667624797831945E+00, \
            -7.22031670788896784611613242225E+00, \
            -6.86325443317953685273532858761E+00, \
            -6.51683481068211606052733958540E+00, \
            -6.17943799227059698624184617873E+00, \
            -5.84978840008106734625265829615E+00, \
            -5.52685725264030314250475751228E+00, \
            -5.20979798304083548615751364163E+00, \
            -4.89790186449757423507450992149E+00, \
            -4.59056657444351902292712945691E+00, \
            -4.28727333528244040317276161995E+00, \
            -3.98756991041971574852270520681E+00, \
            -3.69105770009634651173228105598E+00, \
            -3.39738177133039118527559418063E+00, \
            -3.10622302792825663291386167460E+00, \
            -2.81729196728379777507471356574E+00, \
            -2.53032363047120109268552217185E+00, \
            -2.24507346048120662989959181793E+00, \
            -1.96131385830814852939220084113E+00, \
            -1.67883127917201375208028006226E+00, \
            -1.39742374860496251075707520637E+00, \
            -1.11689870509964626905109702778E+00, \
            -0.837071095589476159777377954613E+00, \
            -0.557761664279082216687636652538E+00, \
            -0.278795385671152239866876286272E+00, \
             0.0E+00, \
             0.278795385671152239866876286272E+00, \
             0.557761664279082216687636652538E+00, \
             0.837071095589476159777377954613E+00, \
             1.11689870509964626905109702778E+00, \
             1.39742374860496251075707520637E+00, \
             1.67883127917201375208028006226E+00, \
             1.96131385830814852939220084113E+00, \
             2.24507346048120662989959181793E+00, \
             2.53032363047120109268552217185E+00, \
             2.81729196728379777507471356574E+00, \
             3.10622302792825663291386167460E+00, \
             3.39738177133039118527559418063E+00, \
             3.69105770009634651173228105598E+00, \
             3.98756991041971574852270520681E+00, \
             4.28727333528244040317276161995E+00, \
             4.59056657444351902292712945691E+00, \
             4.89790186449757423507450992149E+00, \
             5.20979798304083548615751364163E+00, \
             5.52685725264030314250475751228E+00, \
             5.84978840008106734625265829615E+00, \
             6.17943799227059698624184617873E+00, \
             6.51683481068211606052733958540E+00, \
             6.86325443317953685273532858761E+00, \
             7.22031670788896784611613242225E+00, \
             7.59013951986410667624797831945E+00, \
             7.97559508014203731815418062985E+00, \
             8.38076834518632193430106510438E+00, \
             8.81185814372845464425266282756E+00, \
             9.27920195430503913194047455065E+00, \
             9.80287599129749636352239352865E+00, \
            10.4354998778541680534681154273E+00 ] )

    w = np.array ( [ \
            3.70992064349030055823376157823E-48, \
            1.04007786152246672212559599908E-42, \
            1.97968047083199197900260998813E-38, \
            8.46874781919035663281042885251E-35, \
            1.30713059308206243904769877879E-31, \
            9.34378371756582396450246862195E-29, \
            3.60274266352851638202340658522E-26, \
            8.29638631162099766157527065317E-24, \
            1.22666299091434557721622529775E-21, \
            1.22884356288353036990240371039E-19, \
            8.69255369584585252225619256428E-18, \
            4.48570586893158184069444097978E-16, \
            1.73358179557891044383064226749E-14, \
            5.1265062385197846998384009333E-13, \
            1.18089218445696923817995132237E-11, \
            2.15086982978749617679069862879E-10, \
            3.13719295353830786449435629291E-09, \
            3.70416259848969809883356560995E-08, \
            3.57347329499908777461505032558E-07, \
            2.83931144984692884712301165567E-06, \
            0.0000187091130037887216027832755405E+00, \
            0.000102848808006856425543062213642E+00, \
            0.000474117026103206754395975199216E+00, \
            0.0018409222622442103760124297917E+00, \
            0.00604360445513757113209247151533E+00, \
            0.0168292991996521044559098701555E+00, \
            0.0398582640278170328649908688578E+00, \
            0.0804670879942008323850873860195E+00, \
            0.138719508176584635072239096351E+00, \
            0.204486953468973988225911656103E+00, \
            0.25799889943138332612723393346E+00, \
            0.278766948849251654365527505911E+00, \
            0.25799889943138332612723393346E+00, \
            0.204486953468973988225911656103E+00, \
            0.138719508176584635072239096351E+00, \
            0.0804670879942008323850873860195E+00, \
            0.0398582640278170328649908688578E+00, \
            0.0168292991996521044559098701555E+00, \
            0.00604360445513757113209247151533E+00, \
            0.0018409222622442103760124297917E+00, \
            0.000474117026103206754395975199216E+00, \
            0.000102848808006856425543062213642E+00, \
            0.0000187091130037887216027832755405E+00, \
            2.83931144984692884712301165567E-06, \
            3.57347329499908777461505032558E-07, \
            3.70416259848969809883356560995E-08, \
            3.13719295353830786449435629291E-09, \
            2.15086982978749617679069862879E-10, \
            1.18089218445696923817995132237E-11, \
            5.1265062385197846998384009333E-13, \
            1.73358179557891044383064226749E-14, \
            4.48570586893158184069444097978E-16, \
            8.69255369584585252225619256428E-18, \
            1.22884356288353036990240371039E-19, \
            1.22666299091434557721622529775E-21, \
            8.29638631162099766157527065317E-24, \
            3.60274266352851638202340658522E-26, \
            9.34378371756582396450246862195E-29, \
            1.30713059308206243904769877879E-31, \
            8.46874781919035663281042885251E-35, \
            1.97968047083199197900260998813E-38, \
            1.04007786152246672212559599908E-42, \
            3.70992064349030055823376157823E-48 ] )

  elif ( n == 64 ):

    x = np.array ( [ \
           -10.5261231679605458833268262838E+00, \
            -9.89528758682953902120446147716E+00, \
            -9.37315954964672116254565243972E+00, \
            -8.90724909996476975729597288564E+00, \
            -8.47752908337986309056416634482E+00, \
            -8.07368728501022522585879114076E+00, \
            -7.68954016404049682844780422987E+00, \
            -7.32101303278094920118956936372E+00, \
            -6.96524112055110752924264219349E+00, \
            -6.62011226263602737903666010894E+00, \
            -6.28401122877482823541809319507E+00, \
            -5.95566632679948604534456718098E+00, \
            -5.63405216434997214724992048331E+00, \
            -5.31832522463327085732364951520E+00, \
            -5.00777960219876819644370262718E+00, \
            -4.70181564740749981609753801581E+00, \
            -4.39991716822813764776793253544E+00, \
            -4.10163447456665671497098123846E+00, \
            -3.80657151394536046116597200046E+00, \
            -3.51437593574090621153995058647E+00, \
            -3.22473129199203572584817111019E+00, \
            -2.93735082300462180968533902619E+00, \
            -2.65197243543063501100545778600E+00, \
            -2.36835458863240140411151126534E+00, \
            -2.08627287988176202083256330236E+00, \
            -1.80551717146554491890377357419E+00, \
            -1.52588914020986366294897013315E+00, \
            -1.24720015694311794069356453069E+00, \
            -0.969269423071178016743541489019E+00, \
            -0.691922305810044577268219287596E+00, \
            -0.414988824121078684576929129200E+00, \
            -0.138302244987009724115049767967E+00, \
             0.138302244987009724115049767967E+00, \
             0.414988824121078684576929129200E+00, \
             0.691922305810044577268219287596E+00, \
             0.969269423071178016743541489019E+00, \
             1.24720015694311794069356453069E+00, \
             1.52588914020986366294897013315E+00, \
             1.80551717146554491890377357419E+00, \
             2.08627287988176202083256330236E+00, \
             2.36835458863240140411151126534E+00, \
             2.65197243543063501100545778600E+00, \
             2.93735082300462180968533902619E+00, \
             3.22473129199203572584817111019E+00, \
             3.51437593574090621153995058647E+00, \
             3.80657151394536046116597200046E+00, \
             4.10163447456665671497098123846E+00, \
             4.39991716822813764776793253544E+00, \
             4.70181564740749981609753801581E+00, \
             5.00777960219876819644370262718E+00, \
             5.31832522463327085732364951520E+00, \
             5.63405216434997214724992048331E+00, \
             5.95566632679948604534456718098E+00, \
             6.28401122877482823541809319507E+00, \
             6.62011226263602737903666010894E+00, \
             6.96524112055110752924264219349E+00, \
             7.32101303278094920118956936372E+00, \
             7.68954016404049682844780422987E+00, \
             8.07368728501022522585879114076E+00, \
             8.47752908337986309056416634482E+00, \
             8.90724909996476975729597288564E+00, \
             9.37315954964672116254565243972E+00, \
             9.89528758682953902120446147716E+00, \
            10.5261231679605458833268262838E+00 ] )

    w = np.array ( [ \
             5.53570653585694282057546330099E-49, \
             1.67974799010815921866628833063E-43, \
             3.42113801125574050432722182815E-39, \
             1.55739062462976380230933538026E-35, \
             2.54966089911299925660476658044E-32, \
             1.92910359546496685030196877907E-29, \
             7.86179778892591036909999149628E-27, \
             1.91170688330064282995845696553E-24, \
             2.98286278427985115447870070202E-22, \
             3.15225456650378141612134668341E-20, \
             2.35188471067581911695767591556E-18, \
             1.28009339132243804163956329526E-16, \
             5.21862372659084752295780851305E-15, \
             1.62834073070972036208430708124E-13, \
             3.95917776694772392723644586425E-12, \
             7.61521725014545135331529567532E-11, \
             1.17361674232154934354250646708E-09, \
             1.4651253164761093549266220038E-08, \
             1.49553293672724706110246169293E-07, \
             1.25834025103118457615784218002E-06, \
             8.7884992308503591814440474067E-06, \
             0.0000512592913578627466082191141274E+00, \
             0.000250983698513062486082362017982E+00, \
             0.00103632909950757766345674174628E+00, \
             0.00362258697853445876066812537162E+00, \
             0.0107560405098791370494651727867E+00, \
             0.0272031289536889184538348212615E+00, \
             0.0587399819640994345496889462518E+00, \
             0.108498349306186840633025845506E+00, \
             0.171685842349083702000727970124E+00, \
             0.232994786062678046650566029333E+00, \
             0.271377424941303977945606508418E+00, \
             0.271377424941303977945606508418E+00, \
             0.232994786062678046650566029333E+00, \
             0.171685842349083702000727970124E+00, \
             0.108498349306186840633025845506E+00, \
             0.0587399819640994345496889462518E+00, \
             0.0272031289536889184538348212615E+00, \
             0.0107560405098791370494651727867E+00, \
             0.00362258697853445876066812537162E+00, \
             0.00103632909950757766345674174628E+00, \
             0.000250983698513062486082362017982E+00, \
             0.0000512592913578627466082191141274E+00, \
             8.7884992308503591814440474067E-06, \
             1.25834025103118457615784218002E-06, \
             1.49553293672724706110246169293E-07, \
             1.4651253164761093549266220038E-08, \
             1.17361674232154934354250646708E-09, \
             7.61521725014545135331529567532E-11, \
             3.95917776694772392723644586425E-12, \
             1.62834073070972036208430708124E-13, \
             5.21862372659084752295780851305E-15, \
             1.28009339132243804163956329526E-16, \
             2.35188471067581911695767591556E-18, \
             3.15225456650378141612134668341E-20, \
             2.98286278427985115447870070202E-22, \
             1.91170688330064282995845696553E-24, \
             7.86179778892591036909999149628E-27, \
             1.92910359546496685030196877907E-29, \
             2.54966089911299925660476658044E-32, \
             1.55739062462976380230933538026E-35, \
             3.42113801125574050432722182815E-39, \
             1.67974799010815921866628833063E-43, \
             5.53570653585694282057546330099E-49 ] )

  elif ( n == 65 ):

    x = np.array ( [ \
           -10.6160229818782811890575602362E+00, \
            -9.98694169167668475289516351866E+00, \
            -9.46632932015538456209230219583E+00, \
            -9.00182332295913301957373193078E+00, \
            -8.57344474441790920512961590649E+00, \
            -8.17090617805258532129873946832E+00, \
            -7.78803908298957078257446963177E+00, \
            -7.42077883436632423648540822493E+00, \
            -7.06626794030689283695626648500E+00, \
            -6.72239982016573443713269171234E+00, \
            -6.38756373978709108766264932629E+00, \
            -6.06049177883150521431844958114E+00, \
            -5.74016182369022552144785845004E+00, \
            -5.42573329769734933377879520007E+00, \
            -5.11650300472141247403405938903E+00, \
            -4.81187385202746476469375701958E+00, \
            -4.51133211136821338520053781440E+00, \
            -4.21443050997195460766227433230E+00, \
            -3.92077540444472380734866143333E+00, \
            -3.63001687763289533380743256995E+00, \
            -3.34184096844683005348576537026E+00, \
            -3.05596348432867100471992904351E+00, \
            -2.77212500515709167382401243242E+00, \
            -2.49008679530393550665251461372E+00, \
            -2.20962741516918436363972079745E+00, \
            -1.93053987597722550177796442890E+00, \
            -1.65262921904032541019598694267E+00, \
            -1.37571042772366833613088581439E+00, \
            -1.09960660005694495033699221150E+00, \
            -0.824147324402412861055989047706E+00, \
            -0.549167211221599184571872835161E+00, \
            -0.274504541753944755855051087074E+00, \
             0.0E+00, \
             0.274504541753944755855051087074E+00, \
             0.549167211221599184571872835161E+00, \
             0.824147324402412861055989047706E+00, \
             1.09960660005694495033699221150E+00, \
             1.37571042772366833613088581439E+00, \
             1.65262921904032541019598694267E+00, \
             1.93053987597722550177796442890E+00, \
             2.20962741516918436363972079745E+00, \
             2.49008679530393550665251461372E+00, \
             2.77212500515709167382401243242E+00, \
             3.05596348432867100471992904351E+00, \
             3.34184096844683005348576537026E+00, \
             3.63001687763289533380743256995E+00, \
             3.92077540444472380734866143333E+00, \
             4.21443050997195460766227433230E+00, \
             4.51133211136821338520053781440E+00, \
             4.81187385202746476469375701958E+00, \
             5.11650300472141247403405938903E+00, \
             5.42573329769734933377879520007E+00, \
             5.74016182369022552144785845004E+00, \
             6.06049177883150521431844958114E+00, \
             6.38756373978709108766264932629E+00, \
             6.72239982016573443713269171234E+00, \
             7.06626794030689283695626648500E+00, \
             7.42077883436632423648540822493E+00, \
             7.78803908298957078257446963177E+00, \
             8.17090617805258532129873946832E+00, \
             8.57344474441790920512961590649E+00, \
             9.00182332295913301957373193078E+00, \
             9.46632932015538456209230219583E+00, \
             9.98694169167668475289516351866E+00, \
            10.6160229818782811890575602362E+00 ] )

    w = np.array ( [ \
            8.25161081325244640518686536873E-50, \
            2.70767584528327632245086261566E-44, \
            5.89628446597893219238447711362E-40, \
            2.8541849032786262808377028501E-36, \
            4.95258625502059879210418105309E-33, \
            3.96328698707468682361835959189E-30, \
            1.70591158107580273148997822331E-27, \
            4.37697419487184691809226004173E-25, \
            7.20161078913500757836854034749E-23, \
            8.0222187354240312838311535001E-21, \
            6.30789104558609987896303941119E-19, \
            3.61819961904286485492939434525E-17, \
            1.55466357223809604941702812296E-15, \
            5.11391748171652449009988302839E-14, \
            1.31125161063902569430172028735E-12, \
            2.66086534779295548413319751434E-11, \
            4.32865615344850974821379264835E-10, \
            5.70758293277877491250362877931E-09, \
            6.15779622145053848599380659292E-08, \
            5.48045603501799498244047819842E-07, \
            4.05224939102373376093012342174E-06, \
            0.0000250453428904958321201946621231E+00, \
            0.000130082916298451204382435919638E+00, \
            0.000570398967523771524725931177791E+00, \
            0.00211998163203684165580510045255E+00, \
            0.00670140453800573713948633700424E+00, \
            0.018069433112703589006399924887E+00, \
            0.0416611087624784398909512089873E+00, \
            0.0823001633697352251543326980867E+00, \
            0.139526139482843953007755621004E+00, \
            0.203250574154441897747728738409E+00, \
            0.254628811852790103887643365928E+00, \
            0.274478226559263167375288621205E+00, \
            0.254628811852790103887643365928E+00, \
            0.203250574154441897747728738409E+00, \
            0.139526139482843953007755621004E+00, \
            0.0823001633697352251543326980867E+00, \
            0.0416611087624784398909512089873E+00, \
            0.018069433112703589006399924887E+00, \
            0.00670140453800573713948633700424E+00, \
            0.00211998163203684165580510045255E+00, \
            0.000570398967523771524725931177791E+00, \
            0.000130082916298451204382435919638E+00, \
            0.0000250453428904958321201946621231E+00, \
            4.05224939102373376093012342174E-06, \
            5.48045603501799498244047819842E-07, \
            6.15779622145053848599380659292E-08, \
            5.70758293277877491250362877931E-09, \
            4.32865615344850974821379264835E-10, \
            2.66086534779295548413319751434E-11, \
            1.31125161063902569430172028735E-12, \
            5.11391748171652449009988302839E-14, \
            1.55466357223809604941702812296E-15, \
            3.61819961904286485492939434525E-17, \
            6.30789104558609987896303941119E-19, \
            8.0222187354240312838311535001E-21, \
            7.20161078913500757836854034749E-23, \
            4.37697419487184691809226004173E-25, \
            1.70591158107580273148997822331E-27, \
            3.96328698707468682361835959189E-30, \
            4.95258625502059879210418105309E-33, \
            2.8541849032786262808377028501E-36, \
            5.89628446597893219238447711362E-40, \
            2.70767584528327632245086261566E-44, \
            8.25161081325244640518686536873E-50 ] )

  elif ( n == 127 ):

    x = np.array ( [ \
            -15.2283381481673509782469544335E+00, \
            -14.6695951588339726327463541129E+00, \
            -14.2090859952848707551682442509E+00, \
            -13.7997222902116766346452467467E+00, \
            -13.4235185900709500624382583219E+00, \
            -13.0712086604746019015839954396E+00, \
            -12.7372356524156863381380039241E+00, \
            -12.4179393788697158054458796241E+00, \
            -12.1107490209477476001321235081E+00, \
            -11.8137721982677271951345841362E+00, \
            -11.5255651125726965991678885886E+00, \
            -11.2449945837855434451943841943E+00, \
            -10.9711505698402474234230402639E+00, \
            -10.7032882010274813476709407447E+00, \
            -10.4407879577727728677425917980E+00, \
            -10.1831274734503438886241264504E+00, \
             -9.92986104951142507368470042737E+00, \
             -9.68060444124747280381507127327E+00, \
             -9.43502333898816501350195985063E+00, \
             -9.19282449884603057157741950525E+00, \
             -8.95374881085654043238078901700E+00, \
             -8.71756580870763073638339995485E+00, \
             -8.48406926898324733260971803400E+00, \
             -8.25307364544571565796941242439E+00, \
             -8.02441115147033755785947397968E+00, \
             -7.79792935138701054208291204556E+00, \
             -7.57348915560834540228349607633E+00, \
             -7.35096313922690527019612580437E+00, \
             -7.13023412203507106680640257134E+00, \
             -6.91119396154657131974656331094E+00, \
             -6.69374252087582941900744173817E+00, \
             -6.47778678116453654481449038215E+00, \
             -6.26324007427373543456097238571E+00, \
             -6.05002141614198456944654744824E+00, \
             -5.83805492487741873866016908078E+00, \
             -5.62726931054648166594234557949E+00, \
             -5.41759742592432407228484258729E+00, \
             -5.20897586931539835875702583722E+00, \
             -5.00134463203863600385208091074E+00, \
             -4.79464678437649250097485099309E+00, \
             -4.58882819476983729516064850312E+00, \
             -4.38383727784647362942537444075E+00, \
             -4.17962476753520313494211898924E+00, \
             -3.97614351206733559160358141959E+00, \
             -3.77334828812505267210046784001E+00, \
             -3.57119563177821804471997564852E+00, \
             -3.36964368417173978966436292400E+00, \
             -3.16865205019536301918577982615E+00, \
             -2.96818166859559102677616495215E+00, \
             -2.76819469218240588012265459589E+00, \
             -2.56865437694735017231440130224E+00, \
             -2.36952497904904010800124746457E+00, \
             -2.17077165874115068794984980837E+00, \
             -1.97236039041950200793247432276E+00, \
             -1.77425787805167915846764421037E+00, \
             -1.57643147532678013155195976219E+00, \
             -1.37884910992617780914415570537E+00, \
             -1.18147921137006858486785835984E+00, \
             -0.984290641940272777265689842138E+00, \
             -0.787252630218250341515968318790E+00, \
             -0.590334706809421021422304393461E+00, \
             -0.393506641851301365680378262002E+00, \
             -0.196738383924232519642722397371E+00, \
              0.0E+00, \
              0.196738383924232519642722397371E+00, \
              0.393506641851301365680378262002E+00, \
              0.590334706809421021422304393461E+00, \
              0.787252630218250341515968318790E+00, \
              0.984290641940272777265689842138E+00, \
              1.18147921137006858486785835984E+00, \
              1.37884910992617780914415570537E+00, \
              1.57643147532678013155195976219E+00, \
              1.77425787805167915846764421037E+00, \
              1.97236039041950200793247432276E+00, \
              2.17077165874115068794984980837E+00, \
              2.36952497904904010800124746457E+00, \
              2.56865437694735017231440130224E+00, \
              2.76819469218240588012265459589E+00, \
              2.96818166859559102677616495215E+00, \
              3.16865205019536301918577982615E+00, \
              3.36964368417173978966436292400E+00, \
              3.57119563177821804471997564852E+00, \
              3.77334828812505267210046784001E+00, \
              3.97614351206733559160358141959E+00, \
              4.17962476753520313494211898924E+00, \
              4.38383727784647362942537444075E+00, \
              4.58882819476983729516064850312E+00, \
              4.79464678437649250097485099309E+00, \
              5.00134463203863600385208091074E+00, \
              5.20897586931539835875702583722E+00, \
              5.41759742592432407228484258729E+00, \
              5.62726931054648166594234557949E+00, \
              5.83805492487741873866016908078E+00, \
              6.05002141614198456944654744824E+00, \
              6.26324007427373543456097238571E+00, \
              6.47778678116453654481449038215E+00, \
              6.69374252087582941900744173817E+00, \
              6.91119396154657131974656331094E+00, \
              7.13023412203507106680640257134E+00, \
              7.35096313922690527019612580437E+00, \
              7.57348915560834540228349607633E+00, \
              7.79792935138701054208291204556E+00, \
              8.02441115147033755785947397968E+00, \
              8.25307364544571565796941242439E+00, \
              8.48406926898324733260971803400E+00, \
              8.71756580870763073638339995485E+00, \
              8.95374881085654043238078901700E+00, \
              9.19282449884603057157741950525E+00, \
              9.43502333898816501350195985063E+00, \
              9.68060444124747280381507127327E+00, \
              9.92986104951142507368470042737E+00, \
             10.1831274734503438886241264504E+00, \
             10.4407879577727728677425917980E+00, \
             10.7032882010274813476709407447E+00, \
             10.9711505698402474234230402639E+00, \
             11.2449945837855434451943841943E+00, \
             11.5255651125726965991678885886E+00, \
             11.8137721982677271951345841362E+00, \
             12.1107490209477476001321235081E+00, \
             12.4179393788697158054458796241E+00, \
             12.7372356524156863381380039241E+00, \
             13.0712086604746019015839954396E+00, \
             13.4235185900709500624382583219E+00, \
             13.7997222902116766346452467467E+00, \
             14.2090859952848707551682442509E+00, \
             14.6695951588339726327463541129E+00, \
             15.2283381481673509782469544335E+00 ] )

    w = np.array ( [ \
           1.25044975770895101066558695394E-101, \
           1.72727980594728851329952877284E-94, \
           8.93216815722645216635320162557E-89, \
           7.7306185241134158744827181222E-84, \
           2.01439576527109443920782513994E-79, \
           2.15037147336771602203551878273E-75, \
           1.13419242086298913875376620343E-71, \
             3.34891390118992716444169809114E-68, \
             6.04865489642049179016214753843E-65, \
              7.13750929465743002965122123123E-62, \
              5.78845633750656959788340019085E-59, \
            3.3581166223962736386929935773E-56, \
            1.4394641949298720336141068619E-53, \
            4.68218083833618292793410025836E-51, \
            1.18170544407210392716367665268E-48, \
            2.35816591560823143778744566357E-46, \
            3.78144279409152203964384313149E-44, \
              4.9411031115925407477456893331E-42, \
              5.32553037755907921458489847863E-40, \
              4.78543906802804099967221020647E-38, \
              3.61918834460649868835433546523E-36, \
              2.3232083386415854084664074623E-34, \
            1.27533314110484056196532640642E-32, \
            6.02777538509463291699314327193E-31, \
            2.4679773241854004762148469348E-29, \
            8.8019567691972403392314252914E-28, \
            2.74824892121260880467531987939E-26, \
              7.54682189033203465872349657723E-25, \
              1.83031346363374264415878982576E-23, \
              3.93559908609832906838466602268E-22, \
              7.52931616388155067444192947319E-21, \
              1.28579977867628696999762170542E-19, \
              1.96593268885070384943390296306E-18, \
            2.69865119072980851232572568063E-17, \
            3.33444143033026256341061235315E-16, \
            3.71733031252663248624409938613E-15, \
            3.74739544729563577089986076081E-14, \
              3.42300944935037851188976963928E-13, \
              2.83853037250817094975750489262E-12, \
              2.14069202905212884993201956606E-11, \
              1.47063312734774830028408333227E-10, \
              9.21739409677215086782446989876E-10, \
              5.27816639371369729333040255118E-09, \
              2.76504970450371674155194812923E-08, \
            1.32678558425807549298485884004E-07, \
            5.83809442762947462901022315301E-07, \
            2.35815617248490159838145978859E-06, \
              8.75244680345528247507614056972E-06, \
              0.0000298767905360019901790649251988E+00, \
              0.0000938744357203646866361259710004E+00, \
              0.000271707626280157286781639661883E+00, \
              0.000724939297427239633212185817821E+00, \
              0.0017841208326818955520088211458E+00, \
              0.00405248551861722466559241860023E+00, \
              0.00850002630418086349941683729112E+00, \
            0.0164711422416609467530350356258E+00, \
            0.0294992962483054353948393364098E+00, \
              0.0488473871144520262535428484316E+00, \
              0.074807989768816537216026182806E+00, \
              0.10598520508123912472195529192E+00, \
              0.138939453090947794093360848265E+00, \
              0.168562360742603870987330592834E+00, \
              0.189278495801793364889704841035E+00, \
              0.196733406888845140995323677102E+00, \
              0.189278495801793364889704841035E+00, \
            0.168562360742603870987330592834E+00, \
            0.138939453090947794093360848265E+00, \
              0.10598520508123912472195529192E+00, \
              0.074807989768816537216026182806E+00, \
              0.0488473871144520262535428484316E+00, \
              0.0294992962483054353948393364098E+00, \
              0.0164711422416609467530350356258E+00, \
              0.00850002630418086349941683729112E+00, \
              0.00405248551861722466559241860023E+00, \
              0.0017841208326818955520088211458E+00, \
            0.000724939297427239633212185817821E+00, \
            0.000271707626280157286781639661883E+00, \
              0.0000938744357203646866361259710004E+00, \
              0.0000298767905360019901790649251988E+00, \
                8.75244680345528247507614056972E-06, \
                2.35815617248490159838145978859E-06, \
                5.83809442762947462901022315301E-07, \
                1.32678558425807549298485884004E-07, \
                2.76504970450371674155194812923E-08, \
                5.27816639371369729333040255118E-09, \
              9.21739409677215086782446989876E-10, \
              1.47063312734774830028408333227E-10, \
              2.14069202905212884993201956606E-11, \
                2.83853037250817094975750489262E-12, \
                3.42300944935037851188976963928E-13, \
                3.74739544729563577089986076081E-14, \
                3.71733031252663248624409938613E-15, \
                3.33444143033026256341061235315E-16, \
                2.69865119072980851232572568063E-17, \
                1.96593268885070384943390296306E-18, \
              1.28579977867628696999762170542E-19, \
              7.52931616388155067444192947319E-21, \
              3.93559908609832906838466602268E-22, \
              1.83031346363374264415878982576E-23, \
               7.54682189033203465872349657723E-25, \
                 2.74824892121260880467531987939E-26, \
                 8.8019567691972403392314252914E-28, \
                 2.4679773241854004762148469348E-29, \
                 6.02777538509463291699314327193E-31, \
                 1.27533314110484056196532640642E-32, \
               2.3232083386415854084664074623E-34, \
               3.61918834460649868835433546523E-36, \
               4.78543906802804099967221020647E-38, \
               5.32553037755907921458489847863E-40, \
               4.9411031115925407477456893331E-42, \
               3.78144279409152203964384313149E-44, \
                 2.35816591560823143778744566357E-46, \
                 1.18170544407210392716367665268E-48, \
                 4.68218083833618292793410025836E-51, \
                 1.4394641949298720336141068619E-53, \
               3.3581166223962736386929935773E-56, \
               5.78845633750656959788340019085E-59, \
               7.13750929465743002965122123123E-62, \
               6.04865489642049179016214753843E-65, \
               3.34891390118992716444169809114E-68, \
               1.13419242086298913875376620343E-71, \
               2.15037147336771602203551878273E-75, \
             2.01439576527109443920782513994E-79, \
             7.7306185241134158744827181222E-84, \
             8.93216815722645216635320162557E-89, \
             1.72727980594728851329952877284E-94, \
             1.25044975770895101066558695394E-101 ] )

  elif ( n == 128 ):

    x = np.array ( [ \
           -15.2918197668827409717467886552E+00, \
           -14.7338424735892990556131447177E+00, \
           -14.2739813047878355625094356564E+00, \
           -13.8652069844762415897768433203E+00, \
           -13.4895564126231418263791177750E+00, \
           -13.1377747880276511010650586719E+00, \
           -12.8043120820671312950137141654E+00, \
             -12.4855125853494481606990566084E+00, \
             -12.1788086198312463132740693095E+00, \
              -11.8823101188783115808359168093E+00, \
              -11.5945750547414517467820845908E+00, \
            -11.3144716442899779172120028451E+00, \
            -11.0410909760196333842428986719E+00, \
            -10.7736891151614406713116609896E+00, \
            -10.5116473299148686173941369279E+00, \
            -10.2544439284709307170245436605E+00, \
            -10.0016337989301228460111363000E+00, \
              -9.75283321343916867454942614151E+00, \
              -9.50770832327905657695490182674E+00, \
              -9.26596630029617592185364037517E+00, \
              -9.02734841339478834482665573280E+00, \
              -8.79162454488868640635040291427E+00, \
            -8.55858879506450828896030380072E+00, \
            -8.32805592079014664500802003672E+00, \
            -8.09985842150789607545794348110E+00, \
            -7.87384413353543446678710891884E+00, \
            -7.64987422768100656113184995327E+00, \
              -7.42782152995230111565739552073E+00, \
              -7.20756910338733385441779947109E+00, \
              -6.98900904264477401185223744438E+00, \
              -6.77204144325592885820688621877E+00, \
              -6.55657351526448288962578894289E+00, \
              -6.34251881700177947172938955573E+00, \
            -6.12979658942216202462059597877E+00, \
            -5.91833117508581167511681743446E+00, \
            -5.70805150876808626177490879113E+00, \
            -5.49889066897390948452218926009E+00, \
              -5.29078548147717957643674180866E+00, \
              -5.08367616748933990673505368300E+00, \
              -4.87750603026481441216755173491E+00, \
              -4.67222117493263892214567470373E+00, \
              -4.46777025714858268344631831723E+00, \
              -4.26410425682551915674979043600E+00, \
              -4.06117627374927282427754765790E+00, \
            -3.85894134234428182659062673118E+00, \
            -3.65735626323530809623058740618E+00, \
            -3.45637944957173748220943445337E+00, \
              -3.25597078635065934665290567700E+00, \
              -3.05609150120268005595784091684E+00, \
              -2.85670404529740528265184910544E+00, \
              -2.65777198318948399631081621992E+00, \
              -2.45925989056573940193677619199E+00, \
              -2.26113325897306228028420817752E+00, \
              -2.06335840670856597768175136750E+00, \
              -1.86590239514059869664912407799E+00, \
            -1.66873294980372363048660121191E+00, \
            -1.47181838567448600067837560546E+00, \
              -1.27512753608915832143251082623E+00, \
              -1.07862968481090893047100757570E+00, \
              -0.882294500792981406000508343227E+00, \
              -0.686091975217334872045286432691E+00, \
              -0.489992360415458918089044385637E+00, \
              -0.293966110300295702813351867404E+00, \
              -0.0979838219558189543137713246862E+00, \
              0.0979838219558189543137713246862E+00, \
            0.293966110300295702813351867404E+00, \
            0.489992360415458918089044385637E+00, \
              0.686091975217334872045286432691E+00, \
              0.882294500792981406000508343227E+00, \
              1.07862968481090893047100757570E+00, \
              1.27512753608915832143251082623E+00, \
              1.47181838567448600067837560546E+00, \
              1.66873294980372363048660121191E+00, \
              1.86590239514059869664912407799E+00, \
              2.06335840670856597768175136750E+00, \
            2.26113325897306228028420817752E+00, \
            2.45925989056573940193677619199E+00, \
              2.65777198318948399631081621992E+00, \
              2.85670404529740528265184910544E+00, \
                3.05609150120268005595784091684E+00, \
                3.25597078635065934665290567700E+00, \
                3.45637944957173748220943445337E+00, \
                3.65735626323530809623058740618E+00, \
                3.85894134234428182659062673118E+00, \
                4.06117627374927282427754765790E+00, \
              4.26410425682551915674979043600E+00, \
              4.46777025714858268344631831723E+00, \
              4.67222117493263892214567470373E+00, \
                4.87750603026481441216755173491E+00, \
                5.08367616748933990673505368300E+00, \
                5.29078548147717957643674180866E+00, \
                5.49889066897390948452218926009E+00, \
                5.70805150876808626177490879113E+00, \
                5.91833117508581167511681743446E+00, \
                6.12979658942216202462059597877E+00, \
              6.34251881700177947172938955573E+00, \
              6.55657351526448288962578894289E+00, \
              6.77204144325592885820688621877E+00, \
              6.98900904264477401185223744438E+00, \
               7.20756910338733385441779947109E+00, \
                 7.42782152995230111565739552073E+00, \
                 7.64987422768100656113184995327E+00, \
                 7.87384413353543446678710891884E+00, \
                 8.09985842150789607545794348110E+00, \
                 8.32805592079014664500802003672E+00, \
               8.55858879506450828896030380072E+00, \
               8.79162454488868640635040291427E+00, \
               9.02734841339478834482665573280E+00, \
               9.26596630029617592185364037517E+00, \
               9.50770832327905657695490182674E+00, \
               9.75283321343916867454942614151E+00, \
                 10.0016337989301228460111363000E+00, \
                 10.2544439284709307170245436605E+00, \
                 10.5116473299148686173941369279E+00, \
                 10.7736891151614406713116609896E+00, \
               11.0410909760196333842428986719E+00, \
               11.3144716442899779172120028451E+00, \
               11.5945750547414517467820845908E+00, \
               11.8823101188783115808359168093E+00, \
               12.1788086198312463132740693095E+00, \
               12.4855125853494481606990566084E+00, \
               12.8043120820671312950137141654E+00, \
             13.1377747880276511010650586719E+00, \
             13.4895564126231418263791177750E+00, \
             13.8652069844762415897768433203E+00, \
             14.2739813047878355625094356564E+00, \
             14.7338424735892990556131447177E+00, \
               15.2918197668827409717467886552E+00 ] )

    w = np.array ( [ \
           1.79906598010928472082336338805E-102, \
           2.60817240240911107924885148459E-95, \
           1.40468977131508863479865725345E-89, \
           1.2612494833385383033093221663E-84, \
           3.4012300869366371268669286673E-80, \
           3.75121586880472499656274624235E-76, \
           2.04158579724398501580069247379E-72, \
             6.21424416183031366240930730224E-69, \
             1.15615516409637521334725409468E-65, \
              1.40446725774048726044186592003E-62, \
              1.17197850121298051738559888373E-59, \
            6.9930729240519559879874741506E-57, \
            3.08207738333929868710425541163E-54, \
            1.03048625205569473422672330856E-51, \
            2.67274375173606785452021989916E-49, \
            5.48021702897879649820616283051E-47, \
            9.02804013878664400917961564574E-45, \
              1.21177953413059190735434940091E-42, \
              1.34149748176436936696556841563E-40, \
              1.2380855579763680376188381669E-38, \
              9.6167080679675069775952182446E-37, \
              6.33991352636648906076753997388E-35, \
            3.57437889587942107216457034803E-33, \
            1.73510302028206120881601688138E-31, \
            7.29654500676840425381868704321E-30, \
            2.67292362005807324017266437183E-28, \
            8.5728304837693537445493254974E-27, \
              2.41840345964766496960390574396E-25, \
              6.02598403200645428864656987226E-24, \
              1.33136785903358960440599429474E-22, \
              2.61745758393481115586873166674E-21, \
              4.59400767732972159221172605389E-20, \
              7.22010731692829201964437734131E-19, \
            1.01893323042329252403658204469E-17, \
            1.2945481593393715343954569556E-16, \
            1.4842238375138564829118955689E-15, \
            1.53904973035354581424981070383E-14, \
              1.44634732119041656320590928428E-13, \
              1.23421448660055669081623604437E-12, \
              9.58031650873585770862066358548E-12, \
              6.77578048777455378630839649193E-11, \
              4.37318665984840344563217253619E-10, \
              2.57939722942639480114980569527E-9, \
              1.39219071529351788119578816175E-8, \
            6.88458112215435009064406266312E-8, \
            3.12287298617890308197944991751E-7, \
            1.30074700323819923351375586698E-6, \
              4.97992453259098701134099270598E-6, \
              0.0000175404858480939050383677619791E+00, \
              0.0000568874376004024109270187885882E+00, \
              0.000170014088262809409409897155763E+00, \
              0.000468551537808411365479802126842E+00, \
              0.00119156381445716723911680561041E+00, \
              0.00279783940160578927319080368252E+00, \
              0.00606886240692588762066801419927E+00, \
            0.0121669188644693394910166328856E+00, \
            0.0225543101678244224102498222492E+00, \
              0.0386739548106369026550248867136E+00, \
              0.061360721004490065664651069257E+00, \
              0.090108678376448919548057439804E+00, \
              0.122503273164135694618664605611E+00, \
              0.154210435298354383363527713284E+00, \
              0.179773083907799264988697956102E+00, \
              0.194097611864087756977697028723E+00, \
              0.194097611864087756977697028723E+00, \
            0.179773083907799264988697956102E+00, \
            0.154210435298354383363527713284E+00, \
              0.122503273164135694618664605611E+00, \
              0.090108678376448919548057439804E+00, \
              0.061360721004490065664651069257E+00, \
              0.0386739548106369026550248867136E+00, \
              0.0225543101678244224102498222492E+00, \
              0.0121669188644693394910166328856E+00, \
              0.00606886240692588762066801419927E+00, \
              0.00279783940160578927319080368252E+00, \
            0.00119156381445716723911680561041E+00, \
            0.000468551537808411365479802126842E+00, \
              0.000170014088262809409409897155763E+00, \
              0.0000568874376004024109270187885882E+00, \
                0.0000175404858480939050383677619791E+00, \
                4.97992453259098701134099270598E-06, \
                1.30074700323819923351375586698E-06, \
                3.12287298617890308197944991751E-07, \
                6.88458112215435009064406266312E-08, \
                1.39219071529351788119578816175E-08, \
              2.57939722942639480114980569527E-09, \
              4.37318665984840344563217253619E-10, \
              6.77578048777455378630839649193E-11, \
                9.58031650873585770862066358548E-12, \
                1.23421448660055669081623604437E-12, \
                1.44634732119041656320590928428E-13, \
                1.53904973035354581424981070383E-14, \
                1.4842238375138564829118955689E-15, \
                1.2945481593393715343954569556E-16, \
                1.01893323042329252403658204469E-17, \
              7.22010731692829201964437734131E-19, \
              4.59400767732972159221172605389E-20, \
              2.61745758393481115586873166674E-21, \
              1.33136785903358960440599429474E-22, \
               6.02598403200645428864656987226E-24, \
                 2.41840345964766496960390574396E-25, \
                 8.5728304837693537445493254974E-27, \
                 2.67292362005807324017266437183E-28, \
                 7.29654500676840425381868704321E-30, \
                 1.73510302028206120881601688138E-31, \
               3.57437889587942107216457034803E-33, \
               6.33991352636648906076753997388E-35, \
               9.6167080679675069775952182446E-37, \
               1.2380855579763680376188381669E-38, \
               1.34149748176436936696556841563E-40, \
               1.21177953413059190735434940091E-42, \
                 9.02804013878664400917961564574E-45, \
                 5.48021702897879649820616283051E-47, \
                 2.67274375173606785452021989916E-49, \
                 1.03048625205569473422672330856E-51, \
               3.08207738333929868710425541163E-54, \
               6.9930729240519559879874741506E-57, \
               1.17197850121298051738559888373E-59, \
               1.40446725774048726044186592003E-62, \
               1.15615516409637521334725409468E-65, \
               6.21424416183031366240930730224E-69, \
               2.04158579724398501580069247379E-72, \
             3.75121586880472499656274624235E-76, \
             3.4012300869366371268669286673E-80, \
             1.2612494833385383033093221663E-84, \
             1.40468977131508863479865725345E-89, \
             2.60817240240911107924885148459E-95, \
             1.79906598010928472082336338805E-102 ] )

  elif ( n == 129 ):

    x = np.array ( [ \
           -15.3550496746831285549167746019E+00, \
           -14.7978308964903080628845608050E+00, \
           -14.3386115290089672811362217078E+00, \
           -13.9304208664791805435265533989E+00, \
           -13.5553179661308567022816946453E+00, \
           -13.2040593596741921982903144147E+00, \
           -12.8711017789036282758938040681E+00, \
             -12.5527939524445397878411009214E+00, \
             -12.2465713150240016840404064819E+00, \
              -11.9505460927691823148587203418E+00, \
              -11.6632780120689523111895976521E+00, \
            -11.3836366735119364919041401601E+00, \
            -11.1107142851416459382067369906E+00, \
            -10.8437678377155441232588867872E+00, \
            -10.5821793789735138638177686355E+00, \
            -10.3254278845735933555309803756E+00, \
            -10.0730688225840385168071109595E+00, \
              -9.82471897583315292981163227664E+00, \
              -9.58004495076523054718996925368E+00, \
              -9.33875432946329683313144773753E+00, \
              -9.10058875441877630705419698871E+00, \
              -8.86531845144460445006059884245E+00, \
            -8.63273783950843552405601767759E+00, \
            -8.40266197362535012572889592790E+00, \
            -8.17492363437398978801516910338E+00, \
            -7.94937092512605027069441566240E+00, \
            -7.72586527212128476858225880726E+00, \
              -7.50427974726352240601473698475E+00, \
              -7.28449765174015372725258835236E+00, \
              -7.06641131216039069912389691607E+00, \
              -6.84992105116014925339717178568E+00, \
              -6.63493430223598850302862096202E+00, \
              -6.42136484458510366813184121466E+00, \
            -6.20913213839958724139275362341E+00, \
            -5.99816074472179863235247556956E+00, \
            -5.78837981685588271189500366573E+00, \
            -5.57972265262736517721195076411E+00, \
              -5.37212629862206810544406569124E+00, \
              -5.16553119901808798749445925424E+00, \
              -4.95988088282680494441019859192E+00, \
              -4.75512168433945660698412105871E+00, \
              -4.55120249237992751786552441506E+00, \
              -4.34807452462720039287086617988E+00, \
              -4.14569112381985885943227755134E+00, \
            -3.94400757311174034591077592589E+00, \
            -3.74298092822942697020355662873E+00, \
            -3.54256986440235708810942555303E+00, \
              -3.34273453630584653564135188865E+00, \
              -3.14343644948499981855157130224E+00, \
              -2.94463834192045889859029200431E+00, \
              -2.74630407456093830886162508356E+00, \
              -2.54839852978722422234239962660E+00, \
              -2.35088751689161374336515868011E+00, \
              -2.15373768375879465132813086025E+00, \
              -1.95691643402151503173496953711E+00, \
            -1.76039184903921457004681976795E+00, \
            -1.56413261411186298656139617983E+00, \
              -1.36810794839605047973791359079E+00, \
              -1.17228753803712318264391216760E+00, \
              -0.976641472070867557126534700881E+00, \
              -0.781140180681760289238140546741E+00, \
              -0.585754375432805697119652981369E+00, \
              -0.390454991105046004780513867383E+00, \
              -0.195213128803407573801607754230E+00, \
              0.0E+00, \
            0.195213128803407573801607754230E+00, \
            0.390454991105046004780513867383E+00, \
              0.585754375432805697119652981369E+00, \
              0.781140180681760289238140546741E+00, \
              0.976641472070867557126534700881E+00, \
              1.17228753803712318264391216760E+00, \
              1.36810794839605047973791359079E+00, \
              1.56413261411186298656139617983E+00, \
              1.76039184903921457004681976795E+00, \
              1.95691643402151503173496953711E+00, \
            2.15373768375879465132813086025E+00, \
            2.35088751689161374336515868011E+00, \
              2.54839852978722422234239962660E+00, \
              2.74630407456093830886162508356E+00, \
                2.94463834192045889859029200431E+00, \
                3.14343644948499981855157130224E+00, \
                3.34273453630584653564135188865E+00, \
                3.54256986440235708810942555303E+00, \
                3.74298092822942697020355662873E+00, \
                3.94400757311174034591077592589E+00, \
              4.14569112381985885943227755134E+00, \
              4.34807452462720039287086617988E+00, \
              4.55120249237992751786552441506E+00, \
                4.75512168433945660698412105871E+00, \
                4.95988088282680494441019859192E+00, \
                5.16553119901808798749445925424E+00, \
                5.37212629862206810544406569124E+00, \
                5.57972265262736517721195076411E+00, \
                5.78837981685588271189500366573E+00, \
                5.99816074472179863235247556956E+00, \
              6.20913213839958724139275362341E+00, \
              6.42136484458510366813184121466E+00, \
              6.63493430223598850302862096202E+00, \
              6.84992105116014925339717178568E+00, \
               7.06641131216039069912389691607E+00, \
                 7.28449765174015372725258835236E+00, \
                 7.50427974726352240601473698475E+00, \
                 7.72586527212128476858225880726E+00, \
                 7.94937092512605027069441566240E+00, \
                 8.17492363437398978801516910338E+00, \
               8.40266197362535012572889592790E+00, \
               8.63273783950843552405601767759E+00, \
               8.86531845144460445006059884245E+00, \
               9.10058875441877630705419698871E+00, \
               9.33875432946329683313144773753E+00, \
               9.58004495076523054718996925368E+00, \
                 9.82471897583315292981163227664E+00, \
                 10.0730688225840385168071109595E+00, \
                 10.3254278845735933555309803756E+00, \
                 10.5821793789735138638177686355E+00, \
               10.8437678377155441232588867872E+00, \
               11.1107142851416459382067369906E+00, \
               11.3836366735119364919041401601E+00, \
               11.6632780120689523111895976521E+00, \
               11.9505460927691823148587203418E+00, \
               12.2465713150240016840404064819E+00, \
               12.5527939524445397878411009214E+00, \
             12.8711017789036282758938040681E+00, \
             13.2040593596741921982903144147E+00, \
             13.5553179661308567022816946453E+00, \
             13.9304208664791805435265533989E+00, \
             14.3386115290089672811362217078E+00, \
               14.7978308964903080628845608050E+00, \
               15.3550496746831285549167746019E+00 ] )

    w = np.array ( [ \
           2.58755395082114927399064139631E-103, \
           3.93601845908067608811461078697E-96, \
           2.20725529577484588586177997021E-90, \
           2.05563087297774646200941835216E-85, \
           5.73584763407311509769038083955E-81, \
           6.53456499014096713882711627986E-77, \
           3.66903606454555600244832281797E-73, \
             1.15105101975113879079427442365E-69, \
             2.20553774145133363585421051568E-66, \
              2.75763663311195533797446164671E-63, \
              2.36731747071610805241477009401E-60, \
            1.45257860403230704544333281907E-57, \
            6.58119121529392093666305170751E-55, \
            2.26137732951303228667152914802E-52, \
            6.02643011329776195986432204924E-50, \
            1.26938407638088455004457398255E-47, \
            2.14791778799787733305388107076E-45, \
              2.96092183537878053158423564486E-43, \
              3.36616090532826422441501486485E-41, \
              3.19014783528482307711547124192E-39, \
              2.54439796712780366695746038013E-37, \
              1.72239465322100711581154624691E-35, \
            9.97105538735197785176257533162E-34, \
            4.97009943352064894027841342072E-32, \
            2.14620630607238052957787041268E-30, \
            8.07377921555793000987040030256E-29, \
            2.65936924028161851577004868287E-27, \
              7.70515053183270746145645250031E-26, \
              1.97204966381589933881729892459E-24, \
              4.47579713475437089012921294273E-23, \
              9.0403370335874459959906960673E-22, \
              1.63036407035294103578729410788E-20, \
              2.63320491826449443345354482912E-19, \
            3.81944198027838553902522199764E-18, \
            4.98833273307808866457667338365E-17, \
            5.88022772755071728094452091844E-16, \
            6.27023947714728862011748531319E-15, \
              6.06072571359080078068964155295E-14, \
              5.32049070753884105044682362639E-13, \
              4.24955065877498808023415505556E-12, \
              3.09330203932473692244204789801E-11, \
              2.05524352987860630455845773203E-10, \
              1.2482251818681431772545606389E-09, \
              6.93896714453731562418029048785E-09, \
            3.53518234605234028369262582274E-08, \
            1.65252704577539544523562160076E-07, \
            7.09535030601389014268064639021E-07, \
              2.80106033677073567813925250808E-06, \
              0.0000101764715414468349837840217278E+00, \
              0.0000340541841724020078441933069804E+00, \
              0.000105047486997647220847004754607E+00, \
              0.000298922505941519029186629138321E+00, \
              0.000785197220610268688197653195861E+00, \
              0.00190506673927936544347937172051E+00, \
              0.00427162074179231114560048384305E+00, \
            0.00885609926394363549300290104701E+00, \
            0.0169845117091580731620255503875E+00, \
              0.0301436534848915408822025025241E+00, \
              0.0495245901368945546436264039895E+00, \
              0.0753454506416603410859342903275E+00, \
              0.106172669789632918045101372957E+00, \
              0.138604146980788427972651263139E+00, \
              0.167654732143619067997522798882E+00, \
              0.187923095463858179335367694936E+00, \
              0.195208341719164170910088609838E+00, \
            0.187923095463858179335367694936E+00, \
            0.167654732143619067997522798882E+00, \
              0.138604146980788427972651263139E+00, \
              0.106172669789632918045101372957E+00, \
              0.0753454506416603410859342903275E+00, \
              0.0495245901368945546436264039895E+00, \
              0.0301436534848915408822025025241E+00, \
              0.0169845117091580731620255503875E+00, \
              0.00885609926394363549300290104701E+00, \
              0.00427162074179231114560048384305E+00, \
            0.00190506673927936544347937172051E+00, \
            0.000785197220610268688197653195861E+00, \
              0.000298922505941519029186629138321E+00, \
              0.000105047486997647220847004754607E+00, \
                0.0000340541841724020078441933069804E+00, \
                0.0000101764715414468349837840217278E+00, \
                2.80106033677073567813925250808E-06, \
                7.09535030601389014268064639021E-07, \
                1.65252704577539544523562160076E-07, \
                3.53518234605234028369262582274E-08, \
              6.93896714453731562418029048785E-09, \
              1.2482251818681431772545606389E-09, \
              2.05524352987860630455845773203E-10, \
                3.09330203932473692244204789801E-11, \
                4.24955065877498808023415505556E-12, \
                5.32049070753884105044682362639E-13, \
                6.06072571359080078068964155295E-14, \
                6.27023947714728862011748531319E-15, \
                5.88022772755071728094452091844E-16, \
                4.98833273307808866457667338365E-17, \
              3.81944198027838553902522199764E-18, \
              2.63320491826449443345354482912E-19, \
              1.63036407035294103578729410788E-20, \
              9.0403370335874459959906960673E-22, \
               4.47579713475437089012921294273E-23, \
                 1.97204966381589933881729892459E-24, \
                 7.70515053183270746145645250031E-26, \
                 2.65936924028161851577004868287E-27, \
                 8.07377921555793000987040030256E-29, \
                 2.14620630607238052957787041268E-30, \
               4.97009943352064894027841342072E-32, \
               9.97105538735197785176257533162E-34, \
               1.72239465322100711581154624691E-35, \
               2.54439796712780366695746038013E-37, \
               3.19014783528482307711547124192E-39, \
               3.36616090532826422441501486485E-41, \
                 2.96092183537878053158423564486E-43, \
                 2.14791778799787733305388107076E-45, \
                 1.26938407638088455004457398255E-47, \
                 6.02643011329776195986432204924E-50, \
               2.26137732951303228667152914802E-52, \
               6.58119121529392093666305170751E-55, \
               1.45257860403230704544333281907E-57, \
               2.36731747071610805241477009401E-60, \
               2.75763663311195533797446164671E-63, \
               2.20553774145133363585421051568E-66, \
               1.15105101975113879079427442365E-69, \
             3.66903606454555600244832281797E-73, \
             6.53456499014096713882711627986E-77, \
             5.73584763407311509769038083955E-81, \
             2.05563087297774646200941835216E-85, \
             2.20725529577484588586177997021E-90, \
               3.93601845908067608811461078697E-96, \
               2.58755395082114927399064139631E-103 ] )
    
  else:

    print ( '' )
    print ( 'HERMITE_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1:20, 31/32/33, 63/64/65, 127/128/129.' )
    raise Exception ( 'HERMITE_SET(): Fatal error!' )

  return x, w

def hermite_set_test ( ):

#*****************************************************************************80
#
## hermite_set_test() tests hermite_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_set_test():' )
  print ( '  hermite_set() sets a Hermite quadrature rule over (-oo,+oo).' )
  print ( '' )
  print ( '  Index       X             W' )
  print ( '' )

  for n in range ( 1, 11 ):

    x, w = hermite_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def hyper_2f1_values ( n_data ):

#*****************************************************************************80
#
## hyper_2f1_values() returns some values of the hypergeometric 2F1 function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      fx = Hypergeometric2F1 [ a, b, c, x ]
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
#    real A, B, C, X, the parameters.
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
## hyper_2f1_values_test() demonstrates the use of HYPER_2F1_VALUES.
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
  print ( '' )
  print ( 'HYPER_2F1_VALUES_TEST:' )
  print ( '  HYPER_2F1_VALUES stores values of the hypergeometric function 2F1' )
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

def imtqlx ( n, d, e, z ):

#*****************************************************************************80
#
## imtqlx() diagonalizes a symmetric tridiagonal matrix.
#
#  Discussion:
#
#    This routine is a slightly modified version of the EISPACK routine to
#    perform the implicit QL algorithm on a symmetric tridiagonal matrix.
#
#    The authors thank the authors of EISPACK for permission to use this
#    routine.
#
#    It has been modified to produce the product Q' * Z, where Z is an input
#    vector and Q is the orthogonal matrix diagonalizing the input matrix.
#    The changes consist (essentially) of applying the orthogonal 
#    transformations directly to Z as they are generated.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#    Roger Martin, James Wilkinson,
#    The Implicit QL Algorithm,
#    Numerische Mathematik,
#    Volume 12, Number 5, December 1968, pages 377-383.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real D(N), the diagonal entries of the matrix.
#
#    real E(N), the subdiagonal entries of the
#    matrix, in entries E(1) through E(N-1). 
#
#    real Z(N), a vector to be operated on.
#
#  Output:
#
#    real LAM(N), the diagonal entries of the diagonalized matrix.
#
#    real QTZ(N), the value of Q' * Z, where Q is the matrix that 
#    diagonalizes the input symmetric tridiagonal matrix.
#
  import numpy as np

  lam = np.zeros ( n )
  for i in range ( 0, n ):
    lam[i] = d[i]

  qtz = np.zeros ( n )
  for i in range ( 0, n ):
    qtz[i] = z[i]

  if ( n == 1 ):
    return lam, qtz

  itn = 30

  prec = np.finfo(float).eps

  e[n-1] = 0.0

  for l in range ( 1, n + 1 ):

    j = 0

    while ( True ):

      for m in range ( l, n + 1 ):

        if ( m == n ):
          break

        if ( abs ( e[m-1] ) <= prec * ( abs ( lam[m-1] ) + abs ( lam[m] ) ) ):
          break

      p = lam[l-1]

      if ( m == l ):
        break

      if ( itn <= j ):
        print ( '' )
        print ( 'imtqlx(): Fatal error!' )
        print ( '  Iteration limit exceeded.' )
        raise Exception ( 'imtqlx(): Fatal error!' )

      j = j + 1
      g = ( lam[l] - p ) / ( 2.0 * e[l-1] )
      r = np.sqrt ( g * g + 1.0 )

      if ( g < 0.0 ):
        t = g - r
      else:
        t = g + r

      g = lam[m-1] - p + e[l-1] / ( g + t )
 
      s = 1.0
      c = 1.0
      p = 0.0
      mml = m - l

      for ii in range ( 1, mml + 1 ):

        i = m - ii
        f = s * e[i-1]
        b = c * e[i-1]

        if ( abs ( g ) <= abs ( f ) ):
          c = g / f
          r = np.sqrt ( c * c + 1.0 )
          e[i] = f * r
          s = 1.0 / r
          c = c * s
        else:
          s = f / g
          r = np.sqrt ( s * s + 1.0 )
          e[i] = g * r
          c = 1.0 / r
          s = s * c

        g = lam[i] - p
        r = ( lam[i-1] - g ) * s + 2.0 * c * b
        p = s * r
        lam[i] = g + p
        g = c * r - b
        f = qtz[i]
        qtz[i]   = s * qtz[i-1] + c * f
        qtz[i-1] = c * qtz[i-1] - s * f

      lam[l-1] = lam[l-1] - p
      e[l-1] = g
      e[m-1] = 0.0

  for ii in range ( 2, n + 1 ):

     i = ii - 1
     k = i
     p = lam[i-1]

     for j in range ( ii, n + 1 ):

       if ( lam[j-1] < p ):
         k = j
         p = lam[j-1]

     if ( k != i ):

       lam[k-1] = lam[i-1]
       lam[i-1] = p

       p        = qtz[i-1]
       qtz[i-1] = qtz[k-1]
       qtz[k-1] = p

  return lam, qtz

def imtqlx_test ( ):

#*****************************************************************************80
#
## imtqlx_test() tests imtqlx().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'imtqlx_test():' )
  print ( '  imtqlx() takes a symmetric tridiagonal matrix A' )
  print ( '  and computes its eigenvalues LAM.' )
  print ( '  It also accepts a vector Z and computes Q\'*Z,' )
  print ( '  where Q is the matrix that diagonalizes A.' )

  n = 5
  d = np.zeros ( n )
  for i in range ( 0, n ):
    d[i] = 2.0;
  e = np.zeros ( n )
  for i in range ( 0, n - 1 ):
    e[i] = -1.0
  e[n-1] = 0.0
  z = np.ones ( n )

  lam, qtz = imtqlx ( n, d, e, z )

  r8vec_print ( n, lam, '  Computed eigenvalues:' )

  lam2 = np.zeros ( n )
  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( 2 * ( n + 1 ) )
    lam2[i] = 4.0 * ( np.sin ( angle ) ) ** 2

  r8vec_print ( n, lam2, '  Exact eigenvalues:' )

  r8vec_print ( n, z, '  Vector Z:' )
  r8vec_print ( n, qtz, '  Vector Q''*Z:' )

  return

def jacobi_ek_compute ( n, alpha, beta ):

#*****************************************************************************80
#
## jacobi_ek_compute(): Elhay-Kautsky method for Gauss-Jacobi quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x <= 1 ) (1-x)^alpha * (1+x)^beta * f(x) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#  Input:
#
#    integer N, the number of abscissas.
#
#    real ALPHA, BETA, the exponents of (1-X) and
#    (1+X) in the quadrature rule.  For simple Gauss-Legendre quadrature,
#    set ALPHA = BETA = 0.0.  -1.0 < ALPHA and -1.0 < BETA are required.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np
  from scipy.special import gamma
#
#  Define the zero-th moment.
#
  zemu = 2.0 ** ( alpha + beta + 1 ) \
       * gamma ( alpha + 1.0 ) \
       * gamma ( beta + 1.0 ) \
       / gamma ( alpha + beta + 2.0 )
#
#  Define the Jacobi matrix.
#
  bj = np.zeros ( n )

  bj[0] = 4.0 * ( 1.0 + alpha ) * ( 1.0 + beta ) \
    / ( ( 3.0 + alpha + beta ) * ( 2.0 + alpha + beta ) ** 2 )

  for i in range ( 1, n ):
    ip1_r8 = float ( i + 1 )
    abi = 2.0 * ip1_r8 + alpha + beta
    bj[i] = 4.0 * ip1_r8 * ( ip1_r8 + alpha ) * ( ip1_r8 + beta ) \
      * ( ip1_r8 + alpha + beta ) \
      / ( ( abi - 1.0 ) * ( abi + 1.0 ) * abi * abi )

  for i in range ( 0, n ):
    bj[i] = np.sqrt ( bj[i] )

  x = np.zeros ( n )
  x[0] = ( beta - alpha ) / ( 2.0 + alpha + beta )
  for i in range ( 1, n ):
    ip1_r8 = float ( i + 1 )
    abi = 2.0 * ip1_r8 + alpha + beta
    x[i] = ( beta + alpha ) * ( beta - alpha ) / ( ( abi - 2.0 ) * abi )

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return x, w

def jacobi_ek_compute_test ( ):

#*****************************************************************************80
#
## jacobi_ek_compute_test() tests jacobi_ek_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
  alpha = 1.5
  beta = 0.5

  print ( '' )
  print ( 'jacobi_ek_compute_test():' )
  print ( '  jacobi_ek_compute() computes' )
  print ( '  a generalized Jacobi quadrature rule' )
  print ( '  using the Elhay-Kautsky algorithm.' )
  print ( '' )
  print ( '  Using ALPHA = %g' % ( alpha ) )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = jacobi_ek_compute ( n, alpha, beta )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def jacobi_integral ( expon, alpha, beta ):

#*****************************************************************************80
#
## jacobi_integral() evaluates the integral of a monomial with Jacobi weight.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= +1 ) x^EXPON (1-x)^ALPHA (1+x)^BETA dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#
#    real ALPHA, the exponent of (1-X) in the weight factor.
#
#    real BETA, the exponent of (1+X) in the weight factor.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import gamma

  c = expon

  if ( ( expon % 2 ) == 0 ):
    s = +1.0
  else:
    s = -1.0

  arg1 = - alpha
  arg2 =   1.0 + c
  arg3 =   2.0 + beta + c
  arg4 = - 1.0

  value1 = r8_hyper_2f1 ( arg1, arg2, arg3, arg4 )

  arg1 = - beta
  arg2 =   1.0 + c
  arg3 =   2.0 + alpha + c
  arg4 = - 1.0

  value2 = r8_hyper_2f1 ( arg1, arg2, arg3, arg4 )

  value = gamma ( 1.0 + c ) * ( \
      s * gamma ( 1.0 + beta  ) * value1 / gamma ( 2.0 + beta  + c ) \
    +     gamma ( 1.0 + alpha ) * value2 / gamma ( 2.0 + alpha + c ) )

  return value

def jacobi_integral_test ( ):

#*****************************************************************************80
#
## jacobi_integral_test() tests jacobi_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  alpha = 1.5
  beta = 0.5

  print ( '' )
  print ( 'jacobi_integral_test():' )
  print ( '  jacobi_integral() evaluates' )
  print ( '  Integral ( -1 < x < +1 ) x^n (1-x)^alpha (1+x)^beta dx' )
  print ( '' )
  print ( '  Use ALPHA = %g' % ( alpha ) )
  print ( '      BETA =  %g' % ( beta ) )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = jacobi_integral ( n, alpha, beta )

    print ( '  %8d  %24.16g' % ( n, value ) )

  return

def kronrod_set ( n ):

#*****************************************************************************80
#
## kronrod_set() sets abscissas and weights for Gauss-Kronrod quadrature.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    A Kronrod rule is used in conjunction with a lower order
#    Gauss rule, and provides an efficient error estimation.
#
#    The error may be estimated as the difference in the two integral
#    approximations.
#
#    The efficiency comes about because the Kronrod uses the abscissas
#    of the Gauss rule, thus saving on the number of function evaluations
#    necessary.  If the Kronrod rule were replaced by a Gauss rule of
#    the same order, a higher precision integral estimate would be
#    made, but the function would have to be evaluated at many more
#    points.
#
#    The Gauss Kronrod pair of rules involves an ( N + 1 ) / 2
#    point Gauss-Legendre rule and an N point Kronrod rule.
#    Thus, the 15 point Kronrod rule should be paired with the
#    Gauss-Legendre 7 point rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    R Piessens, E de Doncker-Kapenger, C Ueberhuber, D Kahaner,
#    QUADPACK, A Subroutine Package for Automatic Integration,
#    Springer Verlag, 1983.
#
#  Input:
#
#    integer N, the order.
#    N may be 15, 21, 31 or 41, corresponding to Gauss-Legendre rules of
#    order 7, 10, 15 or 20.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 15 ):

    x = np.array ( [ \
            - 0.9914553711208126, \
            - 0.9491079123427585, \
            - 0.8648644233597691, \
            - 0.7415311855993944, \
            - 0.5860872354676911, \
            - 0.4058451513773972, \
            - 0.2077849550789850, \
              0.0, \
              0.2077849550789850, \
              0.4058451513773972, \
              0.5860872354676911, \
              0.7415311855993944, \
              0.8648644233597691, \
              0.9491079123427585, \
              0.9914553711208126 ] )

    w = np.array ( [ \
            0.2293532201052922E-01, \
            0.6309209262997855E-01, \
            0.1047900103222502, \
            0.1406532597155259, \
            0.1690047266392679, \
            0.1903505780647854, \
            0.2044329400752989, \
            0.2094821410847278, \
            0.2044329400752989, \
            0.1903505780647854, \
            0.1690047266392679, \
            0.1406532597155259, \
            0.1047900103222502, \
            0.6309209262997855E-01, \
            0.2293532201052922E-01 ] )

  elif ( n == 21 ):

    x = np.array ( [ \
            - 0.9956571630258081, \
            - 0.9739065285171717, \
            - 0.9301574913557082, \
            - 0.8650633666889845, \
            - 0.7808177265864169, \
            - 0.6794095682990244, \
            - 0.5627571346686047, \
            - 0.4333953941292472, \
            - 0.2943928627014602, \
            - 0.1488743389816312, \
              0.0, \
              0.1488743389816312, \
              0.2943928627014602, \
              0.4333953941292472, \
              0.5627571346686047, \
              0.6794095682990244, \
              0.7808177265864169, \
              0.8650633666889845, \
              0.9301574913557082, \
              0.9739065285171717, \
              0.9956571630258081 ] )

    w = np.array ( [ \
            0.1169463886737187E-01, \
            0.3255816230796473E-01, \
            0.5475589657435200E-01, \
            0.7503967481091995E-01, \
            0.9312545458369761E-01, \
            0.1093871588022976, \
            0.1234919762620659, \
            0.1347092173114733, \
            0.1427759385770601, \
            0.1477391049013385, \
            0.1494455540029169, \
            0.1477391049013385, \
            0.1427759385770601, \
            0.1347092173114733, \
            0.1234919762620659, \
            0.1093871588022976, \
            0.9312545458369761E-01, \
            0.7503967481091995E-01, \
            0.5475589657435200E-01, \
            0.3255816230796473E-01, \
            0.1169463886737187E-01 ] )

  elif ( n == 31 ):

    x = np.array ( [ \
            - 0.9980022986933971, \
            - 0.9879925180204854, \
            - 0.9677390756791391, \
            - 0.9372733924007059, \
            - 0.8972645323440819, \
            - 0.8482065834104272, \
            - 0.7904185014424659, \
            - 0.7244177313601700, \
            - 0.6509967412974170, \
            - 0.5709721726085388, \
            - 0.4850818636402397, \
            - 0.3941513470775634, \
            - 0.2991800071531688, \
            - 0.2011940939974345, \
            - 0.1011420669187175, \
              0.0, \
              0.1011420669187175, \
              0.2011940939974345, \
              0.2991800071531688, \
              0.3941513470775634, \
              0.4850818636402397, \
              0.5709721726085388, \
              0.6509967412974170, \
              0.7244177313601700, \
              0.7904185014424659, \
              0.8482065834104272, \
              0.8972645323440819, \
              0.9372733924007059, \
              0.9677390756791391, \
              0.9879925180204854, \
              0.9980022986933971 ] )

    w = np.array ( [ \
            0.5377479872923349E-02, \
            0.1500794732931612E-01, \
            0.2546084732671532E-01, \
            0.3534636079137585E-01, \
            0.4458975132476488E-01, \
            0.5348152469092809E-01, \
            0.6200956780067064E-01, \
            0.6985412131872826E-01, \
            0.7684968075772038E-01, \
            0.8308050282313302E-01, \
            0.8856444305621177E-01, \
            0.9312659817082532E-01, \
            0.9664272698362368E-01, \
            0.9917359872179196E-01, \
            0.1007698455238756, \
            0.1013300070147915, \
            0.1007698455238756, \
            0.9917359872179196E-01, \
            0.9664272698362368E-01, \
            0.9312659817082532E-01, \
            0.8856444305621177E-01, \
            0.8308050282313302E-01, \
            0.7684968075772038E-01, \
            0.6985412131872826E-01, \
            0.6200956780067064E-01, \
            0.5348152469092809E-01, \
            0.4458975132476488E-01, \
            0.3534636079137585E-01, \
            0.2546084732671532E-01, \
            0.1500794732931612E-01, \
            0.5377479872923349E-02 ] )

  elif ( n == 41 ):

    x = np.array ( [ \
            - 0.9988590315882777, \
            - 0.9931285991850949, \
            - 0.9815078774502503, \
            - 0.9639719272779138, \
            - 0.9408226338317548, \
            - 0.9122344282513259, \
            - 0.8782768112522820, \
            - 0.8391169718222188, \
            - 0.7950414288375512, \
            - 0.7463319064601508, \
            - 0.6932376563347514, \
            - 0.6360536807265150, \
            - 0.5751404468197103, \
            - 0.5108670019508271, \
            - 0.4435931752387251, \
            - 0.3737060887154196, \
            - 0.3016278681149130, \
            - 0.2277858511416451, \
            - 0.1526054652409227, \
            - 0.7652652113349733E-01, \
              0.0, \
              0.7652652113349733E-01, \
              0.1526054652409227, \
              0.2277858511416451, \
              0.3016278681149130, \
              0.3737060887154196, \
              0.4435931752387251, \
              0.5108670019508271, \
              0.5751404468197103, \
              0.6360536807265150, \
              0.6932376563347514, \
              0.7463319064601508, \
              0.7950414288375512, \
              0.8391169718222188, \
              0.8782768112522820, \
              0.9122344282513259, \
              0.9408226338317548, \
              0.9639719272779138, \
              0.9815078774502503, \
              0.9931285991850949, \
              0.9988590315882777 ] )

    w = np.array ( [ \
            0.3073583718520532E-02, \
            0.8600269855642942E-02, \
            0.1462616925697125E-01, \
            0.2038837346126652E-01, \
            0.2588213360495116E-01, \
            0.3128730677703280E-01, \
            0.3660016975820080E-01, \
            0.4166887332797369E-01, \
            0.4643482186749767E-01, \
            0.5094457392372869E-01, \
            0.5519510534828599E-01, \
            0.5911140088063957E-01, \
            0.6265323755478117E-01, \
            0.6583459713361842E-01, \
            0.6864867292852162E-01, \
            0.7105442355344407E-01, \
            0.7303069033278667E-01, \
            0.7458287540049919E-01, \
            0.7570449768455667E-01, \
            0.7637786767208074E-01, \
            0.7660071191799966E-01, \
            0.7637786767208074E-01, \
            0.7570449768455667E-01, \
            0.7458287540049919E-01, \
            0.7303069033278667E-01, \
            0.7105442355344407E-01, \
            0.6864867292852162E-01, \
            0.6583459713361842E-01, \
            0.6265323755478117E-01, \
            0.5911140088063957E-01, \
            0.5519510534828599E-01, \
            0.5094457392372869E-01, \
            0.4643482186749767E-01, \
            0.4166887332797369E-01, \
            0.3660016975820080E-01, \
            0.3128730677703280E-01, \
            0.2588213360495116E-01, \
            0.2038837346126652E-01, \
            0.1462616925697125E-01, \
            0.8600269855642942E-02, \
            0.3073583718520532E-02 ] )
  else:

    print ( '' )
    print ( 'KRONROD_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 15, 21, 31 or 41.' )
    raise Exception ( 'KRONROD_SET(): Fatal error!' )

  return x, w

def kronrod_set_test ( ):

#*****************************************************************************80
#
## kronrod_set_test() tests kronrod_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nl_test = np.array ( [ 7, 10, 15, 20 ] )

  print ( '' )
  print ( 'kronrod_set_test():' )
  print ( '  kronrod_set() sets up a Kronrod quadrature rule,' )
  print ( '  This is used following a lower order Legendre rule.' )

  for test in range ( 0, 4 ):

    print ( '' )
    print ( '  Legendre/Kronrod quadrature pair #%d' % ( test ) )
    print ( '                W                         X' )
    print ( '' )

    nl = nl_test[test]
    xl, wl = legendre_set ( nl )

    for i in range ( 0, nl ):
      print ( '  %8d  %24.16g  %24.16g' % ( i, xl[i], wl[i] ) )

    print ( '' )

    nk = 2 * nl + 1
    xk, wk = kronrod_set ( nk )

    for i in range ( 0, nk ):
      print ( '  %8d  %24.16g  %24.16g' % ( i, xk[i], wk[i] ) )

  return

def laguerre_1_set ( n ):

#*****************************************************************************80
#
## laguerre_1_set() sets abscissas and weights for Laguerre quadrature.
#
#  Discussion:
#
#    This routine is specialized for the case where the density function is 1.
#
#    The integral is:
#      I(f) = integral ( 0 <= x < +oo ) f(x) dx
#    The quadrature rule is
#      Q(f) = sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order.
#    N must be between 1 and 10.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
            1.00000000000000000000000000000 ] )

    w = np.array ( [ \
            2.7182818284590451 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
           0.585786437626904951198311275790, \
           3.41421356237309504880168872421 ] )

    w = np.array ( [ \
           1.5333260331194167, \
           4.4509573350545928 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
           0.415774556783479083311533873128, \
           2.29428036027904171982205036136, \
           6.28994508293747919686641576551 ] )

    w = np.array ( [ \
           1.0776928592709207, \
           2.7621429619015876, \
           5.6010946254344267 ] )

  elif ( n == 4 ):

    x = np.array ( [ \
           0.322547689619392311800361459104, \
           1.74576110115834657568681671252, \
           4.53662029692112798327928538496, \
           9.39507091230113312923353644342 ] )

    w = np.array ( [ \
           0.83273912383788917, \
           2.0481024384542965, \
           3.6311463058215168, \
           6.4871450844076604 ] )

  elif ( n == 5 ):

    x = np.array ( [ \
           0.263560319718140910203061943361, \
           1.41340305910651679221840798019, \
           3.59642577104072208122318658878, \
           7.08581000585883755692212418111, \
           12.6408008442757826594332193066 ] )

    w = np.array ( [ \
           0.67909404220775038, \
           1.6384878736027471, \
           2.7694432423708375, \
           4.3156569009208940, \
           7.2191863543544450 ] )

  elif ( n == 6 ):

    x = np.array ( [ \
           0.222846604179260689464354826787, \
           1.18893210167262303074315092194, \
           2.99273632605931407769132528451, \
           5.77514356910451050183983036943, \
           9.83746741838258991771554702994, \
           15.9828739806017017825457915674 ] )

    w = np.array ( [ \
           0.57353550742273818, \
           1.3692525907123045, \
           2.2606845933826722, \
           3.3505245823554555, \
           4.8868268002108213, \
           7.8490159455958279 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
           0.193043676560362413838247885004, \
           1.02666489533919195034519944317, \
           2.56787674495074620690778622666, \
           4.90035308452648456810171437810, \
           8.18215344456286079108182755123, \
           12.7341802917978137580126424582, \
           19.3957278622625403117125820576 ] )

    w = np.array ( [ \
           0.49647759753997234, \
           1.1776430608611976, \
           1.9182497816598063, \
           2.7718486362321113, \
           3.8412491224885148, \
           5.3806782079215330, \
           8.4054324868283103 ] )

  elif ( n == 8 ):

    x = np.array ( [ \
           0.170279632305100999788861856608, \
           0.903701776799379912186020223555, \
           2.25108662986613068930711836697, \
           4.26670017028765879364942182690, \
           7.04590540239346569727932548212, \
           10.7585160101809952240599567880, \
           15.7406786412780045780287611584, \
           22.8631317368892641057005342974 ] )

    w = np.array ( [ \
           0.43772341049291136, \
           1.0338693476655976, \
           1.6697097656587756, \
           2.3769247017585995, \
           3.2085409133479259, \
           4.2685755108251344, \
           5.8180833686719184, \
           8.9062262152922216 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
           0.152322227731808247428107073127, \
           0.807220022742255847741419210952, \
           2.00513515561934712298303324701, \
           3.78347397333123299167540609364, \
           6.20495677787661260697353521006, \
           9.37298525168757620180971073215, \
           13.4662369110920935710978818397, \
           18.8335977889916966141498992996, \
           26.3740718909273767961410072937 ] )

    w = np.array ( [ \
           0.39143112431563987, \
           0.92180502852896307, \
           1.4801279099429154, \
           2.0867708075492613, \
           2.7729213897119713, \
           3.5916260680922663, \
           4.6487660021402037, \
           6.2122754197471348, \
           9.3632182377057980 ] )

  elif ( n == 10 ):

    x = np.array ( [ \
           0.137793470540492430830772505653, \
           0.729454549503170498160373121676, \
           1.80834290174031604823292007575, \
           3.40143369785489951448253222141, \
           5.55249614006380363241755848687, \
           8.33015274676449670023876719727, \
           11.8437858379000655649185389191, \
           16.2792578313781020995326539358, \
           21.9965858119807619512770901956, \
           29.9206970122738915599087933408 ] )

    w = np.array ( [ \
           0.35400973860699630, \
           0.83190230104358065, \
           1.3302885617493283, \
           1.8630639031111309, \
           2.4502555580830108, \
           3.1227641551351848, \
           3.9341526955615240, \
           4.9924148721930299, \
           6.5722024851307994, \
           9.7846958403746243 ] )

  else:

    print ( '' )
    print ( 'LAGUERRE_1_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 to 10.' )
    raise Exception ( 'LAGUERRE_1_SET(): Fatal error!' )

  return x, w

def laguerre_1_set_test ( ):

#*****************************************************************************80
#
## laguerre_1_set_test() tests laguerre_1_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'laguerre_1_set_test():' )
  print ( '  laguerre_1_set() sets a Laguerre rule.' )
  print ( '  The density function is rho(x)=1.' )
  print ( '' )
  print ( '         I            X                  W' )

  for n in range ( 1, 11 ):

    x, w = laguerre_1_set ( n )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %8d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def laguerre_ek_compute ( n ):

#*****************************************************************************80
#
## laguerre_ek_compute(): Gauss-Laguerre, Elhay-Kautsky method.
#
#  Discussion:
#
#    The integral:
#
#      integral ( 0 < x < +oo ) exp ( -x ) * f(x) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#  Input:
#
#    integer N, the number of abscissas.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np
  from scipy.special import gamma
#
#  Define the zero-th moment.
#
  zemu = 1.0
#
#  Define the Jacobi matrix.
#
  bj = np.zeros ( n )
  for i in range ( 0, n ):
    ip1_r8 = float ( i + 1 )
    bj[i] = ip1_r8

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( 2 * i + 1 )

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return x, w

def laguerre_ek_compute_test ( ):

#*****************************************************************************80
#
## laguerre_ek_compute_test() tests laguerre_ek_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'laguerre_ek_compute_test():' )
  print ( '  laguerre_ek_compute() computes' )
  print ( '  a Laguerre quadrature rule' )
  print ( '  using the Elhay-Kautsky algorithm.' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = laguerre_ek_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def laguerre_integral ( expon ):

#*****************************************************************************80
#
## laguerre_integral() evaluates a monomial Laguerre integral.
#
#  Discussion:
#
#    The integral:
#
#      integral ( 0 <= x < +oo ) x^n * exp ( -x ) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#    0 <= EXPON.
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  from math import factorial

  exact = factorial ( expon )

  return exact

def laguerre_integral_test ( ):

#*****************************************************************************80
#
## laguerre_integral_test() tests laguerre_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'laguerre_integral_test():' )
  print ( '  laguerre_integral() evaluates' )
  print ( '  Integral ( 0 < x < oo ) x^n * exp(-x) dx' )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = laguerre_integral ( n )

    print ( '  %8d  %24.16g' % ( n, value ) )

  return

def laguerre_set ( n ):

#*****************************************************************************80
#
## laguerre_set() sets abscissas and weights for Laguerre quadrature.
#
#  Discussion:
#
#    The abscissas are the zeroes of the Laguerre polynomial L(N)(X).
#
#    The integral:
#
#      Integral ( 0 <= X < +oo ) exp ( -X ) * F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * f ( X(I) )
#
#    The integral:
#
#      Integral ( 0 <= X < +oo ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * exp ( X(I) ) * f ( X(I) )
#
#    Mathematica can numerically estimate the abscissas for the
#    n-th order polynomial to p digits of precision by the command:
#
#      NSolve [ LaguerreL[n,x] == 0, x, p ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
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
#    Vladimir Krylov,
#    Approximate Calculation of Integrals,
#    Dover, 2006,
#    ISBN: 0486445798,
#    LC: QA311.K713.
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
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
#    integer N, the order.
#    N must be between 1 and 20, 31/32/33, 63/64/65, 127/128/129.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
            1.00000000000000000000000000000E+00 ] )

    w = np.array ( [ \
            1.00000000000000000000000000000E+00 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
           0.585786437626904951198311275790E+00, \
           3.41421356237309504880168872421E+00 ] )

    w = np.array ( [ \
           0.85355339059327376220042218105E+00, \
           0.146446609406726237799577818948E+00 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
           0.415774556783479083311533873128E+00, \
           2.29428036027904171982205036136E+00, \
           6.28994508293747919686641576551E+00 ] )

    w = np.array ( [ \
           0.71109300992917301544959019114E+00, \
           0.27851773356924084880144488846E+00, \
           0.010389256501586135748964920401E+00 ] )

  elif ( n == 4 ):

    x = np.array ( [ \
           0.322547689619392311800361459104E+00, \
           1.74576110115834657568681671252E+00, \
           4.53662029692112798327928538496E+00, \
           9.39507091230113312923353644342E+00 ] )

    w = np.array ( [ \
           0.60315410434163360163596602382E+00, \
           0.35741869243779968664149201746E+00, \
           0.03888790851500538427243816816E+00, \
           0.0005392947055613274501037905676E+00 ] )

  elif ( n == 5 ):

    x = np.array ( [ \
           0.263560319718140910203061943361E+00, \
           1.41340305910651679221840798019E+00, \
           3.59642577104072208122318658878E+00, \
           7.08581000585883755692212418111E+00, \
           12.6408008442757826594332193066E+00 ] )

    w = np.array ( [ \
           0.52175561058280865247586092879E+00, \
           0.3986668110831759274541333481E+00, \
           0.0759424496817075953876533114E+00, \
           0.00361175867992204845446126257E+00, \
           0.00002336997238577622789114908455E+00 ] )

  elif ( n == 6 ):

    x = np.array ( [ \
           0.222846604179260689464354826787E+00, \
           1.18893210167262303074315092194E+00, \
           2.99273632605931407769132528451E+00, \
           5.77514356910451050183983036943E+00, \
           9.83746741838258991771554702994E+00, \
           15.9828739806017017825457915674E+00 ] )

    w = np.array ( [ \
           0.45896467394996359356828487771E+00, \
           0.4170008307721209941133775662E+00, \
           0.1133733820740449757387061851E+00, \
           0.01039919745314907489891330285E+00, \
           0.000261017202814932059479242860E+00, \
           8.98547906429621238825292053E-07 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
           0.193043676560362413838247885004E+00, \
           1.02666489533919195034519944317E+00, \
           2.56787674495074620690778622666E+00, \
           4.90035308452648456810171437810E+00, \
           8.18215344456286079108182755123E+00, \
           12.7341802917978137580126424582E+00, \
           19.3957278622625403117125820576E+00 ] )

    w = np.array ( [ \
           0.40931895170127390213043288002E+00, \
           0.4218312778617197799292810054E+00, \
           0.1471263486575052783953741846E+00, \
           0.0206335144687169398657056150E+00, \
           0.00107401014328074552213195963E+00, \
           0.0000158654643485642012687326223E+00, \
           3.17031547899558056227132215E-08 ] )

  elif ( n == 8 ):

    x = np.array ( [ \
           0.170279632305100999788861856608E+00, \
           0.903701776799379912186020223555E+00, \
           2.25108662986613068930711836697E+00, \
           4.26670017028765879364942182690E+00, \
           7.04590540239346569727932548212E+00, \
           10.7585160101809952240599567880E+00, \
           15.7406786412780045780287611584E+00, \
           22.8631317368892641057005342974E+00 ] )

    w = np.array ( [ \
           0.36918858934163752992058283938E+00, \
           0.4187867808143429560769785813E+00, \
           0.175794986637171805699659867E+00, \
           0.033343492261215651522132535E+00, \
           0.0027945362352256725249389241E+00, \
           0.00009076508773358213104238501E+00, \
           8.4857467162725315448680183E-07, \
           1.04800117487151038161508854E-09 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
           0.152322227731808247428107073127E+00, \
           0.807220022742255847741419210952E+00, \
           2.00513515561934712298303324701E+00, \
           3.78347397333123299167540609364E+00, \
           6.20495677787661260697353521006E+00, \
           9.37298525168757620180971073215E+00, \
           13.4662369110920935710978818397E+00, \
           18.8335977889916966141498992996E+00, \
           26.3740718909273767961410072937E+00 ] )

    w = np.array ( [ \
           0.336126421797962519673467717606E+00, \
           0.411213980423984387309146942793E+00, \
           0.199287525370885580860575607212E+00, \
           0.0474605627656515992621163600479E+00, \
           0.00559962661079458317700419900556E+00, \
           0.000305249767093210566305412824291E+00, \
           6.59212302607535239225572284875E-06, \
           4.1107693303495484429024104033E-08, \
           3.29087403035070757646681380323E-11 ] )

  elif ( n == 10 ):

    x = np.array ( [ \
           0.137793470540492430830772505653E+00, \
           0.729454549503170498160373121676E+00, \
           1.80834290174031604823292007575E+00, \
           3.40143369785489951448253222141E+00, \
           5.55249614006380363241755848687E+00, \
           8.33015274676449670023876719727E+00, \
           11.8437858379000655649185389191E+00, \
           16.2792578313781020995326539358E+00, \
           21.9965858119807619512770901956E+00, \
            29.9206970122738915599087933408E+00 ] )

    w = np.array ( [ \
           0.30844111576502014154747083468E+00, \
           0.4011199291552735515157803099E+00, \
           0.218068287611809421588648523E+00, \
           0.062087456098677747392902129E+00, \
           0.009501516975181100553839072E+00, \
           0.0007530083885875387754559644E+00, \
           0.00002825923349599565567422564E+00, \
           4.249313984962686372586577E-07, \
           1.839564823979630780921535E-09, \
            9.911827219609008558377547E-13 ] )

  elif ( n == 11 ):

    x = np.array ( [ \
           0.125796442187967522675794577516E+00, \
           0.665418255839227841678127839420E+00, \
           1.64715054587216930958700321365E+00, \
           3.09113814303525495330195934259E+00, \
           5.02928440157983321236999508366E+00, \
           7.50988786380661681941099714450E+00, \
           10.6059509995469677805559216457E+00, \
           14.4316137580641855353200450349E+00, \
           19.1788574032146786478174853989E+00, \
            25.2177093396775611040909447797E+00, \
            33.4971928471755372731917259395E+00 ] )

    w = np.array ( [ \
           0.28493321289420060505605102472E+00, \
           0.3897208895278493779375535080E+00, \
           0.232781831848991333940223796E+00, \
           0.076564453546196686400854179E+00, \
           0.014393282767350695091863919E+00, \
           0.001518880846484873069847776E+00, \
           0.0000851312243547192259720424E+00, \
           2.29240387957450407857683E-06, \
           2.48635370276779587373391E-08, \
            7.71262693369132047028153E-11, \
            2.883775868323623861597778E-14 ] )

  elif ( n == 12 ):

    x = np.array ( [ \
           0.115722117358020675267196428240E+00, \
           0.611757484515130665391630053042E+00, \
           1.51261026977641878678173792687E+00, \
           2.83375133774350722862747177657E+00, \
           4.59922763941834848460572922485E+00, \
           6.84452545311517734775433041849E+00, \
           9.62131684245686704391238234923E+00, \
           13.0060549933063477203460524294E+00, \
           17.1168551874622557281840528008E+00, \
            22.1510903793970056699218950837E+00, \
            28.4879672509840003125686072325E+00, \
            37.0991210444669203366389142764E+00 ] )

    w = np.array ( [ \
           0.26473137105544319034973889206E+00, \
           0.3777592758731379820244905567E+00, \
           0.244082011319877564254870818E+00, \
           0.09044922221168093072750549E+00, \
           0.02010238115463409652266129E+00, \
           0.002663973541865315881054158E+00, \
           0.000203231592662999392121433E+00, \
           8.3650558568197987453363E-06, \
           1.66849387654091026116990E-07, \
            1.34239103051500414552392E-09, \
            3.06160163503502078142408E-12, \
            8.148077467426241682473119E-16 ] )

  elif ( n == 13 ):

    x = np.array ( [ \
           0.107142388472252310648493376977E+00, \
           0.566131899040401853406036347177E+00, \
           1.39856433645101971792750259921E+00, \
           2.61659710840641129808364008472E+00, \
           4.23884592901703327937303389926E+00, \
           6.29225627114007378039376523025E+00, \
           8.81500194118697804733348868036E+00, \
           11.8614035888112425762212021880E+00, \
           15.5107620377037527818478532958E+00, \
            19.8846356638802283332036594634E+00, \
            25.1852638646777580842970297823E+00, \
            31.8003863019472683713663283526E+00, \
            40.7230086692655795658979667001E+00 ] )

    w = np.array ( [ \
           0.24718870842996262134624918596E+00, \
           0.3656888229005219453067175309E+00, \
           0.252562420057658502356824289E+00, \
           0.10347075802418370511421863E+00, \
           0.02643275441556161577815877E+00, \
           0.00422039604025475276555209E+00, \
           0.000411881770472734774892473E+00, \
           0.0000235154739815532386882897E+00, \
           7.3173116202490991040105E-07, \
            1.10884162570398067979151E-08, \
            6.7708266922058988406462E-11, \
            1.15997995990507606094507E-13, \
            2.245093203892758415991872E-17 ] )

  elif ( n == 14 ):

    x = np.array ( [ \
           0.0997475070325975745736829452514E+00, \
           0.526857648851902896404583451502E+00, \
           1.30062912125149648170842022116E+00, \
           2.43080107873084463616999751038E+00, \
           3.93210282229321888213134366778E+00, \
           5.82553621830170841933899983898E+00, \
           8.14024014156514503005978046052E+00, \
           10.9164995073660188408130510904E+00, \
           14.2108050111612886831059780825E+00, \
            18.1048922202180984125546272083E+00, \
            22.7233816282696248232280886985E+00, \
            28.2729817232482056954158923218E+00, \
            35.1494436605924265828643121364E+00, \
            44.3660817111174230416312423666E+00 ] )

    w = np.array ( [ \
           0.23181557714486497784077486110E+00, \
           0.3537846915975431518023313013E+00, \
           0.258734610245428085987320561E+00, \
           0.11548289355692321008730499E+00, \
           0.03319209215933736003874996E+00, \
           0.00619286943700661021678786E+00, \
           0.00073989037786738594242589E+00, \
           0.000054907194668416983785733E+00, \
           2.4095857640853774967578E-06, \
            5.801543981676495180886E-08, \
            6.819314692484974119616E-10, \
            3.2212077518948479398089E-12, \
            4.2213524405165873515980E-15, \
            6.05237502228918880839871E-19 ] )

  elif ( n == 15 ):

    x = np.array ( [ \
           0.0933078120172818047629030383672E+00, \
           0.492691740301883908960101791412E+00, \
           1.21559541207094946372992716488E+00, \
           2.26994952620374320247421741375E+00, \
           3.66762272175143727724905959436E+00, \
           5.42533662741355316534358132596E+00, \
           7.56591622661306786049739555812E+00, \
           10.1202285680191127347927394568E+00, \
           13.1302824821757235640991204176E+00, \
            16.6544077083299578225202408430E+00, \
            20.7764788994487667729157175676E+00, \
            25.6238942267287801445868285977E+00, \
            31.4075191697539385152432196202E+00, \
            38.5306833064860094162515167595E+00, \
            48.0260855726857943465734308508E+00 ] )

    w = np.array ( [ \
           0.21823488594008688985641323645E+00, \
           0.3422101779228833296389489568E+00, \
           0.263027577941680097414812275E+00, \
           0.12642581810593053584303055E+00, \
           0.04020686492100091484158548E+00, \
           0.00856387780361183836391576E+00, \
           0.00121243614721425207621921E+00, \
           0.00011167439234425194199258E+00, \
           6.459926762022900924653E-06, \
            2.226316907096272630332E-07, \
            4.227430384979365007351E-09, \
            3.921897267041089290385E-11, \
            1.4565152640731264063327E-13, \
            1.4830270511133013354616E-16, \
            1.60059490621113323104998E-20 ] )

  elif ( n == 16 ):

    x = np.array ( [ \
           0.0876494104789278403601980973401E+00, \
           0.462696328915080831880838260664E+00, \
           1.14105777483122685687794501811E+00, \
           2.12928364509838061632615907066E+00, \
           3.43708663389320664523510701675E+00, \
           5.07801861454976791292305830814E+00, \
           7.07033853504823413039598947080E+00, \
           9.43831433639193878394724672911E+00, \
           12.2142233688661587369391246088E+00, \
            15.4415273687816170767647741622E+00, \
            19.1801568567531348546631409497E+00, \
            23.5159056939919085318231872752E+00, \
            28.5787297428821403675206137099E+00, \
            34.5833987022866258145276871778E+00, \
            41.9404526476883326354722330252E+00, \
            51.7011603395433183643426971197E+00 ] )

    w = np.array ( [ \
           0.20615171495780099433427363674E+00, \
           0.3310578549508841659929830987E+00, \
           0.265795777644214152599502021E+00, \
           0.13629693429637753997554751E+00, \
           0.0473289286941252189780623E+00, \
           0.0112999000803394532312490E+00, \
           0.0018490709435263108642918E+00, \
           0.00020427191530827846012602E+00, \
           0.00001484458687398129877135E+00, \
            6.828319330871199564396E-07, \
            1.881024841079673213882E-08, \
            2.862350242973881619631E-10, \
            2.127079033224102967390E-12, \
            6.297967002517867787174E-15, \
            5.050473700035512820402E-18, \
            4.1614623703728551904265E-22 ] )

  elif ( n == 17 ):

    x = np.array ( [ \
           0.0826382147089476690543986151980E+00, \
           0.436150323558710436375959029847E+00, \
           1.07517657751142857732980316755E+00, \
           2.00519353164923224070293371933E+00, \
           3.23425612404744376157380120696E+00, \
           4.77351351370019726480932076262E+00, \
           6.63782920536495266541643929703E+00, \
           8.84668551116980005369470571184E+00, \
           11.4255293193733525869726151469E+00, \
            14.4078230374813180021982874959E+00, \
            17.8382847307011409290658752412E+00, \
            21.7782682577222653261749080522E+00, \
            26.3153178112487997766149598369E+00, \
            31.5817716804567331343908517497E+00, \
            37.7960938374771007286092846663E+00, \
            45.3757165339889661829258363215E+00, \
            55.3897517898396106640900199790E+00 ] )

    w = np.array ( [ \
           0.19533220525177083214592729770E+00, \
           0.3203753572745402813366256320E+00, \
           0.267329726357171097238809604E+00, \
           0.14512985435875862540742645E+00, \
           0.0544369432453384577793806E+00, \
           0.0143572977660618672917767E+00, \
           0.0026628247355727725684324E+00, \
           0.0003436797271562999206118E+00, \
           0.00003027551783782870109437E+00, \
            1.768515053231676895381E-06, \
            6.57627288681043332199E-08, \
            1.469730932159546790344E-09, \
            1.81691036255544979555E-11, \
            1.095401388928687402976E-13, \
            2.617373882223370421551E-16, \
            1.6729356931461546908502E-19, \
            1.06562631627404278815253E-23 ] )

  elif ( n == 18 ):

    x = np.array ( [ \
           0.0781691666697054712986747615334E+00, \
           0.412490085259129291039101536536E+00, \
           1.01652017962353968919093686187E+00, \
           1.89488850996976091426727831954E+00, \
           3.05435311320265975115241130719E+00, \
           4.50420553888989282633795571455E+00, \
           6.25672507394911145274209116326E+00, \
           8.32782515660563002170470261564E+00, \
           10.7379900477576093352179033397E+00, \
            13.5136562075550898190863812108E+00, \
            16.6893062819301059378183984163E+00, \
            20.3107676262677428561313764553E+00, \
            24.4406813592837027656442257980E+00, \
            29.1682086625796161312980677805E+00, \
            34.6279270656601721454012429438E+00, \
            41.0418167728087581392948614284E+00, \
            48.8339227160865227486586093290E+00, \
            59.0905464359012507037157810181E+00 ] )

    w = np.array ( [ \
           0.18558860314691880562333775228E+00, \
           0.3101817663702252936495975957E+00, \
           0.267866567148536354820854395E+00, \
           0.15297974746807490655384308E+00, \
           0.0614349178609616527076780E+00, \
           0.0176872130807729312772600E+00, \
           0.0036601797677599177980266E+00, \
           0.0005406227870077353231284E+00, \
           0.0000561696505121423113818E+00, \
            4.01530788370115755859E-06, \
            1.91466985667567497969E-07, \
            5.8360952686315941292E-09, \
            1.07171126695539012773E-10, \
            1.08909871388883385562E-12, \
            5.38666474837830887608E-15, \
            1.049865978035703408779E-17, \
            5.405398451631053643566E-21, \
            2.6916532692010286270838E-25 ] )

  elif ( n == 19 ):

    x = np.array ( [ \
           0.0741587837572050877131369916024E+00, \
           0.391268613319994607337648350299E+00, \
           0.963957343997958058624878377130E+00, \
           1.79617558206832812557725825252E+00, \
           2.89365138187378399116494713237E+00, \
           4.26421553962776647436040018167E+00, \
           5.91814156164404855815360191408E+00, \
           7.86861891533473373105668358176E+00, \
           10.1324237168152659251627415800E+00, \
            12.7308814638423980045092979656E+00, \
            15.6912783398358885454136069861E+00, \
            19.0489932098235501532136429732E+00, \
            22.8508497608294829323930586693E+00, \
            27.1606693274114488789963947149E+00, \
            32.0691222518622423224362865906E+00, \
            37.7129058012196494770647508283E+00, \
            44.3173627958314961196067736013E+00, \
            52.3129024574043831658644222420E+00, \
            62.8024231535003758413504690673E+00 ] )

    w = np.array ( [ \
           0.17676847491591250225103547981E+00, \
           0.3004781436072543794821568077E+00, \
           0.267599547038175030772695441E+00, \
           0.15991337213558021678551215E+00, \
           0.0682493799761491134552355E+00, \
           0.0212393076065443249244062E+00, \
           0.0048416273511483959672501E+00, \
           0.0008049127473813667665946E+00, \
           0.0000965247209315350170843E+00, \
            8.20730525805103054409E-06, \
            4.8305667247307725394E-07, \
            1.90499136112328569994E-08, \
            4.8166846309280615577E-10, \
            7.3482588395511443768E-12, \
            6.2022753875726163989E-14, \
            2.54143084301542272372E-16, \
            4.07886129682571235007E-19, \
            1.707750187593837061004E-22, \
            6.715064649908189959990E-27 ] )

  elif ( n == 20 ):

    x = np.array ( [ \
           0.0705398896919887533666890045842E+00, \
           0.372126818001611443794241388761E+00, \
           0.916582102483273564667716277074E+00, \
           1.70730653102834388068768966741E+00, \
           2.74919925530943212964503046049E+00, \
           4.04892531385088692237495336913E+00, \
           5.61517497086161651410453988565E+00, \
           7.45901745367106330976886021837E+00, \
           9.59439286958109677247367273428E+00, \
            12.0388025469643163096234092989E+00, \
            14.8142934426307399785126797100E+00, \
            17.9488955205193760173657909926E+00, \
            21.4787882402850109757351703696E+00, \
            25.4517027931869055035186774846E+00, \
            29.9325546317006120067136561352E+00, \
            35.0134342404790000062849359067E+00, \
            40.8330570567285710620295677078E+00, \
            47.6199940473465021399416271529E+00, \
            55.8107957500638988907507734445E+00, \
            66.5244165256157538186403187915E+00 ] )

    w = np.array ( [ \
           0.168746801851113862149223899689E+00, \
           0.291254362006068281716795323812E+00, \
           0.266686102867001288549520868998E+00, \
           0.166002453269506840031469127816E+00, \
           0.0748260646687923705400624639615E+00, \
           0.0249644173092832210728227383234E+00, \
           0.00620255084457223684744754785395E+00, \
           0.00114496238647690824203955356969E+00, \
           0.000155741773027811974779809513214E+00, \
            0.0000154014408652249156893806714048E+00, \
            1.08648636651798235147970004439E-06, \
            5.33012090955671475092780244305E-08, \
            1.7579811790505820035778763784E-09, \
            3.72550240251232087262924585338E-11, \
            4.76752925157819052449488071613E-13, \
            3.37284424336243841236506064991E-15, \
            1.15501433950039883096396247181E-17, \
            1.53952214058234355346383319667E-20, \
            5.28644272556915782880273587683E-24, \
            1.65645661249902329590781908529E-28 ] )

  elif ( n == 31 ):

    x = np.array ( [ \
           0.0459019476211082907434960802752E+00, \
           0.241980163824772048904089741517E+00, \
           0.595253894222350737073301650054E+00, \
           1.10668949953299871621113087898E+00, \
           1.77759569287477272115937274827E+00, \
           2.60970341525668065038933759253E+00, \
           3.60519680234004426988058175542E+00, \
           4.76674708447176113136291272711E+00, \
           6.09755456718174092699254293285E+00, \
            7.60140094923313742293601069429E+00, \
            9.28271431347088941825366952977E+00, \
            11.1466497556192913589938156296E+00, \
            13.1991895762449985224649250286E+00, \
            15.4472683155493100758093258918E+00, \
            17.8989298266447576467257938178E+00, \
            20.5635263367158221707430489688E+00, \
            23.4519734820118585910502555759E+00, \
            26.5770813521182604599758769865E+00, \
            29.9539908723464455069519178400E+00, \
            33.6007595329022027354103138858E+00, \
            37.5391644073304408828879025580E+00, \
            41.7958308701822199813479458533E+00, \
            46.4038668064111231360292276044E+00, \
            51.4053144767977551618614610884E+00, \
            56.8549928687158436205119220557E+00, \
            62.8268559087863214536775233048E+00, \
            69.4252771910803456233222516564E+00, \
            76.8070477638627328376099722855E+00, \
            85.2303586075456691693870656070E+00, \
            95.1889398915256299813086068540E+00, \
            107.952243827578714750024401177E+00 ] )

    w = np.array ( [ \
           0.112527895503725838208477280828E+00, \
           0.21552760818089123795222505285E+00, \
           0.238308251645696547319057880892E+00, \
           0.195388309297902292499153033907E+00, \
           0.126982832893061901436352729046E+00, \
           0.0671861689238993006709294419935E+00, \
           0.029303224993879487404888669312E+00, \
           0.0105975699152957360895293803144E+00, \
           0.0031851272582386980320974842433E+00, \
            0.000795495483079403829220921490125E+00, \
            0.000164800521266366873178629671164E+00, \
            0.000028229237864310816393860971469E+00, \
            3.98029025510085803871161749001E-06, \
            4.59318398418010616737296945103E-07, \
            4.30755451877311009301314574659E-08, \
            3.25512499382715708551757492579E-09, \
            1.96202466754105949962471515931E-10, \
            9.31904990866175871295347164313E-12, \
            3.43775418194116205203125978983E-13, \
            9.67952471304467169974050357762E-15, \
            2.03680661101152473980106242193E-16, \
            3.12126872807135268317653586326E-18, \
            3.37295817041610524533956783083E-20, \
            2.46727963866166960110383632425E-22, \
            1.15822019045256436348345645766E-24, \
            3.2472922591425422434798022809E-27, \
            4.91430173080574327408200762597E-30, \
            3.45000711048083941322231359538E-33, \
            8.76637101171620414729327607329E-37, \
            5.03636439211614904112971723166E-41, \
            1.99099845825314564824395490803E-46 ] )

  elif ( n == 32 ):

    x = np.array ( [ \
           0.0444893658332670184188501945244E+00, \
           0.234526109519618537452909561302E+00, \
           0.576884629301886426491552569378E+00, \
           1.07244875381781763304091397718E+00, \
           1.72240877644464544113093292797E+00, \
           2.52833670642579488112419990556E+00, \
           3.49221327302199448960880339977E+00, \
           4.61645676974976738776205229617E+00, \
           5.90395850417424394656152149158E+00, \
            7.35812673318624111322198973719E+00, \
            8.98294092421259610337824752677E+00, \
            10.7830186325399720675019491381E+00, \
            12.7636979867427251149690330822E+00, \
            14.9311397555225573197969646873E+00, \
            17.2924543367153147892357183836E+00, \
            19.8558609403360547397899445841E+00, \
            22.6308890131967744886757793394E+00, \
            25.6286360224592477674761768768E+00, \
            28.8621018163234747443426407115E+00, \
            32.3466291539647370032321654237E+00, \
            36.1004948057519738040171189479E+00, \
            40.1457197715394415362093439289E+00, \
            44.5092079957549379759066043775E+00, \
            49.2243949873086391767222218066E+00, \
            54.3337213333969073328671815512E+00, \
            59.8925091621340181961304753247E+00, \
            65.9753772879350527965630761193E+00, \
            72.6876280906627086386753490878E+00, \
            80.1874469779135230674916385687E+00, \
            88.7353404178923986893554495243E+00, \
            98.8295428682839725591844784095E+00, \
            111.751398097937695213664716539E+00 ] )

    w = np.array ( [ \
           0.109218341952384971136131337943E+00, \
           0.210443107938813232936062071392E+00, \
           0.235213229669848005394941106676E+00, \
           0.195903335972881043413247901182E+00, \
           0.129983786286071760607216822326E+00, \
           0.0705786238657174415601643320433E+00, \
           0.0317609125091750703058255211629E+00, \
           0.0119182148348385570565446505756E+00, \
           0.00373881629461152478966122847796E+00, \
            0.000980803306614955132230630611308E+00, \
            0.000214864918801364188023199483686E+00, \
            0.0000392034196798794720432695682782E+00, \
            5.93454161286863287835582893773E-06, \
            7.4164045786675522190708220213E-07, \
            7.60456787912078148111926545943E-08, \
            6.35060222662580674242777108552E-09, \
            4.28138297104092887881360582098E-10, \
            2.30589949189133607927336809618E-11, \
            9.79937928872709406333455225995E-13, \
            3.23780165772926646231042646142E-14, \
            8.17182344342071943320186059177E-16, \
            1.54213383339382337217855949129E-17, \
            2.11979229016361861204093474373E-19, \
            2.05442967378804542665570987602E-21, \
            1.34698258663739515580519340478E-23, \
            5.66129413039735937112634432382E-26, \
            1.41856054546303690595142933892E-28, \
            1.91337549445422430937127829683E-31, \
            1.19224876009822235654164532831E-34, \
            2.67151121924013698599867893958E-38, \
            1.33861694210625628271905701423E-42, \
            4.51053619389897423222342830132E-48 ] )

  elif ( n == 33 ):

    x = np.array ( [ \
           0.0431611356173268921917334738206E+00, \
           0.227517802803371123850290226913E+00, \
           0.559616655851539887586282303916E+00, \
           1.04026850775100205382209621927E+00, \
           1.67055919607571519092562973257E+00, \
           2.45192079589763054651073898192E+00, \
           3.38615533758800483230187851832E+00, \
           4.47545949839977145702059137905E+00, \
           5.72245472027210352266790817933E+00, \
            7.13022434440010801631414039534E+00, \
            8.70235923062140624893696399459E+00, \
            10.4430136502059824268455293839E+00, \
            12.3569737593502859624441255236E+00, \
            14.4497416815855402377145121178E+00, \
            16.7276392186383223532615229942E+00, \
            19.1979365872124466372283088222E+00, \
            21.8690135249281898713512287043E+00, \
            24.7505629061577956433730931987E+00, \
            27.8538511114133567797747375537E+00, \
            31.1920555455751298677734295989E+00, \
            34.7807091535383377002292521853E+00, \
            38.6382967177740302250360622751E+00, \
            42.7870720782534794879639219927E+00, \
            47.2542066029932658172690829767E+00, \
            52.0734519015142202671640200482E+00, \
            57.2876345410929400754514841078E+00, \
            62.9525659469066302071906336861E+00, \
            69.1435133801098924457366348147E+00, \
            75.9666870142470623437939790250E+00, \
            83.5816372232708807614192336050E+00, \
            92.2511394441351012341481184391E+00, \
            102.477844336823322575825984750E+00, \
            115.554756448995807306876850793E+00 ] )

    w = np.array ( [ \
           0.106097745553686759448980241986E+00, \
           0.205582983661932603502389046086E+00, \
           0.232126523496060850848680143719E+00, \
           0.196207372769141916829837191484E+00, \
           0.132744856705171098099698375677E+00, \
           0.0738518038877138714048058524075E+00, \
           0.0342232334108640270351258175641E+00, \
           0.0132939751808086665861981468532E+00, \
           0.00434094309504623645941229723703E+00, \
            0.0011922509906686840510776728263E+00, \
            0.000275158225582396584420253012954E+00, \
            0.0000532433409922782412444424323192E+00, \
            8.60957132646331618369236329569E-06, \
            1.15837796102469195604266695945E-06, \
            1.28985114856525884538052927779E-07, \
            1.18096786980325241031580363325E-08, \
            8.82276640967020246770192412272E-10, \
            5.32961213410302701363055555216E-11, \
            2.57550403748317439431393144398E-12, \
            9.8314133225207825980561863437E-14, \
            2.92041495556546845392792035892E-15, \
            6.63077156752381637730149511056E-17, \
            1.12609863704995018019882580368E-18, \
            1.39311657122392009414616980902E-20, \
            1.21481009891544297673141523063E-22, \
            7.16158181142099840535743381278E-25, \
            2.70320712488116872172720734689E-27, \
            6.07192361286922243586897316027E-30, \
            7.32134211132579407517616095945E-33, \
            4.06131706145569795511645700604E-36, \
            8.04952284545203726871355981553E-40, \
            3.52902990360469937522008596417E-44, \
            1.01716656299412569799194166119E-49 ] )

  elif ( n == 63 ):

    x = np.array ( [ \
           0.0227688937325761537859943302486E+00, \
           0.119983252427278247157714164264E+00, \
           0.294941854447701495774277385174E+00, \
           0.547790878962377253638650737759E+00, \
           0.878690611799319016738955670523E+00, \
           1.28784643359197063023092077886E+00, \
           1.77551238153885537639794632687E+00, \
           2.34199255670859892560556283377E+00, \
           2.98764232232464739399767310536E+00, \
            3.71286959920180003462996374134E+00, \
            4.51813633495035843911055685616E+00, \
            5.40396017818259462869025997827E+00, \
            6.37091637878653302203922508918E+00, \
            7.41963993393117111548884931990E+00, \
            8.55082800084033283125890487222E+00, \
            9.76524259992453668070045929780E+00, \
            11.0637136351406617362205504106E+00, \
            12.4471422623564927497986875693E+00, \
            13.9165046410578185629129670082E+00, \
            15.4728561100362964247771436078E+00, \
            17.1173358338635887531169003039E+00, \
            18.8511719741548568508734837875E+00, \
            20.6756874480565156603772656674E+00, \
            22.5923063463115283812922777600E+00, \
            24.6025610949726388837006427600E+00, \
            26.7081004587373439697790879988E+00, \
            28.9106985004513826401777181032E+00, \
            31.2122646311759128854777738208E+00, \
            33.6148549091011548365988428883E+00, \
            36.1206847744848230563063287408E+00, \
            38.7321434429335821456260416077E+00, \
            41.4518102223187411911147261814E+00, \
            44.2824730714792338393588571346E+00, \
            47.2271497842956868989350952315E+00, \
            50.2891122642406957617490218394E+00, \
            53.4719144567886528083482806195E+00, \
            56.7794246363420622130997810571E+00, \
            60.2158629090198628864175501144E+00, \
            63.7858450042359746317011396018E+00, \
            67.4944337022938858303743256950E+00, \
            71.3471996042952662866548033761E+00, \
            75.3502934256532342542905047443E+00, \
            79.5105326299863091495553913548E+00, \
            83.8355060808722578433398176585E+00, \
            88.3337015703543690861127663265E+00, \
            93.0146627285585474053033990371E+00, \
            97.8891841475781400433867276771E+00, \
            102.969556907413816507839527468E+00, \
            108.269881619615953922263509672E+00, \
            113.806473502874627389344859559E+00, \
            119.598395388304586669624529633E+00, \
            125.668172558561194312911963033E+00, \
            132.042772720911657465855905830E+00, \
            138.754984181037890781675905675E+00, \
            145.845413183135403582839942484E+00, \
            153.365484594978636237108159627E+00, \
            161.382151948137612435621726696E+00, \
            169.985706006658394387951753012E+00, \
            179.303662474015809102518278585E+00, \
            189.527895965324754736687213330E+00, \
            200.975211599246567416286718410E+00, \
            214.253685366387886426980562964E+00, \
            230.934657470897039712465629851E+00 ] )

    w = np.array ( [ \
           0.0571186332138689798115872833905E+00, \
           0.120674760906403952833199320363E+00, \
           0.159250010965818737238705610965E+00, \
           0.168751783275607992345961929636E+00, \
           0.153666419776689566961937113101E+00, \
           0.123687706147164816410866522619E+00, \
           0.0892750988548486715452791500574E+00, \
           0.0582584854461059449575718257252E+00, \
           0.0345466575459925808747170858125E+00, \
            0.0186756859857146567982865525912E+00, \
            0.00922334490440935365284900752416E+00, \
            0.00416712506848395927625826634702E+00, \
            0.0017238120299900582715386728542E+00, \
            0.00065320845029716311169340559359E+00, \
            0.000226776446709095869524051732075E+00, \
            0.0000721276741548106684107502702349E+00, \
            0.0000210112611804664845988115368512E+00, \
            5.60355008933572127491815360713E-06, \
            1.3673642785604888017836641282E-06, \
            3.050726393019581724073609719E-07, \
            6.21800618393097635599817754E-08, \
            1.1566529551931711260022449E-08, \
            1.9614588267565478081534782E-09, \
            3.028617119570941124433476E-10, \
            4.252134453940068676901296E-11, \
            5.42022205780738193346988E-12, \
            6.2627306838597672554167E-13, \
            6.5474443156573322992307E-14, \
            6.18155758087291818463E-15, \
            5.259272136350738140426E-16, \
            4.023092009264648401539E-17, \
            2.7600740511819536505E-18, \
            1.69369467569682960533E-19, \
            9.2689146872177087315E-21, \
            4.509373906036563294E-22, \
            1.9435162876132376574E-23, \
            7.392627089516920704E-25, \
            2.471436415443463262E-26, \
            7.228864944674159766E-28, \
            1.840761729261403936E-29, \
            4.058349856684196011E-31, \
            7.70004964164383681E-33, \
            1.248850576499933433E-34, \
            1.71850002267670107E-36, \
            1.989637263667239694E-38, \
            1.919967137880405827E-40, \
            1.527858828552216692E-42, \
            9.9054752688842143E-45, \
            5.159752367302921188E-47, \
            2.124984666408411125E-49, \
            6.790385276685291059E-52, \
            1.6466654148296177468E-54, \
            2.9509065402691055027E-57, \
            3.78384206475710519849E-60, \
            3.33581300685424318782E-63, \
            1.922346102227388098136E-66, \
            6.781269696108301687278E-70, \
            1.34047528024406046076205E-73, \
            1.3109745101805029757648E-77, \
            5.262486388140178738869458E-82, \
            6.3780013856587414257760666E-87, \
            1.299707894237292456634747392E-92, \
            1.00085114969687540634437401684E-99 ] )
 
  elif ( n == 64 ):

    x = np.array ( [ \
           0.0224158741467052800228118848190E+00, \
           0.118122512096770479797466436710E+00, \
           0.290365744018036483999130066385E+00, \
           0.539286221227979039318144947812E+00, \
           0.865037004648113944619955074710E+00, \
           1.26781404077524139811570887769E+00, \
           1.74785962605943625282996395129E+00, \
           2.30546373930750871854807054389E+00, \
           2.94096515672525184067946815211E+00, \
            3.65475265020729052703539791209E+00, \
            4.44726634331309435674255098016E+00, \
            5.31899925449639034352210985919E+00, \
            6.27049904692365391291106464633E+00, \
            7.30237000258739574722349840952E+00, \
            8.41527523948302419449521859120E+00, \
            9.60993919279610803576288204955E+00, \
            10.8871503838863721425945504202E+00, \
            12.2477645042443016181623692907E+00, \
            13.6927078455475051527299325746E+00, \
            15.2229811115247288480082687834E+00, \
            16.8396636526487372105288380392E+00, \
            18.5439181708591905236196259711E+00, \
            20.3369959487302355011498158064E+00, \
            22.2202426659508765399221543471E+00, \
            24.1951048759332539898864438802E+00, \
            26.2631372271184857851260239548E+00, \
            28.4260105275010272994997715268E+00, \
            30.6855207675259717710485823984E+00, \
            33.0435992364378291255202106805E+00, \
            35.5023238911412095869787785351E+00, \
            38.0639321656464682603573179150E+00, \
            40.7308354444586263657318695132E+00, \
            43.5056354664215298527031849317E+00, \
            46.3911429786161920736053999424E+00, \
            49.3903990256246866792358008227E+00, \
            52.5066993413463016501792769805E+00, \
            55.7436224132783804633357112912E+00, \
            59.1050619190171066088487420918E+00, \
            62.5952644001513955960550179012E+00, \
            66.2188732512475643822137626710E+00, \
            69.9809803771468292285346579722E+00, \
            73.8871872324829632109574031135E+00, \
            77.9436774344631203136879758706E+00, \
            82.1573037783193042951958683422E+00, \
            86.5356933494565182102162783753E+00, \
            91.0873756131330901456367153493E+00, \
            95.8219400155207320947672154365E+00, \
            100.750231969513979629259261451E+00, \
            105.884599468799949356360427851E+00, \
            111.239207524439582063484736638E+00, \
            116.830445051306498463386669077E+00, \
            122.677460268538576577419690565E+00, \
            128.802878769237672512753623054E+00, \
            135.233787949525827833980498879E+00, \
            142.003121489931519025140038291E+00, \
            149.151665900049388587293462932E+00, \
            156.731075132671161233616960814E+00, \
            164.808602655150522993190109025E+00, \
            173.474946836424274522152844867E+00, \
            182.858204691431463646342794510E+00, \
            193.151136037072911479385527417E+00, \
            204.672028485059455949064433343E+00, \
            218.031851935328516332452384448E+00, \
            234.809579171326164713055529725E+00 ] )

    w = np.array ( [ \
           0.0562528423390298457410218545063E+00, \
           0.119023987312426027814903505889E+00, \
           0.157496403862144523820196434706E+00, \
           0.167547050415773947880904411659E+00, \
           0.153352855779236618085454792564E+00, \
           0.124221053609329744512613782193E+00, \
           0.0903423009864850577389741092016E+00, \
           0.0594777557683550242122469974397E+00, \
           0.0356275189040360718541657353369E+00, \
            0.0194804104311664060433373802715E+00, \
            0.00974359489938200224010796027138E+00, \
            0.00446431036416627529236482419054E+00, \
            0.00187535958132311482675012822252E+00, \
            0.000722646981575005122719108706619E+00, \
            0.00025548753283349670971444840218E+00, \
            0.0000828714353439694217906322403988E+00, \
            0.0000246568639678855874597337022172E+00, \
            6.7267138788296685276125455363E-06, \
            1.6817853699640888978212010865E-06, \
            3.850812981546684414827886111E-07, \
            8.06872804099049979041511092E-08, \
            1.54572370675768882800370393E-08, \
            2.7044801476174814099886074E-09, \
            4.316775475427200912314164E-10, \
            6.27775254176145220165296E-11, \
            8.30631737628895806387893E-12, \
            9.9840317872201640558973E-13, \
            1.0883538871166626853261E-13, \
            1.0740174034415901864828E-14, \
            9.57573723157444210559E-16, \
            7.69702802364858609886E-17, \
            5.56488113745402536653E-18, \
            3.6097564090104464983E-19, \
            2.0950953695489462348E-20, \
            1.0847933010975493612E-21, \
            4.994699486363804116E-23, \
            2.037836974598822311E-24, \
            7.339537564278837039E-26, \
            2.323783082198694261E-27, \
            6.43823470690876242E-29, \
            1.553121095788275271E-30, \
            3.24425009201953731E-32, \
            5.8323862678362015E-34, \
            8.96325483310285406E-36, \
            1.168703989550736241E-37, \
            1.282055984359980381E-39, \
            1.172094937405002292E-41, \
            8.83533967232860498E-44, \
            5.42495559030618659E-46, \
            2.675542666678893829E-48, \
            1.042917031411367078E-50, \
            3.152902351957772624E-53, \
            7.22954191064752234E-56, \
            1.2242353012300822645E-58, \
            1.48216850490191041178E-61, \
            1.23251934881451880806E-64, \
            6.69149900457126952681E-68, \
            2.220465941850448995507E-71, \
            4.1209460947388762499791E-75, \
            3.77439906189648917041762E-79, \
            1.414115052917619417463147E-83, \
            1.5918330640413679178610318E-88, \
            2.98948434886063430774131269E-94, \
            2.0890635084369527708281542544E-101 ] )

  elif ( n == 65 ):

    x = np.array ( [ \
           0.0220736343882500875264595737093E+00, \
           0.116318612213376151729622328698E+00, \
           0.285929513070813951834551909860E+00, \
           0.531041775784488438911664842933E+00, \
           0.851801670809046586655299989571E+00, \
           1.24839628201831707727195703687E+00, \
           1.72105687981755734816623923359E+00, \
           2.27006018491690256109784837001E+00, \
           2.89572940756799471192249006458E+00, \
            3.59843535756478540694788870796E+00, \
            4.37859769744118464804519621154E+00, \
            5.23668636694320050319815958793E+00, \
            6.17322319658730631921440545744E+00, \
            7.18878372629467202131889616235E+00, \
            8.28399924588871831467573911308E+00, \
            9.45955907610065448076092041454E+00, \
            10.7162131111897048393914349801E+00, \
            12.0547746472322707150580323735E+00, \
            13.4761235235671154056092903386E+00, \
            14.9812096088541520753799758172E+00, \
            16.5710566677964491577962746244E+00, \
            18.2467666498987672118974219097E+00, \
            20.0095244478287060731090711532E+00, \
            21.8606031801774165914390699117E+00, \
            23.8013700618933285635853631176E+00, \
            25.8332929356397220962712840077E+00, \
            27.9579475491204073878989540109E+00, \
            30.1770256774182582795717815112E+00, \
            32.4923442060863420003362903722E+00, \
            34.9058553107319841822666865568E+00, \
            37.4196578929107315489849223258E+00, \
            40.0360104612770088389674875188E+00, \
            42.7573456823686148915804841094E+00, \
            45.5862868687358177811114530444E+00, \
            48.5256667254367437021219033875E+00, \
            51.5785487419130140104165726852E+00, \
            54.7482516984863756567192528045E+00, \
            58.0383778598867354584946224426E+00, \
            61.4528455586293273580430507845E+00, \
            64.9959270371996369214889214525E+00, \
            68.6722926314626183977917033408E+00, \
            72.4870626544527259157609330997E+00, \
            76.4458687019847672439750100021E+00, \
            80.5549265807842719390299008467E+00, \
            84.8211237010524840445780520727E+00, \
            89.2521246438779093867045988317E+00, \
            93.8564998060605244752886814683E+00, \
            98.6438836854008198627513004124E+00, \
            103.625171719648548339736534290E+00, \
            108.812767977808831403825388295E+00, \
            114.220900975902615729136419234E+00, \
            119.866032356536657109576887729E+00, \
            125.767394661236316522917056970E+00, \
            131.947712599442095787498603776E+00, \
            138.434191890473005752666966171E+00, \
            145.259909991527292147157412636E+00, \
            152.465831757831086161761248192E+00, \
            160.103837850755827943698932303E+00, \
            168.241478626055331550636477652E+00, \
            176.969855979856624954098184957E+00, \
            186.417642483351089954653964415E+00, \
            196.778474440876949259615139650E+00, \
            208.372107380940491095442543113E+00, \
            221.812376576320945562507410640E+00, \
            238.685811594674270102373709659E+00 ] )

    w = np.array ( [ \
           0.0554129011565536469555170462551E+00, \
           0.117417396564162014386769936525E+00, \
           0.15577793159527363526750345236E+00, \
           0.166347955884031811873697185854E+00, \
           0.153013207065446887512281359026E+00, \
           0.12471061536737329712442529837E+00, \
           0.0913671486268474804579363734334E+00, \
           0.0606693673532322224974724445698E+00, \
           0.0366985078337756899608575633553E+00, \
            0.0202884358923229233158787730215E+00, \
            0.0102732022687699783894639990081E+00, \
            0.00477128781081110626106879095602E+00, \
            0.00203437021965744474885076853755E+00, \
            0.00079674216708789273511811886929E+00, \
            0.000286683812097562728436084278246E+00, \
            0.0000947743836779584423250711498309E+00, \
            0.0000287808776386491122522878225936E+00, \
            8.025921887785674361327140519E-06, \
            2.0542534210210521080625753887E-06, \
            4.822974163227069271800228998E-07, \
            1.037906330975825689484858253E-07, \
            2.04556458252437904249066042E-08, \
            3.6885834829334325209249956E-09, \
            6.07893150020096839531226E-10, \
            9.14524981574057744811517E-11, \
            1.25427414380884616209197E-11, \
            1.56600212784699337922365E-12, \
            1.7771074191193507379193E-13, \
            1.829851898040443279934E-14, \
            1.70645929547049792703E-15, \
            1.438412537484673440005E-16, \
            1.09354404172789017674E-17, \
            7.4805627565827998507E-19, \
            4.5927490046001844919E-20, \
            2.5237976161210732972E-21, \
            1.2376030276622370811E-22, \
            5.398129612170324038E-24, \
            2.086925656272980914E-25, \
            7.12363601216912351E-27, \
            2.13797949495352507E-28, \
            5.61585996656691837E-30, \
            1.2845455347843963E-31, \
            2.5444410680246895E-33, \
            4.33793017530204526E-35, \
            6.3222072485073684E-37, \
            7.8174607001716233E-39, \
            8.1320382378781478E-41, \
            7.0491916339430245E-43, \
            5.03749289878460876E-45, \
            2.93162035252999008E-47, \
            1.370002490040754814E-49, \
            5.05827802154356236E-52, \
            1.447822639997111427E-54, \
            3.141466864703300069E-57, \
            5.03056294905086669E-60, \
            5.7547901892214244076E-63, \
            4.5172924325696051375E-66, \
            2.31224468889972999556E-69, \
            7.22311071834335770012E-73, \
            1.2595483022441380495635E-76, \
            1.08123622593537779961256E-80, \
            3.78397004144107162756714E-85, \
            3.9595563374024690284872814E-90, \
            6.85929105947869810086088696E-96, \
            4.3543678721167358517710196959E-103 ] )

  elif ( n == 127 ):

    x = np.array ( [ \
           0.0113396352985186116918931696313E+00, \
           0.0597497534357266202813482370574E+00, \
           0.146850986907461676123882236874E+00, \
           0.272675907358595531313780082789E+00, \
           0.437246006441926655545770358699E+00, \
           0.640586882225669295335764164000E+00, \
           0.882729686390583644814876536500E+00, \
           1.16371141601665376615605847010E+00, \
           1.48357501528346138913135848610E+00, \
            1.84236943516135653806863208099E+00, \
            2.24014968395790242445133156565E+00, \
            2.67697687801413036921678699612E+00, \
            3.15291829570828255657715083088E+00, \
            3.66804743603047525402263399265E+00, \
            4.22244408233018884559778766674E+00, \
            4.81619437158705024756655350873E+00, \
            5.44939086945594167558621789084E+00, \
            6.12213265129972541939445847632E+00, \
            6.83452538941226681122379949733E+00, \
            7.58668144663674721742059868368E+00, \
            8.37871997659327252548421206595E+00, \
            9.21076703074265587779225061024E+00, \
            10.0829556725286438091664393536E+00, \
            10.9954260988581254298031473588E+00, \
            11.9483257691977259976106051279E+00, \
            12.9418095425855310537233810982E+00, \
            13.9760398228785065200144056687E+00, \
            15.0511867125795236315747963654E+00, \
            16.1674281756128529229773950518E+00, \
            17.3249502094436734465611637126E+00, \
            18.5239470269656885608117113093E+00, \
            19.7646212486115041040716693869E+00, \
            21.0471841051731836068770440201E+00, \
            22.3718556518555428176481239181E+00, \
            23.7388649941224971836523137887E+00, \
            25.1484505259373682340772783856E+00, \
            26.6008601810417496072533842798E+00, \
            28.0963516979646192017539612921E+00, \
            29.6351928995041789106102271386E+00, \
            31.2176619874797591442144671526E+00, \
            32.8440478536104304605229513413E+00, \
            34.5146504074411491491056359474E+00, \
            36.2297809223068040196153885089E+00, \
            37.9897624003999564359687801403E+00, \
            39.7949299580899617783964371417E+00, \
            41.6456312327301807051539908975E+00, \
            43.5422268122868595499508929938E+00, \
            45.4850906892287911379961513367E+00, \
            47.4746107402319647194687665991E+00, \
            49.5111892333790877167288845844E+00, \
            51.5952433646712444431827712669E+00, \
            53.7272058258193167582881400691E+00, \
            55.9075254054475533058306059917E+00, \
            58.1366676260224391970775260257E+00, \
            60.4151154190185902957071920538E+00, \
            62.7433698410518097002071267427E+00, \
            65.1219508339499963119560254171E+00, \
            67.5513980319978863144118724431E+00, \
            70.0322716198845845112298711920E+00, \
            72.5651532452068490908886694168E+00, \
            75.1506469897399352993543623251E+00, \
            77.7893804040858160006474054621E+00, \
            80.4820056107507292058039629268E+00, \
            83.2292004811959148867961200190E+00, \
            86.0316698929535829667982387326E+00, \
            88.8901470735120510996525185443E+00, \
            91.8053950383581779949712501705E+00, \
            94.7782081313315832053870310348E+00, \
            97.8094136763051164110541101154E+00, \
            100.899873750172859403719397622E+00, \
            104.050487088215989347040768450E+00, \
            107.262191134146004284231164014E+00, \
            110.535964248515005306027713513E+00, \
            113.872828090758394853483761877E+00, \
            117.273850191925177740954778864E+00, \
            120.740146737188801061739780027E+00, \
            124.272885579556983542595064469E+00, \
            127.873289508859426450938417454E+00, \
            131.542639803143669218093777421E+00, \
            135.282280093118369701327381064E+00, \
            139.093620574329700139644220870E+00, \
            142.978142606436017768082277536E+00, \
            146.937403744373665494410809691E+00, \
            150.973043252521871274925114375E+00, \
            155.086788160346125722296414206E+00, \
            159.280459926632882354019569899E+00, \
            163.555981789575711040159671821E+00, \
            167.915386891943601342455471847E+00, \
            172.360827284738125368381561917E+00, \
            176.894583929601921763116749935E+00, \
            181.519077840368130692275288340E+00, \
            186.236882528281123738612025304E+00, \
            191.050737944509291967908366108E+00, \
            195.963566148798798378390025430E+00, \
            200.978488976000251536964755261E+00, \
            206.098848024688711121272830428E+00, \
            211.328227356716552605723772570E+00, \
            216.670479376582303234770894658E+00, \
            222.129754459296872462673049638E+00, \
             227.710535020722324190891324313E+00, \
             233.417674882826024533677753226E+00, \
             239.256444988303086200187496671E+00, \
             245.232586778715671725312540190E+00, \
             251.352374887181280300055009918E+00, \
             257.622691237920614130761918823E+00, \
             264.051113229082405517543772418E+00, \
             270.646019457227967492991117186E+00, \
             277.416717501636510717983882181E+00, \
             284.373599742208703266744028731E+00, \
             291.528335213464957195812820216E+00, \
             298.894108370282486008788956154E+00, \
             306.485919782626113204181124239E+00, \
             314.320969864711774874000075076E+00, \
             322.419155891286796833494403613E+00, \
             330.803726638024056519338473349E+00, \
             339.502161278324337477353675960E+00, \
             348.547375594726973554807617874E+00, \
             357.979420280298454540490074431E+00, \
             367.847945200760045788583414229E+00, \
             378.215906231355328183329791889E+00, \
             389.165391412510041015794753252E+00, \
             400.807293314517025899963612864E+00, \
             413.298536817793844180082600819E+00, \
             426.875791536636755382885090171E+00, \
             441.930854853108414124603092718E+00, \
             459.218046398884299819712673132E+00, \
             480.693782633883738597042692293E+00 ] )

    w = np.array ( [ \
           0.0287732466920001243557700103008E+00, \
           0.0638174681751346493634809492651E+00, \
           0.0919196697215705713898641946531E+00, \
           0.11054167914413766381245463003E+00, \
           0.118797716333758501883283294227E+00, \
           0.117378185300526951488044516301E+00, \
           0.108193059841805514883351455812E+00, \
           0.0938270752904896280803772614011E+00, \
           0.0769664509605888439958224859284E+00, \
            0.0599349039129397143325707300635E+00, \
            0.0444177420738890013717083162729E+00, \
            0.0313850809662523209830093722151E+00, \
            0.021172316041924506411370709025E+00, \
            0.0136501453642305416521711855646E+00, \
            0.00841728527105991722793666573854E+00, \
            0.00496749900598827605159128586202E+00, \
            0.00280699038950018846319619574464E+00, \
            0.00151929510039419524604453410578E+00, \
            0.000787890287517960840862172871405E+00, \
            0.00039156751064868450584507324649E+00, \
            0.000186524342688258605500935662601E+00, \
            0.0000851731604155766219088098281602E+00, \
            0.0000372856391978530377121453215777E+00, \
            0.0000156484167917129939474478052968E+00, \
            6.2964340695224829035692735525E-06, \
            2.42889297113287245745413799382E-06, \
            8.9824607890051007201922871545E-07, \
            3.18441747407603537107429663281E-07, \
            1.08212729055668392118618075427E-07, \
            3.52450767506355360159027790853E-08, \
            1.10012243657193474070638397617E-08, \
            3.29040796167179321253293430033E-09, \
            9.4289145237889976419772700773E-10, \
            2.58825789046683181840501953093E-10, \
            6.80474371033707626309422590176E-11, \
            1.71313988051208378353995644756E-11, \
            4.12917445240528654694439223049E-12, \
            9.52641897188072732207076648735E-13, \
            2.10326044324424259329629420475E-13, \
            4.44271519387293528609404342858E-14, \
            8.97605003628337033233198464055E-15, \
            1.73415114077692870746279483468E-15, \
            3.20280995489883566314943798352E-16, \
            5.65313889507936820226607420952E-17, \
            9.53296727990265912345880440259E-18, \
            1.53534534773101425652885094376E-18, \
            2.36089621794673656860578421322E-19, \
            3.46487427944566113321938766532E-20, \
            4.85152418970864613201269576635E-21, \
            6.47862286335198134281373737907E-22, \
            8.2476020965403242936448553126E-23, \
            1.0005361880214719793491658283E-23, \
            1.1561395116207304954233181264E-24, \
            1.271934273116792265561213426E-25, \
            1.331658471416537296734000416E-26, \
            1.32612184546789440336461085E-27, \
            1.25549954476439498072860741E-28, \
            1.1294412178579462703240913E-29, \
            9.649102027956211922850061E-31, \
            7.82418467683020993967331E-32, \
            6.01815035422196266582499E-33, \
            4.38824827049617415515105E-34, \
            3.0314137647517256304036E-35, \
            1.9826016543944539545225E-36, \
            1.2267623373665926559014E-37, \
            7.176393169250888894381E-39, \
            3.965937883383696358411E-40, \
            2.068897055386804009958E-41, \
            1.017958701797951724527E-42, \
            4.72008277459863746257E-44, \
            2.06068289855533748257E-45, \
            8.4627575907305987246E-47, \
            3.2661123687088798658E-48, \
            1.1833939207883162381E-49, \
            4.021120912389501381E-51, \
            1.2799824394111125389E-52, \
            3.81238777475488465E-54, \
            1.061205754270115677E-55, \
            2.757144694720040359E-57, \
            6.67725442409284929E-59, \
            1.505243838386823495E-60, \
            3.15389868001137585E-62, \
            6.13266142994831808E-64, \
            1.10485100303248106E-65, \
            1.84105635380913481E-67, \
            2.83239265700528322E-69, \
            4.01544098437636555E-71, \
            5.23515302156837088E-73, \
            6.2634476665005101E-75, \
            6.861221053566653E-77, \
            6.8651298840956019E-79, \
            6.25813884337280849E-81, \
            5.1833271237514904E-83, \
            3.88936215719184435E-85, \
            2.63577113794769328E-87, \
            1.60788512939179797E-89, \
            8.79780420709689396E-92, \
            4.30134050774951099E-94, \
            1.871343588134283853E-96, \
             7.212574470806047168E-99, \
             2.450874606217787438E-101, \
             7.304209461947087578E-104, \
             1.8983290818383463538E-106, \
             4.2757400244246684123E-109, \
             8.2894681420515755691E-112, \
             1.37294322193244000131E-114, \
             1.926546412640497322204E-117, \
             2.269334450330135482614E-120, \
             2.2209290603717355061909E-123, \
             1.7851087685544512662857E-126, \
             1.16309319903871644674312E-129, \
             6.05244435846523922909528E-133, \
             2.472956911506352864762838E-136, \
             7.778906500648941036499721E-140, \
             1.8409738662712607039570678E-143, \
             3.1900921131079114970179072E-147, \
             3.917948713917419973761766608E-151, \
             3.2782158394188697053774429821E-155, \
             1.77935907131388880628196401287E-159, \
             5.88823534089326231574678353812E-164, \
             1.09572365090711698777472032739E-168, \
             1.02816211148670008982850769758E-173, \
             4.1704725557697758145816510854E-179, \
             5.8002877720316101774638319602E-185, \
             1.88735077458255171061716191011E-191, \
             6.91066018267309116827867059509E-199, \
             4.35068132011058556283833133344E-208 ] )

  elif ( n == 128 ):

    x = np.array ( [ \
           0.0112513882636759629608518403162E+00, \
           0.0592847412690264542879220089614E+00, \
           0.145707966594312465141854059102E+00, \
           0.270553178758665066190760897100E+00, \
           0.433841407553836803056096580754E+00, \
           0.635597665781621938340867677969E+00, \
           0.875852384546520779155346013261E+00, \
           1.15464170197439795008153355708E+00, \
           1.47200756316673547554446633038E+00, \
            1.82799777831235028535984528718E+00, \
            2.22266607156190244817896452914E+00, \
            2.65607212988348119522885329309E+00, \
            3.12828165502791695498310369738E+00, \
            3.63936641985240321221074522169E+00, \
            4.18940432959404797478493079865E+00, \
            4.77847948843487609165724239213E+00, \
            5.40668227160049918527893820105E+00, \
            6.07410940319653684309155844506E+00, \
            6.78086403997562541104804929943E+00, \
            7.52705586122937588585512279842E+00, \
            8.31280116500777060337884381191E+00, \
            9.13822297088039239600262641969E+00, \
            10.0034511294682220892682761435E+00, \
            10.9086224389908825478488613010E+00, \
            11.8538807690918568038332644538E+00, \
            12.8393771922232496874551935673E+00, \
            13.8652701228920803029536799971E+00, \
            14.9317254650919274737473553133E+00, \
            16.0389167682670793509213783428E+00, \
            17.1870253921812651027585044591E+00, \
            18.3762406810896949333827523370E+00, \
            19.6067601476416467279054690989E+00, \
            20.8787896669713729158932014403E+00, \
            22.1925436814678369066763923182E+00, \
            23.5482454167489205609249730097E+00, \
            24.9461271094034886279510396640E+00, \
            26.3864302471052908976269305132E+00, \
            27.8694058217463902295696818564E+00, \
            29.3953145962849137215656288381E+00, \
            30.9644273860527540023220861317E+00, \
            32.5770253553237501781419486456E+00, \
            34.2334003300022426604794108753E+00, \
            35.9338551273561538107722924963E+00, \
            37.6787039037883744300655582016E+00, \
            39.4682725217157641271489033004E+00, \
            41.3028989367070896380080417637E+00, \
            43.1829336061203832438783635225E+00, \
            45.1087399205772317441506148507E+00, \
            47.0806946597172168560725351128E+00, \
            49.0991884737910268021535852860E+00, \
            51.1646263927766594446404335916E+00, \
            53.2774283648407739161085367944E+00, \
            55.4380298261178918683089638291E+00, \
            57.6468823039452288144249811220E+00, \
            59.9044540558720556965292635062E+00, \
            62.2112307469614582456791552962E+00, \
            64.5677161681212154290410515467E+00, \
            66.9744329984415610548027156195E+00, \
            69.4319236147834299557621097742E+00, \
            71.9407509521543751573018481062E+00, \
            74.5014994187340277930279831855E+00, \
            77.1147758697705705283198924354E+00, \
            79.7812106449685528544582124991E+00, \
            82.5014586744314529140391768845E+00, \
            85.2762006587153587377964042582E+00, \
            88.1061443290995036940317393258E+00, \
            90.9920257947926131560303030245E+00, \
            93.9346109844796944955244642925E+00, \
            96.9346971903819404516199551240E+00, \
            99.9931147238642715216213000267E+00, \
            103.110728692593987392319749158E+00, \
            106.288440910345442668426129659E+00, \
            109.527191951777550806618056918E+00, \
            112.827963365904193877333487264E+00, \
            116.191780063556780940235871708E+00, \
            119.619712895932010462348887420E+00, \
            123.112881443360190060911814509E+00, \
            126.672457035760183662338694957E+00, \
            130.299666028913462587217492864E+00, \
            133.995793363747964343582120836E+00, \
            137.762186439339380964302666578E+00, \
            141.600259334393040305789642722E+00, \
            145.511497416659592393640597008E+00, \
            149.497462385177707088173175451E+00, \
            153.559797796566440117982748261E+00, \
            157.700235133978105059095336546E+00, \
            161.920600485975634163753629031E+00, \
            166.222821912768875092875739160E+00, \
            170.608937589242234646550663310E+00, \
            175.081104828414604880617405502E+00, \
            179.641610105866994602634964639E+00, \
            184.292880225846805341834505020E+00, \
            189.037494793954109001292998345E+00, \
            193.878200190472967540802875940E+00, \
            198.817925273720602804745944994E+00, \
            203.859799085769844571664824897E+00, \
            209.007170885510867853387511181E+00, \
            214.263632898788021280527758492E+00, \
            219.633046255578174038387401024E+00, \
             225.119570684209027756659796566E+00, \
             230.727698658203619681658868680E+00, \
             236.462294850177665966018904158E+00, \
             242.328641949702698267864519866E+00, \
             248.332494162357178892016601780E+00, \
             254.480140044869131893543803358E+00, \
             260.778476773579736538560064538E+00, \
             267.235098528953836763992472029E+00, \
             273.858402462693609793414602648E+00, \
             280.657716776323492397504100977E+00, \
             287.643456899219330638473677900E+00, \
             294.827317787647739179806672104E+00, \
             302.222513246449465380535981711E+00, \
             309.844077326612663447772363643E+00, \
             317.709248954906289495678052340E+00, \
             325.837970121194949650401277931E+00, \
             334.253542067654135375184450174E+00, \
             342.983506273825316408508913329E+00, \
             352.060853546526185083043426984E+00, \
             361.525726392325047599066851839E+00, \
             371.427889214327523078517984867E+00, \
             381.830444119061080196207616882E+00, \
             392.815671240808098809377819898E+00, \
             404.494724750515074389666071660E+00, \
             417.024902977989015820197277594E+00, \
             430.643444166597381558323551668E+00, \
             445.743096973927989652171720726E+00, \
             463.080034109446258208013793406E+00, \
             484.615543986443976044063131110E+00 ] )

    w = np.array ( [ \
           0.0285518444532397286290731773612E+00, \
           0.0633502117845051187797978127259E+00, \
           0.0913083813661343144231616325903E+00, \
           0.109913900410911746101013915833E+00, \
           0.118274171034173698789809688874E+00, \
           0.117045739000406721566458439207E+00, \
           0.108089987545568415436473783125E+00, \
           0.0939428886389285017878088436356E+00, \
           0.0772536687978980532077800252359E+00, \
            0.0603270562656615705389303086003E+00, \
            0.0448473482471952140682424657998E+00, \
            0.0317969479368768461739632484821E+00, \
            0.0215301494537944439261107285438E+00, \
            0.0139369517338463483277576885975E+00, \
            0.00863158538020224714884473096489E+00, \
            0.00511777701366922852873936722845E+00, \
            0.00290634743648595585817980077219E+00, \
            0.00158143294331667939723416013489E+00, \
            0.000824738985098812150435438593253E+00, \
            0.000412326088539694730970290830804E+00, \
            0.000197649426442591498620529889783E+00, \
            0.0000908515788782451508022826306153E+00, \
            0.0000400484927835805298977887660442E+00, \
            0.0000169307623980817855755102888475E+00, \
            6.86452529111068208938636278412E-06, \
            2.66921659814210266015872228584E-06, \
            9.95364010286384477177483332196E-07, \
            3.55943575300306543988020166563E-07, \
            1.22053255194881194831205615734E-07, \
            4.01279192093563506890167766024E-08, \
            1.26481141474759786445650110908E-08, \
            3.82148972942657229023411372003E-09, \
            1.10664105922734169994480044024E-09, \
            3.07100923709742319582290034639E-10, \
            8.16549938415448956026437885004E-11, \
            2.07985363278137784234189612116E-11, \
            5.0739537708398704043296986402E-12, \
            1.1853143771796112305093733131E-12, \
            2.65092752372887358600565488195E-13, \
            5.67463221575765876681065606161E-14, \
            1.16237381470751589221529434901E-14, \
            2.27776629270238637919733104451E-15, \
            4.26883197029764927739172104126E-16, \
            7.64928879936327510525948457803E-17, \
            1.31013139198382464188082886821E-17, \
            2.1441452341246636343706788692E-18, \
            3.35194428720884780801470729044E-19, \
            5.00373308645947376823179365121E-20, \
            7.13003064195856212049702464626E-21, \
            9.6945407403972664035320905829E-22, \
            1.25728475563978459844059927432E-22, \
            1.5546610955630634482202731199E-23, \
            1.832109793253421778719084254E-24, \
            2.056797978136734920722781372E-25, \
            2.19866605262329119257657449E-26, \
            2.23691600732428936729406222E-27, \
            2.1649606446339054400256309E-28, \
            1.9922276806187937873877251E-29, \
            1.742153886325439585907653E-30, \
            1.446949786106284637699605E-31, \
            1.1407517061230822834189E-32, \
            8.5318050978102090722116E-34, \
            6.04970117793885843505E-35, \
            4.0643432432648003017795E-36, \
            2.585349374987909630703E-37, \
            1.556028762522623447585E-38, \
            8.85462584966333001103E-40, \
            4.76045751736458068032E-41, \
            2.416078510661232205E-42, \
            1.15664705033873749321E-43, \
            5.2185106194923759952E-45, \
            2.2169743353361803305E-46, \
            8.86010275661369606E-48, \
            3.327811159201095553E-49, \
            1.173490043078302544E-50, \
            3.880967726420921431E-52, \
            1.202426327933061418E-53, \
            3.48602304410554638E-55, \
            9.44554522159556681E-57, \
            2.38888427455968395E-58, \
            5.63188475075463052E-60, \
            1.23592861191216019E-61, \
            2.52100420237726743E-63, \
            4.7722246219998052E-65, \
            8.3700198919995783E-67, \
            1.35782434112020985E-68, \
            2.03368872715315416E-70, \
            2.8068384806953538E-72, \
            3.562567607062096E-74, \
            4.1494527492937706E-76, \
            4.4250079657663219E-78, \
            4.3100842612898497E-80, \
            3.8246610167617398E-82, \
            3.08354784259879275E-84, \
            2.25213982217062084E-86, \
            1.48551474064504312E-88, \
            8.8196354763726564E-91, \
            4.69641782212598507E-93, \
            2.23439382545477274E-95, \
             9.45878703822074032E-98, \
             3.546960831240672614E-100, \
             1.17253213003488723E-102, \
             3.399090555639915548E-105, \
             8.591907200623898045E-108, \
             1.8818913973535359647E-110, \
             3.5473586323062565237E-113, \
             5.7114822282836004745E-116, \
             7.78947378804446095611E-119, \
             8.91589869949126935148E-122, \
             8.476856358868403207418E-125, \
             6.617326935494900345408E-128, \
             4.1862163574157095190077E-131, \
             2.11438516898114207120093E-134, \
             8.38216350136786953641675E-138, \
             2.557202302197677884687798E-141, \
             5.8667686421912043720461236E-145, \
             9.8498610300648438019885689E-149, \
             1.171383943342068942456857274E-152, \
             9.483963265567383663821702301E-157, \
             4.9770963811238028116653976343E-161, \
             1.59089852775099765481980638695E-165, \
             2.85630382911900292320607568044E-170, \
             2.58225071969148999265031459122E-175, \
             1.00735025005079740952983187255E-180, \
             1.34425250044381631821772983363E-186, \
             4.18296221403683473389726627221E-193, \
             1.45716530772618631594481663188E-200, \
             8.64059169046870867692891422354E-210 ] )

  elif ( n == 129 ):

    x = np.array ( [ \
           0.0111645041367687260935881187114E+00, \
           0.0588269115255121725669144777376E+00, \
           0.144582603939087375345544455104E+00, \
           0.268463250498790809142537571727E+00, \
           0.430489433028069665583513882755E+00, \
           0.630685596971157529700818698614E+00, \
           0.869081474989540465988995980646E+00, \
           1.14571237269034129786358037349E+00, \
           1.46061926689785560022252086358E+00, \
            1.81384886225287260620048305182E+00, \
            2.20545363849013952710373368048E+00, \
            2.63549189753739459262727316570E+00, \
            3.10402781353627480023526416641E+00, \
            3.61113148701933289479734007535E+00, \
            4.15687900382495881133416031205E+00, \
            4.74135249908325871733484826319E+00, \
            5.36464022650680264548807369539E+00, \
            6.02683663318167548105631862177E+00, \
            6.72804244004243132025609101021E+00, \
            7.46836472821534963467632383543E+00, \
            8.24791703142169723816558449856E+00, \
            9.06681943464370270026626900050E+00, \
            9.92519867926931734070041188408E+00, \
            10.8231882749469306495297612192E+00, \
            11.7609286183977310387181197615E+00, \
            12.7385671194512351722694605084E+00, \
            13.7562583345886271805335101149E+00, \
            14.8141641082989854857712290559E+00, \
            15.9124537225752979381236294324E+00, \
            17.0513040549004685335351914932E+00, \
            18.2308997450984136591429080617E+00, \
            19.4514333714519620150207362048E+00, \
            20.7131056365177555775299262985E+00, \
            22.0161255630988608706489924430E+00, \
            23.3607107008685190470514486749E+00, \
            24.7470873441735867407744490421E+00, \
            26.1754907615839641134296855243E+00, \
            27.6461654377949106206644801830E+00, \
            29.1593653285328756045576144321E+00, \
            30.7153541291626095441732915451E+00, \
            32.3144055577441922161871665693E+00, \
            33.9568036533435689847296719094E+00, \
            35.6428430904596160112634717165E+00, \
            37.3728295104950910213327545948E+00, \
            39.1470798712685466663878582421E+00, \
            40.9659228156399190364649448364E+00, \
            42.8296990604046437906422357564E+00, \
            44.7387618067004519884778950119E+00, \
            46.6934771732681867037686990052E+00, \
            48.6942246540138734219622380649E+00, \
            50.7413976014347803131042845818E+00, \
            52.8354037375983340937979164025E+00, \
            54.9766656945006500240481182310E+00, \
            57.1656215857823649284158070179E+00, \
            59.4027256119448606421881531943E+00, \
            61.6884487013914405461822377003E+00, \
            64.0232791898173852597210780437E+00, \
            66.4077235406921080587914699631E+00, \
            68.8423071098181639647332557636E+00, \
            71.3275749572182499453797757024E+00, \
            73.8640927098955268421782575110E+00, \
            76.4524474793379566181613942983E+00, \
            79.0932488379977030145472340597E+00, \
            81.7871298593763443093790704140E+00, \
            84.5347482267906647046323684124E+00, \
            87.3367874163878117910865422310E+00, \
            90.1939579605291478450570652459E+00, \
            93.1069987982766656767050611186E+00, \
            96.0766787204029972427806506124E+00, \
            99.1037979171157474398207782757E+00, \
            102.189189637550616978355114969E+00, \
            105.333721971058838012388514189E+00, \
            108.538299761408281119757506569E+00, \
            111.803866666252185387269569516E+00, \
            115.131407375615803792171876281E+00, \
            118.521950004733905726449958829E+00, \
            121.976568678369858697173472594E+00, \
            125.496386325793836628100280130E+00, \
            129.082577707933597477650969878E+00, \
            132.736372700883616552797038522E+00, \
            136.459059863023413416361147154E+00, \
            140.251990316520692590651584246E+00, \
            144.116581978059547282038191264E+00, \
            148.054324178334554730971189024E+00, \
            152.066782715303825347545842677E+00, \
            156.155605392537787829354492826E+00, \
            160.322528101405362530717313062E+00, \
            164.569381514511906899139962575E+00, \
            168.898098467996847713856358122E+00, \
            173.310722122324145053009369479E+00, \
            177.809415005439611927392788370E+00, \
            182.396469059102149766157602559E+00, \
            187.074316829415599837320402996E+00, \
            191.845543966839763114071401295E+00, \
            196.712903230183761859963922576E+00, \
            201.679330224475912387142876872E+00, \
            206.747961145685983577272619640E+00, \
            211.922152858007833039218477193E+00, \
            217.205505694330143211608701365E+00, \
             222.601889450939732907762241579E+00, \
             228.115473147766504188912042615E+00, \
             233.750759251359480867215068547E+00, \
             239.512623216994726852324857048E+00, \
             245.406359409276117119061170837E+00, \
             251.437734721509742305967783880E+00, \
             257.613051552607945102309836371E+00, \
             263.939222243647173894814944292E+00, \
             270.423857663083214051346532320E+00, \
             277.075373415313344577287378499E+00, \
             283.903118212107869887400929941E+00, \
             290.917530409009503510470042900E+00, \
             298.130330747241946479391511151E+00, \
             305.554762228622700877217556637E+00, \
             313.205892212538716296350101328E+00, \
             321.100997941634721519100026717E+00, \
             329.260065894410473958350680155E+00, \
             337.706449515634131989920236326E+00, \
             346.467752279350659621376501841E+00, \
             355.577039643063413893183224979E+00, \
             365.074545471124791778391196263E+00, \
             375.010148136708978052975802762E+00, \
             385.447095254054417308720464640E+00, \
             396.467858100744210106334636127E+00, \
             408.183851152492844798297769341E+00, \
             420.752744334742187498526476928E+00, \
             434.412341688764625555428748148E+00, \
             449.556338392256949417199002480E+00, \
             466.942750921706688536121321308E+00, \
             488.537715007400745716181291102E+00 ] )

    w = np.array ( [ \
           0.0283338232816188129433412493366E+00, \
           0.0628897352309939992519628028429E+00, \
           0.0907050560197830441591715791845E+00, \
           0.109292734964339745013347523543E+00, \
           0.117753891824430328742552706746E+00, \
           0.116712333575132760088854393741E+00, \
           0.1079821092277907522768638822E+00, \
           0.0940513886437790878162542877426E+00, \
           0.0775328171368385256641246588694E+00, \
            0.0607119801995722871258201910352E+00, \
            0.0452716214541695196710137988047E+00, \
            0.0322057586869443933590250840601E+00, \
            0.0218870093879284288723521418152E+00, \
            0.0142243242185532561642375502974E+00, \
            0.00884734285745239479408590424342E+00, \
            0.00526983370954167607842815218011E+00, \
            0.00300740619275414763773247784756E+00, \
            0.00164498171784021535901621253553E+00, \
            0.000862641473273809069700952476134E+00, \
            0.000433807488545501081264834235514E+00, \
            0.000209234988721404556453070968853E+00, \
            0.0000968044053231071525887634259114E+00, \
            0.0000429650601010182583779356860953E+00, \
            0.0000182943298240488545326843922155E+00, \
            7.47320473307839845584026474317E-06, \
            2.92876004890558731746712968433E-06, \
            1.10111937532188602299646730309E-06, \
            3.97133727854894494886436944708E-07, \
            1.37391737873739072964678053016E-07, \
            4.55898285044463980401770363171E-08, \
            1.45082031554226827387170770004E-08, \
            4.42736861865778798052557346184E-09, \
            1.29540549841465072618582643105E-09, \
            3.63353401896969889688016611161E-10, \
            9.76889957112077658988662065766E-11, \
            2.51697359198850123687093430919E-11, \
            6.2136427115425329244941688694E-12, \
            1.46947065273427272155102255087E-12, \
            3.3283536396381226771786168693E-13, \
            7.21860543546415622515782097245E-14, \
            1.49874700296546634758941598894E-14, \
            2.97813865190408297766537928957E-15, \
            5.66223500996744709699260363288E-16, \
            1.02976110977345161229212606736E-16, \
            1.79087076765055918801501255712E-17, \
            2.97741214327584722879794953728E-18, \
            4.73066849378813640521244315218E-19, \
            7.18076704552391091114386577815E-20, \
            1.0409591754013912471892470954E-20, \
            1.44063705945958837668569771815E-21, \
            1.9027009013059586477368991424E-22, \
            2.3972421860336028068385342016E-23, \
            2.880065029076382866335001882E-24, \
            3.2980570110683255202892323E-25, \
            3.59822818119059018987046195E-26, \
            3.7384843519427824153681456E-27, \
            3.6971969670644497346136084E-28, \
            3.478607942989822329014257E-29, \
            3.112229078360896126467536E-30, \
            2.64630166366922810478446E-31, \
            2.13731385180863223984415E-32, \
            1.63873356712820982018691E-33, \
            1.1920639048111247727415E-34, \
            8.221888191494076473793E-36, \
            5.373327742595686629791E-37, \
            3.325235584661609413228E-38, \
            1.94717317556033610096E-39, \
            1.07813497736466418105E-40, \
            5.6402504582069233692E-42, \
            2.785716667292756732E-43, \
            1.2978694111929463222E-44, \
            5.699117216622829387E-46, \
            2.356556045713220169E-47, \
            9.167179452095711245E-49, \
            3.351643630271094859E-50, \
            1.15053967361148792E-51, \
            3.70428664291287775E-53, \
            1.117334474142203311E-54, \
            3.15377989811063792E-56, \
            8.319920981942047E-58, \
            2.04876111892933112E-59, \
            4.7028955186049464E-61, \
            1.00491633674668433E-62, \
            1.9959187047623038E-64, \
            3.6789923736675531E-66, \
            6.2831482675040959E-68, \
            9.925201342288209E-70, \
            1.4475221077412768E-71, \
            1.945364935931307E-73, \
            2.4042822695448614E-75, \
            2.7267496829701407E-77, \
            2.8313374255297656E-79, \
            2.6851895059223692E-81, \
            2.3199549783717045E-83, \
            1.821032672647817E-85, \
            1.29486019972133753E-87, \
            8.3146100960594316E-90, \
            4.8053665090563748E-92, \
            2.49071240066108676E-94, \
             1.15335704284873844E-96, \
             4.75169815023478164E-99, \
             1.733951399870136754E-101, \
             5.57731896834145892E-104, \
             1.573010564351007982E-106, \
             3.867845242632879313E-109, \
             8.239883435606238718E-112, \
             1.5104570697877326124E-114, \
             2.3645657754433596259E-117, \
             3.1349053289923477642E-120, \
             3.48739145376585928069E-123, \
             3.22170074744057989255E-126, \
             2.443048415722317309221E-129, \
             1.5008657805760609578501E-132, \
             7.3592251345721592465131E-136, \
             2.83121162238276011127992E-139, \
             8.3785828758598937096069E-143, \
             1.8637689328976254234922931E-146, \
             3.0323700940390393081087066E-150, \
             3.49260330326226204565809172E-154, \
             2.736761201290944128360070077E-158, \
             1.3888959774881077581342370711E-162, \
             4.28912860126508716947322409477E-167, \
             7.43133882324715291928018394696E-172, \
             6.47421443374096511679045401121E-177, \
             2.42953692988216878005255824922E-182, \
             3.11143287762562176520260181694E-188, \
             9.26127289624597363219192415542E-195, \
             3.07023341560782650495387872798E-202, \
             1.71530871887294016615286222244E-211 ] )
 
  else:

    print ( '' )
    print ( 'LAGUERRE_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 to 20, 31/32/33, 63/64/65, 127/128/129' )
    raise Exception ( 'LAGUERRE_SET(): Fatal error!' )

  return x, w

def laguerre_set_test ( ):

#*****************************************************************************80
#
## laguerre_set_test() tests laguerre_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'laguerre_set_test():' )
  print ( '  laguerre_set() sets a Laguerre rule.' )
  print ( '' )
  print ( '         I            X                  W' )

  for n in range ( 1, 11 ):

    x, w = laguerre_set ( n )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %8d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def legendre_dr_compute ( n ):

#*****************************************************************************80
#
## legendre_dr_compute(): Gauss-Legendre quadrature by Davis-Rabinowitz method.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt.
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
#    integer N, the order.
#    N must be greater than 0.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  x = np.zeros ( n )
  w = np.zeros ( n )

  if ( n < 1 ):
    print ( '' )
    print ( 'legendre_dr_compute(): Fatal error!' )
    print ( '  Illegal value of N = ', n )
    raise Exception ( 'legendre_dr_compute(): Fatal error!' )

  e1 = n * ( n + 1 )

  m = ( ( n + 1 ) // 2 )

  for i in range ( 1, m + 1 ):

    mp1mi = m + 1 - i

    t = float ( 4 * i - 1 ) * np.pi / float ( 4 * n + 2 )

    x0 = np.cos ( t ) \
      * ( 1.0 - ( 1.0 - 1.0 / float ( n ) ) / float ( 8 * n * n ) )

    pkm1 = 1.0
    pk = x0

    for k in range ( 2, n + 1 ):
      pkp1 = 2.0 * x0 * pk - pkm1 - ( x0 * pk - pkm1 ) / float ( k )
      pkm1 = pk
      pk = pkp1

    d1 = float ( n ) * ( pkm1 - x0 * pk )

    dpn = d1 / ( 1.0 - x0 * x0 )

    d2pn = ( 2.0 * x0 * dpn - e1 * pk ) / ( 1.0 - x0 * x0 )

    d3pn = ( 4.0 * x0 * d2pn + ( 2.0 - e1 ) * dpn ) / ( 1.0 - x0 * x0 )

    d4pn = ( 6.0 * x0 * d3pn + ( 6.0 - e1 ) * d2pn ) / ( 1.0 - x0 * x0 )

    u = pk / dpn
    v = d2pn / dpn
#
#  Initial approximation H:
#
    h = - u * ( 1.0 + 0.5 * u * ( v + u * ( v * v - d3pn / ( 3.0 * dpn ) ) ) )
#
#  Refine H using one step of Newton's method:
#
    p = pk + h * ( dpn + 0.5 * h * ( d2pn + h / 3.0 \
      * ( d3pn + 0.25 * h * d4pn ) ) )

    dp = dpn + h * ( d2pn + 0.5 * h * ( d3pn + h * d4pn / 3.0 ) )

    h = h - p / dp

    xtemp = x0 + h

    x[mp1mi-1] = xtemp

    fx = d1 - h * e1 * ( pk + 0.5 * h * ( dpn + h / 3.0 \
      * ( d2pn + 0.25 * h * ( d3pn + 0.2 * h * d4pn ) ) ) )

    w[mp1mi-1] = 2.0 * ( 1.0 - xtemp * xtemp ) / fx / fx

  if ( ( n % 2 ) == 1 ):
    x[0] = 0.0
#
#  Shift the data up.
#
  nmove = ( ( n + 1 ) // 2 )
  ncopy = n - nmove

  for i in range ( 1, nmove + 1 ):
    iback = n + 1 - i
    x[iback-1] = x[iback-ncopy-1]
    w[iback-1] = w[iback-ncopy-1]
#
#  Reflect values for the negative abscissas.
#
  for i in range ( 1, n - nmove + 1 ):
    x[i-1] = - x[n-i]
    w[i-1] =   w[n-i]

  return x, w

def legendre_dr_compute_test ( ):

#*****************************************************************************80
#
## legendre_dr_compute_test() tests legendre_dr_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'legendre_dr_compute_test():' )
  print ( '  legendre_dr_compute() computes a Legendre quadrature rule' )
  print ( '  using the Davis-Rabinowitz algorithm.' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = legendre_dr_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def legendre_ek_compute ( n ):

#*****************************************************************************80
#
## legendre_ek_compute(): Gauss-Legendre, Elhay-Kautsky method.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 < x < +1 ) f(x) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#  Input:
#
#    integer N, the number of abscissas.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np
#
#  Define the zero-th moment.
#
  zemu = 2.0
#
#  Define the Jacobi matrix.
#
  bj = np.zeros ( n )
  for i in range ( 0, n ):
    ip1_r8 = float ( i + 1 )
    bj[i] = ip1_r8 * ip1_r8 / ( 4.0 * ip1_r8 * ip1_r8 - 1.0 )
    bj[i] = np.sqrt ( bj[i] )

  x = np.zeros ( n )

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return x, w

def legendre_ek_compute_test ( ):

#*****************************************************************************80
#
## legendre_ek_compute_test() tests legendre_ek_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'legendre_ek_compute_test():' )
  print ( '  legendre_ek_compute() computes' )
  print ( '  a Legendre quadrature rule' )
  print ( '  using the Elhay-Kautsky algorithm.' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = legendre_ek_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def legendre_integral ( expon ):

#*****************************************************************************80
#
## legendre_integral() evaluates a monomial Legendre integral.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x <= +1 ) x^n dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON, the exponent.
#
#  Output:
#
#    real EXACT, the value of the exact integral.
#
  if ( ( expon % 2 ) == 0 ):

    exact = 2.0 / float ( expon + 1 )
	
  else:

    exact = 0.0
	
  return exact

def legendre_integral_test ( ):

#*****************************************************************************80
#
## legendre_integral_test() tests legendre_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'legendre_integral_test():' )
  print ( '  legendre_integral() evaluates' )
  print ( '  Integral ( -1 < x < +1 ) x^n dx' )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = legendre_integral ( n )

    print ( '  %8d  %24.16g' % ( n, value ) )

  return

def legendre_set ( n ):

#*****************************************************************************80
#
## legendre_set() sets abscissas and weights for Gauss-Legendre quadrature.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    Quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    The quadrature rule will is exact for all polynomials through degree 2*N-1.
#
#    The abscissas are the zeroes of the Legendre polynomial P(N)(X).
#
#    Mathematica can compute the abscissas and weights of a Gauss-Legendre
#    rule of order N for the interval [A,B] with P digits of precision
#    by the commands:
#
#    Needs["NumericalDifferentialEquationAnalysis`"]
#    GaussianQuadratureWeights [ n, a, b, p ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2015
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
#    Vladimir Krylov,
#    Approximate Calculation of Integrals,
#    Dover, 2006,
#    ISBN: 0486445798,
#    LC: QA311.K713.
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
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
#    integer N, the order.
#    N must be between 1 and 33 or 63/64/65, 127/128/129, 
#    255/256/257.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
           0.000000000000000000000000000000 ] )

    w = np.array ( [ \
           2.000000000000000000000000000000 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
           -0.577350269189625764509148780502, \
           0.577350269189625764509148780502 ] )

    w = np.array ( [ \
           1.000000000000000000000000000000, \
           1.000000000000000000000000000000 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
           -0.774596669241483377035853079956, \
           0.000000000000000000000000000000, \
           0.774596669241483377035853079956 ] )

    w = np.array ( [ \
           0.555555555555555555555555555556, \
           0.888888888888888888888888888889, \
           0.555555555555555555555555555556 ] )

  elif ( n == 4 ):

    x = np.array ( [ \
           -0.861136311594052575223946488893, \
           -0.339981043584856264802665759103, \
           0.339981043584856264802665759103, \
           0.861136311594052575223946488893 ] )

    w = np.array ( [ \
           0.347854845137453857373063949222, \
           0.652145154862546142626936050778, \
           0.652145154862546142626936050778, \
           0.347854845137453857373063949222 ] )

  elif ( n == 5 ):

    x = np.array ( [ \
           -0.906179845938663992797626878299, \
           -0.538469310105683091036314420700, \
           0.000000000000000000000000000000, \
           0.538469310105683091036314420700, \
           0.906179845938663992797626878299 ] )

    w = np.array ( [ \
           0.236926885056189087514264040720, \
           0.478628670499366468041291514836, \
           0.568888888888888888888888888889, \
           0.478628670499366468041291514836, \
           0.236926885056189087514264040720 ] )

  elif ( n == 6 ):

    x = np.array ( [ \
           -0.932469514203152027812301554494, \
           -0.661209386466264513661399595020, \
           -0.238619186083196908630501721681, \
           0.238619186083196908630501721681, \
           0.661209386466264513661399595020, \
           0.932469514203152027812301554494 ] )

    w = np.array ( [ \
           0.171324492379170345040296142173, \
           0.360761573048138607569833513838, \
           0.467913934572691047389870343990, \
           0.467913934572691047389870343990, \
           0.360761573048138607569833513838, \
           0.171324492379170345040296142173 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
           -0.949107912342758524526189684048, \
           -0.741531185599394439863864773281, \
           -0.405845151377397166906606412077, \
           0.000000000000000000000000000000, \
           0.405845151377397166906606412077, \
           0.741531185599394439863864773281, \
           0.949107912342758524526189684048 ] )

    w = np.array ( [ \
           0.129484966168869693270611432679, \
           0.279705391489276667901467771424, \
           0.381830050505118944950369775489, \
           0.417959183673469387755102040816, \
           0.381830050505118944950369775489, \
           0.279705391489276667901467771424, \
           0.129484966168869693270611432679 ] )

  elif ( n == 8 ):

    x = np.array ( [ \
           -0.960289856497536231683560868569, \
           -0.796666477413626739591553936476, \
           -0.525532409916328985817739049189, \
           -0.183434642495649804939476142360, \
           0.183434642495649804939476142360, \
           0.525532409916328985817739049189, \
           0.796666477413626739591553936476, \
           0.960289856497536231683560868569 ] )

    w = np.array ( [ \
           0.101228536290376259152531354310, \
           0.222381034453374470544355994426, \
           0.313706645877887287337962201987, \
           0.362683783378361982965150449277, \
           0.362683783378361982965150449277, \
           0.313706645877887287337962201987, \
           0.222381034453374470544355994426, \
           0.101228536290376259152531354310 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
           -0.968160239507626089835576203, \
           -0.836031107326635794299429788, \
           -0.613371432700590397308702039, \
           -0.324253423403808929038538015, \
           0.000000000000000000000000000, \
           0.324253423403808929038538015, \
           0.613371432700590397308702039, \
           0.836031107326635794299429788, \
           0.968160239507626089835576203 ] )

    w = np.array ( [ \
           0.081274388361574411971892158111, \
           0.18064816069485740405847203124, \
           0.26061069640293546231874286942, \
           0.31234707704000284006863040658, \
           0.33023935500125976316452506929, \
           0.31234707704000284006863040658, \
           0.26061069640293546231874286942, \
           0.18064816069485740405847203124, \
           0.081274388361574411971892158111 ] )

  elif ( n == 10 ):

    x = np.array ( [ \
           -0.973906528517171720077964012, \
           -0.865063366688984510732096688, \
           -0.679409568299024406234327365, \
           -0.433395394129247190799265943, \
           -0.148874338981631210884826001, \
           0.148874338981631210884826001, \
           0.433395394129247190799265943, \
           0.679409568299024406234327365, \
           0.865063366688984510732096688, \
            0.973906528517171720077964012 ] )

    w = np.array ( [ \
           0.066671344308688137593568809893, \
           0.14945134915058059314577633966, \
           0.21908636251598204399553493423, \
           0.26926671930999635509122692157, \
           0.29552422471475287017389299465, \
           0.29552422471475287017389299465, \
           0.26926671930999635509122692157, \
           0.21908636251598204399553493423, \
           0.14945134915058059314577633966, \
            0.066671344308688137593568809893 ] )

  elif ( n == 11 ):

    x = np.array ( [ \
           -0.978228658146056992803938001, \
           -0.887062599768095299075157769, \
           -0.730152005574049324093416252, \
           -0.519096129206811815925725669, \
           -0.269543155952344972331531985, \
           0.000000000000000000000000000, \
           0.269543155952344972331531985, \
           0.519096129206811815925725669, \
           0.730152005574049324093416252, \
            0.887062599768095299075157769, \
            0.978228658146056992803938001 ] )

    w = np.array ( [ \
           0.055668567116173666482753720443, \
           0.12558036946490462463469429922, \
           0.18629021092773425142609764143, \
           0.23319376459199047991852370484, \
           0.26280454451024666218068886989, \
           0.27292508677790063071448352834, \
           0.26280454451024666218068886989, \
           0.23319376459199047991852370484, \
           0.18629021092773425142609764143, \
            0.12558036946490462463469429922, \
            0.055668567116173666482753720443 ] )

  elif ( n == 12 ):

    x = np.array ( [ \
           -0.981560634246719250690549090, \
           -0.904117256370474856678465866, \
           -0.769902674194304687036893833, \
           -0.587317954286617447296702419, \
           -0.367831498998180193752691537, \
           -0.125233408511468915472441369, \
           0.125233408511468915472441369, \
           0.367831498998180193752691537, \
           0.587317954286617447296702419, \
            0.769902674194304687036893833, \
            0.904117256370474856678465866, \
            0.981560634246719250690549090 ] )

    w = np.array ( [ \
           0.047175336386511827194615961485, \
           0.10693932599531843096025471819, \
           0.16007832854334622633465252954, \
           0.20316742672306592174906445581, \
           0.23349253653835480876084989892, \
           0.24914704581340278500056243604, \
           0.24914704581340278500056243604, \
           0.23349253653835480876084989892, \
           0.20316742672306592174906445581, \
            0.16007832854334622633465252954, \
            0.10693932599531843096025471819, \
            0.047175336386511827194615961485 ] )

  elif ( n == 13 ):

    x = np.array ( [ \
           -0.984183054718588149472829449, \
           -0.917598399222977965206547837, \
           -0.801578090733309912794206490, \
           -0.642349339440340220643984607, \
           -0.448492751036446852877912852, \
           -0.230458315955134794065528121, \
           0.000000000000000000000000000, \
           0.230458315955134794065528121, \
           0.448492751036446852877912852, \
            0.642349339440340220643984607, \
            0.80157809073330991279420649, \
            0.91759839922297796520654784, \
            0.98418305471858814947282945 ] )

    w = np.array ( [ \
           0.040484004765315879520021592201, \
           0.092121499837728447914421775954, \
           0.13887351021978723846360177687, \
           0.17814598076194573828004669200, \
           0.20781604753688850231252321931, \
           0.22628318026289723841209018604, \
           0.23255155323087391019458951527, \
           0.22628318026289723841209018604, \
           0.20781604753688850231252321931, \
            0.17814598076194573828004669200, \
            0.13887351021978723846360177687, \
            0.092121499837728447914421775954, \
            0.040484004765315879520021592201 ] )

  elif ( n == 14 ):

    x = np.array ( [ \
           -0.986283808696812338841597267, \
           -0.928434883663573517336391139, \
           -0.827201315069764993189794743, \
           -0.687292904811685470148019803, \
           -0.515248636358154091965290719, \
           -0.319112368927889760435671824, \
           -0.108054948707343662066244650, \
           0.108054948707343662066244650, \
           0.31911236892788976043567182, \
            0.51524863635815409196529072, \
            0.68729290481168547014801980, \
            0.82720131506976499318979474, \
            0.92843488366357351733639114, \
            0.98628380869681233884159727 ] )

    w = np.array ( [ \
           0.035119460331751863031832876138, \
           0.08015808715976020980563327706, \
           0.12151857068790318468941480907, \
           0.15720316715819353456960193862, \
           0.18553839747793781374171659013, \
           0.20519846372129560396592406566, \
           0.21526385346315779019587644332, \
           0.21526385346315779019587644332, \
           0.20519846372129560396592406566, \
            0.18553839747793781374171659013, \
            0.15720316715819353456960193862, \
            0.12151857068790318468941480907, \
            0.08015808715976020980563327706, \
            0.035119460331751863031832876138 ] )

  elif ( n == 15 ):

    x = np.array ( [ \
           -0.987992518020485428489565719, \
           -0.937273392400705904307758948, \
           -0.848206583410427216200648321, \
           -0.724417731360170047416186055, \
           -0.570972172608538847537226737, \
           -0.394151347077563369897207371, \
           -0.201194093997434522300628303, \
           0.00000000000000000000000000, \
           0.20119409399743452230062830, \
            0.39415134707756336989720737, \
            0.57097217260853884753722674, \
            0.72441773136017004741618605, \
            0.84820658341042721620064832, \
            0.93727339240070590430775895, \
            0.98799251802048542848956572 ] )

    w = np.array ( [ \
           0.030753241996117268354628393577, \
           0.070366047488108124709267416451, \
           0.107159220467171935011869546686, \
           0.13957067792615431444780479451, \
           0.16626920581699393355320086048, \
           0.18616100001556221102680056187, \
           0.19843148532711157645611832644, \
           0.20257824192556127288062019997, \
           0.19843148532711157645611832644, \
            0.18616100001556221102680056187, \
            0.16626920581699393355320086048, \
            0.13957067792615431444780479451, \
            0.107159220467171935011869546686, \
            0.070366047488108124709267416451, \
            0.030753241996117268354628393577 ] )

  elif ( n == 16 ):

    x = np.array ( [ \
           -0.989400934991649932596154173, \
           -0.944575023073232576077988416, \
           -0.865631202387831743880467898, \
           -0.755404408355003033895101195, \
           -0.617876244402643748446671764, \
           -0.458016777657227386342419443, \
           -0.281603550779258913230460501, \
           -0.09501250983763744018531934, \
           0.09501250983763744018531934, \
            0.28160355077925891323046050, \
            0.45801677765722738634241944, \
            0.61787624440264374844667176, \
            0.75540440835500303389510119, \
            0.86563120238783174388046790, \
            0.94457502307323257607798842, \
            0.98940093499164993259615417 ] )

    w = np.array ( [ \
           0.027152459411754094851780572456, \
           0.062253523938647892862843836994, \
           0.09515851168249278480992510760, \
           0.12462897125553387205247628219, \
           0.14959598881657673208150173055, \
           0.16915651939500253818931207903, \
           0.18260341504492358886676366797, \
           0.18945061045506849628539672321, \
           0.18945061045506849628539672321, \
            0.18260341504492358886676366797, \
            0.16915651939500253818931207903, \
            0.14959598881657673208150173055, \
            0.12462897125553387205247628219, \
            0.09515851168249278480992510760, \
            0.062253523938647892862843836994, \
            0.027152459411754094851780572456 ] )

  elif ( n == 17 ):

    x = np.array ( [ \
           -0.990575475314417335675434020, \
           -0.950675521768767761222716958, \
           -0.880239153726985902122955694, \
           -0.781514003896801406925230056, \
           -0.657671159216690765850302217, \
           -0.512690537086476967886246569, \
           -0.35123176345387631529718552, \
           -0.17848418149584785585067749, \
           0.00000000000000000000000000, \
            0.17848418149584785585067749, \
            0.35123176345387631529718552, \
            0.51269053708647696788624657, \
            0.65767115921669076585030222, \
            0.78151400389680140692523006, \
            0.88023915372698590212295569, \
            0.95067552176876776122271696, \
            0.99057547531441733567543402 ] )

    w = np.array ( [ \
           0.024148302868547931960110026288, \
           0.055459529373987201129440165359, \
           0.085036148317179180883535370191, \
           0.111883847193403971094788385626, \
           0.13513636846852547328631998170, \
           0.15404576107681028808143159480, \
           0.16800410215645004450997066379, \
           0.17656270536699264632527099011, \
           0.17944647035620652545826564426, \
            0.17656270536699264632527099011, \
            0.16800410215645004450997066379, \
            0.15404576107681028808143159480, \
            0.13513636846852547328631998170, \
            0.111883847193403971094788385626, \
            0.085036148317179180883535370191, \
            0.055459529373987201129440165359, \
            0.024148302868547931960110026288 ] )

  elif ( n == 18 ):

    x = np.array ( [ \
           -0.991565168420930946730016005, \
           -0.955823949571397755181195893, \
           -0.892602466497555739206060591, \
           -0.803704958972523115682417455, \
           -0.691687043060353207874891081, \
           -0.55977083107394753460787155, \
           -0.41175116146284264603593179, \
           -0.25188622569150550958897285, \
           -0.08477501304173530124226185, \
            0.08477501304173530124226185, \
            0.25188622569150550958897285, \
            0.41175116146284264603593179, \
            0.55977083107394753460787155, \
            0.69168704306035320787489108, \
            0.80370495897252311568241746, \
            0.89260246649755573920606059, \
            0.95582394957139775518119589, \
            0.99156516842093094673001600 ] )

    w = np.array ( [ \
           0.021616013526483310313342710266, \
           0.049714548894969796453334946203, \
           0.07642573025488905652912967762, \
           0.10094204410628716556281398492, \
           0.12255520671147846018451912680, \
           0.14064291467065065120473130375, \
           0.15468467512626524492541800384, \
           0.16427648374583272298605377647, \
           0.16914238296314359184065647013, \
            0.16914238296314359184065647013, \
            0.16427648374583272298605377647, \
            0.15468467512626524492541800384, \
            0.14064291467065065120473130375, \
            0.12255520671147846018451912680, \
            0.10094204410628716556281398492, \
            0.07642573025488905652912967762, \
            0.049714548894969796453334946203, \
            0.021616013526483310313342710266 ] )

  elif ( n == 19 ):

    x = np.array ( [ \
           -0.992406843843584403189017670, \
           -0.960208152134830030852778841, \
           -0.903155903614817901642660929, \
           -0.822714656537142824978922487, \
           -0.72096617733522937861709586, \
           -0.60054530466168102346963816, \
           -0.46457074137596094571726715, \
           -0.31656409996362983199011733, \
           -0.16035864564022537586809612, \
            0.00000000000000000000000000, \
            0.16035864564022537586809612, \
            0.31656409996362983199011733, \
            0.46457074137596094571726715, \
            0.60054530466168102346963816, \
            0.72096617733522937861709586, \
            0.82271465653714282497892249, \
            0.90315590361481790164266093, \
            0.96020815213483003085277884, \
            0.99240684384358440318901767 ] )

    w = np.array ( [ \
           0.019461788229726477036312041464, \
           0.044814226765699600332838157402, \
           0.069044542737641226580708258006, \
           0.091490021622449999464462094124, \
           0.111566645547333994716023901682, \
           0.12875396253933622767551578486, \
           0.14260670217360661177574610944, \
           0.15276604206585966677885540090, \
           0.15896884339395434764995643946, \
            0.16105444984878369597916362532, \
            0.15896884339395434764995643946, \
            0.15276604206585966677885540090, \
            0.14260670217360661177574610944, \
            0.12875396253933622767551578486, \
            0.111566645547333994716023901682, \
            0.091490021622449999464462094124, \
            0.069044542737641226580708258006, \
            0.044814226765699600332838157402, \
            0.019461788229726477036312041464 ] )

  elif ( n == 20 ):

    x = np.array ( [ \
           -0.993128599185094924786122388, \
           -0.963971927277913791267666131, \
           -0.912234428251325905867752441, \
           -0.83911697182221882339452906, \
           -0.74633190646015079261430507, \
           -0.63605368072651502545283670, \
           -0.51086700195082709800436405, \
           -0.37370608871541956067254818, \
           -0.22778585114164507808049620, \
            -0.07652652113349733375464041, \
            0.07652652113349733375464041, \
            0.22778585114164507808049620, \
            0.37370608871541956067254818, \
            0.51086700195082709800436405, \
            0.63605368072651502545283670, \
            0.74633190646015079261430507, \
            0.83911697182221882339452906, \
            0.91223442825132590586775244, \
            0.96397192727791379126766613, \
            0.99312859918509492478612239 ] )

    w = np.array ( [ \
           0.017614007139152118311861962352, \
           0.040601429800386941331039952275, \
           0.062672048334109063569506535187, \
           0.08327674157670474872475814322, \
           0.10193011981724043503675013548, \
           0.11819453196151841731237737771, \
           0.13168863844917662689849449975, \
           0.14209610931838205132929832507, \
           0.14917298647260374678782873700, \
            0.15275338713072585069808433195, \
            0.15275338713072585069808433195, \
            0.14917298647260374678782873700, \
            0.14209610931838205132929832507, \
            0.13168863844917662689849449975, \
            0.11819453196151841731237737771, \
            0.10193011981724043503675013548, \
            0.08327674157670474872475814322, \
            0.062672048334109063569506535187, \
            0.040601429800386941331039952275, \
            0.017614007139152118311861962352 ] )

  elif ( n == 21 ):

    x = np.array ( [ \
             -0.99375217062038950026024204, \
             -0.96722683856630629431662221, \
             -0.92009933415040082879018713, \
             -0.85336336458331728364725064, \
             -0.76843996347567790861587785, \
             -0.66713880419741231930596667, \
             -0.55161883588721980705901880, \
             -0.42434212020743878357366889, \
             -0.28802131680240109660079252, \
             -0.14556185416089509093703098, \
              0.00000000000000000000000000, \
             +0.14556185416089509093703098, \
             +0.28802131680240109660079252, \
             +0.42434212020743878357366889, \
             +0.55161883588721980705901880, \
             +0.66713880419741231930596667, \
             +0.76843996347567790861587785, \
             +0.85336336458331728364725064, \
             +0.92009933415040082879018713, \
             +0.96722683856630629431662221, \
             +0.99375217062038950026024204 ] )

    w = np.array ( [ \
              0.016017228257774333324224616858, \
              0.036953789770852493799950668299, \
              0.057134425426857208283635826472, \
              0.076100113628379302017051653300, \
              0.093444423456033861553289741114, \
              0.108797299167148377663474578070, \
              0.12183141605372853419536717713, \
              0.13226893863333746178105257450, \
              0.13988739479107315472213342387, \
              0.14452440398997005906382716655, \
              0.14608113364969042719198514768, \
              0.14452440398997005906382716655, \
              0.13988739479107315472213342387, \
              0.13226893863333746178105257450, \
              0.12183141605372853419536717713, \
              0.108797299167148377663474578070, \
              0.093444423456033861553289741114, \
              0.076100113628379302017051653300, \
              0.057134425426857208283635826472, \
              0.036953789770852493799950668299, \
              0.016017228257774333324224616858 ] )

  elif ( n == 22 ):

    x = np.array ( [ \
           -0.99429458548239929207303142, \
           -0.97006049783542872712395099, \
           -0.92695677218717400052069294, \
           -0.86581257772030013653642564, \
           -0.78781680597920816200427796, \
           -0.69448726318668278005068984, \
           -0.58764040350691159295887693, \
           -0.46935583798675702640633071, \
           -0.34193582089208422515814742, \
            -0.20786042668822128547884653, \
            -0.06973927331972222121384180, \
            0.06973927331972222121384180, \
            0.20786042668822128547884653, \
            0.34193582089208422515814742, \
            0.46935583798675702640633071, \
            0.58764040350691159295887693, \
            0.69448726318668278005068984, \
            0.78781680597920816200427796, \
            0.86581257772030013653642564, \
            0.92695677218717400052069294, \
            0.97006049783542872712395099, \
            0.99429458548239929207303142 ] )
 
    w = np.array ( [ \
           0.014627995298272200684991098047, \
           0.033774901584814154793302246866, \
           0.052293335152683285940312051273, \
           0.06979646842452048809496141893, \
           0.08594160621706772741444368137, \
           0.10041414444288096493207883783, \
           0.11293229608053921839340060742, \
           0.12325237681051242428556098615, \
           0.13117350478706237073296499253, \
            0.13654149834601517135257383123, \
            0.13925187285563199337541024834, \
            0.13925187285563199337541024834, \
            0.13654149834601517135257383123, \
            0.13117350478706237073296499253, \
            0.12325237681051242428556098615, \
            0.11293229608053921839340060742, \
            0.10041414444288096493207883783, \
            0.08594160621706772741444368137, \
            0.06979646842452048809496141893, \
            0.052293335152683285940312051273, \
            0.033774901584814154793302246866, \
            0.014627995298272200684991098047 ] )

  elif ( n == 23 ):

    x = np.array ( [ \
           -0.99476933499755212352392572, \
           -0.97254247121811523195602408, \
           -0.93297108682601610234919699, \
           -0.87675235827044166737815689, \
           -0.80488840161883989215111841, \
           -0.71866136313195019446162448, \
           -0.61960987576364615638509731, \
           -0.50950147784600754968979305, \
           -0.39030103803029083142148887, \
            -0.26413568097034493053386954, \
            -0.13325682429846611093174268, \
            0.00000000000000000000000000, \
            0.13325682429846611093174268, \
            0.26413568097034493053386954, \
            0.39030103803029083142148887, \
            0.50950147784600754968979305, \
            0.61960987576364615638509731, \
            0.71866136313195019446162448, \
            0.80488840161883989215111841, \
            0.87675235827044166737815689, \
            0.93297108682601610234919699, \
            0.97254247121811523195602408, \
            0.99476933499755212352392572 ] )

    w = np.array ( [ \
           0.013411859487141772081309493459, \
           0.030988005856979444310694219642, \
           0.048037671731084668571641071632, \
           0.064232421408525852127169615159, \
           0.079281411776718954922892524742, \
           0.092915766060035147477018617370, \
           0.104892091464541410074086185015, \
           0.11499664022241136494164351293, \
           0.12304908430672953046757840067, \
            0.12890572218808214997859533940, \
            0.13246203940469661737164246470, \
            0.13365457218610617535145711055, \
            0.13246203940469661737164246470, \
            0.12890572218808214997859533940, \
            0.12304908430672953046757840067, \
            0.11499664022241136494164351293, \
            0.104892091464541410074086185015, \
            0.092915766060035147477018617370, \
            0.079281411776718954922892524742, \
            0.064232421408525852127169615159, \
            0.048037671731084668571641071632, \
            0.030988005856979444310694219642, \
            0.013411859487141772081309493459 ] )

  elif ( n == 24 ):

    x = np.array ( [ \
           -0.99518721999702136017999741, \
           -0.97472855597130949819839199, \
           -0.93827455200273275852364900, \
           -0.88641552700440103421315434, \
           -0.82000198597390292195394987, \
           -0.74012419157855436424382810, \
           -0.64809365193697556925249579, \
           -0.54542147138883953565837562, \
           -0.43379350762604513848708423, \
            -0.31504267969616337438679329, \
            -0.19111886747361630915863982, \
            -0.06405689286260562608504308, \
            0.06405689286260562608504308, \
            0.19111886747361630915863982, \
            0.31504267969616337438679329, \
            0.43379350762604513848708423, \
            0.54542147138883953565837562, \
            0.64809365193697556925249579, \
            0.74012419157855436424382810, \
            0.82000198597390292195394987, \
            0.88641552700440103421315434, \
            0.93827455200273275852364900, \
            0.97472855597130949819839199, \
            0.99518721999702136017999741 ] )

    w = np.array ( [ \
           0.012341229799987199546805667070, \
           0.028531388628933663181307815952, \
           0.044277438817419806168602748211, \
           0.059298584915436780746367758500, \
           0.07334648141108030573403361525, \
           0.08619016153195327591718520298, \
           0.09761865210411388826988066446, \
           0.10744427011596563478257734245, \
           0.11550566805372560135334448391, \
            0.12167047292780339120446315348, \
            0.12583745634682829612137538251, \
            0.12793819534675215697405616522, \
            0.12793819534675215697405616522, \
            0.12583745634682829612137538251, \
            0.12167047292780339120446315348, \
            0.11550566805372560135334448391, \
            0.10744427011596563478257734245, \
            0.09761865210411388826988066446, \
            0.08619016153195327591718520298, \
            0.07334648141108030573403361525, \
            0.059298584915436780746367758500, \
            0.044277438817419806168602748211, \
            0.028531388628933663181307815952, \
            0.012341229799987199546805667070 ] )

  elif ( n == 25 ):

    x = np.array ( [ \
           -0.99555696979049809790878495, \
           -0.97666392145951751149831539, \
           -0.94297457122897433941401117, \
           -0.89499199787827536885104201, \
           -0.83344262876083400142102111, \
           -0.75925926303735763057728287, \
           -0.67356636847346836448512063, \
           -0.57766293024122296772368984, \
           -0.47300273144571496052218212, \
            -0.36117230580938783773582173, \
            -0.24386688372098843204519036, \
            -0.12286469261071039638735982, \
            0.00000000000000000000000000, \
            0.12286469261071039638735982, \
            0.24386688372098843204519036, \
            0.36117230580938783773582173, \
            0.47300273144571496052218212, \
            0.57766293024122296772368984, \
            0.67356636847346836448512063, \
            0.75925926303735763057728287, \
            0.83344262876083400142102111, \
            0.89499199787827536885104201, \
            0.94297457122897433941401117, \
            0.97666392145951751149831539, \
            0.99555696979049809790878495 ] )

    w = np.array ( [ \
           0.0113937985010262879479029641132, \
           0.026354986615032137261901815295, \
           0.040939156701306312655623487712, \
           0.054904695975835191925936891541, \
           0.068038333812356917207187185657, \
           0.080140700335001018013234959669, \
           0.091028261982963649811497220703, \
           0.100535949067050644202206890393, \
           0.108519624474263653116093957050, \
            0.11485825914571164833932554587, \
            0.11945576353578477222817812651, \
            0.12224244299031004168895951895, \
            0.12317605372671545120390287308, \
            0.12224244299031004168895951895, \
            0.11945576353578477222817812651, \
            0.11485825914571164833932554587, \
            0.108519624474263653116093957050, \
            0.100535949067050644202206890393, \
            0.091028261982963649811497220703, \
            0.080140700335001018013234959669, \
            0.068038333812356917207187185657, \
            0.054904695975835191925936891541, \
            0.040939156701306312655623487712, \
            0.026354986615032137261901815295, \
            0.0113937985010262879479029641132 ] )

  elif ( n == 26 ):

    x = np.array ( [ \
           -0.99588570114561692900321696, \
           -0.97838544595647099110058035, \
           -0.94715906666171425013591528, \
           -0.90263786198430707421766560, \
           -0.84544594278849801879750706, \
           -0.77638594882067885619296725, \
           -0.69642726041995726486381391, \
           -0.60669229301761806323197875, \
           -0.50844071482450571769570306, \
            -0.40305175512348630648107738, \
            -0.29200483948595689514283538, \
            -0.17685882035689018396905775, \
            -0.05923009342931320709371858, \
            0.05923009342931320709371858, \
            0.17685882035689018396905775, \
            0.29200483948595689514283538, \
            0.40305175512348630648107738, \
            0.50844071482450571769570306, \
            0.60669229301761806323197875, \
            0.69642726041995726486381391, \
            0.77638594882067885619296725, \
            0.84544594278849801879750706, \
            0.90263786198430707421766560, \
            0.94715906666171425013591528, \
            0.97838544595647099110058035, \
            0.99588570114561692900321696 ] )

    w = np.array ( [ \
           0.010551372617343007155651187685, \
           0.024417851092631908789615827520, \
           0.037962383294362763950303141249, \
           0.050975825297147811998319900724, \
           0.063274046329574835539453689907, \
           0.07468414976565974588707579610, \
           0.08504589431348523921044776508, \
           0.09421380035591414846366488307, \
           0.10205916109442542323841407025, \
            0.10847184052857659065657942673, \
            0.11336181654631966654944071844, \
            0.11666044348529658204466250754, \
            0.11832141527926227651637108570, \
            0.11832141527926227651637108570, \
            0.11666044348529658204466250754, \
            0.11336181654631966654944071844, \
            0.10847184052857659065657942673, \
            0.10205916109442542323841407025, \
            0.09421380035591414846366488307, \
            0.08504589431348523921044776508, \
            0.07468414976565974588707579610, \
            0.063274046329574835539453689907, \
            0.050975825297147811998319900724, \
            0.037962383294362763950303141249, \
            0.024417851092631908789615827520, \
            0.010551372617343007155651187685 ] )

  elif ( n == 27 ):

    x = np.array ( [ \
           -0.99617926288898856693888721, \
           -0.97992347596150122285587336, \
           -0.95090055781470500685190803, \
           -0.90948232067749110430064502, \
           -0.85620790801829449030273722, \
           -0.79177163907050822714439734, \
           -0.71701347373942369929481621, \
           -0.63290797194649514092773464, \
           -0.54055156457945689490030094, \
            -0.44114825175002688058597416, \
            -0.33599390363850889973031903, \
            -0.22645936543953685885723911, \
            -0.11397258560952996693289498, \
            0.00000000000000000000000000, \
            0.11397258560952996693289498, \
            0.22645936543953685885723911, \
            0.33599390363850889973031903, \
            0.44114825175002688058597416, \
            0.54055156457945689490030094, \
            0.63290797194649514092773464, \
            0.71701347373942369929481621, \
            0.79177163907050822714439734, \
            0.85620790801829449030273722, \
            0.90948232067749110430064502, \
            0.95090055781470500685190803, \
            0.97992347596150122285587336, \
            0.99617926288898856693888721 ] )

    w = np.array ( [ \
           0.0097989960512943602611500550912, \
           0.022686231596180623196034206447, \
           0.035297053757419711022578289305, \
           0.047449412520615062704096710114, \
           0.058983536859833599110300833720, \
           0.069748823766245592984322888357, \
           0.079604867773057771263074959010, \
           0.088423158543756950194322802854, \
           0.096088727370028507565652646558, \
            0.102501637817745798671247711533, \
            0.107578285788533187212162984427, \
            0.111252488356845192672163096043, \
            0.113476346108965148620369948092, \
            0.11422086737895698904504573690, \
            0.113476346108965148620369948092, \
            0.111252488356845192672163096043, \
            0.107578285788533187212162984427, \
            0.102501637817745798671247711533, \
            0.096088727370028507565652646558, \
            0.088423158543756950194322802854, \
            0.079604867773057771263074959010, \
            0.069748823766245592984322888357, \
            0.058983536859833599110300833720, \
            0.047449412520615062704096710114, \
            0.035297053757419711022578289305, \
            0.022686231596180623196034206447, \
            0.0097989960512943602611500550912 ] )

  elif ( n == 28 ):

    x = np.array ( [ \
           -0.99644249757395444995043639, \
           -0.98130316537087275369455995, \
           -0.95425928062893819725410184, \
           -0.91563302639213207386968942, \
           -0.86589252257439504894225457, \
           -0.80564137091717917144788596, \
           -0.73561087801363177202814451, \
           -0.65665109403886496121989818, \
           -0.56972047181140171930800328, \
            -0.47587422495511826103441185, \
            -0.37625151608907871022135721, \
            -0.27206162763517807767682636, \
            -0.16456928213338077128147178, \
            -0.05507928988403427042651653, \
            0.05507928988403427042651653, \
            0.16456928213338077128147178, \
            0.27206162763517807767682636, \
            0.37625151608907871022135721, \
            0.47587422495511826103441185, \
            0.56972047181140171930800328, \
            0.65665109403886496121989818, \
            0.73561087801363177202814451, \
            0.80564137091717917144788596, \
            0.86589252257439504894225457, \
            0.91563302639213207386968942, \
            0.95425928062893819725410184, \
            0.98130316537087275369455995, \
            0.99644249757395444995043639 ] )

    w = np.array ( [ \
           0.009124282593094517738816153923, \
           0.021132112592771259751500380993, \
           0.032901427782304379977630819171, \
           0.044272934759004227839587877653, \
           0.055107345675716745431482918227, \
           0.06527292396699959579339756678, \
           0.07464621423456877902393188717, \
           0.08311341722890121839039649824, \
           0.09057174439303284094218603134, \
            0.09693065799792991585048900610, \
            0.10211296757806076981421663851, \
            0.10605576592284641791041643700, \
            0.10871119225829413525357151930, \
            0.11004701301647519628237626560, \
            0.11004701301647519628237626560, \
            0.10871119225829413525357151930, \
            0.10605576592284641791041643700, \
            0.10211296757806076981421663851, \
            0.09693065799792991585048900610, \
            0.09057174439303284094218603134, \
            0.08311341722890121839039649824, \
            0.07464621423456877902393188717, \
            0.06527292396699959579339756678, \
            0.055107345675716745431482918227, \
            0.044272934759004227839587877653, \
            0.032901427782304379977630819171, \
            0.021132112592771259751500380993, \
            0.009124282593094517738816153923 ] )

  elif ( n == 29 ):

    x = np.array ( [ \
           -0.99667944226059658616319153, \
           -0.98254550526141317487092602, \
           -0.95728559577808772579820804, \
           -0.92118023295305878509375344, \
           -0.87463780492010279041779342, \
           -0.81818548761525244498957221, \
           -0.75246285173447713391261008, \
           -0.67821453760268651515618501, \
           -0.59628179713822782037958621, \
            -0.50759295512422764210262792, \
            -0.41315288817400866389070659, \
            -0.31403163786763993494819592, \
            -0.21135228616600107450637573, \
            -0.10627823013267923017098239, \
            0.00000000000000000000000000, \
            0.10627823013267923017098239, \
            0.21135228616600107450637573, \
            0.31403163786763993494819592, \
            0.41315288817400866389070659, \
            0.50759295512422764210262792, \
            0.59628179713822782037958621, \
            0.67821453760268651515618501, \
            0.75246285173447713391261008, \
            0.81818548761525244498957221, \
            0.87463780492010279041779342, \
            0.92118023295305878509375344, \
            0.95728559577808772579820804, \
            0.98254550526141317487092602, \
            0.99667944226059658616319153 ] )

    w = np.array ( [ \
           0.0085169038787464096542638133022, \
           0.019732085056122705983859801640, \
           0.030740492202093622644408525375, \
           0.041402062518682836104830010114, \
           0.051594826902497923912594381180, \
           0.061203090657079138542109848024, \
           0.070117933255051278569581486949, \
           0.078238327135763783828144888660, \
           0.085472257366172527545344849297, \
            0.091737757139258763347966411077, \
            0.096963834094408606301900074883, \
            0.101091273759914966121820546907, \
            0.104073310077729373913328471285, \
            0.105876155097320941406591327852, \
            0.10647938171831424424651112691, \
            0.105876155097320941406591327852, \
            0.104073310077729373913328471285, \
            0.101091273759914966121820546907, \
            0.096963834094408606301900074883, \
            0.091737757139258763347966411077, \
            0.085472257366172527545344849297, \
            0.078238327135763783828144888660, \
            0.070117933255051278569581486949, \
            0.061203090657079138542109848024, \
            0.051594826902497923912594381180, \
            0.041402062518682836104830010114, \
            0.030740492202093622644408525375, \
            0.019732085056122705983859801640, \
            0.0085169038787464096542638133022 ] )

  elif ( n == 30 ):

    x = np.array ( [ \
           -0.99689348407464954027163005, \
           -0.98366812327974720997003258, \
           -0.96002186496830751221687103, \
           -0.92620004742927432587932428, \
           -0.88256053579205268154311646, \
           -0.82956576238276839744289812, \
           -0.76777743210482619491797734, \
           -0.69785049479331579693229239, \
           -0.62052618298924286114047756, \
            -0.53662414814201989926416979, \
            -0.44703376953808917678060990, \
            -0.35270472553087811347103721, \
            -0.25463692616788984643980513, \
            -0.15386991360858354696379467, \
            -0.05147184255531769583302521, \
            0.05147184255531769583302521, \
            0.15386991360858354696379467, \
            0.25463692616788984643980513, \
            0.35270472553087811347103721, \
            0.44703376953808917678060990, \
            0.53662414814201989926416979, \
            0.62052618298924286114047756, \
            0.69785049479331579693229239, \
            0.76777743210482619491797734, \
            0.82956576238276839744289812, \
            0.88256053579205268154311646, \
            0.92620004742927432587932428, \
            0.96002186496830751221687103, \
            0.98366812327974720997003258, \
            0.99689348407464954027163005 ] )

    w = np.array ( [ \
           0.007968192496166605615465883475, \
           0.018466468311090959142302131912, \
           0.028784707883323369349719179611, \
           0.038799192569627049596801936446, \
           0.048402672830594052902938140423, \
           0.057493156217619066481721689402, \
           0.06597422988218049512812851512, \
           0.07375597473770520626824385002, \
           0.08075589522942021535469493846, \
            0.08689978720108297980238753072, \
            0.09212252223778612871763270709, \
            0.09636873717464425963946862635, \
            0.09959342058679526706278028210, \
            0.10176238974840550459642895217, \
            0.10285265289355884034128563671, \
            0.10285265289355884034128563671, \
            0.10176238974840550459642895217, \
            0.09959342058679526706278028210, \
            0.09636873717464425963946862635, \
            0.09212252223778612871763270709, \
            0.08689978720108297980238753072, \
            0.08075589522942021535469493846, \
            0.07375597473770520626824385002, \
            0.06597422988218049512812851512, \
            0.057493156217619066481721689402, \
            0.048402672830594052902938140423, \
            0.038799192569627049596801936446, \
            0.028784707883323369349719179611, \
            0.018466468311090959142302131912, \
            0.007968192496166605615465883475 ] )

  elif ( n == 31 ):

    x = np.array ( [ \
           -0.99708748181947707405562655, \
           -0.98468590966515248400246517, \
           -0.96250392509294966178905240, \
           -0.93075699789664816495694576, \
           -0.88976002994827104337419201, \
           -0.83992032014626734008690454, \
           -0.78173314841662494040636002, \
           -0.71577678458685328390597087, \
           -0.64270672292426034618441820, \
            -0.56324916140714926272094492, \
            -0.47819378204490248044059404, \
            -0.38838590160823294306135146, \
            -0.29471806998170161661790390, \
            -0.19812119933557062877241300, \
            -0.09955531215234152032517479, \
            0.00000000000000000000000000, \
            0.09955531215234152032517479, \
            0.19812119933557062877241300, \
            0.29471806998170161661790390, \
            0.38838590160823294306135146, \
            0.47819378204490248044059404, \
            0.56324916140714926272094492, \
            0.64270672292426034618441820, \
            0.71577678458685328390597087, \
            0.78173314841662494040636002, \
            0.83992032014626734008690454, \
            0.88976002994827104337419201, \
            0.93075699789664816495694576, \
            0.96250392509294966178905240, \
            0.98468590966515248400246517, \
            0.99708748181947707405562655 ] )

    w = np.array ( [ \
           0.0074708315792487758586968750322, \
           0.017318620790310582463157996087, \
           0.027009019184979421800608708092, \
           0.036432273912385464024392010468, \
           0.045493707527201102902315857895, \
           0.054103082424916853711666259087, \
           0.062174786561028426910343543687, \
           0.069628583235410366167756126255, \
           0.076390386598776616426357674901, \
            0.082392991761589263903823367432, \
            0.087576740608477876126198069695, \
            0.091890113893641478215362871607, \
            0.095290242912319512807204197488, \
            0.097743335386328725093474010979, \
            0.099225011226672307874875514429, \
            0.09972054479342645142753383373, \
            0.099225011226672307874875514429, \
            0.097743335386328725093474010979, \
            0.095290242912319512807204197488, \
            0.091890113893641478215362871607, \
            0.087576740608477876126198069695, \
            0.082392991761589263903823367432, \
            0.076390386598776616426357674901, \
            0.069628583235410366167756126255, \
            0.062174786561028426910343543687, \
            0.054103082424916853711666259087, \
            0.045493707527201102902315857895, \
            0.036432273912385464024392010468, \
            0.027009019184979421800608708092, \
            0.017318620790310582463157996087, \
            0.0074708315792487758586968750322 ] )

  elif ( n == 32 ):

    x = np.array ( [ \
           -0.99726386184948156354498113, \
           -0.98561151154526833540017504, \
           -0.96476225558750643077381193, \
           -0.93490607593773968917091913, \
           -0.89632115576605212396530724, \
           -0.84936761373256997013369300, \
           -0.79448379596794240696309730, \
           -0.73218211874028968038742667, \
           -0.66304426693021520097511517, \
            -0.58771575724076232904074548, \
            -0.50689990893222939002374747, \
            -0.42135127613063534536411944, \
            -0.33186860228212764977991681, \
            -0.23928736225213707454460321, \
            -0.14447196158279649348518637, \
            -0.04830766568773831623481257, \
            0.04830766568773831623481257, \
            0.14447196158279649348518637, \
            0.23928736225213707454460321, \
            0.33186860228212764977991681, \
            0.42135127613063534536411944, \
            0.50689990893222939002374747, \
            0.58771575724076232904074548, \
            0.66304426693021520097511517, \
            0.73218211874028968038742667, \
            0.79448379596794240696309730, \
            0.84936761373256997013369300, \
            0.89632115576605212396530724, \
            0.93490607593773968917091913, \
            0.96476225558750643077381193, \
            0.98561151154526833540017504, \
            0.99726386184948156354498113 ] )

    w = np.array ( [ \
           0.007018610009470096600407063739, \
           0.016274394730905670605170562206, \
           0.025392065309262059455752589789, \
           0.034273862913021433102687732252, \
           0.042835898022226680656878646606, \
           0.050998059262376176196163244690, \
           0.058684093478535547145283637300, \
           0.06582222277636184683765006371, \
           0.07234579410884850622539935648, \
            0.07819389578707030647174091883, \
            0.08331192422694675522219907460, \
            0.08765209300440381114277146275, \
            0.09117387869576388471286857711, \
            0.09384439908080456563918023767, \
            0.09563872007927485941908200220, \
            0.09654008851472780056676483006, \
            0.09654008851472780056676483006, \
            0.09563872007927485941908200220, \
            0.09384439908080456563918023767, \
            0.09117387869576388471286857711, \
            0.08765209300440381114277146275, \
            0.08331192422694675522219907460, \
            0.07819389578707030647174091883, \
            0.07234579410884850622539935648, \
            0.06582222277636184683765006371, \
            0.058684093478535547145283637300, \
            0.050998059262376176196163244690, \
            0.042835898022226680656878646606, \
            0.034273862913021433102687732252, \
            0.025392065309262059455752589789, \
            0.016274394730905670605170562206, \
            0.007018610009470096600407063739 ] )

  elif ( n == 33 ):

    x = np.array ( [ \
           -0.99742469424645521726616802, \
           -0.98645572623064248811037570, \
           -0.96682290968999276892837771, \
           -0.93869437261116835035583512, \
           -0.90231676774343358304053133, \
           -0.85800965267650406464306148, \
           -0.80616235627416658979620087, \
           -0.74723049644956215785905512, \
           -0.68173195996974278626821595, \
            -0.61024234583637902730728751, \
            -0.53338990478634764354889426, \
            -0.45185001727245069572599328, \
            -0.36633925774807334107022062, \
            -0.27760909715249702940324807, \
            -0.18643929882799157233579876, \
            -0.09363106585473338567074292, \
            0.00000000000000000000000000, \
            0.09363106585473338567074292, \
            0.18643929882799157233579876, \
            0.27760909715249702940324807, \
            0.36633925774807334107022062, \
            0.45185001727245069572599328, \
            0.53338990478634764354889426, \
            0.61024234583637902730728751, \
            0.68173195996974278626821595, \
            0.74723049644956215785905512, \
            0.80616235627416658979620087, \
            0.85800965267650406464306148, \
            0.90231676774343358304053133, \
            0.93869437261116835035583512, \
            0.96682290968999276892837771, \
            0.98645572623064248811037570, \
            0.99742469424645521726616802 ] )

    w = np.array ( [ \
           0.0066062278475873780586492352085, \
           0.015321701512934676127945768534, \
           0.023915548101749480350533257529, \
           0.032300358632328953281561447250, \
           0.040401541331669591563409790527, \
           0.048147742818711695670146880138, \
           0.055470846631663561284944495439, \
           0.062306482530317480031627725771, \
           0.068594572818656712805955073015, \
            0.074279854843954149342472175919, \
            0.079312364794886738363908384942, \
            0.083647876067038707613928014518, \
            0.087248287618844337607281670945, \
            0.090081958660638577239743705500, \
            0.092123986643316846213240977717, \
            0.093356426065596116160999126274, \
            0.09376844616020999656730454155, \
            0.093356426065596116160999126274, \
            0.092123986643316846213240977717, \
            0.090081958660638577239743705500, \
            0.087248287618844337607281670945, \
            0.083647876067038707613928014518, \
            0.079312364794886738363908384942, \
            0.074279854843954149342472175919, \
            0.068594572818656712805955073015, \
            0.062306482530317480031627725771, \
            0.055470846631663561284944495439, \
            0.048147742818711695670146880138, \
            0.040401541331669591563409790527, \
            0.032300358632328953281561447250, \
            0.023915548101749480350533257529, \
            0.015321701512934676127945768534, \
            0.0066062278475873780586492352085 ] )

  elif ( n == 63 ):

    x = np.array ( [ \
           -0.99928298402912378037893614, \
           -0.99622401277797010860219336, \
           -0.99072854689218946681089467, \
           -0.98280881059372723486251141, \
           -0.97248403469757002280196068, \
           -0.95977944975894192707035417, \
           -0.94472613404100980296637532, \
           -0.92736092062184320544703138, \
           -0.90772630277853155803695313, \
            -0.88587032850785342629029846, \
            -0.86184648236412371953961184, \
            -0.83571355431950284347180777, \
            -0.80753549577345676005146599, \
            -0.7773812629903723355633302, \
            -0.7453246483178474178293217, \
            -0.7114440995848458078514315, \
            -0.6758225281149860901311033, \
            -0.6385471058213653850003070, \
            -0.5997090518776252357390089, \
            -0.5594034094862850132676978, \
            -0.5177288132900332481244776, \
            -0.4747872479948043999222123, \
            -0.4306837987951116006620889, \
            -0.3855263942122478924776150, \
            -0.3394255419745844024688344, \
            -0.2924940585862514400361572, \
            -0.2448467932459533627484046, \
            -0.1966003467915066845576275, \
            -0.1478727863578719685698391, \
            -0.0987833564469452795297037, \
            -0.0494521871161596272342338, \
            0.0000000000000000000000000, \
            0.0494521871161596272342338, \
            0.0987833564469452795297037, \
            0.1478727863578719685698391, \
            0.1966003467915066845576275, \
            0.2448467932459533627484046, \
            0.2924940585862514400361572, \
            0.3394255419745844024688344, \
            0.3855263942122478924776150, \
            0.4306837987951116006620889, \
            0.4747872479948043999222123, \
            0.5177288132900332481244776, \
            0.5594034094862850132676978, \
            0.5997090518776252357390089, \
            0.6385471058213653850003070, \
            0.6758225281149860901311033, \
            0.7114440995848458078514315, \
            0.7453246483178474178293217, \
            0.7773812629903723355633302, \
            0.8075354957734567600514660, \
            0.8357135543195028434718078, \
            0.8618464823641237195396118, \
            0.8858703285078534262902985, \
            0.9077263027785315580369531, \
            0.9273609206218432054470314, \
            0.9447261340410098029663753, \
            0.9597794497589419270703542, \
            0.9724840346975700228019607, \
            0.9828088105937272348625114, \
            0.9907285468921894668108947, \
            0.9962240127779701086021934, \
            0.9992829840291237803789361 ] )

    w = np.array ( [ \
           0.0018398745955770841170924455540, \
           0.0042785083468637618660784110826, \
           0.0067102917659601362519069307298, \
           0.0091259686763266563540586454218, \
           0.011519376076880041750750606149, \
           0.013884612616115610824866086368, \
           0.016215878410338338882283672975, \
           0.018507464460161270409260545805, \
           0.020753761258039090775341953421, \
            0.022949271004889933148942319562, \
            0.025088620553344986618630138068, \
            0.027166574359097933225189839439, \
            0.029178047208280526945551502154, \
            0.031118116622219817508215988557, \
            0.032982034883779341765683179672, \
            0.034765240645355877697180504643, \
            0.036463370085457289630452409788, \
            0.038072267584349556763638324928, \
            0.039587995891544093984807928149, \
            0.041006845759666398635110037009, \
            0.042325345020815822982505485403, \
            0.043540267083027590798964315704, \
            0.044648638825941395370332669517, \
            0.045647747876292608685885992609, \
            0.046535149245383696510395418747, \
            0.047308671312268919080604988339, \
            0.047966421137995131411052756195, \
            0.048506789097883847864090099146, \
            0.048928452820511989944709361549, \
            0.049230380423747560785043116988, \
            0.049411833039918178967039646117, \
            0.04947236662393102088866936042, \
            0.049411833039918178967039646117, \
            0.049230380423747560785043116988, \
            0.048928452820511989944709361549, \
            0.048506789097883847864090099146, \
            0.047966421137995131411052756195, \
            0.047308671312268919080604988339, \
            0.046535149245383696510395418747, \
            0.045647747876292608685885992609, \
            0.044648638825941395370332669517, \
            0.043540267083027590798964315704, \
            0.042325345020815822982505485403, \
            0.041006845759666398635110037009, \
            0.039587995891544093984807928149, \
            0.038072267584349556763638324928, \
            0.036463370085457289630452409788, \
            0.034765240645355877697180504643, \
            0.032982034883779341765683179672, \
            0.031118116622219817508215988557, \
            0.029178047208280526945551502154, \
            0.027166574359097933225189839439, \
            0.025088620553344986618630138068, \
            0.022949271004889933148942319562, \
            0.020753761258039090775341953421, \
            0.018507464460161270409260545805, \
            0.016215878410338338882283672975, \
            0.013884612616115610824866086368, \
            0.011519376076880041750750606149, \
            0.0091259686763266563540586454218, \
            0.0067102917659601362519069307298, \
            0.0042785083468637618660784110826, \
            0.0018398745955770841170924455540 ] )
 
  elif ( n == 64 ):

    x = np.array ( [ \
           -0.99930504173577213945690562, \
           -0.99634011677195527934692450, \
           -0.99101337147674432073938238, \
           -0.98333625388462595693129930, \
           -0.97332682778991096374185351, \
           -0.96100879965205371891861412, \
           -0.94641137485840281606248149, \
           -0.92956917213193957582149015, \
           -0.91052213707850280575638067, \
            -0.88931544599511410585340404, \
            -0.86599939815409281976078339, \
            -0.8406292962525803627516915, \
            -0.8132653151227975597419233, \
            -0.7839723589433414076102205, \
            -0.7528199072605318966118638, \
            -0.7198818501716108268489402, \
            -0.6852363130542332425635584, \
            -0.6489654712546573398577612, \
            -0.6111553551723932502488530, \
            -0.5718956462026340342838781, \
            -0.5312794640198945456580139, \
            -0.4894031457070529574785263, \
            -0.4463660172534640879849477, \
            -0.4022701579639916036957668, \
            -0.3572201583376681159504426, \
            -0.3113228719902109561575127, \
            -0.2646871622087674163739642, \
            -0.2174236437400070841496487, \
            -0.1696444204239928180373136, \
            -0.1214628192961205544703765, \
            -0.0729931217877990394495429, \
            -0.0243502926634244325089558, \
            0.0243502926634244325089558, \
            0.0729931217877990394495429, \
            0.1214628192961205544703765, \
            0.1696444204239928180373136, \
            0.2174236437400070841496487, \
            0.2646871622087674163739642, \
            0.3113228719902109561575127, \
            0.3572201583376681159504426, \
            0.4022701579639916036957668, \
            0.4463660172534640879849477, \
            0.4894031457070529574785263, \
            0.5312794640198945456580139, \
            0.5718956462026340342838781, \
            0.6111553551723932502488530, \
            0.6489654712546573398577612, \
            0.6852363130542332425635584, \
            0.7198818501716108268489402, \
            0.7528199072605318966118638, \
            0.7839723589433414076102205, \
            0.8132653151227975597419233, \
            0.8406292962525803627516915, \
            0.8659993981540928197607834, \
            0.8893154459951141058534040, \
            0.9105221370785028057563807, \
            0.9295691721319395758214902, \
            0.9464113748584028160624815, \
            0.9610087996520537189186141, \
            0.9733268277899109637418535, \
            0.9833362538846259569312993, \
            0.9910133714767443207393824, \
            0.9963401167719552793469245, \
            0.9993050417357721394569056 ] )

    w = np.array ( [ \
           0.0017832807216964329472960791450, \
           0.0041470332605624676352875357286, \
           0.006504457968978362856117360400, \
           0.008846759826363947723030914660, \
           0.011168139460131128818590493019, \
           0.013463047896718642598060766686, \
           0.015726030476024719321965995298, \
           0.017951715775697343085045302001, \
           0.020134823153530209372340316729, \
            0.022270173808383254159298330384, \
            0.024352702568710873338177550409, \
            0.026377469715054658671691792625, \
            0.028339672614259483227511305200, \
            0.030234657072402478867974059820, \
            0.032057928354851553585467504348, \
            0.033805161837141609391565482111, \
            0.035472213256882383810693146715, \
            0.037055128540240046040415101810, \
            0.038550153178615629128962496947, \
            0.039953741132720341386656926128, \
            0.041262563242623528610156297474, \
            0.042473515123653589007339767909, \
            0.043583724529323453376827860974, \
            0.044590558163756563060134710031, \
            0.045491627927418144479770996971, \
            0.046284796581314417295953249232, \
            0.046968182816210017325326285755, \
            0.047540165714830308662282206944, \
            0.04799938859645830772812617987, \
            0.04834476223480295716976952716, \
            0.04857546744150342693479906678, \
            0.04869095700913972038336539073, \
            0.04869095700913972038336539073, \
            0.04857546744150342693479906678, \
            0.04834476223480295716976952716, \
            0.04799938859645830772812617987, \
            0.047540165714830308662282206944, \
            0.046968182816210017325326285755, \
            0.046284796581314417295953249232, \
            0.045491627927418144479770996971, \
            0.044590558163756563060134710031, \
            0.043583724529323453376827860974, \
            0.042473515123653589007339767909, \
            0.041262563242623528610156297474, \
            0.039953741132720341386656926128, \
            0.038550153178615629128962496947, \
            0.037055128540240046040415101810, \
            0.035472213256882383810693146715, \
            0.033805161837141609391565482111, \
            0.032057928354851553585467504348, \
            0.030234657072402478867974059820, \
            0.028339672614259483227511305200, \
            0.026377469715054658671691792625, \
            0.024352702568710873338177550409, \
            0.022270173808383254159298330384, \
            0.020134823153530209372340316729, \
            0.017951715775697343085045302001, \
            0.015726030476024719321965995298, \
            0.013463047896718642598060766686, \
            0.011168139460131128818590493019, \
            0.008846759826363947723030914660, \
            0.006504457968978362856117360400, \
            0.0041470332605624676352875357286, \
            0.0017832807216964329472960791450 ] )

  elif ( n == 65 ):

    x = np.array ( [ \
           -0.99932609707541287726569361, \
           -0.99645094806184916305579494, \
           -0.99128527617680166872182118, \
           -0.98383981218703494137763778, \
           -0.97413153983355116907496789, \
           -0.96218275471805523771198375, \
           -0.94802092816840750637376974, \
           -0.93167862822874933796567699, \
           -0.91319344054284626173654692, \
            -0.89260788050473893142328554, \
            -0.8699692949264070361941320, \
            -0.8453297528999302839424500, \
            -0.8187459259226514534339191, \
            -0.7902789574921218430473804, \
            -0.7599943224419997868739828, \
            -0.7279616763294246790119737, \
            -0.6942546952139916335526225, \
            -0.6589509061936251330409408, \
            -0.6221315090854002415825996, \
            -0.5838811896604873133271545, \
            -0.5442879248622271385455725, \
            -0.5034427804550068823410431, \
            -0.4614397015691450576978341, \
            -0.4183752966234090092641990, \
            -0.3743486151220660120087939, \
            -0.3294609198374864076452867, \
            -0.2838154539022487306176554, \
            -0.2375172033464168065707124, \
            -0.1906726556261427697749124, \
            -0.1433895546989751711312496, \
            -0.0957766532091975056522186, \
            -0.0479434623531718575225298, \
            0.0000000000000000000000000, \
            0.0479434623531718575225298, \
            0.0957766532091975056522186, \
            0.1433895546989751711312496, \
            0.1906726556261427697749124, \
            0.2375172033464168065707124, \
            0.2838154539022487306176554, \
            0.3294609198374864076452867, \
            0.3743486151220660120087939, \
            0.4183752966234090092641990, \
            0.4614397015691450576978341, \
            0.5034427804550068823410431, \
            0.5442879248622271385455725, \
            0.5838811896604873133271545, \
            0.6221315090854002415825996, \
            0.6589509061936251330409408, \
            0.6942546952139916335526225, \
            0.7279616763294246790119737, \
            0.7599943224419997868739828, \
            0.7902789574921218430473804, \
            0.8187459259226514534339191, \
            0.8453297528999302839424500, \
            0.8699692949264070361941320, \
            0.8926078805047389314232855, \
            0.9131934405428462617365469, \
            0.9316786282287493379656770, \
            0.9480209281684075063737697, \
            0.9621827547180552377119837, \
            0.9741315398335511690749679, \
            0.9838398121870349413776378, \
            0.9912852761768016687218212, \
            0.9964509480618491630557949, \
            0.9993260970754128772656936 ] )

    w = np.array ( [ \
           0.0017292582513002508983395851463, \
           0.0040215241720037363470786599528, \
           0.0063079425789717545501888719039, \
           0.0085801482668814598936358121592, \
           0.0108326787895979686215140551272, \
           0.013060311639994846336168342922, \
           0.015257912146448310349265388145, \
           0.017420421997670248495365759969, \
           0.019542865836750062826837429313, \
            0.021620361284934062841654274667, \
            0.023648129691287236698780978994, \
            0.025621506938037758214084978694, \
            0.027535954088450343942499722327, \
            0.029387067789310668062644859210, \
            0.031170590380189142464431845777, \
            0.032882419676368574984049638008, \
            0.034518618398549058625221276859, \
            0.036075423225565273932166270524, \
            0.037549253448257709809772223198, \
            0.038936719204051197616673806364, \
            0.040234629273005533815446337743, \
            0.041439998417240293022686299233, \
            0.042550054246755802719217150803, \
            0.043562243595800486532284821661, \
            0.044474238395082974427323504000, \
            0.045283941026300230657128240574, \
            0.045989489146651696963893390818, \
            0.046589259972233498302255136790, \
            0.047081874010454522246006808290, \
            0.047466198232885503152644458740, \
            0.047741348681240621559038972227, \
            0.047906692500495862031347289176, \
            0.04796184939446661812070762137, \
            0.047906692500495862031347289176, \
            0.047741348681240621559038972227, \
            0.047466198232885503152644458740, \
            0.047081874010454522246006808290, \
            0.046589259972233498302255136790, \
            0.045989489146651696963893390818, \
            0.045283941026300230657128240574, \
            0.044474238395082974427323504000, \
            0.043562243595800486532284821661, \
            0.042550054246755802719217150803, \
            0.041439998417240293022686299233, \
            0.040234629273005533815446337743, \
            0.038936719204051197616673806364, \
            0.037549253448257709809772223198, \
            0.036075423225565273932166270524, \
            0.034518618398549058625221276859, \
            0.032882419676368574984049638008, \
            0.031170590380189142464431845777, \
            0.029387067789310668062644859210, \
            0.027535954088450343942499722327, \
            0.025621506938037758214084978694, \
            0.023648129691287236698780978994, \
            0.021620361284934062841654274667, \
            0.019542865836750062826837429313, \
            0.017420421997670248495365759969, \
            0.015257912146448310349265388145, \
            0.013060311639994846336168342922, \
            0.0108326787895979686215140551272, \
            0.0085801482668814598936358121592, \
            0.0063079425789717545501888719039, \
            0.0040215241720037363470786599528, \
            0.0017292582513002508983395851463 ] )
    
  elif ( n == 127 ):
  
    x = np.array ( [ \
           -0.9998221304153061462673512, \
           -0.9990629343553118951383159, \
           -0.9976975661898046210744170, \
           -0.9957265513520272266354334, \
           -0.9931510492545171473611308, \
           -0.9899726145914841576077867, \
           -0.9861931740169316667104383, \
           -0.9818150208038141100334631, \
           -0.9768408123430703268174439, \
            -0.9712735681615291922889469, \
            -0.9651166679452921210908251, \
            -0.9583738494252387711491029, \
            -0.9510492060778803105479076, \
            -0.9431471846248148273454496, \
            -0.9346725823247379685736349, \
            -0.9256305440562338491274647, \
            -0.9160265591914658093130886, \
            -0.9058664582618213828024613, \
            -0.8951564094170837089690438, \
            -0.8839029146800265699452579, \
            -0.8721128059985607114196375, \
            -0.8597932410977408098120313, \
            -0.8469516991340975984533393, \
            -0.8335959761548995143795572, \
            -0.8197341803650786741551191, \
            -0.8053747272046802146665608, \
            -0.7905263342398137999454500, \
            -0.7751980158702023824449628, \
            -0.7593990778565366715566637, \
            -0.7431391116709545129205669, \
            -0.7264279886740726855356929, \
            -0.7092758541221045609994446, \
            -0.6916931210077006701564414, \
            -0.6736904637382504853466825, \
            -0.6552788116554826302767651, \
            -0.6364693424002972413476082, \
            -0.6172734751268582838576392, \
            -0.5977028635700652293844120, \
            -0.5777693889706125800032517, \
            -0.5574851528619322329218619, \
            -0.5368624697233975674581664, \
            -0.5159138595042493572772773, \
            -0.4946520400227821173949402, \
            -0.4730899192454052416450999, \
            -0.4512405874502662273318986, \
            -0.4291173092801933762625441, \
            -0.4067335156897825634086729, \
            -0.3841027957915169357790778, \
            -0.3612388886058697060709248, \
            -0.3381556747203985013760003, \
            -0.3148671678628949814860148, \
            -0.2913875063937056207945188, \
            -0.2677309447223886208883435, \
            -0.2439118446539178579707132, \
            -0.2199446666696875424545234, \
            -0.1958439611486108515042816, \
            -0.1716243595336421650083449, \
            -0.1473005654490856693893293, \
            -0.1228873457740829717260337, \
            -0.0983995216776989707510918, \
            -0.0738519596210485452734404, \
            -0.0492595623319266303153793, \
            -0.0246372597574209446148971, \
            0.0000000000000000000000000, \
            0.0246372597574209446148971, \
            0.0492595623319266303153793, \
            0.0738519596210485452734404, \
            0.0983995216776989707510918, \
            0.1228873457740829717260337, \
            0.1473005654490856693893293, \
            0.1716243595336421650083449, \
            0.1958439611486108515042816, \
            0.2199446666696875424545234, \
            0.2439118446539178579707132, \
            0.2677309447223886208883435, \
            0.2913875063937056207945188, \
            0.3148671678628949814860148, \
            0.3381556747203985013760003, \
            0.3612388886058697060709248, \
            0.3841027957915169357790778, \
            0.4067335156897825634086729, \
            0.4291173092801933762625441, \
            0.4512405874502662273318986, \
            0.4730899192454052416450999, \
            0.4946520400227821173949402, \
            0.5159138595042493572772773, \
            0.5368624697233975674581664, \
            0.5574851528619322329218619, \
            0.5777693889706125800032517, \
            0.5977028635700652293844120, \
            0.6172734751268582838576392, \
            0.6364693424002972413476082, \
            0.6552788116554826302767651, \
            0.6736904637382504853466825, \
            0.6916931210077006701564414, \
            0.7092758541221045609994446, \
            0.7264279886740726855356929, \
            0.7431391116709545129205669, \
            0.7593990778565366715566637, \
             0.7751980158702023824449628, \
             0.7905263342398137999454500, \
             0.8053747272046802146665608, \
             0.8197341803650786741551191, \
             0.8335959761548995143795572, \
             0.8469516991340975984533393, \
             0.8597932410977408098120313, \
             0.8721128059985607114196375, \
             0.8839029146800265699452579, \
             0.8951564094170837089690438, \
             0.9058664582618213828024613, \
             0.9160265591914658093130886, \
             0.9256305440562338491274647, \
             0.9346725823247379685736349, \
             0.9431471846248148273454496, \
             0.9510492060778803105479076, \
             0.9583738494252387711491029, \
             0.965116667945292121090825, \
             0.971273568161529192288947, \
             0.976840812343070326817444, \
             0.981815020803814110033463, \
             0.986193174016931666710438, \
             0.989972614591484157607787, \
             0.993151049254517147361131, \
             0.995726551352027226635433, \
             0.997697566189804621074417, \
             0.999062934355311895138316, \
             0.999822130415306146267351 ] )

    w = np.array ( [ \
           0.00045645726109586662791936519265, \
           0.00106227668695384869596523598532, \
           0.0016683488125171936761028862915, \
           0.0022734860707492547802810840776, \
           0.0028772587656289004082883197514, \
           0.0034792893810051465908910894100, \
           0.0040792095178254605327114733457, \
           0.0046766539777779034772638165663, \
           0.0052712596565634400891303815906, \
            0.0058626653903523901033648343751, \
            0.0064505120486899171845442463869, \
            0.0070344427036681608755685893033, \
            0.0076141028256526859356393930849, \
            0.0081891404887415730817235884719, \
            0.0087592065795403145773316804234, \
            0.0093239550065309714787536985834, \
            0.0098830429087554914716648010900, \
            0.0104361308631410052256731719977, \
            0.0109828830900689757887996573761, \
            0.011522967656921087154811609735, \
            0.012056056679400848183529562145, \
            0.012581826520465013101514365424, \
            0.013099957986718627426172681913, \
            0.013610136522139249906034237534, \
            0.014112052399003395774044161634, \
            0.014605400905893418351737288079, \
            0.015089882532666922992635733981, \
            0.015565203152273955098532590263, \
            0.016031074199309941802254151843, \
            0.016487212845194879399346060358, \
            0.016933342169871654545878815295, \
            0.017369191329918731922164721250, \
            0.017794495722974774231027912900, \
            0.018208997148375106468721469154, \
            0.018612443963902310429440419899, \
            0.019004591238555646611148901045, \
            0.019385200901246454628112623489, \
            0.019754041885329183081815217323, \
            0.020110890268880247225644623956, \
            0.020455529410639508279497065713, \
            0.020787750081531811812652137291, \
            0.021107350591688713643523847922, \
            0.021414136912893259295449693234, \
            0.021707922796373466052301324695, \
            0.021988529885872983756478409759, \
            0.022255787825930280235631416460, \
            0.022509534365300608085694429903, \
            0.022749615455457959852242553241, \
            0.022975885344117206754377437839, \
            0.023188206663719640249922582982, \
            0.023386450514828194170722043497, \
            0.023570496544381716050033676844, \
            0.023740233018760777777714726703, \
            0.023895556891620665983864481754, \
            0.024036373866450369675132086026, \
            0.024162598453819584716522917711, \
            0.024274154023278979833195063937, \
            0.024370972849882214952813561907, \
            0.024452996155301467956140198472, \
            0.024520174143511508275183033290, \
            0.024572466031020653286354137335, \
            0.024609840071630254092545634003, \
            0.024632273575707679066033370218, \
            0.02463975292396109441957941748, \
            0.024632273575707679066033370218, \
            0.024609840071630254092545634003, \
            0.024572466031020653286354137335, \
            0.024520174143511508275183033290, \
            0.024452996155301467956140198472, \
            0.024370972849882214952813561907, \
            0.024274154023278979833195063937, \
            0.024162598453819584716522917711, \
            0.024036373866450369675132086026, \
            0.023895556891620665983864481754, \
            0.023740233018760777777714726703, \
            0.023570496544381716050033676844, \
            0.023386450514828194170722043497, \
            0.023188206663719640249922582982, \
            0.022975885344117206754377437839, \
            0.022749615455457959852242553241, \
            0.022509534365300608085694429903, \
            0.022255787825930280235631416460, \
            0.021988529885872983756478409759, \
            0.021707922796373466052301324695, \
            0.021414136912893259295449693234, \
            0.021107350591688713643523847922, \
            0.020787750081531811812652137291, \
            0.020455529410639508279497065713, \
            0.020110890268880247225644623956, \
            0.019754041885329183081815217323, \
            0.019385200901246454628112623489, \
            0.019004591238555646611148901045, \
            0.018612443963902310429440419899, \
            0.018208997148375106468721469154, \
            0.017794495722974774231027912900, \
            0.017369191329918731922164721250, \
            0.016933342169871654545878815295, \
            0.016487212845194879399346060358, \
            0.016031074199309941802254151843, \
             0.015565203152273955098532590263, \
             0.015089882532666922992635733981, \
             0.014605400905893418351737288079, \
             0.014112052399003395774044161634, \
             0.013610136522139249906034237534, \
             0.013099957986718627426172681913, \
             0.012581826520465013101514365424, \
             0.012056056679400848183529562145, \
             0.011522967656921087154811609735, \
             0.0109828830900689757887996573761, \
             0.0104361308631410052256731719977, \
             0.0098830429087554914716648010900, \
             0.0093239550065309714787536985834, \
             0.0087592065795403145773316804234, \
             0.0081891404887415730817235884719, \
             0.0076141028256526859356393930849, \
             0.0070344427036681608755685893033, \
             0.0064505120486899171845442463869, \
             0.0058626653903523901033648343751, \
             0.0052712596565634400891303815906, \
             0.0046766539777779034772638165663, \
             0.0040792095178254605327114733457, \
             0.0034792893810051465908910894100, \
             0.0028772587656289004082883197514, \
             0.0022734860707492547802810840776, \
             0.0016683488125171936761028862915, \
             0.00106227668695384869596523598532, \
             0.00045645726109586662791936519265 ] )
 
  elif ( n == 128 ):

    x = np.array ( [ \
           -0.9998248879471319144736081, \
           -0.9990774599773758950119878, \
           -0.9977332486255140198821574, \
           -0.9957927585349811868641612, \
           -0.9932571129002129353034372, \
           -0.9901278184917343833379303, \
           -0.9864067427245862088712355, \
           -0.9820961084357185360247656, \
           -0.9771984914639073871653744, \
            -0.9717168187471365809043384, \
            -0.9656543664319652686458290, \
            -0.9590147578536999280989185, \
            -0.9518019613412643862177963, \
            -0.9440202878302201821211114, \
            -0.9356743882779163757831268, \
            -0.9267692508789478433346245, \
            -0.9173101980809605370364836, \
            -0.9073028834017568139214859, \
            -0.8967532880491581843864474, \
            -0.8856677173453972174082924, \
            -0.8740527969580317986954180, \
            -0.8619154689395484605906323, \
            -0.8492629875779689691636001, \
            -0.8361029150609068471168753, \
            -0.8224431169556438424645942, \
            -0.8082917575079136601196422, \
            -0.7936572947621932902433329, \
            -0.7785484755064119668504941, \
            -0.7629743300440947227797691, \
            -0.7469441667970619811698824, \
            -0.7304675667419088064717369, \
            -0.7135543776835874133438599, \
            -0.6962147083695143323850866, \
            -0.6784589224477192593677557, \
            -0.6602976322726460521059468, \
            -0.6417416925623075571535249, \
            -0.6228021939105849107615396, \
            -0.6034904561585486242035732, \
            -0.5838180216287630895500389, \
            -0.5637966482266180839144308, \
            -0.5434383024128103634441936, \
            -0.5227551520511754784539479, \
            -0.5017595591361444642896063, \
            -0.4804640724041720258582757, \
            -0.4588814198335521954490891, \
            -0.4370245010371041629370429, \
            -0.4149063795522750154922739, \
            -0.3925402750332674427356482, \
            -0.3699395553498590266165917, \
            -0.3471177285976355084261628, \
            -0.3240884350244133751832523, \
            -0.3008654388776772026671541, \
            -0.2774626201779044028062316, \
            -0.2538939664226943208556180, \
            -0.2301735642266599864109866, \
            -0.2063155909020792171540580, \
            -0.1823343059853371824103826, \
            -0.1582440427142249339974755, \
            -0.1340591994611877851175753, \
            -0.1097942311276437466729747, \
            -0.0854636405045154986364980, \
            -0.0610819696041395681037870, \
            -0.0366637909687334933302153, \
            -0.0122236989606157641980521, \
            0.0122236989606157641980521, \
            0.0366637909687334933302153, \
            0.0610819696041395681037870, \
            0.0854636405045154986364980, \
            0.1097942311276437466729747, \
            0.1340591994611877851175753, \
            0.1582440427142249339974755, \
            0.1823343059853371824103826, \
            0.2063155909020792171540580, \
            0.2301735642266599864109866, \
            0.2538939664226943208556180, \
            0.2774626201779044028062316, \
            0.3008654388776772026671541, \
            0.3240884350244133751832523, \
            0.3471177285976355084261628, \
            0.3699395553498590266165917, \
            0.3925402750332674427356482, \
            0.4149063795522750154922739, \
            0.4370245010371041629370429, \
            0.4588814198335521954490891, \
            0.4804640724041720258582757, \
            0.5017595591361444642896063, \
            0.5227551520511754784539479, \
            0.5434383024128103634441936, \
            0.5637966482266180839144308, \
            0.5838180216287630895500389, \
            0.6034904561585486242035732, \
            0.6228021939105849107615396, \
            0.6417416925623075571535249, \
            0.6602976322726460521059468, \
            0.6784589224477192593677557, \
            0.6962147083695143323850866, \
            0.7135543776835874133438599, \
            0.7304675667419088064717369, \
            0.7469441667970619811698824, \
             0.7629743300440947227797691, \
             0.7785484755064119668504941, \
             0.7936572947621932902433329, \
             0.8082917575079136601196422, \
             0.8224431169556438424645942, \
             0.8361029150609068471168753, \
             0.8492629875779689691636001, \
             0.8619154689395484605906323, \
             0.8740527969580317986954180, \
             0.8856677173453972174082924, \
             0.8967532880491581843864474, \
             0.9073028834017568139214859, \
             0.9173101980809605370364836, \
             0.926769250878947843334625, \
             0.935674388277916375783127, \
             0.944020287830220182121111, \
             0.951801961341264386217796, \
             0.959014757853699928098919, \
             0.965654366431965268645829, \
             0.971716818747136580904338, \
             0.977198491463907387165374, \
             0.982096108435718536024766, \
             0.986406742724586208871236, \
             0.990127818491734383337930, \
             0.993257112900212935303437, \
             0.995792758534981186864161, \
             0.997733248625514019882157, \
             0.999077459977375895011988, \
             0.999824887947131914473608 ] )

    w = np.array ( [ \
           0.00044938096029209037639429223999, \
           0.0010458126793403487793128516001, \
           0.0016425030186690295387908755948, \
           0.0022382884309626187436220542727, \
           0.0028327514714579910952857346468, \
           0.0034255260409102157743377846601, \
           0.0040162549837386423131943434863, \
           0.0046045842567029551182905419803, \
           0.0051901618326763302050707671348, \
            0.0057726375428656985893346176261, \
            0.006351663161707188787214327826, \
            0.006926892566898813563426670360, \
            0.007497981925634728687671962688, \
            0.008064589890486057972928598698, \
            0.008626377798616749704978843782, \
            0.009183009871660874334478743688, \
            0.009734153415006805863548266094, \
            0.010279479015832157133215340326, \
            0.010818660739503076247659646277, \
            0.011351376324080416693281668453, \
            0.011877307372740279575891106926, \
            0.012396139543950922968821728197, \
            0.012907562739267347220442834004, \
            0.013411271288616332314488951616, \
            0.013906964132951985244288007396, \
            0.014394345004166846176823892009, \
            0.014873122602147314252385498520, \
            0.015343010768865144085990853741, \
            0.015803728659399346858965631687, \
            0.016255000909785187051657456477, \
            0.016696557801589204589091507954, \
            0.017128135423111376830680987619, \
            0.017549475827117704648706925634, \
            0.017960327185008685940196927525, \
            0.018360443937331343221289290991, \
            0.018749586940544708650919548474, \
            0.019127523609950945486518531668, \
            0.019494028058706602823021918681, \
            0.019848881232830862219944413265, \
            0.020191871042130041180673158406, \
            0.020522792486960069432284967788, \
            0.020841447780751149113583948423, \
            0.021147646468221348537019535180, \
            0.021441205539208460137111853878, \
            0.021721949538052075375260957768, \
            0.021989710668460491434122106599, \
            0.022244328893799765104629133607, \
            0.022485652032744966871824603941, \
            0.022713535850236461309712635923, \
            0.022927844143686846920410987209, \
            0.023128448824387027879297902403, \
            0.023315229994062760122415671273, \
            0.023488076016535913153025273282, \
            0.023646883584447615143651392303, \
            0.023791557781003400638780709885, \
            0.023922012136703455672450408817, \
            0.024038168681024052637587316820, \
            0.024139957989019284997716653890, \
            0.024227319222815248120093308442, \
            0.024300200167971865323442606364, \
            0.024358557264690625853268520246, \
            0.024402355633849582093297989694, \
            0.02443156909785004505484856143, \
            0.02444618019626251821132585261, \
            0.02444618019626251821132585261, \
            0.02443156909785004505484856143, \
            0.024402355633849582093297989694, \
            0.024358557264690625853268520246, \
            0.024300200167971865323442606364, \
            0.024227319222815248120093308442, \
            0.024139957989019284997716653890, \
            0.024038168681024052637587316820, \
            0.023922012136703455672450408817, \
            0.023791557781003400638780709885, \
            0.023646883584447615143651392303, \
            0.023488076016535913153025273282, \
            0.023315229994062760122415671273, \
            0.023128448824387027879297902403, \
            0.022927844143686846920410987209, \
            0.022713535850236461309712635923, \
            0.022485652032744966871824603941, \
            0.022244328893799765104629133607, \
            0.021989710668460491434122106599, \
            0.021721949538052075375260957768, \
            0.021441205539208460137111853878, \
            0.021147646468221348537019535180, \
            0.020841447780751149113583948423, \
            0.020522792486960069432284967788, \
            0.020191871042130041180673158406, \
            0.019848881232830862219944413265, \
            0.019494028058706602823021918681, \
            0.019127523609950945486518531668, \
            0.018749586940544708650919548474, \
            0.018360443937331343221289290991, \
            0.017960327185008685940196927525, \
            0.017549475827117704648706925634, \
            0.017128135423111376830680987619, \
            0.016696557801589204589091507954, \
            0.016255000909785187051657456477, \
             0.015803728659399346858965631687, \
             0.015343010768865144085990853741, \
             0.014873122602147314252385498520, \
             0.014394345004166846176823892009, \
             0.013906964132951985244288007396, \
             0.013411271288616332314488951616, \
             0.012907562739267347220442834004, \
             0.012396139543950922968821728197, \
             0.011877307372740279575891106926, \
             0.011351376324080416693281668453, \
             0.010818660739503076247659646277, \
             0.010279479015832157133215340326, \
             0.009734153415006805863548266094, \
             0.009183009871660874334478743688, \
             0.008626377798616749704978843782, \
             0.008064589890486057972928598698, \
             0.007497981925634728687671962688, \
             0.006926892566898813563426670360, \
             0.006351663161707188787214327826, \
             0.0057726375428656985893346176261, \
             0.0051901618326763302050707671348, \
             0.0046045842567029551182905419803, \
             0.0040162549837386423131943434863, \
             0.0034255260409102157743377846601, \
             0.0028327514714579910952857346468, \
             0.0022382884309626187436220542727, \
             0.0016425030186690295387908755948, \
             0.0010458126793403487793128516001, \
             0.00044938096029209037639429223999 ] )

  elif ( n == 129 ):

    x = np.array ( [ \
           -0.9998275818477487191077441, \
           -0.9990916504696409986514389, \
           -0.9977681080525852721429460, \
           -0.9958574393142831982149111, \
           -0.9933607326210712814854011, \
           -0.9902794486488178389207689, \
           -0.9866153978313475022005761, \
           -0.9823707352517413115507418, \
           -0.9775479582993672474447814, \
            -0.9721499048427034297274163, \
            -0.9661797514202097197778763, \
            -0.9596410113101918904168119, \
            -0.9525375324342090471027732, \
            -0.9448734950776734726784764, \
            -0.9366534094216514605284616, \
            -0.9278821128840036204317296, \
            -0.9185647672698286252225115, \
            -0.9087068557320696331245539, \
            -0.8983141795436338850435985, \
            -0.8873928546826803665034968, \
            -0.8759493082329433892035217, \
            -0.8639902746011257878940216, \
            -0.8515227915535356930243826, \
            -0.8385541960742664442975407, \
            -0.8250921200473358809210133, \
            -0.8111444857653120742087717, \
            -0.7967195012670592680339606, \
            -0.7818256555073413245387500, \
            -0.7664717133611208816717785, \
            -0.7506667104654910227632368, \
            -0.7344199479022727047791516, \
            -0.7177409867244055767721220, \
            -0.7006396423293521790044710, \
            -0.6831259786828258512462248, \
            -0.6652103023962409818802202, \
            -0.6469031566613704719753373, \
            -0.6282153150457794374886895, \
            -0.6091577751526861909563306, \
            -0.5897417521489813916767844, \
            -0.5699786721652138894754096, \
            -0.5498801655714271702189358, \
            -0.5294580601328034000099406, \
            -0.5087243740491428186199463, \
            -0.4876913088822746111853066, \
            -0.4663712423755613514331869, \
            -0.4447767211697226217818454, \
            -0.4229204534192644388475065, \
            -0.4008153013138596117693121, \
            -0.3784742735090801012801265, \
            -0.3559105174709357969672656, \
            -0.3331373117387248575049982, \
            -0.3101680581107488341147318, \
            -0.2870162737574911929568755, \
            -0.2636955832669005409666949, \
            -0.2402197106264598167721148, \
            -0.2166024711467599103221439, \
            -0.1928577633313305998663880, \
            -0.1689995606975133227390302, \
            -0.1450419035531891084328306, \
            -0.1209988907342009817690539, \
            -0.0968846713073332753086909, \
            -0.0727134362437305599118207, \
            -0.0484994100676562986191764, \
            -0.0242568424855058415749954, \
            0.0000000000000000000000000, \
            0.0242568424855058415749954, \
            0.0484994100676562986191764, \
            0.0727134362437305599118207, \
            0.0968846713073332753086909, \
            0.1209988907342009817690539, \
            0.1450419035531891084328306, \
            0.1689995606975133227390302, \
            0.1928577633313305998663880, \
            0.2166024711467599103221439, \
            0.2402197106264598167721148, \
            0.2636955832669005409666949, \
            0.2870162737574911929568755, \
            0.3101680581107488341147318, \
            0.3331373117387248575049982, \
            0.3559105174709357969672656, \
            0.3784742735090801012801265, \
            0.4008153013138596117693121, \
            0.4229204534192644388475065, \
            0.4447767211697226217818454, \
            0.4663712423755613514331869, \
            0.4876913088822746111853066, \
            0.5087243740491428186199463, \
            0.5294580601328034000099406, \
            0.5498801655714271702189358, \
            0.5699786721652138894754096, \
            0.5897417521489813916767844, \
            0.6091577751526861909563306, \
            0.6282153150457794374886895, \
            0.6469031566613704719753373, \
            0.6652103023962409818802202, \
            0.6831259786828258512462248, \
            0.7006396423293521790044710, \
            0.7177409867244055767721220, \
            0.7344199479022727047791516, \
             0.7506667104654910227632368, \
             0.7664717133611208816717785, \
             0.7818256555073413245387500, \
             0.7967195012670592680339606, \
             0.8111444857653120742087717, \
             0.8250921200473358809210133, \
             0.8385541960742664442975407, \
             0.8515227915535356930243826, \
             0.8639902746011257878940216, \
             0.875949308232943389203522, \
             0.887392854682680366503497, \
             0.898314179543633885043599, \
             0.908706855732069633124554, \
             0.918564767269828625222511, \
             0.927882112884003620431730, \
             0.936653409421651460528462, \
             0.944873495077673472678476, \
             0.952537532434209047102773, \
             0.959641011310191890416812, \
             0.966179751420209719777876, \
             0.972149904842703429727416, \
             0.977547958299367247444781, \
             0.982370735251741311550742, \
             0.986615397831347502200576, \
             0.990279448648817838920769, \
             0.993360732621071281485401, \
             0.995857439314283198214911, \
             0.997768108052585272142946, \
             0.999091650469640998651439, \
             0.999827581847748719107744 ] )

    w = np.array ( [ \
           0.00044246794182939296923668005717, \
           0.00102972844619622394463273519315, \
           0.0016172530556785534682413679271, \
           0.0022039015180966937075786419741, \
           0.0027892681877797554940944677057, \
           0.0033729979506246246117755709288, \
           0.0039547444682113562172392974765, \
           0.0045341644298525434513226874954, \
           0.0051109164669246267289761565766, \
            0.0056846609912469045788016012203, \
            0.0062550602724461408889348709586, \
            0.0068217785893519121070498527769, \
            0.0073844824072454014447165055698, \
            0.0079428405646668029041114107832, \
            0.0084965244635723279730542832506, \
            0.0090452082602137316404219313819, \
            0.0095885690555104190787301294510, \
            0.0101262870842733548093160774580, \
            0.0106580459029055185304204093001, \
            0.0111835325753305049735380697538, \
            0.011702437856964778185746436834, \
            0.012214456376582979416221105914, \
            0.012719286815944623465099036330, \
            0.013216632087061724231482387345, \
            0.013706199506993971244060563234, \
            0.014187700970062900419317230938, \
            0.014660853117380060971041027493, \
            0.015125377503587024690403432771, \
            0.015581000760707523415881287558, \
            0.016027454759014214436403950465, \
            0.016464476764814667467169189640, \
            0.016891809595063204177526208819, \
            0.017309201768707240731293596444, \
            0.017716407654678809269702031810, \
            0.018113187616443980503999783812, \
            0.018499308153024985727791918518, \
            0.018874542036411948181617592169, \
            0.019238668445283284085199492202, \
            0.019591473094956024580283987216, \
            0.019932748363489542089706675388, \
            0.020262293413868438317104423081, \
            0.020579914312192665948185517085, \
            0.020885424141805311409990024684, \
            0.021178643113290860912881038703, \
            0.021459398670279205389981598196, \
            0.021727525590993110687305178710, \
            0.021982866085479386179554968899, \
            0.022225269888466526554736910919, \
            0.022454594347794176432066564511, \
            0.022670704508362374313093970958, \
            0.022873473191551169638592083492, \
            0.023062781070063872924670495006, \
            0.023238516738149892544490435771, \
            0.023400576777165831146714346635, \
            0.023548865816436258377269094263, \
            0.023683296589378342897341543485, \
            0.023803789984857314051325299744, \
            0.023910275093742530302367230296, \
            0.024002689250636756075547029720, \
            0.024080978070754089272959634041, \
            0.024145095481924836783843156014, \
            0.024195003751708503129818111597, \
            0.024230673509598936275508460625, \
            0.024252083764308562906498864071, \
            0.02425922191612154143202867472, \
            0.024252083764308562906498864071, \
            0.024230673509598936275508460625, \
            0.024195003751708503129818111597, \
            0.024145095481924836783843156014, \
            0.024080978070754089272959634041, \
            0.024002689250636756075547029720, \
            0.023910275093742530302367230296, \
            0.023803789984857314051325299744, \
            0.023683296589378342897341543485, \
            0.023548865816436258377269094263, \
            0.023400576777165831146714346635, \
            0.023238516738149892544490435771, \
            0.023062781070063872924670495006, \
            0.022873473191551169638592083492, \
            0.022670704508362374313093970958, \
            0.022454594347794176432066564511, \
            0.022225269888466526554736910919, \
            0.021982866085479386179554968899, \
            0.021727525590993110687305178710, \
            0.021459398670279205389981598196, \
            0.021178643113290860912881038703, \
            0.020885424141805311409990024684, \
            0.020579914312192665948185517085, \
            0.020262293413868438317104423081, \
            0.019932748363489542089706675388, \
            0.019591473094956024580283987216, \
            0.019238668445283284085199492202, \
            0.018874542036411948181617592169, \
            0.018499308153024985727791918518, \
            0.018113187616443980503999783812, \
            0.017716407654678809269702031810, \
            0.017309201768707240731293596444, \
            0.016891809595063204177526208819, \
            0.016464476764814667467169189640, \
             0.016027454759014214436403950465, \
             0.015581000760707523415881287558, \
             0.015125377503587024690403432771, \
             0.014660853117380060971041027493, \
             0.014187700970062900419317230938, \
             0.013706199506993971244060563234, \
             0.013216632087061724231482387345, \
             0.012719286815944623465099036330, \
             0.012214456376582979416221105914, \
             0.011702437856964778185746436834, \
             0.0111835325753305049735380697538, \
             0.0106580459029055185304204093001, \
             0.0101262870842733548093160774580, \
             0.0095885690555104190787301294510, \
             0.0090452082602137316404219313819, \
             0.0084965244635723279730542832506, \
             0.0079428405646668029041114107832, \
             0.0073844824072454014447165055698, \
             0.0068217785893519121070498527769, \
             0.0062550602724461408889348709586, \
             0.0056846609912469045788016012203, \
             0.0051109164669246267289761565766, \
             0.0045341644298525434513226874954, \
             0.0039547444682113562172392974765, \
             0.0033729979506246246117755709288, \
             0.0027892681877797554940944677057, \
             0.0022039015180966937075786419741, \
             0.0016172530556785534682413679271, \
             0.00102972844619622394463273519315, \
             0.00044246794182939296923668005717 ] )

  elif ( n == 255 ):

    x = np.array ( [ \
           -0.999955705317563751730191, \
           -0.999766621312000569367063, \
           -0.999426474680169959344386, \
           -0.998935241284654635142155, \
           -0.998292986136967889228248, \
           -0.997499804126615814044844, \
           -0.996555814435198617028738, \
           -0.995461159480026294089975, \
           -0.994216004616630164799381, \
            -0.992820538021989138984811, \
            -0.991274970630385567164523, \
            -0.989579536085920123498574, \
            -0.987734490699732356281248, \
            -0.985740113407419277752900, \
            -0.983596705724776358640192, \
            -0.981304591701017185126565, \
            -0.978864117869068155239121, \
            -0.976275653192735980815246, \
            -0.973539589010643617645393, \
            -0.970656338976880365477697, \
            -0.967626338998338798105523, \
            -0.964450047168726298761719, \
            -0.961127943699247839572910, \
            -0.957660530845962076295490, \
            -0.954048332833816317950921, \
            -0.950291895777368285733522, \
            -0.946391787598204251752103, \
            -0.942348597939064408301480, \
            -0.938162938074687317626793, \
            -0.933835440819386124349338, \
            -0.929366760431369935739045, \
            -0.924757572513824425220425, \
            -0.920008573912766315142721, \
            -0.915120482611686961035103, \
            -0.910094037623000801254172, \
            -0.904929998876314959753358, \
            -0.899629147103536800144342, \
            -0.894192283720836729335637, \
            -0.888620230707484040924981, \
            -0.882913830481574073645470, \
            -0.877073945772665439532627, \
            -0.871101459491346550796200, \
            -0.864997274595751144137121, \
            -0.858762313955042966785823, \
            -0.852397520209890250084237, \
            -0.845903855629951054143931, \
            -0.839282301968391021084600, \
            -0.832533860313455524647230, \
            -0.825659550937118650611534, \
            -0.818660413140831885432406, \
            -0.811537505098395829833580, \
            -0.804291903695978689734633, \
            -0.796924704369305728807154, \
            -0.789437020938044295117764, \
            -0.781829985437409458675147, \
            -0.774104747947015717207115, \
            -0.766262476417000644100858, \
            -0.758304356491446765092016, \
            -0.750231591329128358931528, \
            -0.742045401421610281838045, \
            -0.733747024408726316001889, \
            -0.725337714891464938687812, \
            -0.716818744242290800531501, \
            -0.708191400412930589382399, \
            -0.699456987739652339456557, \
            -0.690616826746067624571761, \
            -0.681672253943486448787259, \
            -0.672624621628855017806731, \
            -0.663475297680306939970658, \
            -0.654225665350358766508700, \
            -0.644877123056781136890077, \
            -0.635431084171177146547142, \
            -0.625888976805299900901619, \
            -0.616252243595141561442344, \
            -0.606522341482826526536576, \
            -0.596700741496341721653202, \
            -0.586788928527137300685706, \
            -0.576788401105631382036211, \
            -0.566700671174652760010815, \
            -0.556527263860855843833077, \
            -0.546269717244142383159817, \
            -0.535929582125124840335150, \
            -0.525508421790666565699453, \
            -0.515007811777534223035005, \
            -0.504429339634198197635551, \
            -0.493774604680816999489812, \
            -0.483045217767441948626854, \
            -0.472242801030478698742627, \
            -0.461368987647442418771401, \
            -0.450425421590043710043279, \
            -0.439413757375642589040685, \
            -0.428335659817108112494341, \
            -0.417192803771121462605751, \
            -0.405986873884960545511889, \
            -0.394719564341804385683361, \
            -0.383392578604595822734854, \
            -0.372007629158501235092510, \
            -0.360566437252006227074021, \
            -0.349070732636686422161576, \
             -0.337522253305692705554261, \
             -0.325922745230990453444769, \
             -0.314273962099392474845918, \
             -0.302577665047425574167140, \
             -0.290835622395070819082047, \
             -0.279049609378417768508970, \
             -0.267221407881273079721012, \
             -0.255352806165764071686080, \
             -0.243445598601977973686482, \
             -0.231501585396677734059116, \
             -0.219522572321135403508985, \
             -0.207510370438124240859625, \
             -0.195466795828110816293869, \
             -0.183393669314688508087976, \
             -0.171292816189293903533225, \
             -0.159166065935247723154292, \
             -0.147015251951161989456661, \
             -0.134842211273755257250625, \
             -0.122648784300117812092492, \
             -0.110436814509468826540991, \
             -0.098208148184447540736015, \
             -0.085964634131980604256000, \
             -0.073708123403767780288977, \
             -0.061440469016428270850728, \
             -0.049163525671349973093019, \
             -0.036879149474284021657652, \
             -0.024589197654727010541405, \
             -0.012295528285133320036860, \
             0.000000000000000000000000, \
             0.012295528285133320036860, \
             0.024589197654727010541405, \
             0.036879149474284021657652, \
             0.049163525671349973093019, \
             0.061440469016428270850728, \
             0.073708123403767780288977, \
             0.085964634131980604256000, \
             0.098208148184447540736015, \
             0.110436814509468826540991, \
             0.122648784300117812092492, \
             0.134842211273755257250625, \
             0.147015251951161989456661, \
             0.159166065935247723154292, \
             0.171292816189293903533225, \
             0.183393669314688508087976, \
             0.195466795828110816293869, \
             0.207510370438124240859625, \
             0.219522572321135403508985, \
             0.231501585396677734059116, \
             0.243445598601977973686482, \
             0.255352806165764071686080, \
             0.267221407881273079721012, \
             0.279049609378417768508970, \
             0.290835622395070819082047, \
             0.302577665047425574167140, \
             0.314273962099392474845918, \
             0.325922745230990453444769, \
             0.337522253305692705554261, \
             0.349070732636686422161576, \
             0.360566437252006227074021, \
             0.372007629158501235092510, \
             0.383392578604595822734854, \
             0.394719564341804385683361, \
             0.405986873884960545511889, \
             0.417192803771121462605751, \
             0.428335659817108112494341, \
             0.439413757375642589040685, \
             0.450425421590043710043279, \
             0.461368987647442418771401, \
             0.472242801030478698742627, \
             0.483045217767441948626854, \
             0.493774604680816999489812, \
             0.504429339634198197635551, \
             0.515007811777534223035005, \
             0.525508421790666565699453, \
             0.535929582125124840335150, \
             0.546269717244142383159817, \
             0.556527263860855843833077, \
             0.566700671174652760010815, \
             0.576788401105631382036211, \
             0.586788928527137300685706, \
             0.596700741496341721653202, \
             0.606522341482826526536576, \
             0.616252243595141561442344, \
             0.625888976805299900901619, \
             0.635431084171177146547142, \
             0.644877123056781136890077, \
             0.654225665350358766508700, \
             0.663475297680306939970658, \
             0.672624621628855017806731, \
             0.681672253943486448787259, \
             0.690616826746067624571761, \
             0.699456987739652339456557, \
             0.708191400412930589382399, \
             0.716818744242290800531501, \
             0.725337714891464938687812, \
             0.733747024408726316001889, \
             0.742045401421610281838045, \
             0.750231591329128358931528, \
             0.758304356491446765092016, \
             0.766262476417000644100858, \
             0.774104747947015717207115, \
             0.781829985437409458675147, \
             0.789437020938044295117764, \
             0.796924704369305728807154, \
             0.804291903695978689734633, \
             0.811537505098395829833580, \
             0.818660413140831885432406, \
             0.825659550937118650611534, \
             0.832533860313455524647230, \
             0.839282301968391021084600, \
             0.845903855629951054143931, \
             0.852397520209890250084237, \
             0.858762313955042966785823, \
             0.864997274595751144137121, \
             0.871101459491346550796200, \
             0.877073945772665439532627, \
             0.882913830481574073645470, \
             0.888620230707484040924981, \
             0.894192283720836729335637, \
             0.899629147103536800144342, \
             0.904929998876314959753358, \
             0.910094037623000801254172, \
             0.915120482611686961035103, \
             0.920008573912766315142721, \
             0.924757572513824425220425, \
             0.929366760431369935739045, \
             0.933835440819386124349338, \
             0.938162938074687317626793, \
             0.942348597939064408301480, \
             0.946391787598204251752103, \
             0.950291895777368285733522, \
             0.954048332833816317950921, \
             0.957660530845962076295490, \
             0.961127943699247839572910, \
             0.964450047168726298761719, \
             0.967626338998338798105523, \
             0.970656338976880365477697, \
             0.973539589010643617645393, \
             0.976275653192735980815246, \
             0.978864117869068155239121, \
             0.981304591701017185126565, \
             0.983596705724776358640192, \
             0.985740113407419277752900, \
             0.987734490699732356281248, \
             0.989579536085920123498574, \
             0.991274970630385567164523, \
             0.992820538021989138984811, \
             0.994216004616630164799381, \
             0.995461159480026294089975, \
             0.996555814435198617028738, \
             0.997499804126615814044844, \
             0.998292986136967889228248, \
             0.998935241284654635142155, \
             0.999426474680169959344386, \
             0.999766621312000569367063, \
             0.999955705317563751730191 ] )

    w = np.array ( [ \
           0.00011367361999142272115645954414, \
           0.00026459387119083065532790838855, \
           0.00041569762526823913616284210066, \
           0.00056675794564824918946626058353, \
           0.00071773647800611087798371518325, \
           0.00086860766611945667949717690640, \
           0.00101934797642732530281229369360, \
           0.0011699343729388079886897709773, \
           0.0013203439900221692090523602144, \
            0.0014705540427783843160097204304, \
            0.0016205417990415653896921100325, \
            0.0017702845706603213070421243905, \
            0.0019197597117132050055085980675, \
            0.0020689446195015801533643667413, \
            0.0022178167367540171700373764020, \
            0.0023663535543962867157201855305, \
            0.0025145326145997073931298921370, \
            0.0026623315139717112732749157331, \
            0.0028097279068204407457332299361, \
            0.0029566995084575002760043344138, \
            0.0031032240985191112621977893133, \
            0.0032492795242943133198690930777, \
            0.0033948437040533928255056951665, \
            0.0035398946303722552150296713510, \
            0.0036844103734499176530742235517, \
            0.0038283690844171626400743524999, \
            0.0039717489986349171988699773906, \
            0.0041145284389812475901826468094, \
            0.0042566858191260658425395494472, \
            0.0043981996467927779838546384780, \
            0.0045390485270061921259394035112, \
            0.0046792111653260640506279893190, \
            0.0048186663710656988918572043815, \
            0.0049573930604950563104281084148, \
            0.0050953702600278273039420404117, \
            0.0052325771093919661294970523234, \
            0.0053689928647831724787741258653, \
            0.0055045969020008281904902120813, \
            0.0056393687195659001929970994675, \
            0.0057732879418203275712033691864, \
            0.0059063343220074160130475409466, \
            0.0060384877453327676663371666884, \
            0.0061697282320052788060812561217, \
            0.0063000359402577418025981070425, \
            0.0064293911693465917826140832500, \
            0.0065577743625303421548456356354, \
            0.0066851661100262568757892743568, \
            0.0068115471519448109954345674817, \
            0.0069368983812014946719507501243, \
            0.0070612008464055194979848418291, \
            0.0071844357547249896530757997058, \
            0.0073065844747281040972736443146, \
            0.0074276285391999597581348419714, \
            0.0075475496479345294426435656724, \
            0.0076663296705013920315933272426, \
            0.0077839506489867963897419914623, \
            0.0079003948007086443529587296692, \
            0.0080156445209049821352946484008, \
            0.0081296823853955935356080649925, \
            0.0082424911532162924158504385939, \
            0.0083540537692255160718568405530, \
            0.0084643533666828253227353760036, \
            0.0085733732697989214067758505840, \
            0.0086810969962567940901133439612, \
            0.0087875082597036197689825483144, \
            0.0088925909722130327769834298578, \
            0.0089963292467173975949700110383, \
            0.0090987073994097142025303711406, \
            0.0091997099521147934060534414075, \
            0.0092993216346293436285393234867, \
            0.0093975273870306153500305317074, \
            0.0094943123619532541442165010292, \
            0.0095896619268340180657610209655, \
            0.0096835616661240200035669970076, \
            0.0097759973834681605268499842249, \
            0.0098669551038514217128483481814, \
            0.0099564210757116974565448593910, \
            0.0100443817730188408231888789497, \
            0.0101308238973196141129538950955, \
            0.0102157343797482324629939488415, \
            0.0102991003830021970147153502911, \
            0.0103809093032831189224876935085, \
            0.0104611487722022407735015844669, \
            0.0105398066586503673262517188088, \
            0.0106168710706319228563864391054, \
            0.0106923303570628578226139809571, \
            0.0107661731095321330311788312990, \
            0.0108383881640265149842990798832, \
            0.0109089646026184216450603134401, \
            0.0109778917551165634377595759712, \
            0.0110451592006791299277436662993, \
            0.0111107567693892782875426356195, \
            0.0111746745437926853557086684962, \
            0.0112369028603969308303734810332, \
            0.0112974323111324849102690558722, \
            0.0113562537447750795009464486204, \
            0.011413358268329247942299599697, \
            0.011468737248372824084374355981, \
            0.011522382312362197440930930031, \
             0.011574285349898127083439539046, \
             0.011624438513951922901227922331, \
             0.011672834222051808845465154244, \
             0.011719465157429288794653489478, \
             0.011764324270125341726399410909, \
             0.011807404778056278953532930501, \
             0.011848700168039102281222824051, \
             0.011888204196776208064673282076, \
             0.011925910891799288293359117699, \
             0.011961814552372285996633285380, \
             0.011995909750353268455989686823, \
             0.012028191331015087920350431142, \
             0.012058654413824705751531083631, \
             0.012087294393181062176578184854, \
             0.012114106939111380091025793650, \
             0.012139087997925797641334635250, \
             0.012162233792830230614908682534, \
             0.012183540824497371981177306326, \
             0.012203005871595742256331865516, \
             0.012220625991276710706457005806, \
             0.012236398519619413758040249691, \
             0.012250321072033503350218104906, \
             0.012262391543619664338660618398, \
             0.012272608109487846445745237751, \
             0.012280969225033162644659793962, \
             0.012287473626169412265336919908, \
             0.012292120329520193516690694701, \
             0.012294908632567576531532225710, \
             0.01229583811375831445681490730, \
             0.012294908632567576531532225710, \
             0.012292120329520193516690694701, \
             0.012287473626169412265336919908, \
             0.012280969225033162644659793962, \
             0.012272608109487846445745237751, \
             0.012262391543619664338660618398, \
             0.012250321072033503350218104906, \
             0.012236398519619413758040249691, \
             0.012220625991276710706457005806, \
             0.012203005871595742256331865516, \
             0.012183540824497371981177306326, \
             0.012162233792830230614908682534, \
             0.012139087997925797641334635250, \
             0.012114106939111380091025793650, \
             0.012087294393181062176578184854, \
             0.012058654413824705751531083631, \
             0.012028191331015087920350431142, \
             0.011995909750353268455989686823, \
             0.011961814552372285996633285380, \
             0.011925910891799288293359117699, \
             0.011888204196776208064673282076, \
             0.011848700168039102281222824051, \
             0.011807404778056278953532930501, \
             0.011764324270125341726399410909, \
             0.011719465157429288794653489478, \
             0.011672834222051808845465154244, \
             0.011624438513951922901227922331, \
             0.011574285349898127083439539046, \
             0.011522382312362197440930930031, \
             0.011468737248372824084374355981, \
             0.011413358268329247942299599697, \
             0.0113562537447750795009464486204, \
             0.0112974323111324849102690558722, \
             0.0112369028603969308303734810332, \
             0.0111746745437926853557086684962, \
             0.0111107567693892782875426356195, \
             0.0110451592006791299277436662993, \
             0.0109778917551165634377595759712, \
             0.0109089646026184216450603134401, \
             0.0108383881640265149842990798832, \
             0.0107661731095321330311788312990, \
             0.0106923303570628578226139809571, \
             0.0106168710706319228563864391054, \
             0.0105398066586503673262517188088, \
             0.0104611487722022407735015844669, \
             0.0103809093032831189224876935085, \
             0.0102991003830021970147153502911, \
             0.0102157343797482324629939488415, \
             0.0101308238973196141129538950955, \
             0.0100443817730188408231888789497, \
             0.0099564210757116974565448593910, \
             0.0098669551038514217128483481814, \
             0.0097759973834681605268499842249, \
             0.0096835616661240200035669970076, \
             0.0095896619268340180657610209655, \
             0.0094943123619532541442165010292, \
             0.0093975273870306153500305317074, \
             0.0092993216346293436285393234867, \
             0.0091997099521147934060534414075, \
             0.0090987073994097142025303711406, \
             0.0089963292467173975949700110383, \
             0.0088925909722130327769834298578, \
             0.0087875082597036197689825483144, \
             0.0086810969962567940901133439612, \
             0.0085733732697989214067758505840, \
             0.0084643533666828253227353760036, \
             0.0083540537692255160718568405530, \
             0.0082424911532162924158504385939, \
             0.0081296823853955935356080649925, \
             0.0080156445209049821352946484008, \
             0.0079003948007086443529587296692, \
             0.0077839506489867963897419914623, \
             0.0076663296705013920315933272426, \
             0.0075475496479345294426435656724, \
             0.0074276285391999597581348419714, \
             0.0073065844747281040972736443146, \
             0.0071844357547249896530757997058, \
             0.0070612008464055194979848418291, \
             0.0069368983812014946719507501243, \
             0.0068115471519448109954345674817, \
             0.0066851661100262568757892743568, \
             0.0065577743625303421548456356354, \
             0.0064293911693465917826140832500, \
             0.0063000359402577418025981070425, \
             0.0061697282320052788060812561217, \
             0.0060384877453327676663371666884, \
             0.0059063343220074160130475409466, \
             0.0057732879418203275712033691864, \
             0.0056393687195659001929970994675, \
             0.0055045969020008281904902120813, \
             0.0053689928647831724787741258653, \
             0.0052325771093919661294970523234, \
             0.0050953702600278273039420404117, \
             0.0049573930604950563104281084148, \
             0.0048186663710656988918572043815, \
             0.0046792111653260640506279893190, \
             0.0045390485270061921259394035112, \
             0.0043981996467927779838546384780, \
             0.0042566858191260658425395494472, \
             0.0041145284389812475901826468094, \
             0.0039717489986349171988699773906, \
             0.0038283690844171626400743524999, \
             0.0036844103734499176530742235517, \
             0.0035398946303722552150296713510, \
             0.0033948437040533928255056951665, \
             0.0032492795242943133198690930777, \
             0.0031032240985191112621977893133, \
             0.0029566995084575002760043344138, \
             0.0028097279068204407457332299361, \
             0.0026623315139717112732749157331, \
             0.0025145326145997073931298921370, \
             0.0023663535543962867157201855305, \
             0.0022178167367540171700373764020, \
             0.0020689446195015801533643667413, \
             0.0019197597117132050055085980675, \
             0.0017702845706603213070421243905, \
             0.0016205417990415653896921100325, \
             0.0014705540427783843160097204304, \
             0.0013203439900221692090523602144, \
             0.0011699343729388079886897709773, \
             0.00101934797642732530281229369360, \
             0.00086860766611945667949717690640, \
             0.00071773647800611087798371518325, \
             0.00056675794564824918946626058353, \
             0.00041569762526823913616284210066, \
             0.00026459387119083065532790838855, \
             0.00011367361999142272115645954414 ] )

  elif ( n == 256 ):

    x = np.array ( [ \
           -0.999956050018992230734801, \
           -0.999768437409263186104879, \
           -0.999430937466261408240854, \
           -0.998943525843408856555026, \
           -0.998306266473006444055500, \
           -0.997519252756720827563409, \
           -0.996582602023381540430504, \
           -0.995496454481096356592647, \
           -0.994260972922409664962878, \
            -0.992876342608822117143534, \
            -0.991342771207583086922189, \
            -0.989660488745065218319244, \
            -0.987829747564860608916488, \
            -0.985850822286125956479245, \
            -0.983724009760315496166686, \
            -0.981449629025464405769303, \
            -0.979028021257622038824238, \
            -0.976459549719234155621011, \
            -0.973744599704370405266079, \
            -0.970883578480743029320923, \
            -0.967876915228489454909004, \
            -0.964725060975706430932612, \
            -0.961428488530732144006407, \
            -0.957987692411178129365790, \
            -0.954403188769716241764448, \
            -0.950675515316628276363852, \
            -0.946805231239127481372052, \
            -0.942792917117462443183076, \
            -0.938639174837814804981926, \
            -0.934344627502003094292477, \
            -0.929909919334005641180246, \
            -0.925335715583316202872730, \
            -0.920622702425146495505047, \
            -0.915771586857490384526670, \
            -0.910783096595065011890907, \
            -0.905657979960144647082682, \
            -0.900397005770303544771620, \
            -0.895000963223084577441223, \
            -0.889470661777610888828677, \
            -0.883806931033158284859826, \
            -0.878010620604706543986435, \
            -0.872082599995488289130046, \
            -0.866023758466554519297515, \
            -0.859835004903376350696173, \
            -0.853517267679502965073036, \
            -0.847071494517296207187072, \
            -0.840498652345762713895068, \
            -0.833799727155504894348444, \
            -0.826975723850812514289093, \
            -0.820027666098917067403478, \
            -0.812956596176431543136410, \
            -0.805763574812998623257389, \
            -0.798449681032170758782543, \
            -0.791016011989545994546707, \
            -0.783463682808183820750670, \
            -0.775793826411325739132053, \
            -0.768007593352445635975891, \
            -0.760106151642655454941907, \
            -0.752090686575492059587530, \
            -0.743962400549111568455683, \
            -0.735722512885917834620373, \
            -0.727372259649652126586894, \
            -0.718912893459971448372640, \
            -0.710345683304543313394566, \
            -0.701671914348685159406084, \
            -0.692892887742576960105342, \
            -0.684009920426075953124877, \
            -0.675024344931162763855919, \
            -0.665937509182048559906408, \
            -0.656750776292973221887500, \
            -0.647465524363724862617016, \
            -0.638083146272911368668689, \
            -0.628605049469014975432210, \
            -0.619032655759261219430968, \
            -0.609367401096333939522311, \
            -0.599610735362968321730388, \
            -0.589764122154454300785786, \
            -0.579829038559082944921832, \
            -0.569806974936568759057668, \
            -0.559699434694481145136907, \
            -0.549507934062718557042427, \
            -0.539234001866059181127936, \
            -0.528879179294822261951476, \
            -0.518445019673674476221662, \
            -0.507933088228616036231925, \
            -0.497344961852181477119512, \
            -0.486682228866890350103621, \
            -0.475946488786983306390738, \
            -0.465139352078479313645570, \
            -0.454262439917589998774455, \
            -0.443317383947527357216926, \
            -0.432305826033741309953441, \
            -0.421229418017623824976812, \
            -0.410089821468716550006434, \
            -0.398888707435459127713463, \
            -0.387627756194515583637985, \
            -0.376308656998716390283056, \
            -0.364933107823654018533465, \
            -0.353502815112969989537790, \
             -0.342019493522371636480730, \
             -0.330484865662416976229187, \
             -0.318900661840106275631683, \
             -0.307268619799319076258610, \
             -0.295590484460135614563787, \
             -0.283868007657081741799766, \
             -0.272102947876336609505245, \
             -0.260297069991942541978561, \
             -0.248452145001056666833243, \
             -0.236569949758284018477508, \
             -0.224652266709131967147878, \
             -0.212700883622625957937040, \
             -0.200717593323126670068001, \
             -0.188704193421388826461504, \
             -0.176662486044901997403722, \
             -0.164594277567553849829285, \
             -0.152501378338656395374607, \
             -0.140385602411375885913025, \
             -0.128248767270607094742050, \
             -0.116092693560332804940735, \
             -0.103919204810509403639197, \
             -0.091730127163519552031146, \
             -0.079527289100232965903227, \
             -0.067312521165716400242290, \
             -0.055087655694633984104561, \
             -0.042854526536379098381242, \
             -0.030614968779979029366279, \
             -0.018370818478813665117926, \
             -0.006123912375189529501170, \
             0.006123912375189529501170, \
             0.018370818478813665117926, \
             0.030614968779979029366279, \
             0.042854526536379098381242, \
             0.055087655694633984104561, \
             0.067312521165716400242290, \
             0.079527289100232965903227, \
             0.091730127163519552031146, \
             0.103919204810509403639197, \
             0.116092693560332804940735, \
             0.128248767270607094742050, \
             0.140385602411375885913025, \
             0.152501378338656395374607, \
             0.164594277567553849829285, \
             0.176662486044901997403722, \
             0.188704193421388826461504, \
             0.200717593323126670068001, \
             0.212700883622625957937040, \
             0.224652266709131967147878, \
             0.236569949758284018477508, \
             0.248452145001056666833243, \
             0.260297069991942541978561, \
             0.272102947876336609505245, \
             0.283868007657081741799766, \
             0.295590484460135614563787, \
             0.307268619799319076258610, \
             0.318900661840106275631683, \
             0.330484865662416976229187, \
             0.342019493522371636480730, \
             0.353502815112969989537790, \
             0.364933107823654018533465, \
             0.376308656998716390283056, \
             0.387627756194515583637985, \
             0.398888707435459127713463, \
             0.410089821468716550006434, \
             0.421229418017623824976812, \
             0.432305826033741309953441, \
             0.443317383947527357216926, \
             0.454262439917589998774455, \
             0.465139352078479313645570, \
             0.475946488786983306390738, \
             0.486682228866890350103621, \
             0.497344961852181477119512, \
             0.507933088228616036231925, \
             0.518445019673674476221662, \
             0.528879179294822261951476, \
             0.539234001866059181127936, \
             0.549507934062718557042427, \
             0.559699434694481145136907, \
             0.569806974936568759057668, \
             0.579829038559082944921832, \
             0.589764122154454300785786, \
             0.599610735362968321730388, \
             0.609367401096333939522311, \
             0.619032655759261219430968, \
             0.628605049469014975432210, \
             0.638083146272911368668689, \
             0.647465524363724862617016, \
             0.656750776292973221887500, \
             0.665937509182048559906408, \
             0.675024344931162763855919, \
             0.684009920426075953124877, \
             0.692892887742576960105342, \
             0.701671914348685159406084, \
             0.710345683304543313394566, \
             0.718912893459971448372640, \
             0.727372259649652126586894, \
             0.735722512885917834620373, \
             0.743962400549111568455683, \
             0.752090686575492059587530, \
             0.760106151642655454941907, \
             0.768007593352445635975891, \
             0.775793826411325739132053, \
             0.783463682808183820750670, \
             0.791016011989545994546707, \
             0.798449681032170758782543, \
             0.805763574812998623257389, \
             0.812956596176431543136410, \
             0.820027666098917067403478, \
             0.826975723850812514289093, \
             0.833799727155504894348444, \
             0.840498652345762713895068, \
             0.847071494517296207187072, \
             0.853517267679502965073036, \
             0.859835004903376350696173, \
             0.866023758466554519297515, \
             0.872082599995488289130046, \
             0.878010620604706543986435, \
             0.883806931033158284859826, \
             0.889470661777610888828677, \
             0.895000963223084577441223, \
             0.900397005770303544771620, \
             0.905657979960144647082682, \
             0.910783096595065011890907, \
             0.915771586857490384526670, \
             0.920622702425146495505047, \
             0.925335715583316202872730, \
             0.929909919334005641180246, \
             0.934344627502003094292477, \
             0.938639174837814804981926, \
             0.942792917117462443183076, \
             0.946805231239127481372052, \
             0.950675515316628276363852, \
             0.954403188769716241764448, \
             0.957987692411178129365790, \
             0.961428488530732144006407, \
             0.964725060975706430932612, \
             0.967876915228489454909004, \
             0.970883578480743029320923, \
             0.973744599704370405266079, \
             0.976459549719234155621011, \
             0.979028021257622038824238, \
             0.981449629025464405769303, \
             0.983724009760315496166686, \
             0.985850822286125956479245, \
             0.987829747564860608916488, \
             0.989660488745065218319244, \
             0.991342771207583086922189, \
             0.992876342608822117143534, \
             0.994260972922409664962878, \
             0.995496454481096356592647, \
             0.996582602023381540430504, \
             0.997519252756720827563409, \
             0.998306266473006444055500, \
             0.998943525843408856555026, \
             0.999430937466261408240854, \
             0.999768437409263186104879, \
             0.999956050018992230734801 ] )

    w = np.array ( [ \
           0.00011278901782227217551253887725, \
           0.00026253494429644590628745756250, \
           0.00041246325442617632843218583774, \
           0.00056234895403140980281523674759, \
           0.0007121541634733206669089891511, \
           0.0008618537014200890378140934163, \
           0.0010114243932084404526058128414, \
           0.0011608435575677247239705981135, \
           0.0013100886819025044578316804271, \
            0.0014591373333107332010883864996, \
            0.0016079671307493272424499395690, \
            0.0017565557363307299936069145295, \
            0.0019048808534997184044191411746, \
            0.0020529202279661431745487818492, \
            0.0022006516498399104996848834189, \
            0.0023480529563273120170064609087, \
            0.0024951020347037068508395354372, \
            0.0026417768254274905641208292516, \
            0.0027880553253277068805747610763, \
            0.0029339155908297166460123254142, \
            0.0030793357411993375832053528316, \
            0.0032242939617941981570107134269, \
            0.0033687685073155510120191062489, \
            0.0035127377050563073309710549844, \
            0.0036561799581425021693892413052, \
            0.0037990737487662579981170192082, \
            0.0039413976414088336277290349840, \
            0.0040831302860526684085997759212, \
            0.0042242504213815362723565049060, \
            0.0043647368779680566815684200621, \
            0.0045045685814478970686417923159, \
            0.0046437245556800603139790923525, \
            0.0047821839258926913729317340448, \
            0.0049199259218138656695587765655, \
            0.0050569298807868423875578160762, \
            0.0051931752508692809303287536296, \
            0.0053286415939159303170811114788, \
            0.0054633085886443102775705318566, \
            0.0055971560336829100775514452572, \
            0.005730163850601437177384417555, \
            0.005862312086922653060661598801, \
            0.005993580919115338221127696870, \
            0.006123950655567932542389081187, \
            0.006253401739542401272063645975, \
            0.006381914752107880570375164275, \
            0.006509470415053660267809899951, \
            0.006636049593781065044590038355, \
            0.006761633300173798780927861108, \
            0.006886202695446320346713323775, \
            0.007009739092969822621234436194, \
            0.007132223961075390071672422986, \
            0.007253638925833913783829137214, \
            0.007373965773812346437572440695, \
            0.007493186454805883358599761133, \
            0.007611283084545659461618719618, \
            0.007728237947381555631110194958, \
            0.007844033498939711866810316151, \
            0.007958652368754348353613161227, \
            0.008072077362873499500946974804, \
            0.008184291466438269935619761004, \
            0.008295277846235225425171412553, \
            0.008405019853221535756180301698, \
            0.008513501025022490693838354790, \
            0.008620705088401014305368838410, \
            0.008726615961698807140336632217, \
            0.008831217757248750025318272685, \
            0.008934494783758207548408417085, \
            0.009036431548662873680227775572, \
            0.009137012760450806402000472219, \
            0.009236223330956302687378716714, \
            0.009334048377623269712466014486, \
            0.009430473225737752747352764482, \
            0.009525483410629284811829685754, \
            0.009619064679840727857162164401, \
            0.009711202995266279964249670496, \
            0.009801884535257327825498800250, \
            0.009891095696695828602630683809, \
            0.009978823097034910124733949495, \
            0.010065053576306383309460978930, \
            0.010149774199094865654634066042, \
            0.010232972256478219656954857160, \
            0.010314635267934015068260713997, \
            0.010394750983211728997101725205, \
            0.010473307384170403003569566927, \
            0.010550292686581481517533575536, \
            0.010625695341896561133961681801, \
            0.010699504038979785603048200583, \
            0.010771707705804626636653631927, \
            0.010842295511114795995293477058, \
            0.010911256866049039700796847788, \
            0.010978581425729570637988203448, \
            0.011044259090813901263517571044, \
            0.011108280009009843630460815451, \
            0.011170634576553449462710881938, \
            0.011231313439649668572656802083, \
            0.011290307495875509508367594121, \
            0.011347607895545491941625714297, \
            0.011403206043039185964847059552, \
            0.011457093598090639152334392298, \
             0.011509262477039497958586392439, \
             0.011559704854043635772668656950, \
             0.011608413162253105722084706677, \
             0.011655380094945242121298939730, \
             0.011700598606620740288189823359, \
             0.011744061914060550305376732759, \
             0.011785763497343426181690117627, \
             0.011825697100823977771160737958, \
             0.011863856734071078731904572908, \
             0.011900236672766489754287204237, \
             0.011934831459563562255873201696, \
             0.011967635904905893729007282670, \
             0.011998645087805811934536710071, \
             0.012027854356582571161267533498, \
             0.012055259329560149814347085327, \
             0.012080855895724544655975183976, \
             0.012104640215340463097757829736, \
             0.012126608720527321034718492205, \
             0.012146758115794459815559837664, \
             0.012165085378535502061307291839, \
             0.012181587759481772174047585032, \
             0.012196262783114713518180974196, \
             0.012209108248037240407514094371, \
             0.012220122227303969191708737227, \
             0.012229303068710278904146266083, \
             0.012236649395040158109242574767, \
             0.012242160104272800769728083260, \
             0.012245834369747920142463857550, \
             0.01224767164028975590407032649, \
             0.01224767164028975590407032649, \
             0.012245834369747920142463857550, \
             0.012242160104272800769728083260, \
             0.012236649395040158109242574767, \
             0.012229303068710278904146266083, \
             0.012220122227303969191708737227, \
             0.012209108248037240407514094371, \
             0.012196262783114713518180974196, \
             0.012181587759481772174047585032, \
             0.012165085378535502061307291839, \
             0.012146758115794459815559837664, \
             0.012126608720527321034718492205, \
             0.012104640215340463097757829736, \
             0.012080855895724544655975183976, \
             0.012055259329560149814347085327, \
             0.012027854356582571161267533498, \
             0.011998645087805811934536710071, \
             0.011967635904905893729007282670, \
             0.011934831459563562255873201696, \
             0.011900236672766489754287204237, \
             0.011863856734071078731904572908, \
             0.011825697100823977771160737958, \
             0.011785763497343426181690117627, \
             0.011744061914060550305376732759, \
             0.011700598606620740288189823359, \
             0.011655380094945242121298939730, \
             0.011608413162253105722084706677, \
             0.011559704854043635772668656950, \
             0.011509262477039497958586392439, \
             0.011457093598090639152334392298, \
             0.011403206043039185964847059552, \
             0.011347607895545491941625714297, \
             0.011290307495875509508367594121, \
             0.011231313439649668572656802083, \
             0.011170634576553449462710881938, \
             0.011108280009009843630460815451, \
             0.011044259090813901263517571044, \
             0.010978581425729570637988203448, \
             0.010911256866049039700796847788, \
             0.010842295511114795995293477058, \
             0.010771707705804626636653631927, \
             0.010699504038979785603048200583, \
             0.010625695341896561133961681801, \
             0.010550292686581481517533575536, \
             0.010473307384170403003569566927, \
             0.010394750983211728997101725205, \
             0.010314635267934015068260713997, \
             0.010232972256478219656954857160, \
             0.010149774199094865654634066042, \
             0.010065053576306383309460978930, \
             0.009978823097034910124733949495, \
             0.009891095696695828602630683809, \
             0.009801884535257327825498800250, \
             0.009711202995266279964249670496, \
             0.009619064679840727857162164401, \
             0.009525483410629284811829685754, \
             0.009430473225737752747352764482, \
             0.009334048377623269712466014486, \
             0.009236223330956302687378716714, \
             0.009137012760450806402000472219, \
             0.009036431548662873680227775572, \
             0.008934494783758207548408417085, \
             0.008831217757248750025318272685, \
             0.008726615961698807140336632217, \
             0.008620705088401014305368838410, \
             0.008513501025022490693838354790, \
             0.008405019853221535756180301698, \
             0.008295277846235225425171412553, \
             0.008184291466438269935619761004, \
             0.008072077362873499500946974804, \
             0.007958652368754348353613161227, \
             0.007844033498939711866810316151, \
             0.007728237947381555631110194958, \
             0.007611283084545659461618719618, \
             0.007493186454805883358599761133, \
             0.007373965773812346437572440695, \
             0.007253638925833913783829137214, \
             0.007132223961075390071672422986, \
             0.007009739092969822621234436194, \
             0.006886202695446320346713323775, \
             0.006761633300173798780927861108, \
             0.006636049593781065044590038355, \
             0.006509470415053660267809899951, \
             0.006381914752107880570375164275, \
             0.006253401739542401272063645975, \
             0.006123950655567932542389081187, \
             0.005993580919115338221127696870, \
             0.005862312086922653060661598801, \
             0.005730163850601437177384417555, \
             0.0055971560336829100775514452572, \
             0.0054633085886443102775705318566, \
             0.0053286415939159303170811114788, \
             0.0051931752508692809303287536296, \
             0.0050569298807868423875578160762, \
             0.0049199259218138656695587765655, \
             0.0047821839258926913729317340448, \
             0.0046437245556800603139790923525, \
             0.0045045685814478970686417923159, \
             0.0043647368779680566815684200621, \
             0.0042242504213815362723565049060, \
             0.0040831302860526684085997759212, \
             0.0039413976414088336277290349840, \
             0.0037990737487662579981170192082, \
             0.0036561799581425021693892413052, \
             0.0035127377050563073309710549844, \
             0.0033687685073155510120191062489, \
             0.0032242939617941981570107134269, \
             0.0030793357411993375832053528316, \
             0.0029339155908297166460123254142, \
             0.0027880553253277068805747610763, \
             0.0026417768254274905641208292516, \
             0.0024951020347037068508395354372, \
             0.0023480529563273120170064609087, \
             0.0022006516498399104996848834189, \
             0.0020529202279661431745487818492, \
             0.0019048808534997184044191411746, \
             0.0017565557363307299936069145295, \
             0.0016079671307493272424499395690, \
             0.0014591373333107332010883864996, \
             0.0013100886819025044578316804271, \
             0.0011608435575677247239705981135, \
             0.0010114243932084404526058128414, \
             0.0008618537014200890378140934163, \
             0.0007121541634733206669089891511, \
             0.00056234895403140980281523674759, \
             0.00041246325442617632843218583774, \
             0.00026253494429644590628745756250, \
             0.00011278901782227217551253887725 ] )

  elif ( n == 257 ):

    x = np.array ( [ \
           -0.999956390712330402472857, \
           -0.999770232390338019056053, \
           -0.999435348366365078441838, \
           -0.998951714093223210129834, \
           -0.998319392445383847808766, \
           -0.997538475365520218731818, \
           -0.996609078365487004512326, \
           -0.995531339486830143483750, \
           -0.994305419008553630362377, \
            -0.992931499332908653172844, \
            -0.991409784923101705201254, \
            -0.989740502257507526030375, \
            -0.987923899788618253106809, \
            -0.985960247902290665366669, \
            -0.983849838875444644048531, \
            -0.981592986831381877693095, \
            -0.979190027692327124191591, \
            -0.976641319128992592610888, \
            -0.973947240507062326750976, \
            -0.971108192830542793021113, \
            -0.968124598681952354372943, \
            -0.964996902159337170373447, \
            -0.961725568810109767190665, \
            -0.958311085561711847074814, \
            -0.954753960649106318830855, \
            -0.951054723539105826691801, \
            -0.947213924851546682950881, \
            -0.943232136277318328151464, \
            -0.939109950493259404355123, \
            -0.934847981073932324370129, \
            -0.930446862400288909805510, \
            -0.925907249565240289235888, \
            -0.921229818276144817520964, \
            -0.916415264754228313295468, \
            -0.911464305630951423630955, \
            -0.906377677841339419411308, \
            -0.901156138514290206476301, \
            -0.895800464859876809085345, \
            -0.890311454053661045810287, \
            -0.884689923118035575018750, \
            -0.878936708800611938658765, \
            -0.873052667449672679799858, \
            -0.867038674886706051812473, \
            -0.860895626276042275514686, \
            -0.854624435991610735314055, \
            -0.848226037480837936478636, \
            -0.841701383125706473284556, \
            -0.835051444100995681967937, \
            -0.828277210229725073186687, \
            -0.821379689835822056081139, \
            -0.814359909594035880004229, \
            -0.807218914377120130552073, \
            -0.799957767100306523636066, \
            -0.792577548563093144962574, \
            -0.785079357288370682385816, \
            -0.777464309358910595129671, \
            -0.769733538251239556788216, \
            -0.761888194666924898264210, \
            -0.753929446361296162339238, \
            -0.745858477969628263337895, \
            -0.737676490830812123299244, \
            -0.729384702808539030149808, \
            -0.720984348110025333531072, \
            -0.712476677102304460118510, \
            -0.703862956126113592426171, \
            -0.695144467307402713168813, \
            -0.686322508366494071200553, \
            -0.677398392424920474813593, \
            -0.668373447809971163711735, \
            -0.659249017856974352220492, \
            -0.650026460709345873208532, \
            -0.640707149116433684724434, \
            -0.631292470229188329449219, \
            -0.621783825393689760680446, \
            -0.612182629942561267650033, \
            -0.602490312984301547488097, \
            -0.592708317190566281032495, \
            -0.582838098581430874902446, \
            -0.572881126308666332759406, \
            -0.562838882437060514424546, \
            -0.552712861723817332466074, \
            -0.542504571396066721967792, \
            -0.532215530926518500400434, \
            -0.521847271807293510797499, \
            -0.511401337321965712746629, \
            -0.500879282315849152005553, \
            -0.490282672964564000798817, \
            -0.479613086540916117008992, \
            -0.468872111180124821505728, \
            -0.458061345643433838720630, \
            -0.447182399080140586238810, \
            -0.436236890788079234603398, \
            -0.425226449972593188682213, \
            -0.414152715504032866791986, \
            -0.403017335673814873281489, \
            -0.391821967949078874408131, \
            -0.380568278725978696070941, \
            -0.369257943081644365255611, \
            -0.357892644524852014873858, \
             -0.346474074745438764010632, \
             -0.335003933362499872399782, \
             -0.323483927671405649204085, \
             -0.311915772389675771851948, \
             -0.300301189401748840754520, \
             -0.288641907502685160168097, \
             -0.276939662140840894253032, \
             -0.265196195159551900488370, \
             -0.253413254537865690008131, \
             -0.241592594130360106108882, \
             -0.229735973406087448117604, \
             -0.217845157186682897983880, \
             -0.205921915383676231351599, \
             -0.193968022735045913454182, \
             -0.181985258541054792946197, \
             -0.169975406399406713716337, \
             -0.157940253939763465806087, \
             -0.145881592557661591770148, \
             -0.133801217147868654144405, \
             -0.121700925837218653121859, \
             -0.109582519716966361063898, \
             -0.097447802574700412082119, \
             -0.085298580625855050603929, \
             -0.073136662244860502573600, \
             -0.060963857695971986730406, \
             -0.048781978863817431238958, \
             -0.036592838983704002816750, \
             -0.024398252371723591403953, \
             -0.012200034154697423345412, \
             0.000000000000000000000000, \
             0.012200034154697423345412, \
             0.024398252371723591403953, \
             0.036592838983704002816750, \
             0.048781978863817431238958, \
             0.060963857695971986730406, \
             0.073136662244860502573600, \
             0.085298580625855050603929, \
             0.097447802574700412082119, \
             0.109582519716966361063898, \
             0.121700925837218653121859, \
             0.133801217147868654144405, \
             0.145881592557661591770148, \
             0.157940253939763465806087, \
             0.169975406399406713716337, \
             0.181985258541054792946197, \
             0.193968022735045913454182, \
             0.205921915383676231351599, \
             0.217845157186682897983880, \
             0.229735973406087448117604, \
             0.241592594130360106108882, \
             0.253413254537865690008131, \
             0.265196195159551900488370, \
             0.276939662140840894253032, \
             0.288641907502685160168097, \
             0.300301189401748840754520, \
             0.311915772389675771851948, \
             0.323483927671405649204085, \
             0.335003933362499872399782, \
             0.346474074745438764010632, \
             0.357892644524852014873858, \
             0.369257943081644365255611, \
             0.380568278725978696070941, \
             0.391821967949078874408131, \
             0.403017335673814873281489, \
             0.414152715504032866791986, \
             0.425226449972593188682213, \
             0.436236890788079234603398, \
             0.447182399080140586238810, \
             0.458061345643433838720630, \
             0.468872111180124821505728, \
             0.479613086540916117008992, \
             0.490282672964564000798817, \
             0.500879282315849152005553, \
             0.511401337321965712746629, \
             0.521847271807293510797499, \
             0.532215530926518500400434, \
             0.542504571396066721967792, \
             0.552712861723817332466074, \
             0.562838882437060514424546, \
             0.572881126308666332759406, \
             0.582838098581430874902446, \
             0.592708317190566281032495, \
             0.602490312984301547488097, \
             0.612182629942561267650033, \
             0.621783825393689760680446, \
             0.631292470229188329449219, \
             0.640707149116433684724434, \
             0.650026460709345873208532, \
             0.659249017856974352220492, \
             0.668373447809971163711735, \
             0.677398392424920474813593, \
             0.686322508366494071200553, \
             0.695144467307402713168813, \
             0.703862956126113592426171, \
             0.712476677102304460118510, \
             0.720984348110025333531072, \
             0.729384702808539030149808, \
             0.737676490830812123299244, \
             0.745858477969628263337895, \
             0.753929446361296162339238, \
             0.761888194666924898264210, \
             0.769733538251239556788216, \
             0.777464309358910595129671, \
             0.785079357288370682385816, \
             0.792577548563093144962574, \
             0.799957767100306523636066, \
             0.807218914377120130552073, \
             0.814359909594035880004229, \
             0.821379689835822056081139, \
             0.828277210229725073186687, \
             0.835051444100995681967937, \
             0.841701383125706473284556, \
             0.848226037480837936478636, \
             0.854624435991610735314055, \
             0.860895626276042275514686, \
             0.867038674886706051812473, \
             0.873052667449672679799858, \
             0.878936708800611938658765, \
             0.884689923118035575018750, \
             0.890311454053661045810287, \
             0.895800464859876809085345, \
             0.901156138514290206476301, \
             0.906377677841339419411308, \
             0.911464305630951423630955, \
             0.916415264754228313295468, \
             0.921229818276144817520964, \
             0.925907249565240289235888, \
             0.930446862400288909805510, \
             0.934847981073932324370129, \
             0.939109950493259404355123, \
             0.943232136277318328151464, \
             0.947213924851546682950881, \
             0.951054723539105826691801, \
             0.954753960649106318830855, \
             0.958311085561711847074814, \
             0.961725568810109767190665, \
             0.964996902159337170373447, \
             0.968124598681952354372943, \
             0.971108192830542793021113, \
             0.973947240507062326750976, \
             0.976641319128992592610888, \
             0.979190027692327124191591, \
             0.981592986831381877693095, \
             0.983849838875444644048531, \
             0.985960247902290665366669, \
             0.987923899788618253106809, \
             0.989740502257507526030375, \
             0.991409784923101705201254, \
             0.992931499332908653172844, \
             0.994305419008553630362377, \
             0.995531339486830143483750, \
             0.996609078365487004512326, \
             0.997538475365520218731818, \
             0.998319392445383847808766, \
             0.998951714093223210129834, \
             0.999435348366365078441838, \
             0.999770232390338019056053, \
             0.999956390712330402472857 ] )

    w = np.array ( [ \
           0.00011191470145601756450862287886, \
           0.00026049995580176964436806680831, \
           0.00040926648283531339591138751432, \
           0.00055799120546880640169677292533, \
           0.00070663671051592291949335494247, \
           0.00085517818446696565626595950963, \
           0.00100359280467969441299468763292, \
           0.0011518582377826677880963146741, \
           0.0012999523174235227389668643832, \
            0.0014478529559255120065233994722, \
            0.0015955381166175133369701690235, \
            0.0017429858051468299509941139300, \
            0.0018901740676190104269878470891, \
            0.0020370809914723626741694800322, \
            0.0021836847075455253317921866057, \
            0.0023299633927021828561308282641, \
            0.0024758952727301488651840215879, \
            0.0026214586253808109266552781372, \
            0.0027666317834818283552560256501, \
            0.0029113931380877846359302447381, \
            0.0030557211416493711130936102459, \
            0.0031995943111899437356540290142, \
            0.0033429912314827618499065991316, \
            0.0034858905582247143702551557840, \
            0.0036282710212037760873102463983, \
            0.0037701114274582873548537007645, \
            0.0039113906644266662571543468015, \
            0.0040520877030864825223229951262, \
            0.0041921816010820254766367595011, \
            0.0043316515058396297504806208252, \
            0.0044704766576701092218388764046, \
            0.0046086363928577081326523656522, \
            0.0047461101467350184936945641585, \
            0.0048828774567433411142588306018, \
            0.0050189179654779878773297516544, \
            0.0051542114237180378340642003713, \
            0.0052887376934400710240953933529, \
            0.0054224767508154127788846727083, \
            0.0055554086891904284012033890901, \
            0.0056875137220494140577838938236, \
            0.0058187721859596348346566361185, \
            0.0059491645434980654366600347567, \
            0.0060786713861593931405204596709, \
            0.0062072734372448464599330978665, \
            0.0063349515547314166407936938524, \
            0.0064616867341210426397202932350, \
            0.0065874601112693336961737372300, \
            0.0067122529651934070221351960200, \
            0.0068360467208584215286561508406, \
            0.0069588229519423919043121805236, \
            0.0070805633835788707705149901066, \
            0.0072012498950770900730828552207, \
            0.0073208645226191563361371026044, \
            0.0074393894619338979090297315972, \
            0.0075568070709469658838993300454, \
            0.0076730998724067939537782250476, \
            0.0077882505564860261212726654404, \
            0.0079022419833580248574070864277, \
            0.0080150571857480760504667455353, \
            0.0081266793714589108764118189068, \
            0.0082370919258701685661946145361, \
            0.0083462784144114279413811886655, \
            0.0084542225850084395379670551258, \
            0.0085609083705021941391459209280, \
            0.0086663198910404675908861979240, \
            0.0087704414564414858792445834744, \
            0.0088732575685293586050755892934, \
            0.0089747529234409331997949023068, \
            0.0090749124139037264846862498962, \
            0.0091737211314845944854270065178, \
            0.0092711643688088057725325917169, \
            0.0093672276217491880067391857021, \
            0.0094618965915850218253881576301, \
            0.0095551571871303607110514249099, \
            0.0096469955268314600363329731559, \
            0.0097373979408330030783691793250, \
            0.0098263509730128164423854701706, \
            0.0099138413829847720250916955489, \
            0.0099998561480695773850435626986, \
            0.0100843824652331611676814627839, \
            0.0101674077529923650568895461852, \
            0.0102489196532876585918958554047, \
            0.0103289060333225980974485876288, \
            0.0104073549873697559257355517893, \
            0.0104842548385428511997370260353, \
            0.0105595941405348182788823332058, \
            0.0106333616793215542382761147904, \
            0.0107055464748310917616231511294, \
            0.0107761377825779489945556541150, \
            0.0108451250952624130885928632830, \
            0.0109124981443345193856719616965, \
            0.0109782469015224934483083029166, \
            0.0110423615803254284301924654946, \
            0.0111048326374699756056269264803, \
            0.0111656507743308312328559850485, \
            0.0112248069383148083152535688671, \
            0.0112822923242082872447042603128, \
            0.0113380983754878447625379269120, \
            0.011392216785593866154247619654, \
             0.011444639499166951104119199270, \
             0.011495358713246929174010288914, \
             0.011544366878434306436012137033, \
             0.011591656700013970380783131035, \
             0.011637221139040985841125311445, \
             0.011681053413388320313049670635, \
             0.011723146998756342723302879656, \
             0.011763495629643945382264331878, \
             0.011802093300281144573421477037, \
             0.011838934265523020964443424791, \
             0.011874013041704866779344562066, \
             0.011907324407458412445505183140, \
             0.011938863404489011222535627643, \
             0.011968625338313666131272065445, \
             0.011996605778959789329711050159, \
             0.012022800561624589927558893338, \
             0.012047205787294992091420946532, \
             0.012069817823327991167612855626, \
             0.012090633303991361438266420912, \
             0.012109649130964635027950450318, \
             0.012126862473800277391553601370, \
             0.012142270770344990738801546574, \
             0.012155871727121082685623083829, \
             0.012167663319667843366755737416, \
             0.012177643792842880196606249581, \
             0.012185811661083365425569178819, \
             0.012192165708627157605870499188, \
             0.012196704989693764053654538465, \
             0.012199428828625117371582840212, \
             0.01220033681998614507777289232, \
             0.012199428828625117371582840212, \
             0.012196704989693764053654538465, \
             0.012192165708627157605870499188, \
             0.012185811661083365425569178819, \
             0.012177643792842880196606249581, \
             0.012167663319667843366755737416, \
             0.012155871727121082685623083829, \
             0.012142270770344990738801546574, \
             0.012126862473800277391553601370, \
             0.012109649130964635027950450318, \
             0.012090633303991361438266420912, \
             0.012069817823327991167612855626, \
             0.012047205787294992091420946532, \
             0.012022800561624589927558893338, \
             0.011996605778959789329711050159, \
             0.011968625338313666131272065445, \
             0.011938863404489011222535627643, \
             0.011907324407458412445505183140, \
             0.011874013041704866779344562066, \
             0.011838934265523020964443424791, \
             0.011802093300281144573421477037, \
             0.011763495629643945382264331878, \
             0.011723146998756342723302879656, \
             0.011681053413388320313049670635, \
             0.011637221139040985841125311445, \
             0.011591656700013970380783131035, \
             0.011544366878434306436012137033, \
             0.011495358713246929174010288914, \
             0.011444639499166951104119199270, \
             0.011392216785593866154247619654, \
             0.0113380983754878447625379269120, \
             0.0112822923242082872447042603128, \
             0.0112248069383148083152535688671, \
             0.0111656507743308312328559850485, \
             0.0111048326374699756056269264803, \
             0.0110423615803254284301924654946, \
             0.0109782469015224934483083029166, \
             0.0109124981443345193856719616965, \
             0.0108451250952624130885928632830, \
             0.0107761377825779489945556541150, \
             0.0107055464748310917616231511294, \
             0.0106333616793215542382761147904, \
             0.0105595941405348182788823332058, \
             0.0104842548385428511997370260353, \
             0.0104073549873697559257355517893, \
             0.0103289060333225980974485876288, \
             0.0102489196532876585918958554047, \
             0.0101674077529923650568895461852, \
             0.0100843824652331611676814627839, \
             0.0099998561480695773850435626986, \
             0.0099138413829847720250916955489, \
             0.0098263509730128164423854701706, \
             0.0097373979408330030783691793250, \
             0.0096469955268314600363329731559, \
             0.0095551571871303607110514249099, \
             0.0094618965915850218253881576301, \
             0.0093672276217491880067391857021, \
             0.0092711643688088057725325917169, \
             0.0091737211314845944854270065178, \
             0.0090749124139037264846862498962, \
             0.0089747529234409331997949023068, \
             0.0088732575685293586050755892934, \
             0.0087704414564414858792445834744, \
             0.0086663198910404675908861979240, \
             0.0085609083705021941391459209280, \
             0.0084542225850084395379670551258, \
             0.0083462784144114279413811886655, \
             0.0082370919258701685661946145361, \
             0.0081266793714589108764118189068, \
             0.0080150571857480760504667455353, \
             0.0079022419833580248574070864277, \
             0.0077882505564860261212726654404, \
             0.0076730998724067939537782250476, \
             0.0075568070709469658838993300454, \
             0.0074393894619338979090297315972, \
             0.0073208645226191563361371026044, \
             0.0072012498950770900730828552207, \
             0.0070805633835788707705149901066, \
             0.0069588229519423919043121805236, \
             0.0068360467208584215286561508406, \
             0.0067122529651934070221351960200, \
             0.0065874601112693336961737372300, \
             0.0064616867341210426397202932350, \
             0.0063349515547314166407936938524, \
             0.0062072734372448464599330978665, \
             0.0060786713861593931405204596709, \
             0.0059491645434980654366600347567, \
             0.0058187721859596348346566361185, \
             0.0056875137220494140577838938236, \
             0.0055554086891904284012033890901, \
             0.0054224767508154127788846727083, \
             0.0052887376934400710240953933529, \
             0.0051542114237180378340642003713, \
             0.0050189179654779878773297516544, \
             0.0048828774567433411142588306018, \
             0.0047461101467350184936945641585, \
             0.0046086363928577081326523656522, \
             0.0044704766576701092218388764046, \
             0.0043316515058396297504806208252, \
             0.0041921816010820254766367595011, \
             0.0040520877030864825223229951262, \
             0.0039113906644266662571543468015, \
             0.0037701114274582873548537007645, \
             0.0036282710212037760873102463983, \
             0.0034858905582247143702551557840, \
             0.0033429912314827618499065991316, \
             0.0031995943111899437356540290142, \
             0.0030557211416493711130936102459, \
             0.0029113931380877846359302447381, \
             0.0027666317834818283552560256501, \
             0.0026214586253808109266552781372, \
             0.0024758952727301488651840215879, \
             0.0023299633927021828561308282641, \
             0.0021836847075455253317921866057, \
             0.0020370809914723626741694800322, \
             0.0018901740676190104269878470891, \
             0.0017429858051468299509941139300, \
             0.0015955381166175133369701690235, \
             0.0014478529559255120065233994722, \
             0.0012999523174235227389668643832, \
             0.0011518582377826677880963146741, \
             0.00100359280467969441299468763292, \
             0.00085517818446696565626595950963, \
             0.00070663671051592291949335494247, \
             0.00055799120546880640169677292533, \
             0.00040926648283531339591138751432, \
             0.00026049995580176964436806680831, \
             0.00011191470145601756450862287886 ] )

  else:

    print ( '' )
    print ( 'legendre_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 to 33, 63/64/65, 127/128/129, 255/256/257.' )
    raise Exception ( 'legendre_SET(): Fatal error!' )

  return x, w

def legendre_set_test ( ):

#*****************************************************************************80
#
## legendre_set_test() tests legendre_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'legendre_set_test():' )
  print ( '  legendre_set() sets a Legendre quadrature rule.' )
  print ( '' )
  print ( '         I            X                  W' )

  for n in range ( 1, 11 ):

    x, w = legendre_set ( n )

    print ( '' )
    for i in range ( 0 , n ):
      print ( '  %8d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def lobatto_compute ( n ):

#*****************************************************************************80
#
## lobatto_compute() computes a Lobatto quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    The quadrature rule will integrate exactly all polynomials up to
#    X^(2*N-3).
#
#    The Lobatto rule is distinguished by the fact that both endpoints
#    (-1 and 1) are always abscissas of the rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 April 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Claudio Canuto, Yousuff Hussaini, Alfio Quarteroni, Thomas Zang,
#    Spectral Methods in Fluid Dynamics,
#    Springer, 1993,
#    ISNB13: 978-3540522058,
#    LC: QA377.S676.
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996,
#    ISBN: 0-8493-2479-3.
#
#  Input:
#
#    integer N, the order.  
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights,
#
  import numpy as np

  x = np.zeros ( n )
  w = np.zeros ( n )

  if ( n == 1 ):
    x[0] = -1.0
    w[0] = 2.0
    return x, w

  tol = 100.0 * np.finfo(float).eps
#
#  Initial estimate for the abscissas is the Chebyshev-Gauss-Lobatto nodes.
#
  for i in range ( 0, n ):
    x[i] = np.cos ( np.pi * float ( i ) / float ( n - 1 ) )

  xold = np.zeros ( n )
  p = np.zeros ( [ n, n ] )

  while ( True  ):

    for i in range ( 0, n ):
      xold[i] = x[i]

    for i in range ( 0, n ):
      p[i,0] = 1.0
      p[i,1] = x[i]

    for j in range ( 2, n ):
      for i in range ( 0, n ):
        p[i,j] = ( float ( 2 * j - 1 ) * x[i] * p[i,j-1]     \
                 + float (   - j + 1 ) *        p[i,j-2] ) \
                 / float (     j     )

    for i in range ( 0, n ):
      x[i] = xold[i] - ( x[i] * p[i,n-1] - p[i,n-2] ) \
        / ( float ( n ) * p[i,n-1] )

    dif = r8vec_diff_norm_li ( n, x, xold )
 
    if ( dif <= tol ):
      break

  x = r8vec_reverse ( n, x )

  for i in range ( 0, n ):
    w[i] = 2.0 / ( float ( n * ( n - 1 ) ) * p[i,n-1] ** 2 )

  return x, w

def lobatto_compute_test ( ):

#*****************************************************************************80
#
## lobatto_compute_test() tests lobatto_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'lobatto_compute_test():' )
  print ( '  lobatto_compute() computes a Lobatto rule' )
  print ( '' )
  print ( '         I      X             W' )

  for n in range ( 4, 11, 3 ):

    x, w = lobatto_compute ( n )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %8d  %12g  %12g' % ( i, x[i], w[i] ) )

  return

def lobatto_set ( n ):

#*****************************************************************************80
#
## lobatto_set() sets abscissas and weights for Lobatto quadrature.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    The quadrature rule will integrate exactly all polynomials up to
#    X^(2*N-3).
#
#    The Lobatto rule is distinguished by the fact that both endpoints
#    (-1 and 1) are always abscissas of the rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964.
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966.
#
#    Daniel Zwillinger, editor,
#    Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer N, the order.
#    N must be between 1 and 20.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
           -1.0 ] )

    w = np.array ( [ \
           2.0 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
            - 1.0, \
              1.0 ] )

    w = np.array ( [ \
            1.0, \
            1.0 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
            - 1.0, \
              0.0, \
              1.0 ] )

    w = np.array ( [ \
            1.0 / 3.0, \
            4.0 / 3.0, \
            1.0 / 3.0 ] )

  elif ( n == 4 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.447213595499957939281834733746, \
              0.447213595499957939281834733746, \
              1.0 ] )

    w = np.array ( [ \
            1.0 / 6.0, \
            5.0 / 6.0, \
            5.0 / 6.0, \
            1.0 / 6.0 ] )

  elif ( n == 5 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.654653670707977143798292456247, \
              0.0, \
              0.654653670707977143798292456247, \
              1.0 ] )

    w = np.array ( [ \
            9.0 / 90.0, \
           49.0 / 90.0, \
           64.0 / 90.0, \
           49.0 / 90.0, \
            9.0 / 90.0 ] )

  elif ( n == 6 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.765055323929464692851002973959, \
            - 0.285231516480645096314150994041, \
              0.285231516480645096314150994041, \
              0.765055323929464692851002973959, \
              1.0 ] )

    w = np.array ( [ \
            0.066666666666666666666666666667, \
            0.378474956297846980316612808212, \
            0.554858377035486353016720525121, \
            0.554858377035486353016720525121, \
            0.378474956297846980316612808212, \
            0.066666666666666666666666666667 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.830223896278566929872032213967, \
            - 0.468848793470714213803771881909, \
              0.0, \
              0.468848793470714213803771881909, \
              0.830223896278566929872032213967, \
              1.0 ] )

    w = np.array ( [ \
            0.476190476190476190476190476190E-01, \
            0.276826047361565948010700406290, \
            0.431745381209862623417871022281, \
            0.487619047619047619047619047619, \
            0.431745381209862623417871022281, \
            0.276826047361565948010700406290, \
            0.476190476190476190476190476190E-01 ] )

  elif ( n == 8 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.871740148509606615337445761221, \
            - 0.591700181433142302144510731398, \
            - 0.209299217902478868768657260345, \
              0.209299217902478868768657260345, \
              0.591700181433142302144510731398, \
              0.871740148509606615337445761221, \
              1.0 ] )

    w = np.array ( [ \
            0.357142857142857142857142857143E-01, \
            0.210704227143506039382991065776, \
            0.341122692483504364764240677108, \
            0.412458794658703881567052971402, \
            0.412458794658703881567052971402, \
            0.341122692483504364764240677108, \
            0.210704227143506039382991065776, \
            0.357142857142857142857142857143E-01 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.899757995411460157312345244418, \
            - 0.677186279510737753445885427091, \
            - 0.363117463826178158710752068709, \
              0.0, \
              0.363117463826178158710752068709, \
              0.677186279510737753445885427091, \
              0.899757995411460157312345244418, \
              1.0 ] )

    w = np.array ( [ \
            0.277777777777777777777777777778E-01, \
            0.165495361560805525046339720029, \
            0.274538712500161735280705618579, \
            0.346428510973046345115131532140, \
            0.371519274376417233560090702948, \
            0.346428510973046345115131532140, \
            0.274538712500161735280705618579, \
            0.165495361560805525046339720029, \
            0.277777777777777777777777777778E-01 ] )

  elif ( n == 10 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.919533908166458813828932660822, \
            - 0.738773865105505075003106174860, \
            - 0.477924949810444495661175092731, \
            - 0.165278957666387024626219765958, \
              0.165278957666387024626219765958, \
              0.477924949810444495661175092731, \
              0.738773865105505075003106174860, \
              0.919533908166458813828932660822, \
              1.0 ] )

    w = np.array ( [ \
            0.222222222222222222222222222222E-01, \
            0.133305990851070111126227170755, \
            0.224889342063126452119457821731, \
            0.292042683679683757875582257374, \
            0.327539761183897456656510527917, \
            0.327539761183897456656510527917, \
            0.292042683679683757875582257374, \
            0.224889342063126452119457821731, \
            0.133305990851070111126227170755, \
            0.222222222222222222222222222222E-01 ] )

  elif ( n == 11 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.934001430408059134332274136099, \
            - 0.784483473663144418622417816108, \
            - 0.565235326996205006470963969478, \
            - 0.295758135586939391431911515559, \
              0.0, \
              0.295758135586939391431911515559, \
              0.565235326996205006470963969478, \
              0.784483473663144418622417816108, \
              0.934001430408059134332274136099, \
              1.0 ] )

    w = np.array ( [ \
            0.181818181818181818181818181818E-01, \
            0.109612273266994864461403449580, \
            0.187169881780305204108141521899, \
            0.248048104264028314040084866422, \
            0.286879124779008088679222403332, \
            0.300217595455690693785931881170, \
            0.286879124779008088679222403332, \
            0.248048104264028314040084866422, \
            0.187169881780305204108141521899, \
            0.109612273266994864461403449580, \
            0.181818181818181818181818181818E-01 ] )

  elif ( n == 12 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.944899272222882223407580138303, \
            - 0.819279321644006678348641581717, \
            - 0.632876153031869677662404854444, \
            - 0.399530940965348932264349791567, \
            - 0.136552932854927554864061855740, \
              0.136552932854927554864061855740, \
              0.399530940965348932264349791567, \
              0.632876153031869677662404854444, \
              0.819279321644006678348641581717, \
              0.944899272222882223407580138303, \
              1.0 ] )

    w = np.array ( [ \
            0.151515151515151515151515151515E-01, \
            0.916845174131961306683425941341E-01, \
            0.157974705564370115164671062700, \
            0.212508417761021145358302077367, \
            0.251275603199201280293244412148, \
            0.271405240910696177000288338500, \
            0.271405240910696177000288338500, \
            0.251275603199201280293244412148, \
            0.212508417761021145358302077367, \
            0.157974705564370115164671062700, \
            0.916845174131961306683425941341E-01, \
            0.151515151515151515151515151515E-01 ] )

  elif ( n == 13 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.953309846642163911896905464755, \
            - 0.846347564651872316865925607099, \
            - 0.686188469081757426072759039566, \
            - 0.482909821091336201746937233637, \
            - 0.249286930106239992568673700374, \
              0.0, \
              0.249286930106239992568673700374, \
              0.482909821091336201746937233637, \
              0.686188469081757426072759039566, \
              0.846347564651872316865925607099, \
              0.953309846642163911896905464755, \
              1.0 ] )

    w = np.array ( [ \
            0.128205128205128205128205128205E-01, \
            0.778016867468189277935889883331E-01, \
            0.134981926689608349119914762589, \
            0.183646865203550092007494258747, \
            0.220767793566110086085534008379, \
            0.244015790306676356458578148360, \
            0.251930849333446736044138641541, \
            0.244015790306676356458578148360, \
            0.220767793566110086085534008379, \
            0.183646865203550092007494258747, \
            0.134981926689608349119914762589, \
            0.778016867468189277935889883331E-01, \
            0.128205128205128205128205128205E-01 ] )

  elif ( n == 14 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.959935045267260901355100162015, \
            - 0.867801053830347251000220202908, \
            - 0.728868599091326140584672400521, \
            - 0.550639402928647055316622705859, \
            - 0.342724013342712845043903403642, \
            - 0.116331868883703867658776709736, \
              0.116331868883703867658776709736, \
              0.342724013342712845043903403642, \
              0.550639402928647055316622705859, \
              0.728868599091326140584672400521, \
              0.867801053830347251000220202908, \
              0.959935045267260901355100162015, \
              1.0 ] )

    w = np.array ( [ \
            0.109890109890109890109890109890E-01, \
            0.668372844976812846340706607461E-01, \
            0.116586655898711651540996670655, \
            0.160021851762952142412820997988, \
            0.194826149373416118640331778376, \
            0.219126253009770754871162523954, \
            0.231612794468457058889628357293, \
            0.231612794468457058889628357293, \
            0.219126253009770754871162523954, \
            0.194826149373416118640331778376, \
            0.160021851762952142412820997988, \
            0.116586655898711651540996670655, \
            0.668372844976812846340706607461E-01, \
            0.109890109890109890109890109890E-01 ] )

  elif ( n == 15 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.965245926503838572795851392070, \
            - 0.885082044222976298825401631482, \
            - 0.763519689951815200704118475976, \
            - 0.606253205469845711123529938637, \
            - 0.420638054713672480921896938739, \
            - 0.215353955363794238225679446273, \
              0.0, \
              0.215353955363794238225679446273, \
              0.420638054713672480921896938739, \
              0.606253205469845711123529938637, \
              0.763519689951815200704118475976, \
              0.885082044222976298825401631482, \
              0.965245926503838572795851392070, \
              1.0 ] )

    w = np.array ( [ \
            0.952380952380952380952380952381E-02, \
            0.580298930286012490968805840253E-01, \
            0.101660070325718067603666170789, \
            0.140511699802428109460446805644, \
            0.172789647253600949052077099408, \
            0.196987235964613356092500346507, \
            0.211973585926820920127430076977, \
            0.217048116348815649514950214251, \
            0.211973585926820920127430076977, \
            0.196987235964613356092500346507, \
            0.172789647253600949052077099408, \
            0.140511699802428109460446805644, \
            0.101660070325718067603666170789, \
            0.580298930286012490968805840253E-01, \
            0.952380952380952380952380952381E-02 ] )

  elif ( n == 16 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.969568046270217932952242738367, \
            - 0.899200533093472092994628261520, \
            - 0.792008291861815063931088270963, \
            - 0.652388702882493089467883219641, \
            - 0.486059421887137611781890785847, \
            - 0.299830468900763208098353454722, \
            - 0.101326273521949447843033005046, \
              0.101326273521949447843033005046, \
              0.299830468900763208098353454722, \
              0.486059421887137611781890785847, \
              0.652388702882493089467883219641, \
              0.792008291861815063931088270963, \
              0.899200533093472092994628261520, \
              0.969568046270217932952242738367, \
              1.0 ] )

    w = np.array ( [ \
            0.833333333333333333333333333333E-02, \
            0.508503610059199054032449195655E-01, \
            0.893936973259308009910520801661E-01, \
            0.124255382132514098349536332657, \
            0.154026980807164280815644940485, \
            0.177491913391704125301075669528, \
            0.193690023825203584316913598854, \
            0.201958308178229871489199125411, \
            0.201958308178229871489199125411, \
            0.193690023825203584316913598854, \
            0.177491913391704125301075669528, \
            0.154026980807164280815644940485, \
            0.124255382132514098349536332657, \
            0.893936973259308009910520801661E-01, \
            0.508503610059199054032449195655E-01, \
            0.833333333333333333333333333333E-02 ] )

  elif ( n == 17 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.973132176631418314156979501874, \
            - 0.910879995915573595623802506398, \
            - 0.815696251221770307106750553238, \
            - 0.691028980627684705394919357372, \
            - 0.541385399330101539123733407504, \
            - 0.372174433565477041907234680735, \
            - 0.189511973518317388304263014753, \
              0.0, \
              0.189511973518317388304263014753, \
              0.372174433565477041907234680735, \
              0.541385399330101539123733407504, \
              0.691028980627684705394919357372, \
              0.815696251221770307106750553238, \
              0.910879995915573595623802506398, \
              0.973132176631418314156979501874, \
              1.0 ] )

    w = np.array ( [ \
            0.735294117647058823529411764706E-02, \
            0.449219405432542096474009546232E-01, \
            0.791982705036871191902644299528E-01, \
            0.110592909007028161375772705220, \
            0.137987746201926559056201574954, \
            0.160394661997621539516328365865, \
            0.177004253515657870436945745363, \
            0.187216339677619235892088482861, \
            0.190661874753469433299407247028, \
            0.187216339677619235892088482861, \
            0.177004253515657870436945745363, \
            0.160394661997621539516328365865, \
            0.137987746201926559056201574954, \
            0.110592909007028161375772705220, \
            0.791982705036871191902644299528E-01, \
            0.449219405432542096474009546232E-01, \
            0.735294117647058823529411764706E-02 ] )

  elif ( n == 18 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.976105557412198542864518924342, \
            - 0.920649185347533873837854625431, \
            - 0.835593535218090213713646362328, \
            - 0.723679329283242681306210365302, \
            - 0.588504834318661761173535893194, \
            - 0.434415036912123975342287136741, \
            - 0.266362652878280984167665332026, \
            - 0.897490934846521110226450100886E-01, \
              0.897490934846521110226450100886E-01, \
              0.266362652878280984167665332026, \
              0.434415036912123975342287136741, \
              0.588504834318661761173535893194, \
              0.723679329283242681306210365302, \
              0.835593535218090213713646362328, \
              0.920649185347533873837854625431, \
              0.976105557412198542864518924342, \
              1.0 ] )

    w = np.array ( [ \
            0.653594771241830065359477124183E-02, \
            0.399706288109140661375991764101E-01, \
            0.706371668856336649992229601678E-01, \
            0.990162717175028023944236053187E-01, \
            0.124210533132967100263396358897, \
            0.145411961573802267983003210494, \
            0.161939517237602489264326706700, \
            0.173262109489456226010614403827, \
            0.179015863439703082293818806944, \
            0.179015863439703082293818806944, \
            0.173262109489456226010614403827, \
            0.161939517237602489264326706700, \
            0.145411961573802267983003210494, \
            0.124210533132967100263396358897, \
            0.990162717175028023944236053187E-01, \
            0.706371668856336649992229601678E-01, \
            0.399706288109140661375991764101E-01, \
            0.653594771241830065359477124183E-02 ] )

  elif ( n == 19 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.978611766222080095152634063110, \
            - 0.928901528152586243717940258797, \
            - 0.852460577796646093085955970041, \
            - 0.751494202552613014163637489634, \
            - 0.628908137265220497766832306229, \
            - 0.488229285680713502777909637625, \
            - 0.333504847824498610298500103845, \
            - 0.169186023409281571375154153445, \
              0.0, \
              0.169186023409281571375154153445, \
              0.333504847824498610298500103845, \
              0.488229285680713502777909637625, \
              0.628908137265220497766832306229, \
              0.751494202552613014163637489634, \
              0.852460577796646093085955970041, \
              0.928901528152586243717940258797, \
              0.978611766222080095152634063110, \
              1.0 ] )

    w = np.array ( [ \
            0.584795321637426900584795321637E-02, \
            0.357933651861764771154255690351E-01, \
            0.633818917626297368516956904183E-01, \
            0.891317570992070844480087905562E-01, \
            0.112315341477305044070910015464, \
            0.132267280448750776926046733910, \
            0.148413942595938885009680643668, \
            0.160290924044061241979910968184, \
            0.167556584527142867270137277740, \
            0.170001919284827234644672715617, \
            0.167556584527142867270137277740, \
            0.160290924044061241979910968184, \
            0.148413942595938885009680643668, \
            0.132267280448750776926046733910, \
            0.112315341477305044070910015464, \
            0.891317570992070844480087905562E-01, \
            0.633818917626297368516956904183E-01, \
            0.357933651861764771154255690351E-01, \
            0.584795321637426900584795321637E-02 ] )

  elif ( n == 20 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.980743704893914171925446438584, \
            - 0.935934498812665435716181584931, \
            - 0.866877978089950141309847214616, \
            - 0.775368260952055870414317527595, \
            - 0.663776402290311289846403322971, \
            - 0.534992864031886261648135961829, \
            - 0.392353183713909299386474703816, \
            - 0.239551705922986495182401356927, \
            - 0.805459372388218379759445181596E-01, \
              0.805459372388218379759445181596E-01, \
              0.239551705922986495182401356927, \
              0.392353183713909299386474703816, \
              0.534992864031886261648135961829, \
              0.663776402290311289846403322971, \
              0.775368260952055870414317527595, \
              0.866877978089950141309847214616, \
              0.935934498812665435716181584931, \
              0.980743704893914171925446438584, \
              1.0 ] )

    w = np.array ( [ \
            0.526315789473684210526315789474E-02, \
            0.322371231884889414916050281173E-01, \
            0.571818021275668260047536271732E-01, \
            0.806317639961196031447768461137E-01, \
            0.101991499699450815683781205733, \
            0.120709227628674725099429705002, \
            0.136300482358724184489780792989, \
            0.148361554070916825814713013734, \
            0.156580102647475487158169896794, \
            0.160743286387845749007726726449, \
            0.160743286387845749007726726449, \
            0.156580102647475487158169896794, \
            0.148361554070916825814713013734, \
            0.136300482358724184489780792989, \
            0.120709227628674725099429705002, \
            0.101991499699450815683781205733, \
            0.806317639961196031447768461137E-01, \
            0.571818021275668260047536271732E-01, \
            0.322371231884889414916050281173E-01, \
            0.526315789473684210526315789474E-02 ] )

  else:

    print ( '' )
    print ( 'LOBATTO_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are between 1 and 20.' )
    raise Exception ( 'LOBATTO_SET(): Fatal error!' )

  return x, w

def lobatto_set_test ( ):

#*****************************************************************************80
#
## lobatto_set_test() tests lobatto_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'lobatto_set_test():' )
  print ( '  lobatto_set() sets a Lobatto rule' )
  print ( '' )
  print ( '         I      X             W' )

  for n in range ( 4, 11, 3 ):

    x, w = lobatto_set ( n )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %8d  %12g  %12g' % ( i, x[i], w[i] ) )

  return

def moulton_set ( n ):

#*****************************************************************************80
#
## moulton_set() sets weights for Adams-Moulton quadrature.
#
#  Discussion:
#
#    Adams-Moulton quadrature formulas are normally used in solving
#    ordinary differential equations, and are not suitable for general
#    quadrature computations.  However, an Adams-Moulton formula is
#    equivalent to approximating the integral of F(Y(X)) between X(M)
#    and X(M+1), using an implicit formula that relies on known values
#    of F(Y(X)) at X(M-N+1) through X(M), plus the unknown value at X(M+1).
#
#    Suppose the unknown function is denoted by Y(X), with derivative F(Y(X)),
#    and that approximate values of the function are known at a series of
#    X values, which we write as X(1), X(2), ..., X(M).  We write the value
#    Y(X(1)) as Y(1) and so on.
#
#    Then the solution of the ODE Y' = F(X,Y) at the next point X(M+1) is
#    computed by:
#
#      Y(M+1) = Y(M) + Integral ( X(M) < X < X(M+1) ) F(Y(X)) dX
#             = Y(M) + H * Sum ( 1 <= I <= N ) W(I) * F(Y(M+2-I)) approximately.
#
#    Note that this formula is implicit, since the unknown value Y(M+1)
#    appears on the right hand side.  Hence, in ODE applications, this
#    equation must be solved via a nonlinear equation solver.  For
#    quadrature problems, where the function to be integrated is known
#    beforehand, this is not a problem, and the calculation is explicit.
#
#    In the documentation that follows, we replace F(Y(X)) by F(X).
#
#
#    The Adams-Moulton formulas require equally spaced data.
#
#    Here is how the formula is applied in the case with non-unit spacing:
#
#      Integral ( A <= X <= A+H ) F(X) dX =
#      H * Sum ( 1 <= I <= N ) W(I) * F ( A - (I-2)*H ),
#      approximately.
#
#    The integral:
#
#      Integral ( 0 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( 2 - I )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    page 915 ("Lagrangian Integration Coefficients").
#
#    Jean Lapidus and John Seinfeld,
#    Numerical Solution of Ordinary Differential Equations,
#    Academic Press, 1971.
#
#    Daniel Zwillinger, editor,
#    Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer N, the order.
#    N must be between 1 and 10, 12, 14, 16, 18 or 20.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#    W(1) is the weight at X = 1, W(2) the weight at X = 0, and so on.
#    The weights are rational.  The weights are not symmetric, and
#    some weights may be negative.  They should sum to 1.
#
  import numpy as np

  x = np.zeros ( n )
  w = np.zeros ( n )

  if ( n == 1 ):

    d = 1.0

    w = np.array ( [ \
       1.0 \
    ] )

  elif ( n == 2 ):

    d = 2.0

    w = np.array ( [ \
      1.0, \
      1.0 \
    ] )

  elif ( n == 3 ):

    d = 12.0

    w = np.array ( [ \
        5.0, \
        8.0, \
      - 1.0 \
    ] )

  elif ( n == 4 ):

    d = 24.0

    w = np.array ( [ \
        9.0, \
       19.0, \
      - 5.0, \
        1.0 \
    ] )

  elif ( n == 5 ):

    d = 720.0

    w = np.array ( [ \
        251.0, \
        646.0, \
      - 264.0, \
        106.0, \
       - 19.0 \
    ] )

  elif ( n == 6 ):

    d = 1440.0

    w = np.array ( [ \
        475.0, \
       1427.0, \
      - 798.0, \
        482.0, \
      - 173.0, \
         27.0 \
    ] )

  elif ( n == 7 ):

    d = 60480.0

    w = np.array ( [ \
        19087.0, \
        65112.0, \
      - 46461.0, \
        37504.0, \
      - 20211.0, \
         6312.0, \
        - 863.0 \
    ] )

  elif ( n == 8 ):

    d = 120960.0

    w = np.array ( [ \
        36799.0, \
       139849.0, \
     - 121797.0, \
       123133.0, \
      - 88547.0, \
        41499.0, \
      - 11351.0, \
         1375.0 \
    ] )

  elif ( n == 9 ):
  
    d = 3628800.0

    w = np.array ( [ \
       1070017.0, \
       4467094.0, \
     - 4604594.0, \
       5595358.0, \
     - 5033120.0, \
       3146338.0, \
     - 1291214.0, \
        312874.0, \
       - 33953.0 \
    ] )
  
  elif ( n == 10 ):
  
    d = 7257600.0

    w = np.array ( [ \
        2082753.0, \
        9449717.0, \
     - 11271304.0, \
       16002320.0, \
     - 17283646.0, \
       13510082.0, \
      - 7394032.0, \
        2687864.0, \
       - 583435.0, \
          57281.0 \
    ] )
  
  elif ( n == 12 ):
  
    d = 958003200.0

    w = np.array ( [ \
        262747265.0, \
       1374799219.0, \
      -2092490673.0, \
       3828828885.0, \
      -5519460582.0, \
       6043521486.0, \
      -4963166514.0, \
       3007739418.0, \
      -1305971115.0, \
        384709327.0, \
        -68928781.0, \
          5675265.0 \
    ] )
  
  elif ( n == 14 ):
  
    d = 5230697472000.0

    w = np.array ( [ \
        1382741929621.0, \
        8153167962181.0, \
      -15141235084110.0, \
       33928990133618.0, \
      -61188680131285.0, \
       86180228689563.0, \
      -94393338653892.0, \
       80101021029180.0, \
      -52177910882661.0, \
       25620259777835.0, \
       -9181635605134.0, \
        2268078814386.0, \
        -345457086395.0, \
          24466579093.0 \
    ] )
  
  elif ( n == 16 ):
  
    d = 62768369664000.0

    w = np.array ( [ \
         16088129229375.0, \
        105145058757073.0, \
       -230992163723849.0, \
        612744541065337.0, \
      -1326978663058069.0, \
       2285168598349733.0, \
      -3129453071993581.0, \
       3414941728852893.0, \
      -2966365730265699.0, \
       2039345879546643.0, \
      -1096355235402331.0, \
        451403108933483.0, \
       -137515713789319.0, \
         29219384284087.0, \
         -3867689367599.0, \
           240208245823.0 \
    ] )
  
  elif ( n == 18 ):
  
    d = 64023737057280000.0

    w = np.array ( [ \
          15980174332775873.0, \
         114329243705491117.0, \
        -290470969929371220.0, \
         890337710266029860.0, \
       -2250854333681641520.0, \
        4582441343348851896.0, \
       -7532171919277411636.0, \
       10047287575124288740.0, \
      -10910555637627652470.0, \
        9644799218032932490.0, \
       -6913858539337636636.0, \
        3985516155854664396.0, \
       -1821304040326216520.0, \
         645008976643217360.0, \
        -170761422500096220.0, \
          31816981024600492.0, \
          -3722582669836627.0, \
            205804074290625.0 \
    ] )
  
  elif ( n == 20 ):
  
    d = 102181884343418880000.0

    w = np.array ( [ \
           24919383499187492303.0, \
          193280569173472261637.0, \
         -558160720115629395555.0, \
         1941395668950986461335.0, \
        -5612131802364455926260.0, \
        13187185898439270330756.0, \
       -25293146116627869170796.0, \
        39878419226784442421820.0, \
       -51970649453670274135470.0, \
        56154678684618739939910.0, \
       -50320851025594566473146.0, \
        37297227252822858381906.0, \
       -22726350407538133839300.0, \
        11268210124987992327060.0, \
        -4474886658024166985340.0, \
         1389665263296211699212.0, \
         -325187970422032795497.0, \
           53935307402575440285.0, \
           -5652892248087175675.0, \
             281550972898020815.0 \
      ] )

  else:

    print ( '' )
    print ( 'MOULTON_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 through 10,' )
    print ( '  or 12, 14, 16, 18 or 20.' )
    raise Exception ( 'MOULTON_SET(): Fatal error!' )

  for i in range ( 0, n ):
    w[i] = w[i] / d

  for i in range ( 0, n ):
    x[i] = float ( 1 - i )

  return x, w

def moulton_set_test ( ):

#*****************************************************************************80
#
## moulton_set_test() tests moulton_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'moulton_set_test():' )
  print ( '  moulton_set() sets the abscissas and weights' )
  print ( '  for an Adams-Moulton quadrature rule.' )
  print ( '' )
  print ( '    Order  W             X' )
  print ( '' )

  for n in range ( 1, 11 ):

    x, w = moulton_set ( n )

    print ( '' )
    print ( '  %8d' % ( n ) )

    for i in range ( 0, n ):
      print ( '            %12g  %12g' % ( w[i], x[i] ) )

  return

def ncc_compute ( n ):

#*****************************************************************************80
#
## ncc_compute() computes a Newton-Cotes Closed quadrature rule.
#
#  Discussion:
#
#    For the interval [-1,+1], the Newton-Cotes Closed quadrature rule
#    estimates
#
#      Integral ( -1 <= X <= +1 ) F(X) dX
#
#    using N abscissas X and weights W:
#
#      sum ( 1 <= I <= N ) W(I) * F ( X(I) ).
#
#    For the CLOSED rule, the abscissas are equally spaced, and include
#    the end points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  x_min = -1.0
  x_max = +1.0
  x = np.linspace ( x_min, x_max, n )

  if ( n == 1 ):

    w = np.zeros ( n )
    w[0] = x_max - x_min

  else:

    w = nc_compute_weights ( n, x_min, x_max, x )

  return x, w

def ncc_compute_test ( ):

#*****************************************************************************80
#
## ncc_compute_test() tests ncc_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'ncc_compute_test():' )
  print ( '  ncc_compute() computes a Newton-Cotes Closed quadrature rule' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = ncc_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def nc_compute_weights ( n, x_min, x_max, x ):

#*****************************************************************************80
#
## nc_compute_weights() computes weights for a Newton-Cotes quadrature rule.
#
#  Discussion:
#
#    For the interval [X_MIN,X_MAX], the Newton-Cotes quadrature rule 
#    estimates
#
#      Integral ( X_MIN <= X <= X_MAX ) F(X) dX
#
#    using N abscissas X and weights W:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) ).
#
#    For the CLOSED rule, the equally spaced abscissas include A and B.
#    For the OPEN rule, the equally spaced abscissas do not include A and B.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 April 2010
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order.
#
#    real X_MIN, X_MAX, the endpoints of the interval.
#
#    real X(N), the abscissas.
#
#  Output:
#
#    real W(N), the weights.
#
  import numpy as np

  d = np.zeros ( n )
  w = np.zeros ( n )

  for i in range ( 1, n + 1 ):
#
#  Compute the Lagrange basis polynomial which is 1 at X(I),
#  and zero at the other nodes.
#
    d = np.zeros ( n )
    d[i-1] = 1.0

    for j in range ( 2, n + 1 ):
      for k in range ( j, n + 1 ):
        d[n+j-k-1] = ( d[n+j-k-1-1] - d[n+j-k-1] ) / ( x[n+1-k-1] - x[n+j-k-1] )

    for j in range ( 1, n ):
      for k in range ( 1, n - j + 1 ):
        d[n-k-1] = d[n-k-1] - x[n-k-j] * d[n-k]
#
#  Evaluate the antiderivative of the polynomial at the endpoints.
#
    yvala = d[n-1] / float ( n )
    for j in range ( n - 1, 0, -1 ):
      yvala = yvala * x_min + d[j-1] / float ( j )
    yvala = yvala * x_min

    yvalb = d[n-1] / float ( n )
    for j in range ( n - 1, 0, -1 ):
      yvalb = yvalb * x_max + d[j-1] / float ( j )
    yvalb = yvalb * x_max

    w[i-1] = yvalb - yvala

  return w

def nc_compute_weights_test ( ):

#*****************************************************************************80
#
## nc_compute_weights_test() tests nc_compute_weights().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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

  print ( '' )
  print ( 'nc_compute_weights_test():' )
  print ( '  NC_COMPUTE_WEIGHTS computes weights for' )
  print ( '  a Newton-Cotes quadrature rule' )
  print ( '' )
  print ( '  Index       X             W' )

  x_min = 0.0
  x_max = 1.0

  for n in range ( 1, 11 ):

    x = np.linspace ( x_min, x_max, n )

    w = nc_compute_weights ( n, x_min, x_max, x )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def ncc_set ( n ):

#*****************************************************************************80
#
## ncc_set() sets abscissas and weights for closed Newton-Cotes quadrature.
#
#  Discussion:
#
#    The closed Newton-Cotes rules use equally spaced abscissas, and
#    hence may be used with tabulated function data.
#
#    The rules are called "closed" because they include the endpoints.
#    As a favor, we include an order 1 rule, the midpoint rule, even
#    though this does not satisfy the requirement that the endpoints
#    be included.
#
#    The higher order rules involve negative weights.  These can produce
#    loss of accuracy due to the subtraction of large, nearly equal quantities.
#
#    N = 1 is the midpoint rule (and is not really an NCC rule.)
#    N = 2 is the trapezoidal rule.
#    N = 3 is Simpson's rule.
#    N = 4 is Simpson's 3/8 rule.
#    N = 5 is Bode's rule.
#
#    The Kopal reference for N = 12 lists
#             15494566.0 / 43545600.0D+00
#    but this results in a set of coeffients that don't add up to 2.
#    The correct value is
#             15493566.0 / 43545600.0.
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N )  (I) * F (  (I) )
#
#    In Mathematica, the Newton-Cotes closed weights
#    can be computed by:
#
#      Needs["NumericalDifferentialEquationAnalysis`"]
#      NewtonCotesWeights [ n, -1, 1, QuadratureType -> Closed ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2015
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
#    Johnson,
#    Quarterly Journal of Mathematics,
#    Volume 46, Number 52, 1915.
#
#    Zdenek Kopal,
#    Numerical Analysis,
#    John Wiley, 1955,
#    LC: QA297.K6.
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
#    integer N, the order.
#    N must be between 1 and 21.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):
#
#  2
#
    x = np.array ( [ \
           0.00000000000000000000 ] )

    w = np.array ( [ \
           2.00000000000000000000 ] )

  elif ( n == 2 ):
#
#  1
#  1
#
    x = np.array ( [ \
           -1.00000000000000000000, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
           1.00000000000000000000, \
           1.00000000000000000000 ] )

  elif ( n == 3 ):
#
#  1 / 3
#  4 / 3
#  1 / 3
#
    x = np.array ( [ \
           -1.00000000000000000000, \
            0.00000000000000000000, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
           0.33333333333333333333, \
           1.33333333333333333333, \
           0.33333333333333333333 ] )

  elif ( n == 4 ):
#
#  1 / 4
#  3 / 4
#  3 / 4
#  1 / 4
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.33333333333333333333, \
            0.33333333333333333333, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
           0.25000000000000000000, \
           0.75000000000000000000, \
           0.75000000000000000000, \
           0.25000000000000000000 ] )

  elif ( n == 5 ):
#
#   7 / 45
#  32 / 45
#  12 / 45
#  32 / 45
#   7 / 45
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.50000000000000000000, \
            0.00000000000000000000, \
            0.50000000000000000000, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
           0.15555555555555555556, \
           0.71111111111111111111, \
           0.26666666666666666667, \
           0.71111111111111111111, \
           0.15555555555555555556 ] )

  elif ( n == 6 ):
#
#  19 / 144
#  75 / 144
#  50 / 144
#  50 / 144
#  75 / 144
#  19 / 144
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.60000000000000000000, \
           -0.20000000000000000000, \
            0.20000000000000000000, \
            0.60000000000000000000, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
           0.13194444444444444444, \
           0.52083333333333333333, \
           0.34722222222222222222, \
           0.34722222222222222222, \
           0.52083333333333333333, \
           0.13194444444444444444 ] )

  elif ( n == 7 ):
#
#   41 / 420
#  216 / 420
#   27 / 420
#  272 / 420
#   27 / 420
#  216 / 420
#   41 / 420
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.66666666666666666667, \
           -0.33333333333333333333, \
            0.00000000000000000000, \
            0.33333333333333333333, \
            0.66666666666666666667, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
           0.097619047619047619048, \
           0.51428571428571428571, \
           0.064285714285714285714, \
           0.64761904761904761905, \
           0.064285714285714285714, \
           0.51428571428571428571, \
           0.097619047619047619048 ] )

  elif ( n == 8 ):
#
#   751 / 8640
#  3577 / 8640
#  1323 / 8640
#  2989 / 8640
#  2989 / 8640
#  1323 / 8640
#  3577 / 8640
#   751 / 8640
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.71428571428571428571, \
           -0.42857142857142857143, \
           -0.14285714285714285714, \
            0.14285714285714285714, \
            0.42857142857142857143, \
            0.71428571428571428571, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
           0.086921296296296296296, \
           0.41400462962962962963, \
           0.15312500000000000000, \
           0.34594907407407407407, \
           0.34594907407407407407, \
           0.15312500000000000000, \
           0.41400462962962962963, \
           0.086921296296296296296 ] )

  elif ( n == 9 ):
#
#    989 / 14175
#   5888 / 14175
#   -928 / 14175
#  10496 / 14175
#  -4540 / 14175
#  10496 / 14175
#   -928 / 14175
#   5888 / 14175
#    989 / 14175
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.75000000000000000000, \
           -0.50000000000000000000, \
           -0.25000000000000000000, \
            0.00000000000000000000, \
            0.25000000000000000000, \
            0.50000000000000000000, \
            0.75000000000000000000, \
            1.00000000000000000000 ])

    w = np.array ( [ \
            0.069770723104056437390, \
            0.41537918871252204586, \
           -0.065467372134038800705, \
            0.74045855379188712522, \
           -0.32028218694885361552, \
            0.74045855379188712522, \
           -0.065467372134038800705, \
            0.41537918871252204586, \
            0.069770723104056437390 ] )

  elif ( n == 10 ):
#
#   2857 / 44800
#  15741 / 44800
#   1080 / 44800
#  19344 / 44800
#   5778 / 44800
#   5778 / 44800
#  19344 / 44800
#   1080 / 44800
#  15741 / 44800
#   2857 / 44800
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.77777777777777777778, \
           -0.55555555555555555556, \
           -0.33333333333333333333, \
           -0.11111111111111111111, \
            0.11111111111111111111, \
            0.33333333333333333333, \
            0.55555555555555555556, \
            0.77777777777777777778, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
            0.063772321428571428571, \
            0.35136160714285714286, \
            0.024107142857142857143, \
            0.43178571428571428571, \
            0.12897321428571428571, \
            0.12897321428571428571, \
            0.43178571428571428571, \
            0.024107142857142857143, \
            0.35136160714285714286, \
            0.063772321428571428571 ] )

  elif ( n == 11 ):
#
#     16067 / 299376
#    106300 / 299376
#   - 48525 / 299376
#    272400 / 299376
#  - 260550 / 299376
#    427368 / 299376
#  - 260550 / 299376
#    272400 / 299376
#   - 48525 / 299376
#    106300 / 299376
#     16067 / 299376
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.80000000000000000000, \
           -0.60000000000000000000, \
           -0.40000000000000000000, \
           -0.20000000000000000000, \
            0.00000000000000000000, \
            0.20000000000000000000, \
            0.40000000000000000000, \
            0.60000000000000000000, \
            0.80000000000000000000, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
            0.053668296723852279408, \
            0.35507188284966062744, \
           -0.16208714125380792047, \
            0.90989257655924322591, \
           -0.87031024531024531025, \
            1.4275292608625941959, \
           -0.87031024531024531025, \
            0.90989257655924322591, \
           -0.16208714125380792047, \
            0.35507188284966062744, \
            0.053668296723852279408 ] )

  elif ( n == 12 ):
#
#     2171465 / 43545600
#    13486539 / 43545600
#   - 3237113 / 43545600
#    25226685 / 43545600
#   - 9595542 / 43545600
#    15493566 / 43545600
#    15493566 / 43545600
#   - 9595542 / 43545600
#    25226685 / 43545600
#   - 3237113 / 43545600
#    13486539 / 43545600
#     2171465 / 43545600
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.81818181818181818182, \
           -0.63636363636363636364, \
           -0.45454545454545454545, \
           -0.27272727272727272727, \
           -0.090909090909090909091, \
            0.090909090909090909091, \
            0.27272727272727272727, \
            0.45454545454545454545, \
            0.63636363636363636364, \
            0.81818181818181818182, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
             0.049866461823927101705, \
             0.30971071704144620811, \
            -0.074338463587595532040, \
             0.57931650958994708995, \
            -0.22035617835097001764, \
             0.35580095348324514991, \
             0.35580095348324514991, \
            -0.22035617835097001764, \
             0.57931650958994708995, \
            -0.074338463587595532040, \
             0.30971071704144620811, \
             0.049866461823927101705 ] )

  elif ( n == 13 ):
#
#      1364651 / 31531500
#      9903168 / 31531500
#    - 7587864 / 31531500
#     35725120 / 31531500
#   - 51491295 / 31531500
#     87516288 / 31531500
#   - 87797136 / 31531500
#     87516288 / 31531500
#   - 51491295 / 31531500
#     35725120 / 31531500
#    - 7587864 / 31531500
#      9903168 / 31531500
#      1364651 / 31531500
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.83333333333333333333, \
           -0.66666666666666666667, \
           -0.50000000000000000000, \
           -0.33333333333333333333, \
           -0.16666666666666666667, \
            0.00000000000000000000, \
            0.16666666666666666667, \
            0.33333333333333333333, \
            0.50000000000000000000, \
            0.66666666666666666667, \
            0.83333333333333333333, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
             0.043278974993260707546, \
             0.31407221350078492936, \
            -0.24064392750107035821, \
             1.1329977958549387121, \
            -1.6330112744398458684, \
             2.7755193378050520908, \
            -2.7844262404262404262, \
             2.7755193378050520908, \
            -1.6330112744398458684, \
             1.1329977958549387121, \
            -0.24064392750107035821, \
             0.31407221350078492936, \
             0.043278974993260707546 ] )

  elif ( n == 14 ):
#
#      6137698213 / 150885504000
#     42194238652 / 150885504000
#   - 23361540993 / 150885504000
#    116778274403 / 150885504000
#  - 113219777650 / 150885504000
#    154424590209 / 150885504000
#   - 32067978834 / 150885504000
#   - 32067978834 / 150885504000
#    154424590209 / 150885504000
#  - 113219777650 / 150885504000
#    116778274403 / 150885504000
#   - 23361540993 / 150885504000
#     42194238652 / 150885504000
#      6137698213 / 150885504000
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.84615384615384615385, \
           -0.69230769230769230769, \
           -0.53846153846153846154, \
           -0.38461538461538461538, \
           -0.23076923076923076923, \
           -0.076923076923076923077, \
            0.076923076923076923077, \
            0.23076923076923076923, \
            0.38461538461538461538, \
            0.53846153846153846154, \
            0.69230769230769230769, \
            0.84615384615384615385, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
             0.040669438210247155353, \
             0.27975217053157074652, \
            -0.15542374057682837445, \
             0.77579230848776566369, \
            -0.75384763266423526013, \
             1.0273523591123107492, \
            -0.21429490310083068020, \
            -0.21429490310083068020, \
             1.0273523591123107492, \
            -0.75384763266423526013, \
             0.77579230848776566369, \
            -0.15542374057682837445, \
             0.27975217053157074652, \
             0.040669438210247155353 ] )

  elif ( n == 15 ):
#
#       90241897 / 2501928000
#      710986864 / 2501928000
#    - 770720657 / 2501928000
#     3501442784 / 2501928000
#   - 6625093363 / 2501928000
#    12630121616 / 2501928000
#  - 16802270373 / 2501928000
#    19534438464 / 2501928000
#  - 16802270373 / 2501928000
#    12630121616 / 2501928000
#   - 6625093363 / 2501928000
#     3501442784 / 2501928000
#    - 770720657 / 2501928000
#      710986864 / 2501928000
#       90241897 / 2501928000
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.85714285714285714286, \
           -0.71428571428571428571, \
           -0.57142857142857142857, \
           -0.42857142857142857143, \
           -0.28571428571428571429, \
           -0.14285714285714285714, \
            0.00000000000000000000, \
            0.14285714285714285714, \
            0.28571428571428571429, \
            0.42857142857142857143, \
            0.57142857142857142857, \
            0.71428571428571428571, \
            0.85714285714285714286, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
             0.036068942431596752584, \
             0.28417558938546592868, \
            -0.30805069410470645039, \
             1.3994978208805369299, \
            -2.6479952112930507992, \
             5.0481555088715582543, \
            -6.7157289790113864188, \
             7.8077540456799716059, \
            -6.7157289790113864188, \
             5.0481555088715582543, \
            -2.6479952112930507992, \
             1.3994978208805369299, \
            -0.30805069410470645039, \
             0.28417558938546592868, \
             0.036068942431596752584 ] )

  elif ( n == 16 ):
#
#     105930069 / 3099672576
#     796661595 / 3099672576
#   - 698808195 / 3099672576
#    3143332755 / 3099672576
#  - 4688522055 / 3099672576
#    7385654007 / 3099672576
#  - 6000998415 / 3099672576
#    3056422815 / 3099672576
#    3056422815 / 3099672576
#  - 6000998415 / 3099672576
#    7385654007 / 3099672576
#  - 4688522055 / 3099672576
#    3143332755 / 3099672576
#   - 698808195 / 3099672576
#     796661595 / 3099672576
#     105930069 / 3099672576
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.86666666666666666667, \
           -0.73333333333333333333, \
           -0.60000000000000000000, \
           -0.46666666666666666667, \
           -0.33333333333333333333, \
           -0.20000000000000000000, \
           -0.066666666666666666667, \
            0.066666666666666666667, \
            0.20000000000000000000, \
            0.33333333333333333333, \
            0.46666666666666666667, \
            0.60000000000000000000, \
            0.73333333333333333333, \
            0.86666666666666666667, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
             0.034174599543251887002, \
             0.25701475735481036820, \
            -0.22544581011901045383, \
             1.0140854164204471124, \
            -1.5125862296882804695, \
             2.3827206990135980091, \
            -1.9360104229924960952, \
             0.98604699046767964179, \
             0.98604699046767964179, \
            -1.9360104229924960952, \
             2.3827206990135980091, \
            -1.5125862296882804695, \
             1.0140854164204471124, \
            -0.22544581011901045383, \
             0.25701475735481036820, \
             0.034174599543251887002 ] )

  elif ( n == 17 ):
#
#       15043611773 / 488462349375
#      127626606592 / 488462349375
#    - 179731134720 / 488462349375
#      832211855360 / 488462349375
#   - 1929498607520 / 488462349375
#     4177588893696 / 488462349375
#   - 6806534407936 / 488462349375
#     9368875018240 / 488462349375
#  - 10234238972220 / 488462349375
#     9368875018240 / 488462349375
#   - 6806534407936 / 488462349375
#     4177588893696 / 488462349375
#   - 1929498607520 / 488462349375
#      832211855360 / 488462349375
#    - 179731134720 / 488462349375
#      127626606592 / 488462349375
#       15043611773 / 488462349375
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.87500000000000000000, \
           -0.75000000000000000000, \
           -0.62500000000000000000, \
           -0.50000000000000000000, \
           -0.37500000000000000000, \
           -0.25000000000000000000, \
           -0.12500000000000000000, \
            0.00000000000000000000, \
            0.12500000000000000000, \
            0.25000000000000000000, \
            0.37500000000000000000, \
            0.50000000000000000000, \
            0.62500000000000000000, \
            0.75000000000000000000, \
            0.87500000000000000000, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
              0.030797894233299012495, \
              0.26128238288028031086, \
             -0.36795289329867605622, \
              1.7037379778090086905, \
             -3.9501480717783930427, \
              8.5525299934402953388, \
            -13.934614237197880038, \
             19.180342211078732848, \
             -20.951950514333334128, \
             19.180342211078732848, \
            -13.934614237197880038, \
             8.5525299934402953388, \
             -3.9501480717783930427, \
              1.7037379778090086905, \
             -0.36795289329867605622, \
              0.26128238288028031086, \
              0.030797894233299012495 ] )

  elif ( n == 18 ):
#
#       55294720874657 / 1883051089920000
#      450185515446285 / 1883051089920000
#    - 542023437008852 / 1883051089920000
#     2428636525764260 / 1883051089920000
#   - 4768916800123440 / 1883051089920000
#     8855416648684984 / 1883051089920000
#  - 10905371859796660 / 1883051089920000
#    10069615750132836 / 1883051089920000
#   - 3759785974054070 / 1883051089920000
#   - 3759785974054070 / 1883051089920000
#    10069615750132836 / 1883051089920000
#  - 10905371859796660 / 1883051089920000
#     8855416648684984 / 1883051089920000
#   - 4768916800123440 / 1883051089920000
#     2428636525764260 / 1883051089920000
#    - 542023437008852 / 1883051089920000
#      450185515446285 / 1883051089920000
#       55294720874657 / 1883051089920000
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.88235294117647058824, \
           -0.76470588235294117647, \
           -0.64705882352941176471, \
           -0.52941176470588235294, \
           -0.41176470588235294118, \
           -0.29411764705882352941, \
           -0.17647058823529411765, \
           -0.058823529411764705882, \
            0.058823529411764705882, \
            0.17647058823529411765, \
            0.29411764705882352941, \
            0.41176470588235294118, \
            0.52941176470588235294, \
            0.64705882352941176471, \
            0.76470588235294117647, \
            0.88235294117647058824, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
             0.029364429446790078519, \
             0.23907238516051669677, \
            -0.28784319231183443641, \
             1.2897348026109258587, \
            -2.5325477495812627261, \
             4.7026959045817496499, \
            -5.7913308450170443690, \
             5.3475000248456540826, \
            -1.9966457597354948350, \
            -1.9966457597354948350, \
             5.3475000248456540826, \
            -5.7913308450170443690, \
             4.7026959045817496499, \
            -2.5325477495812627261, \
             1.2897348026109258587, \
            -0.28784319231183443641, \
             0.23907238516051669677, \
             0.029364429446790078519 ] )

  elif ( n == 19 ):
#
#       203732352169 / 7604556960000
#      1848730221900 / 7604556960000
#    - 3212744374395 / 7604556960000
#     15529830312096 / 7604556960000
#   - 42368630685840 / 7604556960000
#    103680563465808 / 7604556960000
#  - 198648429867720 / 7604556960000
#    319035784479840 / 7604556960000
#  - 419127951114198 / 7604556960000
#    461327344340680 / 7604556960000
#  - 419127951114198 / 7604556960000
#    319035784479840 / 7604556960000
#  - 198648429867720 / 7604556960000
#    103680563465808 / 7604556960000
#   - 42368630685840 / 7604556960000
#     15529830312096 / 7604556960000
#    - 3212744374395 / 7604556960000
#      1848730221900 / 7604556960000
#       203732352169 / 7604556960000
#
    x = np.array ( [ \
           -1.00000000000000000000, \
           -0.88888888888888888889, \
           -0.77777777777777777778, \
           -0.66666666666666666667, \
           -0.55555555555555555556, \
           -0.44444444444444444444, \
           -0.33333333333333333333, \
           -0.22222222222222222222, \
           -0.11111111111111111111, \
            0.00000000000000000000, \
            0.11111111111111111111, \
            0.22222222222222222222, \
            0.33333333333333333333, \
            0.44444444444444444444, \
            0.55555555555555555556, \
            0.66666666666666666667, \
            0.77777777777777777778, \
            0.88888888888888888889, \
            1.00000000000000000000 ] )

    w = np.array ( [ \
              0.026790824664820447344, \
              0.24310820888374278151, \
             -0.42247620621346493274, \
              2.0421742376029227612, \
             -5.5714791681749728126, \
             13.634004454324976218, \
            -26.122288374274995239, \
             41.953237533490708445, \
            -55.115367445968607749, \
             60.664591871329740161, \
            -55.115367445968607749, \
             41.953237533490708445, \
            -26.122288374274995239, \
             13.634004454324976218, \
             -5.5714791681749728126, \
              2.0421742376029227612, \
             -0.42247620621346493274, \
              0.24310820888374278151, \
              0.026790824664820447344 ] )

  elif ( n == 20 ):
#
#       69028763155644023 / 2688996956405760000
#      603652082270808125 / 2688996956405760000
#    - 926840515700222955 / 2688996956405760000
#     4301581538450500095 / 2688996956405760000
#  - 10343692234243192788 / 2688996956405760000
#    22336420328479961316 / 2688996956405760000
#  - 35331888421114781580 / 2688996956405760000
#    43920768370565135580 / 2688996956405760000
#  - 37088370261379851390 / 2688996956405760000
#    15148337305921759574 / 2688996956405760000
#    15148337305921759574 / 2688996956405760000
#  - 37088370261379851390 / 2688996956405760000
#    43920768370565135580 / 2688996956405760000
#  - 35331888421114781580 / 2688996956405760000
#    22336420328479961316 / 2688996956405760000
#  - 10343692234243192788 / 2688996956405760000
#     4301581538450500095 / 2688996956405760000
#    - 926840515700222955 / 2688996956405760000
#      603652082270808125 / 2688996956405760000
#       69028763155644023 / 2688996956405760000
#
    x = np.array ( [ \
            -1.00000000000000000000, \
            -0.89473684210526315789, \
            -0.78947368421052631579, \
            -0.68421052631578947368, \
            -0.57894736842105263158, \
            -0.47368421052631578947, \
            -0.36842105263157894737, \
            -0.26315789473684210526, \
            -0.15789473684210526316, \
            -0.052631578947368421053, \
             0.052631578947368421053, \
             0.15789473684210526316, \
             0.26315789473684210526, \
             0.36842105263157894737, \
             0.47368421052631578947, \
             0.57894736842105263158, \
             0.68421052631578947368, \
             0.78947368421052631579, \
             0.89473684210526315789, \
             1.00000000000000000000 ] )

    w = np.array ( [ \
              0.025670822345560078100, \
              0.22448968595251886556, \
             -0.34467890099030890987, \
              1.5996974366978074270, \
             -3.8466730910952978835, \
              8.3065993344729824120, \
            -13.139430424771119113, \
             16.333513604742678295, \
            -13.792641220001198577, \
             5.6334527526463774045, \
             5.6334527526463774045, \
            -13.792641220001198577, \
             16.333513604742678295, \
            -13.139430424771119113, \
              8.3065993344729824120, \
             -3.8466730910952978835, \
              1.5996974366978074270, \
             -0.34467890099030890987, \
              0.22448968595251886556, \
              0.025670822345560078100 ] )

  elif ( n == 21 ):

    x = np.array ( [ \
            -1.00000000000000000000, \
            -0.90000000000000000000, \
            -0.80000000000000000000, \
            -0.70000000000000000000, \
            -0.60000000000000000000, \
            -0.50000000000000000000, \
            -0.40000000000000000000, \
            -0.30000000000000000000, \
            -0.20000000000000000000, \
            -0.10000000000000000000, \
             0.00000000000000000000, \
             0.10000000000000000000, \
             0.20000000000000000000, \
             0.30000000000000000000, \
             0.40000000000000000000, \
             0.50000000000000000000, \
             0.60000000000000000000, \
             0.70000000000000000000, \
             0.80000000000000000000, \
             0.90000000000000000000, \
             1.00000000000000000000 ] )

    w = np.array ( [ \
               0.023650546498063206389, \
               0.22827543528921394997, \
              -0.47295674102285392846, \
               2.4123737869637513288, \
              -7.5420634534306609355, \
              20.673596439879602287, \
             -45.417631687959024596, \
              83.656114844387109207, \
            -128.15055898030800930, \
             165.59456694494570344, \
            -180.01073427048578932, \
             165.59456694494570344, \
            -128.15055898030800930, \
              83.656114844387109207, \
             -45.417631687959024596, \
              20.673596439879602287, \
              -7.5420634534306609355, \
               2.4123737869637513288, \
              -0.47295674102285392846, \
               0.22827543528921394997, \
               0.023650546498063206389 ] )

  else:

    print ( '' )
    print ( 'NCC_SET(): Fatal error!' )
    print ( '  Illegal value of N   %d' % ( n ) )
    print ( '  Legal values are 1 through 21.' )
    raise Exception ( 'NCC_SET(): Fatal error!' )

  return x, w

def ncc_set_test ( ):

#*****************************************************************************80
#
## ncc_set_test() tests ncc_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'NCC_SET_test():' )
  print ( '  NCC_SET sets up a Newton-Cotes Closed quadrature rule' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = ncc_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %12g  %12g' % ( i, x[i], w[i] ) )

  return

def nco_compute ( n ):

#*****************************************************************************80
#
## nco_compute() computes a Newton-Cotes Open quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= +1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) ).
#
#    For the OPEN rule, the abscissas do not include the end points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  x_min = -1.0
  x_max =  1.0
  x = np.linspace ( x_min, x_max, n )

  w = nc_compute_weights ( n, x_min, x_max, x )

  return x, w

def nco_compute_test ( ):

#*****************************************************************************80
#
## nco_compute_test() tests nco_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'NCO_COMPUTE_test():' )
  print ( '  NCO_COMPUTE computes a Newton-Cotes Open quadrature rule' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = nco_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def ncoh_compute ( n ):

#*****************************************************************************80
#
## ncoh_compute() computes a Newton-Cotes "open half" quadrature rule.
#
#  Discussion:
#
#    The input value N is used to define N equal subintervals of [-1,+1].
#    The I-th abscissa is the center of the I-th subinterval.
#
#    The integral:
#
#      Integral ( X_MIN <= X <= X_MAX ) F(X) dx
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  x = np.zeros ( n )

  x_min = -1.0
  x_max =  1.0

  for i in range ( 0, n ):
    x[i] = ( float ( 2 * n - 2 * i - 1 ) * x_min   \
           + float (         2 * i + 1 ) * x_max ) \
           / float ( 2 * n             )

  w = nc_compute_weights ( n, x_min, x_max, x )

  return x, w

def ncoh_compute_test ( ):

#*****************************************************************************80
#
## ncoh_compute_test() tests ncoh_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'NCOH_COMPUTE_test():' )
  print ( '  NCOH_COMPUTE computes a Newton-Cotes Open Half quadrature rule' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = ncoh_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def ncoh_set ( n ):

#*****************************************************************************80
#
## ncoh_set() sets abscissas and weights for Newton-Cotes "open half" quadrature.
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
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N, the order.
#    1 <= N <= 17.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

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
    print ( 'NCOH_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 to 17.' )
    raise Exception ( 'NCOH_SET(): Fatal error!' )
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
## ncoh_set_test() tests ncoh_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'NCOH_SET_test():' )
  print ( '  NCOH_SET sets up a Newton-Cotes Open half quadrature rule' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = ncoh_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

  return

def nco_set ( n ):

#*****************************************************************************80
#
## nco_set() sets abscissas and weights for open Newton-Cotes quadrature.
#
#  Discussion:
#
#    The open Newton-Cotes rules use equally spaced abscissas, and
#    hence may be used with equally spaced data.
#
#    The rules are called "open" because they do not include the interval
#    endpoints.
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
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Abramowitz and Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#    Daniel Zwillinger, editor,
#    Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer N, the order.
#    N must be between 1 and 10.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  x = np.zeros ( n )
  w = np.zeros ( n )

  if ( n == 1 ):

    w = np.array ( [ \
            2.0 ] )

  elif ( n == 2 ):

    w = np.array ( [ \
           1.0, \
           1.0 ] )

  elif ( n == 3 ):

    d = 3.0

    w = np.array ( [ \
             4.0 / d, \
           - 2.0 / d, \
             4.0 / d ] )

  elif ( n == 4 ):

    d = 12.0

    w = np.array ( [ \
           11.0 / d, \
            1.0 / d, \
            1.0 / d, \
           11.0 / d ] )

  elif ( n == 5 ):

    d = 10.0

    w = np.array ( [ \
             11.0 / d, \
           - 14.0 / d, \
             26.0 / d, \
           - 14.0 / d, \
             11.0 / d ] )

  elif ( n == 6 ):

    d = 1440.0

    w = np.array ( [ \
            1222.0 / d, \
           - 906.0 / d, \
            1124.0 / d, \
            1124.0 / d, \
           - 906.0 / d, \
            1222.0 / d ] )

  elif ( n == 7 ):

    d = 945.0

    w = np.array ( [ \
              920.0 / d, \
           - 1908.0 / d, \
             4392.0 / d, \
           - 4918.0 / d, \
             4392.0 / d, \
           - 1908.0 / d, \
              920.0 / d ] )

  elif ( n == 8 ):

    d = 40320.0

    w = np.array ( [ \
             32166.0 / d, \
           - 50454.0 / d, \
             89406.0 / d, \
           - 30798.0 / d, \
           - 30798.0 / d, \
             89406.0 / d, \
           - 50454.0 / d, \
             32166.0 / d ] )

  elif ( n == 9 ):

    d = 4536.0

    w = np.array ( [ \
              4045.0 / d, \
           - 11690.0 / d, \
             33340.0 / d, \
           - 55070.0 / d, \
             67822.0 / d, \
           - 55070.0 / d, \
             33340.0 / d, \
           - 11690.0 / d, \
              4045.0 / d ] )

  elif ( n == 10 ):

    w = np.array ( [ \
              0.758508873456792, \
             -1.819664627425049, \
              4.319301146384676, \
             -4.708337742504753, \
              2.450192350088813, \
              2.450192350087711, \
             -4.708337742504625, \
              4.319301146384526, \
             -1.819664627425028, \
              0.758508873456790 ] )

  else:

    print ( '' )
    print ( 'NCO_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 and 10.' )
    raise Exception ( 'NCO_SET(): Fatal error!' )
#
#  Set the abscissas.
#
  for i in range ( 0, n ):
    x[i] = float ( 2 * i - n + 1 ) / float ( n + 1 )

  return x, w

def nco_set_test ( ):

#*****************************************************************************80
#
## nco_set_test() tests nco_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'NCO_SET_test():' )
  print ( '  NCO_SET sets up a Newton-Cotes Open quadrature rule' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = nco_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %12g  %12g' % ( i, x[i], w[i] ) )

  return

def patterson_set ( n ):

#*****************************************************************************80
#
## patterson_set() sets abscissas and weights for Gauss-Patterson quadrature.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    The zeroth rule, of order 1, is the standard Gauss-Legendre rule.
#
#    The first rule, of order 3, is the standard Gauss-Legendre rule.
#
#    The second rule, of order 7, includes the abscissas of the previous
#    rule.
#
#    Rules are available of orders 1, 3, 7, 15, 31, 63, 127, 255, and 511.
#
#    These rules constitute a nested family.  The rules can integrate exactly
#    any polynomial of degree 1, 5, 11, 23, 47, 95, 191, 383 or 767, 
#    respectively.
#
#    The data for N = 511 was supplied by Dirk Laurie, and is derived
#    from a NAG Library function d01arf.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Prem Kythe, Michael Schaeferkotter,
#    Handbook of Computational Methods for Integration,
#    Chapman and Hall, 2004,
#    ISBN: 1-58488-428-2,
#    LC: QA299.3.K98.
#
#    NAG Library Documentation,
#    D01ARF,
#    The Numerical Algorithms Group.
#
#    Thomas Patterson,
#    The Optimal Addition of Points to Quadrature Formulae,
#    Mathematics of Computation,
#    Volume 22, Number 104, October 1968, pages 847-856.
#
#  Input:
#
#    integer N, the order.
#    N must be 1, 3, 7, 15, 31, 63, 127, 255 or 511.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
             0.0 ] )

    w = np.array ( [ \
           2.0 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
           -0.77459666924148337704, \
            0.0, \
            0.77459666924148337704 ] )

    w = np.array ( [ \
           0.555555555555555555556, \
           0.888888888888888888889, \
           0.555555555555555555556 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
           -0.96049126870802028342, \
           -0.77459666924148337704, \
           -0.43424374934680255800, \
            0.0, \
            0.43424374934680255800, \
            0.77459666924148337704, \
            0.96049126870802028342 ] )

    w = np.array ( [ \
           0.104656226026467265194, \
           0.268488089868333440729, \
           0.401397414775962222905, \
           0.450916538658474142345, \
           0.401397414775962222905, \
           0.268488089868333440729, \
           0.104656226026467265194 ] )

  elif ( n == 15 ):

    x = np.array ( [ \
            -0.99383196321275502221, \
            -0.96049126870802028342, \
            -0.88845923287225699889, \
            -0.77459666924148337704, \
            -0.62110294673722640294, \
            -0.43424374934680255800, \
            -0.22338668642896688163, \
             0.0, \
             0.22338668642896688163, \
             0.43424374934680255800, \
             0.62110294673722640294, \
             0.77459666924148337704, \
             0.88845923287225699889, \
             0.96049126870802028342, \
             0.99383196321275502221 ] )

    w = np.array ( [ \
            0.0170017196299402603390, \
            0.0516032829970797396969, \
            0.0929271953151245376859, \
            0.134415255243784220360, \
            0.171511909136391380787, \
            0.200628529376989021034, \
            0.219156858401587496404, \
            0.225510499798206687386, \
            0.219156858401587496404, \
            0.200628529376989021034, \
            0.171511909136391380787, \
            0.134415255243784220360, \
            0.0929271953151245376859, \
            0.0516032829970797396969, \
            0.0170017196299402603390 ] )

  elif ( n == 31 ):

    x = np.array ( [ \
            -0.99909812496766759766, \
            -0.99383196321275502221, \
            -0.98153114955374010687, \
            -0.96049126870802028342, \
            -0.92965485742974005667, \
            -0.88845923287225699889, \
            -0.83672593816886873550, \
            -0.77459666924148337704, \
            -0.70249620649152707861, \
            -0.62110294673722640294, \
            -0.53131974364437562397, \
            -0.43424374934680255800, \
            -0.33113539325797683309, \
            -0.22338668642896688163, \
            -0.11248894313318662575, \
             0.0, \
             0.11248894313318662575, \
             0.22338668642896688163, \
             0.33113539325797683309, \
             0.43424374934680255800, \
             0.53131974364437562397, \
             0.62110294673722640294, \
             0.70249620649152707861, \
             0.77459666924148337704, \
             0.83672593816886873550, \
             0.88845923287225699889, \
             0.92965485742974005667, \
             0.96049126870802028342, \
             0.98153114955374010687, \
             0.99383196321275502221, \
             0.99909812496766759766 ] )

    w = np.array ( [ \
            0.00254478079156187441540, \
            0.00843456573932110624631, \
            0.0164460498543878109338, \
            0.0258075980961766535646, \
            0.0359571033071293220968, \
            0.0464628932617579865414, \
            0.0569795094941233574122, \
            0.0672077542959907035404, \
            0.0768796204990035310427, \
            0.0857559200499903511542, \
            0.0936271099812644736167, \
            0.100314278611795578771, \
            0.105669893580234809744, \
            0.109578421055924638237, \
            0.111956873020953456880, \
            0.112755256720768691607, \
            0.111956873020953456880, \
            0.109578421055924638237, \
            0.105669893580234809744, \
            0.100314278611795578771, \
            0.0936271099812644736167, \
            0.0857559200499903511542, \
            0.0768796204990035310427, \
            0.0672077542959907035404, \
            0.0569795094941233574122, \
            0.0464628932617579865414, \
            0.0359571033071293220968, \
            0.0258075980961766535646, \
            0.0164460498543878109338, \
            0.00843456573932110624631, \
            0.00254478079156187441540 ] )

  elif ( n == 63 ):

    x = np.array ( [ \
            -0.99987288812035761194, \
            -0.99909812496766759766, \
            -0.99720625937222195908, \
            -0.99383196321275502221, \
            -0.98868475754742947994, \
            -0.98153114955374010687, \
            -0.97218287474858179658, \
            -0.96049126870802028342, \
            -0.94634285837340290515, \
            -0.92965485742974005667, \
            -0.91037115695700429250, \
            -0.88845923287225699889, \
            -0.86390793819369047715, \
            -0.83672593816886873550, \
            -0.80694053195021761186, \
            -0.77459666924148337704, \
            -0.73975604435269475868, \
            -0.70249620649152707861, \
            -0.66290966002478059546, \
            -0.62110294673722640294, \
            -0.57719571005204581484, \
            -0.53131974364437562397, \
            -0.48361802694584102756, \
            -0.43424374934680255800, \
            -0.38335932419873034692, \
            -0.33113539325797683309, \
            -0.27774982202182431507, \
            -0.22338668642896688163, \
            -0.16823525155220746498, \
            -0.11248894313318662575, \
            -0.056344313046592789972, \
             0.0, \
             0.056344313046592789972, \
             0.11248894313318662575, \
             0.16823525155220746498, \
             0.22338668642896688163, \
             0.27774982202182431507, \
             0.33113539325797683309, \
             0.38335932419873034692, \
             0.43424374934680255800, \
             0.48361802694584102756, \
             0.53131974364437562397, \
             0.57719571005204581484, \
             0.62110294673722640294, \
             0.66290966002478059546, \
             0.70249620649152707861, \
             0.73975604435269475868, \
             0.77459666924148337704, \
             0.80694053195021761186, \
             0.83672593816886873550, \
             0.86390793819369047715, \
             0.88845923287225699889, \
             0.91037115695700429250, \
             0.92965485742974005667, \
             0.94634285837340290515, \
             0.96049126870802028342, \
             0.97218287474858179658, \
             0.98153114955374010687, \
             0.98868475754742947994, \
             0.99383196321275502221, \
             0.99720625937222195908, \
             0.99909812496766759766, \
             0.99987288812035761194 ] )

    w = np.array ( [ \
            0.000363221481845530659694, \
            0.00126515655623006801137, \
            0.00257904979468568827243, \
            0.00421763044155885483908, \
            0.00611550682211724633968, \
            0.00822300795723592966926, \
            0.0104982469096213218983, \
            0.0129038001003512656260, \
            0.0154067504665594978021, \
            0.0179785515681282703329, \
            0.0205942339159127111492, \
            0.0232314466399102694433, \
            0.0258696793272147469108, \
            0.0284897547458335486125, \
            0.0310735511116879648799, \
            0.0336038771482077305417, \
            0.0360644327807825726401, \
            0.0384398102494555320386, \
            0.0407155101169443189339, \
            0.0428779600250077344929, \
            0.0449145316536321974143, \
            0.0468135549906280124026, \
            0.0485643304066731987159, \
            0.0501571393058995374137, \
            0.0515832539520484587768, \
            0.0528349467901165198621, \
            0.0539054993352660639269, \
            0.0547892105279628650322, \
            0.0554814043565593639878, \
            0.0559784365104763194076, \
            0.0562776998312543012726, \
            0.0563776283603847173877, \
            0.0562776998312543012726, \
            0.0559784365104763194076, \
            0.0554814043565593639878, \
            0.0547892105279628650322, \
            0.0539054993352660639269, \
            0.0528349467901165198621, \
            0.0515832539520484587768, \
            0.0501571393058995374137, \
            0.0485643304066731987159, \
            0.0468135549906280124026, \
            0.0449145316536321974143, \
            0.0428779600250077344929, \
            0.0407155101169443189339, \
            0.0384398102494555320386, \
            0.0360644327807825726401, \
            0.0336038771482077305417, \
            0.0310735511116879648799, \
            0.0284897547458335486125, \
            0.0258696793272147469108, \
            0.0232314466399102694433, \
            0.0205942339159127111492, \
            0.0179785515681282703329, \
            0.0154067504665594978021, \
            0.0129038001003512656260, \
            0.0104982469096213218983, \
            0.00822300795723592966926, \
            0.00611550682211724633968, \
            0.00421763044155885483908, \
            0.00257904979468568827243, \
            0.00126515655623006801137, \
            0.000363221481845530659694 ] )

  elif ( n == 127 ):

    x = np.array ( [ \
             -0.99998243035489159858, \
             -0.99987288812035761194, \
             -0.99959879967191068325, \
             -0.99909812496766759766, \
             -0.99831663531840739253, \
             -0.99720625937222195908, \
             -0.99572410469840718851, \
             -0.99383196321275502221, \
             -0.99149572117810613240, \
             -0.98868475754742947994, \
             -0.98537149959852037111, \
             -0.98153114955374010687, \
             -0.97714151463970571416, \
             -0.97218287474858179658, \
             -0.96663785155841656709, \
             -0.96049126870802028342, \
             -0.95373000642576113641, \
             -0.94634285837340290515, \
             -0.93832039777959288365, \
             -0.92965485742974005667, \
             -0.92034002547001242073, \
             -0.91037115695700429250, \
             -0.89974489977694003664, \
             -0.88845923287225699889, \
             -0.87651341448470526974, \
             -0.86390793819369047715, \
             -0.85064449476835027976, \
             -0.83672593816886873550, \
             -0.82215625436498040737, \
             -0.80694053195021761186, \
             -0.79108493379984836143, \
             -0.77459666924148337704, \
             -0.75748396638051363793, \
             -0.73975604435269475868, \
             -0.72142308537009891548, \
             -0.70249620649152707861, \
             -0.68298743109107922809, \
             -0.66290966002478059546, \
             -0.64227664250975951377, \
             -0.62110294673722640294, \
             -0.59940393024224289297, \
             -0.57719571005204581484, \
             -0.55449513263193254887, \
             -0.53131974364437562397, \
             -0.50768775753371660215, \
             -0.48361802694584102756, \
             -0.45913001198983233287, \
             -0.43424374934680255800, \
             -0.40897982122988867241, \
             -0.38335932419873034692, \
             -0.35740383783153215238, \
             -0.33113539325797683309, \
             -0.30457644155671404334, \
             -0.27774982202182431507, \
             -0.25067873030348317661, \
             -0.22338668642896688163, \
             -0.19589750271110015392, \
             -0.16823525155220746498, \
             -0.14042423315256017459, \
             -0.11248894313318662575, \
             -0.084454040083710883710, \
             -0.056344313046592789972, \
             -0.028184648949745694339, \
              0.0, \
              0.028184648949745694339, \
              0.056344313046592789972, \
              0.084454040083710883710, \
              0.11248894313318662575, \
              0.14042423315256017459, \
              0.16823525155220746498, \
              0.19589750271110015392, \
              0.22338668642896688163, \
              0.25067873030348317661, \
              0.27774982202182431507, \
              0.30457644155671404334, \
              0.33113539325797683309, \
              0.35740383783153215238, \
              0.38335932419873034692, \
              0.40897982122988867241, \
              0.43424374934680255800, \
              0.45913001198983233287, \
              0.48361802694584102756, \
              0.50768775753371660215, \
              0.53131974364437562397, \
              0.55449513263193254887, \
              0.57719571005204581484, \
              0.59940393024224289297, \
              0.62110294673722640294, \
              0.64227664250975951377, \
              0.66290966002478059546, \
              0.68298743109107922809, \
              0.70249620649152707861, \
              0.72142308537009891548, \
              0.73975604435269475868, \
              0.75748396638051363793, \
              0.77459666924148337704, \
              0.79108493379984836143, \
              0.80694053195021761186, \
              0.82215625436498040737, \
              0.83672593816886873550, \
              0.85064449476835027976, \
              0.86390793819369047715, \
              0.87651341448470526974, \
              0.88845923287225699889, \
              0.89974489977694003664, \
              0.91037115695700429250, \
              0.92034002547001242073, \
              0.92965485742974005667, \
              0.93832039777959288365, \
              0.94634285837340290515, \
              0.95373000642576113641, \
              0.96049126870802028342, \
              0.96663785155841656709, \
              0.97218287474858179658, \
              0.97714151463970571416, \
              0.98153114955374010687, \
              0.98537149959852037111, \
              0.98868475754742947994, \
              0.99149572117810613240, \
              0.99383196321275502221, \
              0.99572410469840718851, \
              0.99720625937222195908, \
              0.99831663531840739253, \
              0.99909812496766759766, \
              0.99959879967191068325, \
              0.99987288812035761194, \
              0.99998243035489159858 ] )

    w = np.array ( [ \
             0.0000505360952078625176247, \
             0.000180739564445388357820, \
             0.000377746646326984660274, \
             0.000632607319362633544219, \
             0.000938369848542381500794, \
             0.00128952408261041739210, \
             0.00168114286542146990631, \
             0.00210881524572663287933, \
             0.00256876494379402037313, \
             0.00305775341017553113613, \
             0.00357289278351729964938, \
             0.00411150397865469304717, \
             0.00467105037211432174741, \
             0.00524912345480885912513, \
             0.00584344987583563950756, \
             0.00645190005017573692280, \
             0.00707248999543355546805, \
             0.00770337523327974184817, \
             0.00834283875396815770558, \
             0.00898927578406413572328, \
             0.00964117772970253669530, \
             0.0102971169579563555237, \
             0.0109557333878379016480, \
             0.0116157233199551347270, \
             0.0122758305600827700870, \
             0.0129348396636073734547, \
             0.0135915710097655467896, \
             0.0142448773729167743063, \
             0.0148936416648151820348, \
             0.0155367755558439824399, \
             0.0161732187295777199419, \
             0.0168019385741038652709, \
             0.0174219301594641737472, \
             0.0180322163903912863201, \
             0.0186318482561387901863, \
             0.0192199051247277660193, \
             0.0197954950480974994880, \
             0.0203577550584721594669, \
             0.0209058514458120238522, \
             0.0214389800125038672465, \
             0.0219563663053178249393, \
             0.0224572658268160987071, \
             0.0229409642293877487608, \
             0.0234067774953140062013, \
             0.0238540521060385400804, \
             0.0242821652033365993580, \
             0.0246905247444876769091, \
             0.0250785696529497687068, \
             0.0254457699654647658126, \
             0.0257916269760242293884, \
             0.0261156733767060976805, \
             0.0264174733950582599310, \
             0.0266966229274503599062, \
             0.0269527496676330319634, \
             0.0271855132296247918192, \
             0.0273946052639814325161, \
             0.0275797495664818730349, \
             0.0277407021782796819939, \
             0.0278772514766137016085, \
             0.0279892182552381597038, \
             0.0280764557938172466068, \
             0.0281388499156271506363, \
             0.0281763190330166021307, \
             0.0281888141801923586938, \
             0.0281763190330166021307, \
             0.0281388499156271506363, \
             0.0280764557938172466068, \
             0.0279892182552381597038, \
             0.0278772514766137016085, \
             0.0277407021782796819939, \
             0.0275797495664818730349, \
             0.0273946052639814325161, \
             0.0271855132296247918192, \
             0.0269527496676330319634, \
             0.0266966229274503599062, \
             0.0264174733950582599310, \
             0.0261156733767060976805, \
             0.0257916269760242293884, \
             0.0254457699654647658126, \
             0.0250785696529497687068, \
             0.0246905247444876769091, \
             0.0242821652033365993580, \
             0.0238540521060385400804, \
             0.0234067774953140062013, \
             0.0229409642293877487608, \
             0.0224572658268160987071, \
             0.0219563663053178249393, \
             0.0214389800125038672465, \
             0.0209058514458120238522, \
             0.0203577550584721594669, \
             0.0197954950480974994880, \
             0.0192199051247277660193, \
             0.0186318482561387901863, \
             0.0180322163903912863201, \
             0.0174219301594641737472, \
             0.0168019385741038652709, \
             0.0161732187295777199419, \
             0.0155367755558439824399, \
             0.0148936416648151820348, \
             0.0142448773729167743063, \
             0.0135915710097655467896, \
             0.0129348396636073734547, \
             0.0122758305600827700870, \
             0.0116157233199551347270, \
             0.0109557333878379016480, \
             0.0102971169579563555237, \
             0.00964117772970253669530, \
             0.00898927578406413572328, \
             0.00834283875396815770558, \
             0.00770337523327974184817, \
             0.00707248999543355546805, \
             0.00645190005017573692280, \
             0.00584344987583563950756, \
             0.00524912345480885912513, \
             0.00467105037211432174741, \
             0.00411150397865469304717, \
             0.00357289278351729964938, \
             0.00305775341017553113613, \
             0.00256876494379402037313, \
             0.00210881524572663287933, \
             0.00168114286542146990631, \
             0.00128952408261041739210, \
             0.000938369848542381500794, \
             0.000632607319362633544219, \
             0.000377746646326984660274, \
             0.000180739564445388357820, \
             0.0000505360952078625176247 ] )

  elif ( n == 255 ):

    x = np.array ( [ \
             -0.99999759637974846462E+00, \
             -0.99998243035489159858E+00, \
             -0.99994399620705437576E+00, \
             -0.99987288812035761194E+00, \
             -0.99976049092443204733E+00, \
             -0.99959879967191068325E+00, \
             -0.99938033802502358193E+00, \
             -0.99909812496766759766E+00, \
             -0.99874561446809511470E+00, \
             -0.99831663531840739253E+00, \
             -0.99780535449595727456E+00, \
             -0.99720625937222195908E+00, \
             -0.99651414591489027385E+00, \
             -0.99572410469840718851E+00, \
             -0.99483150280062100052E+00, \
             -0.99383196321275502221E+00, \
             -0.99272134428278861533E+00, \
             -0.99149572117810613240E+00, \
             -0.99015137040077015918E+00, \
             -0.98868475754742947994E+00, \
             -0.98709252795403406719E+00, \
             -0.98537149959852037111E+00, \
             -0.98351865757863272876E+00, \
             -0.98153114955374010687E+00, \
             -0.97940628167086268381E+00, \
             -0.97714151463970571416E+00, \
             -0.97473445975240266776E+00, \
             -0.97218287474858179658E+00, \
             -0.96948465950245923177E+00, \
             -0.96663785155841656709E+00, \
             -0.96364062156981213252E+00, \
             -0.96049126870802028342E+00, \
             -0.95718821610986096274E+00, \
             -0.95373000642576113641E+00, \
             -0.95011529752129487656E+00, \
             -0.94634285837340290515E+00, \
             -0.94241156519108305981E+00, \
             -0.93832039777959288365E+00, \
             -0.93406843615772578800E+00, \
             -0.92965485742974005667E+00, \
             -0.92507893290707565236E+00, \
             -0.92034002547001242073E+00, \
             -0.91543758715576504064E+00, \
             -0.91037115695700429250E+00, \
             -0.90514035881326159519E+00, \
             -0.89974489977694003664E+00, \
             -0.89418456833555902286E+00, \
             -0.88845923287225699889E+00, \
             -0.88256884024734190684E+00, \
             -0.87651341448470526974E+00, \
             -0.87029305554811390585E+00, \
             -0.86390793819369047715E+00, \
             -0.85735831088623215653E+00, \
             -0.85064449476835027976E+00, \
             -0.84376688267270860104E+00, \
             -0.83672593816886873550E+00, \
             -0.82952219463740140018E+00, \
             -0.82215625436498040737E+00, \
             -0.81462878765513741344E+00, \
             -0.80694053195021761186E+00, \
             -0.79909229096084140180E+00, \
             -0.79108493379984836143E+00, \
             -0.78291939411828301639E+00, \
             -0.77459666924148337704E+00, \
             -0.76611781930376009072E+00, \
             -0.75748396638051363793E+00, \
             -0.74869629361693660282E+00, \
             -0.73975604435269475868E+00, \
             -0.73066452124218126133E+00, \
             -0.72142308537009891548E+00, \
             -0.71203315536225203459E+00, \
             -0.70249620649152707861E+00, \
             -0.69281376977911470289E+00, \
             -0.68298743109107922809E+00, \
             -0.67301883023041847920E+00, \
             -0.66290966002478059546E+00, \
             -0.65266166541001749610E+00, \
             -0.64227664250975951377E+00, \
             -0.63175643771119423041E+00, \
             -0.62110294673722640294E+00, \
             -0.61031811371518640016E+00, \
             -0.59940393024224289297E+00, \
             -0.58836243444766254143E+00, \
             -0.57719571005204581484E+00, \
             -0.56590588542365442262E+00, \
             -0.55449513263193254887E+00, \
             -0.54296566649831149049E+00, \
             -0.53131974364437562397E+00, \
             -0.51955966153745702199E+00, \
             -0.50768775753371660215E+00, \
             -0.49570640791876146017E+00, \
             -0.48361802694584102756E+00, \
             -0.47142506587165887693E+00, \
             -0.45913001198983233287E+00, \
             -0.44673538766202847374E+00, \
             -0.43424374934680255800E+00, \
             -0.42165768662616330006E+00, \
             -0.40897982122988867241E+00, \
             -0.39621280605761593918E+00, \
             -0.38335932419873034692E+00, \
             -0.37042208795007823014E+00, \
             -0.35740383783153215238E+00, \
             -0.34430734159943802278E+00, \
             -0.33113539325797683309E+00, \
             -0.31789081206847668318E+00, \
             -0.30457644155671404334E+00, \
             -0.29119514851824668196E+00, \
             -0.27774982202182431507E+00, \
             -0.26424337241092676194E+00, \
             -0.25067873030348317661E+00, \
             -0.23705884558982972721E+00, \
             -0.22338668642896688163E+00, \
             -0.20966523824318119477E+00, \
             -0.19589750271110015392E+00, \
             -0.18208649675925219825E+00, \
             -0.16823525155220746498E+00, \
             -0.15434681148137810869E+00, \
             -0.14042423315256017459E+00, \
             -0.12647058437230196685E+00, \
             -0.11248894313318662575E+00, \
             -0.098482396598119202090E+00, \
             -0.084454040083710883710E+00, \
             -0.070406976042855179063E+00, \
             -0.056344313046592789972E+00, \
             -0.042269164765363603212E+00, \
             -0.028184648949745694339E+00, \
             -0.014093886410782462614E+00, \
              0.0E+00, \
              0.014093886410782462614E+00, \
              0.028184648949745694339E+00, \
              0.042269164765363603212E+00, \
              0.056344313046592789972E+00, \
              0.070406976042855179063E+00, \
              0.084454040083710883710E+00, \
              0.098482396598119202090E+00, \
              0.11248894313318662575E+00, \
              0.12647058437230196685E+00, \
              0.14042423315256017459E+00, \
              0.15434681148137810869E+00, \
              0.16823525155220746498E+00, \
              0.18208649675925219825E+00, \
              0.19589750271110015392E+00, \
              0.20966523824318119477E+00, \
              0.22338668642896688163E+00, \
              0.23705884558982972721E+00, \
              0.25067873030348317661E+00, \
              0.26424337241092676194E+00, \
              0.27774982202182431507E+00, \
              0.29119514851824668196E+00, \
              0.30457644155671404334E+00, \
              0.31789081206847668318E+00, \
              0.33113539325797683309E+00, \
              0.34430734159943802278E+00, \
              0.35740383783153215238E+00, \
              0.37042208795007823014E+00, \
              0.38335932419873034692E+00, \
              0.39621280605761593918E+00, \
              0.40897982122988867241E+00, \
              0.42165768662616330006E+00, \
              0.43424374934680255800E+00, \
              0.44673538766202847374E+00, \
              0.45913001198983233287E+00, \
              0.47142506587165887693E+00, \
              0.48361802694584102756E+00, \
              0.49570640791876146017E+00, \
              0.50768775753371660215E+00, \
              0.51955966153745702199E+00, \
              0.53131974364437562397E+00, \
              0.54296566649831149049E+00, \
              0.55449513263193254887E+00, \
              0.56590588542365442262E+00, \
              0.57719571005204581484E+00, \
              0.58836243444766254143E+00, \
              0.59940393024224289297E+00, \
              0.61031811371518640016E+00, \
              0.62110294673722640294E+00, \
              0.63175643771119423041E+00, \
              0.64227664250975951377E+00, \
              0.65266166541001749610E+00, \
              0.66290966002478059546E+00, \
              0.67301883023041847920E+00, \
              0.68298743109107922809E+00, \
              0.69281376977911470289E+00, \
              0.70249620649152707861E+00, \
              0.71203315536225203459E+00, \
              0.72142308537009891548E+00, \
              0.73066452124218126133E+00, \
              0.73975604435269475868E+00, \
              0.74869629361693660282E+00, \
              0.75748396638051363793E+00, \
              0.76611781930376009072E+00, \
              0.77459666924148337704E+00, \
              0.78291939411828301639E+00, \
              0.79108493379984836143E+00, \
              0.79909229096084140180E+00, \
              0.80694053195021761186E+00, \
              0.81462878765513741344E+00, \
              0.82215625436498040737E+00, \
              0.82952219463740140018E+00, \
              0.83672593816886873550E+00, \
              0.84376688267270860104E+00, \
              0.85064449476835027976E+00, \
              0.85735831088623215653E+00, \
              0.86390793819369047715E+00, \
              0.87029305554811390585E+00, \
              0.87651341448470526974E+00, \
              0.88256884024734190684E+00, \
              0.88845923287225699889E+00, \
              0.89418456833555902286E+00, \
              0.89974489977694003664E+00, \
              0.90514035881326159519E+00, \
              0.91037115695700429250E+00, \
              0.91543758715576504064E+00, \
              0.92034002547001242073E+00, \
              0.92507893290707565236E+00, \
              0.92965485742974005667E+00, \
              0.93406843615772578800E+00, \
              0.93832039777959288365E+00, \
              0.94241156519108305981E+00, \
              0.94634285837340290515E+00, \
              0.95011529752129487656E+00, \
              0.95373000642576113641E+00, \
              0.95718821610986096274E+00, \
              0.96049126870802028342E+00, \
              0.96364062156981213252E+00, \
              0.96663785155841656709E+00, \
              0.96948465950245923177E+00, \
              0.97218287474858179658E+00, \
              0.97473445975240266776E+00, \
              0.97714151463970571416E+00, \
              0.97940628167086268381E+00, \
              0.98153114955374010687E+00, \
              0.98351865757863272876E+00, \
              0.98537149959852037111E+00, \
              0.98709252795403406719E+00, \
              0.98868475754742947994E+00, \
              0.99015137040077015918E+00, \
              0.99149572117810613240E+00, \
              0.99272134428278861533E+00, \
              0.99383196321275502221E+00, \
              0.99483150280062100052E+00, \
              0.99572410469840718851E+00, \
              0.99651414591489027385E+00, \
              0.99720625937222195908E+00, \
              0.99780535449595727456E+00, \
              0.99831663531840739253E+00, \
              0.99874561446809511470E+00, \
              0.99909812496766759766E+00, \
              0.99938033802502358193E+00, \
              0.99959879967191068325E+00, \
              0.99976049092443204733E+00, \
              0.99987288812035761194E+00, \
              0.99994399620705437576E+00, \
              0.99998243035489159858E+00, \
              0.99999759637974846462E+00 ] )

    w = np.array ( [ \
             0.69379364324108267170E-05, \
             0.25157870384280661489E-04, \
             0.53275293669780613125E-04, \
             0.90372734658751149261E-04, \
             0.13575491094922871973E-03, \
             0.18887326450650491366E-03, \
             0.24921240048299729402E-03, \
             0.31630366082226447689E-03, \
             0.38974528447328229322E-03, \
             0.46918492424785040975E-03, \
             0.55429531493037471492E-03, \
             0.64476204130572477933E-03, \
             0.74028280424450333046E-03, \
             0.84057143271072246365E-03, \
             0.94536151685852538246E-03, \
             0.10544076228633167722E-02, \
             0.11674841174299594077E-02, \
             0.12843824718970101768E-02, \
             0.14049079956551446427E-02, \
             0.15288767050877655684E-02, \
             0.16561127281544526052E-02, \
             0.17864463917586498247E-02, \
             0.19197129710138724125E-02, \
             0.20557519893273465236E-02, \
             0.21944069253638388388E-02, \
             0.23355251860571608737E-02, \
             0.24789582266575679307E-02, \
             0.26245617274044295626E-02, \
             0.27721957645934509940E-02, \
             0.29217249379178197538E-02, \
             0.30730184347025783234E-02, \
             0.32259500250878684614E-02, \
             0.33803979910869203823E-02, \
             0.35362449977167777340E-02, \
             0.36933779170256508183E-02, \
             0.38516876166398709241E-02, \
             0.40110687240750233989E-02, \
             0.41714193769840788528E-02, \
             0.43326409680929828545E-02, \
             0.44946378920320678616E-02, \
             0.46573172997568547773E-02, \
             0.48205888648512683476E-02, \
             0.49843645647655386012E-02, \
             0.51485584789781777618E-02, \
             0.53130866051870565663E-02, \
             0.54778666939189508240E-02, \
             0.56428181013844441585E-02, \
             0.58078616599775673635E-02, \
             0.59729195655081658049E-02, \
             0.61379152800413850435E-02, \
             0.63027734490857587172E-02, \
             0.64674198318036867274E-02, \
             0.66317812429018878941E-02, \
             0.67957855048827733948E-02, \
             0.69593614093904229394E-02, \
             0.71224386864583871532E-02, \
             0.72849479805538070639E-02, \
             0.74468208324075910174E-02, \
             0.76079896657190565832E-02, \
             0.77683877779219912200E-02, \
             0.79279493342948491103E-02, \
             0.80866093647888599710E-02, \
             0.82443037630328680306E-02, \
             0.84009692870519326354E-02, \
             0.85565435613076896192E-02, \
             0.87109650797320868736E-02, \
             0.88641732094824942641E-02, \
             0.90161081951956431600E-02, \
             0.91667111635607884067E-02, \
             0.93159241280693950932E-02, \
             0.94636899938300652943E-02, \
             0.96099525623638830097E-02, \
             0.97546565363174114611E-02, \
             0.98977475240487497440E-02, \
             0.10039172044056840798E-01, \
             0.10178877529236079733E-01, \
             0.10316812330947621682E-01, \
             0.10452925722906011926E-01, \
             0.10587167904885197931E-01, \
             0.10719490006251933623E-01, \
             0.10849844089337314099E-01, \
             0.10978183152658912470E-01, \
             0.11104461134006926537E-01, \
             0.11228632913408049354E-01, \
             0.11350654315980596602E-01, \
             0.11470482114693874380E-01, \
             0.11588074033043952568E-01, \
             0.11703388747657003101E-01, \
             0.11816385890830235763E-01, \
             0.11927026053019270040E-01, \
             0.12035270785279562630E-01, \
             0.12141082601668299679E-01, \
             0.12244424981611985899E-01, \
             0.12345262372243838455E-01, \
             0.12443560190714035263E-01, \
             0.12539284826474884353E-01, \
             0.12632403643542078765E-01, \
             0.12722884982732382906E-01, \
             0.12810698163877361967E-01, \
             0.12895813488012114694E-01, \
             0.12978202239537399286E-01, \
             0.13057836688353048840E-01, \
             0.13134690091960152836E-01, \
             0.13208736697529129966E-01, \
             0.13279951743930530650E-01, \
             0.13348311463725179953E-01, \
             0.13413793085110098513E-01, \
             0.13476374833816515982E-01, \
             0.13536035934956213614E-01, \
             0.13592756614812395910E-01, \
             0.13646518102571291428E-01, \
             0.13697302631990716258E-01, \
             0.13745093443001896632E-01, \
             0.13789874783240936517E-01, \
             0.13831631909506428676E-01, \
             0.13870351089139840997E-01, \
             0.13906019601325461264E-01, \
             0.13938625738306850804E-01, \
             0.13968158806516938516E-01, \
             0.13994609127619079852E-01, \
             0.14017968039456608810E-01, \
             0.14038227896908623303E-01, \
             0.14055382072649964277E-01, \
             0.14069424957813575318E-01, \
             0.14080351962553661325E-01, \
             0.14088159516508301065E-01, \
             0.14092845069160408355E-01, \
             0.14094407090096179347E-01, \
             0.14092845069160408355E-01, \
             0.14088159516508301065E-01, \
             0.14080351962553661325E-01, \
             0.14069424957813575318E-01, \
             0.14055382072649964277E-01, \
             0.14038227896908623303E-01, \
             0.14017968039456608810E-01, \
             0.13994609127619079852E-01, \
             0.13968158806516938516E-01, \
             0.13938625738306850804E-01, \
             0.13906019601325461264E-01, \
             0.13870351089139840997E-01, \
             0.13831631909506428676E-01, \
             0.13789874783240936517E-01, \
             0.13745093443001896632E-01, \
             0.13697302631990716258E-01, \
             0.13646518102571291428E-01, \
             0.13592756614812395910E-01, \
             0.13536035934956213614E-01, \
             0.13476374833816515982E-01, \
             0.13413793085110098513E-01, \
             0.13348311463725179953E-01, \
             0.13279951743930530650E-01, \
             0.13208736697529129966E-01, \
             0.13134690091960152836E-01, \
             0.13057836688353048840E-01, \
             0.12978202239537399286E-01, \
             0.12895813488012114694E-01, \
             0.12810698163877361967E-01, \
             0.12722884982732382906E-01, \
             0.12632403643542078765E-01, \
             0.12539284826474884353E-01, \
             0.12443560190714035263E-01, \
             0.12345262372243838455E-01, \
             0.12244424981611985899E-01, \
             0.12141082601668299679E-01, \
             0.12035270785279562630E-01, \
             0.11927026053019270040E-01, \
             0.11816385890830235763E-01, \
             0.11703388747657003101E-01, \
             0.11588074033043952568E-01, \
             0.11470482114693874380E-01, \
             0.11350654315980596602E-01, \
             0.11228632913408049354E-01, \
             0.11104461134006926537E-01, \
             0.10978183152658912470E-01, \
             0.10849844089337314099E-01, \
             0.10719490006251933623E-01, \
             0.10587167904885197931E-01, \
             0.10452925722906011926E-01, \
             0.10316812330947621682E-01, \
             0.10178877529236079733E-01, \
             0.10039172044056840798E-01, \
             0.98977475240487497440E-02, \
             0.97546565363174114611E-02, \
             0.96099525623638830097E-02, \
             0.94636899938300652943E-02, \
             0.93159241280693950932E-02, \
             0.91667111635607884067E-02, \
             0.90161081951956431600E-02, \
             0.88641732094824942641E-02, \
             0.87109650797320868736E-02, \
             0.85565435613076896192E-02, \
             0.84009692870519326354E-02, \
             0.82443037630328680306E-02, \
             0.80866093647888599710E-02, \
             0.79279493342948491103E-02, \
             0.77683877779219912200E-02, \
             0.76079896657190565832E-02, \
             0.74468208324075910174E-02, \
             0.72849479805538070639E-02, \
             0.71224386864583871532E-02, \
             0.69593614093904229394E-02, \
             0.67957855048827733948E-02, \
             0.66317812429018878941E-02, \
             0.64674198318036867274E-02, \
             0.63027734490857587172E-02, \
             0.61379152800413850435E-02, \
             0.59729195655081658049E-02, \
             0.58078616599775673635E-02, \
             0.56428181013844441585E-02, \
             0.54778666939189508240E-02, \
             0.53130866051870565663E-02, \
             0.51485584789781777618E-02, \
             0.49843645647655386012E-02, \
             0.48205888648512683476E-02, \
             0.46573172997568547773E-02, \
             0.44946378920320678616E-02, \
             0.43326409680929828545E-02, \
             0.41714193769840788528E-02, \
             0.40110687240750233989E-02, \
             0.38516876166398709241E-02, \
             0.36933779170256508183E-02, \
             0.35362449977167777340E-02, \
             0.33803979910869203823E-02, \
             0.32259500250878684614E-02, \
             0.30730184347025783234E-02, \
             0.29217249379178197538E-02, \
             0.27721957645934509940E-02, \
             0.26245617274044295626E-02, \
             0.24789582266575679307E-02, \
             0.23355251860571608737E-02, \
             0.21944069253638388388E-02, \
             0.20557519893273465236E-02, \
             0.19197129710138724125E-02, \
             0.17864463917586498247E-02, \
             0.16561127281544526052E-02, \
             0.15288767050877655684E-02, \
             0.14049079956551446427E-02, \
             0.12843824718970101768E-02, \
             0.11674841174299594077E-02, \
             0.10544076228633167722E-02, \
             0.94536151685852538246E-03, \
             0.84057143271072246365E-03, \
             0.74028280424450333046E-03, \
             0.64476204130572477933E-03, \
             0.55429531493037471492E-03, \
             0.46918492424785040975E-03, \
             0.38974528447328229322E-03, \
             0.31630366082226447689E-03, \
             0.24921240048299729402E-03, \
             0.18887326450650491366E-03, \
             0.13575491094922871973E-03, \
             0.90372734658751149261E-04, \
             0.53275293669780613125E-04, \
             0.25157870384280661489E-04, \
             0.69379364324108267170E-05 ] )

  elif ( n == 511 ):

    x = np.array ( [ \
             -0.999999672956734384381, \
             -0.999997596379748464620, \
             -0.999992298136257588028, \
             -0.999982430354891598580, \
             -0.999966730098486276883, \
             -0.999943996207054375764, \
             -0.999913081144678282800, \
             -0.999872888120357611938, \
             -0.999822363679787739196, \
             -0.999760490924432047330, \
             -0.999686286448317731776, \
             -0.999598799671910683252, \
             -0.999497112467187190535, \
             -0.999380338025023581928, \
             -0.999247618943342473599, \
             -0.999098124967667597662, \
             -0.998931050830810562236, \
             -0.998745614468095114704, \
             -0.998541055697167906027, \
             -0.998316635318407392531, \
             -0.998071634524930323302, \
             -0.997805354495957274562, \
             -0.997517116063472399965, \
             -0.997206259372221959076, \
             -0.996872143485260161299, \
             -0.996514145914890273849, \
             -0.996131662079315037786, \
             -0.995724104698407188509, \
             -0.995290903148810302261, \
             -0.994831502800621000519, \
             -0.994345364356723405931, \
             -0.993831963212755022209, \
             -0.993290788851684966211, \
             -0.992721344282788615328, \
             -0.992123145530863117683, \
             -0.991495721178106132399, \
             -0.990838611958294243677, \
             -0.990151370400770159181, \
             -0.989433560520240838716, \
             -0.988684757547429479939, \
             -0.987904547695124280467, \
             -0.987092527954034067190, \
             -0.986248305913007552681, \
             -0.985371499598520371114, \
             -0.984461737328814534596, \
             -0.983518657578632728762, \
             -0.982541908851080604251, \
             -0.981531149553740106867, \
             -0.980486047876721339416, \
             -0.979406281670862683806, \
             -0.978291538324758539526, \
             -0.977141514639705714156, \
             -0.975955916702011753129, \
             -0.974734459752402667761, \
             -0.973476868052506926773, \
             -0.972182874748581796578, \
             -0.970852221732792443256, \
             -0.969484659502459231771, \
             -0.968079947017759947964, \
             -0.966637851558416567092, \
             -0.965158148579915665979, \
             -0.963640621569812132521, \
             -0.962085061904651475741, \
             -0.960491268708020283423, \
             -0.958859048710200221356, \
             -0.957188216109860962736, \
             -0.955478592438183697574, \
             -0.953730006425761136415, \
             -0.951942293872573589498, \
             -0.950115297521294876558, \
             -0.948248866934137357063, \
             -0.946342858373402905148, \
             -0.944397134685866648591, \
             -0.942411565191083059813, \
             -0.940386025573669721370, \
             -0.938320397779592883655, \
             -0.936214569916450806625, \
             -0.934068436157725787999, \
             -0.931881896650953639345, \
             -0.929654857429740056670, \
             -0.927387230329536696843, \
             -0.925078932907075652364, \
             -0.922729888363349241523, \
             -0.920340025470012420730, \
             -0.917909278499077501636, \
             -0.915437587155765040644, \
             -0.912924896514370590080, \
             -0.910371156957004292498, \
             -0.907776324115058903624, \
             -0.905140358813261595189, \
             -0.902463227016165675048, \
             -0.899744899776940036639, \
             -0.896985353188316590376, \
             -0.894184568335559022859, \
             -0.891342531251319871666, \
             -0.888459232872256998890, \
             -0.885534668997285008926, \
             -0.882568840247341906842, \
             -0.879561752026556262568, \
             -0.876513414484705269742, \
             -0.873423842480859310192, \
             -0.870293055548113905851, \
             -0.867121077859315215614, \
             -0.863907938193690477146, \
             -0.860653669904299969802, \
             -0.857358310886232156525, \
             -0.854021903545468625813, \
             -0.850644494768350279758, \
             -0.847226135891580884381, \
             -0.843766882672708601038, \
             -0.840266795261030442350, \
             -0.836725938168868735503, \
             -0.833144380243172624728, \
             -0.829522194637401400178, \
             -0.825859458783650001088, \
             -0.822156254364980407373, \
             -0.818412667287925807395, \
             -0.814628787655137413436, \
             -0.810804709738146594361, \
             -0.806940531950217611856, \
             -0.803036356819268687782, \
             -0.799092290960841401800, \
             -0.795108445051100526780, \
             -0.791084933799848361435, \
             -0.787021875923539422170, \
             -0.782919394118283016385, \
             -0.778777615032822744702, \
             -0.774596669241483377036, \
             -0.770376691217076824278, \
             -0.766117819303760090717, \
             -0.761820195689839149173, \
             -0.757483966380513637926, \
             -0.753109281170558142523, \
             -0.748696293616936602823, \
             -0.744245161011347082309, \
             -0.739756044352694758677, \
             -0.735229108319491547663, \
             -0.730664521242181261329, \
             -0.726062455075389632685, \
             -0.721423085370098915485, \
             -0.716746591245747095767, \
             -0.712033155362252034587, \
             -0.707282963891961103412, \
             -0.702496206491527078610, \
             -0.697673076273711232906, \
             -0.692813769779114702895, \
             -0.687918486947839325756, \
             -0.682987431091079228087, \
             -0.678020808862644517838, \
             -0.673018830230418479199, \
             -0.667981708447749702165, \
             -0.662909660024780595461, \
             -0.657802904699713735422, \
             -0.652661665410017496101, \
             -0.647486168263572388782, \
             -0.642276642509759513774, \
             -0.637033320510492495071, \
             -0.631756437711194230414, \
             -0.626446232611719746542, \
             -0.621102946737226402941, \
             -0.615726824608992638014, \
             -0.610318113715186400156, \
             -0.604877064481584353319, \
             -0.599403930242242892974, \
             -0.593898967210121954393, \
             -0.588362434447662541434, \
             -0.582794593837318850840, \
             -0.577195710052045814844, \
             -0.571566050525742833992, \
             -0.565905885423654422623, \
             -0.560215487612728441818, \
             -0.554495132631932548866, \
             -0.548745098662529448608, \
             -0.542965666498311490492, \
             -0.537157119515795115982, \
             -0.531319743644375623972, \
             -0.525453827336442687395, \
             -0.519559661537457021993, \
             -0.513637539655988578507, \
             -0.507687757533716602155, \
             -0.501710613415391878251, \
             -0.495706407918761460170, \
             -0.489675444004456155436, \
             -0.483618026945841027562, \
             -0.477534464298829155284, \
             -0.471425065871658876934, \
             -0.465290143694634735858, \
             -0.459130011989832332874, \
             -0.452944987140767283784, \
             -0.446735387662028473742, \
             -0.440501534168875795783, \
             -0.434243749346802558002, \
             -0.427962357921062742583, \
             -0.421657686626163300056, \
             -0.415330064175321663764, \
             -0.408979821229888672409, \
             -0.402607290368737092671, \
             -0.396212806057615939183, \
             -0.389796704618470795479, \
             -0.383359324198730346916, \
             -0.376901004740559344802, \
             -0.370422087950078230138, \
             -0.363922917266549655269, \
             -0.357403837831532152376, \
             -0.350865196458001209011, \
             -0.344307341599438022777, \
             -0.337730623318886219621, \
             -0.331135393257976833093, \
             -0.324522004605921855207, \
             -0.317890812068476683182, \
             -0.311242171836871800300, \
             -0.304576441556714043335, \
             -0.297893980296857823437, \
             -0.291195148518246681964, \
             -0.284480308042725577496, \
             -0.277749822021824315065, \
             -0.271004054905512543536, \
             -0.264243372410926761945, \
             -0.257468141491069790481, \
             -0.250678730303483176613, \
             -0.243875508178893021593, \
             -0.237058845589829727213, \
             -0.230229114119222177156, \
             -0.223386686428966881628, \
             -0.216531936228472628081, \
             -0.209665238243181194766, \
             -0.202786968183064697557, \
             -0.195897502711100153915, \
             -0.188997219411721861059, \
             -0.182086496759252198246, \
             -0.175165714086311475707, \
             -0.168235251552207464982, \
             -0.161295490111305257361, \
             -0.154346811481378108692, \
             -0.147389598111939940054, \
             -0.140424233152560174594, \
             -0.133451100421161601344, \
             -0.126470584372301966851, \
             -0.119483070065440005133, \
             -0.112488943133186625746, \
             -0.105488589749541988533, \
             -0.984823965981192020903E-01, \
             -0.914707508403553909095E-01, \
             -0.844540400837108837102E-01, \
             -0.774326523498572825675E-01, \
             -0.704069760428551790633E-01, \
             -0.633773999173222898797E-01, \
             -0.563443130465927899720E-01, \
             -0.493081047908686267156E-01, \
             -0.422691647653636032124E-01, \
             -0.352278828084410232603E-01, \
             -0.281846489497456943394E-01, \
             -0.211398533783310883350E-01, \
             -0.140938864107824626142E-01, \
             -0.704713845933674648514E-02, \
             +0.000000000000000000000, \
             +0.704713845933674648514E-02, \
             +0.140938864107824626142E-01, \
             +0.211398533783310883350E-01, \
             +0.281846489497456943394E-01, \
             +0.352278828084410232603E-01, \
             +0.422691647653636032124E-01, \
             +0.493081047908686267156E-01, \
             +0.563443130465927899720E-01, \
             +0.633773999173222898797E-01, \
             +0.704069760428551790633E-01, \
             +0.774326523498572825675E-01, \
             +0.844540400837108837102E-01, \
             +0.914707508403553909095E-01, \
             +0.984823965981192020903E-01, \
             +0.105488589749541988533, \
             +0.112488943133186625746, \
             +0.119483070065440005133, \
             +0.126470584372301966851, \
             +0.133451100421161601344, \
             +0.140424233152560174594, \
             +0.147389598111939940054, \
             +0.154346811481378108692, \
             +0.161295490111305257361, \
             +0.168235251552207464982, \
             +0.175165714086311475707, \
             +0.182086496759252198246, \
             +0.188997219411721861059, \
             +0.195897502711100153915, \
             +0.202786968183064697557, \
             +0.209665238243181194766, \
             +0.216531936228472628081, \
             +0.223386686428966881628, \
             +0.230229114119222177156, \
             +0.237058845589829727213, \
             +0.243875508178893021593, \
             +0.250678730303483176613, \
             +0.257468141491069790481, \
             +0.264243372410926761945, \
             +0.271004054905512543536, \
             +0.277749822021824315065, \
             +0.284480308042725577496, \
             +0.291195148518246681964, \
             +0.297893980296857823437, \
             +0.304576441556714043335, \
             +0.311242171836871800300, \
             +0.317890812068476683182, \
             +0.324522004605921855207, \
             +0.331135393257976833093, \
             +0.337730623318886219621, \
             +0.344307341599438022777, \
             +0.350865196458001209011, \
             +0.357403837831532152376, \
             +0.363922917266549655269, \
             +0.370422087950078230138, \
             +0.376901004740559344802, \
             +0.383359324198730346916, \
             +0.389796704618470795479, \
             +0.396212806057615939183, \
             +0.402607290368737092671, \
             +0.408979821229888672409, \
             +0.415330064175321663764, \
             +0.421657686626163300056, \
             +0.427962357921062742583, \
             +0.434243749346802558002, \
             +0.440501534168875795783, \
             +0.446735387662028473742, \
             +0.452944987140767283784, \
             +0.459130011989832332874, \
             +0.465290143694634735858, \
             +0.471425065871658876934, \
             +0.477534464298829155284, \
             +0.483618026945841027562, \
             +0.489675444004456155436, \
             +0.495706407918761460170, \
             +0.501710613415391878251, \
             +0.507687757533716602155, \
             +0.513637539655988578507, \
             +0.519559661537457021993, \
             +0.525453827336442687395, \
             +0.531319743644375623972, \
             +0.537157119515795115982, \
             +0.542965666498311490492, \
             +0.548745098662529448608, \
             +0.554495132631932548866, \
             +0.560215487612728441818, \
             +0.565905885423654422623, \
             +0.571566050525742833992, \
             +0.577195710052045814844, \
             +0.582794593837318850840, \
             +0.588362434447662541434, \
             +0.593898967210121954393, \
             +0.599403930242242892974, \
             +0.604877064481584353319, \
             +0.610318113715186400156, \
             +0.615726824608992638014, \
             +0.621102946737226402941, \
             +0.626446232611719746542, \
             +0.631756437711194230414, \
             +0.637033320510492495071, \
             +0.642276642509759513774, \
             +0.647486168263572388782, \
             +0.652661665410017496101, \
             +0.657802904699713735422, \
             +0.662909660024780595461, \
             +0.667981708447749702165, \
             +0.673018830230418479199, \
             +0.678020808862644517838, \
             +0.682987431091079228087, \
             +0.687918486947839325756, \
             +0.692813769779114702895, \
             +0.697673076273711232906, \
             +0.702496206491527078610, \
             +0.707282963891961103412, \
             +0.712033155362252034587, \
             +0.716746591245747095767, \
             +0.721423085370098915485, \
             +0.726062455075389632685, \
             +0.730664521242181261329, \
             +0.735229108319491547663, \
             +0.739756044352694758677, \
             +0.744245161011347082309, \
             +0.748696293616936602823, \
             +0.753109281170558142523, \
             +0.757483966380513637926, \
             +0.761820195689839149173, \
             +0.766117819303760090717, \
             +0.770376691217076824278, \
             +0.774596669241483377036, \
             +0.778777615032822744702, \
             +0.782919394118283016385, \
             +0.787021875923539422170, \
             +0.791084933799848361435, \
             +0.795108445051100526780, \
             +0.799092290960841401800, \
             +0.803036356819268687782, \
             +0.806940531950217611856, \
             +0.810804709738146594361, \
             +0.814628787655137413436, \
             +0.818412667287925807395, \
             +0.822156254364980407373, \
             +0.825859458783650001088, \
             +0.829522194637401400178, \
             +0.833144380243172624728, \
             +0.836725938168868735503, \
             +0.840266795261030442350, \
             +0.843766882672708601038, \
             +0.847226135891580884381, \
             +0.850644494768350279758, \
             +0.854021903545468625813, \
             +0.857358310886232156525, \
             +0.860653669904299969802, \
             +0.863907938193690477146, \
             +0.867121077859315215614, \
             +0.870293055548113905851, \
             +0.873423842480859310192, \
             +0.876513414484705269742, \
             +0.879561752026556262568, \
             +0.882568840247341906842, \
             +0.885534668997285008926, \
             +0.888459232872256998890, \
             +0.891342531251319871666, \
             +0.894184568335559022859, \
             +0.896985353188316590376, \
             +0.899744899776940036639, \
             +0.902463227016165675048, \
             +0.905140358813261595189, \
             +0.907776324115058903624, \
             +0.910371156957004292498, \
             +0.912924896514370590080, \
             +0.915437587155765040644, \
             +0.917909278499077501636, \
             +0.920340025470012420730, \
             +0.922729888363349241523, \
             +0.925078932907075652364, \
             +0.927387230329536696843, \
             +0.929654857429740056670, \
             +0.931881896650953639345, \
             +0.934068436157725787999, \
             +0.936214569916450806625, \
             +0.938320397779592883655, \
             +0.940386025573669721370, \
             +0.942411565191083059813, \
             +0.944397134685866648591, \
             +0.946342858373402905148, \
             +0.948248866934137357063, \
             +0.950115297521294876558, \
             +0.951942293872573589498, \
             +0.953730006425761136415, \
             +0.955478592438183697574, \
             +0.957188216109860962736, \
             +0.958859048710200221356, \
             +0.960491268708020283423, \
             +0.962085061904651475741, \
             +0.963640621569812132521, \
             +0.965158148579915665979, \
             +0.966637851558416567092, \
             +0.968079947017759947964, \
             +0.969484659502459231771, \
             +0.970852221732792443256, \
             +0.972182874748581796578, \
             +0.973476868052506926773, \
             +0.974734459752402667761, \
             +0.975955916702011753129, \
             +0.977141514639705714156, \
             +0.978291538324758539526, \
             +0.979406281670862683806, \
             +0.980486047876721339416, \
             +0.981531149553740106867, \
             +0.982541908851080604251, \
             +0.983518657578632728762, \
             +0.984461737328814534596, \
             +0.985371499598520371114, \
             +0.986248305913007552681, \
             +0.987092527954034067190, \
             +0.987904547695124280467, \
             +0.988684757547429479939, \
             +0.989433560520240838716, \
             +0.990151370400770159181, \
             +0.990838611958294243677, \
             +0.991495721178106132399, \
             +0.992123145530863117683, \
             +0.992721344282788615328, \
             +0.993290788851684966211, \
             +0.993831963212755022209, \
             +0.994345364356723405931, \
             +0.994831502800621000519, \
             +0.995290903148810302261, \
             +0.995724104698407188509, \
             +0.996131662079315037786, \
             +0.996514145914890273849, \
             +0.996872143485260161299, \
             +0.997206259372221959076, \
             +0.997517116063472399965, \
             +0.997805354495957274562, \
             +0.998071634524930323302, \
             +0.998316635318407392531, \
             +0.998541055697167906027, \
             +0.998745614468095114704, \
             +0.998931050830810562236, \
             +0.999098124967667597662, \
             +0.999247618943342473599, \
             +0.999380338025023581928, \
             +0.999497112467187190535, \
             +0.999598799671910683252, \
             +0.999686286448317731776, \
             +0.999760490924432047330, \
             +0.999822363679787739196, \
             +0.999872888120357611938, \
             +0.999913081144678282800, \
             +0.999943996207054375764, \
             +0.999966730098486276883, \
             +0.999982430354891598580, \
             +0.999992298136257588028, \
             +0.999997596379748464620, \
             +0.999999672956734384381 ] )

    w = np.array ( [ \
             0.945715933950007048827E-06, \
             0.345456507169149134898E-05, \
             0.736624069102321668857E-05, \
             0.125792781889592743525E-04, \
             0.190213681905875816679E-04, \
             0.266376412339000901358E-04, \
             0.353751372055189588628E-04, \
             0.451863674126296143105E-04, \
             0.560319507856164252140E-04, \
             0.678774554733972416227E-04, \
             0.806899228014035293851E-04, \
             0.944366322532705527066E-04, \
             0.109085545645741522051E-03, \
             0.124606200241498368482E-03, \
             0.140970302204104791413E-03, \
             0.158151830411132242924E-03, \
             0.176126765545083195474E-03, \
             0.194872642236641146532E-03, \
             0.214368090034216937149E-03, \
             0.234592462123925204879E-03, \
             0.255525589595236862014E-03, \
             0.277147657465187357459E-03, \
             0.299439176850911730874E-03, \
             0.322381020652862389664E-03, \
             0.345954492129903871350E-03, \
             0.370141402122251665232E-03, \
             0.394924138246873704434E-03, \
             0.420285716355361231823E-03, \
             0.446209810101403247488E-03, \
             0.472680758429262691232E-03, \
             0.499683553312800484519E-03, \
             0.527203811431658386125E-03, \
             0.555227733977307579715E-03, \
             0.583742058714979703847E-03, \
             0.612734008012225209294E-03, \
             0.642191235948505088403E-03, \
             0.672101776960108194646E-03, \
             0.702453997827572321358E-03, \
             0.733236554224767912055E-03, \
             0.764438352543882784191E-03, \
             0.796048517297550871506E-03, \
             0.828056364077226302608E-03, \
             0.860451377808527848128E-03, \
             0.893223195879324912340E-03, \
             0.926361595613111283368E-03, \
             0.959856485506936206261E-03, \
             0.993697899638760857945E-03, \
             0.102787599466367326179E-02, \
             0.106238104885340071375E-02, \
             0.109720346268191941940E-02, \
             0.113233376051597664917E-02, \
             0.116776259302858043685E-02, \
             0.120348074001265964881E-02, \
             0.123947911332878396534E-02, \
             0.127574875977346947345E-02, \
             0.131228086370221478128E-02, \
             0.134906674928353113127E-02, \
             0.138609788229672549700E-02, \
             0.142336587141720519900E-02, \
             0.146086246895890987689E-02, \
             0.149857957106456636214E-02, \
             0.153650921735128916170E-02, \
             0.157464359003212166189E-02, \
             0.161297501254393423070E-02, \
             0.165149594771914570655E-02, \
             0.169019899554346019117E-02, \
             0.172907689054461607168E-02, \
             0.176812249885838886701E-02, \
             0.180732881501808930079E-02, \
             0.184668895851282540913E-02, \
             0.188619617015808475394E-02, \
             0.192584380831993546204E-02, \
             0.196562534503150547732E-02, \
             0.200553436203751169944E-02, \
             0.204556454679958293446E-02, \
             0.208570968849203942640E-02, \
             0.212596367401472533045E-02, \
             0.216632048404649142727E-02, \
             0.220677418916003329194E-02, \
             0.224731894601603393082E-02, \
             0.228794899365195972378E-02, \
             0.232865864987842738864E-02, \
             0.236944230779380495146E-02, \
             0.241029443242563417382E-02, \
             0.245120955750556483923E-02, \
             0.249218228238276930060E-02, \
             0.253320726907925325750E-02, \
             0.257427923948908888092E-02, \
             0.261539297272236109225E-02, \
             0.265654330259352828314E-02, \
             0.269772511525294586667E-02, \
             0.273893334695947541201E-02, \
             0.278016298199139435045E-02, \
             0.282140905069222207923E-02, \
             0.286266662764757868253E-02, \
             0.290393082998878368175E-02, \
             0.294519681581857582284E-02, \
             0.298645978275408290247E-02, \
             0.302771496658198544480E-02, \
             0.306895764002069252174E-02, \
             0.311018311158427546158E-02, \
             0.315138672454287935858E-02, \
             0.319256385597434736790E-02, \
             0.323370991590184336368E-02, \
             0.327482034651233969564E-02, \
             0.331589062145094394706E-02, \
             0.335691624518616761342E-02, \
             0.339789275244138669739E-02, \
             0.343881570768790591876E-02, \
             0.347968070469521146972E-02, \
             0.352048336613417922682E-02, \
             0.356121934322919357659E-02, \
             0.360188431545532431869E-02, \
             0.364247399027690353194E-02, \
             0.368298410292403911967E-02, \
             0.372341041620379550870E-02, \
             0.376374872034296338241E-02, \
             0.380399483285952829161E-02, \
             0.384414459846013158917E-02, \
             0.388419388896099560998E-02, \
             0.392413860322995774660E-02, \
             0.396397466714742455513E-02, \
             0.400369803358421688562E-02, \
             0.404330468239442998549E-02, \
             0.408279062042157838350E-02, \
             0.412215188151643401528E-02, \
             0.416138452656509745764E-02, \
             0.420048464352596631772E-02, \
             0.423944834747438184434E-02, \
             0.427827178065384480959E-02, \
             0.431695111253279479928E-02, \
             0.435548253986604343679E-02, \
             0.439386228676004195260E-02, \
             0.443208660474124713206E-02, \
             0.447015177282692726900E-02, \
             0.450805409759782158001E-02, \
             0.454578991327213285488E-02, \
             0.458335558178039420335E-02, \
             0.462074749284080687482E-02, \
             0.465796206403469754658E-02, \
             0.469499574088179046532E-02, \
             0.473184499691503264714E-02, \
             0.476850633375474925263E-02, \
             0.480497628118194150483E-02, \
             0.484125139721057135214E-02, \
             0.487732826815870573054E-02, \
             0.491320350871841897367E-02, \
             0.494887376202437487201E-02, \
             0.498433569972103029914E-02, \
             0.501958602202842039909E-02, \
             0.505462145780650125058E-02, \
             0.508943876461803986674E-02, \
             0.512403472879005351831E-02, \
             0.515840616547381084096E-02, \
             0.519254991870341614863E-02, \
             0.522646286145300596306E-02, \
             0.526014189569259311205E-02, \
             0.529358395244259896547E-02, \
             0.532678599182711857974E-02, \
             0.535974500312596681161E-02, \
             0.539245800482555593606E-02, \
             0.542492204466865704951E-02, \
             0.545713419970309863995E-02, \
             0.548909157632945623482E-02, \
             0.552079131034778706457E-02, \
             0.555223056700346326850E-02, \
             0.558340654103215637610E-02, \
             0.561431645670402467678E-02, \
             0.564495756786715368885E-02, \
             0.567532715799029830087E-02, \
             0.570542254020497332312E-02, \
             0.573524105734693719020E-02, \
             0.576478008199711142954E-02, \
             0.579403701652197628421E-02, \
             0.582300929311348057702E-02, \
             0.585169437382850155033E-02, \
             0.588008975062788803205E-02, \
             0.590819294541511788161E-02, \
             0.593600151007459827614E-02, \
             0.596351302650963502011E-02, \
             0.599072510668009471472E-02, \
             0.601763539263978131522E-02, \
             0.604424155657354634589E-02, \
             0.607054130083414983949E-02, \
             0.609653235797888692923E-02, \
             0.612221249080599294931E-02, \
             0.614757949239083790214E-02, \
             0.617263118612191922727E-02, \
             0.619736542573665996342E-02, \
             0.622178009535701763157E-02, \
             0.624587310952490748541E-02, \
             0.626964241323744217671E-02, \
             0.629308598198198836688E-02, \
             0.631620182177103938227E-02, \
             0.633898796917690165912E-02, \
             0.636144249136619145314E-02, \
             0.638356348613413709795E-02, \
             0.640534908193868098342E-02, \
             0.642679743793437438922E-02, \
             0.644790674400605734710E-02, \
             0.646867522080231481688E-02, \
             0.648910111976869964292E-02, \
             0.650918272318071200827E-02, \
             0.652891834417652442012E-02, \
             0.654830632678944064054E-02, \
             0.656734504598007641819E-02, \
             0.658603290766824937794E-02, \
             0.660436834876456498276E-02, \
             0.662234983720168509457E-02, \
             0.663997587196526532519E-02, \
             0.665724498312454708217E-02, \
             0.667415573186258997654E-02, \
             0.669070671050613006584E-02, \
             0.670689654255504925648E-02, \
             0.672272388271144108036E-02, \
             0.673818741690825799086E-02, \
             0.675328586233752529078E-02, \
             0.676801796747810680683E-02, \
             0.678238251212300746082E-02, \
             0.679637830740619795480E-02, \
             0.681000419582894688374E-02, \
             0.682325905128564571420E-02, \
             0.683614177908911221841E-02, \
             0.684865131599535812903E-02, \
             0.686078663022780697951E-02, \
             0.687254672150094831613E-02, \
             0.688393062104341470995E-02, \
             0.689493739162046825872E-02, \
             0.690556612755588354803E-02, \
             0.691581595475321433825E-02, \
             0.692568603071643155621E-02, \
             0.693517554456992049848E-02, \
             0.694428371707782549438E-02, \
             0.695300980066273063177E-02, \
             0.696135307942366551493E-02, \
             0.696931286915342540213E-02, \
             0.697688851735519545845E-02, \
             0.698407940325846925786E-02, \
             0.699088493783425207545E-02, \
             0.699730456380953992594E-02, \
             0.700333775568106572820E-02, \
             0.700898401972830440494E-02, \
             0.701424289402572916425E-02, \
             0.701911394845431165171E-02, \
             0.702359678471225911031E-02, \
             0.702769103632498213858E-02, \
             0.703139636865428709508E-02, \
             0.703471247890678765907E-02, \
             0.703763909614153052319E-02, \
             0.704017598127683066242E-02, \
             0.704232292709631209597E-02, \
             0.704407975825415053266E-02, \
             0.704544633127951476780E-02, \
             0.704642253458020417748E-02, \
             0.704700828844548013730E-02, \
             0.704720354504808967346E-02, \
             0.704700828844548013730E-02, \
             0.704642253458020417748E-02, \
             0.704544633127951476780E-02, \
             0.704407975825415053266E-02, \
             0.704232292709631209597E-02, \
             0.704017598127683066242E-02, \
             0.703763909614153052319E-02, \
             0.703471247890678765907E-02, \
             0.703139636865428709508E-02, \
             0.702769103632498213858E-02, \
             0.702359678471225911031E-02, \
             0.701911394845431165171E-02, \
             0.701424289402572916425E-02, \
             0.700898401972830440494E-02, \
             0.700333775568106572820E-02, \
             0.699730456380953992594E-02, \
             0.699088493783425207545E-02, \
             0.698407940325846925786E-02, \
             0.697688851735519545845E-02, \
             0.696931286915342540213E-02, \
             0.696135307942366551493E-02, \
             0.695300980066273063177E-02, \
             0.694428371707782549438E-02, \
             0.693517554456992049848E-02, \
             0.692568603071643155621E-02, \
             0.691581595475321433825E-02, \
             0.690556612755588354803E-02, \
             0.689493739162046825872E-02, \
             0.688393062104341470995E-02, \
             0.687254672150094831613E-02, \
             0.686078663022780697951E-02, \
             0.684865131599535812903E-02, \
             0.683614177908911221841E-02, \
             0.682325905128564571420E-02, \
             0.681000419582894688374E-02, \
             0.679637830740619795480E-02, \
             0.678238251212300746082E-02, \
             0.676801796747810680683E-02, \
             0.675328586233752529078E-02, \
             0.673818741690825799086E-02, \
             0.672272388271144108036E-02, \
             0.670689654255504925648E-02, \
             0.669070671050613006584E-02, \
             0.667415573186258997654E-02, \
             0.665724498312454708217E-02, \
             0.663997587196526532519E-02, \
             0.662234983720168509457E-02, \
             0.660436834876456498276E-02, \
             0.658603290766824937794E-02, \
             0.656734504598007641819E-02, \
             0.654830632678944064054E-02, \
             0.652891834417652442012E-02, \
             0.650918272318071200827E-02, \
             0.648910111976869964292E-02, \
             0.646867522080231481688E-02, \
             0.644790674400605734710E-02, \
             0.642679743793437438922E-02, \
             0.640534908193868098342E-02, \
             0.638356348613413709795E-02, \
             0.636144249136619145314E-02, \
             0.633898796917690165912E-02, \
             0.631620182177103938227E-02, \
             0.629308598198198836688E-02, \
             0.626964241323744217671E-02, \
             0.624587310952490748541E-02, \
             0.622178009535701763157E-02, \
             0.619736542573665996342E-02, \
             0.617263118612191922727E-02, \
             0.614757949239083790214E-02, \
             0.612221249080599294931E-02, \
             0.609653235797888692923E-02, \
             0.607054130083414983949E-02, \
             0.604424155657354634589E-02, \
             0.601763539263978131522E-02, \
             0.599072510668009471472E-02, \
             0.596351302650963502011E-02, \
             0.593600151007459827614E-02, \
             0.590819294541511788161E-02, \
             0.588008975062788803205E-02, \
             0.585169437382850155033E-02, \
             0.582300929311348057702E-02, \
             0.579403701652197628421E-02, \
             0.576478008199711142954E-02, \
             0.573524105734693719020E-02, \
             0.570542254020497332312E-02, \
             0.567532715799029830087E-02, \
             0.564495756786715368885E-02, \
             0.561431645670402467678E-02, \
             0.558340654103215637610E-02, \
             0.555223056700346326850E-02, \
             0.552079131034778706457E-02, \
             0.548909157632945623482E-02, \
             0.545713419970309863995E-02, \
             0.542492204466865704951E-02, \
             0.539245800482555593606E-02, \
             0.535974500312596681161E-02, \
             0.532678599182711857974E-02, \
             0.529358395244259896547E-02, \
             0.526014189569259311205E-02, \
             0.522646286145300596306E-02, \
             0.519254991870341614863E-02, \
             0.515840616547381084096E-02, \
             0.512403472879005351831E-02, \
             0.508943876461803986674E-02, \
             0.505462145780650125058E-02, \
             0.501958602202842039909E-02, \
             0.498433569972103029914E-02, \
             0.494887376202437487201E-02, \
             0.491320350871841897367E-02, \
             0.487732826815870573054E-02, \
             0.484125139721057135214E-02, \
             0.480497628118194150483E-02, \
             0.476850633375474925263E-02, \
             0.473184499691503264714E-02, \
             0.469499574088179046532E-02, \
             0.465796206403469754658E-02, \
             0.462074749284080687482E-02, \
             0.458335558178039420335E-02, \
             0.454578991327213285488E-02, \
             0.450805409759782158001E-02, \
             0.447015177282692726900E-02, \
             0.443208660474124713206E-02, \
             0.439386228676004195260E-02, \
             0.435548253986604343679E-02, \
             0.431695111253279479928E-02, \
             0.427827178065384480959E-02, \
             0.423944834747438184434E-02, \
             0.420048464352596631772E-02, \
             0.416138452656509745764E-02, \
             0.412215188151643401528E-02, \
             0.408279062042157838350E-02, \
             0.404330468239442998549E-02, \
             0.400369803358421688562E-02, \
             0.396397466714742455513E-02, \
             0.392413860322995774660E-02, \
             0.388419388896099560998E-02, \
             0.384414459846013158917E-02, \
             0.380399483285952829161E-02, \
             0.376374872034296338241E-02, \
             0.372341041620379550870E-02, \
             0.368298410292403911967E-02, \
             0.364247399027690353194E-02, \
             0.360188431545532431869E-02, \
             0.356121934322919357659E-02, \
             0.352048336613417922682E-02, \
             0.347968070469521146972E-02, \
             0.343881570768790591876E-02, \
             0.339789275244138669739E-02, \
             0.335691624518616761342E-02, \
             0.331589062145094394706E-02, \
             0.327482034651233969564E-02, \
             0.323370991590184336368E-02, \
             0.319256385597434736790E-02, \
             0.315138672454287935858E-02, \
             0.311018311158427546158E-02, \
             0.306895764002069252174E-02, \
             0.302771496658198544480E-02, \
             0.298645978275408290247E-02, \
             0.294519681581857582284E-02, \
             0.290393082998878368175E-02, \
             0.286266662764757868253E-02, \
             0.282140905069222207923E-02, \
             0.278016298199139435045E-02, \
             0.273893334695947541201E-02, \
             0.269772511525294586667E-02, \
             0.265654330259352828314E-02, \
             0.261539297272236109225E-02, \
             0.257427923948908888092E-02, \
             0.253320726907925325750E-02, \
             0.249218228238276930060E-02, \
             0.245120955750556483923E-02, \
             0.241029443242563417382E-02, \
             0.236944230779380495146E-02, \
             0.232865864987842738864E-02, \
             0.228794899365195972378E-02, \
             0.224731894601603393082E-02, \
             0.220677418916003329194E-02, \
             0.216632048404649142727E-02, \
             0.212596367401472533045E-02, \
             0.208570968849203942640E-02, \
             0.204556454679958293446E-02, \
             0.200553436203751169944E-02, \
             0.196562534503150547732E-02, \
             0.192584380831993546204E-02, \
             0.188619617015808475394E-02, \
             0.184668895851282540913E-02, \
             0.180732881501808930079E-02, \
             0.176812249885838886701E-02, \
             0.172907689054461607168E-02, \
             0.169019899554346019117E-02, \
             0.165149594771914570655E-02, \
             0.161297501254393423070E-02, \
             0.157464359003212166189E-02, \
             0.153650921735128916170E-02, \
             0.149857957106456636214E-02, \
             0.146086246895890987689E-02, \
             0.142336587141720519900E-02, \
             0.138609788229672549700E-02, \
             0.134906674928353113127E-02, \
             0.131228086370221478128E-02, \
             0.127574875977346947345E-02, \
             0.123947911332878396534E-02, \
             0.120348074001265964881E-02, \
             0.116776259302858043685E-02, \
             0.113233376051597664917E-02, \
             0.109720346268191941940E-02, \
             0.106238104885340071375E-02, \
             0.102787599466367326179E-02, \
             0.993697899638760857945E-03, \
             0.959856485506936206261E-03, \
             0.926361595613111283368E-03, \
             0.893223195879324912340E-03, \
             0.860451377808527848128E-03, \
             0.828056364077226302608E-03, \
             0.796048517297550871506E-03, \
             0.764438352543882784191E-03, \
             0.733236554224767912055E-03, \
             0.702453997827572321358E-03, \
             0.672101776960108194646E-03, \
             0.642191235948505088403E-03, \
             0.612734008012225209294E-03, \
             0.583742058714979703847E-03, \
             0.555227733977307579715E-03, \
             0.527203811431658386125E-03, \
             0.499683553312800484519E-03, \
             0.472680758429262691232E-03, \
             0.446209810101403247488E-03, \
             0.420285716355361231823E-03, \
             0.394924138246873704434E-03, \
             0.370141402122251665232E-03, \
             0.345954492129903871350E-03, \
             0.322381020652862389664E-03, \
             0.299439176850911730874E-03, \
             0.277147657465187357459E-03, \
             0.255525589595236862014E-03, \
             0.234592462123925204879E-03, \
             0.214368090034216937149E-03, \
             0.194872642236641146532E-03, \
             0.176126765545083195474E-03, \
             0.158151830411132242924E-03, \
             0.140970302204104791413E-03, \
             0.124606200241498368482E-03, \
             0.109085545645741522051E-03, \
             0.944366322532705527066E-04, \
             0.806899228014035293851E-04, \
             0.678774554733972416227E-04, \
             0.560319507856164252140E-04, \
             0.451863674126296143105E-04, \
             0.353751372055189588628E-04, \
             0.266376412339000901358E-04, \
             0.190213681905875816679E-04, \
             0.125792781889592743525E-04, \
             0.736624069102321668857E-05, \
             0.345456507169149134898E-05, \
             0.945715933950007048827E-06 ] )

  else:

    print ( '' )
    print ( 'PATTERSON_SET(): Fatal error!' )
    print ( '  Illegal input value of N.' )
    print ( '  N must be 1, 3, 7, 15, 31, 63, 127, 255 or 511.' )
    raise Exception ( 'PATTERSON_SET(): Fatal error!' )

  return x, w

def patterson_set_test ( ):

#*****************************************************************************80
#
## patterson_set_test() tests patterson_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n_test = np.array ( [ 1, 3, 7, 15 ] )

  print ( '' )
  print ( 'PATTERSON_SET_test():' )
  print ( '  PATTERSON_SET sets a Patterson quadrature rule.' )
  print ( '' )
  print ( '  Index       X             W' )

  for j in range ( 0, 4 ):

    n = n_test[j]

    x, w = patterson_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

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
## psi_values_test() demonstrates the use of psi_values().
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
  print ( 'PSI_VALUES_TEST:' )
  print ( '  PSI_VALUES stores values of the PSI function.' )
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

def quad_rule_test ( ):

#*****************************************************************************80
#
## quad_rule_test() tests quad_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'quad_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test quad_rule().' )
#
#  Utility functions:
#
  hyper_2f1_values_test ( )
  psi_values_test ( )
  r8_hyper_2f1_test ( )
  r8_psi_test ( )
  r8vec_diff_norm_li_test ( )
  r8vec_indicator1_test ( )
  r8vec_reverse_test ( )
#
#  Library functions:
#
  bashforth_set_test ( )

  chebyshev_set_test ( )

  chebyshev1_compute_test ( )
  chebyshev1_integral_test ( )
  chebyshev1_set_test ( )

  chebyshev2_compute_test ( )
  chebyshev2_integral_test ( )
  chebyshev2_set_test ( )

  chebyshev3_compute_test ( )
  chebyshev3_integral_test ( )
  chebyshev3_set_test ( )

  clenshaw_curtis_compute_test ( )
  clenshaw_curtis_set_test ( )

  fejer1_compute_test ( )
  fejer1_set_test ( )

  fejer2_compute_test ( )
  fejer2_set_test ( )

  gegenbauer_integral_test ( )
  gegenbauer_ss_compute_test ( )

  gen_hermite_ek_compute_test ( )
  gen_hermite_integral_test ( )

  gen_laguerre_ek_compute_test ( )
  gen_laguerre_integral_test ( )

  hermite_ek_compute_test ( )
  hermite_integral_test ( )
  hermite_set_test ( )
  hermite_gk16_set_test ( )
  hermite_gk18_set_test ( )
  hermite_gk22_set_test ( )
  hermite_gk24_set_test ( )
  hermite_1_set_test ( )
  hermite_probabilist_set_test ( )

  imtqlx_test ( )

  jacobi_ek_compute_test ( )
  jacobi_integral_test ( )

  kronrod_set_test ( )

  laguerre_ek_compute_test ( )
  laguerre_integral_test ( )
  laguerre_set_test ( )
  laguerre_1_set_test ( )

  legendre_dr_compute_test ( )
  legendre_ek_compute_test ( )
  legendre_integral_test ( )
  legendre_set_test ( )

  lobatto_compute_test ( )
  lobatto_set_test ( )

  moulton_set_test ( )

  nc_compute_weights_test ( )

  ncc_compute_test ( )
  ncc_set_test ( )

  nco_compute_test ( )
  nco_set_test ( )

  ncoh_compute_test ( )
  ncoh_set_test ( )

  patterson_set_test ( )

  radau_set_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'quad_rule_test():' )
  print ( '  Normal end of execution.' )
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
#    The F77 original version of this routine is copyrighted by
#    Shanjie Zhang and Jianming Jin.  However, they give permission to
#    incorporate this routine into a user program provided that the copyright
#    is acknowledged.
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
    print ( 'R8_HYPER_2F1(): Fatal error!' )
    print ( '  The hypergeometric series is divergent.' )
    print ( '  C is integral and negative.' )
    print ( '  C = %f' % ( c ) )

  if ( l1 ):
    print ( '' )
    print ( 'R8_HYPER_2F1(): Fatal error!' )
    print ( '  The hypergeometric series is divergent.' )
    print ( '  1 = X < 0, C - A - B <= 0.' )
    print ( '  A = %f' % ( a ) )
    print ( '  B = %f' % ( b ) )
    print ( '  C = %f' % ( c ) )
    print ( '  X = %f' % ( x ) )

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
    print ( 'R8_HYPER_2F1 - Warning!' )
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

  print ( '' )
  print ( 'R8_HYPER_2F1_test():' )
  print ( '  R8_HYPER_2F1 evaluates the hypergeometric 2F1 function.' )
  print ( '' )
  print ( '      A       B       C       X       2F1                       2F1                     DIFF' )
  print ( '                                     ' )
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
  print ( '' )
  print ( 'R8_PSI_TEST:' )
  print ( '  R8_PSI evaluates the PSI function.' )
  print ( '' )
  print ( '      X            PSI(X)    R8_PSI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_psi ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )

  return

def r8vec_diff_norm_li ( n, a, b ):

#*****************************************************************************80
#
## r8vec_diff_norm_li() returns the L-infinity norm of the difference of R8VEC's.
#
#  Discussion:
#
#    The vector L-infinity norm is defined as:
#
#      value = max ( 1 <= I <= N ) abs ( A(I) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in A.
#
#    real A(N), B(N), the vectors.
#
#  Output:
#
#    real VALUE, the L-infinity norm of A - B.
#
  value = 0.0
  for i in range ( 0, n ):
    value = max ( value, abs ( a[i] - b[i] ) )

  return value

def r8vec_diff_norm_li_test ( ):

#*****************************************************************************80
#
## r8vec_diff_norm_li_test() tests r8vec_diff_norm_li().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'r8vec_diff_norm_li_test():' )
  print ( '  r8vec_diff_norm_li(): L-infinity norm of the difference' )
  print ( '  of two R8VEC\'s.' )
 
  n = 5
  r8_lo = -10.0
  r8_hi = +10.0

  v1 = r8_lo + ( r8_hi - r8_lo ) * rng.random ( size = n )
  v2 = r8_lo + ( r8_hi - r8_lo ) * rng.random ( size = n )

  r8vec_print ( n, v1, '  Vector V1:' )
  r8vec_print ( n, v2, '  Vector V2:' )

  diff = r8vec_diff_norm_li ( n, v1, v2 )

  print ( '' )
  print ( '  L-Infinity norm of V1-V2: %g' % ( diff ) )

  return

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## r8vec_indicator1() sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
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
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    real A(N), the indicator array.
#
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## r8vec_indicator1_test() tests r8vec_indicator1().
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
  print ( 'r8vec_indicator1_test():' )
  print ( '  r8vec_indicator1() returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print prints an R8VEC.
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

  return

def r8vec_reverse ( n, a1 ):

#*****************************************************************************80
#
## r8vec_reverse() reverses the elements of an R8VEC.
#
#  Example:
#
#    Input:
#
#      N = 5, A = ( 11.0, 12.0, 13.0, 14.0, 15.0 ).
#
#    Output:
#
#      A = ( 15.0, 14.0, 13.0, 12.0, 11.0 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the array.
#
#    real A1(N), the array to be reversed.
#
#  Output:
#
#    real A2(N), the reversed array.
#
  import numpy as np

  a2 = np.zeros ( n )
  for i in range ( 0, n ):
    a2[i] = a1[n-1-i]

  return a2

def r8vec_reverse_test ( ):

#*****************************************************************************80
#
## r8vec_reverse_test() tests r8vec_reverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'r8vec_reverse_test():' )
  print ( '  r8vec_reverse() reverses an R8VEC.' )
 
  a1 = np.zeros ( n )
  for i in range ( 0, n ):
    a1[i] = float ( i + 1 )
 
  r8vec_print ( n, a1, '  Original array:' )

  a2 = r8vec_reverse ( n, a1 )

  r8vec_print ( n, a2, '  Reversed array:' )

  return

def radau_set ( n ):

#*****************************************************************************80
#
## radau_set() sets abscissas and weights for Radau quadrature.
#
#  Discussion:
#
#    The Radau rule is distinguished by the fact that the left endpoint
#    (-1) is always an abscissa.
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    The quadrature rule will integrate exactly all polynomials up to
#    X^(2*N-2).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2005
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
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996,
#    ISBN: 0-8493-2479-3.
#
#  Input:
#
#    integer N, the order.
#    N must be between 1 and 15.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( n == 1 ):

    x = np.array ( [ \
             - 1.0 ] )

    w = np.array ( [ \
             2.0 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
            - 1.0, \
              1.0 / 3.0 ] )

    w = np.array ( [ \
            0.5, \
            1.5 ] )

  elif ( n == 3 ):

    x = np.array ( [ \
             - 1.0, \
             - 0.289897948556635619639456814941, \
               0.689897948556635619639456814941 ] )

    w = np.array ( [ \
            0.222222222222222222222222222222, \
            1.02497165237684322767762689304, \
            0.752806125400934550100150884739 ] )

  elif ( n == 4 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.575318923521694112050483779752, \
              0.181066271118530578270147495862, \
              0.822824080974592105208907712461 ] )

    w = np.array ( [ \
            0.125, \
            0.657688639960119487888578442146, \
            0.776386937686343761560464613780, \
            0.440924422353536750550956944074 ] )

  elif ( n == 5 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.720480271312438895695825837750, \
            - 0.167180864737833640113395337326, \
              0.446313972723752344639908004629, \
              0.885791607770964635613757614892 ] )

    w = np.array ( [ \
            0.08, \
            0.446207802167141488805120436457, \
            0.623653045951482508163709823153, \
            0.562712030298924120384345300681, \
            0.287427121582451882646824439708 ] )

  elif ( n == 6 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.802929828402347147753002204224, \
            - 0.390928546707272189029229647442, \
              0.124050379505227711989974959990, \
              0.603973164252783654928415726409, \
              0.920380285897062515318386619813 ] )

    w = np.array ( [ \
            0.0555555555555555555555555555556, \
            0.319640753220510966545779983796, \
            0.485387188468969916159827915587, \
            0.520926783189574982570229406570, \
            0.416901334311907738959406382743, \
            0.201588385253480840209200755749 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.853891342639482229703747931639, \
            - 0.538467724060109001833766720231, \
            - 0.117343037543100264162786683611, \
              0.326030619437691401805894055838, \
              0.703842800663031416300046295008, \
              0.941367145680430216055899446174 ] )

    w = np.array ( [ \
            0.0408163265306122448979591836735, \
            0.239227489225312405787077480770, \
            0.380949873644231153805938347876, \
            0.447109829014566469499348953642, \
            0.424703779005955608398308039150, \
            0.318204231467301481744870434470, \
            0.148988471112020635866497560418 ] )

  elif ( n == 8 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.887474878926155707068695617935, \
            - 0.639518616526215270024840114382, \
            - 0.294750565773660725252184459658, \
              0.0943072526611107660028971153047, \
              0.468420354430821063046421216613, \
              0.770641893678191536180719525865, \
              0.955041227122575003782349000858 ] )

    w = np.array ( [ \
            0.03125, \
            0.185358154802979278540728972699, \
            0.304130620646785128975743291400, \
            0.376517545389118556572129261442, \
            0.391572167452493593082499534004, \
            0.347014795634501280228675918422, \
            0.249647901329864963257869293513, \
            0.114508814744257199342353728520 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.910732089420060298533757956283, \
            - 0.711267485915708857029562959544, \
            - 0.426350485711138962102627520502, \
            - 0.0903733696068532980645444599064, \
              0.256135670833455395138292079035, \
              0.571383041208738483284917464837, \
              0.817352784200412087992517083851, \
              0.964440169705273096373589797925 ] )

    w = np.array ( [ \
            0.0246913580246913580246913580247, \
            0.147654019046315385819588499802, \
            0.247189378204593052361239794969, \
            0.316843775670437978338000849642, \
            0.348273002772966594071991031186, \
            0.337693966975929585803724239792, \
            0.286386696357231171146705637752, \
            0.200553298024551957421165090417, \
            0.907145049232829170128934984159E-01 ] )

  elif ( n == 10 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.927484374233581078117671398464, \
            - 0.763842042420002599615429776011, \
            - 0.525646030370079229365386614293, \
            - 0.236234469390588049278459503207, \
              0.760591978379781302337137826389E-01, \
              0.380664840144724365880759065541, \
              0.647766687674009436273648507855, \
              0.851225220581607910728163628088, \
              0.971175180702246902734346518378 ] )

    w = np.array ( [ \
            0.02, \
            0.120296670557481631517310522702, \
            0.204270131879000675555788672223, \
            0.268194837841178696058554475262, \
            0.305859287724422621016275475401, \
            0.313582457226938376695902847302, \
            0.290610164832918311146863077963, \
            0.239193431714379713376571966160, \
            0.164376012736921475701681668908, \
            0.736170054867584989310512940790E-01 ] )

  elif ( n == 11 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.939941935677027005913871284731, \
            - 0.803421975580293540697597956820, \
            - 0.601957842073797690275892603234, \
            - 0.351888923353330214714301017870, \
            - 0.734775314313212657461903554238E-01, \
              0.210720306228426314076095789845, \
              0.477680647983087519467896683890, \
              0.705777100713859519144801128840, \
              0.876535856245703748954741265611, \
              0.976164773135168806180508826082 ] )

    w = np.array ( [ \
            0.165289256198347107438016528926E-01, \
            0.998460819079680638957534695802E-01, \
            0.171317619206659836486712649042, \
            0.228866123848976624401683231126, \
            0.267867086189684177806638163355, \
            0.285165563941007337460004408915, \
            0.279361333103383045188962195720, \
            0.250925377697128394649140267633, \
            0.202163108540024418349931754266, \
            0.137033682133202256310153880580, \
            0.609250978121311347072183268883E-01 ] )

  elif ( n == 12 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.949452759204959300493337627077, \
            - 0.833916773105189706586269254036, \
            - 0.661649799245637148061133087811, \
            - 0.444406569781935851126642615609, \
            - 0.196994559534278366455441427346, \
              0.637247738208319158337792384845E-01, \
              0.319983684170669623532789532206, \
              0.554318785912324288984337093085, \
              0.750761549711113852529400825472, \
              0.895929097745638894832914608454, \
              0.979963439076639188313950540264 ] )

    w = np.array ( [ \
            0.138888888888888888888888888888E-01, \
            0.841721349386809762415796536813E-01, \
            0.145563668853995128522547654706, \
            0.196998534826089634656049637969, \
            0.235003115144985839348633985940, \
            0.256991338152707776127974253598, \
            0.261465660552133103438074715743, \
            0.248121560804009959403073107079, \
            0.217868879026192438848747482023, \
            0.172770639313308564306065766966, \
            0.115907480291738392750341908272, \
            0.512480992072692974680229451351E-01 ] )

  elif ( n == 13 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.956875873668299278183813833834, \
            - 0.857884202528822035697620310269, \
            - 0.709105087529871761580423832811, \
            - 0.519197779050454107485205148087, \
            - 0.299201300554509985532583446686, \
            - 0.619016986256353412578604857936E-01, \
              0.178909837597084635021931298881, \
              0.409238231474839556754166331248, \
              0.615697890940291918017885487543, \
              0.786291018233046684731786459135, \
              0.911107073689184553949066402429, \
              0.982921890023145161262671078244 ] )

    w = np.array ( [ \
            0.118343195266272189349112426036E-01, \
            0.719024162924955289397537405641E-01, \
            0.125103834331152358133769287976, \
            0.171003460470616642463758674512, \
            0.206960611455877074631132560829, \
            0.230888862886995434012203758668, \
            0.241398342287691148630866924129, \
            0.237878547660712031342685189180, \
            0.220534229288451464691077164199, \
            0.190373715559631732254759820746, \
            0.149150950090000205151491864242, \
            0.992678068818470859847363877478E-01, \
            0.437029032679020748288533846051E-01 ] )

  elif ( n == 14 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.962779269978024297120561244319, \
            - 0.877048918201462024795266773531, \
            - 0.747389642613378838735429134263, \
            - 0.580314056546874971105726664999, \
            - 0.384202003439203313794083903375, \
            - 0.168887928042680911008441695622, \
              0.548312279917645496498107146428E-01, \
              0.275737205435522399182637403545, \
              0.482752918588474966820418534355, \
              0.665497977216884537008955042481, \
              0.814809550601994729434217249123, \
              0.923203722520643299246334950272, \
              0.985270697947821356698617003172 ] )

    w = np.array ( [ \
            0.102040816326530612244897959184E-01, \
            0.621220169077714601661329164668E-01, \
            0.108607722744362826826720935229, \
            0.149620539353121355950520836946, \
            0.183127002125729654123867302103, \
            0.207449763335175672668082886489, \
            0.221369811499570948931671683021, \
            0.224189348002707794238414632220, \
            0.215767100604618851381187446115, \
            0.196525518452982430324613091930, \
            0.167429727891086278990102277038, \
            0.129939668737342347807425737146, \
            0.859405354429804030893077310866E-01, \
            0.377071632698969142774627282919E-01 ] )

  elif ( n == 15 ):

    x = np.array ( [ \
            - 1.0, \
            - 0.967550468197200476562456018282, \
            - 0.892605400120550767066811886849, \
            - 0.778685617639031079381743321893, \
            - 0.630779478886949283946148437224, \
            - 0.455352905778529370872053455981, \
            - 0.260073376740807915768961188263, \
            - 0.534757226797460641074538896258E-01, \
              0.155410685384859484319182024964, \
              0.357456512022127651195319205174, \
              0.543831458701484016930711802760, \
              0.706390264637572540152679669478, \
              0.838029000636089631215097384520, \
              0.932997190935973719928072142859, \
              0.987166478414363086378359071811 ] )

    w = np.array ( [ \
            0.00888888888888888888888888888889, \
            0.0542027800486444943382142368018, \
            0.0951295994604808992038477266346, \
            0.131875462504951632186262157944, \
            0.162854477303832629448732245828, \
            0.186715145839450908083795103799, \
            0.202415187030618429872703310435, \
            0.209268608147694581430889790306, \
            0.206975960249553755479027321787, \
            0.195637503045116116473556617575, \
            0.175748872642447685670310440476, \
            0.148179527003467253924682058743, \
            0.114135203489752753013075582569, \
            0.0751083927605064397329716653914, \
            0.0328643915845935322530428528231 ] )

  else:

    print ( '' )
    print ( 'RADAU_SET(): Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 to 15.' )
    raise Exception ( 'RADAU_SET(): Fatal error!' )

  return x, w

def radau_set_test ( ):

#*****************************************************************************80
#
## radau_set_test() tests radau_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'radau_set_test():' )
  print ( '  radau_set() sets a Radau rule.' )
  print ( '' )
  print ( '         I            X                  W' )

  for n in range ( 4, 12, 3 ):

    x, w = radau_set ( n )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %8d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )

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

if ( __name__ == '__main__' ):
  timestamp ( )
  quad_rule_test ( )
  timestamp ( )

