#! /usr/bin/env python
#
def i4vec_run_count ( n, a ):

#*****************************************************************************80
#
## I4VEC_RUN_COUNT counts runs of equal values in an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of integer values.
#
#    A run is a sequence of equal values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer A(N), the vector to be examined.
#
#    Output, integer RUN_COUNT, the number of runs.
#
  run_count = 0

  if ( n < 1 ):
    return run_count

  test = -1

  for i in range ( 0, n ):

    if ( i == 0 or a[i] != test ):
      run_count = run_count + 1
      test = a[i]

  return run_count

def i4vec_run_count_test ( ):

#*****************************************************************************80
#
## I4VEC_RUN_COUNT_TEST tests I4VEC_RUN_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_uniform_ab import i4vec_uniform_ab

  n = 20

  print ( '' )
  print ( 'I4VEC_RUN_COUNT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_RUN_COUNT counts runs in an I4VEC' )
  print ( '' )
  print ( ' Run Count        Sequence' )
  print ( '' )

  seed = 123456789

  for test in range ( 0, 10 ):

    a, seed = i4vec_uniform_ab ( n, 0, 1, seed )

    run_count = i4vec_run_count ( n, a )

    print ( '  %8d        ' % ( run_count ), end = '' )
    for i in range ( 0, n ):
      print ( '%2d' % ( a[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_RUN_COUNT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_run_count_test ( )
  timestamp ( )

