# known as an function
# return statement is not required as it return always value

def main():
    #function_double = lambda x : x*2
    def function_double(x): return x*2
    x = 10
    print('The doubled value is {}'.format(function_double(x)))


if __name__ == '__main__':
    main()
