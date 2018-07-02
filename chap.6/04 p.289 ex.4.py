count = 0
infile = open('names.txt', 'r')

for contents in infile:
    count+=1

print('There are', count, 'names in the file')

infile.closed