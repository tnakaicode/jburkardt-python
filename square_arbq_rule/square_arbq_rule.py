#! /usr/bin/env python3
#
def square_arbq_rule_test ( ):

#*****************************************************************************80
#
## square_arbq_rule_test() tests square_arbq_rule().
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'square_arbq_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test square_arbq_rule().' )

  degree = 8
  n = square_arbq_size ( degree )
  header = 'square08'

  square_arbq_rule_test01 ( degree, n )

  square_arbq_rule_test02 ( degree, n, header )

  square_arbq_rule_test04 ( degree, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'square_arbq_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def square_arbq_rule_test01 ( degree, n ):

#*****************************************************************************80
#
## square_arbq_rule_test01() calls square_arbq() for a quadrature rule of given order.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer DEGREE, the desired total polynomial degree exactness
#    of the quadrature rule.
#
#    integer N, the number of nodes.
#
  import numpy as np

  print ( '' )
  print ( 'square_arbq_rule_test01():' )
  print ( '  Symmetric quadrature rule for a square.' )
  print ( '  Polynomial exactness degree DEGREE = ', degree )

  area = 4.0
#
#  Retrieve and print a symmetric quadrature rule.
#
  x, w = square_arbq ( degree, n )

  print ( '' )
  print ( '  Number of nodes N = ', n )

  print ( '' )
  print ( '     I  W       X       Y' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %14.6g  %14.6g  %14.6g' % ( i, w[i], x[i,0], x[i,1] ) )

  d = np.sum ( w )

  print ( '   Sum  ', d )
  print ( '  Area  ', area )

  return

def square_arbq_rule_test02 ( degree, n, header ):

#*****************************************************************************80
#
## square_arbq_rule_test02() gets a rule and writes it to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer DEGREE, the desired total polynomial degree exactness
#    of the quadrature rule.  0 <= DEGREE <= 50.
#
#    integer N, the number of nodes to be used by the rule.
#
#    string HEADER, an identifier for the filenames.
#
  print ( '' )
  print ( 'square_arbq_rule_test02():' )
  print ( '  Get a quadrature rule for the symmetric square.' )
  print ( '  Then write it to a file.' )
  print ( '  Polynomial exactness degree DEGREE = ', degree )
#
#  Retrieve a symmetric quadrature rule.
#
  x, w = square_arbq ( degree, n )
#
#  Write the points and weights to a file.
#
  filename = header + '.txt'

  output = open ( filename, 'w' )
  for i in range ( 0, n ):
    output.write ( '  %g  %g  %g\n' % ( x[i,0], x[i,1], w[i] ) )
  output.close ( )

  print ( '' )
  print ( '  Quadrature rule written to file "' + filename + '"' )

  return

def square_arbq_rule_test04 ( degree, n ):

#*****************************************************************************80
#
## square_arbq_rule_test04() gets a rule and tests its accuracy.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer DEGREE, the desired total polynomial degree exactness
#    of the quadrature rule.  0 <= DEGREE <= 50.
#
#    integer N, the number of nodes to be used by the rule.
#
  import numpy as np

  print ( '' )
  print ( 'square_arbq_rule_test04():' )
  print ( '  Get a quadrature rule for the symmetric square.' )
  print ( '  Test its accuracy.' )
  print ( '  Polynomial exactness degree DEGREE = ', degree )
#
#  Retrieve a symmetric quadrature rule.
#
  x, w = square_arbq ( degree, n )

  npols = int ( ( ( degree + 1 ) * ( degree + 2 ) ) // 2 )

  rints = np.zeros ( npols )

  for i in range ( 0, n ):
    pols = lege2eva ( degree, x[i,:] )
    rints = rints + w[i] * pols
 
  area = 4.0

  d = 0.0
  d = ( rints[0] - np.sqrt ( area ) )**2
  for i in range ( 1, npols ):
    d = d + rints[i]**2
  d = np.sqrt ( d ) / npols

  print ( '' )
  print ( '  RMS error = ', d )

  return

def lege2eva ( degree, z ):

#*****************************************************************************80
#
## lege2eva() evaluates orthogonal polynomials on the symmetric square.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer DEGREE, the maximum degree of the polynomials.
#
#    real Z(2), the evaluation point.
#
#  Output:
#
#    real POLS((DEGREE+1)*(DEGREE+2)/2), the orthogonal
#    polynomials evaluated at Z.
#
  import numpy as np

  npols = int ( ( ( degree + 1 ) * ( degree + 2 ) ) // 2 )
  pols = np.zeros ( npols )

  f1 = llegepols1 ( degree, z[0] )
  f2 = llegepols1 ( degree, z[1] )

  kk = 0
  for m in range ( 0, degree + 1 ):
    for n in range ( 0, m + 1 ):
      pols[kk] = f1[m-n] * f2[n]
      scale = ( 1 + 2 * n ) * ( 1 + 2 * ( m - n ) )
      scale = 0.5 * np.sqrt ( scale )
      pols[kk] = pols[kk] * scale
      kk = kk + 1

  return pols

def llegepols1 ( degree, x ):

#*****************************************************************************80
#
## llegepols1() evaluates orthogonal polynomials on the symmetric interval.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer DEGREE, the maximum degree.
#
#    real X, the evaluation point.
#
#  Output:
#
#    real POLS(DEGREE+1)), the orthogonal
#    polynomials evaluated at X.
#
  import numpy as np

  pols = np.zeros ( degree + 1 )

  pkp1 = 1.0
  pols[0] = pkp1

  if ( degree == 0 ):
    return pols

  pk = pkp1
  pkp1 = x
  pols[1] = pkp1

  if ( degree == 1 ):
    return pols
 
  for k in range ( 1, degree ):

    pkm1 = pk
    pk = pkp1
    pkp1 = ( ( 2 * k + 1 ) * x * pk \
           - (     k     ) * pkm1 ) \
           / (     k + 1 )

    pols[k+1] = pkp1

  return pols

def rule01 ( n ):

#*****************************************************************************80
#
## rule01() returns the rule of degree 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
       0.00000000000000000 ] )
  ys = np.array ( [ \
       0.00000000000000000 ] )
  ws = np.array ( [ \
       0.2828427124746189E+01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule02 ( n ):

#*****************************************************************************80
#
## rule02() returns the rule of degree 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.6700319885140564, 0.6424528854269665, \
    -0.5079273596590297 ] )
  ys = np.array ( [ \
    -0.8727274074699508, 0.8751842913892396, \
    -0.8014238374817481E-02 ] )
  ws = np.array ( [ \
    0.6106555690526828, 0.6235399890121793, \
    0.1594231566681328E+01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule03 ( n ):

#*****************************************************************************80
#
## rule03() returns the rule of degree 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.5773502691896256,  0.5773502691896260, \
     0.5773502691896256, -0.5773502691896260 ] )
  ys = np.array ( [ \
    -0.5773502691896260, -0.5773502691896256, \
     0.5773502691896260,  0.5773502691896256 ] )
  ws = np.array ( [ \
    0.7071067811865476, 0.7071067811865476, \
    0.7071067811865476, 0.7071067811865476 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule04 ( n ):

#*****************************************************************************80
#
## rule04() returns the rule of degree 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.8434867168489557,0.7481765370372371, \
    -0.4061851500656107,-0.4581090172172534, \
    0.1816993641713940,-0.9077196977637252 ] )
  ys = np.array ( [ \
    0.7332250861965538,-0.6280294280975105, \
    -0.7973798546121016,0.8743017248509551, \
    0.1628466016041256,0.8506794801388022E-02 ] )
  ws = np.array ( [ \
    0.2754640609309160,0.4372667066134153, \
    0.4966805368802857,0.3707670373943532, \
    0.8675752571634261,0.3806735257637942 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule05 ( n ):

#*****************************************************************************80
#
## rule05() returns the rule of degree 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
     0.1775868202077551E-01, -0.1775868202077539E-01, \
     0.7788710544649639,  -0.7788710544649639, \
    -0.7703781288541645,  0.7703781288541645, \
    -0.7490353914168658E-33 ] )
  ys = np.array ( [ \
    -0.9659285494001192,  0.9659285494001192, \
    -0.5715708301251639,  0.5715708301251639, \
    -0.5829672991828014,  0.5829672991828014, \
     0.1356144833394667E-33 ] )
  ws = np.array ( [ \
     0.2246199725165690,  0.2246199725165690, \
     0.3901817339168917,  0.3901817339168917, \
     0.3953508381187504,  0.3953508381187504, \
     0.8081220356417684 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule06 ( n ):

#*****************************************************************************80
#
## rule06() returns the rule of degree 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.7347550761673839,0.8662152988634034, \
    0.1596873653424614,-0.8905137714296896, \
    -0.1469707846748791,0.9240009259977663, \
    -0.8463324986375500,-0.4086308482879689, \
    0.5175294652720337,0.4801002492857063 ] )
  ys = np.array ( [ \
    0.8933891941643415,-0.7037359670513631, \
    -0.9085856749287847,0.1644347368502312, \
    0.5352177835541986,0.4879643750888035, \
    -0.8394767448218339,-0.4262330870004397, \
    0.9176357850707917,-0.1009764561823168 ] )
  ws = np.array ( [ \
    0.1541850714382379,0.1900556513689156, \
    0.2246942645703077,0.2465847648329768, \
    0.5062382287542438,0.1829226437278864, \
    0.1373586623279704,0.4754388545735908, \
    0.1856913242244974,0.5252576589275637 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule07 ( n ):

#*****************************************************************************80
#
## rule07() returns the rule of degree 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.4595981103653579E-16,  0.9258200997725515, \
    0.6742045114073804E-16, -0.9258200997725515, \
    -0.3805544332083157,      0.3805544332083157, \
    0.3805544332083157,-0.3805544332083157, \
    -0.8059797829185990,0.8059797829185988, \
    0.8059797829185990,-0.8059797829185988 ] )
  ys = np.array ( [ \
    -0.9258200997725515, -0.1073032005210112E-16, \
    0.9258200997725515, 0.1241105822293750E-15, \
    -0.3805544332083157, -0.3805544332083157, \
    0.3805544332083157, 0.3805544332083157, \
    -0.8059797829185988, -0.8059797829185990, \
    0.8059797829185988, 0.8059797829185990 ] )
  ws = np.array ( [ \
    0.1711023816204485,0.1711023816204485, \
    0.1711023816204485,0.1711023816204485, \
    0.3681147816131979,0.3681147816131979, \
    0.3681147816131979,0.3681147816131979, \
    0.1678896179529011,0.1678896179529011, \
    0.1678896179529011,0.1678896179529011 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule08 ( n ):

#*****************************************************************************80
#
## rule08() returns the rule of degree 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.2272218649369121,0.2786782798124801, \
    0.9215721988395638,-0.5229427015551803, \
    0.8309170589376613,-0.6080254018462903, \
    -0.9822549066167084,0.4959470731361600E-01, \
    0.5910013957537859,0.3626589212754838, \
    -0.9369162594801185,-0.8850131220663160, \
    -0.1934658240272289,0.5772453681919104, \
    0.9213070164035271,-0.7176037958340967 ] )
  ys = np.array ( [ \
    0.8703146041404044,0.9856262640199153, \
    0.2224095500358621,-0.9282264259882677, \
    0.8435111761265234,0.5825946042673711, \
    -0.8211266831948021,-0.6917239446781449, \
    -0.2614406969784849,0.5198121135620160, \
    0.2153771996329335,0.9090384216207131, \
    0.3526321874643216E-01,-0.9622555555961493, \
    -0.7082682674817122,-0.4130619139730907 ] )
  ws = np.array ( [ \
    0.1444235515837947,0.5206905878850610E-01, \
    0.1365819925705312,0.1136963049256808, \
    0.1156201396846171,0.2194056396025883, \
    0.4570142629159132E-01,0.3040158377300561, \
    0.3227772111095287,0.3341175763908440, \
    0.1202823186503543,0.6155232134515501E-01, \
    0.4037250536437860,0.8510021531985533E-01, \
    0.1026971066172272,0.2666613704920739 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule09 ( n ):

#*****************************************************************************80
#
## rule09() returns the rule of degree 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.7502770999789001,-0.7502770999789001, \
    -0.9279616459595694,0.9279616459595694, \
    0.6306801197316682,-0.6306801197316682, \
    0.9688499663619775,-0.9688499663619775, \
    -0.7620832819261721E-01,0.7620832819261719E-01, \
    0.8526157293336627,-0.8526157293336627, \
    0.4533398211356476,-0.5237358202144297, \
    0.5237358202144297,-0.4533398211356476, \
    -0.7154960467453349E-17 ] )
  ys = np.array ( [ \
    -0.9279616459595700,0.9279616459595700, \
    -0.7502770999789009,0.7502770999789010, \
    0.9688499663619778,-0.9688499663619778, \
    -0.6306801197316696,0.6306801197316697, \
    0.8526157293336619,-0.8526157293336618, \
    0.7620832819261708E-01,-0.7620832819261709E-01, \
    0.5237358202144290,0.4533398211356468, \
    -0.4533398211356468,-0.5237358202144290, \
    -0.1536427274631298E-17 ] )
  ws = np.array ( [ \
    0.7926638883415150E-01,0.7926638883415155E-01, \
    0.7926638883415171E-01,0.7926638883415174E-01, \
    0.6284721101179108E-01,0.6284721101179105E-01, \
    0.6284721101179126E-01,0.6284721101179125E-01, \
    0.1902480253324007,0.1902480253324007, \
    0.1902480253324001,0.1902480253324001, \
    0.2816282136297291,0.2816282136297291, \
    0.2816282136297291,0.2816282136297291, \
    0.3724677695139016 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule10 ( n ):

#*****************************************************************************80
#
## rule10() returns the rule of degree 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
     -0.9853833119314600, \
     -0.9262105001258388, \
     -0.9119588710357346, \
     -0.8792348043990323, \
      0.7551269206143556, \
     -0.3188453596839296, \
     -0.6474946981752547, \
      0.9492191314088700, \
     -0.6188661913929927, \
     -0.9215290755789827, \
     -0.1043123255663635, \
      0.9707183739677747, \
      0.9246684242905355, \
     -0.1655785251003832, \
     -0.1844717206212201, \
      0.6666473305982110, \
     -0.6115967830349248, \
      0.3187935759364068, \
      0.3663139167806795, \
      0.2105273891482153, \
      0.7631114939243835, \
      0.6258661935323967 ] )
  ys = np.array ( [ \
      0.6240243795898477, \
     -0.9577495916000753, \
      0.2065013461988724, \
      0.9225481682574119, \
     -0.9538019223425510, \
      0.9406185571992116, \
      0.6476354842626755, \
      0.1142951736422384, \
     -0.1073322786510873, \
     -0.5089131904296068, \
     -0.9663420836873585, \
     -0.7529656324799600, \
      0.8117151060164874, \
     -0.4732489884927658, \
      0.3507267260891900, \
      0.4711392149070170, \
     -0.8103749226019182, \
     -0.3211002312038632E-01, \
     -0.7605065507139738, \
      0.7788254159831852, \
     -0.3924748753960959, \
      0.9817119264047970 ] )
  ws = np.array ( [ \
      0.2360826549495683E-01, \
      0.2437222107469133E-01, \
      0.9518348391179431E-01, \
      0.4422100229516362E-01, \
      0.5077443794275623E-01, \
      0.8474079765068482E-01, \
      0.1630376427353708, \
      0.8387536029255430E-01, \
      0.2227307039000182, \
      0.9431200171676321E-01, \
      0.6925434184055250E-01, \
      0.4179721982807350E-01, \
      0.6271061498530471E-01, \
      0.2628440705130901, \
      0.2744383764593098, \
      0.2007889259004832, \
      0.1415509025856471, \
      0.2886706704866435, \
      0.1841475599924024, \
      0.1879992823185209, \
      0.1826311110112870, \
      0.4473813181012295E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule11 ( n ):

#*****************************************************************************80
#
## rule11() returns the rule of degree 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.1885861387186414,0.9535395282015320, \
    -0.1885861387186413,-0.9535395282015320, \
    -0.6980761045495679,0.9826392235408555, \
    0.6980761045495681,-0.9826392235408555, \
    -0.9394863828167370,0.8257758359029639, \
    0.9394863828167370,-0.8257758359029637, \
    -0.7120019130753364,0.5253202503645475, \
    0.7120019130753364,-0.5253202503645475, \
    -0.3156234329152547,0.8125205483048131, \
    0.3156234329152548,-0.8125205483048131, \
    -0.4248472488486694,0.4165807191202203E-01, \
    0.4248472488486694,-0.4165807191202197E-01 ] )
  ys = np.array ( [ \
    -0.9535395282015320,0.1885861387186414, \
    0.9535395282015320,-0.1885861387186413, \
    -0.9826392235408555,-0.6980761045495680, \
    0.9826392235408555,0.6980761045495683, \
    -0.8257758359029640,-0.9394863828167370, \
    0.8257758359029638,0.9394863828167370, \
    -0.5253202503645475,-0.7120019130753364, \
    0.5253202503645475,0.7120019130753364, \
    -0.8125205483048131,-0.3156234329152547, \
    0.8125205483048131,0.3156234329152549, \
    -0.4165807191202205E-01,-0.4248472488486694, \
    0.4165807191202200E-01,0.4248472488486694 ] )
  ws = np.array ( [ \
    0.6886285066821880E-01,0.6886285066821880E-01, \
    0.6886285066821880E-01,0.6886285066821880E-01, \
    0.3395580740305121E-01,0.3395580740305121E-01, \
    0.3395580740305121E-01,0.3395580740305121E-01, \
    0.4671948489426224E-01,0.4671948489426224E-01, \
    0.4671948489426224E-01,0.4671948489426224E-01, \
    0.1595417182608939,0.1595417182608939, \
    0.1595417182608939,0.1595417182608939, \
    0.1497202089079448,0.1497202089079448, \
    0.1497202089079448,0.1497202089079448, \
    0.2483067110521767,0.2483067110521767, \
    0.2483067110521767,0.2483067110521767 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule12 ( n ):

#*****************************************************************************80
#
## rule12() returns the rule of degree 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.9711185107918885,0.6489450771045480, \
    -0.9547543104262661,-0.9065777988000044, \
    0.9288045791287373,-0.9425162358139516, \
    -0.9438108523148829,-0.6477285885089000, \
    0.9399983037047607,-0.6866282782659429, \
    0.7379913501268124,-0.3293152288819712, \
    0.6556399582616308,0.4257309111871534, \
    0.9692829476897494,-0.8505721097622355, \
    0.2079264382173936,-0.8025201782903676, \
    -0.5197237466355563,-0.2734035281447398E-02, \
    -0.3699658428845123,-0.6558970744607242, \
    0.3202734978144128,0.8244469498554706, \
    0.2278925123542080E-01,0.5651896934359196E-01, \
    0.4889968338954821,-0.3555976156822369, \
    0.7575512967066254,-0.1870234315112276, \
    -0.9967741042631649 ] )
  ys = np.array ( [ \
    -0.8672105154213969,0.9928922644702000, \
    0.2857493181383339,0.9656011790176721, \
    0.8921207951072256,-0.9100219543607504, \
    0.7000393501436398,-0.9664634507775797, \
    0.4769006675305678,0.4257467094739614, \
    -0.9615153562096814,0.9693604253119810, \
    0.7113042249747283,-0.7943285461026974, \
    -0.1992840398255900,-0.7990773209000775E-01, \
    0.8876704665740045,-0.6649760891057823, \
    -0.3390779542043381,-0.5354471390418425, \
    0.1502820099360215,0.8334029046137713, \
    0.3881559105148546,-0.5879856922234445, \
    -0.2000991752759776E-01,-0.9646721637922943, \
    -0.2761642039851812,-0.8128294162538594, \
    0.1215344546399007,0.6390274229299343, \
    -0.4400036004541968 ] )
  ws = np.array ( [ \
    0.2294319212922989E-01,0.2269718640167010E-01, \
    0.3814000586151853E-01,0.1921567026521910E-01, \
    0.3433859117158319E-01,0.2503589002871782E-01, \
    0.4151906822977771E-01,0.3384747145223248E-01, \
    0.5960510578836526E-01,0.1273691684426847, \
    0.3629732156183973E-01,0.4288352023218015E-01, \
    0.1186836445978463,0.1223937757234154, \
    0.4775972626669994E-01,0.1037607311404478, \
    0.1017344934330748,0.9441812422392200E-01, \
    0.1662942328844954,0.1752158503094866, \
    0.1535404788337684,0.8331450401650711E-01, \
    0.1951461758691787,0.1055576202902579, \
    0.1749572560557213,0.5131431669876880E-01, \
    0.1804321296492865,0.1127530309084298, \
    0.1400307997981144,0.1721261711453589, \
    0.2510187133639127E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule13 ( n ):

#*****************************************************************************80
#
## rule13() returns the rule of degree 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.9572976997863074,0.8595560056416388, \
    0.9572976997863074,-0.8595560056416386, \
    -0.7788097115544195,0.9834866824398722, \
    0.7788097115544197,-0.9834866824398722, \
    -0.4758086252182752,0.8500766736997490, \
    0.4758086252182753,-0.8500766736997490, \
    0.3907362161294613,0.9413272258729251, \
    -0.3907362161294612,-0.9413272258729251, \
    -0.1381834598624646,0.9589251702875351, \
    0.1381834598624647,-0.9589251702875351, \
    0.6478216371870111,0.7558053565720809, \
    -0.6478216371870111,-0.7558053565720809, \
    0.7074150899644462E-01,0.6962500784917495, \
    -0.7074150899644453E-01,-0.6962500784917495, \
    -0.3427165560404070,0.4093045616940387, \
    0.3427165560404070,-0.4093045616940387, \
    -0.7375869198366919E-30 ] )
  ys = np.array ( [ \
    -0.8595560056416389,-0.9572976997863074, \
    0.8595560056416387,0.9572976997863074, \
    -0.9834866824398722,-0.7788097115544196, \
    0.9834866824398722,0.7788097115544198, \
    -0.8500766736997490,-0.4758086252182752, \
    0.8500766736997490,0.4758086252182753, \
    -0.9413272258729251,0.3907362161294612, \
    0.9413272258729251,-0.3907362161294611, \
    -0.9589251702875351,-0.1381834598624647, \
    0.9589251702875351,0.1381834598624648, \
    -0.7558053565720809,0.6478216371870111, \
    0.7558053565720809,-0.6478216371870111, \
    -0.6962500784917495,0.7074150899644457E-01, \
    0.6962500784917495,-0.7074150899644449E-01, \
    -0.4093045616940387,-0.3427165560404070, \
    0.4093045616940387,0.3427165560404070, \
    -0.6522588594679827E-30 ] )
  ws = np.array ( [ \
    0.2699339218118215E-01,0.2699339218118215E-01, \
    0.2699339218118215E-01,0.2699339218118215E-01, \
    0.2120743264134157E-01,0.2120743264134157E-01, \
    0.2120743264134157E-01,0.2120743264134157E-01, \
    0.8403587015611026E-01,0.8403587015611026E-01, \
    0.8403587015611026E-01,0.8403587015611026E-01, \
    0.5479564090947502E-01,0.5479564090947502E-01, \
    0.5479564090947502E-01,0.5479564090947502E-01, \
    0.4272687338421139E-01,0.4272687338421139E-01, \
    0.4272687338421139E-01,0.4272687338421139E-01, \
    0.9175668641747110E-01,0.9175668641747110E-01, \
    0.9175668641747110E-01,0.9175668641747110E-01, \
    0.1508552789574409,0.1508552789574409, \
    0.1508552789574409,0.1508552789574409, \
    0.1816350488471704,0.1816350488471704, \
    0.1816350488471704,0.1816350488471704, \
    0.2124022307685795 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule14 ( n ):

#*****************************************************************************80
#
## rule14() returns the rule of degree 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.7971028933442358E-01,0.5471061974611687, \
    0.9884165047157199E-02,-0.3207474755493107, \
    -0.9553717233098673E-01,0.4082649649717013, \
    0.7282812616257787,-0.3472810864715026, \
    -0.7915820141518555,0.2785829529075714, \
    0.2099338375706851,-0.3770688843422310, \
    0.1546298932128112,0.9706353820201650, \
    -0.9710188308157890,-0.8089422169597223E-01, \
    -0.6907103686706517,-0.3766500271820025, \
    -0.5730050261123937,0.2628896117741670, \
    0.5452072294160648,-0.8660081844945786, \
    0.5293743439059322,0.8326824008480398, \
    -0.9838433394477736,0.9724693366798177, \
    0.7239917862034132,-0.8848792748044129, \
    0.9060729882068399,0.9965542304973446, \
    -0.8318061454455522,-0.3342315451147794, \
    0.7013190684905666,0.9589226582728134, \
    -0.6067867745349950,0.9099368375229098, \
    -0.9529480307145739,-0.9784887714287833, \
    -0.6288709123199404,-0.8984845926717366, \
    0.7834593049247998 ] )
  ys = np.array ( [ \
    0.7997982556617036,0.8939858342635323, \
    0.4772113760639611,0.7590210924614017, \
    -0.1641336121692613,0.6627639082081634, \
    0.9910176287834889,0.1897335228068912, \
    0.1071320357310403,0.1628717488606178, \
    -0.4874120187172733,0.9815580199193836, \
    0.9428958078193180,-0.9568920474226420, \
    0.2935671028498448,-0.8120950161302742, \
    0.8737574543065562,-0.5687517308443202, \
    0.5033945159864817,-0.9476918771401073, \
    -0.1446903403457750,0.6085144943023661, \
    -0.7379657281768257,0.7553490523545380, \
    -0.7955014974234428,0.5032746878924270, \
    -0.9513994070448035,-0.9641836389975580, \
    -0.7647494365215827,-0.4197122679990931, \
    -0.5991295673421837,-0.9870420901808716, \
    0.3662527369607260,0.9255947941322170, \
    -0.2432439926029902,0.2516141162390789E-01, \
    -0.2593532979101687,0.8203127557579633, \
    -0.8613154366604666,0.9766163862390111, \
    -0.4322894664059549 ] )
  ws = np.array ( [ \
    0.5306119137159240E-01,0.4422789838333461E-01, \
    0.1273937944867034,0.7175684820689888E-01, \
    0.1568138398057906,0.1082893191419578, \
    0.1425381117124736E-01,0.1362424642572790, \
    0.9621728531430029E-01,0.1420579284045241, \
    0.1461917185380448,0.2659569714822968E-01, \
    0.5071663615284024E-01,0.8265110949266337E-02, \
    0.3089045691835443E-01,0.9808292446464849E-01, \
    0.5780479268214644E-01,0.1229597898540734, \
    0.1040216750542093,0.4885605487211036E-01, \
    0.1309068037017440,0.5947734706318328E-01, \
    0.9812697893659589E-01,0.5941729254373463E-01, \
    0.1721117182291158E-01,0.3143615055818434E-01, \
    0.3320596149477782E-01,0.1938593289821144E-01, \
    0.4495089530188040E-01,0.1917919328230456E-01, \
    0.7662013919695503E-01,0.2566629926215708E-01, \
    0.1191871942506123,0.1558050723920070E-01, \
    0.1194301874701882,0.7623831743082932E-01, \
    0.4693631023011145E-01,0.1603574648435874E-01, \
    0.7006443647504916E-01,0.1296824822458430E-01, \
    0.9170277370106396E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule15 ( n ):

#*****************************************************************************80
#
## rule15() returns the rule of degree 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.7749527857778351,0.9885448991378063, \
    -0.7749527857778349,-0.9885448991378063, \
    -0.9070374303651182,0.9571446613308432, \
    0.9070374303651184,-0.9571446613308430, \
    -0.4303978306869286,0.9769578054468787, \
    0.4303978306869287,-0.9769578054468787, \
    -0.9756646723906326,0.1107064048513496, \
    0.9756646723906326,-0.1107064048513495, \
    -0.7388921437312957,0.7868610204187212, \
    0.7388921437312957,-0.7868610204187212, \
    0.1995220876718269,0.6659287668239546, \
    -0.1995220876718268,-0.6659287668239546, \
    -0.1934983412061240,0.8412271039808018, \
    0.1934983412061241,-0.8412271039808018, \
    0.4882189227791580,0.8922368778153702, \
    -0.4882189227791579,-0.8922368778153702, \
    -0.5772265461040059,0.9526539504944950, \
    0.5772265461040061,-0.9526539504944950, \
    -0.4474426063114782,0.5675455860909890, \
    0.4474426063114783,-0.5675455860909890, \
    -0.7044956995149931E-01,0.3256679896817100, \
    0.7044956995149934E-01,-0.3256679896817100 ] )
  ys = np.array ( [ \
    -0.9885448991378063,0.7749527857778350, \
    0.9885448991378063,-0.7749527857778348, \
    -0.9571446613308433,-0.9070374303651183, \
    0.9571446613308431,0.9070374303651185, \
    -0.9769578054468787,-0.4303978306869286, \
    0.9769578054468787,0.4303978306869287, \
    -0.1107064048513496,-0.9756646723906326, \
    0.1107064048513495,0.9756646723906326, \
    -0.7868610204187212,-0.7388921437312957, \
    0.7868610204187212,0.7388921437312957, \
    -0.6659287668239546,0.1995220876718268, \
    0.6659287668239546,-0.1995220876718268, \
    -0.8412271039808018,-0.1934983412061240, \
    0.8412271039808018,0.1934983412061241, \
    -0.8922368778153702,0.4882189227791580, \
    0.8922368778153702,-0.4882189227791578, \
    -0.9526539504944950,-0.5772265461040060, \
    0.9526539504944950,0.5772265461040063, \
    -0.5675455860909890,-0.4474426063114783, \
    0.5675455860909890,0.4474426063114784, \
    -0.3256679896817100,-0.7044956995149933E-01, \
    0.3256679896817100,0.7044956995149936E-01 ] )
  ws = np.array ( [ \
    0.1443015463807196E-01,0.1443015463807196E-01, \
    0.1443015463807196E-01,0.1443015463807196E-01, \
    0.1816242330920956E-01,0.1816242330920956E-01, \
    0.1816242330920956E-01,0.1816242330920956E-01, \
    0.1290815898308381E-01,0.1290815898308381E-01, \
    0.1290815898308381E-01,0.1290815898308381E-01, \
    0.3010764365372140E-01,0.3010764365372140E-01, \
    0.3010764365372140E-01,0.3010764365372140E-01, \
    0.6540469907131932E-01,0.6540469907131932E-01, \
    0.6540469907131932E-01,0.6540469907131932E-01, \
    0.1197895531736646,0.1197895531736646, \
    0.1197895531736646,0.1197895531736646, \
    0.8473841548096289E-01,0.8473841548096289E-01, \
    0.8473841548096289E-01,0.8473841548096289E-01, \
    0.6453833756714425E-01,0.6453833756714425E-01, \
    0.6453833756714425E-01,0.6453833756714425E-01, \
    0.2403055376316494E-01,0.2403055376316494E-01, \
    0.2403055376316494E-01,0.2403055376316494E-01, \
    0.1196130510491228,0.1196130510491228, \
    0.1196130510491228,0.1196130510491228, \
    0.1533837904970821,0.1533837904970821, \
    0.1533837904970821,0.1533837904970821 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule16 ( n ):

#*****************************************************************************80
#
## rule16() returns the rule of degree 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.4455077315117606,-0.2848639978436560, \
    0.3281612731066613,0.8918323090897292, \
    0.5080739455207711,-0.1604014838336734, \
    -0.5084786013975685,0.6830501661618820, \
    0.3958609078545774E-01,-0.9505884228486957, \
    -0.9618117119546932,-0.9824876605856204, \
    0.7294909884375445,0.1663512176814138, \
    -0.8401346406026955,0.7196828159773350, \
    0.2530272226250717,0.6403128558574714E-01, \
    0.9867649245062882,-0.2009570267598735, \
    -0.4385685045405642,0.9942720499027967, \
    -0.8306577686854565,0.1540093368841131, \
    0.5127230397362322,-0.9896697019211779, \
    0.9721677355950014,-0.7432189863550824, \
    0.7845206176595362,0.9792382924978336, \
    -0.7071472873150695,-0.1416891896032315, \
    0.8901118844470474,0.8991291622644930, \
    -0.8948787586840297,-0.1685236423690618, \
    0.8814614259143865,-0.9727794481100781, \
    -0.2335640652756550,0.9317484014546712, \
    0.4462548323794501,-0.4956609448877936, \
    -0.7464462325957708,-0.6209288757442605, \
    -0.9729904625306640,0.6851689211463186, \
    -0.6950237982778372,0.1406973647399049, \
    -0.8903519744155600,-0.4494459013630722, \
    0.6393855383975146,0.4185604687784284 ] )
  ys = np.array ( [ \
    -0.4133544718603057,-0.7739045957079853, \
    -0.9418618376442869,-0.5606355473579230, \
    0.9698717423735355,-0.4892197731244818, \
    -0.9117050044897801,-0.5146278686624721, \
    -0.8810600362311165,-0.9545711191201147, \
    -0.5466258413042109,-0.8038321990753307, \
    -0.1738438525238659,-0.6521123405187266, \
    -0.3199762775663758,0.8583352444264194, \
    0.9559713160961977,0.8638442022353128, \
    -0.7782646945578277,0.6577321912732575, \
    -0.2429524974731521,0.3876054361677954, \
    -0.7951217128043849,-0.2163105603296342, \
    -0.7522598930908062,0.5914422527084512, \
    -0.2390927720573675,-0.9749994483165604, \
    -0.8444622014821822,0.8810775159513397, \
    0.6173187727164633,0.7292324652124864E-01, \
    0.1389731666217061,0.6539121663076461, \
    0.8152409648202001,-0.9939582277051608, \
    0.9818676808679303,0.9582010007957961, \
    0.9824162852107247,-0.9611203598796459, \
    0.1014796681115945,0.8630083224142983, \
    0.9693553936129727,-0.5969027498090264, \
    -0.3789880325419188E-01,0.4272704958652744, \
    0.4313302857584844E-01,0.4101941952194764, \
    0.3277950128817075,0.3540266909627898, \
    -0.9786311482371555,0.6960968466161754 ] )
  ws = np.array ( [ \
    0.7760560264177564E-01,0.6557384620049388E-01, \
    0.3492505367961147E-01,0.4902394774171961E-01, \
    0.2071780611220039E-01,0.9663554422001587E-01, \
    0.4275428371393922E-01,0.4251351999693562E-01, \
    0.4614134112945410E-01,0.1008804262208153E-01, \
    0.2597909269494542E-01,0.7243920128199269E-02, \
    0.8689727864752500E-01,0.7770693383996630E-01, \
    0.6824785727785596E-01,0.4942860806128915E-01, \
    0.1939352812224098E-01,0.6287664325857020E-01, \
    0.1228661441972498E-01,0.1029914685037788, \
    0.1129049857606719,0.1469344234054041E-01, \
    0.4431063501362172E-01,0.1183113207778475, \
    0.6355581532812171E-01,0.1527602237522992E-01, \
    0.2841229216361006E-01,0.1472432061291935E-01, \
    0.4129113754659276E-01,0.1149253014935389E-01, \
    0.7883123749996855E-01,0.1339728049062325, \
    0.6215863520566767E-01,0.4742159015437373E-01, \
    0.3530277887828205E-01,0.1663690106625590E-01, \
    0.1074607484017106E-01,0.6944512701761030E-02, \
    0.2298755190493018E-01,0.1230850655669064E-01, \
    0.1267827808948161,0.6295607382580996E-01, \
    0.2066068139152711E-01,0.8653018393026629E-01, \
    0.2938486912464724E-01,0.9600456501593493E-01, \
    0.9622610521466571E-01,0.1308302132754554, \
    0.6115363632570159E-01,0.1144365242523608, \
    0.1628247685682751E-01,0.9586498584301183E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule17 ( n ):

#*****************************************************************************80
#
## rule17() returns the rule of degree 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.7710386602263628,0.7710386602263630, \
    0.9803457456469387,-0.9803457456469384, \
    -0.2292639639675523,0.2292639639675524, \
    0.4847176019505991E-03,-0.4847176019504780E-03, \
    -0.6189416389750175,0.6189416389750177, \
    0.9587315519802511,-0.9587315519802511, \
    0.8409306922533750,-0.8409306922533748, \
    -0.4308042054877432,0.4308042054877433, \
    0.4761431266211590,-0.4761431266211589, \
    0.8651144531733139,-0.8651144531733139, \
    0.9846617345267017,-0.9846617345267017, \
    -0.7981639404863030,0.7981639404863030, \
    0.6877591943414725,-0.6877591943414725, \
    -0.3038305486106544,0.3038305486106544, \
    0.9852576255116258,-0.9852576255116258, \
    0.9853756930046446,-0.9853756930046446, \
    0.7024672194580522,-0.7024672194580522, \
    0.4589513024499020,-0.4589513024499019, \
    -0.5838938372432102,0.5838938372432102, \
    0.4855363777625971,-0.4855363777625971, \
    0.1909552287968119,-0.1909552287968118, \
    0.1970910744873101,-0.1970910744873101, \
    0.9070140000742543,-0.9070140000742543, \
    -0.9370706813548184,0.9370706813548186, \
    -0.1024098809482286,0.1024098809482287, \
    0.9018657853563646,-0.9018657853563646, \
    0.7422255782894629,-0.7422255782894629, \
    -0.1975779250586182E-19 ] )
  ys = np.array ( [ \
    -0.9187170657318696,0.9187170657318696, \
    -0.9679135253250817,0.9679135253250819, \
    -0.9437800394025085,0.9437800394025085, \
    -0.9886578344699537,0.9886578344699537, \
    -0.9803491213417113,0.9803491213417113, \
    -0.8226737868824753,0.8226737868824755, \
    -0.9649601466712245,0.9649601466712245, \
    -0.8370492275539414,0.8370492275539414, \
    -0.9716943047473653,0.9716943047473653, \
    -0.6326447362896030,0.6326447362896030, \
    0.2029425559112923,-0.2029425559112922, \
    -0.7906135688735062,0.7906135688735062, \
    -0.8442560578129694,0.8442560578129694, \
    -0.3117615836793495,0.3117615836793495, \
    0.7701659795648228,-0.7701659795648226, \
    -0.4379432170880169,0.4379432170880170, \
    -0.3820619012323893,0.3820619012323894, \
    -0.6514286057161101,0.6514286057161101, \
    -0.5711068454496305,0.5711068454496305, \
    -0.8072896746317025E-01,0.8072896746317031E-01, \
    -0.8630149364726712,0.8630149364726712, \
    -0.3872678175415290,0.3872678175415290, \
    0.5103334842355030,-0.5103334842355027, \
    -0.9584329986119476,0.9584329986119474, \
    -0.6619201369182062,0.6619201369182062, \
    -0.1238115372273944,0.1238115372273945, \
    0.2071876599633523,-0.2071876599633522, \
    0.5346688849930886E-20 ] )
  ws = np.array ( [ \
    0.1261638293838951E-01,0.1261638293838951E-01, \
    0.3408339905429266E-02,0.3408339905429266E-02, \
    0.2796862081921473E-01,0.2796862081921473E-01, \
    0.1252812914329644E-01,0.1252812914329644E-01, \
    0.1635296523785200E-01,0.1635296523785200E-01, \
    0.1720881227455075E-01,0.1720881227455075E-01, \
    0.1523407270818440E-01,0.1523407270818440E-01, \
    0.5600796522816800E-01,0.5600796522816800E-01, \
    0.2382823797668716E-01,0.2382823797668716E-01, \
    0.4513279974663867E-01,0.4513279974663867E-01, \
    0.1931215256841166E-01,0.1931215256841166E-01, \
    0.4158804216001467E-01,0.4158804216001467E-01, \
    0.4685849665862760E-01,0.4685849665862760E-01, \
    0.1200522449400290,0.1200522449400290, \
    0.1238565802221201E-01,0.1238565802221201E-01, \
    0.1760077392303538E-01,0.1760077392303538E-01, \
    0.8264937698824523E-01,0.8264937698824523E-01, \
    0.8629133710270168E-01,0.8629133710270168E-01, \
    0.8660536182880048E-01,0.8660536182880048E-01, \
    0.1134857467272575,0.1134857467272575, \
    0.6518861145910534E-01,0.6518861145910534E-01, \
    0.1184802238173896,0.1184802238173896, \
    0.4767526390300979E-01,0.4767526390300979E-01, \
    0.1203076112968188E-01,0.1203076112968188E-01, \
    0.1010849820160845,0.1010849820160845, \
    0.5753445241741756E-01,0.5753445241741756E-01, \
    0.8946701652955226E-01,0.8946701652955226E-01, \
    0.1312734684062163 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule18 ( n ):

#*****************************************************************************80
#
## rule18() returns the rule of degree 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.9824292972819758,-0.9803800150830472, \
    0.9786873970954008,0.9783064717068459, \
    0.9721036514650782,0.5934299192489508, \
    0.5976341012197494,-0.3692961886011435, \
    0.7049479055795181,-0.7373468008004338, \
    0.9861989064660380,-0.8465158209874328E-01, \
    0.8850139974482023,-0.9313926150284875, \
    -0.7089981957319805,0.8732614092173598, \
    -0.8419399215622921,0.3224279462028189, \
    0.2244640124522700,-0.8347180004932071, \
    -0.8279536304784142,-0.6568125381001307, \
    -0.8460042964230963,-0.9242174294702851, \
    -0.5414368844899894,0.9265304841706828, \
    -0.8981156173043389,-0.4115732120271069, \
    0.6047453622518654,-0.5983900835098156, \
    0.4320397790648277,0.4499667234152572, \
    0.9513764564603604,-0.6795979700947666, \
    -0.6564652118524049,0.8378047852517292, \
    -0.1113556772390856,-0.3608746962710803, \
    0.9862753904173321,-0.2331918978886594, \
    -0.9870492227974196,-0.9894160854750882, \
    -0.9836502238795436,0.8002432442611336, \
    0.6492404239850669,0.8701160725699196, \
    0.7389321385106327,-0.4715855030569622, \
    0.7436165358202136,0.3534834684769252, \
    -0.3650849452075164,-0.2283506208713122, \
    0.1740274102467612,0.8995839783500573, \
    0.3405925655026003,0.4295328792252409E-01, \
    0.1448653016063912,-0.1312827821241097, \
    0.5004638295686703,0.6006609259220026E-01, \
    0.1552257232885370,-0.9395864632354990, \
    -0.4791507758959901,-0.8137902397325638 ] )
  ys = np.array ( [ \
    -0.9492304540136947,0.9469609026131530, \
    0.7622186219256711,-0.9196983748762729, \
    0.9764183470032382,-0.9616466720526158, \
    0.8343589711117383,0.9800036938552533, \
    0.9870747330066914,-0.8333460482416958, \
    -0.3278737740897394,0.8908466843089227, \
    -0.9855803626832146,-0.8212845135474046, \
    0.6822143912173052,0.9031148761319726, \
    0.9885786707367459,0.5365154393395204E-01, \
    0.7350437600270140,0.5084609108470370, \
    -0.6132315128115761,0.2290780703350274, \
    -0.9786418155875946,-0.3102577845761006, \
    -0.6275098391746888,0.1407483577400233E-01, \
    0.8295680022967102,0.7753196502785407, \
    -0.6526316599009200,-0.9333674622588783, \
    0.9243432783386737,0.7005646989935736E-01, \
    -0.6925969506257750,-0.3641945758998874, \
    0.9193665018045939,-0.4639915525654867, \
    -0.9041936920710849,-0.7808865818750257, \
    0.2974467982752778,-0.4343746051515523, \
    -0.5898322990766285,-0.1604383366455782E-01, \
    0.6393477839238390,-0.8481629731994191, \
    -0.2054507717193144,-0.1017355764563722, \
    0.7159568279790096,-0.1245817088489083, \
    0.2542532076804419,-0.8415199898068800, \
    -0.9897219383699781,0.1556384545656453, \
    -0.9791074324031704,0.5295267411341480, \
    -0.4165391069331053,-0.1509802365687459, \
    0.3347376662738560,0.5759504751299614, \
    0.5086985983019631,-0.6661951769904182, \
    0.9847264496502689,0.3003342534564235, \
    0.4492326697835803,-0.6261874651130582E-02 ] )
  ws = np.array ( [ \
    0.4880182878194577E-02,0.5801719791846293E-02, \
    0.1363202620128554E-01,0.7756485561516194E-02, \
    0.4249395346845679E-02,0.2449228653823736E-01, \
    0.2751148878355652E-01,0.1865262619502059E-01, \
    0.1160827955745764E-01,0.2909451783554787E-01, \
    0.1614009453230349E-01,0.5169172255655628E-01, \
    0.7388591103278081E-02,0.2021700469490708E-01, \
    0.4636019735255641E-01,0.2315518049910366E-01, \
    0.7815468109974862E-02,0.3769198715796499E-01, \
    0.7881010252197586E-01,0.3988856078693273E-01, \
    0.4079805534552380E-01,0.6645673137795649E-01, \
    0.1072546708888146E-01,0.3868425989902273E-01, \
    0.5522501374016728E-01,0.3253997663365805E-01, \
    0.2752684329481517E-01,0.6117844466269161E-01, \
    0.7168779734796255E-01,0.2620423047578233E-01, \
    0.3392741843404458E-01,0.7458228761237336E-01, \
    0.2478342723311915E-01,0.6447492653722675E-01, \
    0.3284650513806075E-01,0.5368779603413000E-01, \
    0.4545538155398856E-01,0.5397016565409892E-01, \
    0.1519721989624682E-01,0.1031663549936232, \
    0.1231416020827792E-01,0.1349682430871745E-01, \
    0.1395336957267540E-01,0.3753801076980155E-01, \
    0.8258232039188609E-01,0.2489123627268648E-01, \
    0.4546454333835988E-01,0.9452263223987649E-01, \
    0.7842163445187621E-01,0.5876926206730445E-01, \
    0.1249000951778932E-01,0.1088923354481117, \
    0.1951366247998040E-01,0.4179385297531394E-01, \
    0.1033273611701436,0.1162365062083885, \
    0.1023818705273872,0.8804476252208088E-01, \
    0.8910543971624120E-01,0.8874335328605459E-01, \
    0.1602722062379702E-01,0.3378674145303614E-01, \
    0.7595232871119993E-01,0.6022146552676879E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule19 ( n ):

#*****************************************************************************80
#
## rule19() returns the rule of degree 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.9734386316165470,0.9744990929036832, \
    0.9734386316165472,-0.9744990929036830, \
    -0.3841574585766744,0.9670641778942685, \
    0.3841574585766745,-0.9670641778942685, \
    0.2986734938364671,0.9905525689050123, \
    -0.2986734938364670,-0.9905525689050123, \
    -0.7396581737067777,0.9869464369033261, \
    0.7396581737067779,-0.9869464369033261, \
    -0.1425244970455050,0.9733021904515969, \
    0.1425244970455051,-0.9733021904515969, \
    0.7650240374639232,0.9804863471920530, \
    -0.7650240374639230,-0.9804863471920530, \
    -0.7599006633708002,0.7279453517455540, \
    0.7599006633708002,-0.7279453517455540, \
    -0.1192987760526789,-0.2637912058730560E-02, \
    0.1192987760526789,0.2637912058730575E-02, \
    -0.8850504442537889,0.9022234232868145, \
    0.8850504442537889,-0.9022234232868145, \
    0.5304174652462883,0.9125489607085608, \
    -0.5304174652462881,-0.9125489607085608, \
    -0.2858528945041368,0.2941600854694212, \
    0.2858528945041368,-0.2941600854694212, \
    -0.5671850101113227,0.8836081660895880, \
    0.5671850101113227,-0.8836081660895880, \
    0.3174295148500719,0.7293427112089215, \
    -0.3174295148500718,-0.7293427112089215, \
    -0.2492430513869149,0.7672563284436533, \
    0.2492430513869150,-0.7672563284436533, \
    -0.5087793568494521,0.5623738439118215, \
    0.5087793568494521,-0.5623738439118215, \
    0.7335719396414396E-01,0.8930925855397183, \
    -0.7335719396414385E-01,-0.8930925855397183, \
    0.8350775723842838E-02,0.5392457387102469, \
    -0.8350775723842772E-02,-0.5392457387102469 ] )
  ys = np.array ( [ \
    -0.9744990929036833,-0.9734386316165471, \
    0.9744990929036831,0.9734386316165473, \
    -0.9670641778942685,-0.3841574585766744, \
    0.9670641778942685,0.3841574585766745, \
    -0.9905525689050123,0.2986734938364670, \
    0.9905525689050123,-0.2986734938364669, \
    -0.9869464369033261,-0.7396581737067778, \
    0.9869464369033261,0.7396581737067780, \
    -0.9733021904515969,-0.1425244970455050, \
    0.9733021904515969,0.1425244970455051, \
    -0.9804863471920530,0.7650240374639231, \
    0.9804863471920530,-0.7650240374639229, \
    -0.7279453517455540,-0.7599006633708002, \
    0.7279453517455540,0.7599006633708002, \
    0.2637912058730553E-02,-0.1192987760526789, \
    -0.2637912058730568E-02,0.1192987760526789, \
    -0.9022234232868145,-0.8850504442537889, \
    0.9022234232868145,0.8850504442537889, \
    -0.9125489607085608,0.5304174652462882, \
    0.9125489607085608,-0.5304174652462880, \
    -0.2941600854694212,-0.2858528945041368, \
    0.2941600854694212,0.2858528945041368, \
    -0.8836081660895880,-0.5671850101113227, \
    0.8836081660895880,0.5671850101113227, \
    -0.7293427112089215,0.3174295148500719, \
    0.7293427112089215,-0.3174295148500718, \
    -0.7672563284436533,-0.2492430513869149, \
    0.7672563284436533,0.2492430513869150, \
    -0.5623738439118215,-0.5087793568494521, \
    0.5623738439118215,0.5087793568494521, \
    -0.8930925855397183,0.7335719396414390E-01, \
    0.8930925855397183,-0.7335719396414379E-01, \
    -0.5392457387102469,0.8350775723842805E-02, \
    0.5392457387102469,-0.8350775723842739E-02 ] )
  ws = np.array ( [ \
    0.4076118519980060E-02,0.4076118519980060E-02, \
    0.4076118519980060E-02,0.4076118519980060E-02, \
    0.1627326938099484E-01,0.1627326938099484E-01, \
    0.1627326938099484E-01,0.1627326938099484E-01, \
    0.1254157952509427E-01,0.1254157952509427E-01, \
    0.1254157952509427E-01,0.1254157952509427E-01, \
    0.1028929333936017E-01,0.1028929333936017E-01, \
    0.1028929333936017E-01,0.1028929333936017E-01, \
    0.1475928282295525E-01,0.1475928282295525E-01, \
    0.1475928282295525E-01,0.1475928282295525E-01, \
    0.1207323692393111E-01,0.1207323692393111E-01, \
    0.1207323692393111E-01,0.1207323692393111E-01, \
    0.4619184040692218E-01,0.4619184040692218E-01, \
    0.4619184040692218E-01,0.4619184040692218E-01, \
    0.3696173437828049E-01,0.3696173437828049E-01, \
    0.3696173437828049E-01,0.3696173437828049E-01, \
    0.2018069481193246E-01,0.2018069481193246E-01, \
    0.2018069481193246E-01,0.2018069481193246E-01, \
    0.3738944032940469E-01,0.3738944032940469E-01, \
    0.3738944032940469E-01,0.3738944032940469E-01, \
    0.9821701539315209E-01,0.9821701539315209E-01, \
    0.9821701539315209E-01,0.9821701539315209E-01, \
    0.3844110871724747E-01,0.3844110871724747E-01, \
    0.3844110871724747E-01,0.3844110871724747E-01, \
    0.7127049386881731E-01,0.7127049386881731E-01, \
    0.7127049386881731E-01,0.7127049386881731E-01, \
    0.6966749913838975E-01,0.6966749913838975E-01, \
    0.6966749913838975E-01,0.6966749913838975E-01, \
    0.7715964130310782E-01,0.7715964130310782E-01, \
    0.7715964130310782E-01,0.7715964130310782E-01, \
    0.4598470092336809E-01,0.4598470092336809E-01, \
    0.4598470092336809E-01,0.4598470092336809E-01, \
    0.9562983140360957E-01,0.9562983140360957E-01, \
    0.9562983140360957E-01,0.9562983140360957E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule20 ( n ):

#*****************************************************************************80
#
## rule20() returns the rule of degree 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.7903555901298286,0.2252273789362463, \
    -0.1371556203352229,0.9516912467651903, \
    0.8981438613797404,0.3511327336932318, \
    0.9759068343062448E-01,-0.1920781702210826, \
    0.6695436306885109,0.5830289505702392, \
    -0.4278190227205511,0.5727845316573248E-01, \
    0.7351507200926066,0.7898934964234535, \
    -0.3594399777482915,0.3376839183112454, \
    0.9886396714914109,-0.3907721596661082, \
    -0.6046899139754487,0.9173007153030285, \
    -0.4141396903659944E-01,-0.6385982895810176, \
    0.6013396134438070,0.9161661661998538, \
    -0.3278639859221721,0.8802460227981840, \
    -0.2034581078060147,0.6969166399839279, \
    0.5351593293803870,-0.2787747819837111, \
    0.9910314479371701,-0.8252889264259545, \
    -0.9599491206891601,0.4944916835714113, \
    -0.7703896716180660,0.9129604837711394, \
    0.8500373866499284,-0.3755453354695931E-01, \
    -0.9734574105217517,0.2897016770313429, \
    0.7688438290660360,-0.8388618516990838, \
    -0.5341286913684105,-0.9174806831430735, \
    -0.9474346838846874,-0.6131936263177837E-01, \
    0.7605933106317154,-0.9848886462575595, \
    -0.7572987820459326,0.5080745682281066E-01, \
    -0.4636550029355001,0.9705319244227489, \
    -0.8914079947263784,-0.9873056954830064, \
    -0.9758313372889643,-0.8819170869186215, \
    -0.9709635895278415,0.9822722262702339, \
    -0.8873503942891041,-0.6569247082044029, \
    -0.9870905373622706,-0.5734674551654146, \
    0.1507888619083396E-01,0.5506050560553492, \
    -0.7366839885772312,-0.7117026556332434, \
    0.2333965922395885,-0.2878681152474931, \
    0.4361746990352844,0.9814633895599361, \
    -0.5319601634991685,0.9850987522022563, \
    0.1957972824970721,0.2084217400195901, \
    0.4755027720742199,0.9147494843686150, \
    -0.8645689328165518,0.6772212070927294 ] )
  ys = np.array ( [ \
    -0.8898248168845113E-01,-0.7280953904485143E-01, \
    -0.8653524201560835,-0.2902346585197535, \
    0.1218660048097990,-0.2471221282702101, \
    -0.7467915296200941,-0.5589830789081398, \
    -0.2090651941599068,-0.4355704406099477, \
    -0.7264771605644266,-0.1363590388950549, \
    -0.9878512802669168,0.9209737732078764, \
    -0.9535217391501140,-0.5953361238026516, \
    -0.7515863705429210E-01,0.9865491452054407, \
    -0.9940939029178233,-0.9840832904192385, \
    0.8284898564271251E-01,-0.8660720584668250, \
    0.9809450037856990,0.8048533499129369, \
    0.2790289740151233,-0.4082743843038831, \
    0.9740226654958868,0.3035697582018394, \
    -0.9862725985120795,0.7185672952170555, \
    -0.9193256145694509,-0.9544384245126734, \
    -0.9898146349839960,0.7338947136259082E-01, \
    -0.2075330463780984,0.9907318998968393, \
    0.5387986220469478,0.8834131451429665, \
    -0.8934522638909749,-0.9207656972246965, \
    -0.6367076114754525,0.9978913196317913, \
    0.5300943949356414,-0.4262998259673880, \
    0.1841144567160324,0.5090691042712456, \
    -0.9214501612581178,-0.6400027811642439, \
    0.3209231678914174,-0.3846636405176737, \
    0.8697161095697501,0.3470098428369617, \
    0.5711239311935090,0.4067912914297930, \
    0.7624786524458222,-0.7770143745259210, \
    0.9584356802550765,0.6551973976459680, \
    0.2854578772720695E-01,0.9551619780680761, \
    -0.1675185677029804,0.4240021284329500E-01, \
    -0.9864545039606490,-0.7989550278861819, \
    -0.6071839996966222,0.7388672054082017, \
    0.3140775120692750,-0.1793826353802805, \
    0.8772336982049433,-0.6033076898494673, \
    -0.4039805189289538,0.9282498625490752, \
    0.7185098783764428,0.9758090760986288, \
    0.5388255455349226,-0.8020212431755418, \
    0.8814335976449187,0.7393267487868044 ] )
  ws = np.array ( [ \
    0.4220810999582407E-01,0.4210468769855168E-01, \
    0.4111495137274749E-01,0.1602722818539338E-01, \
    0.3619967055440460E-01,0.5719761023753370E-01, \
    0.5553932136722374E-01,0.7027947643456225E-01, \
    0.3877224057962559E-01,0.5615678549912440E-01, \
    0.5631946977958934E-01,0.1879677326120675E-01, \
    0.1313057162810730E-02,0.2109221815204442E-01, \
    0.2451480331747192E-01,0.6556422061834499E-01, \
    0.1119235292343633E-01,0.7115563056913567E-02, \
    0.6714100241623257E-02,0.5885829448742507E-02, \
    0.8309083447844690E-01,0.3590868298232087E-01, \
    0.1246127664791048E-01,0.2018878910488524E-01, \
    0.8451815870413146E-01,0.3248692905689807E-01, \
    0.1341510929402505E-01,0.6472935261954060E-01, \
    0.1145237221800998E-01,0.5872712613961156E-01, \
    0.4508959666015173E-02,0.1493403238757605E-01, \
    0.2665017934074124E-02,0.7704806248110788E-01, \
    0.5726954359349042E-01,0.4528203295472384E-02, \
    0.4279817302411395E-01,0.4285481643886387E-01, \
    0.8072115177434423E-02,0.3701323444432086E-01, \
    0.4613328158120365E-01,0.3966194341947075E-02, \
    0.6788885180206457E-01,0.3480913280397030E-01, \
    0.1958947629336374E-01,0.7993874305725486E-01, \
    0.2433364291226502E-01,0.1062990044699051E-01, \
    0.6170560315322090E-01,0.7521981238448959E-01, \
    0.3621544028408890E-01,0.1839043728583574E-01, \
    0.3635800635820290E-01,0.1087561990443862E-01, \
    0.1235528041521356E-01,0.2670676504697193E-01, \
    0.5756245567725824E-02,0.1016410330068744E-01, \
    0.3155355506307831E-01,0.1843695052008212E-01, \
    0.1362846461516491E-01,0.8050841953401032E-01, \
    0.1413883594050338E-01,0.5019314017226575E-01, \
    0.5096315858878126E-01,0.4491888769330514E-01, \
    0.8622086129893808E-01,0.9032569802582428E-01, \
    0.4214427133348429E-01,0.1315668261444553E-01, \
    0.7308371765738744E-01,0.5122200740309473E-02, \
    0.6652468674436235E-01,0.1888655008314831E-01, \
    0.7163064878569746E-01,0.2352000357823148E-01, \
    0.2167515013056250E-01,0.4797944511124803E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule21 ( n ):

#*****************************************************************************80
#
## rule21() returns the rule of degree 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.9754554632015029,-0.9754554632015029, \
    0.9807628529972264,-0.9807628529972262, \
    0.9864691810349792,-0.9864691810349792, \
    0.9817752275809579,-0.9817752275809579, \
    0.8942647503363536,-0.8942647503363533, \
    -0.7926169940479519,0.7926169940479522, \
    0.9673238098903247,-0.9673238098903247, \
    -0.6233424472175393,0.6233424472175395, \
    0.8075494298208362,-0.8075494298208362, \
    -0.9112339448388380,0.9112339448388382, \
    0.5294700780841287,-0.5294700780841285, \
    0.9126054184220483,-0.9126054184220483, \
    -0.8005037324172778,0.8005037324172778, \
    -0.9786316733709013,0.9786316733709015, \
    -0.1931251782159229,0.1931251782159230, \
    0.7448428411561702,-0.7448428411561699, \
    0.9910640341773119,-0.9910640341773119, \
    0.4487876769216255,-0.4487876769216254, \
    0.7730731265491211,-0.7730731265491211, \
    -0.8538350485874476E-02,0.8538350485874577E-02, \
    0.9305948052973293,-0.9305948052973293, \
    -0.4410686164106586,0.4410686164106588, \
    0.5726168020738448,-0.5726168020738448, \
    0.9094921563319007,-0.9094921563319007, \
    0.6650799110223121,-0.6650799110223121, \
    0.9845379327215906,-0.9845379327215906, \
    -0.1489897109425285E-01,0.1489897109425291E-01, \
    0.4777858927462423,-0.4777858927462423, \
    0.2346150739656185E-01,-0.2346150739656185E-01, \
    -0.6464750210052006,0.6464750210052006, \
    -0.3898509033065152,0.3898509033065153, \
    -0.2596817297614839,0.2596817297614840, \
    0.8930982971146899E-01,-0.8930982971146888E-01, \
    0.2378419730518350,-0.2378419730518349, \
    -0.4923226235686091,0.4923226235686091, \
    0.3260553152624549,-0.3260553152624548, \
    0.6900640280303905,-0.6900640280303905, \
    0.8399949350854392,-0.8399949350854392, \
    0.2175201355296100,-0.2175201355296099, \
    -0.2552655348509120,0.2552655348509120, \
    0.8967910069881992,-0.8967910069881992 ] )
  ys = np.array ( [ \
    -0.8684124523298049,0.8684124523298051, \
    -0.9445108390325675,0.9445108390325677, \
    0.8224833612237958,-0.8224833612237956, \
    -0.6674381398519379,0.6674381398519381, \
    -0.9903377411510502,0.9903377411510502, \
    -0.9907543940322484,0.9907543940322484, \
    0.4473528589231669E-01,-0.4473528589231656E-01, \
    -0.9343866955469575,0.9343866955469575, \
    0.4520870573336636,-0.4520870573336634, \
    -0.9274277947725086,0.9274277947725084, \
    -0.9866712872285782,0.9866712872285782, \
    -0.4550564012095777,0.4550564012095778, \
    -0.8127883212479330,0.8127883212479330, \
    -0.9813307175904386,0.9813307175904383, \
    -0.9279142876740704,0.9279142876740704, \
    -0.9320431789499202,0.9320431789499202, \
    0.4282792320995888,-0.4282792320995887, \
    -0.5362236701446004,0.5362236701446004, \
    -0.6399087385202717,0.6399087385202717, \
    -0.8135057649888232,0.8135057649888232, \
    0.6470101042020234,-0.6470101042020232, \
    -0.8155924092874611,0.8155924092874611, \
    -0.7941248493230142,0.7941248493230142, \
    0.2473440793805384,-0.2473440793805383, \
    -0.3454192145795777,0.3454192145795778, \
    -0.2668503935770928,0.2668503935770929, \
    -0.4625176827521818,0.4625176827521818, \
    -0.6895677594851285E-01,0.6895677594851290E-01, \
    -0.2404342948898286E-01,0.2404342948898286E-01, \
    -0.6484663233565804,0.6484663233565804, \
    -0.9898736812731077,0.9898736812731077, \
    -0.6343263441026139,0.6343263441026139, \
    -0.9814223809013130,0.9814223809013130, \
    -0.2765567197102583,0.2765567197102583, \
    -0.4080894058196405,0.4080894058196404, \
    -0.9078967063955937,0.9078967063955937, \
    0.1497779073446914,-0.1497779073446913, \
    -0.1279062882959751,0.1279062882959752, \
    -0.6902255847834162,0.6902255847834162, \
    -0.2059314662901914,0.2059314662901914, \
    -0.8238753864861620,0.8238753864861620 ] )
  ws = np.array ( [ \
    0.2118008413970087E-02,0.2118008413970087E-02, \
    0.4561991935236101E-02,0.4561991935236101E-02, \
    0.6876351365235698E-02,0.6876351365235698E-02, \
    0.1124466702102733E-01,0.1124466702102733E-01, \
    0.4818715192537238E-02,0.4818715192537238E-02, \
    0.5989564896092799E-02,0.5989564896092799E-02, \
    0.1767795981651036E-01,0.1767795981651036E-01, \
    0.2380089975465993E-01,0.2380089975465993E-01, \
    0.4148355130225962E-01,0.4148355130225962E-01, \
    0.1184358597738201E-01,0.1184358597738201E-01, \
    0.1089514188613057E-01,0.1089514188613057E-01, \
    0.3129460714416973E-01,0.3129460714416973E-01, \
    0.2951898806186879E-01,0.2951898806186879E-01, \
    0.2370685766690177E-02,0.2370685766690177E-02, \
    0.2822396585947564E-01,0.2822396585947564E-01, \
    0.2219335711268346E-01,0.2219335711268346E-01, \
    0.9583664348129897E-02,0.9583664348129897E-02, \
    0.6372673897970250E-01,0.6372673897970250E-01, \
    0.4375827379330900E-01,0.4375827379330900E-01, \
    0.4429543031127132E-01,0.4429543031127132E-01, \
    0.2471410210516637E-01,0.2471410210516637E-01, \
    0.4249825844225831E-01,0.4249825844225831E-01, \
    0.4558876680953739E-01,0.4558876680953739E-01, \
    0.2756490338260340E-01,0.2756490338260340E-01, \
    0.6243396099268773E-01,0.6243396099268773E-01, \
    0.1168182946833649E-01,0.1168182946833649E-01, \
    0.7382665975220684E-01,0.7382665975220684E-01, \
    0.7666679963909392E-01,0.7666679963909392E-01, \
    0.4391713647273730E-01,0.4391713647273730E-01, \
    0.4705013653249818E-01,0.4705013653249818E-01, \
    0.9574427334796009E-02,0.9574427334796009E-02, \
    0.6262807887841917E-01,0.6262807887841917E-01, \
    0.1507382504443397E-01,0.1507382504443397E-01, \
    0.7853972113541645E-01,0.7853972113541645E-01, \
    0.6890694586576196E-01,0.6890694586576196E-01, \
    0.3574201277291281E-01,0.3574201277291281E-01, \
    0.6408284590143187E-01,0.6408284590143187E-01, \
    0.4908916812527610E-01,0.4908916812527610E-01, \
    0.5502691558122864E-01,0.5502691558122864E-01, \
    0.8126618865329004E-01,0.8126618865329004E-01, \
    0.2206473054465979E-01,0.2206473054465979E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule22 ( n ):

#*****************************************************************************80
#
## rule22() returns the rule of degree 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.1168773459913643E-01,-0.7371881387645758, \
    0.8294952934036814,-0.5954751704041336, \
    -0.4324369794733402,-0.7688482950823662, \
    0.9204074310294709,0.9345989584398445E-01, \
    -0.8936155650763420,-0.7702459791051814, \
    -0.1373629144933700,0.5509811434354096, \
    -0.1491245367450688,0.3561825582103059, \
    0.9353031268387029,-0.2924575431987692, \
    0.2443965863661181,-0.6390847658587071, \
    -0.4984730279242101,0.7392293471332223, \
    -0.9874262069353944,-0.9183316919543670E-01, \
    -0.7612182335622527,-0.8617096626977842E-01, \
    0.9888069308129792,-0.5588987313328233, \
    -0.5751189401814027,-0.9225108518720977, \
    0.8984615209750768,0.8382620472105732, \
    0.1626926025129410,-0.9967788148796793, \
    -0.6486037112886791,-0.5668454455159495, \
    0.9856879280293260,0.9717573267273887, \
    -0.3076008058514624,0.3587016306051349, \
    -0.7623612106456181,0.6388680957517785, \
    0.5510537420201546,0.1053488710493425, \
    0.9916832391481870,-0.8977327473577641, \
    0.4016301282586624,-0.9838441232429354, \
    0.7905399896596540,-0.9824504337674188, \
    -0.5775436902276508,-0.9772275458992810, \
    -0.8927278831009643,0.6072501413880697, \
    0.3391264841215570,0.8802736916527715, \
    -0.3614572700854332,0.7628120974888042, \
    0.9410464685954009,0.5766667841609323, \
    0.3785886954980848,-0.7336046871225165, \
    -0.3595240670259577,0.1395498733753600, \
    -0.8379800610987231,0.9026858439122091, \
    -0.7544128178700894,-0.1371254063139990, \
    0.7326981395585584,0.1008288194176049, \
    -0.1402954353279801,0.5600957930752593, \
    -0.9835815408757524,0.9794922442499654, \
    -0.3422476201633468,0.8847947144492797, \
    0.3480028949057162,0.1399751797907734, \
    0.7410269267329871,-0.8707213419949226, \
    -0.7829703967945006,-0.7518531217472861E-01, \
    0.1797607493737034,0.5514938721272684, \
    0.9189774855743247,-0.9478502721386363, \
    -0.3753442057328584,0.9824594434447735, \
    0.7794560599617187,0.5868549502954560, \
    -0.9830132030284936,-0.9109869789024120, \
    -0.3369368343786870,-0.9656919342504539, \
    0.9878086002165142 ] )
  ys = np.array ( [ \
    0.2190948368619670,-0.5638633812668349, \
    0.7772605528528743,-0.2566398183828403, \
    -0.5129047910078139,-0.4506194723257167, \
    0.8425861006849568,-0.4518983245417754, \
    0.3543337144777458,0.4959761932603439, \
    0.2485911682035064,-0.3132773446075675, \
    -0.9937282156984992,-0.2003997888710157, \
    -0.5607980017506478,-0.3522379616257777, \
    -0.4426431371959611,-0.3692415241854752E-01, \
    0.7496615691984209,0.6926590385285363, \
    -0.1850687765410226,-0.1925693267588198, \
    0.1363788459324560,0.9515651662120697, \
    0.5579343853339161E-01,0.9517652105508706, \
    -0.9389370283909926,-0.3771353916795439, \
    -0.9947202210423953,-0.3609118075153294, \
    0.9902936741983037,0.3133668776125615, \
    0.6199365920821208,0.2873358944700919, \
    -0.7434073625585887,0.3666474918307532, \
    0.8685050837394444,0.9342984101597417, \
    -0.8496275328566278,-0.4918800631346358, \
    0.5207829647449653,0.4875959314271490, \
    -0.3759522691536638,-0.9452616179455003, \
    -0.6399489008638399,-0.5698761741539897, \
    -0.6821182736060648,-0.9838318115418717, \
    -0.7110797215818025,-0.8424531888684956, \
    -0.7019404243765398,-0.8133442851406898, \
    0.6937136042433247,0.1403628667969644, \
    0.4853142503301350,-0.9404688641752270, \
    -0.1594253939471121,0.8410558281897980, \
    -0.9090435768164216,0.8618858293632953, \
    -0.9801201774367985,0.2925291147308246E-01, \
    -0.1389383474162093,-0.8488076014783108, \
    -0.9950422147374585,0.6774278489603331, \
    0.3281092020661301,0.8336091093259060, \
    -0.6447342914933101,-0.9855619048067824, \
    0.9863388067410731,-0.9474857272173681, \
    -0.8291238758195407,0.5386555528488844, \
    0.2895743833834052,-0.7848534988754099, \
    -0.1043902046106473,0.7337865418484663, \
    0.9901322140668845,-0.9181369104835962, \
    -0.9807391493006852,0.7602577556121397E-01, \
    0.9902833594797992,0.7639725935225382E-01, \
    0.1089930212643242E-01,0.6870529955030933, \
    0.9401212847078045,0.9891928053902059, \
    0.8336461919417253,0.9356252744608189, \
    0.9934890766781104,0.5866648232658751, \
    0.9371299738758988 ] )
  ws = np.array ( [ \
    0.6067121956035168E-02,0.2527104513859865E-01, \
    0.9025528955311097E-02,0.5803636803454140E-01, \
    0.4942739001800841E-01,0.2794072665175644E-01, \
    0.1603496923754518E-01,0.6013880064040703E-01, \
    0.2941264773858220E-01,0.3334592290253230E-01, \
    0.7897021060987033E-01,0.3685303544908184E-01, \
    0.3948104138816246E-02,0.6679001222692597E-01, \
    0.2111954975158539E-01,0.4792141258829016E-01, \
    0.2695976162319685E-01,0.2470945430647790E-01, \
    0.3947338905928970E-01,0.3294627756714954E-01, \
    0.9846011394782925E-02,0.7297001782497028E-01, \
    0.4106989048022942E-01,0.2161795857158166E-01, \
    0.8365413396512252E-02,0.1967362232030983E-01, \
    0.2188213465301344E-01,0.2494392526364261E-01, \
    0.3519731383753954E-02,0.3478325192787569E-01, \
    0.8190571090769309E-02,0.6108434551087310E-02, \
    0.3434968062753964E-01,0.6007998437323292E-01, \
    0.7504666111448662E-02,0.1603184108436172E-01, \
    0.3437516964723778E-01,0.2571624349884583E-01, \
    0.2694235332130491E-01,0.4466450734173113E-01, \
    0.5500707054662403E-01,0.7222938823304295E-01, \
    0.7486350326225666E-02,0.1143517520249437E-01, \
    0.5817171888321045E-01,0.9994978126228900E-02, \
    0.3467709360229788E-01,0.1964349392895841E-02, \
    0.4240321318174279E-01,0.8728495324106815E-02, \
    0.2591557111759762E-01,0.3720861411904331E-01, \
    0.5505688737445376E-01,0.3631603425342831E-01, \
    0.6567401226660792E-01,0.1795583567053723E-01, \
    0.2289367999547543E-01,0.3547488447682710E-01, \
    0.2995254108777568E-01,0.2686044680493277E-01, \
    0.1079041750322994E-01,0.7877736606773408E-01, \
    0.3733692480386966E-01,0.1821095142444074E-01, \
    0.5325368320113208E-02,0.5922160899036626E-01, \
    0.5076619476679856E-01,0.4372734278286988E-01, \
    0.6332661510009212E-01,0.9790273018996520E-02, \
    0.1776555836345017E-02,0.4813300061774173E-02, \
    0.4258882597057490E-01,0.3052111793035846E-01, \
    0.7003826037949971E-01,0.5120830680793959E-01, \
    0.4944440063240135E-01,0.2605683245528804E-01, \
    0.6201489406026509E-02,0.3089929178556832E-01, \
    0.1316878814412241E-01,0.6382065038385205E-01, \
    0.3990900163624796E-02,0.2334151205865433E-01, \
    0.7860422025755921E-01,0.1000548940130294E-01, \
    0.1798134856368640E-01,0.8411973937140507E-02, \
    0.7382035812019881E-02,0.1170576178999751E-01, \
    0.6920800809156403E-02,0.1595811031270932E-01, \
    0.3880611624295888E-02 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule23 ( n ):

#*****************************************************************************80
#
## rule23() returns the rule of degree 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.1922689542773817,-0.1922689542773816, \
    -0.9880860844879094,0.9880860844879096, \
    0.4588599108929147,-0.4588599108929146, \
    0.2847661416086631,-0.2847661416086630, \
    0.8023730521007825,-0.8023730521007822, \
    -0.4008300617025742,0.4008300617025743, \
    0.9128169992246806,-0.9128169992246804, \
    0.6402796135160949,-0.6402796135160946, \
    0.6316970739891037,-0.6316970739891037, \
    -0.5737921022421535,0.5737921022421535, \
    0.4346256934364524,-0.4346256934364522, \
    0.7764676048715878,-0.7764676048715878, \
    0.7244917270725689,-0.7244917270725689, \
    -0.1888739484686455,0.1888739484686456, \
    0.9943536134460622,-0.9943536134460622, \
    -0.7313948142734760,0.7313948142734760, \
    0.8943097577057932,-0.8943097577057932, \
    0.8436479267198643,-0.8436479267198643, \
    0.7791831851449014,-0.7791831851449014, \
    0.8641774713700604,-0.8641774713700604, \
    0.9617690298704565,-0.9617690298704563, \
    -0.4195385320317492,0.4195385320317493, \
    0.2226040785176633,-0.2226040785176632, \
    0.9898168214058006,-0.9898168214058006, \
    -0.7489474270848241,0.7489474270848243, \
    0.1917103338448669E-01,-0.1917103338448658E-01, \
    0.9493597561722253,-0.9493597561722253, \
    0.9904394141829281,-0.9904394141829279, \
    -0.5829692270288439,0.5829692270288439, \
    -0.6147395289066456,0.6147395289066458, \
    0.9535616627723794,-0.9535616627723796, \
    -0.2159492946526814,0.2159492946526815, \
    0.6262127585905694,-0.6262127585905694, \
    0.9907200353310519,-0.9907200353310519, \
    0.9843113976598121,-0.9843113976598121, \
    -0.8786718625785459,0.8786718625785461, \
    0.9324996820585237,-0.9324996820585237, \
    0.8556365285580105,-0.8556365285580105, \
    0.6098296498831587,-0.6098296498831587, \
    0.2401978383668566E-02,-0.2401978383668536E-02, \
    -0.2160362298752296,0.2160362298752297, \
    0.9419047852611938,-0.9419047852611938, \
    0.9784325270256451,-0.9784325270256451, \
    0.4245835794119392,-0.4245835794119392, \
    0.2180806198402934,-0.2180806198402933, \
    0.4211715480246619,-0.4211715480246619, \
    0.2159184187190165,-0.2159184187190165, \
    0.9145012870119151,-0.9145012870119151, \
    -0.6659715296954374E-02,0.6659715296954456E-02 ] )
  ys = np.array ( [ \
    -0.8413204499428454,0.8413204499428454, \
    -0.9814588472800125,0.9814588472800123, \
    -0.6684346870698402,0.6684346870698402, \
    -0.7992729842209235,0.7992729842209235, \
    -0.9416742417176776,0.9416742417176776, \
    -0.6678440121187212,0.6678440121187212, \
    -0.9891421484914774,0.9891421484914776, \
    -0.9915720334011255,0.9915720334011255, \
    -0.4898989236348730,0.4898989236348731, \
    -0.4662751769077947,0.4662751769077946, \
    -0.9416451658784137,0.9416451658784137, \
    -0.2882717499568009,0.2882717499568010, \
    0.2486649083667506,-0.2486649083667505, \
    -0.9882692965051619,0.9882692965051619, \
    0.7885280263196212,-0.7885280263196209, \
    -0.6589298745979582,0.6589298745979582, \
    -0.5251907426680982,0.5251907426680982, \
    0.2698952252390472E-01,-0.2698952252390462E-01, \
    -0.7058148204376444,0.7058148204376444, \
    0.8039684450793269,-0.8039684450793269, \
    -0.9795669903911515,0.9795669903911517, \
    -0.9436139885736695,0.9436139885736695, \
    -0.9897986315498021,0.9897986315498021, \
    -0.1515697280553813E-02,0.1515697280553934E-02, \
    -0.9288927030420643,0.9288927030420643, \
    -0.9319407769628315,0.9319407769628315, \
    0.6363710989431733,-0.6363710989431731, \
    -0.9179467622904829,0.9179467622904831, \
    -0.8263113277740309,0.8263113277740309, \
    -0.9928811295871781,0.9928811295871781, \
    0.9091589955140115,-0.9091589955140112, \
    -0.4548720285260120,0.4548720285260120, \
    -0.8475542857772346,0.8475542857772346, \
    0.4247422802343108,-0.4247422802343107, \
    -0.3947150748420805,0.3947150748420806, \
    -0.9832744227413978,0.9832744227413978, \
    -0.1923063082978693,0.1923063082978694, \
    0.4580266855460115,-0.4580266855460114, \
    -0.4698541060861779E-01,0.4698541060861786E-01, \
    -0.2437626817883838,0.2437626817883838, \
    -0.8348003321715464,0.8348003321715464, \
    0.2268917425003757,-0.2268917425003756, \
    -0.6927513253690014,0.6927513253690016, \
    -0.2736597506928621,0.2736597506928621, \
    -0.4885665960318681,0.4885665960318681, \
    0.2093478053463650,-0.2093478053463650, \
    -0.1584479979856305E-01,0.1584479979856307E-01, \
    -0.8398490539050634,0.8398490539050636, \
    -0.6725993072235357,0.6725993072235357 ] )
  ws = np.array ( [ \
    0.2087996398690324E-01,0.2087996398690324E-01, \
    0.1454948755827531E-02,0.1454948755827531E-02, \
    0.4748321475897626E-01,0.4748321475897626E-01, \
    0.2581005409389433E-01,0.2581005409389433E-01, \
    0.1501004260111713E-01,0.1501004260111713E-01, \
    0.4842495146008856E-01,0.4842495146008856E-01, \
    0.2506826413864942E-02,0.2506826413864942E-02, \
    0.6535276655159778E-02,0.6535276655159778E-02, \
    0.4894280385061923E-01,0.4894280385061923E-01, \
    0.4975905503606815E-01,0.4975905503606815E-01, \
    0.2214413184536724E-01,0.2214413184536724E-01, \
    0.4313124475180520E-01,0.4313124475180520E-01, \
    0.4433897643935200E-01,0.4433897643935200E-01, \
    0.9046276329783944E-02,0.9046276329783944E-02, \
    0.3911096929389304E-02,0.3911096929389304E-02, \
    0.3599231426419872E-01,0.3599231426419872E-01, \
    0.2838276711743061E-01,0.2838276711743061E-01, \
    0.3373992192798946E-01,0.3373992192798946E-01, \
    0.3336454855497337E-01,0.3336454855497337E-01, \
    0.2095059245259030E-01,0.2095059245259030E-01, \
    0.2046044703097752E-02,0.2046044703097752E-02, \
    0.2164205919445887E-01,0.2164205919445887E-01, \
    0.8285628342573098E-02,0.8285628342573098E-02, \
    0.8397251850551729E-02,0.8397251850551729E-02, \
    0.1731140501927820E-01,0.1731140501927820E-01, \
    0.2467601783099452E-01,0.2467601783099452E-01, \
    0.1682157937509966E-01,0.1682157937509966E-01, \
    0.3331814718792869E-02,0.3331814718792869E-02, \
    0.3259337068821334E-01,0.3259337068821334E-01, \
    0.6005493842446140E-02,0.6005493842446140E-02, \
    0.8210801440654199E-02,0.8210801440654199E-02, \
    0.6548837153964436E-01,0.6548837153964436E-01, \
    0.3088139176161778E-01,0.3088139176161778E-01, \
    0.7183392776926659E-02,0.7183392776926659E-02, \
    0.9748230121097153E-02,0.9748230121097153E-02, \
    0.5383514720217621E-02,0.5383514720217621E-02, \
    0.2224440941283463E-01,0.2224440941283463E-01, \
    0.3213763319312607E-01,0.3213763319312607E-01, \
    0.5959500864875663E-01,0.5959500864875663E-01, \
    0.7353356562572214E-01,0.7353356562572214E-01, \
    0.3920268743920687E-01,0.3920268743920687E-01, \
    0.2191097090277860E-01,0.2191097090277860E-01, \
    0.1035031173873475E-01,0.1035031173873475E-01, \
    0.6659548623039759E-01,0.6659548623039759E-01, \
    0.6553251667930458E-01,0.6553251667930458E-01, \
    0.6644084983327379E-01,0.6644084983327379E-01, \
    0.7384544963870446E-01,0.7384544963870446E-01, \
    0.1649581640678158E-01,0.1649581640678158E-01, \
    0.5651348047241081E-01,0.5651348047241081E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule24 ( n ):

#*****************************************************************************80
#
## rule24() returns the rule of degree 24.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.9947148928250171,0.9910990446809216, \
    0.9693866534373358,0.8366669887301708, \
    0.9976180969133432,-0.9626395872771291, \
    -0.9956012694874316,0.9827883755011416, \
    0.9899696481565038,-0.1027795858264751, \
    -0.5372013809570906,-0.1302736589054738, \
    -0.9966597496356319,-0.8416889461091814, \
    -0.9888026187105032,0.5314747340473951, \
    -0.8162827902273060,0.9739798586001176, \
    -0.9411304883795972,-0.9821743630414852, \
    -0.8146483736791913,0.2216111751930999, \
    0.9919273511735743,0.8515268909036164, \
    -0.6344208939912110E-01,0.8124697219833941, \
    -0.9159342331978603,0.1939576002609792, \
    0.9879450437516667,0.2535126040886103, \
    -0.9628662071921108,0.8784885445188073, \
    -0.8980693800663294,-0.4876187319409098, \
    0.8244493216582833,-0.7771226957924775E-01, \
    0.9133806640305893,-0.2863497657037777, \
    -0.7746256411943806,0.8788745310361548, \
    -0.9610911899226917,0.9600320888811048, \
    0.9425138210931967,0.7626320556994604, \
    -0.3308772778351785,0.1279919952613696, \
    0.5294732769614892,0.3555627902477361, \
    -0.9279977222115954,0.9931449449560651, \
    0.5102490315575532E-01,-0.7525118688957001, \
    -0.4719724839934526,0.1520260254758981, \
    0.9489604126336816,-0.2169062988895815, \
    -0.8687157102597637,-0.7360447596642431, \
    0.8497144016937899,-0.6403949304059380, \
    0.9160879280172893,0.5974122417304695, \
    0.9356564573866695,0.2602110178808541E-02, \
    0.2185370159809754,-0.4174601636720920, \
    -0.6704915695516799,0.7098684394657311, \
    -0.6662903518807954,0.6842750704411169, \
    0.6940401495592319,0.2055436622280245, \
    0.5409016726579078,-0.2111056222157408, \
    0.4249715565953610,-0.4579852398972861, \
    -0.4762834069005017,-0.3112968492969387, \
    -0.9861402159543649,0.5994434867749180, \
    -0.6329536320758256,0.4071516862564607, \
    -0.5899049368040069,-0.8873886456704851, \
    -0.9429884035167735,-0.8103411028772554, \
    -0.6172197178932676,0.4403002993242678, \
    -0.5964555068203565,0.4214363261995724, \
    -0.2167017340827659,0.3600751655325609, \
    0.9573652308066442E-02,-0.1986519498186896, \
    0.5940360363603530,0.7449094683537840, \
    0.3446198859685110,0.7550496004921502, \
    0.2034447821293972,-0.8764429892755836, \
    -0.9821148921468710E-02,-0.4283906719131795, \
    -0.2565291139819166,-0.4253124084387095, \
    -0.4107973035474266,0.6107899647074595, \
    -0.7740269973316680,-0.9874686104628365, \
    -0.1780069523272345E-01 ] )
  ys = np.array ( [ \
    0.9921816068213789,0.9927512676582938, \
    -0.9807210913639813,-0.9849335979706825, \
    -0.9031203174435843,-0.9807185407289059, \
    0.1826280218638680,0.1985977578306220E-03, \
    -0.1343242025779884,0.9836572598301550, \
    -0.9945228775385402,-0.9932466930618153, \
    -0.9021729201562282,0.9919450680865269, \
    -0.5469411165135486,-0.9946152107188805, \
    -0.9833999582719447,-0.7694911408818028, \
    0.9454206624475765,0.5820485751363867, \
    0.8726697552774600,0.9884035519660979, \
    0.3773859079404019,0.9854732000616159, \
    0.7430686212004588,-0.8172733392382462, \
    0.7368090773498677,0.8191066542200217, \
    -0.5129857572745989,0.7339438859190308, \
    0.3121292180404563,0.4238556817241846, \
    -0.9023577502860924,-0.8635258163522489, \
    -0.5019428343401774,-0.9100031022978671, \
    -0.6538056836085887,0.9419753943798090, \
    -0.8083978001656728,0.7971819583886433, \
    -0.7612052337333153,0.6275466264499783, \
    0.1573227985990733,0.6249214522371203, \
    -0.9587696584061124,-0.9822260622287698, \
    -0.8459845466706856,-0.6962190414609735, \
    -0.3797057196057647,0.8208860694583049, \
    0.9117911472030502,0.2466478148353290, \
    0.2531249337761478,-0.8311014632352622, \
    0.9327963019854183,0.3901208978319467, \
    -0.6258430618900800,-0.4854699629184363, \
    -0.8013355833035751E-01,0.7663811452715913, \
    -0.9064248594697549,0.9816002629218432, \
    -0.3156827868701995,0.5928915583696132, \
    -0.2758048916460264E-01,0.6590354293018823, \
    -0.9381955060600012,-0.2998249948498765, \
    0.9581605160533719,-0.6881340269166623, \
    -0.9406665893940601,0.3996485712287530, \
    -0.5101678225103823,-0.4421541038328301, \
    0.5912997929743822,0.9932623278482910, \
    0.8781241163707275,0.5625436230792860, \
    -0.1854744570391582,0.7725191379684401, \
    -0.2272561659397919E-01,-0.2598606537214366, \
    0.4549553364199058,0.4412559753061466, \
    -0.7387531735800691E-02,-0.1993131251585695, \
    -0.7001646090032370,0.8894305723468252, \
    -0.3651421534696686,0.2021031040499760, \
    -0.4759573989947036E-01,0.9560701833067996, \
    -0.2523062776553245,0.8029027500701331, \
    -0.3052326412673496E-01,0.9085765488533346, \
    -0.9429472498836997,0.1985140340578119, \
    -0.4744209684134443,0.8925996493449884E-01, \
    0.1788338183287970,-0.5864723938922081, \
    -0.7750597333889675,-0.2335671290163587, \
    0.1465570094281399,0.4191985939494091, \
    0.6100181397154107,0.8429972982275405, \
    -0.6496814943785820 ] )
  ws = np.array ( [ \
    0.7673500038857188E-03,0.8868846753542908E-03, \
    0.2702370475569613E-02,0.5392375480513576E-02, \
    0.1761998115149276E-02,0.3252629117203137E-02, \
    0.4483878506691741E-02,0.4387445903456329E-02, \
    0.6293360138903417E-02,0.9110559046011608E-02, \
    0.4960172913990594E-02,0.4540132762921259E-02, \
    0.2380910242803054E-02,0.4079407684566781E-02, \
    0.7372795522491610E-02,0.5764065832069020E-02, \
    0.5996283579933687E-02,0.8231405547532079E-02, \
    0.7742564602285441E-02,0.9689437679198899E-02, \
    0.1992786357523802E-01,0.7578960870331433E-02, \
    0.7297515243700454E-02,0.5560565572125132E-02, \
    0.1431910744302743E-01,0.2083181247879573E-01, \
    0.1871125538452946E-01,0.1856480159069449E-01, \
    0.7926961712192319E-02,0.3149563402986980E-01, \
    0.1220979773721510E-01,0.3064077139403503E-01, \
    0.1246839879952511E-01,0.2727439670515271E-01, \
    0.2989955062354429E-01,0.2568927037462639E-01, \
    0.1731775418487197E-01,0.1651762549497732E-01, \
    0.2348412516559215E-01,0.2103194138017257E-01, \
    0.1218315588129536E-01,0.1587611356755889E-01, \
    0.2192984739792703E-01,0.3559892184688495E-01, \
    0.1598768389647512E-01,0.9998012603521544E-02, \
    0.3014828623151700E-01,0.4445807626369159E-01, \
    0.2303305529498344E-01,0.4177457820842124E-02, \
    0.2595692066159871E-01,0.4297075322654262E-01, \
    0.2734909126669048E-01,0.3576989995633175E-01, \
    0.8104038598451695E-02,0.5896633070443507E-01, \
    0.2530733931631170E-01,0.3397799558910337E-01, \
    0.3681905878262371E-01,0.3127418749936042E-01, \
    0.1043340150186936E-01,0.9877922117697804E-02, \
    0.2268684828187055E-01,0.5274200508727377E-01, \
    0.6668503169982437E-01,0.4053161003772505E-01, \
    0.1580741394786280E-01,0.4437844031312334E-01, \
    0.1465934495793213E-01,0.3316127050631540E-01, \
    0.1633165248572775E-01,0.6234782740688132E-01, \
    0.4701994260472551E-01,0.5761066620189915E-01, \
    0.4794170534889713E-01,0.5798541312289998E-02, \
    0.2505250386803961E-01,0.2055053414266298E-01, \
    0.8995847445576632E-02,0.3472177169167036E-01, \
    0.5444084929958415E-01,0.5971645153263631E-01, \
    0.4912587830256034E-01,0.2538968252075221E-01, \
    0.1542318408388366E-01,0.4013335870948910E-01, \
    0.3298688496369413E-01,0.2322125010689848E-01, \
    0.3671677541506277E-01,0.6139982772160751E-01, \
    0.6362592843510947E-01,0.9567538562556033E-02, \
    0.6459890039693177E-01,0.3562315409338049E-01, \
    0.5516254605923790E-01,0.1998312905915403E-01, \
    0.2052118732484228E-01,0.4458997988822495E-01, \
    0.5811519536921120E-01,0.2297223481430297E-01, \
    0.6766667516677112E-01,0.4532069980219111E-01, \
    0.4089559205492352E-01,0.5328231011100253E-01, \
    0.4369211916320918E-01,0.4895075796108013E-01, \
    0.3261352596485557E-01,0.5100190068919709E-02, \
    0.5182667283735970E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule25 ( n ):

#*****************************************************************************80
#
## rule25() returns the rule of degree 25.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.7103850079486462,0.7103850079486462, \
    0.2350136833954603,-0.2350136833954603, \
    0.2319467644431913,-0.2319467644431913, \
    0.1887551793322332E-01,-0.1887551793322329E-01, \
    0.4762227841581165,-0.4762227841581164, \
    0.9223578267424110,-0.9223578267424110, \
    0.8612991449140567,-0.8612991449140567, \
    -0.2008507367686636,0.2008507367686637, \
    0.9910315414864325,-0.9910315414864325, \
    0.3217353529776810,-0.3217353529776809, \
    0.8933439162316077,-0.8933439162316077, \
    -0.5783268726892828,0.5783268726892828, \
    0.1876981715173633,-0.1876981715173632, \
    -0.4040937317707446,0.4040937317707447, \
    -0.8086692861933220,0.8086692861933220, \
    0.7699071344451243,-0.7699071344451243, \
    0.1349449671364110,-0.1349449671364109, \
    0.7067483874126944,-0.7067483874126944, \
    0.9941851173182269,-0.9941851173182271, \
    0.9823116186120971,-0.9823116186120969, \
    0.4238538814747814E-01,-0.4238538814747803E-01, \
    -0.1196214241956023,0.1196214241956024, \
    0.6534777415625678,-0.6534777415625675, \
    0.9750429947957491,-0.9750429947957491, \
    0.8117686312525225,-0.8117686312525225, \
    0.6171167577694838,-0.6171167577694838, \
    0.5721736374948944,-0.5721736374948944, \
    -0.3415910753286391,0.3415910753286392, \
    -0.9491077472873352,0.9491077472873354, \
    0.9925898844290307,-0.9925898844290307, \
    -0.2361386817708837,0.2361386817708838, \
    0.4376492710177434,-0.4376492710177433, \
    0.9907335874081320,-0.9907335874081320, \
    0.3690348754186010,-0.3690348754186009, \
    0.2356776284326877,-0.2356776284326877, \
    0.9290327147765426,-0.9290327147765426, \
    0.5315931005621322,-0.5315931005621322, \
    -0.7970927883912756,0.7970927883912758, \
    -0.6382950957253196,0.6382950957253198, \
    0.9125245471252791,-0.9125245471252793, \
    -0.1417325966030156,0.1417325966030157, \
    0.4628221381215424,-0.4628221381215424, \
    0.9500761399436652,-0.9500761399436652, \
    0.6585082411431559,-0.6585082411431559, \
    -0.5874365186841102E-02,0.5874365186841170E-02, \
    0.9830805981225823,-0.9830805981225823, \
    0.9607858073894220,-0.9607858073894220, \
    0.8126469869288578,-0.8126469869288578, \
    0.9197969485441327,-0.9197969485441327, \
    -0.5479961396095706,0.5479961396095708, \
    -0.4470049599321014,0.4470049599321015, \
    0.7873844821702739,-0.7873844821702737, \
    0.3012570662899303E-30,0.4368201344745598, \
    -0.4368201344745598,0.8506134670179059, \
    -0.8506134670179059,0.9113188530371741, \
    -0.9113188530371739,0.9836230570941239, \
    -0.9836230570941239,0.7402837708508578, \
    -0.7402837708508578 ] )
  ys = np.array ( [ \
    -0.7506170245096466,0.7506170245096466, \
    -0.6015670998122035E-01,0.6015670998122038E-01, \
    0.6313639161925437E-01,-0.6313639161925434E-01, \
    -0.2037217515148590,0.2037217515148590, \
    -0.9891004866173655,0.9891004866173655, \
    -0.3246552383950583,0.3246552383950584, \
    -0.1540352101742460,0.1540352101742461, \
    -0.3377511016941964,0.3377511016941964, \
    -0.6383724442924701,0.6383724442924703, \
    -0.8954389923107672,0.8954389923107672, \
    0.6633371340392643,-0.6633371340392643, \
    -0.6441606686218248,0.6441606686218248, \
    -0.9825525591494771,0.9825525591494771, \
    -0.4921744377774439,0.4921744377774439, \
    -0.8285906504912744,0.8285906504912744, \
    0.5016460262480213,-0.5016460262480213, \
    -0.7648310056858745,0.7648310056858745, \
    -0.7008712571932789,0.7008712571932789, \
    0.9429421827689296,-0.9429421827689294, \
    -0.9889464727951927,0.9889464727951929, \
    -0.9395791578550448,0.9395791578550448, \
    -0.8631057904957280,0.8631057904957280, \
    -0.9411634392706579,0.9411634392706579, \
    0.7901512634507242,-0.7901512634507240, \
    -0.8620663504329279,0.8620663504329279, \
    0.3181861315943668,-0.3181861315943667, \
    -0.4998028335682857,0.4998028335682858, \
    -0.9494727492703661,0.9494727492703661, \
    -0.9900142583759359,0.9900142583759357, \
    -0.2005292720209485,0.2005292720209486, \
    -0.6936010697328517,0.6936010697328517, \
    -0.9618522647938675,0.9618522647938675, \
    0.2336705239348026,-0.2336705239348024, \
    -0.6422765133729448,0.6422765133729448, \
    -0.4058616631814986,0.4058616631814986, \
    -0.7553494223525696,0.7553494223525699, \
    -0.8131056508171524,0.8131056508171524, \
    -0.9753835609823820,0.9753835609823820, \
    -0.9152847871689571,0.9152847871689571, \
    0.9075396692621631,-0.9075396692621629, \
    -0.9916640269515081,0.9916640269515081, \
    -0.2319599091440556,0.2319599091440556, \
    0.2744706063362164E-01,-0.2744706063362152E-01, \
    -0.4230837956698025E-01,0.4230837956698034E-01, \
    -0.5553447391265243,0.5553447391265243, \
    0.5512083775806552,-0.5512083775806550, \
    -0.4486213975897800,0.4486213975897801, \
    0.1653383270128847,-0.1653383270128846, \
    0.3695711955638312,-0.3695711955638311, \
    -0.9920191871388367,0.9920191871388367, \
    -0.8211053506315364,0.8211053506315364, \
    -0.9936569020855669,0.9936569020855669, \
    -0.1899153506582438E-30,0.1367147397139465, \
    -0.1367147397139464,-0.5673411356087702, \
    0.5673411356087702,-0.9545649683609251, \
    0.9545649683609253,-0.8813580692740732, \
    0.8813580692740735,-0.3448010185338413, \
    0.3448010185338414 ] )
  ws = np.array ( [ \
    0.1890289035282082E-01,0.1890289035282082E-01, \
    0.4408519139496046E-01,0.4408519139496046E-01, \
    0.1760012528851595E-01,0.1760012528851595E-01, \
    0.5135792991631447E-01,0.5135792991631447E-01, \
    0.5903718396467129E-02,0.5903718396467129E-02, \
    0.1169110569868906E-01,0.1169110569868906E-01, \
    0.2797734321676553E-01,0.2797734321676553E-01, \
    0.5430655753317624E-01,0.5430655753317624E-01, \
    0.5579615408482969E-02,0.5579615408482969E-02, \
    0.2529071368793077E-01,0.2529071368793077E-01, \
    0.2144063823465160E-01,0.2144063823465160E-01, \
    0.3501744210151039E-01,0.3501744210151039E-01, \
    0.8405006765794200E-02,0.8405006765794200E-02, \
    0.4833682312227475E-01,0.4833682312227475E-01, \
    0.1594545160823835E-01,0.1594545160823835E-01, \
    0.3558939192260235E-01,0.3558939192260235E-01, \
    0.4226984758231494E-01,0.4226984758231494E-01, \
    0.3140501945419725E-01,0.3140501945419725E-01, \
    0.2024434452721722E-02,0.2024434452721722E-02, \
    0.1349622146875648E-02,0.1349622146875648E-02, \
    0.1534182110464278E-01,0.1534182110464278E-01, \
    0.2952379758820060E-01,0.2952379758820060E-01, \
    0.1647236890585741E-01,0.1647236890585741E-01, \
    0.8590118628187588E-02,0.8590118628187588E-02, \
    0.1949659427579714E-01,0.1949659427579714E-01, \
    0.4728589565124858E-01,0.4728589565124858E-01, \
    0.4410722929300222E-01,0.4410722929300222E-01, \
    0.1872860198784019E-01,0.1872860198784019E-01, \
    0.2411335871046539E-02,0.2411335871046539E-02, \
    0.6741232108638781E-02,0.6741232108638781E-02, \
    0.4411511228498587E-01,0.4411511228498587E-01, \
    0.4232733780262361E-02,0.4232733780262361E-02, \
    0.6812146781301679E-02,0.6812146781301679E-02, \
    0.4593608235278822E-01,0.4593608235278822E-01, \
    0.5792082516805559E-01,0.5792082516805559E-01, \
    0.1593195877796943E-01,0.1593195877796943E-01, \
    0.3056610289854859E-01,0.3056610289854859E-01, \
    0.8554835231990672E-02,0.8554835231990672E-02, \
    0.1956601012663267E-01,0.1956601012663267E-01, \
    0.1051117872480982E-01,0.1051117872480982E-01, \
    0.6521513110348300E-02,0.6521513110348300E-02, \
    0.5717074378851367E-01,0.5717074378851367E-01, \
    0.1929092010649333E-01,0.1929092010649333E-01, \
    0.5062498553433200E-01,0.5062498553433200E-01, \
    0.5402053691556560E-01,0.5402053691556560E-01, \
    0.8931127348310931E-02,0.8931127348310931E-02, \
    0.1271750255435475E-01,0.1271750255435475E-01, \
    0.3860453155876481E-01,0.3860453155876481E-01, \
    0.2372095848832025E-01,0.2372095848832025E-01, \
    0.5971489271210207E-02,0.5971489271210207E-02, \
    0.3192818361403054E-01,0.3192818361403054E-01, \
    0.4118255231945603E-02,0.4118255231945603E-02, \
    0.1843978737274201E-01,0.5393241195495463E-01, \
    0.5393241195495463E-01,0.2787139422709562E-01, \
    0.2787139422709562E-01,0.8002087241718343E-02, \
    0.8002087241718343E-02,0.5159834028120074E-02, \
    0.5159834028120074E-02,0.3908234388553434E-01, \
    0.3908234388553434E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule26 ( n ):

#*****************************************************************************80
#
## rule26() returns the rule of degree 26.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.4833333960601769,0.8342454172040494, \
    0.7576455307285274,-0.5897785388721970, \
    -0.1965092140379674,-0.7806410759767570, \
    0.7735458124538029,0.2194354253840281, \
    -0.6123258347540325,-0.3875195310855452, \
    0.4210764575469916,0.6717143218134665, \
    0.4937567886903959,0.4310467214948753, \
    -0.8221934052978648E-01,0.1474744561277340, \
    -0.7849971862231101,0.2788743412255506, \
    -0.9174091785830387,-0.2680062461938560, \
    -0.6869484833848130,-0.5769800391396182, \
    -0.3175999245771031,-0.6900722826105213, \
    -0.4494495234589641,0.2720327015362536, \
    0.9844767989506050,0.9539566427635388, \
    -0.6618689211018638,0.9948047635608559, \
    0.6791817577488417,-0.7660679944748241, \
    -0.3544317327177745,0.8846710719994197, \
    -0.4769291205740912,0.3374006730427574, \
    -0.5230046201031646,0.9773104137186888, \
    0.8460741659581372,0.7811230642538761, \
    -0.7917954564682173,0.6689548567706126, \
    0.8995533103742481,0.5803086536096742, \
    0.9125294970192420,0.9864324103956210, \
    -0.9634751680719612,0.9171821405508755, \
    -0.8464504414046380,0.1148682640972169E-01, \
    -0.8893878433260284,0.1985037063041746, \
    0.6321992170210116,-0.8764667800594454E-01, \
    0.9612042270501360,0.8449547678280973, \
    -0.3143374729428800E-01,-0.7221561416927453, \
    -0.7408359655977623,-0.6573270993518512, \
    0.7579600253683801,0.1336947783582028, \
    -0.8801486144575378,0.9863146730096674, \
    0.5018023174101623,0.5456331728950238, \
    0.9966649790149599,-0.3664122751853194E-01, \
    0.3253875792212299E-01,0.9510103999741907, \
    0.4259089402020555,0.5239001877754490, \
    0.6028877215019741,0.3449303649336414, \
    -0.5679703819864291,-0.5650724066199918, \
    -0.8419709514596180E-01,0.8402671970302827E-01, \
    -0.9108885214110795,0.8192687649356658, \
    -0.9543907466564233,-0.7146063535728425, \
    -0.3837061453087470,0.4746594317998059E-01, \
    -0.1741432512718204,0.2800861092084038, \
    -0.8207343144238776,-0.9935648502810311, \
    -0.8697847685325190,-0.2948353200874713, \
    -0.8584906175082293,0.8306678364449214, \
    -0.9930049118920397,-0.4621304609915161, \
    0.1460010936826870,-0.9839106590889559, \
    -0.4906721644588728,-0.9896275589251841, \
    -0.9930899945869894,0.9038157695421652E-01, \
    0.9976519966165041,0.9439357544987950, \
    -0.8915811088898837,0.9306112013193892, \
    -0.9907255740995738,-0.9338876300481137, \
    0.3077773696572407,-0.9878642619619029, \
    0.6952834621750591,0.8445020176382917, \
    0.5386138090792357,-0.9518141860165342, \
    -0.1344815378332747,-0.3695179976651696, \
    0.9873492554611523,0.7062788639769675, \
    -0.6456167225977583,-0.3396836721033217, \
    -0.9362361756962438,-0.9626677628820013, \
    0.3015160924588678,0.7067532860197516, \
    -0.9571646423196823,0.9839100297235785, \
    -0.2419685587001514,0.9438884112343363, \
    -0.1742260222577426 ] )
  ys = np.array ( [ \
    -0.4215090372415874E-01,-0.3692934551145019, \
    -0.1931519618055097,0.3988972577148074, \
    -0.1715260024620762,0.9094199619403520, \
    0.6714959797593258,0.3368323178193660, \
    0.6925643585799712,-0.3334911148152457, \
    0.1579601812062493,0.7212403727697902, \
    0.7924318088830316,0.4711520853394768, \
    0.2329014884732836,0.7688776471476298E-01, \
    -0.2427208512979698,-0.9819844652166957, \
    0.6275746962958220,0.3958917640748951, \
    0.8330411855203188,-0.4968412520921159, \
    0.4887729302167374E-01,-0.3604995467485130, \
    0.5502876418517838,-0.1552754382216172, \
    0.5038985691395298,-0.3255794611786079, \
    0.3310081213549004,-0.6602065173414950, \
    -0.4894888916356721,0.5399510111685960, \
    0.7655039704316382,-0.5820392397031763, \
    0.1995474060499386,0.8781656258066206, \
    -0.1525213978780895,-0.5001983735790505, \
    0.7986695769024170,0.4824228603329770, \
    0.1592378639694050,0.1732234025449527E-02, \
    -0.9985738973637792E-01,0.5955792594614818, \
    0.3498450621988221,0.2407129566690367, \
    0.9947445171943684,0.6288090977170689, \
    0.7414927225667501,-0.9929600347714176, \
    0.3684373427277031,-0.9535682594324043, \
    0.3034752604286319,0.8507770288950726, \
    0.6305231708999399E-01,-0.8678090617845265, \
    -0.4141884020649694E-01,0.9931812444078701, \
    -0.6492023240589931,-0.6795234046038703E-02, \
    -0.7116015253442534,-0.5912100888422367, \
    0.9669064714907090,-0.9896978591786247, \
    -0.6357772860044338,-0.2816935374305686, \
    0.9465152907473502,0.9835467134448914, \
    0.5163644022959618,0.9899894348223212, \
    -0.9119806917142169,0.9594778630442550, \
    -0.8263115619511332,-0.4386676054811558, \
    0.9540273279949707,-0.7748522899685367, \
    -0.7271449178503047,-0.8683831780306135, \
    -0.9979822139283684,0.1525566715594689, \
    -0.3052870542039953,-0.8823794421118246, \
    -0.6417482148168809,-0.3240255976105304, \
    0.6580511661237559,0.6610461063468759, \
    -0.9615342517942168,-0.8967208208364033E-01, \
    -0.4912350350325419,-0.8431987564696162, \
    -0.7917868223215425,-0.9934797396330936, \
    0.4007666180051725,0.8621553422717932, \
    0.9342344412005841,-0.9702959974411298, \
    -0.9316660034779380,0.7509009750438762, \
    -0.5058825420350775,0.7766280231903698, \
    -0.1591105418860929,-0.7614693278871865, \
    -0.6171441191167790E-01,-0.9548062395608765, \
    -0.8211827496355327,-0.9063342142005131, \
    0.9909185703328497,0.9397084665195838, \
    0.8902356582373753,0.9582397465258308, \
    -0.9888160497196922,-0.6701339599706453, \
    -0.9449104256261275,0.9907698250163826, \
    -0.8840101170670746,0.9954576420924693, \
    -0.9868058887952446,-0.9884037853120492, \
    0.8605082508169065,0.1586026433797343, \
    -0.7662425769553762,-0.9472631440912187, \
    0.5782109944873408,0.7561475499065624, \
    0.9307512366430157,0.8850736835159266, \
    -0.4904564371890563 ] )
  ws = np.array ( [ \
    0.2913207807844331E-01,0.2275827975953009E-01, \
    0.2791249243709578E-01,0.1938452906022129E-01, \
    0.4364917601570797E-01,0.1237342034594484E-01, \
    0.1138865003097454E-01,0.4923704893009620E-01, \
    0.3063932561386288E-01,0.4428512850707964E-01, \
    0.4629109684697653E-01,0.1691765251942423E-01, \
    0.2741532810734821E-01,0.4052530459111174E-01, \
    0.5261109228291892E-01,0.4417466900490126E-01, \
    0.3058410753870397E-01,0.6406355493167926E-02, \
    0.6769861004210370E-02,0.4884106698203454E-01, \
    0.1697345666295625E-01,0.3712422414211005E-01, \
    0.4783538888580537E-01,0.2351215352613192E-01, \
    0.3967485550125242E-01,0.5227057590404430E-01, \
    0.7706038595693665E-02,0.1393888240267354E-01, \
    0.2605232454276587E-01,0.3221602953245650E-02, \
    0.3639783162612337E-01,0.3177013439355753E-01, \
    0.2662783889362856E-01,0.2133361104980210E-01, \
    0.4324098371978138E-01,0.2186171413802145E-01, \
    0.3997793758416952E-01,0.7491762737168889E-02, \
    0.1718989677527449E-01,0.3150610588787735E-01, \
    0.3338285362580999E-01,0.3522688180840185E-01, \
    0.2250843481977659E-01,0.2767390941687784E-01, \
    0.2163076701762542E-01,0.6370202612529778E-02, \
    0.1292816837261490E-02,0.1772036481071653E-01, \
    0.2045516332866545E-01,0.5029942715423091E-02, \
    0.2555860092259501E-01,0.8908434653957875E-02, \
    0.4462964590144296E-01,0.2350361388650933E-01, \
    0.1300162042596963E-01,0.1619762342723978E-01, \
    0.3633406947058673E-01,0.4148575443002976E-02, \
    0.3043458935989431E-01,0.3780056077982088E-01, \
    0.2670761755118099E-01,0.4679248624556967E-01, \
    0.6655017468306593E-02,0.1016870301128343E-02, \
    0.3956208492384800E-01,0.4422000056024995E-01, \
    0.1600493333371462E-02,0.9542615574085509E-02, \
    0.5101463103747718E-01,0.2316486911009150E-02, \
    0.2082363944511977E-01,0.1450858408533323E-01, \
    0.2593506316945297E-01,0.4854771494052668E-01, \
    0.1406093874479688E-01,0.2980564799727076E-01, \
    0.4032704717924811E-01,0.2836242586524349E-01, \
    0.1662837317311870E-02,0.3331747639887452E-01, \
    0.1737244435785181E-01,0.1818621007558914E-01, \
    0.4099371056923931E-01,0.5481494042070843E-01, \
    0.4070179363666812E-01,0.4218182579123851E-01, \
    0.8533899793279886E-02,0.5949667491635394E-02, \
    0.2693305692079543E-01,0.3035811941473991E-01, \
    0.1815553496055310E-01,0.3365556943518273E-02, \
    0.5641437853076681E-02,0.1997142107835644E-01, \
    0.1803786451914521E-01,0.2269810849285899E-02, \
    0.1824056247133745E-01,0.4961745614234228E-02, \
    0.5229975396089418E-02,0.3090226019029179E-01, \
    0.4530557980884387E-02,0.1260165841456744E-01, \
    0.2688472868433625E-01,0.6305207130138189E-02, \
    0.4114195161424335E-02,0.8573396052945570E-02, \
    0.6467557193927746E-02,0.2703578258059107E-02, \
    0.1975997243239372E-01,0.9381005409995410E-02, \
    0.6472606174579578E-02,0.1382406712148664E-01, \
    0.1805324127586059E-01,0.6329200107849942E-02, \
    0.3895024567992489E-02,0.3809507629042853E-02, \
    0.6517542895566797E-02,0.7169776873936058E-02, \
    0.1060178841340027E-01,0.1641915380777178E-01, \
    0.3678722762764779E-01,0.1379818565014169E-01, \
    0.1123917596421086E-01,0.6410312514956618E-02, \
    0.1884563206279892E-01,0.8912626526178684E-02, \
    0.4962602708111043E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule27 ( n ):

#*****************************************************************************80
#
## rule27() returns the rule of degree 27.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.3179234344617641,0.9945426115270097, \
    0.3179234344617642,-0.9945426115270097, \
    -0.9658581524130557,0.9842821312283567, \
    0.9658581524130559,-0.9842821312283565, \
    0.4546608217543911,0.9794570195190775, \
    -0.4546608217543910,-0.9794570195190775, \
    0.9203445363225692,0.9966680243748195, \
    -0.9203445363225690,-0.9966680243748197, \
    0.5921826557247571,0.9227007102569557, \
    -0.5921826557247569,-0.9227007102569557, \
    -0.6265556238656111,0.9943315661391944, \
    0.6265556238656114,-0.9943315661391944, \
    -0.9106466233445932,0.9127106311205702, \
    0.9106466233445935,-0.9127106311205699, \
    -0.4796281374834562,0.9651530210115425, \
    0.4796281374834563,-0.9651530210115425, \
    0.6298732844502039,0.9921721529860120, \
    -0.6298732844502036,-0.9921721529860120, \
    -0.8335744040052592,0.9824660135148449, \
    0.8335744040052594,-0.9824660135148449, \
    0.1959395767367455,0.9899174626675955, \
    -0.1959395767367454,-0.9899174626675955, \
    -0.1386302484544642,0.9830581303940688, \
    0.1386302484544643,-0.9830581303940688, \
    -0.7022171903082602,0.9292585099108952, \
    0.7022171903082605,-0.9292585099108952, \
    0.7970439287784883,0.9675649927064782, \
    -0.7970439287784881,-0.9675649927064782, \
    -0.8020178388613470,0.8160591260895965, \
    0.8020178388613470,-0.8160591260895965, \
    -0.5398233377470387,0.8364692379579785, \
    0.5398233377470387,-0.8364692379579785, \
    -0.1520649596611693,0.8369974777769484, \
    0.1520649596611695,-0.8369974777769484, \
    -0.2998875490507344,0.3409328206751328, \
    0.2998875490507344,-0.3409328206751328, \
    -0.3209420000531037,0.9175861963438381, \
    0.3209420000531039,-0.9175861963438381, \
    -0.9020677393268002E-01,0.1670667038911821, \
    0.9020677393268005E-01,-0.1670667038911821, \
    0.1926515070565072,0.5293872532788142, \
    -0.1926515070565071,-0.5293872532788142, \
    0.4976080851052046,0.7953917795116896, \
    -0.4976080851052045,-0.7953917795116896, \
    0.3002782637358375E-01,0.9362295643614138, \
    -0.3002782637358363E-01,-0.9362295643614138, \
    0.6881617137006012,0.8842713205559528, \
    -0.6881617137006012,-0.8842713205559528, \
    0.2200611683790181,0.8481900686404982, \
    -0.2200611683790180,-0.8481900686404982, \
    0.4531153802420229E-01,0.3769373245611116, \
    -0.4531153802420225E-01,-0.3769373245611116, \
    -0.4941549461445193,0.5167583593472795, \
    0.4941549461445194,-0.5167583593472795, \
    0.3405123948054840,0.6649111597000639, \
    -0.3405123948054839,-0.6649111597000639, \
    -0.1521097283009047,0.5602567958473701, \
    0.1521097283009048,-0.5602567958473701, \
    0.3710843473830662,0.9336952377043988, \
    -0.3710843473830661,-0.9336952377043988, \
    -0.3536770731498163,0.7123617422035845, \
    0.3536770731498164,-0.7123617422035845, \
    -0.6668117984035637,0.6750511711635266, \
    0.6668117984035637,-0.6750511711635266, \
    0.3880331998977081E-01,0.7201416766661869, \
    -0.3880331998977073E-01,-0.7201416766661869 ] )
  ys = np.array ( [ \
    -0.9945426115270097,-0.3179234344617641, \
    0.9945426115270097,0.3179234344617642, \
    -0.9842821312283568,-0.9658581524130558, \
    0.9842821312283566,0.9658581524130561, \
    -0.9794570195190775,0.4546608217543910, \
    0.9794570195190775,-0.4546608217543909, \
    -0.9966680243748194,0.9203445363225691, \
    0.9966680243748196,-0.9203445363225689, \
    -0.9227007102569557,0.5921826557247570, \
    0.9227007102569557,-0.5921826557247568, \
    -0.9943315661391944,-0.6265556238656113, \
    0.9943315661391944,0.6265556238656115, \
    -0.9127106311205703,-0.9106466233445933, \
    0.9127106311205700,0.9106466233445936, \
    -0.9651530210115425,-0.4796281374834563, \
    0.9651530210115425,0.4796281374834564, \
    -0.9921721529860120,0.6298732844502037, \
    0.9921721529860120,-0.6298732844502035, \
    -0.9824660135148449,-0.8335744040052593, \
    0.9824660135148449,0.8335744040052595, \
    -0.9899174626675955,0.1959395767367454, \
    0.9899174626675955,-0.1959395767367453, \
    -0.9830581303940688,-0.1386302484544642, \
    0.9830581303940688,0.1386302484544643, \
    -0.9292585099108952,-0.7022171903082604, \
    0.9292585099108952,0.7022171903082606, \
    -0.9675649927064782,0.7970439287784882, \
    0.9675649927064782,-0.7970439287784880, \
    -0.8160591260895965,-0.8020178388613470, \
    0.8160591260895965,0.8020178388613470, \
    -0.8364692379579785,-0.5398233377470387, \
    0.8364692379579785,0.5398233377470387, \
    -0.8369974777769484,-0.1520649596611694, \
    0.8369974777769484,0.1520649596611695, \
    -0.3409328206751328,-0.2998875490507344, \
    0.3409328206751328,0.2998875490507344, \
    -0.9175861963438381,-0.3209420000531038, \
    0.9175861963438381,0.3209420000531039, \
    -0.1670667038911821,-0.9020677393268003E-01, \
    0.1670667038911821,0.9020677393268006E-01, \
    -0.5293872532788142,0.1926515070565072, \
    0.5293872532788142,-0.1926515070565071, \
    -0.7953917795116896,0.4976080851052045, \
    0.7953917795116896,-0.4976080851052044, \
    -0.9362295643614138,0.3002782637358369E-01, \
    0.9362295643614138,-0.3002782637358357E-01, \
    -0.8842713205559528,0.6881617137006012, \
    0.8842713205559528,-0.6881617137006012, \
    -0.8481900686404982,0.2200611683790180, \
    0.8481900686404982,-0.2200611683790179, \
    -0.3769373245611116,0.4531153802420227E-01, \
    0.3769373245611116,-0.4531153802420223E-01, \
    -0.5167583593472795,-0.4941549461445193, \
    0.5167583593472795,0.4941549461445194, \
    -0.6649111597000639,0.3405123948054840, \
    0.6649111597000639,-0.3405123948054838, \
    -0.5602567958473701,-0.1521097283009047, \
    0.5602567958473701,0.1521097283009048, \
    -0.9336952377043988,0.3710843473830662, \
    0.9336952377043988,-0.3710843473830661, \
    -0.7123617422035845,-0.3536770731498164, \
    0.7123617422035845,0.3536770731498165, \
    -0.6750511711635266,-0.6668117984035637, \
    0.6750511711635266,0.6668117984035637, \
    -0.7201416766661869,0.3880331998977077E-01, \
    0.7201416766661869,-0.3880331998977068E-01 ] )
  ws = np.array ( [ \
    0.2672899331427035E-02,0.2672899331427035E-02, \
    0.2672899331427035E-02,0.2672899331427035E-02, \
    0.2445906596530064E-02,0.2445906596530064E-02, \
    0.2445906596530064E-02,0.2445906596530064E-02, \
    0.5784555125932030E-02,0.5784555125932030E-02, \
    0.5784555125932030E-02,0.5784555125932030E-02, \
    0.1774682379035372E-02,0.1774682379035372E-02, \
    0.1774682379035372E-02,0.1774682379035372E-02, \
    0.9666652283416993E-02,0.9666652283416993E-02, \
    0.9666652283416993E-02,0.9666652283416993E-02, \
    0.3475754833559290E-02,0.3475754833559290E-02, \
    0.3475754833559290E-02,0.3475754833559290E-02, \
    0.9738340699044858E-02,0.9738340699044858E-02, \
    0.9738340699044858E-02,0.9738340699044858E-02, \
    0.9913445575624551E-02,0.9913445575624551E-02, \
    0.9913445575624551E-02,0.9913445575624551E-02, \
    0.4024564097795350E-02,0.4024564097795350E-02, \
    0.4024564097795350E-02,0.4024564097795350E-02, \
    0.5467642658052182E-02,0.5467642658052182E-02, \
    0.5467642658052182E-02,0.5467642658052182E-02, \
    0.6791307131143990E-02,0.6791307131143990E-02, \
    0.6791307131143990E-02,0.6791307131143990E-02, \
    0.7849471971542231E-02,0.7849471971542231E-02, \
    0.7849471971542231E-02,0.7849471971542231E-02, \
    0.1481562369739479E-01,0.1481562369739479E-01, \
    0.1481562369739479E-01,0.1481562369739479E-01, \
    0.8652776980870136E-02,0.8652776980870136E-02, \
    0.8652776980870136E-02,0.8652776980870136E-02, \
    0.1938931217339045E-01,0.1938931217339045E-01, \
    0.1938931217339045E-01,0.1938931217339045E-01, \
    0.2728047644809397E-01,0.2728047644809397E-01, \
    0.2728047644809397E-01,0.2728047644809397E-01, \
    0.2833042504936177E-01,0.2833042504936177E-01, \
    0.2833042504936177E-01,0.2833042504936177E-01, \
    0.5141433190365619E-01,0.5141433190365619E-01, \
    0.5141433190365619E-01,0.5141433190365619E-01, \
    0.1775207295130232E-01,0.1775207295130232E-01, \
    0.1775207295130232E-01,0.1775207295130232E-01, \
    0.4944421261124536E-01,0.4944421261124536E-01, \
    0.4944421261124536E-01,0.4944421261124536E-01, \
    0.3632695571196309E-01,0.3632695571196309E-01, \
    0.3632695571196309E-01,0.3632695571196309E-01, \
    0.2905709329104403E-01,0.2905709329104403E-01, \
    0.2905709329104403E-01,0.2905709329104403E-01, \
    0.1861253661440120E-01,0.1861253661440120E-01, \
    0.1861253661440120E-01,0.1861253661440120E-01, \
    0.1362514538944166E-01,0.1362514538944166E-01, \
    0.1362514538944166E-01,0.1362514538944166E-01, \
    0.2778931208298291E-01,0.2778931208298291E-01, \
    0.2778931208298291E-01,0.2778931208298291E-01, \
    0.4496161760244370E-01,0.4496161760244370E-01, \
    0.4496161760244370E-01,0.4496161760244370E-01, \
    0.4391754850935400E-01,0.4391754850935400E-01, \
    0.4391754850935400E-01,0.4391754850935400E-01, \
    0.3461629438577501E-01,0.3461629438577501E-01, \
    0.3461629438577501E-01,0.3461629438577501E-01, \
    0.4733898929183223E-01,0.4733898929183223E-01, \
    0.4733898929183223E-01,0.4733898929183223E-01, \
    0.1448889464186536E-01,0.1448889464186536E-01, \
    0.1448889464186536E-01,0.1448889464186536E-01, \
    0.3863763742526743E-01,0.3863763742526743E-01, \
    0.3863763742526743E-01,0.3863763742526743E-01, \
    0.3295515782263461E-01,0.3295515782263461E-01, \
    0.3295515782263461E-01,0.3295515782263461E-01, \
    0.3809514391912308E-01,0.3809514391912308E-01, \
    0.3809514391912308E-01,0.3809514391912308E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule28 ( n ):

#*****************************************************************************80
#
## rule28() returns the rule of degree 28.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.2827621856762107,-0.8043038962721508, \
    -0.3395780944817125,0.9664085101515743, \
    -0.1096329656209190E-01,0.8193786706976756, \
    -0.9286317198271657,0.4198022792026188, \
    -0.8604918125918429,0.8109783092388664, \
    0.5614606479838853,0.1250139096754087E-01, \
    0.6890874578865651,-0.8003785261499256, \
    -0.7186772992712774,0.2097379198022608E-01, \
    -0.9904175004752394,0.5247683324321177, \
    0.9879057318966782,0.9872995514825285, \
    -0.2010899760026548,-0.7150754139309137, \
    -0.9744175518522036,-0.2743957404149748, \
    -0.8801155850915744E-01,-0.9120488211036881, \
    0.5997911603089924E-01,-0.9822903323396509, \
    0.9933058426309856,-0.1094425840746250, \
    0.8016032845806299,-0.3785896040093871, \
    0.9908494000362051,-0.9920099650417782, \
    -0.5334142633484058,-0.6081971936243052, \
    -0.9913559247973139,-0.4420258077139650, \
    0.9904922021473850,-0.2701059581013934, \
    -0.6762870118531359,0.4550203878192706, \
    -0.9933274734742550,0.1025031015215653, \
    -0.9908021888968861,0.4018136560549200E-02, \
    0.1830465948969627,-0.9190332253043175, \
    -0.7967293798867977,0.8910586530553062, \
    0.9738677077447094,0.4922211332598602, \
    -0.9935974988322385,-0.7469015595759197, \
    -0.7474851457426346,-0.8461768034166064, \
    0.7263311602661456,0.1838655693690960, \
    -0.8924925604346934,0.3473229569871696, \
    0.7888084262939273,-0.1622547625661196, \
    0.1708950639909230,-0.9858834062192522, \
    0.8595474037303855,-0.2487721441258377, \
    0.9897369384324803,-0.8592565754231390, \
    0.3552890037180957,0.9343486754942414, \
    -0.5982760380368914,0.9012497934650560, \
    -0.8867898943082418,-0.2973823530897202, \
    0.2929780512625694,0.5109886162010564, \
    -0.6362138293509048,0.9840555620580882, \
    0.6242255274464619,0.9500492760473710, \
    0.6206677950945041,0.3667200892151265, \
    -0.3354257519635134,0.6532050712129780, \
    0.8340712667685216,0.9517120425530485, \
    0.4939764190001616,0.8519117390868273, \
    -0.4641713197529147,0.3096864797777032, \
    -0.9951406550164114,0.6849334791605266, \
    0.5377487266764005,0.6596506837798173, \
    -0.6190982139272722,0.9676681958645598, \
    -0.8663734426507712,0.9229408505602535, \
    0.8925298503917507,0.1376340175855351, \
    -0.4255923534036878,-0.5069417238664446, \
    -0.9581264401591332,0.7956423904664977, \
    -0.9438198089736733,-0.9602193183322451, \
    -0.9546324794056378,0.7865853669573317, \
    0.7640178616435913,-0.9037187541181603E-01, \
    0.6583886775017005,0.9394184495408773, \
    0.1210974568433837,0.3181846883529323, \
    -0.9476649688000099,-0.7447346202738520, \
    0.7669083321105266,0.3177180418892223, \
    0.9005374034994568,0.4905235558364557, \
    -0.2799102574207112,-0.7756668408683119, \
    -0.7847585523489610,-0.5947448678197160, \
    -0.6835954896209653E-01,-0.4603444798372620, \
    0.1267789889405305,0.9957007235251634, \
    -0.9555617449567378,0.4926175951876377, \
    0.9580744421864001,0.6544409855907934, \
    -0.2589485669037206,-0.4625383187120728, \
    0.8779137327105354,-0.8753270142023138, \
    -0.7680237343653598,-0.4646141113930034, \
    -0.6237643000374615,-0.1004225708457810, \
    0.2934408497776114,-0.8838031019815079, \
    -0.8252198025376763E-01,0.1013709068378068, \
    -0.6355163316600663,-0.2814473462899598, \
    0.9991999747547105 ] )
  ys = np.array ( [ \
    -0.2146915742023843,-0.3602259227928870, \
    -0.2366070789246893,-0.1067737835329393, \
    -0.7832467667692294E-01,0.5090533388398083E-02, \
    0.5655320173536176E-02,-0.9091460408400718, \
    -0.3610436689009546,0.1173540113566495, \
    -0.7580822207698504,0.7636857906206649, \
    -0.6742700466367159,0.3605821467647248, \
    0.2565264593758684,0.8682397249203467, \
    -0.9887795883901583,-0.8777099834380453, \
    -0.9937283708213308,0.9906296802548810, \
    0.8788092453036578,0.9706849956765652, \
    -0.7829696251737753E-01,0.9937649402523892, \
    -0.1524877190213388,-0.2242135513466236, \
    0.9919534212785273,0.9960588898544035, \
    -0.5034894383669408,0.9599951355029216, \
    -0.5645937597081716,0.9447996831444674, \
    0.2711989824047218,0.1447359435070455, \
    0.9871535260388329,0.9140753757822478, \
    -0.2960350108035981,0.8371402678277077, \
    -0.7650309750102933,-0.3188681363434392, \
    -0.9938368658433656,-0.6339545710762906, \
    -0.6212095493273496,-0.9934382054756534, \
    0.4715389357436094,-0.7215460671816014, \
    0.6773640866690520,0.9779955899159012, \
    0.9970513707078691,-0.1551145670991118, \
    -0.3024178806712221,-0.9926567100374114, \
    -0.8660993570031557,-0.4956056862948234, \
    0.8382998942855415,0.9259687805728221, \
    -0.8351882927550272,0.9386358290968080, \
    -0.9900384261478909,-0.4464745325070345, \
    -0.9936162118016632,-0.8235872679034352, \
    -0.5983594352543780,0.9398154839397104, \
    -0.7371773517980565,0.7366500643247871, \
    0.8982625204679442,0.1211489804261566, \
    0.9859353129167986,-0.8465334600907201, \
    0.7342041846853576,-0.4349009915613299, \
    0.5008348384608579,-0.9942925485328575, \
    -0.9626593056228334,-0.2709700923096490, \
    0.5944472663027801E-01,-0.9248481403512147, \
    -0.4757878778805171,0.9921234070894396E-01, \
    0.9864359054124004,0.5564466223050852, \
    -0.9075561035062022,0.6130603473347437, \
    -0.9196402734279348,-0.6285797630023995, \
    0.7360652264674404,0.9946281004658378, \
    -0.1056502846403645,0.8343858336015567, \
    0.7795434558480316,0.2437361149690468, \
    0.4083791315159580,-0.8237952273107227E-01, \
    -0.6450626080823243,0.4764961946576270, \
    0.7429354103100736,-0.9752458082257867, \
    0.3137605530793695,0.7602258278505522E-01, \
    0.6028197206610887,-0.9665994542595457, \
    -0.9448687562971092,0.7450892979512898, \
    0.8580812769827701,0.6469685322672528, \
    -0.4730667721016463,0.4691067254414554, \
    0.9468223400568799,0.5747271977509141, \
    0.8487224420002684,0.9604420521431418, \
    0.4325756220233750,-0.1154193690840114, \
    0.2996859346038543,0.6079262704780987, \
    -0.3014753479396839,0.2694764821728903, \
    0.6210587156046703,0.9250623306784818, \
    0.4091950530277537,-0.1149400908487048, \
    -0.9509596164554358,0.4489210023756193, \
    0.2491367754635779,0.2328542094943754, \
    -0.3147181280829211,0.6575404381717325, \
    -0.7572545223612748,0.8744761196977546E-01, \
    0.7809511457782177,-0.9573612252124380, \
    0.5984333435621010E-01,-0.4795365437914892, \
    0.8758201084343584,-0.6288667697841542, \
    -0.7704960778314179,-0.7807547746986493, \
    -0.2948221971565224,-0.9595773298541288, \
    -0.7859464731741874,-0.8701241408788146, \
    -0.4848613986697829,-0.8903571922698699, \
    -0.8832911479917025,-0.6435327316304572, \
    -0.5075800418230667E-01 ] )
  ws = np.array ( [ \
    0.1740144063407695E-02,0.6784563755290567E-02, \
    0.1209466540188899E-01,0.5276845120506419E-02, \
    0.2120637597472411E-01,0.1500950169216209E-01, \
    0.1016605179698056E-01,0.1052237804962158E-01, \
    0.1389531092331450E-01,0.1799231574573814E-01, \
    0.1681749672744976E-01,0.2190516172058484E-01, \
    0.1802050074136916E-01,0.1929827700816552E-01, \
    0.2322655354121691E-01,0.1715984331158577E-01, \
    0.7585152723116851E-03,0.1423586238543194E-01, \
    0.6209204642340611E-03,0.8055582944619972E-03, \
    0.1686431398199053E-01,0.6130199135277467E-02, \
    0.8266675752855135E-02,0.3947441053087870E-02, \
    0.3763432904885534E-01,0.1544537020393182E-01, \
    0.4895887118324937E-02,0.5766157576611153E-03, \
    0.3911408899973994E-02,0.1134055149899166E-01, \
    0.2045540821981484E-01,0.1254460489172730E-01, \
    0.5370936278809426E-02,0.5162980339438905E-02, \
    0.5510957955189620E-02,0.1348681146014646E-01, \
    0.5293461261550956E-02,0.2135158963906704E-01, \
    0.3872040956962797E-02,0.4041863730898066E-01, \
    0.3480075985572175E-02,0.3082881220603644E-01, \
    0.3934841673430547E-02,0.4955048643733777E-02, \
    0.5332713420324274E-02,0.3127092112918890E-01, \
    0.3263868066569824E-01,0.3643906126193626E-02, \
    0.1773410002914162E-02,0.2031653637703585E-01, \
    0.9778965531187402E-02,0.4720821658621592E-02, \
    0.2492177802034716E-02,0.2644508244904856E-01, \
    0.1656291578773864E-01,0.9176500057842589E-02, \
    0.1732347887472145E-01,0.1561854636309510E-01, \
    0.2892151505244423E-02,0.3887473612274506E-01, \
    0.3107151229520027E-02,0.2613845455837795E-01, \
    0.3698667210865119E-01,0.2566493481700192E-02, \
    0.1615348439627276E-01,0.3075142974941159E-01, \
    0.2904460597417912E-02,0.2398826862979595E-01, \
    0.7145392996633393E-02,0.8978366822810722E-02, \
    0.2612889620260116E-01,0.1874378199539706E-01, \
    0.1917559308928981E-01,0.4661196658021693E-02, \
    0.1235879177909568E-01,0.4010025698621002E-01, \
    0.3740253247098928E-01,0.3148001303878885E-02, \
    0.3330951974159902E-01,0.1500177718625442E-01, \
    0.6070126982071918E-02,0.3772728641321498E-01, \
    0.1934239152098538E-01,0.2980908782028305E-01, \
    0.1060149985804505E-01,0.1169140727671868E-01, \
    0.2913863637730209E-01,0.2512926081791887E-02, \
    0.4408214653268561E-01,0.2616523021560373E-01, \
    0.2824238355893381E-02,0.3534124084616964E-01, \
    0.3855284013804392E-01,0.3769601120920466E-01, \
    0.3068556194531641E-01,0.1107117178829623E-01, \
    0.1675502525295356E-01,0.4250234458185585E-02, \
    0.2160027234544727E-01,0.4964511475611218E-01, \
    0.3661675186805007E-01,0.1113946092997709E-01, \
    0.4594039996241282E-02,0.2058836038539646E-01, \
    0.8608231530163511E-02,0.1071439010120374E-01, \
    0.1325231032613585E-01,0.2793585524817994E-01, \
    0.1060087465526644E-01,0.4186289109506627E-01, \
    0.2038937560848930E-01,0.4779376144301057E-02, \
    0.4600352201496827E-01,0.4850236286164095E-01, \
    0.1563580434067219E-01,0.2738173661329469E-01, \
    0.3152680760913545E-01,0.4699759394230683E-01, \
    0.1758154363368765E-01,0.1705163560097511E-01, \
    0.4564749915571795E-01,0.3274246294590765E-01, \
    0.9932190596257133E-02,0.3764556185875566E-01, \
    0.5058095830353233E-01,0.4537296603002153E-01, \
    0.4951708484325965E-01,0.3279405659962938E-02, \
    0.9987676851635598E-02,0.4573491590126628E-01, \
    0.9304988468918474E-02,0.1136613167624352E-01, \
    0.5119306902579393E-01,0.4198377464395852E-01, \
    0.1182329164018337E-01,0.1992962132997380E-01, \
    0.2179036392120167E-01,0.2957452226482192E-01, \
    0.3999530391333647E-01,0.1478968751484580E-01, \
    0.3170728715126719E-01,0.1199170942901081E-01, \
    0.4711944799135396E-01,0.2445849079621999E-01, \
    0.1955624669135905E-01,0.4043330460830744E-01, \
    0.2815879734180029E-02 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule29 ( n ):

#*****************************************************************************80
#
## rule29() returns the rule of degree 29.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.9957609056803307,0.9554778819247284, \
    0.9957609056803309,-0.9554778819247282, \
    -0.8018419403764031,0.9936244517402659, \
    0.8018419403764033,-0.9936244517402659, \
    -0.9579902382554616,0.9905651653257478, \
    0.9579902382554618,-0.9905651653257476, \
    0.2638223412555635E-01,0.9935202992997069, \
    -0.2638223412555623E-01,-0.9935202992997069, \
    -0.5066682706262957,0.9913300131756428, \
    0.5066682706262959,-0.9913300131756428, \
    -0.2298993811511364,0.9820954997507334, \
    0.2298993811511365,-0.9820954997507334, \
    0.4377228178889339,0.9940035328985276, \
    -0.4377228178889338,-0.9940035328985276, \
    -0.6971536278750922,0.9699469973610456, \
    0.6971536278750924,-0.9699469973610456, \
    -0.1287796452538595,0.9374257301963881, \
    0.1287796452538596,-0.9374257301963881, \
    0.2219765871034010,0.9669818379796637, \
    -0.2219765871034008,-0.9669818379796637, \
    0.8793284704221047,0.9627913549967865, \
    -0.8793284704221045,-0.9627913549967865, \
    -0.4224857795905392,0.8997395988035505, \
    0.4224857795905393,-0.8997395988035505, \
    0.7561015490560310,0.9929163478894405, \
    -0.7561015490560308,-0.9929163478894405, \
    0.2640620995843525,0.8673709698403427, \
    -0.2640620995843524,-0.8673709698403427, \
    -0.8876763767236916,0.9499938690143425, \
    0.8876763767236918,-0.9499938690143425, \
    0.6107736243515250,0.9600495691709722, \
    -0.6107736243515248,-0.9600495691709722, \
    -0.7868750412424903,0.8719483642340994, \
    0.7868750412424903,-0.8719483642340994, \
    -0.1141990095980696E-01,0.9167780797645280, \
    0.1141990095980707E-01,-0.9167780797645280, \
    0.6200952646798407,0.8398067949907553, \
    -0.6200952646798407,-0.8398067949907553, \
    -0.4280702467551835,0.3950643020883297, \
    0.4280702467551835,-0.3950643020883297, \
    0.3401810242198736,0.6973120201514252, \
    -0.3401810242198735,-0.6973120201514252, \
    -0.2617868665129255,0.2355937519408776, \
    0.2617868665129255,-0.2355937519408775, \
    0.1411576681950311,0.8161158957508043, \
    -0.1411576681950309,-0.8161158957508043, \
    -0.3695797105378154E-01,0.6981295844594165, \
    0.3695797105378162E-01,-0.6981295844594165, \
    -0.6312274766498698,0.9353634542809267, \
    0.6312274766498700,-0.9353634542809267, \
    -0.1150463641736545,0.9674061994537117E-01, \
    0.1150463641736545,-0.9674061994537114E-01, \
    -0.3747271550737231,0.9438572336357420, \
    0.3747271550737232,-0.9438572336357420, \
    0.5008869009053424,0.7904714944143627, \
    -0.5008869009053424,-0.7904714944143627, \
    0.1608699923234913,0.5513908795637696, \
    -0.1608699923234913,-0.5513908795637696, \
    -0.5657668007893579,0.8210097847827826, \
    0.5657668007893579,-0.8210097847827826, \
    0.7712590259177344,0.8970730060299638, \
    -0.7712590259177344,-0.8970730060299638, \
    0.4163780011554897,0.9113544664316420, \
    -0.4163780011554896,-0.9113544664316420, \
    -0.5836842069804584,0.5579917371493338, \
    0.5836842069804584,-0.5579917371493338, \
    -0.2215359986069006,0.8254893061838994, \
    0.2215359986069007,-0.8254893061838994, \
    -0.4009765829120037,0.6957123574117627, \
    0.4009765829120038,-0.6957123574117627, \
    -0.2343918950839540E-01,0.3763993540852892, \
    0.2343918950839545E-01,-0.3763993540852892, \
    -0.7105079759089011,0.7179044391714098, \
    0.7105079759089011,-0.7179044391714098, \
    -0.2200751569931638,0.5431094815533654, \
    0.2200751569931638,-0.5431094815533654 ] )
  ys = np.array ( [ \
    -0.9554778819247285,-0.9957609056803308, \
    0.9554778819247283,0.9957609056803310, \
    -0.9936244517402659,-0.8018419403764032, \
    0.9936244517402659,0.8018419403764034, \
    -0.9905651653257479,-0.9579902382554617, \
    0.9905651653257477,0.9579902382554619, \
    -0.9935202992997069,0.2638223412555629E-01, \
    0.9935202992997069,-0.2638223412555617E-01, \
    -0.9913300131756428,-0.5066682706262958, \
    0.9913300131756428,0.5066682706262960, \
    -0.9820954997507334,-0.2298993811511365, \
    0.9820954997507334,0.2298993811511366, \
    -0.9940035328985276,0.4377228178889339, \
    0.9940035328985276,-0.4377228178889337, \
    -0.9699469973610456,-0.6971536278750923, \
    0.9699469973610456,0.6971536278750925, \
    -0.9374257301963881,-0.1287796452538595, \
    0.9374257301963881,0.1287796452538596, \
    -0.9669818379796637,0.2219765871034009, \
    0.9669818379796637,-0.2219765871034008, \
    -0.9627913549967865,0.8793284704221046, \
    0.9627913549967865,-0.8793284704221044, \
    -0.8997395988035505,-0.4224857795905393, \
    0.8997395988035505,0.4224857795905394, \
    -0.9929163478894405,0.7561015490560309, \
    0.9929163478894405,-0.7561015490560307, \
    -0.8673709698403427,0.2640620995843524, \
    0.8673709698403427,-0.2640620995843523, \
    -0.9499938690143425,-0.8876763767236917, \
    0.9499938690143425,0.8876763767236919, \
    -0.9600495691709722,0.6107736243515249, \
    0.9600495691709722,-0.6107736243515247, \
    -0.8719483642340994,-0.7868750412424903, \
    0.8719483642340994,0.7868750412424903, \
    -0.9167780797645280,-0.1141990095980701E-01, \
    0.9167780797645280,0.1141990095980712E-01, \
    -0.8398067949907553,0.6200952646798407, \
    0.8398067949907553,-0.6200952646798407, \
    -0.3950643020883297,-0.4280702467551835, \
    0.3950643020883297,0.4280702467551835, \
    -0.6973120201514252,0.3401810242198735, \
    0.6973120201514252,-0.3401810242198734, \
    -0.2355937519408776,-0.2617868665129255, \
    0.2355937519408775,0.2617868665129255, \
    -0.8161158957508043,0.1411576681950310, \
    0.8161158957508043,-0.1411576681950309, \
    -0.6981295844594165,-0.3695797105378158E-01, \
    0.6981295844594165,0.3695797105378167E-01, \
    -0.9353634542809267,-0.6312274766498699, \
    0.9353634542809267,0.6312274766498701, \
    -0.9674061994537118E-01,-0.1150463641736545, \
    0.9674061994537116E-01,0.1150463641736545, \
    -0.9438572336357420,-0.3747271550737232, \
    0.9438572336357420,0.3747271550737233, \
    -0.7904714944143627,0.5008869009053424, \
    0.7904714944143627,-0.5008869009053424, \
    -0.5513908795637696,0.1608699923234913, \
    0.5513908795637696,-0.1608699923234912, \
    -0.8210097847827826,-0.5657668007893579, \
    0.8210097847827826,0.5657668007893579, \
    -0.8970730060299638,0.7712590259177344, \
    0.8970730060299638,-0.7712590259177344, \
    -0.9113544664316420,0.4163780011554896, \
    0.9113544664316420,-0.4163780011554895, \
    -0.5579917371493338,-0.5836842069804584, \
    0.5579917371493338,0.5836842069804584, \
    -0.8254893061838994,-0.2215359986069006, \
    0.8254893061838994,0.2215359986069007, \
    -0.6957123574117627,-0.4009765829120038, \
    0.6957123574117627,0.4009765829120039, \
    -0.3763993540852892,-0.2343918950839542E-01, \
    0.3763993540852892,0.2343918950839547E-01, \
    -0.7179044391714098,-0.7105079759089011, \
    0.7179044391714098,0.7105079759089011, \
    -0.5431094815533654,-0.2200751569931638, \
    0.5431094815533654,0.2200751569931639 ] )
  ws = np.array ( [ \
    0.1227297430951934E-02,0.1227297430951934E-02, \
    0.1227297430951934E-02,0.1227297430951934E-02, \
    0.2705540778783016E-02,0.2705540778783016E-02, \
    0.2705540778783016E-02,0.2705540778783016E-02, \
    0.1737911403412906E-02,0.1737911403412906E-02, \
    0.1737911403412906E-02,0.1737911403412906E-02, \
    0.4392077971620324E-02,0.4392077971620324E-02, \
    0.4392077971620324E-02,0.4392077971620324E-02, \
    0.5022826333532844E-02,0.5022826333532844E-02, \
    0.5022826333532844E-02,0.5022826333532844E-02, \
    0.7874070819611865E-02,0.7874070819611865E-02, \
    0.7874070819611865E-02,0.7874070819611865E-02, \
    0.4436852998533855E-02,0.4436852998533855E-02, \
    0.4436852998533855E-02,0.4436852998533855E-02, \
    0.5267024709906290E-02,0.5267024709906290E-02, \
    0.5267024709906290E-02,0.5267024709906290E-02, \
    0.5674802470601283E-02,0.5674802470601283E-02, \
    0.5674802470601283E-02,0.5674802470601283E-02, \
    0.1214093209674204E-01,0.1214093209674204E-01, \
    0.1214093209674204E-01,0.1214093209674204E-01, \
    0.6621349971001042E-02,0.6621349971001042E-02, \
    0.6621349971001042E-02,0.6621349971001042E-02, \
    0.1231662091800690E-01,0.1231662091800690E-01, \
    0.1231662091800690E-01,0.1231662091800690E-01, \
    0.3418869012187221E-02,0.3418869012187221E-02, \
    0.3418869012187221E-02,0.3418869012187221E-02, \
    0.1030951784492058E-01,0.1030951784492058E-01, \
    0.1030951784492058E-01,0.1030951784492058E-01, \
    0.7362609227691093E-02,0.7362609227691093E-02, \
    0.7362609227691093E-02,0.7362609227691093E-02, \
    0.1132084139272881E-01,0.1132084139272881E-01, \
    0.1132084139272881E-01,0.1132084139272881E-01, \
    0.1579946795763282E-01,0.1579946795763282E-01, \
    0.1579946795763282E-01,0.1579946795763282E-01, \
    0.1762701971434555E-01,0.1762701971434555E-01, \
    0.1762701971434555E-01,0.1762701971434555E-01, \
    0.1445134560321702E-01,0.1445134560321702E-01, \
    0.1445134560321702E-01,0.1445134560321702E-01, \
    0.4104428749850738E-01,0.4104428749850738E-01, \
    0.4104428749850738E-01,0.4104428749850738E-01, \
    0.3339495242559154E-01,0.3339495242559154E-01, \
    0.3339495242559154E-01,0.3339495242559154E-01, \
    0.4184373496097664E-01,0.4184373496097664E-01, \
    0.4184373496097664E-01,0.4184373496097664E-01, \
    0.2495764669470555E-01,0.2495764669470555E-01, \
    0.2495764669470555E-01,0.2495764669470555E-01, \
    0.3707130727927116E-01,0.3707130727927116E-01, \
    0.3707130727927116E-01,0.3707130727927116E-01, \
    0.9609787849027714E-02,0.9609787849027714E-02, \
    0.9609787849027714E-02,0.9609787849027714E-02, \
    0.3355691943165765E-01,0.3355691943165765E-01, \
    0.3355691943165765E-01,0.3355691943165765E-01, \
    0.8580982368089280E-02,0.8580982368089280E-02, \
    0.8580982368089280E-02,0.8580982368089280E-02, \
    0.1755951049274731E-01,0.1755951049274731E-01, \
    0.1755951049274731E-01,0.1755951049274731E-01, \
    0.4298498004935582E-01,0.4298498004935582E-01, \
    0.4298498004935582E-01,0.4298498004935582E-01, \
    0.2200937149220828E-01,0.2200937149220828E-01, \
    0.2200937149220828E-01,0.2200937149220828E-01, \
    0.1430848314758049E-01,0.1430848314758049E-01, \
    0.1430848314758049E-01,0.1430848314758049E-01, \
    0.1667506010717100E-01,0.1667506010717100E-01, \
    0.1667506010717100E-01,0.1667506010717100E-01, \
    0.3444495645764802E-01,0.3444495645764802E-01, \
    0.3444495645764802E-01,0.3444495645764802E-01, \
    0.2897820038333119E-01,0.2897820038333119E-01, \
    0.2897820038333119E-01,0.2897820038333119E-01, \
    0.3492622185053053E-01,0.3492622185053053E-01, \
    0.3492622185053053E-01,0.3492622185053053E-01, \
    0.4881429507850928E-01,0.4881429507850928E-01, \
    0.4881429507850928E-01,0.4881429507850928E-01, \
    0.2338133304387865E-01,0.2338133304387865E-01, \
    0.2338133304387865E-01,0.2338133304387865E-01, \
    0.4325777192033273E-01,0.4325777192033273E-01, \
    0.4325777192033273E-01,0.4325777192033273E-01 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def rule30 ( n ):

#*****************************************************************************80
#
## rule30() returns the rule of degree 30.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  xs = np.array ( [ \
    -0.2489884108477549,-0.8955668996881347, \
    -0.9323001501704753,0.7405445449992548, \
    -0.9340642229281805,-0.9095962664223526, \
    0.5608633663495270,0.8616511147917938, \
    0.1660321315312064,0.6574874238191415, \
    -0.1433381379425067,0.1329569336990351, \
    -0.8829748195890315,0.6632673829575200, \
    0.4936163200514849,-0.2027212042708638, \
    -0.9958809661720823,-0.3073287548883581, \
    -0.8217303027626981,0.8261783389660409, \
    -0.4397988250817157,0.5010528086431736, \
    0.5909729749119785,-0.3540551267912417, \
    -0.1341504650225714,0.8797782958287345, \
    0.7856276574168712,0.2511140307013671E-01, \
    0.6793669279007186,0.5990617334262452, \
    -0.6571411220532614E-01,0.2486338305340984, \
    0.2517441361617084,0.4956264496869945, \
    0.6407808309272243,0.3783356039497430, \
    0.4110110511714637,-0.8395840683102380, \
    -0.8086877648916926,0.1348481347528898, \
    0.7911211318084024E-01,0.1744159174802842, \
    0.3212567387892802E-01,-0.9336794010864112E-02, \
    0.7322797884447179,0.3357167967967313E-01, \
    0.5935826720491633,0.8968431432339444, \
    0.1799598313156058,0.7269821230572000, \
    -0.1856842034490502,0.6913593560408486, \
    -0.4397815672742683,-0.7758135419229234, \
    -0.9616538724444206,0.3193596929830660, \
    0.3777165903330749,-0.7679662364686681, \
    -0.7298701218806570,0.4065079920371972, \
    -0.9227465688784468E-01,-0.5950684639841661, \
    -0.9013518967720980,0.8836909793143869, \
    -0.9967771339953647,-0.9944392441466685, \
    -0.2195956599465894,-0.4351118739522196, \
    -0.4349934895265168,0.8129226389660974, \
    0.9133061964092235,-0.7096773902564911, \
    -0.7019587221008244E-01,0.3087832511180271, \
    -0.4541723274189980,0.1380191907138354, \
    0.9551957279557286,-0.7407772548705425, \
    -0.6078105587102869,-0.8435179784664049, \
    0.5490559994565902,0.2444037338918357, \
    0.2400810439649010,-0.5106820540745040E-01, \
    0.5284630091276127,0.8294520284860720, \
    0.9644131173686892,0.5513347774529967, \
    -0.7997415011464921,0.9063983320825396E-01, \
    0.5014531965594803,-0.3847230717105717, \
    -0.2781131563704615,-0.9344492367354887, \
    -0.9030917852729532,-0.4172241922741589E-01, \
    -0.2640772153341865,0.9665539194330073, \
    -0.2367623099741220,-0.8626350293444497, \
    -0.5924624188363723,-0.2560781746707642, \
    -0.9697346473592514,-0.5129714977732606, \
    0.9006954577534996,0.4485570029784398, \
    -0.9929762013100525,-0.4556636018911340, \
    -0.6294980126555781,-0.3125079163601901, \
    -0.7343713176297997,-0.6080741370996756, \
    0.7969083548584857,0.9691866547839980, \
    0.3151361183804022,0.3344055950815164, \
    0.9472309841785602,-0.1247403647674209, \
    -0.9779732163470612,-0.7256364179379601, \
    0.9970921358526692,-0.9954560187756241, \
    0.9951087682452733,-0.6883166208655062, \
    0.4290000273640588,-0.9880739319478465, \
    0.9072764372199305,0.9928546893888752, \
    -0.9917918025218534,-0.4805464361132344, \
    -0.8469642292616028,-0.8369560183233818, \
    -0.9779640479084950,0.9687313192733549, \
    -0.7547772532654357,0.7252641746474808, \
    0.6646022965583286,-0.5644091993909820, \
    0.8026432404348592,0.9543957566085060, \
    -0.3557861147500951,0.9951864328005721, \
    -0.9294765518337259,-0.9726603739446762, \
    0.9908893344007184,0.9593076671548199, \
    -0.9203911103942219,-0.5020036235062807, \
    0.8473616010099635,0.7880730531161636, \
    0.1506248287699496,0.9937769310041399, \
    0.9894968458978942,0.5755438442317007, \
    0.9058856705910572,0.9189816123793266, \
    0.6951883785315084,-0.6234868878005112, \
    -0.9575663408305919,-0.9618986262036308, \
    0.8232277101227666,0.9715176930569319, \
    -0.6414127133627360,-0.9547454138171275, \
    -0.9923199594879274,-0.8900231674458331, \
    0.9908836025186869 ] )
  ys = np.array ( [ \
    -0.2460485077113066,-0.4965476117162992, \
    -0.6487707118457230,0.3697665250429530, \
    -0.2243181000931358,-0.1272532317878749, \
    0.6675821699023886E-01,-0.3572065887354983, \
    -0.5859511801028319,0.2705477662356954, \
    -0.1384585540894461,-0.4984429846834076, \
    -0.6385136736297631,-0.9972347998858430, \
    0.9914800246598282,0.7647568592516673, \
    0.5617037705569573,0.7101121364821149, \
    -0.9361722473508081,0.4495309095930795, \
    0.9980930920696178,0.1901925696164289, \
    0.9914568702475882,-0.3600355152827119, \
    0.5732016635520147,-0.4984298059079483, \
    -0.2335476149195165,0.6688792604932079, \
    -0.5195288082893980E-01,-0.2801670391820981, \
    0.8352476010432909,-0.7081859480565704, \
    -0.8979072023199524,-0.4437687184357049, \
    -0.5837384948634179,0.3614240616611519, \
    -0.8230684981188165,0.3172654777326074E-01, \
    -0.9623528941703298,0.7321217620214555, \
    -0.8096610148202545,-0.1586165019412888, \
    0.2323785604104418E-01,-0.3309606689238450, \
    -0.4388893082509347,0.4126373875717694, \
    0.7615965342755699,0.2500590258181676, \
    0.2336722577585314,0.8396217552527814, \
    -0.5038771822936119,0.5974085228316085, \
    0.9608827453877556,0.9958546191278792, \
    -0.4499429575894099,0.5431833943398334E-01, \
    -0.5768346162092601,0.9424496317962137, \
    0.2149562696494443,-0.9626198942478345, \
    -0.9006091929700322,0.3935553572852833, \
    -0.9903441091784717,-0.9730346543555619E-01, \
    0.2076974492755955,-0.6015458100234288, \
    -0.7914402846211577,-0.9950700583024972, \
    0.5506915379662010,0.6946004094913842, \
    0.5611276703738952,-0.9902901583614324, \
    -0.9923523090719414,-0.3380059761467528, \
    0.2166811227803833,0.9084360793204729, \
    -0.6099079065118447,-0.1613429998348757, \
    0.2829088743783339E-01,-0.3475035436069812, \
    0.4843880673732963,-0.9945285505783277, \
    0.5463996157581324,0.9658858240647616, \
    -0.7106923954489180,0.9126926988703539, \
    0.9995360204936274,-0.9899747511065149, \
    -0.7645030064887491,-0.9580271636184000, \
    0.8948233603717312,-0.8974768652542269, \
    0.3866240780739671,0.7812537795763034, \
    -0.8567508357551102,-0.6608100052801699, \
    0.9104312794921889,0.3794498701460580, \
    0.9917517335327534,0.8711471531031385, \
    0.6865345494324926,-0.9676402895588128, \
    -0.7614862881147397,-0.7974426670548660, \
    0.8007048860105550,-0.1342520685119810, \
    -0.2726893919561137,0.8259904245622020, \
    -0.3535762642754187,0.2570082752527717E-01, \
    0.5408483080025682,0.9034516527900712, \
    0.1094396192245524,-0.9898880600690686, \
    0.8171118504095591,0.9624825870234074, \
    -0.3058427697709690,0.2042047511467314, \
    0.6881014856247000,0.8038659949683351, \
    -0.9483358470837810,-0.8774593970142823, \
    0.8159614789170281,-0.8758831247154076, \
    0.6649096212014286,-0.9861910838287823, \
    0.9701981255999362,-0.7285580220078556, \
    0.9697520026151714,-0.1654759673552738, \
    0.3730458721291450,0.6880375541948958, \
    -0.1463794215119850E-01,0.6931515112743655, \
    -0.5310794389210227,-0.9586758167636964, \
    0.9527988373282164,-0.9549818827769936, \
    -0.6636898088045536,0.4709151069275523E-01, \
    -0.6618488641031038,0.5367182637758624, \
    0.1898490002080080,0.3931950072226694, \
    0.9627353314786278,0.8959541550605267, \
    0.5524608659159009,-0.5236758593851664, \
    -0.9898656273130529,0.9909061133703810, \
    0.9951465511067116,0.1849675400643637, \
    -0.1455654267961535,-0.9037901015984503, \
    -0.7708757339972588,-0.9444760769791583, \
    -0.7980610860639374,0.9837596096190924, \
    -0.9414770920443709,0.9976903799315803, \
    -0.8814229711931103,-0.8637004475570209, \
    -0.6773031038124658,0.9224881482845090, \
    0.8455113672684367,0.9760969611534657, \
    -0.4540561623942587 ] )
  ws = np.array ( [ \
    0.1656982041847443E-01,0.6241957476859499E-02, \
    0.5216414751791839E-02,0.1560407651121931E-01, \
    0.9922352722380101E-02,0.1044885486074365E-01, \
    0.1879260280925844E-01,0.7828025997082013E-02, \
    0.6646815879562722E-02,0.2535391408286021E-01, \
    0.3596968831636211E-01,0.3381660954529117E-01, \
    0.1200214214883407E-01,0.1160844683478245E-02, \
    0.3455740863097736E-02,0.1153404181974989E-01, \
    0.2326794602666712E-02,0.2497552316469688E-01, \
    0.6829794315843321E-02,0.1834140231596609E-01, \
    0.1335225445575319E-02,0.2522798332446686E-01, \
    0.1595934032110033E-02,0.3325015027182070E-01, \
    0.3467011496498743E-01,0.1611839351364714E-01, \
    0.2222188812186740E-01,0.1902350040458492E-01, \
    0.2953427938744245E-01,0.2950256499869300E-01, \
    0.2375703035217899E-01,0.2641584105673240E-01, \
    0.1690793382324671E-01,0.2648926396425241E-01, \
    0.2312689012710705E-01,0.3659471133442508E-01, \
    0.2037361988036312E-01,0.2428599858933432E-01, \
    0.2744225331234096E-02,0.2314679166528731E-01, \
    0.2431857706237597E-01,0.3987956826883379E-01, \
    0.4134270745058791E-01,0.4048978066628536E-01, \
    0.2251078653857245E-01,0.4125065697406070E-01, \
    0.2175419992100145E-01,0.1864439716615348E-01, \
    0.3968876145073878E-01,0.1521710713143089E-01, \
    0.3736662827386808E-01,0.2360382881992710E-01, \
    0.9970157722257745E-02,0.1786030245435301E-02, \
    0.1077371157065800E-01,0.3789581847120879E-01, \
    0.2650233252873021E-01,0.8678377005773784E-02, \
    0.3088113765197352E-01,0.1042906365431807E-01, \
    0.1836452487305106E-01,0.3403335573613761E-01, \
    0.2495937103585967E-02,0.1987508148017507E-01, \
    0.3001373057974097E-02,0.3414083443427366E-02, \
    0.2598635525971543E-01,0.3548865418196895E-02, \
    0.3429487078025957E-01,0.1785504393755270E-01, \
    0.1456023929593576E-01,0.3984363472067331E-02, \
    0.4363711971919699E-02,0.3712059926790805E-01, \
    0.3986478887569449E-01,0.1913617153849744E-01, \
    0.1049511173281814E-01,0.3060958199220223E-01, \
    0.3647607908842043E-01,0.2174227606463140E-01, \
    0.3117137400117779E-01,0.3796109966676785E-02, \
    0.3772008807242438E-01,0.1190095135082278E-01, \
    0.2275866415131214E-01,0.9507317753716060E-02, \
    0.6602435439732473E-03,0.3562338138346624E-02, \
    0.1790794872114957E-01,0.1166720090620105E-01, \
    0.1835513327961018E-01,0.1782419810205321E-01, \
    0.4039879332467389E-01,0.8544698960003014E-02, \
    0.1019822565974266E-01,0.3318239678979050E-01, \
    0.1843639498443942E-01,0.1049436999441544E-01, \
    0.4401594721967702E-02,0.1035186584479928E-01, \
    0.2774663878371582E-01,0.1038891259079699E-01, \
    0.7200083574761216E-02,0.2284618397210542E-01, \
    0.1143761979472999E-01,0.3626034532564225E-01, \
    0.4552809166608951E-02,0.2292163519800657E-01, \
    0.3339012139070554E-01,0.4305115781657949E-01, \
    0.2689701371924873E-01,0.1397250038349306E-01, \
    0.2657597849484922E-01,0.1419885923832320E-02, \
    0.2482810620945660E-01,0.1189134969439302E-01, \
    0.1376786292971261E-01,0.4412810694947523E-01, \
    0.5396384182228113E-02,0.1824530377035380E-01, \
    0.1045375639904588E-02,0.1889471014408118E-02, \
    0.2161857112903824E-02,0.1668110451401195E-01, \
    0.3023692617299402E-01,0.9232726779228300E-03, \
    0.4418205190510442E-02,0.3242974435474479E-02, \
    0.1103547225797253E-02,0.3921202767387279E-01, \
    0.2351260224707112E-01,0.1749878242380525E-01, \
    0.9478556031843440E-02,0.7823816828409005E-02, \
    0.2512073023506692E-01,0.8748252477568070E-02, \
    0.1020629440191134E-01,0.1142386634483088E-01, \
    0.2036353481009834E-01,0.1287466988683176E-01, \
    0.3056687396551737E-01,0.3145655833062538E-02, \
    0.1700461827659660E-01,0.9197009770615088E-02, \
    0.1441218157540074E-02,0.5481672105012487E-02, \
    0.1455840676178983E-01,0.3167421637373095E-01, \
    0.3035466841344861E-02,0.3337345728148663E-02, \
    0.4142211764571325E-02,0.4237586226174837E-02, \
    0.5970530714448440E-02,0.1594194686963999E-01, \
    0.1264147552673667E-01,0.5857851156194439E-02, \
    0.1967714628271757E-01,0.5157040758112765E-02, \
    0.4236825269003221E-02,0.7120803451144430E-03, \
    0.1238091173770127E-01,0.5529561908151683E-02, \
    0.2467962146273505E-01,0.4839010235595776E-02, \
    0.2559138088025228E-02,0.4161994856862944E-02, \
    0.4970131407881912E-02 ] )

  x = np.zeros ( [ n, 2 ] )
  x[:,0] = xs[:]
  x[:,1] = ys[:]
  w = ws.copy ( )

  return x, w

def square_arbq ( degree, n ):

#*****************************************************************************80
#
## square_arbq() returns a quadrature rule for the symmetric square.
#
#  Discussion:
#
#    This procedure returns a quadrature rule for smooth functions
#    on the unit square [-1,1]^2.
#
#    All quadratures are accurate to 15 digits
#    All weights are positive and inside the square
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer DEGREE, the degree of the quadrature rule.
#    1 <= DEGREE <= 20.
#
#    integer N, the number of nodes.
#    This can be determined by a call to SQUARE_ARBQ_SIZE(DEGREE).
#
#  Output:
#
#    real x(n,2), the coordinates of the nodes.
#
#    real W(N), the weights.
#
  import numpy as np

  if ( degree == 1 ):
    x, w = rule01 ( n )
  elif ( degree == 2 ):
    x, w = rule02 ( n )
  elif ( degree == 3 ):
    x, w = rule03 ( n )
  elif ( degree == 4 ):
    x, w = rule04 ( n )
  elif ( degree == 5 ):
    x, w = rule05 ( n )
  elif ( degree == 6 ):
    x, w = rule06 ( n )
  elif ( degree == 7 ):
    x, w = rule07 ( n )
  elif ( degree == 8 ):
    x, w = rule08 ( n )
  elif ( degree == 9 ):
    x, w = rule09 ( n )
  elif ( degree == 10 ):
    x, w = rule10 ( n )
  elif ( degree == 11 ):
    x, w = rule11 ( n )
  elif ( degree == 12 ):
    x, w = rule12 ( n )
  elif ( degree == 13 ):
    x, w = rule13 ( n )
  elif ( degree == 14 ):
    x, w = rule14 ( n )
  elif ( degree == 15 ):
    x, w = rule15 ( n )
  elif ( degree == 16 ):
    x, w = rule16 ( n )
  elif ( degree == 17 ):
    x, w = rule17 ( n )
  elif ( degree == 18 ):
    x, w = rule18 ( n )
  elif ( degree == 19 ):
    x, w = rule19 ( n )
  elif ( degree == 20 ):
    x, w = rule20 ( n )
  elif ( degree == 21 ):
    x, w = rule21 ( n )
  elif ( degree == 22 ):
    x, w = rule22 ( n )
  elif ( degree == 23 ):
    x, w = rule23 ( n )
  elif ( degree == 24 ):
    x, w = rule24 ( n )
  elif ( degree == 25 ):
    x, w = rule25 ( n )
  elif ( degree == 26 ):
    x, w = rule26 ( n )
  elif ( degree == 27 ):
    x, w = rule27 ( n )
  elif ( degree == 28 ):
    x, w = rule28 ( n )
  elif ( degree == 29 ):
    x, w = rule29 ( n )
  elif ( degree == 30 ):
    x, w = rule30 ( n )
  else:
    print ( '' )
    print ( 'square_arbq(): Fatal error!' )
    print ( '  Illegal value of DEGREE.' )
    raise Exception ( 'square_arbq(): Fatal error!' )

  w_sum = np.sum ( w )

  w = 4.0 * w / w_sum

  return x, w

def square_arbq_size ( degree ):

#*****************************************************************************80
#
## square_arbq_size(): size of quadrature rule for the symmetric square.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer DEGREE, the desired degree of exactness.
#    1 <= DEGREE <= 30.
#
#  Output:
#
#    integer N, the number of points in the corresponding rule.
#
  import numpy as np

  n_save = np.array ( [ \
      1,   3,   4,   6,   7, \
     10,  12,  16,  17,  22, \
     24,  31,  33,  41,  44, \
     52,  55,  64,  68,  78, \
     82,  93,  98, 109, 115, \
    127, 132, 147, 152, 167 ] )

  if ( degree < 1 or 30 < degree ):
    print ( '' )
    print ( 'square_arbq_size(): Fatal error!' )
    print ( '  Illegal value of DEGREE.' )
    raise Exception ( 'square_arbq_size(): Fatal error!' )

  n = n_save [ degree - 1 ]

  return n

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
  square_arbq_rule_test ( )
  timestamp ( )

