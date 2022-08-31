# Numpy Library
# The NumPy library is used in almost all numerical computation in Python.
# We can say that NumPy could be the most important library for the whole Python Data Ecosystem package.
# It provides high-performance vector, matrix, and higher-dimensional data structures for Python.
# It writes in C and FORTRAN, meaning that when the math calculations are formulated with vectors and matrices,
# the performance is very high.


# Numpy Array
# NumPy array is a central data structure of the Installing Python libraries.
# It provides a collection of tools for high-performance multidimensional array objects
# and is a powerful data structure for the efficient computation of arrays and matrices.
# To work with these arrays, there is a vast amount of high-level mathematical functions
# that operate on the matrices and arrays.
# We will now look at the following one-dimensional array creation.

import numpy as np


def main():
    print("numpy version: {}".format(np.__version__))

    np_array = a = np.array([1, 2, 3, 4])
    print("creates array from list")
    print(np.array(np_array))

    np_array = a = np.array((1, 2, 3, 4))
    print("creates array from tuple")
    print(np_array)

    np_shape = np_array.shape
    print('one dimensional array shape, 4 elements : ')
    print(np_shape)

    np_array = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
    print("two dimensional array")
    print(np_array)

    np_shape = np_array.shape
    print(np_shape)

    np_array = a = np.array((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    np_reshape = np_array.reshape(5, 2)
    print(np_reshape)

    np_dim = np_array.ndim
    print(np_dim)

    np_dtype = np_array.dtype
    print(np_dtype)

    np_itemsize = np_array.itemsize
    print(np_itemsize)

    np_data = np_array.data
    print("The buffer containing the actual element if the array. dont need ot for calculations")
    print(np_data)

    array_1 = np.array([1, 2, 3, 4, 5])
    array_2 = np.array([6, 7, 8, 9, 10])

    array_result = array_1 + array_2
    print("additional operation :")
    print(array_result)

    array_result = array_1 - array_2
    print("substration operation :")
    print(array_result)

    array_result = array_2 - array_1
    print("substration operation :")
    print(array_result)

    array_result = array_1 / array_2
    print("division operation :")
    print(array_result)

    np_corrcoef = np.corrcoef(array_1, array_2)
    print("person product-moment correlation coefficients")
    print(np_corrcoef)

    np_mean = np.mean(array_1)
    print("arithmetic mean: ")
    print(np_mean)

    np_average = np.average(array_1)
    print("weighted average: ")
    print(np_average)

    np_median = np.median(array_1)
    print("median:")
    print(np_median)

    np_variance = np.var(array_1)
    print("variance:")
    print(np_variance)

    np_min = np.min(array_1)
    print("minimum:")
    print(np_min)

    np_max = np.max(array_1)
    print("maximum:")
    print(np_max)

    np_summa = np.sum(array_1)
    print("summa:")
    print(np_summa)


if __name__ == '__main__':
    main()
