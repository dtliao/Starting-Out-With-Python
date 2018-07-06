list=[]
total = 0
average = 0
for i in range(20):
    numbers=float(input('Enter a number in integer:'))
    list.append(numbers)
    total += numbers
average = total/20
highest = max(list)
lowest = min(list)

print('Total:', format(total, ',.2f'))
print ('Average:', format(average, ',.2f'))
print ('High:', high)
print ('Low:', low)



