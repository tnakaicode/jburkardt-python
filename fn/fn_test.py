#! /usr/bin/env python3
#
def fn_test ( ):

#*****************************************************************************80
#
## FN_TEST tests the FN library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 May 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  from airy_ai_values                   import airy_ai_values_test
  from airy_ai_prime_values             import airy_ai_prime_values_test
  from airy_bi_values                   import airy_bi_values_test
  from airy_bi_prime_values             import airy_bi_prime_values_test
  from arccos_values                    import arccos_values_test
  from arccosh_values                   import arccosh_values_test
  from arcsin_values                    import arcsin_values_test
  from arcsinh_values                   import arcsinh_values_test
  from arctan_values                    import arctan_values_test
  from arctan2_values                   import arctan2_values_test
  from arctanh_values                   import arctanh_values_test
  from bessel_i0_values                 import bessel_i0_values_test
  from bessel_i1_values                 import bessel_i1_values_test
  from bessel_j0_values                 import bessel_j0_values_test
  from bessel_j1_values                 import bessel_j1_values_test
  from bessel_k0_values                 import bessel_k0_values_test
  from bessel_k1_values                 import bessel_k1_values_test
  from bessel_kx_values                 import bessel_kx_values_test
  from bessel_y0_values                 import bessel_y0_values_test
  from bessel_y1_values                 import bessel_y1_values_test
  from beta_values                      import beta_values_test
  from beta_inc_values                  import beta_inc_values_test
  from beta_log_values                  import beta_log_values_test
  from binomial_values                  import binomial_values_test
  from cbrt_values                      import cbrt_values_test
  from chi_values                       import chi_values_test
  from ci_values                        import ci_values_test
  from cin_values                       import cin_values_test
  from cinh_values                      import cinh_values_test
  from cos_values                       import cos_values_test
  from cos_degree_values                import cos_degree_values_test
  from cosh_values                      import cosh_values_test
  from cot_values                       import cot_values_test
  from dawson_values                    import dawson_values_test
  from dilogarithm_values               import dilogarithm_values_test
  from e1_values                        import e1_values_test
  from ei_values                        import ei_values_test
  from erf_values                       import erf_values_test
  from erfc_values                      import erfc_values_test
  from exp_values                       import exp_values_test
  from gamma_values                     import gamma_values_test
  from gamma_inc_values                 import gamma_inc_values_test
  from gamma_inc_tricomi_values         import gamma_inc_tricomi_values_test
  from gamma_log_values                 import gamma_log_values_test
  from i4_uniform_ab                    import i4_uniform_ab_test
  from hypergeometric_u_values          import hypergeometric_u_values_test
  from int_values                       import int_values_test
  from log_values                       import log_values_test
  from log10_values                     import log10_values_test
  from logarithmic_integral_values      import logarithmic_integral_values_test
  from psi_values                       import psi_values_test
  from r8_factorial_values              import r8_factorial_values_test
  from r8_rise_values                   import r8_rise_values_test
  from shi_values                       import shi_values_test
  from si_values                        import si_values_test
  from sin_values                       import sin_values_test
  from sin_degree_values                import sin_degree_values_test
  from sinh_values                      import sinh_values_test
  from sqrt_values                      import sqrt_values_test
  from tan_values                       import tan_values_test
  from tanh_values                      import tanh_values_test

  from machine                          import i4_mach_test
  from machine                          import r8_mach_test

  from r8_acos                          import r8_acos_test
  from r8_acosh                         import r8_acosh_test
  from r8_aint                          import r8_aint_test
  from r8_airy                          import r8_ai_test
  from r8_airy                          import r8_aid_test
  from r8_airy                          import r8_bi_test
  from r8_airy                          import r8_bid_test
  from r8_asin                          import r8_asin_test
  from r8_asinh                         import r8_asinh_test
  from r8_atan                          import r8_atan_test
  from r8_atan2                         import r8_atan2_test
  from r8_atanh                         import r8_atanh_test
  from r8_besi0                         import r8_besi0_test
  from r8_besi0                         import r8_besk0_test
  from r8_besi1                         import r8_besi1_test
  from r8_besi1                         import r8_besk1_test
  from r8_besj0                         import r8_besj0_test
  from r8_besj1                         import r8_besj1_test
  from r8_besj0                         import r8_besy0_test
  from r8_besj1                         import r8_besy1_test
  from r8_besk                          import r8_besk_test
  from r8_beta                          import r8_beta_test
  from r8_betai                         import r8_betai_test
  from r8_binom                         import r8_binom_test
  from r8_cbrt                          import r8_cbrt_test
  from r8_chi                           import r8_chi_test
  from r8_chu                           import r8_chu_test
  from r8_ci                            import r8_ci_test
  from r8_ci                            import r8_cin_test
  from r8_ci                            import r8_si_test
  from r8_cinh                          import r8_cinh_test
  from r8_cos                           import r8_cos_test
  from r8_cos_deg                       import r8_cos_deg_test
  from r8_cosh                          import r8_cosh_test
  from r8_cot                           import r8_cot_test
  from r8_csevl                         import r8_csevl_test
  from r8_dawson                        import r8_dawson_test
  from r8_e1                            import r8_e1_test
  from r8_ei                            import r8_ei_test
  from r8_erf                           import r8_erf_test
  from r8_erf                           import r8_erfc_test
  from r8_exp                           import r8_exp_test
  from r8_fac                           import r8_fac_test
  from r8_gamic                         import r8_gamic_test
  from r8_gamit                         import r8_gamit_test
  from r8_gaml                          import r8_gaml_test
  from r8_gamma                         import r8_gamma_test
  from r8_gamr                          import r8_gamr_test
  from r8_inits                         import r8_inits_test
  from r8_int                           import r8_int_test
  from r8_lbeta                         import r8_lbeta_test
  from r8_lgams                         import r8_lgams_test
  from r8_lgmc                          import r8_lgmc_test
  from r8_li                            import r8_li_test
  from r8_lngam                         import r8_lngam_test
  from r8_lnrel                         import r8_lnrel_test
  from r8_log                           import r8_log_test
  from r8_log10                         import r8_log10_test
  from r8_mop                           import r8_mop_test
  from r8_pak                           import r8_pak_test
  from r8_pak                           import r8_upak_test
  from r8_poch                          import r8_poch_test
  from r8_psi                           import r8_psi_test
  from r8_rand                          import r8_rand_test
  from r8_randgs                        import r8_randgs_test
  from r8_random                        import r8_random_test
  from r8_ren                           import r8_ren_test
  from r8_shi                           import r8_shi_test
  from r8_sign                          import r8_sign_test
  from r8_sin                           import r8_sin_test
  from r8_sin_deg                       import r8_sin_deg_test
  from r8_sinh                          import r8_sinh_test
  from r8_spence                        import r8_spence_test
  from r8_sqrt                          import r8_sqrt_test
  from r8_tan                           import r8_tan_test
  from r8_tanh                          import r8_tanh_test

  print ( '' )
  print ( 'FN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the FN library.' )
#
#  Utilities.
#
  airy_ai_values_test ( )
  airy_ai_prime_values_test ( )
  airy_bi_values_test ( )
  airy_bi_prime_values_test ( )
  arccos_values_test ( )
  arccosh_values_test ( )
  arcsin_values_test ( )
  arcsinh_values_test ( )
  arctan_values_test ( )
  arctan2_values_test ( )
  arctanh_values_test ( )
  bessel_i0_values_test ( )
  bessel_i1_values_test ( )
  bessel_j0_values_test ( )
  bessel_j1_values_test ( )
  bessel_k0_values_test ( )
  bessel_k1_values_test ( )
  bessel_kx_values_test ( )
  bessel_y0_values_test ( )
  bessel_y1_values_test ( )
  beta_values_test ( )
  beta_inc_values_test ( )
  beta_log_values_test ( )
  binomial_values_test ( )
  cbrt_values_test ( )
  chi_values_test ( )
  ci_values_test ( )
  cin_values_test ( )
  cinh_values_test ( )
  cos_values_test ( )
  cos_degree_values_test ( )
  cosh_values_test ( )
  cot_values_test ( )
  dawson_values_test ( )
  dilogarithm_values_test ( )
  e1_values_test ( )
  ei_values_test ( )
  erf_values_test ( )
  erfc_values_test ( )
  exp_values_test ( )
  gamma_values_test ( )
  gamma_inc_values_test ( )
  gamma_inc_tricomi_values_test ( )
  gamma_log_values_test ( )
  hypergeometric_u_values_test ( )
  i4_uniform_ab_test ( )
  int_values_test ( )
  log_values_test ( )
  log10_values_test ( )
  logarithmic_integral_values_test ( )
  psi_values_test ( )
  r8_factorial_values_test ( )
  r8_rise_values_test ( )
  shi_values_test ( )
  si_values_test ( )
  sin_values_test ( )
  sin_degree_values_test ( )
  sinh_values_test ( )
  sqrt_values_test ( )
  tan_values_test ( )
  tanh_values_test ( )

  i4_mach_test ( )

  r8_acos_test ( )
  r8_acosh_test ( )
  r8_ai_test ( )
  r8_aid_test ( )
  r8_aint_test ( )
  r8_asin_test ( )
  r8_asinh_test ( )
  r8_atan_test ( )
  r8_atan2_test ( )
  r8_atanh_test ( )
  r8_besi0_test ( )
  r8_besi1_test ( )
  r8_besj0_test ( )
  r8_besj1_test ( )
  r8_besk0_test ( )
  r8_besk_test ( )
  r8_besk1_test ( )
  r8_besy0_test ( )
  r8_besy1_test ( )
  r8_beta_test ( )
  r8_betai_test ( )
  r8_bi_test ( )
  r8_bid_test ( )
  r8_binom_test ( )
  r8_cbrt_test ( )
  r8_chi_test ( )
  r8_chu_test ( )
  r8_ci_test ( )
  r8_cin_test ( )
  r8_cinh_test ( )
  r8_cos_test ( )
  r8_cos_deg_test ( )
  r8_cosh_test ( )
  r8_cot_test ( )
  r8_csevl_test ( )
  r8_dawson_test ( )
  r8_e1_test ( )
  r8_ei_test ( )
  r8_erf_test ( )
  r8_erfc_test ( )
  r8_exp_test ( )
  r8_fac_test ( )
  r8_gamic_test ( )
  r8_gamit_test ( )
  r8_gaml_test ( )
  r8_gamma_test ( )
  r8_gamr_test ( )
  r8_inits_test ( )
  r8_int_test ( )
  r8_lbeta_test ( )
  r8_lgams_test ( )
  r8_lgmc_test ( )
  r8_li_test ( )
  r8_lngam_test ( )
  r8_lnrel_test ( )
  r8_log_test ( )
  r8_log10_test ( )
  r8_mach_test ( )
  r8_mop_test ( )
  r8_pak_test ( )
  r8_poch_test ( )
  r8_psi_test ( )
  r8_rand_test ( )
  r8_randgs_test ( )
  r8_random_test ( )
  r8_ren_test ( )
  r8_shi_test ( )
  r8_si_test ( )
  r8_sign_test ( )
  r8_sin_test ( )
  r8_sin_deg_test ( )
  r8_sinh_test ( )
  r8_spence_test ( )
  r8_sqrt_test ( )
  r8_tan_test ( )
  r8_tanh_test ( )
  r8_upak_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'FN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fn_test ( )
  timestamp ( )
