infile = open('USPopulation.txt', 'r')

list = []
for line in infile:
    line = line.rstrip('\n')
    list.append(line)
infile.close()

annual_change = 0
total_annual_change = 0
increase_list= []
base_year = 1950
for i in range(len(list)-1):
    annual_change = int(list[i+1])- int(list[i])
    increase_list.append(annual_change)
    total_annual_change+=annual_change

for j in range(len(increase_list)):
    if increase_list[j]==max(increase_list):
        greatest_increase = base_year + j + 1
# see blank 2 file for references
for r in range(len(increase_list)):
    if increase_list[r] == min(increase_list):
        smallest_increase = base_year + r + 1
average_annual_change = total_annual_change/len(increase_list)
# see blank 2 file for references

print('The average annual change:',average_annual_change )
print('The greatest increase:',greatest_increase )
print('The smallest increase:',smallest_increase )



