sum=0
number=1
while number>0:
    number = float(input('Enter a positive number(negative to quit):'))
    if number>0:
    sum+=number
print('Sum=', format(sum, ',.2f'))
