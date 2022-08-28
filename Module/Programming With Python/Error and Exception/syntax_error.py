# In computer programming, three types of errors may occur:
# syntax errors,
# runtime errors,
# or logic errors.


# Example of syntax error

def main():
    print(1/1)
    # print(1/1)) -syntax error


if __name__ == '__main__':
    main()


# example of runtime error

def main():
    print(1/0) - ZeroDivisionError


if __name__ == '__main__':
    main()


# example of logic error

def main():
    a = "Python"
    if a == 'Python':
        print("a is equal to java")


if __name__ == '__main__':
    main()
