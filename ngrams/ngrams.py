#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp

'''
Allows scoring of text using n-gram probabilities
17/07/12
'''


class ngram_score (object):

    # *****************************************************************************80
    #
    # NGRAM_SCORE is a class for the Ngram scoring program.
    #
    #  Author:
    #
    #    Unknown
    #
    def __init__(self, ngramfile, sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''

        import numpy as np

        self.ngrams = {}
        fh = open(ngramfile, 'rt')
        for line in fh:
            key, count = line.split(sep)
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.values())

        #
        #  Calculate log probabilities.
        #
        for key in self.ngrams.keys():
            self.ngrams[key] = np.log10(float(self.ngrams[key]) / self.N)
        self.floor = np.log10(0.01 / self.N)

    def score(self, text):
        ''' compute the score of text '''
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text) - self.L + 1):
            if text[i:i + self.L] in self.ngrams:
                score += ngrams(text[i:i + self.L])
            else:
                score += self.floor
        return score


def ngram_score_test1():

    # *****************************************************************************80
    #
    # NGRAM_SCORE_TEST1 tests text against monogram statistics.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('NGRAM_SCORE_TEST1:')
    print('  Python version: %s' % (platform.python_version()))
    print('  NGRAM_SCORE tests a string or text against English ngram statistics.')
    print('  Here we do a test against English monograms.')
    print('')
    print('  Apparently, you want to remove all nonalphabetic information,')
    print('  and uppercase your text.  But you may wish to preserve spaces.')
    print('')

    fitness = ngram_score('english_monograms.txt')

    #
    #  Notice that NGRAM_SCORE is affected by the case of the text,
    #  by spaces, and by punctuation.
    #
    s = 'HELLOWORLD'
    score = fitness.score(s)
    print('  %s length = %d, score = %g' % (s, len(s), score))

    s = 'HELLO WORLD'
    score = fitness.score(s)
    print('  %s length = %d, score = %g' % (s, len(s), score))

    s = 'helloworld'
    score = fitness.score(s)
    print('  %s length = %d, score = %g' % (s, len(s), score))

    s = 'HELLO, WORLD!'
    score = fitness.score(s)
    print('  %s length = %d, score = %g' % (s, len(s), score))

    s = 'Hello, world!'
    score = fitness.score(s)
    print('  %s length = %d, score = %g' % (s, len(s), score))

    #
    #  Read text from a file.
    #  Oddly enough, HELLOWORLD read from a file gives a different
    #  score from HELLOWORLD entered as a string.  It seems to have
    #  a terminating character.
    #
    f = 'HELLOWORLD.txt'
    file = open(f, 'r')
    t = file.read()
    t = str.upper(t)
    score = fitness.score(t)
    print('  %s length = %d, score = %g' % (f, len(t), score))
    file.close()

    #
    #  How do we feed it the text in a file?
    #
    f = 'desiderata.txt'
    file = open(f, 'r')
    t = file.read()
    t = str.upper(t)
    score = fitness.score(t)
    print('  %s length = %d, score = %g' % (f, len(t), score))
    file.close()

    print('')
    print('NGRAM_SCORE_TEST1:')
    print('  Normal end of execution.')


def ngram_score_test2():

    # *****************************************************************************80
    #
    # NGRAM_SCORE_TEST2 tests text against bigram statistics.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NGRAM_SCORE_TEST2:')
    print('  Python version: %s' % (platform.python_version()))
    print('  NGRAM_SCORE tests a string or text against English ngram statistics.')
    print('  Here we do a test against English bigrams.')
    print('')
    print('  Apparently, you want to remove all nonalphabetic information,')
    print('  and uppercase your text.  But you may wish to preserve spaces.')
    print('')

    fitness = ngram_score('english_bigrams.txt')
    #
    #  Notice that NGRAM_SCORE is affected by the case of the text,
    #  by spaces, and by punctuation.
    #
    s = 'HELLOWORLD'
    score = fitness.score(s)
    print('  %s length = %d, score = %g' % (s, len(s), score))

    s = 'HELLO WORLD'
    score = fitness.score(s)
    print('  %s length = %d, score = %g' % (s, len(s), score))

    s = 'helloworld'
    score = fitness.score(s)
    print('  %s length = %d, score = %g' % (s, len(s), score))

    s = 'HELLO, WORLD!'
    score = fitness.score(s)
    print('  %s length = %d, score = %g' % (s, len(s), score))

    s = 'Hello, world!'
    score = fitness.score(s)
    print('  %s length = %d, score = %g' % (s, len(s), score))
    #
    #  Read text from the file "HELLOWORLD.txt".
    #  Oddly enough, HELLOWORLD read from a file gives a different
    #  score from HELLOWORLD entered as a string.  It seems to have
    #  a terminating character.
    #
    f = 'HELLOWORLD.txt'
    file = open(f, 'r')
    t = file.read()
    t = str.upper(t)
    score = fitness.score(t)
    print('  %s length = %d, score = %g' % (f, len(t), score))
    file.close()
    #
    #  Read text from the file "desiderata.txt".
    #
    f = 'desiderata.txt'
    file = open(f, 'r')
    t = file.read()
    t = str.upper(t)
    score = fitness.score(t)
    print('  %s length = %d, score = %g' % (f, len(t), score))
    file.close()

    print('')
    print('NGRAM_SCORE_TEST2:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    ngram_score_test1()
    ngram_score_test2()
    timestamp()
