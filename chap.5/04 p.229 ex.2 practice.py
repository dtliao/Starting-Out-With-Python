def total(purchase, state_tax, county_tax, total_sale, sum):
    print('Amount of purchase is $', format(purchase, ',.2f'))
    print('State sales tax is $', format(state_tax, ',.2f'))
    print('County sales tax is $', format(county_tax, ',.2f'))
    print('Total sales tax is $', format(total_sale, ',.2f'))
    print('Total of the Sale is $', format(sum, ',.2f'))


purchase=int(input('Enter the amount of purchase:'))
sRate=0.05
cRate=0.025
state_tax=sRate*purchase
county_tax=cRate*purchase
total_sale=state_tax+county_tax
sum=purchase+total_sale
total(purchase, state_tax, county_tax, total_sale, sum)