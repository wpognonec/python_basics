def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
# number = input() # need to convert input to int
number = int(input())

print(f"The result is {multiply_by_five(number)}!")