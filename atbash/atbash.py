#! /usr/bin/env python3
#
def atbash_encrypt ( plain ):

#*****************************************************************************80
#
## ATBASH_ENCRYPT encrypts a string using the ATBASH code.
#
#  Discussion:
#
#    Only the alphabetic characters will be encrypted.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string PLAIN(*), the string to be encrypted.
#
#    Output, string CRYPT(*), the encrypted version of the string.
#

#
#  How long is the plain text?
#
  n = len ( plain ) 
#
#  Initialize the encrypted string to the plain text.  This way,
#  nonalphabetic characters are passed through.
#
  crypt = ''
#
#  Convert plain text characters to unsigned integers,
#  and reverse the index.
#
  for i in range ( 0, n ):
    ival = ord ( plain[i] )
    if ( ord ( 'a' ) <= ival and ival <= ord ( 'z' ) ):
      jval = ord ( 'a' ) + ord ( 'z' ) - ival
      crypt = crypt + chr ( jval )
    elif ( ord ( 'A' ) <= ival and ival <= ord ( 'Z' ) ):
      jval = ord ( 'A' ) + ord ( 'Z' ) - ival
      crypt = crypt + chr ( jval )
    else:
      crypt = crypt + plain[i]
      
  return crypt

def atbash_test ( ):

#*****************************************************************************80
#
## ATBASH_TEST tests ATBASH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 October 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ATBASH_TEST\n' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ATBASH_ENCRYPT encrypts a plain text using the Atbash' )
  print ( '  substitution cipher.' )
  print ( '  ATBASH_ENCRYPT can also decrypt an encryted text.' )
#
#  Test 1
#
  plain = 'A man, a plan, a canal - Panama!'
  crypt = atbash_encrypt ( plain )
  decrypt = atbash_encrypt ( crypt )
  print ( '' )
  print ( 'PLAIN:   "%s"' % ( plain ) )
  print ( 'CRYPT:   "%s"' % ( crypt ) )
  print ( 'DECRYPT: "%s"' % ( decrypt ) )
#
#  Test 2.
#
  plain = 'There are a thousand hacking at the branches of evil for every one who is striking at its root.'
  crypt = atbash_encrypt ( plain )
  crypt2 = atbash_encrypt ( crypt )
  print ( '\n' )
  print ( 'PLAIN:   "%s"' % ( plain ) )
  print ( 'CRYPT:   "%s"' % ( crypt ) )
  print ( 'DECTYPT: "%s"' % ( crypt2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ATBASH_TEST' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  atbash_test ( )
  timestamp ( )
