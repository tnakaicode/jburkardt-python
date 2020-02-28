#! /usr/bin/env python3
#
def row_echelon_integer_test ( ):

#*****************************************************************************80
#
## ROW_ECHELON_INTEGER_TEST tests the ROW_ECHELON_INTEGER library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  from i4_gcd                     import i4_gcd_test
  from i4mat_is_integer           import i4mat_is_integer_test
  from i4mat_print                import i4mat_print_test
  from i4mat_print_some           import i4mat_print_some_test
  from i4mat_ref                  import i4mat_ref_test
  from i4mat_row_swap             import i4mat_row_swap_test
  from i4mat_rref                 import i4mat_rref_test
  from i4mat_rref_solve_binary    import i4mat_rref_solve_binary_test
  from i4mat_rref_solve_binary_nz import i4mat_rref_solve_binary_nz_test
  from i4mat_rref_system          import i4mat_rref_system_test
  from i4mat_u_solve              import i4mat_u_solve_test
  from i4vec_binary_next          import i4vec_binary_next_test
  from i4vec_identity_row         import i4vec_identity_row_test
  from i4vec_is_binary            import i4vec_is_binary_test
  from i4vec_print                import i4vec_print_test
  from i4vec_red                  import i4vec_red_test
  from i4vec_transpose_print      import i4vec_transpose_print_test
  from ksub_next4                 import ksub_next4_test
  from r8vec_is_integer           import r8vec_is_integer_test
  from r8vec_print                import r8vec_print_test
  from r8vec_transpose_print      import r8vec_transpose_print_test

  print ( '' )
  print ( 'ROW_ECHELON_INTEGER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the ROW_ECHELON_INTEGER library.' )

  i4_gcd_test ( )

  i4mat_is_integer_test ( )
  i4mat_print_test ( )
  i4mat_print_some_test ( )
  i4mat_ref_test ( )
  i4mat_row_swap_test ( )
  i4mat_rref_test ( )
  i4mat_rref_solve_binary_test ( )
  i4mat_rref_solve_binary_nz_test ( )
  i4mat_rref_system_test ( )
  i4mat_u_solve_test ( )

  i4vec_binary_next_test ( )
  i4vec_identity_row_test ( )
  i4vec_is_binary_test ( )
  i4vec_print_test ( )
  i4vec_red_test ( )
  i4vec_transpose_print_test ( )

  ksub_next4_test ( )

  r8vec_is_integer_test ( )
  r8vec_print_test ( )
  r8vec_transpose_print_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ROW_ECHELON_INTEGER_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  row_echelon_integer_test ( )
  timestamp ( )

