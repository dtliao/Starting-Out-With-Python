def allCost(l,i,g,o,t,m,totalAnnual):
    print('Loan payment is $ ',format(l, ',.2f'))
    print('Insurance expenses is $ ', format(i, ',.2f'))
    print('Gas expenses is $ ', format(g, ',.2f'))
    print('Oil expenses is $ ', format(o, ',.2f'))
    print('Tires expenses is $ ', format(t, ',.2f'))
    print('Maintenace expenses is $ ', format(m, ',.2f'))
    print('The Total annual cost is $ ', format(totalAnnual, ',.2f'))

l=float(input('Enter the loan payment:'))
i=float(input('Enter the insurance expenses:'))
g=float(input('Enter the gas expenses:'))
o=float(input('Enter the oil expenses:'))
t=float(input('Enter the tires expenses:'))
m=float(input('Enter the maintenance expenses:'))
totalAnnual=l+i+g+0+t+m
allCost(l,i,g,o,t,m,totalAnnual)

