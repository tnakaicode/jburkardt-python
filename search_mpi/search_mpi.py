#! /usr/bin/env python3
#
def search_mpi(a, b, c):

# *****************************************************************************80
#
# SEARCH_MPI searches for a solution to an integer equation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the lower limit of the search.
#
#    Input, integer B, the upper limit of the search.
#
#    Input, integer C, the desired value.
#
#    Output, integer J, is:
#    -1, if no solution could be found.
#    otherwise, F(J) = C and A <= J <= B.
#
	import numpy
	import sys
	from mpi4py import MPI

	comm = MPI.COMM_WORLD

	id = comm.Get_rank()

	p = comm.Get_size()

	if (id == 0):
		print('')
		print('SEARCH_MPI:')
		print('  Python/MPI version')
		print('  Search the integers from A to B')
		print('  for a value J such that F(J) = C.')
		print('')
		print('  Use MPI to divide the computation among')
		print('  %d processes.' % (p))
		print('')
		print('  A        = %d' % (a))
		print('  B        = %d' % (b))
		print('  C        = %d' % (c))
		wtime = MPI.Wtime()

	j = search_partial(a, b, c, id, p)

	if (j != -1):
		print('  Process %d found J = %d' % (id, j))
		print('  Verify F(J) = %d' % (f(j))

	if (id == 0):
		wtime=MPI.Wtime() - wtime
		print('  Time     = %g' % (wtime))
#
#  Terminate.
#
	print('')
	print('SEARCH_MPI:')
	print('  Normal end of execution.')
	return j

def search_partial(a, b, c, id, p):

# *****************************************************************************80
#
# SEARCH_PARTIAL searches 'partially' through [A,B] for a J so that F(J) = C.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, B, the search range.
#
#    Input, integer C, the desired function value.
#
#    Input, integer ID, the increment between successive values that
#    are to be checked.
#
#    Input, integer P, the number of processes.
#
#    Output, integer J, the computed solution, or -1
#    if no solution was found.
#
	for i in range(a + id, b + 1, p):

		if (f(i) == c):
			return i

	return (- 1)

def f(i):

# *****************************************************************************80
#
# F is the function we are analyzing.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the argument.
#
#    Input, integer VALUE, the value.
#
	i4_huge=2147483647

	value=i

	for j in range(0, 5):

		k=(value // 127773)

		value=16807 * (value - k * 127773) - k * 2836

		if (value <= 0):
			value=value + i4_huge

	return value

def timestamp():

# *****************************************************************************80
#
# TIMESTAMP prints the date as a timestamp.
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

	t=time.time()
	print(time.ctime(t))

	return None

def timestamp_test():

# *****************************************************************************80
#
# TIMESTAMP_TEST tests TIMESTAMP.
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

	print('')
	print('TIMESTAMP_TEST:')
	print('  Python version: %s' % (platform.python_version()))
	print('  TIMESTAMP prints a timestamp of the current date and time.')
	print('')

	timestamp()
#
#  Terminate.
#
	print('')
	print('TIMESTAMP_TEST:')
	print('  Normal end of execution.')
	return

if (__name__ == '__main__'):
	timestamp()
	search_mpi(1, 10000, 45)
	search_mpi(1, 100000, 45)
	search_mpi(1, 1000000, 45)
	search_mpi(1674924000, 1674924999, 45)
	timestamp()
