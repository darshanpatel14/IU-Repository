# Based on this file, the data preprocessing requirements document will include the fol- lowing points:
# Drop duplicated rows and keep the first.
# Replace empty values with the mean value in columns 1 and 2.
# Replace empty values with the median value in column 3.
# Replace empty values with the “club” string in column 4.
# Replace empty values with the true boolean in column 5.
# Replace empty values with the current date in column 6.
# Replace empty values with the £0.0 in column 7.
# Remove the first character (English pound symbol) in column 8.
# Substitute the abbreviation in column 8.
# Define x column labels.
# Define y column target.
# Save the final file as “output_data.csv”. File location path must be defined.

import os
import sys
import datetime
import pandas as pd
import numpy as np
import config


def main():

    print("using pandas library for data manipulation and cleansing:")
    print()

    project_directory_path = os.path.dirname(sys.argv[0])
    print("project directory path:")
    print(project_directory_path)
    print()

    input_file_path = os.path.join(project_directory_path,
                                   config.INPUT_FILE_PATH)
    print("input file path:")
    print(input_file_path)
    print()

    output_file_path = os.path.join(project_directory_path,
                                    config.OUTPUT_FILE_PATH)
    print("output file path:")
    print(output_file_path)
    print()

    df_input_file = pd.read_csv(filepath_or_buffer=input_file_path, sep=",",
                                encoding="latin1")
    print("pandas data frame for input file:")
    print(df_input_file)
    print()

    print("number of rows and columns:")
    print(df_input_file.shape)
    print()

    print("summary descriptive stats for numerical columns:")
    print(df_input_file.describe())
    print()

    df_result = df_input_file["four"].value_counts()
    print("frequency distribution for categorical column four:")
    print(df_result)
    print()

    df_result = df_input_file["eight"].value_counts()
    print("frequency distribution for categorical column eight:")
    print(df_result)
    print()

    df_result = df_input_file.apply(lambda x: sum(x.isnull()), axis=0)
    print("missing values (nan) by columns:")
    print(df_result)
    print()

    df_result = df_input_file.duplicated()
    print("duplicated rows:")
    print(df_result)
    print()

    df_input_file = df_input_file.drop_duplicates(keep="first")
    print("drop duplicated rows and keep the first:")
    print(df_input_file)
    print()

    df_input_file = df_input_file.fillna(df_input_file.mean()["one":"two"])
    print("replace nan values with the mean value in columns one and two:")
    print(df_input_file)
    print()

    df_input_file = df_input_file.fillna(df_input_file.median()[:"three"])
    print("replace nan values with the median value in column three:")
    print(df_input_file)
    print()

    df_input_file["four"] = df_input_file["four"].fillna("club")
    print("replace nan values with the 'club' string in column four:")
    print(df_input_file)
    print()

    df_input_file["five"] = df_input_file["five"].fillna(True)
    print("replace nan values with the true boolean in column five:")
    print(df_input_file)
    print()

    now = datetime.datetime.now().strftime("%m/%d/%Y")
    df_input_file["six"] = df_input_file["six"].fillna(str(now))
    df_input_file["six"] = pd.to_datetime(df_input_file["six"])
    print("replace nan values with the current date in column six:")
    print(df_input_file)
    print()

    df_input_file["seven"] = df_input_file["seven"].fillna("£0.0")
    print("replace nan values with the £0.0 in column seven:")
    print(df_input_file)
    print()

    df_input_file["seven"] = df_input_file["seven"].map(lambda x: str(x)[1:])
    print("remove the first character (English pound symbol) in column seven:")
    print(df_input_file)
    print()

    df_input_file["eight"].replace(to_replace=dict(BMC="BioMed Central",
                                                   ACS="American Chemical Society",
                                                   BPS="Biophysical Society",
                                                   CJS="Cadmus Journal Services",
                                                   FM="Frontiers Media"), inplace=True)
    print("substitute the abbreviation in column eight:")
    print(df_input_file)
    print()

    x = df_input_file.drop(labels="eight", axis=1)
    print("x: labels by dropping column eight:")
    print(x)
    print()

    x = df_input_file.iloc[:, 0:6].values
    print("x: labels selection by using index location method ilo():")
    print(x)
    print()
    y = df_input_file["eight"]
    print("y: target selection by column eight:")
    print(y)
    print()

    y = df_input_file.iloc[:, 7].values
    print("y: target selection by using index location method ilo():")
    print(y)
    print()

    df_input_file.to_csv(output_file_path, encoding="latin1")
    print("the output file has been created successfully:")
    print(output_file_path)
    print()


if __name__ == '__main__':
    main()
