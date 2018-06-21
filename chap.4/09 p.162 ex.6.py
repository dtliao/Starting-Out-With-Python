f=0
print('Celsius', '\t', 'Fahrenheit')
print('-----------------------')

for c in range(0,22):
    f=(9/5)*c+32
    print(c, '\t\t\t', format(f, ',.2f'))
