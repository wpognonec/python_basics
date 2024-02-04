destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(dest, cities):
    for city in cities:
        if city == dest:
            return True
    return False

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False