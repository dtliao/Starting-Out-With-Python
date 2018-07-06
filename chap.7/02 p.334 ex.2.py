import random

list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(7):
    list[i] = random.randint(0, 9)
    print(list[i], end='')
    if i<6:
        print(', ', end='')