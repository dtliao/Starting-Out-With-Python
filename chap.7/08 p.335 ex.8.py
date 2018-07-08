Girl_file = open('GirlNames.txt', 'r')
Boy_file = open('BoyNames.txt', 'r')

G_list = []
B_list = []
for g in Girl_file:
    g = g.rstrip('\n')
    G_list.append(g)
for b in Boy_file:
    b = b.rstrip('\n')
    B_list.append(b)

Girl_file.close()
Boy_file.close()

boysName = input('Enter a boy\'s name(enter N if you do not wish to enter):')
girlsName = input('Enter a girl\'s name(enter N if you do not wish to enter):')

if boysName =='N':
    print('You choose not to enter a boy\'s name.')
elif boysName in B_list:
    print(boysName, 'is among the most popular name.')
else:
    print('Sorry, it is not one of the most popular name.')

if girlsName =='N':
    print('You choose not to enter a girl\'s name.')
elif girlsName in G_list:
    print(girlsName, 'is among the most popular name.')
else:
    print('Sorry, it is not one of the most popular name.')


