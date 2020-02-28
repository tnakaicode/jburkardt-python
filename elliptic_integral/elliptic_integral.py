#! /usr/bin/env python3
#
def elliptic_integral_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_INTEGRAL_TEST tests ELLIPTIC_INTEGRAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 June 2018
#
#  Author:
#
#    John Burkardt.
#
  import platform

  from elliptic_ea import elliptic_ea_test
  from elliptic_ek import elliptic_ek_test
  from elliptic_em import elliptic_em_test

  from elliptic_fa import elliptic_fa_test
  from elliptic_fk import elliptic_fk_test
  from elliptic_fm import elliptic_fm_test

  from elliptic_pia import elliptic_pia_test
  from elliptic_pik import elliptic_pik_test
  from elliptic_pim import elliptic_pim_test

  from elliptic_inc_ea import elliptic_inc_ea_test
  from elliptic_inc_ek import elliptic_inc_ek_test
  from elliptic_inc_em import elliptic_inc_em_test

  from elliptic_inc_fa import elliptic_inc_fa_test
  from elliptic_inc_fk import elliptic_inc_fk_test
  from elliptic_inc_fm import elliptic_inc_fm_test

  from elliptic_inc_pia import elliptic_inc_pia_test
  from elliptic_inc_pik import elliptic_inc_pik_test
  from elliptic_inc_pim import elliptic_inc_pim_test

  from jacobi_cn import jacobi_cn_test
  from jacobi_dn import jacobi_dn_test
  from jacobi_sn import jacobi_sn_test

  from rc import rc_test
  from rc import rc_test2
  from rd import rd_test
  from rf import rf_test
  from rj import rj_test

  from sncndn import sncndn_test

  print ( '' )
  print ( 'ELLIPTIC_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPTIC_INTEGRAL evaluates some complete elliptic integrals.' )
#
#  Carlson elliptic integrals.
#
  rc_test ( )
  rc_test2 ( )
  rd_test ( )
  rf_test ( )
  rj_test ( )
#
#  Complete elliptic integrals of the first kind.
#
  elliptic_fa_test ( )
  elliptic_fk_test ( )
  elliptic_fm_test ( )
#
#  Complete elliptic integrals of the second kind.
#
  elliptic_ea_test ( )
  elliptic_ek_test ( )
  elliptic_em_test ( )
#
#  Complete elliptic integrals of the third kind.
#
  elliptic_pia_test ( )
  elliptic_pik_test ( )
  elliptic_pim_test ( )
#
#  Incomplete elliptic integrals of the first kind.
#
  elliptic_inc_fa_test ( )
  elliptic_inc_fk_test ( )
  elliptic_inc_fm_test ( )
#
#  Incomplete elliptic integrals of the second kind.
#
  elliptic_inc_ea_test ( )
  elliptic_inc_ek_test ( )
  elliptic_inc_em_test ( )
#
#  Incomplete elliptic integrals of the third kind.
#
  elliptic_inc_pia_test ( )
  elliptic_inc_pik_test ( )
  elliptic_inc_pim_test ( )
#
#  Jacobi elliptic functions.
#
  jacobi_cn_test ( )
  jacobi_dn_test ( )
  jacobi_sn_test ( )
  sncndn_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPTIC_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp 
  timestamp ( )
  elliptic_integral_test ( )
  timestamp ( )
