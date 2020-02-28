#! /usr/bin/env python
#
def index_box2_next_2d ( n1, n2, ic, jc, i, j, more ):

#*****************************************************************************80
#
## INDEX_BOX2_NEXT_2D produces index vectors on the surface of a box in 2D.
#
#  Discussion:
#
#    The box is has center at (IC,JC), and has half-widths N1 and N2.
#    The index vectors are exactly those which are between (IC-N1,JC-N1) and
#    (IC+N1,JC+N2) with the property that at least one of I and J
#    is an "extreme" value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N1, N2, the half-widths of the box, that is, the
#    maximum distance allowed between (IC,JC) and (I,J).
#
#    Input, integer IC, JC, the central cell of the box.
#
#    Input, integer I, J, the output value of I and J on the previous call.
#    Input values ignored on first call.
#
#    Input, logical MORE, set this to 0 on the first call, and therafter,
#    set it to its output value on the previous call.
#
#    Output, integer I, J, the next index set.
#
#    Output, logical MORE, is FALSE (or 0) if there are no more indices
#    to return, and TRUE otherwise.
#
  if ( not more ):
    more = True
    i = ic - n1
    j = jc - n2
    return i, j, more

  if ( i == ic + n1 and j == jc + n2 ):
    more = False
    return i, j, more
#
#  Increment J.
#
  j = j + 1
#
#  Check J.
#
  if ( jc + n2 < j ):
    j = jc - n2
    i = i + 1
  elif ( j < jc + n2 and ( i == ic - n1 or i == ic + n1 ) ):
    pass
  else:
    j = jc + n2

  return i, j, more

def index_box2_next_2d_test ( ):

#*****************************************************************************80
#
## INDEX_BOX2_NEXT_2D_TEST tests INDEX_BOX2_NEXT_2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  ic = 10
  jc = 20
  n1 = 4
  n2 = 3

  print ( '' )
  print ( 'INDEX_BOX2_NEXT_2D_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  INDEX_BOX2_NEXT_2D produces IJ indices that' )
  print ( '  lie on the surface of a box2 in 2D.' )
  print ( '' )
  print ( '  The box has half-widths:' )
  print ( '  %3d  %3d' % ( n1, n2 ) )
  print ( '' )
  print ( '  and has center cell:' )
  print ( '  %3d  %3d' % ( ic, jc ) )
  print ( '' )
  print ( '   #    I   J' )
  print ( '' )

  i = -1
  j = -1
  more = False
  n = 0

  while ( True ):

    i, j, more = index_box2_next_2d ( n1, n2, ic, jc, i, j, more )

    if ( not more ):
      break

    n = n + 1
    print ( '  %3d  %3d  %3d' % ( n, i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'INDEX_BOX2_NEXT_2D_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  index_box2_next_2d_test ( )
  timestamp ( )

