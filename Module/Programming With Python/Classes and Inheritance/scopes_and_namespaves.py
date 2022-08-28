# name in python
# name is simple way to access any variable
# a variable is declared by a assigning name to it

# name to reference values

person_name = "Darshan"
person_age = 26
person_weight = 62
person_is_old = False


# Name to Function

def my_function():
    print("Hello function")


hello_function = my_function


# NameSpaces
# A namespace is a system used to make sure that all
# the names in a program are unique and can be used without any conflict.

# example:

namespace_example = {"name_1": "object_1"}

# following used of namespaces in python

# 1. Global namespaces — They are based on imported module definition(s) used in the program.
# The namespace is created for every module.
# It is available until the pro- gram ends.

# 2. Local namespaces — They are based on local names inside a function.
# The name- space is created or every function is called in a program.
# It is available until the function returns.

# 3. Built-in namespaces — They are based on built-in functions and built-in exception names.
# The namespace is created until the interpreter starts, it will then keep it until you exit.
# These are the outermost level of the Python language.


# Scopes
# 1. Local scope (innermost scope) — This defines all local names available in the cur- rent function.
# 2. Outermost scope — This defines the list of all built-in names in the whole program.
# 3. Module scope — This defines all global names from the current module.
# 4. Enclosing functions scope — This defines a name from the nearest enclosing scope
# and goes outwards.


# example

def scope_testing():

    def local_scope():
        spam = "Local spam defined"

    def nonlocal_scope():
        nonlocal spam
        spam = "nonlocal spam defined"

    def global_spam():
        global spam
        spam = "global spam defined"

    spam = "spam testing"
    local_scope()
    print('After local scope test', spam)
    nonlocal_scope()
    print('After non local scope test', spam)
    global_spam()
    print('After global spam test', spam)


def main():
    scope_testing()
    print('In global scope spam test', spam)


if __name__ == '__main__':
    main()
