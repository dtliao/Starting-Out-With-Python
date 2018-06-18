month=int(input('Enter a month in numeric form:'))
day=int(input('Enter a day:'))
year=int(input('Enter a year in two digit:'))
if month>12 or month<1:
    print('Error: invalid input')
elif day>31 or day<1:
    print('Error: Invalid input')
elif year>99 or year<0:
    print ('Error: invalid input')
else:
    print('The date is', month, "/", day, "/", year)
    if month* day== year:
        print('The date is magic')
    else:
        print('The date is not magic')