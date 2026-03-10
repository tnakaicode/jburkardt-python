#! /usr/bin/env python3
#
def coin_average_plot ( n, v, label, filename ):

#*****************************************************************************80
#
## coin_average_plot() plots the running average of N coin tosses.
#
#  Discussion:
#
#    Note that this function does not call CLF to clear the figure.
#    Therefore, invoking the function twice in a row will
#    show both the old and new plots together.  This operation can be
#    repeated.  Since we expect the plots to show similar behavior
#    towards the right, this may be a useful feature.  If not,
#    call clf, or uncomment the "clf" below.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of tosses.
#
#    real V(N), the toss results, -1 or +1.
#
#    string LABEL, a label for the plot.
#
#    string FILENAME, a name for the plot file.
#
  import matplotlib.pyplot as plt
  import numpy as np

  a = r8vec_mean_running ( n, v )
  ip1 = np.linspace ( 1, n + 1, n + 1 )
#
#  Uncomment this "CLF" if you want to guarantee the plot
#  appears on a new plot figure.
#
  plt.clf ( )
  plt.plot ( ip1, a, 'b.-', markersize = 25, linewidth = 2 )
  plt.xlabel ( '<-- Tosses -->' )
  plt.ylabel ( 'Running Average' )
  plt.title ( label )
  plt.ylim ( [ -1.1, +1.1 ] )

  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def coin_barchart ( n, v, label, filename ):

#*****************************************************************************80
#
## coin_barchart() makes a bar chart of N coin tosses.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of tosses.
#
#    real V(N), the toss results, -1 or +1.
#
#    string LABEL, a label for the plot.
#
#    string FILENAME, a name for the plot file.
#
  import matplotlib.pyplot as plt

  plt.clf ( )
  plt.hist ( v )

  plt.grid ( True )
  plt.title ( label )
  plt.ylim ( [ 0, n ] )

  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def coin_biased ( n, heads, rng ):

#*****************************************************************************80
#
## coin_biased() generates N biased random coin flips.
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
#    integer N, the number of tosses.
#
#    real HEADS, the probability of heads with this coin.
#    0.0 <= HEADS <= 1.0.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer V(N), a vector of -1's for tails, and 1's for heads.
#
  v = rng.integers ( low = 0, high = 1, size = n, endpoint = True )

  v = 2 * v - 1

  return v

def coin_biased_test ( ):

#*****************************************************************************80
#
## coin_biased_test() tests coin_biased().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng

  rng = default_rng ( )

  print ( '' )
  print ( 'coin_biased_test()' )
  print ( '  coin_biased() simulates the tossing of a biased coin N times.' )

  n = 100
  heads = 0.70

  print ( '  HEADS has a probability of', heads )

  v = coin_biased ( n, heads, rng )

  print ( '' )
  print ( '  Coin toss results: -1=Tails, +1=Heads' )
  print ( n )

  return

def coin_plot ( n, v, label, filename ):

#*****************************************************************************80
#
## coin_plot() makes a plot of N coin tosses.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of tosses.
#
#    real V(N), the toss results, -1 or +1.
#
#    string LABEL, a label for the plot.
#
#    string FILENAME, a name for the plot file.
#
  import matplotlib.pyplot as plt
  import numpy as np

  i = np.linspace ( 1, n, n )

  plt.clf ( )
  plt.plot ( i, v, 'b.-', markersize = 25, linewidth = 2 )
  plt.xlabel ( '<-- Tosses -->' )
  plt.ylabel ( 'T <-------------------> H' )
  plt.title ( label )
  plt.ylim ( [ -1.1, +1.1 ] )

  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def coins_average_plot ( m, n, v, label, filename ):

#*****************************************************************************80
#
## coins_average_plot() plots the running average of M sets of N coin tosses.
#
#  Discussion:
#
#    Note that this function does not call CLF to clear the figure.
#    Therefore, invoking the function twice in a row will
#    show both the old and new plots together.  This operation can be
#    repeated.  Since we expect the plots to show similar behavior
#    towards the right, this may be a useful feature.  If not,
#    call clf, or uncomment the "clf" below.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of repetitions.
#
#    integer N, the number of tosses.
#
#    real V(M,N), the toss results, -1 or +1.
#
#    string LABEL, a label for the plot.
#
#    string FILENAME, a name for the plot file.
#
  import matplotlib.pyplot as plt
  import numpy as np

  a = r8row_mean_running ( m, n, v )

  ip1 = np.linspace ( 1, n + 1, n + 1 )

  plt.clf ( )
  plt.plot ( ip1, a.T, 'b.-', markersize = 25, linewidth = 2 )
  plt.xlabel ( '<-- Tosses -->' )
  plt.ylabel ( 'Running Average' )
  plt.title ( label )
  plt.ylim ( [ -1.1, +1.1 ] )

  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def coins_barchart ( n, v, label, filename ):

#*****************************************************************************80
#
## coins_barchart() makes a bar chart of N coin tosses.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of tosses.
#
#    real V(N), the toss results, -1 or +1.
#
#    string LABEL, a label for the plot.
#
#    string FILENAME, a name for the plot file.
#
  import matplotlib.pyplot as plt

  plt.clf ( )
  histogram ( v )

  plt.grid ( True )
  plt.title ( label )
  plt.ylim ( [ 0, n ] )

  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def coins_biased ( m, n, heads, rng ):

#*****************************************************************************80
#
## coins_biased() generates M sets of N biased random coin flips.
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
#    integer M, the number of repetitions.
#
#    integer N, the number of tosses.
#
#    real HEADS, the probability of heads with this coin.
#    0.0 <= HEADS <= 1.0.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer V(M,N), a vector of -1's for tails, and 1's for heads.
#
  w = rng.random ( size = [ m, n ] )
  v = ( w < 1.0 - heads )

  v = 2 * v - 1

  return v

def coin_sign_plot ( n, v, label, filename ):

#*****************************************************************************80
#
## coin_sign_plot() plots the running sign (+/-) of N coin tosses.
#
#  Discussion:
#
#    Note that this function does not call CLF to clear the figure.
#    Therefore, invoking the function twice in a row will
#    show both the old and new plots together.  This operation can be
#    repeated.  Since we expect the plots to show similar behavior
#    towards the right, this may be a useful feature.  If not,
#    call clf, or uncomment the "clf" below.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of tosses.
#
#    real V(N), the toss results, -1 or +1.
#
#    string LABEL, a label for the plot.
#
#    string FILENAME, a name for the plot file.
#
  import matplotlib.pyplot as plt
  import numpy as np

  s = r8vec_sign3_running ( n, v )

  ip1 = np.linspace ( 1, n + 1, n + 1 )

  plt.clf ( )
  plt.plot ( ip1, s, 'b.-', markersize = 25, linewidth = 2 )
  plt.xlabel ( '<-- Tosses -->' )
  plt.ylabel ( 'Running Sign' )
  plt.title ( label )
  plt.ylim ( [ -1.1, +1.1 ] )

  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def coin_simulation_test ( ):

#*****************************************************************************80
#
## coin_simulation_test() tests coin_simulation().
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
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( 'n' )
  print ( 'coin_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  coin_simulation() simulates and visualizes the repeated' )
  print ( '  tossing of a coin.' )

  rng = default_rng ( )
#
#  Generate lists of values.
#
  coin_biased_test ( )
  coin_streak_test ( )
  coin_uniform_test ( )
#
#  Generate one set of biased data for all the plots.
#
  n = 100
  heads = 0.70
  v = coin_biased ( n, heads, rng )
#
#  Generate various plots based on the biased data.
#
  label = ( 'Tails(left) versus Heads(right), %d tosses with head bias %g' % ( n, heads ) )
  filename = 'coin_biased_barchart.png'
  coin_barchart ( n, v, label, filename )

  label = ( 'Tossing a coin with %g bias %d times' % ( heads, n ) )
  filename = 'coin_biased_plot.png'
  coin_plot ( n, v, label, filename )

  label = ( 'Tossing a coin with %g bias %d times' % ( heads, n ) )
  filename = 'coin_biased_average.png'
  coin_average_plot ( n, v, label, filename )

  label = ( 'Tossing a coin with %g bias %d times' % ( heads, n ) )
  filename = 'coin_biased_sign.png'
  coin_sign_plot ( n, v, label, filename )

  label = ( 'Tossing a coin with %g bias %d times' % ( heads, n ) )
  filename = 'coin_biased_streak.png'
  coin_streak_plot ( n, v, label, filename )

  label = ( 'Tossing a coin with %g bias %d times' % ( heads, n ) )
  filename = 'coin_biased_sum.png'
  coin_sum_plot ( n, v, label, filename )
#
#  1024 experiments, toss 10 times and count the heads on a biased coin.
#
  m = 1024
  n = 10
  heads = 0.70

  v = coins_biased ( m, n, heads, rng )

  label = ( '%d cases, number of heads tossing a coin with %g bias %d times' % ( m, heads, n ) )
  filename = 'coins_biased_sum_barchart.png'
  coins_sum_barchart ( m, n, v, label, filename )
#
#  Generate one set of uniform data for all the plots.
#
  n = 100
  v = coin_uniform ( n, rng )
#
#  Generate various plots based on the uniform data.
#
  label = ( 'Tails(left) versus Heads(right), %d tosses with fair coin' % ( n ) )
  filename = 'coin_uniform_barchart.png'
  coin_barchart ( n, v, label, filename )

  label = ( 'Tossing a fair coin %d times' % ( n ) )
  filename = 'coin_uniform_plot.png'
  coin_plot ( n, v, label, filename )

  label = ( 'Tossing a fair coin %d times' % ( n ) )
  filename = 'coin_uniform_average.png'
  coin_average_plot ( n, v, label, filename )

  label = ( 'Tossing a fair coin %d times' % ( n ) )
  filename = 'coin_uniform_sign.png'
  coin_sign_plot ( n, v, label, filename )

  label = ( 'Tossing a fair coin %d times' % ( n ) )
  filename = 'coin_uniform_streak.png'
  coin_streak_plot ( n, v, label, filename )

  label = ( 'Tossing a fair coin %d times' % ( n ) )
  filename = 'coin_uniform_sum.png'
  coin_sum_plot ( n, v, label, filename )
#
#  Generate M sets of uniform data for all the plots.
#
  m = 20
  n = 100
  v = coins_uniform ( m, n, rng )

  label = ( '%d cases, tossing a fair coin %d times' % ( m, n ) )
  filename = 'coins_uniform_plot.png'
  coins_plot ( m, n, v, label, filename )

  label = ( '%d cases, tossing a fair coin %d times' % ( m, n ) )
  filename = 'coins_uniform_average.png'
  coins_average_plot ( m, n, v, label, filename )

  label = ( '%d cases, tossing a fair coin %d times' % ( m, n ) )
  filename = 'coins_uniform_sum.png'
  coins_sum_plot ( m, n, v, label, filename )
#
#  1024 experiments, toss 10 times and count the heads on a fair coin.
#
  m = 1024
  n = 10
  v = coins_uniform ( m, n, rng )

  label = ( '%d cases, number of heads tossing a fair coin %d times'% ( m, n ) )
  filename = 'coins_uniform_sum_barchart.png'
  coins_sum_barchart ( m, n, v, label, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'coin_simulation_test():' )
  print ( '  Normal end of execution.' )

  return

def coins_plot ( m, n, v, label, filename ):

#*****************************************************************************80
#
## coins_plot() makes a plot of M sets of N coin tosses.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of repetitions.
#
#    integer N, the number of tosses.
#
#    real V(M,N), the toss results, -1 or +1.
#
#    string LABEL, a label for the plot.
#
#    string FILENAME, a name for the plot file.
#
  import matplotlib.pyplot as plt
  import numpy as np

  i = np.linspace ( 1, n, n )

  plt.clf ( )
  plt.plot ( i, v.T, 'b.-', markersize = 25, linewidth = 2 )
  plt.xlabel ( '<-- Tosses -->' )
  plt.ylabel ( 'T <-------------------> H' )
  plt.title ( label )
  plt.ylim ( [ -1.1, +1.1 ] )
 
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def coins_sum_barchart ( m, n, v, label, filename ):

#*****************************************************************************80
#
## coins_sum_barchart() makes a bar chart of M instances of N coin tosses.
#
#  Discussion:
#
#    Our barchart will display the frequency of the number of heads
#    between 0 and N.
#
#    For usable plots, you want N to be relatively low (like 5 or 10)
#    while M can be large, like 50, or 100, or 10,000.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of repetitions.
#
#    integer N, the number of tosses.
#
#    real V(M,N), the toss results, -1 or +1.
#
#    string LABEL, a label for the plot.
#
#    string FILENAME, a name for the plot file.
#
  import matplotlib.pyplot as plt
  import numpy as np

  plt.clf ( )
#
#  W contains the row sums, between 0 and N.
#
  w = ( np.sum ( v, axis = 1 ) + n ) / 2

  plt.hist ( w )

  plt.grid ( True )
  plt.title ( label )
  plt.xlim ( [ -0.5, n + 0.5 ] )
  plt.ylim ( [ 0, 300 ] )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def coins_sum_plot ( m, n, v, label, filename ):

#*****************************************************************************80
#
## coins_sum_plot() plots the running sums of M sets of N coin tosses.
#
#  Discussion:
#
#    Note that this function does not call CLF to clear the figure.
#    Therefore, invoking the function twice in a row will
#    show both the old and new plots together.  This operation can be
#    repeated.  Since we expect the plots to show similar behavior
#    towards the right, this may be a useful feature.  If not,
#    call clf, or uncomment the "clf" below.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of repetitions.
#
#    integer N, the number of tosses.
#
#    real V(M,N), the toss results, -1 or +1.
#
#    string LABEL, a label for the plot.
#
#    string FILENAME, a name for the plot file.
#
  import matplotlib.pyplot as plt
  import numpy as np

  s = r8row_sum_running ( m, n, v )

  ip1 = np.linspace ( 1, n + 1, n + 1 )
#
#  Uncomment this "CLF" if you want to guarantee the plot
#  appears on a new plot figure.
#
  plt.clf ( )
  plt.plot ( ip1, s.T, 'b.-', markersize = 25, linewidth = 2 )
  plt.xlabel ( '<-- Tosses -->' )
  plt.ylabel ( 'Running Sum' )
  plt.title ( label )

  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def coin_streak ( n, v ):

#*****************************************************************************80
#
## coin_streak() counts streaks in a sequence of coin flips.
#
#  Example:
#
#    V = (   -1  -1   +1   -1   +1  +1  +1   -1  -1   +1   )
#    S = (  0  -1  -2 | +1 | -1 | +1  +2  +3 | -1  -2 | +1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of tosses.
#
#    real V(N), the sequence of coin flips.
#    -1 = tails, +1 = heads.
#
#  Output:
#
#    real S(N+1), indicates streaks.
#
  import numpy as np

  s = np.zeros ( n + 1 )

  s[0] = 0
  s[1] = v[0]

  for i in range ( 2, n + 1 ):
    s[i] = v[i-1]
    if ( v[i-2] == v[i-1] ):
      s[i] = s[i] + s[i-1]
 
  return s

def coin_streak_plot ( n, v, label, filename ):

#*****************************************************************************80
#
## coin_streak_plot() plots streaks of H's and T's in N coin tosses.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of tosses.
#
#    real V(N), the toss results, -1 or +1.
#
#    string LABEL, a label for the plot.
#
#    string FILENAME, a name for the plot file.
#
  import matplotlib.pyplot as plt
  import numpy as np

  s = coin_streak ( n, v )

  plt.clf ( )
  np1 = np.linspace ( 0, n, n + 1 )
  plt.bar ( np1, s )

  plt.grid ( True )
  plt.title ( label )
  plt.xlabel ( '<-- Tosses -->' )
  plt.ylabel ( '<-- Streaks -->' )

  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def coin_streak_test ( ):

#*****************************************************************************80
#
## coin_streak_test() tests coin_streak().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng

  print ( '' )
  print ( 'coin_streak_test():' )
  print ( '  coin_streak() computes streaks of H\'s or T\'s' )
  print ( '  in N tosses of a coin.' )

  rng = default_rng ( )
  n = 20
  v = coin_uniform ( n, rng )
  print ( '' )
  print ( '  Coin toss results: -1=Tails, +1=Heads' )
  print ( v )

  s = coin_streak ( n, v )
  print ( '' )
  print ( '  Streak list:' )
  print ( s )

  return

def coin_sum_plot ( n, v, label, filename ):

#*****************************************************************************80
#
## coin_sum_plot() plots the running sum of N coin tosses.
#
#  Discussion:
#
#    Note that this function does not call CLF to clear the figure.
#    Therefore, invoking the function twice in a row will
#    show both the old and new plots together.  This operation can be
#    repeated.  Since we expect the plots to show similar behavior
#    towards the right, this may be a useful feature.  If not,
#    call clf, or uncomment the "clf" below.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of tosses.
#
#    real V(N), the toss results, -1 or +1.
#
#    string LABEL, a label for the plot.
#
#    string FILENAME, a name for the plot file.
#
  import matplotlib.pyplot as plt
  import numpy as np

  s = r8vec_sum_running ( n, v )

  ip1 = np.linspace ( 1, n + 1, n + 1 )

  plt.clf ( )
  plt.plot ( ip1, s, 'b.-', markersize = 25, linewidth = 2 )
  plt.xlabel ( '<-- Tosses -->' )
  plt.ylabel ( 'Running Sum' )
  plt.title ( label )

  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def coins_uniform ( m, n, rng ):

#*****************************************************************************80
#
## coins_uniform() computes M sets of N uniformly random coin flips.
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
#    integer M, the number of repetitions.
#
#    integer N, the number of tosses.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer V(M,N), a vector of -1's for tails, and 1's for heads.
#
  v = rng.integers ( low = 0, high = 1, size = [ m, n ], endpoint = True )

  v = 2 * v - 1

  return v

def coin_uniform ( n, rng ):

#*****************************************************************************80
#
## coin_uniform() generates N uniformly random coin flips.
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
#    integer N, the number of tosses.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer V(N), a vector of -1's for tails, and 1's for heads.
#
  v = rng.integers ( low = 0, high = 1, size = n, endpoint = True )
 
  v = 2 * v - 1

  return v

def coin_uniform_test ( ):

#*****************************************************************************80
#
## coin_uniform_test() tests coin_uniform().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng

  print ( '' )
  print ( 'coin_uniform_test():' )
  print ( '  coin_uniform() simulates the tossing of a fair coin N times.' )

  rng = default_rng ( )
  n = 100
  v = coin_uniform ( n, rng )
  print ( '' )
  print ( '  Coin toss results: -1=Tails, +1=Heads' )
  print ( v )

  return

def r8row_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8row_print() prints an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8row_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8row_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8row_print_some() prints out a portion of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8row_mean_running ( m, n, v ):

#*****************************************************************************80
#
## r8row_mean_running() computes the running averages of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows.
#
#    integer N, the number of items in each row.
#
#    real V(M,N), the data.
#
#  Output:
#
#    real A(M,N+1), the running average.  A(I,J) is the average value
#    of V(I,1:J-1).
#
  import numpy as np

  a = np.zeros ( [ m, n + 1 ] )
#
#  Sum.
#
  for j in range ( 1, n + 1 ):
    for i in range ( 0, m ):
      a[i,j] = a[i,j-1] + v[i,j-1]
#
#  Average.
#
  for j in range ( 1, n + 1 ):
    for i in range ( 0, m ):
      a[i,j] = a[i,j] / float ( j )

  return a

def r8row_sum_running ( m, n, v ):

#*****************************************************************************80
#
## r8row_sum_running() computes the running sum of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows.
#
#    integer N, the number of items in each row.
#
#    real V(M,N), the data.
#
#  Output:
#
#    real S(M,N+1), the running sums.  S(I,J) is the sum of V(i,1:J-1).
#
  import numpy as np

  s = np.zeros ( [ m, n + 1 ] )
#
#  Sum.
#
  for j in range ( 1, n + 1 ):
    for i in range ( 0, m ):
      s[i,j] = s[i,j-1] + v[i,j-1]

  return s

def r8vec_mean_running ( n, v ):

#*****************************************************************************80
#
## r8vec_mean_running() computes the running mean of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of items.
#
#    real V(N), the data.
#
#  Output:
#
#    real A(N+1), the running means.  A(I) is the average value
#    of the first I-1 values in V.
#
  import numpy as np

  a = np.zeros ( n + 1 )
#
#  Sum.
#
  for i in range ( 1, n + 1 ):
    a[i] = a[i-1] + v[i-1]
#
#  Average.
#
  for i in range ( 1, n + 1 ):
    a[i] = a[i] / float ( i )

  return a

def r8vec_sign3_running ( n, v ):

#*****************************************************************************80
#
## r8vec_sign3_running() computes the running threeway sign of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of items.
#
#    real V(N), the data.
#
#  Output:
#
#    real S(N+1), the running threeway sign.  S(I) is:
#    -1 if the sum of the first I-1 values in V is negative
#     0, if zero
#    +1, if positive.
#
  import numpy as np

  s = np.zeros ( n + 1 )
#
#  Sum.
#
  for i in range ( 1, n + 1 ):
    s[i] = s[i-1] + v[i-1]

  for i in range ( 0, n + 1 ):
    if ( s[i] < 0.0 ):
      s[i] = -1.0
    elif ( s[i] == 0.0 ):
      s[i] = 0.0
    else:
      s[i] = +1.0

  return s

def r8vec_sum_running ( n, v ):

#*****************************************************************************80
#
## r8vec_sum_running() computes the running sum of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of items.
#
#    real V(N), the data.
#
#  Output:
#
#    real S(N+1), the running sum.  S(I) is the sum
#    of the first I-1 values in V.
#
  import numpy as np

  s = np.zeros ( n + 1 )
#
#  Sum.
#
  for i in range ( 1, n + 1 ):
    s[i] = s[i-1] + v[i-1]

  return s

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
#    06 April 2013
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
  coin_simulation_test ( )
  timestamp ( )

