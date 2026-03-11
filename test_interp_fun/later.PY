function test_interp_fun_test04 ( )

#*****************************************************************************80
#
## test_interp_fun_test04() uses Bernstein polynomial approximation on functional problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  max_tab = 21

  print ( '' )
  print ( 'test_interp_fun_test04():' )
  print ( '  Bernstein polynomial approximation.' )
  print ( '  Evaluate the function at N equally spaced points.' )
  print ( '  Determine the N-1 degree Bernstein polynomial approximant.' )
  print ( '  Estimate the maximum difference between the function' )
  print ( '  and the approximant.' )

  prob_num = p00_prob_num ( )

  for prob = 1 : prob_num

    title = p00_title ( prob )
    [ a, b ] = p00_lim ( prob )

    print ( '' )
    print ( '  Problem #d', prob )
    print ( '  #s', title )
    print ( '' )
    print ( '     N   Max |Error|' )
    print ( '' )

    for n = 1 : 4 : max_tab
#
#  Evaluate the function at N equally spaced points.
#
      xdata = zeros ( n, 1 )
      ydata = zeros ( n, 1 )

      for i = 1 : n

        if ( n == 1 )
          xdata(i) = 0.5 * ( a + b )
        else
          xdata(i) = ( ( n - i     ) * a    ...
                     + (     i - 1 ) * b  ) ...
                     / ( n     - 1 )
        end

        ydata(i) = p00_fun ( prob, xdata(i) )

      end
#
#  Now examine the approximation error.
#
      error_max = 0.0
      imax = 100

      for i = 0 : imax

        if ( imax == 0 )
          xval = 0.5 * ( a + b )
        else
          xval = ( ( imax - i ) * a    ...
                 + (        i ) * b  ) ...
                 / ( imax     )
        end

        ytrue = p00_fun ( prob, xval )

        yval = bpab_approx ( n - 1, a, b, ydata, xval )

        error_max = max ( error_max, abs ( ytrue - yval ) )

      end

      print ( '  #4d  #14g', n, error_max )

    end

  end

  return
end
function test_interp_fun_test05 ( )

#*****************************************************************************80
#
## test_interp_fun_test05() uses linear spline interpolation on all problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  max_data = 21

  print ( '' )
  print ( 'test_interp_fun_test05():' )
  print ( '  Linear spline interpolation.' )

  prob_num = p00_prob_num ( )

  for prob = 1 : prob_num

    title = p00_title ( prob )
    [ a, b ] = p00_lim ( prob )

    print ( '' )
    print ( '  Problem #d', prob )
    print ( '  #s', title )
    print ( '' )
    print ( '     N   Max |Error|' )
    print ( '' )

    for ndata = 2 : 4 : max_data
#
#  Evaluate the function at NDATA equally spaced points.
#
      xdata = zeros ( ndata, 1 )
      ydata = zeros ( ndata, 1 )

      for i = 1 : ndata

        if ( ndata == 1 )
          xdata(i) = 0.5 * ( a + b )
        else
          xdata(i) = ( ( ndata - i     ) * a    ...
                     + (         i - 1 ) * b  ) ...
                     / ( ndata     - 1 )
        end

        ydata(i) = p00_fun ( prob, xdata(i) )

      end
#
#  Evaluate the interpolation function.
#
      error_max = 0.0
      imax = 100

      for i = 0 : imax

        if ( imax == 0 )
          xval = 0.5 * ( a + b )
        else
          xval = ( ( imax - i ) * a    ...
                 + (        i ) * b  ) ...
                 / ( imax     )
        end

        [ yval, ypval ] = spline_linear_val ( ndata, xdata, ydata, xval )

        ytrue = p00_fun ( prob, xval )

        error_max = max ( error_max, abs ( yval - ytrue ) )

      end

      print ( '  #4d  #14g', ndata, error_max )

    end

  end

  return
end
function test_interp_fun_test06 ( )

#*****************************************************************************80
#
## test_interp_fun_test06() uses Overhauser spline interpolation on all problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  num_dim = 1

  print ( '' )
  print ( 'test_interp_fun_test06():' )
  print ( '  Overhauser spline interpolation.' )

  prob_num = p00_prob_num ( )

  for prob = 1 : prob_num

    title = p00_title ( prob )
    [ a, b ] = p00_lim ( prob )

    ndim = 1
    ndata = 11

    xdata = zeros ( ndim, ndata )
    ydata = zeros ( ndim, ndata )

    for i = 1 : ndata
      xdata(1,i) = ( ( ndata - i     ) * a   ...
                   + (         i - 1 ) * b ) ...
                   / ( ndata     - 1 )
      ydata(1,i) = p00_fun ( prob, xdata(1,i) )
    end

    print ( '' )
    print ( '  Problem #d', prob )
    print ( '  #s', title )
    print ( '' )
    print ( '  X   Y' )
    print ( '' )
#
#  Evaluate the interpolation function.
#
    for i = 1 : ndata - 1

      jmax = 3

      if ( i == ndata - 1 )
        jhi = jmax
      else
        jhi = jmax - 1
      end

      for j = 1 : jhi

        xval = ( ( jmax - j     ) * xdata(1,i)     ...
               + (        j - 1 ) * xdata(1,i+1) ) ...
               / ( jmax     - 1 )

        yval = spline_overhauser_val ( num_dim, ndata, xdata, ydata, xval )

        if ( j == 1 | j == 3 )
          mark = '*'
        else
          mark = ' '
        end

        print ( '  #c  #14g  #14g', mark, xval, yval )

      end

    end

  end

  return
end
function test_interp_fun_test07 ( )

#*****************************************************************************80
#
## test_interp_fun_test07() uses cubic spline interpolation on all problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  ibcbeg = 0
  ibcend = 0
  ybcbeg = 0.0
  ybcend = 0.0

  print ( '' )
  print ( 'test_interp_fun_test07():' )
  print ( '  Cubic spline interpolation.' )

  prob_num = p00_prob_num ( )

  for prob = 1 : prob_num

    title = p00_title ( prob )
    [ a, b ] = p00_lim ( prob )

    ndata = 11
    xdata = zeros ( ndata, 1 )
    ydata = zeros ( ndata, 1 )

    for i = 1 : ndata
      xdata(i) = ( ( ndata - i     ) * a   ...
                 + (         i - 1 ) * b ) ...
                 / ( ndata     - 1 )
      ydata(i) = p00_fun ( prob, xdata(i) )
    end
#
#  Set up the interpolation function.
#
    ypp = spline_cubic_set ( ndata, xdata, ydata, ibcbeg, ybcbeg, ibcend, ...
      ybcend )

    print ( '' )
    print ( '  Problem #d', prob )
    print ( '  #s', title )
    print ( '' )
    print ( '    X   Y' )
    print ( '' )
#
#  Evaluate the interpolation function.
#
    for i = 1 : ndata - 1

      jmax = 3

      if ( i == ndata - 1 )
        jhi = jmax
      else
        jhi = jmax - 1
      end

      for j = 1 : jhi

        xval = ( ( jmax - j     ) * xdata(i)     ...
               + (        j - 1 ) * xdata(i+1) ) ...
               / ( jmax     - 1 )

        [ yval, ypval, yppval ] = spline_cubic_val ( ndata, xdata, ydata, ...
          ypp, xval )

        if ( j == 1 | j == 3 )
          mark = '*'
        else
          mark = ' '
        end

        print ( '  #c  #14g  #14g', mark, xval, yval )

      end

    end

  end

  return
end
function test_interp_fun_test08 ( )

#*****************************************************************************80
#
## test_interp_fun_test08() uses B spline approximation on all problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'test_interp_fun_test08():' )
  print ( '  B spline approximation.' )

  prob_num = p00_prob_num ( )

  for prob = 1 : prob_num

    title = p00_title ( prob )
    [ a, b ] = p00_lim ( prob )

    ndata = 11
    xdata = zeros ( ndata, 1 )
    ydata = zeros ( ndata, 1 )

    for i = 1 : ndata
      xdata(i) = ( ( ndata - i     ) * a   ...
                 + (         i - 1 ) * b ) ...
                 / ( ndata     - 1 )
      ydata(i) = p00_fun ( prob, xdata(i) )
    end

    print ( '' )
    print ( '  Problem #d', prob )
    print ( '  #s', title )
    print ( '' )
    print ( '       X        Y' )
    print ( '' )
#
#  Evaluate the interpolation function.
#
    for i = 1 : ndata - 1

      jmax = 3

      if ( i == ndata - 1 )
        jhi = jmax
      else
        jhi = jmax - 1
      end

      for j = 1 : jhi

        xval = ( ( jmax - j     ) * xdata(i)     ...
               + (        j - 1 ) * xdata(i+1) ) ...
               / ( jmax     - 1 )

        yval = spline_b_val ( ndata, xdata, ydata, xval )

        if ( j == 1 | j == 3 )
          mark = '*'
        else
          mark = ' '
        end

        print ( '  #c  #14g  #14g', mark, xval, yval )

      end

    end

  end

  return
