def getLargerInput():
    num1=int(input('Enter the first number:'))
    num2=int(input('Enter the second number'))
    return(num1, num2)


(num1,num2)=getLargerInput()
print(max(num1,num2))