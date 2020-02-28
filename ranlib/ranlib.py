#! /usr/bin/env python3
#
def ranlib_test ( ):

#*****************************************************************************80
#
## RANLIB_TEST tests the RANLIB library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  from genbet                import genbet_test
  from genchi                import genchi_test
  from genexp                import genexp_test
  from genf                  import genf_test
  from gengam                import gengam_test
  from genmn                 import genmn_test
  from genmul                import genmul_test
  from gennch                import gennch_test
  from gennf                 import gennf_test
  from gennor                import gennor_test
  from genprm                import genprm_test
  from genunf                import genunf_test
  from ignbin                import ignbin_test
  from ignnbn                import ignnbn_test
  from ignpoi                import ignpoi_test
  from ignuin                import ignuin_test
  from initialize            import initialize
  from lennob                import lennob_test
  from low_level_test        import low_level_test
  from phrtsd                import phrtsd_test
  from prcomp                import prcomp_test
  from r4_exp                import r4_exp_test
  from r4_exponential_sample import r4_exponential_sample_test
  from r4vec_covariance      import r4vec_covariance_test
  from r8_exponential_sample import r8_exponential_sample_test
  from r8vec_covariance      import r8vec_covariance_test
  from setcov                import setcov_test
  from sexpo                 import sexpo_test
  from sgamma                import sgamma_test
  from snorm                 import snorm_test
  from spofa                 import spofa_test
  from stats                 import stats_test
  from trstat                import trstat_test

  phrase = 'Randomizer'

  initialize ( )

  print ( '' )
  print ( 'RANLIB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the RANLIB library.' )

  genbet_test ( phrase )
  genchi_test ( phrase )
  genexp_test ( phrase )
  genf_test ( phrase )
  gengam_test ( phrase )
  genmn_test ( phrase )
  genmul_test ( phrase )
  gennch_test ( phrase )
  gennf_test ( phrase )
  gennor_test ( phrase )
  genprm_test ( phrase )
  genunf_test ( phrase )
  ignbin_test ( phrase )
  ignnbn_test ( phrase )
  ignpoi_test ( phrase )
  ignuin_test ( phrase )
  lennob_test ( )
  low_level_test ( )
  phrtsd_test ( )
  prcomp_test ( )
  r4_exp_test ( )
  r4_exponential_sample_test ( )
  r4vec_covariance_test ( )
  r8_exponential_sample_test ( )
  r8vec_covariance_test ( )
  setcov_test ( )
  sexpo_test ( )
  sgamma_test ( )
  snorm_test ( )
  spofa_test ( )
  stats_test ( )
  trstat_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'RANLIB_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ranlib_test ( )
  timestamp ( )
