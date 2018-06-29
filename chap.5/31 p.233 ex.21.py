import random

def printChoice():
    print('MENU')
    print('1) Rock')
    print('2) Paper')
    print('3) Scissors ')
    choice=input('Enter your choice:')
    return choice

def compare(x, y):
    if x == 1:
        if y == 2:
            win = True
        elif y == 3:
            win = False
    elif x == 2:
        if y==3:
            win = True
        elif y==1:
            win = False
    elif x ==3:
        if y==1:
            win = True
        elif y==2:
            win = False
    return win

# win == True, 使用者 輸
# win == False, 使用者 贏
win = True
while win:
    x = printChoice()  # user的選擇
    y = random.randint(1,4)  # computer的選擇
    while x==y:
        print("Same guess, Guess again! ")
        x = printChoice()  # user的選擇
        y = random.randint(1,4)  # computer的選擇
    win = compare(x,y)
    if win:
        print("You lost")
    else:
        print("You win")