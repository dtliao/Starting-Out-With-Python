millimeters=1.6
Total_M=0
print('Year', '\t', 'Millimeters')
print('--------------------')
for year in range(26):
    Total_M+= millimeters
    print(year, '\t\t', format(Total_M, ',.2f'))