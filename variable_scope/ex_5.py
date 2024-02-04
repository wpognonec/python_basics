a = 1

def my_function():
    print(a)
    a = 2

my_function()

# When a name is not found at all, a NameError exception is raised.
# If the current scope is a function scope, and the name refers to a
# local variable that has not yet been bound to a value at the point
# where the name is used, an UnboundLocalError exception is raised.
# UnboundLocalError is a subclass of NameError.