pennies_n=int(input('Enter number of pennies:'))
nickles_n=int(input('Enter number of nickles:'))
dimes_n=int(input('Enter number of dimes:'))
quarters_n=int(input('Enter number of quarters:'))

pennies=pennies_n* 0.01
nickles=nickles_n* 0.05
dimes= dimes_n* 0.1
quarters=quarters_n*0.25

Total=(pennies+nickles+dimes+quarters)
if Total==1.00:
    print('CONGRATULATION YOU WON THE GAME!')
else:
    if Total>1.00:
        print('It is more than one dollar')
    else:
        print('It is less than one dollar')


