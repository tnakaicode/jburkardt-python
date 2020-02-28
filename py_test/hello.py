#! /usr/bin/env python3
#
import platform
import time

t = time.time()
print ( time.ctime(t) )

print ( '' )
print ( 'HELLO:' )
print ( '  Python version: %s' % ( platform.python_version ( ) ) )
print ( '  This is how to say' )
print ( '' )
print ( '  Hello, world!' )
print ( '' )

t = time.time()
print ( time.ctime(t) )
