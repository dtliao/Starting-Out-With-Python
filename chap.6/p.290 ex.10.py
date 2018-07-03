num=int(input('Enter the number of players:'))
outfile = open('golf.txt', 'w')

for i in range(num):
    name = input('Enter the player\'s name:')
    score = int(input('Enter the player\'s score:'))

    outfile.write(name + '\n' )
    outfile.write(str(score) + '\n')

#outfile.close()

#infile = open('golf.txt', 'r')


#for line in infile:
    #print(line.rstrip())


#infile.close()
