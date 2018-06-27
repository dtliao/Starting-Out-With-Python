
import random

def main():
    a= random.randint(0,999)
    b= random.randint(0,999)
    correct_answer=a+b
    display(a,b)
    answer=guess()
    show_result(correct_answer, answer)

def display(a,b):
    print('',a)
    print('+', end='')
    print(b)
def guess():
    answer=int(input('Enter sum of answer:'))
    return answer
def show_result(correct_answer,answer):
    if correct_answer==answer:
        print('Congratulation!!! you are right')
    else:
        print('Correct answer is: ', answer)



main()
display(1,2)