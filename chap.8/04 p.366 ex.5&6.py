infile = open('text.txt', 'r')
total = 0
count = 0
for line in infile:
    word = line.split()
    total += len(word)
    count += 1
average = total/count
print(average)
infile.close()