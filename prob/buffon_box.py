#! /usr/bin/env python
#
def buffon_box_pdf ( a, b, l ):

#*****************************************************************************80
#
## BUFFON_BOX_PDF evaluates the Buffon Box PDF.
#
#  Discussion:
#
#    In the Buffon-Laplace needle experiment, we suppose that the plane has been
#    tiled into a grid of rectangles of width A and height B, and that a
#    needle of length L is dropped "at random" onto this grid.  
# 
#    We may assume that one end, the "eye" of the needle falls at the point
#    (X1,Y1), taken uniformly at random in the cell [0,A]x[0,B].
#
#    ANGLE, the angle that the needle makes is taken to be uniformly random.
#    The point of the needle, (X2,Y2), therefore lies at
#
#      (X2,Y2) = ( X1+L*cos(ANGLE), Y1+L*sin(ANGLE) )
#
#    The needle will have crossed at least one grid line if any of the 
#    following are true:
#
#      X2 <= 0, A <= X2, Y2 <= 0, B <= Y2.
#
#    If L is larger than sqrt ( A*A + B*B ), then the needle will
#    cross every time, and the computation is uninteresting.  However, if
#    L is smaller than this limit, then the probability of a crossing on
#    a single trial is
#
#      P(L,A,B) = ( 2 * L * ( A + B ) - L * L ) / ( PI * A * B )
#
#    and therefore, a record of the number of hits for a given number of
#    trials can be used as a very roundabout way of estimating PI.  
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sudarshan Raghunathan,
#    Making a Supercomputer Do What You Want: High Level Tools for 
#    Parallel Programming,
#    Computing in Science and Engineering,
#    Volume 8, Number 5, September/October 2006, pages 70-80.
#
#  Parameters:
#
#    Input, real A, B, the horizontal and vertical dimensions
#    of each cell of the grid.  0 <= A, 0 <= B.
#
#    Input, real L, the length of the needle.
#    0 <= L <= min ( A, B ).
#
#    Output, real PDF, the PDF.
#
  import numpy as np
  from sys import exit

  if ( a < 0.0 ):
    print ( '' )
    print ( 'BUFFON_BOX_PDF - Fatal error!' )
    print ( '  Input A < 0.' )
    exit ( 'BUFFON_BOX_PDF - Fatal error!' )
  elif ( a == 0.0 ):
    pdf = 1.0
    return pdf

  if ( b < 0.0 ):
    print ( '' )
    print ( 'BUFFON_BOX_PDF - Fatal error!' )
    print ( '  Input B < 0.' )
    exit ( 'BUFFON_BOX_PDF - Fatal error!' )
  elif ( b == 0.0 ):
    pdf = 1.0
    return pdf

  if ( l < 0.0 ):
    print ( '' )
    print ( 'BUFFON_BOX_PDF - Fatal error!' )
    print ( '  Input L < 0.' )
    exit ( 'BUFFON_BOX_PDF - Fatal error!' )
  elif ( l == 0.0 ):
    pdf = 0.0
    return pdf
  elif ( min ( a, b ) < l ):
    print ( '' )
    print ( 'BUFFON_BOX_PDF - Fatal error!' )
    print ( '  min ( A, B ) < L.' )
    exit ( 'BUFFON_BOX_PDF - Fatal error!' )
    
  pdf = l * ( 2.0 * ( a + b ) - l ) / ( np.pi * a * b )

  return pdf

def buffon_box_pdf_test ( ):

#*****************************************************************************80
#
## BUFFON_BOX_PDF_TEST tests BUFFON_LAPLACE_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BUFFON_BOX_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BUFFON_BOX_PDF evaluates the Buffon-Laplace PDF,' )
  print ( '  the probability that, on a grid of cells of width A' )
  print ( '  and height B, a needle of length L, dropped at random,' )
  print ( '  will cross at least one grid line.' )
  print ( '' )
  print ( '      A         B         L        PDF' )
  print ( '' )

  for i in range ( 1, 6 ):
    a = float ( i )
    for j in range ( 1, 6 ):
      b = float ( j )
      for k in range ( 0, 6 ):
        l = float ( k ) * min ( a, b ) / 5.0
        pdf = buffon_box_pdf ( a, b, l )
        print ( '  %8.4g  %8.4g  %8.4g  %14g' % ( a, b, l, pdf ) )

      print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'BUFFON_BOX_PDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def buffon_box_sample ( a, b, l, trial_num, seed ):

#*****************************************************************************80
#
## BUFFON_BOX_SAMPLE samples the Buffon Box distribution.
#
#  Discussion:
#
#    In the Buffon-Laplace needle experiment, we suppose that the plane has been
#    tiled into a grid of rectangles of width A and height B, and that a
#    needle of length L is dropped "at random" onto this grid.  
# 
#    We may assume that one end, the "eye" of the needle falls at the point
#    (X1,Y1), taken uniformly at random in the cell [0,A]x[0,B].
#
#    ANGLE, the angle that the needle makes is taken to be uniformly random.
#    The point of the needle, (X2,Y2), therefore lies at
#
#      (X2,Y2) = ( X1+L*cos(ANGLE), Y1+L*sin(ANGLE) )
#
#    The needle will have crossed at least one grid line if any of the 
#    following are true:
#
#      X2 <= 0, A <= X2, Y2 <= 0, B <= Y2.
#
#    This routine simulates the tossing of the needle, and returns the number
#    of times that the needle crossed at least one grid line.
#
#    If L is larger than sqrt ( A*A + B*B ), then the needle will
#    cross every time, and the computation is uninteresting.  However, if
#    L is smaller than this limit, then the probability of a crossing on
#    a single trial is
#
#      P(L,A,B) = ( 2 * L * ( A + B ) - L * L ) / ( PI * A * B )
#
#    and therefore, a record of the number of hits for a given number of
#    trials can be used as a very roundabout way of estimating PI.  
#    (Particularly roundabout, since we actually will use a good value of
#    PI in order to pick the random angles%)
#
#    Note that this routine will try to generate 5 * TRIAL_NUM random
#    double precision values at one time, using automatic arrays.  
#    When I tried this with TRIAL_NUM = 1,000,000, the program failed,
#    because of internal system limits on such arrays.
#
#    Such a problem could be avoided by using a DO loop running through
#    each trial individually, but this tend to run much more slowly than
#    necessary.
# 
#    Since this routine invokes the MATLAB random number generator,
#    the user should initialize the random number generator, particularly
#    if it is desired to control whether the sequence is to be varied
#    or repeated.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sudarshan Raghunathan,
#    Making a Supercomputer Do What You Want: High Level Tools for 
#    Parallel Programming,
#    Computing in Science and Engineering,
#    Volume 8, Number 5, September/October 2006, pages 70-80.
#
#  Parameters:
#
#    Input, real A, B, the horizontal and vertical dimensions
#    of each cell of the grid.  0 <= A, 0 <= B.
#
#    Input, real L, the length of the needle.
#    0 <= L <= min ( A, B ).
#
#    Input, integer TRIAL_NUM, the number of times the needle is
#    to be dropped onto the grid.
#
#    Input/output, integer SEED, a seed for the random number generator.
#
#    Output, integer BUFFON_BOX_SAMPLE, the number of times the needle crossed
#    at least one line of the grid of cells.
#
#  Local Parameters:
#
#    Local, integer BATCH_SIZE, specifies the number of trials to be done
#    in a single batch.  Setting BATCH_SIZE to 1 will be very slow.
#    Replacing it by TRIAL_NUM would be fine except that your system
#    may have a limit on the size of automatic arrays.  We have set a default 
#    value of 10,000 here which should be large enough to be efficient
#    but small enough not to annoy the system.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  batch_size = 10000

  hits = 0

  for i in range ( 0, trial_num ):
#
#  Randomly choose the location of the eye of the needle in [0,0]x[A,B],
#  and the angle the needle makes.
#
    x1, seed = r8_uniform_01 ( seed )
    y1, seed = r8_uniform_01 ( seed )
    angle, seed = r8_uniform_01 ( seed )

    x1 = a * x1
    y1 = b * y1
    angle = 2.0 * np.pi * angle
#
#  Compute the location of the point of the needle.
#
    x2 = x1 + l * np.cos ( angle )
    y2 = y1 + l * np.sin ( angle )
#
#  Count the end locations that lie outside the cell.
#
    if ( x2 <= 0.0 or a <= x2 or y2 <= 0.0 or b <= y2 ):
      hits = hits + 1

  return hits

def buffon_box_sample_test ( ):

#*****************************************************************************80
#
## BUFFON_BOX_SAMPLE_TEST tests BUFFON_SAMPLE_TEST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  trial_num_test = np.array ( [ 10, 100, 10000, 1000000 ] )

  a = 1.0
  b = 1.0
  l = 1.0
  seed = 123456789

  print ( '' )
  print ( 'BUFFON_BOX_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BUFFON_BOX_SAMPLE simulates a Buffon-Laplace needle dropping' )
  print ( '  experiment.  On a grid of cells of width A and height B' )
  print ( '  a needle of length L is dropped at random.  We count' )
  print ( '  the number of times it crosses at least one grid line,' )
  print ( '  and use this to estimate the value of PI.' )

  print ( '' )
  print ( '  Cell width A =    %g' % ( a ) )
  print ( '  Cell height B =   %g' % ( b ) )
  print ( '  Needle length L = %g' % ( l ) )
  print ( '' )
  print ( '    Trials      Hits          Est(Pi)         Err' )
  print ( '' )

  for test in range ( 0, 4 ):

    trial_num = trial_num_test[test]

    hits = buffon_box_sample ( a, b, l, trial_num, seed )

    if ( 0 < hits ):
      pi_est = ( 2.0 * l * ( a + b ) - l * l ) * trial_num  / ( a * b * hits )
    else:
      pi_est = 1.0E+30

    err = abs ( pi_est - np.pi )

    print ( '  %8d  %8d  %14g  %14g' % ( trial_num, hits, pi_est, err ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BUFFON_BOX_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  buffon_box_pdf_test ( )
  buffon_box_sample_test ( )
  timestamp ( )
 
