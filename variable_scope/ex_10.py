b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# This will print [10, 2, 3]. The list b is global.
# b[0] = 10 is a mutating method, assigning the value 10 to the index 0 spot in the list.