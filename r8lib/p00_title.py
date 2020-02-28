#! /usr/bin/env python
#
def p00_title ( prob ):

#*****************************************************************************80
#
## P00_TITLE returns the title of any problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer PROB, the number of the desired test problem.
#
#    Output, string TITLE, the title of the problem.
#
  from sys import exit

  if ( prob == 1 ):
    title = p01_title ( )
  elif ( prob == 2 ):
    title = p02_title ( )
  elif ( prob == 3 ):
    title = p03_title ( )
  elif ( prob == 4 ):
    title = p04_title ( )
  elif ( prob == 5 ):
    title = p05_title ( )
  elif ( prob == 6 ):
    title = p06_title ( )
  elif ( prob == 7 ):
    title = p07_title ( )
  elif ( prob == 8 ):
    title = p08_title ( )
  else:
    print ( '' )
    print ( 'P00_TITLE - Fatal error!' )
    print ( '  Illegal problem number = %d' % ( prob ) )
    exit ( 'P00_TITLE - Fatal error!' )

  return title

def p01_title ( ):

#*****************************************************************************80
#
## P01_TITLE returns the title of problem p01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = steps -1/2/1 at [0,1/3], [1/3,4/5], [4/5,1].'

  return title

def p02_title ( ):

#*****************************************************************************80
#
## P02_TITLE returns the title of problem p02.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = (1-3x), x < 1/3 (6x-2) if 1/3 < x'

  return title

def p03_title ( ):

#*****************************************************************************80
#
## P03_TITLE returns the title of problem p03.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = x (10*x-1) (5x-2) (5x-2) (4x-3.4) (x-1)'

  return title

def p04_title ( ):

#*****************************************************************************80
#
## P04_TITLE returns the title of problem p04.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = atan ( 40 * x - 15 )'

  return title

def p05_title ( ):

#*****************************************************************************80
#
## P05_TITLE returns the title of problem p05.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = cos(7*x)+5*cos(11.2*x)-2*cos(14*x)+5*cos(31.5*x)+7*cos(63*x).'

  return title

def p06_title ( ):

#*****************************************************************************80
#
## P06_TITLE returns the title of problem p06.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = exp ( - ( 4*x-1 )^2 )'

  return title

def p07_title ( ):

#*****************************************************************************80
#
## P07_TITLE returns the title of problem p07.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = exp ( 2 x ) if x < 0.5, 0 otherwise'

  return title

def p08_title ( ):

#*****************************************************************************80
#
## P08_TITLE returns the title of problem p08.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, string TITLE, the title of the problem.
#
  title = 'f(x) = 1 / ( 1 + ( 10 * (x-1/2) )^2 )'

  return title

def p00_title_test ( ):

#*****************************************************************************80
#
## P00_TITLE_TEST tests P00_TITLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from p00_prob_num import p00_prob_num

  print ( '' )
  print ( 'P00_TITLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P00_TITLE returns the title of any test problems.' )

  num = p00_prob_num ( )
  print ( '' )
  print ( '  TEST_INTERP_1D includes %d test problems.' % ( num ) )

  print ( '' )
  for prob in range ( 1, num + 1 ):
    title = p00_title ( prob )
    print ( '  #%d  "%s"' % ( prob, title ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P00_TITLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  p00_title_test ( )
  timestamp ( )
