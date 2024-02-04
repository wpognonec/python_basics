speed = 0
acceleration = 24
braking_force = 19

is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
#AND has higher precedence than OR, so parens are needed even though these specific values will have the same outcome.

print(is_moving)