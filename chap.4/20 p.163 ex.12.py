Starting_organism=0
Average_daily_increase=0
Days=0

while Starting_organism<=0:
    Starting_organism= int(input('Starting number of organisms:'))
while Average_daily_increase<=0:
    Average_daily_increase=int(input('Average daily increase:'))
while Days<=0:
    Days= int(input('Number of days to multiply:'))

if Average_daily_increase>=1:
    Average_daily_increase/=100

print('Day Approximate', '\t', 'Population')
print('-------------------------------')

for i in range(Days):
    if i>0:
        Starting_organism+=(Starting_organism*Average_daily_increase)
    print(i+1, '\t\t\t', format(Starting_organism))
