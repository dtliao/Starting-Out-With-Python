sum=0
positive=1
while positive>0:
    positive=float(input('Enter a  positive numbers(negative to quit):'))
    if positive>0:
        sum+=positive
print('Sum is', format(sum, '.2f'))
