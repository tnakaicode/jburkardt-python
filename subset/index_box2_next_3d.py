#! /usr/bin/env python
#
def index_box2_next_3d ( n1, n2, n3, ic, jc, kc, i, j, k, more ):

#*****************************************************************************80
#
## INDEX_BOX2_NEXT_3D produces index vectors on the surface of a box in 3D.
#
#  Discussion:
#
#    The box has a central cell of (IC,JC,KC), with a half widths of
#    (N1,N2,N3).  The index vectors are exactly those between
#    (IC-N1,JC-N2,KC-N3) and (IC+N1,JC+N2,KC+N3) with the property that
#    at least one of I, J, and K is an "extreme" value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N1, N2, N3, the "half widths" of the box, that is, the
#    maximum distances from the central cell allowed for I, J and K.
#
#    Input, integer IC, JC, KC, the central cell of the box.
#
#    Input, integer I, J, K.  On input with MORE = TRUE, the previous index set
#    If MORE is FALSE, the input values of I, J and K are not needed.
#
#    Input, logical MORE, is FALSE on an initialization call.  Thereafter,
#    MORE should be TRUE to request the next index set.
#
#    Output, integer I, J, K, the next index set.
#
#    Output, logical MORE, is TRUE until there are no more index sets to return.
#
  if ( not more ):
    more = True
    i = ic - n1
    j = jc - n2
    k = kc - n3
    return i, j, k, more

  if ( i == ic + n1 and j == jc + n2 and k == kc + n3 ):
    more = False
    return i, j, k, more
#
#  Increment K.
#
  k = k + 1
#
#  Check K.
#
  if ( kc + n3 < k ):
    k = kc - n3
    j = j + 1
  elif ( k < kc + n3 and \
    ( i == ic - n1 or i == ic + n1 or j == jc - n2 or j == jc + n2 ) ):
    return i, j, k, more
  else:
    k = kc + n3
    return i, j, k, more
#
#  Check J.
#
  if ( jc + n2 < j ):
    j = jc - n2
    i = i + 1
  elif ( j < jc + n2 and \
    ( i == ic - n1 or i == ic + n1 or k == kc - n3 or k == kc + n3 ) ):
    pass
  else:
    j = jc + n2

  return i, j, k, more

def index_box2_next_3d_test ( ):

#*****************************************************************************80
#
## INDEX_BOX2_NEXT_3D_TEST tests INDEX_BOX2_NEXT_3D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  ic = 10
  jc = 20
  kc = 30
  n1 = 5
  n2 = 3
  n3 = 4

  print ( '' )
  print ( 'INDEX_BOX2_NEXT_3D_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  INDEX_BOX2_NEXT_3D produces IJK indices that' )
  print ( '  lie on the surface of a box.' )
  print ( '' )
  print ( '  The box has half widths:' )
  print ( '  %3d  %3d  %3d' % ( n1, n2, n3 ) )
  print ( '' )
  print ( '  and central cell:' )
  print ( '  %3d  %3d  %3d' % ( ic, jc, kc ) )
  print ( '' )
  print ( '  We will only print a PORTION of the data!' )
  print ( '' )
  print ( '   #    I   J   K' )
  print ( '' )

  i = -1
  j = -1
  k = -1
  more = False

  n = 0

  while ( True ):

    i, j, k, more = index_box2_next_3d ( n1, n2, n3, ic, jc, kc, i, j, k, more )

    if ( not more ):
      break

    n = n + 1
    print ( '  %3d  %3d  %3d  %3d' % ( n, i, j, k ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'INDEX_BOX2_NEXT_3D_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  index_box2_next_3d_test ( )
  timestamp ( )

