#! /usr/bin/env python3
#
def triangle_integrands_test ( ):

#*****************************************************************************80
#
## triangle_integrands_test() tests triangle_integrands().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'triangle_integrands_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test triangle_integrands().' )

  triangle_integrands_test01 ( )
  triangle_integrands_test02 ( )
  triangle_integrands_test03 ( )
  triangle_integrands_test04 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'triangle_integrands_test():' )
  print ( '  Normal end of execution.' )

  return

def get_prob_num ( ):

#*****************************************************************************80
#
## get_prob_num() returns the number of test integration problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer PROB_NUM, the number of problems.
#
  prob_num = 22

  return prob_num

def p00_fun ( problem, n, x, y ):

#*****************************************************************************80
#
## p00_fun() evaluates the integrand for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem number.
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  if ( problem == 1 ):
    f = p01_fun ( n, x, y )
  elif ( problem == 2 ):
    f = p02_fun ( n, x, y )
  elif ( problem == 3 ):
    f = p03_fun ( n, x, y )
  elif ( problem == 4 ):
    f = p04_fun ( n, x, y )
  elif ( problem == 5 ):
    f = p05_fun ( n, x, y )
  elif ( problem == 6 ):
    f = p06_fun ( n, x, y )
  elif ( problem == 7 ):
    f = p07_fun ( n, x, y )
  elif ( problem == 8 ):
    f = p08_fun ( n, x, y )
  elif ( problem == 9 ):
    f = p09_fun ( n, x, y )
  elif ( problem == 10 ):
    f = p10_fun ( n, x, y )
  elif ( problem == 11 ):
    f = p11_fun ( n, x, y )
  elif ( problem == 12 ):
    f = p12_fun ( n, x, y )
  elif ( problem == 13 ):
    f = p13_fun ( n, x, y )
  elif ( problem == 14 ):
    f = p14_fun ( n, x, y )
  elif ( problem == 15 ):
    f = p15_fun ( n, x, y )
  elif ( problem == 16 ):
    f = p16_fun ( n, x, y )
  elif ( problem == 17 ):
    f = p17_fun ( n, x, y )
  elif ( problem == 18 ):
    f = p18_fun ( n, x, y )
  elif ( problem == 19 ):
    f = p19_fun ( n, x, y )
  elif ( problem == 20 ):
    f = p20_fun ( n, x, y )
  elif ( problem == 21 ):
    f = p21_fun ( n, x, y )
  elif ( problem == 22 ):
    f = p22_fun ( n, x, y )
  else:
    print ( '' )
    print ( 'p00_fun(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )
    raise Exception ( 'p00_fun(): Fatal error!' )

  return f

def p00_monte_carlo ( problem, n ):

#*****************************************************************************80
#
## p00_monte_carlo() applies the Monte Carlo rule to integrate a function.
#
#  Discussion:
#
#    The function f(x,y) is to be integrated over a triangle T.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem index.
#
#    integer N, the number of sample points.
#
#  Output:
#
#    real RESULT, the approximate integral.
#
  import numpy as np

  t = p00_vertices ( problem )

  x, y = triangle_sample ( t, n )

  f = p00_fun ( problem, n, x, y )

  area = triangle_area ( t )

  result = area * np.sum ( f ) / n

  return result

def p00_singularity ( problem ):

#*****************************************************************************80
#
## p00_singularity() warns of common singularities for any problem.
#
#  Discussion:
#
#    This routine can be used to check whether the integrand function
#    for a given problem has singularities at the vertices or along
#    the edges of the triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem number.
#
#  Output:
#
#    integer SINGULARITY.
#    0, there are no vertex or edge singularities.
#    1, there are singularities at one or more vertices, but not on edges.
#    2, there are singularities on one or more edges, possibly 
#       including vertices.
#    3, there are singularities somewhere inside or on the triangle.
#
  if ( problem == 1 ):
    singularity = 0
  elif ( problem == 2 ):
    singularity = 0
  elif ( problem == 3 ):
    singularity = 0
  elif ( problem == 4 ):
    singularity = 0
  elif ( problem == 5 ):
    singularity = 0
  elif ( problem == 6 ):
    singularity = 0
  elif ( problem == 7 ):
    singularity = 0
  elif ( problem == 8 ):
    singularity = 0
  elif ( problem == 9 ):
    singularity = 0
  elif ( problem == 10 ):
    singularity = 2
  elif ( problem == 11 ):
    singularity = 1
  elif ( problem == 12 ):
    singularity = 2
  elif ( problem == 13 ):
    singularity = 2
  elif ( problem == 14 ):
    singularity = 2
  elif ( problem == 15 ):
    singularity = 2
  elif ( problem == 16 ):
    singularity = 2
  elif ( problem == 17 ):
    singularity = 3
  elif ( problem == 18 ):
    singularity = 1
  elif ( problem == 19 ):
    singularity = 0
  elif ( problem == 20 ):
    singularity = 0
  elif ( problem == 21 ):
    singularity = 1
  elif ( problem == 22 ):
    singularity = 1
  else:
    print ( '' )
    print ( 'p00_singularity(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )
    raise Exception ( 'p00_singularity(): Fatal error!' )

  return singularity

def p00_title ( problem ):

#*****************************************************************************80
#
## p00_title() returns the title for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem number.
#
#  Output:
#
#    string TITLE,the title.
#
  if ( problem == 1 ):
    title = p01_title ( )
  elif ( problem == 2 ):
    title = p02_title ( )
  elif ( problem == 3 ):
    title = p03_title ( )
  elif ( problem == 4 ):
    title = p04_title ( )
  elif ( problem == 5 ):
    title = p05_title ( )
  elif ( problem == 6 ):
    title = p06_title ( )
  elif ( problem == 7 ):
    title = p07_title ( )
  elif ( problem == 8 ):
    title = p08_title ( )
  elif ( problem == 9 ):
    title = p09_title ( )
  elif ( problem == 10 ):
    title = p10_title ( )
  elif ( problem == 11 ):
    title = p11_title ( )
  elif ( problem == 12 ):
    title = p12_title ( )
  elif ( problem == 13 ):
    title = p13_title ( )
  elif ( problem == 14 ):
    title = p14_title ( )
  elif ( problem == 15 ):
    title = p15_title ( )
  elif ( problem == 16 ):
    title = p16_title ( )
  elif ( problem == 17 ):
    title = p17_title ( )
  elif ( problem == 18 ):
    title = p18_title ( )
  elif ( problem == 19 ):
    title = p19_title ( )
  elif ( problem == 20 ):
    title = p20_title ( )
  elif ( problem == 21 ):
    title = p21_title ( )
  elif ( problem == 22 ):
    title = p22_title ( )
  else:
    print ( '' )
    print ( 'p00_title(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )
    raise Exception ( 'p00_title(): Fatal error!' )

  return title

def p00_vertex_sub ( problem, level, n, result ):

#*****************************************************************************80
#
## p00_vertex_sub() approximates an integral in a triangle by subdivision.
#
#  Discussion:
#
#    The function f(x,y) is to be integrated over a triangle T.
#
#    The first approximation averages the values at the vertices.
#
#    If a second approximation is requested, the routine subdivides each
#    existing triangle into 4, evaluates the function at the new vertices,
#    and returns an improved estimate.
#
#    The routine may be called repeatedly in this way, to get an improved
#    estimate of the integral.
#
#    Note that this routine will fail in the case that there
#    are singularities at the vertices or along the sides of the triangle.
#
#    Moreover, since the number of new vertices grows as a power of 4,
#    the use of an automatic array to store all the new vertices at one
#    time may fail when a memory limit is reached.
#
#    Finally, note that the rule has a very low order of convergence.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem index.
#
#    integer LEVEL, the level of subdivision.  The first call
#    should be with LEVEL = 0.  For successive refinement, the routine
#    may be called repeatedly.  Each time, the user should increase the
#    value of LEVEL by 1, and also input the value of RESULT that was
#    output on the previous call.
#
#    integer N, the number of function evaluations used.
#    If LEVEL = 0, the input value is ignored.  Otherwise, the input
#    value is assumed to be the output value from the previous call.
#
#    real RESULT, the approximate integral.
#    If LEVEL = 0, then the input value is ignored.  Otherwise, the
#    input value is assumed to be the result from the previous call,
#    at the previous level.  
#
#  Output:
#
#    integer N, the number of function evaluations used,
#    including function evaluations from previous levels.
#
#    real RESULT, the updated approximate integral, based on the input
#    value, adjusted by information determined at the new level.
#
  import numpy as np

  t = p00_vertices ( problem )
  area = triangle_area ( t )
#
#  Compute first level.
#
  if ( level == 0 ):
 
    n = 3

    f = p00_fun ( problem, n, t[:,0], t[:,1] )

    result = np.sum ( f ) * area / 3.0
#
#  Compute next level.
#
  else:

    if ( level == 1 ):
      n_new = 3
    else:
      n_new = ( 2**( level - 1 ) + 1 ) * 2**( level - 1 ) * 3

    order_max_1d = 2**level

    i_new = 0
    xsi = np.zeros ( 3 )
    x = np.zeros ( n_new )
    y = np.zeros ( n_new )

    for i in range ( 0, order_max_1d, 2 ):
      for j in range ( 0, order_max_1d - i, 2 ):
 
        xsi[0] = ( order_max_1d - i - 1 - j ) / ( order_max_1d )
        xsi[1] = (                i + 1     ) / ( order_max_1d )
        xsi[2] = (                        j ) / ( order_max_1d )

        x[i_new] = np.dot ( xsi, t[:,0] )
        y[i_new] = np.dot ( xsi, t[:,1] )

        i_new = i_new + 1

        xsi[0] = ( order_max_1d - i - j - 1 ) / ( order_max_1d )
        xsi[1] = (                i         ) / ( order_max_1d )
        xsi[2] = (                    j + 1 ) / ( order_max_1d )

        x[i_new] = np.dot ( xsi, t[:,0] )
        y[i_new] = np.dot ( xsi, t[:,1] )

        i_new = i_new + 1

        xsi[0] = ( order_max_1d - i - 1 - j - 1 ) / ( order_max_1d )
        xsi[1] = (                i + 1         ) / ( order_max_1d )
        xsi[2] = (                        j + 1 ) / ( order_max_1d )

        x[i_new] = np.dot ( xsi, t[:,0] )
        y[i_new] = np.dot ( xsi, t[:,1] )

        i_new = i_new + 1

    f = p00_fun ( problem, n_new, x, y )

    result_new = np.sum ( f ) * area / n_new

    result = ( 3.0 * result_new + result ) / 4.0

    n = n + n_new

  return result, n

def p00_vertices ( problem ):

#*****************************************************************************80
#
## p00_vertices() returns the vertices for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the problem number.
#
#  Output:
#
#    real T(3,2), the vertices.
#
  if ( problem == 1 ):
    t = p01_vertices ( )
  elif ( problem == 2 ):
    t = p02_vertices ( )
  elif ( problem == 3 ):
    t = p03_vertices ( )
  elif ( problem == 4 ):
    t = p04_vertices ( )
  elif ( problem == 5 ):
    t = p05_vertices ( )
  elif ( problem == 6 ):
    t = p06_vertices ( )
  elif ( problem == 7 ):
    t = p07_vertices ( )
  elif ( problem == 8 ):
    t = p08_vertices ( )
  elif ( problem == 9 ):
    t = p09_vertices ( )
  elif ( problem == 10 ):
    t = p10_vertices ( )
  elif ( problem == 11 ):
    t = p11_vertices ( )
  elif ( problem == 12 ):
    t = p12_vertices ( )
  elif ( problem == 13 ):
    t = p13_vertices ( )
  elif ( problem == 14 ):
    t = p14_vertices ( )
  elif ( problem == 15 ):
    t = p15_vertices ( )
  elif ( problem == 16 ):
    t = p16_vertices ( )
  elif ( problem == 17 ):
    t = p17_vertices ( )
  elif ( problem == 18 ):
    t = p18_vertices ( )
  elif ( problem == 19 ):
    t = p19_vertices ( )
  elif ( problem == 20 ):
    t = p20_vertices ( )
  elif ( problem == 21 ):
    t = p21_vertices ( )
  elif ( problem == 22 ):
    t = p22_vertices ( )
  else:
    print ( '' )
    print ( 'p00_vertices(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )
    raise Exception ( 'p00_vertices(): Fatal error!' )

  return t

def p00_wandzura05_sub ( problem, level ):

#*****************************************************************************80
#
## p00_wandzura05_sub() uses subdivision and a Wandzura rule.
#
#  Discussion:
#
#    The Wandzura rule is a seven point rule of polynomial exactness 5.
#
#    The function f(x,y) is to be integrated over a triangle T.
#
#    The triangle is subdivided by subdividing each side into LEVEL sections,
#    which produces LEVEL*LEVEL subtriangles.  The Wandzura rule is then
#    applied to each subtriangle, and the result is summed.
#
#    The abscissas of this Wandzura rule do not lie on the vertices
#    or sides of the reference triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wandzura, Hong Xiao,
#    Symmetric Quadrature Rules on a Triangle,
#    Computers and Mathematics with Applications,
#    Volume 45, pages 1829-1840, 2003.
#
#  Input:
#
#    integer PROBLEM, the problem index.
#
#    integer LEVEL, the level of subdivision.  This indicates the
#    number of equally spaced subedges into which each edge of the triangle
#    is to be divided.  This will result in a total of LEVEL*LEVEL subtriangles
#    being used.
#
#  Output:
#
#    real RESULT, the approximate integral.
#
#    integer N, the number of function evaluations used.
#
  import numpy as np

  order = 7

  w = np.array ( [ \
    0.22500000000000, \
    0.13239415278851, \
    0.13239415278851, \
    0.13239415278851, \
    0.12593918054483, \
    0.12593918054483, \
    0.12593918054483 ] )

  xy_ref = np.array ( [ \
    [  0.33333333333333, 0.33333333333333, 0.33333333333333 ], \
    [  0.05971587178977, 0.47014206410512, 0.47014206410512 ], \
    [  0.47014206410512, 0.05971587178977, 0.47014206410512 ], \
    [  0.47014206410512, 0.47014206410512, 0.05971587178977 ], \
    [  0.79742698535309, 0.10128650732346, 0.10128650732346 ], \
    [  0.10128650732346, 0.79742698535309, 0.10128650732346 ], \
    [  0.10128650732346, 0.10128650732346, 0.79742698535309 ] ] )

  result = 0.0

  tri_phys = p00_vertices ( problem )

  area = triangle_area ( tri_phys )

  more = False
  i1 = -1
  j1 = -1
  i2 = -1
  j2 = -1
  i3 = -1
  j3 = -1

  xsi = np.zeros ( [ 3, 3 ] )

  while ( True ):
#
#  Get the integer indices of the next reference subtriangle.
#
    more, i1, j1, i2, j2, i3, j3 = subtriangle_next ( level, \
      more, i1, j1, i2, j2, i3, j3 )
#
#  Get the barycentric coordinates of the vertices of the reference subtriangle.
#   
    xsi[0,0] = (         i1      ) / level
    xsi[1,0] = (              j1 ) / level
    xsi[2,0] = ( level - i1 - j1 ) / level

    xsi[0,1] = (         i2      ) / level
    xsi[1,1] = (              j2 ) / level
    xsi[2,1] = ( level - i2 - j2 ) / level

    xsi[0,2] = (         i3      ) / level
    xsi[1,2] = (              j3 ) / level
    xsi[2,2] = ( level - i3 - j3 ) / level
#
#  Map the reference subtriangle to the physical subtriangle.
#
    x_sub_phys = np.dot ( np.transpose ( xsi ), tri_phys[:,0] )
    y_sub_phys = np.dot ( np.transpose ( xsi ), tri_phys[:,1] )
#
#  Now map the integration abscissas to the physical subtriangle.
#
    x_phys = np.dot ( xy_ref, x_sub_phys )
    y_phys = np.dot ( xy_ref, y_sub_phys )
#
#  Evaluate the function.
#
    f = p00_fun ( problem, order, x_phys, y_phys )
#
#  Update the quadrature estimate.
#
    result = result + np.dot ( w, f )

    if ( not more ):
      break
#
#  Scale by area and number of subtriangles.
#
  n = level * level * order

  result = result * area / ( level * level )

  return result, n

def p01_fun ( n, x, y ):

#*****************************************************************************80
#
## p01_fun() evaluates the integrand for problem 1.
#
#  Integrand:
#
#    f(x,y) = 2
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = 2.0 * np.ones ( n )

  return f

def p01_title ( ):

#*****************************************************************************80
#
## p01_title() returns the title of problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = 2'

  return title

def p01_vertices ( ):

#*****************************************************************************80
#
## p01_vertices() returns the vertices for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p02_fun ( n, x, y ):

#*****************************************************************************80
#
## p02_fun() evaluates the integrand for problem 2.
#
#  Integrand:
#
#    f(x,y) = 6 * x
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  f = 6.0 * x

  return f

def p02_title ( ):

#*****************************************************************************80
#
## p02_title() returns the title of problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = 6 * x'

  return title

def p02_vertices ( ):

#*****************************************************************************80
#
## p02_vertices() returns the vertices for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p03_fun ( n, x, y ):

#*****************************************************************************80
#
## p03_fun() evaluates the integrand for problem 3.
#
#  Integrand:
#
#    f(x,y) = 6 * y
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  f = 6.0 * y

  return f

def p03_title ( ):

#*****************************************************************************80
#
## p03_title() returns the title of problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = 6 * y'

  return title

def p03_vertices ( ):

#*****************************************************************************80
#
## p03_vertices() returns the vertices for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p04_fun ( n, x, y ):

#*****************************************************************************80
#
## p04_fun() evaluates the integrand for problem 4.
#
#  Integrand:
#
#    f(x,y) = 12 * x^2
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  f = 12.0 * x**2

  return f

def p04_title ( ):

#*****************************************************************************80
#
## p04_title() returns the title of problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = 12 * x^2'

  return title

def p04_vertices ( ):

#*****************************************************************************80
#
## p04_vertices() returns the vertices for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p05_fun ( n, x, y ):

#*****************************************************************************80
#
## p05_fun() evaluates the integrand for problem 5.
#
#  Integrand:
#
#    f(x,y) = 24 * x * y
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  f = 24.0 * x * y

  return f

def p05_title ( ):

#*****************************************************************************80
#
## p05_title() returns the title of problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = 24 * x*y'

  return title

def p05_vertices ( ):

#*****************************************************************************80
#
## p05_vertices() returns the vertices for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p06_fun ( n, x, y ):

#*****************************************************************************80
#
## p06_fun() evaluates the integrand for problem 6.
#
#  Integrand:
#
#    f(x,y) = 12 * y^2
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  f = 12.0 * y**2

  return f

def p06_title ( ):

#*****************************************************************************80
#
## p06_title() returns the title of problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = 12 * y^2'

  return title

def p06_vertices ( ):

#*****************************************************************************80
#
## p06_vertices() returns the vertices for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p07_fun ( n, x, y ):

#*****************************************************************************80
#
## p07_fun() evaluates the integrand for problem 7.
#
#  Integrand:
#
#    f(x,y) = 20 * x^3
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  f = 20.0 * x**3

  return f

def p07_title ( ):

#*****************************************************************************80
#
## p07_title() returns the title of problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = 20 * x^3'

  return title

def p07_vertices ( ):

#*****************************************************************************80
#
## p07_vertices() returns the vertices for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p08_fun ( n, x, y ):

#*****************************************************************************80
#
## p08_fun() evaluates the integrand for problem 8.
#
#  Integrand:
#
#    f(x,y) = 30 * x^4
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  f = 30.0 * x**4

  return f

def p08_title ( ):

#*****************************************************************************80
#
## p08_title() returns the title of problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = 30 * x^4'

  return title

def p08_vertices ( ):

#*****************************************************************************80
#
## p08_vertices() returns the vertices for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p09_fun ( n, x, y ):

#*****************************************************************************80
#
## p09_fun() evaluates the integrand for problem 9.
#
#  Integrand:
#
#    f(x,y) = 42 * x^5
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  f = 42.0 * x**5

  return f

def p09_title ( ):

#*****************************************************************************80
#
## p09_title() returns the title of problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = 42 * x^5'

  return title

def p09_vertices ( ):

#*****************************************************************************80
#
## p09_vertices() returns the vertices for problem 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p10_fun ( n, x, y ):

#*****************************************************************************80
#
## p10_fun() evaluates the integrand for problem 10.
#
#  Discussion:
#
#    The integral has been transformed from the integral of G(X,Y)
#    over the unit reference triangle.
#
#  Integrand:
#
#    PA = 1
#    PB = 5
#    PC = 0
#    PD = 0
#    PG = 0.25
#    PH = -0.25
#    D = PB - PA
#    U(X) = ( X - PA ) / D
#    V1(X) = ( 1 - ( X - PA ) / D ) / ( ( PG - PC ) * X + PH - PD )
#    V(X,Y) = V1(X) * ( Y - PC * X - PD )
#
#    G(X,Y) = X^(-0.2)
#
#    f(x,y) = g ( u(x), v(x,y) ) * v1(x) / d
#
#  Vertices:
#
#    (1,0), (5,0), (5,1)
#
#  Integral:
#
#    0.6944444444444444
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Elise deDoncker, Ian Robinson,
#    Algorithm 612:
#    Integration over a Triangle Using Nonlinear Extrapolation,
#    ACM Transactions on Mathematical Software,
#    Volume 10, Number 1, March 1984, pages 17-22.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  pa = 1.0
  pb = 5.0
  pc = 0.0
  pd = 0.0
  pg = 0.25
  ph = -0.25
  power = -0.2

  d = pb - pa
  u = ( x - pa ) / d
  v1 = ( 1.0 - u ) / ( ( pg - pc ) * x + ph - pd )
  v = v1 * ( y - pc * x - pd )

  zero = np.where ( u <= 0.0 )

  if ( np.any ( u <= 0.0 ) ):
    print ( ' u[]', u[zero] )
    print ( ' v1[]', v1[zero] )

  f = ( 36.0 / 25.0 ) * u**power * v1 / d

  return f

def p10_title ( ):

#*****************************************************************************80
#
## p10_title() returns the title of problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = x^(-0.2) on ((1,0),(5,0),(5,1))'

  return title

def p10_vertices ( ):

#*****************************************************************************80
#
## p10_vertices() returns the vertices for problem 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 1.0, 0.0 ], \
    [ 5.0, 0.0 ], \
    [ 5.0, 1.0 ] ] )

  return t

def p11_fun ( n, x, y ):

#*****************************************************************************80
#
## p11_fun() evaluates the integrand for problem 11.
#
#  Discussion:
#
#    The integral has been transformed from the integral of G(X,Y)
#    over the unit reference triangle.
#
#  Integrand:
#
#    PA = 0
#    PB = 1
#    PC = 0
#    PD = 0
#    PG = -1.0
#    PH = 1.0
#    D = PB - PA
#    U(X) = ( X - PA ) / D
#    V1(X) = ( 1 - ( X - PA ) / D ) / ( ( PG - PC ) * X + PH - PD )
#    V(X,Y) = V1(X) * ( Y - PC * X - PD )
#
#    G(X,Y) = (X+Y)^-0.2
#
#    f(x,y) = g ( u(x), v(x,y) ) * v1(x) / d
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    0.5555555555555556
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Elise deDoncker, Ian Robinson,
#    Algorithm 612:
#    Integration over a Triangle Using Nonlinear Extrapolation,
#    ACM Transactions on Mathematical Software,
#    Volume 10, Number 1, March 1984, pages 17-22.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  pa = 0.0
  pb = 1.0
  pc = 0.0
  pd = 0.0
  pg = -1.0
  ph =  1.0
  power = -0.2

  d = pb - pa
  u = ( x - pa ) / d
  v1 = ( 1.0 - u ) / ( ( pg - pc ) * x + ph - pd )
  v = v1 * ( y - pc * x - pd )

  f = ( 9.0 / 5.0 ) * ( u + v )**power * v1 / d

  return f

def p11_title ( ):

#*****************************************************************************80
#
## p11_title() returns the title of problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = (x+y)^(-0.2)'

  return title

def p11_vertices ( ):

#*****************************************************************************80
#
## p11_vertices() returns the vertices for problem 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p12_fun ( n, x, y ):

#*****************************************************************************80
#
## p12_fun() evaluates the integrand for problem 12.
#
#  Discussion:
#
#    The integral has been transformed from the integral of G(X,Y)
#    over the unit reference triangle.
#
#  Integrand:
#
#    PA = -1
#    PB = 3
#    PC = 0.25
#    PD = -2.75
#    PG = -1.0
#    PH = 1.0
#    D = PB - PA
#    U(X) = ( X - PA ) / D
#    V1(X) = ( 1 - ( X - PA ) / D ) / ( ( PG - PC ) * X + PH - PD )
#    V(X,Y) = V1(X) * ( Y - PC * X - PD )
#
#    G(X,Y) = (1-X-Y)^-0.2
#
#    f(x,y) = g ( u(x), v(x,y) ) * v1(x) / d
#
#  Vertices:
#
#    (-1,-3), (3,-2), (-1,2)
#
#  Integral:
#
#    0.6944444444444444
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Elise deDoncker, Ian Robinson,
#    Algorithm 612:
#    Integration over a Triangle Using Nonlinear Extrapolation,
#    ACM Transactions on Mathematical Software,
#    Volume 10, Number 1, March 1984, pages 17-22.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  pa = -1.0
  pb = 3.0
  pc = 0.25
  pd = -2.75
  pg = -1.0
  ph =  1.0
  power = -0.2

  d = pb - pa
  u  = ( x - pa ) / d
  v1 = ( 1.0 - u ) / ( ( pg - pc ) * x + ph - pd )
  v = v1 * ( y - pc * x - pd )
  f = ( 36.0 / 25.0 ) * ( 1.0 - u - v )**power * v1 / d

  return f

def p12_title ( ):

#*****************************************************************************80
#
## p12_title() returns the title of problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = (1-x-y)^(-0.2) on ((-1,-3),(3,-2),(-1,2))'

  return title

def p12_vertices ( ):

#*****************************************************************************80
#
## p12_vertices() returns the vertices for problem 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ -1.0, -3.0 ], \
    [  3.0, -2.0 ], \
    [ -1.0,  2.0 ] ] )

  return t

def p13_fun ( n, x, y ):

#*****************************************************************************80
#
## p13_fun() evaluates the integrand for problem 13.
#
#  Discussion:
#
#    The integral has been transformed from the integral of G(X,Y)
#    over the unit reference triangle.
#
#  Integrand:
#
#    PA = 0
#    PB = -7
#    PC = 0
#    PD = 0
#    PG = -3/7
#    PH = -3
#    D = PB - PA
#    U(X) = ( X - PA ) / D
#    V1(X) = ( 1 - ( X - PA ) / D ) / ( ( PG - PC ) * X + PH - PD )
#    V(X,Y) = V1(X) * ( Y - PC * X - PD )
#
#    G(X,Y) = (X*Y)^-0.2
#
#    f(x,y) = g ( u(x), v(x,y) ) * v1(x) / d
#
#  Vertices:
#
#    (0,0), (-7,0), (0,-3)
#
#  Integral:
#
#    0.94810264549557699446
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Elise deDoncker, Ian Robinson,
#    Algorithm 612:
#    Integration over a Triangle Using Nonlinear Extrapolation,
#    ACM Transactions on Mathematical Software,
#    Volume 10, Number 1, March 1984, pages 17-22.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  c = 0.94810264549557699446
  pa = 0.0
  pb = -7.0
  pc = 0.0
  pd = 0.0
  pg = ( -3.0 / 7.0 )
  ph =  -3.0
  power = -0.2

  d = pb - pa
  u = ( x - pa ) / d
  v1 = ( 1.0 - u ) / ( ( pg - pc ) * x + ph - pd )
  v = v1 * ( y - pc * x - pd )
  f = ( u * v )**power * v1 / d / c

  return f

def p13_title ( ):

#*****************************************************************************80
#
## p13_title() returns the title of problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = (x*y)^(-0.2) on ((0,0),(-7,0),(0,-3))'

  return title

def p13_vertices ( ):

#*****************************************************************************80
#
## p13_vertices() returns the vertices for problem 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [  0.0,  0.0 ], \
    [ -7.0,  0.0 ], \
    [  0.0, -3.0 ] ] )

  return t

def p14_fun ( n, x, y ):

#*****************************************************************************80
#
## p14_fun() evaluates the integrand for problem 14.
#
#  Integrand:
#
#    f(x,y) = 1 / sqrt ( X ) + 1 / sqrt ( Y ) + 1 / sqrt ( X + Y )
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    10/3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Elise deDoncker, Ian Robinson,
#    Algorithm 612:
#    Integration over a Triangle Using Nonlinear Extrapolation,
#    ACM Transactions on Mathematical Software,
#    Volume 10, Number 1, March 1984, pages 17-22.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = 3.0 / 10.0 * (      \
      1.0 / np.sqrt ( x ) \
    + 1.0 / np.sqrt ( y ) \
    + 1.0 / np.sqrt ( x + y ) )

  return f

def p14_title ( ):

#*****************************************************************************80
#
## p14_title() returns the title of problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = 1/sqrt(x) + 1/sqrt(y) + 1/sqrt(x+y)'

  return title

def p14_vertices ( ):

#*****************************************************************************80
#
## p14_vertices() returns the vertices for problem 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p15_fun ( n, x, y ):

#*****************************************************************************80
#
## p15_fun() evaluates the integrand for problem 15.
#
#  Integrand:
#
#    f(x,y) = 1 / sqrt ( 1 - X - Y )
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    4/3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Elise deDoncker, Ian Robinson,
#    Algorithm 612:
#    Integration over a Triangle Using Nonlinear Extrapolation,
#    ACM Transactions on Mathematical Software,
#    Volume 10, Number 1, March 1984, pages 17-22.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = 0.75 / np.sqrt ( 1.0 - x - y )

  return f

def p15_title ( ):

#*****************************************************************************80
#
## p15_title() returns the title of problem 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = 1/sqrt(1-x-y)'

  return title

def p15_vertices ( ):

#*****************************************************************************80
#
## p15_vertices() returns the vertices for problem 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p16_fun ( n, x, y ):

#*****************************************************************************80
#
## p16_fun() evaluates the integrand for problem 16.
#
#  Integrand:
#
#    f(x,y) = log ( x * y )
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    -1.5
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Elise deDoncker, Ian Robinson,
#    Algorithm 612:
#    Integration over a Triangle Using Nonlinear Extrapolation,
#    ACM Transactions on Mathematical Software,
#    Volume 10, Number 1, March 1984, pages 17-22.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = ( - 2.0 / 3.0 ) * np.log ( x * y )

  return f

def p16_title ( ):

#*****************************************************************************80
#
## p16_title() returns the title of problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = log(x*y)'

  return title

def p16_vertices ( ):

#*****************************************************************************80
#
## p16_vertices() returns the vertices for problem 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p17_fun ( n, x, y ):

#*****************************************************************************80
#
## p17_fun() evaluates the integrand for problem 17.
#
#  Integrand:
#
#    f(x,y) = 1/sqrt(|x-1/4|) + 1/sqrt(|y-1/2|)
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    3.11357229949...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Elise deDoncker, Ian Robinson,
#    Algorithm 612:
#    Integration over a Triangle Using Nonlinear Extrapolation,
#    ACM Transactions on Mathematical Software,
#    Volume 10, Number 1, March 1984, pages 17-22.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = ( 1.0 / 3.11357229949 ) * \
    ( 1.0 / np.sqrt ( np.abs ( x - 0.25 ) ) \
    + 1.0 / np.sqrt ( np.abs ( y - 0.50 ) ) )

  return f

def p17_title ( ):

#*****************************************************************************80
#
## p17_title() returns the title of problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = 1/sqrt(|x-1/4|) + 1/sqrt(|y-1/2|)'

  return title

def p17_vertices ( ):

#*****************************************************************************80
#
## p17_vertices() returns the vertices for problem 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p18_fun ( n, x, y ):

#*****************************************************************************80
#
## p18_fun() evaluates the integrand for problem 18.
#
#  Integrand:
#
#    f(x,y) = log ( x + y )
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    -1/4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Elise deDoncker, Ian Robinson,
#    Algorithm 612:
#    Integration over a Triangle Using Nonlinear Extrapolation,
#    ACM Transactions on Mathematical Software,
#    Volume 10, Number 1, March 1984, pages 17-22.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = - 4.0 * np.log ( x + y )

  return f

def p18_title ( ):

#*****************************************************************************80
#
## p18_title() returns the title of problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = log ( x + y )'

  return title

def p18_vertices ( ):

#*****************************************************************************80
#
## p18_vertices() returns the vertices for problem 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p19_fun ( n, x, y ):

#*****************************************************************************80
#
## p19_fun() evaluates the integrand for problem 19.
#
#  Integrand:
#
#    f(x,y) = sin ( x ) * cos ( 5 * y )
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    ( 3 + 2 * cos ( 2 ) ) * sin ( 1 )^3 / 30 = 0.043052326655855175018
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Elise deDoncker, Ian Robinson,
#    Algorithm 612:
#    Integration over a Triangle Using Nonlinear Extrapolation,
#    ACM Transactions on Mathematical Software,
#    Volume 10, Number 1, March 1984, pages 17-22.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  c = 0.043052326655855175018

  f = np.sin ( x ) * np.cos ( 5.0 * y ) / c

  return f

def p19_title ( ):

#*****************************************************************************80
#
## p19_title() returns the title of problem 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = sin ( x ) cos ( 5 y )'

  return title

def p19_vertices ( ):

#*****************************************************************************80
#
## p19_vertices() returns the vertices for problem 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p20_fun ( n, x, y ):

#*****************************************************************************80
#
## p20_fun() evaluates the integrand for problem 20.
#
#  Integrand:
#
#    f(x,y) = sin ( 11 x ) * cos ( y )
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    ( 11 * sin ( 1 ) - sin ( 11 ) / 120 = 0.085468091995313041919
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Elise deDoncker, Ian Robinson,
#    Algorithm 612:
#    Integration over a Triangle Using Nonlinear Extrapolation,
#    ACM Transactions on Mathematical Software,
#    Volume 10, Number 1, March 1984, pages 17-22.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  c = 0.085468091995313041919

  f = np.sin ( 11.0 * x ) * np.cos ( y ) / c

  return f

def p20_title ( ):

#*****************************************************************************80
#
## p20_title() returns the title of problem 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = sin ( 11 x ) cos ( y )'

  return title

def p20_vertices ( ):

#*****************************************************************************80
#
## p20_vertices() returns the vertices for problem 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p21_fun ( n, x, y ):

#*****************************************************************************80
#
## p21_fun() evaluates the integrand for problem 21.
#
#  Discussion:
#
#    To do this integral by hand, convert to polar coordinates:
#
#    Integral ( 0 <= t <= Pi/2 )
#      Integral ( 0 <= r <= 1/(cos(t)+sin(t)) ) 1/r * r dr dt
#
#  Integrand:
#
#    f(x,y) = 1 / sqrt ( x * x + y * y )
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    sqrt ( 2 ) * atanh ( 1/sqrt(2) ) = 1.246450480...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Elise deDoncker, Ian Robinson,
#    Algorithm 612:
#    Integration over a Triangle Using Nonlinear Extrapolation,
#    ACM Transactions on Mathematical Software,
#    Volume 10, Number 1, March 1984, pages 17-22.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  c = 1.2464504802804610268

  f = 1.0 / np.sqrt ( x**2 + y**2 ) / c

  return f

def p21_title ( ):

#*****************************************************************************80
#
## p21_title() returns the title of problem 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = 1 / r = 1 / sqrt ( x^2 + y^2 )'

  return title

def p21_vertices ( ):

#*****************************************************************************80
#
## p21_vertices() returns the vertices for problem 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def p22_fun ( n, x, y ):

#*****************************************************************************80
#
## p22_fun() evaluates the integrand for problem 22.
#
#  Discussion:
#
#    To do this integral by hand, convert to polar coordinates:
#
#    Integral ( 0 <= t <= Pi/2 )
#      Integral ( 0 <= r <= 1/(cos(t)+sin(t))) Log(r)/r * r dr dt
#
#  Integrand:
#
#    f(x,y) = log ( sqrt ( x * x + y * y ) ) / sqrt ( x * x + y * y )
#
#  Vertices:
#
#    (0,0), (1,0), (0,1)
#
#  Integral:
#
#    -1.5280234546641884580...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Elise deDoncker, Ian Robinson,
#    Algorithm 612:
#    Integration over a Triangle Using Nonlinear Extrapolation,
#    ACM Transactions on Mathematical Software,
#    Volume 10, Number 1, March 1984, pages 17-22.
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  c = -1.5280234546641884580

  f = np.log ( np.sqrt ( x**2 + y**2 ) ) / np.sqrt ( x**2 + y**2 ) / c

  return f

def p22_title ( ):

#*****************************************************************************80
#
## p22_title() returns the title of problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'f(x,y) = log ( r ) / r'

  return title

def p22_vertices ( ):

#*****************************************************************************80
#
## p22_vertices() returns the vertices for problem 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real T(3,2), the vertices.
#
  import numpy as np

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] )

  return t

def subtriangle_next ( n, more, i1, j1, i2, j2, i3, j3 ):

#*****************************************************************************80
#
## subtriangle_next() computes the next subtriangle of a triangle.
#
#  Discussion:
#
#    The three sides of a triangle have been subdivided into N segments,
#    inducing a natural subdivision of the triangle into N*N subtriangles.
#    It is desired to consider each subtriangle, one at a time, in some
#    definite order.  This routine can produce information defining each 
#    of the subtriangles, one after another.
#
#    The subtriangles are described in terms of the integer coordinates 
#    (I,J) of their vertices.  These coordinates both range from 0 to N,
#    with the additional restriction that I + J <= N.
#
#    The vertices of each triangle are listed in counterclockwise order.
#
#  Example:
#
#    N = 4
#
#    4  *
#       |\
#       16\
#    3  *--*
#       |14|\
#       13\15\
#    2  *--*--*
#       |\9|11|\
#       |8\10\12\
#    1  *--*--*--*
#       |\2|\4|\6|\
#       |1\|3\|5\|7\
#   0   *--*--*--*--*
#
#       0  1  2  3  4
#
#    Rank  I1 J1  I2 J2  I3 J3
#    ----  -----  -----  ----- 
#       1   0  0   1  0   0  1
#       2   1  1   0  1   1  0
#       3   1  0   2  0   1  1
#       4   2  1   1  1   2  0
#       5   2  0   3  0   2  1
#       6   3  1   1  1   3  0
#       7   3  0   4  0   3  1
#       8   0  1   1  1   0  2
#       9   1  2   0  2   1  1
#      10   1  1   2  1   1  2
#      11   2  2   1  2   2  1
#      12   2  1   3  1   2  2
#      13   0  2   1  2   0  3
#      14   1  3   0  3   1  2
#      15   1  2   2  2   1  3
#      16   0  3   1  3   0  4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, indicates the number of subdivisions of each side
#    of the original triangle.
#
#    logical MORE.  On first call, set MORE to false.  Thereafter, 
#    the input value of MORE should be the output value from the previous
#    call.
#
#    integer I1, J1, I2, J2, I3, J3, the indices of the vertices 
#    of the subtriangle as computed on the previous call.  On the first call
#    with MORE set to false, set these values to 0.
#
#  Output:
#
#    logical MORE, the output value of MORE will be true if there 
#    are more subtriangles that can be generated by further calls.  However, 
#    if MORE is returned as false, the accompanying subtriangle information 
#    refers to the last subtriangle that can be generated.
#
#    integer I1, J1, I2, J2, I3, J3, the indices of the 
#    vertices of the subtriangle.
#
  if ( n < 1 ):
    more = False
    return more, i1, j1, i2, j2, i3, j3

  if ( not more ):

    i1 = 0
    j1 = 0
    i2 = 1
    j2 = 0
    i3 = 0
    j3 = 1

    if ( n == 1 ):
      more = False
    else:
      more = True
#
#  We last generated a triangle like:
#
#    2---1
#     \  |
#      \ |
#       \|
#        3
#
  elif ( i2 < i3 ):

    i1 = i3
    j1 = j3
    i2 = i1 + 1
    j2 = j1
    i3 = i1
    j3 = j1 + 1
#
#  We last generated a triangle like
#
#    3
#    |\
#    | \
#    |  \
#    1---2
#
  elif ( i1 + 1 + j1 + 1 <= n ):

    i1 = i1 + 1
    j1 = j1 + 1
    i2 = i1 - 1
    j2 = j1
    i3 = i1
    j3 = j1 - 1
#
#  We must be at the end of a row.
#
  else:

    i1 = 0
    j1 = j1 + 1
    i2 = i1 + 1
    j2 = j1
    i3 = i1
    j3 = j1 + 1

    if ( n <= j1 + 1 ):
      more = False

  return more, i1, j1, i2, j2, i3, j3

def triangle_area ( t ):

#*****************************************************************************80
#
## triangle_area() computes the area of a triangle in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(3,2), the triangle vertices.
#
#  Output:
#
#    real AREA, the absolute area of the triangle.
#
  import numpy as np

  area = 0.5 * np.abs ( \
      t[0,0] * ( t[1,1] - t[2,1] ) \
    + t[1,0] * ( t[2,1] - t[0,1] ) \
    + t[2,0] * ( t[0,1] - t[1,1] ) )

  return area

def triangle_integrands_test01 ( ):

#*****************************************************************************80
#
## triangle_integrands_test01() tests get_prob_num() and p00_title().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'triangle_integrands_test01():' )
  print ( '  get_prob_num() reports the number of problems.' )
  print ( '  p00_title() returns a title for each problem.' )

  prob_num = get_prob_num ( )

  print ( '' )
  print ( '  The number of problems available is ', prob_num )
  print ( '' )
  print ( '  The problem titles:' )
  print ( '' )

  for problem in range ( 1, prob_num + 1 ):

    title = p00_title ( problem )

    print ( '  %8d  %s' % ( problem, title ) )

  return

def triangle_integrands_test02 ( ):

#*****************************************************************************80
#
## triangle_integrands_test02() tests p00_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  exact = 1.0
  n_log_max = 15

  print ( '' )
  print ( 'triangle_integrands_test02():' )
  print ( '  p00_monte_carlo() applies a Monte Carlo rule.' )

  prob_num = get_prob_num ( )

  print ( '' )
  print ( '  Problem            Exact' )
  print ( '           Pts       Approx        Error' )
  print ( '' )
#
#  Pick a problem.
#
  for problem in range ( 1, prob_num + 1 ):

    title = p00_title ( problem )

    print ( '' )
    print ( title )
    print ( '%8d        %12f' % ( problem, exact ) )
    print ( '' )
#
#  Pick a number of points.
#
    for n_log in range ( 0, n_log_max + 1 ):

      n = 2**n_log

      result = p00_monte_carlo ( problem, n )

      abs_error = np.abs ( exact - result )

      print ( '      %8d  %12f  %12f' % ( n, result, abs_error ) )

  return

def triangle_integrands_test03 ( ):

#*****************************************************************************80
#
## triangle_integrands_test03() tests p00_vertex_sub().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  exact = 1.0
  level_max = 4

  print ( '' )
  print ( 'triangle_integrands_test03():' )
  print ( '  p00_vertex_sub() applies a vertex rule with subdivision.' )

  prob_num = get_prob_num ( )

  print ( '' )
  print ( '  Problem            Exact' )
  print ( '           Pts       Approx        Error' )
  print ( '' )
#
#  Pick a problem.
#
  for problem in range ( 1, prob_num + 1 ):

    title = p00_title ( problem )
    singularity = p00_singularity ( problem )

    print ( '' )
    print ( title )
    print ( '%8d        %12f' % ( problem, exact ) )
    print ( '' )

    if ( singularity == 1 ):
      print ( '  Skip this problem, it has vertex singularities.' )
    elif ( singularity == 2 ):
      print ( '  Skip this problem, it has edge singularities.' )
    elif ( singularity == 3 ):
      print ( '  Skip this problem, it has internal singularities.' )
    else:
#
#  Pick a number of points.
#
      n = 0
      result = 0.0

      for level in range ( 0, 5 ):

        result, n = p00_vertex_sub ( problem, level, n, result )

        abs_error = np.abs ( exact - result )

        print ( '      %8d  %12f  %12f' % ( n, result, abs_error ) )

  return

def triangle_integrands_test04 ( ):

#*****************************************************************************80
#
## triangle_integrands_test04() tests p00_wandzura05_sub().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  exact = 1.0
  test_max = 5

  print ( '' )
  print ( 'triangle_integrands_test04():' )
  print ( '  p00_wandzura05_sub() applies a Wandzura rule with subdivision.' )

  prob_num = get_prob_num ( )

  print ( '' )
  print ( '  Problem            Exact' )
  print ( '           Pts       Approx        Error' )
  print ( '' )
#
#  Pick a problem.
#
  for problem in range ( 1, prob_num + 1 ):

    title = p00_title ( problem )

    print ( '' )
    print ( title )
    print ( '%8d        %12f' % ( problem, exact ) )
    print ( '' )
#
#  Pick a number of points.
#
    for test in range ( 0, test_max + 1 ):

      level = 2**test

      result, n = p00_wandzura05_sub ( problem, level )

      abs_error = np.abs ( exact - result )

      print ( '      %8d  %12f  %12f' % ( n, result, abs_error ) )

      if ( abs_error < 1.0E-06 ):
        print ( '                            Accuracy acceptable' )
        break

  return

def triangle_sample ( t, n ):

#*****************************************************************************80
#
## triangle_sample() returns random points in a triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(3,2), the triangle vertices.
#
#    integer N, the number of points to generate.
#
#  Output:
#
#    real X(N), Y(N), random points in the triangle.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )
#
#  Interpret R as a percentage of the triangle's area.
#
#  Imagine a line L, parallel to side 1, so that the area between
#  vertex 1 and line L is R percent of the full triangle's area.
#
#  The line L will intersect sides 2 and 3 at a fraction
#  ALPHA = SQRT ( R ) of the distance from vertex 1 to vertices 2 and 3.
#
#
#  Determine the coordinates of the points on sides 2 and 3 intersected
#  by line L.
#
  alpha = rng.random ( size = n )
  alpha = np.sqrt ( alpha )

  x12 = ( 1.0 - alpha ) * t[0,0] + alpha * t[1,0]
  x13 = ( 1.0 - alpha ) * t[0,0] + alpha * t[2,0]

  y12 = ( 1.0 - alpha ) * t[0,1] + alpha * t[1,1]
  y13 = ( 1.0 - alpha ) * t[0,1] + alpha * t[2,1]
#
#  Now choose, uniformly at random, a point on the line L.
#
  beta = rng.random ( size = n )

  x = ( 1.0 - beta ) * x12 + beta * x13
  y = ( 1.0 - beta ) * y12 + beta * y13

  return x, y

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  triangle_integrands_test ( )
  timestamp ( )

