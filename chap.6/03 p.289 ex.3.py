count=0
name = input('Enter the name of the file:')
infile = open(name, 'r')
for line in infile:
    count+=1
    print(count, end='')
    print(':', end='')

    line = line.rstrip('\n')
    print(line)


infile.close