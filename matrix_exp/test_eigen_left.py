#! /usr/bin/env python3
#
def test_eigen_left ( ):

#*****************************************************************************80
#
## TEST_EIGEN_LEFT tests left eigensystems.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  from a123                  import a123
  from a123                  import a123_eigen_left
  from a123                  import a123_eigenvalues
  from carry                 import carry
  from carry                 import carry_eigen_left
  from carry                 import carry_eigenvalues
  from chow                  import chow
  from chow                  import chow_eigen_left
  from chow                  import chow_eigenvalues
  from diagonal              import diagonal
  from diagonal              import diagonal_eigen_left
  from diagonal              import diagonal_eigenvalues
  from i4_uniform_ab         import i4_uniform_ab
  from r8_uniform_ab         import r8_uniform_ab
  from r8mat_is_eigen_left   import r8mat_is_eigen_left
  from r8mat_norm_fro        import r8mat_norm_fro
  from r8mat_print           import r8mat_print
  from r8vec_print           import r8vec_print
  from r8vec_uniform_ab      import r8vec_uniform_ab
  from rosser1               import rosser1
  from rosser1               import rosser1_eigen_left
  from rosser1               import rosser1_eigenvalues
  from symm_random           import symm_random
  from symm_random           import symm_random_eigen_left
  from symm_random           import symm_random_eigenvalues

  print ( '' )
  print ( 'TEST_EIGEN_LEFT' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Compute the Frobenius norm of the left eigensystem error:' )
  print ( '    X * A - LAMBDA * X' )
  print ( '  given K left eigenvectors X and eigenvalues lambda.' )
  print ( '' )
  print ( '  Title                    N     K      ||A||          ' ),
  print ( '||X*A-LAMBDA*X||' )
  print ( '' )
#
#  A123
#
  title = 'A123'
  n = 3
  k = 3
  a = a123 ( )
  lam = a123_eigenvalues ( )
  x = a123_eigen_left ( )
  error_frobenius = r8mat_is_eigen_left ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  CARRY
#
  title = 'CARRY'
  n = 5
  k = 5
  i4_lo = 2
  i4_hi = 20
  seed = 123456789
  i1, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  a = carry ( n, i1 )
  lam = carry_eigenvalues ( n, i1 )
  x = carry_eigen_left ( n, i1 )
  error_frobenius = r8mat_is_eigen_left ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  CHOW
#
  title = 'CHOW'
  n = 5
  k = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = chow ( alpha, beta, n, n )
  lam = chow_eigenvalues ( alpha, beta, n )
  x = chow_eigen_left ( alpha, beta, n )
  error_frobenius = r8mat_is_eigen_left ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  DIAGONAL
#
  title = 'DIAGONAL'
  n = 5
  k = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  d, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = diagonal ( n, n, d )
  lam = diagonal_eigenvalues ( n, d )
  x = diagonal_eigen_left ( n, d )
  error_frobenius = r8mat_is_eigen_left ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  ROSSER1
#
  title = 'ROSSER1'
  n = 8
  k = 8
  a = rosser1 ( )
  lam = rosser1_eigenvalues ( )
  x = rosser1_eigen_left ( )
  error_frobenius = r8mat_is_eigen_left ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  SYMM_RANDOM
#
  title = 'SYMM_RANDOM'
  n = 5
  k = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  d, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  key = 123456789
  a = symm_random ( n, d, key )
  lam = symm_random_eigenvalues ( n, d, key )
  x = symm_random_eigen_left ( n, d, key )
  error_frobenius = r8mat_is_eigen_left ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TEST_EIGEN_LEFT:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  test_eigen_left ( )
  timestamp ( )
