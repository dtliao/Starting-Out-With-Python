def display(gallonNeed, hour_labor, costPaint, laborCharge, totalCost):
    print('The number of gallons pf paint required:', gallonNeed)
    print('The hours of labor required:', hour_labor)
    print('The cost of the paint', format(costPaint, ',.2f'))
    print('The labor charges:', format(laborCharge, ',.2f'))
    print('The total cost of the paint job:',format(totalCost,',.2f'))
import math
sq_feet=112
H_labor=35

sqfeet_painted=float(input('Enter the square feet to be painted:'))
price_per_g=float(input('Enter the price of the paint per gallon:'))

gallonNeed=math.ceil(sqfeet_painted/112)
hour_labor=gallonNeed*8
costPaint=gallonNeed*price_per_g
laborCharge=hour_labor*H_labor
totalCost=costPaint+laborCharge
display(gallonNeed, hour_labor, costPaint, laborCharge, totalCost)


