#! /usr/bin/env python
#
def marriage ( n, prefer, rank ):

#*****************************************************************************80
#
## MARRIAGE finds a stable set of marriages for given preferences.
#
#  Discussion:
#
#    Given a set of N men and N women who must be married in pairs,
#    and information defining the relative rankings that each person
#    assigns to the candidates of the opposite sex, this routine finds
#    a stable set of marriages for them.
#
#    A stable set of marriages is a pairing of the men and women with
#    the stability property: if M1 marries W1 and M2 marries W2, then
#    it is never the case that M1 and W2 would both prefer to be married
#    to each other.
#
#    An important application of stable marriage algorithms occurs in
#    the annual matching of medical residents to hospitals.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Sedgewick,
#    Algorithms in C,
#    Addison-Wesley, 1990,
#    ISBN: 0-201-51425-7,
#    LC: QA76.73.C15S43.
#
#  Parameters:
#
#    Input, integer N, the number of pairs of men and women.
#
#    Input, integer PREFER(N,N) for man I, the value of
#    PREFER(I,J) represents his J-th preference for a wife.
#
#    Input, integer RANK(N,N) for woman I, the value of RANK(I,J)
#    represents her ranking of man number J.  A value of 1 for RANK(I,J)
#    means woman I ranks man J most preferable, while a value of N
#    would mean she ranked him least preferable.
#
#    Output, integer FIANCEE(N) for woman I, FIANCEE(I) is the
#    man to whom she is now engaged.
#
#    Output, integer NEXT(N) for man I, NEXT(I) is his preference
#    ranking for the woman to whom he is now engaged.  A value of 1 represents
#    his first choice, a value of N his last.
#
  import numpy as np
#
#  For man I, NEXT(I) is the woman I has most recently proposed to,
#  and hence NEXT(I)+1 is the next one to try.
#
  next = np.zeros ( n, dtype = np.int32 )
#
#  For woman I, FIANCEE(I) is the man she has agree to marry,
#  or 0 if she has not agreed to any man yet.
#
  fiancee = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    fiancee[i] = -1
#
#  Start with an unengaged man, and end with an engaged woman.
#
  for i in range ( 0, n ):

    m = i

    while ( True ):

      next[m] = next[m] + 1

      w = prefer[m,next[m]-1] - 1

      if ( fiancee[w] == -1 ):
        fiancee[w] = m
        break

      if ( rank[w,m] < rank[w,fiancee[w]] ):
        temp       = fiancee[w]
        fiancee[w] = m
        m          = temp

  return fiancee, next

def marriage_test ( ):

#*****************************************************************************80
#
## MARRIAGE_TEST tests MARRIAGE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
#
#  PREFER(M,W) is the index of women W on man M's list.
#
  prefer = np.array ( [ \
    [ 2, 5, 1, 3, 4 ], \
    [ 1, 2, 3, 4, 5 ], \
    [ 2, 3, 5, 4, 1 ], \
    [ 1, 3, 2, 4, 5 ], \
    [ 5, 3, 2, 1, 4 ] ], dtype = np.int32 )
#
#  RANK(W,M) is the index of man M on woman W's list.
#
  rank = np.array ( [ \
    [ 2, 4, 5, 3, 1 ], \
    [ 4, 3, 5, 1, 2 ], \
    [ 1, 3, 4, 2, 5 ], \
    [ 4, 2, 1, 3, 5 ], \
    [ 5, 2, 3, 1, 4 ] ], dtype = np.int32 )

  print ( '' )
  print ( 'MARRIAGE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MARRIAGE arranges a set of stable marriages' )
  print ( '  given a set of preferences.' )

  fiancee, next = marriage ( n, prefer, rank )

  print ( '' )
  print ( '  Man, Wife\'s rank, Wife' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %6d  %6d' % ( i + 1, next[i], prefer[i,next[i]-1] ) )

  print ( '' )
  print ( '  Woman, Husband\'s rank, Husband' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %6d  %6d' % ( i + 1, rank[i,fiancee[i]], fiancee[i]+1 ) )

  print ( '' )
  print ( '  Correct result:' )
  print ( '' )
  print ( '  M:W 1  2  3  4  5' )
  print ( '   1  +  .  .  .  .' )
  print ( '   2  .  .  .  +  .' )
  print ( '   3  .  .  .  .  +' )
  print ( '   4  .  .  +  .  .' )
  print ( '   5  .  +  .  .  .' )
#
#  Terminate.
#
  print ( '' )
  print ( 'MARRIAGE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  marriage_test ( )
  timestamp ( )
 
