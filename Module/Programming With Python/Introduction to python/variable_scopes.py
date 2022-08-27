# two types of scopes
# 1. local variable ex. inside function variable
# 2. global variable ex. outside of function

x_global_var = 100


def calculate_double(x):
    global x_local_var
    x_local_var = x*2
    return x_local_var


def main():
    value = 10
    calculate_double(value)
    print("the value double in main is {}".format(x_global_var))
    print("the value X local in main is {}".format(x_local_var))


if __name__ == "__main__":
    main()
