#! /usr/bin/env python3
#
def r8poly_test ( ):

#*****************************************************************************80
#
## R8POLY_TEST tests the R8POLY library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 November 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  from r8_sign                     import r8_sign_test

  from r82poly2_print              import r82poly2_print_test
  from r82poly2_type               import r82poly2_type_test

  from r8mat_inverse_3d            import r8mat_inverse_3d_test
  from r8mat_print                 import r8mat_print_test
  from r8mat_print_some            import r8mat_print_some_test

  from r8poly_add                  import r8poly_add_test
  from r8poly_ant_coef             import r8poly_ant_coef_test
  from r8poly_ant_value            import r8poly_ant_value_test
  from r8poly_degree               import r8poly_degree_test
  from r8poly_deriv                import r8poly_deriv_test
  from r8poly_division             import r8poly_division_test
  from r8poly_lagrange_0           import r8poly_lagrange_0_test
  from r8poly_lagrange_1           import r8poly_lagrange_1_test
  from r8poly_lagrange_2           import r8poly_lagrange_2_test
  from r8poly_lagrange_coef        import r8poly_lagrange_coef_test
  from r8poly_lagrange_factor      import r8poly_lagrange_factor_test
  from r8poly_lagrange_value       import r8poly_lagrange_value_test
  from r8poly_multiply             import r8poly_multiply_test
  from r8poly_power                import r8poly_power_test
  from r8poly_print                import r8poly_print_test
  from r8poly_shift                import r8poly_shift_test
  from r8poly_value                import r8poly_value_test
  from r8poly_value_horner         import r8poly_value_horner_test
  from r8poly_values_horner        import r8poly_values_horner_test

  from r8poly2_ex                  import r8poly2_ex_test
  from r8poly2_ex2                 import r8poly2_ex2_test
  from r8poly2_root                import r8poly2_root_test
  from r8poly2_rroot               import r8poly2_rroot_test
  from r8poly2_val                 import r8poly2_val_test
  from r8poly2_val2                import r8poly2_val2_test

  from r8poly3_root                import r8poly3_root_test

  from r8poly4_root                import r8poly4_root_test

  from r8vec_even                  import r8vec_even_test
  from r8vec_even_select           import r8vec_even_select_test
  from r8vec_indicator1            import r8vec_indicator1_test
  from r8vec_is_distinct           import r8vec_is_distinct_test
  from r8vec_is_zero               import r8vec_is_zero_test
  from r8vec_linspace              import r8vec_linspace_test
  from r8vec_print                 import r8vec_print_test
  from r8vec_transpose_print       import r8vec_transpose_print_test
  from r8vec_uniform_01            import r8vec_uniform_01_test

  from r8vec2_print                import r8vec2_print_test

  from roots_to_r8poly             import roots_to_r8poly_test

  from timestamp                   import timestamp_test

  print ( '' )
  print ( 'R8POLY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the R8POLY library.' )

  r8_sign_test ( )

  r82poly2_print_test ( )
  r82poly2_type_test ( )

  r8mat_inverse_3d_test ( );
  r8mat_print_test ( )
  r8mat_print_some_test ( )

  r8poly_add_test ( )
  r8poly_ant_coef_test ( )
  r8poly_ant_value_test ( )
  r8poly_degree_test ( )
  r8poly_deriv_test ( )
  r8poly_division_test ( )
  r8poly_lagrange_0_test ( )
  r8poly_lagrange_1_test ( )
  r8poly_lagrange_2_test ( )
  r8poly_lagrange_coef_test ( )
  r8poly_lagrange_factor_test ( )
  r8poly_lagrange_value_test ( )
  r8poly_multiply_test ( )
  r8poly_power_test ( )
  r8poly_print_test ( )
  r8poly_shift_test ( )
  r8poly_value_test ( )
  r8poly_value_horner_test ( )
  r8poly_values_horner_test ( )

  r8poly2_ex_test ( );
  r8poly2_ex2_test ( );
  r8poly2_root_test ( )
  r8poly2_rroot_test ( )
  r8poly2_val_test ( )
  r8poly2_val2_test ( )

  r8poly3_root_test ( )

  r8poly4_root_test ( )

  r8vec_even_test ( )
  r8vec_even_select_test ( )
  r8vec_indicator1_test ( )
  r8vec_is_distinct_test ( )
  r8vec_is_zero_test ( )
  r8vec_linspace_test ( )
  r8vec_print_test ( )
  r8vec_transpose_print_test ( )
  r8vec_uniform_01_test ( )

  r8vec2_print_test ( )

  roots_to_r8poly_test ( )

  timestamp_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp  import timestamp
  timestamp ( )
  r8poly_test ( )
  timestamp ( )
 
