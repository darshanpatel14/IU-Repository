# Python allows software engineers to create custom exception classes.
# This implementa- tion can be done by following the exception class
# hierarchy structure shown in the fol- lowing graphic.
# As you can see, the “BaseException” class is the root of all exception classes in Python.
# The exception is never raised on
# its own and should instead be inhe- rited by other,
# lesser exception classes that can be raised. The “Exception” class is the most commonly inherited exception type for creating a custom exception class.
# In general, all exception classes that are considered errors are subclasses of the Exception class (Beazley & Jones, 2013).
