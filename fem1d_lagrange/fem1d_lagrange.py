#! /usr/bin/env python3
#
def fem1d_lagrange_test ( ):

#*****************************************************************************80
#
## fem1d_lagrange_test() tests fem1d_lagrange().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'fem1d_lagrange_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test fem1d_lagrange().' )

  legendre_set_test ( )
  lagrange_value_test ( )
  lagrange_derivative_test ( )

  x_num = 11
  q_num = 15
  fem1d_lagrange_stiffness_test ( x_num, q_num )

  x_num = 21
  q_num = 15
  fem1d_lagrange_stiffness_test ( x_num, q_num )

#  Terminate.
#
  print ( '' )
  print ( 'fem1d_lagrange_test():' )
  print ( '  Normal end of execution.' )

  return

def fem1d_lagrange_stiffness ( x_num, x, q_num, f ):

#*****************************************************************************80
#
## fem1d_lagrange_stiffness() evaluates the Lagrange polynomial stiffness matrix.
#
#  Discussion:
#
#    The finite element method is to be applied over a given interval that
#    has been meshed with X_NUM points X.
#
#    The finite element basis functions are to be the X_NUM Lagrange
#    basis polynomials L(i)(X), such that
#      L(i)(X(j)) = delta(i,j).
#
#    The following items are computed:
#    * A, the stiffness matrix, with A(I,J) = integral L'(i)(x) L'(j)(x)
#    * M, the mass matrix, with M(I,J) = integral L(i)(x) L(j)(x)
#    * B, the load vector, with B(I) = integral L(i)(x) F(x)
#
#    The integrals are approximated by quadrature.
#
#    Boundary conditions are not handled by this routine.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X_NUM, the number of nodes.
#
#    real X(X_NUM,1), the coordinates of the nodes.
#
#    integer Q_NUM, the number of quadrature points to use.
#
#    function handle, real F(X), the right hand side function.
#
#  Output:
#
#    real A(X_NUM,X_NUM), the stiffness matrix.
#
#    real M(X_NUM,X_NUM), the mass matrix.
#
#    real B(X_NUM), the right hand side vector.
#
  import numpy as np
#
#  Get the quadrature rule for [-1,+1].
#
  q_x, q_w = legendre_set ( q_num )
#
#  Adjust the quadrature rule to the interval [ x(1), x(x_num) }
#
  q_x =  ( ( 1.0 - q_x ) * x[0] \
         + ( 1.0 + q_x ) * x[x_num-1] ) \
         /   2.0

  q_w = q_w * ( x[x_num-1] - x[0] ) / 2.0
#
#  Evaluate all the Lagrange basis polynomials at all the quadrature points.
#
  L = lagrange_value ( x_num, x, q_num, q_x )
#
#  Evaluate all the Lagrange basis polynomial derivatives at all the quadrature points.
#
  LP = lagrange_derivative ( x_num, x, q_num, q_x )
#
#  Assemble the matrix and right hand side.
#
  A = np.zeros ( [ x_num, x_num ] )
  M = np.zeros ( [ x_num, x_num ] )
  b = np.zeros ( x_num )

  for x_i in range ( 0, x_num ):
    for q_i in range ( 0, q_num ):
      li = L[q_i,x_i]
      lpi = LP[q_i,x_i]
      for x_j in range ( 0, x_num ):
        lj = L[q_i,x_j]
        lpj = LP[q_i,x_j]
        A[x_i,x_j] = A[x_i,x_j] + q_w[q_i] * lpi * lpj
        M[x_i,x_j] = M[x_i,x_j] + q_w[q_i] * li * lj

      b[x_i] = b[x_i] + q_w[q_i] * li * f ( q_x[q_i] )

  return A, M, b

def fem1d_lagrange_stiffness_test ( x_num, q_num ):

#*****************************************************************************80
#
## fem1d_lagrange_stiffness_test() tests fem1d_lagrange_stiffness().
#
#  Discussion:
#
#    The results are very sensitive to the quadrature rule.
#
#    In particular, if X_NUM points are used, the mass matrix will
#    involve integrals of polynomials of degree 2*(X_NUM-1), so the
#    quadrature rule should use at least Q_NUM = X_NUM - 1 points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X_NUM, the number of nodes.
#
#    integer Q_NUM, the number of quadrature points.
#
  import numpy as np

  print ( '' )
  print ( 'fem1d_lagrange_stiffness_test():' )
  print ( '  fem1d_lagrange_stiffness() computes the stiffness matrix,' )
  print ( '  the mass matrix, and right hand side vector for a' )
  print ( '  finite element problem using Lagrange interpolation' )
  print ( '  basis polynomials.' )
  print ( '' )
  print ( '  Solving:' )
  print ( '    -u"+u=x on 0 < x < 1' )
  print ( '    u(0) = u(1) = 0' )
  print ( '  Exact solution:' )
  print ( '    u(x) = x - sinh(x)/sinh(1)' )
  print ( '' )
  print ( '  The mesh used ', x_num, ' points.' )
  print ( '  Quadrature uses ', q_num, ' points.' )

  x_lo = 0.0
  x_hi = 1.0
  x = np.linspace ( x_lo, x_hi, x_num )

  [ A, M, b ] = fem1d_lagrange_stiffness ( x_num, x, q_num, f )

  K = A + M

  K[0,:] = 0.0
  K[0,0] = 1.0
  b[0] = 0.0

  K[x_num-1,:] = 0.0
  K[x_num-1,x_num-1] = 1.0
  b[x_num-1] = 0.0

  u = np.linalg.solve ( K, b )
  u_e = exact ( x )

  print ( '' )
  print ( '   I      X             U              U(exact)         Error' )
  print ( '' )

  for i in range ( 0, x_num ):
    print ( '  %2d  %8.4f  %14.6g  %14.6g  %14.6g' \
      % ( i, x[i], u[i], u_e[i], np.abs ( u[i] - u_e[i] ) ) )

  return

def f ( x ):

#*****************************************************************************80
#
## f() evaluates the right hand side.

  value = x

  return value

def exact ( x ):

#*****************************************************************************80
#
## exact() evaluates the exact solution.
#
  import numpy as np

  value = x - np.sinh ( x ) / np.sinh ( 1.0 )

  return value

def lagrange_derivative ( nd, xd, ni, xi ):

#*****************************************************************************80
#
## lagrange_derivative() evaluates the derivative of the Lagrange basis polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ND, the number of data points.
#
#    real XD(ND,1), the data nodes.
#
#    integer NI, the number of evaluation points.
#
#    real XI(NI,1), the evaluation points.
#
#  Output:
#
#    real LP(NI,ND), the value, at the I-th point XI, of the
#    Jth basis function.
#
  import numpy as np

  LP = np.zeros ( [ ni, nd ] )
  
  for i in range ( 0, ni ):
    for j in range ( 0, nd ):

      for j1 in range ( 0, nd ):

        if ( j1 != j ):
          p = 1.0
          for j2 in range ( 0, nd ):
            if ( j2 == j1 ):
              p = p / ( xd[j] - xd[j2] )
            elif ( j2 != j ):
              p = p * ( xi[i] - xd[j2] ) / ( xd[j] - xd[j2] )

          LP[i,j] = LP[i,j] + p

  return LP

def lagrange_derivative_test ( ):

#*****************************************************************************80
#
## lagrange_derivative_test() tests lagrange_derivative().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'lagrange_derivative_test():' )
  print ( '  lagrange_derivative() evaluates the Lagrange basis derivatives.' )

  nd = 5
  xlo = 0.0
  xhi = nd - 1 
  xd = np.linspace ( xlo, xhi, nd )

  print ( '' )
  print ( '  Lagrange basis points:' )
  pprint.pprint ( xd )
#
#  Evaluate the polynomials.
#
  print ( '' )
  print ( '   I      X          L1\'(X)      L2\'(X)      L3\'(X)      L4\'(X)      L5\'(X)' )
  print ( '' )
 
  ni = 2 * nd - 1
  xi = np.linspace ( xlo, xhi, ni )
  LI = lagrange_derivative ( nd, xd, ni, xi )

  for i in range ( 0, ni ):
 
    print ( '  %2d  %10f' % ( i, xi[i] ), end = '' )
    for j in range ( 0, nd ):
      print ( '  %10f' % ( LI[i,j] ), end = '' )
    print ( '' )

  return

def lagrange_value ( nd, xd, ni, xi ):

#*****************************************************************************80
#
## lagrange_value() evaluates the Lagrange basis polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ND, the number of data points.
#
#    real XD(ND,1), the data nodes.
#
#    integer NI, the number of evaluation points.
#
#    real XI(NI,1), the evaluation points.
#
#  Output:
#
#    real LI(NI,ND), the value, at the I-th point XI, of the
#    Jth basis function.
#
  import numpy as np

  LI = np.zeros ( [ ni, nd ] )
  
  for i in range ( 0, ni ):
    for j in range ( 0, nd ):
      LI[i,j] = np.prod ( ( xi[i] - xd[0:j]    ) / ( xd[j] - xd[0:j]  ) ) \
              * np.prod ( ( xi[i] - xd[j+1:nd] ) / ( xd[j] - xd[j+1:nd] ) )

  return LI

def lagrange_value_test ( ):

#*****************************************************************************80
#
## lagrange_value_test() tests lagrange_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'lagrange_value_test():' )
  print ( '  lagrange_value() evaluates the Lagrange basis polynomials.' )

  nd = 5
  xlo = 0.0
  xhi = nd - 1 
  xd = np.linspace ( xlo, xhi, nd )

  print ( '' )
  print ( '  Lagrange basis points:' )
  pprint.pprint ( xd )
#
#  Evaluate the polynomials.
#
  print ( '' )
  print ( '   I      X          L1(X)       L2(X)       L3(X)       L4(X)' )
  print ( '       L5(X)' )
  print ( '' )
 
  ni = 2 * nd - 1
  xi = np.linspace ( xlo, xhi, ni )
  LI = lagrange_value ( nd, xd, ni, xi )

  for i in range ( 0, ni ):
 
    print ( '  %2d  %10f' % ( i, xi[i] ), end = '' )
    for j in range ( 0, nd ):
      print ( '  %10f' % ( LI[i,j] ), end = '' )
    print ( '' )

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

  else:

    print ( '' )
    print ( 'legendre_set(): Fatal error!' )
    print ( '  Illegal value of N = ', n )
    print ( '  Legal values are 1 to 16.' )
    raise Exception ( 'legendre_set(): Fatal error!' )

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
#    16 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'legendre_set_test():' )
  print ( '  legendre_set() returns points and weights of ' )
  print ( '  Gauss-Legendre quadrature rules.' )
  print ( '' )
  print ( '   N               1             X^4           Runge' )
  print ( '' )

  for n in range ( 1, 11 ):
    x, w = legendre_set ( n )
    e1 = np.sum ( w )
    e2 = np.dot ( w, x**4 )
    e3 = np.dot ( w, ( 1.0 / ( 1.0 + 25.0 * x**2 ) ) )
    print ( '  %2d  %14.6g  %14.6g  %14.6g' % ( n, e1, e2, e3 ) )

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
  fem1d_lagrange_test ( )
  timestamp ( )

