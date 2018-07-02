infile=open('numbers.txt', 'r')
total = 0
average=0
for content in infile:
    number = int(content)
    total+=number
    print(number)
average = format((total/number), '.2f')
print('The average is:',average)

infile.close