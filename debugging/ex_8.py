sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(list(sub_list)) # Need to make a shallow copy of list.

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]