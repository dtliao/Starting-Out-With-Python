numbers = input('Enter a series of single-digit numbers:')


sum = 0
for i in range(len(numbers)):
   sum+=int(numbers[i])


print('The sum is:', sum)
