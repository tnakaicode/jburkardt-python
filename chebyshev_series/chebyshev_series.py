#! /usr/bin/env python3
#
def chebyshev_series_test ( ):

#*****************************************************************************80
#
## chebyshev_series_test() tests chebyshev_series().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'chebyshev_series_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test chebyshev_series().' )

  chebyshev_series_test01 ( )
  chebyshev_series_test02 ( )
  chebyshev_series_test03 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'chebyshev_series_test():' )
  print ( '  Normal end of execution.' )

  return

def chebyshev_series_test01 ( ):

#*****************************************************************************80
#
## chebyshev_series_test01() considers an even Chebyshev series for EXP(X).
#
#  Discussion:
#
#    Table 5 is from Clenshaw, and contains 18 terms of the Chebyshev
#    series for exp(x) over [-1,+1].
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
  import numpy as np

  nc = 18

  table5 = np.array ( [ \
    2.53213175550401667120, \
    1.13031820798497005442, \
    0.27149533953407656237, \
    0.04433684984866380495, \
    0.00547424044209373265, \
    0.00054292631191394375, \
    0.00004497732295429515, \
    0.00000319843646240199, \
    0.00000019921248066728, \
    0.00000001103677172552, \
    0.00000000055058960797, \
    0.00000000002497956617, \
    0.00000000000103915223, \
    0.00000000000003991263, \
    0.00000000000000142376, \
    0.00000000000000004741, \
    0.00000000000000000148, \
    0.00000000000000000004 ] )

  print ( '' )
  print ( 'chebyshev_series_test01():' )
  print ( '  echebser3() computes a Chebyshev series approximation' )
  print ( '  and the first three derivatives.' )
  print ( '' )
  print ( '  Errors of a Chebyshev series for exp(x)' )
  print ( '' )
  print ( '    x        err(y)       err(y'')       err(y")      err(y"'')' )
  print ( '' )

  for i in range ( -10, 11 ):
    x = i / 10.0
    s, s1, s2, s3 = echebser3 ( x, table5, nc )
    y = np.exp ( x )
    s = s - y
    s1 = s1 - y
    s2 = s2 - y
    s3 = s3 - y
    print ( '%7.4f  %14.6g  %14.6g  %14.6g  %14.6g' % ( x, s, s1, s2, s3 ) )

  return

def chebyshev_series_test02 ( ):

#*****************************************************************************80
#
## chebyshev_series_test02() considers an even Chebyshev series for COS(PI*X/2).
#
#  Discussion:
#
#    TABLE1 contains the even Chebyshev series coefficients for
#    cos(pi*x/2) over [-1,+1].
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
  import numpy as np

  nc = 11

  table1 = np.array ( [ \
    +0.94400243153646953490, \
    -0.49940325827040708740, \
    +0.02799207961754761751, \
    -0.00059669519654884650, \
    +0.00000670439486991684, \
    -0.00000004653229589732, \
    +0.00000000021934576590, \
    -0.00000000000074816487, \
    +0.00000000000000193230, \
    -0.00000000000000000391, \
    +0.00000000000000000001 ] )

  print ( '' )
  print ( 'chebyshev_series_test02():' )
  print ( '  evenchebser2() computes an even Chebyshev series' )
  print ( '  and its first two derivatives.' )
  print ( '' )
  print ( '  Errors of an even Chebyshev series for cos(pi*x/2):' )
  print ( '' )
  print ( '    x        err(y)       err(y'')       err(y")' )
  print ( '' )

  for i in range ( 0, 11 ):
    x = i / 10.0
    s, s1, s2 = evenchebser2 ( x, table1, nc )
    y = np.cos ( 0.5 * np.pi * x )
    y1 = - 0.5 * np.pi * np.sin ( 0.5 * np.pi * x )
    y2 = - 0.25 * np.pi * np.pi * np.cos ( 0.5 * np.pi * x )
    s = s - y
    s1 = s1 - y1
    s2 = s2 - y2
    print ( '%7.4f  %14.6g  %14.6g  %14.6g' % ( x, s, s1, s2 ) )

  return

def chebyshev_series_test03 ( ):

#*****************************************************************************80
#
## chebyshev_series_test03() considers an odd Chebyshev series for SINH(X).
#
#  Discussion:
#
#    TABLE5ODD contains the odd Chebyshev series coefficients for
#    sinh(x) over -1 <= x <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
  import numpy as np

  nc = 9

  table5odd = np.array ( [ \
    1.13031820798497005442, \
    0.04433684984866380495, \
    0.00054292631191394375, \
    0.00000319843646240199, \
    0.00000001103677172552, \
    0.00000000002497956617, \
    0.00000000000003991263, \
    0.00000000000000004741, \
    0.00000000000000000004 ] )

  print ( '' )
  print ( 'chebyshev_series_test03():' )
  print ( '  oddchebser2() computes an odd Chebyshev series approximation.' )
  print ( '  and its first two derivatives.' )
  print ( '' )
  print ( '  Errors of an odd Chebyshev series y(x) approximating sinh(x):' )
  print ( '' )
  print ( '    x        err(y)       err(y'')       err(y")' )
  print ( '' )

  for i in range ( 0, 11 ):
    x = i / 10.0
    s, s1, s2 = oddchebser2 ( x, table5odd, nc )
    y = np.sinh ( x )
    y1 = np.cosh ( x )
    s = s - y
    s1 = s1 - y1
    s2 = s2 - y
    print ( '%7.4f  %14.6g  %14.6g  %14.6g' % ( x, s, s1, s2 ) )

  return

def echebser0 ( x, coef, nc ):

#*****************************************************************************80
#
## echebser0() evaluates a Chebyshev series.
#
#  Discussion:
#
#    This function implements a modification and extension of
#    Maess's algorithm.  Table 6.5.1 on page 164 of the reference
#    gives an example for treating the first derivative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
#    Gerhard Maess,
#    Vorlesungen ueber Numerische Mathematik II, Analysis,
#    Berlin, Akademie_Verlag, 1984-1988,
#    ISBN: 978-3764318840,
#    LC: QA297.M325.
#
#  Input:
#
#    real X, the evaluation point.
#    -1 <= X <= +1.
#
#    real COEF(NC), the Chebyshev series.
#
#    integer NC, the number of terms in the series.
#    0 < NC.
#
#  Output:
#
#    real Y0, the value of the Chebyshev series at X.
#
  b0 = coef[nc-1]
  b1 = 0.0
  b2 = 0.0

  x2 = 2.0 * x

  for i in range ( nc - 2, -1, -1 ):
    b2 = b1
    b1 = b0
    b0 = coef[i] - b2 + x2 * b1

  y0 = 0.5 * ( b0 - b2 )

  return y0

def echebser1 ( x, coef, nc ):

#*****************************************************************************80
#
## echebser1() evaluates a Chebyshev series and first derivative.
#
#  Discussion:
#
#    This function implements a modification and extension of
#    Maess's algorithm.  Table 6.5.1 on page 164 of the reference
#    gives an example for treating the first derivative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
#    Gerhard Maess,
#    Vorlesungen ueber Numerische Mathematik II, Analysis,
#    Berlin, Akademie_Verlag, 1984-1988,
#    ISBN: 978-3764318840,
#    LC: QA297.M325.
#
#  Input:
#
#    real X, the evaluation point.
#    -1 <= X <= +1.
#
#    real COEF(NC), the Chebyshev series.
#
#    integer NC, the number of terms in the series.
#    0 < NC.
#
#  Output:
#
#    real Y0, the value of the Chebyshev series at X.
#
#    real Y1, the value of the 1st derivative of the
#    Chebyshev series at X.
#
  import numpy as np

  b0 = coef[nc-1]
  b1 = 0.0
  b2 = 0.0

  c0 = coef[nc-1]
  c1 = 0.0
  c2 = 0.0

  x2 = 2.0 * x

  for i in range ( nc - 2, -1, -1 ):

    b2 = b1
    b1 = b0
    b0 = coef[i] - b2 + x2 * b1

    if ( 0 < i ):
      c2 = c1
      c1 = c0
      c0 = b0 - c2 + x2 * c1

  y0 = 0.5 * ( b0 - b2 )
  y1 = c0 - c2

  return y0, y1

def echebser2 ( x, coef, nc ):

#*****************************************************************************80
#
## echebser2() evaluates a Chebyshev series and two derivatives.
#
#  Discussion:
#
#    This function implements a modification and extension of
#    Maess's algorithm.  Table 6.5.1 on page 164 of the reference
#    gives an example for treating the first derivative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
#    Gerhard Maess,
#    Vorlesungen ueber Numerische Mathematik II, Analysis,
#    Berlin, Akademie_Verlag, 1984-1988,
#    ISBN: 978-3764318840,
#    LC: QA297.M325.
#
#  Input:
#
#    real X, the evaluation point.
#    -1 <= X <= +1.
#
#    real COEF(NC), the Chebyshev series.
#
#    integer NC, the number of terms in the series.
#    0 < NC.
#
#  Output:
#
#    real Y0, the value of the Chebyshev series at X.
#
#    real Y1, the value of the 1st derivative of the
#    Chebyshev series at X.
#
#    real Y2, the value of the 2nd derivative of the
#    Chebyshev series at X.
#
  b0 = coef[nc-1]
  b1 = 0.0
  b2 = 0.0
  c0 = coef[nc-1]
  c1 = 0.0
  c2 = 0.0
  d0 = coef[nc-1]
  d1 = 0.0
  d2 = 0.0

  x2 = 2.0 * x

  for i in range ( nc - 2, -1, -1 ):

    b2 = b1
    b1 = b0
    b0 = coef[i] - b2 + x2 * b1

    if ( 0 < i ):
      c2 = c1
      c1 = c0
      c0 = b0 - c2 + x2 * c1

    if ( 1 < i ):
      d2 = d1
      d1 = d0
      d0 = c0 - d2 + x2 * d1

  y0 = 0.5 * ( b0 - b2 )
  y1 = c0 - c2
  y2 = ( d0 - d2 ) * 4.0

  return y0, y1, y2

def echebser3 ( x, coef, nc ):

#*****************************************************************************80
#
## echebser3() evaluates a Chebyshev series and three derivatives.
#
#  Discussion:
#
#    This function implements a modification and extension of
#    Maess's algorithm.  Table 6.5.1 on page 164 of the reference
#    gives an example for treating the first derivative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
#    Gerhard Maess,
#    Vorlesungen ueber Numerische Mathematik II, Analysis,
#    Berlin, Akademie_Verlag, 1984-1988,
#    ISBN: 978-3764318840,
#    LC: QA297.M325.
#
#  Input:
#
#    real X, the evaluation point.
#    -1 <= X <= +1.
#
#    real COEF(NC), the Chebyshev series.
#
#    integer NC, the number of terms in the series.
#    0 < NC.
#
#  Output:
#
#    real Y0, the value of the Chebyshev series at X.
#
#    real Y1, the value of the 1st derivative of the
#    Chebyshev series at X.
#
#    real Y2, the value of the 2nd derivative of the
#    Chebyshev series at X.
#
#    real Y3, the value of the 3rd derivative of the
#    Chebyshev series at X.
#
  b0 = coef[nc-1]
  b1 = 0.0
  b2 = 0.0
  c0 = coef[nc-1]
  c1 = 0.0
  c2 = 0.0
  d0 = coef[nc-1]
  d1 = 0.0
  d2 = 0.0
  e0 = coef[nc-1]
  e1 = 0.0
  e2 = 0.0

  x2 = 2.0 * x

  for i in range ( nc - 2, -1, -1 ):

    b2 = b1
    b1 = b0
    b0 = coef[i] - b2 + x2 * b1

    if ( 0 < i ):
      c2 = c1
      c1 = c0
      c0 = b0 - c2 + x2 * c1

    if ( 1 < i ):
      d2 = d1
      d1 = d0
      d0 = c0 - d2 + x2 * d1

    if ( 2 < i ):
      e2 = e1
      e1 = e0
      e0 = d0 - e2 + x2 * e1

  y0 = 0.5 * ( b0 - b2 )
  y1 = c0 - c2
  y2 = ( d0 - d2 ) * 4.0
  y3 = ( e0 - e2 ) * 24.0

  return y0, y1, y2, y3

def echebser4 ( x, coef, nc ):

#*****************************************************************************80
#
## echebser4() evaluates a Chebyshev series and four derivatives.
#
#  Discussion:
#
#    This function implements a modification and extension of
#    Maess's algorithm.  Table 6.5.1 on page 164 of the reference
#    gives an example for treating the first derivative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
#    Gerhard Maess,
#    Vorlesungen ueber Numerische Mathematik II, Analysis,
#    Berlin, Akademie_Verlag, 1984-1988,
#    ISBN: 978-3764318840,
#    LC: QA297.M325.
#
#  Input:
#
#    real X, the evaluation point.
#    -1 <= X <= +1.
#
#    real COEF(NC), the Chebyshev series.
#
#    integer NC, the number of terms in the series.
#    0 < NC.
#
#  Output:
#
#    real Y0, Y1, Y2, Y3, Y4, the value of the 
#    Chebyshev series and its first four derivatives at X.
#
  b0 = coef[nc-1]
  b1 = 0.0
  b2 = 0.0
  c0 = coef[nc-1]
  c1 = 0.0
  c2 = 0.0
  d0 = coef[nc-1]
  d1 = 0.0
  d2 = 0.0
  e0 = coef[nc-1]
  e1 = 0.0
  e2 = 0.0
  f0 = coef[nc-1]
  f1 = 0.0
  f2 = 0.0

  for i in range ( nc - 2, -1, -1 ):

    b2 = b1
    b1 = b0
    b0 = coef[i] - b2 + 2.0 * x * b1

    if ( 0 < i ):
      c2 = c1
      c1 = c0
      c0 = b0 - c2 + 2.0 * x * c1

    if ( 1 < i ):
      d2 = d1
      d1 = d0
      d0 = c0 - d2 + 2.0 * x * d1

    if ( 2 < i ):
      e2 = e1
      e1 = e0
      e0 = d0 - e2 + 2.0 * x * e1

    if ( 3 < i ):
      f2 = f1
      f1 = f0
      f0 = e0 - f2 + 2.0 * x * f1

  y0 = ( b0 - b2 )        / 2.0
  y1 =   c0 - c2
  y2 = ( d0 - d2 ) *  2.0 * 2.0
  y3 = ( e0 - e2 ) *  6.0 * 4.0
  y4 = ( f0 - f2 ) * 24.0 * 8.0

  return y0, y1, y2, y3, y4

def evenchebser0 ( x, coef, nc ):

#*****************************************************************************80
#
## evenchebser0() evaluates an even Chebyshev series.
#
#  Discussion:
#
#    This function implements Clenshaw's modification of his
#    algorithm for even series.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
#    Gerhard Maess,
#    Vorlesungen ueber Numerische Mathematik II, Analysis,
#    Berlin, Akademie_Verlag, 1984-1988,
#    ISBN: 978-3764318840,
#    LC: QA297.M325.
#
#  Input:
#
#    real X, the evaluation point.
#    -1 <= X <= +1.
#
#    real COEF(NC), the Chebyshev series.
#
#    integer NC, the number of terms in the series.
#    0 < NC.
#
#  Output:
#
#    real Y0, the value of the Chebyshev series at X.
#
  b0 = coef[nc-1]
  b1 = 0.0
  b2 = 0.0

  x2 = 4.0 * x * x - 2.0

  for i in range ( nc - 2, -1, -1 ):

    b2 = b1
    b1 = b0
    b0 = coef[i] - b2 + x2 * b1

  y0 = 0.5 * ( b0 - b2 )

  return y0

def evenchebser1 ( x, coef, nc ):

#*****************************************************************************80
#
## evenchebser1() evaluates an even Chebyshev series and first derivative.
#
#  Discussion:
#
#    This function implements a modification and extension of
#    Maess's algorithm.  Table 6.5.1 on page 164 of the reference
#    gives an example for treating the first derivative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2014
#
#  Author:
#
#    12 March 2026
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
#    Gerhard Maess,
#    Vorlesungen ueber Numerische Mathematik II, Analysis,
#    Berlin, Akademie_Verlag, 1984-1988,
#    ISBN: 978-3764318840,
#    LC: QA297.M325.
#
#  Input:
#
#    real X, the evaluation point.
#    -1 <= X <= +1.
#
#    real COEF(NC), the Chebyshev series.
#
#    integer NC, the number of terms in the series.
#    0 < NC.
#
#  Output:
#
#    real Y0, the value of the Chebyshev series at X.
#
#    real Y1, the value of the 1st derivative of the
#    Chebyshev series at X.
#
  b0 = coef[nc-1]
  b1 = 0.0
  b2 = 0.0
  c0 = coef[nc-1]
  c1 = 0.0
  c2 = 0.0

  x2 = 4.0 * x * x - 2.0

  for i in range ( nc - 2, -1, -1 ):

    b2 = b1
    b1 = b0
    b0 = coef[i] - b2 + x2 * b1

    if ( 0 < i ):
      c2 = c1
      c1 = c0
      c0 = b0 - c2 + x2 * c1

  y0 = 0.5 * ( b0 - b2 )
  y1 = ( c0 - c2 ) * 4.0 * x

  return y0, y1

def evenchebser2 ( x, coef, nc ):

#*****************************************************************************80
#
## evenchebser2() evaluates an even Chebyshev series and first two derivatives.
#
#  Discussion:
#
#    This function implements a modification and extension of
#    Maess's algorithm.  Table 6.5.1 on page 164 of the reference
#    gives an example for treating the first derivative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
#    Gerhard Maess,
#    Vorlesungen ueber Numerische Mathematik II, Analysis,
#    Berlin, Akademie_Verlag, 1984-1988,
#    ISBN: 978-3764318840,
#    LC: QA297.M325.
#
#  Input:
#
#    real X, the evaluation point.
#    -1 <= X <= +1.
#
#    real COEF(NC), the Chebyshev series.
#
#    integer NC, the number of terms in the series.
#    0 < NC.
#
#  Output:
#
#    real Y0, the value of the Chebyshev series at X.
#
#    real Y1, the value of the 1st derivative of the
#    Chebyshev series at X.
#
#    real Y2, the value of the 2nd derivative of the
#    Chebyshev series at X.
#
  b0 = coef[nc-1]
  b1 = 0.0
  b2 = 0.0
  c0 = coef[nc-1]
  c1 = 0.0
  c2 = 0.0
  d0 = coef[nc-1]
  d1 = 0.0
  d2 = 0.0

  x2 = 4.0 * x * x - 2.0

  for i in range ( nc - 2, -1, -1 ):

    b2 = b1
    b1 = b0
    b0 = coef[i] - b2 + x2 * b1

    if ( 0 < i ):
      c2 = c1
      c1 = c0
      c0 = b0 - c2 + x2 * c1

    if ( 1 < i ):
      d2 = d1
      d1 = d0
      d0 = c0 - d2 + x2 * d1

  y0 = 0.5 * ( b0 - b2 )
  y1 = ( c0 - c2 ) * 4.0 * x
  y2 = ( d0 - d2 ) * 64.0 * x * x + ( c0 - c2 ) * 4.0

  return y0, y1, y2

def oddchebser0 ( x, coef, nc ):

#*****************************************************************************80
#
## oddchebser0() evaluates an odd Chebyshev series.
#
#  Discussion:
#
#    This function implements Clenshaw's modification of his algorithm
#    for odd series.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
#  Input:
#
#    real X, the evaluation point.
#    -1 <= X <= +1.
#
#    real COEF(NC), the Chebyshev series.
#
#    integer NC, the number of terms in the series.
#    0 < NC.
#
#  Output:
#
#    real Y0, the value of the Chebyshev series at X.
#
  b0 = coef[nc-1]
  b1 = 0.0
  b2 = 0.0

  x2 = 4.0 * x * x - 2.0

  for i in range ( nc - 2, -1, -1 ):

    b2 = b1
    b1 = b0
    b0 = coef[i] - b2 + x2 * b1

  y0 = ( b0 - b1 ) * x

  return y0

def oddchebser1 ( x, coef, nc ):

#*****************************************************************************80
#
## oddchebser1() evaluates an odd Chebyshev series and the first derivative.
#
#  Discussion:
#
#    This function implements a modification and extension of
#    Clenshaw's algorithm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
#    Gerhard Maess,
#    Vorlesungen ueber Numerische Mathematik II, Analysis,
#    Berlin, Akademie_Verlag, 1984-1988,
#    ISBN: 978-3764318840,
#    LC: QA297.M325.
#
#  Input:
#
#    real X, the evaluation point.
#    -1 <= X <= +1.
#
#    real COEF(NC), the Chebyshev series.
#
#    integer NC, the number of terms in the series.
#    0 < NC.
#
#  Output:
#
#    real Y0, the value of the Chebyshev series at X.
#
#    real Y1, the value of the 1st derivative of the
#    Chebyshev series at X.
#
  coefi = 2.0 * coef[nc-1]
  b0 = coefi
  b1 = 0.0
  b2 = 0.0
  c0 = coefi
  c1 = 0.0
  c2 = 0.0

  x2 = 4.0 * x * x - 2.0

  for i in range ( nc - 2, -1, -1 ):

    b2 = b1
    b1 = b0
    coefi = 2.0 * coef[i] - coefi
    b0 = coefi - b2 + x2 * b1

    if ( 0 < i ):
      c2 = c1
      c1 = c0
      c0 = b0 - c2 + x2 * c1

  y0 = ( b0 - b2 ) * 0.5 * x
  y1 = ( c0 - c2 ) * 4.0 * x * x + ( b0 - b2 ) * 0.5

  return y0, y1

def oddchebser2 ( x, coef, nc ):

#*****************************************************************************80
#
## oddchebser2() evaluates an odd Chebyshev series and first two derivatives.
#
#  Discussion:
#
#    This function implements a modification and extension of
#    Clenshaw's algorithm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    Original Fortran version by Manfred Zimmer.
#    This version by John Burkardt.
#
#  Reference:
#
#    Charles Clenshaw,
#    Mathematical Tables, Volume 5,
#    Chebyshev series for mathematical functions,
#    London, 1962.
#
#    Gerhard Maess,
#    Vorlesungen ueber Numerische Mathematik II, Analysis,
#    Berlin, Akademie_Verlag, 1984-1988,
#    ISBN: 978-3764318840,
#    LC: QA297.M325.
#
#  Input:
#
#    real X, the evaluation point.
#    -1 <= X <= +1.
#
#    real COEF(NC), the Chebyshev series.
#
#    integer NC, the number of terms in the series.
#    0 < NC.
#
#  Output:
#
#    real Y0, the value of the Chebyshev series at X.
#
#    real Y1, the value of the 1st derivative of the
#    Chebyshev series at X.
#
#    real Y2, the value of the 2nd derivative of the
#    Chebyshev series at X.
#
  coefi = 2.0 * coef[nc-1]
  b0 = coefi
  b1 = 0.0
  b2 = 0.0
  c0 = coefi
  c1 = 0.0
  c2 = 0.0
  d0 = coefi
  d1 = 0.0
  d2 = 0.0

  x2 = 4.0 * x * x - 2.0

  for i in range ( nc - 2, -1, -1 ):

    b2 = b1
    b1 = b0
    coefi = 2.0 * coef[i] - coefi
    b0 = coefi - b2 + x2 * b1

    if ( 0 < i ):
      c2 = c1
      c1 = c0
      c0 = b0 - c2 + x2 * c1
 
    if ( 1 < i ):
      d2 = d1
      d1 = d0
      d0 = c0 - d2 + x2 * d1

  x2 = x * x

  y0 = ( b0 - b2 ) * 0.5 * x
  y1 = ( c0 - c2 ) * 4.0 * x2 + ( b0 - b2 ) * 0.5
  y2 = ( ( d0 - d2 ) * 64.0 * x2 + ( c0 - c2 ) * 12.0 ) * x

  return y0, y1, y2

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
  chebyshev_series_test ( )
  timestamp ( )

