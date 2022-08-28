# iterable objects

def main():

    programming_language = ['JavaScript', 'Java', 'Ruby', 'Python', 'C', 'C++']

    for item in programming_language:
        print(item)


if __name__ == '__main__':
    main()


# this program prints every item in list objects that
# python has several built in iterator objects that
# list,tuples,dictionaries,string and files
# itearator provides clean and well organized code

# iter()  function
# Python supports a built-in function “iter”.
# This function takes an iterable object and returns an iterator.

def main():
    number_list = [1, 2, 3, 4, 5]
    number_list_iter = iter(number_list)

    # print 1
    print(next(number_list_iter))

    # print 2
    print(next(number_list_iter))

    # print 3
    print(next(number_list_iter))

    # print 4
    print(next(number_list_iter))

    # print 5
    print(next(number_list_iter))

    # an error occurred - StopItearation
    # print(next(number_list_iter))


if __name__ == "__main__":
    main()


# if there is no more elements,the exception error "Stopiteration" occur
