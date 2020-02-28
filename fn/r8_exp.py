#! /usr/bin/env python3
#
def r8_exp ( x ):

#*****************************************************************************80
#
## R8_EXP evaluates the exponential of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the exponential of X.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from machine import r8_mach
  from r8_pak import r8_pak
  from sys import exit

  aln216 = +0.83120654223414517758794896030274E-01

  expcs = np.array ( [ \
      +0.866569493314985712733404647266231E-01, \
      +0.938494869299839561896336579701203E-03, \
      +0.677603970998168264074353014653601E-05, \
      +0.366931200393805927801891250687610E-07, \
      +0.158959053617461844641928517821508E-09, \
      +0.573859878630206601252990815262106E-12, \
      +0.177574448591421511802306980226000E-14, \
      +0.480799166842372422675950244533333E-17, \
      +0.115716376881828572809260000000000E-19, \
      +0.250650610255497719932458666666666E-22, \
      +0.493571708140495828480000000000000E-25, \
      +0.890929572740634240000000000000000E-28, \
      +0.148448062907997866666666666666666E-30, \
      +0.229678916630186666666666666666666E-33 ] )

  twon16 = np.array ( [ \
      +0.0, \
      +0.44273782427413840321966478739929E-01, \
      +0.90507732665257659207010655760707E-01, \
      +0.13878863475669165370383028384151, \
      +0.18920711500272106671749997056047, \
      +0.24185781207348404859367746872659, \
      +0.29683955465100966593375411779245, \
      +0.35425554693689272829801474014070, \
      +0.41421356237309504880168872420969, \
      +0.47682614593949931138690748037404, \
      +0.54221082540794082361229186209073, \
      +0.61049033194925430817952066735740, \
      +0.68179283050742908606225095246642, \
      +0.75625216037329948311216061937531, \
      +0.83400808640934246348708318958828, \
      +0.91520656139714729387261127029583, \
      +1.0 ] )

  nterms = int ( r8_inits ( expcs, 14, 0.1 * r8_mach ( 3 ) ) )
  xmin = np.log ( r8_mach ( 1 ) ) + 0.01
  xmax = np.log ( r8_mach ( 2 ) ) - 0.001

  if ( x < xmin ):

    print ( '' )
    print ( 'R8_EXP - Warning!' )
    print ( '  X so small that exp(X) underflows.' )
    value = 0.0

  elif ( x <= xmax ):

    xint = int ( np.fix ( x ) )
 
    y = x - xint

    y = 23.0 * y + x * aln216

    n = int ( np.fix ( y ) )

    f = y - n

    n = int ( np.fix ( 23.0 * xint + n ) )

    n16 = int ( np.fix ( n / 16 ) )
    if ( n < 0 ):
      n16 = n16 - 1
    ndx = n - 16 * n16 + 1
    if ( 17 < ndx ):
      ndx = 17

    value = 1.0 + ( twon16[ndx-1] + f * ( 1.0 + twon16[ndx-1] ) \
      * r8_csevl ( f, expcs, nterms ) )

    value = r8_pak ( value, n16 )

  else:

    print ( '' )
    print ( 'R8_EXP - Fatal error!' )
    print ( '  X so large that exp(X) overflows.' )
    exit ( 'R8_EXP - Fatal error!' )

  return value

def r8_exp_test ( ):

#*****************************************************************************80
#
## R8_EXP_TEST tests R8_EXP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from exp_values import exp_values

  print ( '' )
  print ( 'R8_EXP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_EXP evaluates the exponential function.' )
  print ( '' )
  print ( '             X          EXP(X)  R8_EXP(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = exp_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_exp ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_EXP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_exp_test ( )
  timestamp ( )

