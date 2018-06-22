tuition=8000
rate=0.03

print('Year', '\t', 'Tuition total')
print('-----------------------')

for year in range(1,6):
    tuition+=(rate*tuition)
    print(year, '\t\t', '$', format(tuition, ',.2f', ), sep='')