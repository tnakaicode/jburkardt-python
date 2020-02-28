#! /usr/bin/env python3
#
def test_eigen_right ( ):

#*****************************************************************************80
#
## TEST_EIGEN_RIGHT tests right eigensystems.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  from a123                  import a123
  from a123                  import a123_eigen_right
  from a123                  import a123_eigenvalues
  from bab                   import bab
  from bab                   import bab_eigen_right
  from bab                   import bab_eigenvalues
  from bodewig               import bodewig
  from bodewig               import bodewig_eigen_right
  from bodewig               import bodewig_eigenvalues
  from carry                 import carry
  from carry                 import carry_eigen_right
  from carry                 import carry_eigenvalues
  from chow                  import chow
  from chow                  import chow_eigen_right
  from chow                  import chow_eigenvalues
  from combin                import combin
  from combin                import combin_eigen_right
  from combin                import combin_eigenvalues
  from dif2                  import dif2
  from dif2                  import dif2_eigen_right
  from dif2                  import dif2_eigenvalues
  from exchange              import exchange
  from exchange              import exchange_eigen_right
  from exchange              import exchange_eigenvalues
  from i4_uniform_ab         import i4_uniform_ab
  from idem_random           import idem_random
  from idem_random           import idem_random_eigen_right
  from idem_random           import idem_random_eigenvalues
  from identity              import identity
  from identity              import identity_eigen_right
  from identity              import identity_eigenvalues
  from ill3                  import ill3
  from ill3                  import ill3_eigen_right
  from ill3                  import ill3_eigenvalues
  from kershaw               import kershaw
  from kershaw               import kershaw_eigen_right
  from kershaw               import kershaw_eigenvalues
  from kms                   import kms
  from kms                   import kms_eigen_right
  from kms                   import kms_eigenvalues
  from line_adj              import line_adj
  from line_adj              import line_adj_eigen_right
  from line_adj              import line_adj_eigenvalues
  from line_loop_adj         import line_loop_adj
  from line_loop_adj         import line_loop_adj_eigen_right
  from line_loop_adj         import line_loop_adj_eigenvalues
  from one                   import one
  from one                   import one_eigen_right
  from one                   import one_eigenvalues
  from ortega                import ortega
  from ortega                import ortega_eigen_right
  from ortega                import ortega_eigenvalues
  from oto                   import oto
  from oto                   import oto_eigen_right
  from oto                   import oto_eigenvalues
  from pei                   import pei
  from pei                   import pei_eigen_right
  from pei                   import pei_eigenvalues
  from r8_uniform_ab         import r8_uniform_ab
  from r8mat_is_eigen_right  import r8mat_is_eigen_right
  from r8mat_norm_fro        import r8mat_norm_fro
  from r8vec_uniform_ab      import r8vec_uniform_ab
  from rodman                import rodman
  from rodman                import rodman_eigen_right
  from rodman                import rodman_eigenvalues
  from rosser1               import rosser1
  from rosser1               import rosser1_eigen_right
  from rosser1               import rosser1_eigenvalues
  from rutis1                import rutis1
  from rutis1                import rutis1_eigen_right
  from rutis1                import rutis1_eigenvalues
  from rutis2                import rutis2
  from rutis2                import rutis2_eigen_right
  from rutis2                import rutis2_eigenvalues
  from rutis5                import rutis5
  from rutis5                import rutis5_eigen_right
  from rutis5                import rutis5_eigenvalues
  from spd_random            import spd_random
  from spd_random            import spd_random_eigen_right
  from spd_random            import spd_random_eigenvalues
  from sylvester_kac         import sylvester_kac
  from sylvester_kac         import sylvester_kac_eigen_right
  from sylvester_kac         import sylvester_kac_eigenvalues
  from symm_random           import symm_random
  from symm_random           import symm_random_eigen_right
  from symm_random           import symm_random_eigenvalues
  from wilk12                import wilk12
  from wilk12                import wilk12_eigen_right
  from wilk12                import wilk12_eigenvalues
  from wilson                import wilson
  from wilson                import wilson_eigen_right
  from wilson                import wilson_eigenvalues
  from zero                  import zero
  from zero                  import zero_eigen_right
  from zero                  import zero_eigenvalues

  print ( '' )
  print ( 'TEST_EIGEN_RIGHT' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Compute the Frobenius norm of the right eigensystem error:' )
  print ( '    A * X - X * lambda' )
  print ( '  given K right eigenvectors X and eigenvalues lambda.' )
  print ( '' )
  print ( '  Title                    N     K      ||A||          ' ),
  print ( '||A*X-X*LAMBDA||' )
  print ( '' )
#
#  A123
#
  title = 'A123'
  n = 3
  k = 3
  a = a123 ( )
  lam = a123_eigenvalues ( )
  x = a123_eigen_right ( )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  BAB
#
  title = 'BAB'
  n = 5
  k = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = bab ( n, alpha, beta )
  lam = bab_eigenvalues ( n, alpha, beta )
  x = bab_eigen_right ( n, alpha, beta )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  BODEWIG
#
  title = 'BODEWIG'
  n = 4
  k = 4
  a = bodewig ( )
  lam = bodewig_eigenvalues ( )
  x = bodewig_eigen_right ( )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
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
  x = carry_eigen_right ( n, i1 )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
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
  x = chow_eigen_right ( alpha, beta, n )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  COMBIN
#
  title = 'COMBIN'
  n = 5
  k = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = combin ( alpha, beta, n )
  lam = combin_eigenvalues ( alpha, beta, n )
  x = combin_eigen_right ( alpha, beta, n )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  DIF2
#
  title = 'DIF2'
  n = 5
  k = 5
  a = dif2 ( n, n )
  lam = dif2_eigenvalues ( n )
  x = dif2_eigen_right ( n )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  EXCHANGE
#
  title = 'EXCHANGE'
  n = 5
  k = 5
  a = exchange ( n, n )
  lam = exchange_eigenvalues ( n )
  x = exchange_eigen_right ( n )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  IDEM_RANDOM
#
  title = 'IDEM_RANDOM'
  n = 5
  k = 5
  rank = 3
  key = 123456789
  a = idem_random ( n, rank, key )
  lam = idem_random_eigenvalues ( n, rank, key )
  x = idem_random_eigen_right ( n, rank, key )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  IDENTITY
#
  title = 'IDENTITY'
  n = 5
  k = 5
  a = identity ( n, n )
  lam = identity_eigenvalues ( n )
  x = identity_eigen_right ( n )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  ILL3
#
  title = 'ILL3'
  n = 3
  k = 3
  a = ill3 ( )
  lam = ill3_eigenvalues ( )
  x = ill3_eigen_right ( )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  KERSHAW
#
  title = 'KERSHAW'
  n = 4
  k = 4
  a = kershaw ( )
  lam = kershaw_eigenvalues ( )
  x = kershaw_eigen_right ( )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  KMS matrix
#  Eigenvalue information requires 0 <= ALPHA <= 1.
#
  title = 'KMS'
  n = 5
  k = 5
  r8_lo = +0.0
  r8_hi = +1.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = kms ( alpha, n, n )
  lam = kms_eigenvalues ( alpha, n )
  x = kms_eigen_right ( alpha, n )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  LINE_ADJ
#
  title = 'LINE_ADJ'
  n = 5
  k = 5
  a = line_adj ( n )
  lam = line_adj_eigenvalues ( n )
  x = line_adj_eigen_right ( n )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  LINE_LOOP_ADJ
#
  title = 'LINE_LOOP_ADJ'
  n = 5
  k = 5
  a = line_loop_adj ( n )
  lam = line_loop_adj_eigenvalues ( n )
  x = line_loop_adj_eigen_right ( n )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  ONE
#
  title = 'ONE'
  n = 5
  k = 5
  a = one ( n, n )
  lam = one_eigenvalues ( n )
  x = one_eigen_right ( n )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  ORTEGA
#
  title = 'ORTEGA'
  n = 5
  k = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  v1, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  v2, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  v3, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = ortega ( n, v1, v2, v3 )
  lam = ortega_eigenvalues ( n, v1, v2, v3 )
  x = ortega_eigen_right ( n, v1, v2, v3 )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  OTO
#
  title = 'OTO'
  n = 5
  k = 5
  a = oto ( n, n )
  lam = oto_eigenvalues ( n )
  x = oto_eigen_right ( n )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  PEI
#
  title = 'PEI'
  n = 5
  k = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = pei ( alpha, n )
  lam = pei_eigenvalues ( alpha, n )
  x = pei_eigen_right ( alpha, n )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  RODMAN
#
  title = 'RODMAN'
  n = 5
  k = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = rodman ( n, n, alpha )
  lam = rodman_eigenvalues ( n, alpha )
  x = rodman_eigen_right ( n, alpha )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
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
  x = rosser1_eigen_right ( )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  RUTIS1
#
  title = 'RUTIS1'
  n = 4
  k = 4
  a = rutis1 ( )
  lam = rutis1_eigenvalues ( )
  x = rutis1_eigen_right ( )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  RUTIS2
#
  title = 'RUTIS2'
  n = 4
  k = 4
  a = rutis2 ( )
  lam = rutis2_eigenvalues ( )
  x = rutis2_eigen_right ( )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  RUTIS5
#
  title = 'RUTIS5'
  n = 4
  k = 4
  a = rutis5 ( )
  lam = rutis5_eigenvalues ( )
  x = rutis5_eigen_right ( )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  spd_random
#
  title = 'spd_random'
  n = 5
  k = 5
  key = 123456789
  a = spd_random ( n, key )
  lam = spd_random_eigenvalues ( n, key )
  x = spd_random_eigen_right ( n, key )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  SYLVESTER_KAC
#
  title = 'SYLVESTER_KAC'
  n = 5
  k = 5
  a = sylvester_kac ( n )
  lam = sylvester_kac_eigenvalues ( n )
  x = sylvester_kac_eigen_right ( n )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
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
  x = symm_random_eigen_right ( n, d, key )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  WILK12
#
  title = 'WILK12'
  n = 12
  k = 12
  a = wilk12 ( )
  lam = wilk12_eigenvalues ( )
  x = wilk12_eigen_right ( )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  WILSON
#
  title = 'WILSON'
  n = 4
  k = 4
  a = wilson ( )
  lam = wilson_eigenvalues ( )
  x = wilson_eigen_right ( )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  ZERO
#
  title = 'ZERO'
  n = 5
  k = 5
  a = zero ( n, n )
  lam = zero_eigenvalues ( n )
  x = zero_eigen_right ( n )
  error_frobenius = r8mat_is_eigen_right ( n, k, a, x, lam )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print ( '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, n, k, norm_frobenius, error_frobenius ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TEST_EIGEN_RIGHT:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  test_eigen_right ( )
  timestamp ( )
