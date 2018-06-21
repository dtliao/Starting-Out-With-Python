Total_pay=0
penny=0.01
days=int(input('Enter number of days:'))

print('Day', '\t', 'Pay')
print('---------------')

for i in range(1, days+1):
    Total_pay+=penny
    penny *=2
    print(i,'\t\t', '$', penny)
print('The total pay for', days, 'days is:',format(penny) )