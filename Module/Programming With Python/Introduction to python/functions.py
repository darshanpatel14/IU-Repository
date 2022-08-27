# python has
# 1. built in functions in interpreter ex.print
# 2. user defined functions
# 3. anonymous functions ex. lambda function

# user defined functions called by def keyword

# custom declarations of functions
def print_message(msg):
    print('The message is {}'.format(msg))


# return statement example
def addition_of_two_numbers(number_1, number_2):
    return number_1 + number_2


# default parameters example
def payment_day(working_hours, payment_hours=25):
    return working_hours * payment_hours


# some case we dont know about default param value
# so we need to pass None as default param value
def payments_day(working_hours, payment_hours=None):
    if payment_hours is not None:
        total_payment = working_hours * payment_hours
    else:
        total_payment = 0
    return total_payment


# variable numbers of params we dont know exactly param
# with * single asterisk we cans send number of list arguments
def sum_params(*params):
    total_sum = sum(params)
    return total_sum


# with the help of ** asterisk sign we can send dictrinory ky:val
def print_dictionary(**args):
    for key, value in args.items():
        print("The value of {}:{}".format(key, value))


def main():
    my_message = "Hello"
    number_1 = 100
    number_2 = 100
    result = addition_of_two_numbers(number_1, number_2)
    working_hours = 8
    total_payment = payment_day(working_hours)
    print("Total payment is {}".format(total_payment))
    print(result)
    print_message(my_message)
    sum_numbers = sum_params(1, 2, 3, 4, 5)
    print("Sum numbers are {}".format(sum_numbers))
    print_dictionary(value1=1, value2=2, value3=False)


if __name__ == '__main__':
    main()
