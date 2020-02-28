#! /usr/bin/env python3
#
def asa047_test ( ):

#*****************************************************************************80
#
## ASA047_TEST tests the ASA047 library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from asa047  import nelmin_helical_test
  from asa047  import nelmin_powell_test
  from asa047  import nelmin_quartic_test
  from asa047  import nelmin_rosenbrock_test

  print ( '' )
  print ( 'ASA047_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the ASA047 library.' )

  nelmin_helical_test ( )
  nelmin_powell_test ( )
  nelmin_quartic_test ( )
  nelmin_rosenbrock_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ASA047_TEST:' )
  print ( '  Normal end of execution.' )
  return

def nelmin ( fn, n, start, reqmin, step, konvge, kcount ):

#*****************************************************************************80
#
## NELMIN minimizes a function using the Nelder-Mead algorithm.
#
#  Discussion:
#
#    This routine seeks the minimum value of a user-specified function.
#
#    Simplex function minimisation procedure due to Nelder+Mead(1965),
#    as implemented by O'Neill(1971, Appl.Statist. 20, 338-45), with
#    subsequent comments by Chambers+Ertel(1974, 23, 250-1), Benyon(1976,
#    25, 97) and Hill(1978, 27, 380-2)
#
#    The function to be minimized must have the form:
#
#      function value = fn ( x )
#
#    where X is a vector, and VALUE is the (scalar) function value.
#    The name of this function must be passed as the argument FN.
#
#    This routine does not include a termination test using the
#    fitting of a quadratic surface.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    Original FORTRAN77 version by R ONeill.
#    Python version by John Burkardt.
#
#  Reference:
#
#    John Nelder, Roger Mead,
#    A simplex method for function minimization,
#    Computer Journal,
#    Volume 7, 1965, pages 308-313.
#
#    R ONeill,
#    Algorithm AS 47:
#    Function Minimization Using a Simplex Procedure,
#    Applied Statistics,
#    Volume 20, Number 3, 1971, pages 338-345.
#
#  Parameters:
#
#    Input, real value = FN ( X ), the name of the MATLAB function which 
#    evaluates the function to be minimized, preceded by an "@" sign.
#
#    Input, integer N, the number of variables.
#
#    Input, real START(N).  On input, a starting point
#    for the iteration.  On output, this data may have been overwritten.
#
#    Input, real REQMIN, the terminating limit for the variance
#    of function values.
#
#    Input, real STEP(N), determines the size and shape of the
#    initial simplex.  The relative magnitudes of its elements should reflect
#    the units of the variables.
#
#    Input, integer KONVGE, the convergence check is carried out
#    every KONVGE iterations.
#
#    Input, integer KCOUNT, the maximum number of function
#    evaluations.
#
#    Output, real XMIN(N), the coordinates of the point which
#    is estimated to minimize the function.
#
#    Output, real YNEWLO, the minimum value of the function.
#
#    Output, integer ICOUNT, the number of function evaluations.
#
#    Output, integer NUMRES, the number of restarts.
#
#    Output, integer IFAULT, error indicator.
#    0, no errors detected.
#    1, REQMIN, N, or KONVGE has an illegal value.
#    2, iteration terminated because KCOUNT was exceeded without convergence.
#
  import numpy as np

  xmin = np.zeros ( n )
  ynewlo = 0.0
  icount = 0
  numres = 0
  ifault = 0

  ccoeff = 0.5
  ecoeff = 2.0
  eps = 0.001
  rcoeff = 1.0
#
#  Check the input parameters.
#
  if ( reqmin <= 0.0 ):
    ifault = 1
    return xmin, ynewlo, icount, numres, ifault

  if ( n < 1 ):
    ifault = 1
    return xmin, ynewlo, icount, numres, ifault

  if ( konvge < 1 ):
    ifault = 1
    return xmin, ynewlo, icount, numres, ifault
#
#  Initialization.
#
  jcount = konvge
  delta = 1.0
  rq = reqmin * float ( n )

  p = np.zeros ( [ n, n + 1 ] )
  p2star = np.zeros ( n )
  pbar = np.zeros ( n )
  pstar = np.zeros ( n )
  y = np.zeros ( n + 1 )
#
#  Initial or restarted loop.
#
  while ( True ):

    for i in range ( 0, n ):
      p[i,n] = start[i]

    y[n] = fn ( start )
    icount = icount + 1
#
#  Define the initial simplex.
#
    for j in range ( 0, n ):
      x = start[j]
      start[j] = start[j] + step[j] * delta
      for i in range ( 0, n ):
        p[i,j] = start[i]
      y[j] = fn ( start )
      icount = icount + 1
      start[j] = x
#
#  The simplex construction is complete.
#
#  Find highest and lowest Y values.  YNEWLO = Y(IHI) indicates
#  the vertex of the simplex to be replaced.
#
    ylo = y[0]
    ilo = 0

    for i in range ( 1, n + 1 ):
      if ( y[i] < ylo ):
        ylo = y[i]
        ilo = i
#
#  Inner loop.
#
    while ( icount < kcount ):

      ynewlo = y[0]
      ihi = 0

      for i in range ( 1, n + 1 ):
        if ( ynewlo < y[i] ):
          ynewlo = y[i]
          ihi = i
#
#  Calculate PBAR, the centroid of the simplex vertices
#  excepting the vertex with Y value YNEWLO.
#
      for i in range ( 0, n ):
        z = 0.0
        for j in range ( 0, n + 1 ):
          z = z + p[i,j]
        z = z - p[i,ihi]
        pbar[i] = z / float ( n )
#
#  Reflection through the centroid.
#
      for i in range ( 0, n ):
        pstar[i] = pbar[i] + rcoeff * ( pbar[i] - p[i,ihi] )

      ystar = fn ( pstar )
      icount = icount + 1
#
#  Successful reflection, so extension.
#
      if ( ystar < ylo ):

        for i in range ( 0, n ):
          p2star[i] = pbar[i] + ecoeff * ( pstar[i] - pbar[i] )

        y2star = fn ( p2star )
        icount = icount + 1
#
#  Check extension.
#
        if ( ystar < y2star ):

          for i in range ( 0, n ):
            p[i,ihi] = pstar[i]

          y[ihi] = ystar
#
#  Retain extension or contraction.
#
        else:

          for i in range ( 0, n ):
            p[i,ihi] = p2star[i]

          y[ihi] = y2star
#
#  No extension.
#
      else:

        l = 0
        for i in range ( 0, n + 1 ):
          if ( ystar < y[i] ):
            l = l + 1

        if ( 1 < l ):

          for i in range ( 0, n ):
            p[i,ihi] = pstar[i]

          y[ihi] = ystar
#
#  Contraction on the Y(IHI) side of the centroid.
#
        elif ( l == 0 ):

          for i in range ( 0, n ):
            p2star[i] = pbar[i] + ccoeff * ( p[i,ihi] - pbar[i] )

          y2star = fn ( p2star )
          icount = icount + 1
#
#  Contract the whole simplex.
#
          if ( y[ihi] < y2star ):

            for j in range ( 0, n + 1 ):
              for i in range ( 0, n ):
                p[i,j] = ( p[i,j] + p[i,ilo] ) * 0.5
                xmin[i] = p[i,j]
              y[j] = fn ( xmin )
              icount = icount + 1

            ylo = y[0]
            ilo = 0

            for i in range ( 1, n + 1 ):
              if ( y[i] < ylo ):
                ylo = y[i]
                ilo = i

            continue
#
#  Retain contraction.
#
          else:

            for i in range ( 0, n ):
              p[i,ihi] = p2star[i]
            y[ihi] = y2star

#
#  Contraction on the reflection side of the centroid.
#
        elif ( l == 1 ):

          for i in range ( 0, n ):
            p2star[i] = pbar[i] + ccoeff * ( pstar[i] - pbar[i] )

          y2star = fn ( p2star )
          icount = icount + 1
#
#  Retain reflection?
#
          if ( y2star <= ystar ):

            for i in range ( 0, n ):
              p[i,ihi] = p2star[i]
            y[ihi] = y2star

          else:

            for i in range ( 0, n ):
              p[i,ihi] = pstar[i]
            y[ihi] = ystar
#
#  Check if YLO improved.
#
      if ( y[ihi] < ylo ):
        ylo = y[ihi]
        ilo = ihi

      jcount = jcount - 1

      if ( 0 < jcount ):
        continue
#
#  Check to see if minimum reached.
#
      if ( icount <= kcount ):

        jcount = konvge

        z = 0.0
        for i in range ( 0, n + 1 ):
          z = z + y[i]
        x = z / float ( n + 1 )

        z = 0.0
        for i in range ( 0, n + 1 ):
          z = z + ( y[i] - x ) ** 2

        if ( z <= rq ):
          break
#
#  Factorial tests to check that YNEWLO is a local minimum.
#
    for i in range ( 0, n ):
      xmin[i] = p[i,ilo]

    ynewlo = y[ilo]

    if ( kcount < icount ):
      ifault = 2
      break

    ifault = 0

    for i in range ( 0, n ):
      delta = step[i] * eps
      xmin[i] = xmin[i] + delta
      z = fn ( xmin )
      icount = icount + 1
      if ( z < ynewlo ):
        ifault = 2
        break
      xmin[i] = xmin[i] - delta - delta
      z = fn ( xmin )
      icount = icount + 1
      if ( z < ynewlo ):
        ifault = 2
        break
      xmin[i] = xmin[i] + delta

    if ( ifault == 0 ):
      break
#
#  Restart the procedure.
#
    for i in range ( 0, n ):
      start[i] = xmin[i]

    delta = eps
    numres = numres + 1

  return xmin, ynewlo, icount, numres, ifault

def nelmin_helical_test ( ):

#*****************************************************************************80
#
## NELMIN_HELICAL_TEST demonstrates the use of NELMIN on HELICAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  print ( '' )
  print ( 'NELMIN_HELICAL_TEST' )
  print ( '  Apply NELMIN to the HELICAL function.' )

  start = np.array ( [ -1.0, 0.0, 0.0 ] )

  reqmin = 1.0E-08

  step = np.ones ( n )

  konvge = 10
  kcount = 500

  r8vec_print ( n, start, '  Starting point x:' )

  ynewlo = helical ( start )

  print ( '' )
  print ( '  F(X) = %g' % ( ynewlo ) )

  xmin, ynewlo, icount, numres, ifault = nelmin ( helical, n, start, \
    reqmin, step, konvge, kcount )

  print ( '' )
  print ( '  Return code IFAULT = %d' % ( ifault ) )

  r8vec_print ( n, xmin, '  Estimated minimizer x*:' )

  print ( '' )
  print ( '  F(X*) = %g' % ( ynewlo ) )

  print ( '' )
  print ( '  Number of iterations = %d' % ( icount ) )
  print ( '  Number of restarts =   %d' % ( numres ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NELMIN_HELICAL_TEST' )
  print ( '  Normal end of execution.' )

def nelmin_powell_test ( ):

#*****************************************************************************80
#
## NELMIN_POWELL_TEST demonstrates the use of NELMIN on POWELL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'NELMIN_POWELL_TEST' )
  print ( '  Apply NELMIN to POWELL quartic function.' )

  start =  np.array ( [ 3.0, - 1.0, 0.0, 1.0 ] )
  reqmin = 1.0E-08
  step = np.ones ( n )
  konvge = 10
  kcount = 500

  r8vec_print ( n, start, '  Starting point x:' )

  ynewlo = powell ( start )

  print ( '' )
  print ( '  F(X) = %g' % ( ynewlo ) )

  xmin, ynewlo, icount, numres, ifault = nelmin ( powell, n, start, \
    reqmin, step, konvge, kcount )

  print ( '' )
  print ( '  Return code IFAULT = %d' % ( ifault ) )

  r8vec_print ( n, xmin, '  Estimated minimizer x*:' )

  print ( '' )
  print ( '  F(X*) = %g' % ( ynewlo ) )

  print ( '' )
  print ( '  Number of iterations = %d' % ( icount ) )
  print ( '  Number of restarts =   %d' % ( numres ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NELMIN_POWELL_TEST' )
  print ( '  Normal end of execution.' )
  return

def nelmin_quartic_test ( ):

#*****************************************************************************80
#
## NELMIN_QUARTIC_TEST demonstrates the use of NELMIN on QUARTIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'NELMIN_QUARTIC_TEST' )
  print ( '  Apply NELMIN to QUARTIC function.' )

  start = np.ones ( n )
  reqmin = 1.0E-08
  step = np.ones ( n )
  konvge = 10
  kcount = 2000

  r8vec_print ( n, start, '  Starting point x:' )

  ynewlo = quartic ( start )

  print ( '' )
  print ( '  F(X) = %g' % ( ynewlo ) )

  xmin, ynewlo, icount, numres, ifault = nelmin ( quartic, n, start, \
    reqmin, step, konvge, kcount )

  print ( '' )
  print ( '  Return code IFAULT = %d' % ( ifault ) )

  r8vec_print ( n, xmin, '  Estimated minimizer x*:' )

  print ( '' )
  print ( '  F(X*) = %g' % ( ynewlo ) )

  print ( '' )
  print ( '  Number of iterations = %d' % ( icount ) )
  print ( '  Number of restarts =   %d' % ( numres ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NELMIN_QUARTIC_TEST' )
  print ( '  Normal end of execution.' )
  return

def nelmin_rosenbrock_test ( ):

#*****************************************************************************80
#
## NELMIN_ROSENBROCK_TEST demonstrates the use of NELMIN on ROSENBROCK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 2

  print ( '' )
  print ( 'NELMIN_ROSENBROCK_TEST' )
  print ( '  Apply NELMIN to ROSENBROCK function.' )

  start = np.array ( [ -1.2, 1.0 ] )
  reqmin = 1.0E-08
  step = np.ones ( n )
  konvge = 10
  kcount = 500

  r8vec_print ( n, start, '  Starting point x:' )

  ynewlo = rosenbrock ( start )

  print ( '' )
  print ( '  F(X) = %g' % ( ynewlo ) )

  xmin, ynewlo, icount, numres, ifault = nelmin ( rosenbrock, n, start, \
    reqmin, step, konvge, kcount )

  print ( '' )
  print ( '  Return code IFAULT = %d' % ( ifault ) )

  r8vec_print ( n, xmin, '  Estimated minimizer x*:' )

  print ( '' )
  print ( '  F(X*) = %g' % ( ynewlo ) )

  print ( '' )
  print ( '  Number of iterations = %d' % ( icount ) )
  print ( '  Number of restarts =   %d' % ( numres ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NELMIN_ROSENBROCK_TEST' )
  print ( '  Normal end of execution.' )
  return

def helical ( x ):

#*****************************************************************************80
#
## HELICAL evaluates the Fletcher-Powell helical valley function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    R ONeill,
#    Algorithm AS 47:
#    Function Minimization Using a Simplex Procedure,
#    Applied Statistics,
#    Volume 20, Number 3, 1971, pages 338-345.
#
#  Parameters:
#
#    Input, real X(3), the argument.
#
#    Output, real FX, the value of the function.
#
  import math
  import numpy as np

  if ( 0.0 < x[0] ):
    theta = math.atan2 ( x[1], x[0] ) / 2.0 / np.pi
  elif ( x[0] < 0.0 ):
    theta = 0.5 + math.atan2 ( x[1], x[0] ) / 2.0 / np.pi
  elif ( x[0] == 0.0 ):
    theta = 0.25

  fx1 = x[2] - 10.0 * theta
  fx2 = np.sqrt ( x[0] * x[0] + x[1] * x[1] )
  fx3 = x[2]

  fx = 100.0 * fx1 * fx1 + fx2 * fx2 + fx3 * fx3

  return fx

def powell ( x ):

#*****************************************************************************80
#
## POWELL evaluates the Powell quartic function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    R ONeill,
#    Algorithm AS 47:
#    Function Minimization Using a Simplex Procedure,
#    Applied Statistics,
#    Volume 20, Number 3, 1971, pages 338-345.
#
#  Parameters:
#
#    Input, real X(4), the argument.
#
#    Output, real FX, the value of the function.
#
  fx1 = x[0] + 10.0 * x[1]
  fx2 = x[2] - x[3]
  fx3 = x[1] - 2.0 * x[2]
  fx4 = x[0] - x[3]

  fx =        fx1 * fx1 \
     +  5.0 * fx2 * fx2 \
     +        fx3 * fx3 * fx3 * fx3 \
     + 10.0 * fx4 * fx4 * fx4 * fx4

  return fx

def quartic ( x ):

#*****************************************************************************80
#
## QUARTIC evaluates a function defined by a sum of fourth powers.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    R ONeill,
#    Algorithm AS 47:
#    Function Minimization Using a Simplex Procedure,
#    Applied Statistics,
#    Volume 20, Number 3, 1971, pages 338-345.
#
#  Parameters:
#
#    Input, real X(10), the argument.
#
#    Output, real FX, the value of the function.
#
  fx = 0.0
  for i in range ( 0, 10 ):
    fx = fx + x[i] ** 4

  return fx

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %12g' % ( i, a[i] ) )

def rosenbrock ( x ):

#*****************************************************************************80
#
## ROSENBROCK evaluates the Rosenbrock parabolic value function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    R ONeill,
#    Algorithm AS 47:
#    Function Minimization Using a Simplex Procedure,
#    Applied Statistics,
#    Volume 20, Number 3, 1971, pages 338-345.
#
#  Parameters:
#
#    Input, real X(2), the argument.
#
#    Output, real FX, the value of the function.
#
  fx1 = x[1] - x[0] * x[0]
  fx2 = 1.0 - x[0]

  fx = 100.0 * fx1 * fx1 + fx2 * fx2

  return fx

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  asa047_test ( )
  timestamp ( )
