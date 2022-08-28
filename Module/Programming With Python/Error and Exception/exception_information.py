# The built-in sys.exc_info() function returns a tuple of three values (type, value, traceback)
# that all give information about the exception that is currently being handled.
# These parameters mean the following:


# type — This finds out the type of the exception being handled.
# value — This finds out the exception instance type.
# traceback — This finds a traceback object that encapsulates the call stack at the
# point where the exception originally occurred.

# exception_type, exception_value, exception_traceback = sys.exc_info()


# Traceback
# Traceback is an object that contains the information of the statements
# like where the call made in the specific line
# this obj returns a tuple of following params
# 1.File Name
# 2.Line Number
# 3.Method Name
# 4.line code


import sys
import traceback


def main():
    division_by_zero = 1/0
    print(division_by_zero)


if __name__ == '__main__':
    main()


# exception type - zero division error
# exception value - division by zero
