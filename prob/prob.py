#! /usr/bin/env python3
#
def prob_test ( ):

#*****************************************************************************80
#
## PROB_TEST tests the PROB library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform
  from angle                 import angle_cdf_test
  from angle                 import angle_mean_test
  from angle                 import angle_pdf_test
  from anglit                import anglit_cdf_test
  from anglit                import anglit_sample_test
  from arcsin                import arcsin_cdf_test
  from arcsin                import arcsin_sample_test
  from benford               import benford_cdf_test
  from benford               import benford_pdf_test
  from bernoulli             import bernoulli_cdf_test
  from bernoulli             import bernoulli_sample_test
  from bessel_i0             import bessel_i0_test
  from bessel_i0_values      import bessel_i0_values_test
  from bessel_i1             import bessel_i1_test
  from bessel_i1_values      import bessel_i1_values_test
  from beta                  import beta_cdf_test
  from beta                  import beta_sample_test
  from beta_binomial         import beta_binomial_cdf_test
  from beta_binomial         import beta_binomial_sample_test
  from beta_cdf_values       import beta_cdf_values_test
  from beta_inc              import beta_inc_test
  from beta_inc_values       import beta_inc_values_test
  from beta_values           import beta_values_test
  from binomial              import binomial_cdf_test
  from binomial              import binomial_sample_test
  from birthday              import birthday_cdf_test
  from birthday              import birthday_sample_test
  from bradford              import bradford_cdf_test
  from bradford              import bradford_sample_test
  from buffon_box            import buffon_box_pdf_test
  from buffon_box            import buffon_box_sample_test
  from buffon                import buffon_pdf_test
  from buffon                import buffon_sample_test
  from burr                  import burr_cdf_test
  from burr                  import burr_sample_test
  from cardioid              import cardioid_cdf_test
  from cardioid              import cardioid_sample_test
  from cauchy                import cauchy_cdf_test
  from cauchy                import cauchy_sample_test
  from chebyshev1            import chebyshev1_cdf_test
  from chebyshev1            import chebyshev1_sample_test
  from chi                   import chi_cdf_test
  from chi                   import chi_sample_test
  from chi_square            import chi_square_cdf_test
  from chi_square            import chi_square_sample_test
  from chi_square_noncentral import chi_square_noncentral_sample_test
  from circular_normal       import circular_normal_sample_test
  from circular_normal_01    import circular_normal_01_sample_test
  from cosine                import cosine_cdf_test
  from cosine                import cosine_sample_test
  from coupon                import coupon_sample_test
  from coupon_complete       import coupon_complete_pdf_test
  from deranged              import deranged_cdf_test
  from deranged              import deranged_sample_test
  from digamma               import digamma_test
  from dipole                import dipole_cdf_test
  from dipole                import dipole_sample_test
  from dirichlet             import dirichlet_pdf_test
  from dirichlet             import dirichlet_sample_test
  from dirichlet_mix         import dirichlet_mix_pdf_test
  from dirichlet_mix         import dirichlet_mix_sample_test
  from discrete              import discrete_cdf_test
  from discrete              import discrete_sample_test
  from disk                  import disk_sample_test
  from empirical_discrete    import empirical_discrete_cdf_test
  from empirical_discrete    import empirical_discrete_sample_test
  from english_letter        import english_letter_cdf_test
  from english_sentence_length  import english_sentence_length_cdf_test
  from english_sentence_length  import english_sentence_length_sample_test
  from english_word_length   import english_word_length_cdf_test
  from english_word_length   import english_word_length_sample_test
  from erlang                import erlang_cdf_test
  from erlang                import erlang_sample_test
  from exponential_01        import exponential_01_cdf_test
  from exponential_01        import exponential_01_sample_test
  from exponential           import exponential_cdf_test
  from exponential           import exponential_sample_test
  from extreme_values        import extreme_values_cdf_test
  from extreme_values        import extreme_values_sample_test
  from f                     import f_cdf_test
  from f                     import f_sample_test
  from fermi_dirac           import fermi_dirac_sample_test
  from fisher                import fisher_pdf_test
  from fisk                  import fisk_cdf_test
  from fisk                  import fisk_sample_test
  from folded_normal         import folded_normal_cdf_test
  from folded_normal         import folded_normal_sample_test
  from frechet               import frechet_cdf_test
  from frechet               import frechet_sample_test
  from gamma                 import gamma_cdf_test
  from gamma                 import gamma_sample_test
  from gamma_inc_values      import gamma_inc_values_test
  from gamma_values          import gamma_values_test
  from genlogistic           import genlogistic_cdf_test
  from genlogistic           import genlogistic_sample_test
  from geometric             import geometric_cdf_test
  from geometric             import geometric_sample_test
  from gompertz              import gompertz_cdf_test
  from gompertz              import gompertz_sample_test
  from gumbel                import gumbel_cdf_test
  from gumbel                import gumbel_sample_test
  from half_normal           import half_normal_cdf_test
  from half_normal           import half_normal_sample_test
  from hypergeometric        import hypergeometric_cdf_test
  from hypergeometric        import hypergeometric_sample_test
  from i4_choose             import i4_choose_test
  from i4_choose_log         import i4_choose_log_test
  from i4_is_power_of_10     import i4_is_power_of_10_test
  from i4_uniform_ab         import i4_uniform_ab_test
  from i4mat_print           import i4mat_print_test
  from i4mat_print_some      import i4mat_print_some_test
  from i4row_max             import i4row_max_test
  from i4row_mean            import i4row_mean_test
  from i4row_min             import i4row_min_test
  from i4row_variance        import i4row_variance_test
  from i4vec_max             import i4vec_max_test
  from i4vec_mean            import i4vec_mean_test
  from i4vec_min             import i4vec_min_test
  from i4vec_print           import i4vec_print_test
  from i4vec_run_count       import i4vec_run_count_test
  from i4vec_sum             import i4vec_sum_test
  from i4vec_uniform_ab      import i4vec_uniform_ab_test
  from i4vec_unique_count    import i4vec_unique_count_test
  from i4vec_variance        import i4vec_variance_test
  from inverse_gaussian      import inverse_gaussian_cdf_test
  from inverse_gaussian      import inverse_gaussian_sample_test
  from laplace               import laplace_cdf_test
  from laplace               import laplace_sample_test
  from levy                  import levy_cdf_test
  from log_normal            import log_normal_cdf_test
  from log_normal            import log_normal_sample_test
  from log_series            import log_series_cdf_test
  from log_series            import log_series_sample_test
  from log_uniform           import log_uniform_cdf_test
  from log_uniform           import log_uniform_sample_test
  from logistic              import logistic_cdf_test
  from logistic              import logistic_sample_test
  from lorentz               import lorentz_cdf_test
  from lorentz               import lorentz_sample_test
  from maxwell               import maxwell_cdf_test
  from maxwell               import maxwell_sample_test
  from multinomial_coef      import multinomial_coef_test
  from multinomial           import multinomial_pdf_test
  from multinomial           import multinomial_sample_test
  from multinoulli           import multinoulli_pdf_test
  from nakagami              import nakagami_cdf_test
  from nakagami              import nakagami_sample_test
  from negative_binomial     import negative_binomial_cdf_test
  from negative_binomial     import negative_binomial_sample_test
  from normal_01             import normal_01_cdf_test
  from normal_01             import normal_01_sample_test
  from normal_01_cdf_values  import normal_01_cdf_values_test
  from normal                import normal_cdf_test
  from normal                import normal_sample_test
  from normal_truncated_ab   import normal_truncated_ab_cdf_test
  from normal_truncated_ab   import normal_truncated_ab_sample_test
  from normal_truncated_a    import normal_truncated_a_cdf_test
  from normal_truncated_a    import normal_truncated_a_sample_test
  from normal_truncated_b    import normal_truncated_b_cdf_test
  from normal_truncated_b    import normal_truncated_b_sample_test
  from owen_values           import owen_values_test
  from pareto                import pareto_cdf_test
  from pareto                import pareto_sample_test
  from pearson_05            import pearson_05_pdf_test
  from planck                import planck_pdf_test
  from planck                import planck_sample_test
  from poisson               import poisson_cdf_test
  from poisson               import poisson_sample_test
  from power                 import power_cdf_test
  from power                 import power_sample_test
  from psi_values            import psi_values_test
  from quasigeometric        import quasigeometric_cdf_test
  from quasigeometric        import quasigeometric_sample_test
  from r8_beta               import r8_beta_test
  from r8_csc                import r8_csc_test
  from r8_epsilon            import r8_epsilon_test
  from r8_erf                import r8_erf_test
  from r8_factorial          import r8_factorial_test
  from r8_factorial_values   import r8_factorial_values_test
  from r8_gamma              import r8_gamma_test
  from r8_gamma_inc          import r8_gamma_inc_test
  from r8_gamma_log          import r8_gamma_log_test
  from r8_gamma_log_int      import r8_gamma_log_int_test
  from r8_huge               import r8_huge_test
  from r8_uniform_01         import r8_uniform_01_test
  from r8_zeta               import r8_zeta_test
  from r8mat_print           import r8mat_print_test
  from r8mat_print_some      import r8mat_print_some_test
  from r8poly_print          import r8poly_print_test
  from r8poly_value_horner   import r8poly_value_horner_test
  from r8row_max             import r8row_max_test
  from r8row_mean            import r8row_mean_test
  from r8row_min             import r8row_min_test
  from r8row_variance        import r8row_variance_test
  from r8vec_dot_product     import r8vec_dot_product_test
  from r8vec_max             import r8vec_max_test
  from r8vec_mean            import r8vec_mean_test
  from r8vec_min             import r8vec_min_test
  from r8vec_norm            import r8vec_norm_test
  from r8vec_print           import r8vec_print_test
  from r8vec_sum             import r8vec_sum_test
  from r8vec_transpose_print import r8vec_transpose_print_test
  from r8vec_uniform_01      import r8vec_uniform_01_test
  from r8vec_uniform_ab      import r8vec_uniform_ab_test
  from r8vec_variance        import r8vec_variance_test
  from r8vec2_print          import r8vec2_print_test
  from rayleigh              import rayleigh_cdf_test
  from rayleigh              import rayleigh_sample_test
  from reciprocal            import reciprocal_cdf_test
  from reciprocal            import reciprocal_sample_test
  from sech                  import sech_cdf_test
  from sech                  import sech_sample_test
  from semicircular          import semicircular_cdf_test
  from semicircular          import semicircular_sample_test
  from sin_power_int         import sin_power_int_test
  from sin_power_int_values  import sin_power_int_values_test
  from stirling2             import stirling2_test
  from student               import student_cdf_test
  from student               import student_sample_test
  from student_noncentral    import student_noncentral_cdf_test
  from tfn                   import tfn_test
  from triangle              import triangle_cdf_test
  from triangle              import triangle_sample_test
  from triangular            import triangular_cdf_test
  from triangular            import triangular_sample_test
  from trigamma              import trigamma_test
  from trigamma_values       import trigamma_values_test
  from uniform               import uniform_cdf_test
  from uniform               import uniform_sample_test
  from uniform_01            import uniform_01_cdf_test
  from uniform_01            import uniform_01_sample_test
  from uniform_01_order      import uniform_01_order_sample_test
  from uniform_discrete      import uniform_discrete_cdf_test
  from uniform_discrete      import uniform_discrete_sample_test
  from uniform_nsphere       import uniform_nsphere_sample_test
  from von_mises             import von_mises_cdf_test
  from von_mises             import von_mises_sample_test
  from weibull               import weibull_cdf_test
  from weibull               import weibull_sample_test
  from weibull_discrete      import weibull_discrete_cdf_test
  from weibull_discrete      import weibull_discrete_sample_test
  from zipf                  import zipf_cdf_test
  from zipf                  import zipf_sample_test

  print ( '' )
  print ( 'PROB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the PROB library.' )

  angle_cdf_test ( )
  angle_mean_test ( )
  angle_pdf_test ( )
  anglit_cdf_test ( )
  anglit_sample_test ( )
  arcsin_cdf_test ( )
  arcsin_sample_test ( )
  benford_cdf_test ( )
  benford_pdf_test ( )
  bernoulli_cdf_test ( )
  bernoulli_sample_test ( )
  bessel_i0_test ( )
  bessel_i0_values_test ( )
  bessel_i1_test ( )
  bessel_i1_values_test ( )
  beta_binomial_cdf_test ( )
  beta_binomial_sample_test ( )
  beta_cdf_test ( )
  beta_cdf_values_test ( )
  beta_inc_test ( )
  beta_inc_values_test ( )
  beta_sample_test ( )
  beta_values_test ( )
  binomial_cdf_test ( )
  binomial_sample_test ( )
  birthday_cdf_test ( )
  birthday_sample_test ( )
  bradford_cdf_test ( )
  bradford_sample_test ( )
  buffon_box_pdf_test ( )
  buffon_box_sample_test ( )
  buffon_pdf_test ( )
  buffon_sample_test ( )
  burr_cdf_test ( )
  burr_sample_test ( )
  cardioid_cdf_test ( )
  cardioid_sample_test ( )
  cauchy_cdf_test ( )
  cauchy_sample_test ( )
  chebyshev1_cdf_test ( )
  chebyshev1_sample_test ( )
  chi_cdf_test ( )
  chi_sample_test ( )
  chi_square_cdf_test ( )
  chi_square_sample_test ( )
  chi_square_noncentral_sample_test ( )
  circular_normal_sample_test ( )
  circular_normal_01_sample_test ( )
  cosine_cdf_test ( )
  cosine_sample_test ( )
  coupon_sample_test ( )
  coupon_complete_pdf_test ( )
  deranged_cdf_test ( )
  deranged_sample_test ( )
  digamma_test ( )
  dipole_cdf_test ( )
  dipole_sample_test ( )
  dirichlet_pdf_test ( )
  dirichlet_sample_test ( )
  dirichlet_mix_pdf_test ( )
  dirichlet_mix_sample_test ( )
  discrete_cdf_test ( )
  discrete_sample_test ( )
  disk_sample_test ( )
  empirical_discrete_cdf_test ( )
  empirical_discrete_sample_test ( )
  english_letter_cdf_test ( )
  english_sentence_length_cdf_test ( )
  english_sentence_length_sample_test ( )
  english_word_length_cdf_test ( )
  english_word_length_sample_test ( )
  erlang_cdf_test ( )
  erlang_sample_test ( )
  exponential_cdf_test ( )
  exponential_sample_test ( )
  exponential_01_cdf_test ( )
  exponential_01_sample_test ( )
  extreme_values_cdf_test ( )
  extreme_values_sample_test ( )
  f_cdf_test ( )
  f_sample_test ( )
  fermi_dirac_sample_test ( )
  fisher_pdf_test ( )
  fisk_cdf_test ( )
  fisk_sample_test ( )
  folded_normal_cdf_test ( )
  folded_normal_sample_test ( )
  frechet_cdf_test ( )
  frechet_sample_test ( )
  gamma_cdf_test ( )
  gamma_sample_test ( )
  gamma_inc_values_test ( )
  gamma_values_test ( )
  geometric_cdf_test ( )
  geometric_sample_test ( )
  gompertz_cdf_test ( )
  gompertz_sample_test ( )
  gumbel_cdf_test ( )
  gumbel_sample_test ( )
  half_normal_cdf_test ( )
  half_normal_sample_test ( )
  hypergeometric_cdf_test ( )
  hypergeometric_sample_test ( )
  i4_choose_test ( )
  i4_choose_log_test ( )
  i4_is_power_of_10_test ( )
  i4_uniform_ab_test ( )
  i4mat_print_test ( )
  i4mat_print_some_test ( )
  i4row_max_test ( )
  i4row_mean_test ( )
  i4row_min_test ( )
  i4row_variance_test ( )
  i4vec_max_test ( )
  i4vec_mean_test ( )
  i4vec_min_test ( )
  i4vec_print_test ( )
  i4vec_run_count_test ( )
  i4vec_sum_test ( )
  i4vec_uniform_ab_test ( )
  i4vec_unique_count_test ( )
  i4vec_variance_test ( )
  inverse_gaussian_cdf_test ( )
  inverse_gaussian_sample_test ( )
  laplace_cdf_test ( )
  laplace_sample_test ( )
  levy_cdf_test ( )
  log_normal_cdf_test ( )
  log_normal_sample_test ( )
  log_series_cdf_test ( )
  log_series_sample_test ( )
  log_uniform_cdf_test ( )
  log_uniform_sample_test ( )
  logistic_cdf_test ( )
  logistic_sample_test ( )
  lorentz_cdf_test ( )
  lorentz_sample_test ( )
  maxwell_cdf_test ( )
  maxwell_sample_test ( )
  multinomial_coef_test ( )
  multinomial_pdf_test ( )
  multinomial_sample_test ( )
  multinoulli_pdf_test ( )
  nakagami_cdf_test ( )
  nakagami_sample_test ( )
  negative_binomial_cdf_test ( )
  negative_binomial_sample_test ( )
  normal_01_cdf_test ( )
  normal_01_cdf_values_test ( )
  normal_01_sample_test ( )
  normal_cdf_test ( )
  normal_sample_test ( )
  normal_truncated_ab_cdf_test ( )
  normal_truncated_ab_sample_test ( )
  normal_truncated_a_cdf_test ( )
  normal_truncated_a_sample_test ( )
  normal_truncated_b_cdf_test ( )
  normal_truncated_b_sample_test ( )
  owen_values_test ( )
  pareto_cdf_test ( )
  pareto_sample_test ( )
  pearson_05_pdf_test ( )
  planck_pdf_test ( )
  planck_sample_test ( )
  poisson_cdf_test ( )
  poisson_sample_test ( )
  power_cdf_test ( )
  power_sample_test ( )
  psi_values_test ( )
  quasigeometric_cdf_test ( )
  quasigeometric_sample_test ( )
  r8_beta_test ( )
  r8_csc_test ( )
  r8_epsilon_test ( )
  r8_erf_test ( )
  r8_factorial_test ( )
  r8_factorial_values_test ( )
  r8_gamma_test ( )
  r8_gamma_inc_test ( )
  r8_gamma_log_test ( )
  r8_gamma_log_int_test ( )
  r8_huge_test ( )
  r8_uniform_01_test ( )
  r8_zeta_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8poly_print_test ( )
  r8poly_value_horner_test ( )
  r8row_max_test ( )
  r8row_mean_test ( )
  r8row_min_test ( )
  r8row_variance_test ( )
  r8vec_dot_product_test ( )
  r8vec_max_test ( )
  r8vec_mean_test ( )
  r8vec_min_test ( )
  r8vec_norm_test ( )
  r8vec_print_test ( )
  r8vec_sum_test ( )
  r8vec_transpose_print_test ( )
  r8vec_uniform_01_test ( )
  r8vec_uniform_ab_test ( )
  r8vec_variance_test ( )
  r8vec2_print_test ( )
  rayleigh_cdf_test ( )
  rayleigh_sample_test ( )
  reciprocal_cdf_test ( )
  reciprocal_sample_test ( )
  sech_cdf_test ( )
  sech_sample_test ( )
  semicircular_cdf_test ( )
  semicircular_sample_test ( )
  sin_power_int_test ( )
  sin_power_int_values_test ( )
  stirling2_test ( )
  student_cdf_test ( )
  student_sample_test ( )
  student_noncentral_cdf_test ( )
  tfn_test ( )
  triangle_cdf_test ( )
  triangle_sample_test ( )
  triangular_cdf_test ( )
  triangular_sample_test ( )
  trigamma_test ( )
  trigamma_values_test ( )
  uniform_01_cdf_test ( )
  uniform_01_sample_test ( )
  uniform_01_order_sample_test ( )
  uniform_cdf_test ( )
  uniform_sample_test ( )
  uniform_discrete_cdf_test ( )
  uniform_discrete_sample_test ( )
  uniform_nsphere_sample_test ( )
  von_mises_cdf_test ( )
  von_mises_sample_test ( )
  weibull_cdf_test ( )
  weibull_sample_test ( )
  weibull_discrete_cdf_test ( )
  weibull_discrete_sample_test ( )
  zipf_cdf_test ( )
  zipf_sample_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'PROB_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  prob_test ( )
  timestamp ( )
 
