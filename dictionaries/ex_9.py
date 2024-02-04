numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

num_list = []

for num in numbers.values():
    num_list.append(num // 2)

print(num_list)