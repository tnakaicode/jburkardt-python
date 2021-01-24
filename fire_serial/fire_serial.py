#! /usr/bin/env python3
#
UNBURNT = 0
SMOLDERING = 1
BURNING = 2
BURNT = 3


def fire_serial(forest_size, prob_spread):

    # *****************************************************************************80
    #
    # FIRE_SERIAL simulates a fire in a rectangular forest of trees.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FOREST_SIZE, the number of trees in a horizontal
    #    or vertical line.
    #
    #    Input, real PROB_SPREAD, the probability that a burning tree will
    #    ignite a neighboring tree.
    #
    import platform

    print('')
    print('FIRE_SERIAL')
    print('  Python version: %s' % (platform.python_version()))
    print('  A probabilistic simulation of a forest fire.')
    print('  The forest is a square grid with %d trees on a side.' % (forest_size))
    print('  The probability of tree-to-tree spread is %g' % (prob_spread))
#
#  Initialize the random number generator.
#
    seed = 123456789
    print('  The random number generator is seeded by %d' % (seed))
#
#  Initialize the values in the forest.
#
    forest = forest_initialize(forest_size)
#
#  Choose a tree at random where the fire will start.
#
    i_ignite, seed = i4_uniform_ab(0, forest_size - 1, seed)
    j_ignite, seed = i4_uniform_ab(0, forest_size - 1, seed)
    tree_ignite(forest_size, forest, i_ignite, j_ignite)

    print('')
    print('  Fire starts at tree[%d,%d]' % (i_ignite, j_ignite))
#
#  Let time run until nothing is burning any more.
#
    while (forest_is_burning(forest_size, forest)):
        seed = forest_burns(forest_size, forest, seed, prob_spread)
#
#  Display the final forest state.
#
    forest_print(forest_size, forest, i_ignite, j_ignite)
#
#  Report the percentage of forest burned.
#
    percent = get_percent_burned(forest_size, forest)

    print('')
    print('  Percentage of forest burned = %g' % (percent))
#
#  Terminate.
#
    print('')
    print('FIRE_SERIAL:')
    print('  Normal end of execution.')
    return


def fire_spreads(seed, prob_spread):

    # *****************************************************************************80
    #
    # FIRE_SPREADS determines whether the fire spreads.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer SEED, a seed for the random
    #    number generator.
    #
    #    Input, real PROB_SPREAD, the probability of spreading.
    #
    #    Output, logical FIRE_SPREADS, is TRUE if the fire spreads.
    #
    #    Output, integer SEED, a seed for the random
    #    number generator.
    #
    u, seed = r8_uniform_01(seed)

    if (u < prob_spread):
        value = True
    else:
        value = False

    return value, seed


def forest_burns(forest_size, forest, seed, prob_spread):

    # *****************************************************************************80
    #
    # FOREST_BURNS models a single time step of the burning forest.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FOREST_SIZE, the linear dimension of the forest.
    #
    #    Input/output, integer FOREST(FOREST_SIZE,FOREST_SIZE), an
    #    array with an entry for each tree in the forest.
    #
    #    Input, integer SEED, a seed for the random
    #    number generator.
    #
    #    Input, real PROB_SPREAD, the probability that the fire will
    #    spread from a burning tree to an unburnt one.
    #
    #    Output, integer SEED, a seed for the random
    #    number generator.
    #

    #
    #  Burning trees burn down;
    #  Smoldering trees ignite;
    #
    for j in range(0, forest_size):
        for i in range(0, forest_size):
            if (forest[i, j] == BURNING):
                forest[i, j] = BURNT
            elif (forest[i, j] == SMOLDERING):
                forest[i, j] = BURNING
#
#  Unburnt trees might catch fire.
#
    for j in range(0, forest_size):
        for i in range(0, forest_size):

            if (forest[i, j] == BURNING):
                #
                #  North.
                #
                if (0 < i):
                    value, seed = fire_spreads(seed, prob_spread)
                    if (value and forest[i - 1, j] == UNBURNT):
                        forest[i - 1, j] = SMOLDERING
#
#  South.
#
                if (i < forest_size - 1):
                    value, seed = fire_spreads(seed, prob_spread)
                    if (value and forest[i + 1, j] == UNBURNT):
                        forest[i + 1, j] = SMOLDERING
#
#  West.
#
                if (0 < j):
                    value, seed = fire_spreads(seed, prob_spread)
                    if (value and forest[i, j - 1] == UNBURNT):
                        forest[i, j - 1] = SMOLDERING
#
#  East.
#
                if (j < forest_size - 1):
                    value, seed = fire_spreads(seed, prob_spread)
                    if (value and forest[i, j + 1] == UNBURNT):
                        forest[i, j + 1] = SMOLDERING

    return seed


def forest_initialize(forest_size):

    # *****************************************************************************80
    #
    # FOREST_INITIALIZE initializes the forest values.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FOREST_SIZE, the linear dimension of the forest.
    #
    #    Output, integer FOREST(FOREST_SIZE,FOREST_SIZE), an array
    #    with an entry for each tree in the forest.
    #
    import numpy as np

    forest = UNBURNT * np.zeros([forest_size, forest_size])

    return forest


def forest_is_burning(forest_size, forest):

    # *****************************************************************************80
    #
    # FOREST_IS_BURNING reports whether any trees in the forest are burning.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FOREST_SIZE, the linear dimension of the forest.
    #
    #    Input, integer FOREST(FOREST_SIZE,FOREST_SIZE), an array
    #    with an entry for each tree in the forest.
    #
    #    Output, logical FOREST_IS_BURNING, is TRUE if any tree in the forest
    #    is in the SMOLDERING or BURNING state.
    #
    value = False

    for j in range(0, forest_size):
        for i in range(0, forest_size):
            if (forest[i, j] == SMOLDERING or forest[i, j] == BURNING):
                value = True
                return value

    return value


def forest_print(forest_size, forest, i_ignite, j_ignite):

    # *****************************************************************************80
    #
    # FOREST_PRINT prints the state of the trees in the forest.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer ( kind = 4 ) FOREST_SIZE, the linear dimension of the forest.
    #
    #    Input, integer ( kind = 4 ) FOREST(FOREST_SIZE,FOREST_SIZE), an array
    #    with an entry for each tree in the forest.
    #
    #    Input, integer ( kind = 4 ) I_IGNITE, J_IGNITE, the location of the start
    #    of the fire.
    #
    import sys as sys

    print('')
    print('  Map of fire damage.')
    print('  Fire started at "*".')
    print('  Burned trees are indicated by "."')
    print('  Unburned trees are indicated by "X".')
    print('')

    for i in range(0, forest_size):
        sys.stdout.write('  ')
        for j in range(0, forest_size):
            if (i == i_ignite and j == j_ignite):
                sys.stdout.write('*')
            elif (forest[i, j] == BURNT):
                sys.stdout.write('.')
            else:
                sys.stdout.write('X')
        print('')

    return


def get_percent_burned(forest_size, forest):

    # *****************************************************************************80
    #
    # GET_PERCENT_BURNED computes the percentage of the forest that burned.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FOREST_SIZE, the linear dimension of the forest.
    #
    #   Input, integer FOREST(FOREST_SIZE,FOREST_SIZE), an array
    #    with an entry for each tree in the forest.
    #
    #    Output, real PERCENT, the percentage of the forest
    #    that burned.
    #
    total = 0
    for j in range(0, forest_size):
        for i in range(0, forest_size):
            if (forest[i, j] == BURNT):
                total = total + 1

    percent = float(total) / float(forest_size) / float(forest_size)

    return percent


def i4_uniform_ab(a, b, seed):

    # *****************************************************************************80
    #
    # I4_UNIFORM_AB returns a scaled pseudorandom I4.
    #
    #  Discussion:
    #
    #    The pseudorandom number will be scaled to be uniformly distributed
    #    between A and B.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer A, B, the minimum and maximum acceptable values.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer C, the randomly chosen integer.
    #
    #    Output, integer SEED, the updated seed.
    #
    from math import floor
    from sys import exit

    i4_huge = 2147483647

    seed = floor(seed)

    seed = (seed % i4_huge)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('I4_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('I4_UNIFORM_AB - Fatal error!')

    k = floor(seed / 127773)

    seed = 16807 * (seed - k * 127773) - k * 2836

    if (seed < 0):
        seed = seed + i4_huge

    r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
    a = round(a)
    b = round(b)

    r = (1.0 - r) * (min(a, b) - 0.5) \
        + r * (max(a, b) + 0.5)
#
#  Use rounding to convert R to an integer between A and B.
#
    value = round(r)

    value = max(value, min(a, b))
    value = min(value, max(a, b))
    value = int(value)

    return value, seed


def i4_uniform_ab_test():

    # *****************************************************************************80
    #
    # I4_UNIFORM_AB_TEST tests I4_UNIFORM_AB.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    a = -100
    b = 200
    seed = 123456789

    print('')
    print('I4_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4_UNIFORM_AB computes pseudorandom values')
    print('  in an interval [A,B].')
    print('')
    print('  The lower endpoint A = %d' % (a))
    print('  The upper endpoint B = %d' % (b))
    print('  The initial seed is %d' % (seed))
    print('')

    for i in range(1, 21):
        [j, seed] = i4_uniform_ab(a, b, seed)
        print('  %8d  %8d' % (i, j))
#
#  Terminate.
#
    print('')
    print('I4_UNIFORM_AB_TEST:')
    print('  Normal end of execution.')
    return


def r8_uniform_01(seed):

    # *****************************************************************************80
    #
    # R8_UNIFORM_01 returns a unit pseudorandom R8.
    #
    #  Discussion:
    #
    #    This routine implements the recursion
    #
    #      seed = 16807 * seed mod ( 2^31 - 1 )
    #      r8_uniform_01 = seed / ( 2^31 - 1 )
    #
    #    The integer arithmetic never requires more than 32 bits,
    #    including a sign bit.
    #
    #    If the initial seed is 12345, then the first three computations are
    #
    #      Input     Output      R8_UNIFORM_01
    #      SEED      SEED
    #
    #         12345   207482415  0.096616
    #     207482415  1790989824  0.833995
    #    1790989824  2035175616  0.947702
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 March 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.  SEED should not be 0.
    #
    #    Output, real R, a random value between 0 and 1.
    #
    #    Output, integer SEED, the updated seed.  This would
    #    normally be used as the input seed on the next call.
    #
    from math import floor
    from sys import exit

    i4_huge = 2147483647

    seed = floor(seed)

    seed = (seed % i4_huge)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8_UNIFORM_01 - Fatal error!')

    k = floor(seed / 127773)

    seed = 16807 * (seed - k * 127773) - k * 2836

    if (seed < 0):
        seed = seed + i4_huge

    r = seed * 4.656612875E-10

    return r, seed


def r8_uniform_01_test():

    # *****************************************************************************80
    #
    # R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_UNIFORM_01 produces a sequence of random values.')

    seed = 123456789

    print('')
    print('  Using random seed %d' % (seed))

    print('')
    print('  SEED  R8_UNIFORM_01(SEED)')
    print('')
    for i in range(0, 10):
        seed_old = seed
        x, seed = r8_uniform_01(seed)
        print('  %12d  %14f' % (seed, x))

    print('')
    print('  Verify that the sequence can be restarted.')
    print('  Set the seed back to its original value, and see that')
    print('  we generate the same sequence.')

    seed = 123456789
    print('')
    print('  SEED  R8_UNIFORM_01(SEED)')
    print('')

    for i in range(0, 10):
        seed_old = seed
        x, seed = r8_uniform_01(seed)
        print('  %12d  %14f' % (seed, x))
#
#  Terminate.
#
    print('')
    print('R8_UNIFORM_01_TEST')
    print('  Normal end of execution.')
    return


def tree_ignite(forest_size, forest, i_ignite, j_ignite):

    # *****************************************************************************80
    #
    # TREE_IGNITE sets a given tree to the SMOLDERING state.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2016
    #
    #  Author:
    #
    #    Python version by John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer FOREST_SIZE, the linear dimension of
    #    the forest.
    #
    #    Input, integer FOREST(FOREST_SIZE,FOREST_SIZE), an array
    #    with an entry for each tree in the forest.
    #
    #    Input, integer I_IGNITE, J_IGNITE, the coordinates of the
    #    tree which is to be set to SMOLDERING.
    #
    forest[i_ignite, j_ignite] = SMOLDERING


if (__name__ == '__main__'):
    timestamp()
    forest_size = 20
    prob_spread = 0.5
    fire_serial(forest_size, prob_spread)
    timestamp()
