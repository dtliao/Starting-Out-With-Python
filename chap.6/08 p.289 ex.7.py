import random
Name = input('Enter the name of the file:')
Numbers = int(input('Enter the number of random numbers:'))
outfile = open(Name, 'w')

for content in range(Numbers):
    random_num = random.randint(1, 501)
    outfile.write(str(random_num) + '\n')

outfile.close()



