import random
num = random.randint(1, 101)
count = 0
#cont =True
while True: #While cont:
    g = int(input('Guess a number in the range of 1 thorugh 100(0 to quit):'))
    count += 1
    if g == 0:
        print('Thanks for playing!')
        break #cont = False
    elif g > num:
        print('Too high, try again')
    elif g < num:
        print('Too low, try again')
    else:
        print('Congratulation!!!')
        print("You guessed ", count," times.")
        count = 0
        num = random.randint(1, 101)

