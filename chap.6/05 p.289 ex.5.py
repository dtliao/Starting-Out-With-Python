infile = open('numbers.txt', 'r')
total=0

line = infile.readline()
while line !='':
    line = line.rstrip()
    total+=int(line)
    print(int(line))
    line = infile.readline()


print('Total is:', total)
infile.close()

# Two ways using for or while
#I wrote on other sheet using for