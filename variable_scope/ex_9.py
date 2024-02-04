a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# This will print 7. Integers are immutable so b is being reassigned to a new integer object.
# There reference to a remains unchanged.