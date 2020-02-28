#! /usr/bin/env python3
#
def gmtry ( nb, nw, nwall, wall ):

#*****************************************************************************80
#
#% GMTRY computes solid-related arrays.
#
#  Discussion:
#
#    This function was extracted from a vortex method program.
#    It sets up arrays needed for the computation, and performs
#    Gauss elimination on the matrix of wall-influence coefficients.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2015
#
#  Author:
#
#    Original FORTRAN77 version by David Bailey.
#    Python version by John Burkardt.
#
  import numpy as np

  period = 3.0
#
#  Compute arclength.
#
  matdim = 0
  arcl = 0.0
  ymin = 1.0E+30
  ymax = -1.0E+30
  pidp = np.pi / period

  for l in range ( 1, nb + 1 ):
    matdim = matdim + nwall[l-1]
    for k in range ( 1, nwall[l-1] + 1 ):
      arcl = arcl + abs ( wall[k-1,l-1] - wall[(k%nwall[l-1]),l-1] )
#
#  Compute core radius.
#
  r0 = 0.5 * arcl / matdim
  sigma = r0 / 2.0
#
#  Define creation points.
#
  xmax = np.zeros ( nb, dtype = np.float64 )
  zcr = np.zeros ( [ nw, nb ], dtype = np.complex128 )

  for l in range ( 1, nb + 1 ):

    for k in range ( 1, nwall[l-1] + 1 ):
      zz = wall[(k+nwall[l-1]-2)%nwall[l-1],l-1] - wall[(k%nwall[l-1]),l-1]
      zcr[k-1,l-1] = wall[k-1,l-1] + r0 * 1j / abs ( zz ) * zz
#
#  Check that wall and creation points are not crossed due to
#  too sharp a concave kink or an error in defining the body.
#  Also find highest, lowest and right-most point.
#
    value = zcr[0,l-1]
    xmax[l-1] =  value.real
    ls = 0

    for k in range ( 1, nwall[l-1] + 1 ):

      value = zcr[k-1,l-1]
      ymin = min ( ymin, value.imag )
      ymax = max ( ymax, value.imag )
      xmax[l-1] = max ( xmax[l-1], value.real )
      kp = 1 + ( k % nwall[l-1] )

      value1 = wall[kp-1,l-1] - wall[k-1,l-1]
      value2 = ( zcr[kp-1,l-1] - zcr[k-1,l-1] ) * value1.conjugate ( )

      if ( 0.0 < value2.real ):
        ls = l
        ks = k
#
#  The "main period" will be between ylimit and ylimit + period.
#
  ylimit = ( ymin - period + ymax ) / 2.0
#
#  Project creation points into main period.  This is technical.
#
  proj = np.zeros ( [ nw, nb ], dtype = np.complex128 )

  for l in range ( 1, nb + 1 ):
    for k in range ( 1, nwall[l-1] + 1 ):
      value = zcr[k-1,l-1]
      proj[k-1,l-1] = zcr[k-1,l-1] - 1j * period * \
      ( np.floor ( 5.0 + ( value.imag - ylimit ) / period ) - 5.0 )
#
#  Compute matrix.
#
  rmatrx = np.zeros ( [ nw*nb, nw*nb ], dtype = np.float64 )
  sig2 = ( 2.0 * pidp * sigma ) ** 2
  i0 = 0

  for l1 in range ( 1, nb + 1 ):

    j0 = 0

    for l2 in range ( 1, nb + 1 ):

      if ( l1 == l2 ):
        kron = 1
      else:
        kron = 0

      for j in range ( 1, nwall[l2-1] + 1 ):
        rmatrx[i0,j0+j-1] = kron
        z1 = np.exp ( ( wall[0,l1-1] - zcr[j-1,l2-1] ) * pidp )
        z1 = z1 - 1.0 / z1
        dum = sig2 + ( z1.real ) ** 2 + ( z1.imag ) ** 2
        for i in range ( 2, nwall[l1-1] + 1 ):
          zi = np.exp ( ( wall[i-1,l1-1] - zcr[j-1,l2-1] ) * pidp )
          zz = zi - 1.0 / zi
          rmatrx[i0+i-1,j0+j-1] = -0.25 / np.pi * np.log ( dum / \
            ( sig2 + ( zz.real ) ** 2 + ( zz.imag ) ** 2 ) )

      j0 = j0 + nwall[l2-1]

    i0 = i0 + nwall[l1-1]
#
#  Gauss elimination.
#
  for i in range ( 1, matdim + 1 ):
    rmatrx[i-1,i-1] = 1.0 / rmatrx[i-1,i-1]
    for j in range ( i + 1, matdim + 1 ):
      rmatrx[j-1,i-1] = rmatrx[j-1,i-1] * rmatrx[i-1,i-1]
      for k in range ( i + 1, matdim + 1 ):
        rmatrx[j-1,k-1] = rmatrx[j-1,k-1] - rmatrx[j-1,i-1] * rmatrx[i-1,k-1]

  return rmatrx

def gmtry_test ( ):

#*****************************************************************************80
#
#% GMTRY_TEST tests GMTRY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2015
#
#  Author:
#
#    Original FORTRAN77 version by David Bailey.
#    Python version by John Burkardt.
#
  import numpy as np
  from time import clock

  nb = 5
  nw = 100

  it = 2
  ans = -2.57754233214174
  lw = 2 * nw * nb
#
#  Random initialization.
#
  f7 = 78125.0
  t30 = 1073741824.0
  t2 = f7 / t30
 
  nwall = np.zeros ( nb, dtype = np.int32 )

  for i in range ( 0, nb ):
    nwall[i] = nw

  wall = np.zeros ( [ nw, nb ], dtype = np.complex128 )

  for j in range ( 0, nb ):
    for i in range ( 0, nw ):
      t1 = ( ( f7 * t2 ) % 1.0 )
      t2 = ( ( f7 * t1 ) % 1.0 )
      wall[i,j] = t1 + 1j * t2
#
#  Timing.
#
  tm = clock ( )

  for i in range ( 0, it ):
    rmatrx = gmtry ( nb, nw, nwall, wall )

  tm = clock ( ) - tm
#
#  Results.
#
  er = abs ( ( rmatrx[18,18] - ans ) / ans )
  fp = it * ( 120 * ( nb * nw ) ** 2 + 0.666 * ( nb * nw ) ** 3 )
  rt = 1.0E-06 * fp / tm
#
#  Terminate.
#
  return er, fp, tm, rt

if ( __name__ == '__main__' ):
  import platform
  from timestamp import timestamp
  timestamp ( )
  er, fp, tm, rt = gmtry_test ( )
  print ( '' )
  print ( 'GMTRY:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '' )
  print ( ' Program          Error         FP Ops     Seconds      MFLOPS' )
  print ( '' )
  print ( ' GMTRY    %13.4e  %13.4e  %10.4e  %10.2e' % ( er, fp, tm, rt ) )
  print ( '' )
  print ( 'GMTRY:' )
  print ( '  Normal end of execution.' )
  timestamp ( )

