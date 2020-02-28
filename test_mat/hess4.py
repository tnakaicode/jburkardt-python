#! /usr/bin/env python
#
def hess4 ( ):

#*****************************************************************************80
#
## HESS4 returns the HESS4 matrix.
#
#  Example:
#
#    4+8i  7+6i  7+10i 7+10i
#    9+9i  8+1i  8+10i 2 +5i
#    0     8+3i  7+ 2i 7 +8i
#    0     0     4+10i 0 +1i
#
#  Properties:
#
#    A is integral.
#
#    A is not symmetric.
#
#    A is complex.
#
#    A is upper Hessenberg.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, complex A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ 4+8*1j,  7+6*1j,  7+10*1j, 7+10*1j ], \
    [ 9+9*1j,  8+1*1j,  8+10*1j, 2+ 5*1j ], \
    [ 0+0*1j,  8+3*1j,  7+ 2*1j, 7+ 8*1j ], \
    [ 0+0*1j,  0+0*1j,  4+10*1j, 0+ 1*1j ] ] )

  return a

def hess4_determinant ( ):

#*****************************************************************************80
#
## HESS4_DETERMINANT returns the determinant of the HESS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, complex VALUE, the determinant.
#
  value = 6.393999999999999e+03 - 4.548000000000000e+03*1j

  return value

def hess4_eigen_right ( ):

#*****************************************************************************80
#
## HESS4_EIGEN_RIGHT returns the right eigenvectors of the HESS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, complex A(4,4), the right eigenvector matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ -0.330070042547862-0.222298022567869*1j, \
      1.000000000000000+0.000000000000000*1j, \
      0.335490948571943-0.068002965084462*1j, \
      0.952157320531579+0.250709960744793*1j ], \
    [ 1.000000000000000+0.000000000000000*1j, \
      0.503205870426247-0.824241552742355*1j, \
     -0.768179408120474+0.010513990305666*1j, \
      1.000000000000000+0.000000000000000*1j ], \
    [ 0.257417722386482+0.309094498615456*1j, \
     -0.215016769732540+0.275479867860766*1j, \
      1.000000000000000+0.000000000000000*1j, \
      0.501508766439785-0.172182272014276*1j ], \
    [-0.842630039297297+0.197751498603984*1j, \
     -0.238196952722339+0.597205448629795*1j, \
     -0.972653465585451-0.104040336437224*1j, \
      0.218561824850003+0.044757232962382*1j ] ] )

  return a

def hess4_eigenvalues ( ):

#*****************************************************************************80
#
## HESS4_EIGENVALUES returns the eigenvalues of the HESS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, complex LAMBA(4), the eigenvalues.
#
  import numpy as np

  lamda = np.array ( [ \
        3.324431041502838- 2.742026572531628*1j, \
        0.568541187348097+ 6.826204344246118*1j, \
       -5.153228803481162- 8.729936381660266*1j, \
       20.260256574630240+16.645758609945791*1j ] )

  return lamda

def hess4_inverse ( ):

#*****************************************************************************80
#
## HESS4_INVERSE returns the pseudo-inverse of the HESS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, complex B(4,4), the matrix.
#
  import numpy as np

  b = np.array ( [ \
  [  0.055479592005787-0.046555961144460*1j, \
    0.008223391741817-0.036847046349424*1j, \
   -0.072930346088215+0.062294774161839*1j, \
   -0.165446110076836-0.054339835569198*1j ], \
  [ 0.098221887702513+0.072992359285429*1j, \
    0.151056059735374+0.029715821031667*1j, \
   -0.013605643493308-0.002639735159144*1j, \
    0.008483821182396+0.004783299771276*1j ], \
  [ 0.003980766488315+0.005177436032039*1j, \
    0.146615375569659-0.028025222381794*1j, \
   -0.103971410909060-0.013897712983173*1j, \
   -0.060517409011307-0.035851294367129*1j] , \
  [-0.048947708484049+0.045728154803651*1j, \
   -0.018713432435338+0.036423414026287*1j, \
    0.034460691461767-0.089345132191411*1j, \
    0.012773614147975+0.031294087761181*1j ] ] )

  return b

def hess4_test ( ):

#*****************************************************************************80
#
## HESS4_TEST tests HESS4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2018
#
#  Author:
#
#    John Burkardt
#
  import platform
  from c8mat_print import c8mat_print

  print ( '' )
  print ( 'HESS4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HESS4 computes the HESS4 matrix.' )

  m = 4
  n = 4
  a = hess4 ( )

  c8mat_print ( m, n, a, '  HESS4 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'HESS4_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hess4_test ( )
  timestamp ( )
