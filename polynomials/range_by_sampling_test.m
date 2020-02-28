function range_by_sampling_test ( )

%*****************************************************************************80
%
%% RANGE_BY_SAMPLING_TEST uses sampling to estimate the range.
%
%  Discussion:
%
%    An R8MAT is an array of R8's.
%
%  Licensing:
%
%    This code is distributed under the GNU LGPL license. 
%
%  Modified:
%
%    26 January 2016
%
%  Author:
%
%    John Burkardt
%
  fprintf ( 1, '\n' );
  fprintf ( 1, 'RANGE_BY_SAMPLING_TEST:\n' );
  fprintf ( 1, '  Use N sample values of each polynomial over its domain to estimate\n' );
  fprintf ( 1, '  its minimum Pmin and maximum Pmax\n' );
  fprintf ( 1, '\n' );
  fprintf ( 1, '         N           Pmin             Pmax\n' );

  n = 50;

  for i = 1 : 28

    fprintf ( 1, '\n' );

    if ( i == 1 )
      m = butcher_m ( );
      [ l, u ] = butcher_b ( m );
      fprintf ( 1, '  butcher: [-1.4393333333, +0.219]\n' );
    elseif ( i == 2 )
      m = camel_m ( );
      [ l, u ] = camel_b ( m );
      fprintf ( 1, '  camel, pmin = -1.031628453489616:\n' );
    elseif ( i == 3 )
      m = camera_m ( );
      [ l, u ] = camera_b ( m );
      fprintf ( 1, '  camera: [-270397.4, +270202.6]\n' );
    elseif ( i == 4 )
      m = caprasse_m ( );
      [ l, u ] = caprasse_b ( m );
      fprintf ( 1, '  caprasse: [-3.1800966258, +4.4852773332]\n' );
    elseif ( i == 5 )
      m = cyclic5_m ( );
      [ l, u ] = cyclic5_b ( m );
      fprintf ( 1, '  cyclic5: [-30000, +50000]\n' );
    elseif ( i == 6 )
      m = cyclic7_m ( );
      [ l, u ] = cyclic7_b ( m );
      fprintf ( 1, '  cyclic7: [-5.0, +7.0]\n' );
    elseif ( i == 7 )
      m = cyclic8_m ( );
      [ l, u ] = cyclic8_b ( m );
      fprintf ( 1, '  cyclic8: [-8.0, +8.0]\n' );
    elseif ( i == 8 )
      m = goldstein_price_m ( );
      [ l, u ] = goldstein_price_b ( m );
      fprintf ( 1, '  goldstein_price: [ 3, ? ]:\n' );
    elseif ( i == 9 )
      m = hairer_m ( );
      [ l, u ] = hairer_b ( m );
      fprintf ( 1, '  hairer: [-18.75.25, -48.25]\n' );
    elseif ( i == 10 )
      m = heart_m ( );
      [ l, u ] = heart_b ( m );
      fprintf ( 1, '  heart: [-1.36775, +1.74345327935\n' );
    elseif ( i == 11 )
      m = himmelblau_m ( );
      [ l, u ] = himmelblau_b ( m );
      fprintf ( 1, '  himmelblau, [ 0, ? ]:\n' );
    elseif ( i == 12 )
      m = hunecke_m ( );
      [ l, u ] = hunecke_b ( m );
      fprintf ( 1, '  hunecke: [-1436.515078155, +161.120543283]\n' );
    elseif ( i == 13 )
      m = kearfott_m ( );
      [ l, u ] = kearfott_b ( m );
      fprintf ( 1, '  kearfott: [ 0, ? ]:\n' );
    elseif ( i == 14 )
      m = lv3_m ( );
      [ l, u ] = lv3_b ( m );
      fprintf ( 1, '  lv3: [-9.35, +14.8 ]\n' );
    elseif ( i == 15 )
      m = lv4_m ( );
      [ l, u ] = lv4_b ( m );
      fprintf ( 1, '  lv4: [-20.8, +22.8]\n' );
    elseif ( i == 16 )
      m = magnetism6_m ( );
      [ l, u ] = magnetism6_b ( m );
      fprintf ( 1, '  magnetism6: [-0.25, +280.0]\n' );
    elseif ( i == 17 )
      m = magnetism7_m ( );
      [ l, u ] = magnetism7_b ( m );
      fprintf ( 1, '  magnetism7: [-0.25, +330.0]\n' );
    elseif ( i == 18 )
      m = quadratic_m ( );
      [ l, u ] = quadratic_b ( m );
      fprintf ( 1, '  quadratic: [ -2, ? ]:\n' );
    elseif ( i == 19 )
      m = rd_m ( );
      [ l, u ] = rd_b ( m );
      fprintf ( 1, '  rd: [-36.71269068, +10.40560403]\n' );
    elseif ( i == 20 )
      m = reimer5_m ( );
      [ l, u ] = reimer5_b ( m );
      fprintf ( 1, '  reimer5: [-5.0, +5.0]\n' );
    elseif ( i == 21 )
      m = reimer6_m ( );
      [ l, u ] = reimer6_b ( m );
      fprintf ( 1, '  reimer6: [-937501, +937499]\n' );
    elseif ( i == 22 )
      m = rosenbrock_m ( );
      [ l, u ] = rosenbrock_b ( m );
      fprintf ( 1, '  rosenbrock: [ 0, ? ]::\n' );
    elseif ( i == 23 )
      m = schwefel_m ( );
      [ l, u ] = schwefel_b ( m );
      fprintf ( 1, '  schwefel: [ ?, ? ]:\n' );
    elseif ( i == 24 )
      m = smith1_m ( );
      [ l, u ] = smith1_b ( m );
      fprintf ( 1, '  smith1: [ ?, ? ]:\n' );
    elseif ( i == 25 )
      m = smith2_m ( );
      [ l, u ] = smith2_b ( m );
      fprintf ( 1, '  smith2: [ ?, ? ]:\n' );
    elseif ( i == 26 )
      m = virasoro_m ( );
      [ l, u ] = virasoro_b ( m );
      fprintf ( 1, '  virasoro: [-29.0, +21.0]\n' );
    elseif ( i == 27 )
      m = wright_m ( );
      [ l, u ] = wright_b ( m );
      fprintf ( 1, '  wright: [-30.25, 40.0 ]\n' );
    elseif ( i == 28 )
      m = zakharov_m ( );
      [ l, u ] = zakharov_b ( m );
      fprintf ( 1, '  zakharov: [ 0, ? ]:\n' );
    end

    seed = 123456789;

    n = 8;

    for n_log_2 = 4 : 20

      n = n * 2;
      x = r8mat_uniform_abvec ( m, n, u, l, seed );

      if ( i == 1 )
        f = butcher_f ( m, n, x );
      elseif ( i == 2 )
        f = camel_f ( m, n, x );
      elseif ( i == 3 )
        f = camera_f ( m, n, x );
      elseif ( i == 4 )
        f = caprasse_f ( m, n, x );
      elseif ( i == 5 )
        f = cyclic5_f ( m, n, x );
      elseif ( i == 6 )
        f = cyclic7_f ( m, n, x );
      elseif ( i == 7 )
        f = cyclic8_f ( m, n, x );
      elseif ( i == 8 )
        f = goldstein_price_f ( m, n, x );
      elseif ( i == 9 )
        f = hairer_f ( m, n, x );
      elseif ( i == 10 )
        f = heart_f ( m, n, x );
      elseif ( i == 11 )
        f = himmelblau_f ( m, n, x );
      elseif ( i == 12 )
        f = hunecke_f ( m, n, x );
      elseif ( i == 13 )
        f = kearfott_f ( m, n, x );
      elseif ( i == 14 )
        f = lv3_f ( m, n, x );
      elseif ( i == 15 )
        f = lv4_f ( m, n, x );
      elseif ( i == 16 )
        f = magnetism6_f ( m, n, x );
      elseif ( i == 17 )
        f = magnetism7_f ( m, n, x );
      elseif ( i == 18 )
        f = quadratic_f ( m, n, x );
      elseif ( i == 19 )
        f = rd_f ( m, n, x );
      elseif ( i == 20 )
        f = reimer5_f ( m, n, x );
      elseif ( i == 21 )
        f = reimer6_f ( m, n, x );
      elseif ( i == 22 )
        f = rosenbrock_f ( m, n, x );
      elseif ( i == 23 )
        f = schwefel_f ( m, n, x );
      elseif ( i == 24 )
        f = smith1_f ( m, n, x );
      elseif ( i == 25 )
        f = smith2_f ( m, n, x );
      elseif ( i == 26 )
        f = virasoro_f ( m, n, x );
      elseif ( i == 27 )
        f = wright_f ( m, n, x );
      elseif ( i == 28 )
        f = zakharov_f ( m, n, x );
      end

      fprintf ( 1, '  %8d  %16.8g  %16.8g\n', n, min ( f ), max ( f ) );

    end

  end

  return
end
