import random
weather = random.choice(('sunny', 'rainy', 'thundering'))

if weather == 'sunny':
    print("It's a beautiful day!")
elif weather == 'rainy':
    print("Grab your umbrella.")
else:
    print("Let's stay inside.")
