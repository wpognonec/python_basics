import random
weather = random.choice(('sunny', 'rainy', 'thundering'))

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella.")
    case _:
        print("Let's stay inside.")
