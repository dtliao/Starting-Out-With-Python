import math
def main():
    feet_per_gallon=112
    hours=8
    labor=35
    sq_feet=float(input('Enter the square feet of wall space to be painted:'))
    price_per_gallon= float(input('Enter the price of the paint per gallon:'))


    gallon_paint=sq_feet/feet_per_gallon
    hour_labor=gallon_paint*hours
    paint_cost=price_per_gallon*gallon_paint
    labor_charge=hour_labor*labor
    cost(gallon_paint, hour_labor, paint_cost, labor_charge)
def cost(gallon_paint, hour_labor, paint_cost, labor_charge):
    total_cost= labor_charge+paint_cost
    print('Gallons Paint Required:', math.ceil(gallon_paint))
    print('Hours of labor:', hour_labor)
    print('Paint cost: $', format(paint_cost, ',.2f'), sep='')
    print('Labor charges: $', format(labor_charge, ',.2f'), sep='')
    print('Total cost: $', format(total_cost, ',.2f'), sep='')
main()


