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

sys.path.append(os.path.join("./"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp


if (__name__ == '__main__'):
    timestamp()
