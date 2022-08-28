# A generator is an object that allows you to create iterators in an easy way.
# You do not need to use a customized class with methods __iter__() and __next__() to create a generator.
# A simple function without a return statement and the “yield” keyword can create a generator.


def sequence_number_generator(low, high):
    while low <= high:
        yield low
        low += 1


def main():
    number_list = []
    for number in sequence_number_generator(0, 5):
        number_list.append(number)
    print(number_list)


if __name__ == '__main__':
    main()
