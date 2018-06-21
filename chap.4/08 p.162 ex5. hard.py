years=int(input('Enter number of years:'))
year=0
total_months=0
total_rainfall=0
average_rainfall=0
month_rainfall=0

for years in range(years):
    print('For year', years+1, ':' )
    for month in range(12):
        month_rainfall=float(input('Enter the inches of rainfall for the month:'))

        total_months+=1
        total_rainfall+=month_rainfall
    average_rainfall= total_rainfall/total_months
    

print('The number of months is', total_months)
print('The total inches of rainfall is', total_rainfall)
print('The average rainfall per month is', format(average_rainfall, '.2f'))