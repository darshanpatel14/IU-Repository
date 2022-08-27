# function within a function
# nested function can access the value only as read only
# to change value we need have to use nonlocal keyword in nested function

def outer_function(x):
    def inner_function():
        nonlocal x
        x = 5
        print("The value inside the inner function is {}".format(x))
        x_local_var = x * 2
        print("The x local value inside the inner function is {}".format(x_local_var))

    inner_function()
    print("The value outside the inner function is {}".format(x))


def main():
    value = 10
    outer_function(value)


if __name__ == "__main__":
    main()
