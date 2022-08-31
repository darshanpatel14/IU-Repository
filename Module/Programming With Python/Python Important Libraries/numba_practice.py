# Numba is an open source JIT compiler that translates a subset of Python and NumPy code into fast machine code at run time.
# It is the most common program used to speed up Python programs today.
# It was specifically designed for scientific computing with NumPy arrays and functions.
# Numba can automatically execute NumPy array expressions on multiple CPU cores,
# which makes it easy to write paral- lel loops.

import time
from numba import jit
import numpy as np


@jit(nopython=True)
def sum2dimensional(np_array):
    array_rows, array_columns = np_array.shape
    result = 0.0
    for i in range(array_rows):
        for j in range(array_columns):
            result += np_array[i, j]
    return result


def main():
    np_array = np.arange(100000000).reshape(10000, 10000)
    print("Sum calculation: {}".format(sum2dimensional(np_array)))


if __name__ == '__main__':

    # method of time module in python is used to get
    # the current processor time as floating point number
    # expressed in second

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    diff_time = end_time - start_time
    result = time.strftime("%H:%M:%S", time.gmtime(diff_time))
    print("program runtime: {}".format(result))
