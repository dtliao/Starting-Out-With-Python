def condition():
    if guess==answer:
        print('Congratulation!!! You are right')
    else:
        print('The answer is:', answer)


import random
a=random.randint(0,999)
b=random.randint(0,999)
print(' ', a,'\n', \
    '+',end='')
print(b)
guess=int(input('Enter your answer:'))
answer=a+b
condition()
