starting=0
increase=0
days=0

while starting<=0:
    starting=int(input('Starting number of organism:'))
while increase<=0:
    increase= int(input('Average daily increase:'))
while days<=0:
    days=int(input('Number of days to multiply:'))

print('Day Approximate', '\t', 'Population')
print('-----------------------------')

for i in range(days):
    if i>0:
        starting+=(starting*(increase/100))
    print(i+1, '\t\t\t', format(starting, ',.2f'))