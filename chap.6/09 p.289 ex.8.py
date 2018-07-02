infile = open('Daniel.txt', 'r')
total=0
count =0
for content in infile:
    line = int(content.rstrip('\n'))
    total+=line
    count+=1
    print(line)

print('Total:', format(total, ','))
print(count, 'numbers were read from the file.')

infile.close()
