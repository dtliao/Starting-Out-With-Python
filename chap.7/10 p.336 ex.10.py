infile = open('WorldSeriesWinners.txt', 'r')

World_list = []
for line in infile:
    line = line.rstrip('\n')
    World_list.append(line)
infile.close()

team = input('Enter the name of the team:')
count = 0
for t in range (len(World_list)):
    if team == World_list[t]:
        count+=1
print(team, 'won the the World Series', count, 'times from 1903 through 2009.')
