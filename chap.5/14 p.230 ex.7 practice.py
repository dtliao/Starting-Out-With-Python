def income(IncomeA, IncomeB, IncomeC, total):
    print('Class A Income is $', format(IncomeA, ',.2f'))
    print('Class B Income is $', format(IncomeB, ',.2f'))
    print('Class C Income is $', format(IncomeC, ',.2f'))
    print('Total Income is $', format(total, ',.2f'))

a=20
b=15
c=10
seatsA=int(input('How many tickets for class A seats were sold?'))
seatsB=int(input('How many tickets for class B seats were sold?'))
seatsC=int(input('How many tickets for class C seats were sold?'))

IncomeA=a*seatsA
IncomeB=b*seatsB
IncomeC=c*seatsC
total=IncomeA+IncomeB+IncomeC
income(IncomeA, IncomeB, IncomeC, total)
