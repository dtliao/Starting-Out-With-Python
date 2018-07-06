total = 0
average = 0
list=[]
for i in range(1, 4):
    rainfall = float(input('Enter the total rainfall for ' + str(i) + ' month:'))
    list.append(rainfall)
    total += rainfall

average = total/12
highest = max(list)
lowest = min(list)

print('The total rainfall for the year:', total)
print('The average monthly rainfall:', average)
print('The highest rainfall amount:', highest)
print('The lowest rainfall amount:', lowest)