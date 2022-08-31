# 1. Series — This is a one-dimensional labeled array that can hold any data type,
# for example, integers, strings, floating point numbers, Python objects, etc.
# The axis labels are collectively referred to as the index.
# A series can be created as

# s_data = pd.Series(data, ...)

# whereas “data” can be Python dictionary,
# ndarray (n-dimensional array or any scalar value), etc.


import numpy as np
import pandas as pd


def main():
    print("pandas version: {}".format(pd.__version__))
   # randn(): return a sample (or samples) from the standard normal distribution
    s_data = pd.Series(np.random.randn(5))
    print(s_data)


if __name__ == '__main__':
    main()


# 2. DataFrames — This is a two||-dimensional labeled data structure with rows and columns that have the same or different data types.
# It is similar to a Microsoft Excel spreadsheet or SQL database table objects.
# The first column of this component is reserved for the index values.
# If these values are not defined, pandas will automatically generate integers starting with zero.
# This component is the most useful in machine learning projects for data manipulation today.
# Below is the code that demonstrates how to create a pandas DataFrame object:
#    df_data = pd.DataFrame(data, ...)

def main():

 # create a dataframe from a dictionary
    dictionary = {"col 1": [1., 2., 3., 4., 5.], "col 2": [6, 7, 8, 9, 10],
                  "col 3": ["uno", "dos", "tres", "cuatro", "cinco"]}
    df_data = pd.DataFrame(data=dictionary)
    print(df_data)

    #     create a dataframe from a dictionary with text row numbers indexes
    df_data = pd.DataFrame(data=dictionary, index=["row1", "row2", "row3",
                                                   "row4", "row5"])
    print(df_data)

    # to read data from the csv file
    df_input_file = pd.read_csv(filepath_or_buffer="input_file_with_nan.csv")
    print(df_input_file)


if __name__ == '__main__':
    main()
