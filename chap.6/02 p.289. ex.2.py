userName = input('Enter the name of the file:')
infile = open(userName, 'r')
line = infile.readline()
count = 1

while line !='' and count<= 5:
    line = line.rstrip('\n')
    print(line)
    line = infile.readline()
    count+=1

infile.close()

