a = 1

def my_function():
    print(a)

my_function()

# a is not declared in my_function so it looks for a in the nearest scope.
# a is 1 in global scope so it will print 1