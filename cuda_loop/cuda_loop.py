#! /usr/bin/env python3
#


def cuda_loop(blocks, threads, n):

    # *****************************************************************************80
    #
    # CUDA_LOOP simulates the behavior of a CUDA loop.
    #
    #  Discussion:
    #
    #    A CUDA kernel "kernel()" is invoked by a command of the form
    #
    #      kernel << blocks, threads >> ( args )
    #
    #    where blocks and threads are each vectors of up to 3 values,
    #    listing the number of blocks and number of threads to be used.
    #
    #    If a problem involves N tasks, then tasks are allotted to
    #    specific CUDA processes in an organized fashion.  Some processes
    #    may get no tasks, one task, or multiple tasks.
    #
    #    Each process is given variables that can be used to determine
    #    the tasks to be performed:
    #
    #      gridDim.x, gridDim.y, gridDim.z: the block dimensions as
    #      given by the user in "blocks"
    #
    #      blockDim.x, blockDim.y, blockDim.z: the thread dimensions as
    #      given by the user in "threads"
    #
    #      blockIdx.x, blockIdx.y, blockId.z: the block indices for this process.
    #
    #      threadIdx.x, threadIdx.y, threadIdx.z: the thread indices for this process.
    #
    #    Essentially, a process can determine its linear index K by:
    #
    #      K = threadIdx.x
    #        +  blockdim.x  * threadIdx.y
    #        +  blockDim.x  *  blockDim.y  * threadIdx.z
    #        +  blockDim.x  *  blockDim.y  *  blockDim.z  * blockIdx.x
    #        +  blockDim.x  *  blockDim.y  *  blockDim.z  *  gridDim.x  * blockIdx.y
    #        +  blockDim.x  *  blockDim.y  *  blockDim.z  *  gridDim.x  *  gridDim.y  * blockIdx.z
    #
    #    Set task T = K.
    #
    #    while ( T < N )
    #      carry out task T
    #      T = T + blockDim.x * blockDim.y * blockDim.z * gridDim.x * gridDim.y * gridDim.z.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer BLOCKS[3], the CUDA block values.  These should be nonnegative.
    #    Typically, the third entry is 1.  Generally, the first two values cannot
    #    be greater than 35,535.
    #
    #    Input, integer THREADS[3], the CUDA thread values.  These should be nonnegative.
    #    Typically, there is a maximum value imposed on these quantities, which
    #    depends on the GPU model.
    #
    #    Input, integer N, the number of tasks to be carried out.
    #
    print("")
    print("CUDA_LOOP:")
    print("  Simulate the assignment of N tasks to the blocks")
    print("  and threads of a GPU using CUDA.")
    print("")
    print("  Number of tasks is %d" % (n))
    print("  BLOCKS:  { %d, %d, %d }" % (blocks[0], blocks[1], blocks[2]))
    print("  THREADS: { %d, %d, %d }" % (threads[0], threads[1], threads[2]))

    k1 = 0

    blockDimx = threads[0]
    blockDimy = threads[1]
    blockDimz = threads[2]

    gridDimx = blocks[0]
    gridDimy = blocks[1]
    gridDimz = blocks[2]

    chunk = blocks[1] * blocks[0] * threads[2] * threads[1] * threads[0]
    print("  Total threads = %d" % (chunk))
    print("")
    print("  Process   Process (bx,by,bz) (tx,ty,tz)  Tasks...")
    print("  Increment Formula")
    print("")

    for blockIdz in range(0, gridDimz):
        for blockIdy in range(0, gridDimy):
            for blockIdx in range(0, gridDimx):
                for threadIdz in range(0, blockDimz):
                    for threadIdy in range(0, blockDimy):
                        for threadIdx in range(0, blockDimx):
                            t = k1
                            k2 = \
                                threadIdx \
                                + blockDimx * threadIdy \
                                + blockDimx * blockDimy * threadIdz \
                                + blockDimx * blockDimy * blockDimz * blockIdx \
                                + blockDimx * blockDimy * blockDimz * gridDimx * blockIdy \
                                + blockDimx * blockDimy * blockDimz * gridDimx * gridDimy * blockIdz

                            print("  %7d  %7d: (%2d,%2d,%2d) (%2d,%2d,%2d)" %
                                  (k1, k2, blockIdx, blockIdy, blockIdz, threadIdx, threadIdy, threadIdz), end='')
                            while (t < n):
                                print("%3d" % (t)),
                                t = t + chunk
                            print("")
                            k1 = k1 + 1

    return


def cuda_loop_test():

    # *****************************************************************************80
    #
    # CUDA_LOOP_TEST demonstrates CUDA_LOOP.
    #
    #  Discussion:
    #
    #    A CUDA kernel "kernel()" is invoked by a command of the form
    #
    #      kernel << blocks, threads >> ( args )
    #
    #    where blocks and threads are each vectors of up to 3 values,
    #    listing the number of blocks and number of threads to be used.
    #
    #    If a problem involves N tasks, then tasks are allotted to
    #    specific CUDA processes in an organized fashion.  Some processes
    #    may get no tasks, one task, or multiple tasks.
    #
    #    Each process is given variables that can be used to determine
    #    the tasks to be performed:
    #
    #      gridDim.x, gridDim.y, gridDim.z: the block dimensions as
    #      given by the user in "blocks"
    #
    #      blockDim.x, blockDim.y, blockDim.z: the thread dimensions as
    #      given by the user in "threads"
    #
    #      blockIdx.x, blockIdx.y, blockId.z: the block indices for this process.
    #
    #      threadIdx.x, threadIdx.y, threadIdx.z: the thread indices for this process.
    #
    #    Essentially, a process can determine its linear index K by:
    #
    #      K = threadIdx.x
    #        +  blockdim.x  * threadIdx.y
    #        +  blockDim.x  *  blockDim.y  * threadIdx.z
    #        +  blockDim.x  *  blockDim.y  *  blockDim.z  * blockIdx.x
    #        +  blockDim.x  *  blockDim.y  *  blockDim.z  *  gridDim.x  * blockIdx.y
    #        +  blockDim.x  *  blockDim.y  *  blockDim.z  *  gridDim.x  *  gridDim.y  * blockIdx.z
    #
    #    Set task T = K.
    #
    #    while ( T < N )
    #      carry out task T
    #      T = T + blockDim.x * blockDim.y * blockDim.z * gridDim.x * gridDim.y * gridDim.z.
    #
    #    This program suggests how a specific set of block and thread parameters
    #    would determine the assignment of individual tasks to CUDA processes.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Local, integer BLOCKS[3], the CUDA block values.  These should be nonnegative.
    #    Typically, the third entry is 1.  Generally, the first two values cannot
    #    be greater than 35,535.
    #
    #    Local, integer THREADS[3], the CUDA thread values.  These should be nonnegative.
    #    Typically, there is a maximum value imposed on these quantities, which
    #    depends on the GPU model.
    #
    #    Local, integer N, the number of tasks to be carried out.
    #
    import numpy as np

    print("")
    print("CUDA_LOOP_TEST:")
    print("  Python version")
    print("  Simulate the way CUDA breaks up an iterative task, using")
    print("  blocks and threads.")
#
#  Linear array of blocks and threads.
#  Essentially, blocks = your hands and threads = your fingers.
#  Now count up to 23.
#
    blocks = np.array([2, 1, 1])
    threads = np.array([5, 1, 1])
    n = 23
    cuda_loop(blocks, threads, n)
#
#  Unit arrays of blocks and threads.
#  Waste your GPU by having a single block and thread do everything.
#
    blocks = np.array([1, 1, 1])
    threads = np.array([1, 1, 1])
    n = 23
    cuda_loop(blocks, threads, n)
#
#  2D block array, 3D thread array.
#  More processes than tasks.
#
    blocks = np.array([2, 3, 1])
    threads = np.array([2, 1, 4])
    n = 40
    cuda_loop(blocks, threads, n)
#
#  One block, 8 threads.
#
    blocks = np.array([1, 1, 1])
    threads = np.array([2, 2, 2])
    n = 23
    cuda_loop(blocks, threads, n)
#
#  Terminate.
#
    print("")
    print("CUDA_LOOP_TEST:")
    print("  Normal end of execution.")
    return


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

    t = time.time()
    print(time.ctime(t))

    return None


if (__name__ == '__main__'):
    timestamp()
    cuda_loop_test()
    timestamp()
