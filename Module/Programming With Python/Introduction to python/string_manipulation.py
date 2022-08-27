# String object are immutable
# String methods


def main():

    string_value = "darshan"
    print(string_value)
    print(string_value[5])

    # error occurs when trying to assign a string value
    # string_value[5] = 'b'
    # print(string_value)

    # len method
    check_length = "Python is the most popular programming language in the world"
    print(len(check_length))

    # concat using + signs
    concat_1 = "hi "
    concat_2 = "how r u"

    print(concat_1 + concat_2)

    # concat using join methods
    join_test = "Hi ".join(("Darshan ", "How r u?"))
    print(join_test)

    # substrings (or splices) using [start, start + length]
    str_1 = "python is the best programming language in the word"
    print(str_1[0:6])

    # remove python word from the str_1
    print(str_1[7:])

    # remove word from str_1
    print(str_1[:-5])

    # select best word only
    print(str_1[14: 19])

    # count how many times a letter occurs in string
    print(str_1.count('a'))

    # found what position best word starts from
    print(str_1.find('best'))

    # remove any whitespaces from start to end
    print(str_1.strip())

    # convert to lowercase
    print(str_1.lower())

    # convert to uppercase
    print(str_1.upper())

    # check best word is in string or not
    print('best' in str_1)

    # Replace 'python' word with java
    print(str_1.replace('python', 'java'))

    # split string into substrings in better word
    print(str_1.split('best'))

    # check if popular word is in string or not
    print('popular' not in str_1)


if __name__ == '__main__':
    main()
