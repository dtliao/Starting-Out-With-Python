tuition=8000

print('Year', '\t', 'Tuition')

for year in range(1,6):
    tuition*=1.03
    print(year, '\t\t$', format(tuition, ',.2f'))