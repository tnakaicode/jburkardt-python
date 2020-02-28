#! /usr/bin/env python3
#
def btrix ( js, je, ls, le, k, jd, kd, ld, md, a, b, c, s ):

#*****************************************************************************80
#
## BTRIX is a block tridiagonal solver in one direction.
#
#  Discussion:
#
#    The array has four dimensions.  The routine solves along the
#    "J" index.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    Original FORTRAN77 version by David Bailey.
#    Python version by John Burkardt.
#
  import numpy as np

  l11 = np.zeros ( md )
  l21 = np.zeros ( md )
  l31 = np.zeros ( md )
  l41 = np.zeros ( md )
  l51 = np.zeros ( md )
  l22 = np.zeros ( md )
  l32 = np.zeros ( md )
  l33 = np.zeros ( md )
  l42 = np.zeros ( md )
  l43 = np.zeros ( md )
  l44 = np.zeros ( md )
  l52 = np.zeros ( md )
  l53 = np.zeros ( md )
  l54 = np.zeros ( md )
  l55 = np.zeros ( md )
  u12 = np.zeros ( md )
  u13 = np.zeros ( md )
  u14 = np.zeros ( md )
  u15 = np.zeros ( md )
  u23 = np.zeros ( md )
  u24 = np.zeros ( md )
  u25 = np.zeros ( md )
  u34 = np.zeros ( md )
  u35 = np.zeros ( md )
  u45 = np.zeros ( md )
#
#  Part 1.  Forward block sweep.
#
  for j in range ( js, je + 1 ):
#
#  Step 1.  Construct L(I) in B.
#
    if ( j != js ):
      for m in range ( 1, 6 ):
        for n in range ( 1, 6 ):
          for l in range ( ls, le + 1 ):
            b[m-1,n-1,j-1,l-1] = b[m-1,n-1,j-1,l-1]       \
              - a[m-1,0,j-1,l-1] * b[0,n-1,j-2,l-1] \
              - a[m-1,1,j-1,l-1] * b[1,n-1,j-2,l-1] \
              - a[m-1,2,j-1,l-1] * b[2,n-1,j-2,l-1] \
              - a[m-1,3,j-1,l-1] * b[3,n-1,j-2,l-1] \
              - a[m-1,4,j-1,l-1] * b[4,n-1,j-2,l-1]
#
#  Step 2.  Compute L inverse.
#
#  A.  Decompose L(I) into L and U.
#
    for l in range ( ls, le + 1 ):
      l11[l-1] = 1.0 / b[0,0,j-1,l-1]
      u12[l-1] = b[0,1,j-1,l-1] * l11[l-1]
      u13[l-1] = b[0,2,j-1,l-1] * l11[l-1]
      u14[l-1] = b[0,3,j-1,l-1] * l11[l-1]
      u15[l-1] = b[0,4,j-1,l-1] * l11[l-1]
      l21[l-1] = b[1,0,j-1,l-1]
      l22[l-1] = 1.0 / ( b[1,1,j-1,l-1] - l21[l-1] * u12[l-1] )
      u23[l-1] = ( b[1,2,j-1,l-1] - l21[l-1] * u13[l-1] ) * l22[l-1]
      u24[l-1] = ( b[1,3,j-1,l-1] - l21[l-1] * u14[l-1] ) * l22[l-1]
      u25[l-1] = ( b[1,4,j-1,l-1] - l21[l-1] * u15[l-1] ) * l22[l-1]
      l31[l-1] = b[2,0,j-1,l-1]
      l32[l-1] = b[2,1,j-1,l-1] - l31[l-1] * u12[l-1]
      l33[l-1] = 1.0 / ( b[2,2,j-1,l-1] - l31[l-1] * u13[l-1] - l32[l-1] * u23[l-1] )
      u34[l-1]  = ( b[2,3,j-1,l-1] - l31[l-1] * u14[l-1] - l32[l-1] * u24[l-1] ) * l33[l-1]
      u35[l-1]  = ( b[2,4,j-1,l-1] - l31[l-1] * u15[l-1] - l32[l-1] * u25[l-1] ) * l33[l-1]

    for l in range ( ls, le + 1 ):
      l41[l-1] = b[3,0,j-1,l-1]
      l42[l-1] = b[3,1,j-1,l-1] - l41[l-1] * u12[l-1]
      l43[l-1] = b[3,2,j-1,l-1] - l41[l-1] * u13[l-1] - l42[l-1] * u23[l-1]
      l44[l-1] = 1.0 / ( b[3,3,j-1,l-1] - l41[l-1] * u14[l-1] \
        - l42[l-1] * u24[l-1] - l43[l-1] * u34[l-1] )
      u45[l-1] = ( b[3,4,j-1,l-1] - l41[l-1] * u15[l-1] - l42[l-1] * u25[l-1] \
        - l43[l-1] * u35[l-1] ) * l44[l-1]
      l51[l-1] = b[4,0,j-1,l-1]
      l52[l-1] = b[4,1,j-1,l-1] - l51[l-1] * u12[l-1]
      l53[l-1] = b[4,2,j-1,l-1] - l51[l-1] * u13[l-1] - l52[l-1] * u23[l-1]
      l54[l-1] = b[4,3,j-1,l-1] - l51[l-1] * u14[l-1] - l52[l-1] * u24[l-1] - l53[l-1] * u34[l-1]
      l55[l-1] = 1.0 / ( b[4,4,j-1,l-1] - l51[l-1] * u15[l-1] - l52[l-1] * u25[l-1] \
        - l53[l-1] * u35[l-1] - l54[l-1] * u45[l-1] )
#
#  Step 3.  Solve for intermediate vector.
#
#  A.  Construct the right hand side.
#
    if ( j != js ):
      for m in range ( 1, 6 ):
        for l in range ( ls, le + 1 ):
          s[j-1,k-1,l-1,m-1] = s[j-1,k-1,l-1,m-1] \
            - a[m-1,0,j-1,l-1] * s[j-2,k-1,l-1,0] \
            - a[m-1,1,j-1,l-1] * s[j-2,k-1,l-1,1] \
            - a[m-1,2,j-1,l-1] * s[j-2,k-1,l-1,2] \
            - a[m-1,3,j-1,l-1] * s[j-2,k-1,l-1,3] \
            - a[m-1,4,j-1,l-1] * s[j-2,k-1,l-1,4]
#
#  B. Intermediate vector.
#
#  Forward substitution.
#
    for l in range ( ls, le + 1 ):
      d1 =   s[j-1,k-1,l-1,0] * l11[l-1]
      d2 = ( s[j-1,k-1,l-1,1] - l21[l-1] * d1 ) * l22[l-1]
      d3 = ( s[j-1,k-1,l-1,2] - l31[l-1] * d1 - l32[l-1] * d2 ) * l33[l-1]
      d4 = ( s[j-1,k-1,l-1,3] - l41[l-1] * d1 - l42[l-1] * d2 - l43[l-1] * d3 ) * l44[l-1]
      d5 = ( s[j-1,k-1,l-1,4] - l51[l-1] * d1 - l52[l-1] * d2 - l53[l-1] * d3 \
        - l54[l-1] * d4 ) * l55[l-1]
#
#  Backward substitution.
#
      s[j-1,k-1,l-1,4] = d5
      s[j-1,k-1,l-1,3] = d4 - u45[l-1] * d5
      s[j-1,k-1,l-1,2] = d3 - u34[l-1] * s[j-1,k-1,l-1,3] - u35[l-1] * d5
      s[j-1,k-1,l-1,1] = d2 - u23[l-1] * s[j-1,k-1,l-1,2] - u24[l-1] * s[j-1,k-1,l-1,3] - u25[l-1] * d5
      s[j-1,k-1,l-1,0] = d1 - u12[l-1] * s[j-1,k-1,l-1,1] - u13[l-1] * s[j-1,k-1,l-1,2] \
        - u14[l-1] * s[j-1,k-1,l-1,3] - u15[l-1] * d5
#
#  Step 4.  Construct U(I) = inverse(L(I))*C(I+1) by columns and store in B.
#
    if ( j != je ):

      for n in range ( 1, 6 ):
        for l in range ( ls, le + 1 ):
#
#  Forward substitution.
#
          c1 =   c[0,n-1,j-1,l-1] * l11[l-1]
          c2 = ( c[1,n-1,j-1,l-1] - l21[l-1] * c1 ) * l22[l-1]
          c3 = ( c[2,n-1,j-1,l-1] - l31[l-1] * c1 - l32[l-1] * c2 ) * l33[l-1]
          c4 = ( c[3,n-1,j-1,l-1] - l41[l-1] * c1 - l42[l-1] * c2 - l43[l-1] * c3 ) * l44[l-1]
          c5 = ( c[4,n-1,j-1,l-1] - l51[l-1] * c1 - l52[l-1] * c2 \
            - l53[l-1] * c3 - l54[l-1] * c4 ) * l55[l-1]
#
#  Backward substitution.
#
          b[4,n-1,j-1,l-1] = c5
          b[3,n-1,j-1,l-1] = c4 - u45[l-1] * c5
          b[2,n-1,j-1,l-1] = c3 - u34[l-1] * b[3,n-1,j-1,l-1] - u35[l-1] * c5
          b[1,n-1,j-1,l-1] = c2 - u23[l-1] * b[2,n-1,j-1,l-1] - u24[l-1] * b[3,n-1,j-1,l-1] \
            - u25[l-1] * c5
          b[0,n-1,j-1,l-1] = c1 - u12[l-1] * b[1,n-1,j-1,l-1] - u13[l-1] * b[2,n-1,j-1,l-1] \
            - u14[l-1] * b[3,n-1,j-1,l-1] - u15[l-1] * c5
#
#  Part 2.  Backward block sweep.
#
  jem1 = je - 1

  for j in range ( jem1, js - 1, -1 ):
    for m in range ( 1, 6 ):
      for l in range ( ls, le + 1 ):
        s[j-1,k-1,l-1,m-1] = s[j-1,k-1,l-1,m-1] \
          - b[m-1,0,j-1,l-1] * s[j,k-1,l-1,0] \
          - b[m-1,1,j-1,l-1] * s[j,k-1,l-1,1] \
          - b[m-1,2,j-1,l-1] * s[j,k-1,l-1,2] \
          - b[m-1,3,j-1,l-1] * s[j,k-1,l-1,3] \
          - b[m-1,4,j-1,l-1] * s[j,k-1,l-1,4]

  return s

def btrix_test ( ):

#*****************************************************************************80
#
## BTRIX_TEST tests BTRIX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    Original FORTRAN77 version by David Bailey.
#    Python version by John Burkardt.
#
  import numpy as np
  import platform
  from time import clock

  jd = 30
  kd = 30
  ld = 30
  md = 30

  js = 2
  je = 29
  ls = 2
  le = 29
  it = 20
  ans = -0.286282658663962
  nb = 25 * md * md
  ns = jd * kd * ld * 5
#
#  Random initialization.
#
  f7 = 78125.0
  t30 = 1073741824.0
  t = f7 / t30

  a = np.zeros ( [ 5, 5, md, md ] )
  bx = np.zeros ( [ 5, 5, md, md ] )
  c = np.zeros ( [ 5, 5, md, md ] )

  for l in range ( 1, md + 1 ):
    for k in range ( 1, md + 1 ):
      for j in range ( 1, 6 ):
        for i in range ( 1, 6 ):
          t = ( ( f7 * t ) % 1.0 )
          a[i-1,j-1,k-1,l-1] = t
          t = ( ( f7 * t ) % 1.0 )
          bx[i-1,j-1,k-1,l-1] = t
          t = ( ( f7 * t ) % 1.0 )
          c[i-1,j-1,k-1,l-1] = t

  sx = np.zeros ( [ jd, kd, ld, 5 ] )

  for l in range ( 1, 5 + 1 ):
    for k in range ( 1, ld + 1 ):
      for j in range ( 1, kd + 1 ):
        for i in range ( 1, jd + 1 ):
          t = ( ( f7 * t ) % 1.0 )
          sx[i-1,j-1,k-1,l-1] = t
#
#  Timing.
#
  b = np.zeros ( [ 5, 5, md, md ] )
  s = np.zeros ( [ jd, kd, ld, 5 ] )

  tm = clock ( )

  for ii in range ( 0, it ):

    for i in range ( 1, jd + 1 ):
      for j in range ( 1, kd + 1 ):
        for k in range ( 1, ld + 1 ):
          for l in range ( 1, 6 ):
            s[i-1,j-1,k-1,l-1] = sx[i-1,j-1,k-1,l-1]
    
    for kk in range ( 1, kd + 1 ):

      for i in range ( 1, 6 ):
        for j in range ( 1, 6 ):
          for k in range ( 1, md + 1 ):
            for l in range ( 1, md + 1 ):
              b[i-1,j-1,k-1,l-1] = bx[i-1,j-1,k-1,l-1]

      s = btrix ( js, je, ls, le, kk, jd, kd, ld, md, a, b, c, s )

  tm = clock ( ) - tm
#
#  Results.
#
  er = abs ( ( s[18,18,18,0] - ans ) / ans )
  fp = it * md * ( le - 1 ) * 19165
  rt = 1.0E-06 * fp / tm
#
#  Terminate.
#
  return er, fp, tm, rt

if ( __name__ == '__main__' ):
  import platform
  from timestamp import timestamp
  timestamp ( )
  er, fp, tm, rt = btrix_test ( )
  print ( '' )
  print ( 'BTRIX:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '' )
  print ( ' Program          Error         FP Ops     Seconds      MFLOPS' )
  print ( '' )
  print ( ' BTRIX    %13.4e  %13.4e  %10.4e  %10.2e' % ( er, fp, tm, rt ) )
  print ( '' )
  print ( 'BTRIX:' )
  print ( '  Normal end of execution.' )
  timestamp ( )

