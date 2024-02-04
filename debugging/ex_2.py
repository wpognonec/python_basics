import random

# Our predict_weather function should output a message indicating whether
# a sunny or cloudy day lies ahead. However, the output is the same every
# time the method is invoked. Why? Fix the code so that it behaves as expected.

def predict_weather():
    # sunshine = random.choice(['True', 'False'])
    # 'True' and 'False' both truthy since they are nonempty strings
    sunshine = random.choice([True, False])
    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()