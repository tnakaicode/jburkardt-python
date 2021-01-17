#! /usr/bin/env python
#
def average_length():

    # *****************************************************************************80
    #
    # AVERAGE_LENGTH estimates the average length of a one-player game.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('AVERAGE_LENGTH')
    print('  Python version: %s' % (platform.python_version()))
    print('  Estimate the average length of a game of snakes and ladders.')

    games = 0
    total = 0

    while (games < 1000):
        games = games + 1
        n = game_length()
        total = total + n

    average = total / 1000
    print('Average number of moves is %d' % (average))

    print('')
    print('AVERAGE_LENGTH')
    print('  Normal end of execution.')


def game_length():

    # *****************************************************************************80
    #
    # GAME_LENGTH plays a randomly selected game and returns the number of moves.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 September 2014.
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, integer S, the number of moves.
    #
    import numpy as np

    from numpy.random import random_integers
#
#  Set up the snakes and ladders.
#
    final = np.linspace(0, 100, 101, dtype=np.int32)

    final[1] = 38
    final[4] = 14
    final[9] = 31
    final[16] = 6
    final[21] = 42
    final[28] = 84
    final[36] = 44
    final[48] = 26
    final[49] = 11
    final[51] = 67
    final[56] = 53
    final[62] = 10
    final[64] = 60
    final[71] = 91
    final[80] = 100
    final[87] = 24
    final[93] = 73
    final[95] = 75
    final[98] = 78
#
#  Initial position is 0.
#
    i = 0
    s = 0
#
#  Play until you reach 100.
#
    while (i < 100):
        s = s + 1
        d = random_integers(1, 6)
        i = i + d
        if (100 < i):
            i = 100
        i = final[i]

    return s


def game_length_test():

    # *****************************************************************************80
    #
    # GAME_LENGTH_TEST tests GAME_LENGTH.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 September 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('GAME_LENGTH_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  GAME_LENGTH reports the length of a single random game of Snakes and Ladders.')

    n = game_length()

    print('')
    print('  This random game took %d moves.' % (n))
#
#  Terminate.
#
    print('')
    print('GAME_LENGTH_TEST')
    print('  Normal end of execution.')

    return


def one_game():

    # *****************************************************************************80
    #
    # ONE_GAME plays one game of Snakes and Ladders, printing every move.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 September 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    from numpy.random import random_integers
#
#  FINAL[I] indicates where you end up if your die roll takes you to square I.
#
    final = np.linspace(0, 100, 101, dtype=np.int32)

    final[1] = 38
    final[4] = 14
    final[9] = 31
    final[16] = 6
    final[21] = 42
    final[28] = 84
    final[36] = 44
    final[48] = 26
    final[49] = 11
    final[51] = 67
    final[56] = 53
    final[62] = 10
    final[64] = 60
    final[71] = 91
    final[80] = 100
    final[87] = 24
    final[93] = 73
    final[95] = 75
    final[98] = 78
#
#  Initial position is 0.
#
    i = 0
    moves = 0
#
#  Play until you reach 100.
#
    while (i < 100):
        d = random_integers(1, 6)
        moves = moves + 1
        print('You rolled %d ' % (d), end='')
        i = i + d
        print('and moved to %d ' % (i), end='')
        if (100 < i):
            i = 100
            print('and moved back to %d ' % (i), end='')
        if (i < final[i]):
            i = final[i]
            print('and took a ladder up to %d ' % (i), end='')
        elif (final[i] < i):
            i = final[i]
            print('and took a snake down to %d' % (i), end='')

        if (100 <= i):
            print('and you won after %d moves!' % moves)
        else:
            print('.')


if (__name__ == '__main__'):
    one_game()
    game_length_test()
    average_length()
