penny=0.01
total=0
days=0

days=int(input('Enter the number of days:'))

print('Day', '\t', 'Salary')
print('----------------')

for r in range(1, days+1):
    total+=penny
    print(r, '\t\t', penny)
    penny*=2

print('The Total Pay is: $', format(total, ',.2f'))
