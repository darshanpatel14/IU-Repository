# Logging
# used for debugging and the auditing

# Logging Levels
# DEBUG — This is used to log messages during programming debugging. It is very often applied in order to see returner values of variables and functions.
# INFO — This is used to log any information messages during program running.
# WARNING — This is used to log warning messages. It is very often applied in order to
# see preventing information that may have occurred during program running.
# ERROR — This is used to log error messages that occurred during program running.
# In general, these messages include specific error information, error line of code, date and time that the error occurred, function and module file names where the error occurred, etc.
# CRITICAL — This is used to log critical errors. It is very often applied in order to see generic program crashes.


# basic config
# level: This is the event severity level (DEBUG, INFO, WARNING, ERROR, and CRITICAL).
# filename: This is the file path and name.
# filemode: If filename is defined, the file is opened in this mode. The default is a,
# which means append.
# format: This is the message format.

import logging


def main():
    logging.basicConfig(filename="app.log", filemode="w",
                        format="%(name)s - %(levelname)s - %(message)s")
    logging.warning("This message gets logged as warning")

    # logging variable data
    name = "python"
    logging.error(f'{name} raised exception')


if __name__ == "__main__":
    main()
