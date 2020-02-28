#! /usr/bin/env python3
#
def file_name_sequence ( file_name ):

#*****************************************************************************80
#
## FILE_NAME_SEQUENCE generates the next file name in a series.
#
#  Discussion:
#
#    It is assumed that the digits in the name, whether scattered or
#    connected, represent a number that is to be increased by 1 on
#    each call.  If this number is all 9's on input, the output number
#    is all 0's.  Non-numeric letters of the name are unaffected..
#
#    If the name is empty, then the routine stops.
#
#    If the name contains no digits, the empty string is returned.
#
#  Example:
#
#      Input            Output
#      -----            ------
#      'a7to11.txt'     'a7to12.txt'  (typical case.  Last digit incremented)
#      'a7to99.txt'     'a8to00.txt'  (last digit incremented, with carry.)
#      'a9to99.txt'     'a0to00.txt'  (wrap around)
#      'cat.txt'        ' '           (no digits in input name.)
#      ' '              STOP!         (error.)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILE_NAME, the string to be incremented.
#
#    Output, string FILE_NAME_NEXT, the incremented string.
#
#
#  Because of Python's particular treatment of strings, (look up the
#  word "immutable"!) we IMMEDIATELY copy a string into a list, treating
#  the list like a normal data item, and then at the end, turning it back 
#  into a string.
#
  file_name_list = list ( file_name )

  flen = len ( file_name_list )

  if ( flen <= 0 ):
    print ( '' )
    print ( 'FILE_NAME_SEQUENCE - Fatal error!' )
    print ( '  The input file name is empty.' )
    exit ( 'FILE_NAME_SEQUENCE - Fatal error!' )

  change = 0

  for i in range ( flen - 1, -1, -1 ):

    c = file_name_list[i]

    if ( '0' <= c and c <= '8' ):

      change = change + 1

      c = chr ( ord ( c ) + 1 )
      
      file_name_list[i] = c

      break

    elif ( c == '9' ):

      change = change + 1

      c = '0'
      
      file_name_list[i] = c

  if ( change == 0 ):
    print ( '' )
    print ( 'FILE_NAME_SEQUENCE - Fatal error!' )
    print ( '  The input file name contains no digits to increment.' )
    exit ( 'FILE_NAME_SEQUENCE - Fatal error!' )

  file_name_next = "".join ( file_name_list )

  return file_name_next

def file_name_sequence_test ( ):

#*****************************************************************************80
#
## FILE_NAME_SEQUENCE_TEST tests FILE_NAME_SEQUENCE.
#
#  Discussion:
#
#    There are situations such as animations or parallel processing in which
#    it is necessary to generate a sequence of file names which include
#    an embedded index that increases.  A simple example might be
#
#      'fred0.txt', 'fred1.txt', 'fred2.txt'
#
#    A side issue arises when the number of files is large enough that the
#    number of digits in the index will vary.  Thus, if we are going to have
#    15 files, do we want to number them as
#
#      'fred00.txt' through 'fred14.txt'
#
#    which means, for one thing, that they will alphabetize properly, or
#    will we be satisfied with
#
#      'fred0.txt' through 'fred14.txt' ?
#
#    Schemes for generating such a sequence in MATLAB can involve the
#    NUM2STR function, the SPRINTF function, or a more elaborate function
#    called FILE_NAME_INC which searches a string for embedded numeric
#    data and increments it.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'FILE_NAME_SEQUENCE_TEST:' )
  print ( '  Python version' )
  print ( '  FILE_NAME_SEQUENCE generates a numeric sequence of file names.' )

  file_name_sequence_test01 ( 'frado_', '_lives.txt', 0, 12 )
  file_name_sequence_test02 ( 'fredo_', '_lives.txt', 0, 12 )
  file_name_sequence_test03 ( 'frido_', '_lives.txt', 0, 12 )
  file_name_sequence_test04 ( 'frodo_000_lives.txt', 12 )
#
#  Terminate.
#
  print ( '' )
  print ( 'FILE_NAME_SEQUENCE:' )
  print ( '  Normal end of execution.' )
  return

def file_name_sequence_test01 ( prefix, suffix, first, last ):

#*****************************************************************************80
#
## FILE_NAME_SEQUENCE_TEST01 uses concatenation and the str() function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'FILE_NAME_SEQUENCE_TEST01:' )
  print ( '  FILE_NAME = PREFIX + STR(I) + SUFFIX' )
  print ( '  PREFIX = "%s"' % ( prefix ) )
  print ( '  SUFFIX = "%s"' % ( suffix ) )
  print ( '  %d <= I <= %d' % ( first, last ) )
  print ( '  Numbers do NOT include leading zeros.' )
  print ( '' )

  for i in range ( first, last + 1 ):
    file_name = prefix + str ( i ) + suffix
    print ( '  %4d:  "%s"' % ( i, file_name ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FILE_NAME_SEQUENCE_TEST01:' )
  print ( '  Normal end of execution.' )
  return

def file_name_sequence_test02 ( prefix, suffix, first, last ):

#*****************************************************************************80
#
## FILE_NAME_SEQUENCE_TEST02 uses output formats.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'FILE_NAME_SEQUENCE_TEST02:' )
  print ( '  FILE_NAME(I) = \'%s%d%s\' % ( PREFIX, I, SUFFIX )' )
  print ( '  PREFIX = "%s"' % ( prefix ) )
  print ( '  SUFFIX = "%s"' % ( suffix ) )
  print ( '  %d <= I <= %d' % ( first, last ) )
  print ( '  Numbers do NOT include leading zeros.' )
  print ( '' )

  for i in range ( first, last + 1 ):
    file_name = '%s%d%s' % ( prefix, i, suffix )
    print ( '  %4d:  "%s"' % ( i, file_name ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FILE_NAME_SEQUENCE_TEST02:' )
  print ( '  Normal end of execution.' )
  return

def file_name_sequence_test03 ( prefix, suffix, first, last ):

#*****************************************************************************80
#
## FILE_NAME_SEQUENCE_TEST03 uses output formats.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'FILE_NAME_SEQUENCE_TEST03:' )
  print ( '  FILE_NAME(I) = \'%s%02d%s\' % ( PREFIX, I, SUFFIX )' )
  print ( '  PREFIX = "%s"' % ( prefix ) )
  print ( '  SUFFIX = "%s"' % ( suffix ) )
  print ( '  %d <= I <= %d' % ( first, last ) )
  print ( '  Numbers include leading zeros.' )
  print ( '' )

  for i in range ( first, last + 1 ):
    file_name = '%s%02d%s' % ( prefix, i, suffix )
    print ( '  %4d:  "%s"' % ( i, file_name ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FILE_NAME_SEQUENCE_TEST03:' )
  print ( '  Normal end of execution.' )
  return

def file_name_sequence_test04 ( file_name, file_name_num ):

#*****************************************************************************80
#
## FILE_NAME_SEQUENCE_TEST04 uses FILE_NAME_SEQUENCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'FILE_NAME_SEQUENCE_TEST04' )
  print ( '  FILE_NAME = FILE_NAME_INC ( FILE_NAME )' )
  print ( '  First FILE_NAME = "%s"' % ( file_name ) )
  print ( '  Number of file names = %d' % ( file_name_num ) )
  print ( '  Numbers may include leading zeros.' )
  print ( '' )
  i = 0
  print ( '  %4d:  "%s"' % ( i, file_name ) )

  for i in range ( 1, file_name_num + 1 ):
    file_name = file_name_sequence ( file_name )
    print ( '  %4d:  "%s"' % ( i, file_name ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FILE_NAME_SEQUENCE_TEST04:' )
  print ( '  Normal end of execution.' )
  return

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

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  file_name_sequence_test ( )
  timestamp ( )

