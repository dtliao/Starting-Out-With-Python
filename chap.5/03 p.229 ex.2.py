state_rate=0.05
county_rate=0.025

def main():
    amount=0
    state_tax=0
    county_tax=0
    amount=int(input('Enter the amount of purchase: '))
    state_tax = state_rate * amount
    county_tax = county_rate * amount
    sum(amount, state_tax, county_tax)

def sum(amount, state_tax, county_tax):
    total_sale_tax=0
    total_sale=0
    total_sale_tax=state_tax+county_tax
    total_sale=total_sale_tax+amount

    print('Purchase Amount $', format(amount, ',.2f'))
    print('State Tax $', format(state_tax, ',.2f'))
    print('County Tax $', format(county_tax, ',.2f'))
    print('Total Sale Tax $', format(total_sale_tax, ',.2f'))
    print('Total of the Sale $', format(total_sale, ',.2f'))
main()



