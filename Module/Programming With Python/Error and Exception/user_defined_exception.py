# class MyException(Exception):

#     def __init__(self, *args, **kwargs):
#         super().__init__(self, *args, **kwargs)


# class MyIndexError(IndexError):
#     def __init__(self, *args, **kwargs):
#         super().__init__(self, *args, **kwargs)


class MyException(Exception):

    def __init__(self, exception_parameter, exception_message):
        super().__init__(self, exception_parameter, exception_message)


def main():
    programming_language = ['JavaScript', 'Java', 'C', 'Ruby', 'C++']
    for item in programming_language:
        if item != 'Python':
            raise MyException(
                item, "My exception was raise with the exception argunment : {}".format(item))


if __name__ == '__main__':
    main()
