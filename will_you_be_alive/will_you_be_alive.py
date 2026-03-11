#! /usr/bin/env python3
#
def will_you_be_alive_test ( ):

#*****************************************************************************80
#
## will_you_be_alive_test() tests will_you_be_alive().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#   John Burkardt
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
# 
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'will_you_be_alive_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test will_you_be_alive().' )

  rng = default_rng ( )

  airplane_seat_test ( rng )
  before_test ( rng )
  bernoulli_dice_test ( rng )
  bingo_test ( )
  black_test ( rng )
  chain_test ( )
  double_dart_test ( rng )
  double_six_test ( rng )
  final_test ( rng )
  flips_test ( rng )
  galileo_test ( )
  gamblers_ruin_test ( rng )
  golf_test ( rng )
  inside_test ( rng )
  liar_test ( rng )
  long_test ( rng )
  marks_test ( rng )
  newton_test ( rng )
  obtuse1_test ( rng )
  obtuse2_test ( rng )
  ping_pong_test ( )
  plums_test ( rng )
  ratio1_test ( rng )
  ratio2_test ( rng )
  spaghetti_test ( )
  square_adjacent_test ( rng )
  square_inside_test ( rng )
  square_opposite_test ( rng )
  squash_test ( )
  steve2_test ( rng )
  ten_years_test ( )
  top_test ( rng )
  twins_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'will_you_be_alive_test():' )
  print ( '  Normal end of execution.' )

  return

def airplane_seat ( trial_num, n, rng ):

#*****************************************************************************80
#
## airplane_seat() simulates the airplane seat problem.
#
#  Discussion:
#
#    Airline passengers 1 through N are assigned seats 1 through N.
#    But passenger 1 is clueless, and chooses a seat randomly.
#    The remaining passengers board in order, choosing their assigned seat
#    if possible, otherwise taking an empty seat at random.
#    What is the probability that the last passenger, N, will be able to 
#    sit in the correct assigned seat N?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    integer trial_num: the number of simulations.
#
#    integer N, the number of passengers.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real PROB: the probability that the last passenger will be 
#    properly seated.
#
  import numpy as np

  prob = 0.0

  for trial in range ( 0, trial_num ):

    occupant = -1 * np.ones ( n )
#
#  Passenger 0 chooses a seat at random.
#
    passenger = 0
    seat = rng.integers ( low = 0, high = n, endpoint = False )

    occupant[seat] = passenger
#
#  Passenger I will choose seat I if it is available,
#  otherwise a random available seat.
#
    for passenger in range ( 1, n ):

      seat = passenger
      while ( occupant[seat] != -1 ):
        seat = rng.integers ( low = 0, high = n, endpoint = False )

      occupant[seat] = passenger
#
#  Did the last passenger sit in the last seat?
#
    if ( occupant[n-1] == n - 1 ):
      prob = prob + 1

  prob = prob / trial_num

  return prob

def airplane_seat_test ( rng ):

#*****************************************************************************80
#
## airplane_seat_test() tests airplane_seat().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'airplane_seat_test():' )
  print ( '  Airline passengers 1 to N are assigned seats 1 to N.' )
  print ( '  The first passenger to board, #1, is clueless, ' )
  print ( '  and chooses a seat randomly.' )
  print ( '  The remaining passengers board in order, choosing their' )
  print ( '  assigned seat if possible, otherwise taking an empty' )
  print ( '  seat at random.' )
  print ( '' )
  print ( '  What is the probability that the last passenger, N, ' )
  print ( '  will be able to sit in the correct assigned seat N?' )

  trial_num = 100000
  n = 100

  prob = airplane_seat ( trial_num, n, rng )

  print ( '' )
  print ( '  Number of seats available =', n )
  print ( '  Number of simulations =', trial_num )
  print ( '  Estimated probability   = ', prob )
  print ( '  Theoretical probability = 0.5' )

  return

def before ( trial_num, bias, rng ):

#*****************************************************************************80
#
## before() analyzes the second Newton gambling problem.
#
#  Discussion:
#
#    What is the probability of getting 4 heads before 7 tails?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    integer trial_num: the number of simulations.
#
#    real bias, the probability of heads on a single toss.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real prob, the probability of getting 4 heads before 7 tails,
#    for which the exact value is:
#    0.733962, if bias = 0.45
#    0.828125, if bias = 0.50
#
  total = 0

  for loop in range ( 0, trial_num ):

    H = 0
    T = 0

    while ( H < 4 and T < 7 ):
      if ( rng.random ( ) < bias ):
        H = H + 1
      else:
        T = T + 1

    if ( H == 4 ):
      total = total + 1

  prob = total / trial_num

  return prob

def before_test ( rng ):

#*****************************************************************************80
#
## before_test() tests before().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'before_test():' )
  print ( '  before() estimates the probability that a person,' )
  print ( '  flipping a biased coin repeatedly, will reach 4 heads' )
  print ( '  before reaching 7 tails.' )
  print ( '' )
  print ( '  bias     p(4H before 7T)' )
  print ( '' )

  trial_num = 100000

  for i in range ( 0, 105, 5 ):
    bias = i / 100
    prob = before ( trial_num, bias, rng )
    print ( '  %g  %g' % ( bias, prob ) )

  return

def bernoulli_dice ( rng ):

#*****************************************************************************80
#
## bernoulli_dice() simulates a Bernoulli dice problem.
#
#  Discussion:
#
#    This program models a two-player game.  Players A and B take turns
#    tossing a fair die.  The first to throw a 1 wins.  On the first
#    round, A gets 1 toss, then B gets 1 toss, on the second A gets 2
#    tosses, then B gets 2 tosses and so on.  
#
#    What is the probability that A will win?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#    James Bernoulii,
#    Acta Eruditorum,
#    1690.
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real prob, the probability that player A will win.
#
  w = 0
  p = 1.0 / 6.0
  trial_num = 100000

  for loop in range ( 0, trial_num ):
    
    a = 0
    b = 0
    turn = 1
    keepgoing = True

    while ( keepgoing ):

      for loopa in range ( 0, turn ):
        if ( rng.random ( ) < p ):
          a = 1

      for loopa in range ( 0, turn ):
        if ( rng.random ( ) < p ):
          b = 1

      if ( a == 0 ):
        if ( b == 0 ):
          turn = turn + 1
        else:
          keepgoing = False
      else:
        w = w + 1
        keepgoing = False

  prob = w / trial_num

  return prob

def bernoulli_dice_test ( rng ):

#*****************************************************************************80
#
## bernoulli_dice_test() tests bernoulli_dice().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'bernoulli_dice_test():' )
  print ( '  bernoulli_dice() considers the Bernoulli dice game.' )
  print ( '  Players A and B toss a fair die, until a 1 is rolled.' )
  print ( '  On round 1, A gets 1 toss, then B gets 1 toss.' )
  print ( '  On round k, A gets k tosses, then B gets k tosses.' )
  print ( '  What is the probability that A wins?' )

  p = bernoulli_dice ( rng )
  exact = 0.596794

  print ( '' )
  print ( '  Estimate = ', p )
  print ( '  Exact =    ', exact )

  return

def bingo ( A, B ):

#*****************************************************************************80
#
## bingo() analyzes a nontransitive set of bingo cards.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    integer A[2,2], B[2,2]: the bingo cards for players X and Y.
#
#  Output:
#
#    xwins, ywins, ties: the number of times X wins, Y wins, or there is a tie.
#
  import itertools
#
#  Consider all 720 permutations of the integers 1 through 6.
#
  xwin = 0
  ywin = 0
  ties = 0

  for perm in itertools.permutations ( [ 1, 2, 3, 4, 5, 6 ] ):

    X = A.copy()
    Y = B.copy()

    keepplaying = True
    i = 0
    xbingo = 0
    ybingo = 0

    while ( keepplaying ):

      n = perm[i]

      for j in range ( 0, 2 ):
        for k in range ( 0, 2 ):
          if ( X[j,k] == n ):
            X[j,k] = 0
          if ( Y[j,k] == n ):
            Y[j,k] = 0

      if ( X[0,0] + X[0,1] == 0 ):
        xbingo = True
      elif ( X[1,0] + X[1,1] == 0 ):
        xbingo = True

      if ( Y[0,0] + Y[0,1] == 0 ):
        ybingo = True
      elif ( Y[1,0] + Y[1,1] == 0 ):
        ybingo = True

      if ( xbingo and ybingo ):
        ties = ties + 1
        keepplaying = False
      elif ( xbingo and not ybingo ):
        xwin = xwin + 1
        keepplaying = False
      elif ( not xbingo and ybingo ):
        ywin = ywin + 1
        keepplaying = False

      i = i + 1

  return xwin, ywin, ties

def bingo_test ( ):

#*****************************************************************************80
#
## bingo_test() tests bingo().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'bingo_test():' )
  print ( '  bingo(A,B) simulates a simplified game of bingo.' )
  print ( '  The bingo card is just a 2x2 array.' )
  print ( '  Player X gets card A, and player Y gets card B.' )
  print ( '  Many random games are played, and the results are reported.' )
  print ( '  There are four possible bingo cards, C1, C2, C3, C4.' )
  print ( '  It turns out to be a nontransitive system, in which every' )
  print ( '  card will beat one of the others, and lose to another.' )

  A = np.array ( [ [ 1, 2 ], [ 3, 4 ] ] )
  B = np.array ( [ [ 2, 4 ], [ 5, 6 ] ] )
  C = np.array ( [ [ 1, 3 ], [ 4, 5 ] ] )
  D = np.array ( [ [ 1, 5 ], [ 2, 6 ] ] )

  card = np.array ( [ A, B, C, D ] )

  name = 'ABCD'

  print ( '' )
  print ( '  The four bingo cards:' )
  print ( card )

  for k1 in range ( 0, 4 ):
    for k2 in range ( 0, 4 ):
      xwin, ywin, ties = bingo ( card[k1], card[k2] )
      print ( '  %s  %s  %d, %d, %d' % ( name[k1], name[k2], xwin, ywin, ties ) )

  return

def black ( b_init, w_init, rng ):

#*****************************************************************************80
#
## black() estimates the probability that the last ball drawn is black.
#
#  Discussion:
#
#    A bag of black and white marbles is to be emptied in a series of rounds.
#
#    A round begins when a single ball is drawn from the bag, its color is 
#    noted, and the ball is discarded.  Then, one at a time, more balls are 
#    drawn from the bag.  If they match the first ball, then they are also 
#    discarded.  Otherwise, they are replaced in the bag, and this round stops.
#
#    Rounds are taken until the bag is empty.
#
#    This function simulates the process of a single round.
#
#    It is desired to estimate the probability that the last marble in 
#    the bag is black.  It turns out this probability is 1/2.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    integer b_init, w_init: the initial number of black and white
#    balls  Typical values are b_init = 15, w_init = 39
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real p, the probability that the last ball is black.
#
  total = 0.0
  trial_num = 10000

  for loop in range ( 0, trial_num ):

    b = b_init
    w = w_init

    while ( 0 < b + w ):

      blackball, whiteball = draw ( b, w, rng )
      b = blackball
      w = whiteball

      if ( b == 0 ):
        w = 0
      elif ( w == 0 ):
        total = total + 1
        b = 0

  p = total / trial_num

  return p

def black_test ( rng ):

#*****************************************************************************80
#
## black_test() tests black() and draw().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'black_test():' )
  print ( '  A bag of B black and W white marbles is to be emptied in a ' )
  print ( '  series of rounds.' )
  print ( '' )
  print ( '  A round begins when a single ball is drawn from the bag, ' )
  print ( '  its color is noted, and the ball is discarded.  Then,' )
  print ( '  one at a time, more balls are drawn from the bag.  If ' )
  print ( '  they match the first ball, they are also discarded.  ' )
  print ( '  Otherwise, they are replaced in the bag, and the ' )
  print ( '  round stops.' )
  print ( '' )
  print ( '  Rounds are taken until the bag is empty.' )
  print ( '' )
  print ( '  This function simulates the process of a single round.' )
  print ( '' )
  print ( '  Estimate the probability P that the last marble in ' )
  print ( '  the bag is black.  It turns out P=1/2.' )

  print ( '' )
  print ( '   B   W   P' )
  print ( '' )

  for b, w in ( [ 1, 1], [ 1, 10 ], [ 2, 3 ], [ 3, 3 ], [ 5, 4 ], \
    [ 7, 9 ], [ 18, 13], [ 15, 39] ):
    p = black ( b, w, rng )
    print ( '  %2d  %2d  %g' % ( b, w, p ) )

  return

def chain ( c, p ):

#*****************************************************************************80
#
## chain() plots the probability that a chain letter will terminate.
#
#  Discussion:
#
#    A chain letter asks the recipient to make C copies and send them on.
#    Suppose each recipient complies, with probability p.  What is the
#    likelihood that the chain letter will eventually terminate?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    real c: the number of copies that each recipient is asked to make.
#
#    real p: the probability that a recipient will NOT make c copies and 
#    send them on.
#
#  Output:
#
#    real term: the probability that this chain of letters will terminate.
#
  from scipy.optimize import fsolve

  term0 = 0.5

  term = fsolve ( \
    lambda term: term - p - ( 1.0 - p ) * term**c, term0 )

  return term[0]

def chain_test ( ):

#*****************************************************************************80
#
## chain_test() tests chain().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chain_test():' )
  print ( '  chain() estimates the extinction probability of a chain letter.' )
  print ( '  A chain letter asks the recipient to make C copies' )
  print ( '  and send them on.  Suppose that, with probability P,' )
  print ( '  any recipient ignores the request, and with probability' )
  print ( '  any recipient complies with it.' )
  print ( '  Estimate the probability E that the chain' )
  print ( '  letter will terminate.' )
  print ( '' )
  print ( '  Need to solve E = p + ( 1 - p ) * E^c )' )
  print ( '' )
  print ( '  C    P    E' )

  for c in range ( 1, 6 ):
    print ( '' )
    for i in range ( 1, 11, 2 ):
      p = i / 10
      e = chain ( c, p )
      print ( '  %d  %g  %g' % ( c, p, e ) )

  return

def draw ( b, w, rng ):

#*****************************************************************************80
#
## draw() simulates drawing balls from a set of black and white balls.
#
#  Discussion:
#
#    A bag of black and white marbles is to be emptied in a series of rounds.
#
#    A round begins when a single ball is drawn from the bag, its color is 
#    noted, and the ball is discarded.  Then, one at a time, more balls are 
#    drawn from the bag.  If they match the first ball, then they are also 
#    discarded.  Otherwise, they are replaced in the bag, and this round stops.
#
#    Rounds are taken until the bag is empty.
#
#    This function simulates the process of a single round.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    integer b, w, the number of black and white balls at the
#    beginning of the round.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer blackball, whiteball, the number of black and
#    white balls at the end of the round.
#
  if ( rng.random ( ) < b / ( w + b ) ):
    fcolor = 1
    b = b - 1
  else:
    fcolor = 0
    w = w - 1

  keepgoing = True
  while ( keepgoing ):

    if ( fcolor == 1 ):

      if ( rng.random ( ) < b / ( w + b ) ):
        b = b - 1
        if ( b == 0 ):
          keepgoing = False
      else:
        keepgoing = False

    else:

      if ( rng.random ( ) < w / ( w + b ) ):
        w = w - 1
        if ( w == 0 ):
          keepgoing = False
      else:
        keepgoing = False

  blackball = b
  whiteball = w

  return blackball, whiteball

def double_dart ( rng ):

#*****************************************************************************80
#
## double_dart() analyzes the double dart problem.
#
#  Discussion:
#
#    If two darts land inside the unit circle, what is the probability
#    that they will be at least 1 unit apart?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real prob, the probability that two darts, landing inside
#    the unit circle, will be at least 1 unit apart.
#
  hits = 0
  total = 0
  trial_num = 100000

  while ( hits < trial_num ):

    x1 = -1.0 + 2.0 * rng.random ( )
    y1 = -1.0 + 2.0 * rng.random ( )
    d1 = x1**2 + y1**2

    x2 = -1.0 + 2.0 * rng.random ( )
    y2 = -1.0 + 2.0 * rng.random ( )
    d2 = x2**2 + y2**2

    if ( d1 < 1.0 and d2 < 1.0 ):
      hits = hits + 1
      s = ( x1 - x2 )**2 + ( y1 - y2 )**2
      if ( 1.0 < s ):
        total = total + 1

  prob = total / hits

  return prob

def double_dart_test ( rng ):

#*****************************************************************************80
#
## double_dart_test() tests double_dart().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'double_dart_test():' )
  print ( '  double_dart() considers the double dart problem.' )
  print ( '  If two darts land randomly in the unit circle,' )
  print ( '  what is the probability that they are at least 1 unit apart?' )

  prob = double_dart ( rng )

  exact = 3.0 * np.sqrt ( 3.0 ) / 4.0 / np.pi

  print ( '' )
  print ( '  Estimate = ', prob )
  print ( '  Exact =    ', exact )

  return

def double_six ( rng ):

#*****************************************************************************80
#
## double_six() analyzes the Newton double six dice problem.
#
#  Discussion:
#
#    If we toss a fair die repeatedly, how many tosses will we expect to make
#    until we encounter two consecutive 6's?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real P, the expected number of tosses until two 6's appear consecutively.
#
  import numpy as np

  trial_num = 100000
  person = np.zeros ( trial_num )

  check = 1.0 / 6.0

  for loop in range ( 0, trial_num ):

    toss = 1
    flip2 = 0
    keeptossing = True

    while ( keeptossing ):

      result = rng.random ( )
      if ( result < check ):
        flip1 = 1
      else:
        flip1 = 0

      if ( flip1 + flip2 == 2 ):
        keeptossing = False
        person[loop] = toss
      else:
        toss = toss + 1
        flip2 = flip1

  p = np.sum ( person ) / trial_num

  return p

def double_six_test ( rng ):

#*****************************************************************************80
#
## double_six_test() tests double_six().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'double_six_test():' )
  print ( '  double_six() considers Newton\'s double six dice problem.' )
  print ( '  What is the expected number of times you must roll a fair die' )
  print ( '  in order to observe two consecutive values of six?' )

  p = double_six ( rng )
  p2 = 1.0 / 6.0
  exact = 1.0 / p2**2 + 1.0 / p2

  print ( '' )
  print ( '  Estimate = ', p )
  print ( '  Exact =    ', exact )

  return

def final ( rng ):

#*****************************************************************************80
#
## final() considers ( A^2/3 + B^2/3 <? 1 ) for random A and B.
#
#  Discussion:
#
#    For A and B uniform random in [-1,+1], what is the probability that
#      A^2/3 + B^2/3 < 1?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real S: the estimated probability.
#
  trial_num = 100000

  s = 0
  
  for loop in range ( 0, trial_num ):

    A = ( - 1 + 2.0 * rng.random ( ) )
    B = ( - 1 + 2.0 * rng.random ( ) )
    A = ( A**2 ) ** ( 1/3 )
    B = ( B**2 ) ** ( 1/3 )
 
    if ( A + B  < 1 ):
      s = s + 1

  s = s / trial_num;

  return s

def final_test ( rng ):

#*****************************************************************************80
#
## final_test() tests final().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'final_test():' )
  print ( '  final() estimates the probability, for random A and B' )
  print ( '  that:' )
  print ( '    A^2/3 + B^2/3 < 1' )

  s = final ( rng )
  print ( '' )
  print ( '  Estimated probability = ', s )
  print ( '  Exact probability     = ', 3 * np.pi / 32 )

  return

def flips ( n, p, rng ):

#*****************************************************************************80
#
## flips() estimates chances of an even number of heads in N coin flips.
#
#  Discussion:
#
#    A biased coin has probability P of heads.
#    The coin is tossed N times.
#    What is the probability of an even number of heads?
#
#  Examples:
#
#    N    P   Exact
#
#    9  0.1  0.5671
#    9  0.9  0.4329
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    integer N, the number of flips.
#
#    real P, the probability of heads on one toss.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real EVEN: the probability of an even number of heads.
#
  import numpy as np

  trial_num = 100000

  even = 0

  for loop1 in range ( 0, trial_num ):

    total = 0
    for loop2 in range ( 0, n ):
      result = rng.random ( )
      if ( result < p ):
        total = total + 1

    if ( ( total % 2 ) == 0 ):
      even = even + 1

  even = even / trial_num

  return even

def flips_test ( rng ):

#*****************************************************************************80
#
## flips_test() tests flips().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'flips_test():' )
  print ( '  flips() estimates EVEN, the probability of an even number of heads' )
  print ( '  after N tosses of a biased coin, whose probability of heads' )
  print ( '  on a single toss is P.' )
  print ( '' )
  print ( '    N     P     EVEN' )
  print ( '' )

  n_test = np.array ( [ 9, 9 ] )
  p_test = np.array ( [ 0.1, 0.99 ] )

  for i in range ( 0, 2 ):
    n = n_test[i]
    p = p_test[i]
    even = flips ( n, p, rng )
    print ( '  %d  %g  %g' % ( n, p, even ) )

  return

def galileo ( ):

#*****************************************************************************80
#
## galileo() computes the frequency of various sums of three dice.
#
#  Discussion:
#
#    If three dice are thrown, the sum will be between 3 and 18.
#    How many ways are there to make each sum?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Output:
#
#    real TOTAL(19): the number of ways of making a sum between 0 and 18.
#
  import numpy as np

  total = np.zeros ( 19 )

  for i in range ( 1, 7 ):
    for j in range ( 1, 7 ):
      for k in range ( 1, 7 ):
        s = i + j + k
        total[s] = total[s] + 1

  return total

def galileo_test ( ):

#*****************************************************************************80
#
## galileo_test() tests galileo().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'galileo_test():' )
  print ( '  galileo() reports the number of ways to make each sum' )
  print ( '  from 0 to 18, when three dice are rolled.' )

  total = galileo ( )
  n = np.sum ( total )

  print ( '' )
  print ( '  Total  Number of ways   Probability' )
  print ( '' )
  for s in range ( 0, 19 ):
    print ( '     %2d     %2d  %g' % ( s, total[s], total[s] / n ) )

  return

def gamblers_ruin ( a, b, p, rng ):

#*****************************************************************************80
#
## gamblers_ruin() simulates the Gambler's Ruin process.
#
#  Discussion:
#
#    Players A and B repeatedly play a game against each other.
#    On each game, player A has a probability P of winning.
#    After each game, the winner gets 1 dollar from the loser.
#    The players begin with A nd B dollars, respectively.
#    They play until one is bankrupt.
#    How long will it take for one player to go bankrupt?
#    What is the probability that A is ruined?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    real A, B: the initial dollars for players A and B.
#
#    real P: the probability that A will win any one game.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real AR: the probability that A will be ruined.
#
#    integer LS: the average number of games played before one player is ruined.
#
  LS = 0
  AR = 0.0
  trial_num = 100000

  for loop in range ( 0, trial_num ):

    A = a
    B = b
    X = 0

    while ( 0 < A and 0 < B ):

      if ( rng.random ( ) < p ):
        A = A + 1
        B = B - 1
      else:
        A = A - 1
        B = B + 1
      X = X + 1

    LS = LS + X
    if ( A == 0 ):
      AR = AR + 1

  LS = LS / trial_num
  AR = AR / trial_num

  return AR, LS

def gamblers_ruin_test ( rng ):

#*****************************************************************************80
#
## gamblers_ruin_test() tests gamblers_ruin().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'gamblers_ruin_test():' )
  print ( '  gamblers_ruin() considers the gambler''s ruin problem.' )
  print ( '  Players A and B repeatedly play a game against each other.' )
  print ( '  On each game, player A has a probability P of winning.' )
  print ( '  After each game, the winner gets 1 dollar from the loser.' )
  print ( '  The players begin with A and B dollars, respectively.' )
  print ( '  They play until one is bankrupt.' )
  print ( '  How long will it take for one player to go bankrupt?' )
  print ( '  What is the probability that A is ruined?' )
  print ( '' )
  print ( '  A  B  P  Prob(ruin)  AverageGames' )
  print ( '' )

  a_test = np.array ( [ 9, 90, 9, 99 ] )
  b_test = np.array ( [ 1, 10, 1,  1 ] )
  p_test = np.array ( [ 0.50, 0.50, 0.45, 0.40 ] )

  for i in range ( 0, 4 ):
    a = a_test[i]
    b = b_test[i]
    p = p_test[i]
    AR, LS = gamblers_ruin ( a, b, p, rng )
    print ( '  %2d  %2d  %g  %g  %g' % ( a, b, p, AR, LS ) )
 
  return

def golf ( rng ):

#*****************************************************************************80
#
## golf() estimates probability golf ball nearer to center than side of square.
#
#  Discussion:
#
#    Estimate the probability that a golf ball, hit into the unit square,
#    is closer to the center of the unit square than to any side.
#
#    For a geometric solution, it is important to know that the curve
#    of equal distance between a point and a line is a parabola.  Disect
#    the square into 4 triangles with the origin at the apex, and focus
#    on one triangle.  Determine the equation of the parabola.  Work out
#    the area of the piece of the triangle that is above the parabola.
#    Your answer will follow.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real p, the probability a golf ball randomly landing in the
#    unit square is nearer the center than to any side.
#    Exact value is (4*sqrt(2)-5)/3 = 0.2189514...
#
  import numpy as np

  total = 0
  trial_num = 100000

  for loop in range ( 0, trial_num ):

    x = rng.random ( )
    y = rng.random ( )
    V = np.array ( [ x, 1.0 - x, y, 1.0 - y ] )
    dedge = np.min ( V )
    dcenter = np.sqrt ( ( x - 0.5 )**2 + ( y - 0.5 )**2 )
    if ( dcenter < dedge ):
      total = total + 1

  p = total / trial_num

  return p

def golf_test ( rng ):

#*****************************************************************************80
#
## golf_test() tests golf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'golf_test():' )
  print ( '  golf() estimates the probability that a golf ball,' )
  print ( '  randomly landing in the unit square, will be' )
  print ( '  closer to the center than to any edge.' )

  p = golf ( rng )
  exact = ( 4.0 * np.sqrt ( 2.0 ) - 5.0 ) / 3.0

  print ( '' )
  print ( '  Estimate = ', p )
  print ( '  Exact    = ', exact )

  return

def inside ( rng ):

#*****************************************************************************80
#
## inside() analyzes the origin in the random triangle in the circle problem.
#
#  Discussion:
#
#    Pick three points on the unit circle and create a triangle.
#    What is the probability that the origin is inside the triangle?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
# 
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real prob, the probability that the origin is inside the triangle.
#
  import numpy as np

  total = 0
#
#  We are free to designate the first "random" point as (1,0).
#
  x1 = 1.0
  y1 = 0.0

  trial_num = 100000

  for loop in range ( 0, trial_num ):

    alpha = 2.0 * np.pi * rng.random ( )
    x2 = np.cos ( alpha )
    y2 = np.sin ( alpha )

    betta = 2.0 * np.pi * rng.random ( )
    x3 = np.cos ( betta )
    y3 = np.sin ( betta )
#
#  Line from P1 to P2, compare P3 and Z.
#
    m = ( y2 - y1 ) / ( x2 - x1 )
    b = y1 - m * x1
    check1 = y3 - ( m * x3 + b )
    check2 = - b
#
#  Line from P2 to P3, compare P1 and Z.
#
    m = ( y3 - y2 ) / ( x3 - x2 )
    b = y2 - m * x2
    check5 = y1 - ( m * x1 + b )
    check6 = - b
#
#  Line from P3 to P1, compare P2 and Z.
#
    m = ( y1 - y3 ) / ( x1 - x3 )
    b = y3 - m * x3
    check3 = y2 - ( m * x2 + b )
    check4 = - b

    p1 = check1 * check2
    p2 = check3 * check4
    p3 = check5 * check6

    if ( 0.0 < p1 and 0.0 < p2 and 0.0 < p3 ):
      total = total + 1

  prob = total / trial_num

  return prob

def inside_test ( rng ):

#*****************************************************************************80
#
## inside_test() tests inside().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'inside_test():' )
  print ( '  inside() estimates the probability that, choosing three' )
  print ( '  points at random on the unit circle, the origin will be' )
  print ( '  inside the resulting triangle?' )

  p = inside ( rng )
  exact = 0.25

  print ( '' )
  print ( '  Estimate = ', p )
  print ( '  Exact    = ', exact )

  return

def liar ( n, p1, rng ):

#*****************************************************************************80
#
## liar() analyzes the liar problem.
#
#  Discussion:
#
#    A chain of N ocassional liars is created.
#
#    With probability p, each person repeats correctly the statement
#    they just heard or with probability 1-p, repeats the negation
#    of the statement.
#
#    Suppose a true statement is given to the first person, who
#    passes it on or, if lying, passes on its opposite, to the next.
#    What is the probability that a true statement will emerge as a
#    true statement at the end of the chain?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    integer n, the number of people in the chain.
#
#    real p1, the probability that a given person will pass on
#    the statement they have just heard, instead of its negative.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real p2, the probability that an initial true statement will
#    emerge as a true statement at the end of the chain.
#
  trial_num = 100000
  total = 0.0

  for game in range ( 0, trial_num ):

    lies = 0
    for k in range ( 0, n ):
      if ( p1 < rng.random ( ) ):
        lies = lies + 1

    if ( ( lies % 2 ) == 0 ):
      total = total + 1

  p2 = total / trial_num

  return p2

def liar_test ( rng ):

#*****************************************************************************80
#
## liar_test() tests liar().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'liar_test():' )
  print ( '  liar() estimates the probability PROB that a true statement,' )
  print ( '  passed sequentially along a chain of N people,' )
  print ( '  will reach the end of the chain as a true statement,' )
  print ( '  given that, with probability P, each person repeats' )
  print ( '  the statement they just hear, or with probability 1-P,' )
  print ( '  repeats the opposite of the statement.' )

  n_test = np.array ( [ 1, 2, 3, 41, 42, 1, 2, 3, 41, 42 ] )
  p_test = np.array ( [ 0.99, 0.99, 0.99, 0.99, 0.99, 0.01, 0.01, 0.01, 0.01, 0.01 ] )

  print ( '' )
  print ( '  N  P  PROB' )
  print ( '' )
  for i in range ( 0, 10 ):
    n = n_test[i]
    p = p_test[i]
    prob = liar ( n, p, rng )
    print ( '  %d  %g  %g' % ( n, p, prob ) )

  return

def long ( rng ):

#*****************************************************************************80
#
## long() analyzes a stick breaking problem.
#
#  Discussion:
#
#    A stick of unit length is randomly broken into two pieces.
#
#    Then the longer of the two pieces is randomly broken again.
#
#    What is the probability that these three pieces form a triangle?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real prob, the probability that a triangle is formed.
#
  total = 0
  trial_num = 100000

  for loop in range ( 0, trial_num ):

    x = rng.random ( )
    y = 1.0 - x
    big = max ( x, y )
    s = min ( x, y )

    v = big * rng.random ( )
    u = big - v

    m = min ( u, v )
    l = max ( u, v )
#
#  Check triangle inequality.
#
    if ( l < s + m and m < s + l and s < m + l ):
      total = total + 1

  prob = total / trial_num

  return prob

def long_test ( rng ):

#*****************************************************************************80
#
## long_test() tests long().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'long_test():' )
  print ( '  long() estimates the probability that a triangle will be' )
  print ( '  after a stick of unit length is randomly broken in two,' )
  print ( '  and then the longer piece is randomly broken again.' )

  p = long ( rng )
  exact = 2.0 * np.log ( 2.0 ) - 1.0

  print ( '' )
  print ( '  Estimate = ', p )
  print ( '  Exact    = ', exact )

  return

def marks ( n, rng ):

#*****************************************************************************80
#
## marks() analyzes the marks problem.
#
#  Discussion:
#
#    Suppose we break each of N sticks randomly into 2 parts, a long part 
#    and a short part.  Then we create N new sticks by randomly selecting
#    (without replacement) pairs of parts.
#
#    What is the probability that every new stick consists of a long part
#    and a short part?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    integer N, the number of strands of spaghetti.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real P: the estimated probability.  The exact value is 2/(N+1).
#
  import numpy as np

  trial_num = 100000

  same = 0

  for trials in range ( 0, trial_num ):

    cut = rng.random ( n )
    cut[0] = 1.0
    cut = np.sort ( cut )

    y = rng.random ( 2 )
    look = True
    k = 0

    while ( look ):

      if ( cut[k] < y[0] ):
        k = k + 1
      else:
        remember = k
        look = False

    if ( remember == 0 ):
      if ( y[1] < cut[remember] ):
        same = same + 1
    else:
      if ( y[1] < cut[remember] and cut[remember-1] < y[1] ):
        same = same + 1

  p = same / trial_num

  return p

def marks_test ( rng ):

#*****************************************************************************80
#
## marks_test() tests marks().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'marks_test():' )
  print ( '  marks() considers a problem in which N sticks are' )
  print ( '  each broken into a long and short piece.' )
  print ( '  Pairs of the 2*N pieces are then randomly combined' )
  print ( '  to form N new sticks.  What is PROB, the probability' )
  print ( '  that every new stick will be formed from a long and' )
  print ( '  a short piece?' )
  print ( '' )
  print ( '    N    Prob  Exact' )
  print ( '' )
  for n in range ( 1, 11 ):
    p = marks ( n, rng )
    print ( '  %2d  %g  %g' % ( n, p, 2.0 / ( n + 1 ) ) )

  return

def newton ( rng ):

#*****************************************************************************80
#
## newton() simulates Newton's dice problem.
#
#  Discussion:
#
#    Estimate the probability that
#    A: a fair die rolled 6 times will show 6 at least once
#    B: a fair die rolled 12 times will show 6 at least twice
#    C: a fair die rolled 18 times will show 6 at least 3 times.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real a, b, c: the probabilities of cases A, B, and C.
#
  import numpy as np

  a = 0
  b = 0
  c = 0
  trial_num = 100000

  for sim in range ( 0, trial_num ):

    roll = rng.integers ( low = 1, high = 6, size = 6, endpoint = True )
    count = np.sum ( roll == 6 )
    if ( 1 <= count ):
      a = a + 1

    roll = rng.integers ( low = 1, high = 6, size = 12, endpoint = True )
    count = np.sum ( roll == 6 )
    if ( 2 <= count ):
      b = b + 1

    roll = rng.integers ( low = 1, high = 6, size = 18, endpoint = True )
    count = np.sum ( roll == 6 )
    if ( 3 <= count ):
      c = c + 1

  a = a / trial_num
  b = b / trial_num
  c = c / trial_num

  return a, b, c

def newton_test ( rng ):

#*****************************************************************************80
#
## newton_test() tests newton().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'newton_test():' )
  print ( '  newton() estimates the probability that' )
  print ( '    A: a fair die rolled  6 times will show 6 at least 1 time' )
  print ( '    B: a fair die rolled 12 times will show 6 at least 2 times' )
  print ( '    C: a fair die rolled 18 times will show 6 at least 3 times.' )
  print ( '  Samuel Pepys believed C was more likely than A or B.' )
  print ( '  Newton showed that A was more likely.' )

  a, b, c = newton ( rng )

  print ( '' )
  print ( '  Case  Estimate  Exact' )
  print ( '     A: %6.4g  %6.4g' % ( a, 0.6651 ) )
  print ( '     B: %6.4g  %6.4g' % ( b, 0.6187 ) )
  print ( '     C: %6.4g  %6.4g' % ( c, 0.5973 ) )

  return

def obtuse1 ( rng ):

#*****************************************************************************80
#
## obtuse1() estimates the probability of an obtuse triangle.
#
#  Discussion:
#
#    A triangle has a side of length s1 = 1.  Choose the lengths of the other
#    two sides s2 and s3 uniformly at random, and proceed only if these sides 
#    create a triangle.  Determine the probability the triangle is obtuse.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real p, the probability of creating an obtuse triangle.
#
  obtuse = 0
  triangle = 0
  trial_num = 100000

  while ( triangle < trial_num ):

    s2 = rng.random ( )
    s3 = rng.random ( )

    if ( 1.0 < s2 + s3 ):
      triangle = triangle + 1
      if ( s2**2 + s3**2 < 1.0 ):
        obtuse = obtuse + 1

  p = obtuse / trial_num

  return p

def obtuse1_test ( rng ):

#*****************************************************************************80
#
## obtuse1_test() tests obtuse1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'obtuse1_test():' )
  print ( '  obtuse1() estimates the probability that an obtuse triangle' )
  print ( '  will be formed, assuming that one side has length 1, and' )
  print ( '  the other two side lengths are chosen uniformly at random' )
  print ( '  between 0 and 1.' )

  p = obtuse1 ( rng )
  exact = 0.5 * np.pi - 1.0

  print ( '' )
  print ( '  Estimate = ', p )
  print ( '  Exact    = ', exact )

  return

def obtuse2 ( rng ):

#*****************************************************************************80
#
## obtuse2() estimates the probability of an obtuse triangle.
#
#  Discussion:
#
#    A stick of length 1 is randomly broken into 3 pieces.
#    What is the probablity that an obtuse triangle is formed?
#
#    Here, we choose x and y at random, and use these to determine
#    the lengths of the sides.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 May 2019
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real p, the probability of creating an obtuse triangle.
#
  obtuse = 0
  triangle = 0
  trial_num = 100000

  while ( triangle < trial_num ):

    x = rng.random ( )
    y = rng.random ( )

    if ( x < y ):
      s1 = x
      s2 = y - x 
      s3 = 1.0 - y
    else:
      s1 = y
      s2 = x - y
      s3 = 1.0 - x

    if ( s1 < s2 and s2 < s1 + s3 and s3 < s1 + s2 ):
      triangle = triangle + 1
      d1 = s1**2
      d2 = s2**2
      d3 = s3**2
      if ( d2 + d3 < d1 or d1 + d3 < d2 or d1 + d2 < d3 ):
        obtuse = obtuse + 1

  p = obtuse / trial_num

  return p

def obtuse2_test ( rng ):

#*****************************************************************************80
#
## obtuse2_test() tests obtuse2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'obtuse2_test():' )
  print ( '  obtuse2() estimates the probability that, after a stick' )
  print ( '  of unit length is randomly broken into three pieces,' )
  print ( '  an obtuse triangle can be formed from the pieces.' )

  p = obtuse2 ( rng )
  exact = 9.0 - 12.0 * np.log ( 2.0 )

  print ( '' )
  print ( '  Estimate = ', p )
  print ( '  Exact    = ', exact )

  return

def ping_pong ( p ):

#*****************************************************************************80
#
## ping_pong() computes the likelihood of winning at ping pong.
#
#  Discussion:
#
#    A score of 11 wins in ping-pong...except that the winner must be
#    ahead by at least 2 points.  We ignore that exception here.
#    
#    We assume player 1 has a probability p of winning any single point.
#
#    We construct a table T such that T(i,j) is the probability that
#    player 1 will win, given that player 1 needs i more points to win,
#    and player 2 needs j more points to win.  Then T(11,11) is the
#    probability that player 1 wins.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    real p: the probability that player 1 wins a single point.
#
#  Output:
#
#    real prob: the probability that player 1 wins the game.
#
  import numpy as np

  t = np.zeros ( [ 11, 11 ] )

  q = 1.0 - p
#
#  t(1,j) is the probability that player 1 will win, 
#  assuming player 1 needs 1 more point to win, 
#  and player 2 needs j more points to win.
#
  for j in range ( 0, 11 ):
    t[0,j] = 1.0 - q**(j+1)
#
#  t(j,1) is the probability that player 1 will win, 
#  assuming player 1 needs j more points to win, 
#  and player 2 needs 1 more point to win.
#
#  In each case, player 1 must make j points in a row.
#
  for j in range ( 0, 11 ):
    t[j,0] = p**(j+1)
#
#  t(i,j) is the probability that player 1 will win,
#  assuming player 1 needs i more points, and player 2 j more points.
#
#  This can happen in two ways:
#    player 1 had i-1 points, player 2 had j points, and player 1 made the next point.
#  OR
#    player 1 had i points, player 2 had j-1 points, and player 2 made the next point.
#
  for i in range ( 1, 11 ):
    for j in range ( 1, 11 ):
      t[i,j] = p * t[i-1,j] + q * t[i,j-1]
#
#  Our answer is the probability that player 1 will win, starting
#  from the beginning, when both players needed 11 points to win.
#
  prob = t[10,10]

  return prob

def ping_pong_test ( ):

#*****************************************************************************80
#
## ping_pong_test() tests ping_pong().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ping_pong_test():' )
  print ( '  ping_pong() estimates PROB, the probability that a player' )
  print ( '  will win a game of ping pong, assuming the player has' )
  print ( '  a probability P of winning a single point.' )

  p_test =     np.array ( [ 0.3,    0.4,    0.5, 0.6 ] )
  exact_test = np.array ( [ 0.0264, 0.1744, 0.5, 0.8256 ] )

  print ( '' )
  print ( '  P  PROB  Exact' )
  print ( '' )
  for i in range ( 0, 4 ):
    p = p_test[i]
    prob = ping_pong ( p )
    exact = exact_test[i]
    print ( '  %g  %g  %g' % ( p, prob, exact ) )

  return

def plums ( n, rng ):

#*****************************************************************************80
#
## plums(): average distance to surface of closest of n plums in a spherical pudding.
#
#  Discussion:
#
#    The correct expected value is r/(3*n+1) where r is the radius of the
#    pudding.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real s, an estimate for the expected length.
#
  import numpy as np

  trial_num = 100000

  total = 0
  for trials in range ( 0, trial_num ):

    points = np.zeros ( n )

    for loop2 in range ( 0, n ):
#
#  Keep picking random points in the unit cube
#  until you get one that's also in the unit sphere.
#
      while ( True ):
        x = 2.0 * rng.random ( ) - 1.0
        y = 2.0 * rng.random ( ) - 1.0
        z = 2.0 * rng.random ( ) - 1.0
        d2 = x**2 + y**2 + z**2
        if ( d2 < 1.0 ):
          break
#
#  Remember the distance of this point to the center of the sphere.
#
      points[loop2] = np.sqrt ( d2 )
#
#  Find plum furthest from center (and closest to surface)
#
    total = total + np.max ( points )

  s = 1.0 - ( total / trial_num )

  return s

def plums_test ( rng ):

#*****************************************************************************80
#
## plums_test() tests plums().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'plums_test():' )
  print ( '  plums() estimates the expected distance D from the surface' )
  print ( '  to the nearest of N plums randomly placed inside a unit' )
  print ( '  spherical pudding.' )
  print ( '' )
  print ( '  N  D(Estimate)  D(Exact)' )
  print ( '' )

  for n in range ( 5, 11 ):
    s = plums ( n, rng )
    s_exact = 1.0 / ( 3 * n + 1 )
    print ( '  %2d  %g  %g' % ( n, s, s_exact ) )

  return

def ratio1 ( k, rng ):

#*****************************************************************************80
#
## ratio1() tabulates how often a random ratio exceeds 1, 2, 3, ...
#
#  Discussion:
#
#    We pick two random numbers from [0,1] uniformly.  
#    What is the probability that the ratio of the larger to the smaller
#    value is more than k?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    real k, the ratio limit.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real p, the probability, which should be about 1/k.
#
  trial_num = 100000

  total = 0
  for trials in range ( 0, trial_num ):
    x1 = rng.random ( )
    x2 = rng.random ( )
    r = max ( x1, x2 ) / min ( x1, x2 )
    if ( k <= r ):
      total = total + 1

  p = total / trial_num

  return p

def ratio1_test ( rng ):

#*****************************************************************************80
#
## ratio1_test() tests ratio1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'ratio1_test():' )
  print ( '  ratio1() estimates the probability PROB that the ratio of' )
  print ( '  two random numbers is greater than K.' )
  print ( '' )
  print ( '  K  Estimated  Approximated' )
  print ( '' )
  for k in range ( 2, 11 ):
    prob = ratio1 ( k, rng )
    approximated = 1.0 / k
    print ( '  %2d  %g  %g' % ( k, prob, approximated ) )

  return

def ratio2 ( k, rng ):

#*****************************************************************************80
#
## ratio2() tabulates how often a random ratio exceeds 1, 2, 3, ...
#
#  Discussion:
#
#    We pick three random numbers from [0,1] uniformly.  
#    What is the probability that the ratio of the largest to the smallest
#    value is more than k?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    real k, the ratio limit.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real p, the probability.
#
  trial_num = 100000

  total = 0
  for trials in range ( 0, trial_num ):
    x = rng.random ( 3 )
    r = max ( x ) / min ( x )
    if ( k <= r ):
      total = total + 1

  p = total / trial_num

  return p

def ratio2_test ( rng ):

#*****************************************************************************80
#
## ratio2_test() tests ratio2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'ratio2_test():' )
  print ( '  ratio2() estimates the probability PROB that, given three' )
  print ( '  random numbers, the ratio of the largest to the smallest' )
  print ( '  is greater than or equal to K.' )

  print ( '' )
  print ( '  K  PROB' )
  print ( '' )
  for k in range ( 2, 11 ):
    prob = ratio2 ( k, rng )
    print ( '  %2d  %g' % ( k, prob ) )

  return

def spaghetti ( n ):

#*****************************************************************************80
#
## spaghetti() analyzes the spaghetti problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    integer N, the number of strands of spaghetti.
#
#  Output:
#
#    real E, the expected number of loops created
#    if we begin with N strands of spaghetti and randomly pair the 2*N
#    ends, possibly making loops.
#
  e = 1.0
  for i in range ( 2, n + 1 ):
    e = e + 1.0 / ( 2 * i - 1 )

  return e

def spaghetti_test ( ):

#*****************************************************************************80
#
## spaghetti_test() tests spaghetti().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'spaghetti_test():' )
  print ( '  spaghetti() estimates E, the expected number of loops created' )
  print ( '  if N strands of spaghetti are randomly joined at the ends.' )

  print ( '' )
  print ( '  N   E' )
  print ( '' )
  for i in range ( 1, 5 ):
    n = 10**i
    e = spaghetti ( n )
    print ( '  %d  %g' % ( n, e ) )

  return

def square_adjacent ( rng ):

#*****************************************************************************80
#
## square_adjacent(): expected distance between random points on adjacent square sides.
#
#  Discussion:
#
#    We may take the two sides as unit intervals on the x and y axis,
#    both starting at the origin.
#
#    The correct expected value is 0.7652.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real s, an estimate for the expected length.
#
  import numpy as np

  trial_num = 100000

  total = 0
  for trials in range ( 0, trial_num ):
    x1 = rng.random ( )
    y1 = 0.0
    x2 = 0.0
    y2 = rng.random ( )
    r = np.sqrt ( ( x1 - x2 )**2 + ( y1 - y2 )**2 )
    total = total + r

  s = total / trial_num

  return s

def square_adjacent_test ( rng ):

#*****************************************************************************80
#
## square_adjacent_test() tests square_adjacent().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'square_adjacent_test():' )
  print ( '  square_adjacent() estimates S, the expected distance' )
  print ( '  between random points on adjacent sides of a unit square.' )

  s = square_adjacent ( rng )

  print ( '' )
  print ( '  Estimate = ', s )
  print ( '  Exact    = ', 0.7652 )

  return

def square_inside ( rng ):

#*****************************************************************************80
#
## square_inside(): expected distance between random points inside unit square.
#
#  Discussion:
#
#    The correct expected value is 0.5214...
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real s, an estimate for the expected length.
#
  import numpy as np

  trial_num = 100000

  total = 0
  for trials in range ( 0, trial_num ):
    x1 = rng.random ( )
    y1 = rng.random ( )
    x2 = rng.random ( )
    y2 = rng.random ( )
    r = np.sqrt ( ( x1 - x2 )**2 + ( y1 - y2 )**2 )
    total = total + r

  s = total / trial_num

  return s

def square_inside_test ( rng ):

#*****************************************************************************80
#
## square_inside_test() tests square_inside().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'square_inside_test():' )
  print ( '  square_inside() estimates the expected distance between' )
  print ( '  random points inside a unit square.' )

  s = square_inside ( rng )

  print ( '  Estimate = ', s )
  print ( '  Exact    = ', 0.5214 )

  return

def square_opposite ( rng ):

#*****************************************************************************80
#
## square_opposite(): expected length of line between random points on opposite square sides.
#
#  Discussion:
#
#    We consider a unit square, and randomly choose a points on two
#    opposite sides and measure their distance.
#
#    The correct expected value is 1.0766.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real s, an estimate for the expected length.
#
  import numpy as np

  trial_num = 100000

  total = 0
  for trials in range ( 0, trial_num ):
    x1 = 0.0
    y1 = rng.random ( )
    x2 = 1.0
    y2 = rng.random ( )
    r = np.sqrt ( ( x1 - x2 )**2 + ( y1 - y2 )**2 )
    total = total + r

  s = total / trial_num

  return s

def square_opposite_test ( rng ):

#*****************************************************************************80
#
## square_opposite_test() tests square_opposite().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'square_opposite_test():' )
  print ( '  square_opposite() estimates the expected distance ' )
  print ( '  between random points on opposite sides of the perimeter' )
  print ( '  of a unit square.' )

  s = square_opposite ( rng )

  print ( '' )
  print ( '  Estimate = ', s )
  print ( '  Exact    = ', 1.0766 )

  return

def squash ( ):

#*****************************************************************************80
#
## squash() computes probabilities a player will win the game of squash.
#
#  Discussion:
#
#    Players P and Q can each score a point only by winning a rally in
#    which they served.  If a player wins the rally, he keeps the serve
#    otherwise, the serve goes to the opposing player.  The winner is the
#    first to reach 9 points.
#
#    Here, we suppose both players P and Q have 1/2 chance of winning
#    any given rally.
#
#    We compute the probability that player P will win, depending on
#    whether P or Q serves first.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Output:
#
#    real p, q, the probabilities that P wins, given that 
#    P serves first, or that Q serves first.
#    Expected values are 0.534863456 and 0.465136543.
#
  import numpy as np

  r = 2.0 / 3.0

  ps = np.zeros ( [ 9, 9 ] )
  qs = np.zeros ( [ 9, 9 ] )

  for i in range ( 0, 9 ):
    ps[i,0] = r**(i+1)
    qs[i,0] = ps[i,0] / 2.0

  for i in range ( 0, 9 ):
    qs[0,i] = 1.0 - ps[i,0]
    ps[0,i] = 1.0 - qs[i,0]

  for i in range ( 1, 9 ):
    for j in range ( 1, 9 ):
      ps[i,j] = r * ( ps[i-1,j] + 0.5 * qs[i,j-1] )
      qs[i,j] = 0.5 * ( ps[i,j] + qs[i,j-1] )

  p = ps[8,8]
  q = qs[8,8]

  return p, q

def squash_test ( ):

#*****************************************************************************80
#
## squash_test() tests squash().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'squash_test():' )
  print ( '  squash() estimates the probability of winning the game of squash' )
  print ( '  played between two equally good players:' )
  print ( '  P: if you serve first,' )
  print ( '  Q: if you serve second.' )

  p, q = squash ( )

  p_exact = 0.534863456
  q_exact = 0.465136543

  print ( '' )
  print ( '  P Estimate = %g, exact is %g' % ( p, p_exact ) )
  print ( '  Q Estimate = %g, exact is %g' % ( q, q_exact ) )

  return

def steve2 ( k, n, rng ):

#*****************************************************************************80
#
## steve2(): Steve's elevator problem.
#
#  Discussion:
#
#    Steve gets on an elevator going up.  There are N higher floors.
#    Steve wishes to go up 9 floors.
#    There are K additional riders in the elevator, each of whom has
#    randomly chosen one of the N higher floors as destination.
#    On average, how many times will the elevator stop until Steve
#    reaches his floor?
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 May 2019
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    integer K, the number of elevator riders in addition to Steve.
#
#    integer N, the number of higher floors.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real S: the estimated number of stops.
#
#    real T: the theoretical number of stops.
#
  import numpy as np

  trial_num = 100000

  S = 0

  for loop in range ( 0, trial_num ):
#
#  Randomly decide whether each floor has at least one rider who wants to go there.
#
    x = np.zeros ( n )
    x[8] = 1
    for j in range ( 0, k ):
      rider = rng.integers ( low = 0, high = n, endpoint = False )
      x[rider] = 1
#
#  Count the number of times the elevator will stop, including at Steve's floor.
#
    stops = 1
    for j in range ( 0, 8 ):
      stops = stops + x[j]

    S = S + stops

  S = S / trial_num

  T = 1.0 + ( n - 3 ) * ( 1.0 - ( 1.0 - 1.0 / n ) ** k )

  return S, T

def steve2_test ( rng ):

#*****************************************************************************80
#
## steve2_test() tests steve2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'steve2_test():' )
  print ( '  steve2() analyzes Steve''s elevator problem.' )
  print ( '  Steve gets on an elevator going up.  There are N higher floors.' )
  print ( '  Steve wishes to go up 9 floors.' )
  print ( '  There are K additional riders in the elevator, each of whom has' )
  print ( '  randomly chosen one of the higher floors as destination.' )
  print ( '  On average, how many times S will the elevator stop until Steve' )
  print ( '  reaches his floor?' )
  print ( '  The theoretical value is T.' )

  k_test = np.array ( [  3,  3, 10, 10 ] )
  n_test = np.array ( [ 11, 20, 11, 20 ] )

  print ( '' )
  print ( '   N   K   S   T' )
  print ( '' )

  for i in range ( 0, 4 ):
    k = k_test[i]
    n = n_test[i]
    S, T = steve2 ( k, n, rng )
    print ( '  %d  %d  %g  %g' % ( n, k, S, T ) )

  return

def ten_years ( years ):

#*****************************************************************************80
#
## ten_years() estimates whether you will be alive in 10 years.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    integer years: the number of years in the future, between 0 and 10.
#
#  Output:
#
#    real prob: the probability you will still be alive.
#
  import numpy as np

  if ( years < 0 or 10 < years ):
    raise Exception ( 'ten_years: 0 <= years <= 10 is required!' )

  phi = np.array ( [ 20.3, \
          19.5, 18.9, 18.2, 17.6, 16.9, \
          16.2, 15.6, 15.0, 14.4, 13.8 ] )

  phi_int = 0.0
  for y in range ( 0, years ):
    phi_int = phi_int + 0.5 * ( 1.0 / phi[y] + 1.0 / phi[y+1] )

  log_prob = np.log ( phi[0] ) - np.log ( phi [ years ] ) - phi_int

  prob = np.exp ( log_prob )

  return prob

def ten_years_test ( ):

#*****************************************************************************80
#
## ten_years_test() tests ten_years().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'ten_years_test():' )
  print ( '  ten_years() estimates the probability that a certain' )
  print ( '  person will still be alive in 1, 2, ..., 10 years.' )

  print ( '' )
  print ( '  Years  Probability' )
  print ( '' )
 
  for years in range ( 0, 11 ):
    prob = ten_years ( years )
    print ( '  %2d  %g' % ( years, prob ) )

  return

def top ( p, rng ):

#*****************************************************************************80
#
## top() analyzes the dreidel game.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    real p, the number of players.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real winnings(p), the expected winnings per player.
#
  import numpy as np

  winnings = np.zeros ( p )

  trial_num = 100000

  for game in range ( 0, trial_num ):

    pot = p
    keepplaying = True
    player = 0

    while ( keepplaying ):

      spin = rng.random ( )

      if ( spin < 0.25 ):
        pass
      elif ( spin < 0.50 ):
        pot = pot / 2
        winnings[player] = winnings[player] + pot
      elif ( spin < 0.75 ):
        winnings[player] = winnings[player] + pot
        pot = 0
        keepplaying = False
      else:
        pot = pot + 1
        winnings[player] = winnings[player] - 1
#
#  Next player.
#
      player = ( ( player + 1 ) % p )

  winnings = winnings / trial_num

  return winnings

def top_test ( rng ):

#*****************************************************************************80
#
## top_test() tests top().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'top_test():' )
  print ( '  top() estimates winning ratios for dreidel' )
  print ( '' )
  for k in range ( 2, 6 ):
    winnings = top ( k, rng )
    print ( '  %2d:  ' % ( k ), end = '' )
    for i in range ( 0, k ):
      print ( '  %g' % ( winnings[i] ), end = '' )
    print ( '' )

  return

def twins ( rng ):

#*****************************************************************************80
#
## twins() analyzes the twins problem.
#
#  Discussion:
#
#    There are 20 students in a class.  Two of the students are twins.
#    The class is divided into five lab groups of size four.
#
#    Estimate that probability that the twins are assigned to the same
#    lab group.
#
#    The expected value is 3/19.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    Original MATLAB version by Paul Nahin;
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Will You Be Alive 10 Years From Now?,
#    Princeton, 2014,
#    ISBN: 978-0691156804,
#    LC: QA273.25.N344
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real prob: the probability that the twins are in the same group.
#
  import numpy as np

  trial_num = 100000

  together = 0
  n = 20

  for loop1 in range ( 0, trial_num ):
#
#  Use a permutation to assign students to lab groups.
#
    p = rng.permutation ( n )

    r1 = p[0] % 5
    r2 = p[1] % 5

    if ( r1 == r2 ):
      together = together + 1

  prob = together / trial_num

  return prob

def twins_test ( rng ):

#*****************************************************************************80
#
## twins_test() tests twins().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'twins_test():' )
  print ( '  twins() estimates the probability that 2 twins in 20 students' )
  print ( '  will be randomly assigned the same lab group of 4 students.' )

  p = twins ( rng )
  exact = 3 / 19

  print ( '' )
  print ( '  Estimate = ', p )
  print ( '  Exact    = ', exact )

  return

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
  will_you_be_alive_test ( )
  timestamp ( )

