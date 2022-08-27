# use for reading and writing data from files
# The access mode defined in the “open(mode, [buffering])” function selects the action related to the file
# These modes are:

# “r” — read mode, which is used when the file is only being read.
# “w” — write mode, which is used to edit and write new information to the file (any
# existing files with the same name will be erased when this mode is activated).
# “a” — appending mode, which is used to add new data to the end of the file. New
# information is automatically appended to the end.
# “r+” — special read and write mode, which is used to handle both actions when wor-
# king with a file.


# write function
# to write in file

from pathlib import Path, PureWindowsPath


def main():
    file_test = open("test.txt", "w")
    file_test.write("Python is a great programming language.\nSure!\n")
    file_test.close()

    # append data to the same file
    file_test = open("test.txt", "a")
    file_test.write("new line added")
    file_test.close()

    # read data from the same file
    file_test = open("test.txt", "r")
    print(file_test.read())

    # loop through line by line need to use for loop
    file_test = open("test.txt", "r")
    for item in file_test:
        print(item)

    # If you would like to return one line from the file,
    # the method “readline()” can be used.
    # The general syntax of this method is “file.readline(size)”
    # where the “size” parameter is optional.
    # It represents the number of bytes from the line that will return.
    # The default number is —1, which indicates the whole line.

    file_test = open("test.txt", "r")
    lines = file_test.readline(10)
    print(lines)

    # till now we can create file on current working directory
    # pathlib help to create file on system directory
    folder_path = Path(
        r"C: / folder_path/eclipse-workspace/iuds_fernstudium /src/1.4_input_output")
    file_name = "test.txt"
    file_path_name = folder_path / file_name
    file_test = open(file_path_name, "r")
    for item in file_test:
        print(item)

    # content of the text file can be read without
    # looping through
    folder_path = Path(
        r"C:/folder_path/eclipse-workspace/iubh_fernstudium/src/1.4_input_output")
    file_name = "test.txt"
    file_path_name = folder_path / file_name
    print(file_path_name.read_text())

    # The “Path()” object can explicitly convert a Unix path into a Windows-formatted path.
    folder_path = Path(
        r"C:/Users/ebonat/eclipse-workspace/iubh_fernstudium/src/1.4_input_output")
    file_name = "test.txt"
    file_path_name = folder_path / file_name
    path_on_windows = PureWindowsPath(file_path_name)
    print(path_on_windows)


if __name__ == '__main__':
    main()
