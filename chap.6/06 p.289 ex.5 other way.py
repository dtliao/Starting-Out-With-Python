infile=open('numbers.txt', 'r')
total = 0

for content in infile:
    number = int(content)
    total+= number
    print(number)


print('Total is:', total)

infile.close